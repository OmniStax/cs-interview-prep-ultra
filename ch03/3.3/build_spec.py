"""What tools/build_text.py needs to assemble 3.3 Deques (the plan is plan.md beside this file).

Everything here is placement, markup or what the plan decided; the source's words come from the converters.
ODS's prose is its pseudocode edition (METHOD decision 20), read by tools/read_latex.py (dialect `ods`). ODS's
listings (\\codeimport) are four-language code sets: Python, Java and C++ read from ODS's own sources by
tools/ods_listing.py as the editions print them (printed=True, as 2.2); JavaScript translated by the AI from the
Java (CODE_TRANSLATIONS), and AI-marked. ODS's Python is shown unchanged: on Python 3 its `i < self.n/2` is the
real comparison the prose and Figure 2.3 make (plan, question 1). No FIXES table: the reader's output needs no
correction.
"""
import html
import os
import re
import sys

_BOOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(_BOOK, 'tools'))
import ods_listing  # noqa: E402
import read_latex  # noqa: E402

TITLE = 'Deques'
INTRO = 'sources/_cache/ods/latex/intro.tex'
ARRAYS = 'sources/_cache/ods/latex/arrays.tex'

BLOCKS = [
    # the Deque paragraph of ODS's subsection "The Queue, Stack, and Deque Interfaces" (its FIFO paragraph is 3.2's)
    dict(id='deque', source='ods', reader='latex', dialect='ods', file=INTRO, chapter=1,
         parts=[('A #Deque#', '\\subsection{The #List# Interface')],
         locator='ods:intro#the-queue-stack-and-deque-interfaces, the Deque paragraph (“A Deque is a generalization of '
                 'both…” to “…addLast(x) and removeFirst().”)',
         h2='The Deque interface'),
    dict(id='arraydeque', source='ods', reader='latex', dialect='ods', file=ARRAYS, chapter=2, drop_first_heading=True, heading_shift=0,
         parts=[('\\section{#ArrayDeque#', '\\section{#DualArrayDeque#')],
         locator='ods:arrays#sec:arraydeque, the whole section with thm:arraydeque',
         h2='ArrayDeque: Fast Deque Operations Using an Array'),
    dict(id='dualarraydeque', source='ods', reader='latex', dialect='ods', file=ARRAYS, chapter=2, drop_first_heading=True, heading_shift=0,
         parts=[('\\section{#DualArrayDeque#', '\\section{#RootishArrayStack#')],
         locator='ods:arrays#sec:dualarraydeque, the whole section with lem:dualarraydeque-amortized and thm:dualarraydeque',
         h2='DualArrayDeque: Building a Deque from Two Stacks'),
]

# ODS's figure numbers stay as printed and link to the Sims that stand for them; its lemma on ArrayStack's resize()
# is 2.2's (B18), kept as "Lemma 2.1" (plan, question 5).
LATEX_REFS = {
    'figref:arraydeque': ('<a href="#sim-arraydeque">Figure 2.3</a>', 'Figure 2.3'),
    'figref:dualarraydeque': ('<a href="#sim-dualarraydeque">Figure 2.4</a>', 'Figure 2.4'),
    'lemref:arraystack-amortized': ('<a href="/cs-interview-prep-ultra/ch02/2.2/#arraystack-cost">Lemma 2.1</a>', 'Lemma 2.1'),
}
# The Sims stand where the source's figures stood (the add(i,x) listing that follows each is the Sim's panel)
FIGURE_AT = {'arraydeque': 'sim-arraydeque', 'dualarraydeque': 'sim-dualarraydeque'}
# The proof's two printed eqnarray* displays, which the derivation replaces (root item 29.2), by a piece of their TeX
REPLACE = [
    ('dualarraydeque', '\\frac{4}{3}', 'drv-balance-potential'),
    ('dualarraydeque', '\\frac{2}{3}\\times', ''),
]

AI = 'claude-opus-5-5 high'

