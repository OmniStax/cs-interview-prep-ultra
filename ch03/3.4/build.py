#!/usr/bin/env python3
"""Assemble 3.4's source.md, text.html, footnotes.json and captions.json from its spec, by script.

The page joins two cp-algorithms articles and a Wikipedia article block by block, which neither shared
assembler does (tools/build_markdown.py reads one Markdown page, tools/build_wikitext.py one Wikipedia
article, and neither the other's blocks), so this assembler calls their readers, imported unchanged:

- **cp-algorithms**: each block is a slice of its article from one heading line to another, cut by
  tools/build_markdown.py's own `front_matter_end`, `slice_block` and `prepare`, and set with
  tools/build_translation.py's parser and inline setter, as 2.7's page is. Beyond 2.7's page, these
  articles print `*` bullets (each operation's label before its snippet), read as the parser's `-` items.
  A fenced snippet is what the spec's CODE says: a Sim's panel carries it (left out here; the Sim stands
  where AT puts it), or a four-language code set whose C++ variant is the snippet verbatim and whose other
  variants are the spec's, AI-marked.
- **Wikipedia**: the article's lead and sections, read by tools/wikitext.py, the book's one Wikipedia reader
  (`{{harvtxt}}`, `{{sfnp}}`, `{{citation}}` in CS2, `<code>`, `<sup>` and `:` lines are its readings); the
  citations are book footnotes in Wikipedia's words, numbered as their markers stand on the page.

Then the spec's MARKS (concept spans, referent spans, erratum markers, links) are applied outside tags, and
tools/apply_terms.py applies the section's judged concept mentions.

    python3 -I ch03/3.4/build.py
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
import build_markdown as BM  # noqa: E402  front_matter_end, slice_block, prepare (used as they are)
import build_translation as BT  # noqa: E402  parse, inline, el_html, el_text, outside_tags (used as they are)
import wikitext as WT  # noqa: E402  tools/wikitext.py, the book's one Wikipedia reader


def load_spec():
    sp = importlib.util.spec_from_file_location('build_spec_34', os.path.join(HERE, 'build_spec.py'))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def esc(s):
    return html.escape(s, quote=False)


# ---------------------------------------------------------------- code sets

def code_set(cpp, variants, ai):
    pres = []
    for lang in ('python', 'java', 'cpp', 'javascript'):
        code = cpp if lang == 'cpp' else variants[lang]
        mark = '' if lang == 'cpp' else f' data-ai="{ai}"'
        body = esc('\n'.join(l.rstrip() for l in code.strip('\n').split('\n'))).replace('$', '&#36;')
        pres.append(f'<pre data-lang="{lang}"{mark}><code>{body}</code></pre>')
    return '<div class="code-set">\n' + '\n'.join(pres) + '\n</div>'


# ---------------------------------------------------------------- cp-algorithms

def cpa_block(b, spec, pages, used_code):
    path = os.path.join(BOOK, b['file'])
    if path not in pages:
        lines = open(path, encoding='utf-8').read().split('\n')
        pages[path] = lines[BM.front_matter_end(lines):]
    src = BM.slice_block(pages[path], b)
    md = '\n'.join(src)
    lines, _ = BM.prepare(src, {})
    lines = [re.sub(r'^(\s*)\* ', r'\1- ', l) for l in lines]   # cpa's `*` bullets, read as the parser's items
    els = BT.parse(lines)
    drop = [d for blk, d in spec.get('DROP', []) if blk == b['id']]
    after = [a for a in spec.get('AT', []) if a[0] == b['id']]
    parts, placed, dropped, top = [], set(), set(), None
    for e in els:
        t = e['text'] if e['kind'] == 'code' else BT.el_text(e)
        if e['kind'] == 'heading':
            if top is None:
                top = e['level']
                parts.append(f'<h2>{BT.inline(b.get("h2") or e["text"], {})}</h2>')
            else:
                lv = min(6, 2 + e['level'] - top)
                parts.append(f'<h{lv}>{BT.inline(e["text"], {})}</h{lv}>')
            continue
        if e['kind'] == 'code':
            hit = next((i for i, c in enumerate(spec['CODE']) if c[0] == b['id'] and c[1] in e['text']), None)
            if hit is None:
                raise SystemExit(f'{b["id"]}: a fenced block is not in CODE: {e["text"][:60]!r}')
            used_code.add(hit)
            what = spec['CODE'][hit][2]
            if isinstance(what, dict):
                parts.append(code_set(e['text'], what, spec['AI']))
            elif what is None:
                parts.append('<pre>' + esc(e['text']).replace('$', '&#36;') + '</pre>')
            # else: a Sim's panel carries the snippet; the Sim stands where AT puts it
            continue
        if e['kind'] == 'list' and drop:
            h = BT.el_html(e, {}, drop, dropped)
        elif e['kind'] != 'list' and any(d in t for d in drop):
            dropped.add(next(d for d in drop if d in t))
            continue
        else:
            h = BT.el_html(e, {}, [], set())
        if h:
            parts.append(h)
        for blk, anchor, key in after:
            if anchor in t and key not in placed:
                parts.append(spec['HTML'][key])
                placed.add(key)
    for d in drop:
        if d not in dropped:
            raise SystemExit(f'{b["id"]}: DROP {d!r} matched nothing')
    want = {a[2] for a in after}
    if want - placed:
        raise SystemExit(f'{b["id"]}: never placed {sorted(want - placed)}')
    return md, '\n'.join(parts), []


# ---------------------------------------------------------------- the page

def build():
    mod = load_spec()
    spec = {k: getattr(mod, k) for k in dir(mod) if k.isupper()}
    pages, used_code = {}, set()
    notes, log, state = WT.Notes(), [], {}
    md_blocks, html_blocks = [], []
    for b in spec['BLOCKS']:
        head = f'<!-- block {b["id"]} · source {b["source"]} · {b["locator"]} -->'
        if b['source'] == 'cpa':
            md, body, _ = cpa_block(b, spec, pages, used_code)
        else:
            md, parts = WT.block(b, spec, notes, log, state=state)
            body = '\n'.join(parts)
        md_blocks.append(head + '\n\n' + md)
        figs = []   # the marks are the prose's: a figure's caption carries its own spans
        body = re.sub(r'<figure\b.*?</figure>', lambda m: figs.append(m.group(0)) or f'\x06{len(figs) - 1}\x06', body, flags=re.S)
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
        body = re.sub(r'\x06(\d+)\x06', lambda m: figs[int(m.group(1))], body)
        attrs = f'id="{b["id"]}" data-source="{b["source"]}" data-locator="{html.escape(b["locator"], quote=True)}"'
        html_blocks.append(f'<section {attrs}>\n{body}\n</section>')
    fn_rows = notes.rows
    for m in WT.unplaced(spec, state):
        if not m.startswith('CODE'):
            raise SystemExit(m)
    unused = [c[:2] for i, c in enumerate(spec['CODE']) if i not in used_code]
    if unused:
        raise SystemExit(f'CODE entries matched no fenced block: {unused}')
    md = f'# {spec["TITLE"]}\n\n' + '\n\n'.join(md_blocks) + '\n'
    open(os.path.join(HERE, 'source.md'), 'w', encoding='utf-8').write(md)
    with open(os.path.join(HERE, 'text.html'), 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(html_blocks) + '\n')
    import apply_terms  # the judged concept mentions, after the page is written
    apply_terms.apply(HERE)
    json.dump(fn_rows, open(os.path.join(HERE, 'footnotes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump({}, open(os.path.join(HERE, 'captions.json'), 'w', encoding='utf-8'))
    print(f'{HERE}: {len(html_blocks)} blocks, {len(fn_rows)} footnotes', file=sys.stderr)


if __name__ == '__main__':
    build()
