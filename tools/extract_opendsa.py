#!/usr/bin/env python3
"""Read an OpenDSA module (`opendsa`, reStructuredText) and its code fragments (`opendsa-code`).

OpenDSA writes its modules in Sphinx's reStructuredText (RST/en/<Chapter>/<Module>.rst) and includes its
code from SourceCode/<Language>/<Chapter>/<File> between `/* *** ODSATag: <tag> *** */` and
`/* *** ODSAendTag: <tag> *** */` lines. This reads the subset the modules use into elements, each with
its HTML and its Markdown, so that tools/build_text.py can assemble a block the way it does for the
other sources; no passage is typed by hand.

Block level, in the module's order:

- section titles (the underline character decides the level, in order of first appearance, as docutils
  does), the module's own title and the `avmetadata` header left out;
- paragraphs; an indented paragraph that is not a directive is a block quote (a definition set off);
- `.. math::` (a display), `.. topic:: Title` (a box with its title, holding its own elements);
- `.. codeinclude:: <path>` with `:tag:` (a code element naming the fragment), `.. inlineav::` and
  `.. avembed::` (a slideshow or an exercise, by name), `.. _label:` and comments (left out);
- `.. [#]` footnotes, numbered as docutils numbers them, each a list of elements of its own; the
  marker `[#]_` in the text becomes the note's marker.

Inline: :math:`x` is maths ($x$); :term:`x` and :ref:`x <target>` are their text (a :ref: the caller maps
becomes its link); *x*, **x** and ``x`` are emphasis, strong and code; straight quotes become curly ones,
as Sphinx's smartquotes sets them.

    python3 -I tools/extract_opendsa.py sources/_cache/opendsa/RST/en/AlgAnal/AnalLower.rst   # a dump
    python3 -I tools/extract_opendsa.py --code sources/_cache/opendsa-code Java Misc/Anal Collatz
"""
import html
import json
import os
import re
import sys
import textwrap

UNDERLINE = re.compile(r'^([=\-~^"\'`#*+.:_])\1{2,}\s*$')
DIRECTIVE = re.compile(r'^\.\.\s+([\w-]+)::\s*(.*)$')
FOOTNOTE = re.compile(r'^\.\.\s+\[#\]\s*(.*)$')
LABEL = re.compile(r'^\.\.\s+_[^:]+:\s*$')
CODE_EXT = {'Java': '.java', 'C++': '.cpp', 'C': '.c', 'Python': '.py', 'JavaScript': '.js', 'Pseudo': '.txt',
            'Java_Generic': '.java', 'C++_Templates': '.cpp'}


# ---------------------------------------------------------------- inline

def smartquotes(s):
    """Straight quotes to curly ones, the way docutils' smartquotes reads them: a quote after a space, an
    opening bracket or the start is an opening quote; an apostrophe inside a word is ’."""
    s = re.sub(r'(^|[\s(\[{—–-])"', '\\1“', s)
    s = s.replace('"', '”')
    s = re.sub(r"(\w)'(\w)", '\\1’\\2', s)
    s = re.sub(r"(^|[\s(\[{—–-])'", '\\1‘', s)
    s = s.replace("'", '’')
    return s


def inline(text, refs=None, notes=None):
    """One paragraph's RST inline markup to (html, md). `refs` maps a :ref: target to (html, md); `notes`
    is a callback that takes the next auto-numbered footnote and returns (html marker, md marker)."""
    refs = refs or {}
    pieces = []      # (kind, payload) in order: text, math, code, ref, term, fn
    pat = re.compile(r':math:`([^`]+)`|:term:`([^`]+)`|:ref:`([^`]+)`|``([^`]+)``|\[#\]_')
    pos = 0
    for m in pat.finditer(text):
        if m.start() > pos:
            pieces.append(('text', text[pos:m.start()]))
        if m.group(1) is not None:
            pieces.append(('math', m.group(1)))
        elif m.group(2) is not None:
            t = m.group(2)
            t = re.sub(r'\s*<[^>]+>$', '', t)
            pieces.append(('term', t))
        elif m.group(3) is not None:
            pieces.append(('ref', m.group(3)))
        elif m.group(4) is not None:
            pieces.append(('code', m.group(4)))
        else:
            pieces.append(('fn', None))
        pos = m.end()
    if pos < len(text):
        pieces.append(('text', text[pos:]))

    def styled(s, md):
        if md:
            return s
        s = html.escape(s, quote=False).replace('$', '&#36;')
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
        return s

    h, md = [], []
    for kind, p in pieces:
        if kind in ('text', 'term'):
            t = smartquotes(p)
            h.append(styled(t, False))
            md.append(t)
        elif kind == 'math':
            h.append('$' + html.escape(p, quote=False) + '$')
            md.append('$' + p + '$')
        elif kind == 'code':
            h.append('<code>' + html.escape(p, quote=False).replace('$', '&#36;') + '</code>')
            md.append('`' + p + '`')
        elif kind == 'ref':
            m = re.match(r'(.*?)\s*<([^>]+)>(?:\s*<([^>]+)>)?\s*$', p)
            label = (m.group(1) if m else p).strip()
            target = (m.group(2) if m else p).strip()
            if target in refs:
                h.append(refs[target][0])
                md.append(refs[target][1])
            else:
                h.append(styled(smartquotes(label), False))
                md.append(label)
        else:
            if notes is None:
                raise SystemExit('a footnote marker where no footnotes are taken')
            a, b = notes()
            # the marker hangs on the word before it (docutils drops the space)
            if h:
                h[-1] = h[-1].rstrip()
                md[-1] = md[-1].rstrip()
            h.append(a)
            md.append(b)
    return ''.join(h).strip(), ''.join(md).strip()


