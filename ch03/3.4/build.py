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
- **Wikipedia**: the article's lead and sections, read by ch02/2.3/wikitext.py (2.3's reader). Beyond 2.3's
  articles this one prints `{{harvtxt}}` (set as Wikipedia prints it: the authors, then the year in
  brackets), `{{sfnp}}` (a footnote in Wikipedia's short form), a `{{citation}}` inside a `<ref>`,
  `<code>` and `<sup>` inline, and `:` indented lines (set as `<blockquote>`). They are rewritten into what
  the reader reads before it reads the passage; `source.md` keeps the wikitext as the article prints it.
  The references become book footnotes in Wikipedia's words, numbered as their markers stand.

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
sys.path.insert(0, os.path.join(BOOK, 'ch02', '2.3'))
import build_markdown as BM  # noqa: E402  front_matter_end, slice_block, prepare (used as they are)
import build_translation as BT  # noqa: E402  parse, inline, el_html, el_text, outside_tags (used as they are)
import wikitext as WT  # noqa: E402  2.3's Wikipedia reader (used as it is)


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


# ---------------------------------------------------------------- Wikipedia

def harv_names(args):
    """{{harvtxt|A|B|C|1993}} → the authors as Wikipedia joins them, and the year."""
    pos = [a.strip() for a in args if '=' not in a]
    kv = dict(a.split('=', 1) for a in args if '=' in a)
    names, year = pos[:-1], pos[-1]
    if len(names) == 1:
        who = names[0]
    elif len(names) == 2:
        who = f'{names[0]} & {names[1]}'
    elif len(names) == 3:
        who = f'{names[0]}, {names[1]} & {names[2]}'
    else:
        who = f'{names[0]} et al.'
    return who, year, kv.get('loc', '').strip()


def citation(body):
    """A {{citation}} as Wikipedia's Citation Style 2 prints it, near enough: author (year), "contribution",
    title, location: publisher, page."""
    args = WT.split_args(body)
    kv = {}
    for a in args[1:]:
        if '=' in a:
            k, v = a.split('=', 1)
            kv[k.strip()] = v.strip()
    who = kv.get('last', '') + (', ' + kv['first'] if kv.get('first') else '')
    bits = [f'{who} ({kv["year"]})' if kv.get('year') else who]
    if kv.get('contribution'):
        bits.append(f'"{kv["contribution"]}"')
    bits.append(f"''{re.sub(r'^\[\[(.*)\]\]$', r'\1', kv.get('title', ''))}''")
    if kv.get('publisher'):
        bits.append((kv['location'] + ': ' if kv.get('location') else '') + kv['publisher'])
    if kv.get('page'):
        bits.append(f'p. {kv["page"]}')
    return ', '.join(bits)


def wiki_prepare(text):
    """The article as 2.3's reader reads it (see the module's docstring); the cached text is not changed."""
    text = re.sub(r'^\{\{short description\|[^}]*\}\}\n', '', text, flags=re.I)

    def tmpl(m):
        body = m.group(1)
        args = WT.split_args(body)
        name = args[0].strip().lower()
        if name == 'harvtxt':
            who, year, _ = harv_names(args[1:])
            return f'{who} ({year})'
        if name == 'sfnp':
            who, year, loc = harv_names(args[1:])
            return f'<ref>{who} ({year}){", " + loc if loc else ""}.</ref>'
        return m.group(0)
    text = re.sub(r'\{\{((?:harvtxt|sfnp)\|[^{}]*)\}\}', tmpl, text)
    text = re.sub(r'<ref>\s*\{\{(citation\b.*?)\}\}\.?\s*</ref>', lambda m: '<ref>' + citation(m.group(1)) + '.</ref>', text, flags=re.S)
    text = re.sub(r'<code>(.*?)</code>', r'{{mono|\1}}', text)
    text = re.sub(r'<sup>(.*?)</sup>', '\x02\\1\x03', text)
    # an indented line (`:`) stands apart, as Wikipedia sets it
    text = re.sub(r'^:(.*)$', lambda m: '\n\x05' + m.group(1).strip() + '\n', text, flags=re.M)
    return text


def wiki_block(b, spec, articles):
    path = os.path.join(BOOK, 'sources/_cache/wikipedia', b['file'])
    raw = articles.setdefault(path, open(path, encoding='utf-8').read())
    text = wiki_prepare(raw)
    refs = WT.named_refs(text)
    md_parts, parts = [], [f'<h2>{esc(b["h2"])}</h2>']
    after = [a for a in spec.get('AT', []) if a[0] == b['id']]
    placed = set()
    for kind, name in b['parts']:
        lines = WT.lead(text) if kind == 'lead' else WT.section(text, name)
        rawl = WT.lead(raw) if kind == 'lead' else WT.section(raw, name)
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        md_parts.append(('' if kind == 'lead' else f'== {name} ==\n') + '\n'.join(rawl).strip('\n'))
        if kind == 'section':
            parts.append(f'<h3>{esc(name)}</h3>')
        for e in WT.elements(lines, refs):
            if e['kind'] == 'pre':
                parts.append(f'<pre>{e["html"]}</pre>')
                anchor_text = html.unescape(e['html'])
            elif e['kind'] == 'display':
                parts.append(f'$${esc(e["tex"])}$$')
                anchor_text = e['tex']
            else:
                h = e['html'].replace('\x02', '<sup>').replace('\x03', '</sup>')
                quote = h.startswith('\x05')
                parts.append(('Q' if quote else 'P', h.lstrip('\x05'), e['notes']))
                anchor_text = e['wiki']
            for _, anchor, key in after:
                if anchor in anchor_text and key not in placed:
                    parts.append(spec['HTML'][key])
                    placed.add(key)
    want = {a[2] for a in after}
    if want - placed:
        raise SystemExit(f'{b["id"]}: never placed {sorted(want - placed)}')
    return '\n\n'.join(md_parts), parts


# ---------------------------------------------------------------- the page

def build():
    mod = load_spec()
    spec = {k: getattr(mod, k) for k in dir(mod) if k.isupper()}
    pages, articles, used_code = {}, {}, set()
    md_blocks, html_blocks, fn_rows = [], [], []
    for b in spec['BLOCKS']:
        head = f'<!-- block {b["id"]} · source {b["source"]} · {b["locator"]} -->'
        if b['source'] == 'cpa':
            md, body, _ = cpa_block(b, spec, pages, used_code)
        else:
            md, parts = wiki_block(b, spec, articles)
            out = []
            for p in parts:
                if isinstance(p, tuple):
                    tag, h, ns = p
                    for k in [int(x) for x in re.findall(r'\x01(\d+)\x01', h)]:
                        fid = f'wp-{b["id"]}-{len(fn_rows) + 1}'
                        fn_rows.append({'id': fid, 'kind': 'book', 'number': str(len(fn_rows) + 1), 'html': ns[k]['html'], 'source': 'wikipedia'})
                        h = h.replace(f'\x01{k}\x01', f'<sup class="fn" data-note="{fid}"></sup>', 1)
                    out.append(f'<blockquote><p>{h}</p></blockquote>' if tag == 'Q' else f'<p>{h}</p>')
                else:
                    out.append(p)
            body = '\n'.join(out)
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