# ---------------------------------------------------------------- the code sets (decision 20)
# JavaScript for each listing, translated by the AI from ODS's Java line for line (same names, same order; `this.`
# for a field; Java's integer n/2 as Math.floor). balance() is translated from ODS's C++, since the Java version
# leans on java.util's List (subList, Collections.reverse) and the C++ one on arrays alone.
CODE_TRANSLATIONS = {
    'ods/ArrayDeque.a.j.n': '''
a;
j;
n;
''',
    'ods/ArrayDeque.get(i).set(i,x)': '''
get(i) {
    return this.a[(this.j+i)%this.a.length];
}

set(i, x) {
    const y = this.a[(this.j+i)%this.a.length];
    this.a[(this.j+i)%this.a.length] = x;
    return y;
}
''',
    'ods/ArrayDeque.add(i,x)': '''
add(i, x) {
    if (this.n+1 > this.a.length) this.resize();
    if (i < Math.floor(this.n/2)) { // shift a[0],..,a[i-1] left one position
        this.j = (this.j == 0) ? this.a.length - 1 : this.j - 1; //(j-1)mod a.length
        for (let k = 0; k <= i-1; k++)
            this.a[(this.j+k)%this.a.length] = this.a[(this.j+k+1)%this.a.length];
    } else { // shift a[i],..,a[n-1] right one position
        for (let k = this.n; k > i; k--)
            this.a[(this.j+k)%this.a.length] = this.a[(this.j+k-1)%this.a.length];
    }
    this.a[(this.j+i)%this.a.length] = x;
    this.n++;
}
''',
    'ods/ArrayDeque.remove(i)': '''
remove(i) {
    const x = this.a[(this.j+i)%this.a.length];
    if (i < Math.floor(this.n/2)) {  // shift a[0],..,[i-1] right one position
        for (let k = i; k > 0; k--)
            this.a[(this.j+k)%this.a.length] = this.a[(this.j+k-1)%this.a.length];
        this.j = (this.j + 1) % this.a.length;
    } else { // shift a[i+1],..,a[n-1] left one position
        for (let k = i; k < this.n-1; k++)
            this.a[(this.j+k)%this.a.length] = this.a[(this.j+k+1)%this.a.length];
    }
    this.n--;
    if (3*this.n < this.a.length) this.resize();
    return x;
}
''',
    'ods/ArrayDeque.resize()': '''
resize() {
    const b = new Array(Math.max(2*this.n, 1));
    for (let k = 0; k < this.n; k++)
        b[k] = this.a[(this.j+k) % this.a.length];
    this.a = b;
    this.j = 0;
}
''',
    'ods/DualArrayDeque.front.back': '''
front;
back;
''',
    'ods/DualArrayDeque.size()': '''
size() {
    return this.front.size() + this.back.size();
}
''',
    'ods/DualArrayDeque.get(i).set(i,x)': '''
get(i) {
    if (i < this.front.size()) {
        return this.front.get(this.front.size()-i-1);
    } else {
        return this.back.get(i-this.front.size());
    }
}

set(i, x) {
    if (i < this.front.size()) {
        return this.front.set(this.front.size()-i-1, x);
    } else {
        return this.back.set(i-this.front.size(), x);
    }
}
''',
    'ods/DualArrayDeque.add(i,x)': '''
add(i, x) {
    if (i < this.front.size()) {
        this.front.add(this.front.size()-i, x);
    } else {
        this.back.add(i-this.front.size(), x);
    }
    this.balance();
}
''',
    'ods/DualArrayDeque.remove(i)': '''
remove(i) {
    let x;
    if (i < this.front.size()) {
        x = this.front.remove(this.front.size()-i-1);
    } else {
        x = this.back.remove(i-this.front.size());
    }
    this.balance();
    return x;
}
''',
    'ods/DualArrayDeque.balance()': '''
balance() {
    if (3*this.front.size() < this.back.size()
            || 3*this.back.size() < this.front.size()) {
        const n = this.front.size() + this.back.size();
        const nf = Math.floor(n/2);
        const af = new Array(Math.max(2*nf, 1));
        for (let i = 0; i < nf; i++) {
            af[nf-i-1] = this.get(i);
        }
        const nb = n - nf;
        const ab = new Array(Math.max(2*nb, 1));
        for (let i = 0; i < nb; i++) {
            ab[i] = this.get(nf+i);
        }
        this.front.a = af;
        this.front.n = nf;
        this.back.a = ab;
        this.back.n = nb;
    }
}
''',
}

# the listings each Sim's panel holds: printed there, where the source figure and the listing stood, not again
IN_PANEL = {'ods/ArrayDeque.add(i,x)', 'ods/DualArrayDeque.add(i,x)'}


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
    """Every \\codeimport as a code set, except each class's add(i,x), which its Sim's panel holds (plan, question 3);
    the pseudocode edition prints no \\javaimport or \\cppimport here."""
    if e['cmd'] != 'codeimport' or e['ref'] in IN_PANEL:
        return ''
    return _code_set(listing(e['ref']))


# ---------------------------------------------------------------- the figures' original captions, as plain text

CAPTIONS = read_latex.figure_captions(os.path.join(_BOOK, ARRAYS), 2, 'ods')


def plain(t):
    """A caption for an attribute (root item 19: no maths in an attribute): $\\mathrm{add}(i,x)$ as add(i,x)."""
    return re.sub(r'\$([^$]*)\$', lambda m: re.sub(r'\\math(?:rm|it)\{([^}]*)\}', r'\1', m.group(1)), t)


ORIGINAL_ARRAYDEQUE = plain(CAPTIONS['arraydeque']['text'])
ORIGINAL_DUAL = plain(CAPTIONS['dualarraydeque']['text'])


# ---------------------------------------------------------------- figures and the derivation in the text

def sim(fid, caption, original=None, original_caption=None):
    attrs = f'class="sim" id="{fid}"'
    if original:
        attrs += f' data-original="{original}" data-original-caption="{html.escape(original_caption, quote=True)}"'
    return f'<figure {attrs}>\n  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>'


def R(rid, s=None):
    return f'<span data-ref="{rid}"><em>{s or rid}</em></span>'


def RC(rid):
    """A referent that is a code name (front, back): set as the code panel sets it."""
    return f'<span data-ref="{rid}"><code>{rid}</code></span>'


