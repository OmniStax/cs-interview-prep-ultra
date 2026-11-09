#!/usr/bin/env python3
"""Extract the text of one of Erickson's chapter PDFs (`jeffe`) as styled lines.

The cached `.txt` and `pdftotext` lose every digit, minus sign and small-caps
letter, because the PDF's fonts map those glyphs to no Unicode. The glyphs
themselves are named in each font's /Encoding /Differences (`one.oldstyle`,
`b.sc`, `minus`), so this script reads the PDF with pdfminer at the character
level and decodes every glyph by its name.

Output (JSON, one record per page): the page's lines in reading order, each a
list of runs {t, i, b, sc, sans, sup, sub, sz}, with its baseline, left edge and
body size; the page's boxes (the frames round pseudocode) and rules (the
footnote rule). `build_text.py` turns these into source.md and text.html.

    python3 -I tools/extract_jeffe.py sources/_cache/jeffe/00-intro.pdf 1-16 > /tmp/x.json
    python3 -I tools/extract_jeffe.py sources/_cache/jeffe/00-intro.pdf 4 --show   # a readable dump

Nothing here is specific to one chapter; the chapter's own corrections live in
build_text.py's replacement table.
"""
import json
import re
import sys

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTChar, LTLine, LTRect, LTCurve
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdftypes import resolve1
from pdfminer.psparser import PSLiteral

try:
    from pdfminer.glyphlist import glyphname2unicode
except ImportError:  # pragma: no cover
    glyphname2unicode = {}

# Glyph names the Adobe list lacks or that the fonts spell their own way.
NAMES = {
    'minus': '−', 'arrowleft': '←', 'arrowright': '→', 'greaterequal': '≥', 'lessequal': '≤',
    'floorleft': '⌊', 'floorright': '⌋', 'ceilingleft': '⌈', 'ceilingright': '⌉',
    'multiply': '×', 'angleleft': '⟨', 'angleright': '⟩', 'element': '∈', 'radicallow': '√',
    'radicalbig1': '√', 'aleph': 'ℵ', 'prime': '′', 'ff': 'ff', 'ffi': 'ffi', 'ffl': 'ffl', 'fi': 'fi',
    'fl': 'fl', 'uniFB01': 'fi', 'uniFB02': 'fl', 'summationdisplay': '∑', 'summationtext': '∑',
    'parenleftbig1': '(', 'parenrightbig1': ')', 'slashbig1': '/', 'lscript': 'ℓ',
    'bracelefttp': '{', 'braceex': '', 'braceleftmid': '', 'braceleftbt': '',
    'a12': '☞', 'a110': '☜', 'periodcentered': '·', 'dotmath': '·', 'notequal': '≠',
    'infinity': '∞', 'Theta': 'Θ', 'quoteleft': '‘', 'quoteright': '’',
}
DIGITS = {n: str(i) for i, n in enumerate(
    ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])}


def decode(name):
    """A glyph name to (text, small_caps)."""
    if name is None:
        return None, False
    base, _, suffix = name.partition('.')
    sc = 'sc' in suffix.split('.') or 'c2sc' in suffix.split('.')
    if base in DIGITS:
        return DIGITS[base], False
    if name in NAMES:
        return NAMES[name], False
    if base in NAMES:
        return NAMES[base], sc
    if re.fullmatch(r'uni[0-9A-F]{4}', base):
        return chr(int(base[3:], 16)), sc
    if len(base) == 1:
        return (base.lower() if suffix == 'sc' else base), sc
    u = glyphname2unicode.get(base)
    if u:
        return u, sc
    return None, sc


class Dev(PDFPageAggregator):
    def render_char(self, matrix, font, fontsize, scaling, rise, cid, ncs, gs):
        w = super().render_char(matrix, font, fontsize, scaling, rise, cid, ncs, gs)
        self.cur_item._objs[-1].cid = cid
        return w


def walk(o):
    for x in o:
        if isinstance(x, (LTChar, LTRect, LTLine, LTCurve)):
            yield x
        if hasattr(x, '__iter__') and not isinstance(x, LTChar):
            yield from walk(x)


