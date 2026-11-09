#!/usr/bin/env python3
"""Assemble a section's source.md and text.html from Wikipedia's wikitext, by script.

Wikipedia (`wikipedia`) is cached as one `.wiki` file per article at a pinned revision
(sources/_cache/wikipedia/_meta.json). tools/build_text.py reads Erickson, ODS and OpenDSA, and
tools/build_markdown.py and build_translation.py read Markdown; this reads wikitext. Nothing is typed:

- **The source**: each block of the spec is one or more slices of an article, each from a heading line
  (inclusive; None for the article's lead) to another heading line (exclusive), optionally cut before the
  paragraph that starts with `stop_at`. The slices are written to `source.md` verbatim under the block's
  marker line.
- **The page**: the slices are read as the article prints them: headings, paragraphs (lines joined until
  a blank line), `'''bold'''` and `''italic''`, `[[links|text]]`, `<code>`, `<math>` (as `$…$`),
  `{{IPA|…}}`, `<syntaxhighlight>` listings, one-space-indented preformatted lines (pseudocode, set as a
  `<pre>` in plain text, its bold and italics dropped), and `[[File:…]]`/`[[Image:…]]` frames.
  A citation (`<ref>…</ref>`, `<ref name=… />`) is not carried; a `<ref group="note">` is the article's
  own explanatory note and becomes a book footnote. A template standing alone on a line (`{{Short
  description}}`, a maintenance box, a transcluded table) is left out and named on stderr; one inline is
  left out too, except `{{IPA}}`.

What the section's build_spec.py gives, beside TITLE and BLOCKS:

- BLOCKS [{id, source, locator, file, h2, parts: [(from heading line | None, to heading line | None,
  stop_at text | None)], headings: {heading text: level | None}}]: `headings` sets a heading's level
  (None leaves it out); others take the article's level plus one, at most 4.
- IMAGES {file name: [HTML key | None, …]}: what stands in place of each occurrence of a file's frame,
  in order (None: left out). A frame's caption goes to captions.json under the file name, HTML and text.
- CODE [(piece of the listing, HTML key | {python, java, javascript} variants)]: a `<syntaxhighlight>`
  listing whose text holds the piece becomes that figure (a Sim whose panel is the listing) or a code set
  whose C++ variant is the source's listing verbatim (it is C that compiles as C++) and whose other
  variants are the spec's, AI-marked with AI.
- LINKS {wikilink target: href}: a link the book carries the target of; any other wikilink is its text.
- AT [(block id, a piece of an element's text, HTML key)]: a figure that stands after that element.
- MARKS [(block id, old, new, count?)]: the spans (concepts, referents, the erratum markers), set
  outside tags unless `old` holds a tag.
- FIXES [(old, new, why)]: the replacement table, each entry with its reason (empty where nothing needs
  correcting).

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


def esc(s):
    return html.escape(s, quote=False)


# ---------------------------------------------------------------- slicing

def heading_of(line):
    m = re.match(r'^(={2,6})\s*(.*?)\s*\1\s*$', line)
    return (len(m.group(1)), m.group(2)) if m else None


def slice_part(lines, start, stop, stop_at):
    """The lines from the heading line `start` (None: the top of the article) to the line before `stop`
    (None: the next level-2 heading after the start, for the lead the first heading), cut before the
    paragraph that starts with `stop_at`."""
    if start is None:
        i0 = 0
    else:
        i0 = next(i for i, l in enumerate(lines) if l.strip() == start)
    if stop is not None:
        i1 = next(i for i, l in enumerate(lines) if i > i0 and l.strip() == stop)
    else:
        i1 = next((i for i, l in enumerate(lines) if i > i0 and heading_of(l) and (start is None or heading_of(l)[0] <= heading_of(lines[i0])[0])), len(lines))
    out = lines[i0:i1]
    if stop_at:
        k = next(i for i, l in enumerate(out) if l.startswith(stop_at))
        out = out[:k]
    while out and not out[-1].strip():
        out.pop()
    return out


# ---------------------------------------------------------------- inline wikitext

def strip_templates(s, log):
    """Inline templates: {{IPA|x}} is its text; any other is left out (named on stderr)."""
    def one(m):
        body = m.group(1)
        name = body.split('|')[0].strip()
        if name.upper() == 'IPA':
            return body.split('|', 1)[1] if '|' in body else ''
        log.append(name)
        return ''
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\{\{([^{}]*)\}\}', one, s)
    return s


def quotes(s):
    """MediaWiki's '' and ''' (and ''''') as <em> and <strong>, in one pass over the line."""
    parts = re.split(r"('{2,5})", s)
    out, em, strong = [], False, False
    for p in parts:
        if re.fullmatch(r"'{2,5}", p):
            n = len(p)
            if n == 5:
                if strong:
                    out.append('</strong>'); strong = False
                else:
                    out.append('<strong>'); strong = True
                if em:
                    out.append('</em>'); em = False
                else:
                    out.append('<em>'); em = True
            elif n == 3:
                out.append('</strong>' if strong else '<strong>'); strong = not strong
            elif n == 2:
                out.append('</em>' if em else '<em>'); em = not em
            else:   # four: an apostrophe and bold
                out.append("’"); out.append('</strong>' if strong else '<strong>'); strong = not strong
        else:
            out.append(p)
    if em:
        out.append('</em>')
    if strong:
        out.append('</strong>')
    return ''.join(out)


def inline(s, spec, notes, log):
    """One paragraph of wikitext as HTML (and its notes appended to `notes`)."""
    links = spec.get('LINKS', {})
    # the article's own notes (a ref of group "note") become footnote markers; citations are not carried
    def note(m):
        notes.append(m.group(1))
        return f'\x00NOTE{len(notes)}\x00'
    s = re.sub(r'<ref\s+group="?note"?\s*>(.*?)</ref>', note, s, flags=re.S)
    s = re.sub(r'<ref[^>/]*/>', '', s)
    s = re.sub(r'<ref[^>]*>.*?</ref>', '', s, flags=re.S)
    s = strip_templates(s, log)
    # protect code and maths from the quote pass and from escaping
    keep = []
    def protect(h):
        keep.append(h)
        return f'\x00K{len(keep) - 1}\x00'
    s = re.sub(r'<code>(.*?)</code>', lambda m: protect('<code>' + esc(plain_pre(m.group(1))) + '</code>'), s)
    s = re.sub(r'<math>(.*?)</math>', lambda m: protect('$' + m.group(1).strip() + '$'), s)

    def link(m):
        target, _, text = m.group(1).partition('|')
        text = text or target
        t = target.strip()
        key = t[0].upper() + t[1:] if t else t
        href = links.get(t) or links.get(key)
        inner = quotes(esc(text))
        return protect(f'<a href="{href}">' + inner + '</a>') if href else protect(inner)
    s = re.sub(r'\[\[(?!File:|Image:)([^\[\]]*)\]\]([a-z]*)', lambda m: link(m) + m.group(2), s)
    s = esc(html.unescape(s))
    s = quotes(s)
    s = re.sub(r'\x00K(\d+)\x00', lambda m: keep[int(m.group(1))], s)
    return s


def plain_pre(s):
    """A preformatted (pseudocode) line in plain text: links as their text, bold and italics dropped."""
    s = re.sub(r'<ref[^>/]*/>', '', s)
    s = re.sub(r'<ref[^>]*>.*?</ref>', '', s)
    s = re.sub(r'\[\[(?:[^\[\]|]*\|)?([^\[\]]*)\]\]', r'\1', s)
    s = re.sub(r"'{2,5}", '', s)
    return s


# ---------------------------------------------------------------- elements

def elements(lines, log):
    """The slice as elements: heading, p, pre, code, image, template."""
    els, para, pre = [], [], []
    i = 0

    def close():
        if para:
            els.append({'kind': 'p', 'text': ' '.join(x.strip() for x in para)})
            para.clear()
        if pre:
            els.append({'kind': 'pre', 'lines': list(pre)})
            pre.clear()
    while i < len(lines):
        l = lines[i]
        h = heading_of(l)
        if h:
            close(); els.append({'kind': 'heading', 'level': h[0], 'text': h[1]}); i += 1; continue
        m = re.match(r'\s*<syntaxhighlight([^>]*)>(.*)$', l)
        if m:
            close()
            body, j = [m.group(2)] if m.group(2) else [], i + 1
            while '</syntaxhighlight>' not in lines[j]:
                body.append(lines[j]); j += 1
            last = lines[j].split('</syntaxhighlight>')[0]
            if last:
                body.append(last)
            lang = re.search(r'lang="?(\w+)', m.group(1))
            els.append({'kind': 'code', 'lang': lang.group(1).lower() if lang else '', 'text': '\n'.join(body).strip('\n')})
            i = j + 1; continue
        m = re.match(r'\s*\[\[(?:File|Image):([^|\]]+)\|(.*)\]\]\s*$', l)
        if m:
            close()
            fields = m.group(2).split('|')
            els.append({'kind': 'image', 'file': m.group(1).strip(), 'caption': fields[-1].strip()})
            i += 1; continue
        if re.match(r'^\{\{.*\}\}\s*$', l):
            close(); log.append(re.match(r'^\{\{([^|}]*)', l).group(1).strip()); i += 1; continue
        if not l.strip():
            # a blank line ends a paragraph; inside preformatted text it ends the block as well
            close(); i += 1; continue
        if l.startswith(' '):
            if para:
                close()
            pre.append(l[1:])
            i += 1; continue
        if pre:
            close()
        para.append(l)
        i += 1
    close()
    return els


# ---------------------------------------------------------------- assembly

def code_set(source_code, variants, ai):
    pres = []
    for lang in ('python', 'java', 'cpp', 'javascript'):
        code = source_code if lang == 'cpp' else variants.get(lang)
        if code is None:
            continue
        mark = '' if lang == 'cpp' else f' data-ai="{ai}"'
        pres.append(f'<pre data-lang="{lang}"{mark}><code>{esc(code.strip(chr(10)))}</code></pre>')
    no_py = '' if 'python' in variants else f' data-no-python="{html.escape(variants.get("_no_python", ""), quote=True)}"'
    return f'<div class="code-set"{no_py}>\n' + '\n'.join(pres) + '\n</div>'


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


def build(sec_dir):
    sp = importlib.util.spec_from_file_location('build_spec', os.path.join(sec_dir, 'build_spec.py'))
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    spec = {k: getattr(mod, k) for k in dir(mod) if k.isupper()}
    fixes = spec.get('FIXES', [])
    used_fix, used_code, used_at = set(), set(), set()
    captions, fn_rows, md_notes = {}, [], []
    seen_img = {}
    log = []

    # the frames' captions first, by file name, so a figure's attributes can carry them
    for b in spec['BLOCKS']:
        lines = open(os.path.join(BOOK, b['file']), encoding='utf-8').read().split('\n')
        for start, stop, stop_at in b['parts']:
            for e in elements(slice_part(lines, start, stop, stop_at), []):
                if e['kind'] == 'image' and e['file'] not in captions:
                    h = inline(e['caption'], spec, [], [])
                    captions[e['file']] = {'html': h, 'text': html.unescape(re.sub(r'<[^>]+>', '', h))}

    def fill(s):
        s = re.sub(r'\{\{caption-text ([^}]+)\}\}', lambda m: html.escape(captions[m.group(1)]['text'], quote=True), s)
        return re.sub(r'\{\{caption ([^}]+)\}\}', lambda m: captions[m.group(1)]['html'], s)
    HTML = {k: fill(v) for k, v in spec.get('HTML', {}).items()}

    html_blocks, md_blocks = [], []
    for b in spec['BLOCKS']:
        lines = open(os.path.join(BOOK, b['file']), encoding='utf-8').read().split('\n')
        hparts = [f'<h2>{esc(b["h2"])}</h2>']
        md = []
        notes = []
        for start, stop, stop_at in b['parts']:
            sl = slice_part(lines, start, stop, stop_at)
            md.append('\n'.join(sl))
            for e in elements(sl, log):
                k = e['kind']
                if k == 'heading':
                    lvl = b.get('headings', {}).get(e['text'], min(4, e['level'] + 1))
                    if lvl is not None:
                        hparts.append(f'<h{lvl}>{inline(e["text"], spec, notes, log)}</h{lvl}>')
                    continue
                if k == 'image':
                    n = seen_img.get(e['file'], 0)
                    seen_img[e['file']] = n + 1
                    keys = spec.get('IMAGES', {}).get(e['file'])
                    if keys is None or n >= len(keys):
                        print(f'{b["id"]}: no decision for image {e["file"]} (occurrence {n + 1}); left out', file=sys.stderr)
                        continue
                    if keys[n]:
                        hparts.append(HTML[keys[n]])
                    continue
                if k == 'code':
                    hit = next(((j, c) for j, c in enumerate(spec.get('CODE', [])) if c[0] in e['text']), None)
                    if hit is None:
                        print(f'{b["id"]}: no decision for a {e["lang"]} listing starting {e["text"][:40]!r}; set as <pre>', file=sys.stderr)
                        hparts.append('<pre>' + esc(e['text']) + '</pre>')
                        continue
                    used_code.add(hit[0])
                    what = hit[1][1]
                    hparts.append(HTML[what] if isinstance(what, str) else code_set(e['text'], what, spec.get('AI', '')))
                    continue
                if k == 'pre':
                    hparts.append('<pre>' + esc('\n'.join(plain_pre(x) for x in e['lines'])) + '</pre>')
                    continue
                h = inline(e['text'], spec, notes, log)
                for i, (old, new, why) in enumerate(fixes):
                    if old in h:
                        h = h.replace(old, new); used_fix.add(i)
                hparts.append(f'<p>{h}</p>')
                for j, (blk, piece, key) in enumerate(spec.get('AT', [])):
                    if blk == b['id'] and piece in e['text'] and j not in used_at:
                        hparts.append(HTML[key]); used_at.add(j)
        body = '\n'.join(hparts)
        # the article's notes: markers and rows, numbered as the article numbers them ("note 1")
        for i, n in enumerate(notes, start=1):
            nid = f'{b["id"]}-note-{i}'
            body = body.replace(f'\x00NOTE{i}\x00', f'<sup class="fn" data-note="{nid}"></sup>')
            fn_rows.append({'id': nid, 'kind': 'book', 'number': f'note {i}', 'html': inline(n, spec, [], log), 'source': b['source']})
            md_notes.append(f'[^{nid}]: {n}')
        for blk, old, new, *cnt in spec.get('MARKS', []):
            if blk != b['id']:
                continue
            if '<' in old:
                n = min(body.count(old), cnt[0] if cnt else 1)
                body = body.replace(old, new, n)
            else:
                body, n = outside_tags(body, old, new, cnt[0] if cnt else 1)
            if n == 0:
                print(f"MARK NOT FOUND {b['id']}: {old!r}", file=sys.stderr)
        attrs = f'id="{b["id"]}" data-source="{b["source"]}" data-locator="{html.escape(b["locator"], quote=True)}"'
        html_blocks.append(f'<section {attrs}>\n{body}\n</section>')
        md_blocks.append(f'<!-- block {b["id"]} · source {b["source"]} · {b["locator"]} -->\n\n' + '\n\n'.join(md))

    out_md = f'# {spec["TITLE"]}\n\n' + '\n\n'.join(md_blocks) + '\n'
    if md_notes:
        out_md += '\n## Notes\n\n' + '\n\n'.join(md_notes) + '\n'
    open(os.path.join(sec_dir, 'source.md'), 'w', encoding='utf-8').write(out_md)
    with open(os.path.join(sec_dir, 'text.html'), 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(html_blocks) + '\n')
    import apply_terms  # the judged concept mentions, after the page is written
    apply_terms.apply(sec_dir)
    json.dump(fn_rows, open(os.path.join(sec_dir, 'footnotes.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(captions, open(os.path.join(sec_dir, 'captions.json'), 'w'), ensure_ascii=False, indent=1)
    for i, c in enumerate(spec.get('CODE', [])):
        if i not in used_code:
            print(f'CODE never matched: {c[0]!r}', file=sys.stderr)
    for i, a in enumerate(spec.get('AT', [])):
        if i not in used_at:
            print(f'AT never placed: {a!r}', file=sys.stderr)
    unused = [fixes[i][0] for i in range(len(fixes)) if i not in used_fix]
    if unused:
        print('FIXES never applied:', unused, file=sys.stderr)
    if log:
        print('templates left out:', sorted(set(log)), file=sys.stderr)
    print(f'{sec_dir}: {len(html_blocks)} blocks, {len(fn_rows)} notes', file=sys.stderr)


if __name__ == '__main__':
    build(os.path.abspath(sys.argv[1]))
