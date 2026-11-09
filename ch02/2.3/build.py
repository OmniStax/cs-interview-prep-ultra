#!/usr/bin/env python3
"""Assemble 2.3's source.md, text.html, footnotes.json and captions.json from its spec, by script.

The page joins two sources block by block, which neither shared assembler does (tools/build_translation.py
builds a page of OI Wiki blocks, tools/build_text.py one of ODS, Erickson, OpenDSA and LaTeX blocks), so this
assembler calls the shared translation tool's own parser, parity check and HTML writer for the OI Wiki blocks
and `tools/wikitext.py`, the book's one Wikipedia reader, for the Wikipedia blocks. Nothing of either source is typed:

- **OI Wiki** (translated): each block is a slice of the page from one heading to another, cut by script and
  written to source.md verbatim. An admonition box (`???+ note …` and its indented lines) that restates a
  LeetCode problem is link-only (RULES.md, Source): it is read as one slot on both halves, `[[<key>]]`, so the
  parity check passes over it and the spec's HTML stands in its place. The English is translation.md.
- **Wikipedia**: each block is the article's lead or a section, cut at the spec's anchors, read by
  `tools/wikitext.py`; its wikitext slice is written to source.md verbatim; its references become book footnotes in
  Wikipedia's words, numbered in the order their markers stand on the page.

Then the spec's figures and derivations are placed (`AT`: after the element holding an anchor; `REPLACE`: a
display a derivation replaces), its replacement table (`FIXES`, each entry with its reason) and its marks
(`MARKS`: concept spans, referent spans, maths marked with \\htmlData) are applied outside tags, and
tools/apply_terms.py applies the section's judged concept mentions.

    python3 -I ch02/2.3/build.py            # writes source.md, text.html, footnotes.json, captions.json
    python3 -I ch02/2.3/build.py --check    # also prints the translated blocks' parity tables
"""
import html
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(BOOK, 'tools'))
import build_translation as BT  # noqa: E402  the shared OI Wiki parser, parity check and HTML writer
import wikitext as WT  # noqa: E402  tools/wikitext.py, the book's one Wikipedia reader


def load_spec():
    sp = importlib.util.spec_from_file_location('build_spec_23', os.path.join(HERE, 'build_spec.py'))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


# ---------------------------------------------------------------- OI Wiki

def oi_slice(lines, b):
    """From the heading `from` to the first heading `to` after it (a heading text recurs on OI Wiki's pages)."""
    a = next((i for i, l in enumerate(lines) if l.strip() == b['from']), None)
    if a is None:
        raise SystemExit(f'{b["id"]}: heading {b["from"]!r} is not on the page')
    z = next((i for i in range(a + 1, len(lines)) if lines[i].strip() == b['to']), None) if b.get('to') else len(lines)
    if z is None:
        raise SystemExit(f'{b["id"]}: no heading {b["to"]!r} after {b["from"]!r}')
    out = lines[a:z]
    while out and not out[-1].strip():
        out.pop()
    return out


def boxes_as_slots(lines, keys):
    """Each `???+ note` box, with its indented lines, as one `[[key]]` line, the keys taken in order."""
    out, i, k = [], 0, 0
    while i < len(lines):
        if lines[i].startswith('???'):
            if k >= len(keys):
                raise SystemExit(f'a box on the page has no slot key: {lines[i]!r}')
            out.append(f'[[{keys[k]}]]')
            k += 1
            i += 1
            while i < len(lines) and (lines[i].startswith('    ') or (not lines[i].strip() and i + 1 < len(lines) and lines[i + 1].startswith('    '))):
                i += 1
            continue
        out.append(lines[i])
        i += 1
    if k != len(keys):
        raise SystemExit(f'{len(keys)} slot keys for {k} boxes')
    return out


def oi_block(b, spec, page, trans, check):
    zh_lines = oi_slice(page, b)
    md = '\n'.join(zh_lines)
    zh = BT.parse(boxes_as_slots(zh_lines, b.get('boxes', [])))
    if b['id'] not in trans:
        raise SystemExit(f'{b["id"]}: translation.md has no block of this id')
    en = BT.parse(trans[b['id']])
    BT.parity(b['id'], zh, en, b.get('drop_headings', []), check)
    first = next(e['level'] for e in en if e['kind'] == 'heading')
    parts, placed = [], set()
    after = [a for a in spec.get('AT', []) if a[0] == b['id']]
    seen_first = False
    for e in en:
        t = BT.el_text(e)
        if e['kind'] == 'heading':
            if not seen_first:
                parts.append(f'<h2>{BT.inline(b.get("h2") or e["text"], {})}</h2>')
                seen_first = True
            else:
                lvl = min(4, 2 + e['level'] - first)
                parts.append(f'<h{lvl}>{BT.inline(e["text"], {})}</h{lvl}>')
            continue
        if e['kind'] == 'slot':
            parts.append(spec['HTML'][e['key']])
            placed.add(e['key'])
            continue
        parts.append(BT.el_html(e, {}, [], set()))
        for _, anchor, key in after:
            if anchor in t:
                parts.append(spec['HTML'][key])
                placed.add(key)
    want = {a[2] for a in after} | set(b.get('boxes', []))
    if want - placed:
        raise SystemExit(f'{b["id"]}: never placed {sorted(want - placed)}')
    return md, '\n'.join(p for p in parts if p), []


