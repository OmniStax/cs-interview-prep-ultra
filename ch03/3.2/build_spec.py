"""What tools/build_text.py needs to assemble 3.2 Queues and circular buffers (the plan is plan.md beside this file).

Everything here is placement, markup or what the plan decided; the source's words come from the converters.
ODS's prose is its pseudocode edition (METHOD decision 20), read by tools/read_latex.py (dialect `ods`), as 2.2
reads it. ODS's listings (\\codeimport) are four-language code sets: Python, Java and C++ read from ODS's own
sources by tools/ods_listing.py as the editions print them (printed=True); JavaScript translated by the AI from
the Java (CODE_TRANSLATIONS) and AI-marked. No FIXES table: the reader's output needs no correction.
"""
import html
import json
import os
import re
import sys

_BOOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(_BOOK, 'tools'))
import ods_listing  # noqa: E402
import read_latex  # noqa: E402

TITLE = 'Queues and circular buffers'
INTRO = 'sources/_cache/ods/latex/intro.tex'
ARRAYS = 'sources/_cache/ods/latex/arrays.tex'
LINKED = 'sources/_cache/ods/latex/linkedlists.tex'
_ODS = dict(source='ods', reader='latex', dialect='ods')

BLOCKS = [
    # intro.tex §The Queue, Stack, and Deque Interfaces: the opening paragraph with its list, the FIFO paragraph and
    # fig. queue; the priority-queue paragraph (chapter 9), the LIFO paragraph (the stack is Wikipedia's, 3.1) and the
    # Deque paragraph (3.3) are not carried. The source's heading names Stack and Deque too, so the block opens on an
    # OmniStax header naming its concept.
    dict(id='queue', **_ODS, file=INTRO, chapter=1, drop_first_heading=True,
         parts=[('\\subsection{The #Queue#, #Stack#, and #Deque# Interfaces}', 'A \\emph{priority #Queue#}')],
         locator='ods:intro#the-queue-stack-and-deque-interfaces, the opening paragraph and its list, the FIFO paragraph '
                 'and fig. queue (to “…called enqueue(x) and dequeue(), respectively.”)',
         h2='The Queue Interface'),
    # arrays.tex §ArrayQueue, its circular-array half: the section's one-sentence opening, then from “Notice that an
    # ArrayStack is a poor choice” to “…does not exceed the size of a.”
    dict(id='circular', **_ODS, file=ARRAYS, chapter=2, drop_first_heading=True,
         parts=[('\\section{#ArrayQueue#', '\\codeimport{ods/ArrayQueue.a.j.n}')],
         locator='ods:arrays#sec:arrayqueue, from the opening through “…does not exceed the size of a.” (the circular array)',
         h2='ArrayQueue: An Array-Based Queue'),
    # the rest of §ArrayQueue, from the first listing to the end of its Summary, under a header of OmniStax's (the
    # source's section runs on)
    dict(id='arrayqueue', **_ODS, file=ARRAYS, chapter=2,
         parts=[('\\codeimport{ods/ArrayQueue.a.j.n}', '\\section{#ArrayDeque#')],
         locator='ods:arrays#sec:arrayqueue, from the first code import (ArrayQueue.a.j.n) to the end of “Summary”',
         h2='ArrayQueue’s add(x), remove() and resize()'),
    # linkedlists.tex §SLList: “Queue Operations”, then the paragraph after thm:sllist (the tail-removal paragraph);
    # the Summary heading and theorem between them are SLList's (Stack and Queue) and are not carried
    dict(id='linked-queue', **_ODS, file=LINKED, chapter=3, drop_first_heading=True,
         parts=[('\\subsection{Queue Operations}', '\\subsection{Summary}'),
                ('An #SLList# nearly implements the full set', '\\section{#DLList#')],
         locator='ods:linkedlists#sec:sllist, “Queue Operations” and the paragraph after thm:sllist (“An SLList nearly '
                 'implements the full set of Deque operations…”)',
         h2='Queue Operations'),
]

# ODS's figure numbers stay as printed and link to the Sims that stand for them (book RULES, Cross-references)
LATEX_REFS = {
    'figref:queue': ('<a href="#sim-fifo-queue">Figure 1.1</a>', 'Figure 1.1'),
    'figref:arrayqueue': ('<a href="#sim-arrayqueue">Figure 2.2</a>', 'Figure 2.2'),
}
FIGURE_AT = {'queue': 'sim-fifo-queue', 'arrayqueue': 'sim-arrayqueue'}

