#!/usr/bin/env python3
"""Assemble a section's source.md and text.html from the sources, by script.

The source's words are never typed by hand. Each block of the page is read out
of its source by a converter and assembled here:

- Erickson (`jeffe`): tools/extract_jeffe.py reads the chapter PDF glyph by
  glyph; this script lays the lines out as headings, paragraphs, lists, quotes,
  pseudocode, display maths and footnotes, and drops what belongs to a figure.
- Open Data Structures (`ods`): a small LaTeX reader for the constructs ODS's
  prose uses (sections, \\paragraph, \\emph, maths, #code#, \\footnote, refs).

What a section needs beyond that lives in its `build_spec.py`, beside its
plan.md: the blocks (source, locator, where each starts and stops), the small
replacement table for what the extraction gets wrong (a display formula the
PDF draws in pieces, a word the PDF splits), the figures and where they stand,
and the spans that mark concepts and referents. The replacement table is the
only place text is written by hand, and each entry says why.

    python3 -I tools/build_text.py ch01/1.1            # writes source.md, text.html, footnotes.json
    python3 -I tools/build_text.py ch01/1.1 --check    # also lists every line-end hyphen it joined

`footnotes.json` and `captions.json` (beside the section, not shipped) carry the
book footnotes the blocks use and the figures' printed captions, for
tools/build_section.py to write into section.json.
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
import extract_jeffe  # noqa: E402

SC_STYLE = 'font-variant:small-caps'


# ---------------------------------------------------------------- inline runs

def esc(s):
    return html.escape(s, quote=False).replace('$', '&#36;')


def merge_small_caps(runs):
    """Erickson sets procedure names in small caps: a capital in the roman font, then the rest of the
    word as small-cap glyphs (B + ottles, O + f, B + eer). Pull each capital into the small-caps run
    after it and join the pieces of one name."""
    out = [dict(r) for r in runs]
    for i, r in enumerate(out):
        if r['sc'] and i > 0 and not out[i - 1]['sc']:
            m = re.search(r'([A-Z])$', out[i - 1]['t'])
            if m:
                out[i - 1]['t'] = out[i - 1]['t'][:-1]
                r['t'] = m.group(1) + r['t']
    merged = []
    for r in out:
        if not r['t']:
            continue
        if merged and r['sc'] and merged[-1]['sc'] and not merged[-1]['t'].endswith(' '):
            merged[-1]['t'] += r['t']
        else:
            merged.append(r)
    return merged


def runs_html(runs, notes=None, page=None):
    """Runs to inline HTML. A superscript number standing where the page has that footnote is the
    footnote's marker."""
    out = []
    for r in merge_small_caps(runs):
        t = r['t']
        trail = ''
        if t.endswith(' '):
            t, trail = t.rstrip(' '), ' '
        num = t.strip()
        if r['sup'] and notes is not None and num.isdigit() and num in notes:
            out.append(f'<sup class="fn" data-note="{notes[num]}"></sup>' + trail)
            continue
        s = esc(t)
        if r['sc']:
            s = f'<span style="{SC_STYLE}">{s}</span>'
        if r['i']:
            s = f'<em>{s}</em>'
        if r['b']:
            s = f'<strong>{s}</strong>'
        if r['sup']:
            s = f'<sup>{s}</sup>'
        if r['sub']:
            s = f'<sub>{s}</sub>'
        out.append(s + trail)
    h = tidy(''.join(out))
    # adjacent runs of one style that the PDF split (an italic word broken by a kern) join again
    for tag in ('em', 'strong', 'sup', 'sub'):
        h = h.replace(f'</{tag}><{tag}>', '')
    return h


def tidy(h):
    """What the glyph-by-glyph reading leaves untidy, fixed the same way everywhere: a style the PDF
    broke at a space or a line end joins again; a formula's operators stand between single spaces, as
    Erickson sets them; no space before punctuation after a formula."""
    for tag in ('em', 'strong'):
        h = h.replace(f'</{tag}> <{tag}>', ' ')
    parts = re.split(r'(<[^>]+>)', h)
    for i, p in enumerate(parts):
        if p.startswith('<'):
            continue
        p = re.sub(r'\s*([−=≥≤←])\s*', r' \1 ', p)
        p = re.sub(r'(?<=\S)\s*\+\s*(?=\S)', ' + ', p)
        p = re.sub(r'\s*\.\.\s*', ' .. ', p)
        p = re.sub(r'\.\. \.\.', '. . . .', p)
        parts[i] = p
    h = ''.join(parts)
    # an operator at the very start or end of a text piece next to a tag keeps one space only
    h = re.sub(r'  +', ' ', h)
    h = re.sub(r'(</em>|</sub>|</sup>|\)) ([.,;:])', r'\1\2', h)
    h = re.sub(r'\( ', '(', h)
    return h