SIM_ARRAYDEQUE = (
    f'ODS’s ArrayDeque keeps the list in a circular array {R("a")}: list position <em>k</em> sits at '
    f'{R("a")}[({R("j")} + <em>k</em>) mod length({R("a")})], so the list can run past the last cell and on from cell 0. '
    f'add({R("i")}, x) and remove({R("i")}) shift whichever side of position {R("i")} is shorter, and step {R("j")} '
    f'back or forward a cell when they shift the front part, so a call shifts at most '
    f'<span data-type="cost">min({R("i")}, {R("n")} − {R("i")})</span> elements. At either end nothing shifts; in the '
    f'middle about {R("n")}/2 elements move every time. When {R("a")} is full, resize() copies the list, from '
    f'{R("a")}[{R("j")}] on, into the start of a new array {R("b")} twice as long, and sets {R("j")} to 0.'
)

SIM_DUAL = (
    f'ODS’s DualArrayDeque keeps the list in two ArrayStacks back to back: {RC("front")} holds list positions 0 to '
    f'front.size() − 1 in reverse order, so that both stacks grow outward from the middle, and {RC("back")} holds the '
    f'rest. Each call adds or removes in the stack that holds position {R("i")}. When one stack holds more than three '
    f'times as many elements as the other, balance() copies every element into two new stacks of ⌊{R("n")}/2⌋ and '
    f'⌈{R("n")}/2⌉. The potential <span data-type="cost">Φ</span> = |front.size() − back.size()| is at most 1 just '
    f'after a balance and rises by at most 1 a call, so the calls since the last balance are never fewer than '
    f'<span data-type="cost">Φ − Φ₀</span>, and more than {R("n")}/2 − 1 by the time the next one comes. Adding at the '
    f'back keeps triggering balances; adding at the two ends in turn never needs one.'
)

HTML = {
    'sim-arraydeque': sim('sim-arraydeque', SIM_ARRAYDEQUE, '/media/ch03/ods-arraydeque.png', ORIGINAL_ARRAYDEQUE),
    'sim-dualarraydeque': sim('sim-dualarraydeque', SIM_DUAL, '/media/ch03/ods-dualarraydeque.png', ORIGINAL_DUAL),
    'drv-balance-potential': '<figure class="dv" id="drv-balance-potential"></figure>',
}


# ---------------------------------------------------------------- marks

def _fn(nid):
    return f'<sup class="fn" data-note="{nid}"></sup>'


def _refmath(tex, letters):
    """A maths run with the figure's referents marked: a lone letter (not one inside a name such as
    \\mathrm{length} or a command such as \\bmod), and \\mathit{front} or \\mathit{back}."""
    t = re.sub(r'\\mathit\{(front|back)\}', lambda m: '\\htmlData{ref=' + m.group(1) + '}{\\mathit{' + m.group(1) + '}}', tex)
    if letters:
        # an escaped brace (\\min\\{i, …\\}) is a brace of the maths, not of a name: it is set aside first
        t = t.replace('\\{', '\x01').replace('\\}', '\x02')
        t = re.sub(r'(?<![\\A-Za-z{])([' + letters + r'])(?![A-Za-z}])',
                   lambda m: '\\htmlData{ref=' + m.group(1) + '}{' + m.group(1) + '}', t)
        t = t.replace('\x01', '\\{').replace('\x02', '\\}')
    return t


def _block_maths(bid):
    """The inline maths of a block as the reader prints them, once each (for the referent marks)."""
    b = next(x for x in BLOCKS if x['id'] == bid)
    hs, *_ = read_latex.passage(os.path.join(_BOOK, b['file']), *b['parts'][0], b['chapter'], 'ods', refs=LATEX_REFS)
    seen = []
    for h in hs:
        if h.startswith('$$'):
            continue
        for m in re.findall(r'\$[^$]+\$', h):
            if m not in seen:
                seen.append(m)
    return seen


# the referents each block's maths names (plan, Referents): ArrayDeque's a, i, j, n; DualArrayDeque's front, back,
# i and n
_REF_LETTERS = {'arraydeque': 'aijn', 'dualarraydeque': 'in'}

MARKS = [
    # concepts: the span that introduces each (plan, Concepts), and the mentions of the potential method
    ('deque', 'A Deque is a generalization of both the FIFO Queue and LIFO Queue (Stack).',
     '<span data-concept="deque">A Deque is a generalization of both the FIFO Queue and LIFO Queue (Stack).</span>'),
    ('arraydeque', 'The ArrayDeque data structure allows for efficient addition and removal at both ends.',
     '<span data-concept="array-deque">The ArrayDeque data structure allows for efficient addition and removal at both ends.</span>'),
    ('dualarraydeque', 'back-to-back so that operations are fast at either end',
     '<span data-concept="dual-array-deque">back-to-back so that operations are fast at either end</span>'),
    ('dualarraydeque', '<em>potential method</em>', '<span data-concept="potential-method"><em>potential method</em></span>'),
    # ODS's "the previous section" is 3.2's ArrayQueue (book RULES, Cross-references: the source's words, linked)
    ('arraydeque', 'from the previous section',
     'from <a href="/cs-interview-prep-ultra/ch03/3.2/#arrayqueue">the previous section</a>'),
    # corrections (plan, Errata)
    # (each 'plain': the blocks' maths hold a bare <, which outside_tags would read as a tag)
    ('arraydeque', 'left by one position. Otherwise', 'left by one position.' + _fn('err-positions') + ' Otherwise', 1, 'plain'),
    ('arraydeque', 'and $\\mathrm{remove}(x)$ operations', 'and $\\mathrm{remove}(x)$' + _fn('err-remove-x') + ' operations', 1, 'plain'),
    ('arraydeque', 'elements. Thus, the running', 'elements.' + _fn('err-half') + ' Thus, the running', 1, 'plain'),
    ('dualarraydeque', '$\\mathrm{front.add}(\\mathrm{front.size}()-i-1,x)$.',
     '$\\mathrm{front.add}(\\mathrm{front.size}()-i-1,x)$.' + _fn('err-front-add'), 1, 'plain'),
    ('dualarraydeque', 'a technique knows as', 'a technique knows as' + _fn('err-knows'), 1, 'plain'),
    # the words between the two displays drv-balance-potential replaces (root item 29.2; its steps carry them)
    ('dualarraydeque', '<p>Furthermore, the potential at this point in time is</p>\n', ''),
]
for _bid, _letters in _REF_LETTERS.items():
    for _m in _block_maths(_bid):
        _t = _refmath(_m, _letters)
        if _t != _m:
            MARKS.append((_bid, _m, _t, 40, 'plain'))