def differences(page):
    out = {}
    for _, v in resolve1(page.resources.get('Font', {})).items():
        v = resolve1(v)
        enc = resolve1(v.get('Encoding'))
        if isinstance(enc, dict) and enc.get('Differences'):
            m, c = {}, 0
            for x in resolve1(enc['Differences']):
                if isinstance(x, int):
                    c = x
                elif isinstance(x, PSLiteral):
                    m[c] = x.name
                    c += 1
            out[resolve1(v['BaseFont']).name] = m
    return out


def char_record(c, diffs):
    name = diffs.get(c.fontname, {}).get(c.cid)
    t, sc = decode(name)
    raw = c.get_text()
    if t is None:
        t = '' if raw in ('￿', '\x00') else raw
    if raw not in ('￿', '\x00', '') and name is None:
        t = raw
    font = c.fontname.split('+')[-1]
    return {
        't': t, 'x0': c.x0, 'x1': c.x1, 'base': c.matrix[5], 'sz': round(c.size, 1),
        'i': ('Italic' in font or 'Slanted' in font), 'b': 'Bold' in font, 'sc': sc,
        'sans': font.startswith('Roboto'), 'math': font.startswith('MathDesign') or font.startswith('CharterBT'),
        'font': font,
    }


ACCENTS = {'¯': '\u0304', '˙': '\u0307', '´': '\u0301', '`': '\u0300', '˜': '\u0303', 'ˆ': '\u0302', '¨': '\u0308'}


def combine_accents(chars):
    """Fold the spacing accents the PDF draws as glyphs of their own (the macron of al-Khwārizmī, the
    dot under the ḥ of Muḥammad) into the letter they sit over or under, as combining marks."""
    import unicodedata
    letters = [c for c in chars if c['t'] not in ACCENTS and c['t'].strip() and c['t'] != '.']
    plain = [c for c in chars if c['t'] not in ACCENTS]

    def under(cx, base, lo, hi):
        best = None
        for c in letters:
            d = c['base'] - base
            if lo <= d <= hi and c['x0'] - 0.5 <= cx <= c['x1'] + 0.5:
                if best is None or abs((c['x0'] + c['x1']) / 2 - cx) < abs((best['x0'] + best['x1']) / 2 - cx):
                    best = c
        return best

    dropped = set()
    for c in chars:
        cx = (c['x0'] + c['x1']) / 2
        if c['t'] in ACCENTS:
            b = under(cx, c['base'], -0.5, 0.5)
            if b:
                b['t'] += ACCENTS[c['t']]
                dropped.add(id(c))
    # a full stop alone on a baseline a little under a line, inside a letter, is a dot below
    for c in plain:
        if c['t'] != '.':
            continue
        same = [o for o in plain if o is not c and abs(o['base'] - c['base']) < 0.9]
        if same:
            continue
        b = under((c['x0'] + c['x1']) / 2, c['base'], 1.5, 3.5)
        if b:
            b['t'] += '\u0323'
            dropped.add(id(c))
    out = [c for c in chars if id(c) not in dropped]
    for c in out:
        c['t'] = unicodedata.normalize('NFC', c['t'].replace('ı\u0304', 'ī'))
    return out