AI = 'claude-opus-5-5 high'

# JavaScript for each listing, translated by the AI from ODS's Java line for line (same names, same order), keyed
# by the listing's reference. Java's NoSuchElementException is a plain Error.
CODE_TRANSLATIONS = {
    'ods/ArrayQueue.a.j.n': '''
a;
j;
n;
''',
    'ods/ArrayQueue.add(x)': '''
add(x) {
    if (this.n + 1 > this.a.length) this.resize();
    this.a[(this.j+this.n) % this.a.length] = x;
    this.n++;
    return true;
}
''',
    'ods/ArrayQueue.remove()': '''
remove() {
    if (this.n === 0) throw new Error("no such element");
    const x = this.a[this.j];
    this.j = (this.j + 1) % this.a.length;
    this.n--;
    if (this.a.length >= 3*this.n) this.resize();
    return x;
}
''',
    'ods/ArrayQueue.resize()': '''
resize() {
    const b = new Array(Math.max(1, this.n*2));
    for (let k = 0; k < this.n; k++)
        b[k] = this.a[(this.j+k) % this.a.length];
    this.a = b;
    this.j = 0;
}
''',
    'ods/SLList.remove()': '''
remove() {
    if (this.n === 0) return null;
    const x = this.head.x;
    this.head = this.head.next;
    if (--this.n === 0) this.tail = null;
    return x;
}
''',
    'ods/SLList.add(x)': '''
add(x) {
    const u = new Node();
    u.x = x;
    if (this.n === 0) {
        this.head = u;
    } else {
        this.tail.next = u;
    }
    this.tail = u;
    this.n++;
    return true;
}
''',
}


def listing(ref):
    """The listing ODS's \\codeimport{ref} names, in the four languages: {python, java, cpp, javascript, _ai}."""
    cls, members = ref.split('/', 1)[1].split('.', 1)
    return {'python': ods_listing.python(cls, members, printed=True), 'java': ods_listing.java(cls, members, printed=True),
            'cpp': ods_listing.cpp(cls, members, printed=True), 'javascript': CODE_TRANSLATIONS[ref].strip('\n'),
            '_ai': {'javascript'}}


def _code_set(v, set_id=None):
    pres = []
    for lang in ('python', 'java', 'cpp', 'javascript'):
        mark = f' data-ai="{AI}"' if lang in v['_ai'] else ''
        body = html.escape(v[lang].strip('\n'), quote=False).replace('$', '&#36;')
        pres.append(f'<pre data-lang="{lang}"{mark}><code>{body}</code></pre>')
    attr = f' id="{set_id}"' if set_id else ''
    return f'<div class="code-set"{attr}>\n' + '\n'.join(pres) + '\n</div>'


# the code sets that carry an id: array-queue's coverage names the first ArrayQueue listing, queue-linked-list's
# the add(x) listing that the span's paragraph introduces
SET_IDS = {'ods/ArrayQueue.a.j.n': 'arrayqueue-code', 'ods/SLList.add(x)': 'sllist-add-code'}


def CODE_HOOK(e):
    """ODS's listings: every \\codeimport as a code set (the pseudocode edition comments out \\cppimport and
    \\javaimport, so they print nothing; none stands in these passages)."""
    if e['cmd'] == 'codeimport':
        return _code_set(listing(e['ref']), SET_IDS.get(e['ref']))
    return ''


# ---------------------------------------------------------------- the figures' original captions, as plain text

CAPTIONS_INTRO = read_latex.figure_captions(os.path.join(_BOOK, INTRO), 1, 'ods')
CAPTIONS_ARRAYS = read_latex.figure_captions(os.path.join(_BOOK, ARRAYS), 2, 'ods')


def plain(t):
    """A caption for an attribute (root item 19: no maths in an attribute): $\\mathrm{add}(x)$ as add(x)."""
    return re.sub(r'\$([^$]*)\$', lambda m: re.sub(r'\\math(?:rm|it)\{([^}]*)\}', r'\1', m.group(1)), t)


CAP_QUEUE = plain(CAPTIONS_INTRO['queue']['text'])
CAP_ARRAYQUEUE = plain(CAPTIONS_ARRAYS['arrayqueue']['text'])


