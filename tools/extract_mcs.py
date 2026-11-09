#!/usr/bin/env python3
"""Read a passage of *Mathematics for Computer Science* (MCS 2018, `mcs2018`) from its PDF, glyph by glyph.

The cached `mcs-2018.txt` (pdftotext) is wrong wherever the book sets mathematics: the MathTime Pro 2
fonts carry no Unicode map and no /Differences, so pdftotext reads each glyph by its code and prints
"=" as "D", "{" as "f", "[" as "Œ", "(" as "." and "≤" as nothing. This script reads the PDF with
pdfminer at the character level (as tools/extract_jeffe.py does for Erickson) and decodes each math
glyph by its font and code, from the table below, which was read off the page renders.

It lays the page out as MCS sets it: headings in the bold face, paragraphs opened by an indent, displays
set off to the right. Text in the math fonts becomes inline TeX ($…$) so the page sets it as the rest of
the book's mathematics; text in the italic face becomes <em>. A display is returned by its key
("p866#2": the second display on PDF page 866) for the section's build_spec.py to set in LaTeX, since
the PDF draws a display's underbraces and fractions in pieces.

    python3 -I tools/extract_mcs.py sources/_cache/mcs2018/mcs.pdf 865-867 --show
"""
import html
import re
import sys
from collections import Counter

from pdfminer.layout import LTChar
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extract_jeffe  # noqa: E402

# The MathTime Pro 2 glyphs MCS uses, by font and code: (TeX, text). Letters and digits of the math
# fonts are themselves; a code missing here is reported, never guessed.
MATH = {
    'MT2MIT': {33: (r'\omega', 'ω'), 46: ('(', '('), 47: (')', ')'), 58: ('.', '.'), 59: (',', ','),
               61: ('/', '/'), 140: ('[', '['), 141: (']', ']')},
    'MT2SYT': {1: (r'\cdot', '·'), 20: (r'\le', '≤'), 50: (r'\in', '∈'), 67: ('+', '+'), 68: ('=', '='),
               102: (r'\{', '{'), 103: (r'\}', '}'), 133: (r'\notin', '∉'), 164: (r'\ne', '≠')},
    'MT2SYS': {68: ('=', '=')},
    'CMSY10': {83: (r'\mathcal{S}', '𝒮')},
    'MSBM10': {82: (r'\mathbb{R}', 'ℝ')},
}
MATH['MT2MIS'] = MATH['MT2MIT']
# the pieces of underbraces and large delimiters: a display that holds them is set by hand
DRAWN = {'MT2EXA'}


def short(fontname):
    return fontname.split('+')[-1]


def char_record(c):
    font = short(c.fontname)
    raw = c.get_text()
    rec = {'x0': c.x0, 'x1': c.x1, 'base': c.matrix[5], 'sz': round(c.size, 1), 'font': font}
    if font.startswith('Nimbus'):
        t = raw.replace('ﬁ', 'fi').replace('ﬂ', 'fl').replace('ﬀ', 'ff').replace('ﬃ', 'ffi')
        rec.update(t=t, math=False, i='Ital' in font, b='Medi' in font)
    elif font in MATH or font.startswith('MT2'):
        table = MATH.get(font, {})
        if c.cid in table:
            tex, t = table[c.cid]
        elif font in DRAWN:
            tex, t = '', ''
        elif re.fullmatch(r'[A-Za-z0-9]', raw) and font in ('MT2MIT', 'MT2MIS'):
            tex, t = raw, raw
        else:
            print(f'extract_mcs: unknown glyph {font} {c.cid} {raw!r}', file=sys.stderr)
            tex, t = '?', '?'
        rec.update(t=t, tex=tex, math=True, i=False, b=False)
    else:
        rec.update(t=raw, tex=raw, math=True, i=False, b=False)
    return rec


def page_chars(pdf, pages):
    doc = PDFDocument(PDFParser(open(pdf, 'rb')))
    rm = PDFResourceManager()
    dev = extract_jeffe.Dev(rm, laparams=None)
    it = PDFPageInterpreter(rm, dev)
    out = {}
    for n, page in enumerate(PDFPage.create_pages(doc), 1):
        if n not in pages:
            continue
        it.process_page(page)
        out[n] = [char_record(o) for o in extract_jeffe.walk(dev.get_result()) if isinstance(o, LTChar)]
        if n >= max(pages):
            break
    return out


