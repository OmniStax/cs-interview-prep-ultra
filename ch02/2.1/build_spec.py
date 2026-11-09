"""What tools/build_text.py needs to assemble 2.1 Arrays and the list interface (the plan is plan.md beside this file).

Everything here is placement, markup or a correction note; the sources' words come from the readers in readers.py
(Wikipedia's wikitext, and ODS's LaTeX through tools/read_latex.py). WIKI_FIXES is the replacement table: empty,
since nothing the readers give needed correcting.
"""
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location('readers_2_1', os.path.join(_HERE, 'readers.py'))
readers = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(readers)
_BOOK = os.path.dirname(os.path.dirname(_HERE))

TITLE = 'Arrays and the list interface'
ARRAY = 'sources/_cache/wikipedia/Array_data_structure.wiki'
POINTER = 'sources/_cache/wikipedia/Pointer_computer_programming.wiki'
INTRO = 'sources/_cache/ods/latex/intro.tex'

BLOCKS = [
    dict(id='array', source='wikipedia', reader=readers.wikitext_block, file=ARRAY, note_prefix='wp-array-fn',
         start="In [[computer science]], an '''array'''", stop='==History==',
         locator='wikipedia:Array_(data_structure), the lead', h2='Arrays'),
    dict(id='addressing', source='wikipedia', reader=readers.wikitext_block, file=ARRAY, note_prefix='wp-array-fn',
         start='==Element identifier and addressing formulas==', stop='===Dope vectors===', drop_first_heading=True,
         locator='wikipedia:Array_(data_structure)#Element identifier and addressing formulas, its opening with “One-dimensional arrays” and “Multidimensional arrays”, before “Dope vectors”',
         h2='Element identifier and addressing formulas'),
    dict(id='efficiency', source='wikipedia', reader=readers.wikitext_block, file=ARRAY, note_prefix='wp-array-fn',
         start='==Efficiency==', stop='===Comparison with other data structures===', drop_first_heading=True,
         locator='wikipedia:Array_(data_structure)#Efficiency, its opening, before “Comparison with other data structures”',
         h2='Efficiency'),
    dict(id='iliffe', source='wikipedia', reader=readers.wikitext_block, file=ARRAY, note_prefix='wp-array-fn',
         start='[[Image:Array of array storage.svg', stop='==Dimension==',
         locator='wikipedia:Array_(data_structure)#Comparison with other data structures, the Iliffe-vector paragraph and its image',
         h2='Iliffe vectors'),
    dict(id='c-arrays', source='wikipedia', reader=readers.wikitext_block, file=POINTER, note_prefix='wp-pointer-fn',
         start='====C arrays====', stop='====C linked list====', drop_first_heading=True,
         locator='wikipedia:Pointer_(computer_programming)#C arrays', h2='C arrays'),
    dict(id='list-interface', source='ods', reader=readers.ods_block, file=INTRO, chapter='1',
         start='\\subsection{The #List# Interface', stop='\\subsection{The #USet#', drop_first_heading=True,
         locator='ods:intro#the-list-interface-linear-sequences', h2='The List Interface: Linear Sequences'),
]

# the image lines of the passages: the Sim or photograph that stands in their place, or '' where the Sim stands
# after a paragraph instead (AFTER_TEXT) or the image is dropped (the 3D diagram: plan.md)
WIKI_FIGURES = {
    ('addressing', '1D array diagram.svg'): '',
    ('addressing', '2D array diagram.svg'): '',
    ('addressing', '3D array diagram.svg'): '',
    ('iliffe', 'Array of array storage.svg'): 'photo-iliffe',
}
# the indented formula line of “Multidimensional arrays”, set as the display the article means by it
WIKI_DISPLAYS = {
    ('addressing', 0): r'B + c_1 \cdot i_1 + c_2 \cdot i_2 + \dots + c_k \cdot i_k.',
}
WIKI_FIXES = []

ODS_FIGURE_AT = {'list': 'sim-list'}
ODS_LATEX_REFS = {'figref:list': ('<a href="#sim-list">Figure 1.4</a>', 'Figure 1.4')}

