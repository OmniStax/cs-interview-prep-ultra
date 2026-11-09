"""Readers for section 2.1's ODS blocks (the Wikipedia blocks are read by tools/wikitext.py, the book's one
Wikipedia reader, since the chapter 2–3 pass), called by tools/build_text.py through a block's `reader`
(a function of the block, the spec and the book's folder, returning the block's HTML and Markdown parts).

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
