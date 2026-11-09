"""The book's one Wikipedia reader: a passage of a cached article (wikitext, `sources/_cache/wikipedia/<Title>.wiki`,
at the revision `_meta.json` pins) read into the elements of a page, by script, so that no sentence is typed.

Every Wikipedia section builds with it (chapter 2–3 pass; it replaces 2.1's `readers.py`, 2.3's `wikitext.py`, the
readings 3.1's and 3.4's `build.py` added around that one, and the reader inside `tools/build_wikitext.py`):
2.1 through `tools/build_text.py`'s reader hook (`text_block`), 2.5 through `tools/build_wikitext.py`, and 2.3, 3.1
and 3.4, which join Wikipedia to other sources block by block, through their own `build.py` calling `block()`.

**Slices.** A block's `parts` are dicts, each one slice of the article, and each may be opened by an `<h3>` the spec
names (`h3`):
- `{'lead': True}`: what stands before the first heading;
- `{'section': name}`: from the heading `name` (any level) to the next heading of the same or a higher level;
- `{'from': heading line | None, 'to': heading line | None}`: from a heading line (inclusive; None for the top of the
  article) to another (exclusive; None for the next heading of the same or a higher level);
- `{'start': text, 'stop': text | None}`: from the line holding `start` to the line before the one holding `stop`.
Any slice may be cut before the paragraph that starts with `stop_at`, or just after the words `cut_after`.

**Elements.** Headings; paragraphs (lines joined until a blank line or another element, as MediaWiki renders them);
`*` lists; `;` definition lists (each term in bold); `:` indented lines (a quote, or a display where the spec gives
its TeX); `{|` tables; `<syntaxhighlight>` listings; one-space-indented preformatted lines (Wikipedia's pseudocode
and traces: a `<pre>` in plain text, links as their text, bold and italic dropped, a `<span style="color:…">` kept,
since its words name the colour); `<math display="block">` displays; `[[File:…]]`/`[[Image:…]]` frames, whatever
the case, with their captions (the spec's IMAGES say what stands in place of each occurrence); a template standing
alone on a line (a hatnote, a maintenance box, a transcluded table) is the page's frame and is left out, named.

**Inline.** `'''bold'''` and `''italic''` as MediaWiki pairs them; `[[target|text]]tail` as its text, or as a link
where the spec's WIKILINKS name a section of this book that carries the target (RULES, Cross-references); `[url text]`
as a link; `<code>`, `{{mono}}` and inline `<syntaxhighlight>` as code; `<math>` as `$…$`; `<sub>`, `<sup>`; the
templates `mvar`, `math`, `=`, `nowrap`, `lang`, `IPA`, `ISBN`, `dead link`, `slink` ("Article § Section"), `harvtxt`;
`Anchor` and `harv` left out. Any other template stops the build, naming it, unless the spec's DROP_TEMPLATES
leave it out or its CITE_TEMPLATES give the words Wikipedia prints for it.

**Notes** (the book's rule, RULES.md "Wikipedia's citations"). Every citation the passage stands on (`<ref>…</ref>`,
`<ref name=… />` resolved over the whole article, `{{r|…}}` with its `{{rp|…}}`, `{{sfn}}`/`{{sfnp}}`) is a book
footnote in Wikipedia's words, its template set as Wikipedia's citation styles print it (`cite …` as CS1,
`citation` as CS2). The notes are numbered in the order their markers stand on the page, 1, 2, … across the
page's Wikipedia blocks; a named citation used again keeps its number and is a second note, so every note has
one marker. An article's own explanatory notes (`<ref group="note">`, `<ref group="nb" name=…/>` defined in its
reflist) are book footnotes labelled as Wikipedia labels them, "note 1", "nb 1", numbered per group in page order.
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(HERE)
CACHE = os.path.join(BOOK, 'sources', '_cache', 'wikipedia')
HEAD = re.compile(r'^(={2,6})\s*(.*?)\s*\1\s*$')
FRAME = re.compile(r'^\s*\[\[(?:[Ff]ile|[Ii]mage):([^|\]]+)(?:\|(.*))?\]\]\s*$')


def esc(s):
    return html.escape(s, quote=False)


def heading_level(line):
    m = HEAD.match(line.strip())
    return (len(m.group(1)), m.group(2)) if m else None


def strip_comments(t):
    return re.sub(r'<!--.*?-->', '', t, flags=re.S)


# ---------------------------------------------------------------- templates

def template_end(s, i):
    """s[i:i+2] is '{{': the index just past its matching '}}'."""
    depth, j = 0, i
    while j < len(s):
        if s.startswith('{{', j):
            depth += 1
            j += 2
            continue
        if s.startswith('}}', j):
            depth -= 1
            j += 2
            if depth == 0:
                return j
            continue
        j += 1
    raise SystemExit('wikitext: unbalanced template at ' + s[i:i + 60])


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


def params(body):
    """A template's name and its parameters ({name: value}, positional as '1', '2' …). CS1's aliases
    `author-lastN`/`author-firstN` are read as `lastN`/`firstN`."""
    parts = split_args(body)
    name, out, pos = parts[0].strip(), {}, 0
    for p in parts[1:]:
        m = re.match(r'\s*([\w-]+)\s*=(.*)$', p, re.S)
        if m:
            k = m.group(1).lower()
            k = re.sub(r'^author-(last|first)(\d*)$', r'\1\2', k)
            out[k] = m.group(2).strip()
        else:
            pos += 1
            out[str(pos)] = p.strip()
    return name, out


# ---------------------------------------------------------------- the article

class Article:
    """A cached article: its text without comments, its named citations and its explanatory notes by name."""

    def __init__(self, file):
        path = file if os.path.isabs(file) else os.path.join(CACHE, file)
        if not os.path.exists(path):
            path = os.path.join(BOOK, file)
        self.path = path
        self.raw = open(path, encoding='utf-8').read()
        self.text = strip_comments(self.raw)
        self.refs, self.groups = {}, {}
        for m in re.finditer(r'<ref(\s[^>]*?)(?<!/)>(.*?)</ref>', self.text, re.S):
            a = attrs(m.group(1))
            if a.get('name') and a.get('group'):
                self.groups.setdefault((a['group'], a['name']), m.group(2).strip())
            elif a.get('name'):
                self.refs.setdefault(a['name'], m.group(2).strip())


def attrs(s):
    return {k.lower(): (v1 or v2).strip() for k, v1, v2 in re.findall(r'(\w+)\s*=\s*(?:"([^"]*)"|([^\s"/>]+))', s or '')}


# ---------------------------------------------------------------- slicing

def _lead(lines):
    out = []
    for l in lines:
        if heading_level(l):
            break
        out.append(l)
    return out


def _section(lines, name):
    for i, l in enumerate(lines):
        h = heading_level(l)
        if h and h[1] == name:
            out = []
            for m in lines[i + 1:]:
                hh = heading_level(m)
                if hh and hh[0] <= h[0]:
                    break
                out.append(m)
            return out
    raise SystemExit(f'wikitext: no section {name!r}')


def _between(lines, start, stop):
    i0 = 0 if start is None else next((i for i, l in enumerate(lines) if l.strip() == start), None)
    if i0 is None:
        raise SystemExit(f'wikitext: no heading line {start!r}')
    if stop is not None:
        i1 = next((i for i, l in enumerate(lines) if i > i0 and l.strip() == stop), None)
        if i1 is None:
            raise SystemExit(f'wikitext: no heading line {stop!r} after {start!r}')
    else:
        lv = heading_level(lines[i0])[0] if start is not None else None
        i1 = next((i for i, l in enumerate(lines) if i > i0 and heading_level(l) and (lv is None or heading_level(l)[0] <= lv)), len(lines))
    return lines[i0:i1]


def _span(text, start, stop):
    a = text.index(start)
    a = text.rfind('\n', 0, a) + 1
    b = text.index(stop, a + 1) if stop else len(text)
    b = text.rfind('\n', 0, b) + 1
    return text[a:b].split('\n')


def part_lines(article, part):
    """A part's lines, and how source.md writes it (the slice as the article prints it)."""
    lines = article.text.split('\n')
    if part.get('lead'):
        out, md_head = _lead(lines), ''
    elif 'section' in part:
        out, md_head = _section(lines, part['section']), f'== {part["section"]} ==\n'
    elif 'start' in part:
        out, md_head = _span(article.text, part['start'], part.get('stop')), ''
    else:
        out, md_head = _between(lines, part.get('from'), part.get('to')), ''
    if part.get('cut_after'):
        k = next((i for i, l in enumerate(out) if part['cut_after'] in l), None)
        if k is None:
            raise SystemExit(f'wikitext: cut_after {part["cut_after"]!r} not in the passage')
        out = out[:k] + [out[k][:out[k].index(part['cut_after']) + len(part['cut_after'])]]
    if part.get('stop_at'):
        k = next((i for i, l in enumerate(out) if l.startswith(part['stop_at'])), None)
        if k is None:
            raise SystemExit(f'wikitext: stop_at {part["stop_at"]!r} not in the passage')
        out = out[:k]
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()
    return out, md_head + '\n'.join(out)


