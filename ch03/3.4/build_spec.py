"""3.4 Min-stacks and monotonic queues: the spec ch03/3.4/build.py reads (placement, marks, code-set translations)
and tools/build_section.py reads (the section record and the exercises).

Sources: cp-algorithms data_structures/stack_queue_modification and dynamic_programming/zero_matrix at d55d3f5
(C++ only), Wikipedia "All nearest smaller values" at revision 1377501815. No source text is typed here: the
blocks are cut from the cache by heading, the C++ is the page's own, and what is written here is OmniStax's
(placement, the Python, Java and JavaScript translations of the code sets, the correction notes, the lead, the
captions and the exercise harnesses). There is no replacement table: nothing in the sources' words is changed.
"""
TITLE = 'Min-stacks and monotonic queues'
SQM = 'sources/_cache/cpa/src/data_structures/stack_queue_modification.md'
ZM = 'sources/_cache/cpa/src/dynamic_programming/zero_matrix.md'
LOC = 'cpa:data_structures/stack_queue_modification'
AI = 'claude-opus-5-5 high'
SEC = '/cs-interview-prep-ultra'

BLOCKS = [
    dict(id='min-stack', source='cpa', file=SQM, locator=f'{LOC}, its opening and #stack-modification',
         **{'from': '# Minimum stack / Minimum queue', 'to': '## Queue modification (method 1)'}),
    dict(id='min-queue', source='cpa', file=SQM, locator=f'{LOC}#queue-modification-method-1',
         **{'from': '## Queue modification (method 1)', 'to': '## Queue modification (method 2)'}),
    dict(id='min-queue-index', source='cpa', file=SQM, locator=f'{LOC}#queue-modification-method-2',
         **{'from': '## Queue modification (method 2)', 'to': '## Queue modification (method 3)'}),
    dict(id='two-stack-queue', source='cpa', file=SQM, locator=f'{LOC}#queue-modification-method-3',
         **{'from': '## Queue modification (method 3)', 'to': '## Finding the minimum for all subarrays of fixed length'}),
    dict(id='window-minimum', source='cpa', file=SQM, locator=f'{LOC}#finding-the-minimum-for-all-subarrays-of-fixed-length',
         **{'from': '## Finding the minimum for all subarrays of fixed length', 'to': '## Practice Problems'}),
    dict(id='nearest-smaller', source='wikipedia', file='All_nearest_smaller_values.wiki', h2='All nearest smaller values',
         locator='wikipedia:All_nearest_smaller_values lead, #Example, #Sequential algorithm',
         parts=[('lead', None), ('section', 'Example'), ('section', 'Sequential algorithm')]),
    dict(id='zero-submatrix', source='cpa', file=ZM, locator='cpa:dynamic_programming/zero_matrix',
         **{'from': '# Finding the largest zero submatrix', 'to': None}),
]


def ref(rid, word):
    return f'<span data-ref="{rid}">{word}</span>'


def sim(fid, caption):
    return (f'<figure class="sim" id="{fid}">\n'
            f'  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>')