def runs_md(runs, notes=None):
    out = []
    for r in merge_small_caps(runs):
        t = r['t']
        trail = ''
        if t.endswith(' '):
            t, trail = t.rstrip(' '), ' '
        num = t.strip()
        if r['sup'] and notes is not None and num.isdigit() and num in notes:
            out.append(f'[^{num}]' + trail)
            continue
        if r['sc']:
            t = t  # small caps read as the name itself
        if r['i'] and t:
            t = f'*{t}*'
        if r['b'] and t:
            t = f'**{t}**'
        if r['sup']:
            t = f'^{t}^'
        if r['sub']:
            t = f'~{t}~'
        out.append(t + trail)
    return ''.join(out).replace('**', '**').replace('*  *', ' ')


def plain(runs):
    return ''.join(r['t'] for r in merge_small_caps(runs))


# ---------------------------------------------------------------- Erickson: lines to elements

def page_geometry(page):
    """The page's left margin (the most common start of a body line), its footnote rule and its boxes."""
    from collections import Counter
    body = [round(l['x0']) for l in page['lines'] if 10.0 <= l['sz'] <= 11.0]
    left = Counter(body).most_common(1)[0][0] if body else 54
    fnrule = None
    for x0, y, x1 in page['rules']:
        if abs(x0 - left) < 2 and 130 < x1 - x0 < 160 and y < 400:
            fnrule = y
    # a box is a pair of rules with the same extent, the frame round a listing
    boxes = []
    rs = sorted(page['rules'], key=lambda r: -r[1])
    for i, a in enumerate(rs):
        for b in rs[i + 1:]:
            if abs(a[0] - b[0]) < 0.6 and abs(a[2] - b[2]) < 0.6 and a[2] - a[0] < 340 and a[1] - b[1] > 20:
                boxes.append((a[0], b[1], a[2], a[1]))
                break
    return left, fnrule, boxes


def in_box(line, boxes):
    for x0, y0, x1, y1 in boxes:
        if y0 < line['base'] < y1 and x0 - 2 <= line['x0'] <= x1:
            return (x0, y0, x1, y1)
    return None


def is_caption(line):
    r = line['runs']
    return bool(r) and r[0]['sans'] and r[0]['b'] and plain(r).startswith('Figure ')


def is_heading(line):
    rs = [r for r in line['runs'] if r['t'].strip()]
    return bool(rs) and all(r['sans'] and r['b'] for r in rs) and line['sz'] >= 10.6


def classify(pages):
    """The pages' lines as a flat list of items in reading order: ('line', page, line, kind) with kind
    one of body, indent, heading, item, quote, pre, display, caption, fig, footnote, drop."""
    items = []
    for page in pages:
        left, fnrule, boxes = page_geometry(page)
        lines = page['lines']
        # a box with a caption right under it is a figure: everything in it is the figure's
        caption_bases = [l['base'] for l in lines if is_caption(l)]
        fig_boxes = [b for b in boxes if any(0 < b[1] - c < 45 for c in caption_bases)]
        for l in lines:
            kind = None
            if l['base'] > 640 or (l['base'] < 35 and len(plain(l['runs'])) <= 3):
                kind = 'drop'
            elif fnrule is not None and l['base'] < fnrule and l['sz'] < 9.5:
                kind = 'footnote'
            elif is_caption(l):
                kind = 'caption'
            elif is_heading(l):
                kind = 'heading'
            elif in_box(l, fig_boxes):
                kind = 'fig'
            elif in_box(l, boxes):
                kind = 'pre'
            elif l['sz'] < 9.5 and any(r['sans'] for r in l['runs']) and l['x0'] > left + 20 and not in_box(l, boxes):
                kind = 'quote' if l['sz'] >= 8.9 else 'fig'
            elif l['sz'] < 9.5:
                kind = 'fig'
            elif plain(l['runs']).startswith('•'):
                kind = 'item'
            elif abs(l['x0'] - (left + 17)) < 2.5:
                kind = 'indent'
            elif abs(l['x0'] - left) < 2.5:
                kind = 'body'
            elif l['x0'] > left + 30 or len(plain(l['runs']).strip()) < 6:
                kind = 'display'
            elif abs(l['x0'] - (left + 5.3)) < 1.5:
                kind = 'cont'   # a list item's second line
            else:
                kind = 'body'
            items.append({'page': page['page'], 'line': l, 'kind': kind, 'left': left})
    return items