# ---------------------------------------------------------------- citations

def _plain(s):
    """A citation field: links to their text, italics and bold dropped."""
    s = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', s)
    s = re.sub(r"'''?", '', s)
    return html.unescape(s.replace('&sect;', '§'))


def _authors(p):
    names = []
    for k in [''] + [str(i) for i in range(1, 10)]:
        if k == '1' and 'last' in p and 'last1' not in p:
            continue
        last = p.get('last' + k) or p.get('author' + k)
        if not last:
            continue
        first = p.get('first' + k)
        names.append(f'{last}, {first}' if first else last)
    return '; '.join(_plain(x) for x in names)


def harv_names(args):
    """{{harvtxt|A|B|C|1993}} → the authors as Wikipedia joins them, the year, and `loc`."""
    pos = [a.strip() for a in args if '=' not in a]
    kv = dict((k.strip(), v.strip()) for k, v in (a.split('=', 1) for a in args if '=' in a))
    names, year = pos[:-1], pos[-1]
    if len(names) == 1:
        who = names[0]
    elif len(names) == 2:
        who = f'{names[0]} & {names[1]}'
    elif len(names) == 3:
        who = f'{names[0]}, {names[1]} & {names[2]}'
    else:
        who = f'{names[0]} et al.'
    loc = kv.get('loc') or (f'p. {kv["p"]}' if kv.get('p') else '') or (f'pp. {kv["pp"]}' if kv.get('pp') else '')
    return who, year, loc


