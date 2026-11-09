#!/usr/bin/env python3
"""Write 3.4's NC exercise card, exercises-nc.json (METHOD §0: CC BY-NC-SA cards live in their own file).

MIT 6.046J Spring 2015, Problem Set 4, Problem 4-1 "Extreme FIFO Queues" (chapter 1 plans, question 31: set here,
not in 1.5). The statement is read by script from the cached handout's text (`pdftotext -layout` of the problem
set, sources/_cache/mitocw-6-046j-spring2015), whose text font survives the extraction; the replacement table
puts back what the layout breaks, each entry with its reason. The point values in brackets are the handout's
grading and are left out, as 1.3's cards leave out their write-up preambles. The key is MIT's worked solution,
linked (tools/nc_cards.py).

    python3 -I ch03/3.4/build_nc.py
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(BOOK, 'tools'))
import nc_cards  # noqa: E402

PSET = 'sources/_cache/mitocw-6-046j-spring2015/5eb7c1134350c89889dcaf7ec3fd609a_MIT6_046JS15_pset4.txt'
# (as extracted, as the page prints it, why)
FIXES = [
    ('E NQUEUE', 'ENQUEUE', 'small caps: the capital is set apart from the rest of the name'),
    ('D EUEUE', 'DEUEUE', 'the same (the handout prints “DEUEUE” here, for the DEQUEUE of part (b); kept as printed)'),
    ('D EQUEUE', 'DEQUEUE', 'small caps'),
    ('F IND -M IN', 'FIND-MIN', 'small caps, and the hyphen set apart'),
    ('op­ erations', 'operations', 'a word broken at a line end (a soft hyphen)'),
]


def statement():
    raw = open(os.path.join(BOOK, PSET), encoding='utf-8').read().split('\n')
    a = next(i for i, l in enumerate(raw) if l.startswith('Problem 4-1.'))
    z = next(i for i, l in enumerate(raw) if i > a and re.match(r'^\d+\s+Problem Set 4\s*$', l.strip()))
    body = raw[a + 1:z]
    paras, cur = [], []
    for l in body:
        s = l.strip()
        if not s:
            continue
        if re.match(r'^\([a-d]\)', s) and cur:
            paras.append(' '.join(cur))
            cur = []
        cur.append(s)
    paras.append(' '.join(cur))
    used = set()
    out = []
    for p in paras:
        for i, (x, y, _) in enumerate(FIXES):
            if x in p:
                p = p.replace(x, y)
                used.add(i)
        p = re.sub(r'^\(([a-d])\) \[\d+ points\] ', r'(\1) ', p)
        out.append(p)
    unused = [FIXES[i][0] for i in range(len(FIXES)) if i not in used]
    if unused:
        raise SystemExit(f'fixes never applied: {unused}')

    def to_html(p):
        h = html.escape(p, quote=False)
        h = re.sub(r'O\((\d|m)\)', r'$O(\1)$', h)
        h = re.sub(r'^\(([a-d])\)\s', r'<strong>(\1)</strong> ', h)
        h = h.replace(' Hint:', ' <em>Hint:</em>')
        return f'<p>{h}</p>'
    return '<p><strong>Extreme FIFO Queues</strong></p>\n' + '\n'.join(to_html(p) for p in out)


CARDS = [dict(id='nc-6046s15-ps4-1', origin='mitocw-6-046j-spring2015', handout='Solutions to Problem Set 4', set_='Problem Set 4',
              n='4-1', source_id='mitocw-6-046j-spring2015:ps4#4-1', bloom='Create', cite='min-queue',
              changes='The point values of the parts are left out. The worked solution is MIT’s, linked rather than copied.',
              concepts=['monotonic-queue-minimum', 'queue-from-two-stacks', 'amortized-analysis'], prompt=None)]

if __name__ == '__main__':
    CARDS[0]['prompt'] = statement()
    print(CARDS[0]['prompt'])
    nc_cards.write('3.4', CARDS)