def join_lines(lines, keep_hyphen, joined):
    """Lines of one paragraph to one list of runs: a word broken at a line end joins up again."""
    runs = []
    for l in lines:
        rs = [dict(r) for r in l['runs']]
        if not rs:
            continue
        if runs:
            last = runs[-1]
            lt = last['t'].rstrip()
            first = rs[0]['t'].lstrip()
            if lt.endswith('-') and first[:1].islower():
                word = re.search(r'(\S*)-$', lt).group(1) + '-' + re.match(r'(\S*)', first).group(1)
                joined.append(word)
                if any(word.startswith(k) for k in keep_hyphen):
                    last['t'] = lt
                else:
                    last['t'] = lt[:-1]
            elif lt.endswith(('—', '/')) and not lt.endswith('//'):
                last['t'] = lt
            else:
                last['t'] = lt + ' '
            rs[0]['t'] = first
        runs.extend(rs)
    if runs:
        runs[-1]['t'] = runs[-1]['t'].rstrip()
    return runs


def pre_text(lines):
    """A pseudocode box as text, its indentation read off the left edges of its lines."""
    xs = sorted(set(round(l['x0'], 0) for l in lines[1:])) or [lines[0]['x0']]
    base = xs[0]
    out = []
    for i, l in enumerate(lines):
        t = re.sub(r'\s*\.\.\s*', ' .. ', plain(l['runs']).rstrip())
        if i == 0:
            out.append(t)
        else:
            level = max(0, round((l['x0'] - base) / 19.1))
            out.append('  ' + '    ' * level + t)
    return out


def elements(items, notes_by_page, keep_hyphen, joined):
    """Items to elements: heading, p, li, quote, pre, display, caption. A paragraph that a figure or a
    page turn interrupts mid-sentence carries on."""
    els = []
    cur = None

    def close():
        nonlocal cur
        if cur:
            els.append(cur)
        cur = None

    i = 0
    while i < len(items):
        it = items[i]
        k, l = it['kind'], it['line']
        if k in ('drop', 'footnote', 'fig'):
            i += 1
            continue
        if k == 'caption':
            close()
            grp = [l]
            j = i + 1
            while j < len(items) and items[j]['kind'] in ('fig', 'quote') and items[j]['line']['sz'] < 8.5 and items[j]['page'] == it['page']:
                grp.append(items[j]['line'])
                j += 1
            els.append({'kind': 'caption', 'page': it['page'], 'lines': grp})
            i = j
            continue
        if k == 'heading':
            close()
            els.append({'kind': 'heading', 'page': it['page'], 'lines': [l], 'level': 2 if l['sz'] >= 12 else 3})
            i += 1
            continue
        if k == 'pre':
            close()
            grp = [l]
            j = i + 1
            while j < len(items) and items[j]['kind'] == 'pre':
                grp.append(items[j]['line'])
                j += 1
            els.append({'kind': 'pre', 'page': it['page'], 'lines': grp})
            i = j
            continue
        if k == 'display':
            close()
            grp = [l]
            j = i + 1
            while j < len(items) and items[j]['kind'] == 'display' and items[j]['page'] == it['page']:
                grp.append(items[j]['line'])
                j += 1
            n = sum(1 for e in els if e['kind'] == 'display' and e['page'] == it['page']) + 1
            els.append({'kind': 'display', 'page': it['page'], 'lines': grp, 'key': f'p{it["page"]}#{n}'})
            i = j
            continue
        if k == 'quote':
            if cur and cur['kind'] == 'quote' and l['x0'] < cur['lines'][0]['x0'] - 5:
                cur['lines'].append(l)
            else:
                close()
                cur = {'kind': 'quote', 'page': it['page'], 'lines': [l]}
            i += 1
            continue
        if k == 'item':
            close()
            cur = {'kind': 'li', 'page': it['page'], 'lines': [l]}
            i += 1
            continue
        if k == 'cont' and cur and cur['kind'] == 'li':
            cur['lines'].append(l)
            i += 1
            continue
        # body or indent
        starts_new = k == 'indent'
        if not starts_new and cur and cur['kind'] == 'p':
            cur['lines'].append(l)
        elif not starts_new and cur is None and els:
            # after a figure, a display or a page turn: carry on the last paragraph if it stopped mid-sentence
            prev = next((e for e in reversed(els) if e['kind'] in ('p', 'display', 'pre', 'caption', 'heading', 'li', 'quote')), None)
            first = plain(l['runs']).lstrip()[:1]
            last_p = next((e for e in reversed(els) if e['kind'] == 'p'), None)
            if prev is not None and prev['kind'] in ('caption',) and last_p is not None and first.islower():
                els.remove(last_p)
                cur = last_p
                cur['lines'].append(l)
            elif prev is not None and prev['kind'] == 'p' and first.islower():
                els.remove(prev)
                cur = prev
                cur['lines'].append(l)
            else:
                cur = {'kind': 'p', 'page': it['page'], 'lines': [l], 'after_display': prev is not None and prev['kind'] in ('display', 'pre')}
        else:
            close()
            cur = {'kind': 'p', 'page': it['page'], 'lines': [l]}
        i += 1
    close()
    return els


