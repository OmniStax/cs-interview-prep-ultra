#!/usr/bin/env python3
"""Assemble a translated section's source.md and text.html: OI Wiki blocks, by script.

OI Wiki (`oiwiki`, CC BY-SA 4.0 + SATA, METHOD decision 15) is Chinese Markdown with KaTeX. A section
whose blocks come from it is built in two halves that never mix:

- **The source**, read by script. Each block of the spec is a slice of the page's Markdown, from one
  heading (inclusive) to another (exclusive), cut here and written to `source.md` verbatim under its
  marker line. Nothing of the Chinese is typed.
- **The translation**, written by the translator into `translation.md` beside the spec: the same
  marker lines, and under each the block in English, element for element (a paragraph for a paragraph,
  an item for an item, a display for a display; translate.md item 3). A code block of the source that is
  outside OI Wiki's licence is not translated: the translation puts `[[<html key>]]` in its place, the
  figure that is drawn from the prose's numbers.

The parity check compares the two halves block by block: the same elements in the same order (headings
the spec drops aside), and the same inline and display maths, character for character (within an element in any order, since
English may order the words of a sentence differently). It fails the
build on any difference, so a sentence cannot be lost or a formula changed in translation.

Then `text.html` is made from the translation, as `tools/build_text.py` makes it from its converters:
the block's `<h2>` (the spec's where the source's heading does not name the concept), its deeper
headings as `<h3>`, the figures and derivations the spec places (`AT`: a placeholder or after an
element; `REPLACE`: a run of elements a derivation replaces, root rule 29.2; `DROP`: list items whose
lines a derivation now carries), the spans of `MARKS`, and the translation's AI mark on the block
(`data-ai`, the model and effort, as a code set's translated variant carries it). The page's footnotes
(`[^name]: …` at its end) are written to `footnotes.json` in the source's words, numbered in the order
their markers first stand on the page, as OI Wiki's renderer numbers them.

    python3 -I tools/build_translation.py ch01/1.5            # writes source.md, text.html, footnotes.json, captions.json
    python3 -I tools/build_translation.py ch01/1.5 --check    # also prints each block's parity table
"""
import html
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(HERE)

MARKER = re.compile(r'^<!-- block (\S+) · source (\S+) · (.*) -->$')


# ---------------------------------------------------------------- the source: slices of the page

def page_lines(path):
    return open(path, encoding='utf-8').read().split('\n')


def slice_block(lines, b):
    """The lines of one block: from the line that is heading `from` to the line before heading `to`."""
    def at(h):
        for i, l in enumerate(lines):
            if l.strip() == h:
                return i
        raise SystemExit(f'{b["id"]}: heading {h!r} is not on the page')
    a = at(b['from'])
    z = at(b['to']) if b.get('to') else len(lines)
    if z <= a:
        raise SystemExit(f'{b["id"]}: {b["to"]!r} does not come after {b["from"]!r}')
    out = lines[a:z]
    while out and not out[-1].strip():
        out.pop()
    return out


def page_footnotes(lines):
    """`[^name]: text` definitions, as the page writes them."""
    notes = {}
    for l in lines:
        m = re.match(r'^\[\^([^\]]+)\]:\s*(.*)$', l)
        if m:
            notes[m.group(1)] = m.group(2).strip()
    return notes


# ---------------------------------------------------------------- Markdown (the subset OI Wiki writes) to elements