# ---------------------------------------------------------------- the derivation

_F, _B = '\\mathrm{front.size}()', '\\mathrm{back.size}()'
DRV = {
    'id': 'balance-potential',
    'what': 'the potential just before a balance that shifts elements',
    'source': 'Open Data Structures, 2.4.3 Balancing, the proof of Lemma 2.2',
    'nodes': [
        {
            'assumes': [
                {'tex': f'n = {_F} + {_B}', 'src': '2.4 DualArrayDeque'},
                {'tex': f'3{_F} < {_B}', 'src': 'Lemma 2.2, proof'},
            ],
            'then': {'tex': f'\\mk{{n}}{{n}} = \\mk{{f}}{{{_F}}} + \\mk{{b}}{{{_B}}}', 'uses': []},
            'steps': [
                {'tex': f'\\mk{{n}}{{n}} < \\mk{{f}}{{{_B}/3}} + \\mk{{b}}{{{_B}}}', 'uses': [1],
                 'cap': 'Dividing $3\\mathrm{front.size}() < \\mathrm{back.size}()$ by 3 bounds $\\mathrm{front.size}()$ by $\\mathrm{back.size}()/3$.'},
                {'tex': f'\\mk{{n}}{{n}} < \\mk{{b}}{{\\frac{{4}}{{3}}{_B}}}', 'uses': [], 'map': {'f': 'b'}},
            ],
            'src': 'Lemma 2.2, proof',
        },
        {
            'assumes': [
                {'tex': f'\\Phi_1 = {_B} - {_F}', 'src': 'Lemma 2.2, proof'},
                {'tex': f'3{_F} < {_B}', 'src': 'Lemma 2.2, proof'},
                {'step': 0},
            ],
            'then': {'tex': f'\\mk{{p}}{{\\Phi_1}} = \\mk{{b}}{{{_B}}} - \\mk{{f}}{{{_F}}}', 'uses': [],
                     'why': 'With $3\\mathrm{front.size}() < \\mathrm{back.size}()$, $\\mathit{back}$ is the larger stack, so the absolute value in $\\Phi$ opens this way.'},
            'steps': [
                {'tex': f'\\mk{{p}}{{\\Phi_1}} > \\mk{{b}}{{{_B}}} - \\mk{{f}}{{{_B}/3}}', 'uses': [1],
                 'cap': 'Taking away less than $\\mathrm{back.size}()/3$ leaves more than taking away $\\mathrm{back.size}()/3$.'},
                {'tex': f'\\mk{{p}}{{\\Phi_1}} > \\mk{{b}}{{\\frac{{2}}{{3}}{_B}}}', 'uses': [], 'map': {'f': 'b'}},
                {'tex': f'\\mk{{p}}{{\\Phi_1}} > \\mk{{b}}{{\\frac{{2}}{{3}}\\times\\frac{{3}}{{4}}n}}', 'uses': [2],
                 'cap': 'From $n < \\frac{4}{3}\\mathrm{back.size}()$, $\\mathrm{back.size}() > \\frac{3}{4}n$.'},
                {'tex': '\\mk{p}{\\Phi_1} > \\mk{b}{n/2}', 'uses': []},
            ],
            'src': 'Lemma 2.2, proof',
        },
    ],
}


def check_derivations():
    """Every line holds, in exact arithmetic, for every pair of sizes with 3·front.size() < back.size() up to 400."""
    from fractions import Fraction as Fr
    for b in range(1, 401):
        for f in range(0, b):
            if not 3 * f < b:
                continue
            n, b_, f_ = Fr(f + b), Fr(b), Fr(f)
            assert n == f_ + b_ and n < b_ / 3 + b_ and n < Fr(4, 3) * b_
            phi = abs(f_ - b_)
            assert phi == b_ - f_ and phi > b_ - b_ / 3 and phi > Fr(2, 3) * b_
            assert b_ > Fr(3, 4) * n and Fr(2, 3) * b_ > Fr(2, 3) * Fr(3, 4) * n
            assert phi > Fr(2, 3) * Fr(3, 4) * n == n / 2
    return True


# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]