def footnotes(items, keep_hyphen, joined):
    """The footnotes of the pages, by number: each starts with its superscript number."""
    notes = {}
    order = []
    cur = None
    for it in items:
        if it['kind'] != 'footnote':
            continue
        l = it['line']
        rs = l['runs']
        if rs and rs[0]['sup'] and rs[0]['t'].strip().isdigit():
            num = rs[0]['t'].strip()
            cur = {'num': num, 'page': it['page'], 'lines': [dict(l, runs=rs[1:])]}
            notes[num] = cur
            order.append(num)
        elif cur:
            cur['lines'].append(l)
    for n in order:
        notes[n]['runs'] = join_lines(notes[n]['lines'], keep_hyphen, joined)
    return notes


# ---------------------------------------------------------------- ODS LaTeX

def ods_tex(path, first, last, spec):
    """Lines first..last (1-based, inclusive) of an ODS .tex file to elements."""
    src = open(path, encoding='utf-8').read().split('\n')[first - 1:last]
    text = '\n'.join(l for l in src if not l.lstrip().startswith('%'))
    text = re.sub(r'\\index\{[^{}]*(\{[^{}]*\}[^{}]*)*\}%?\n?', '', text)
    text = re.sub(r'\\(sec|fig)label\{[^}]*\}\n?', '', text)
    paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    els = []
    for p in paras:
        m = re.match(r'\\section\{(.*?)\}\s*(.*)', p, re.S)
        if m:
            els.append({'kind': 'heading', 'level': 2, 'tex': m.group(1)})
            p = m.group(2).strip()
            if not p:
                continue
        els.append({'kind': 'p', 'tex': ' '.join(p.split())})
    return els