# ---------------------------------------------------------------- Wikipedia

def math_refs(body, table):
    """Inside each $…$ of the block, a referent's letter (or a \\mathit{name}) wrapped in \\htmlData{ref=…}, as 1.3
    marks its referents in maths; a letter that is part of a command or of a longer name is left alone."""
    def one(m):
        tex = m.group(1)
        for sym, rid in table.items():
            wrap = lambda _m, sym=sym, rid=rid: '\\htmlData{ref=' + rid + '}{' + sym + '}'
            if sym.startswith('\\'):
                tex = re.sub(re.escape(sym), wrap, tex)
            else:
                tex = re.sub(r'(?<![A-Za-z\\])' + re.escape(sym) + r'(?![A-Za-z])', wrap, tex)
        return '$' + tex + '$'
    return re.sub(r'(?<![\\$])\$([^$]+?)\$', one, body)


def build(check=False):
    mod = load_spec()
    spec = {k: getattr(mod, k) for k in dir(mod) if k.isupper()}
    oi_page = BT.page_lines(os.path.join(BOOK, spec['OIWIKI_FILE']))
    trans = BT.read_translation(os.path.join(HERE, 'translation.md'))
    notes, log, state = WT.Notes(), [], {}
    md_blocks, html_blocks, used = [], [], set()
    for b in spec['BLOCKS']:
        head = f'<!-- block {b["id"]} · source {b["source"]} · {b["locator"]} -->'
        if b['source'] == 'oiwiki':
            md, body, _ = oi_block(b, spec, oi_page, trans, check)
        else:
            md, parts = WT.block(b, spec, notes, log, state=state)
            body = '\n'.join(parts)
        md_blocks.append(head + '\n\n' + md)
        for blk, old, new, why in spec.get('FIXES', []):
            if blk != b['id']:
                continue
            if old not in body:
                raise SystemExit(f'FIX not found in {blk}: {old!r} ({why})')
            body = body.replace(old, new, 1)
            used.add((blk, old))
        for blk, table in spec.get('MATH_REFS', []):
            if blk != b['id']:
                continue
            body = math_refs(body, table)
        for blk, old, new, *cnt in spec.get('MARKS', []):
            if blk != b['id']:
                continue
            if '<' in old:
                k = min(body.count(old), cnt[0] if cnt else 1)
                body = body.replace(old, new, k)
            else:
                body, k = BT.outside_tags(body, old, new, cnt[0] if cnt else 1)
            if k == 0:
                raise SystemExit(f'MARK NOT FOUND {b["id"]}: {old!r}')
        attrs = f'id="{b["id"]}" data-source="{b["source"]}" data-locator="{html.escape(b["locator"], quote=True)}"'
        if b['source'] == 'oiwiki':
            attrs += f' data-ai="{spec["AI"]}"'
        html_blocks.append(f'<section {attrs}>\n{body}\n</section>')
    for m in WT.unplaced(spec, state):
        raise SystemExit(m)
    fn_rows = notes.rows
    md = f'# {spec["TITLE"]}\n\n' + '\n\n'.join(md_blocks) + '\n'
    open(os.path.join(HERE, 'source.md'), 'w', encoding='utf-8').write(md)
    with open(os.path.join(HERE, 'text.html'), 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(html_blocks) + '\n')
    import apply_terms  # the judged concept mentions, after the page is written
    apply_terms.apply(HERE)
    json.dump([{k: v for k, v in r.items()} for r in fn_rows], open(os.path.join(HERE, 'footnotes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump({}, open(os.path.join(HERE, 'captions.json'), 'w', encoding='utf-8'))
    print(f'{HERE}: {len(html_blocks)} blocks, {len(fn_rows)} footnotes', file=sys.stderr)


if __name__ == '__main__':
    build('--check' in sys.argv)
