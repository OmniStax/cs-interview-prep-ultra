#!/usr/bin/env python3
"""Read a passage of a LaTeX source (Brisk Walk `brisk`, Open Data Structures `ods`) as page elements.

tools/build_text.py's first ODS reader handles running prose only. This one reads what a mathematics
passage holds: sections and subsections, paragraphs, display maths (\\[ \\], align, align*), framed boxes,
centred lines and tables, numbered and bulleted lists (with `[resume]`), lemma and proof environments,
figures (their caption and label kept, their drawing left to the section's Sim), footnotes and
cross-references. The source's words are never retyped: every word on the page comes out of the .tex.

Two dialects:

- `brisk`: Davies closes a quotation with a straight double quote (``like this"), so `"` is a closing
  quote; `\\textbf` marks a defined term.
- `ods`: Morin's `#name#` marks code. The pseudocode edition (METHOD decision 20) sets a capitalised
  #Name# as plain text and any other #name# as maths (latex/snarf-python.py, code_subs); inside maths
  #x# is the variable x. `\\E` is `\\mathrm{E}` (ods.tex).

Labels are resolved over whole files (a chapter's sections, figures, list items and footnotes are
numbered from the start of its file, under the chapter number the caller gives), so a reference reads
as the source prints it: `Rule~\\ref{nonegs}` is "Rule 2", `Figure~\\ref{venn}` is "Figure 4.1". A
reference the caller maps (refs) is printed the caller's way, for a target this book does not carry.

    python3 -I tools/read_latex.py sources/_cache/brisk/probability.tex 4 "\\section{Conditional" "\\section{Total"
"""
import html
import re
import sys

SIZE = r'(?:tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE|huge|Huge)'


# ---------------------------------------------------------------- braces

def group_end(s, i):
    """s[i] is '{' (or '['): the index just past its matching close."""
    op = s[i]
    cl = '}' if op == '{' else ']'
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == op:
            depth += 1
        elif c == cl:
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    raise ValueError('unbalanced group at ' + s[i:i + 60])


def arg(s, i):
    """The braced argument starting at or after s[i] (spaces skipped): (content, index past it)."""
    while i < len(s) and s[i] in ' \n\t':
        i += 1
    if i >= len(s) or s[i] != '{':
        # an unbraced single token
        m = re.match(r'\\[A-Za-z]+|.', s[i:])
        return m.group(0), i + len(m.group(0))
    e = group_end(s, i)
    return s[i + 1:e - 1], e


def drop_command(s, name, nargs=1):
    """Remove every \\name{…} (with its arguments)."""
    out, i = [], 0
    pat = re.compile(r'\\' + name + r'\*?(?![A-Za-z])')
    while True:
        m = pat.search(s, i)
        if not m:
            out.append(s[i:])
            return ''.join(out)
        out.append(s[i:m.start()])
        j = m.end()
        for _ in range(nargs):
            _, j = arg(s, j)
        # an \index line ends with % or a newline that should not leave a blank line
        i = j


def strip_comments(s):
    """Comments out; a line that held only an index entry or a comment goes whole, so that it leaves
    no blank line, which would end the paragraph."""
    out = []
    for l in s.split('\n'):
        t = re.sub(r'(?<!\\)%.*$', '', l)
        bare = drop_command(t, 'index').strip()
        if not bare and l.strip():
            continue
        out.append(t)
    return '\n'.join(out)


# ---------------------------------------------------------------- labels over whole files

