"""What ch03/3.1/build.py and tools/build_section.py need to assemble 3.1 Stacks and bracket matching (the plan is
plan.md beside this file).

Two Wikipedia blocks, read from the cached wikitext of "Stack (abstract data type)" at its pinned revision
(sources/_cache/wikipedia/_meta.json: 1376688119), and two cp-algorithms blocks from
`src/combinatorics/bracket_sequences.md`. Nothing here is the sources' text: the blocks and where each starts and
stops, what stands in place of each image frame, the words a link wraps, the spans, the section record and the
exercises. The replacement table is empty: nothing needed correcting in place (err-top is a note). CITE_TEMPLATES holds
what Wikipedia prints for the one citation template of the passage that is not a `cite …` template.
"""
import json
import os

TITLE = 'Stacks and bracket matching'
AI = 'claude-opus-5-5 high'
SEC = '/cs-interview-prep-ultra'
WP = 'Stack_abstract_data_type.wiki'
CPA = 'sources/_cache/cpa/src/combinatorics/bracket_sequences.md'

BLOCKS = [
    dict(id='stack', source='wikipedia', file=WP, h2='Stacks',
         locator='wikipedia:Stack_(abstract_data_type) lead + #Non-essential operations',
         heading_shift=-1, parts=[{'lead': True}, {'section': 'Non-essential operations', 'h3': 'Non-essential operations'}]),
    dict(id='stack-implementation', source='wikipedia', file=WP, h2='Implementation',
         locator='wikipedia:Stack_(abstract_data_type)#Implementation, with ====Array==== and ====Linked list====',
         heading_shift=-1, parts=[{'section': 'Implementation'}]),
    dict(id='balanced', source='cpa', file=CPA, h2=None,
         locator='cpa:combinatorics/bracket_sequences#balanced-bracket-sequences, to “…in a similar fashion.”, before the article’s list of its problems',
         **{'from': '# Balanced bracket sequences', 'to': '## Balance validation', 'stop_at': 'In this article we discuss'}),
    dict(id='validation', source='cpa', file=CPA, h2=None,
         locator='cpa:combinatorics/bracket_sequences#balance-validation',
         **{'from': '## Balance validation', 'to': '## Number of balanced sequences'}),
]

# Wikipedia's {{Introduction to Algorithms|3|pages=232–233}}, as the template prints the third edition's citation
CITE_TEMPLATES = {
    'Introduction to Algorithms': ('Cormen, Thomas H.; Leiserson, Charles E.; Rivest, Ronald L.; Stein, Clifford (2009) [1990]. '
                                   '<em>Introduction to Algorithms</em> (3rd ed.). MIT Press and McGraw-Hill. pp.&nbsp;232–233. '
                                   'ISBN&nbsp;0-262-03384-4.'),
}

# each occurrence of a file's frame, in order: what stands there (None: left out)
IMAGES = {
    'Tallrik - Ystad-2018.jpg': [None],               # a photograph of plates: decoration (plan)
    'Lifo stack.svg': ['photo-lifo-stack'],
    'Stack UML class diagram.svg': [None],            # UML is not taught here (plan)
    'Stack Push operation-en.gif': [None],            # folded into sim-array-stack, which stands after the pop listing
    'Stack Pop Operation-en.gif': [None],
    'Linked-list-based Stack Push operation-en.gif': [None],   # folded into sim-linked-stack
    'Linked-list-based Stack Pop Operation-en.gif': [None],
}

# wikilinks whose subject this book carries and no concept span names there (RULES.md, Wikipedia's wikilinks)
WIKILINKS = {
    'Singly linked list': f'{SEC}/ch02/2.5/',
    'Dynamic array': f'{SEC}/ch02/2.2/',
}


# ---------------------------------------------------------------- figures
def sim(fid, caption, original=None, original_caption=None):
    attrs = f' data-original="{original}" data-original-caption="{original_caption}"' if original else ''
    return (f'<figure class="sim" id="{fid}"{attrs}>\n  <div class="sim-head"><span class="eyebrow">Sim</span>'
            f'<span>{caption}</span></div>\n</figure>')


def R(ref, word):
    return f'<span data-ref="{ref}">{word}</span>'