# ---------------------------------------------------------------- figures in the text

def sim(fid, caption, original=None, original_caption=None):
    attrs = f'class="sim" id="{fid}"'
    if original:
        attrs += f' data-original="{original}" data-original-caption="{html.escape(original_caption, quote=True)}"'
    return f'<figure {attrs}>\n  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>'


def R(rid, s=None):
    return f'<span data-ref="{rid}"><em>{s or rid}</em></span>'


CAPTION_FIFO = (
    'Values join the queue at one end with add(x) and leave from the other with remove(), so each remove() returns '
    'the value that has waited longest, and the values come out in the order they went in.'
)

CAPTION_ARRAYQUEUE = (
    f'ODS’s ArrayQueue running add(x) and remove() on its backing array {R("a")}, seen both as the ring that modular '
    f'arithmetic makes of it and as the array itself. The {R("n")} elements sit in {R("a")}[{R("j")}], '
    f'{R("a")}[({R("j")} + 1) mod length({R("a")})], …, {R("a")}[({R("j")} + {R("n")} − 1) mod length({R("a")})]: add(x) '
    f'writes at ({R("j")} + {R("n")}) mod length({R("a")}), which runs past the last cell back to cell 0, and remove() '
    f'moves {R("j")} one cell on. When {R("a")} is full, resize() copies {R("a")}[({R("j")} + {R("k")}) mod '
    f'length({R("a")})] into {R("b")}[{R("k")}], so the ring is unrolled into an array of length 2{R("n")} that starts '
    f'at 0, and sets {R("j")} = 0. The resizes follow ArrayStack’s rule, so their copies never pass '
    '<span data-type="cost">2<em>m</em> + 2<em>r</em></span> for <em>m</em> calls and <em>r</em> resizes, as in '
    '<a href="/cs-interview-prep-ultra/ch02/2.2/#arraystack-cost">Section 2.2</a>.'
)

HTML = {
    'sim-fifo-queue': sim('sim-fifo-queue', CAPTION_FIFO, '/media/ch03/ods-queue.png', CAP_QUEUE),
    'sim-arrayqueue': sim('sim-arrayqueue', CAPTION_ARRAYQUEUE, '/media/ch03/ods-arrayqueue.png', CAP_ARRAYQUEUE),
}


# ---------------------------------------------------------------- marks

def _refmath(tex):
    """A passage's maths with the figure's referents a, b, j, k and n marked (a lone letter, not one inside a name
    such as \\mathrm{length})."""
    return re.sub(r'(?<![\\A-Za-z{])([abjkn])(?![A-Za-z}])', lambda m: '\\htmlData{ref=' + m.group(1) + '}{' + m.group(1) + '}', tex)


def _ref(block, before, maths, after='', count=1):
    """A mark of the referents in one maths run, found by the words around it: (block, old, new, count)."""
    return (block, before + maths + after, before + _refmath(maths) + after, count)


FN_24 = '<sup class="fn" data-note="err-theorem-ops"></sup>'
FN_25 = '<sup class="fn" data-note="err-resize-size"></sup>'
B18 = '<a href="/cs-interview-prep-ultra/ch02/2.2/#resize">the $\\mathrm{resize}()$ operation of ArrayStack</a>'

# the arrayqueue block's maths: every a, b, j and n in it is the ArrayQueue's (the theorem's maths names none)
_AQ_MATHS = ['$a[(j+n)\\bmod \\mathrm{length}(a)]$', '$j=(j+1)\\bmod \\mathrm{length}(a)$', '$\\mathrm{length}(a)$',
             '$a[j]$', '$j=0$', '$2n$', '$a$', '$b$', '$j$', '$n$',
             '$$a[j],a[(j+1)\\bmod \\mathrm{length}(a)],\\ldots,a[(j+n-1)\\bmod \\mathrm{length}(a)]$$',
             '$$b[0],b[1],\\ldots,b[n-1]$$']

