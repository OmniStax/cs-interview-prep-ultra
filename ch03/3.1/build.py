#!/usr/bin/env python3
"""Assemble 3.1's source.md, text.html, footnotes.json and captions.json from its spec, by script.

The page joins two sources block by block: Wikipedia's "Stack (abstract data type)" (wikitext) and cp-algorithms'
"Balanced bracket sequences" (Markdown). No shared assembler joins those two, so this one calls the readers the book
already has and types none of either source:

- **Wikipedia**: `ch02/2.3/wikitext.py`, imported unchanged (lead and section slicing, named references, inline markup,
  preformatted pseudocode). This article needs four readings that reader lacks, done here before or around it: a `*` line
  is a list item; `<ref group="nb" name="…" />` is the article's own explanatory note, defined in its Notes list
  (`{{reflist|group="nb"|refs=…}}`), and becomes a book note numbered as Wikipedia numbers it ("nb 1"); a `[[file:…]]`
  frame is recognised whatever the case of "file" (the spec's IMAGES say what stands in its place); a template standing
  alone on a line (`{{short description}}`, `{{Use dmy dates}}`, …) is left out and named on stderr. The one citation
  template the passage cites that is not a `cite …` one, `{{Introduction to Algorithms|3|pages=…}}`, is set from the
  spec's CITE_TEMPLATES (what the template prints on Wikipedia), and every citation becomes a book footnote in
  Wikipedia's words, numbered in the order its markers stand on the page, a named one keeping its number where it is
  used again (2.1's and 2.3's rule).
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
sys.path.insert(0, os.path.join(BOOK, 'ch02', '2.3'))
import build_translation as BT  # noqa: E402  the shared Markdown parser and inline setter
import wikitext as WT  # noqa: E402  2.3's Wikipedia reader (the chapter pass moves one reader to tools/)


def load_spec():
    sp = importlib.util.spec_from_file_location('build_spec_31', os.path.join(HERE, 'build_spec.py'))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


# ---------------------------------------------------------------- Wikipedia

FRAME = re.compile(r'^\s*\[\[(?:[Ff]ile|[Ii]mage):([^|\]]+)\|(.*)\]\]\s*$')


def nb_notes(text):
    """The article's own notes, `<ref group="nb" name="x">…</ref>`, by name."""
    return {m.group(1): m.group(2).strip()
            for m in re.finditer(r'<ref\s+group="?nb"?\s+name="?([^">/]+?)"?\s*>(.*?)</ref>', text, re.S)}


def cite_templates(s, spec):
    """Inside a <ref>: a citation template the spec sets from what Wikipedia prints for it is held as a token (set after
    the reader has escaped the rest), and CS1's `author-last` / `author-first` are read as the `last` / `first` the
    reader knows (the same fields under their other names)."""
    for k, name in enumerate(spec.get('CITE_TEMPLATES', {})):
        s = re.sub(r'\{\{' + re.escape(name) + r'\|[^{}]*\}\}', f'CITETEMPLATE{k}X', s)
    return re.sub(r'\|\s*author-(last|first)(\d*)\s*=', r'|\1\2=', s)


def cite_words(h, spec):
    for k, words in enumerate(spec.get('CITE_TEMPLATES', {}).values()):
        h = h.replace(f'CITETEMPLATE{k}X', words)
    return h


