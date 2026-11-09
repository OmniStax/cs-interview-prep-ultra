#!/usr/bin/env python3
"""Write 2.6's NC exercise card, exercises-nc.json (METHOD §0: CC BY-NC-SA cards live in their own file).

MIT 6.006 Spring 2020, Problem Set 1, Problem 1-4 "Doubly Linked List", which the chapter config assigns to
doubly-linked-list (held from 2.5). The statement is read from the cached handout's text (pdftotext keeps it
whole) and set as HTML here; the table below restores what the text layer loses, each entry checked against the
page render (p. 3): the underscores of the code names, the code face of x.prev, x.next, L, L.head and L.tail,
x₁ and x₂, and O(1). The problem's point values are left out, as 1.3's cards leave out a problem's preamble. The
key is MIT's worked solution, linked (tools/nc_cards.py).

    python3 -I ch02/2.6/build_nc.py
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(BOOK, 'tools'))
import nc_cards  # noqa: E402

TXT = os.path.join(BOOK, 'sources/_cache/mitocw-6-006-spring2020/dc56bd1995baf20cfcdd3fbabdd2dbc9_MIT6_006S20_ps1-questions.txt')

# (what the text layer gives, what the page prints, why)
FIXES = [
    ('insert first(x) insert last(x) delete first() delete last()',
     '<code>insert_first(x)</code>, <code>insert_last(x)</code>, <code>delete_first()</code>, <code>delete_last()</code>',
     'the four names in the code face with their underscores, which the text layer drops'),
    ('Doubly Linked List Seq', '<code>Doubly_Linked_List_Seq</code>', 'a class name in the code face'),
    ('Doubly Linked List Node', '<code>Doubly_Linked_List_Node</code>', 'a class name in the code face'),
    ('x.prev', '<code>x.prev</code>', 'code face'),
    ('x.next', '<code>x.next</code>', 'code face'),
    ('L.tail', '<code>L.tail</code>', 'code face'),
    ('L.head', '<code>L.head</code>', 'code face'),
    ('list L maintains', 'list <code>L</code> maintains', 'code face'),
    ('node x of a', 'node <code>x</code> of a', 'code face'),
    ('O(1) time', '$O(1)$ time', 'maths'),
    ('nodes x1 and x2', 'nodes $x_1$ and $x_2$', 'subscripts the text layer flattens'),
    ('list L, where x1 occurs before x2', 'list $L$, where $x_1$ occurs before $x_2$', 'maths'),
    ('from x1 to x2', 'from $x_1$ to $x_2$', 'maths'),
    ('from L, and', 'from $L$, and', 'maths'),
    ('node x from a doubly linked list L1 and second doubly linked list L2', 'node $x$ from a doubly linked list $L_1$ and second doubly linked list $L_2$', 'maths'),
    ('list L2 into list L1 after node x.', 'list $L_2$ into list $L_1$ after node $x$.', 'maths'),
    ('L1 should contain', '$L_1$ should contain', 'maths'),
    ('and L2 should', 'and $L_2$ should', 'maths'),
    ('doubly linked list', '<strong>doubly linked list</strong>', 'bold on its first use, as printed'),
    ('should not maintain their length', '<strong>should not maintain their length</strong>', 'bold as printed'),
    ('to remove all', 'to <strong>remove</strong> all', 'bold as printed'),
    ('algorithm to splice', 'algorithm to <strong>splice</strong>', 'bold as printed'),
    ('do not modify', '<strong>do not modify</strong>', 'bold as printed'),
]


def statement():
    lines = open(TXT, encoding='utf-8').read().split('\n')
    a = next(k for k, l in enumerate(lines) if l.startswith('Problem 1-4.'))
    b = next(k for k, l in enumerate(lines) if k > a and 'MIT OpenCourseWare' in l)
    body = lines[a + 1:b]
    paras, cur = [], []
    for l in body:
        t = l.strip()
        m = re.match(r'\(([a-d])\)\s*\[\d+ points\]\s*(.*)', t)
        if m or not t:
            if cur:
                paras.append(cur)
            cur = [f'({m.group(1)})', m.group(2)] if m else []
            continue
        cur.append(t)
    if cur:
        paras.append(cur)
    out, used = [], set()
    for p in paras:
        label = p[0] if re.match(r'\([a-d]\)$', p[0]) else None
        words = ' '.join(p[1:] if label else p)
        words = re.sub(r'(\w)- (\w)', r'\1\2', words)       # a word broken at a line end
        words = re.sub(r'\s+', ' ', words).replace('ﬁ', 'fi')
        h = html.escape(words, quote=False)
        for old, new, _why in FIXES:
            if old in h and old not in used:
                h = h.replace(old, new, 1)
                used.add(old)
        out.append(f'<p><strong>{label}</strong> {h}</p>' if label else f'<p>{h}</p>')
    title = '<p><strong>Doubly Linked List</strong></p>'
    return title + '\n' + '\n'.join(out)


CARDS = [
    dict(id='nc-6006s20-ps1-4', origin='mitocw-6-006-spring2020', handout='Problem Set 1 Solutions', set_='Problem Set 1',
         n='1-4', source_id='mitocw-6-006-spring2020:ps1#1-4', bloom='Create', cite='dllist',
         concepts=['doubly-linked-list'], prompt=None),
]

if __name__ == '__main__':
    CARDS[0]['prompt'] = statement()
    print(CARDS[0]['prompt'])
    nc_cards.write('2.6', CARDS)