C = lambda s: f'<code>{s}</code>'  # noqa: E731
HTML = {
    'sim-min-stack': sim(
        'sim-min-stack',
        f'Each entry of {ref("st", C("st"))} holds an element and the smallest element from there down, so the minimum is always '
        f'the top entry’s second value. Adding {ref("new-elem", C("new_elem"))} takes one comparison with the top; removing takes '
        f'none, and the minimum below shows again. With a repeated minimum, the copy below keeps it after the top one goes.'),
    'sim-min-queue': sim(
        'sim-min-queue',
        f'A window of length <em>M</em> slides along <em>A</em>, as in the last part of this article: each step adds the next '
        f'element, removes the oldest by its value and reads the minimum at the front of {ref("q", C("q"))}. Before '
        f'{ref("new-element", C("new_element"))} goes in at the back, every larger element there is cut, since it leaves the '
        f'window first and can never be its minimum. On increasing input nothing is cut; on decreasing input each element '
        f'cuts all the others. Each element is added and removed at most once.'),
    'sim-two-stack-queue': sim(
        'sim-two-stack-queue',
        f'New elements go onto {ref("s1", C("s1"))} and leave from {ref("s2", C("s2"))}. Only when {ref("s2", C("s2"))} is '
        f'empty does all of {ref("s1", C("s1"))} move across, reversed, so the oldest element ends on top. The minimum is the '
        f'smaller of the two tops’ second values. In bursts, one transfer moves many elements; alternating, each transfer '
        f'moves one. Either way each element is added once, moved once and removed once.'),
    'sim-nearest-smaller': sim(
        'sim-nearest-smaller',
        f'For each {ref("x", C("x"))}, the stack {ref("S", C("S"))} first loses every top value at least as large as '
        f'{ref("x", C("x"))}; whatever is left on top is the nearest smaller value, and then {ref("x", C("x"))} goes on. '
        f'{ref("S", C("S"))} always increases from bottom to top. On increasing input nothing is popped; on decreasing '
        f'input no value has a smaller one before it, and each pops the last. A value is popped at most once, so there are '
        f'never more pops than values.'),
}

