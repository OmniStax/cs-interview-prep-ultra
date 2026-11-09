#!/usr/bin/env python3
"""Assemble a section's source.md and text.html from an English Markdown source (cp-algorithms first), by script.

cp-algorithms (`cpa`) and the other Markdown sources in English (the System Design Primer, CIU) need no
translation, so tools/build_translation.py, which pairs OI Wiki's Chinese with a translation, does not fit
them, and tools/build_text.py reads only Erickson, ODS and OpenDSA. This reads the page itself:

- **The source**: each block of the spec is a slice of the page's Markdown, from one heading line
  (inclusive) to another (exclusive), cut here and written to `source.md` verbatim under its marker line.
  A heading the page prints twice is named with `from_nth` / `to_nth` (1-based). Nothing is typed.
- **The page**: the slice is set with tools/build_translation.py's own Markdown parser and inline setter
  (imported, unchanged), plus what an English page prints beyond OI Wiki's subset: a level-1 heading,
  a centred `<div><img></div>` (the spec's IMAGES name the figure that stands there, or None to leave it
  out; the image's alt text is its caption, written to captions.json under the file's name), and a fenced
  block (CODE names, by a piece of its text, the figure that stands in its place, or None for a `<pre>`).
  The block's first heading becomes its `<h2>` (the spec's h2 where the source's does not fit the page);
  deeper headings keep their depth below it. REPLACE swaps a run of elements for a derivation, DROP
  leaves an element out (a line a derivation now carries), AT places a figure after an element, and
  MARKS sets the spans, as in build_translation.py.

    python3 -I tools/build_markdown.py ch02/2.7
"""
import html
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build_translation as bt  # noqa: E402  (parse, inline, el_html, el_text, outside_tags: used as they are)


def heading_at(lines, text, nth=1):
    seen = 0
    for i, l in enumerate(lines):
        if l.strip() == text:
            seen += 1
            if seen == nth:
                return i
    raise SystemExit(f'heading {text!r} (occurrence {nth}) is not on the page')


def front_matter_end(lines):
    """The first line after a `---` … `---` front matter, else 0."""
    if lines and lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                return i + 1
    return 0


def slice_block(lines, b):
    a = heading_at(lines, b['from'], b.get('from_nth', 1))
    z = heading_at(lines, b['to'], b.get('to_nth', 1)) if b.get('to') else len(lines)
    if z <= a:
        raise SystemExit(f'{b["id"]}: {b["to"]!r} does not come after {b["from"]!r}')
    out = lines[a:z]
    while out and not out[-1].strip():
        out.pop()
    return out


IMG = re.compile(r'<img\s+[^>]*src="([^"]+)"[^>]*?(?:alt="(.*?)"\s*)?/?>', re.S)


def prepare(lines, images):
    """The slice as build_translation.parse reads it: headings one level deeper (so a level-1 heading is
    read), each centred image a `[[imgN]]` slot line. Returns the lines and the images in order."""
    out, found, i = [], [], 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith('<div'):
            j = i
            while j < len(lines) and '</div>' not in lines[j]:
                j += 1
            chunk = '\n'.join(lines[i:j + 1])
            m = IMG.search(chunk)
            if m:
                name = os.path.basename(m.group(1))
                alt = re.search(r'alt="+([^"]*)"+', chunk)
                found.append({'file': name, 'alt': alt.group(1).strip() if alt else ''})
                out.append(f'[[img{len(found) - 1}]]')
                i = j + 1
                continue
        if re.match(r'^#{1,5}\s', s):
            out.append('#' + s)
        else:
            out.append(lines[i])
        i += 1
    for f in found:
        if f['file'] not in images:
            raise SystemExit(f'image {f["file"]} is on the page but not in IMAGES (a figure key, or None to leave it out)')
    return out, found