def parse(lines):
    """Lines to elements: heading, p, display, code, table, list (nested items), slot (a [[key]] line)."""
    els, i = [], 0
    n = len(lines)
    while i < n:
        l = lines[i]
        s = l.strip()
        if not s:
            i += 1
            continue
        m = re.match(r'^(#{2,6})\s+(.*)$', s)
        if m:
            els.append({'kind': 'heading', 'level': len(m.group(1)), 'text': m.group(2).strip()})
            i += 1
            continue
        m = re.match(r'^\[\[([\w-]+)\]\]$', s)
        if m:
            els.append({'kind': 'slot', 'key': m.group(1)})
            i += 1
            continue
        if s.startswith('```'):
            j = i + 1
            while j < n and not lines[j].strip().startswith('```'):
                j += 1
            els.append({'kind': 'code', 'text': '\n'.join(lines[i + 1:j])})
            i = j + 1
            continue
        if s.startswith('$$'):
            body = s[2:]
            j = i
            if body.endswith('$$') and len(body) > 2:
                tex = body[:-2]
            else:
                j = i + 1
                acc = [body] if body else []
                while j < n and not lines[j].strip().endswith('$$'):
                    acc.append(lines[j].strip())
                    j += 1
                last = lines[j].strip()[:-2] if j < n else ''
                if last:
                    acc.append(last)
                tex = ' '.join(x for x in acc if x)
            els.append({'kind': 'display', 'tex': tex.strip()})
            i = j + 1
            continue
        if s.startswith('|'):
            rows = []
            while i < n and lines[i].strip().startswith('|'):
                rows.append(lines[i].strip())
                i += 1
            cells = [split_row(r) for r in rows]
            body = [c for c in cells[2:]]
            els.append({'kind': 'table', 'head': cells[0], 'rows': body})
            continue
        if re.match(r'^\s*(\d+\.|-)\s+', l):
            items, i = parse_list(lines, i, indent_of(l))
            els.append({'kind': 'list', 'ordered': bool(re.match(r'^\s*\d+\.', l)), 'items': items})
            continue
        acc = [s]
        i += 1
        while i < n and lines[i].strip() and not re.match(r'^(#{2,6}\s|\$\$|```|\||\s*(\d+\.|-)\s+)', lines[i].strip()):
            acc.append(lines[i].strip())
            i += 1
        els.append({'kind': 'p', 'text': ' '.join(acc)})
    return els


def split_row(r):
    """A table row's cells; a | inside maths (\\lvert written as |) is not a cell boundary."""
    inner = r.strip().strip('|')
    cells, cur, math = [], '', False
    for ch in inner:
        if ch == '$':
            math = not math
        if ch == '|' and not math:
            cells.append(cur.strip())
            cur = ''
        else:
            cur += ch
    cells.append(cur.strip())
    return cells


def indent_of(l):
    return len(l) - len(l.lstrip(' '))


def parse_list(lines, i, base):
    """Items at indent `base`; an item's continuation and its sublists are indented deeper."""
    items, n = [], len(lines)
    while i < n:
        l = lines[i]
        if not l.strip():
            # a blank line inside a list: the list goes on if the next line is an item or a continuation
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            if j < n and indent_of(lines[j]) >= base and re.match(r'^\s*(\d+\.|-)\s+', lines[j]) or (j < n and indent_of(lines[j]) > base):
                i = j
                continue
            break
        ind = indent_of(l)
        m = re.match(r'^\s*(\d+\.|-)\s+(.*)$', l)
        if m and ind == base:
            items.append({'text': m.group(2).strip(), 'sub': []})
            i += 1
            continue
        if m and ind > base and items:
            sub, i = parse_list(lines, i, ind)
            items[-1]['sub'].append({'ordered': bool(re.match(r'^\s*\d+\.', l)), 'items': sub})
            continue
        if ind > base and items:
            items[-1]['text'] += ' ' + l.strip()
            i += 1
            continue
        break
    return items, i


# ---------------------------------------------------------------- parity

MATH = re.compile(r'(?<!\\)\$([^$]+?)(?<!\\)\$')


def maths(text):
    return MATH.findall(text)


def shape(els, drop=()):
    """The block as a flat list of (kind, maths) entries, for comparing the two halves."""
    out = []

    def items(lst, depth):
        for it in lst['items']:
            out.append((f'li{depth}', maths(it['text'])))
            for s in it['sub']:
                items(s, depth + 1)
    for e in els:
        k = e['kind']
        if k == 'heading':
            if e['text'] in drop:
                continue
            out.append((f'h{e["level"]}', maths(e['text'])))
        elif k == 'p':
            out.append(('p', maths(e['text'])))
        elif k == 'display':
            out.append(('display', [e['tex']]))
        elif k in ('code', 'slot'):
            out.append(('code/slot', []))
        elif k == 'table':
            out.append(('table', [m for r in [e['head']] + e['rows'] for c in r for m in maths(c)]))
        elif k == 'list':
            items(e, 0)
    return out