# (block, text as built, replacement, [count]): concepts, the errata markers, B18's link, then the referents
MARKS = [
    # concepts: the span that introduces each (plan, Concepts)
    ('queue', '<em>FIFO (first-in-first-out) Queue</em>',
     '<span data-concept="queue"><em>FIFO (first-in-first-out) Queue</em></span>'),
    ('circular', 'like a <em>circular array</em>', 'like a <span data-concept="circular-buffer"><em>circular array</em></span>'),
    ('arrayqueue', 'An ArrayQueue implements the (FIFO) Queue interface.',
     '<span data-concept="array-queue">An ArrayQueue implements the (FIFO) Queue interface.</span>'),
    ('linked-queue', 'An SLList can also implement the FIFO queue operations',
     '<span data-concept="queue-linked-list">An SLList can also implement the FIFO queue operations</span>'),
    # errata 24 and 25 (judgements/ch01-03-reconciled.md)
    ('arrayqueue', '$\\mathrm{add}(i,x)$ and $\\mathrm{remove}(i)$ operations',
     '$\\mathrm{add}(i,x)$ and $\\mathrm{remove}(i)$ operations' + FN_24),
    ('arrayqueue', 'of size $2n$ and copies', 'of size $2n$' + FN_25 + ' and copies'),
    # B18: ArrayStack's resize() is Section 2.2's
    ('arrayqueue', 'the $\\mathrm{resize}()$ operation of ArrayStack', B18),
    # referents in the circular block, by the words round each run (its “integer a”, k and m are not the array's)
    _ref('circular', 'an infinite array ', '$a$'),
    _ref('circular', 'one index ', '$j$'),
    _ref('circular', 'an integer ', '$n$', ' that counts'),
    _ref('circular', '', '$$a[j],a[j+1],\\ldots,a[j+n-1] \\enspace .$$'),
    _ref('circular', 'Initially, both ', '$j$', ' and $n$'),
    _ref('circular', 'and ', '$n$', ' would be set'),
    _ref('circular', 'place it in ', '$a[j+n]$', ' and increment $n$'),
    _ref('circular', 'and increment ', '$n$', '. To remove'),
    _ref('circular', 'remove it from ', '$a[j]$', ', increment $j$'),
    _ref('circular', 'increment ', '$j$', ', and decrement'),
    _ref('circular', 'and decrement ', '$n$', '.</p>'),
    _ref('circular', 'a finite array ', '$a$'),
    _ref('circular', 'since ', '$i\\bmod \\mathrm{length}(a)$'),
    _ref('circular', 'the range ', '$0,\\ldots,\\mathrm{length}(a)-1$'),
    _ref('circular', '', '$$a[j\\bmod \\mathrm{length}(a)],a[(j+1)\\bmod \\mathrm{length}(a)],\\ldots,a[(j+n-1)\\bmod '
                         '\\mathrm{length}(a)] \\enspace.$$'),
    _ref('circular', 'the array ', '$a$', ' like a'),
    _ref('circular', 'larger than ', '$\\mathrm{length}(a)-1$'),
    _ref('circular', 'the size of ', '$a$', '.</p>'),
] + [('arrayqueue', t, _refmath(t), 20) for t in _AQ_MATHS]


# ---------------------------------------------------------------- the exercises

EXERCISM = 'sources/_cache/exercism/exercises/circular-buffer'
ICC = 'sources/_cache/icc/stacks_queues/queue_list'


def _exercism_prompt(book):
    """Exercism's description.md, as 1.6 sets an Exercism statement: paragraphs, and its buffer pictures as <pre>."""
    t = open(os.path.join(book, EXERCISM, 'description.md'), encoding='utf-8').read()
    t = re.sub(r'^# Instructions\s*', '', t)
    blocks = []
    for p in re.split(r'\n\s*\n', t.strip()):
        if p.startswith('```'):
            code = re.sub(r'^```\w*\n|\n?```$', '', p)
            blocks.append('<pre>' + html.escape(code, quote=False) + '</pre>')
        else:
            x = html.escape(' '.join(p.split()), quote=False)
            x = re.sub(r'`([^`]+)`', r'<code>\1</code>', x)
            blocks.append(x.replace('$', '&#36;'))
    return '\n\n'.join(blocks)