# A fenced snippet: (block, a piece of its text, a Sim whose panel carries it | the other languages of its code set)
CODE = [
    ('min-stack', 'stack<pair<int, int>> st;', 'sim-min-stack'),
    ('min-stack', 'int new_min', 'sim-min-stack'),
    ('min-stack', 'int removed_element', 'sim-min-stack'),
    ('min-stack', 'int minimum = st.top().second;', 'sim-min-stack'),
    ('min-queue', 'deque<int> q;', 'sim-min-queue'),
    ('min-queue', 'int minimum = q.front();', 'sim-min-queue'),
    ('min-queue', 'q.push_back(new_element);', 'sim-min-queue'),
    ('min-queue', 'q.pop_front();', 'sim-min-queue'),
    ('min-queue-index', 'deque<pair<int, int>> q;', {
        'python': 'from collections import deque\n\nq = deque()\ncnt_added = 0\ncnt_removed = 0',
        'java': 'Deque<int[]> q = new ArrayDeque<>();\nint cnt_added = 0;\nint cnt_removed = 0;',
        'javascript': 'const q = [];\nlet cnt_added = 0;\nlet cnt_removed = 0;'}),
    ('min-queue-index', 'int minimum = q.front().first;', {
        'python': 'minimum = q[0][0]',
        'java': 'int minimum = q.peekFirst()[0];',
        'javascript': 'const minimum = q[0][0];'}),
    ('min-queue-index', 'q.push_back({new_element, cnt_added});', {
        'python': 'while q and q[-1][0] > new_element:\n    q.pop()\nq.append((new_element, cnt_added))\ncnt_added += 1',
        'java': ('while (!q.isEmpty() && q.peekLast()[0] > new_element)\n    q.pollLast();\n'
                 'q.addLast(new int[]{new_element, cnt_added});\ncnt_added++;'),
        'javascript': ('while (q.length > 0 && q[q.length - 1][0] > new_element)\n    q.pop();\n'
                       'q.push([new_element, cnt_added]);\ncnt_added++;')}),
    ('min-queue-index', 'cnt_removed++;', {
        'python': 'if q and q[0][1] == cnt_removed:\n    q.popleft()\ncnt_removed += 1',
        'java': 'if (!q.isEmpty() && q.peekFirst()[1] == cnt_removed)\n    q.pollFirst();\ncnt_removed++;',
        'javascript': 'if (q.length > 0 && q[0][1] === cnt_removed)\n    q.shift();\ncnt_removed++;'}),
    ('two-stack-queue', 'stack<pair<int, int>> s1, s2;', 'sim-two-stack-queue'),
    ('two-stack-queue', 'minimum = min(s1.top().second, s2.top().second);', 'sim-two-stack-queue'),
    ('two-stack-queue', 's1.push({new_element, minimum});', 'sim-two-stack-queue'),
    ('two-stack-queue', 'int remove_element = s2.top().first;', 'sim-two-stack-queue'),
    ('zero-submatrix', 'vector<int> d(m, -1);', {
        'python': 'd = [-1] * m\nfor i in range(n):\n    for j in range(m):\n        if a[i][j] == 1:\n            d[j] = i',
        'java': ('int[] d = new int[m];\nArrays.fill(d, -1);\nfor (int i = 0; i < n; ++i) {\n    for (int j = 0; j < m; ++j) {\n'
                 '        if (a[i][j] == 1) {\n            d[j] = i;\n        }\n    }\n}'),
        'javascript': ('const d = new Array(m).fill(-1);\nfor (let i = 0; i < n; ++i) {\n    for (let j = 0; j < m; ++j) {\n'
                       '        if (a[i][j] === 1) {\n            d[j] = i;\n        }\n    }\n}')}),
]
ZERO_PY = '''def zero_matrix(a):
    n = len(a)
    m = len(a[0])

    ans = 0
    d, d1, d2 = [-1] * m, [0] * m, [0] * m
    st = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                d[j] = i

        for j in range(m):
            while st and d[st[-1]] <= d[j]:
                st.pop()
            d1[j] = -1 if not st else st[-1]
            st.append(j)
        while st:
            st.pop()

        for j in range(m - 1, -1, -1):
            while st and d[st[-1]] <= d[j]:
                st.pop()
            d2[j] = m if not st else st[-1]
            st.append(j)
        while st:
            st.pop()

        for j in range(m):
            ans = max(ans, (i - d[j]) * (d2[j] - d1[j] - 1))
    return ans
'''
ZERO_JAVA = '''int zero_matrix(int[][] a) {
    int n = a.length;
    int m = a[0].length;

    int ans = 0;
    int[] d = new int[m], d1 = new int[m], d2 = new int[m];
    Arrays.fill(d, -1);
    Deque<Integer> st = new ArrayDeque<>();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] == 1)
                d[j] = i;
        }

        for (int j = 0; j < m; ++j) {
            while (!st.isEmpty() && d[st.peek()] <= d[j])
                st.pop();
            d1[j] = st.isEmpty() ? -1 : st.peek();
            st.push(j);
        }
        while (!st.isEmpty())
            st.pop();

        for (int j = m - 1; j >= 0; --j) {
            while (!st.isEmpty() && d[st.peek()] <= d[j])
                st.pop();
            d2[j] = st.isEmpty() ? m : st.peek();
            st.push(j);
        }
        while (!st.isEmpty())
            st.pop();

        for (int j = 0; j < m; ++j)
            ans = Math.max(ans, (i - d[j]) * (d2[j] - d1[j] - 1));
    }
    return ans;
}
'''
ZERO_JS = '''function zero_matrix(a) {
    const n = a.length;
    const m = a[0].length;

    let ans = 0;
    const d = new Array(m).fill(-1), d1 = new Array(m), d2 = new Array(m);
    const st = [];
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < m; ++j) {
            if (a[i][j] === 1)
                d[j] = i;
        }

        for (let j = 0; j < m; ++j) {
            while (st.length > 0 && d[st[st.length - 1]] <= d[j])
                st.pop();
            d1[j] = st.length === 0 ? -1 : st[st.length - 1];
            st.push(j);
        }
        while (st.length > 0)
            st.pop();

        for (let j = m - 1; j >= 0; --j) {
            while (st.length > 0 && d[st[st.length - 1]] <= d[j])
                st.pop();
            d2[j] = st.length === 0 ? m : st[st.length - 1];
            st.push(j);
        }
        while (st.length > 0)
            st.pop();

        for (let j = 0; j < m; ++j)
            ans = Math.max(ans, (i - d[j]) * (d2[j] - d1[j] - 1));
    }
    return ans;
}
'''
CODE.append(('zero-submatrix', 'int zero_matrix(', {'python': ZERO_PY, 'java': ZERO_JAVA, 'javascript': ZERO_JS}))