def build(sec_dir):
    sp = importlib.util.spec_from_file_location('build_spec', os.path.join(sec_dir, 'build_spec.py'))
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    spec = {k: getattr(mod, k) for k in dir(mod) if k.isupper()}

    page = open(os.path.join(BOOK, spec['MD_FILE']), encoding='utf-8').read().split('\n')
    page = page[front_matter_end(page):]
    images = spec.get('IMAGES', {})
    code = spec.get('CODE', [])
    captions = {}
    md_blocks, html_blocks = [], []
    used_code, placed_all = set(), set()

    for b in spec['BLOCKS']:
        src = slice_block(page, b)
        head = f'<!-- block {b["id"]} · source {b["source"]} · {b["locator"]} -->'
        md_blocks.append(head + '\n\n' + '\n'.join(src))
        lines, imgs = prepare(src, images)
        els = bt.parse(lines)

        replace = [r for r in spec.get('REPLACE', []) if r[0] == b['id']]
        drop = [d for blk, d in spec.get('DROP', []) if blk == b['id']]
        after = [a for a in spec.get('AT', []) if a[0] == b['id']]
        dropped, placed = set(), set()
        parts, skipping, top = [], None, None
        for e in els:
            t = bt.el_text(e)
            if e['kind'] == 'code':
                t = e['text']
            if skipping is not None:
                if skipping[2] in t:
                    parts.append(spec['HTML'][skipping[3]])
                    placed.add(skipping[3])
                    skipping = None
                continue
            r = next((r for r in replace if r[1] in t), None)
            if r is not None:
                if r[2] in t:
                    parts.append(spec['HTML'][r[3]])
                    placed.add(r[3])
                else:
                    skipping = r
                continue
            if e['kind'] != 'list' and any(d in t for d in drop):
                dropped.add(next(d for d in drop if d in t))
                continue
            if e['kind'] == 'heading':
                if top is None:
                    top = e['level']
                    parts.append(f'<h2>{bt.inline(b.get("h2") or e["text"], {})}</h2>')
                else:
                    lv = min(6, 2 + e['level'] - top)
                    parts.append(f'<h{lv}>{bt.inline(e["text"], {})}</h{lv}>')
                continue
            if e['kind'] == 'slot':
                f = imgs[int(e['key'][3:])]
                captions[f['file']] = {'html': html.escape(f['alt'], quote=False), 'text': f['alt']}
                key = images[f['file']]
                if key:
                    parts.append(spec['HTML'][key])
                    placed.add(key)
                continue
            if e['kind'] == 'code':
                c = next((c for c in code if c[0] == b['id'] and c[1] in e['text']), None)
                if c is None:
                    raise SystemExit(f'{b["id"]}: a fenced block is not in CODE: {e["text"][:60]!r}')
                used_code.add(c)
                if c[2]:
                    if c[2] not in placed:
                        parts.append(spec['HTML'][c[2]])
                        placed.add(c[2])
                else:
                    parts.append('<pre>' + html.escape(e['text'], quote=False).replace('$', '&#36;') + '</pre>')
                continue
            parts.append(bt.el_html(e, {}, drop, dropped))
            for blk, anchor, key in after:
                if anchor in t:
                    parts.append(spec['HTML'][key])
                    placed.add(key)
        if skipping is not None:
            raise SystemExit(f'{b["id"]}: REPLACE {skipping[1]!r} … {skipping[2]!r} never closed')
        for d in drop:
            if d not in dropped:
                raise SystemExit(f'{b["id"]}: DROP {d!r} matched nothing')
        want = {r[3] for r in replace} | {a[2] for a in after}
        if want - placed:
            raise SystemExit(f'{b["id"]}: never placed {sorted(want - placed)}')
        placed_all |= placed
        body = '\n'.join(p for p in parts if p)
        for blk, old, new, *cnt in spec.get('MARKS', []):
            if blk != b['id']:
                continue
            if '<' in old:
                k = min(body.count(old), cnt[0] if cnt else 1)
                body = body.replace(old, new, k)
            else:
                body, k = bt.outside_tags(body, old, new, cnt[0] if cnt else 1)
            if k == 0:
                print(f'MARK NOT FOUND {b["id"]}: {old!r}', file=sys.stderr)
        attrs = f'id="{b["id"]}" data-source="{b["source"]}" data-locator="{html.escape(b["locator"], quote=True)}"'
        html_blocks.append(f'<section {attrs}>\n{body}\n</section>')

    unused = [c for c in code if c not in used_code]
    if unused:
        raise SystemExit(f'CODE entries matched no fenced block: {unused}')
    # a figure's original caption is the image's alt text, as the page prints it ({{caption-text <file>}})
    page_html = '\n\n'.join(html_blocks) + '\n'
    page_html = re.sub(r'\{\{caption-text ([\w.:-]+)\}\}', lambda m: html.escape(captions[m.group(1)]['text'], quote=True), page_html)
    md = f'# {spec["TITLE"]}\n\n' + '\n\n'.join(md_blocks) + '\n'
    open(os.path.join(sec_dir, 'source.md'), 'w', encoding='utf-8').write(md)
    with open(os.path.join(sec_dir, 'text.html'), 'w', encoding='utf-8') as f:
        f.write(page_html)
    import apply_terms  # the judged concept mentions, after the page is written (tools/apply_terms.py)
    apply_terms.apply(sec_dir)
    json.dump([], open(os.path.join(sec_dir, 'footnotes.json'), 'w', encoding='utf-8'))
    json.dump(captions, open(os.path.join(sec_dir, 'captions.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{sec_dir}: {len(html_blocks)} blocks, {len(placed_all)} figures placed', file=sys.stderr)


if __name__ == '__main__':
    build(os.path.abspath(sys.argv[1]))