def cite(name, p):
    """A citation template as Wikipedia prints it: `cite …` in CS1 (fields in CS1's order), `citation` in CS2."""
    kind = name.lower().strip()
    a = _authors(p)
    date = p.get('date') or p.get('year') or ''
    title = _plain(p.get('title', ''))
    url = p.get('url')
    bits = []
    if kind == 'citation':
        bits.append(esc(a) + (f' ({esc(date)})' if date else ''))
        if p.get('contribution'):
            bits.append(f'“{esc(_plain(p["contribution"]))}”')
        tt = f'<em>{esc(title)}</em>'
        bits.append(f'<a href="{html.escape(url)}">{tt}</a>' if url else tt)
        if p.get('publisher'):
            bits.append(esc((_plain(p['location']) + ': ' if p.get('location') else '') + _plain(p['publisher'])))
        if p.get('page'):
            bits.append(esc(f'p. {p["page"]}'))
        if p.get('pages'):
            bits.append(esc(f'pp. {p["pages"]}'))
        return ', '.join(b for b in bits if b)     # CS2 sets no full stop of its own
    head = a + (f' ({date})' if a and date else '')
    if head:
        bits.append(esc(head) + '.')
    if kind in ('cite web', 'cite journal', 'cite arxiv', 'cite conference', 'cite news'):
        tt = f'“{esc(title)}”'
    else:
        tt = f'<em>{esc(title)}</em>'
    ed = f' ({esc(_plain(p["edition"]))} ed.)' if p.get('edition') else ''
    bits.append((f'<a href="{html.escape(url)}">{tt}</a>' if url else tt) + ed + '.')
    if not a and date:
        bits.append(esc(date) + '.')
    work = p.get('work') or p.get('journal') or p.get('website') or p.get('conference') or p.get('book-title')
    if work:
        bits.append(f'<em>{esc(_plain(work))}</em>.')
    if p.get('series'):
        bits.append(esc(_plain(p['series'])) + '.')
    if p.get('volume'):
        if kind in ('cite book', 'cite conference'):
            bits.append(esc(f'Vol. {p["volume"]}') + '.')
        else:
            v = p['volume'] + (f' ({p["issue"]})' if p.get('issue') else '') + (f': {p["pages"]}' if p.get('pages') else '')
            bits.append(esc(v) + '.')
    if p.get('location') and p.get('publisher'):
        bits.append(esc(f'{_plain(p["location"])}: {_plain(p["publisher"])}') + '.')
    elif p.get('publisher'):
        bits.append(esc(_plain(p['publisher'])) + '.')
    if p.get('chapter') or p.get('section'):
        bits.append(esc(_plain(p.get('chapter') or p.get('section'))) + '.')
    if p.get('pages') and not (kind == 'cite journal' and p.get('volume')):
        bits.append(esc('pp. ' + p['pages']) + '.')
    if p.get('page'):
        bits.append(esc('p. ' + re.sub(r'\[(\S+)\s+([^\]]+)\]', r'\2', p['page'])) + '.')
    if kind == 'cite arxiv' and p.get('eprint'):
        bits.append(esc(f'arXiv:{p["eprint"]}' + (f' [{p["class"]}]' if p.get('class') else '')) + '.')
    for k, lab in (('doi', 'doi:'), ('isbn', 'ISBN '), ('issn', 'ISSN '), ('s2cid', 'S2CID ')):
        if p.get(k):
            bits.append(esc(f'{lab}{p[k]}') + '.')
    if p.get('archive-url'):
        state = 'Archived from the original' if p.get('url-status') == 'dead' else 'Archived'
        bits.append(f'<a href="{html.escape(p["archive-url"])}">{state}</a>' + (esc(f' on {p["archive-date"]}') if p.get('archive-date') else '') + '.')
    if p.get('access-date'):
        bits.append(esc(f'Retrieved {p["access-date"]}') + '.')
    if p.get('quote'):
        bits.append(esc(f'“{_plain(p["quote"])}”'))
    return ' '.join(bits)


