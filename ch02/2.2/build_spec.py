"""What tools/build_text.py needs to assemble 2.2 Dynamic arrays (the plan is plan.md beside this file).

Everything here is placement, markup or what the plan decided; the source's words come from the converters.
ODS's prose is its pseudocode edition (METHOD decision 20), read by tools/read_latex.py (dialect `ods`: the
edition macros, #code# as the edition's translate_code sets it). ODS's listings (\\codeimport) are four-language
code sets: Python, Java and C++ read from ODS's own sources by tools/ods_listing.py as the editions print them
(printed=True: bounds checks, `f.`, `Math.` and the C++ class prefix hidden, as ODS's snarf scripts hide them);
JavaScript translated by the AI from the Java (CODE_TRANSLATIONS) and AI-marked. No FIXES table: the reader's
output needs no correction.
"""
import html
import os
import re
import sys

_BOOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(_BOOK, 'tools'))
import ods_listing  # noqa: E402
import read_latex  # noqa: E402

TITLE = 'Dynamic arrays'
ODS = 'sources/_cache/ods/latex/arrays.tex'
_ODS_ARGS = dict(source='ods', reader='latex', dialect='ods', file=ODS, chapter=2)

BLOCKS = [
    # the chapter opening; its \cpponly paragraphs on ODS's C++ array class are not in the pseudocode edition
    dict(id='arrays-intro', **_ODS_ARGS, parts=[('In this chapter, we will study implementations', '\\section{#ArrayStack#')],
         locator='ods:arrays#chap:arrays, the chapter opening (the table, the three points and the amortized paragraph)',
         h2='Array-Based Lists'),
    dict(id='arraystack', **_ODS_ARGS, drop_first_heading=True, heading_shift=0,
         parts=[('\\section{#ArrayStack#', '\\subsection{Growing and Shrinking}')],
         locator='ods:arrays#sec:arraystack, the opening and The Basics',
         h2='ArrayStack: Fast Stack Operations Using an Array'),
    dict(id='resize', **_ODS_ARGS, drop_first_heading=True,
         parts=[('\\subsection{Growing and Shrinking}', 'The running time analysis from the previous section')],
         locator='ods:arrays#growing-and-shrinking, the first two paragraphs and resize()',
         h2='Growing and Shrinking'),
    # the rest of Growing and Shrinking under a header of OmniStax's (the source's subsection runs on), and Summary
    dict(id='arraystack-cost', **_ODS_ARGS,
         parts=[('The running time analysis from the previous section', '\\section{#FastArrayStack#')],
         locator='ods:arrays#growing-and-shrinking, from “The running time analysis from the previous section ignored…” '
                 'to the end of the section: lem:arraystack-amortized with its proof, and the Summary (thm:arraystack and the '
                 'push/pop paragraph)',
         h2='Amortized cost of resizing'),
    dict(id='fastarraystack', **_ODS_ARGS, drop_first_heading=True,
         parts=[('\\section{#FastArrayStack#', '\\section{#ArrayQueue#')],
         locator='ods:arrays#sec:fastarraystack', h2='FastArrayStack: An Optimized ArrayStack'),
]

# ODS's figure reference: its own number, linked to the Sim that stands for it (plans-summary question 18).
LATEX_REFS = {'figref:arraystack': ('<a href="#sim-arraystack">Figure 2.1</a>', 'Figure 2.1')}
# The proof's printed displays the derivations replace (root item 29.2), by a piece of their TeX as printed.
REPLACE = [
    ('arraystack-cost', '(#n#_i/2-1) \\le m', 'drv-arraystack-sum'),
    ('arraystack-cost', '#n#_i \\le 2m + 2r', ''),
    ('arraystack-cost', 'O(m+r) = O(m)', ''),
    ('arraystack-cost', '#a.length#/6 - 1', 'drv-shrink-case'),
]
FIGURE_AT = {'arraystack': 'sim-arraystack'}

