"""Section 3.5 Stack applications: expression evaluation. Read by tools/build_markdown.py (the text) and
tools/build_section.py (section.json). One source, cp-algorithms string/expression_parsing at d55d3f5, in English.

The page prints C++ only. Its four listings (two programs, two one-line fragments) become four-language code sets:
the C++ is read here from the cached page, never typed; the Python, Java and JavaScript are AI translations kept in
code/ beside this file (each checked against the C++ on ~1,150 random expressions, ch03/3.5/log-pass.md).
"""
import html as _html
import os as _os
import re as _re

_HERE = _os.path.dirname(_os.path.abspath(__file__))
_BOOK = _os.path.dirname(_os.path.dirname(_HERE))

TITLE = 'Stack applications: expression evaluation'
MD_FILE = 'sources/_cache/cpa/src/string/expression_parsing.md'
LOC = 'cpa:string/expression_parsing'
BLOCKS = [
    dict(id='rpn', source='cpa', locator=f'{LOC} lead + #reverse-polish-notation',
         **{'from': '# Expression parsing', 'to': '## Parsing of simple expressions'}),
    dict(id='parsing', source='cpa', locator=f'{LOC}#parsing-of-simple-expressions',
         **{'from': '## Parsing of simple expressions', 'to': '## Unary operators'}),
    dict(id='unary', source='cpa', locator=f'{LOC}#unary-operators',
         **{'from': '## Unary operators', 'to': '## Right-associativity'}),
    dict(id='right-assoc', source='cpa', locator=f'{LOC}#right-associativity',
         **{'from': '## Right-associativity'}),
]
AI = 'claude-opus-5-5 high'

# ---------------------------------------------------------------- the code sets
_PAGE = open(_os.path.join(_BOOK, MD_FILE), encoding='utf-8').read()


def _fence(name):
    """A listing the page prints in a ```{.cpp file=name} fence, as printed."""
    return _re.search(r'```\{\.cpp file=' + name + r'\}\n(.*?)\n```', _PAGE, _re.S).group(1)


_FRAGMENTS = _re.findall(r'```cpp\n(.*?)\n```', _PAGE, _re.S)   # the two `while` fragments under Right-associativity
CPP_SIMPLE, CPP_UNARY = _fence('expression_parsing_simple'), _fence('expression_parsing_unary')
CPP_WHILE, CPP_WHILE_RIGHT = _FRAGMENTS


def _code(name):
    return open(_os.path.join(_HERE, 'code', name), encoding='utf-8').read().rstrip('\n')


def _pre(lang, src, ai):
    a = f' data-ai="{AI}"' if ai else ''
    return f'<pre data-lang="{lang}"{a}><code>' + _html.escape(src, quote=False).replace('$', '&#36;') + '</code></pre>'


def code_set(py, java, cpp, js):
    """Python, Java and JavaScript the AI's; C++ the source's."""
    return ('<div class="code-set">\n' + _pre('python', py, True) + '\n' + _pre('java', java, True) + '\n'
            + _pre('cpp', cpp, False) + '\n' + _pre('javascript', js, True) + '\n</div>')


WHILE_PY = 'while op and priority(op[-1]) >= priority(cur_op):'
WHILE_JAVA = 'while (!op.isEmpty() && priority(op.peek()) >= priority(cur_op))'
WHILE_JS = 'while (op.length > 0 && priority(op[op.length - 1]) >= priority(cur_op))'
WHILE_RIGHT_PY = ('while op and (\n'
                  '        (left_assoc(cur_op) and priority(op[-1]) >= priority(cur_op)) or\n'
                  '        (not left_assoc(cur_op) and priority(op[-1]) > priority(cur_op))\n'
                  '    ):')
WHILE_RIGHT_JAVA = ('while (!op.isEmpty() && (\n'
                    '        (left_assoc(cur_op) && priority(op.peek()) >= priority(cur_op)) ||\n'
                    '        (!left_assoc(cur_op) && priority(op.peek()) > priority(cur_op))\n'
                    '    ))')
WHILE_RIGHT_JS = ('while (op.length > 0 && (\n'
                  '        (left_assoc(cur_op) && priority(op[op.length - 1]) >= priority(cur_op)) ||\n'
                  '        (!left_assoc(cur_op) && priority(op[op.length - 1]) > priority(cur_op))\n'
                  '    ))')


def ref(rid, word):
    return f'<span data-ref="{rid}">{word}</span>'