# ---------------------------------------------------------------- inline

class Ctx:
    """What the inline reader needs: the article (named citations and notes), the spec's WIKILINKS, CITE_TEMPLATES and
    DROP_TEMPLATES, and the log of what was left out."""

    def __init__(self, article, spec=None, log=None):
        spec = spec or {}
        self.article = article
        self.links = spec.get('WIKILINKS', {})
        self.cite_templates = spec.get('CITE_TEMPLATES', {})
        self.drop = set(t.lower() for t in spec.get('DROP_TEMPLATES', ()))
        self.log = log if log is not None else []


def quotes(s):
    """MediaWiki's '' and ''' (and ''''') as <em> and <strong>, in one pass over the run."""
    parts = re.split(r"('{2,5})", s)
    out, em, strong = [], False, False
    for p in parts:
        if re.fullmatch(r"'{2,5}", p):
            n = len(p)
            if n == 5:
                out.append('</strong>' if strong else '<strong>')
                strong = not strong
                out.append('</em>' if em else '<em>')
                em = not em
            elif n == 3:
                out.append('</strong>' if strong else '<strong>')
                strong = not strong
            elif n == 2:
                out.append('</em>' if em else '<em>')
                em = not em
            else:   # four: an apostrophe and bold
                out.append("’" + ('</strong>' if strong else '<strong>'))
                strong = not strong
        else:
            out.append(p)
    if em:
        out.append('</em>')
    if strong:
        out.append('</strong>')
    return ''.join(out)


def _refs(s, ctx, notes):
    """Each footnote marker of s held as \\x01k\\x01, its note appended to notes: {group, name, html}."""
    out, i = [], 0
    pat = re.compile(r'<ref(\s[^>]*?)?(/>|>)', re.S)

    def mark(group, name, words):
        if notes is None:
            return ''
        notes.append({'group': group, 'name': name, 'html': words})
        return f'\x01{len(notes) - 1}\x01'
    while True:
        m = pat.search(s, i)
        if not m:
            out.append(s[i:])
            break
        out.append(s[i:m.start()])
        a = attrs(m.group(1))
        if m.group(2) == '>':
            close = s.find('</ref>', m.end())
            if close < 0:
                raise SystemExit('wikitext: a <ref> without its </ref>: ' + s[m.start():m.start() + 120])
            body, i = s[m.end():close], close + len('</ref>')
        else:
            body, i = None, m.end()
        g, n = a.get('group'), a.get('name')
        if g:
            body = body if body is not None else ctx.article.groups[(g, n)]
            out.append(mark(g, n, inline(body, ctx)))
        else:
            body = body if body is not None else ctx.article.refs[n]
            out.append(mark(None, n, ref_html(body, ctx)))
    s = ''.join(out)

    def r(m):
        name, page = m.group(1).strip(), m.group(2)
        words = ref_html(ctx.article.refs[name], ctx)
        return mark(None, name + (f'@{page}' if page else ''), words + (f' p. {esc(page)}.' if page else ''))
    s = re.sub(r'\{\{r\|([^}|]+)\}\}(?:\{\{rp\|([^}]+)\}\})?', r, s)

    def sfn(m):
        who, year, loc = harv_names(split_args(m.group(2))[1:])
        return mark(None, None, esc(f'{who} ({year}){", " + loc if loc else ""}.'))
    return re.sub(r'\{\{(sfnp?)(\|[^{}]*)\}\}', sfn, s, flags=re.I)


def ref_html(body, ctx):
    """The words of a citation: its templates as Wikipedia prints them, the rest as text."""
    return inline(body.strip(), ctx).strip()