def scan_labels(path, chapter):
    """Number a chapter file's sections, subsections, figures, list items and footnotes as LaTeX would,
    and return {label: {kind, number, title}} and the footnote numbers by offset."""
    s = strip_comments(open(path, encoding='utf-8').read())
    labels = {}
    sec = sub = fig = 0
    enum_stack = []
    last_enum = 0
    fn = 0
    fn_at = {}
    cur = None
    tok = re.compile(r'\\(section|subsection|subsubsection)\*?\{|\\begin\{(figure|enumerate|lem|thm)\}(\[[^\]]*\])?|'
                     r'\\end\{(enumerate|figure)\}|\\item\b|\\label\{([^}]*)\}|\\(?:lem|sec|fig|thm)label\{([^}]*)\}|\\footnote\{')
    for m in tok.finditer(s):
        if m.group(1):
            title, _ = arg(s, m.end() - 1)
            if m.group(1) == 'section':
                sec += 1
                sub = 0
                cur = {'kind': 'section', 'number': f'{chapter}.{sec}', 'title': title}
            elif m.group(1) == 'subsection':
                sub += 1
                cur = {'kind': 'section', 'number': f'{chapter}.{sec}.{sub}', 'title': title}
            else:
                cur = {'kind': 'section', 'number': f'{chapter}.{sec}.{sub}', 'title': title}
        elif m.group(2) == 'figure':
            fig += 1
            cur = {'kind': 'figure', 'number': f'{chapter}.{fig}'}
        elif m.group(2) == 'enumerate':
            start = last_enum if m.group(3) and 'resume' in m.group(3) else 0
            enum_stack.append(start)
        elif m.group(2) in ('lem', 'thm'):
            cur = {'kind': m.group(2), 'number': ''}
        elif m.group(4) == 'enumerate':
            last_enum = enum_stack.pop()
        elif m.group(0).startswith('\\item') and enum_stack:
            enum_stack[-1] += 1
            cur = {'kind': 'item', 'number': str(enum_stack[-1])}
        elif m.group(5) is not None or m.group(6) is not None:
            labels[m.group(5) or m.group(6)] = dict(cur or {'kind': 'none', 'number': '?'})
        elif m.group(0) == '\\footnote{':
            fn += 1
            fn_at[m.start()] = fn
    return labels, fn_at


# ---------------------------------------------------------------- blocks

BLOCK_ENVS = ('framed', 'center', 'enumerate', 'itemize', 'figure', 'align', 'align*', 'equation', 'equation*',
              'lem', 'thm', 'proof', 'minipage', 'tabular', 'longtable')


def unwrap_size_groups(s):
    """{\\footnotesize …} and {\\small \\[ … \\]}: the size goes, the content stays."""
    while True:
        m = re.search(r'\{\\' + SIZE + r'(?![A-Za-z])', s)
        if not m:
            break
        e = group_end(s, m.start())
        s = s[:m.start()] + s[m.end():e - 1] + s[e:]
    s = re.sub(r'\\' + SIZE + r'(?![A-Za-z])\s*', '', s)
    return s


def env_end(s, name, i):
    """s[i:] starts just after \\begin{name}: the index of the matching \\end{name} and past it."""
    depth = 1
    pat = re.compile(r'\\(begin|end)\{' + re.escape(name) + r'\}')
    for m in pat.finditer(s, i):
        depth += 1 if m.group(1) == 'begin' else -1
        if depth == 0:
            return m.start(), m.end()
    raise ValueError('no \\end{' + name + '}')