ST, OP = ref('st', '<code>st</code>'), ref('op', '<code>op</code>')
CAPTION = (
    f'The string is read left to right. Each number goes onto {ST}; each operator waits on {OP} until a weaker '
    f'operator, a closing bracket or the end of the string comes after it, and is then executed on the top of {ST}. '
    f'The order in which the operators are executed is the expression’s reverse Polish notation. A unary minus and ^ '
    f'are right-associative, so an operator of equal priority on top is not executed: the new one waits above it.')
SIM = (f'<figure class="sim" id="sim-two-stack-parser">\n'
       f'  <div class="sim-head"><span class="eyebrow">Sim</span><span>{CAPTION}</span></div>\n</figure>')

HTML = {
    'code-simple': code_set(_code('simple.py'), _code('simple.java'), CPP_SIMPLE, _code('simple.js')),
    'code-while': code_set(WHILE_PY, WHILE_JAVA, CPP_WHILE, WHILE_JS),
    'code-while-right': code_set(WHILE_RIGHT_PY, WHILE_RIGHT_JAVA, CPP_WHILE_RIGHT, WHILE_RIGHT_JS),
    'code-unary': code_set(_code('unary.py'), _code('unary.java'), CPP_UNARY, _code('unary.js')) + '\n' + SIM,
}
# a fenced block is matched within its block by a piece of its text, in this order
# a fenced block is matched within its block by a piece of its text, in this order
CODE = [('parsing', 'bool delim(char c)', 'code-simple'),
        ('right-assoc', 'bool is_unary(char c)', 'code-unary'),
        ('right-assoc', 'left_assoc(cur_op) &&', 'code-while-right'),
        ('right-assoc', 'while (!op.empty() && priority(op.top()) >= priority(cur_op))', 'code-while')]
IMAGES = {}

_ST = 'data-ref="st"'
_OP = 'data-ref="op"'
MARKS = [
    # rpn: the term, and the span the concept is introduced by
    ('rpn', '<strong>reverse Polish notation</strong>',
     '<strong><span data-concept="rpn-evaluation">reverse Polish notation</span></strong>'),
    ('rpn', 'The convenience of the reverse Polish notation is, that expressions in this form are very <strong>easy to evaluate</strong> in linear time.',
     '<span data-concept="rpn-evaluation">The convenience of the reverse Polish notation is, that expressions in this form are very '
     '<strong>easy to evaluate</strong> in linear time.</span>'),
    # parsing: the two stacks, every mention of either
    ('parsing', 'We will set up two stacks: one for numbers, and one for operators and parentheses.',
     f'<span data-concept="expression-parsing">We will set up <span data-ref="st op">two stacks</span></span>: '
     f'<span {_ST}>one for numbers</span>, and <span {_OP}>one for operators and parentheses</span>.'),
    ('parsing', 'Initially both stacks are empty.', '<span data-ref="st op">Initially both stacks</span> are empty.'),
    ('parsing', 'For the second stack', f'For <span {_OP}>the second stack</span>'),
    ('parsing', 'If there are parenthesis on the stack,', f'If there are parenthesis on <span {_OP}>the stack</span>,'),
    ('parsing', 'we put the value of this number on the stack.', f'we put the value of this number on <span {_ST}>the stack</span>.'),
    ('parsing', 'then we put it on the stack.', f'then we put it on <span {_OP}>the stack</span>.'),
    ('parsing', 'execute all operators on the stack until', f'execute all operators on <span {_OP}>the stack</span> until'),
    ('parsing', 'while the top of the stack has an operator', f'while the top of <span {_OP}>the stack</span> has an operator'),
    ('parsing', 'put the new operation on the stack.', f'put the new operation on <span {_OP}>the stack</span>.'),
    ('parsing', 'some operators might still be in the stack,', f'some operators might still be in <span {_OP}>the stack</span>,'),
    # unary: the term, the introducing span, the current operator, erratum 30
    ('unary', '<strong>unary</strong>', '<strong><span data-concept="unary-right-assoc">unary</span></strong>'),
    ('unary', 'whether the current operator is', 'whether <span data-ref="cur_op">the current operator</span> is'),
    ('unary', 'You can notice, that before an unary operator, there always is another operator or an opening parenthesis, or nothing at all',
     '<span data-concept="unary-right-assoc">You can notice, that before an unary operator, there always is another operator or an '
     'opening parenthesis, or nothing at all</span>'),
    ('unary', 'higher than all of the binary operators.', 'higher than all of the binary operators.<sup class="fn" data-note="err-unary-pow"></sup>'),
    ('unary', '<strong>right-associative</strong>', '<strong><span data-concept="unary-right-assoc">right-associative</span></strong>'),
]

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]
LEAD = ('An Advanced section on evaluating expressions with stacks: reverse Polish notation with one stack, which is '
        'Essential, then ordinary infix expressions with two stacks, then unary and right-associative operators. '
        'Expressions are read character by character, and the only index is <span data-ref="i"><em>i</em></span>, the '
        'position of the character the code is reading, counted from 0.')