def inline(s, ctx, notes=None):
    """A run of wikitext to HTML. With `notes` (a list), footnote markers are held as \\x01k\\x01 and their notes
    appended; without, they are dropped."""
    keep = []

    def hold(h):
        keep.append(h)
        return f'\x00{len(keep) - 1}\x00'
    s = _refs(s, ctx, notes)
    s = re.sub(r'\x01(\d+)\x01', lambda m: hold(m.group(0)), s)

    def code(text):
        text = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', text)
        text = re.sub(r"'{2,5}", '', text)
        return hold('<code>' + esc(html.unescape(text)) + '</code>')
    s = re.sub(r'<syntaxhighlight[^>]*\binline\b[^>]*>(.*?)</syntaxhighlight>', lambda m: code(m.group(1)), s, flags=re.S)
    s = re.sub(r'<code>(.*?)</code>', lambda m: code(m.group(1)), s, flags=re.S)
    s = re.sub(r'<math>(.*?)</math>', lambda m: hold('$' + esc(' '.join(m.group(1).split())) + '$'), s, flags=re.S)
    # templates, outermost first, their arguments read in turn
    while True:
        j = s.find('{{')
        if j < 0:
            break
        e = template_end(s, j)
        body = s[j + 2:e - 2]
        args = split_args(body)
        name = args[0].strip()
        low = name.lower()
        if low == 'mvar':
            r = '<em>' + inline(args[1], ctx) + '</em>'
        elif low == 'mono':
            r = '<code>' + inline(args[1], ctx) + '</code>'
        elif low in ('math', 'nowrap'):
            r = inline(args[1], ctx)
        elif low == 'lang':
            r = inline(args[-1], ctx)
        elif low == '=':
            r = '='
        elif low == 'ipa':
            r = esc(args[-1])
        elif low == 'isbn':
            r = esc('ISBN ' + args[1])
        elif low == 'dead link':
            r = ' [dead link]'
        elif low == 'slink':
            r = f'{inline(args[1], ctx)} § {inline(args[2], ctx)}'
        elif low == 'harvtxt':
            who, year, _ = harv_names(args[1:])
            r = esc(f'{who} ({year})')
        elif low.startswith('cite ') or low == 'citation':
            r = cite(*params(body))
        elif name in ctx.cite_templates:
            r = ctx.cite_templates[name]
        elif low in ('anchor', 'harv'):
            r = ''
        elif low in ctx.drop:
            ctx.log.append(name)
            r = ''
        else:
            raise SystemExit(f'wikitext: no reading for template {{{{{name}}}}}')
        s = s[:j] + hold(r) + s[e:]

    def link(m):
        target, _, text = m.group(1).partition('|')
        text = (text or target) + m.group(2)
        t = target.strip()
        href = ctx.links.get(t) or ctx.links.get(t[:1].upper() + t[1:])
        inner = quotes(esc(html.unescape(text)))
        return hold(f'<a href="{href}">{inner}</a>') if href else hold(inner)
    s = re.sub(r'\[\[(?![Ff]ile:|[Ii]mage:)([^\[\]]*)\]\]([a-z]*)', link, s)
    s = re.sub(r'\[(https?://[^\s\]]+)\s+([^\]]+)\]', lambda m: hold(f'<a href="{html.escape(m.group(1), quote=True)}">') + m.group(2) + hold('</a>'), s)
    s = re.sub(r'</?(?:sub|sup)>', lambda m: hold(m.group(0)), s)
    s = quotes(esc(html.unescape(s)))
    while '\x00' in s:
        s = re.sub(r'\x00(\d+)\x00', lambda m: keep[int(m.group(1))], s)
    return re.sub(r'[ \t]+', ' ', s).strip()


def pre_text(lines):
    """Preformatted lines: one leading space dropped, citations dropped, links as their text, bold and italic
    dropped, colour spans kept."""
    out = []
    for l in lines:
        l = l[1:] if l.startswith(' ') else l
        l = re.sub(r'<ref[^>/]*/>', '', l)
        l = re.sub(r'<ref[^>]*>.*?</ref>', '', l)
        l = re.sub(r'\[\[(?:[^\[\]|]*\|)?([^\[\]]*)\]\]', r'\1', l)
        spans = []

        def hold(m):
            spans.append(m.group(0))
            return f'\x00{len(spans) - 1}\x00'
        l = re.sub(r'<span style="color:\w+">|</span>', hold, l)
        l = re.sub(r"'{2,5}", '', l)
        l = esc(html.unescape(l))
        l = re.sub(r'\x00(\d+)\x00', lambda m: spans[int(m.group(1))], l)
        out.append(l.rstrip())
    while out and not out[-1].strip():
        out.pop()
    return '\n'.join(out)


# ---------------------------------------------------------------- elements

def _starts_element(l):
    s = l.strip()
    return (not s or l.startswith(' ') or s[0] in '*;:' or s.startswith('{|') or heading_level(l) or FRAME.match(l)
            or s.startswith('<syntaxhighlight') and 'inline' not in s.split('>')[0]
            or s.startswith('<math display="block">')
            or re.match(r'^\{\{', s) and s.endswith('}}') and template_end(s, 0) == len(s))


def _open(t):
    """Whether a run ends inside a template or a citation (MediaWiki reads those before it splits paragraphs, so
    a multi-line `<ref>{{citation …}}</ref>` stays in its paragraph)."""
    return t.count('{{') > t.count('}}') or len(re.findall(r'<ref(?:\s[^>]*?)?(?<!/)>', t)) > t.count('</ref>')