def blocks(s):
    """Source text to block elements, in order."""
    out = []
    para = []

    def flush():
        t = ''.join(para).strip()
        if t:
            out.append({'kind': 'p', 'tex': ' '.join(t.split())})
        para.clear()
    i = 0
    pat = re.compile(r'\\(section|subsection|subsubsection|paragraph)\*?\{|\\begin\{([A-Za-z*]+)\}|\\\[|\n\s*\n|'
                     r'\\(codeimport|javaimport|cppimport|pcodeimport)\{')
    while i < len(s):
        m = pat.search(s, i)
        if not m:
            para.append(s[i:])
            break
        para.append(s[i:m.start()])
        if m.group(0).startswith('\n'):
            flush()
            i = m.end()
            continue
        if m.group(1):
            if m.group(1) == 'paragraph':
                title, j = arg(s, m.end() - 1)
                para.append('\\textbf{' + title + '} ')
                i = j
                continue
            flush()
            title, j = arg(s, m.end() - 1)
            level = {'section': 2, 'subsection': 3, 'subsubsection': 4}[m.group(1)]
            out.append({'kind': 'heading', 'level': level, 'tex': title})
            i = j
            continue
        if m.group(3):
            # ODS's listing of a class's methods by the edition's source (\codeimport{ods/ArrayStack.add(i,x)}):
            # the paragraph breaks where it stands, and the section's code hook sets it
            flush()
            ref, j = arg(s, m.end() - 1)
            out.append({'kind': 'code', 'cmd': m.group(3), 'ref': ref})
            i = j
            continue
        if m.group(0) == '\\[':
            flush()
            e = s.index('\\]', m.end())
            out.append({'kind': 'display', 'tex': s[m.end():e].strip()})
            i = e + 2
            continue
        name = m.group(2)
        if name not in BLOCK_ENVS:
            para.append(m.group(0))
            i = m.end()
            continue
        flush()
        j = m.end()
        opt = ''
        if j < len(s) and s[j] == '[':
            e = group_end(s, j)
            opt = s[j + 1:e - 1]
            j = e
        if name in ('minipage', 'tabular', 'longtable'):
            # a minipage's width, a table's column spec
            if j < len(s) and s[j] == '{':
                _, j = arg(s, j)
        a, b = env_end(s, name, j)
        body = s[j:a]
        i = b
        if name in ('align', 'align*', 'equation', 'equation*'):
            tex = body.strip()
            out.append({'kind': 'display', 'tex': tex, 'aligned': name.startswith('align')})
        elif name in ('enumerate', 'itemize'):
            items = [x.strip() for x in re.split(r'\\item\b', body)[1:]]
            out.append({'kind': 'list', 'ordered': name == 'enumerate', 'resume': 'resume' in opt, 'items': items})
        elif name == 'center':
            if '\\begin{tabular}' in body:
                out.extend(blocks(body))
            else:
                lines = [' '.join(x.split()) for x in re.split(r'\\\\', body)]
                out.append({'kind': 'center', 'lines': [x for x in lines if x]})
        elif name == 'tabular':
            rows = []
            for r in re.split(r'\\\\', body):
                r = r.replace('\\hline', '').strip()
                if r:
                    rows.append([' '.join(c.split()) for c in r.split('&')])
            out.append({'kind': 'table', 'rows': rows})
        elif name == 'minipage':
            out.extend(blocks(body))
        elif name == 'figure':
            cap = ''
            mm = re.search(r'\\caption(\[[^\]]*\])?\{', body)
            if mm:
                cap, _ = arg(body, mm.end() - 1)
            lab = re.search(r'\\(?:fig)?label\{([^}]*)\}', body)
            out.append({'kind': 'figure', 'label': lab.group(1) if lab else None, 'caption': cap})
        else:   # framed, lem, thm, proof
            lab = re.search(r'\\(?:lem|thm)?label\{([^}]*)\}', body)
            out.append({'kind': 'env', 'name': name, 'label': lab.group(1) if lab else None,
                        'children': blocks(re.sub(r'\\(?:lem|thm)label\{[^}]*\}', '', body))})
    flush()
    return out


# ---------------------------------------------------------------- inline

TEXT_CMDS = {'textbf': ('<strong>', '</strong>'), 'textit': ('<em>', '</em>'), 'emph': ('<em>', '</em>'),
             'textsl': ('<em>', '</em>'), 'texttt': ('<code>', '</code>'), 'textsuperscript': ('<sup>', '</sup>'),
             'textrm': ('', ''), 'mbox': ('', ''), 'text': ('', ''), 'textsc': ('<span style="font-variant:small-caps">', '</span>')}
SYMBOLS = {'&': '&amp;', '%': '%', '$': '&#36;', '#': '#', '_': '_', '{': '{', '}': '}', ' ': ' ', ',': ' ', '@': '',
           '/': '', '-': ''}
WORDS = {'dots': '…', 'ldots': '…', 'textregistered': '®', 'copyright': '©', 'S': '§', 'ss': 'ß',
         'noindent': '', 'centering': '', 'quad': ' ', 'qquad': ' ', 'pagebreak': '', 'newpage': '',
         'bigskip': '', 'medskip': '', 'smallskip': '', 'hfill': ' ', 'normalsize': '', 'relax': '', 'linebreak': ' ',
         'qedhere': ''}


# ---------------------------------------------------------------- ODS's pseudocode edition

# The edition macros (latex/Makefile): the pseudocode edition (METHOD decision 20) prints \pcodeonly{…} and
# drops \javaonly{…}, \cpponly{…} and \notpcode{…}, as tools/build_text.py's first ODS reader does.
ODS_EDITION = {'pcodeonly': True, 'javaonly': False, 'cpponly': False, 'notpcode': False}


