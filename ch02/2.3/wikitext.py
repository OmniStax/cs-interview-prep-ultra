"""Read a passage of a cached Wikipedia article (wikitext, `sources/_cache/wikipedia/<Title>.wiki`) into the
elements a page is made of, by script, so that no sentence of it is typed.

What it reads is what the article's passages in this section use, and nothing is guessed: an unknown template
stops the build, naming it. Section 2.3 is the first section of the book with Wikipedia blocks, so this reader
lives beside its spec; 2.1 and 2.5 need the same, and the chapter pass moves one reader to `tools/`.

- **Slices.** `lead(text)` is what stands before the first heading; `section(text, heading)` runs from the
  line `== heading ==` (any level) to the next heading of the same or a higher level.
- **Lines.** A blank line ends a paragraph; a line that starts with a space is preformatted (`<pre>`, Wikipedia's
  pseudocode and traces), a blank-but-for-spaces line inside it kept; `[[File:…]]` lines are images (dropped:
  the plan decides every figure); `<math display="block">…</math>` on its own lines is a display.
- **Inline.** `'''bold'''` and `''italic''`; `[[target|text]]` and `[[text]]` as their text; `[url text]` as a
  link; `<math>…</math>` as `$…$`; `{{mvar|x}}` italic; `{{mono|x}}` code; `{{math|…}}` its wikitext;
  `{{slink|Article|Section}}` as "Article § Section" (the spec decides how a reference to a passage the book
  does not carry is printed); `{{Anchor|…}}`, `{{sfn|…}}` and `{{harv|…}}` dropped (anchors and short
  citations the passage does not stand on).
- **References.** `<ref>…</ref>`, `<ref name="x">…</ref>`, `<ref name="x" />` and `{{r|x}}` (with an optional
  `{{rp|page}}` after it) are footnote markers; a named reference is resolved over the whole article. A note's
  text is Wikipedia's citation, set from its template (`cite book`, `cite journal`, `cite conference`,
  `Cite conference`, `cite web`) in the order Wikipedia prints it, or the reference's own words.
- **Inside a `<pre>`**, the markup of bold and italic is dropped (keywords and comments in ink, COLOR.md),
  and a `<span style="color:…">` the article sets is kept as it is: its own words name the colour.
"""
import html
import re

HEAD = re.compile(r'^(={2,6})\s*(.*?)\s*\1\s*$')


def heading_level(line):
    m = HEAD.match(line.strip())
    return (len(m.group(1)), m.group(2)) if m else None


def lead(text):
    out = []
    for l in text.split('\n'):
        if heading_level(l):
            break
        out.append(l)
    return out


def section(text, name):
    lines = text.split('\n')
    for i, l in enumerate(lines):
        h = heading_level(l)
        if h and h[1] == name:
            lvl, out = h[0], []
            for m in lines[i + 1:]:
                hh = heading_level(m)
                if hh and hh[0] <= lvl:
                    break
                out.append(m)
            return out
    raise SystemExit(f'wikitext: no section {name!r}')


# ---------------------------------------------------------------- templates and references

def split_args(body):
    """A template's body split at its top-level pipes."""
    parts, depth, cur, i = [], 0, '', 0
    while i < len(body):
        two = body[i:i + 2]
        if two in ('{{', '[['):
            depth += 1
            cur += two
            i += 2
            continue
        if two in ('}}', ']]'):
            depth -= 1
            cur += two
            i += 2
            continue
        if body[i] == '|' and depth == 0:
            parts.append(cur)
            cur = ''
        else:
            cur += body[i]
        i += 1
    parts.append(cur)
    return parts


def template_spans(s):
    """The outermost {{…}} spans of s, as (start, end) pairs."""
    out, depth, start, i = [], 0, None, 0
    while i < len(s) - 1:
        if s[i:i + 2] == '{{':
            if depth == 0:
                start = i
            depth += 1
            i += 2
            continue
        if s[i:i + 2] == '}}' and depth:
            depth -= 1
            i += 2
            if depth == 0:
                out.append((start, i))
            continue
        i += 1
    return out


def named_refs(text):
    refs = {}
    for m in re.finditer(r'<ref\s+name\s*=\s*"?([^">/]+?)"?\s*>(.*?)</ref>', text, re.S):
        refs[m.group(1).strip()] = m.group(2).strip()
    return refs