ERRATUM_30 = ('With exponentiation among the binary operators, as in the next subsection, this rule reads $-2^2$ as '
              '$(-2)^2 = 4$; the usual convention reads it as $-(2^2) = -4$, which needs the unary minus to rank below '
              '$\\wedge$ and above $*$ and $/$.')

SECTION = {
    'id': '3.5', 'chapter': '3', 'title': TITLE, 'short': 'Expression evaluation',
    'lead': LEAD,
    'objectives': [], 'summary_html': '',
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': '',
    'figures': [
        {'id': 'sim-two-stack-parser', 'kind': 'sim', 'draws': ['index', 'key', 'cost'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'st', 'label': 'st, the stack of numbers', 'figures': ['sim-two-stack-parser']},
        {'id': 'op', 'label': 'op, the stack of operators and opening brackets', 'figures': ['sim-two-stack-parser']},
        {'id': 'i', 'label': 'i, the position of the character being read', 'figures': ['sim-two-stack-parser']},
        {'id': 'cur_op', 'label': 'cur_op, the operator just read', 'figures': ['sim-two-stack-parser']},
    ],
    'coverage': [
        {'span': 'rpn', 'concept': 'rpn-evaluation', 'verb': 'introduces'},
        {'span': 'parsing', 'concept': 'expression-parsing', 'verb': 'introduces'},
        {'span': 'parsing', 'concept': 'rpn-evaluation', 'verb': 'uses'},
        {'span': 'unary', 'concept': 'unary-right-assoc', 'verb': 'introduces'},
        {'span': 'unary', 'concept': 'expression-parsing', 'verb': 'uses'},
        {'span': 'right-assoc', 'concept': 'unary-right-assoc', 'verb': 'reinforces'},
        {'span': 'right-assoc', 'concept': 'expression-parsing', 'verb': 'reinforces'},
    ],
    'footnotes_extra': [{'id': 'err-unary-pow', 'kind': 'correction', 'html': ERRATUM_30}],
    'derivations': [],
}

SECTION['exercise_notes'] = (
    'The forth card is Exercism’s, with the 54 canonical cases the Exercism Python track runs as its tests and the '
    'track’s example as its Python reference; the JavaScript reference is written by the AI that built the section. The two '
    'Kattis cards keep their samples as source tests; their other tests and both references are written by the same AI. '
    'Kattis circuitmath has only its sample and is not built. TheAlgorithms’ postfix_evaluation, '
    'dijkstras_two_stack_algorithm and infix_to_postfix_conversion and tryalgo’s arithm_expr_eval carry tests but print '
    'no exercise statement, so they have no card. The Wikibooks reverse Polish traces and OpenDSA’s infix-to-postfix '
    'and postfix-evaluation exercises wait for an answer type that checks a sequence. Two pythonds self-checks are NC '
    'cards, kept in exercises-nc.json apart from the book’s CC BY-SA content; its third, postfix3, asks for a change to a '
    'function on a page this book only links, and its end-of-chapter exercises 2–5 and 10–13 print no answers, so they '
    'are left out. Kattis polish evaluates prefix expressions recursively and is held for chapter 4.')

# ---------------------------------------------------------------- exercises (config.md; plan.md "Exercises")
EXERCISM = 'sources/_cache/exercism/exercises'
TRACK = 'sources/_cache/exercism-python/exercises/practice'
KATTIS = 'sources/_cache/kattis'
FORTH_ERRORS = {'empty stack': 'StackUnderflowError', 'only one value on the stack': 'StackUnderflowError',
                'divide by zero': 'ZeroDivisionError', 'undefined operation': 'ValueError', 'illegal operation': 'ValueError'}
FORTH_STARTER_PY = '''class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    pass
'''
FORTH_STARTER_JS = '''class StackUnderflowError extends Error {
  constructor(message) { super(message); this.name = 'StackUnderflowError'; }
}
class ZeroDivisionError extends Error {
  constructor(message) { super(message); this.name = 'ZeroDivisionError'; }
}
class ValueError extends Error {
  constructor(message) { super(message); this.name = 'ValueError'; }
}

function evaluate(instructions) {
}
'''


def _inline(s):
    """Exercism Markdown inline: `code`, [text][ref] links dropped to their text."""
    s = _html.escape(s, quote=False)
    s = _re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = _re.sub(r'\[([^\]]+)\]\[[^\]]*\]', r'\1', s)
    return s.replace('$', '＄')


def md_prompt(path):
    """An Exercism description.md as the card's prompt: paragraphs and lists; link definitions dropped."""
    md = _re.sub(r'^# Instructions\s*', '', open(path, encoding='utf-8').read()).strip()
    out = []
    for blk in _re.split(r'\n\s*\n', md):
        lines = [l for l in blk.split('\n') if not _re.match(r'^\[[^\]]+\]:\s*\S', l)]
        if not lines:
            continue
        if lines[0].startswith('- '):
            out.append('<ul>' + ''.join(f'<li>{_inline(l[2:].strip())}</li>' for l in lines) + '</ul>')
        else:
            out.append(_inline(' '.join(l.strip() for l in lines)))
    return '\n\n'.join(out)


def forth_tests(book):
    """The canonical cases the Python track runs (its tests.toml sets none off but evaluateBoth), errors as the track raises them."""
    import json
    toml = open(_os.path.join(book, TRACK, 'forth/.meta/tests.toml'), encoding='utf-8').read()
    off = set(_re.findall(r'\[([0-9a-f-]+)\]\ndescription = "[^"]*"\ninclude = false', toml))
    data = json.load(open(_os.path.join(book, EXERCISM, 'forth/canonical-data.json'), encoding='utf-8'))
    out = []

    def walk(c):
        for x in c['cases']:
            if 'cases' in x:
                walk(x)
            elif x['property'] == 'evaluate' and x['uuid'] not in off:
                out.append(x)
    walk(data)
    tests = []
    for c in out:
        t = {'args': [c['input']['instructions']]}
        if isinstance(c['expected'], dict):
            t['raises'] = FORTH_ERRORS[c['expected']['error']]
        else:
            t['expect'] = c['expected']
        tests.append(t)
    visible = {0, 3, 38}           # numbers pushed; an error on an empty stack; a user-defined word
    for i, t in enumerate(tests):
        t.update(visible=i in visible, generated_by='source')
    return tests


def kattis_prompt(path):
    """A Kattis statement as the card's prompt: its paragraphs, its Input and Output headings, its maths as $…$."""
    import html as H
    s = open(path, encoding='utf-8').read()
    body = s[s.index('<div class="problembody">'):]
    body = body[:body.index('<table class="sample"')]
    body = _re.sub(r'<span class="tex2jax_process">\\\[(.*?)\\\]</span>', lambda m: '<p>$$' + m.group(1) + '$$</p>', body, flags=_re.S)
    body = _re.sub(r'<span class=\s*"tex2jax_process">(.*?)</span>', lambda m: m.group(1), body, flags=_re.S)
    body = _re.sub(r'<(code|tt)>(.*?)</\1>', lambda m: '<code>' + m.group(2) + '</code>', body, flags=_re.S)
    parts = _re.findall(r'<(p|h2)>(.*?)</\1>', body, flags=_re.S)
    out = []
    for tag, t in parts:
        t = ' '.join(t.split())
        keep = _re.findall(r'<code>.*?</code>', t)
        t = _re.sub(r'<code>(.*?)</code>', '\x00', t)
        t = H.unescape(_re.sub(r'<[^>]+>', '', t))
        t = t.replace(' < ', ' \\lt ') if '$' in t else H.escape(t, quote=False)
        for k in keep:
            t = t.replace('\x00', '<code>' + H.escape(H.unescape(k[6:-7]), quote=False) + '</code>', 1)
        out.append(f'<strong>{t}</strong>' if tag == 'h2' else t)
    return '\n\n'.join(out)


def _samples(book, slug):
    import zipfile
    z = zipfile.ZipFile(_os.path.join(book, KATTIS, 'samples', slug + '.zip'))
    names = sorted(n[:-3] for n in z.namelist() if n.endswith('.in'))
    return [(z.read(n + '.in').decode(), z.read(n + '.ans').decode()) for n in names]


def _run_py(src, stdin):
    import subprocess
    import sys
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        open(d + '/ref.py', 'w').write(src)
        return subprocess.run([sys.executable, '-I', d + '/ref.py'], input=stdin, capture_output=True, text=True, cwd=d, check=True).stdout


def _calc_exact(line):
    """The value of a calculator line, exactly: Python reads + − * / and unary minus with the statement's precedence."""
    from fractions import Fraction
    return eval(_re.sub(r'\d+', lambda m: f'Fraction({m.group(0)})', line), {'Fraction': Fraction})


CALC_AI = [
    # precedence and left-associativity, with and without brackets
    '1+2*3\n(1+2)*3\n10-4-3\n10-(4-3)\n100/10/5\n100/(10/5)\n2*3+4*5\n2*(3+4)*5\n',
    # unary minus: first, after an operator, after an opening bracket, before a bracket, twice
    '-3\n-3*-3\n-(2+3)\n(-2)*(-3)\n4*-(1+1)\n--5\n3--3\n-(-(-1))\n',
    # spaces, none and many, and the bounds of the numbers
    '  1 +   2  \n500*500*500\n-500/500\n( ( ( 7 ) ) )\n1 - - 1\n500 / 3\n',
    # quotients that do not come out even
    '1/3\n2/3\n7/9+1/9\n10/7*7\n22/7\n-1/7*3\n',
]


def _calc_long(seed, n):
    """A long bracketed expression of n numbers, for the bound and for one hidden test."""
    import random
    r = random.Random(seed)
    parts, depth = [], 0
    for k in range(n):
        if r.random() < 0.15:
            parts.append('('); depth += 1
        parts.append(str(r.randint(1, 9)))
        if depth and r.random() < 0.2:
            parts.append(')'); depth -= 1
        if k < n - 1:
            parts.append(r.choice('+-*') if r.random() < 0.9 else '/')
    return ''.join(parts) + ')' * depth


BRACKET_AI = [f'{len(t.split())}\n{t}\n' for t in [
    '7',
    '( 0 1 )',
    '1000000006 1000000006 1000000006',
    '( 1000000006 1000000006 )',
    '( 2 ( 3 4 ) ( 5 ( 6 7 ) ) )',
    '0 ( 0 ) ( 5 ) ( 0 5 )',
]]


def _bracket_deep(depth):
    """Brackets nested depth deep around 2 2: a sum and a product in turn, deeper than a recursion limit."""
    toks = ['('] * depth + ['2', '2'] + [')'] * depth
    return f'{len(toks)}\n' + ' '.join(toks) + '\n'


def _bracket_exact(stdin):
    """An independent reading: the sequence rewritten with its operators and evaluated exactly, then reduced."""
    import sys
    toks = stdin.split()[1:]
    sys.setrecursionlimit(100000)
    pos = 0

    def group(depth):
        nonlocal pos
        vals = []
        while pos < len(toks) and toks[pos] != ')':
            if toks[pos] == '(':
                pos += 1
                vals.append(group(depth + 1))
                pos += 1
            else:
                vals.append(int(toks[pos]))
                pos += 1
        acc = 1 if depth % 2 else 0
        for v in vals:
            acc = acc * v if depth % 2 else acc + v
        return acc % (10 ** 9 + 7)
    return group(0)


def EXERCISES(exercism, book):
    ex, concepts = [], []
    meta = lambda i, src, n, origin, cite: {  # noqa: E731
        'id': i, 'source_id': src, 'source_number': n, 'origin': origin, 'kind': 'code', 'bloom': 'Apply',
        'place': {'at': 'end'}, 'cite': cite}
    example = open(_os.path.join(book, TRACK, 'forth/.meta/example.py'), encoding='utf-8').read().rstrip() + '\n'
    # c1 Exercism forth: the track's 54 cases, the track's example as the Python reference
    ex.append(dict(meta('c1', 'exercism:forth', 'forth', 'exercism', 'rpn'),
                   changes=('The tests call evaluate with the list of input lines and expect the stack as a list, bottom '
                            'first. As the Exercism Python track has it, a word with too few values on the stack raises '
                            'StackUnderflowError, division by zero raises ZeroDivisionError, and an undefined word or the '
                            'redefinition of a number raises ValueError.'),
                   prompt=md_prompt(_os.path.join(book, EXERCISM, 'forth/description.md')),
                   answer={'type': 'code',
                           'python': {'entry': 'evaluate', 'starter': FORTH_STARTER_PY, 'reference': example, 'generated_by': 'source'},
                           'javascript': {'entry': 'evaluate', 'starter': FORTH_STARTER_JS, 'reference': _code('forth.js') + '\n',
                                          'generated_by': 'ai'},
                           'tests': forth_tests(book), 'generated_by': 'source'}))
    concepts.append({'exercise': 'c1', 'concept': 'rpn-evaluation'})

    # c2 Kattis calculator: the sample, then the AI's tests, each value checked exactly and kept off rounding ties
    calc_py, calc_js = _code('calculator.py') + '\n', _code('calculator.js') + '\n'
    (sin, sout), = _samples(book, 'calculator')
    assert _run_py(calc_py, sin).split() == sout.split()
    tests = [{'stdin': sin, 'stdout': sout, 'visible': True, 'generated_by': 'source'}]
    for s in CALC_AI + [_calc_long(35, 120) + '\n']:
        got = _run_py(calc_py, s)
        for line, v in zip([l for l in s.split('\n') if l.strip()], got.split()):
            x = _calc_exact(line) * 100
            assert abs(abs(x - round(x)) - 0.5) > 1e-6, ('a rounding tie', line)
            assert abs(float(v) - float(x) / 100) <= 0.005 + 1e-9, (line, v, x)
            assert v != '-0.00'
        tests.append({'stdin': s, 'stdout': got, 'generated_by': 'ai'})
    ex.append(dict(meta('c2', 'kattis:calculator', 'Calculator', 'kattis-by-sa', 'parsing'),
                   bloom='Apply', prompt=kattis_prompt(_os.path.join(book, KATTIS, 'problems/calculator.html')),
                   answer={'type': 'code',
                           'python': {'starter': 'import sys\n\nfor line in sys.stdin:\n    if not line.strip():\n        continue\n',
                                      'reference': calc_py, 'generated_by': 'ai'},
                           'javascript': {'starter': "const fs = require('fs');\nconst lines = fs.readFileSync(0, 'utf8').split('\\n').filter((l) => l.trim());\n",
                                          'reference': calc_js, 'generated_by': 'ai'},
                           'tests': tests, 'compare': 'tokens', 'bound': 'n',
                           'grow': ("(n, rand) => { let s = String(rand.int(1, 9)); for (let k = 1; k < n; k++) "
                                    "s += '+-*'[rand.int(0, 2)] + rand.int(1, 9); return s + '\\n'; }"),
                           'generated_by': 'ai'}))
    concepts += [{'exercise': 'c2', 'concept': 'expression-parsing'}, {'exercise': 'c2', 'concept': 'unary-right-assoc'}]

    # c3 Kattis bracketsequence: its six sample files, then the AI's tests, each checked by an independent reading
    br_py, br_js = _code('bracketsequence.py') + '\n', _code('bracketsequence.js') + '\n'
    tests = []
    for k, (sin, sout) in enumerate(_samples(book, 'bracketsequence')):
        assert _run_py(br_py, sin).split() == sout.split()
        tests.append({'stdin': sin, 'stdout': sout, 'visible': k == 0, 'generated_by': 'source'})
    for s in BRACKET_AI + [_bracket_deep(3000)]:
        got = _run_py(br_py, s)
        assert int(got) == _bracket_exact(s), s[:40]
        tests.append({'stdin': s, 'stdout': got, 'generated_by': 'ai'})
    ex.append(dict(meta('c3', 'kattis:bracketsequence', 'Bracket Sequence', 'kattis-by-sa', 'parsing'),
                   prompt=kattis_prompt(_os.path.join(book, KATTIS, 'problems/bracketsequence.html')),
                   answer={'type': 'code',
                           'python': {'starter': 'import sys\n\ndata = sys.stdin.read().split()\nn = int(data[0])\ntokens = data[1:1 + n]\n',
                                      'reference': br_py, 'generated_by': 'ai'},
                           'javascript': {'starter': "const fs = require('fs');\nconst data = fs.readFileSync(0, 'utf8').split(/\\s+/).filter(Boolean);\n",
                                          'reference': br_js, 'generated_by': 'ai'},
                           'tests': tests, 'compare': 'tokens', 'bound': 'n',
                           'grow': ("(n, rand) => { const t = []; let d = 0; for (let k = 0; k < n; k++) { const r = rand(); "
                                    "if (r < 0.3) { t.push('('); d++; t.push(String(rand.int(0, 9))); } else if (r < 0.5 && d > 0) "
                                    "{ t.push(')'); d--; } else t.push(String(rand.int(0, 9))); } while (d-- > 0) t.push(')'); "
                                    "return t.length + '\\n' + t.join(' ') + '\\n'; }"),
                           'generated_by': 'ai'}))
    concepts.append({'exercise': 'c3', 'concept': 'expression-parsing'})
    return ex, concepts