LEAD = ('An Essential section on the <span data-concept="deque">deque</span>, a sequence that grows and shrinks at both '
        'ends, and on two ways to keep one in arrays; the <span data-concept="dual-array-deque">DualArrayDeque</span> is '
        'Advanced. Lists are indexed from 0. ODS’s “LIFO Queue” is the stack of '
        '<a href="/cs-interview-prep-ultra/ch03/3.1/">Section 3.1</a>. Its lemma on balance() uses '
        '<a href="/cs-interview-prep-ultra/ch01/1.5/#potential">Section 1.5</a>’s '
        '<span data-concept="potential-method">potential method</span> as a counter: each call that does not rebalance '
        'raises Φ by at most 1, so the calls before a costly balance() pay for it.')

FOOTNOTES = [
    {'id': 'err-positions', 'kind': 'correction',
     'html': 'Here $a[0],\\ldots,a[i-1]$ name the list’s first $i$ elements, not the array’s first cells: they sit at '
             '$a[j],\\ldots,a[(j+i-1)\\bmod \\mathrm{length}(a)]$, where $\\mathrm{get}(i)$ above finds them. The same holds '
             'for $a[i],\\ldots,a[n-1]$ in this paragraph and for the ranges named in the paragraph on $\\mathrm{remove}(i)$.'},
    {'id': 'err-remove-x', 'kind': 'correction',
     'html': 'The second operation is $\\mathrm{remove}(i)$, as the figure’s own caption says.'},
    {'id': 'err-half', 'kind': 'correction',
     'html': 'This holds where $n/2$ is the real quotient, as here and in the Python listing, whose $\\mathtt{/}$ divides '
             'exactly. ODS’s Java and C++ listings divide $n$ by 2 in whole numbers, so when $n$ is odd and $i=(n-1)/2$ they '
             'shift $a[i],\\ldots,a[n-1]$ right, $(n+1)/2$ elements, one more than $\\min\\{i,n-i\\}$; Figure 2.3’s last step, '
             '$\\mathrm{add}(4,z)$ with $n=9$, is such a case, and it shifts left as the prose says. The bound '
             '$O(1+\\min\\{i,n-i\\})$ holds either way.'},
    {'id': 'err-front-add', 'kind': 'correction',
     'html': 'The code calls $\\mathrm{front.add}(\\mathrm{front.size}()-i,x)$. List position $i$ is $\\mathit{front}$’s '
             'element $\\mathrm{front.size}()-i-1$, and $x$, which comes before it in the list, goes after it in '
             '$\\mathit{front}$’s reversed order, at $\\mathrm{front.size}()-i$. With $\\mathrm{front.size}()-i-1$, adding at '
             'position 1 of $a,b,c$ held in $\\mathit{front}$ would give $a,b,x,c$. The cost (2.1) is $O(i+1)$ either way.'},
    {'id': 'err-knows', 'kind': 'correction', 'html': 'Read “known as”.'},
]