CAP_ARRAY = (
    f'The stack is the cells below {R("top", "top")}: a push writes at {R("top", "top")} and moves it up, a pop moves it down '
    f'and reads the cell it lands on. Each call touches one cell, however full the array is. Pushing onto a full array is '
    f'overflow and popping an empty one is underflow, and both are caught before any cell is touched.')
CAP_LINKED = (
    f'A push makes {R("newhead", "newhead")}, points it at the old {R("head", "head")} and makes it the new '
    f'{R("head", "head")}; a pop takes {R("head", "head")}’s data and moves {R("head", "head")} one link on. Each call writes '
    f'at most two links, whatever the size, and the list never fills up; popping an empty one is still underflow.')
CAP_BRACKETS = (
    'With one bracket type, depth counts the brackets still open, and the line under the string must never go below 0 and '
    'must end at 0. With several types, the stack holds the open brackets themselves, and its height is that same line, '
    'but ([)] stays above 0 and ends at 0 and is still not balanced: only the stack sees that ) closes a [.')
HTML = {
    'photo-lifo-stack': (
        '<figure class="photo" id="photo-lifo-stack">\n'
        '  <img src="/media/ch03/wp-lifo-stack.png" alt="">\n'
        '  <figcaption><span>{{caption Lifo stack.svg}}. Image: vectorization by Alhadis, Wikimedia Commons, CC0.</span></figcaption>\n'
        '</figure>'),
    'sim-array-stack': sim('sim-array-stack', CAP_ARRAY, '/media/ch03/wp-stack-push.gif,/media/ch03/wp-stack-pop.gif',
                           '{{caption-text Stack Push operation-en.gif}}. {{caption-text Stack Pop Operation-en.gif}}. '
                           'Images: Michel Bakni, Wikimedia Commons, CC BY-SA 4.0.'),
    'sim-linked-stack': sim('sim-linked-stack', CAP_LINKED, '/media/ch03/wp-linked-stack-push.gif,/media/ch03/wp-linked-stack-pop.gif',
                            '{{caption-text Linked-list-based Stack Push operation-en.gif}}. '
                            '{{caption-text Linked-list-based Stack Pop Operation-en.gif}}. '
                            'Images: Michel Bakni, Wikimedia Commons, CC BY-SA 4.0.'),
    'sim-brackets': sim('sim-brackets', CAP_BRACKETS),
}
# a figure after the element holding the anchor (the pop listings, whose GIFs the Sims fold)
AT = [
    ('stack-implementation', 'r ← stk.items[stk.top]', 'sim-array-stack'),
    ('stack-implementation', 'stk.size ← stk.size - 1', 'sim-linked-stack'),
    ('validation', 'If at any time one of the conditions is not fulfilled', 'sim-brackets'),
]

# ---------------------------------------------------------------- spans
FN_TOP = '<sup class="fn" data-note="err-top"></sup>'
FIXES = []
MARKS = [
    # the concepts where each passage names them first
    ('stack', '<strong>stack</strong>', '<span data-concept="stack"><strong>stack</strong></span>'),
    ('balanced', '<strong>balanced bracket sequence</strong>',
     '<span data-concept="balanced-brackets"><strong>balanced bracket sequence</strong></span>'),
    ('validation', 'We want to check if a given string is balanced or not.',
     'We want to <span data-concept="bracket-validation">check if a given string is balanced</span> or not.'),
    # the array stack's variable top, as the Array paragraphs name it (the referent of sim-array-stack)
    ('stack-implementation', '<em>top</em>', '<span data-ref="top"><em>top</em></span>', 3),
    # err-top: top counts the items on the stack now, not those pushed so far
    ('stack-implementation', 'pushed so far', 'pushed so far' + FN_TOP),
    # the linked stack's head (the referent of sim-linked-stack)
    ('stack-implementation', '"head"', '"<span data-ref="head">head</span>"'),
    ('stack-implementation', 'happens at the head of the list', 'happens at the <span data-ref="head">head</span> of the list'),
    # the cost bound the prose prints in plain text (as 2.5 marks Wikipedia's)
    ('stack-implementation', 'amortized O(1) time', 'amortized <span data-type="cost">O(1)</span> time'),
]

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]
LEAD = (
    'An Essential section on the <span data-concept="stack">stack</span>, the last-in, first-out collection, and on using one '
    'to <span data-concept="bracket-validation">check that a string’s brackets balance</span>. Indexing is 0-based: '
    'the array stack’s <span data-ref="top">top</span> counts the items on it and names the next free cell. The array-backed '
    f'stack is the ArrayStack of <a href="{SEC}/ch02/2.2/">Section 2.2</a> in another notation; the linked-list stack pushes '
    f'and pops at the <span data-ref="head">head</span> of the singly linked list of <a href="{SEC}/ch02/2.5/">Section 2.5</a>.')