def parity(bid, zh, en, drop, check):
    # the maths of one element as a multiset: English word order may put them in another order
    a = [(k, sorted(m)) for k, m in shape(zh, drop)]
    b = [(k, sorted(m)) for k, m in shape(en)]
    bad = []
    for i in range(max(len(a), len(b))):
        x = a[i] if i < len(a) else ('—', [])
        y = b[i] if i < len(b) else ('—', [])
        same = x[0] == y[0] and x[1] == y[1]
        if check:
            print(f'  {bid:16} {i:2} {"ok " if same else "BAD"} {x[0]:10} {y[0]:10} {len(x[1])} maths', file=sys.stderr)
        if not same:
            bad.append((i, x, y))
    if bad:
        for i, x, y in bad[:5]:
            print(f'PARITY {bid} element {i}: source {x[0]} {x[1]} / translation {y[0]} {y[1]}', file=sys.stderr)
        raise SystemExit(f'{bid}: the translation does not match the source element for element')


# ---------------------------------------------------------------- the translation to HTML

def esc(s):
    return html.escape(s, quote=False)


def inline(text, note_ids):
    """One line of Markdown to HTML: maths kept as $…$ (escaped), `code`, **strong**, [^note], [text](url)."""
    parts = re.split(r'((?<!\\)\$[^$]+?(?<!\\)\$|`[^`]+`)', text)
    out = []
    for p in parts:
        if not p:
            continue
        if p.startswith('$'):
            out.append(esc(p))
            continue
        if p.startswith('`'):
            out.append('<code>' + esc(p[1:-1]) + '</code>')
            continue
        h = esc(p)
        h = re.sub(r'\[\^([^\]]+)\]', lambda m: f'<sup class="fn" data-note="{note_ids[m.group(1)]}"></sup>', h)
        h = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'<a href="\2">\1</a>', h)
        out.append(h)
    h = ''.join(out)
    # **strong** may hold code or maths, so it is matched over the joined line
    h = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', h)
    return h


def list_html(lst, note_ids, drop, dropped):
    tag = 'ol' if lst['ordered'] else 'ul'
    lis = []
    for it in lst['items']:
        if any(d in it['text'] for d in drop):
            dropped.add(next(d for d in drop if d in it['text']))
            continue
        sub = ''.join(list_html(s, note_ids, drop, dropped) for s in it['sub'])
        lis.append(f'<li>{inline(it["text"], note_ids)}{sub}</li>')
    return f'<{tag}>' + ''.join(lis) + f'</{tag}>' if lis else ''


def el_text(e):
    if e['kind'] in ('p', 'heading'):
        return e['text']
    if e['kind'] == 'display':
        return e['tex']
    if e['kind'] == 'list':
        acc = []

        def walk(lst):
            for it in lst['items']:
                acc.append(it['text'])
                for s in it['sub']:
                    walk(s)
        walk(e)
        return '\n'.join(acc)
    if e['kind'] == 'table':
        return '\n'.join(' | '.join(r) for r in [e['head']] + e['rows'])
    return e.get('key', '')


def el_html(e, note_ids, drop, dropped):
    k = e['kind']
    if k == 'p':
        return f'<p>{inline(e["text"], note_ids)}</p>'
    if k == 'display':
        return f'$${esc(e["tex"])}$$'
    if k == 'list':
        return list_html(e, note_ids, drop, dropped)
    if k == 'table':
        head = ''.join(f'<th>{inline(c, note_ids)}</th>' for c in e['head'])
        rows = ''.join('<tr>' + ''.join(f'<td>{inline(c, note_ids)}</td>' for c in r) + '</tr>' for r in e['rows'])
        return f'<div class="book-table"><table>\n<thead><tr>{head}</tr></thead>\n<tbody>{rows}</tbody>\n</table></div>'
    raise ValueError(k)


def outside_tags(h, old, new, count=1):
    """Replace old with new in the text of h, never inside a tag, at most count times."""
    parts = re.split(r'(<[^>]+>)', h)
    done = 0
    for i, p in enumerate(parts):
        if p.startswith('<') or done >= count:
            continue
        if old in p:
            k = min(p.count(old), count - done)
            parts[i] = p.replace(old, new, k)
            done += k
    return ''.join(parts), done