def cite(body):
    """A citation template as Wikipedia's CS1 prints it, near enough: authors, (year), title, publisher, pages."""
    args = split_args(body)
    name = args[0].strip().lower()
    kv = {}
    for a in args[1:]:
        if '=' in a:
            k, v = a.split('=', 1)
            kv[k.strip()] = v.strip()
    authors = []
    for n in ('', '1', '2', '3', '4', '5'):
        last, first = kv.get(f'last{n}'), kv.get(f'first{n}')
        if last:
            authors.append(f'{last}, {first}' if first else last)
        au = kv.get(f'author{n}')
        if au:
            authors.append(au)
    year = kv.get('year') or kv.get('date', '')[:4]
    title = inline_text(kv.get('title', ''))
    url = kv.get('url')
    t = f'<a href="{html.escape(url, quote=True)}">{title}</a>' if url else title
    bits = []
    if authors:
        bits.append('; '.join(inline_text(a) for a in authors) + (f' ({year}).' if year else '.'))
    if name in ('cite book',):
        ed = kv.get('edition')
        bits.append(f'<em>{t}</em>' + (f' ({ed} ed.)' if ed else '') + '.')
        if kv.get('publisher'):
            bits.append(inline_text(kv['publisher']) + '.')
        if kv.get('page'):
            bits.append(f'p.&nbsp;{kv["page"]}.')
        if kv.get('isbn'):
            bits.append(f'ISBN&nbsp;{kv["isbn"]}.')
    elif name in ('cite journal',):
        bits.append(f'"{t}".')
        j = f'<em>{inline_text(kv.get("journal", ""))}</em>'
        if kv.get('volume'):
            j += f' {kv["volume"]}'
        if kv.get('issue'):
            j += f' ({kv["issue"]})'
        if kv.get('pages'):
            j += f': {kv["pages"]}'
        bits.append(j + '.')
    elif name in ('cite conference',):
        bits.append(f'"{t}".')
        if kv.get('conference'):
            bits.append(f'<em>{inline_text(kv["conference"])}</em>.')
        if kv.get('series'):
            bits.append(inline_text(kv['series']) + (f' {kv["volume"]}' if kv.get('volume') else '') + '.')
        if kv.get('pages'):
            bits.append(f'pp.&nbsp;{kv["pages"]}.')
        if kv.get('doi'):
            bits.append(f'doi:{kv["doi"]}.')
    elif name in ('cite web',):
        bits.append(f'"{t}".')
        if kv.get('publisher'):
            bits.append(inline_text(kv['publisher']) + '.')
    else:
        raise SystemExit(f'wikitext: no rendering for citation template {name!r}')
    if not authors and year:
        bits.append(f'{year}.')
    return ' '.join(b for b in bits if b and b != '.')


def ref_html(body):
    """The words of a <ref>: a citation template, or the reference's own text with its links."""
    body = body.strip()
    m = re.fullmatch(r'\{\{(.*)\}\}', body, re.S)
    if m and re.match(r'\s*cite', m.group(1), re.I):
        return cite(m.group(1))
    return inline_text(body)


# ---------------------------------------------------------------- inline markup

