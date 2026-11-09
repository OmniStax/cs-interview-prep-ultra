#!/usr/bin/env python3
"""Write 3.3's NC exercise card, exercises-nc.json (METHOD §0: CC BY-NC-SA cards live in their own file).

MIT 6.006 Spring 2020, Problem Session 1, Problem 1-3 "Double-Ended Sequence Operations", which the chapter config
holds for this section (from 2.2) and tags with dynamic-array-cost. The statement is read from the cached handout's
text (pdftotext keeps it whole) and set as HTML here; the table below restores what the text layer loses, each entry
checked against the page render (p. 2): the maths of O(1), O(n) and n, the fi ligature, and the two words set in bold.
The key is MIT's worked solution, linked (tools/nc_cards.py).

    python3 -I ch03/3.3/build_nc.py
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(BOOK, 'tools'))
import nc_cards  # noqa: E402

TXT = os.path.join(BOOK, 'sources/_cache/mitocw-6-006-spring2020/8a750a72b9b9c29f6a0402866bac34b7_MIT6_006S20_prob1.txt')

# (what the text layer gives, what the page prints, why)
FIXES = [
    ('worst-case O(1)-time indexing', 'worst-case $O(1)$-time indexing', 'maths'),
    ('worst-case O(1) time', 'worst-case $O(1)$ time', 'maths'),
    ('supports worst-case O(1)-time index lookup', 'supports <strong>worst-case</strong> $O(1)$-time index lookup', 'bold as printed, and maths'),
    ('as well as amortized O(1)-time', 'as well as <strong>amortized</strong> $O(1)$-time', 'bold as printed, and maths'),
    ('use O(n) space to store n items', 'use $O(n)$ space to store $n$ items', 'maths'),
]


def statement():
    lines = open(TXT, encoding='utf-8').read().split('\n')
    a = next(k for k, l in enumerate(lines) if l.startswith('Problem 1-3.'))
    b = next(k for k, l in enumerate(lines) if k > a and l.startswith('Problem 1-4.'))
    paras, cur = [], []
    for l in lines[a + 1:b]:
        t = l.strip()
        if not t:
            if cur:
                paras.append(cur)
            cur = []
            continue
        cur.append(t)
    if cur:
        paras.append(cur)
    # the page breaks its paragraphs where a line ends short of the measure; the text layer keeps them as lines,
    # so a paragraph ends at a line that ends with a full stop and is followed by one starting a new sentence
    words = ' '.join(' '.join(p) for p in paras)
    words = re.sub(r'(\w)- (\w)', r'\1\2', words).replace('ﬁ', 'fi')
    parts = re.split(r'(?<=linear time\.) (?=On the other hand)|(?<=indexing\.) (?=Show that)', words)
    out, used = [], set()
    for p in parts:
        h = html.escape(' '.join(p.split()), quote=False)
        for old, new, _why in FIXES:
            if old in h and old not in used:
                h = h.replace(old, new, 1)
                used.add(old)
        out.append(f'<p>{h}</p>')
    missing = [f[0] for f in FIXES if f[0] not in used]
    if missing:
        raise SystemExit(f'fixes not applied: {missing}')
    return '<p><strong>Double-Ended Sequence Operations</strong></p>\n' + '\n'.join(out)


CARDS = [
    dict(id='nc-6006s20-prob1-3', origin='mitocw-6-006-spring2020', handout='Problem Session 1 Solutions', set_='Problem Session 1',
         n='1-3', source_id='mitocw-6-006-spring2020:prob1#1-3', bloom='Create', cite='dualarraydeque',
         concepts=['deque', 'dynamic-array-cost', 'dual-array-deque'], prompt=None),
]

if __name__ == '__main__':
    CARDS[0]['prompt'] = statement()
    print(CARDS[0]['prompt'])
    nc_cards.write('3.3', CARDS)