LIST_CAPTION_HTML, LIST_CAPTION = readers.ods_caption(os.path.join(_BOOK, INTRO), 'list', '1')
CREDIT_1D = 'Image: Tropwine, CC BY 4.0, via Wikimedia Commons.'
CAP_1D = 'Diagram of a typical 1D array. ' + CREDIT_1D
CAP_2D = 'Diagram of a typical 2D array. ' + CREDIT_1D


def sim(fid, caption, original=None, original_caption=None):
    attrs = f'class="sim" id="{fid}"'
    if original:
        attrs += f' data-original="{original}" data-original-caption="{original_caption}"'
    return f'<figure {attrs}>\n  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>'


def photo(fid, src, caption, credit, width):
    return (f'<figure class="photo" id="{fid}">\n  <img src="{src}" alt="" data-width="{width}">\n'
            f'  <figcaption><span>{caption} {credit}</span></figcaption>\n</figure>')


HAVE_2D = os.path.exists(os.path.join(_BOOK, 'media/ch02/wp-2d-array-diagram.png'))

HTML = {
    'sim-address': sim(
        'sim-address',
        'Each element of a one-dimensional array starts <em>c</em> bytes after the one before it, so element '
        '<em>i</em> sits at <em>B</em> + <em>c</em> · <em>i</em>. Numbering the elements from 1 or from 31 leaves them '
        'where they are and moves only <em>B</em>, which then lies before the first element, where no element is.',
        '/media/ch02/wp-1d-array-diagram.png', CAP_1D),
    'sim-row-major': sim(
        'sim-row-major',
        'In row-major order the rows of a two-dimensional array follow one another in memory, so the row increment '
        '<em>c</em> is a whole row of bytes and the column increment <em>d</em> is one element. '
        '<em>a</em>[<em>i</em>][<em>j</em>] then sits at <em>B</em> + <em>c</em> · <em>i</em> + <em>d</em> · <em>j</em>.',
        *(('/media/ch02/wp-2d-array-diagram.png', CAP_2D) if HAVE_2D else ())),
    'sim-list': sim(
        'sim-list',
        'A List holds <em>x</em><sub>0</sub>, …, <em>x</em><sub><em>n</em>−1</sub>. add(<em>i</em>, <em>x</em>) moves '
        '<em>x</em><sub><em>n</em>−1</sub> back to <em>x</em><sub><em>i</em></sub> one place right, starting from the end '
        'so that nothing is overwritten, then writes <em>x</em> at position <em>i</em>; remove(<em>i</em>) moves the '
        'values after <em>i</em> one place left. The four Deque operations are these calls at position 0 or at the end.',
        '/media/ch02/ods-1-4-list.png', LIST_CAPTION.replace('"', '&quot;')),
    'photo-iliffe': photo(
        'photo-iliffe', '/media/ch02/wp-array-of-array-storage.png',
        'A two-dimensional array stored as a one-dimensional array of one-dimensional arrays (rows).',
        'Image: “Array of array storage.svg”, Wikimedia Commons, public domain.', 120),
}

AFTER_TEXT = {
    'addressing': [('may not be the address of any element.', 'sim-address'),
                   ('a<sub>22</sub>, a<sub>23</sub>.', 'sim-row-major')],
}