def _exercism_tests(book):
    """Exercism's canonical cases, each as run(capacity, operations) and the list of what its reads and writes give:
    the value a read returns, null for a write that succeeds, "empty" or "full" where one fails."""
    d = json.load(open(os.path.join(book, EXERCISM, 'canonical-data.json'), encoding='utf-8'))
    out = []
    for c in d['cases']:
        ops, exp = [], []
        for o in c['input']['operations']:
            op = o['operation']
            ops.append([op, o['item']] if 'item' in o else [op])
            if op == 'read':
                exp.append(o['expected'] if o['should_succeed'] else 'empty')
            elif op == 'write':
                exp.append(None if o['should_succeed'] else 'full')
        out.append(([c['input']['capacity'], ops], exp, c['description']))
    return out


# The AI's tests beside the canonical ones (generated_by "ai"): a 0 stored and read back, overwritten and read
# back (Exercism notes that every value is an integer, and its own example cannot store 0), and a buffer driven
# round its ring several times.
CB_AI_TESTS = [
    ([2, [['write', 0], ['read'], ['write', 0], ['write', 1], ['overwrite', 0], ['read'], ['read'], ['read']]],
     [None, 0, None, None, 1, 0, 'empty']),
    ([3, [['write', 1], ['write', 2], ['read'], ['write', 3], ['write', 4], ['read'], ['write', 5], ['read'], ['read'],
          ['write', 6], ['write', 7], ['write', 8], ['read'], ['read'], ['read'], ['read']]],
     [None, None, 1, None, None, 2, None, 3, 4, None, None, 'full', 5, 6, 7, 'empty']),
]

CB_RUN_PY = '''

def run(capacity, operations):
    """Given: plays the tests' operations on a CircularBuffer and returns what each read and write gives:
    the value read, None for a write that succeeds, "empty" or "full" for one that raises."""
    buf, out = CircularBuffer(capacity), []
    for op, *args in operations:
        try:
            if op == 'read':
                out.append(buf.read())
            elif op == 'write':
                buf.write(*args)
                out.append(None)
            elif op == 'overwrite':
                buf.overwrite(*args)
            else:
                buf.clear()
        except BufferEmptyException:
            out.append('empty')
        except BufferFullException:
            out.append('full')
    return out
'''
CB_STARTER_PY = '''class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""


class CircularBuffer:
    def __init__(self, capacity):
        pass

    def read(self):
        pass

    def write(self, data):
        pass

    def overwrite(self, data):
        pass

    def clear(self):
        pass
'''
CB_REF_PY = '''class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""


class CircularBuffer:
    def __init__(self, capacity):
        self.a = [None] * capacity
        self.j = 0          # the oldest element
        self.n = 0          # how many are stored

    def read(self):
        if self.n == 0:
            raise BufferEmptyException("Circular buffer is empty")
        x = self.a[self.j]
        self.a[self.j] = None
        self.j = (self.j + 1) % len(self.a)
        self.n -= 1
        return x

    def write(self, data):
        if self.n == len(self.a):
            raise BufferFullException("Circular buffer is full")
        self.a[(self.j + self.n) % len(self.a)] = data
        self.n += 1

    def overwrite(self, data):
        if self.n == len(self.a):
            self.read()
        self.write(data)

    def clear(self):
        self.a = [None] * len(self.a)
        self.j = 0
        self.n = 0
'''
CB_RUN_JS = '''

// Given: plays the tests' operations on a CircularBuffer and returns what each read and write gives:
// the value read, null for a write that succeeds, "empty" or "full" for one that throws.
function run(capacity, operations) {
    const buf = new CircularBuffer(capacity), out = [];
    for (const [op, ...args] of operations) {
        try {
            if (op === 'read') out.push(buf.read());
            else if (op === 'write') { buf.write(...args); out.push(null); }
            else if (op === 'overwrite') buf.forceWrite(...args);
            else buf.clear();
        } catch (e) {
            if (e instanceof BufferEmptyError) out.push('empty');
            else if (e instanceof BufferFullError) out.push('full');
            else throw e;
        }
    }
    return out;
}
'''
CB_STARTER_JS = '''class BufferFullError extends Error {}

class BufferEmptyError extends Error {}

class CircularBuffer {
    constructor(capacity) {
    }

    read() {
    }

    write(data) {
    }

    forceWrite(data) {
    }

    clear() {
    }
}
'''
CB_REF_JS = '''class BufferFullError extends Error {}

class BufferEmptyError extends Error {}

class CircularBuffer {
    constructor(capacity) {
        this.a = new Array(capacity).fill(null);
        this.j = 0;         // the oldest element
        this.n = 0;         // how many are stored
    }

    read() {
        if (this.n === 0) throw new BufferEmptyError('Circular buffer is empty');
        const x = this.a[this.j];
        this.a[this.j] = null;
        this.j = (this.j + 1) % this.a.length;
        this.n -= 1;
        return x;
    }

    write(data) {
        if (this.n === this.a.length) throw new BufferFullError('Circular buffer is full');
        this.a[(this.j + this.n) % this.a.length] = data;
        this.n += 1;
    }

    forceWrite(data) {
        if (this.n === this.a.length) this.read();
        this.write(data);
    }

    clear() {
        this.a.fill(null);
        this.j = 0;
        this.n = 0;
    }
}
'''

