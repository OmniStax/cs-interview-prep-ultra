"""Write 2.3's exercises-nc.json (tools/nc_cards.py): MIT 6.006 Spring 2020, Problem Set 0, Problem 0-6 and Problem Set 3,
Problem 3-5, as code cards. The statements are read by script from the handouts' text (pdftotext, in the cache), with the
replacement table below putting back what the text layer loses, each entry with its reason, checked against the page
render. The tests are the `tests` tuples of MIT's template tests.py, read from the template zip in the cache with
ast.literal_eval (nothing of it is run); the starter is the template's own file; the reference is MIT's solution code,
read from the solutions handout's numbered listing; the solution field links MIT's worked solution.

    python3 -I ch02/2.3/build_nc.py
"""
import ast
import os
import re
import sys
import zipfile

BOOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BOOK, 'tools'))
import nc_cards  # noqa: E402

MIT = 'sources/_cache/mitocw-6-006-spring2020/'
PS0_Q = MIT + '60f0a029ab154553cad51b54cc25605b_MIT6_006S20_ps0-questions.txt'
PS0_S = MIT + 'cfc7d2d5bc3b9f4df35b5bdc7aa49284_MIT6_006S20_ps0-solutions.txt'
PS0_Z = MIT + 'a100caad66c721bdbec9365c4a9d51e3_MIT6_006S20_ps0-template.zip'
PS3_Q = MIT + '03a34fcf3012a242ffcae5534e9fa511_MIT6_006S20_ps3-questions.txt'
PS3_S = MIT + '9aede1539e086a709a75d604a89f08b6_MIT6_006S20_ps3-solutions.txt'
PS3_Z = MIT + 'cbac55d8c2eccf892a6bde90e785393a_MIT6_006S20_ps3-template.zip'

DROP_TEMPLATE = (' You can download a code template containing some test cases from the website.', '',
                 'the card itself holds the template and its tests')
# (what the text layer gives, what the card prints, why)
FIX0 = [
    ('ar- ray', 'array', 'a line-end hyphen of the handout'),
    ('count long subarrays(A)', '<code>count_long_subarray(A)</code>',
     'the underscores are lost in the text layer; the handout prints count_long_subarrays, MIT’s template and tests name it '
     'count_long_subarray, which the tests call'),
    ('A = (a0 , a1 , . . . , an−1 )', '$A = (a_0, a_1, \\ldots, a_{n-1})$', 'subscripts are lost in the text layer'),
    ('of n > 0', 'of $n > 0$', 'maths in the handout'),
    ('speciﬁcally', 'specifically', 'a ligature of the text layer'),
    DROP_TEMPLATE,
]
FIX3 = [
    ('’', "'", 'the text layer curls the straight quotes of the handout’s strings'),
    ('[12 points] ', '', 'the marking, not the problem'),
    ('[3 points] ', '', 'the same'),
    ('[25 points] ', '', 'the same'),
    ('O(|A|)', '$O(|A|)$', 'maths in the handout'),
    ('|B| = k', '$|B| = k$', 'the same'),
    ('O(k) time', '$O(k)$ time', 'the same'),
    ('S = (S0, . . . , Sn−1)', '$S = (S_0, \\ldots, S_{n-1})$', 'subscripts are lost in the text layer'),
    ('0 < k < |T |', '$0 < k < |T|$', 'the same, and a space the text layer adds'),
    ('O(|T | + nk)', '$O(|T| + nk)$', 'the same'),
    ('A = (a0, . . . , an−1)', '$A = (a_0, \\ldots, a_{n-1})$', 'subscripts are lost in the text layer'),
    ('which ai is the anagram substring count of Si in T for all i ∈ {0, . . . , n − 1}',
     'which $a_i$ is the anagram substring count of $S_i$ in $T$ for all $i \\in \\{0, \\ldots, n - 1\\}$', 'the same'),
    ('count anagram substrings(T, S)', '<code>count_anagram_substrings(T, S)</code>', 'the underscores are lost in the text layer'),
    ('O(1) time', '$O(1)$ time', 'maths in the handout'),
    DROP_TEMPLATE,
]


def read(path):
    return open(os.path.join(BOOK, path), encoding='utf-8').read()


def fix(s, table):
    for old, new, _ in table:
        assert old in s, old
        s = s.replace(old, new)
    return s