FN = '<sup class="fn" data-note="{}"></sup>'
MARKS = [
    # concepts: the one introducing span of each
    ('array', 'an <strong>array</strong> is', 'an <span data-concept="array"><strong>array</strong></span> is'),
    ('c-arrays', 'formally defined in terms of pointer arithmetic', 'formally defined in terms of <span data-concept="pointer-arithmetic">pointer arithmetic</span>'),
    ('list-interface', 'interface. A List, illustrated', 'interface. <span data-concept="list-interface">A List</span>, illustrated'),
    # correction markers, right after the words they correct
    ('addressing', 'replaced by <em>B</em> + 30<em>c</em>', 'replaced by <em>B</em> + 30<em>c</em>' + FN.format('err-rebase')),
    ('addressing', 'a<sub>22</sub>, a<sub>23</sub>.', 'a<sub>22</sub>, a<sub>23</sub>.' + FN.format('err-a11')),
    # addresses are positions (index); bounds are costs
    ('addressing', 'the address <em>B</em> + <em>c</em> · <em>i</em>,', 'the address <span data-type="index"><em>B</em> + <em>c</em> · <em>i</em></span>,'),
    ('addressing', 'address <em>B</em> + <em>c</em> · <em>i</em> + <em>d</em> · <em>j</em>,', 'address <span data-type="index"><em>B</em> + <em>c</em> · <em>i</em> + <em>d</em> · <em>j</em></span>,'),
    ('array', 'has the address 2000 + (<em>i</em> × 4).', 'has the address <span data-type="index">2000 + (<em>i</em> × 4)</span>.'),
    ('efficiency', 'worst case) constant time.', 'worst case) <span data-type="cost">constant time</span>.'),
    ('efficiency', 'linear (O(<em>n</em>)) space', '<span data-type="cost">linear (O(<em>n</em>)) space</span>'),
]

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]


def _fig(fid, draws, original=None, caption=None):
    row = {'id': fid, 'kind': 'sim', 'draws': draws, 'ai': FIG_AI}
    if original:
        row['originals'] = [original]
        row['original_caption'] = caption
    return row


SECTION = {
    'id': '2.1', 'chapter': '2', 'title': 'Arrays and the list interface', 'short': 'Arrays and lists',
    'lead': ('An Essential section on the <span data-concept="array">array</span>, whose elements all have one size so that '
             'each element’s address can be computed from its index; on how C defines indexing as '
             '<span data-concept="pointer-arithmetic">pointer arithmetic</span>; and on the '
             '<span data-concept="list-interface">List interface</span>. Indices start at 0 throughout, as in '
             'x<sub>0</sub>, …, x<sub>n−1</sub>. Stacks, queues and deques come in Sections 3.1–3.3, so the Deque '
             'operations in the List passage are a preview.'),
    'objectives': [], 'summary_html': '',
    'notes': ('The Array article’s history, applications, other memory layouts and comparisons, and the Pointer article '
              'outside its section on C arrays, are left out here.'),
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'The true-or-false items are Busbee’s, with Busbee’s answers: items 2, 3 and 5 of 6.17; items 1 and 4 (C++ '
        'declarations) and 6–10 (searching and sorting, taught in later chapters) are left out. ODS Exercise 2.5 has no tests '
        'of its own, so its tests and references are written by the AI that built the section, and keon’s and TheAlgorithms’ '
        'rotate functions pass them. The matrix tests are Exercism’s canonical data and its references the AI’s. ODS '
        'Exercise 1.6 is asked here for the List interface only, with AI tests and references; its USet and SSet parts '
        'wait for chapters 5 and 8, and Exercise 1.7, which has no tests, is left out. Each code card’s starter holds the '
        'small function its tests call. Exercism list-ops is left out, since its operations take functions as arguments, '
        'which a test written as data cannot carry; Kattis nsum is left out as trivial; TheAlgorithms’ index_2d_array_in_1d '
        'and reverse_array are tests with no printed statement. The OpenDSA List questions wait for the converter of '
        'OpenDSA’s exercises, and each is read against the list model this page teaches when it is converted. No open '
        'exercise asks for pointer arithmetic. The MIT 6.006 card is in this section’s NC file.'),
    'figures': [
        _fig('sim-address', ['index', 'key', 'size'], '/media/ch02/wp-1d-array-diagram.png', CAP_1D),
        _fig('sim-row-major', ['index', 'key', 'size'], *(('/media/ch02/wp-2d-array-diagram.png', CAP_2D) if HAVE_2D else ())),
        {'id': 'photo-iliffe', 'kind': 'photo', 'widths': [120]},
        _fig('sim-list', ['index', 'key', 'cost', 'size'], '/media/ch02/ods-1-4-list.png', LIST_CAPTION),
    ],
    'referents': [],
    'coverage': [
        {'span': 'array', 'concept': 'array', 'verb': 'introduces'},
        {'span': 'addressing', 'concept': 'array', 'verb': 'reinforces'},
        {'span': 'efficiency', 'concept': 'array', 'verb': 'reinforces'},
        {'span': 'efficiency', 'concept': 'big-o', 'verb': 'uses'},
        {'span': 'iliffe', 'concept': 'array', 'verb': 'reinforces'},
        {'span': 'c-arrays', 'concept': 'pointer-arithmetic', 'verb': 'introduces'},
        {'span': 'c-arrays', 'concept': 'array', 'verb': 'uses'},
        {'span': 'list-interface', 'concept': 'list-interface', 'verb': 'introduces'},
        {'span': 'list-interface', 'concept': 'interface-vs-implementation', 'verb': 'uses'},
    ],
    'footnotes_extra': [
        {'id': 'err-rebase', 'kind': 'correction',
         'html': 'As printed, “<em>B</em> + 30<em>c</em>”. With element <em>i</em> at <em>B</em> + <em>c</em> · <em>i</em>, the base '
                 'address that numbers the same five elements 31 to 35 is <em>B</em> − 30<em>c</em>, since '
                 '(<em>B</em> − 30<em>c</em>) + <em>c</em> · (<em>i</em> + 30) = <em>B</em> + <em>c</em> · <em>i</em>; replacing '
                 '<em>B</em> by <em>B</em> + 30<em>c</em> would number them −29 to −25.'},
        {'id': 'err-a11', 'kind': 'correction',
         'html': 'The labels a<sub>11</sub> … a<sub>23</sub> count rows and columns from 1, but a C array counts from 0: '
                 '<code>int a[2][3]</code> holds <code>a[0][0]</code>, <code>a[0][1]</code>, <code>a[0][2]</code>, '
                 '<code>a[1][0]</code>, <code>a[1][1]</code>, <code>a[1][2]</code>, stored in that order.'},
        {'id': 'err-rotate', 'kind': 'correction',
         'html': 'As printed, the index set ends at $\\mathrm{length}(a)$; the last index of $a$ is $\\mathrm{length}(a) - 1$, '
                 'so $i$ runs over $\\{0,\\ldots,\\mathrm{length}(a)-1\\}$.'},
    ],
}

