#!/usr/bin/env python3
"""OI Wiki's boxes and images for `tools/build_translation.py`, as an extension that leaves that tool as it is.

`build_translation.py` reads the subset of Markdown that 1.5's page writes. Other OI Wiki pages (basic/prefix-sum,
section 2.4) also write MkDocs admonitions, tabbed code and images:

    ???+ tip "规定"                 a box: its type and title, its body indented four spaces under it
        为方便讨论，……              (`???` folded, `???+` open, `!!!` plain: all the same box here)
    ???+ example "参考实现"         a box that holds only code (in tabs or not) is OI Wiki's code, outside its licence:
        === "C++"                   it is one code element, which the translation replaces with a [[key]] slot
            ```cpp …```
    ![二维前缀和示例](./images/…)    an image: the figure that stands in its place, a [[key]] slot in the translation

This module installs the reading of those into build_translation's parser and its HTML, so a page without them
reads exactly as before (1.5's page has none; its build is byte-identical with and without this module):

- a box is an element `{kind: 'box', type, title, body}`; the parity check compares its title's maths, then its
  body element for element, then its end, so a box cannot lose or gain a sentence in translation;
- a box whose body is only code (and tab lines) is a `code` element, as a code fence is;
- an image is a slot for parity; an image or a slot inside a box is lifted to just after the box, on both sides
  alike, since a figure is not set inside a note;
- a block of the spec may name boxes to leave out by their source title (`drop_boxes`): OI Wiki's practice-problem
  boxes and the code boxes that nothing replaces. `source.md` keeps them; the parity check and the page do not;
- the HTML of a box is a `div.note` with its title as the eyebrow (as 1.3 and 1.6 set a source's boxed note);
- a link whose text is inline code (`[`std::partial_sum`](…)`) becomes a link (the tool matched links only
  outside code).

    python3 -I tools/oiwiki_boxes.py ch02/2.4 [--check]     # build_translation.build with the boxes read
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_translation as bt  # noqa: E402

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
    install()
    bt.build(os.path.abspath(sys.argv[1]), '--check' in sys.argv)