def wp_elements(lines, refs, notes, spec, log):
    """A passage's lines to elements: p (html, refs in order), list (items), pre (html), image (file, caption)."""
    els, i, n = [], 0, len(lines)
    while i < n:
        l = lines[i]
        s = l.strip()
        if not s:
            i += 1
            continue
        h = WT.heading_level(l)
        if h:
            els.append({'kind': 'heading', 'level': h[0], 'text': h[1]})
            i += 1
            continue
        m = FRAME.match(l)
        if m:
            fields = WT.split_args(m.group(2))
            els.append({'kind': 'image', 'file': m.group(1).strip(), 'caption': fields[-1].strip()})
            i += 1
            continue
        if re.match(r'^\{\{.*\}\}$', s):
            log.append(re.match(r'^\{\{([^|}]*)', s).group(1).strip())
            i += 1
            continue
        if l.startswith(' '):
            acc = []
            while i < n and lines[i].startswith(' '):
                acc.append(lines[i])
                i += 1
            els.append({'kind': 'pre', 'html': WT.pre_text(acc)})
            continue
        if s.startswith('*'):
            items = []
            while i < n and lines[i].strip().startswith('*'):
                items.append(lines[i].strip()[1:].strip())
                i += 1
            els.append({'kind': 'list', 'items': [para(t, refs, notes, spec) for t in items], 'wiki': '\n'.join(items)})
            continue
        acc = []
        while i < n and lines[i].strip() and not lines[i].startswith(' ') and not lines[i].strip().startswith('*') \
                and not FRAME.match(lines[i]) and not WT.heading_level(lines[i]) and not re.match(r'^\{\{.*\}\}$', lines[i].strip()):
            acc.append(lines[i].strip())
            i += 1
        text = ' '.join(acc)
        els.append(dict(para(text, refs, notes, spec), kind='p', wiki=text))
    return els


def para(text, refs, notes, spec):
    """One paragraph or list item: the nb note markers held as \\x02k\\x02, the citations as 2.3's reader marks them."""
    held = []

    def nb(m):
        held.append(m.group(1).strip())
        return f'\x02{len(held) - 1}\x02'
    text = re.sub(r'<ref\s+group="?nb"?\s+name="?([^">/]+?)"?\s*/>', nb, text)
    text = re.sub(r'<code>(.*?)</code>', lambda m: '{{mono|' + m.group(1) + '}}', text)
    cites = []
    h = WT.inline_text(cite_templates(text, spec), cites, {k: cite_templates(v, spec) for k, v in refs.items()})
    for c in cites:
        c['html'] = cite_words(c['html'], spec)
    return {'html': h, 'cites': cites, 'nbs': held}


def wp_block(b, spec, articles, log):
    """A block of the article: its parts (the lead, or a section with its subsections, whose headings sit one level
    under the block's <h2>: the article's level 4 as <h3>), each optionally opened by an <h3> the spec names."""
    path = os.path.join(BOOK, 'sources/_cache/wikipedia', b['file'])
    text = articles.setdefault(path, open(path, encoding='utf-8').read())
    refs, nbs = WT.named_refs(text), nb_notes(text)
    md_parts, parts = [], [f'<h2>{b["h2"]}</h2>']
    for kind, name, h3 in b['parts']:
        lines = WT.lead(text) if kind == 'lead' else WT.section(text, name)
        while lines and not lines[-1].strip():
            lines.pop()
        md_parts.append(('' if kind == 'lead' else f'== {name} ==\n') + '\n'.join(lines))
        if h3:
            parts.append(f'<h3>{h3}</h3>')
        for e in wp_elements(lines, refs, nbs, spec, log):
            parts.append(e)
    return '\n\n'.join(md_parts), parts, nbs


# ---------------------------------------------------------------- cp-algorithms

def md_slice(lines, b):
    a = next((i for i, l in enumerate(lines) if l.strip() == b['from']), None)
    if a is None:
        raise SystemExit(f'{b["id"]}: heading {b["from"]!r} is not on the page')
    z = next((i for i in range(a + 1, len(lines)) if lines[i].strip() == b['to']), None) if b.get('to') else len(lines)
    if z is None:
        raise SystemExit(f'{b["id"]}: no heading {b["to"]!r} after {b["from"]!r}')
    out = lines[a:z]
    if b.get('stop_at'):
        k = next((i for i, l in enumerate(out) if l.startswith(b['stop_at'])), None)
        if k is None:
            raise SystemExit(f'{b["id"]}: stop_at {b["stop_at"]!r} not in the slice')
        out = out[:k]
    while out and not out[-1].strip():
        out.pop()
    return out