DROP = [
    ('min-stack', 'Adding an element:'), ('min-stack', 'Removing an element:'), ('min-stack', 'Finding the minimum:'),
    ('min-queue', 'Finding the minimum:'), ('min-queue', 'Adding an element:'), ('min-queue', 'Removing an element:'),
    ('two-stack-queue', 'Finding the minimum:'), ('two-stack-queue', 'Add element:'), ('two-stack-queue', 'Removing an element:'),
]
AT = [
    ('min-stack', 'Implementation:', 'sim-min-stack'),
    ('min-queue', 'Consider the implementations of the above operations:', 'sim-min-queue'),
    ('two-stack-queue', 'Implementation:', 'sim-two-stack-queue'),
    ('nearest-smaller', 'push x onto S', 'sim-nearest-smaller'),
]

FN = lambda i: f'<sup class="fn" data-note="{i}"></sup>'  # noqa: E731
LINK31 = f'{SEC}/ch03/3.1/'
MARKS = [
    # concepts named where their passage states them (the introducing spans are the blocks, in coverage)
    ('min-stack', 'we will store them in pairs: the element itself and the minimum in the stack starting from this element and below.',
     '<span data-concept="min-stack">we will store them in pairs: the element itself and the minimum in the stack starting from this '
     'element and below.</span>'),
    ('min-stack', 'in the whole stack', 'in <span data-ref="st">the whole stack</span>'),
    ('min-queue', 'The key idea is to only store the items in the queue that are needed to determine the minimum.',
     '<span data-concept="monotonic-queue-minimum">The key idea is to only store the items in the queue that are needed to '
     'determine the minimum.</span>'),
    ('min-queue', 'we will keep the queue in nondecreasing order', 'we will keep <span data-ref="q">the queue</span> in nondecreasing order'),
    ('two-stack-queue', 'So we only need to learn how to simulate a queue using two stacks.',
     '<span data-concept="queue-from-two-stacks">So we only need to learn how to simulate a queue using two stacks.</span>'),
    ('two-stack-queue', '<code>s1</code>', '<span data-ref="s1"><code>s1</code></span>', 4),
    ('two-stack-queue', '<code>s2</code>', '<span data-ref="s2"><code>s2</code></span>', 6),
    ('two-stack-queue', 'involves just finding the minimum of both stacks.',
     f'involves just finding the minimum of both stacks.{FN("err-empty-min")}'),
    ('window-minimum', 'We can use any of the three modified queues to solve the problem.',
     '<span data-concept="sliding-window-minimum">We can use any of the three modified queues to solve the problem.</span>'),
    ('nearest-smaller', '<strong>all nearest smaller values</strong>',
     '<strong><span data-concept="nearest-smaller-element">all nearest smaller values</span></strong>'),
    ('nearest-smaller', 'stack-based algorithm', f'<a href="{LINK31}">stack</a>-based algorithm'),
    ('nearest-smaller', 'by using a stack data structure', f'by using a <a href="{LINK31}">stack data structure</a>'),
    ('nearest-smaller', 'using the stack to maintain', '<span data-ref="S">using the stack</span> to maintain'),
    ('zero-submatrix', 'Find the largest submatrix consisting of only zeros (a submatrix is a rectangular area of the matrix).',
     '<span data-concept="largest-zero-submatrix">Find the largest submatrix consisting of only zeros (a submatrix is a '
     'rectangular area of the matrix).</span>'),
    ('zero-submatrix', 'in the <code>j</code>-th column.', f'in the <code>j</code>-th column.{FN("err-d-row")}'),
    ('zero-submatrix', '<code>i = 1...m - 1</code>', f'<code>i = 1...m - 1</code>{FN("err-d-index")}'),
]

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]
LEAD = ('An Essential section on a stack and a queue that report their smallest element in constant time, on using such a queue '
        'to find the minimum of every window of fixed length, and on finding each element’s nearest smaller value with a stack. '
        'The largest all-zero submatrix is Advanced. cp-algorithms counts from 0 (A[0] to A[N − 1], rows 0 to n − 1); '
        'Wikipedia’s A[1..n] counts from 1, with a sentinel A[0].')

