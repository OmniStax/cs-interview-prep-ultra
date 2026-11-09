"""Readers for section 2.1's two source formats, called by tools/build_text.py through a block's `reader`
(a function of the block, the spec and the book's folder, returning the block's HTML and Markdown parts).

- `wikitext_block`: a passage of a cached Wikipedia article (`sources/_cache/wikipedia/<file>.wiki`), from
  the line holding `start` to the line before the one holding `stop`. It reads what these passages hold:
  headings, paragraphs (a single newline continues the paragraph, as MediaWiki renders it), `;` definition
  lists, `*` lists, `:` indented lines, wikitables, `<syntaxhighlight>` listings, image lines, links (their
  text kept, the link dropped), bold and italic, `<code>`, `<sub>`, `<sup>`, the inline templates `nowrap`,
  `mono` and `ISBN`, and `<ref>` citations. The citations become book footnotes under the numbers the
  article prints them under: every `<ref>` of the whole article is numbered in order of first use, a named
  one keeping its number where it is used again, as MediaWiki's Cite numbers them. A citation template is set
  as one line from its fields, in the order MediaWiki's citation style prints them.
- `ods_block`: a passage of ODS's LaTeX through tools/read_latex.py (its ODS dialect sets #code# as the
  pseudocode edition does, METHOD decision 20), with the one thing that reader does not do for this passage
  done first: an eqnarray* becomes an aligned display.

Nothing here is a word of the sources; everything on the page is read out of the cache.
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'tools')
sys.path.insert(0, TOOLS)
import read_latex  # noqa: E402


# ================================================================ Wikipedia wikitext

def _strip_comments(t):
    return re.sub(r'<!--.*?-->', '', t, flags=re.S)


def _template_end(s, i):
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
    raise ValueError('unbalanced template at ' + s[i:i + 60])


def _split_params(body):
    """A template's body to its name and its parameters ({name: value}, positional as '1', '2' …)."""
    parts, depth, cur, k = [], 0, [], 0
    while k < len(body):
        if body.startswith('{{', k) or body.startswith('[[', k):
            depth += 1
            cur.append(body[k:k + 2])
            k += 2
            continue
        if body.startswith('}}', k) or body.startswith(']]', k):
            depth -= 1
            cur.append(body[k:k + 2])
            k += 2
            continue
        if body[k] == '|' and depth == 0:
            parts.append(''.join(cur))
            cur = []
            k += 1
            continue
        cur.append(body[k])
        k += 1
    parts.append(''.join(cur))
    name = parts[0].strip()
    params, pos = {}, 0
    for p in parts[1:]:
        m = re.match(r'\s*([\w-]+)\s*=(.*)$', p, re.S)
        if m:
            params[m.group(1).lower()] = m.group(2).strip()
        else:
            pos += 1
            params[str(pos)] = p.strip()
    return name, params


def ref_numbers(article):
    """Every <ref> of the article, numbered as the rendered page numbers them: [(start, end, number, name,
    content)] in the order they stand. A named ref takes its number from its first use; a ref inside a
    {{efn}} note belongs to another list and is skipped."""
    t = _strip_comments(article)
    out, by_name, n = [], {}, 0
    pat = re.compile(r'<ref(\s[^>]*?)?(/>|>)', re.S)
    for m in pat.finditer(t):
        attrs = m.group(1) or ''
        if 'group' in attrs:
            continue
        nm = re.search(r'name\s*=\s*"?([^"/>]+?)"?\s*(?:/|$)', attrs.strip() + ' ')
        name = nm.group(1).strip() if nm else None
        if m.group(2) == '>':
            close = t.index('</ref>', m.end())
            content, end = t[m.end():close], close + len('</ref>')
        else:
            content, end = None, m.end()
        if name and name in by_name:
            num = by_name[name]
        else:
            n += 1
            num = n
            if name:
                by_name[name] = num
        out.append((m.start(), end, num, name, content))
    contents = {}
    for _, _, num, name, content in out:
        if content:
            contents.setdefault(num, content)
    return out, contents