QL_RUN_PY = '''

def run(ops):
    """Given: plays the tests' operations on a Queue and returns what each dequeue gives."""
    queue, out = Queue(), []
    for op, *args in ops:
        if op == 'enqueue':
            queue.enqueue(*args)
        else:
            out.append(queue.dequeue())
    return out
'''
QL_RUN_JS = '''

// Given: plays the tests' operations on a Queue and returns what each dequeue gives.
function run(ops) {
    const queue = new Queue(), out = [];
    for (const [op, ...args] of ops) {
        if (op === 'enqueue') queue.enqueue(...args);
        else out.push(queue.dequeue());
    }
    return out;
}
'''
QL_STARTER_JS = '''class Node {
    constructor(data) {
        // TODO: Implement me
    }
}

class Queue {
    constructor() {
        // TODO: Implement me
    }

    enqueue(data) {
        // TODO: Implement me
    }

    dequeue() {
        // TODO: Implement me
    }
}
'''
QL_REF_JS = '''class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class Queue {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    enqueue(data) {
        const node = new Node(data);
        // Empty list
        if (this.head === null && this.tail === null) {
            this.head = node;
            this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
    }

    dequeue() {
        // Empty list
        if (this.head === null && this.tail === null) return null;
        const data = this.head.data;
        // Remove only element from a one element list
        if (this.head === this.tail) {
            this.head = null;
            this.tail = null;
        } else {
            this.head = this.head.next;
        }
        return data;
    }
}
'''
# icc's test_queue_list.py has one test method, test_end_to_end; its asserts are the dequeues of one operation list
QL_SOURCE_TEST = ([[['dequeue'], ['enqueue', 1], ['dequeue'], ['enqueue', 2], ['enqueue', 3], ['enqueue', 4],
                    ['dequeue'], ['dequeue'], ['dequeue']]], [None, 1, 2, 3, 4])
# The AI's tests: a queue of several elements drained to empty and used again (the tail must be reset with the
# head), and enqueues and dequeues interleaved.
QL_AI_TESTS = [
    ([[['enqueue', 'a'], ['enqueue', 'b'], ['dequeue'], ['dequeue'], ['dequeue'], ['enqueue', 'c'], ['enqueue', 'd'],
       ['dequeue'], ['dequeue'], ['dequeue']]], ['a', 'b', None, 'c', 'd', None]),
    ([[['enqueue', 1], ['enqueue', 2], ['dequeue'], ['enqueue', 3], ['dequeue'], ['enqueue', 4], ['enqueue', 5],
       ['dequeue'], ['dequeue'], ['enqueue', 6], ['dequeue'], ['dequeue'], ['dequeue']]], [1, 2, 3, 4, 5, 6, None]),
]


def _icc_prompt(book):
    nb = json.load(open(os.path.join(book, ICC, 'queue_list_challenge.ipynb'), encoding='utf-8'))
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
    return html.escape(problem, quote=False) + '\n\nConstraints:\n\n' + '\n'.join(
        html.escape(f'- {q} {a}', quote=False) for q, a in qa)


def _icc_starter_py(book):
    nb = json.load(open(os.path.join(book, ICC, 'queue_list_challenge.ipynb'), encoding='utf-8'))
    code = next(''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'code' and 'class Queue' in ''.join(c['source']))
    return code.rstrip() + '\n'