# ---------------------------------------------------------------- exercises
ROTATE_PROMPT = ('Implement a method $\\mathrm{rotate}(a,r)$ that “rotates” the array $a$ so that $a[i]$ moves to '
                 '$a[(i+r)\\bmod \\mathrm{length}(a)]$, for all $i\\in\\{0,\\ldots,\\mathrm{length}(a)\\}$.'
                 '<sup class="fn" data-note="err-rotate"></sup>')

ROT_PY_START = '''def rotate(a, r):
    pass


def rotated(a, r):
    rotate(a, r)
    return a
'''
ROT_PY = '''def rotate(a, r):
    n = len(a)
    old = a[:]
    for i in range(n):
        a[(i + r) % n] = old[i]


def rotated(a, r):
    rotate(a, r)
    return a
'''
ROT_JS_START = '''function rotate(a, r) {
}

function rotated(a, r) {
  rotate(a, r);
  return a;
}
'''
ROT_JS = '''function rotate(a, r) {
  const n = a.length;
  const old = a.slice();
  for (let i = 0; i < n; i++) a[(i + r) % n] = old[i];
}

function rotated(a, r) {
  rotate(a, r);
  return a;
}
'''
ROT_CASES = [([1, 2, 3, 4, 5], 1), ([1, 2, 3, 4, 5], 0), ([1, 2, 3, 4, 5], 2), ([1, 2, 3, 4, 5], 4),
             ([1, 2, 3, 4, 5], 5), ([1, 2, 3, 4, 5], 7), ([9], 3), ([1, 1, 2, 2], 1), ([0, -1, 5], 2),
             ([3, 8, 9, 7, 6, 1, 2], 1000003), (['a', 'b', 'c', 'd'], 3)]