def ods_edition(text):
    """Apply the edition macros, braces balanced."""
    out, i = [], 0
    pat = re.compile(r'\\(' + '|'.join(ODS_EDITION) + r')\{')
    while True:
        m = pat.search(text, i)
        if not m:
            out.append(text[i:])
            return ''.join(out)
        before = text[i:m.start()]
        e = group_end(text, m.end() - 1)
        if ODS_EDITION[m.group(1)]:
            out.append(before)
            out.append(ods_edition(text[m.end():e - 1]))
        else:
            # a dropped macro that stood on a line of its own takes its line with it, so that it leaves no blank
            # line to end the paragraph
            line_start = before.rfind('\n') + 1
            nl = text.find('\n', e)
            rest = text[e:nl if nl >= 0 else len(text)]
            if not before[line_start:].strip() and not rest.strip() and nl >= 0:
                out.append(before[:line_start])
                e = nl + 1
            else:
                out.append(before)
        i = e


# The words the edition's translate_code sets in bold (latex/snarf-python.py, keywords).
PCODE_KEYWORDS = ('if', 'or', 'and', 'then', 'else', 'in', 'for', 'do', 'return', 'while', 'break', 'repeat', 'times')


def ods_pcode(code):
    """A #code# run that is not one word, as the pseudocode edition sets it in maths (latex/snarf-python.py,
    translate_code, the parts ODS's array chapters use): a call's name upright (get(i), resize(),
    System.arraycopy(s,i,d,j,n)), an array's length as length(a), = as \\gets, ++ as one operator, a name ending
    in a digit with that digit as a subscript (a0 is a₀). The edition's script also strips every colon, which
    turns C++'s std::copy into "stdcopy"; the name is kept as C++ writes it."""
    c = re.sub(r'\b([A-Za-z_]\w*)\.length\b', r'\\mathrm{length}(\1)', code)
    c = re.sub(r'(?<![\w\\])([A-Za-z_][\w.]*(?:::\w+)*)\(', lambda m: '\\mathrm{' + m.group(1).replace(':', '{:}') + '}(', c)
    c = re.sub(r'(?<![=<>!])=(?!=)', r'\\gets ', c)
    c = c.replace('++', '{+}{+}')
    c = re.sub(r'(?<![\\\w])([a-z])(\d)\b', r'\1_\2', c)
    return c


def ods_word(w):
    """A one-word #code#: a keyword in bold, as the edition prints it; a longer name in \\mathit (add, remove), one
    letter the variable itself."""
    if w in PCODE_KEYWORDS:
        return '\\textbf{' + w + '}'
    return '\\mathit{' + w + '}' if len(w) > 1 and not w.isdigit() else w


def math_tex(t, dialect):
    t = t.replace('\\qedhere', '')
    t = re.sub(r'\\(?:label|lemlabel|seclabel)\{[^}]*\}', '', t)
    if dialect == 'ods':
        t = re.sub(r'#(\w+)#', r'\1', t)
        t = re.sub(r'#([^#\s][^#]*)#', lambda m: ods_pcode(m.group(1)), t)
        t = re.sub(r'\\E(?![A-Za-z])', r'\\mathrm{E}', t)
    t = t.replace('\\mbox{', '\\text{')
    if dialect == 'brisk':
        # Davies closes a quotation with ", which TeX's text fonts print as a closing double quote
        t = t.replace('"', "''")
    t = re.sub(r'\\nonumber|\\notag', '', t)
    return ' '.join(t.split())


class Ctx:
    def __init__(self, dialect, labels, refs, fn_at=None, fn_prefix='fn'):
        self.dialect = dialect
        self.labels = labels       # label -> {kind, number, title}
        self.refs = refs or {}     # label -> (html, md): the caller's rendering of a reference
        self.notes = []            # footnotes met, in order: {id, number, html}
        self.fn_at = fn_at or {}
        self.fn_prefix = fn_prefix
        self.unknown = set()