def ods_inline(tex, spec, notes, ctx):
    """ODS's inline LaTeX to HTML, and to Markdown. #x# is ODS's mark for code; in maths it is the
    variable itself."""
    md = tex
    h = tex

    def math(m):
        body = m.group(1)
        body = re.sub(r'#(\w+)#', r'\1', body)
        return '\x00' + body + '\x01'
    h = re.sub(r'\$(.+?)\$', math, h)
    md = h
    # footnotes
    def fn(m):
        ctx['fn'] += 1
        nid = f'ods-fn-{ctx["fn_id"]}'
        ctx['fn_id'] += 1
        notes.append({'id': nid, 'number': str(ctx['fn']), 'tex': m.group(1)})
        return f'\x02{nid}\x03'
    h = re.sub(r'\\footnote\{((?:[^{}]|\{[^{}]*\})*)\}', fn, h)
    for k, v in spec.get('ODS_REFS', {}).items():
        h = h.replace(k, '\x04' + k + '\x05')
    h = esc(h)
    h = re.sub(r'\\paragraph\{(.*?)\}', r'<strong>\1</strong>', h)
    h = re.sub(r'\\emph\{(.*?)\}', r'<em>\1</em>', h)
    # the pseudocode edition (METHOD decision 20) sets a capitalised #Name# as plain text and any other
    # #code# as maths (latex/snarf-python.py, code_subs)
    h = re.sub(r'#([A-Z]\w*)#', r'\1', h)
    h = re.sub(r'#(\w+)#', r'$\1$', h)
    h = h.replace('``', '“').replace("''", '”').replace('---', '—').replace('--', '–').replace('~', ' ')
    h = re.sub(r"(\w)'(\w)", r'\1’\2', h)
    h = re.sub(r'\x00(.*?)\x01', lambda m: '$' + m.group(1) + '$', h)
    h = re.sub(r'\x02(.*?)\x03', r'<sup class="fn" data-note="\1"></sup>', h)
    h = re.sub(r'\x04(.*?)\x05', lambda m: spec['ODS_REFS'][m.group(1)][0], h)
    md = re.sub(r'\x00(.*?)\x01', lambda m: '$' + m.group(1) + '$', md)
    md = re.sub(r'\\footnote\{((?:[^{}]|\{[^{}]*\})*)\}', lambda m: '[^ods]', md)
    md = re.sub(r'\\paragraph\{(.*?)\}', r'**\1**', md)
    md = re.sub(r'\\emph\{(.*?)\}', r'*\1*', md)
    md = re.sub(r'#([A-Z]\w*)#', r'\1', md)
    md = re.sub(r'#(\w+)#', r'$\1$', md)
    for k, v in spec.get('ODS_REFS', {}).items():
        md = md.replace(k, v[1])
    md = md.replace('``', '“').replace("''", '”').replace('~', ' ')
    md = re.sub(r"(\w)'(\w)", r'\1’\2', md)
    return h.strip(), md.strip()


# ---------------------------------------------------------------- assembly

def apply_fixes(s, fixes, where, used):
    for i, (old, new, why) in enumerate(fixes):
        if old in s:
            s = s.replace(old, new)
            used.add(i)
    return s


def outside_tags(h, old, new, count=1):
    """Replace old with new in the text of h, never inside a tag, at most count times."""
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