# ---------------------------------------------------------------- block structure

def _indent(line):
    return len(line) - len(line.lstrip(' '))


def _block(lines, i, base):
    """The lines from i on that are blank or indented deeper than `base`: a directive's body."""
    out = []
    while i < len(lines) and (not lines[i].strip() or _indent(lines[i]) > base):
        out.append(lines[i])
        i += 1
    while out and not out[-1].strip():
        out.pop()
    return out, i


def _dedent(lines):
    return textwrap.dedent('\n'.join(lines)).split('\n')


def parse(lines, ctx, quote=False):
    """Lines (already dedented to their own margin) to elements. `ctx` carries the underline order, the
    :ref: map and the footnote collector across the module."""
    els = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        ind = _indent(line)
        s = line.strip()
        # a section title: text over an underline
        if i + 1 < len(lines) and UNDERLINE.match(lines[i + 1]) and ind == 0 and not s.startswith('..'):
            ch = lines[i + 1].strip()[0]
            if ch not in ctx['levels']:
                ctx['levels'].append(ch)
            h, md = inline(s, ctx['refs'])
            els.append({'kind': 'heading', 'level': ctx['levels'].index(ch) + 1, 'html': h, 'md': md, 'text': re.sub(r'<[^>]+>', '', h)})
            i += 2
            continue
        if ind > 0:
            # an indented run: a block quote of its own elements
            body, j = _block(lines, i, ind - 1)
            inner = parse(_dedent(body), ctx, quote=True)
            if all(c['kind'] in ('code', 'display', 'topic', 'inlineav', 'avembed') for c in inner):
                els.extend(inner)    # an indented directive is the directive itself, not a quotation
            else:
                els.append({'kind': 'quote', 'children': inner})
            i = j
            continue
        m = FOOTNOTE.match(s)
        if m:
            body, j = _block(lines, i + 1, 0)
            first = m.group(1)
            text = [first] + _dedent(body) if first else _dedent(body)
            ctx['fn_defs'].append(parse(text, ctx))
            i = j
            continue
        if LABEL.match(s):
            i += 1
            continue
        m = DIRECTIVE.match(s)
        if m:
            name, arg = m.group(1), m.group(2).strip()
            body, j = _block(lines, i + 1, 0)
            body = _dedent(body)
            opts = {}
            k = 0
            while k < len(body) and re.match(r'^:[\w-]+:', body[k]):
                om = re.match(r'^:([\w-]+):\s*(.*)$', body[k])
                opts[om.group(1)] = om.group(2)
                k += 1
                while k < len(body) and body[k].startswith(' '):
                    opts[om.group(1)] += ' ' + body[k].strip()
                    k += 1
            content = body[k:]
            if name == 'math':
                tex = '\n'.join(l for l in content).strip()
                els.append({'kind': 'display', 'tex': tex})
            elif name == 'topic':
                els.append({'kind': 'topic', 'title': arg, 'children': parse(content, ctx)})
            elif name == 'codeinclude':
                els.append({'kind': 'code', 'path': arg, 'tag': opts.get('tag', '').strip()})
            elif name in ('inlineav', 'avembed'):
                els.append({'kind': name, 'name': arg.split()[0], 'type': (arg.split() + [''])[1], 'opts': opts})
            # avmetadata, index, odsalink, odsascript and the rest carry nothing for the page
            i = j
            continue
        if s.startswith('..'):
            # a comment, and anything indented under it
            _, j = _block(lines, i + 1, 0)
            i = j
            continue
        # a paragraph: lines to the next blank line
        para = []
        while i < len(lines) and lines[i].strip() and _indent(lines[i]) == ind and not DIRECTIVE.match(lines[i].strip()):
            para.append(lines[i].strip())
            i += 1
        text = ' '.join(para)
        h, md = inline(text, ctx['refs'], ctx['note'])
        els.append({'kind': 'p', 'html': h, 'md': md, 'text': re.sub(r'<[^>]+>', '', h)})
    return els