def inline(tex, ctx, fn_numbers=None, _maths=None):
    """Inline LaTeX to HTML. fn_numbers: the printed numbers for the footnotes in this text, in order.
    (_maths: the maths of the text a nested call is part of, already taken out.)"""
    fn_numbers = list(fn_numbers or [])
    nested = _maths is not None
    notes_before = len(ctx.notes)
    maths = _maths if nested else []

    def keep_math(t):
        maths.append(math_tex(t, ctx.dialect))
        return f'\x00{len(maths) - 1}\x01'
    # maths first, so nothing inside it is touched; an escaped dollar is text
    s = tex
    if not nested:
        s = s.replace('\\$', '\x02')
        s = re.sub(r'\$([^$]+)\$', lambda m: keep_math(m.group(1)), s)
        s = re.sub(r'\\\((.+?)\\\)', lambda m: keep_math(m.group(1)), s)
        s = s.replace('\x02', '\\$')
    if ctx.dialect == 'ods' and not nested:
        # the pseudocode edition: a capitalised #Name# is plain text, any other #name# maths
        s = re.sub(r'#([A-Z]\w*)#', r'\1', s)
        s = re.sub(r'#(\w+)#', lambda m: keep_math(ods_word(m.group(1))), s)
        s = re.sub(r'#([^#\s][^#]*)#', lambda m: keep_math(ods_pcode(m.group(1))), s)
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            m = re.match(r'\\([A-Za-z]+)\*?|\\(.)', s[i:])
            if m.group(2) is not None:
                ch = m.group(2)
                if ch == '\\':
                    out.append('<br>')
                elif ch in SYMBOLS:
                    out.append(SYMBOLS[ch])
                elif ch in "'`^\"~":
                    # an accent on the next letter
                    _, j = arg(s, i + 2)
                    base = s[i + 2:j].strip('{}')
                    comb = {"'": '\u0301', '`': '\u0300', '^': '\u0302', '"': '\u0308', '~': '\u0303'}[ch]
                    import unicodedata
                    out.append(unicodedata.normalize('NFC', base + comb))
                    i = j
                    continue
                else:
                    ctx.unknown.add('\\' + ch)
                i += len(m.group(0))
                continue
            name = m.group(1)
            j = i + len(m.group(0))
            if name in TEXT_CMDS:
                body, j = arg(s, j)
                o, cl = TEXT_CMDS[name]
                out.append(o + inline(body, ctx_child(ctx), [], maths) + cl)
                i = j
                continue
            if name == 'footnote':
                body, j = arg(s, j)
                num = fn_numbers.pop(0) if fn_numbers else str(len(ctx.notes) + 1)
                nid = f'{ctx.fn_prefix}-{num}'
                ctx.notes.append({'id': nid, 'number': num, 'html': inline(body, ctx, [], maths)})
                out.append(f'<sup class="fn" data-note="{nid}"></sup>')
                i = j
                continue
            if name in ('ref', 'pageref', 'secref', 'chapref', 'lemref', 'thmref', 'figref', 'eqref'):
                lab, j = arg(s, j)
                key = lab if name in ('ref', 'pageref') else f'{name}:{lab}'
                if key in ctx.refs:
                    out.append(ctx.refs[key][0])
                elif lab in ctx.labels and name == 'ref':
                    out.append(ctx.labels[lab]['number'])
                else:
                    ctx.unknown.add(f'\\{name}{{{lab}}}')
                    out.append('??')
                i = j
                continue
            if name in ('index', 'label', 'vspace', 'hspace', 'seclabel', 'lemlabel'):
                _, j = arg(s, j)
                i = j
                continue
            if name in WORDS:
                out.append(WORDS[name])
                i = j
                # a control word eats the spaces after it, except where it printed a word
                if WORDS[name] in ('', ):
                    while i < len(s) and s[i] in ' \n':
                        i += 1
                elif re.match(r'\{\}', s[i:]):
                    i += 2
                continue
            ctx.unknown.add('\\' + name)
            i = j
            continue
        if c in '{}':
            i += 1
            continue
        if c == '~':
            out.append(' ')
            i += 1
            continue
        out.append(c)
        i += 1
    h = ''.join(out)
    # typography, outside tags
    parts = re.split(r'(<[^>]+>|\x00\d+\x01)', h)
    for k, p in enumerate(parts):
        if p.startswith('<') or p.startswith('\x00'):
            continue
        p = p.replace('``', '“').replace("''", '”').replace('---', '—').replace('--', '–')
        if ctx.dialect == 'brisk':
            p = p.replace('"', '”')
        p = re.sub(r'`', '‘', p)
        p = p.replace("'", '’')
        p = html.escape(p, quote=False).replace('&amp;amp;', '&amp;').replace('&amp;#36;', '&#36;')
        parts[k] = p
    h = ''.join(parts)
    if not nested:
        put = lambda t: re.sub(r'\x00(\d+)\x01', lambda m: '$' + maths[int(m.group(1))] + '$', t)  # noqa: E731
        h = put(h)
        for n in ctx.notes[notes_before:]:
            n['html'] = put(n['html'])
    h = re.sub(r'[ \t\n]+', ' ', h)
    return h.strip()


