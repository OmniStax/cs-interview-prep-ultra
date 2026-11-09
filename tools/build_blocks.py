"""Blocks read by tools/read_latex.py (a LaTeX source) or tools/extract_mcs.py (the MCS 2018 PDF), for
tools/build_text.py, which calls block() for any block whose spec row names a `reader`.

A `latex` block: {id, source, locator, h2, reader: 'latex', file, chapter, dialect, parts: [(start, stop), …],
drop_first_heading?, edition?}. Each part runs from the line holding `start` to the line before the one holding
`stop` (None: the end of the file); the parts are read in order and set one after another.

An `mcs` block: {id, source, locator, h2, reader: 'mcs', pdf, pages, from, to, drop_first_heading?}.

What the section's build_spec.py may add, beside BLOCKS:

- LATEX_REFS {label or 'secref:label': (html, md)}: how a reference to a place this page does not carry is
  printed (a reference to a place it carries reads as the source numbers it, or as the spec says).
- REPLACE [(block id, a piece of the display's TeX, HTML key or '')]: a display set as a figure of the
  section's (a derivation) or dropped.
- ENV_EYEBROW {(block id, environment): eyebrow}: the label a boxed environment carries (a framed theorem).
- FIGURE_AT {label: HTML key}: the Sim that stands where the source's figure stood.
- DISPLAYS {key: TeX}: an MCS display, which the PDF draws in pieces, set from the page render.
- CODE_HOOK(e): the HTML for an ODS listing (`\\codeimport{ods/ArrayStack.add(i,x)}` and the edition imports,
  e = {cmd, ref}); '' drops it, as a spec without the hook does.
The footnotes the passages print go to spec['_latex_notes'] for build_text.py's footnote rows.
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import read_latex  # noqa: E402


def _hooks(b, spec):
    reps = [r for r in spec.get('REPLACE', []) if r[0] == b['id']]
    used = spec.setdefault('_replace_used', set())

    def display_hook(e):
        for r in reps:
            if r[1] in e['tex']:
                used.add(r)
                e['as'] = r[2] or 'dropped'
                return spec['HTML'][r[2]] if r[2] else ''
        return None

    def env_hook(e):
        eb = spec.get('ENV_EYEBROW', {}).get((b['id'], e['name']))
        if eb:
            e['eyebrow'] = eb
        return None

    def figure_hook(e):
        key = spec.get('FIGURE_AT', {}).get(e.get('label'))
        return spec['HTML'][key] if key else ''
    def code_hook(e):
        # an ODS listing (tools/read_latex.py, kind 'code'): the spec's CODE_HOOK sets it, or it is dropped
        f = spec.get('CODE_HOOK')
        return f(e) if f else ''
    return dict(display_hook=display_hook, env_hook=env_hook, figure_hook=figure_hook, code_hook=code_hook)


def latex_block(b, spec, book):
    path = os.path.join(book, b['file'])
    hs, ms = [], []
    notes = spec.setdefault('_latex_notes', [])
    refs = spec.get('LATEX_REFS', {})
    for k, (start, stop) in enumerate(b['parts']):
        h, m, fn, unknown, _ = read_latex.passage(
            path, start, stop, b['chapter'], b['dialect'], refs=refs,
            fn_prefix=f'{b["source"]}-fn-{b["chapter"]}', heading_shift=b.get('heading_shift', 1), edition=b.get('edition'),
            **_hooks(b, spec))
        if k == 0 and b.get('drop_first_heading') and h and re.match(r'<h\d>', h[0]):
            h, m = h[1:], m[1:]
        if unknown:
            print(f'{b["id"]}: LaTeX the reader does not know: {sorted(unknown)}', file=sys.stderr)
        for n in fn:
            if n['id'] not in [x['id'] for x in notes]:
                notes.append({'id': n['id'], 'number': n['number'], 'html': n['html'], 'md': read_latex.to_md(n['html']),
                              'source': b['source']})
        hs += h
        ms += m
    return hs, ms


def mcs_block(b, spec, book):
    import extract_mcs
    hs, ms = [], []
    els = extract_mcs.elements(os.path.join(book, b['pdf']), b['pages'], b['from'], b['to'])
    if b.get('drop_first_heading') and els and els[0]['kind'] == 'heading':
        els = els[1:]
    hooks = _hooks(b, spec)
    for e in els:
        if e['kind'] == 'heading':
            lvl = e['level'] + b.get('heading_shift', 0)
            hs.append(f'<h{lvl}>{html.escape(e["text"], quote=False)}</h{lvl}>')
            ms.append('#' * lvl + ' ' + e['text'])
        elif e['kind'] == 'display':
            tex = spec.get('DISPLAYS', {}).get(e['key'])
            if tex is None:
                print(f'MISSING DISPLAY {b["id"]} {e["key"]}: ' + ' / '.join(e['text']), file=sys.stderr)
                tex = r'\text{(missing)}'
            rep = hooks['display_hook']({'tex': tex})
            if rep is not None:
                if rep:
                    hs.append(rep)
                continue
            hs.append(f'$${tex}$$')
            ms.append(f'$${tex}$$')
        else:
            h, m = e['html'], e['md']
            # a numbered definition, theorem or lemma stands as a note under its own label (book RULES, Apparatus)
            mm = re.match(r'<strong>((?:Definition|Theorem|Lemma|Corollary) [\d.]+)\.</strong>\s*(.*)', h, re.S)
            if mm:
                hs.append(f'<div class="note"><span class="eyebrow">{mm.group(1)}</span><p>{mm.group(2)}</p></div>')
            else:
                hs.append(f'<p>{h}</p>')
            ms.append(m)
    return hs, ms


def block(b, spec, book):
    """The block's HTML parts and Markdown parts, its <h2> first."""
    if b['reader'] == 'latex':
        hs, ms = latex_block(b, spec, book)
    else:
        hs, ms = mcs_block(b, spec, book)
    return [f'<h2>{html.escape(b["h2"], quote=False)}</h2>'] + hs, [f'## {b["h2"]}'] + ms