def lines_of(chars):
    """Group characters into lines by baseline, then fold scripts into their line."""
    chars = sorted(combine_accents(chars), key=lambda c: (-c['base'], c['x0']))
    groups = []
    for c in chars:
        for g in groups:
            if abs(g['base'] - c['base']) < 0.9 and abs(g['sz'] - c['sz']) < 2.2:
                g['chars'].append(c)
                break
        else:
            groups.append({'base': c['base'], 'sz': c['sz'], 'chars': [c]})
    for g in groups:
        sizes = sorted(ch['sz'] for ch in g['chars'])
        g['sz'] = sizes[len(sizes) // 2]
        g['x0'] = min(ch['x0'] for ch in g['chars'])
        g['x1'] = max(ch['x1'] for ch in g['chars'])
    # a group of smaller type close above or below a larger line, inside its extent, is a script of it
    groups.sort(key=lambda g: -g['sz'])
    kept = []
    for g in groups:
        host = None
        for h in kept:
            d = g['base'] - h['base']
            if g['sz'] < 0.86 * h['sz'] and -4.5 < d < 6.5 and g['x0'] >= h['x0'] - 9 and g['x1'] <= h['x1'] + 14:
                host = h
                break
        if host:
            for ch in g['chars']:
                ch['sup' if g['base'] > host['base'] else 'sub'] = True
            host['chars'] += g['chars']
            host['x1'] = max(host['x1'], g['x1'])
        else:
            kept.append(g)
    kept.sort(key=lambda g: -g['base'])
    return kept


STYLE = ('i', 'b', 'sc', 'sans', 'sup', 'sub')


def runs_of(line):
    chars = sorted(line['chars'], key=lambda c: c['x0'])
    runs, prev = [], None
    for c in chars:
        st = {k: bool(c.get(k)) for k in STYLE}
        gap = c['x0'] - prev['x1'] if prev else 0
        # word spaces in this justified type are 0.8 pt and up, kerning stays under 0.7 pt;
        # inside a formula the italic and symbol fonts leave up to 1.7 pt between glyphs
        both_math = prev is not None and c['math'] and prev['math']
        space = prev is not None and gap > (1.7 if both_math else 0.75) * c['sz'] / 10.5
        if runs and space:
            # the space takes the style of the run before it unless the style changes
            runs[-1]['t'] += ' '
        if runs and all(runs[-1][k] == st[k] for k in STYLE):
            runs[-1]['t'] += c['t']
        else:
            runs.append(dict(t=c['t'], **st))
        prev = c
    for r in runs:
        r['t'] = r['t'].replace('ﬁ', 'fi').replace('ﬂ', 'fl').replace('ﬀ', 'ff').replace('ﬃ', 'ffi')
    return [r for r in runs if r['t']]


def extract(pdf, pages):
    f = open(pdf, 'rb')
    doc = PDFDocument(PDFParser(f))
    rm = PDFResourceManager()
    dev = Dev(rm, laparams=None)
    it = PDFPageInterpreter(rm, dev)
    out = []
    for n, page in enumerate(PDFPage.create_pages(doc), 1):
        if n not in pages:
            continue
        diffs = differences(page)
        it.process_page(page)
        lay = dev.get_result()
        chars, boxes, rules = [], [], []
        for o in walk(lay):
            if isinstance(o, LTChar):
                chars.append(char_record(o, diffs))
            elif isinstance(o, LTRect) and o.width > 40 and o.height > 20:
                boxes.append([round(o.x0, 1), round(o.y0, 1), round(o.x1, 1), round(o.y1, 1)])
            elif isinstance(o, (LTLine, LTRect)) and o.height < 1.5 and o.width > 40:
                rules.append([round(o.x0, 1), round(o.y0, 1), round(o.x1, 1)])
        lines = []
        for g in lines_of(chars):
            lines.append({'base': round(g['base'], 1), 'x0': round(g['x0'], 1), 'x1': round(g['x1'], 1),
                          'sz': g['sz'], 'runs': runs_of(g)})
        out.append({'page': n, 'lines': lines, 'boxes': boxes, 'rules': rules})
    return out


def show(pages):
    for p in pages:
        print(f'=== page {p["page"]} boxes={p["boxes"]} rules={p["rules"]}')
        for l in p['lines']:
            s = ''
            for r in l['runs']:
                t = r['t']
                if r['sc']:
                    t = '{sc:' + t + '}'
                if r['i']:
                    t = '_' + t + '_'
                if r['b']:
                    t = '*' + t + '*'
                if r['sup']:
                    t = '^{' + t + '}'
                if r['sub']:
                    t = '_{' + t + '}'
                s += t
            print(f'{l["base"]:6.1f} {l["x0"]:5.1f} {l["sz"]:4.1f} | {s}')


def parse_pages(spec):
    out = set()
    for part in spec.split(','):
        a, _, b = part.partition('-')
        out.update(range(int(a), int(b or a) + 1))
    return out


if __name__ == '__main__':
    pdf, spec = sys.argv[1], sys.argv[2]
    data = extract(pdf, parse_pages(spec))
    if '--show' in sys.argv:
        show(data)
    else:
        json.dump(data, sys.stdout, ensure_ascii=False)
