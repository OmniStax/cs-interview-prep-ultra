"""Write 2.1's exercises-nc.json (tools/nc_cards.py): MIT 6.006 Spring 2020, Problem Set 1, Problem 1-2, keyed by a link
to MIT's worked solution. The statement is read by script from the handout's text (pdftotext, in the cache); the
replacement table below puts back what the text layer loses, each entry with its reason, checked against the page
render. The points line ("[16 points]") is the handout's marking, not the problem."""
import os
import re
import sys

BOOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BOOK, 'tools'))
import nc_cards  # noqa: E402

TXT = 'sources/_cache/mitocw-6-006-spring2020/dc56bd1995baf20cfcdd3fbabdd2dbc9_MIT6_006S20_ps1-questions.txt'
FIXES = [
    ('insert at(', 'insert_at(', 'the underscore of the code name is lost in the text layer'),
    ('delete at(', 'delete_at(', 'the same'),
    ('delete at returns', 'delete_at returns', 'the same'),
]


def statement():
    t = open(os.path.join(BOOK, TXT), encoding='utf-8').read()
    a = t.index('Problem 1-2.')
    b = t.index('Problem 1-3.')
    s = t[a:b]
    s = re.sub(r'^Problem 1-2\.\s*\[\d+ points\]\s*', '', s)
    for old, new, _ in FIXES:
        assert old in s, old
        s = s.replace(old, new)
    paras = [' '.join(p.split()) for p in re.split(r'\n\s*\n', s) if p.strip()]
    out = []
    for p in paras:
        p = p.replace('O(n)', '$O(n)$').replace('O(log n)', '$O(\\log n)$').replace('O(k log n)', '$O(k \\log n)$')
        p = p.replace('i ≤ j < i + k', '$i \\le j < i + k$').replace('i + k − 1', '$i + k - 1$')
        if p.startswith('•'):
            items = [x.strip() for x in p.split('•') if x.strip()]
            out.append('<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>')
        else:
            out.append(p)
    return '\n\n'.join(out).replace(' (b) ', '\n\n(b) ')


if __name__ == '__main__':
    nc_cards.write('2.1', [{
        'id': 'nc-ps1-2', 'source_id': 'mitocw-6-006-spring2020:ps1-questions#1-2', 'set_': 'Problem Set 1', 'n': '1-2',
        'origin': 'mitocw-6-006-spring2020', 'bloom': 'Apply', 'cite': 'list-interface', 'prompt': statement(),
        'handout': 'Problem Set 1 Solutions', 'concepts': ['list-interface'],
    }])