def elements(lines, ctx):
    """A slice's lines to elements, each a dict with `kind`: heading (level, text, html), image (file, caption,
    caption_html), template (name), code (lang, text), table (html), list (items: [html with markers], notes,
    wiki), indent (html, notes, wiki), display (tex), pre (html), p (html, notes, wiki)."""
    els, i, n = [], 0, len(lines)
    while i < n:
        l = lines[i]
        s = l.strip()
        if not s:
            i += 1
            continue
        h = heading_level(l)
        if h:
            els.append({'kind': 'heading', 'level': h[0], 'text': h[1], 'html': inline(h[1], ctx)})
            i += 1
            continue
        m = FRAME.match(l)
        if m:
            cap = split_args(m.group(2) or '')[-1].strip()
            els.append({'kind': 'image', 'file': m.group(1).strip(), 'caption': cap, 'caption_html': inline(cap, ctx)})
            i += 1
            continue
        if re.match(r'^\{\{', s) and s.endswith('}}') and template_end(s, 0) == len(s):
            name = re.match(r'^\{\{([^|}]*)', s).group(1).strip()
            ctx.log.append(name)
            els.append({'kind': 'template', 'name': name})
            i += 1
            continue
        if s.startswith('<syntaxhighlight') and 'inline' not in s.split('>')[0]:
            lang = re.search(r'lang="?(\w+)', s.split('>')[0])
            body, first = [], re.sub(r'^\s*<syntaxhighlight[^>]*>', '', l)
            if first.strip():
                body.append(first)
            j = i + 1
            if '</syntaxhighlight>' in first:
                body, j = [first.split('</syntaxhighlight>')[0]], i
            else:
                while '</syntaxhighlight>' not in lines[j]:
                    body.append(lines[j])
                    j += 1
                last = lines[j].split('</syntaxhighlight>')[0]
                if last.strip():
                    body.append(last)
            els.append({'kind': 'code', 'lang': lang.group(1).lower() if lang else '', 'text': '\n'.join(body).strip('\n')})
            i = j + 1
            continue
        if s.startswith('<math display="block">'):
            acc = [l]
            while '</math>' not in lines[i] and i + 1 < n:
                i += 1
                acc.append(lines[i])
            i += 1
            tex = re.sub(r'^\s*<math display="block">|</math>\s*$', '', '\n'.join(acc).strip(), flags=re.S).strip()
            els.append({'kind': 'display', 'tex': tex})
            continue
        if re.match(r'^:?\{\|', s):
            rows, cur, j = [], None, i + 1
            while not lines[j].strip().startswith('|}'):
                r = lines[j].strip()
                if r.startswith('|-'):
                    cur = []
                    rows.append(cur)
                elif r.startswith('!') or r.startswith('|'):
                    if cur is None:
                        cur = []
                        rows.append(cur)
                    head = r.startswith('!')
                    for c in re.split(r'\s*(?:!!|\|\|)\s*', r[1:]):
                        cur.append((head, c.strip()))
                j += 1
            body = ''.join('<tr>' + ''.join((f'<th>{inline(c, ctx)}</th>' if hd else f'<td>{inline(c, ctx)}</td>') for hd, c in row) + '</tr>'
                           for row in rows if row)
            els.append({'kind': 'table', 'html': f'<table>{body}</table>'})
            i = j + 1
            continue
        if l.startswith(' '):
            acc = []
            while i < n and lines[i].startswith(' '):
                acc.append(lines[i])
                i += 1
            els.append({'kind': 'pre', 'html': pre_text(acc)})
            continue
        if s.startswith(';'):
            items, notes, wiki = [], [], []
            while i < n and lines[i].strip().startswith(';'):
                term, _, rest = lines[i].strip()[1:].partition(':')
                j, more = i + 1, []
                while j < n and lines[j].strip() and not re.match(r'^[;*:=]', lines[j].strip()):
                    more.append(lines[j].strip())
                    j += 1
                d = ' '.join([rest.strip()] + more)
                items.append(f'<strong>{inline(term.strip(), ctx, notes)}</strong> {inline(d, ctx, notes)}')
                wiki.append(lines[i].strip() + ' ' + ' '.join(more))
                i = j
            els.append({'kind': 'list', 'items': items, 'notes': notes, 'wiki': '\n'.join(wiki)})
            continue
        if s.startswith('*'):
            items, notes, wiki = [], [], []
            while i < n and lines[i].strip().startswith('*'):
                t = lines[i].strip()[1:].strip()
                items.append(inline(t, ctx, notes))
                wiki.append(t)
                i += 1
            els.append({'kind': 'list', 'items': items, 'notes': notes, 'wiki': '\n'.join(wiki)})
            continue
        if s.startswith(':'):
            notes = []
            t = s[1:].strip()
            els.append({'kind': 'indent', 'html': inline(t, ctx, notes), 'notes': notes, 'wiki': t})
            i += 1
            continue
        acc = []
        while i < n and (not _starts_element(lines[i]) or acc and _open(' '.join(acc))):
            acc.append(lines[i].strip())
            i += 1
        if not acc:     # a line no element reads (a stray table row): text, so nothing is lost silently
            acc.append(lines[i].strip())
            i += 1
        text = ' '.join(acc)
        disp = None
        m = re.search(r'<math display="block">(.*?)</math>\s*$', text, re.S)
        if m:
            disp, text = m.group(1).strip(), text[:m.start()].rstrip()
        notes = []
        els.append({'kind': 'p', 'html': inline(text, ctx, notes), 'notes': notes, 'wiki': text})
        if disp:
            els.append({'kind': 'display', 'tex': disp})
    return els


