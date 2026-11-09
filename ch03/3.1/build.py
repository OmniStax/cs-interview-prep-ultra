#!/usr/bin/env python3
"""Assemble 3.1's source.md, text.html, footnotes.json and captions.json from its spec, by script.

The page joins two sources block by block: Wikipedia's "Stack (abstract data type)" (wikitext) and cp-algorithms'
"Balanced bracket sequences" (Markdown). No shared assembler joins those two, so this one calls the readers the book
already has and types none of either source:

- **Wikipedia**: `tools/wikitext.py`, the book's one Wikipedia reader (slices, elements, citations as book notes
  numbered in page order, the article's "nb" notes, frames by the spec's IMAGES); the one citation template the
  passage cites that is not a `cite …` one, `{{Introduction to Algorithms|3|pages=…}}`, is set from the spec's
  CITE_TEMPLATES (what the template prints on Wikipedia).
- **cp-algorithms**: `tools/build_translation.py`'s Markdown parser and inline setter (imported, unchanged, as
  `tools/build_markdown.py` uses them), each block a slice of the page from one heading to another, cut before the
  paragraph that starts with the spec's `stop_at`.

Then the spec's figures are placed (`AT`: after the element holding an anchor), its replacement table (`FIXES`, each
entry with its reason) and its marks (`MARKS`) are applied outside tags, and tools/apply_terms.py applies the section's
judged concept mentions.

    python3 -I ch03/3.1/build.py
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
import build_markdown as BM  # noqa: E402  the shared cp-algorithms slicing
import build_translation as BT  # noqa: E402  the shared Markdown parser and inline setter
import wikitext as WT  # noqa: E402  tools/wikitext.py, the book's one Wikipedia reader


def load_spec():
    sp = importlib.util.spec_from_file_location('build_spec_31', os.path.join(HERE, 'build_spec.py'))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


# ---------------------------------------------------------------- cp-algorithms

def md_block(b, spec):
    page = open(os.path.join(BOOK, b['file']), encoding='utf-8').read().split('\n')
    page = page[BM.front_matter_end(page):]
    src = BM.slice_block(page, b)
    lines, _ = BM.prepare(src, {})     # headings one level deeper, as tools/build_markdown.py reads them
    parts, top = [], None
    for e in BT.parse(lines):
        if e['kind'] == 'heading':
            if top is None:
                top = e['level']
                parts.append(f'<h2>{BT.inline(b.get("h2") or e["text"], {})}</h2>')
            else:
                lv = min(6, 2 + e['level'] - top)
                parts.append(f'<h{lv}>{BT.inline(e["text"], {})}</h{lv}>')
            continue
        if e['kind'] == 'code':
            raise SystemExit(f'{b["id"]}: a fenced block, which this block is not meant to hold')
        parts.append(('MD', BT.el_html(e, {}, [], set()), BT.el_text(e)))
    return '\n'.join(src), parts


# ---------------------------------------------------------------- assembly

def build():
    mod = load_spec()
    spec = {k: getattr(mod, k) for k in dir(mod) if k.isupper()}
    notes, log, state = WT.Notes(), [], {}
    md_blocks, html_blocks = [], []
    used_fix, placed = set(), set()
    for b in spec['BLOCKS']:
        head = f'<!-- block {b["id"]} · source {b["source"]} · {b["locator"]} -->'
        after = [a for a in spec.get('AT', []) if a[0] == b['id']]
        out = []

        def place(anchor_text):
            for j, (_, anchor, key) in enumerate(after):
                if (b['id'], j) not in placed and anchor in anchor_text:
                    out.append(spec['HTML'][key])
                    placed.add((b['id'], j))
        if b['source'] == 'wikipedia':
            md, parts = WT.block(b, spec, notes, log, state=state)
            out.extend(parts)
            mine = [j for j, r in enumerate(spec.get('AT', [])) if r[0] == b['id']]
            placed.update((b['id'], k) for k, j in enumerate(mine) if j in state['placed'])
        else:
            md, parts = md_block(b, spec)
            for p in parts:
                if isinstance(p, str):
                    out.append(p)
                    continue
                out.append(p[1])
                place(p[2])
        for j, a in enumerate(after):
            if (b['id'], j) not in placed:
                raise SystemExit(f'{b["id"]}: AT never placed: {a!r}')
        body = '\n'.join(out)
        for i, (blk, old, new, why) in enumerate(spec.get('FIXES', [])):
            if blk != b['id']:
                continue
            if old not in body:
                raise SystemExit(f'FIX not found in {blk}: {old!r} ({why})')
            body = body.replace(old, new, 1)
            used_fix.add(i)
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
        html_blocks.append(f'<section {attrs}>\n{body}\n</section>')
        md_blocks.append(head + '\n\n' + md)

    page = '\n\n'.join(html_blocks) + '\n'
    captions, fn_rows = state.get('captions', {}), notes.rows
    page = re.sub(r'\{\{caption-text ([^}]+)\}\}', lambda m: html.escape(captions[m.group(1)]['text'], quote=True), page)
    page = re.sub(r'\{\{caption ([^}]+)\}\}', lambda m: captions[m.group(1)]['html'], page)
    # a caption that ends in its own full stop takes no second one where the spec joins two
    page = re.sub(r'(data-original-caption="[^"]*)', lambda m: m.group(1).replace('.. ', '. '), page)
    if '\x01' in page or '\x02' in page:
        raise SystemExit('a note marker was left unset')
    open(os.path.join(HERE, 'source.md'), 'w', encoding='utf-8').write(f'# {spec["TITLE"]}\n\n' + '\n\n'.join(md_blocks) + '\n')
    with open(os.path.join(HERE, 'text.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    import apply_terms  # the judged concept mentions, after the page is written
    apply_terms.apply(HERE)
    json.dump([{k: v for k, v in r.items()} for r in fn_rows], open(os.path.join(HERE, 'footnotes.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    json.dump(captions, open(os.path.join(HERE, 'captions.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    unused = [f for i, f in enumerate(spec.get('FIXES', [])) if i not in used_fix]
    if unused:
        raise SystemExit(f'FIXES never applied: {unused}')
    if log:
        print('templates left out:', sorted(set(log)), file=sys.stderr)
    print(f'{HERE}: {len(html_blocks)} blocks, {len(fn_rows)} notes', file=sys.stderr)


if __name__ == '__main__':
    build()
