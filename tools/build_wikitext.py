#!/usr/bin/env python3
"""Assemble a section whose every block is Wikipedia's (2.5): source.md, text.html, footnotes.json and captions.json,
by script, with tools/wikitext.py, the book's one Wikipedia reader (its docstring says what it reads, how a block's
`parts` slice the article and how the citations are numbered).

What the section's build_spec.py gives, beside TITLE and BLOCKS (see wikitext.block for a block's keys):
IMAGES, CODE, WIKILINKS, AT, DROP_TEMPLATES and CITE_TEMPLATES as tools/wikitext.py reads them; MARKS [(block id,
old, new, count?)]: the spans (concepts, referents, the erratum markers), set outside tags unless `old` holds a
tag; FIXES [(old, new, why)]: the replacement table, each entry with its reason. HTML may hold
`{{caption FILE}}` and `{{caption-text FILE}}`, filled with a frame's caption.

    python3 -I tools/build_wikitext.py ch02/2.5
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
import wikitext as WT  # noqa: E402


def outside_tags(h, old, new, count=1):
    parts = re.split(r'(<[^>]+>)', h)
    done = 0
    for i, p in enumerate(parts):
        if p.startswith('<') or done >= count:
            continue
        if old in p:
            n = min(p.count(old), count - done)
            parts[i] = p.replace(old, new, n)
            done += n
    return ''.join(parts), done


def captions_of(spec):
    """Every frame's caption, by file name, before the page is set (a figure's attributes may carry one)."""
    caps, log = {}, []
    for b in spec['BLOCKS']:
        a = WT.Article(b['file'])
        ctx = WT.Ctx(a, spec, log)
        for part in b['parts']:
            for e in WT.elements(WT.part_lines(a, part)[0], ctx):
                if e['kind'] == 'image' and e['file'] not in caps:
                    caps[e['file']] = {'html': e['caption_html'], 'text': html.unescape(re.sub(r'<[^>]+>', '', e['caption_html']))}
    return caps


def build(sec_dir):
    sp = importlib.util.spec_from_file_location('build_spec', os.path.join(sec_dir, 'build_spec.py'))
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    spec = {k: getattr(mod, k) for k in dir(mod) if k.isupper()}
    fixes = spec.get('FIXES', [])
    used_fix, log, state = set(), [], {}
    captions = captions_of(spec)

    def fill(s):
        s = re.sub(r'\{\{caption-text ([^}]+)\}\}', lambda m: html.escape(captions[m.group(1)]['text'], quote=True), s)
        return re.sub(r'\{\{caption ([^}]+)\}\}', lambda m: captions[m.group(1)]['html'], s)
    HTML = {k: fill(v) for k, v in spec.get('HTML', {}).items()}
    notes = WT.Notes()
    html_blocks, md_blocks = [], []
    for b in spec['BLOCKS']:
        md, parts = WT.block(b, spec, notes, log, html_of=HTML.__getitem__, state=state)
        out = []
        for h in parts:
            for i, (old, new, why) in enumerate(fixes):
                if old in h:
                    h = h.replace(old, new)
                    used_fix.add(i)
            out.append(h)
        body = '\n'.join(out)
        for blk, old, new, *cnt in spec.get('MARKS', []):
            if blk != b['id']:
                continue
            if '<' in old:
                n = min(body.count(old), cnt[0] if cnt else 1)
                body = body.replace(old, new, n)
            else:
                body, n = outside_tags(body, old, new, cnt[0] if cnt else 1)
            if n == 0:
                raise SystemExit(f"MARK NOT FOUND {b['id']}: {old!r}")
        attrs = f'id="{b["id"]}" data-source="{b["source"]}" data-locator="{html.escape(b["locator"], quote=True)}"'
        html_blocks.append(f'<section {attrs}>\n{body}\n</section>')
        md_blocks.append(f'<!-- block {b["id"]} · source {b["source"]} · {b["locator"]} -->\n\n' + md)
    out_md = f'# {spec["TITLE"]}\n\n' + '\n\n'.join(md_blocks) + '\n'
    open(os.path.join(sec_dir, 'source.md'), 'w', encoding='utf-8').write(out_md)
    with open(os.path.join(sec_dir, 'text.html'), 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(html_blocks) + '\n')
    import apply_terms  # the judged concept mentions, after the page is written
    apply_terms.apply(sec_dir)
    json.dump(notes.rows, open(os.path.join(sec_dir, 'footnotes.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(captions, open(os.path.join(sec_dir, 'captions.json'), 'w'), ensure_ascii=False, indent=1)
    for m in WT.unplaced(spec, state):
        print(m, file=sys.stderr)
    unused = [fixes[i][0] for i in range(len(fixes)) if i not in used_fix]
    if unused:
        print('FIXES never applied:', unused, file=sys.stderr)
    if log:
        print('templates left out:', sorted(set(log)), file=sys.stderr)
    print(f'{sec_dir}: {len(html_blocks)} blocks, {len(notes.rows)} notes', file=sys.stderr)


if __name__ == '__main__':
    build(os.path.abspath(sys.argv[1]))