# ---------------------------------------------------------------- notes, numbered on the page

class Notes:
    """A page's Wikipedia notes: citations numbered 1, 2, … in the order their markers stand, a named one keeping
    its number where it is used again (a second note, so every note has one marker); explanatory notes labelled
    by their group ("note 1", "nb 1"), numbered per group."""

    def __init__(self):
        self.rows, self.num, self.group_num, self.ids = [], {}, {}, set()

    def _id(self, base):
        nid, k = base, 2
        while nid in self.ids:
            nid = f'{base}-{k}'
            k += 1
        self.ids.add(nid)
        return nid

    def place(self, h, notes, prefix, source='wikipedia'):
        """h with each \\x01k\\x01 set as its note's marker, and the note's row recorded."""
        def one(m):
            note = notes[int(m.group(1))]
            g, name = note['group'], note['name']
            if g:
                key = (g, name or f'anon-{len(self.rows)}')
                per = self.group_num.setdefault(g, {})
                per.setdefault(key, len(per) + 1)
                number, base = f'{g} {per[key]}', f'{prefix}-{g}-{per[key]}'
            else:
                key = name or f'anon-{len(self.rows)}'
                self.num.setdefault(key, len(self.num) + 1)
                number, base = str(self.num[key]), f'{prefix}-{self.num[key]}'
            nid = self._id(base)
            self.rows.append({'id': nid, 'kind': 'book', 'number': number, 'html': note['html'], 'source': source})
            return f'<sup class="fn" data-note="{nid}"></sup>'
        return re.sub(r'\x01(\d+)\x01', one, h)


# ---------------------------------------------------------------- a block

def code_set(source_code, variants, ai, lang='cpp'):
    """A listing as a four-language code set: the source's listing verbatim under `lang`, the spec's variants
    of the other languages AI-marked."""
    pres = []
    for la in ('python', 'java', 'cpp', 'javascript'):
        code = source_code if la == lang else variants.get(la)
        if code is None:
            continue
        mark = '' if la == lang else f' data-ai="{ai}"'
        pres.append(f'<pre data-lang="{la}"{mark}><code>{esc(code.strip(chr(10)))}</code></pre>')
    no_py = '' if 'python' in variants or lang == 'python' else f' data-no-python="{html.escape(variants.get("_no_python", ""), quote=True)}"'
    return f'<div class="code-set"{no_py}>\n' + '\n'.join(pres) + '\n</div>'