EXERCISE_NOTES = (
    'ODS’s Exercises 3.15 (MinQueue) and 3.16 (MinDeque) ask for a design in words and have no tests, so they are not set. '
    'TheAlgorithms’ queue_by_two_stacks, monotonic_queue, sliding_window_maximum, stock_span_problem, next_greater_element and '
    'largest_rectangle_histogram, tryalgo’s our_queue and keon’s max_sliding_window carry tests but print no exercise statement, so '
    'they have no card. Interactive Coding Challenges’ stack_min and queue_from_stacks are left out: the first loses a repeated '
    'minimum and the second moves every element back on each enqueue, which is quadratic. Kattis’s bungeebuilder is left for a '
    'later pass, and keon’s heap version of the window waits for the heaps of chapter 9. MIT 6.046J’s “Extreme FIFO Queues”, '
    'which chapter 1’s plan had placed in 1.5, is set here with the NC cards.')

SECTION = {
    'id': '3.4', 'chapter': '3', 'title': TITLE, 'short': 'Min-stacks and monotonic queues',
    'lead': LEAD, 'objectives': [], 'summary_html': '',
    'notes': ('cp-algorithms’ lists of practice problems are left out, and so are the parts of Wikipedia’s article on applications and '
              'on parallel algorithms.'),
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'built': '2026-11-09',
    'exercise_notes': EXERCISE_NOTES,
    'figures': [
        {'id': 'sim-min-stack', 'kind': 'sim', 'draws': ['key', 'cost'], 'ai': FIG_AI},
        {'id': 'sim-min-queue', 'kind': 'sim', 'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
        {'id': 'sim-two-stack-queue', 'kind': 'sim', 'draws': ['key', 'cost'], 'ai': FIG_AI},
        {'id': 'sim-nearest-smaller', 'kind': 'sim', 'draws': ['index', 'key', 'cost'], 'ai': FIG_AI},
    ],
    'coverage': [
        {'span': 'min-stack', 'concept': 'min-stack', 'verb': 'introduces'},
        {'span': 'min-queue', 'concept': 'monotonic-queue-minimum', 'verb': 'introduces'},
        {'span': 'min-queue-index', 'concept': 'monotonic-queue-minimum', 'verb': 'reinforces'},
        {'span': 'two-stack-queue', 'concept': 'queue-from-two-stacks', 'verb': 'introduces'},
        {'span': 'two-stack-queue', 'concept': 'min-stack', 'verb': 'uses'},
        {'span': 'window-minimum', 'concept': 'sliding-window-minimum', 'verb': 'introduces'},
        {'span': 'window-minimum', 'concept': 'monotonic-queue-minimum', 'verb': 'uses'},
        {'span': 'window-minimum', 'concept': 'sliding-window-fixed', 'verb': 'uses'},
        {'span': 'nearest-smaller', 'concept': 'nearest-smaller-element', 'verb': 'introduces'},
        {'span': 'zero-submatrix', 'concept': 'largest-zero-submatrix', 'verb': 'introduces'},
        {'span': 'zero-submatrix', 'concept': 'nearest-smaller-element', 'verb': 'uses'},
    ],
    'referents': [
        {'id': 'st', 'label': 'st, the stack of pairs', 'figures': ['sim-min-stack']},
        {'id': 'new-elem', 'label': 'new_elem, the element being added', 'figures': ['sim-min-stack']},
        {'id': 'q', 'label': 'q, the deque of method 1', 'figures': ['sim-min-queue']},
        {'id': 'new-element', 'label': 'new_element, the element being added', 'figures': ['sim-min-queue', 'sim-two-stack-queue']},
        {'id': 's1', 'label': 's1, the stack new elements go onto', 'figures': ['sim-two-stack-queue']},
        {'id': 's2', 'label': 's2, the stack elements leave from', 'figures': ['sim-two-stack-queue']},
        {'id': 'S', 'label': 'S, the stack of values', 'figures': ['sim-nearest-smaller']},
        {'id': 'x', 'label': 'x, the value being processed', 'figures': ['sim-nearest-smaller']},
    ],
    'footnotes_extra': [
        {'id': 'err-empty-min', 'kind': 'correction',
         'html': ('When both stacks are empty, the code for the minimum takes its first branch and reads <code>s2.top()</code>, the '
                  'top of an empty stack, which C++ leaves undefined. An empty queue has no minimum, so it can be asked for only '
                  'while the queue holds an element.')},
        {'id': 'err-d-row', 'kind': 'correction',
         'html': ('The code below sets <code>d[j] = i</code> for each 1 in row $i$ before the row is used, so $d[i][j]$ is the '
                  'largest row number from $0$ to $i$, row $i$ itself included, not to $i - 1$. Including row $i$ is what gives a cell '
                  'that holds a 1 the height $i - d[i][j] = 0$, so that no zero submatrix ends on it.')},
        {'id': 'err-d-index', 'kind': 'correction',
         'html': ('The array is indexed by the column: $d[j]$ for $j = 0, \\ldots, m - 1$, as the code’s '
                  '<code>vector&lt;int&gt; d(m, -1)</code> declares it.')},
    ],
    'derivations': [],
}

# ---------------------------------------------------------------- the code exercises
MINSTACK_PY = '''class MinStack:
    def __init__(self):
        self.st = []

    def push(self, x):
        new_min = x if not self.st else min(x, self.st[-1][1])
        self.st.append((x, new_min))

    def pop(self):
        return self.st.pop()[0]

    def size(self):
        return len(self.st)

    def min(self):
        return self.st[-1][1]
'''
MINSTACK_PY_START = '''class MinStack:
    def __init__(self):
        pass

    def push(self, x):
        pass

    def pop(self):
        pass

    def size(self):
        pass

    def min(self):
        pass
'''
RUN_PY = '''

def run(ops):
    # Plays the operations on a new MinStack and returns what pop, size and min return, in order. Leave it as it is.
    s = MinStack()
    out = []
    for name, *args in ops:
        r = getattr(s, name)(*args)
        if name != "push":
            out.append(r)
    return out
'''
MINSTACK_JS = '''class MinStack {
  constructor() {
    this.st = [];
  }

  push(x) {
    const newMin = this.st.length === 0 ? x : Math.min(x, this.st[this.st.length - 1][1]);
    this.st.push([x, newMin]);
  }

  pop() {
    return this.st.pop()[0];
  }

  size() {
    return this.st.length;
  }

  min() {
    return this.st[this.st.length - 1][1];
  }
}
'''
MINSTACK_JS_START = '''class MinStack {
  constructor() {
  }

  push(x) {
  }

  pop() {
  }

  size() {
  }

  min() {
  }
}
'''
RUN_JS = '''
// Plays the operations on a new MinStack and returns what pop, size and min return, in order. Leave it as it is.
function run(ops) {
  const s = new MinStack();
  const out = [];
  for (const [name, ...args] of ops) {
    const r = s[name](...args);
    if (name !== "push") out.push(r);
  }
  return out;
}
'''
ZERO_START_PY = 'def zero_matrix(a):\n    pass\n'
ZERO_START_JS = 'function zero_matrix(a) {\n}\n'


def _play(ops):
    st, out = [], []
    for name, *args in ops:
        if name == 'push':
            st.append(args[0])
        elif name == 'pop':
            out.append(st.pop())
        elif name == 'size':
            out.append(len(st))
        else:
            out.append(min(st))
    return out


def _brute_zero(a):
    n, m, best = len(a), len(a[0]), 0
    for t in range(n):
        for b in range(t, n):
            for l in range(m):
                for r in range(l, m):
                    if all(a[i][j] == 0 for i in range(t, b + 1) for j in range(l, r + 1)):
                        best = max(best, (b - t + 1) * (r - l + 1))
    return best


def ods_statement(book):
    """ODS Exercise 3.14 as linkedlists.tex prints it, its #code# set as code (the pseudocode edition's rule for a call)."""
    import html
    import os
    import re
    tex = open(os.path.join(book, 'sources/_cache/ods/latex/linkedlists.tex'), encoding='utf-8').read()
    a = tex.index('\\index{MinStack@#MinStack#}%')
    body = tex[a:tex.index('\\end{exc}', a)].split('\n', 1)[1]
    body = ' '.join(body.split())
    return re.sub(r'#([^#]+)#', lambda m: '<code>' + html.escape(m.group(1), quote=False) + '</code>', html.escape(body, quote=False))


def cpa_statement(book):
    """cp-algorithms' problem paragraph, the first paragraph after the article's title."""
    import html
    import os
    import re
    md = open(os.path.join(book, ZM), encoding='utf-8').read()
    a = md.index('# Finding the largest zero submatrix')
    para = md[a:].split('\n\n')[1].strip()
    return re.sub(r'`([^`]+)`', lambda m: '<code>' + html.escape(m.group(1), quote=False) + '</code>', html.escape(para, quote=False))


def EXERCISES(exercism, book):
    import random
    src = lambda args, expect, visible=False: {'args': args, 'expect': expect, 'visible': visible, 'generated_by': 'source'}  # noqa: E731
    ai = lambda args, expect, visible=False: {'args': args, 'expect': expect, 'visible': visible, 'generated_by': 'ai'}  # noqa: E731
    # c1 ODS Exercise 3.14 with TheAlgorithms' doctests: pop_value's and get_current_min's sequences, less what fixes the
    # class's quirks (its size limit and the −inf it returns on an empty stack)
    t1 = [['push', 1], ['push', 2], ['pop'], ['pop']]
    t2 = [['push', 123], ['push', -123], ['push', 0], ['min'], ['pop'], ['min'], ['pop'], ['min'], ['pop']]
    rnd = random.Random(34)
    long_ops, n = [], 0
    for _ in range(400):
        k = rnd.random()
        if n == 0 or k < 0.45:
            long_ops.append(['push', rnd.randint(0, 6)])
            n += 1
        elif k < 0.7:
            long_ops.append(['pop'])
            n -= 1
        elif k < 0.9:
            long_ops.append(['min'])
        else:
            long_ops.append(['size'])
    ai_seqs = [
        [['push', 5], ['push', 1], ['push', 1], ['pop'], ['min']],                       # a repeated minimum
        [['push', 2], ['push', 2], ['push', 2], ['min'], ['pop'], ['min'], ['size']],     # all equal
        [['push', 5], ['push', 4], ['push', 3], ['min'], ['pop'], ['min'], ['pop'], ['min']],   # decreasing
        [['push', 1], ['push', 2], ['push', 3], ['min'], ['size'], ['pop'], ['min']],     # increasing
        [['size'], ['push', 7], ['size'], ['min'], ['pop'], ['size']],                    # empty and one element
        long_ops,
    ]
    tests = [src([t1], _play(t1), True), src([t2], _play(t2))] + [ai([s], _play(s), i == 0) for i, s in enumerate(ai_seqs)]
    c1 = {
        'id': 'c1', 'source_id': 'ods:linkedlists#exc-14', 'source_number': 'Exercise 3.14', 'origin': 'ods', 'kind': 'code',
        'bloom': 'Create', 'place': {'at': 'end'}, 'cite': 'min-stack',
        'changes': ('The tests call run(ops), which the starter defines: it plays a list of operations on a new MinStack and returns '
                    'what pop, size and min return. Its first two tests are TheAlgorithms’ doctests for stack_tracking_min_max.py '
                    '(MIT, © The Algorithms), less the size limit and the value they return on an empty stack, which the exercise '
                    'does not ask for; min and pop are never called on an empty stack.'),
        'prompt': ods_statement(book),
        'answer': {'type': 'code',
                   'python': {'entry': 'run', 'starter': MINSTACK_PY_START + RUN_PY, 'reference': MINSTACK_PY + RUN_PY, 'generated_by': 'ai'},
                   'javascript': {'entry': 'run', 'starter': MINSTACK_JS_START + RUN_JS, 'reference': MINSTACK_JS + RUN_JS, 'generated_by': 'ai'},
                   'tests': tests, 'bound': 'n',
                   'grow': "(n, rand) => [Array.from({ length: n }, (_, i) => (i % 4 === 3 ? ['min'] : ['push', rand.int(0, 99)]))]",
                   'generated_by': 'ai'},
    }
    # c2 cp-algorithms' problem with tryalgo's two grids, 0 and 1 swapped (tryalgo searches them for ones)
    g1 = ['10110111', '01000101', '11011000', '00111010', '11011101', '01000101']
    g2 = ['11', '11']
    swap = lambda g: [[1 - int(c) for c in row] for row in g]  # noqa: E731
    rnd = random.Random(35)
    grids = []
    for _ in range(6):
        n, m, p = rnd.randint(2, 7), rnd.randint(2, 7), rnd.choice([0.15, 0.3, 0.5])
        grids.append([[1 if rnd.random() < p else 0 for _ in range(m)] for _ in range(n)])
    fixed = [
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],                # all ones
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],                # all zeros
        [[0, 0, 1, 0, 0, 0, 1]],                                   # 1 × m
        [[0], [0], [1], [0], [0], [0]],                            # n × 1
        [[0]], [[1]],
    ]
    tests2 = [src([swap(g1)], 6, True), src([swap(g2)], 4)] + [ai([g], _brute_zero(g), i == 0) for i, g in enumerate(fixed + grids)]
    c2 = {
        'id': 'c2', 'source_id': 'cpa:dynamic_programming/zero_matrix', 'source_number': 'Finding the largest zero submatrix',
        'origin': 'cpa', 'kind': 'code', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'zero-submatrix',
        'changes': ('zero_matrix(a) returns the area of the largest zero submatrix, as the article’s code does; a is a list of rows of '
                    '0s and 1s with at least one row and one column. The first two tests are tryalgo’s grids for '
                    'rectangles_from_grid (MIT, © 2016 Jill-Jênn Vie) with 0 and 1 swapped, since tryalgo looks for ones; their areas '
                    'are its own.'),
        'prompt': cpa_statement(book),
        'answer': {'type': 'code',
                   'python': {'entry': 'zero_matrix', 'starter': ZERO_START_PY, 'reference': ZERO_PY, 'generated_by': 'ai'},
                   'javascript': {'entry': 'zero_matrix', 'starter': ZERO_START_JS, 'reference': ZERO_JS, 'generated_by': 'ai'},
                   'tests': tests2, 'bound': 'n',
                   'grow': ("(n, rand) => { const k = Math.max(1, Math.ceil(Math.sqrt(n))); "
                            "return [Array.from({ length: k }, () => Array.from({ length: k }, () => (rand() < 0.2 ? 1 : 0)))]; }"),
                   'generated_by': 'ai'},
    }
    concepts = [{'exercise': 'c1', 'concept': 'min-stack'}, {'exercise': 'c2', 'concept': 'largest-zero-submatrix'},
                {'exercise': 'c2', 'concept': 'nearest-smaller-element'}]
    return [c1, c2], concepts