EXERCISE_NOTES = (
    'Exercism’s matching-brackets and simple-linked-list keep their canonical cases (simple-linked-list as the Python track '
    'runs them, last in first out); Donne Martin’s stack challenge keeps his tests; their JavaScript references, and the '
    'Kattis tests beyond the five samples and both Kattis references, are the AI’s. OpenDSA’s stack questions wait for the '
    'converter of OpenDSA’s exercises, and its push and pop proficiency exercises and the seven Wikibooks stack traces for '
    'an answer type that takes a sequence. ODS Exercises 1.2 and 1.3 have no key. Kattis brackets, bracketmatching and GCPC '
    '2023’s loopinvariant were not judged a good fit, and Kattis backspace and throwns are over the cap of two code '
    'exercises for the stack. TheAlgorithms’ stack and balanced-parentheses doctests are tests without a printed statement, '
    'and trekhleb’s valid-parentheses tests read an empty string as unbalanced and a space as a wrong closing bracket, '
    'against Exercism’s statement, so they are not used. pythonds’ end-of-chapter exercises 19 and 30 have no key.')

SECTION = {
    'id': '3.1', 'chapter': '3', 'title': 'Stacks and bracket matching', 'short': 'Stacks and brackets',
    'lead': LEAD, 'objectives': [], 'summary_html': '',
    'notes': ('The stack article’s history, hardware stacks, applications and security, its photograph of plates and its UML '
              'diagram are left out, as are the bracket article’s counting and enumeration problems.'),
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'built': '2026-11-09',
    'exercise_notes': EXERCISE_NOTES,
    'figures': [
        {'id': 'photo-lifo-stack', 'kind': 'photo'},
        {'id': 'sim-array-stack', 'kind': 'sim',
         'originals': ['/media/ch03/wp-stack-push.gif', '/media/ch03/wp-stack-pop.gif'],
         'original_caption': ('{{caption-text Stack Push operation-en.gif}}. {{caption-text Stack Pop Operation-en.gif}}. '
                              'Images: Michel Bakni, Wikimedia Commons, CC BY-SA 4.0.'),
         'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
        {'id': 'sim-linked-stack', 'kind': 'sim',
         'originals': ['/media/ch03/wp-linked-stack-push.gif', '/media/ch03/wp-linked-stack-pop.gif'],
         'original_caption': ('{{caption-text Linked-list-based Stack Push operation-en.gif}} '
                              '{{caption-text Linked-list-based Stack Pop Operation-en.gif}} '
                              'Images: Michel Bakni, Wikimedia Commons, CC BY-SA 4.0.'),
         'draws': ['key', 'cost', 'size'], 'ai': FIG_AI},
        {'id': 'sim-brackets', 'kind': 'sim', 'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
    ],
    'coverage': [
        {'span': 'stack', 'concept': 'stack', 'verb': 'introduces'},
        {'span': 'stack-implementation', 'concept': 'stack', 'verb': 'uses'},
        {'span': 'stack-implementation', 'concept': 'dynamic-array', 'verb': 'uses'},
        {'span': 'stack-implementation', 'concept': 'singly-linked-list', 'verb': 'uses'},
        {'span': 'balanced', 'concept': 'balanced-brackets', 'verb': 'introduces'},
        {'span': 'validation', 'concept': 'bracket-validation', 'verb': 'introduces'},
        {'span': 'validation', 'concept': 'stack', 'verb': 'uses'},
        {'span': 'validation', 'concept': 'balanced-brackets', 'verb': 'uses'},
    ],
    'referents': [
        {'id': 'top', 'label': 'top, the number of items on the array stack and its next free cell', 'figures': ['sim-array-stack']},
        {'id': 'head', 'label': 'head, the frame on top of the linked stack', 'figures': ['sim-linked-stack']},
        {'id': 'newhead', 'label': 'newhead, the frame being pushed', 'figures': ['sim-linked-stack']},
    ],
    'footnotes_extra': [
        {'id': 'err-top', 'kind': 'correction',
         'html': ('<em>top</em> counts the items on the stack now, not every item pushed so far: each pop takes 1 from it. So '
                  'it is the number pushed less the number popped, and that is also the cell the next push writes to.')},
    ],
}


# ---------------------------------------------------------------- exercises
EXERCISM = 'sources/_cache/exercism/exercises'
TRACK = 'sources/_cache/exercism-python/exercises/practice'
ICC = 'sources/_cache/icc/stacks_queues/stack'
KATTIS = 'sources/_cache/kattis'


def _inline(s):
    import html
    import re
    s = html.escape(s, quote=False).replace('$', '＄')
    s = re.sub(r'\[([^\]]+)\]\[[^\]]*\]', r'\1', s)          # a reference-style link: its words
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    return re.sub(r'(?<![\w])_([^_]+)_(?![\w])', r'<em>\1</em>', s)


def md_prompt(path):
    """An Exercism instructions.md as the card's prompt: its paragraphs; an `exercism/note` box read as its paragraphs,
    its link-reference lines left out (the link's words stay)."""
    import re
    md = re.sub(r'^# Instructions\s*', '', open(path, encoding='utf-8').read()).strip()
    md = re.sub(r'^~~~~exercism/note\s*$|^~~~~\s*$', '', md, flags=re.M)
    out = []
    for blk in re.split(r'\n\s*\n', md):
        lines = [l for l in blk.split('\n') if l.strip() and not re.match(r'^\[[^\]]+\]:\s', l)]
        if lines:
            out.append(_inline(' '.join(x.strip() for x in lines)))
    return '\n\n'.join(out)


def track_cases(book, slug):
    """The canonical cases the Python track runs: every case its tests.toml does not set include = false."""
    import re
    toml = open(os.path.join(book, TRACK, slug, '.meta/tests.toml'), encoding='utf-8').read()
    off = set(re.findall(r'\[([0-9a-f-]+)\]\ndescription = "[^"]*"\ninclude = false', toml))
    data = json.load(open(os.path.join(book, EXERCISM, slug, 'canonical-data.json'), encoding='utf-8'))
    out = []

    def walk(c, group=''):
        for x in c['cases']:
            if 'cases' in x:
                walk(x, x['description'])
            elif x['uuid'] not in off:
                out.append(dict(x, group=group))
    walk(data)
    return out


def example(book, slug):
    return open(os.path.join(book, TRACK, slug, '.meta/example.py'), encoding='utf-8').read().rstrip() + '\n'


# -- c1 Exercism simple-linked-list: the Python track's LinkedList, driven by a given run(initial_values, operations)
SLL_RUN_PY = '''

def run(initial_values, operations):
    """Given: builds LinkedList(initial_values), plays the operations on it and returns what the queries give."""
    lst = LinkedList(initial_values)
    out = []
    for op in operations:
        name = op['operation']
        if name == 'push':
            lst.push(op['value'])
        elif name == 'pop':
            out.append(lst.pop())
        elif name == 'peek':
            out.append(lst.head().value())
        elif name == 'count':
            out.append(len(lst))
        elif name == 'toList':
            out.append(list(lst))
        elif name == 'reverse':
            lst = lst.reversed()
    return out
'''
SLL_STARTER_PY_HEAD = '''class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, value):
        pass

    def value(self):
        pass

    def next(self):
        pass


class LinkedList:
    def __init__(self, values=None):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def head(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass

    def reversed(self):
        pass
'''
SLL_RUN_JS = '''

// Given: builds new LinkedList(initialValues), plays the operations on it and returns what the queries give.
function run(initialValues, operations) {
    let lst = new LinkedList(initialValues);
    const out = [];
    for (const op of operations) {
        const name = op.operation;
        if (name === 'push') lst.push(op.value);
        else if (name === 'pop') out.push(lst.pop());
        else if (name === 'peek') out.push(lst.head().value());
        else if (name === 'count') out.push(lst.length);
        else if (name === 'toList') out.push([...lst]);
        else if (name === 'reverse') lst = lst.reversed();
    }
    return out;
}
'''
SLL_STARTER_JS = '''class EmptyListException extends Error {
    constructor(message) {
        super(message);
        this.name = 'EmptyListException';
    }
}

class Node {
    constructor(value) {
    }

    value() {
    }

    next() {
    }
}

class LinkedList {
    constructor(values = []) {
    }

    [Symbol.iterator]() {
    }

    get length() {
    }

    head() {
    }

    push(value) {
    }

    pop() {
    }

    reversed() {
    }
}'''
SLL_REF_JS = '''class EmptyListException extends Error {
    constructor(message) {
        super(message);
        this.name = 'EmptyListException';
    }
}

class Node {
    constructor(value) {
        this._value = value;
        this._next = null;
    }

    value() {
        return this._value;
    }

    next() {
        return this._next;
    }
}

class LinkedList {
    constructor(values = []) {
        this._head = null;
        this._len = 0;
        for (const value of values) this.push(value);
    }

    *[Symbol.iterator]() {
        let current = this._head;
        while (current !== null) {
            yield current.value();
            current = current.next();
        }
    }

    get length() {
        return this._len;
    }

    head() {
        if (this._head === null) throw new EmptyListException('The list is empty.');
        return this._head;
    }

    push(value) {
        const node = new Node(value);
        node._next = this._head;
        this._head = node;
        this._len += 1;
    }

    pop() {
        if (this._head === null) throw new EmptyListException('The list is empty.');
        const value = this._head.value();
        this._head = this._head.next();
        this._len -= 1;
        return value;
    }

    reversed() {
        return new LinkedList(this);
    }
}'''

# -- c2 icc stack: Donne Martin's Stack, driven by a given run(ops)
ICC_RUN_PY = '''

def run(ops):
    """Given: plays the tests' operations on a Stack and returns what pop, peek and is_empty give."""
    out, stack = [], None
    for op, *args in ops:
        if op == 'new':
            stack = Stack(Node(args[0]) if args else None)
        elif op == 'push':
            stack.push(args[0])
        else:
            out.append(getattr(stack, op)())
    return out
'''
ICC_RUN_JS = '''

// Given: plays the tests' operations on a Stack and returns what pop, peek and isEmpty give.
function run(ops) {
    const out = [];
    let stack = null;
    const call = { pop: 'pop', peek: 'peek', is_empty: 'isEmpty' };
    for (const [op, ...args] of ops) {
        if (op === 'new') stack = new Stack(args.length ? new Node(args[0]) : null);
        else if (op === 'push') stack.push(args[0]);
        else out.push(stack[call[op]]());
    }
    return out;
}
'''
ICC_STARTER_JS = '''class Node {
    constructor(data, next = null) {
        // TODO: Implement me
    }
}

class Stack {
    constructor(top = null) {
        // TODO: Implement me
    }

    push(data) {
        // TODO: Implement me
    }

    pop() {
        // TODO: Implement me
    }

    peek() {
        // TODO: Implement me
    }

    isEmpty() {
        // TODO: Implement me
    }
}'''
ICC_REF_JS = '''class Node {
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }
}

class Stack {
    constructor(top = null) {
        this.top = top;
    }

    push(data) {
        this.top = new Node(data, this.top);
    }

    pop() {
        if (this.top === null) return null;
        const data = this.top.data;
        this.top = this.top.next;
        return data;
    }

    peek() {
        return this.top !== null ? this.top.data : null;
    }

    isEmpty() {
        return this.peek() === null;
    }
}'''
# test_stack.py's end-to-end test, its three parts as three operation lists (the asserts in order)
ICC_TESTS = [
    ([['new'], ['peek'], ['pop']], [None, None]),
    ([['new', 5], ['pop'], ['peek']], [5, None]),
    ([['new'], ['push', 1], ['push', 2], ['push', 3], ['pop'], ['peek'], ['pop'], ['peek'], ['is_empty'], ['pop'], ['peek'],
      ['is_empty']], [3, 2, 2, 1, False, 1, None, True]),
]


def icc_prompt(book):
    nb = json.load(open(os.path.join(book, ICC, 'stack_challenge.ipynb'), encoding='utf-8'))
    cells = [''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'markdown']
    problem = next(c for c in cells if c.startswith('## Problem:')).split('\n')[0][len('## Problem: '):].strip()
    cons = next(c for c in cells if c.startswith('## Constraints')).split('\n')[1:]
    qa = []
    for line in cons:
        line = line.rstrip()
        if line.startswith('* '):
            qa.append([line[2:].strip(), None])
        elif line.strip().startswith('* ') and qa:
            qa[-1][1] = line.strip()[2:].strip()
    return problem + '\n\n' + '\n\n'.join(f'{q} {a}.' for q, a in qa)


def icc_starter_py(book):
    nb = json.load(open(os.path.join(book, ICC, 'stack_challenge.ipynb'), encoding='utf-8'))
    return next(''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'code' and 'class Stack' in ''.join(c['source'])).rstrip() + '\n'


# -- c3 Exercism matching-brackets: the track's example, and the AI's JavaScript
BRACKETS_JS = '''function isPaired(inputString) {
    const counterparts = { ')': '(', '}': '{', ']': '[' };
    const stack = [];
    for (const char of inputString) {
        if ('({['.includes(char)) {
            stack.push(char);
        } else if (char in counterparts) {
            if (stack.length === 0) return false;
            if (stack.pop() !== counterparts[char]) return false;
        }
    }
    return stack.length === 0;
}
'''

# -- c4 Kattis delimitersoup: a program on stdin, the AI's references
SOUP_PY = '''import sys

lines = sys.stdin.read().split('\\n')
length = int(lines[0])
program = lines[1][:length]

opening = {')': '(', ']': '[', '}': '{'}
stack = []
error = None
for i, c in enumerate(program):
    if c in '([{':
        stack.append(c)
    elif c in opening:
        if not stack or stack[-1] != opening[c]:
            error = f'{c} {i}'
            break
        stack.pop()

print(error if error is not None else 'ok so far')
'''
SOUP_JS = '''const lines = require('fs').readFileSync(0, 'utf8').split('\\n');
const length = parseInt(lines[0], 10);
const program = (lines[1] || '').slice(0, length);

const opening = { ')': '(', ']': '[', '}': '{' };
const stack = [];
let error = null;
for (let i = 0; i < program.length; i++) {
    const c = program[i];
    if ('([{'.includes(c)) {
        stack.push(c);
    } else if (c in opening) {
        if (stack.length === 0 || stack[stack.length - 1] !== opening[c]) {
            error = `${c} ${i}`;
            break;
        }
        stack.pop();
    }
}
console.log(error !== null ? error : 'ok so far');
'''
# the AI's tests beyond the samples: each a program line; its answer is checked against a second reading (soup_check)
SOUP_AI = [
    ')', '(', '([)]', '{[()]}', '(((', ']', '( ] )', '{ } } {', '[(])', '()[]{}', '(' * 100 + ')' * 100,
    '(' * 100 + '[' * 99 + ')', '{' + '()' * 99 + ']',
]


def soup_check(program):
    """The answer by another reading of the statement: the first closing delimiter at which the program, read so far
    with every adjacent matched pair removed again and again, does not reduce to opening delimiters only."""
    import re
    for i, c in enumerate(program):
        if c not in ')]}':
            continue
        s = re.sub(r'\s', '', program[:i + 1])
        prev = None
        while prev != s:
            prev, s = s, s.replace('()', '').replace('[]', '').replace('{}', '')
        if any(ch in ')]}' for ch in s):
            return f'{c} {i}'
    return 'ok so far'


def kattis_prompt(path):
    """The statement's paragraphs, its Input, Output and Limits headings and its limits list; ‘<tt>…</tt>’ as code."""
    import html as H
    import re
    s = open(path, encoding='utf-8').read()
    body = s[s.index('<div class="problembody">'):]
    body = body[:body.index('<table class="sample"')]
    body = re.sub(r'<div style="width:[^"]*" class="illustration">.*?</div>\s*</div>', '', body, flags=re.S)
    body = re.sub(r'<span class=\s*"tex2jax_process">(.*?)</span>', lambda m: m.group(1), body, flags=re.S)
    out = []
    for tag, t in re.findall(r'<(p|h2|li)>(.*?)</\1>', body, flags=re.S):
        if tag == 'li':
            continue
        t = re.sub(r'<tt[^>]*>(.*?)</tt>', lambda m: '\x00' + ' '.join(m.group(1).split()) + '\x01', t, flags=re.S)
        t = ' '.join(H.unescape(re.sub(r'<[^>]+>', '', t)).split())
        t = t.replace(' \\leq ', ' \\le ')
        t = H.escape(t, quote=False).replace('\x00', '<code>').replace('\x01', '</code>')
        out.append(f'<strong>{t}</strong>' if tag == 'h2' else t)
    # the Limits list, its items as one list
    items = []
    for t in re.findall(r'<li>\s*<p>(.*?)</p>\s*</li>', body, flags=re.S):
        t = re.sub(r'<tt[^>]*>(.*?)</tt>', lambda m: '\x00' + m.group(1) + '\x01', t, flags=re.S)
        t = ' '.join(H.unescape(re.sub(r'<[^>]+>', '', t)).split())
        items.append(H.escape(t, quote=False).replace('\x00', '<code>').replace('\x01', '</code>'))
    i = out.index('<strong>Limits</strong>')
    out = out[:i + 1] + ['<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'] + out[i + 1:]
    return '\n\n'.join(out)


def _run(src, stdin):
    import subprocess
    import sys
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = d + '/ref.py'
        open(p, 'w').write(src)
        return subprocess.run([sys.executable, '-I', p], input=stdin, capture_output=True, text=True, cwd=d, check=True).stdout


def EXERCISES(exercism, book):
    import zipfile
    ex, concepts = [], []
    meta = lambda i, src, n, origin, cite: {  # noqa: E731
        'id': i, 'source_id': src, 'source_number': n, 'origin': origin, 'kind': 'code', 'bloom': 'Apply',
        'place': {'at': 'end'}, 'cite': cite}

    # c1 Exercism simple-linked-list: the canonical cases the Python track runs, the toList FIFO group left out (LIFO)
    tests = []
    for c in track_cases(book, 'simple-linked-list'):
        if c['group'] == 'toList FIFO':
            continue
        inp = c['input']
        ops = [{k: v for k, v in o.items() if k != 'expected'} for o in inp['operations']]
        exp = [o['expected'] for o in inp['operations'] if 'expected' in o]
        t = {'args': [inp.get('initialValues', []), ops]}
        if any(isinstance(e, dict) and 'error' in e for e in exp):
            t['raises'] = 'EmptyListException'
        else:
            t['expect'] = exp
        tests.append(t)
    for i, t in enumerate(tests):
        t.update(visible=i in (2, 12), generated_by='source')
    ex.append(dict(meta('c1', 'exercism:simple-linked-list', 'simple-linked-list', 'exercism', 'stack-implementation'),
                   changes=('The tests call run(initial_values, operations), given in the starter, on your LinkedList: push, '
                            'pop, len for the count, head().value() for a peek, iteration for the list (the last value pushed '
                            'first) and reversed(). pop and head on an empty list raise EmptyListException("The list is '
                            'empty.").'),
                   prompt=md_prompt(os.path.join(book, EXERCISM, 'simple-linked-list/instructions.md')),
                   answer={'type': 'code',
                           'python': {'entry': 'run', 'starter': SLL_STARTER_PY_HEAD + SLL_RUN_PY,
                                      'reference': example(book, 'simple-linked-list') + SLL_RUN_PY, 'generated_by': 'source'},
                           'javascript': {'entry': 'run', 'starter': SLL_STARTER_JS + SLL_RUN_JS, 'reference': SLL_REF_JS + SLL_RUN_JS,
                                          'generated_by': 'ai'},
                           'tests': tests, 'generated_by': 'source'}))
    concepts += [{'exercise': 'c1', 'concept': 'stack'}, {'exercise': 'c1', 'concept': 'singly-linked-list'}]

    # c2 icc stack: Donne Martin's end-to-end test as three operation lists, his stack.py as the reference
    ref_py = open(os.path.join(book, ICC, 'stack.py'), encoding='utf-8').read().rstrip() + '\n'
    tests = [{'args': [ops], 'expect': exp, 'visible': i < 2, 'generated_by': 'source'} for i, (ops, exp) in enumerate(ICC_TESTS)]
    ex.append(dict(meta('c2', 'icc:stacks_queues/stack', 'stack', 'icc', 'stack-implementation'),
                   changes=('The tests are the source’s end-to-end test in its three parts, each a list of operations that a '
                            'given run(ops) plays on your Stack; Stack(Node(5)) starts a stack whose top is 5.'),
                   prompt=icc_prompt(book),
                   answer={'type': 'code',
                           'python': {'entry': 'run', 'starter': icc_starter_py(book) + ICC_RUN_PY, 'reference': ref_py + ICC_RUN_PY,
                                      'generated_by': 'source'},
                           'javascript': {'entry': 'run', 'starter': ICC_STARTER_JS + ICC_RUN_JS, 'reference': ICC_REF_JS + ICC_RUN_JS,
                                          'generated_by': 'ai'},
                           'tests': tests, 'generated_by': 'source'}))
    concepts.append({'exercise': 'c2', 'concept': 'stack'})

    # c3 Exercism matching-brackets: the 20 canonical cases, the track's example
    tests = []
    for i, c in enumerate(track_cases(book, 'matching-brackets')):
        tests.append({'args': [c['input']['value']], 'expect': c['expected'], 'visible': i in (0, 6), 'generated_by': 'source'})
    ex.append(dict(meta('c3', 'exercism:matching-brackets', 'matching-brackets', 'exercism', 'validation'),
                   changes='A solution must run in time linear in the length of the string; the source asks for no bound.',
                   prompt=md_prompt(os.path.join(book, EXERCISM, 'matching-brackets/instructions.md')),
                   answer={'type': 'code',
                           'python': {'entry': 'is_paired', 'starter': 'def is_paired(input_string):\n    pass\n',
                                      'reference': example(book, 'matching-brackets'), 'generated_by': 'source'},
                           'javascript': {'entry': 'isPaired', 'starter': 'function isPaired(inputString) {\n}\n',
                                          'reference': BRACKETS_JS, 'generated_by': 'ai'},
                           'tests': tests, 'bound': 'n',
                           'grow': ("(n, rand) => { const o = Array.from({ length: Math.floor(n / 2) }, () => '([{'[rand.int(0, 2)]); "
                                    "const c = { '(': ')', '[': ']', '{': '}' }; "
                                    "return [o.join('') + o.slice().reverse().map((x) => c[x]).join('')]; }"),
                           'generated_by': 'source'}))
    concepts.append({'exercise': 'c3', 'concept': 'bracket-validation'})

    # c4 Kattis delimitersoup: the five samples, then the AI's tests, each answer checked by a second reading
    z = zipfile.ZipFile(os.path.join(book, KATTIS, 'samples', 'delimitersoup.zip'))
    tests = []
    for k in range(1, 6):
        sin, sout = z.read(f'0{k}.in').decode(), z.read(f'0{k}.ans').decode()
        assert _run(SOUP_PY, sin).strip() == sout.strip(), (k, sin)
        assert soup_check(sin.split('\n')[1][:int(sin.split()[0])]) == sout.strip(), k
        tests.append({'stdin': sin, 'stdout': sout, 'visible': k <= 2, 'generated_by': 'source'})
    for prog in SOUP_AI:
        sin = f'{len(prog)}\n{prog}\n'
        got = _run(SOUP_PY, sin)
        assert got.strip() == soup_check(prog), (prog, got)
        tests.append({'stdin': sin, 'stdout': got, 'generated_by': 'ai'})
    ex.append(dict(meta('c4', 'kattis:delimitersoup', 'Delimiter Soup', 'kattis-by-sa', 'validation'),
                   prompt=kattis_prompt(os.path.join(book, KATTIS, 'problems', 'delimitersoup.html')),
                   answer={'type': 'code',
                           'python': {'starter': "import sys\n\nlines = sys.stdin.read().split('\\n')\n", 'reference': SOUP_PY,
                                      'generated_by': 'ai'},
                           'javascript': {'starter': "const lines = require('fs').readFileSync(0, 'utf8').split('\\n');\n",
                                          'reference': SOUP_JS, 'generated_by': 'ai'},
                           'tests': tests, 'generated_by': 'ai'}))
    concepts.append({'exercise': 'c4', 'concept': 'bracket-validation'})
    return ex, concepts