AI = 'claude-opus-5-5 high'

# JavaScript for each listing, translated by the AI from ODS's Java line for line (same names, same order), keyed
# by the listing's reference. FastArrayStack's block moves are JavaScript's own (copyWithin, slice).
CODE_TRANSLATIONS = {
    'ods/ArrayStack.a.n.size()': '''
a;
n;

size() {
    return this.n;
}
''',
    'ods/ArrayStack.get(i).set(i,x)': '''
get(i) {
    return this.a[i];
}

set(i, x) {
    const y = this.a[i];
    this.a[i] = x;
    return y;
}
''',
    'ods/ArrayStack.add(i,x)': '''
add(i, x) {
    if (this.n + 1 > this.a.length) this.resize();
    for (let j = this.n; j > i; j--)
        this.a[j] = this.a[j-1];
    this.a[i] = x;
    this.n++;
}
''',
    'ods/ArrayStack.remove(i)': '''
remove(i) {
    const x = this.a[i];
    for (let j = i; j < this.n-1; j++)
        this.a[j] = this.a[j+1];
    this.n--;
    if (this.a.length >= 3*this.n) this.resize();
    return x;
}
''',
    'ods/ArrayStack.resize()': '''
resize() {
    const b = new Array(Math.max(this.n*2, 1));
    for (let i = 0; i < this.n; i++) {
        b[i] = this.a[i];
    }
    this.a = b;
}
''',
    'ods/FastArrayStack.add(i,x).remove(i).resize()': '''
resize() {
    const b = this.a.slice(0, this.n);
    b.length = Math.max(2*this.n, 1);
    this.a = b;
}

add(i, x) {
    if (this.n + 1 > this.a.length) this.resize();
    this.a.copyWithin(i+1, i, this.n);
    this.a[i] = x;
    this.n++;
}

remove(i) {
    const x = this.a[i];
    this.a.copyWithin(i, i+1, this.n);
    this.n--;
    if (this.a.length >= 3*this.n) this.resize();
    return x;
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


def CODE_HOOK(e):
    """ODS's listings: every \\codeimport as a code set; the pseudocode edition comments out \\cppimport and
    \\javaimport, so they print nothing, except FastArrayStack's, which the Java and C++ editions print where the
    prose speaks of "our C++ and Java implementations" (plan, question 2). The first ArrayStack listing carries
    the id implement-vector's coverage names (plan, question 6)."""
    ref = e['ref']
    if e['cmd'] == 'codeimport' or (e['cmd'] == 'javaimport' and ref.startswith('ods/FastArrayStack.')):
        return _code_set(listing(ref), 'arraystack-code' if ref == 'ods/ArrayStack.a.n.size()' else None)
    return ''


# ---------------------------------------------------------------- the figure's original caption, as plain text

CAPTIONS = read_latex.figure_captions(os.path.join(_BOOK, ODS), 2, 'ods')


def plain(t):
    """A caption for an attribute (root item 19: no maths in an attribute): $\\mathrm{add}(i,x)$ as add(i,x)."""
    return re.sub(r'\$([^$]*)\$', lambda m: re.sub(r'\\math(?:rm|it)\{([^}]*)\}', r'\1', m.group(1)), t)


ORIGINAL_CAPTION = plain(CAPTIONS['arraystack']['text'])


# ---------------------------------------------------------------- figures and derivations in the text

def sim(fid, caption, original=None, original_caption=None):
    attrs = f'class="sim" id="{fid}"'
    if original:
        attrs += f' data-original="{original}" data-original-caption="{html.escape(original_caption, quote=True)}"'
    return f'<figure {attrs}>\n  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>'


def R(rid, s=None):
    return f'<span data-ref="{rid}"><em>{s or rid}</em></span>'


SIM_CAPTION = (
    f'ODS’s ArrayStack running a sequence of add({R("i")}, x), remove({R("i")}) and set({R("i")}, x) calls on its backing '
    f'array {R("a")}. An add shifts {R("a")}[{R("i")}], …, {R("a")}[{R("n")} − 1] one cell to the right and a remove shifts '
    f'the cells after {R("i")} one cell to the left; when {R("a")} is full, or when length({R("a")}) ≥ 3{R("n")} after a '
    f'remove, resize() copies the {R("n")} elements into a new array {R("b")} of length 2{R("n")}. Each resize copies '
    f'<em>n</em><sub><em>i</em></sub> elements and comes at least <em>n</em><sub><em>i</em></sub>/2 − 1 calls after the one '
    'before it, so the copies never pass <span data-type="cost">2<em>m</em> + 2<em>r</em></span> for <em>m</em> calls and '
    '<em>r</em> resizes. Adding at the front shifts every element each time; at the boundary the array resizes once '
    'and then keeps its length, because it shrinks only once it is two-thirds empty. The same doubling, paid for by the aggregate, accounting '
    'and potential methods, is in <a href="/cs-interview-prep-ultra/ch01/1.5/#sim-pay-for-doubling">Section 1.5</a>.'
)

HTML = {
    'sim-arraystack': sim('sim-arraystack', SIM_CAPTION, '/media/ch02/ods-arraystack.png', ORIGINAL_CAPTION),
    'drv-arraystack-sum': '<figure class="dv" id="drv-arraystack-sum"></figure>',
    'drv-shrink-case': '<figure class="dv" id="drv-shrink-case"></figure>',
}


# ---------------------------------------------------------------- marks

def _refmath(tex):
    """The arraystack block's maths with the figure's referents a, i and n marked (a lone letter, not one inside
    a name such as \\mathrm{length})."""
    return re.sub(r'(?<![\\A-Za-z{])([ain])(?![A-Za-z}])', lambda m: '\\htmlData{ref=' + m.group(1) + '}{' + m.group(1) + '}', tex)


# the arraystack block's maths that name a, i or n, as the reader prints them
_REF_MATHS = [
    '$a[i],\\ldots,a[n-1]$', '$a[i+1],\\ldots,a[n-1]$', '$\\mathrm{length}(a) \\ge 3n$', '$\\mathrm{length}(a) \\ge n$',
    '$\\mathrm{length}(a) > n$', '$\\mathrm{length}(a)$', '$\\mathrm{add}(i,x)$', '$\\mathrm{remove}(i)$',
    '$\\mathrm{get}(i)$', '$\\mathrm{set}(i,x)$', '$a[n-1]$', '$a[0]$', '$a[i]$', '$O(n-i)$', '$a$', '$i$', '$n$',
]
FN_HALF = '<sup class="fn" data-note="err-half"></sup>'

# (block, text as built, replacement, [count]): concepts, referents, the erratum marker, the connectives the
# derivation carries
MARKS = [
    # concepts: the span that introduces each (plan, Concepts), and the chapter opening's mention of the backing array
    ('arrays-intro', 'called the <em>backing array</em>', 'called the <span data-concept="dynamic-array"><em>backing array</em></span>'),
    ('arraystack', 'called the <em>backing array</em>', 'called the <span data-concept="dynamic-array"><em>backing array</em></span>'),
    ('resize', 'method is fairly straightforward; it allocates a new array',
     'method is fairly straightforward; <span data-concept="array-resize">it allocates a new array</span>'),
    ('arraystack-cost', 'then the total time spent during all calls to $\\mathrm{resize}()$ is $O(m)$.',
     'then <span data-concept="dynamic-array-cost">the total time spent during all calls to $\\mathrm{resize}()$ is $O(m)$</span>.'),
    ('arraystack-cost', '<em>amortized analysis</em>', '<span data-concept="amortized-analysis"><em>amortized analysis</em></span>'),
    ('fastarraystack', 'specific functions that are very efficient at copying and moving blocks of data',
     '<span data-concept="block-copy">specific functions that are very efficient at copying and moving blocks of data</span>'),
    # erratum 19: the bound the proof needs and proves is n_i/2 − 1
    ('arraystack-cost', 'call to $\\mathrm{resize}()$ is at least $n_i/2$.</p>',
     'call to $\\mathrm{resize}()$ is at least $n_i/2$.' + FN_HALF + '</p>'),
    # the words between the three displays drv-arraystack-sum replaces (root item 29.2; its steps carry them)
    ('arraystack-cost', '<p>which is equivalent to</p>\n', ''),
    ('arraystack-cost', '<p>On the other hand, the total time spent during all calls to $\\mathrm{resize}()$ is</p>\n', ''),
] + [('arraystack', t, _refmath(t), 20) for t in _REF_MATHS]


# ---------------------------------------------------------------- derivations

DRV_SUM = {
    'id': 'arraystack-sum',
    'what': 'all calls to resize() take O(m) time',
    'source': 'Open Data Structures, 2.1.2 Growing and Shrinking, the proof of Lemma 2.1',
    'nodes': [
        {
            'assumes': [
                {'text': 'Between the $(i-1)$th and the $i$th call to $\\mathrm{resize}()$ there are at least $n_i/2-1$ calls '
                         'to $\\mathrm{add}(i,x)$ or $\\mathrm{remove}(i)$, where $n_i$ is the value of $n$ during the $i$th call.',
                 'src': 'the proof’s two cases'},
                {'text': 'There are $m$ calls to $\\mathrm{add}(i,x)$ and $\\mathrm{remove}(i)$ in all, and $r$ calls to '
                         '$\\mathrm{resize}()$.'},
            ],
            'then': {'tex': '\\mk{s}{\\sum_{i=1}^{r} (n_i/2-1)} \\le \\mk{m}{m}', 'uses': [0, 1],
                     'why': 'The stretches between consecutive calls to $\\mathrm{resize}()$ do not overlap, so their calls add up to at most $m$.'},
            'steps': [
                {'tex': '\\mk{s}{\\sum_{i=1}^{r} n_i/2} - \\mk{r}{r} \\le \\mk{m}{m}', 'uses': []},
                {'tex': '\\mk{s}{\\sum_{i=1}^{r} n_i/2} \\le \\mk{m}{m} + \\mk{r}{r}', 'uses': []},
                {'tex': '\\mk{s}{\\sum_{i=1}^{r} n_i} \\le \\mk{m}{2m} + \\mk{r}{2r}', 'uses': []},
            ],
            'src': 'Lemma 2.1, proof',
        },
        {
            'assumes': [
                {'text': 'A call to $\\mathrm{resize}()$ with $n$ elements stored takes $O(n)$ time.', 'src': '2.1.2 Growing and Shrinking'},
                {'step': 0},
                {'tex': 'r \\le m', 'src': 'Lemma 2.1, proof'},
            ],
            'then': {'tex': '\\mk{T}{\\text{time in } \\mathrm{resize}()} = \\mk{s}{\\sum_{i=1}^{r} O(n_i)}', 'uses': [0]},
            'steps': [
                {'tex': '\\mk{T}{\\text{time in } \\mathrm{resize}()} \\le \\mk{s}{O(2m+2r)}', 'uses': [1],
                 'cap': 'The $r$ terms $O(n_i)$ share one constant, so their sum is $O$ of the sum of the $n_i$.'},
                {'tex': '\\mk{T}{\\text{time in } \\mathrm{resize}()} \\le \\mk{s}{O(m+r)}', 'uses': [],
                 'cap': 'A constant factor does not change the class.'},
                {'tex': '\\mk{T}{\\text{time in } \\mathrm{resize}()} \\le \\mk{s}{O(m)}', 'uses': [2],
                 'cap': 'With $r \\le m$, $m + r \\le 2m$.'},
            ],
            'src': 'Lemma 2.1, proof',
        },
    ],
}

DRV_SHRINK = {
    'id': 'shrink-case',
    'what': 'at least nᵢ/2 − 1 calls to remove(i) since the last resize',
    'source': 'Open Data Structures, 2.1.2 Growing and Shrinking, the proof of Lemma 2.1',
    'nodes': [
        {
            'assumes': [
                {'text': 'After the previous call to $\\mathrm{resize}()$, at least $\\mathrm{length}(a)/2-1$ elements were '
                         'stored in $a$.', 'src': 'Lemma 2.1, proof, the second case'},
                {'tex': 'n_i \\le \\mathrm{length}(a)/3', 'src': 'Lemma 2.1, proof, the second case'},
                {'text': 'Each call to $\\mathrm{remove}(i)$ takes one element out and each call to $\\mathrm{add}(i,x)$ puts '
                         'one in, so the calls to $\\mathrm{remove}(i)$ since the previous resize number at least the elements lost since then.'},
            ],
            'then': {'tex': '\\mk{R}{R} \\ge \\mk{h}{\\mathrm{length}(a)/2 - 1} - \\mk{t}{\\mathrm{length}(a)/3}', 'uses': [0, 1, 2]},
            'steps': [
                {'tex': '\\mk{R}{R} \\ge \\mk{h}{\\mathrm{length}(a)/6 - 1}', 'uses': [], 'map': {'t': 'h'}},
                {'tex': '\\mk{R}{R} \\ge \\mk{h}{(\\mathrm{length}(a)/3)/2 - 1}', 'uses': []},
                {'tex': '\\mk{R}{R} \\ge \\mk{h}{n_i/2 - 1}', 'uses': [1],
                 'cap': 'Since $\\mathrm{length}(a)/3 \\ge n_i$, putting $n_i$ in its place can only make the right-hand side smaller.'},
            ],
            'src': 'Lemma 2.1, proof',
        },
    ],
}


def check_derivations():
    """Every line holds: the align's identities for every length that is a multiple of 6 up to 600; and, over 400
    random runs of 300 calls from an empty ArrayStack (ODS's policy: grow to 2n when full, shrink to 2n when
    length(a) ≥ 3n), the per-resize bound, the sum and the lemma's inequality."""
    import random
    from fractions import Fraction as Fr
    for L in range(6, 601, 6):
        L = Fr(L)
        assert L / 2 - 1 - L / 3 == L / 6 - 1 == (L / 3) / 2 - 1
        for ni in range(0, int(L / 3) + 1):
            assert (L / 3) / 2 - 1 >= Fr(ni, 2) - 1
    rnd = random.Random(22)
    for run in range(400):
        n, cap, since, m, ns = 0, 1, 0, 0, []
        bias = rnd.random()
        for _ in range(300):
            add = n == 0 or rnd.random() < bias
            m += 1
            since += 1
            if add:
                if n == cap:
                    ns.append(n)
                    assert since >= Fr(n, 2) - 1
                    since, cap = 0, max(1, 2 * n)
                n += 1
            else:
                n -= 1
                if cap >= 3 * n:
                    ns.append(n)
                    assert since >= Fr(n, 2) - 1
                    since, cap = 0, max(1, 2 * n)
            r = len(ns)
            assert sum(Fr(x, 2) - 1 for x in ns) <= m
            assert sum(ns) <= 2 * m + 2 * r and r <= m
    return True


# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]

LEAD = ('An Essential section on the array that grows and shrinks behind a list, with ODS’s ArrayStack; '
        '<span data-concept="block-copy">block copying</span> is Advanced. Arrays are indexed from 0. ArrayStack implements '
        '<a href="/cs-interview-prep-ultra/ch02/2.1/">Section 2.1</a>’s List interface and is named by the rule at the end of '
        'that passage. <a href="/cs-interview-prep-ultra/ch01/1.5/">Section 1.5</a> doubled an array only as it grew and wrote '
        '<em>m</em> for its capacity; here length(<em>a</em>), <code>a.length</code> in Java, is the capacity, <em>m</em> '
        'counts operations, and the array also shrinks when length(<em>a</em>) ≥ 3<em>n</em>.')

SECTION = {
    'id': '2.2', 'chapter': '2', 'title': 'Dynamic arrays', 'short': 'Dynamic arrays',
    'lead': LEAD,
    'objectives': [], 'summary_html': '',
    'notes': ('ODS’s C++ array class, which only its C++ edition describes, and the rest of its chapter on array-based lists, '
              'which chapter 3 carries, are left out here.'),
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'No exercise ships with this section yet. OpenDSA’s keyed array-list questions on inserting and deleting at '
        'position i and on where the elements sit (ALMCQinsarb, ALMCQdelarb, ALMCQsucc) wait for the converter of '
        'OpenDSA’s Khan-format exercises, and its AlistInsertPRO and AlistRemovePRO for the sequence answer type; its '
        'questions about a current position (ALMCQinscurr, ALMCQdelcurr, ALTFpred) assume a list model this book does not '
        'teach and are left out. Coding Interview University’s “Implement a vector” has no tests of its own and is left '
        'out; TheAlgorithms’ dynamic_array.py and ODS’s test_arraystack.py and test_fastarraystack.py are tests with no '
        'printed statement. ODS Exercises 2.1 and 2.2 have no published answers and are left out. ODS Exercise 2.7, which '
        'needs an ArrayDeque, and MIT 6.006 Spring 2020 problem 1-3, on a double-ended sequence, are held for Section 3.3.'),
    'figures': [
        {'id': 'sim-arraystack', 'kind': 'sim', 'originals': ['/media/ch02/ods-arraystack.png'],
         'original_caption': ORIGINAL_CAPTION, 'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'a', 'label': 'a, the backing array', 'figures': ['sim-arraystack']},
        {'id': 'b', 'label': 'b, the array resize() fills', 'figures': ['sim-arraystack']},
        {'id': 'i', 'label': 'i, the index a call names', 'figures': ['sim-arraystack']},
        {'id': 'n', 'label': 'n, the number of elements stored', 'figures': ['sim-arraystack']},
    ],
    'coverage': [
        {'span': 'arrays-intro', 'concept': 'dynamic-array', 'verb': 'uses'},
        {'span': 'arrays-intro', 'concept': 'amortized-analysis', 'verb': 'uses'},
        {'span': 'arraystack', 'concept': 'dynamic-array', 'verb': 'introduces'},
        {'span': 'arraystack-code', 'concept': 'implement-vector', 'verb': 'introduces'},
        {'span': 'resize', 'concept': 'array-resize', 'verb': 'introduces'},
        {'span': 'resize', 'concept': 'dynamic-array', 'verb': 'uses'},
        {'span': 'arraystack-cost', 'concept': 'dynamic-array-cost', 'verb': 'introduces'},
        {'span': 'arraystack-cost', 'concept': 'amortized-analysis', 'verb': 'uses'},
        {'span': 'arraystack-cost', 'concept': 'array-resize', 'verb': 'uses'},
        {'span': 'fastarraystack', 'concept': 'block-copy', 'verb': 'introduces'},
        {'span': 'fastarraystack', 'concept': 'dynamic-array', 'verb': 'uses'},
    ],
    'footnotes_extra': [
        {'id': 'err-half', 'kind': 'correction',
         'html': 'The bound the proof needs here is $n_i/2-1$, the one its sum above uses and the one it states at the start '
                 'and at the end. The first case below gives $n_i/2$, but the second gives only $n_i/2-1$.'},
    ],
    'derivations': [DRV_SUM, DRV_SHRINK],
}