def read_translation(path):
    """translation.md: the marker lines of source.md, each followed by its block in English."""
    blocks, cur = {}, None
    for l in open(path, encoding='utf-8').read().split('\n'):
        m = MARKER.match(l.strip())
        if m:
            cur = m.group(1)
            blocks[cur] = []
            continue
        if cur is not None:
            blocks[cur].append(l)
    return blocks


def build(sec_dir, check=False):
    install()
    sp = importlib.util.spec_from_file_location('build_spec', os.path.join(sec_dir, 'build_spec.py'))
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    spec = {k: getattr(mod, k) for k in dir(mod) if k.isupper()}

    page = page_lines(os.path.join(BOOK, spec['OIWIKI_FILE']))
    notes_src = page_footnotes(page)
    trans = read_translation(os.path.join(sec_dir, spec.get('TRANSLATION', 'translation.md')))
    ai = spec['AI']

    md_blocks, html_blocks, order = [], [], []
    for b in spec['BLOCKS']:
        zh_lines = slice_block(page, b)
        head = f'<!-- block {b["id"]} · source {b["source"]} · {b["locator"]} -->'
        md_blocks.append(head + '\n\n' + '\n'.join(zh_lines))
        if b['id'] not in trans:
            raise SystemExit(f'{b["id"]}: translation.md has no block of this id')
        zh = parse(zh_lines)
        en = parse(trans[b['id']])
        parity(b['id'], zh, en, b.get('drop_headings', []), check)

        for e in [x for x in en if x['kind'] == 'p']:
            order.extend(re.findall(r'\[\^([^\]]+)\]', e['text']))
        for e in [x for x in en if x['kind'] == 'list']:
            order.extend(re.findall(r'\[\^([^\]]+)\]', el_text(e)))
        note_ids = {n: f'oiwiki-fn-{n}' for n in notes_src}

        # the block's elements as HTML, with what the spec puts in their place
        replace = [r for r in spec.get('REPLACE', []) if r[0] == b['id']]
        drop = [d for blk, d in spec.get('DROP', []) if blk == b['id']]
        after = [a for a in spec.get('AT', []) if a[0] == b['id']]
        dropped, placed = set(), set()
        parts = []
        skipping = None
        first_heading = True
        for e in en:
            t = el_text(e)
            if skipping is not None:
                if skipping[2] in t:
                    parts.append(spec['HTML'][skipping[3]])
                    placed.add(skipping[3])
                    skipping = None
                continue
            r = next((r for r in replace if r[1] in t), None)
            if r is not None:
                if r[2] in t:
                    parts.append(spec['HTML'][r[3]])
                    placed.add(r[3])
                else:
                    skipping = r
                continue
            if e['kind'] == 'heading':
                if first_heading:
                    parts.append(f'<h2>{inline(b.get("h2") or e["text"], note_ids)}</h2>')
                    first_heading = False
                else:
                    parts.append(f'<h3>{inline(e["text"], note_ids)}</h3>')
                continue
            if e['kind'] == 'slot':
                parts.append(spec['HTML'][e['key']])
                placed.add(e['key'])
                continue
            parts.append(el_html(e, note_ids, drop, dropped))
            for blk, anchor, key in after:
                if anchor in t:
                    parts.append(spec['HTML'][key])
                    placed.add(key)
        if skipping is not None:
            raise SystemExit(f'{b["id"]}: REPLACE {skipping[1]!r} … {skipping[2]!r} never closed')
        for d in drop:
            if d not in dropped:
                raise SystemExit(f'{b["id"]}: DROP {d!r} matched no list item')
        want = {r[3] for r in replace} | {a[2] for a in after}
        if want - placed:
            raise SystemExit(f'{b["id"]}: never placed {sorted(want - placed)}')
        body = '\n'.join(p for p in parts if p)
        for blk, old, new, *cnt in spec.get('MARKS', []):
            if blk != b['id']:
                continue
            if '<' in old:
                k = min(body.count(old), cnt[0] if cnt else 1)
                body = body.replace(old, new, k)
            else:
                body, k = outside_tags(body, old, new, cnt[0] if cnt else 1)
            if k == 0:
                print(f'MARK NOT FOUND {b["id"]}: {old!r}', file=sys.stderr)
        attrs = (f'id="{b["id"]}" data-source="{b["source"]}" data-locator="{html.escape(b["locator"], quote=True)}" '
                 f'data-ai="{ai}"')
        html_blocks.append(f'<section {attrs}>\n{body}\n</section>')

    # the page's footnotes in the order their markers first stand, numbered so
    seen = []
    for n in order:
        if n not in seen:
            seen.append(n)
    fn_rows, md_notes = [], []
    for k, n in enumerate(seen, 1):
        fn_rows.append({'id': f'oiwiki-fn-{n}', 'kind': 'book', 'number': str(k), 'html': inline(notes_src[n], {}), 'source': 'oiwiki'})
        md_notes.append(f'[^{n}]: {notes_src[n]}')

    md = f'# {spec["TITLE"]}\n\n' + '\n\n'.join(md_blocks) + '\n\n## Footnotes\n\n' + '\n\n'.join(md_notes) + '\n'
    open(os.path.join(sec_dir, 'source.md'), 'w', encoding='utf-8').write(md)
    with open(os.path.join(sec_dir, 'text.html'), 'w', encoding='utf-8') as _f:
        _f.write('\n\n'.join(html_blocks) + '\n')
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import apply_terms  # the judged concept mentions, after the page is written (tools/apply_terms.py)
    apply_terms.apply(sec_dir)
    json.dump(fn_rows, open(os.path.join(sec_dir, 'footnotes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump({}, open(os.path.join(sec_dir, 'captions.json'), 'w', encoding='utf-8'))
    print(f'{sec_dir}: {len(html_blocks)} blocks, {len(fn_rows)} footnotes, parity clean', file=sys.stderr)


# ---------------------------------------------------------------- OI Wiki's boxes and images
# Folded in from tools/oiwiki_boxes.py (2.4's extension) in the chapter 2–3 pass. build() installs them; a page
# without boxes reads as before (1.5 rebuilt byte-identical). tools/build_markdown.py and the sections' own
# assemblers that import this module's parse and inline get the plain readers, as before.
#
# `build_translation.py` reads the subset of Markdown that 1.5's page writes. Other OI Wiki pages (basic/prefix-sum,
# section 2.4) also write MkDocs admonitions, tabbed code and images:
#
#     ???+ tip "规定"                 a box: its type and title, its body indented four spaces under it
#         为方便讨论，……              (`???` folded, `???+` open, `!!!` plain: all the same box here)
#     ???+ example "参考实现"         a box that holds only code (in tabs or not) is OI Wiki's code, outside its licence:
#         === "C++"                   it is one code element, which the translation replaces with a [[key]] slot
#             ```cpp …```
#     ![二维前缀和示例](./images/…)    an image: the figure that stands in its place, a [[key]] slot in the translation
#
# This module installs the reading of those into build_translation's parser and its HTML, so a page without them
# reads exactly as before (1.5's page has none; its build is byte-identical with and without this module):
#
# - a box is an element `{kind: 'box', type, title, body}`; the parity check compares its title's maths, then its
#   body element for element, then its end, so a box cannot lose or gain a sentence in translation;
# - a box whose body is only code (and tab lines) is a `code` element, as a code fence is;
# - an image is a slot for parity; an image or a slot inside a box is lifted to just after the box, on both sides
#   alike, since a figure is not set inside a note;
# - a block of the spec may name boxes to leave out by their source title (`drop_boxes`): OI Wiki's practice-problem
#   boxes and the code boxes that nothing replaces. `source.md` keeps them; the parity check and the page do not;
# - the HTML of a box is a `div.note` with its title as the eyebrow (as 1.3 and 1.6 set a source's boxed note);
# - a link whose text is inline code (`[`std::partial_sum`](…)`) becomes a link (the tool matched links only
#   outside code).

bt = sys.modules[__name__]
BOX = re.compile(r'^(\?\?\?\+?|!!!)\s+(\w+)(?:\s+"(.*)")?\s*$')
TAB = re.compile(r'^===\s+"[^"]*"\s*$')
IMAGE = re.compile(r'^!\[([^\]]*)\]\(([^)\s]+)\)$')
_orig = {'parse': bt.parse, 'slice_block': bt.slice_block, 'shape': bt.shape, 'el_html': bt.el_html,
         'el_text': bt.el_text, 'inline': bt.inline}


class Lines(list):
    """A block's source lines, carrying the titles of the boxes its spec leaves out."""
    drop_boxes = ()


def slice_block(lines, b):
    out = Lines(_orig['slice_block'](lines, b))
    out.drop_boxes = tuple(b.get('drop_boxes', ()))
    return out


def _box_body(lines, i):
    """The lines of a box's body, dedented by four, from line i on; and the index after it."""
    body, n = [], len(lines)
    while i < n:
        l = lines[i]
        if not l.strip():
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            if j < n and bt.indent_of(lines[j]) >= 4:
                body.extend([''] * (j - i))
                i = j
                continue
            break
        if bt.indent_of(l) < 4:
            break
        body.append(l[4:])
        i += 1
    return body, i


def _code_only(els):
    return bool(els) and all(e['kind'] in ('code', 'tab') for e in els)


def parse(lines):
    """build_translation.parse, with boxes, tab lines and images read (see the module's docstring)."""
    drop = getattr(lines, 'drop_boxes', ())
    lines = list(lines)
    if not any(BOX.match(l.strip()) or IMAGE.match(l.strip()) or TAB.match(l.strip()) for l in lines if l.strip()):
        return _orig['parse'](lines)
    els, i, n = [], 0, len(lines)
    run = []                         # lines the original parser reads, flushed before a box or an image

    def flush():
        if run:
            els.extend(_orig['parse'](run))
            run.clear()
    while i < n:
        s = lines[i].strip()
        m = BOX.match(s) if bt.indent_of(lines[i]) == 0 else None
        if m:
            flush()
            body, i = _box_body(lines, i + 1)
            title = m.group(3) or ''
            if title in drop:
                continue
            inner = parse(body)
            if _code_only(inner):
                els.append({'kind': 'code', 'text': '\n'.join(body)})
                continue
            lifted = [e for e in inner if e['kind'] in ('slot', 'image')]
            els.append({'kind': 'box', 'type': m.group(2), 'title': title,
                        'body': [e for e in inner if e['kind'] not in ('slot', 'image')]})
            els.extend(lifted)
            continue
        if TAB.match(s):
            flush()
            els.append({'kind': 'tab'})
            i += 1
            continue
        m = IMAGE.match(s)
        if m:
            flush()
            els.append({'kind': 'image', 'alt': m.group(1), 'src': m.group(2)})
            i += 1
            continue
        run.append(lines[i])
        i += 1
    flush()
    return els


def shape(els, drop=()):
    out = []
    for e in els:
        k = e['kind']
        if k == 'box':
            out.append(('box', bt.maths(e['title'])))
            out.extend(shape(e['body'], drop))
            out.append(('/box', []))
        elif k == 'image':
            out.append(('code/slot', []))
        elif k == 'tab':
            continue
        else:
            out.extend(_orig['shape']([e], drop))
    return out


def el_text(e):
    if e['kind'] == 'box':
        return '\n'.join([e['title']] + [el_text(x) for x in e['body']])
    if e['kind'] in ('image', 'tab'):
        return ''
    return _orig['el_text'](e)


def el_html(e, note_ids, drop, dropped):
    if e['kind'] == 'box':
        inner = '\n'.join(el_html(x, note_ids, drop, dropped) for x in e['body'])
        head = f'<div class="eyebrow">{inline(e["title"], note_ids)}</div>' if e['title'] else ''
        return f'<div class="note">{head}\n{inner}\n</div>'
    return _orig['el_html'](e, note_ids, drop, dropped)


def inline(text, note_ids):
    """build_translation.inline, and a link whose text is inline code."""
    h = _orig['inline'](text, note_ids)
    return re.sub(r'\[(<code>[^<]*</code>)\]\(([^)\s]+)\)', r'<a href="\2">\1</a>', h)


def install():
    bt.slice_block, bt.parse, bt.shape, bt.el_text, bt.el_html, bt.inline = slice_block, parse, shape, el_text, el_html, inline


if __name__ == '__main__':
    build(os.path.abspath(sys.argv[1]), '--check' in sys.argv)