def ctx_child(ctx):
    return ctx


def to_md(h):
    """The HTML of a block as Markdown for source.md."""
    m = h
    m = re.sub(r'<sup class="fn" data-note="[^"]*-(\w+)"></sup>', r'[^\1]', m)
    m = m.replace('<strong>', '**').replace('</strong>', '**').replace('<em>', '*').replace('</em>', '*')
    m = m.replace('<code>', '`').replace('</code>', '`').replace('<br>', '  \n')
    m = re.sub(r'<sup>(.*?)</sup>', r'^\1^', m)
    m = re.sub(r'<[^>]+>', '', m)
    return html.unescape(m).replace('$', '$')


# ---------------------------------------------------------------- render

def render(els, ctx, fn_numbers, display_hook=None, env_hook=None, figure_hook=None, heading_shift=0,
           enum_state=None, code_hook=None):
    """Elements to (html list, md list). Hooks let the section replace a display, an environment or a
    figure by its own HTML (a derivation, a Sim): each takes the element and returns HTML, '' to drop
    it, or None to render it as printed."""
    hs, ms = [], []
    enum_state = enum_state if enum_state is not None else {'last': 0}
    for e in els:
        k = e['kind']
        if k == 'heading':
            # a heading never skips a level (a \subsubsection straight under a \section is one below it)
            lvl = min(e['level'] + heading_shift, enum_state.get('h', 1 + heading_shift) + 1)
            enum_state['h'] = lvl
            t = inline(e['tex'], ctx, [])
            hs.append(f'<h{lvl}>{t}</h{lvl}>')
            ms.append('#' * lvl + ' ' + to_md(t))
        elif k == 'p':
            n = e['tex'].count('\\footnote{')
            nums = [fn_numbers.pop(0) for _ in range(n)] if fn_numbers else []
            t = inline(e['tex'], ctx, nums)
            if t:
                hs.append(f'<p>{t}</p>')
                ms.append(to_md(t))
        elif k == 'display':
            rep = display_hook(e) if display_hook else None
            if rep is not None:
                if rep:
                    hs.append(rep)
                    ms.append(f'[{e.get("as", "replaced")}]')
                continue
            tex = math_tex(e['tex'], ctx.dialect)
            if e.get('aligned'):
                tex = '\\begin{aligned}' + tex + '\\end{aligned}'
            hs.append(f'$${tex}$$')
            ms.append(f'$${tex}$$')
        elif k == 'list':
            tag = 'ol' if e['ordered'] else 'ul'
            start = ''
            if e['ordered']:
                first = enum_state['last'] + 1 if e['resume'] else 1
                if first != 1:
                    start = f' start="{first}"'
                enum_state['last'] = first - 1 + len(e['items'])
            items = []
            for it in e['items']:
                n = it.count('\\footnote{')
                nums = [fn_numbers.pop(0) for _ in range(n)] if fn_numbers else []
                items.append(inline(it, ctx, nums))
            hs.append(f'<{tag}{start}>' + ''.join(f'<li>{x}</li>' for x in items) + f'</{tag}>')
            ms.append('\n'.join(('1. ' if e['ordered'] else '- ') + to_md(x) for x in items))
        elif k == 'center':
            lines = [inline(x, ctx, []) for x in e['lines']]
            hs.append('<p>' + '<br>'.join(lines) + '</p>')
            ms.append('  \n'.join(to_md(x) for x in lines))
        elif k == 'table':
            rows = [[inline(c, ctx, []) for c in r] for r in e['rows']]
            head, body = rows[0], rows[1:]
            th = ''.join(f'<th>{c}</th>' for c in head)
            tb = ''.join('<tr>' + ''.join((f'<th>{c}</th>' if j == 0 and c else f'<td>{c}</td>') for j, c in enumerate(r)) + '</tr>' for r in body)
            hs.append(f'<div class="book-table"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>')
            ms.append('| ' + ' | '.join(to_md(c) for c in head) + ' |\n|' + '---|' * len(head) + '\n' +
                      '\n'.join('| ' + ' | '.join(to_md(c) for c in r) + ' |' for r in body))
        elif k == 'code':
            # an ODS listing (\codeimport and the edition imports): the section's code hook sets it, or it is dropped
            rep = code_hook(e) if code_hook else None
            if rep:
                hs.append(rep)
                ms.append(f'[code {e["cmd"]} {e["ref"]}]')
        elif k == 'figure':
            rep = figure_hook(e) if figure_hook else None
            if rep:
                hs.append(rep)
                ms.append(f'[figure {e.get("label")}]')
        elif k == 'env':
            rep = env_hook(e) if env_hook else None
            if rep is not None:
                if rep:
                    hs.append(rep)
                    ms.append(f'[{e["name"]}]')
                continue
            ih, im = render(e['children'], ctx, fn_numbers, display_hook, env_hook, figure_hook, heading_shift, enum_state,
                            code_hook)
            if e['name'] == 'proof':
                # a proof is printed as running text opened by "Proof." (the derivation, if any, stands in it)
                if ih and ih[0].startswith('<p>'):
                    ih[0] = '<p><em>Proof.</em> ' + ih[0][3:]
                    im[0] = '*Proof.* ' + im[0]
                hs.extend(ih)
                ms.extend(im)
                continue
            eyebrow = {'lem': 'Lemma', 'thm': 'Theorem', 'proof': 'Proof'}.get(e['name'], e.get('eyebrow', ''))
            eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ''
            hs.append(f'<div class="note">{eb}' + '\n'.join(ih) + '</div>')
            ms.append('> ' + (f'**{eyebrow}.** ' if eyebrow else '') + '\n> '.join(im))
    return hs, ms