def ps0_prompt():
    t = read(PS0_Q)
    s = t[t.index('Problem 0-6.'):t.index('MIT OpenCourseWare', t.index('Problem 0-6.'))]
    s = ' '.join(s.replace('Problem 0-6.', '').split())
    return fix(s, FIX0)


def ps3_prompt():
    t = read(PS3_Q)
    a = t.index('Problem 3-5.')
    s = t[a:t.index('   1   def count_anagram_substrings', a)]
    s = re.sub(r'^Problem 3-5\.\s*\[\d+ points\]\s*Anagram Archaeology\s*', '', s)
    s = ' '.join(s.split())
    s = fix(s, FIX3)
    for cut in ('Given two strings A and B', '(a) ', '(b) ', '(c) '):
        s = s.replace(' ' + cut, '\n\n' + cut, 1)
    return s


def listing(path, first):
    """MIT's numbered code listing, from the line that starts `first` to the page footer: the line numbers are cut at the
    column of line 1's code (a number of two digits stands one place to the left of a number of one, which the column
    absorbs), and the curled quotes of the text layer are put back straight."""
    t = read(path)
    lines = t[t.index(first) - 40:].split('\n')
    k = next(i for i, l in enumerate(lines) if first in l)
    col = lines[k].index(first)
    out = []
    for l in lines[k:]:
        if l.strip().startswith('MIT OpenCourseWare'):
            break
        if not l.strip():
            continue
        assert re.match(r'^\s*\d+(\s|$)', l), l
        out.append(l[col:].rstrip())
    return '\n'.join(out).replace('’', "'") + '\n'


def template(zpath, name):
    with zipfile.ZipFile(os.path.join(BOOK, zpath)) as z:
        return z.read(name).decode('utf-8')


def mit_tests(zpath, name, star):
    src = template(zpath, name)
    tree = ast.parse(src)
    node = next(n.value for n in tree.body if isinstance(n, ast.Assign) and n.targets[0].id == 'tests')
    out = []
    for i, (args, expect) in enumerate(ast.literal_eval(node)):
        args = [list(a) if isinstance(a, tuple) else a for a in args] if star else [list(args)]
        out.append({'args': args, 'expect': list(expect) if isinstance(expect, tuple) else expect, 'visible': i == 0,
                    'generated_by': 'source'})
    return out


def card_answer(entry, starter, reference, tests):
    return {'type': 'code', 'python': {'entry': entry, 'starter': starter, 'reference': reference, 'generated_by': 'source'},
            'tests': tests, 'generated_by': 'source'}


CHANGES = 'The tests are those of MIT’s code template; the worked solution is MIT’s, linked.'

if __name__ == '__main__':
    ref0 = listing(PS0_S, 'def count_long_subarray(A):')
    ref3 = listing(PS3_S, "ORD_A = ord(")
    nc_cards.write('2.3', [
        {'id': 'nc-ps0-6', 'source_id': 'mitocw-6-006-spring2020:ps0-questions#0-6', 'set_': 'Problem Set 0', 'n': '0-6',
         'origin': 'mitocw-6-006-spring2020', 'bloom': 'Apply', 'cite': 'two-pointers', 'kind': 'code', 'changes': CHANGES,
         'prompt': ps0_prompt(), 'handout': 'Problem Set 0 Solutions', 'concepts': ['two-pointers', 'complexity-analysis'],
         'answer': card_answer('count_long_subarray', template(PS0_Z, 'ps0-template/count_long_subarray.py'), ref0,
                               mit_tests(PS0_Z, 'ps0-template/tests.py', star=False))},
        {'id': 'nc-ps3-5', 'source_id': 'mitocw-6-006-spring2020:ps3-questions#3-5', 'set_': 'Problem Set 3', 'n': '3-5',
         'origin': 'mitocw-6-006-spring2020', 'bloom': 'Apply', 'cite': 'moving-average', 'kind': 'code',
         'changes': CHANGES + ' Parts (a) and (b) are answered in words; the tests check part (c).',
         'prompt': ps3_prompt(), 'handout': 'Problem Set 3 Solutions', 'concepts': ['sliding-window-fixed'],
         'answer': card_answer('count_anagram_substrings', template(PS3_Z, 'ps3-template/count_anagram_substrings.py'), ref3,
                               mit_tests(PS3_Z, 'ps3-template/tests.py', star=True))},
    ])