def block(b, spec, notes, log, html_of=None, state=None):
    """A Wikipedia block of the spec as (source.md text, [html, …], captions): its <h2>, then each part's elements.
    `html_of(key)` gives a figure's HTML (default spec['HTML']); `state` carries the image occurrences and the AT
    rows placed across blocks. Block keys: file, h2, parts, heading_shift (default 1), heading_cap (default 4),
    headings ({text: level | None}), drop_first_heading, note_prefix (default 'wp-<id>'), displays ({n: TeX} for the
    n-th `:` line). Spec rows: IMAGES {file: [key | None, …]} per occurrence; CODE [(piece, key | {lang: code})];
    AT [(block id, piece of an element's wikitext, key)]; REPLACE [(block id, piece of a display's TeX, key)]: a
    display (an `align` set as `aligned`) replaced by a figure or a derivation; WIKILINKS, CITE_TEMPLATES, DROP_TEMPLATES (see Ctx)."""
    html_of = html_of or (lambda k: spec['HTML'][k])
    state = state if state is not None else {}
    seen_img = state.setdefault('images', {})
    placed = state.setdefault('placed', set())
    used_code = state.setdefault('code', set())
    captions = state.setdefault('captions', {})
    state.setdefault('blocks', set()).add(b['id'])
    art = state.setdefault('articles', {})
    a = art.setdefault(b['file'], Article(b['file']))
    ctx = Ctx(a, spec, log)
    prefix = b.get('note_prefix') or f'wp-{b["id"]}'
    out, md = [f'<h2>{esc(b["h2"])}</h2>'], []
    first_heading, disp_n = True, 0
    after = [(j, r) for j, r in enumerate(spec.get('AT', [])) if r[0] == b['id']]

    def place(anchor):
        for j, (_, piece, key) in after:
            if j not in placed and piece in anchor:
                out.append(html_of(key))
                placed.add(j)
    for part in b['parts']:
        lines, m = part_lines(a, part)
        md.append(m)
        if part.get('h3'):
            out.append(f'<h3>{esc(part["h3"])}</h3>')
        for e in elements(lines, ctx):
            k = e['kind']
            if k == 'heading':
                if first_heading and b.get('drop_first_heading'):
                    first_heading = False
                    continue
                first_heading = False
                lvl = b.get('headings', {}).get(e['text'], min(b.get('heading_cap', 4), e['level'] + b.get('heading_shift', 1)))
                if lvl is not None:
                    out.append(f'<h{lvl}>{e["html"]}</h{lvl}>')
                continue
            first_heading = False
            if k == 'template':
                continue
            if k == 'image':
                cnt = seen_img.get(e['file'], 0)
                seen_img[e['file']] = cnt + 1
                captions.setdefault(e['file'], {'html': e['caption_html'], 'text': html.unescape(re.sub(r'<[^>]+>', '', e['caption_html']))})
                keys = spec.get('IMAGES', {}).get(e['file'])
                if keys is None or cnt >= len(keys):
                    raise SystemExit(f'{b["id"]}: no IMAGES decision for {e["file"]} (occurrence {cnt + 1})')
                if keys[cnt]:
                    out.append(html_of(keys[cnt]))
                continue
            if k == 'code':
                hit = next(((j, c) for j, c in enumerate(spec.get('CODE', [])) if c[0] in e['text']), None)
                if hit is None:
                    out.append('<pre>' + esc(e['text']).replace('$', '&#36;') + '</pre>')
                else:
                    used_code.add(hit[0])
                    what = hit[1][1]
                    out.append(html_of(what) if isinstance(what, str) else code_set(e['text'], what, spec.get('AI', ''), e['lang'] if e['lang'] in ('python', 'java', 'javascript') else 'cpp'))
                place(e['text'])
                continue
            if k == 'table':
                out.append(e['html'])
                continue
            if k == 'pre':
                out.append(f'<pre>{e["html"]}</pre>')
                place(html.unescape(e['html']))
                continue
            if k == 'display':
                r = next((r for r in spec.get('REPLACE', []) if r[0] == b['id'] and r[1] in e['tex']), None)
                if r:
                    out.append(html_of(r[2]))
                    placed.add(('REPLACE', r[2]))
                    continue
                tex = e['tex'].replace('\\begin{align}', '\\begin{aligned}').replace('\\end{align}', '\\end{aligned}')
                out.append(f'$${esc(tex)}$$')
                place(e['tex'])
                continue
            if k == 'list':
                out.append('<ul>' + ''.join(f'<li>{notes.place(it, e["notes"], prefix)}</li>' for it in e['items']) + '</ul>')
                place(e['wiki'])
                continue
            if k == 'indent':
                tex = b.get('displays', {}).get(disp_n)
                disp_n += 1
                out.append(f'$${tex}$$' if tex is not None else f'<blockquote><p>{notes.place(e["html"], e["notes"], prefix)}</p></blockquote>')
                place(e['wiki'])
                continue
            out.append(f'<p>{notes.place(e["html"], e["notes"], prefix)}</p>')
            place(e['wiki'])
    return '\n\n'.join(md), out


def unplaced(spec, state):
    """The AT rows never placed and the CODE rows never matched, as messages."""
    ours = state.get('blocks', set())
    msgs = [f'AT never placed: {r!r}' for j, r in enumerate(spec.get('AT', [])) if r[0] in ours and j not in state.get('placed', set())]
    msgs += [f'REPLACE never placed: {r!r}' for r in spec.get('REPLACE', []) if r[0] in ours and ('REPLACE', r[2]) not in state.get('placed', set())]
    msgs += [f'CODE never matched: {c[0]!r}' for j, c in enumerate(spec.get('CODE', [])) if j not in state.get('code', set())]
    return msgs


def text_block(b, spec, book):
    """tools/build_text.py's reader hook (2.1): the block's HTML and Markdown parts, its notes added to the spec's
    `_latex_notes` (with Markdown), numbered across the page's Wikipedia blocks."""
    notes = spec.setdefault('_wiki_notes', Notes())
    state = spec.setdefault('_wiki_state', {})
    log = spec.setdefault('_wiki_log', [])
    before = len(notes.rows)
    md, hs = block(b, spec, notes, log, state=state)
    for r in notes.rows[before:]:
        spec.setdefault('_latex_notes', []).append(dict(r, md=html.unescape(re.sub(r'<[^>]+>', '', r['html']))))
    fixes = spec.get('WIKI_FIXES', [])
    used = spec.setdefault('_wiki_fixes_used', set())
    for i, h in enumerate(hs):
        for k, (old, new, why) in enumerate(fixes):
            if old in h:
                hs[i] = hs[i].replace(old, new)
                used.add(k)
    return hs, [md]