def read(path, start, stop, include_start=True):
    """The text of a .tex file from the line holding `start` to the line before the one holding `stop`,
    with its offset in the comment-stripped file (for footnote numbering)."""
    s = strip_comments(open(path, encoding='utf-8').read())
    a = s.index(start)
    a = s.rfind('\n', 0, a) + 1
    if not include_start:
        a = s.index('\n', a) + 1
    b = s.index(stop, a + 1) if stop else len(s)
    if stop:
        b = s.rfind('\n', 0, b) + 1
    return s[a:b], a


def passage(path, start, stop, chapter, dialect, refs=None, fn_prefix='fn', all_labels=None, **hooks):
    """One passage, read and rendered: (html list, md list, footnotes, unknown commands)."""
    labels, fn_at = scan_labels(path, chapter)
    if all_labels:
        labels = dict(all_labels, **labels)
    text, off = read(path, start, stop)
    nums = [str(n) for pos, n in sorted(fn_at.items()) if off <= pos < off + len(text)]
    text = drop_command(text, 'index')
    if dialect == 'ods':
        # the pseudocode edition's text, and none of the table's spacing set-up (\newlength and its kin)
        text = ods_edition(text)
        for name, nargs in (('newlength', 1), ('setlength', 2), ('addtolength', 2)):
            text = drop_command(text, name, nargs)
    text = re.sub(r'\\(?:seclabel|lemlabel)\{[^}]*\}', '', text)
    text = unwrap_size_groups(text)
    els = blocks(text)
    ctx = Ctx(dialect, labels, refs, fn_prefix=fn_prefix)
    hs, ms = render(els, ctx, nums, **hooks)
    return hs, ms, ctx.notes, ctx.unknown, els


if __name__ == '__main__':
    path, chapter, start, stop = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    dialect = 'ods' if '/ods/' in path else 'brisk'
    hs, ms, notes, unknown, _ = passage(path, start, stop, chapter, dialect)
    print('\n\n'.join(hs))
    for n in notes:
        print('NOTE', n)
    if unknown:
        print('UNKNOWN', sorted(unknown), file=sys.stderr)


def figure_captions(path, chapter, dialect):
    """The figures of a chapter file: {label: {number, html, text}}, the caption as the source prints it."""
    labels, _ = scan_labels(path, chapter)
    s = strip_comments(open(path, encoding='utf-8').read())
    out = {}
    for m in re.finditer(r'\\begin\{figure\}', s):
        a, b = env_end(s, 'figure', m.end())
        body = s[m.end():a]
        lab = re.search(r'\\(?:fig)?label\{([^}]*)\}', body)
        cap = re.search(r'\\caption(\[[^\]]*\])?\{', body)
        if not (lab and cap):
            continue
        t, _ = arg(body, cap.end() - 1)
        h = inline(t, Ctx(dialect, labels, {}), [])
        out[lab.group(1)] = {'number': labels.get(lab.group(1), {}).get('number'), 'html': h,
                             'text': html.unescape(re.sub(r'<[^>]+>', '', h))}
    return out
