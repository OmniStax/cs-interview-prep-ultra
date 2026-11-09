#!/usr/bin/env python3
"""Write 1.6's NC exercise cards, exercises-nc.json (METHOD §0: CC BY-NC-SA cards live in their own file, never
in section.json).

The cards are MIT 6.042J (Fall 2005) problems the plan lists for this section, read by script from the cached
pdftotext output of each problem set (sources/_cache/mitocw-6-042j-fall2005/). Only the problems whose statement
comes through that text whole are carded: pdftotext drops sub- and superscripts and garbles binomials, square
roots and displays, so a problem that leans on them (ps7 #2–#5, ps9 #1, #6, #7, ps10 #2, #6–#8) waits for a reading
of the PDF itself. The key of each card is MIT's own worked solution, linked rather than transcribed for the same
reason.

    python3 -I ch01/1.6/build_nc.py
"""
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
CACHE = os.path.join(BOOK, 'sources/_cache/mitocw-6-042j-fall2005')
ORIGIN = 'mitocw-6-042j-fall2005'

# (problem set, problem, concepts, bloom, what the extraction gets wrong -> what the PDF prints)
CARDS = [
    ('ps7', 1, ['counting'], 'Apply', []),
    ('ps9', 2, ['conditional-probability', 'probability-basics'], 'Evaluate', []),
    ('ps9', 3, ['conditional-probability', 'counting'], 'Analyze', []),
    ('ps9', 4, ['conditional-probability'], 'Apply', []),
    ('ps9', 5, ['conditional-probability'], 'Apply', []),
    ('ps10', 1, ['linearity-of-expectation', 'geometric-expectation'], 'Apply', [('E [B]', 'E[B]'), ('E [R]', 'E[R]'), ('E [U ]', 'E[U]'), ('E [D]', 'E[D]')]),
    ('ps10', 3, ['linearity-of-expectation', 'indicator-variables'], 'Analyze', [('Let Mi be', 'Let M<sub>i</sub> be')]),
    ('ps10', 4, ['linearity-of-expectation'], 'Apply', []),
    ('ps10', 5, ['linearity-of-expectation'], 'Analyze', []),
]


def files():
    """The cached handouts by their OCW names (index.tsv: file, OCW name, URL)."""
    out = {}
    for line in open(os.path.join(CACHE, 'index.tsv'), encoding='utf-8'):
        f, name, url = line.rstrip('\n').split('\t')[:3]
        out[name] = (f, url)
    return out


def problem(txt, n):
    t = open(os.path.join(CACHE, txt.replace('.pdf', '.txt')), encoding='utf-8').read()
    parts = re.split(r'\n(?=Problem \d+\.)', t)
    p = next(x for x in parts if x.startswith(f'Problem {n}.'))
    p = re.sub(r'^Problem \d+\.\s*', '', p)
    lines = []
    for l in p.split('\n'):
        if re.match(r'\s*Copyright ©', l) or re.match(r'\s*Problem Set \d+\s+\d+\s*$', l):
            continue
        lines.append(l)
    p = '\n'.join(lines).replace('­\n', '').replace('­', '-')
    p = p.replace('ﬁ', 'fi').replace('ﬂ', 'fl').replace('ﬀ', 'ff').replace('ﬃ', 'ffi')
    paras = []
    for block in re.split(r'\n\s*\n', p.strip()):
        rows = [r.strip() for r in block.split('\n') if r.strip()]
        if rows and rows[0].startswith('•'):
            items, cur = [], None
            for r in rows:
                if r.startswith('•'):
                    cur = r[1:].strip()
                    items.append(cur)
                else:
                    items[-1] += ' ' + r
            paras.append('<ul>' + ''.join(f'<li>{html.escape(x, quote=False)}</li>' for x in items) + '</ul>')
        elif rows:
            paras.append(html.escape(' '.join(rows), quote=False))
    return '\n\n'.join(paras).replace('</ul>\n\n<ul>', '').replace('$', '&#36;')


def main():
    idx = files()
    ex, con = [], []
    for ps, n, concepts, bloom, fixes in CARDS:
        f, _ = idx[f'{ps}.pdf']
        sf, surl = idx[f'{ps}sol.pdf']
        prompt = problem(f, n)
        for a, b in fixes:
            assert a in prompt, (ps, n, a)
            prompt = prompt.replace(a, b)
        num = ps[2:]
        cid = f'nc-{ps}-{n}'
        ex.append({
            'id': cid, 'source_id': f'{ORIGIN}:{ps}sol#{n}', 'source_number': f'Problem Set {num}, Problem {n}',
            'origin': ORIGIN, 'kind': 'exercise', 'bloom': bloom, 'place': {'at': 'end'},
            'changes': 'The worked solution is MIT’s, linked rather than copied.',
            'prompt': prompt,
            'answer': {'type': 'open', 'generated_by': 'source',
                       'solution': f'MIT’s worked solution: <a href="{surl}">Solutions to Problem Set {num}</a>, Problem {n}.'}})
        con.extend({'exercise': cid, 'concept': c} for c in concepts)
    out = {'section': '1.6', 'license': 'CC BY-NC-SA 4.0', 'license_url': 'https://creativecommons.org/licenses/by-nc-sa/4.0/',
           'exercises': ex, 'exercise_concepts': con}
    with open(os.path.join(HERE, 'exercises-nc.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    print(f'exercises-nc.json: {len(ex)} cards')


if __name__ == '__main__':
    main()