MAT_PY_START = '''class Matrix:
    def __init__(self, matrix_string):
        pass

    def row(self, index):
        pass

    def column(self, index):
        pass


def answer(matrix_string, method, index):
    return getattr(Matrix(matrix_string), method)(index)
'''
MAT_PY = '''class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(v) for v in line.split()] for line in matrix_string.splitlines()]

    def row(self, index):
        return list(self.rows[index - 1])

    def column(self, index):
        return [r[index - 1] for r in self.rows]


def answer(matrix_string, method, index):
    return getattr(Matrix(matrix_string), method)(index)
'''
MAT_JS_START = '''class Matrix {
  constructor(matrixString) {
  }

  row(index) {
  }

  column(index) {
  }
}

function answer(matrixString, method, index) {
  return new Matrix(matrixString)[method](index);
}
'''
MAT_JS = '''class Matrix {
  constructor(matrixString) {
    this.rows = matrixString.split("\\n").map((line) => line.trim().split(/\\s+/).map(Number));
  }

  row(index) {
    return this.rows[index - 1].slice();
  }

  column(index) {
    return this.rows.map((r) => r[index - 1]);
  }
}

function answer(matrixString, method, index) {
  return new Matrix(matrixString)[method](index);
}
'''

LIST_PY_START = '''class ArrayList:
    def __init__(self):
        pass

    def size(self):
        pass

    def get(self, i):
        pass

    def set(self, i, x):
        pass

    def add(self, i, x):
        pass

    def remove(self, i):
        pass


def run(ops):
    lst, out = ArrayList(), []
    for name, *args in ops:
        value = getattr(lst, name)(*args)
        if name in ("get", "size"):
            out.append(value)
    return out
'''
LIST_PY = '''class ArrayList:
    def __init__(self):
        self.a = [None]
        self.n = 0

    def size(self):
        return self.n

    def get(self, i):
        return self.a[i]

    def set(self, i, x):
        y = self.a[i]
        self.a[i] = x
        return y

    def add(self, i, x):
        if self.n == len(self.a):
            self.a = self.a + [None] * len(self.a)
        for j in range(self.n, i, -1):
            self.a[j] = self.a[j - 1]
        self.a[i] = x
        self.n += 1

    def remove(self, i):
        x = self.a[i]
        for j in range(i, self.n - 1):
            self.a[j] = self.a[j + 1]
        self.n -= 1
        self.a[self.n] = None
        return x


def run(ops):
    lst, out = ArrayList(), []
    for name, *args in ops:
        value = getattr(lst, name)(*args)
        if name in ("get", "size"):
            out.append(value)
    return out
'''
LIST_JS_START = '''class ArrayList {
  constructor() {
  }

  size() {
  }

  get(i) {
  }

  set(i, x) {
  }

  add(i, x) {
  }

  remove(i) {
  }
}

function run(ops) {
  const list = new ArrayList();
  const out = [];
  for (const [name, ...args] of ops) {
    const value = list[name](...args);
    if (name === "get" || name === "size") out.push(value);
  }
  return out;
}
'''
LIST_JS = '''class ArrayList {
  constructor() {
    this.a = [null];
    this.n = 0;
  }

  size() {
    return this.n;
  }

  get(i) {
    return this.a[i];
  }

  set(i, x) {
    const y = this.a[i];
    this.a[i] = x;
    return y;
  }

  add(i, x) {
    if (this.n === this.a.length) this.a = this.a.concat(new Array(this.a.length).fill(null));
    for (let j = this.n; j > i; j--) this.a[j] = this.a[j - 1];
    this.a[i] = x;
    this.n++;
  }

  remove(i) {
    const x = this.a[i];
    for (let j = i; j < this.n - 1; j++) this.a[j] = this.a[j + 1];
    this.n--;
    this.a[this.n] = null;
    return x;
  }
}

function run(ops) {
  const list = new ArrayList();
  const out = [];
  for (const [name, ...args] of ops) {
    const value = list[name](...args);
    if (name === "get" || name === "size") out.push(value);
  }
  return out;
}
'''