# ---------------------------------------------------------------- citations

def _authors(p):
    names = []
    for k in [''] + [str(i) for i in range(1, 10)]:
        last = p.get('last' + k) or p.get('author' + k) or (p.get('last') if k == '1' and 'last1' not in p else None)
        if k == '1' and 'last' in p and 'last1' not in p:
            continue
        if not last:
            continue
        first = p.get('first' + k) or (p.get('first') if k == '' else None)
        names.append(f'{last}, {first}' if first else last)
    if not names and p.get('author'):
        names.append(p['author'])
    return '; '.join(_inline_plain(x) for x in names)


def _inline_plain(s):
    """A citation field: links to their text, italics and bold dropped."""
    s = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', s)
    s = re.sub(r"'''?", '', s)
    return s.replace('&sect;', '§').replace('&nbsp;', ' ')


def _e(s):
    return html.escape(s, quote=False)


def cite(name, p):
    """A citation template as one line, (html, text)."""
    kind = name.lower()
    a = _authors(p)
    date = p.get('date') or p.get('year') or ''
    title = _inline_plain(p.get('title', ''))
    url = p.get('url')
    bits_h, bits_t = [], []

    def add(h, t=None):
        bits_h.append(h)
        bits_t.append(t if t is not None else re.sub(r'<[^>]+>', '', h))
    head = a + (f' ({date})' if a and date else '')
    if head:
        add(_e(head) + '.')
    if kind in ('cite web', 'cite journal', 'cite arxiv'):
        tt = f'“{_e(title)}”'
        add((f'<a href="{html.escape(url)}">{tt}</a>' if url else tt) + '.', f'“{title}”.')
    else:
        tt = f'<em>{_e(title)}</em>'
        add((f'<a href="{html.escape(url)}">{tt}</a>' if url else tt) + '.', f'{title}.')
    if not a and date:
        add(_e(date) + '.')
    work = p.get('work') or p.get('journal') or p.get('website') or p.get('conference')
    if work:
        add(f'<em>{_e(_inline_plain(work))}</em>.', f'{_inline_plain(work)}.')
    if p.get('series'):
        add(_e(_inline_plain(p['series'])) + '.')
    if p.get('volume'):
        if kind in ('cite book', 'cite conference'):
            add(_e(f'Vol. {p["volume"]}') + '.')
        else:
            v = p['volume'] + (f' ({p["issue"]})' if p.get('issue') else '') + (f': {p["pages"]}' if p.get('pages') else '')
            add(_e(v) + '.')
    if p.get('location') and p.get('publisher'):
        add(_e(f'{_inline_plain(p["location"])}: {_inline_plain(p["publisher"])}') + '.')
    elif p.get('publisher'):
        add(_e(_inline_plain(p['publisher'])) + '.')
    if p.get('section'):
        add(_e(_inline_plain(p['section'])) + '.')
    if p.get('pages') and not (kind == 'cite journal' and p.get('volume')):
        add(_e('pp. ' + p['pages']) + '.')
    if p.get('page'):
        pg = re.sub(r'\[(\S+)\s+([^\]]+)\]', r'\2', p['page'])
        add(_e(f'p. {pg}') + '.')
    if kind == 'cite arxiv' and p.get('eprint'):
        add(_e(f'arXiv:{p["eprint"]}' + (f' [{p["class"]}]' if p.get('class') else '')) + '.')
    if p.get('doi'):
        add(_e(f'doi:{p["doi"]}') + '.')
    if p.get('isbn'):
        add(_e(f'ISBN {p["isbn"]}') + '.')
    if p.get('issn'):
        add(_e(f'ISSN {p["issn"]}') + '.')
    if p.get('s2cid'):
        add(_e(f'S2CID {p["s2cid"]}') + '.')
    if p.get('archive-url'):
        state = 'Archived from the original' if p.get('url-status') == 'dead' else 'Archived'
        add(f'<a href="{html.escape(p["archive-url"])}">{state}</a>' + (_e(f' on {p["archive-date"]}') if p.get('archive-date') else '') + '.',
            f'{state}' + (f' on {p["archive-date"]}' if p.get('archive-date') else '') + '.')
    if p.get('access-date'):
        add(_e(f'Retrieved {p["access-date"]}') + '.')
    if p.get('quote'):
        q = _inline_plain(p['quote'])
        add(_e(f'“{q}”'), f'“{q}”')
    return ' '.join(bits_h), ' '.join(bits_t)