def EXERCISES(exercism_code, book):
    cb_tests = [{'args': args, 'expect': exp, 'visible': i < 2, 'generated_by': 'source'}
                for i, (args, exp, _) in enumerate(_exercism_tests(book))]
    cb_tests += [{'args': args, 'expect': exp, 'visible': False, 'generated_by': 'ai'} for args, exp in CB_AI_TESTS]
    c1 = {
        'id': 'c1', 'source_id': 'exercism:circular-buffer', 'source_number': 'circular-buffer', 'origin': 'exercism',
        'kind': 'code', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'circular',
        'changes': ('The tests are Exercism’s canonical cases, each a list of operations that a given run(capacity, '
                    'operations) plays on your CircularBuffer, with two more that store 0 and go round the buffer '
                    'several times; a failed read or write is reported as “empty” or “full”.'),
        'prompt': _exercism_prompt(book),
        'answer': {
            'type': 'code',
            'python': {'entry': 'run', 'starter': CB_STARTER_PY + CB_RUN_PY, 'reference': CB_REF_PY + CB_RUN_PY, 'generated_by': 'ai'},
            'javascript': {'entry': 'run', 'starter': CB_STARTER_JS + CB_RUN_JS, 'reference': CB_REF_JS + CB_RUN_JS, 'generated_by': 'ai'},
            'tests': cb_tests, 'generated_by': 'source'},
    }
    ref_py = open(os.path.join(book, ICC, 'queue_list.py'), encoding='utf-8').read().rstrip() + '\n'
    ql_tests = [{'args': QL_SOURCE_TEST[0], 'expect': QL_SOURCE_TEST[1], 'visible': True, 'generated_by': 'source'}]
    ql_tests += [{'args': args, 'expect': exp, 'visible': False, 'generated_by': 'ai'} for args, exp in QL_AI_TESTS]
    c2 = {
        'id': 'c2', 'source_id': 'icc:stacks_queues/queue_list', 'source_number': 'queue_list', 'origin': 'icc',
        'kind': 'code', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'linked-queue',
        'changes': ('The source’s one unit test is a list of operations that a given run(ops) plays on your Queue, with '
                    'two more that empty the queue and use it again and that mix enqueues and dequeues.'),
        'prompt': _icc_prompt(book),
        'answer': {
            'type': 'code',
            'python': {'entry': 'run', 'starter': _icc_starter_py(book) + QL_RUN_PY, 'reference': ref_py + QL_RUN_PY, 'generated_by': 'source'},
            'javascript': {'entry': 'run', 'starter': QL_STARTER_JS + QL_RUN_JS, 'reference': QL_REF_JS + QL_RUN_JS, 'generated_by': 'ai'},
            'tests': ql_tests, 'generated_by': 'source'},
    }
    concepts = [{'exercise': 'c1', 'concept': 'circular-buffer'}, {'exercise': 'c1', 'concept': 'queue'},
                {'exercise': 'c2', 'concept': 'queue-linked-list'}, {'exercise': 'c2', 'concept': 'queue'}]
    return [c1, c2], concepts


# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]

LEAD = ('An Essential section on the <span data-concept="queue">FIFO queue</span> and two ways to build it. Arrays are '
        'indexed from 0. ODS’s ArrayQueue grows and shrinks its circular array as '
        '<a href="/cs-interview-prep-ultra/ch02/2.2/">Section 2.2</a>’s ArrayStack does; the '
        '<span data-concept="circular-buffer">circular buffer</span> of the exercises is the fixed-size kind, which '
        'overwrites its oldest element. The linked queue is <a href="/cs-interview-prep-ultra/ch02/2.6/">Section 2.6</a>’s '
        'SLList, whose pop() removes the head node as <a href="/cs-interview-prep-ultra/ch03/3.1/">Section 3.1</a>’s linked '
        'stack does; the Deque it nearly implements is <a href="/cs-interview-prep-ultra/ch03/3.3/">Section 3.3</a>’s.')