def read_module(path, refs=None, note_id='opendsa-fn'):
    """A module to (elements, footnotes). A footnote is {id, number, children}; its marker in the text is
    <sup class="fn" data-note="<id>"></sup>, its id `note_id`-<number>."""
    lines = open(path, encoding='utf-8').read().replace('\t', '    ').split('\n')
    ctx = {'levels': [], 'refs': refs or {}, 'fn_defs': [], 'fn_count': 0}

    def note():
        ctx['fn_count'] += 1
        n = ctx['fn_count']
        return f'<sup class="fn" data-note="{note_id}-{n}"></sup>', f'[^{n}]'
    ctx['note'] = note
    els = parse(lines, ctx)
    notes = [{'id': f'{note_id}-{k + 1}', 'number': str(k + 1), 'children': c} for k, c in enumerate(ctx['fn_defs'])]
    return els, notes


def flatten(els):
    """Elements in reading order with a topic's or a quote's children after it, for slicing by heading."""
    for e in els:
        yield e


def render(els, md=False, hooks=None):
    """Elements to HTML (or Markdown) lines. `hooks(e)` may return a replacement (a list of strings, or
    None to use the default) for a code, inlineav or avembed element."""
    out = []
    for e in els:
        k = e['kind']
        if hooks:
            r = hooks(e, md)
            if r is not None:
                out.extend(r)
                continue
        if k == 'heading':
            n = e['level']
            out.append(('#' * n + ' ' + e['md']) if md else f'<h{n}>{e["html"]}</h{n}>')
        elif k == 'p':
            out.append(e['md'] if md else f'<p>{e["html"]}</p>')
        elif k == 'display':
            out.append(f'$${e["tex"]}$$' if md else f'$${html.escape(e["tex"], quote=False)}$$')
        elif k == 'quote':
            inner = render(e['children'], md, hooks)
            out.append('\n'.join('> ' + l for l in '\n\n'.join(inner).split('\n')) if md
                       else '<blockquote>' + '\n'.join(inner) + '</blockquote>')
        elif k == 'topic':
            inner = render(e['children'], md, hooks)
            title = html.escape(e['title'], quote=False)
            out.append(f'**{e["title"]}**\n\n' + '\n\n'.join(inner) if md
                       else f'<div class="note"><div class="eyebrow">{title}</div>\n' + '\n'.join(inner) + '\n</div>')
        elif k == 'code':
            out.append(f'[codeinclude {e["path"]} {e["tag"]}]' if md else '')
        elif k in ('inlineav', 'avembed'):
            out.append(f'[{k} {e["name"]}]' if md else '')
    return [o for o in out if o != '']


# ---------------------------------------------------------------- code fragments

def code_region(root, lang, path, tag):
    """The lines of SourceCode/<lang>/<path><ext> between the ODSATag and ODSAendTag lines of `tag`,
    with their common indentation taken off (as the codeinclude directive shows them)."""
    f = os.path.join(root, 'SourceCode', lang, path + CODE_EXT[lang])
    src = open(f, encoding='utf-8').read().replace('\t', '    ').split('\n')
    start = next(i for i, l in enumerate(src) if re.search(r'ODSATag:\s*' + re.escape(tag) + r'\b', l))
    stop = next(i for i, l in enumerate(src) if i > start and re.search(r'ODSAendTag:\s*' + re.escape(tag) + r'\b', l))
    body = [l.rstrip() for l in src[start + 1:stop]]
    return textwrap.dedent('\n'.join(body)).strip('\n')


if __name__ == '__main__':
    if sys.argv[1] == '--code':
        print(code_region(*sys.argv[2:6]))
    else:
        els, notes = read_module(sys.argv[1])
        json.dump({'elements': els, 'footnotes': notes}, sys.stdout, ensure_ascii=False, indent=1)
        print()