# ---------------------------------------------------------------- inline wikitext

def _templates_inline(s, ctx):
    """Inline templates: nowrap's content kept, mono as code, ISBN as text, a citation set as a line, a
    maintenance tag (dead link) as the bracketed words the page prints."""
    out, i = [], 0
    while True:
        j = s.find('{{', i)
        if j < 0:
            out.append(s[i:])
            return ''.join(out)
        out.append(s[i:j])
        e = _template_end(s, j)
        name, p = _split_params(s[j + 2:e - 2])
        key = name.lower()
        if key == 'nowrap':
            out.append(_templates_inline(p['1'], ctx))
        elif key == 'mono':
            out.append('\x10' + p['1'] + '\x11')
        elif key == 'isbn':
            out.append('ISBN ' + p['1'])
        elif key == 'dead link':
            out.append(' [dead link]')
        elif key.startswith('cite'):
            h, t = cite(name, p)
            out.append('\x12' + str(len(ctx['cites'])) + '\x13')
            ctx['cites'].append((h, t))
        else:
            raise SystemExit(f'wikitext: inline template {{{{{name}}}}} not read')
        i = e


def inline(s, ctx):
    """One run of wikitext to (html, md). ctx carries the footnote markers ('refs': {pos-key: id}) and the
    citations set inside it."""
    ctx.setdefault('cites', [])
    s = _templates_inline(s, ctx)
    # code spans first, kept whole
    codes = []

    def keep(text):
        codes.append(re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', text))
        return f'\x14{len(codes) - 1}\x15'
    s = re.sub(r'<syntaxhighlight[^>]*\binline\b[^>]*>(.*?)</syntaxhighlight>', lambda m: keep(m.group(1)), s, flags=re.S)
    s = re.sub(r'<code>(.*?)</code>', lambda m: keep(m.group(1)), s, flags=re.S)
    s = re.sub(r'\x10(.*?)\x11', lambda m: keep(m.group(1)), s, flags=re.S)
    # links: [[target|text]]tail and [[target]]tail, the text kept and the tail letters joined to it
    s = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]([a-z]*)', r'\1\2', s)
    # markup that stays: <sub>, <sup>; everything else is text
    tags = []

    def tag(m):
        tags.append(m.group(0))
        return f'\x16{len(tags) - 1}\x17'
    s = re.sub(r'</?(?:sub|sup)>', tag, s)
    s = s.replace('&nbsp;', '\u00a0')
    s = html.unescape(s) if '&' in s else s
    h = html.escape(s, quote=False)
    md = s
    # bold and italic, as MediaWiki pairs them
    h = re.sub(r"'''(.+?)'''", r'<strong>\1</strong>', h)
    h = re.sub(r"''(.+?)''", r'<em>\1</em>', h)
    md = re.sub(r"'''(.+?)'''", r'**\1**', md)
    md = re.sub(r"''(.+?)''", r'*\1*', md)
    h = re.sub(r'\x16(\d+)\x17', lambda m: tags[int(m.group(1))], h)
    md = re.sub(r'\x16(\d+)\x17', lambda m: {'<sub>': '~', '</sub>': '~', '<sup>': '^', '</sup>': '^'}[tags[int(m.group(1))]], md)
    h = re.sub(r'\x14(\d+)\x15', lambda m: '<code>' + html.escape(html.unescape(codes[int(m.group(1))]), quote=False) + '</code>', h)
    md = re.sub(r'\x14(\d+)\x15', lambda m: '`' + html.unescape(codes[int(m.group(1))]) + '`', md)
    h = re.sub(r'\x12(\d+)\x13', lambda m: ctx['cites'][int(m.group(1))][0], h)
    md = re.sub(r'\x12(\d+)\x13', lambda m: ctx['cites'][int(m.group(1))][1], md)
    # footnote markers
    h = re.sub(r'\x18([\w-]+)\x19', r'<sup class="fn" data-note="\1"></sup>', h)
    md = re.sub(r'\x18[\w-]+-(\d+)(?:-\d+)?\x19', r'[^\1]', md)
    h = re.sub(r'[ \t]+', ' ', h).strip()
    md = re.sub(r'[ \t]+', ' ', md).strip()
    return h, md