SECTION = {
    'id': '3.3', 'chapter': '3', 'title': 'Deques', 'short': 'Deques',
    'lead': LEAD,
    'objectives': [], 'summary_html': '',
    'notes': ('The other paragraphs of ODS’s subsection on the Queue, Stack and Deque interfaces are left out here, the '
              'FIFO Queue being Section 3.2’s, and so are ODS’s exercises, which have no published answers.'),
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'Exercism’s linked-list, held from Section 2.6, is a doubly linked deque: its tests are the canonical data’s, '
        'played by a small driver in the starter, less the case on deleting a value that is not there, which the Python '
        'track drops and answers with an error; its Python reference is the Python track’s example and its JavaScript '
        'reference the AI’s. Kattis’s Integer Lists has a sample only, so its other tests and both references are the '
        'AI’s, checked against a direct simulation. MIT 6.006’s Problem Session 1, problem 1-3, held from Section 2.2, '
        'is in exercises-nc.json, keyed by a link to MIT’s worked solution. ODS Exercises 2.6, 2.8 and 2.9, and Exercise '
        '2.7 held from Section 2.2, have no tests of their own and are left out, as are SICP’s Exercise 3.23 (written, '
        'for Scheme), the unkeyed pythonds exercises and Kattis’s teque; ODS’s test_arraydeque.py and '
        'test_dualarraydeque.py, trekhleb’s deque tests and TheAlgorithms’ double_ended_queue.py are tests with no '
        'printed statement.'),
    'figures': [
        {'id': 'sim-arraydeque', 'kind': 'sim', 'originals': ['/media/ch03/ods-arraydeque.png'],
         'original_caption': ORIGINAL_ARRAYDEQUE, 'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
        {'id': 'sim-dualarraydeque', 'kind': 'sim', 'originals': ['/media/ch03/ods-dualarraydeque.png'],
         'original_caption': ORIGINAL_DUAL, 'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'a', 'label': 'a, the ArrayDeque’s circular array', 'figures': ['sim-arraydeque']},
        {'id': 'b', 'label': 'b, the array resize() fills', 'figures': ['sim-arraydeque']},
        {'id': 'j', 'label': 'j, the cell that holds list position 0', 'figures': ['sim-arraydeque']},
        {'id': 'n', 'label': 'n, the number of elements', 'figures': ['sim-arraydeque', 'sim-dualarraydeque']},
        {'id': 'i', 'label': 'i, the list position a call names', 'figures': ['sim-arraydeque', 'sim-dualarraydeque']},
        {'id': 'front', 'label': 'front, the ArrayStack that holds the first part of the list, reversed', 'figures': ['sim-dualarraydeque']},
        {'id': 'back', 'label': 'back, the ArrayStack that holds the rest of the list', 'figures': ['sim-dualarraydeque']},
    ],
    'coverage': [
        {'span': 'deque', 'concept': 'deque', 'verb': 'introduces'},
        {'span': 'arraydeque', 'concept': 'array-deque', 'verb': 'introduces'},
        {'span': 'arraydeque', 'concept': 'deque', 'verb': 'uses'},
        {'span': 'arraydeque', 'concept': 'list-interface', 'verb': 'uses'},
        {'span': 'dualarraydeque', 'concept': 'dual-array-deque', 'verb': 'introduces'},
        {'span': 'dualarraydeque', 'concept': 'deque', 'verb': 'uses'},
        {'span': 'dualarraydeque', 'concept': 'dynamic-array', 'verb': 'uses'},
        {'span': 'dualarraydeque', 'concept': 'dynamic-array-cost', 'verb': 'uses'},
        {'span': 'dualarraydeque', 'concept': 'potential-method', 'verb': 'uses'},
        {'span': 'dualarraydeque', 'concept': 'array-deque', 'verb': 'uses'},
    ],
    'footnotes_extra': FOOTNOTES,
    'derivations': [DRV],
}


def lead_words():
    return len(re.sub(r'<[^>]+>', '', LEAD).split())


# ---------------------------------------------------------------- exercises (tools/build_section.py calls EXERCISES)

EXERCISM = 'sources/_cache/exercism/exercises/linked-list'
EXERCISM_PY = 'sources/_cache/exercism-python/exercises/practice/linked-list'
KATTIS_HTML = 'sources/_cache/kattis/problems/integerlists.html'
KATTIS_SAMPLES = 'sources/_cache/kattis/samples/integerlists.zip'
# the canonical case the Python track leaves out (it raises ValueError where the canonical data expects nothing)
NOT_FOUND_CASE = '7b420958-f285-4922-b8f9-10d9dcab5179'

RUN_PY = '''

def run(ops):
    """Given: plays a test's operations on a LinkedList and returns, in order, what each checked pop, shift and count
    gives; an operation marked "unchecked" is made and its value not reported."""
    lst, out = LinkedList(), []
    for op, *args in ops:
        if op == 'count':
            out.append(len(lst))
        elif args == ['unchecked']:
            getattr(lst, op)()
        elif op in ('pop', 'shift'):
            out.append(getattr(lst, op)())
        else:
            getattr(lst, op)(*args)
    return out
'''

STARTER_JS = '''class Node {
    constructor(value, next = null, prev = null) {
    }
}

class LinkedList {
    constructor() {
    }

    push(value) {
    }

    pop() {
    }

    shift() {
    }

    unshift(value) {
    }

    delete(value) {
    }

    count() {
    }
}
'''

REF_JS = '''class Node {
    constructor(value, next = null, prev = null) {
        this.value = value;
        this.next = next;
        this.prev = prev;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(value) {
        const node = new Node(value, null, this.tail);
        if (this.tail) this.tail.next = node; else this.head = node;
        this.tail = node;
        this.length++;
    }

    pop() {
        const node = this.tail;
        this.tail = node.prev;
        if (this.tail) this.tail.next = null; else this.head = null;
        this.length--;
        return node.value;
    }

    shift() {
        const node = this.head;
        this.head = node.next;
        if (this.head) this.head.prev = null; else this.tail = null;
        this.length--;
        return node.value;
    }

    unshift(value) {
        const node = new Node(value, this.head, null);
        if (this.head) this.head.prev = node; else this.tail = node;
        this.head = node;
        this.length++;
    }

    delete(value) {
        for (let node = this.head; node; node = node.next) {
            if (node.value === value) {
                if (node.prev) node.prev.next = node.next; else this.head = node.next;
                if (node.next) node.next.prev = node.prev; else this.tail = node.prev;
                this.length--;
                return;
            }
        }
    }

    count() {
        return this.length;
    }
}
'''

RUN_JS = '''
// Given: plays a test's operations on a LinkedList and returns, in order, what each checked pop, shift and count
// gives; an operation marked "unchecked" is made and its value not reported.
function run(ops) {
    const lst = new LinkedList(), out = [];
    for (const [op, ...args] of ops) {
        if (op === 'count') out.push(lst.count());
        else if (args.length === 1 && args[0] === 'unchecked') lst[op]();
        else if (op === 'pop' || op === 'shift') out.push(lst[op]());
        else lst[op](...args);
    }
    return out;
}
'''


def exercism_tests(book):
    """The canonical cases as run(ops) tests: an operation with an expected value is reported, one without is
    "unchecked"; the not-found case is left out (plan, Exercises)."""
    import json
    data = json.load(open(os.path.join(book, EXERCISM, 'canonical-data.json'), encoding='utf-8'))
    tests = []
    for c in data['cases']:
        if c['uuid'] == NOT_FOUND_CASE:
            continue
        ops, expect = [], []
        for o in c['input']['operations']:
            name = o['operation']
            if 'value' in o:
                ops.append([name, o['value']])
            elif 'expected' in o:
                ops.append([name])
                expect.append(o['expected'])
            else:
                ops.append([name, 'unchecked'])
        tests.append({'args': [ops], 'expect': expect, 'visible': len(tests) < 2, 'generated_by': 'source'})
    return tests


def exercism_prompt(book):
    """The problem specification's introduction and instructions, its paragraphs as the card's prompt; the
    instructions' closing note on linked lists in general, with its link, is left out (changes says so)."""
    out = []
    for f in ('introduction.md', 'instructions.md'):
        t = open(os.path.join(book, EXERCISM, f), encoding='utf-8').read()
        t = re.sub(r'~~~~exercism/note.*?~~~~', '', t, flags=re.S)
        t = re.sub(r'^# .*\n', '', t)
        for p in re.split(r'\n\s*\n', t.strip()):
            p = ' '.join(p.split())
            if p:
                p = html.escape(p, quote=False).replace('$', '＄')
                out.append(re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', p))
    return '\n\n'.join(out)


# ---- Kattis Integer Lists (CC BY-SA 3.0): the statement from the cached page, the sample, AI tests

KATTIS_PY = '''import sys
from collections import deque


def main():
    data = sys.stdin.read().split()
    t, pos, out = int(data[0]), 1, []
    for _ in range(t):
        program, n, text = data[pos], int(data[pos + 1]), data[pos + 2]
        pos += 3
        xs = deque(int(v) for v in text[1:-1].split(',')) if n else deque()
        reversed_, ok = False, True
        for c in program:
            if c == 'R':
                reversed_ = not reversed_          # reverse lazily: remember which end is the front
            elif not xs:
                ok = False
                break
            elif reversed_:
                xs.pop()
            else:
                xs.popleft()
        if not ok:
            out.append('error')
            continue
        if reversed_:
            xs.reverse()
        out.append('[' + ','.join(map(str, xs)) + ']')
    print('\\n'.join(out))


main()
'''

KATTIS_JS = '''const data = require('fs').readFileSync(0, 'utf8').split(/\\s+/).filter(Boolean);
let pos = 1;
const out = [];
for (let t = Number(data[0]); t > 0; t--) {
    const program = data[pos], n = Number(data[pos + 1]), text = data[pos + 2];
    pos += 3;
    const xs = n ? text.slice(1, -1).split(',').map(Number) : [];
    // the list between two ends, front and back; R swaps which end is the front
    let lo = 0, hi = xs.length, reversed = false, ok = true;
    for (const c of program) {
        if (c === 'R') reversed = !reversed;
        else if (lo === hi) { ok = false; break; }
        else if (reversed) hi--;
        else lo++;
    }
    if (!ok) { out.push('error'); continue; }
    const rest = xs.slice(lo, hi);
    if (reversed) rest.reverse();
    out.push('[' + rest.join(',') + ']');
}
console.log(out.join('\\n'));
'''

KATTIS_STARTER_PY = 'import sys\n\ndata = sys.stdin.read().split()\n'
KATTIS_STARTER_JS = "const data = require('fs').readFileSync(0, 'utf8').split(/\\s+/).filter(Boolean);\n"

# a worst case of size n: one list of n elements and a program of n letters, R and D in turn, so a solution that
# reverses the list at every R does about n²/4 steps
KATTIS_GROW = ("(n, rand) => { const xs = Array.from({ length: n }, () => 1 + rand.int(0, 99)); "
               "return '1\\n' + 'RD'.repeat(Math.max(1, n >> 1)) + '\\n' + n + '\\n[' + xs.join(',') + ']\\n'; }")


def kattis_brute(stdin):
    """What a test's output must be, by doing what the statement says: reverse the list at every R, drop its first
    element at every D (used to write and check the AI tests, never shipped)."""
    data = stdin.split()
    t, pos, out = int(data[0]), 1, []
    for _ in range(t):
        p, n, s = data[pos], int(data[pos + 1]), data[pos + 2]
        pos += 3
        xs = [int(v) for v in s[1:-1].split(',')] if n else []
        err = False
        for c in p:
            if c == 'R':
                xs = xs[::-1]
            elif not xs:
                err = True
                break
            else:
                xs = xs[1:]
        out.append('error' if err else '[' + ','.join(map(str, xs)) + ']')
    return '\n'.join(out) + '\n'


def _case(p, xs):
    return f'{p}\n{len(xs)}\n[' + ','.join(map(str, xs)) + ']\n'


def kattis_ai_inputs():
    """The AI tests' inputs: what the statement implies (an empty list, D on it, R alone, an even and an odd number of
    R, a program longer than the list, an error followed by a good case), and two larger cases, fixed by a seed."""
    import random
    rnd = random.Random(33)
    big = [rnd.randint(1, 100) for _ in range(3000)]
    prog = ''.join(rnd.choice('RRD') for _ in range(4000))
    mid = [rnd.randint(1, 100) for _ in range(200)]
    return [
        '1\n' + _case('R', []),
        '1\n' + _case('RRRR', [1, 2, 3]),
        '1\n' + _case('R', [5, 6, 7]),
        '2\n' + _case('DRD', [1, 2, 3, 4]) + _case('DDD', [9, 8, 7]),
        '3\n' + _case('DDDD', [1, 2, 3]) + _case('RDRDR', [3, 1, 4, 1, 5, 9, 2, 6]) + _case('D', [100]),
        '1\n' + _case('RRRRRRRRRRRRRRRRRRRRD', [42, 7]),
        '2\n' + _case('D' * 200 + 'R', mid) + _case('RD' * 100, mid),
        '1\n' + _case(prog, big),
    ]


def _kattis_prompt(book):
    """The statement as the card's prompt: its paragraphs, its Input and Output headings and lists, its maths as $…$,
    tt as code; the sample table is the card's visible test."""
    s = open(os.path.join(book, KATTIS_HTML), encoding='utf-8').read()
    body = s[s.index('<div class="problembody">'):]
    body = body[:body.index('<table class="sample"')]
    body = re.sub(r'<span class=\s*"tex2jax_process">(.*?)</span>', lambda m: m.group(1), body, flags=re.S)
    out = []
    for m in re.finditer(r'<h2>(.*?)</h2>|<ul class="itemize">(.*?)</ul>|<p>(.*?)</p>', body, flags=re.S):
        def clean(t):
            t = ' '.join(html.unescape(t).split())
            t = re.sub(r'(\d)\\, (\d)', r'\1\\,\2', t)        # "100\, 000" as one number, as the statement sets it
            t = t.replace('<tt>', '<code>').replace('</tt>', '</code>')
            # a < inside maths is written \lt, so that no bare < stands in the prompt
            t = re.sub(r'\$([^$]*)\$', lambda mm: '$' + mm.group(1).replace('<', '\\lt ') + '$', t)
            return t.replace('"', '”')
        if m.group(1):
            out.append(f'<strong>{clean(m.group(1))}</strong>')
        elif m.group(2):
            items = [clean(x) for x in re.findall(r'<li>\s*<p>(.*?)</p>\s*</li>', m.group(2), flags=re.S)]
            out.append('<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>')
        elif m.group(3) is not None and not m.group(0).startswith('<p>\n      ') or m.group(3):
            # a paragraph inside a list item was taken with its list
            if m.start() and '<li>' in body[max(0, m.start() - 40):m.start()]:
                continue
            out.append(clean(m.group(3)))
    return '\n\n'.join(out)


def _sample(book):
    import zipfile
    z = zipfile.ZipFile(os.path.join(book, KATTIS_SAMPLES))
    names = sorted(z.namelist())
    return z.read(next(n for n in names if n.endswith('.in'))).decode(), z.read(next(n for n in names if n.endswith('.ans'))).decode()


def EXERCISES(exercism_code, book):
    ref_py = open(os.path.join(book, EXERCISM_PY, '.meta/example.py'), encoding='utf-8').read().rstrip() + '\n'
    stub_py = open(os.path.join(book, EXERCISM_PY, 'linked_list.py'), encoding='utf-8').read().rstrip() + '\n'
    c1 = {
        'id': 'c1', 'source_id': 'exercism:linked-list', 'source_number': 'linked-list', 'origin': 'exercism',
        'kind': 'code', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'deque',
        'changes': ('Your LinkedList provides push, pop, shift, unshift, delete and len (count() in JavaScript); the tests '
                    'are the canonical data’s operations, played by the run(ops) the starter gives, less the case on '
                    'deleting a value that is not in the list. The specification’s note on linked lists in general is '
                    'left out.'),
        'prompt': exercism_prompt(book),
        'answer': {
            'type': 'code',
            'python': {'entry': 'run', 'starter': stub_py + RUN_PY, 'reference': ref_py + RUN_PY, 'generated_by': 'source'},
            'javascript': {'entry': 'run', 'starter': STARTER_JS + RUN_JS, 'reference': REF_JS + RUN_JS, 'generated_by': 'ai'},
            'tests': exercism_tests(book), 'generated_by': 'source'},
    }
    sin, sout = _sample(book)
    tests = [{'stdin': sin, 'stdout': sout, 'visible': True, 'generated_by': 'source'}]
    for k, stdin in enumerate(kattis_ai_inputs()):
        tests.append({'stdin': stdin, 'stdout': kattis_brute(stdin), 'visible': k == 0, 'generated_by': 'ai'})
    c2 = {
        'id': 'c2', 'source_id': 'kattis:integerlists', 'source_number': 'Integer Lists', 'origin': 'kattis-by-sa',
        'kind': 'code', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'deque',
        'changes': ('Only the sample is the source’s; the other tests are written for this book from the statement, and a '
                    'solution must take time linear in the input.'),
        'prompt': _kattis_prompt(book),
        'answer': {
            'type': 'code',
            'python': {'starter': KATTIS_STARTER_PY, 'reference': KATTIS_PY, 'generated_by': 'ai'},
            'javascript': {'starter': KATTIS_STARTER_JS, 'reference': KATTIS_JS, 'generated_by': 'ai'},
            'tests': tests, 'compare': 'tokens', 'bound': 'n', 'grow': KATTIS_GROW, 'generated_by': 'ai'},
    }
    concepts = [{'exercise': 'c1', 'concept': 'deque'}, {'exercise': 'c1', 'concept': 'doubly-linked-list'},
                {'exercise': 'c2', 'concept': 'deque'}]
    return [c1, c2], concepts