def lines_of(chars):
    """Characters to lines by baseline; smaller type just above or below a line is its script."""
    body = [c for c in chars if c['sz'] >= 9.5]
    small = [c for c in chars if c['sz'] < 9.5]
    groups = []
    for c in sorted(body, key=lambda c: (-c['base'], c['x0'])):
        for g in groups:
            if abs(g['base'] - c['base']) < 1.2:
                g['chars'].append(c)
                break
        else:
            groups.append({'base': c['base'], 'chars': [c]})
    loose = []
    for c in small:
        host = None
        for g in groups:
            d = c['base'] - g['base']
            xs = [o['x1'] for o in g['chars']]
            if -4.5 < d < 5 and min(o['x0'] for o in g['chars']) - 2 <= c['x0'] <= max(xs) + 8:
                host = g
                break
        if host:
            c['sub' if c['base'] < host['base'] else 'sup'] = True
            host['chars'].append(c)
        else:
            loose.append(c)
    for c in loose:   # a line of small type of its own (the labels under an underbrace)
        for g in groups:
            if abs(g['base'] - c['base']) < 1.2 and g.get('small'):
                g['chars'].append(c)
                break
        else:
            groups.append({'base': c['base'], 'chars': [c], 'small': True})
    for g in groups:
        g['chars'].sort(key=lambda c: c['x0'])
        g['x0'] = min(c['x0'] for c in g['chars'])
        g['sz'] = Counter(c['sz'] for c in g['chars']).most_common(1)[0][0]
    groups.sort(key=lambda g: -g['base'])
    return groups


def inline(chars):
    """One line's characters to (html, md): math runs as $TeX$, italics as <em>, word spaces from the gaps."""
    pieces = []          # (kind, text) kind: 'math' | 'em' | 'b' | 'text'
    prev = None
    for c in chars:
        gap = c['x0'] - prev['x1'] if prev else 0
        space = prev is not None and gap > 0.18 * c['sz']
        kind = 'math' if c['math'] else ('b' if c['b'] else ('em' if c['i'] else 'text'))
        tok = c['tex'] if c['math'] else c['t']
        if c['math'] and c.get('sub'):
            tok = '_{' + tok + '}'
        if pieces and pieces[-1][0] == kind:
            sep = ' ' if space else ''
            # a control word before a letter needs its space in TeX
            if kind == 'math' and not sep and re.search(r'\\[A-Za-z]+$', pieces[-1][1]) and re.match(r'[A-Za-z]', tok):
                sep = ' '
            # a subscript continues its base without a space
            pieces[-1] = (kind, pieces[-1][1] + sep + tok)
        else:
            if space:
                pieces.append(('space', ' '))
            pieces.append((kind, tok))
        prev = c
    # merge consecutive subscripts (_{a}_{b} -> _{ab})
    pieces = [(k, re.sub(r'\}_\{', '', t)) if k == 'math' else (k, t) for k, t in pieces]
    h, m = [], []
    for k, t in pieces:
        if k == 'space':
            h.append(' ')
            m.append(' ')
        elif k == 'math':
            t = t.strip()
            h.append('$' + t + '$')
            m.append('$' + t + '$')
        elif k == 'em':
            h.append('<em>' + html.escape(t, quote=False) + '</em>')
            m.append('*' + t + '*')
        elif k == 'b':
            h.append('<strong>' + html.escape(t, quote=False) + '</strong>')
            m.append('**' + t + '**')
        else:
            h.append(html.escape(t, quote=False))
            m.append(t)
    return ''.join(h), ''.join(m)


def join(parts):
    """The lines of one paragraph, each (html, md), joined: a word broken at a line end joins again."""
    h, m = '', ''
    for ph, pm in parts:
        if h.endswith('-') and re.match(r'[a-z]', ph):
            h, m = h[:-1] + ph, m[:-1] + pm
        elif h:
            h, m = h + ' ' + ph, m + ' ' + pm
        else:
            h, m = ph, pm
    # a style run broken at a line end joins again
    for tag in ('em', 'strong'):
        h = h.replace(f'</{tag}> <{tag}>', ' ')
    h = re.sub(r'\$ \$', ' ', h)
    m = re.sub(r'\$ \$', ' ', m)
    # MCS sets Pr in roman before the bracket of its argument: one formula, \Pr[…]
    h = re.sub(r'\bPr\$\[', r'$\\Pr[', h)
    m = re.sub(r'\bPr\$\[', r'$\\Pr[', m)
    return h, m