# ---------------------------------------------------------------- blocks

def _read(path, start, stop):
    """The article's text from the line holding start to the line before the one holding stop, and its
    offset in the whole text (with comments removed, as ref_numbers reads it)."""
    t = _strip_comments(open(path, encoding='utf-8').read())
    a = t.index(start)
    a = t.rfind('\n', 0, a) + 1
    b = t.index(stop, a + 1) if stop else len(t)
    b = t.rfind('\n', 0, b) + 1
    return t, a, b


def wikitext_block(b, spec, book):
    """A Wikipedia passage as the block's HTML and Markdown parts, its <h2> first. Spec rows read:
    WIKI_FIGURES {(block id, file name): HTML key or ''} for the image lines; WIKI_DISPLAYS {(block id, n):
    TeX} for the n-th indented line (0-based) where the article sets a formula on it; WIKI_FIXES
    [(old, new, why)] applied to the passage's HTML."""
    path = os.path.join(book, b['file'])
    whole, a, z = _read(path, b['start'], b.get('stop'))
    refs, contents = ref_numbers(open(path, encoding='utf-8').read())
    prefix = b['note_prefix']
    notes = spec.setdefault('_latex_notes', [])
    used_ids = {n['id'] for n in notes}
    # footnote markers for the refs inside the passage: \x18id\x19 in place of each <ref …>
    text, pos = [], a
    for (s0, e0, num, name, content) in refs:
        if s0 < a or s0 >= z:
            continue
        text.append(whole[pos:s0])
        nid = f'{prefix}-{num}'
        k = 2
        while nid in used_ids:      # one marker per note: a ref used again is a note of its own, same number
            nid = f'{prefix}-{num}-{k}'
            k += 1
        used_ids.add(nid)
        body = contents.get(num)
        ctx = {}
        h, m = inline(body, ctx)
        notes.append({'id': nid, 'number': str(num), 'html': h, 'md': m, 'source': b['source']})
        text.append(f'\x18{nid}\x19')
        pos = e0
    text.append(whole[pos:z])
    src = ''.join(text)
    lines = src.split('\n')
    hs, ms = [f'<h2>{html.escape(b["h2"], quote=False)}</h2>'], [f'## {b["h2"]}']
    para, first_heading, disp_n = [], True, 0
    figs = spec.get('WIKI_FIGURES', {})
    displays = spec.get('WIKI_DISPLAYS', {})

    def flush():
        t = ' '.join(x.strip() for x in para).strip()
        para.clear()
        if t:
            h, m = inline(t, {})
            hs.append(f'<p>{h}</p>')
            ms.append(m)
    i = 0
    while i < len(lines):
        ln = lines[i]
        st = ln.strip()
        mh = re.match(r'^(={2,6})\s*(.*?)\s*\1\s*$', st)
        if mh:
            flush()
            if first_heading and b.get('drop_first_heading'):
                first_heading = False
                i += 1
                continue
            first_heading = False
            lvl = len(mh.group(1)) + b.get('heading_shift', 0)
            h, m = inline(mh.group(2), {})
            hs.append(f'<h{lvl}>{h}</h{lvl}>')
            ms.append('#' * lvl + ' ' + m)
            i += 1
            continue
        mf = re.match(r'^\[\[(?:File|Image):([^|\]]+)', st)
        if mf:
            flush()
            key = figs.get((b['id'], mf.group(1).strip()))
            if key is None:
                raise SystemExit(f'{b["id"]}: image {mf.group(1)} has no WIKI_FIGURES row')
            if key:
                hs.append(spec['HTML'][key])
                ms.append(f'[{key}]')
            i += 1
            continue
        if re.match(r'^\{\{', st) and st.endswith('}}') and _template_end(st, 0) == len(st):
            flush()     # a line-level template (a hatnote, a navigation box) is the page's frame, not the passage
            i += 1
            continue
        if st.startswith('<syntaxhighlight') and 'inline' not in st.split('>')[0]:
            flush()
            j = i
            body = []
            first = re.sub(r'^<syntaxhighlight[^>]*>', '', st)
            if first:
                body.append(first)
            j += 1
            while '</syntaxhighlight>' not in lines[j]:
                body.append(lines[j])
                j += 1
            last = lines[j].split('</syntaxhighlight>')[0]
            if last.strip():
                body.append(last)
            code = '\n'.join(body).strip('\n')
            hs.append('<pre>' + html.escape(code, quote=False).replace('$', '&#36;') + '</pre>')
            ms.append('```\n' + code + '\n```')
            i = j + 1
            continue
        if re.match(r'^:?\{\|', st):
            flush()
            rows, cur = [], None
            j = i + 1
            while not lines[j].strip().startswith('|}'):
                r = lines[j].strip()
                if r.startswith('|-'):
                    cur = []
                    rows.append(cur)
                elif r.startswith('!') or r.startswith('|'):
                    head = r.startswith('!')
                    cells = re.split(r'\s*(?:!!|\|\|)\s*', r[1:])
                    for c in cells:
                        cur.append((head, c.strip()))
                j += 1
            th = []
            for row in rows:
                if not row:
                    continue
                cells = []
                for head, c in row:
                    h, _ = inline(c, {}) if c else ('', '')
                    cells.append(f'<th>{h}</th>' if head else f'<td>{h}</td>')
                th.append('<tr>' + ''.join(cells) + '</tr>')
            hs.append('<table>' + ''.join(th) + '</table>')
            ms.append('\n'.join('| ' + ' | '.join(c for _, c in row) + ' |' for row in rows if row))
            i = j + 1
            continue
        if st.startswith(';'):
            flush()
            items = []
            while i < len(lines) and lines[i].strip().startswith(';'):
                term, _, rest = lines[i].strip()[1:].partition(':')
                # a definition may run on over the lines up to the next item
                j = i + 1
                more = []
                while j < len(lines) and lines[j].strip() and not re.match(r'^[;*:=]', lines[j].strip()):
                    more.append(lines[j].strip())
                    j += 1
                th, tm = inline(term.strip(), {})
                dh, dm = inline(' '.join([rest.strip()] + more), {})
                items.append((th, dh, tm, dm))
                i = j
            hs.append('<ul>' + ''.join(f'<li><strong>{t}</strong> {d}</li>' for t, d, _, _ in items) + '</ul>')
            ms.append('\n'.join(f'- **{t}** {d}' for _, _, t, d in items))
            continue
        if st.startswith('*'):
            flush()
            items = []
            while i < len(lines) and lines[i].strip().startswith('*'):
                items.append(inline(lines[i].strip()[1:].strip(), {}))
                i += 1
            hs.append('<ul>' + ''.join(f'<li>{h}</li>' for h, _ in items) + '</ul>')
            ms.append('\n'.join(f'- {m}' for _, m in items))
            continue
        if st.startswith(':'):
            flush()
            tex = displays.get((b['id'], disp_n))
            body = st[1:].strip()
            if tex is not None:
                hs.append(f'$${tex}$$')
                ms.append(f'$${tex}$$')
            else:
                h, m = inline(body, {})
                hs.append(f'<blockquote><p>{h}</p></blockquote>')
                ms.append('> ' + m)
            disp_n += 1
            i += 1
            continue
        if not st:
            flush()
            i += 1
            continue
        para.append(ln)
        i += 1
    flush()
    fixes = spec.get('WIKI_FIXES', [])
    used = spec.setdefault('_wiki_fixes_used', set())
    out = []
    for h in hs:
        for k, (old, new, why) in enumerate(fixes):
            if old in h:
                h = h.replace(old, new)
                used.add(k)
        out.append(h)
    return out, ms