SECTION = {
    'id': '3.2', 'chapter': '3', 'title': 'Queues and circular buffers', 'short': 'Queues',
    'lead': LEAD,
    'objectives': [], 'summary_html': '',
    'notes': ('ODS’s paragraphs on priority queues, stacks and deques, which chapter 9 and Sections 3.1 and 3.3 carry, and '
              'the opening and summary of its SLList section are left out here.'),
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'Exercism’s circular-buffer and Interactive Coding Challenges’ queue_list are the code exercises. Exercism’s own '
        'example cannot store 0, so both circular-buffer references are the AI’s, as are the queue’s JavaScript reference '
        'and the tests added to each. OpenDSA’s keyed queue questions (StackQMCQ) wait for the converter of OpenDSA’s '
        'exercises, and its four enqueue and dequeue exercises and the Wikibooks A-level queue traces for an answer type '
        'that takes a sequence; the one Wikibooks question on priority queues is held for chapter 9. Kattis’s ferryloading4 '
        'has only a sample, ODS’s ArrayQueue harness has no printed statement, ODS Exercise 2.3 (RandomQueue) and SICP '
        'Exercises 3.21 and 3.22 have no tests of their own, and the pythonds queue exercises have no published answers, so '
        'they are left out; the TheAlgorithms, keon and trekhleb queue files are tests with no printed statement. Interactive '
        'Coding Challenges’ queue_from_stacks is left out because its queue takes quadratic time on alternating operations. '
        'ODS Exercise 2.8, which replaces the mod operator with bit operations, is held for chapter 7, and MIT 6.006’s '
        'problem 1-4 is with Section 2.6.'),
    'figures': [
        {'id': 'sim-fifo-queue', 'kind': 'sim', 'originals': ['/media/ch03/ods-queue.png'],
         'original_caption': CAP_QUEUE, 'draws': ['key'], 'ai': FIG_AI},
        {'id': 'sim-arrayqueue', 'kind': 'sim', 'originals': ['/media/ch03/ods-arrayqueue.png'],
         'original_caption': CAP_ARRAYQUEUE, 'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'a', 'label': 'a, the backing array', 'figures': ['sim-arrayqueue']},
        {'id': 'b', 'label': 'b, the array resize() fills', 'figures': ['sim-arrayqueue']},
        {'id': 'j', 'label': 'j, the index of the next element to remove', 'figures': ['sim-arrayqueue']},
        {'id': 'n', 'label': 'n, the number of elements in the queue', 'figures': ['sim-arrayqueue']},
        {'id': 'k', 'label': 'k, the element resize() is copying', 'figures': ['sim-arrayqueue']},
    ],
    'coverage': [
        {'span': 'queue', 'concept': 'queue', 'verb': 'introduces'},
        {'span': 'queue', 'concept': 'interface-vs-implementation', 'verb': 'uses'},
        {'span': 'circular', 'concept': 'circular-buffer', 'verb': 'introduces'},
        {'span': 'circular', 'concept': 'queue', 'verb': 'uses'},
        {'span': 'circular', 'concept': 'dynamic-array', 'verb': 'uses'},
        {'span': 'arrayqueue', 'concept': 'array-queue', 'verb': 'introduces'},
        {'span': 'arrayqueue', 'concept': 'circular-buffer', 'verb': 'uses'},
        {'span': 'arrayqueue', 'concept': 'array-resize', 'verb': 'uses'},
        {'span': 'arrayqueue', 'concept': 'dynamic-array-cost', 'verb': 'uses'},
        {'span': 'linked-queue', 'concept': 'queue-linked-list', 'verb': 'introduces'},
        {'span': 'linked-queue', 'concept': 'singly-linked-list', 'verb': 'uses'},
        {'span': 'linked-queue', 'concept': 'queue', 'verb': 'uses'},
    ],
    'footnotes_extra': [
        {'id': 'err-theorem-ops', 'kind': 'correction',
         'html': 'A Queue’s operations are $\\mathrm{add}(x)$ and $\\mathrm{remove}()$; $\\mathrm{add}(i,x)$ and '
                 '$\\mathrm{remove}(i)$ are the List operations of ArrayStack’s theorem. The bound holds for any sequence '
                 'of $m$ calls to $\\mathrm{add}(x)$ and $\\mathrm{remove}()$.'},
        {'id': 'err-resize-size', 'kind': 'correction',
         'html': 'The code allocates an array of size $\\max(1, 2n)$, so that a queue emptied by $\\mathrm{remove}()$ '
                 'keeps an array of length 1 to add into.'},
        {'id': 'err-caption-ops', 'kind': 'correction', 'figure': 'sim-arrayqueue',
         'html': 'The calls drawn are $\\mathrm{add}(x)$ and $\\mathrm{remove}()$, the Queue’s operations; '
                 '$\\mathrm{remove}(i)$ is a List operation.'},
    ],
    'derivations': [],
}