def list_cases():
    """Fixed operation sequences and one seeded random one, each answered by a plain Python list."""
    import random
    seqs = [
        [['size']],
        [['add', 0, 'a'], ['get', 0], ['size']],
        [['add', 0, 'a'], ['add', 1, 'b'], ['add', 2, 'c'], ['get', 0], ['get', 1], ['get', 2], ['size']],
        [['add', 0, 'c'], ['add', 0, 'b'], ['add', 0, 'a'], ['get', 0], ['get', 1], ['get', 2]],
        [['add', 0, 'a'], ['add', 1, 'c'], ['add', 1, 'b'], ['get', 1], ['get', 2], ['size']],
        [['add', 0, 'a'], ['add', 1, 'b'], ['set', 1, 'z'], ['get', 1], ['size']],
        [['add', 0, 'a'], ['add', 1, 'b'], ['add', 2, 'c'], ['remove', 0], ['get', 0], ['size'], ['remove', 1], ['get', 0], ['size']],
        [['add', 0, 'a'], ['add', 1, 'b'], ['add', 2, 'c'], ['add', 3, 'd'], ['remove', 1], ['get', 1], ['get', 2], ['size']],
    ]
    rnd = random.Random(21)
    ops, n = [], 0
    for _ in range(300):
        k = rnd.random()
        if n == 0 or k < 0.45:
            ops.append(['add', rnd.randint(0, n), rnd.randint(0, 99)])
            n += 1
        elif k < 0.65:
            ops.append(['remove', rnd.randint(0, n - 1)])
            n -= 1
        elif k < 0.8:
            ops.append(['set', rnd.randint(0, n - 1), rnd.randint(0, 99)])
        elif k < 0.95:
            ops.append(['get', rnd.randint(0, n - 1)])
        else:
            ops.append(['size'])
    seqs.append(ops)
    cases = []
    for s in seqs:
        ctl, out = [], []
        for name, *args in s:
            if name == 'add':
                ctl.insert(args[0], args[1])
            elif name == 'remove':
                ctl.pop(args[0])
            elif name == 'set':
                ctl[args[0]] = args[1]
            elif name == 'get':
                out.append(ctl[args[0]])
            else:
                out.append(len(ctl))
        cases.append((s, out))
    return cases


def _rot(a, r):
    n = len(a)
    b = [None] * n
    for i in range(n):
        b[(i + r) % n] = a[i]
    return b