def build(sec_dir, check=False):
    spec_path = os.path.join(sec_dir, 'build_spec.py')
    sp = importlib.util.spec_from_file_location('build_spec', spec_path)
    spec_mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(spec_mod)
    spec = {k: getattr(spec_mod, k) for k in dir(spec_mod) if k.isupper()}

    keep = spec.get('KEEP_HYPHEN', [])
    fixes = spec.get('FIXES', [])
    used = set()
    joined = []

    # Erickson's chapter, once
    jeffe_els, jeffe_notes = [], {}
    if any(b['source'] == 'jeffe' for b in spec['BLOCKS']):
        pdf = os.path.join(BOOK, spec['JEFFE_PDF'])
        pages = extract_jeffe.extract(pdf, set(spec['JEFFE_PAGES']))
        items = classify(pages)
        for it in items:
            for ov in spec.get('KIND_OVERRIDES', []):
                if it['page'] == ov[0] and abs(it['line']['base'] - ov[1]) < 0.6:
                    it['kind'] = ov[2]
        jeffe_notes = footnotes(items, keep, joined)
        jeffe_els = elements(items, None, keep, joined)

    note_ids = {n: f'jeffe-fn-{n}' for n in jeffe_notes}
    # the figures' captions as the book prints them, by number, for {{caption N}} and {{caption-text N}}
    captions = {}
    for e in jeffe_els:
        if e['kind'] == 'caption':
            runs = join_lines(e['lines'], keep, joined)
            m = re.match(r'Figure (\d+\.\d+)\.\s*', plain(runs))
            if m:
                h = apply_fixes(runs_html(runs), fixes, 'caption', used)
                h = re.sub(r'^<strong>Figure \d+\.\d+\.\s*</strong>\s*', '', h)
                captions[m.group(1)] = {'html': h, 'text': re.sub(r'<[^>]+>', '', h)}

    def fill(s):
        s = re.sub(r'\{\{caption-text ([\d.]+)\}\}', lambda m: html.escape(captions[m.group(1)]['text']), s)
        return re.sub(r'\{\{caption ([\d.]+)\}\}', lambda m: captions[m.group(1)]['html'], s)
    spec['HTML'] = {k: fill(v) for k, v in spec.get('HTML', {}).items()}
    used_notes = []
    md_blocks, html_blocks, ods_notes = [], [], []
    ctx = {'fn': 0, 'fn_id': 1}
    displays = spec.get('DISPLAYS', {})

    for b in spec['BLOCKS']:
        hparts, mparts = [], []
        if b['source'] == 'jeffe':
            # slice the elements from the one whose text holds `from` to the one before `to`
            def text_of(e):
                if e['kind'] in ('p', 'li', 'quote', 'heading', 'caption'):
                    return plain(join_lines(e['lines'], keep, []))
                if e['kind'] == 'pre':
                    return '\n'.join(pre_text(e['lines']))
                return e.get('key', '')
            start = next(i for i, e in enumerate(jeffe_els) if b['from'] in text_of(e))
            stop = next((i for i, e in enumerate(jeffe_els) if i > start and b['to'] and b['to'] in text_of(e)), len(jeffe_els))
            els = jeffe_els[start:stop]
            if b.get('drop_first_heading') and els and els[0]['kind'] == 'heading':
                els = els[1:]
            drop = b.get('drop_headings', [])
            els = [e for e in els if not (e['kind'] == 'heading' and text_of(e) in drop)]
            # a block that starts or stops inside a paragraph cuts it there
            hparts.append(f'<h2>{esc(b["h2"])}</h2>')
            mparts.append(f'## {b["h2"]}')
            list_open = False
            for e in els:
                k = e['kind']
                if k != 'li' and list_open:
                    hparts.append('</ul>')
                    list_open = False
                if k == 'caption':
                    continue   # a figure's caption is its row's original_caption
                if k == 'heading':
                    runs = join_lines(e['lines'], keep, joined)
                    t = plain(runs).strip()
                    t = re.sub(r'^\d+\.\d+\s+', '', t)
                    hparts.append(f'<h{e["level"] + (1 if e["level"] == 2 else 0)}>{esc(t)}</h{e["level"] + (1 if e["level"] == 2 else 0)}>')
                    mparts.append('### ' + t)
                    continue
                if k == 'pre':
                    lines = pre_text(e['lines'])
                    key = lines[0]
                    if key in spec.get('PRE_AS_FIGURE', {}):
                        fid = spec['PRE_AS_FIGURE'][key]
                        hparts.append(f'<pre data-pseudocode="{fid}">' + esc('\n'.join(apply_fixes('\n'.join(lines), fixes, 'pre', used).split('\n'))) + '</pre>')
                    else:
                        hparts.append('<pre>' + esc(apply_fixes('\n'.join(lines), fixes, 'pre', used)) + '</pre>')
                    mparts.append('```\n' + apply_fixes('\n'.join(lines), fixes, 'pre', used) + '\n```')
                    for after in spec.get('AFTER_PRE', {}).get(key, []):
                        hparts.append(spec['HTML'][after])
                        mparts.append(f'[{after}]')
                    continue
                if k == 'display':
                    tex = displays.get(e['key'])
                    if tex is None:
                        print(f'MISSING DISPLAY {b["id"]} {e["key"]}: ' + ' / '.join(plain(l['runs']) for l in e['lines']), file=sys.stderr)
                        tex = r'\text{(missing)}'
                    hparts.append(f'$${tex}$$')
                    mparts.append(f'$${tex}$$')
                    continue
                runs = join_lines(e['lines'], keep, joined)
                if k == 'li':
                    runs[0]['t'] = runs[0]['t'].lstrip('• ')
                body_h = runs_html(runs, note_ids)
                body_m = runs_md(runs, {n: n for n in jeffe_notes})
                body_h = apply_fixes(body_h, fixes, b['id'], used)
                body_m = apply_fixes(body_m, fixes, b['id'], used)
                for m in re.findall(r'data-note="(jeffe-fn-\d+)"', body_h):
                    used_notes.append(m)
                if k == 'li':
                    if not list_open:
                        hparts.append('<ul>')
                        list_open = True
                    hparts.append(f'<li>{body_h}</li>')
                    mparts.append('- ' + body_m)
                elif k == 'quote':
                    hparts.append(f'<blockquote><p>{body_h}</p></blockquote>')
                    mparts.append('> ' + body_m)
                else:
                    hparts.append(f'<p>{body_h}</p>')
                    mparts.append(body_m)
            if list_open:
                hparts.append('</ul>')
        elif b['source'] == 'ods':
            path = os.path.join(BOOK, b['file'])
            first, last = b['lines']
            for e in ods_tex(path, first, last, spec):
                if e['kind'] == 'heading':
                    continue
                h, m = ods_inline(e['tex'], spec, ods_notes, ctx)
                h = apply_fixes(h, fixes, b['id'], used)
                hparts.append(f'<p>{h}</p>')
                mparts.append(m)
            hparts.insert(0, f'<h2>{esc(b["h2"])}</h2>')
            mparts.insert(0, f'## {b["h2"]}')
        # figures placed after a paragraph
        body = '\n'.join(hparts)
        placed = {}
        for anchor, key in spec.get('AFTER_TEXT', {}).get(b['id'], []):
            idx = body.find(anchor)
            if idx < 0:
                raise SystemExit(f'{b["id"]}: anchor {anchor!r} for {key} not found')
            # a second figure after the same paragraph stands after the first
            end = placed.get(anchor) or body.find('</p>', idx) + len('</p>')
            ins = '\n' + spec['HTML'][key]
            body = body[:end] + ins + body[end:]
            placed[anchor] = end + len(ins)
        # spans: concepts, referents, introducing ids
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
        md_blocks.append(f'<!-- block {b["id"]} · source {b["source"]} · {b["locator"]} -->\n\n' + '\n\n'.join(mparts))

    # the footnotes the blocks use, in the order their markers stand
    seen = []
    for n in used_notes:
        if n not in seen:
            seen.append(n)
    fn_rows = []
    for nid in seen:
        num = nid.rsplit('-', 1)[1]
        h = apply_fixes(runs_html(jeffe_notes[num]['runs']), fixes, 'fn', used)
        fn_rows.append({'id': nid, 'kind': 'book', 'number': num, 'html': h, 'source': 'jeffe'})
    for n in ods_notes:
        h, _ = ods_inline(n['tex'], spec, [], dict(ctx))
        fn_rows.append({'id': n['id'], 'kind': 'book', 'number': n['number'], 'html': h, 'source': 'ods'})

    md_notes = []
    for nid in seen:
        num = nid.rsplit('-', 1)[1]
        md_notes.append(f'[^{num}]: ' + apply_fixes(runs_md(jeffe_notes[num]['runs']), fixes, 'fn', used))
    for n in ods_notes:
        md_notes.append(f'[^ods]: ' + n['tex'])

    title = spec['TITLE']
    md = f'# {title}\n\n' + '\n\n'.join(md_blocks) + '\n\n## Footnotes\n\n' + '\n\n'.join(md_notes) + '\n'
    open(os.path.join(sec_dir, 'source.md'), 'w').write(md)
    open(os.path.join(sec_dir, 'text.html'), 'w').write('\n\n'.join(html_blocks) + '\n')
    json.dump(fn_rows, open(os.path.join(sec_dir, 'footnotes.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(captions, open(os.path.join(sec_dir, 'captions.json'), 'w'), ensure_ascii=False, indent=1)

    unused = [fixes[i][0] for i in range(len(fixes)) if i not in used]
    if unused:
        print('FIXES never applied:', unused, file=sys.stderr)
    if check:
        print('hyphens joined:', file=sys.stderr)
        for w in sorted(set(joined)):
            print('  ', w, file=sys.stderr)
    print(f'{sec_dir}: {len(html_blocks)} blocks, {len(fn_rows)} footnotes', file=sys.stderr)


if __name__ == '__main__':
    build(os.path.abspath(sys.argv[1]), '--check' in sys.argv)