def unused_fixes(spec):
    return [f[0] for k, f in enumerate(spec.get('WIKI_FIXES', [])) if k not in spec.get('_wiki_fixes_used', set())]


# ================================================================ ODS through tools/read_latex.py

def _eqnarray(text):
    """An eqnarray* (lhs & rel & rhs) as an align* of the same lines (lhs &rel rhs), its #code# set as
    tools/read_latex.py sets code in maths (the pseudocode edition: a call's name upright)."""
    def conv(m):
        body = re.sub(r'#([^#\n]+)#', lambda mm: read_latex.ods_pcode(mm.group(1)) if not re.fullmatch(r'\w+', mm.group(1))
                      else read_latex.ods_word(mm.group(1)), m.group(1))
        body = re.sub(r'&\s*(\\[A-Za-z]+|[=<>])\s*&', r'&\1 ', body)
        return '\\begin{align*}' + body + '\\end{align*}'
    return re.sub(r'\\begin\{eqnarray\*\}(.*?)\\end\{eqnarray\*\}', conv, text, flags=re.S)


def ods_block(b, spec, book):
    """An ODS passage (spec row: file, start, stop, chapter, refs) through read_latex, its <h2> first."""
    path = os.path.join(book, b['file'])
    labels, fn_at = read_latex.scan_labels(path, b['chapter'])
    text, off = read_latex.read(path, b['start'], b['stop'])
    nums = [str(n) for pos, n in sorted(fn_at.items()) if off <= pos < off + len(text)]
    text = read_latex.drop_command(text, 'index')
    text = re.sub(r'\\(?:seclabel|lemlabel)\{[^}]*\}', '', text)
    text = read_latex.ods_edition(text)
    text = _eqnarray(text)
    els = read_latex.blocks(text)
    if b.get('drop_first_heading') and els and els[0]['kind'] == 'heading':
        els = els[1:]
    ctx = read_latex.Ctx('ods', labels, spec.get('ODS_LATEX_REFS', {}), fn_prefix=f'ods-fn-{b["chapter"]}')

    def figure_hook(e):
        key = spec.get('ODS_FIGURE_AT', {}).get(e.get('label'))
        return spec['HTML'][key] if key else ''
    hs, ms = read_latex.render(els, ctx, nums, figure_hook=figure_hook, heading_shift=b.get('heading_shift', 1))
    if ctx.unknown:
        raise SystemExit(f'{b["id"]}: LaTeX the reader does not know: {sorted(ctx.unknown)}')
    for n in ctx.notes:
        spec.setdefault('_latex_notes', []).append({'id': n['id'], 'number': n['number'], 'html': n['html'],
                                                   'md': read_latex.to_md(n['html']), 'source': b['source']})
    return [f'<h2>{html.escape(b["h2"], quote=False)}</h2>'] + hs, [f'## {b["h2"]}'] + ms


def ods_caption(path, label, chapter):
    """An ODS figure's caption as the pseudocode edition prints it: (html, plain text)."""
    s = read_latex.strip_comments(open(path, encoding='utf-8').read())
    for m in re.finditer(r'\\begin\{figure\}', s):
        a, _ = read_latex.env_end(s, 'figure', m.end())
        body = s[m.end():a]
        if f'\\figlabel{{{label}}}' not in body:
            continue
        cap = re.search(r'\\caption(\[[^\]]*\])?\{', body)
        t, _ = read_latex.arg(body, cap.end() - 1)
        labels, _ = read_latex.scan_labels(path, chapter)
        h = read_latex.inline(t, read_latex.Ctx('ods', labels, {}), [])
        plain = html.unescape(re.sub(r'<[^>]+>', '', h))
        return h, plain
    raise SystemExit(f'no figure {label} in {path}')