def EXERCISES(exercism, book):
    import html
    import json
    ex, concepts = [], []
    # Busbee 6.17, True / False: items 2, 3 and 5, keyed by the page's own answers (read by script below)
    page = open(os.path.join(book, 'sources/_cache/lt-busbee/6.17__Practice-_Arrays_and_Lists.html'), encoding='utf-8').read()
    import re
    t = re.sub(r'<script.*?</script>|<style.*?</style>', '', page, flags=re.S)
    lines = [x.strip() for x in html.unescape(re.sub(r'<[^>]+>', '\n', t)).split('\n') if x.strip()]
    k0 = lines.index('True / False', lines.index('Review Questions', lines.index('Review Questions') + 1))
    items = lines[k0 + 1:k0 + 11]
    keys = lines[k0 + 12:k0 + 22]
    assert lines[k0 + 11] == 'Answers:' and len(items) == 10
    for n, cite in ((2, 'addressing'), (3, 'array'), (5, 'array')):
        ex.append({'id': f'k{n}', 'source_id': f'lt-busbee:6.17#tf-{n}', 'source_number': f'True / False {n}',
                   'origin': 'lt-busbee', 'kind': 'check', 'bloom': 'Remember', 'place': {'at': 'end'}, 'cite': cite,
                   'prompt': html.escape(items[n - 1], quote=False),
                   'answer': {'type': 'choice', 'options': ['True', 'False'], 'correct': 0 if keys[n - 1] == 'true' else 1,
                              'generated_by': 'source'}})
        concepts.append({'exercise': f'k{n}', 'concept': 'array'})
    # ODS Exercise 2.5
    tests = [{'args': [a, r], 'expect': _rot(a, r), 'visible': i < 2, 'generated_by': 'ai'} for i, (a, r) in enumerate(ROT_CASES)]
    ex.append({'id': 'c1', 'source_id': 'ods:arrays#exc-5', 'source_number': 'Exercise 2.5', 'origin': 'ods', 'kind': 'code',
               'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'addressing',
               'changes': 'The tests call rotated(a, r), which the starter defines: it runs your rotate on a and returns a.',
               'prompt': ROTATE_PROMPT,
               'answer': {'type': 'code',
                          'python': {'entry': 'rotated', 'starter': ROT_PY_START, 'reference': ROT_PY, 'generated_by': 'ai'},
                          'javascript': {'entry': 'rotated', 'starter': ROT_JS_START, 'reference': ROT_JS, 'generated_by': 'ai'},
                          'tests': tests, 'generated_by': 'ai'}})
    concepts.append({'exercise': 'c1', 'concept': 'array'})
    # Exercism matrix: the statement is its description.md, the tests its canonical data
    path = os.path.join(book, 'sources/_cache/exercism/exercises/matrix')
    desc = open(os.path.join(path, 'description.md'), encoding='utf-8').read()
    desc = re.sub(r'^# Instructions\s*', '', desc).strip()
    parts = []
    for blk in re.split(r'\n\s*\n', desc):
        if blk.startswith('```'):
            body = '\n'.join(blk.split('\n')[1:-1])
            parts.append('<pre>' + html.escape(body, quote=False) + '</pre>')
        elif blk.lstrip().startswith('- '):
            parts.append('<ul>' + ''.join(f'<li>{html.escape(x.strip()[2:], quote=False)}</li>' for x in blk.split('\n')) + '</ul>')
        else:
            parts.append(html.escape(' '.join(blk.split()), quote=False))
    data = json.load(open(os.path.join(path, 'canonical-data.json'), encoding='utf-8'))
    mt = [{'args': [c['input']['string'], c['property'], c['input']['index']], 'expect': c['expected'],
           'visible': i in (1, 5), 'generated_by': 'source'} for i, c in enumerate(data['cases'])]
    ex.append({'id': 'c2', 'source_id': 'exercism:matrix', 'source_number': 'matrix', 'origin': 'exercism', 'kind': 'code',
               'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'addressing',
               'changes': 'The tests call answer(matrix_string, method, index), which the starter defines over your Matrix class.',
               'prompt': '\n\n'.join(parts),
               'answer': {'type': 'code',
                          'python': {'entry': 'answer', 'starter': MAT_PY_START, 'reference': MAT_PY, 'generated_by': 'ai'},
                          'javascript': {'entry': 'answer', 'starter': MAT_JS_START, 'reference': MAT_JS, 'generated_by': 'ai'},
                          'tests': mt, 'generated_by': 'source'}})
    concepts.append({'exercise': 'c2', 'concept': 'array'})
    # ODS Exercise 1.6, the List part
    lt = [{'args': [ops], 'expect': out, 'visible': i in (2, 4), 'generated_by': 'ai'} for i, (ops, out) in enumerate(list_cases())]
    ex.append({'id': 'c3', 'source_id': 'ods:intro#exc-6', 'source_number': 'Exercise 1.6', 'origin': 'ods', 'kind': 'code',
               'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'list-interface',
               'changes': ('Only the List interface is asked for and tested. The tests call run(ops), which the starter defines: '
                           'it applies each operation to a new ArrayList and returns what get and size return.'),
               'prompt': ('From scratch, write and test implementations of the List, USet and SSet interfaces. These do not have '
                          'to be efficient. They can be used later to test the correctness and performance of more efficient '
                          'implementations. (The easiest way to do this is to store the elements in an array.)'),
               'answer': {'type': 'code',
                          'python': {'entry': 'run', 'starter': LIST_PY_START, 'reference': LIST_PY, 'generated_by': 'ai'},
                          'javascript': {'entry': 'run', 'starter': LIST_JS_START, 'reference': LIST_JS, 'generated_by': 'ai'},
                          'tests': lt, 'generated_by': 'ai'}})
    concepts.append({'exercise': 'c3', 'concept': 'list-interface'})
    return ex, concepts