def md_block(b, spec):
    page = open(os.path.join(BOOK, b['file']), encoding='utf-8').read().split('\n')
    if page and page[0].strip() == '---':
        end = next(i for i in range(1, len(page)) if page[i].strip() == '---')
        page = page[end + 1:]
    src = md_slice(page, b)
    # a level-1 heading is read one level deeper, as tools/build_markdown.py reads it
    lines = ['#' + l if re.match(r'^#\s', l) else l for l in src]
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
    articles, log = {}, []
    md_blocks, html_blocks, fn_rows = [], [], []
    cite_no, nb_no = {}, {}
    seen_img, captions, used_fix, placed = {}, {}, set(), set()
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
            md, parts, nbs = wp_block(b, spec, articles, log)

            def marks(p):
                h = p['html']
                for k in [int(x) for x in re.findall(r'\x01(\d+)\x01', h)]:
                    c = p['cites'][k]
                    key = c['name'] or f'anon-{len(fn_rows)}'
                    if key not in cite_no:
                        cite_no[key] = len(cite_no) + 1
                        fid = f'wp-{b["id"]}-{cite_no[key]}'
                        fn_rows.append({'id': fid, 'kind': 'book', 'number': str(cite_no[key]), 'html': c['html'], 'source': 'wikipedia'})
                        h = h.replace(f'\x01{k}\x01', f'<sup class="fn" data-note="{fid}"></sup>', 1)
                    else:
                        # a citation used again: a second note with the same number, so every note has one marker (2.1)
                        fid = f'wp-{b["id"]}-{cite_no[key]}-{len(fn_rows)}'
                        fn_rows.append({'id': fid, 'kind': 'book', 'number': str(cite_no[key]), 'html': c['html'], 'source': 'wikipedia'})
                        h = h.replace(f'\x01{k}\x01', f'<sup class="fn" data-note="{fid}"></sup>', 1)
                for k, name in enumerate(p['nbs']):
                    if name not in nb_no:
                        nb_no[name] = len(nb_no) + 1
                    fid = f'wp-{b["id"]}-nb-{nb_no[name]}'
                    words = WT.inline_text(nbs[name])
                    fn_rows.append({'id': fid, 'kind': 'book', 'number': f'nb {nb_no[name]}', 'html': words, 'source': 'wikipedia'})
                    h = h.replace(f'\x02{k}\x02', f'<sup class="fn" data-note="{fid}"></sup>', 1)
                return h
            for p in parts:
                if isinstance(p, str):
                    out.append(p)
                    continue
                if p['kind'] == 'image':
                    n = seen_img.get(p['file'], 0)
                    seen_img[p['file']] = n + 1
                    cap = WT.inline_text(p['caption'])
                    captions.setdefault(p['file'], {'html': cap, 'text': html.unescape(re.sub(r'<[^>]+>', '', cap))})
                    keys = spec['IMAGES'].get(p['file'])
                    if keys is None or n >= len(keys):
                        raise SystemExit(f'{b["id"]}: no decision for image {p["file"]} (occurrence {n + 1})')
                    if keys[n]:
                        out.append(spec['HTML'][keys[n]])
                    continue
                if p['kind'] == 'heading':
                    out.append(f'<h{p["level"] - 1}>{WT.inline_text(p["text"])}</h{p["level"] - 1}>')
                    continue
                if p['kind'] == 'pre':
                    out.append(f'<pre>{p["html"]}</pre>')
                    place(html.unescape(p['html']))
                    continue
                if p['kind'] == 'list':
                    out.append('<ul>' + ''.join(f'<li>{marks(it)}</li>' for it in p['items']) + '</ul>')
                    place(p['wiki'])
                    continue
                out.append(f'<p>{marks(p)}</p>')
                place(p['wiki'])
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
        # wikilinks the book carries the target of: the reader prints a link as its text, so the spec names the words
        for blk, words, href in spec.get('LINKS', []):
            if blk != b['id']:
                continue
            body, k = BT.outside_tags(body, words, f'<a href="{href}">{words}</a>')
            if k == 0:
                raise SystemExit(f'LINK NOT FOUND {blk}: {words!r}')
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