def inline_text(s, notes=None, refs=None):
    """Wikitext inline markup to HTML; footnote markers are recorded in notes (a list) as they stand."""
    refs = refs or {}
    keep = []

    def hold(h):
        keep.append(h)
        return f'\x00{len(keep) - 1}\x00'

    def mark(name, words, page=None):
        if notes is None:
            return ''
        notes.append({'name': name, 'html': words + (f' p.&nbsp;{page}.' if page else '')})
        return hold(f'\x01{len(notes) - 1}\x01')

    # references, named or not
    s = re.sub(r'<ref\s+name\s*=\s*"?([^">/]+?)"?\s*/>', lambda m: mark(m.group(1).strip(), ref_html(refs[m.group(1).strip()])), s)
    s = re.sub(r'<ref\s+name\s*=\s*"?([^">/]+?)"?\s*>(.*?)</ref>', lambda m: mark(m.group(1).strip(), ref_html(m.group(2))), s, flags=re.S)
    s = re.sub(r'<ref>(.*?)</ref>', lambda m: mark(None, ref_html(m.group(1))), s, flags=re.S)
    s = re.sub(r'\{\{r\|([^}|]+)\}\}(?:\{\{rp\|([^}]+)\}\})?', lambda m: mark(m.group(1).strip(), ref_html(refs[m.group(1).strip()]), m.group(2)), s)
    # maths
    s = re.sub(r'<math>(.*?)</math>', lambda m: hold('$' + html.escape(' '.join(m.group(1).split()), quote=False) + '$'), s, flags=re.S)
    # templates, innermost first
    while True:
        spans = [(a, b) for a, b in template_spans(s)]
        if not spans:
            break
        a, b = spans[0]
        args = split_args(s[a + 2:b - 2])
        name = args[0].strip()
        low = name.lower()
        if low == 'mvar':
            r = '<em>' + inline_text(args[1]) + '</em>'
        elif low == 'mono':
            r = '<code>' + inline_text(args[1]) + '</code>'
        elif low == 'math':
            r = inline_text(args[1])
        elif low == '=':
            r = '='
        elif low == 'slink':
            r = f'{inline_text(args[1])} §&nbsp;{inline_text(args[2])}'
        elif low in ('anchor', 'sfn', 'harv'):
            r = ''
        else:
            raise SystemExit(f'wikitext: no reading for template {{{{{name}}}}}')
        s = s[:a] + hold(r) + s[b:]
    # links
    s = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]', lambda m: m.group(1), s)
    s = re.sub(r'\[(https?://[^\s\]]+)\s+([^\]]+)\]', lambda m: hold(f'<a href="{html.escape(m.group(1), quote=True)}">') + m.group(2) + hold('</a>'), s)
    s = html.escape(s, quote=False)
    s = re.sub(r"'''(.+?)'''", r'<strong>\1</strong>', s)
    s = re.sub(r"''(.+?)''", r'<em>\1</em>', s)
    s = s.replace('&amp;nbsp;', '&nbsp;')
    while '\x00' in s:
        s = re.sub(r'\x00(\d+)\x00', lambda m: keep[int(m.group(1))], s)
    return s


def pre_text(lines):
    """Preformatted lines: one leading space dropped, bold and italic markup dropped, colour spans kept."""
    out = []
    for l in lines:
        l = l[1:] if l.startswith(' ') else l
        spans = []

        def hold(m):
            spans.append(m.group(0))
            return f'\x00{len(spans) - 1}\x00'
        l = re.sub(r'<span style="color:\w+">|</span>', hold, l)
        l = l.replace("'''", '').replace("''", '')
        l = html.escape(l, quote=False)
        l = re.sub(r'\x00(\d+)\x00', lambda m: spans[int(m.group(1))], l)
        out.append(l.rstrip())
    while out and not out[-1].strip():
        out.pop()
    return '\n'.join(out)


def elements(lines, refs):
    """A passage's lines to elements: p (html, notes), pre (html), display (tex)."""
    els, i, n = [], 0, len(lines)
    while i < n:
        l = lines[i]
        if not l.strip():
            i += 1
            continue
        if re.match(r'^\s*\[\[File:', l):
            i += 1
            continue
        if l.lstrip().startswith('<math display="block">'):
            acc = [l]
            while '</math>' not in lines[i] and i + 1 < n:
                i += 1
                acc.append(lines[i])
            i += 1
            tex = re.sub(r'^\s*<math display="block">|</math>\s*$', '', '\n'.join(acc).strip(), flags=re.S).strip()
            els.append({'kind': 'display', 'tex': tex})
            continue
        if l.startswith(' '):
            acc = []
            while i < n and (lines[i].startswith(' ')):
                acc.append(lines[i])
                i += 1
            els.append({'kind': 'pre', 'html': pre_text(acc)})
            continue
        acc = []
        while i < n and lines[i].strip() and not lines[i].startswith(' ') and not lines[i].lstrip().startswith('<math display="block">') \
                and not re.match(r'^\s*\[\[File:', lines[i]):
            acc.append(lines[i].strip())
            i += 1
        text = ' '.join(acc)
        # a display that ends a paragraph's line stands after it
        m = re.search(r'<math display="block">(.*?)</math>\s*$', text, re.S)
        disp = None
        if m:
            disp = m.group(1).strip()
            text = text[:m.start()].rstrip()
        notes = []
        els.append({'kind': 'p', 'html': inline_text(text, notes, refs), 'notes': notes, 'wiki': text})
        if disp:
            els.append({'kind': 'display', 'tex': disp})
    return els