def elements(pdf, pages, start, stop):
    """The passage from the heading or line that starts with `start` to the one before `stop`, as elements:
    {'kind': 'heading', 'level', 'text'}, {'kind': 'p', 'html', 'md'}, {'kind': 'display', 'key', 'text'}."""
    chars = page_chars(pdf, set(pages))
    items = []
    for n in sorted(chars):
        lines = lines_of(chars[n])
        bodyx = Counter(round(l['x0']) for l in lines if abs(l['sz'] - 10.9) < 0.2 and not l.get('small'))
        left = min(x for x, k in bodyx.items() if k >= 3)
        dn = 0
        prev_display = False
        for l in lines:
            txt = ''.join(c['t'] for c in l['chars'])
            if l['base'] > 700 or re.match(r'^\d+Chapter|^\d+\.\d+\.', txt.replace(' ', '')) and l['base'] > 640:
                continue   # the build stamp and the running head
            visible = [c for c in l['chars'] if c['t'].strip()]
            bold = bool(visible) and all(c['b'] for c in visible)
            if bold and l['sz'] >= 10.8:
                items.append({'kind': 'heading', 'page': n, 'line': l, 'text': ' '.join(plain_words(l['chars']))})
                prev_display = False
                continue
            # set off from the margin (past a paragraph's indent), in small type, or drawn: a display
            drawn = not visible or any(c['font'] in DRAWN for c in l['chars'])
            if l['x0'] > left + 15 or l.get('small') or drawn:
                if not prev_display:
                    dn += 1
                items.append({'kind': 'display', 'page': n, 'key': f'p{n}#{dn}', 'line': l})
                prev_display = True
                continue
            prev_display = False
            indent = abs(l['x0'] - (left + 10.9)) < 2.5
            items.append({'kind': 'indent' if indent else 'body', 'page': n, 'line': l})
    # slice
    def text(it):
        return ''.join(c['t'] for c in it['line']['chars']).replace(' ', '')
    s = next(i for i, it in enumerate(items) if text(it).startswith(start.replace(' ', '')))
    e = next((i for i, it in enumerate(items) if i > s and stop and text(it).startswith(stop.replace(' ', ''))), len(items))
    out, para, disp = [], [], None

    def close():
        nonlocal para
        if para:
            h, m = join(para)
            out.append({'kind': 'p', 'html': h, 'md': m})
        para = []
    for it in items[s:e]:
        k = it['kind']
        if k == 'heading':
            close()
            t = re.sub(r'^\d+(\.\d+)*\s*', '', it['text'])
            level = 3 if re.match(r'^\d+\.\d+\.\d+', it['text']) else 2
            out.append({'kind': 'heading', 'level': level, 'text': t})
            disp = None
        elif k == 'display':
            close()
            if disp is None or disp['key'] != it['key']:
                disp = {'kind': 'display', 'key': it['key'], 'text': []}
                out.append(disp)
            disp['text'].append(''.join(c['t'] for c in it['line']['chars']))
        else:
            if k == 'indent' or disp is not None and False:
                close()
            disp = None
            para.append(inline(it['line']['chars']))
    close()
    return out


def plain_words(chars):
    out, prev = [], None
    w = ''
    for c in chars:
        if prev is not None and c['x0'] - prev['x1'] > 0.18 * c['sz']:
            out.append(w)
            w = ''
        w += c['t']
        prev = c
    out.append(w)
    return out


def parse_pages(spec):
    out = set()
    for part in spec.split(','):
        a, _, b = part.partition('-')
        out.update(range(int(a), int(b or a) + 1))
    return out


if __name__ == '__main__':
    pdf, spec = sys.argv[1], sys.argv[2]
    start = sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].startswith('--') else '19.1'
    for e in elements(pdf, sorted(parse_pages(spec)), start, '19.2'):
        print(e['kind'], e.get('level', ''), e.get('key', ''), e.get('text') if e['kind'] != 'p' else e['html'])
        print()
