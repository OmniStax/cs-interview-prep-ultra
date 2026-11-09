"""What tools/build_text.py needs to assemble 3.6 Space-efficient lists (the plan is plan.md beside this file).

Everything here is placement, markup or what the plan decided; the source's words come from the converters.
ODS's prose is its pseudocode edition (METHOD decision 20), read by tools/read_latex.py (dialect `ods`), except the
block `rootish-sqrt`, "Computing Square Roots", which only the Java and C++ editions print: it is read the same way
with the edition switch `notpcode` on (plan, question 1). ODS's listings are four-language code sets: Python, Java
and C++ read from ODS's own sources by tools/ods_listing.py as the editions print them (printed=True), JavaScript
translated by the AI from the Java (CODE_TRANSLATIONS) and AI-marked. Two kinds of Python are the AI's too, and
marked: RootishArrayStack's listings that divide an integer with `/` (a float index in Python 3) carry the
mechanical port `//` (judgements/ch01-03-references.md); FastSqrt, which ODS writes in Java and C++ only, is
translated from the Java (PY_TRANSLATIONS). No FIXES table: the reader's output needs no correction.
"""
import html
import os
import re
import sys

_BOOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(_BOOK, 'tools'))
import ods_listing  # noqa: E402
import read_latex  # noqa: E402

TITLE = 'Space-efficient lists'
ARRAYS = 'sources/_cache/ods/latex/arrays.tex'
LISTS = 'sources/_cache/ods/latex/linkedlists.tex'
_A = dict(source='ods', reader='latex', dialect='ods', file=ARRAYS, chapter=2)
_L = dict(source='ods', reader='latex', dialect='ods', file=LISTS, chapter=3)

BLOCKS = [
    dict(id='rootish', **_A, drop_first_heading=True, heading_shift=0,
         parts=[('\\section{#RootishArrayStack#', '\\subsection{Space Usage}')],
         locator='ods:arrays#sec:rootisharraystack, from the opening through “Analysis of Growing and Shrinking”',
         h2='RootishArrayStack: A Space-Efficient Array Stack'),
    dict(id='sqrt-lower-bound', **_A, drop_first_heading=True,
         parts=[('\\subsection{Space Usage}', '\\subsection{Summary}')],
         locator='ods:arrays#sec:rootishspaceusage', h2='Space Usage'),
    # the source's "Summary" does not name the concept, so the header is OmniStax's (plan, question 7)
    dict(id='rootish-summary', **_A,
         parts=[('The following theorem summarizes our discussion of the #RootishArrayStack#', '\\notpcode{')],
         locator='ods:arrays#sec:rootisharraystack, the subsection “Summary” (thm:rootisharraystack)',
         h2='RootishArrayStack: Summary'),
    # printed by the Java and C++ editions only (\notpcode): the edition switch on for this block alone
    dict(id='rootish-sqrt', **_A, drop_first_heading=True, edition={'notpcode': True},
         parts=[('\\subsection{Computing Square Roots}', '\\section{Discussion and Exercises}')],
         locator='ods:arrays#sec:rootisharraystack, the subsection “Computing Square Roots” (lem:root), printed in the '
                 'Java and C++ editions',
         h2='Computing Square Roots'),
    dict(id='selist', **_L, drop_first_heading=True, heading_shift=0,
         parts=[('\\section{#SEList#: A Space-Efficient Linked List}', '\\subsection{Amortized Analysis of Spreading')],
         locator='ods:linkedlists#sec:selist, from the opening through “Removing an Element”',
         h2='SEList: A Space-Efficient Linked List'),
    dict(id='selist-amortized', **_L, drop_first_heading=True,
         parts=[('\\subsection{Amortized Analysis of Spreading', '\\subsection{Summary}')],
         locator='ods:linkedlists#lem:selist-amortized, the subsection “Amortized Analysis of Spreading and Gathering”',
         h2='Amortized Analysis of Spreading and Gathering'),
    dict(id='selist-summary', **_L,
         parts=[('The following theorem summarizes the performance of the #SEList#', '\\section{Discussion and Exercises}')],
         locator='ods:linkedlists#sec:selist, the subsection “Summary” (thm:selist and the closing paragraph)',
         h2='SEList: Summary'),
]

_HERE = '/cs-interview-prep-ultra/ch03/3.6/'
# ODS's references, each the source's number linked to what carries it (RULES, Cross-references). The label
# `rootisharraystack` is ODS's section, figure and theorem at once, so the reader's own numbering cannot find it.
LATEX_REFS = {
    'figref:rootisharraystack': ('<a href="#sim-rootish">Figure 2.5</a>', 'Figure 2.5'),
    'figref:gauss': ('<a href="#sim-gauss">Figure 2.6</a>', 'Figure 2.6'),
    'figref:selist-add': ('<a href="#sim-selist-add">Figure 3.4</a>', 'Figure 3.4'),
    'figref:selist-remove': ('<a href="#sim-selist-remove">Figure 3.5</a>', 'Figure 3.5'),
    'lemref:root': ('<a href="#rootish-sqrt">Lemma 2.3</a>', 'Lemma 2.3'),
    'secref:model': ('<a href="/cs-interview-prep-ultra/ch01/1.4/#word-ram">Section 1.4</a>', 'Section 1.4'),
    'secref:arraydeque': ('<a href="/cs-interview-prep-ultra/ch03/3.3/#arraydeque">Section 3.3</a>', 'Section 3.3'),
    'secref:rootishspaceusage': (f'<a href="{_HERE}#sqrt-lower-bound">Section 3.6</a>', 'Section 3.6'),
}
FIGURE_AT = {'rootisharraystack': 'sim-rootish', 'gauss': 'sim-gauss',
             'selist-add': 'sim-selist-add', 'selist-remove': 'sim-selist-remove'}
# The printed displays the derivations replace (root item 29.2), by a piece of their TeX as printed.
REPLACE = [
    ('sqrt-lower-bound', '(#r#-2)(#r#-1)/2 \\le #n#', 'drv-rootish-blocks'),
    ('sqrt-lower-bound', '\\le \\frac{1}{2}\\left(3+\\sqrt{8#n#+1}\\right)', ''),
    ('rootish-sqrt', '\\sqrt{#x#-\\sqrt{#x#}} \\ge \\sqrt{#x#}-1', 'drv-root'),
    ('rootish-sqrt', '#x#-\\sqrt{#x#} \\ge #x#-2\\sqrt{#x#}+1', ''),
    ('rootish-sqrt', '\\sqrt{#x#} \\ge 1', ''),
]
# A derivation of a proof printed as prose stands after the paragraph that completes it (root item 29.2); the
# growth plot after the paragraph that bounds the wasted space.
AFTER_TEXT = {
    'sqrt-lower-bound': [('The last two blocks have sizes', 'sim-wasted-space'),
                         ('Suppose we start with an empty data structure', 'drv-sqrt-lower-bound')],
    'selist-amortized': [('In summary, the potential starts at 0', 'drv-selist-spread')],
}

AI = 'claude-opus-5-5 high'

# ---------------------------------------------------------------- the code

# JavaScript for each listing, translated by the AI from ODS's Java line for line (same names, same order), keyed
# by the listing's reference. Java's integer division is Math.floor or >> where its operands are ints.
CODE_TRANSLATIONS = {
    'ods/RootishArrayStack.blocks.n': '''
blocks;
n;
''',
    'ods/RootishArrayStack.i2b(i)': '''
i2b(i) {
    const db = (-3.0 + Math.sqrt(9 + 8*i)) / 2.0;
    const b = Math.ceil(db);
    return b;
}
''',
    'ods/RootishArrayStack.get(i).set(i,x)': '''
get(i) {
    const b = this.i2b(i);
    const j = i - b*(b+1)/2;
    return this.blocks.get(b)[j];
}

set(i, x) {
    const b = this.i2b(i);
    const j = i - b*(b+1)/2;
    const y = this.blocks.get(b)[j];
    this.blocks.get(b)[j] = x;
    return y;
}
''',
    'ods/RootishArrayStack.add(i,x)': '''
add(i, x) {
    const r = this.blocks.size();
    if (r*(r+1)/2 < this.n + 1) this.grow();
    this.n++;
    for (let j = this.n-1; j > i; j--)
        this.set(j, this.get(j-1));
    this.set(i, x);
}
''',
    'ods/RootishArrayStack.grow()': '''
grow() {
    this.blocks.add(new Array(this.blocks.size()+1));
}
''',
    'ods/RootishArrayStack.remove(i)': '''
remove(i) {
    const x = this.get(i);
    for (let j = i; j < this.n-1; j++)
        this.set(j, this.get(j+1));
    this.n--;
    const r = this.blocks.size();
    if ((r-2)*(r-1)/2 >= this.n) this.shrink();
    return x;
}
''',
    'ods/RootishArrayStack.shrink()': '''
shrink() {
    let r = this.blocks.size();
    while (r > 0 && (r-2)*(r-1)/2 >= this.n) {
        this.blocks.remove(this.blocks.size()-1);
        r--;
    }
}
''',
    'ods/FastSqrt.sqrt(x,r)': '''
sqrt(x, r) {
    let s = sqrtab[x>>(r>>1)];
    while ((s+1)*(s+1) <= x) s++; // executes at most twice
    return s;
}
''',
    'ods/FastSqrt.sqrt(x)': '''
sqrt(x) {
    const rp = log(x);
    const upgrade = ((r-rp)>>1) * 2;
    const xp = x << upgrade;  // xp has r or r-1 bits
    let s = sqrtab[xp>>(r>>1)] >> (upgrade/2);
    while ((s+1)*(s+1) <= x) s++;  // executes at most twice
    return s;
}
''',
    'ods/FastSqrt.log(x)': '''
log(x) {
    if (x >= halfint)
        return 16 + logtab[x>>>16];
    return logtab[x];
}
''',
    'ods/FastSqrt.inittabs()': '''
inittabs() {
    sqrtab = new Array(1<<(r>>1));
    logtab = new Array(1<<(r>>1));
    for (let d = 0; d < r>>1; d++)
        logtab.fill(d, 1<<d, 2<<d);
    let s = 1<<(r>>2);                   // sqrt(2^(r/2))
    for (let i = 0; i < 1<<(r>>1); i++) {
        if ((s+1)*(s+1) <= i << (r>>1)) s++; // sqrt increases
        sqrtab[i] = s;
    }
}
''',
    'ods/SEList.get_location(i)': '''
getLocation(i) {
    if (i < Math.floor(this.n/2)) {
        let u = this.dummy.next;
        while (i >= u.d.size()) {
            i -= u.d.size();
            u = u.next;
        }
        return new Location(u, i);
    } else {
        let u = this.dummy;
        let idx = this.n;
        while (i < idx) {
            u = u.prev;
            idx -= u.d.size();
        }
        return new Location(u, i-idx);
    }
}
''',
    'ods/SEList.get(i).set(i,x)': '''
get(i) {
    const l = this.getLocation(i);
    return l.u.d.get(l.j);
}

set(i, x) {
    const l = this.getLocation(i);
    const y = l.u.d.get(l.j);
    l.u.d.set(l.j, x);
    return y;
}
''',
    'ods/SEList.append(x)': '''
add(x) {
    let last = this.dummy.prev;
    if (last === this.dummy || last.d.size() === this.b+1) {
        last = this.addBefore(this.dummy);
    }
    last.d.add(x);
    this.n++;
    return true;
}
''',
    'ods/SEList.add(i,x)': '''
addAt(i, x) {
    if (i === this.n) {
        this.add(x);
        return;
    }
    const l = this.getLocation(i);
    let u = l.u;
    let r = 0;
    while (r < this.b && u !== this.dummy && u.d.size() === this.b+1) {
        u = u.next;
        r++;
    }
    if (r === this.b) {      // b blocks each with b+1 elements
        this.spread(l.u);
        u = l.u;
    }
    if (u === this.dummy) {  // ran off the end - add new node
        u = this.addBefore(u);
    }
    while (u !== l.u) { // work backwards, shifting elements
        u.d.add(0, u.prev.d.remove(u.prev.d.size()-1));
        u = u.prev;
    }
    u.d.add(l.j, x);
    this.n++;
}
''',
    'ods/SEList.remove(i)': '''
remove(i) {
    const l = this.getLocation(i);
    const y = l.u.d.get(l.j);
    let u = l.u;
    let r = 0;
    while (r < this.b && u !== this.dummy && u.d.size() === this.b-1) {
        u = u.next;
        r++;
    }
    if (r === this.b) {  // b blocks each with b-1 elements
        this.gather(l.u);
    }
    u = l.u;
    u.d.remove(l.j);
    while (u.d.size() < this.b-1 && u.next !== this.dummy) {
        u.d.add(u.next.d.remove(0));
        u = u.next;
    }
    if (u.d.isEmpty()) this.removeNode(u);
    this.n--;
    return y;
}
''',
    'ods/SEList.spread(u)': '''
spread(u) {
    let w = u;
    for (let j = 0; j < this.b; j++) {
        w = w.next;
    }
    w = this.addBefore(w);
    while (w !== u) {
        while (w.d.size() < this.b)
            w.d.add(0, w.prev.d.remove(w.prev.d.size()-1));
        w = w.prev;
    }
}
''',
    'ods/SEList.gather(u)': '''
gather(u) {
    let w = u;
    for (let j = 0; j < this.b-1; j++) {
        while (w.d.size() < this.b)
            w.d.add(w.next.d.remove(0));
        w = w.next;
    }
    this.removeNode(w);
}
''',
}

# FastSqrt's Python, translated by the AI from ODS's Java line for line (ODS's Python edition has no FastSqrt);
# sqrtab, logtab, halfint and r are module globals, as the Java class's static fields are.
PY_TRANSLATIONS = {
    'ods/FastSqrt.sqrt(x,r)': '''
def sqrt(x, r):
    s = sqrtab[x>>r//2]
    while (s+1)*(s+1) <= x: s += 1  # executes at most twice
    return s
''',
    'ods/FastSqrt.sqrt(x)': '''
def sqrt(x):
    rp = log(x)
    upgrade = ((r-rp)//2) * 2
    xp = x << upgrade  # xp has r or r-1 bits
    s = sqrtab[xp>>(r//2)] >> (upgrade//2)
    while (s+1)*(s+1) <= x: s += 1  # executes at most twice
    return s
''',
    'ods/FastSqrt.log(x)': '''
def log(x):
    if x >= halfint:
        return 16 + logtab[x>>16]
    return logtab[x]
''',
    'ods/FastSqrt.inittabs()': '''
def inittabs():
    global sqrtab, logtab
    sqrtab = new_array(1<<(r//2))
    logtab = new_array(1<<(r//2))
    for d in range(r//2):
        logtab[1<<d:2<<d] = [d] * (1<<d)
    s = 1<<(r//4)                         # sqrt(2^(r/2))
    for i in range(1<<(r//2)):
        if (s+1)*(s+1) <= i << (r//2): s += 1  # sqrt increases
        sqrtab[i] = s
''',
}

# The members each edition prints where the pseudocode edition's \\pcodeimport stands (plan, Code): the Java and
# C++ editions name SEList's lookup getLocation and its append add(x).
PCODE_MEMBERS = {
    'ods/SEList.get_location(i)': {'python': 'get_location(i)', 'java': 'getLocation(i)', 'cpp': 'getLocation(i,ell)'},
    'ods/SEList.append(x)': {'python': 'append(x)', 'java': 'add(x)', 'cpp': 'add(x)'},
}


def _port(py):
    """RootishArrayStack's Python as it runs on Python 3: `/` on an integer is `//` (the mechanical port of
    judgements/ch01-03-references.md, five lines of rootisharraystack.py)."""
    return re.sub(r'(\b[br]\*\([br]\+1\)|\(r-2\)\*\(r-1\))/2', r'\1//2', py)


def listing(ref):
    """The listing ODS's \\codeimport{ref} names, in the four languages: {python, java, cpp, javascript, _ai}."""
    cls, members = ref.split('/', 1)[1].split('.', 1)
    per = PCODE_MEMBERS.get(ref, {})
    ai = {'javascript'}
    if cls == 'FastSqrt':
        py = PY_TRANSLATIONS[ref].strip('\n')
        ai.add('python')
    else:
        py = ods_listing.python(cls, per.get('python', members), printed=True)
        if cls == 'RootishArrayStack' and _port(py) != py:
            py = _port(py)
            ai.add('python')
    java = ods_listing.java(cls, per.get('java', members), printed=True)
    # RootishArrayStack.java indents i2b's line by a tab and a space; the space stays after the modifiers go
    java = java.lstrip(' ')
    cpp = ods_listing.cpp(cls, per.get('cpp', members), printed=True)
    for lang, v in (('python', py), ('java', java), ('cpp', cpp)):
        if not v.strip():
            raise SystemExit(f'{ref}: no {lang} listing')
    return {'python': py, 'java': java, 'cpp': cpp, 'javascript': CODE_TRANSLATIONS[ref].strip('\n'), '_ai': ai}


def _code_set(v, set_id=None):
    pres = []
    for lang in ('python', 'java', 'cpp', 'javascript'):
        mark = f' data-ai="{AI}"' if lang in v['_ai'] else ''
        body = html.escape(v[lang].strip('\n'), quote=False).replace('$', '&#36;')
        pres.append(f'<pre data-lang="{lang}"{mark}><code>{body}</code></pre>')
    attr = f' id="{set_id}"' if set_id else ''
    return f'<div class="code-set"{attr}>\n' + '\n'.join(pres) + '\n</div>'


def CODE_HOOK(e):
    """ODS's listings: every \\codeimport and \\pcodeimport as a code set. The pseudocode edition prints no
    \\javaimport or \\cppimport; the Java and C++ editions' "Computing Square Roots" prints FastSqrt's at each pair,
    so the set stands at the \\javaimport and the \\cppimport beside it (the same listing) prints nothing.
    sim-fastsqrt, whose panel is sqrt(x), stands after that listing's set."""
    ref, cmd = e['ref'], e['cmd']
    if cmd in ('codeimport', 'pcodeimport'):
        return _code_set(listing(ref))
    if cmd == 'javaimport' and ref.startswith('ods/FastSqrt.'):
        out = _code_set(listing(ref))
        if ref == 'ods/FastSqrt.sqrt(x)':
            out += '\n' + HTML['sim-fastsqrt']
        return out
    return ''


# ---------------------------------------------------------------- the figures' original captions, as plain text

CAPTIONS = {**read_latex.figure_captions(os.path.join(_BOOK, ARRAYS), 2, 'ods'),
            **read_latex.figure_captions(os.path.join(_BOOK, LISTS), 3, 'ods')}


def plain(t):
    """A caption for an attribute (root item 19: no maths in an attribute): $\\mathrm{add}(i,x)$ as add(i,x)."""
    return re.sub(r'\$([^$]*)\$', lambda m: re.sub(r'\\math(?:rm|it)\{([^}]*)\}', r'\1', m.group(1)), t)


ORIG = {k: plain(CAPTIONS[k]['text']) for k in ('rootisharraystack', 'gauss', 'selist-add', 'selist-remove')}


# ---------------------------------------------------------------- figures and derivations in the text

def sim(fid, caption, original=None, original_caption=None):
    attrs = f'class="sim" id="{fid}"'
    if original:
        attrs += f' data-original="{original}" data-original-caption="{html.escape(original_caption, quote=True)}"'
    return f'<figure {attrs}>\n  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>'


def R(rid, s=None):
    return f'<span data-ref="{rid}"><em>{s or rid}</em></span>'


_I, _B, _R, _X, _S, _U, _W = R('i'), R('b'), R('r'), R('x'), R('s'), R('u'), R('w')
CAP = {
    'sim-rootish': (
        f'ODS’s RootishArrayStack running add({_I}, x), remove({_I}) and get({_I}) on its blocks. Each get and set finds '
        f'the block {_B} = ⌈(−3 + √(9 + 8{_I}))/2⌉ that holds index {_I} and the place j = {_I} − {_B}({_B} + 1)/2 '
        'within it, so a shift carries an element across a block boundary as easily as along a block. grow() adds a block '
        f'of {_R} + 1 cells only when all {_R}({_R} + 1)/2 cells are in use, and remove({_I}) frees blocks only when two '
        f'or more stand empty, so only the last two blocks can have unused cells and the waste stays at most 2{_R} − 1. '
        'Adding at the front shifts every element on every call.'),
    'sim-gauss': (
        'Two copies of the staircase 1 + 2 + ⋯ + <em>r</em>, one turned half a turn, fill a rectangle <em>r</em> cells '
        'tall and <em>r</em> + 1 wide, so each holds <em>r</em>(<em>r</em> + 1)/2 cells: the cells of blocks 0 to '
        '<em>r</em> − 1 of a RootishArrayStack.'),
    'sim-wasted-space': (
        'The space wasted after <em>n</em> appends to an empty structure. A RootishArrayStack’s unused cells and block '
        'references stay within a small multiple of √<em>n</em>, while an ArrayStack that has just doubled wastes nearly '
        '<em>n</em>. Both rise above √<em>n</em> at some moment, as the lower bound says every such structure must.'),
    'sim-fastsqrt': (
        f'FastSqrt computing ⌊√{_X}⌋ for {_X} below 2³⁰ with one table lookup. Shifting {_X} up an even number of '
        'places, 2<em>k</em>, multiplies its square root by exactly 2<sup><em>k</em></sup>; the top 16 bits then index '
        f'sqrtab, which holds ⌊√(<em>t</em>·2¹⁴)⌋, and shifting the entry back down by <em>k</em> leaves {_S} within 2 '
        f'of ⌊√{_X}⌋, so the last loop adds 1 at most twice. One million needs no correction; 66,049 = 257² needs one.'),
    'sim-selist-add': (
        f'An SEList with block size <em>b</em> = 3 adding x at index {_I}. Starting at {_U}, the block that holds index '
        f'{_I}, {_W} looks at most <em>b</em> blocks ahead for one with room. If it finds one (Case 1), or runs off the '
        f'end and a new last block is added (Case 2), the last element of each block from {_U} to {_W} moves one block '
        f'on, which frees a cell in {_U}. If <em>b</em> blocks in a row are full (Case 3), spread({_U}) first deals their '
        'elements into <em>b</em> + 1 blocks of <em>b</em>. Adding at the front again and again spreads at most once in '
        'every <em>b</em> adds: each spread removes <em>b</em> − 1 fragile nodes, which the adds before it made.'),
    'sim-selist-remove': (
        f'An SEList with <em>b</em> = 3 removing the element at index {_I}. Starting at {_U}, {_W} looks at most '
        '<em>b</em> blocks ahead for one with more than <em>b</em> − 1 elements. After the element leaves, '
        f'{_U} takes the first element of the next block, and each block after it does the same, until the chain '
        f'reaches {_W} (Case 1) or the end of the list, where an emptied last block is dropped (Case 2). If <em>b</em> '
        f'blocks in a row hold only <em>b</em> − 1 (Case 3), gather({_U}) first fills <em>b</em> − 1 of them to '
        '<em>b</em> and removes the last. Removing from the front again and again gathers at most once in every '
        '<em>b</em> removes.'),
}
M = '/media/ch03/'
HTML = {
    'sim-rootish': sim('sim-rootish', CAP['sim-rootish'], M + 'ods-rootisharraystack.png', ORIG['rootisharraystack']),
    'sim-gauss': sim('sim-gauss', CAP['sim-gauss'], M + 'ods-gauss.png', ORIG['gauss']),
    'sim-wasted-space': sim('sim-wasted-space', CAP['sim-wasted-space']),
    'sim-fastsqrt': sim('sim-fastsqrt', CAP['sim-fastsqrt']),
    'sim-selist-add': sim('sim-selist-add', CAP['sim-selist-add'],
                          ','.join(M + f'ods-selist-add-{c}.png' for c in 'abc'), ORIG['selist-add']),
    'sim-selist-remove': sim('sim-selist-remove', CAP['sim-selist-remove'],
                             ','.join(M + f'ods-selist-remove-{c}.png' for c in 'abc'), ORIG['selist-remove']),
    'drv-root': '<figure class="dv" id="drv-root"></figure>',
    'drv-rootish-blocks': '<figure class="dv" id="drv-rootish-blocks"></figure>',
    'drv-sqrt-lower-bound': '<figure class="dv" id="drv-sqrt-lower-bound"></figure>',
    'drv-selist-spread': '<figure class="dv" id="drv-selist-spread"></figure>',
}


# ---------------------------------------------------------------- marks

def _refmath(tex, letters):
    """A maths string with the figure's referents marked (\\htmlData{ref=…}): a lone letter of `letters`, never one
    inside a name such as \\mathrm{get} or \\mathit{blocks}, which are set aside first."""
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f'\x00{len(keep) - 1}\x01'
    t = re.sub(r'\\(?:mathrm|mathit|text)\{[^}]*\}|\\[A-Za-z]+', hold, tex)
    t = re.sub(r'(?<![A-Za-z])([' + letters + r'])(?![A-Za-z])', lambda m: '\\htmlData{ref=' + m.group(1) + '}{' + m.group(1) + '}', t)
    return re.sub(r'\x00(\d+)\x01', lambda m: keep[int(m.group(1))], t)


# The maths of the two blocks the debugger figures stand in that name a referent, as the reader prints them:
# rootish's i, b, n and r (sim-rootish), selist's i and u (sim-selist-add, sim-selist-remove). Longest first, so a
# piece never marks inside a longer one already marked.
_ROOTISH_MATHS = [
    '$$b = \\left\\lceil(-3 + \\sqrt{9+8i}) / 2\\right\\rceil \\enspace .$$', '$$(b+1)(b+2)/2 \\ge i+1 \\enspace .$$',
    '$$b^2 + 3b - 2i \\ge 0 \\enspace .$$', '$$1+ 2+ 3+\\cdots +r = r(r+1)/2$$', '$$j = i - b(b+1)/2$$',
    '$b \\ge (-3 + \\sqrt{9+8i}) / 2$', '$b = (-3 + \\sqrt{9+8i}) / 2$', '$b=(-3 - \\sqrt{9+8i}) / 2$',
    '$b=(-3 + \\sqrt{9+8i}) / 2$', '$b^2 + 3b - 2i = 0$', '$(b+1)(b+2)/2$', '$0,1,\\ldots,r-1$', '$O(\\sqrt{n})$',
    '$\\mathrm{set}(i,x)$', '$\\mathrm{add}(i,x)$', '$\\mathrm{remove}(i)$', '$\\mathrm{get}(i)$', '$r(r+1)/2 = n$',
    '$i+1,\\ldots,n$', '$i,\\ldots,n-1$', '$0,\\ldots,b-1$', '$0,\\ldots,b$', '$O(1+n-i)$', '$b(b+1)/2$', '$O(n-i)$',
    '$b+1$', '$i+1$', '$r-1$', '$O(r)$', '$b$', '$i$', '$n$', '$r$',
]
_SELIST_MATHS = [
    '$O(b+\\min\\{i,n-i\\}/b)$', '$O(1+\\min\\{i,n-i\\}/b)$', '$O(1+(n-i)/b)$', '$O(1+i/b)$', '$\\mathrm{spread}(u)$',
    '$\\mathrm{gather}(u)$', '$\\mathrm{set}(i,x)$', '$\\mathrm{add}(i,x)$', '$\\mathrm{remove}(i)$', '$\\mathrm{get}(i)$',
    '$i$', '$u$',
]


def _href(url, text):
    return f'<a href="{url}">{text}</a>'


_22 = '/cs-interview-prep-ultra/ch02/2.2/'
FN = lambda nid: f'<sup class="fn" data-note="{nid}"></sup>'  # noqa: E731

# (block, text as built, replacement, [count]): what the converter cannot set, then concepts, the cross-references
# B18 asks for, the errata markers, the connectives the derivations carry, and the referents.
MARKS = [
    # the reader sets a two-dot field and a one-word name inside multi-word code as letters; ODS's editions set them
    # as names (u.next.next, sqrttab[i])
    ('selist', '\\mathit{u}.\\mathit{next}.next', '\\mathit{u}.\\mathit{next}.\\mathit{next}', 2),
    ('rootish-sqrt', '$$sqrttab[i]', '$$\\mathit{sqrttab}[i]'),
    ('rootish-sqrt', '$sqrttab[i]$', '$\\mathit{sqrttab}[i]$'),
    ('rootish-sqrt', '$s=sqrttab[x>>', '$s=\\mathit{sqrttab}[x>>'),
    # concepts: the span that introduces each (plan, Concepts)
    ('rootish', 'stores its elements in a list of $r$ arrays called <em>blocks</em>',
     '<span data-concept="rootish-array-stack">stores its elements in a list of $r$ arrays called <em>blocks</em></span>'),
    ('sqrt-lower-bound', 'this space usage is optimal for any data structure that starts out empty and can support the '
     'addition of one item at a time',
     '<span data-concept="sqrt-space-lower-bound">this space usage is optimal for any data structure that starts out '
     'empty and can support the addition of one item at a time</span>'),
    ('rootish-sqrt', 'the square root operation can be implemented efficiently',
     '<span data-concept="rootish-index-math">the square root operation can be implemented efficiently</span>'),
    ('selist', 'reduces this wasted space using a simple idea',
     '<span data-concept="space-efficient-list">reduces this wasted space using a simple idea</span>'),
    ('selist-amortized', 'the total time spent during all calls to $\\mathrm{spread}()$ and $\\mathrm{gather}()$ is $O(bm)$',
     '<span data-concept="selist-spread-gather">the total time spent during all calls to $\\mathrm{spread}()$ and '
     '$\\mathrm{gather}()$ is $O(bm)$</span>'),
    # B18: ArrayStack's resize() and its analysis are Section 2.2's
    ('rootish', 'a $\\mathrm{resize}()$ operation on an ArrayStack',
     'a ' + _href(_22 + '#resize', '$\\mathrm{resize}()$ operation on an ArrayStack')),
    ('rootish', 'unlike the $\\mathrm{ArrayStack.resize}()$ operation',
     'unlike the ' + _href(_22 + '#resize', '$\\mathrm{ArrayStack.resize}()$ operation')),
    ('rootish-sqrt', 'the cost of $\\mathrm{resize}()$ is analyzed in the ArrayStack implementation',
     _href(_22 + '#arraystack-cost', 'the cost of $\\mathrm{resize}()$ is analyzed in the ArrayStack implementation')),
    # errata 27, 35, 36
    ('sqrt-lower-bound', 'wasting at least in $\\sqrt{n}$ space', 'wasting at least in $\\sqrt{n}$ space' + FN('err-wasting')),
    ('selist', '(see <a href="#sim-selist-remove">Figure 3.5</a>):',
     '(see <a href="#sim-selist-remove">Figure 3.5</a>):' + FN('err-case2')),
    ('rootish-sqrt', 'initializes $\\mathit{logtab}$ and $\\mathit{sqrttab}$:',
     'initializes $\\mathit{logtab}$ and $\\mathit{sqrttab}$:' + FN('err-inittabs')),
    # the words between the displays the derivations replace (root item 29.2; their steps carry them)
    ('sqrt-lower-bound', '<p>Again, using the quadratic equation on this gives</p>\n', ''),
    ('rootish-sqrt', '<p>Square both sides of this inequality to get</p>\n', ''),
    ('rootish-sqrt', '<p>and gather terms to get</p>\n', ''),
    ('rootish-sqrt', '<p>which is clearly true for any $x\\ge 1$.</p>\n', ''),
] + [('rootish', t, _refmath(t, 'ibnr'), 40) for t in _ROOTISH_MATHS] \
  + [('selist', t, _refmath(t, 'iu'), 40) for t in _SELIST_MATHS]


# ---------------------------------------------------------------- derivations

DRV_ROOT = {
    'id': 'root',
    'what': '√x′ ≥ √x − 1',
    'source': 'Open Data Structures, 2.6.4 Computing Square Roots, the proof of Lemma 2.3',
    'nodes': [
        {
            'assumes': [{'tex': 'x \\ge 1', 'src': 'Lemma 2.3'}],
            'then': {'tex': '\\mk{s}{\\sqrt{x}} \\ge \\mk{o}{1}', 'uses': [0],
                     'why': 'The square root is increasing, and $\\sqrt{1} = 1$.'},
            'steps': [
                {'tex': '\\mk{x1}{x} - \\mk{s}{\\sqrt{x}} \\ge \\mk{x2}{x} - \\mk{t}{2\\sqrt{x}} + \\mk{o}{1}', 'uses': []},
                {'tex': '\\mk{l}{\\left(\\sqrt{x-\\sqrt{x}}\\right)^2} \\ge \\mk{r}{\\left(\\sqrt{x}-1\\right)^2}', 'uses': [],
                 'map': {'x1': 'l', 's': 'l', 'x2': 'r', 't': 'r', 'o': 'r'},
                 'cap': 'Both sides are squares: $x - \\sqrt{x} \\ge 0$ because $x \\ge \\sqrt{x}$ when $x \\ge 1$, and '
                        '$x - 2\\sqrt{x} + 1 = (\\sqrt{x} - 1)^2$.'},
                {'tex': '\\mk{l}{\\sqrt{x-\\sqrt{x}}} \\ge \\mk{r}{\\sqrt{x}-1}', 'uses': [],
                 'cap': 'Both bases are at least 0, $\\sqrt{x} - 1$ by the first line, and for numbers at least 0, '
                        '$p^2 \\ge q^2$ gives $p \\ge q$.'},
            ],
            'src': 'Lemma 2.3, proof',
        },
        {
            'assumes': [
                {'text': '$x\' = x - a$, where $0 \\le a \\le \\sqrt{x}$.', 'src': 'Lemma 2.3'},
                {'step': 0},
            ],
            'then': {'tex': '\\mk{p}{x\'} \\ge \\mk{q}{x - \\sqrt{x}}', 'uses': [0],
                     'why': 'Taking away at most $\\sqrt{x}$ leaves at least $x - \\sqrt{x}$.'},
            'steps': [
                {'tex': '\\mk{p}{\\sqrt{x\'}} \\ge \\mk{q}{\\sqrt{x-\\sqrt{x}}}', 'uses': [],
                 'cap': 'The square root is increasing.'},
                {'tex': '\\mk{p}{\\sqrt{x\'}} \\ge \\mk{q}{\\sqrt{x}-1}', 'uses': [1]},
            ],
            'src': 'Lemma 2.3',
        },
    ],
}

DRV_BLOCKS = {
    'id': 'rootish-blocks',
    'what': 'r = O(√n)',
    'source': 'Open Data Structures, 2.6.2 Space Usage',
    'nodes': [
        {
            'assumes': [
                {'text': 'The $\\mathrm{remove}(i)$ operation ensures that a RootishArrayStack never has more than two '
                         'blocks that are not completely full.', 'src': '2.6.2'},
                {'text': 'Block $b$ contains $b + 1$ elements, so blocks $0, \\ldots, r - 3$ hold '
                         '$1 + 2 + \\cdots + (r-2) = (r-2)(r-1)/2$ of them.', 'src': '2.6'},
            ],
            'then': {'tex': '\\mk{f}{(r-2)(r-1)/2} \\le \\mk{n}{n}', 'uses': [0, 1],
                     'why': 'All but the last two of the $r$ blocks are full, and their elements are among the $n$.'},
            'steps': [
                {'tex': '\\mk{f}{r^2 - 3r + 2} \\le \\mk{n}{2n}', 'uses': []},
                {'tex': '\\mk{f}{r^2 - 3r + 2 - 2n} \\le \\mk{z}{0}', 'uses': [], 'map': {'n': 'f'}},
                {'tex': '\\mk{r}{r} \\le \\mk{q}{\\frac{1}{2}\\left(3+\\sqrt{8n+1}\\right)}', 'uses': [],
                 'map': {'f': 'r', 'z': 'q'},
                 'cap': 'A parabola that opens upward is at most 0 only between its roots, and by the quadratic formula '
                        'the larger root of $r^2 - 3r + (2 - 2n)$ is $\\frac{1}{2}\\left(3 + \\sqrt{9 - 4(2 - 2n)}\\right)$.'},
                {'tex': '\\mk{r}{r} \\le \\mk{q}{\\frac{1}{2}\\left(3+\\sqrt{8n+1}\\right)} = \\mk{o}{O(\\sqrt{n})}', 'uses': [],
                 'cap': 'For $n \\ge 1$, $\\sqrt{8n + 1} \\le 3\\sqrt{n}$.'},
            ],
            'src': '2.6.2',
        },
    ],
}

DRV_LOWER = {
    'id': 'sqrt-lower-bound',
    'what': 'some moment wastes √n space',
    'source': 'Open Data Structures, 2.6.2 Space Usage',
    'nodes': [
        {
            'assumes': [
                {'text': 'An empty data structure receives $n$ items one at a time, and at the end they are distributed '
                         'among $r$ memory blocks.', 'src': '2.6.2'},
                {'text': 'The pigeonhole principle: $n$ items in $r$ blocks put at least $n/r$ of them in one block.'},
                {'text': 'Immediately after it is allocated, a block is empty, so all of its space is wasted.', 'src': '2.6.2'},
            ],
            'then': {'tex': '\\mk{s}{\\text{size of some block}} \\ge \\mk{q}{n/r}', 'uses': [0, 1]},
            'steps': [
                {'tex': '\\mk{w}{\\text{waste when it was allocated}} \\ge \\mk{q}{n/r}', 'uses': [2], 'map': {'s': 'w'}},
            ],
            'src': '2.6.2',
        },
        {
            'assumes': [
                {'text': 'The structure must keep $r$ pointers (or references) to its $r$ blocks, and these pointers are '
                         'wasted space.', 'src': '2.6.2'},
                {'step': 0},
            ],
            'then': {'tex': '\\mk{w}{\\text{most waste at any moment}} \\ge \\mk{m}{\\max(r,\\ n/r)}', 'uses': [0, 1],
                     'why': 'The $r$ pointers are wasted at the end, and the large block was wasting its space the moment '
                            'it was allocated.'},
            'steps': [
                {'tex': '\\mk{w}{\\text{most waste at any moment}} \\ge \\mk{m}{\\sqrt{n}}', 'uses': [],
                 'cap': 'If $r \\ge \\sqrt{n}$, the first is at least $\\sqrt{n}$; if $r < \\sqrt{n}$, then '
                        '$n/r > n/\\sqrt{n} = \\sqrt{n}$.'},
            ],
            'src': '2.6.2',
        },
    ],
}

DRV_SPREAD = {
    'id': 'selist-spread',
    'what': 'O(bm) time in all calls to spread()',
    'source': 'Open Data Structures, 3.3.4 Amortized Analysis of Spreading and Gathering, the proof of Lemma 3.1',
    'nodes': [
        {
            'assumes': [
                {'text': 'The potential $\\Phi$, the number of fragile nodes, starts at 0 and is never less than 0.',
                 'src': 'Lemma 3.1, proof'},
                {'text': 'Each time Case 1 or Case 2 occurs, the potential increases by at most 1.', 'src': 'Lemma 3.1, proof'},
                {'text': 'Each time Case 3 occurs, the potential decreases by $b - 1$.', 'src': 'Lemma 3.1, proof'},
                {'text': 'Of the $m$ calls to $\\mathrm{add}(i,x)$, $s$ reach Case 3 and call $\\mathrm{spread}(u)$, and '
                         'the other $m - s$ are Case 1 or Case 2.'},
            ],
            'then': {'tex': '\\mk{p}{\\Phi} \\le \\mk{o}{0} + \\mk{u}{(m-s)} - \\mk{d}{(b-1)s}', 'uses': [1, 2, 3],
                     'why': 'The potential starts at 0, the $m - s$ other calls add at most 1 each, and each spread takes '
                            '$b - 1$ away.'},
            'steps': [
                {'tex': '\\mk{p}{0} \\le \\mk{u}{(m-s)} - \\mk{d}{(b-1)s}', 'uses': [0], 'map': {'o': 'p'}},
                {'tex': '\\mk{d}{(b-1)s} \\le \\mk{u}{m-s}', 'uses': []},
                {'tex': '\\mk{d}{bs} \\le \\mk{u}{m}', 'uses': []},
                {'tex': '\\mk{d}{s} \\le \\mk{u}{m/b}', 'uses': []},
            ],
            'src': 'Lemma 3.1, proof',
        },
        {
            'assumes': [
                {'text': 'Each call to $\\mathrm{spread}(u)$ runs two nested loops of at most $b + 1$ steps, so it takes '
                         '$O(b^2)$ time.', 'src': '3.3.4'},
                {'step': 0},
            ],
            'then': {'tex': '\\mk{T}{\\text{time in } \\mathrm{spread}()} = \\mk{s}{s \\cdot O(b^2)}', 'uses': [0]},
            'steps': [
                {'tex': '\\mk{T}{\\text{time in } \\mathrm{spread}()} \\le \\mk{s}{(m/b) \\cdot O(b^2)}', 'uses': [1]},
                {'tex': '\\mk{T}{\\text{time in } \\mathrm{spread}()} = \\mk{s}{O(bm)}', 'uses': []},
            ],
            'src': 'Lemma 3.1',
        },
    ],
}


def check_derivations():
    """Every line holds. drv-root: the lemma and each of its lines for x on a grid up to 10⁶ and a in [0, √x].
    drv-rootish-blocks: over 300 random runs of a RootishArrayStack's grow and shrink policy (ODS's code), every
    reached (n, r) satisfies (r − 2)(r − 1)/2 ≤ n, r ≤ (3 + √(8n + 1))/2 and, for n ≥ 1, √(8n + 1) ≤ 3√n.
    drv-sqrt-lower-bound: for every split of n ≤ 200 items into r blocks, max(r, largest block) ≥ √n.
    drv-selist-spread: over random runs of ODS's SEList add(i, x) (the logic of selist.py), the fragile count
    rises by at most 1 in Cases 1 and 2, falls by b − 1 in Case 3, and the spreads s satisfy b·s ≤ m."""
    import math
    import random
    for x in [1 + k * 0.37 for k in range(3000)] + list(range(1, 10 ** 6, 997)):
        r = math.sqrt(x)
        assert r >= 1 - 1e-12
        assert x - r >= x - 2 * r + 1 - 1e-9
        assert math.sqrt(x - r) >= r - 1 - 1e-9
        for a in (0, r / 3, r / 2, r):
            assert math.sqrt(x - a) >= r - 1 - 1e-9
    rnd = random.Random(36)
    for _ in range(300):
        n, r = 0, 0
        for _ in range(400):
            if n == 0 or rnd.random() < rnd.choice((0.3, 0.5, 0.7)):
                if r * (r + 1) // 2 < n + 1:
                    r += 1
                n += 1
            else:
                n -= 1
                if (r - 2) * (r - 1) // 2 >= n:
                    while r > 0 and (r - 2) * (r - 1) // 2 >= n:
                        r -= 1
            # (with no block at all, r = 0, the count of full blocks is 0, not (r − 2)(r − 1)/2)
            assert r == 0 or (r - 2) * (r - 1) / 2 <= n
            assert r <= (3 + math.sqrt(8 * n + 1)) / 2 + 1e-9
            if n >= 1:
                assert math.sqrt(8 * n + 1) <= 3 * math.sqrt(n) + 1e-12
    for n in range(1, 201):
        for r in range(1, n + 1):
            big = -(-n // r)
            assert max(r, big) >= math.sqrt(n) - 1e-12
    for b in (2, 3, 4, 5):
        for run in range(60):
            blocks, m, s = [], 0, 0
            for _ in range(250):
                n = sum(blocks)
                i = rnd.randrange(0, n + 1)
                phi0 = sum(1 for z in blocks if z != b)
                m += 1
                case = _selist_add(blocks, b, i)
                phi1 = sum(1 for z in blocks if z != b)
                if case == 3:
                    s += 1
                    assert phi1 - phi0 == -(b - 1), (b, case, phi0, phi1)
                else:
                    assert phi1 - phi0 <= 1
                assert b * s <= m
                assert all(b - 1 <= z <= b + 1 for z in blocks[:-1]) and blocks[-1] >= 1
    return True


def _selist_add(blocks, b, i):
    """ODS's SEList add(i, x) on block sizes alone (selist.py's logic): the case it takes."""
    n = sum(blocks)
    if i == n:
        if not blocks or blocks[-1] == b + 1:
            blocks.append(0)
        blocks[-1] += 1
        return 2 if blocks[-1] == 1 else 1
    k, j = 0, i
    if i < n // 2:
        while j >= blocks[k]:
            j -= blocks[k]
            k += 1
    else:
        k, idx = len(blocks), n
        while i < idx:
            k -= 1
            idx -= blocks[k]
    w, r = k, 0
    while r < b and w < len(blocks) and blocks[w] == b + 1:
        w += 1
        r += 1
    case = 1
    if r == b:
        blocks[k:k + b] = [b] * (b + 1)
        w, case = k, 3
    if w == len(blocks):
        blocks.append(0)
        case = 2
    while w != k:
        blocks[w] += 1
        blocks[w - 1] -= 1
        w -= 1
    blocks[k] += 1
    return case


# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]

LEAD = ('An Advanced section on lists that waste little space: ODS’s RootishArrayStack, the √<em>n</em> lower bound on '
        'wasted space, and the SEList; <span data-concept="rootish-index-math">computing square roots in constant '
        'time</span> is Beyond. Blocks and list indices count from 0. The SEList proof’s “potential method” is '
        '<a href="/cs-interview-prep-ultra/ch01/1.5/#potential">Section 1.5</a>’s <span data-concept="potential-method">method</span> used as a counter: Φ is the '
        'number of fragile nodes, each add that does not spread raises it by at most 1, and so the adds before a spread '
        'pay for it.')

FIGS = ['sim-rootish', 'sim-gauss', 'sim-wasted-space', 'sim-fastsqrt', 'sim-selist-add', 'sim-selist-remove']

SECTION = {
    'id': '3.6', 'chapter': '3', 'title': 'Space-efficient lists', 'short': 'Space-efficient lists',
    'lead': LEAD,
    'objectives': [], 'summary_html': '',
    'notes': 'The Discussion and Exercises sections of ODS’s two chapters are left out here.',
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'No exercise ships with this section yet. ODS’s test_rootisharraystack.py and test_selist.py are tests with no '
        'printed statement (they pass on ODS’s Python once its integer division and print statements are ported). '
        'ODS Exercises 2.10 to 2.13 (faster RootishArrayStack variants and a CubishArrayStack) and 3.17 and 3.18 (an '
        'SEList used as a stack and a variant of it) have no published answers or tests and are left out. No open '
        'exercise exists for computing square roots in constant time or for the √n lower bound on wasted space.'),
    'figures': [
        {'id': 'sim-rootish', 'kind': 'sim', 'originals': ['/media/ch03/ods-rootisharraystack.png'],
         'original_caption': ORIG['rootisharraystack'], 'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
        {'id': 'sim-gauss', 'kind': 'sim', 'originals': ['/media/ch03/ods-gauss.png'],
         'original_caption': ORIG['gauss'], 'draws': ['size'], 'ai': FIG_AI},
        {'id': 'sim-wasted-space', 'kind': 'sim', 'draws': ['cost', 'size'], 'ai': FIG_AI},
        {'id': 'sim-fastsqrt', 'kind': 'sim', 'draws': ['index', 'key', 'cost'], 'ai': FIG_AI},
        {'id': 'sim-selist-add', 'kind': 'sim', 'originals': [M + f'ods-selist-add-{c}.png' for c in 'abc'],
         'original_caption': ORIG['selist-add'], 'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
        {'id': 'sim-selist-remove', 'kind': 'sim', 'originals': [M + f'ods-selist-remove-{c}.png' for c in 'abc'],
         'original_caption': ORIG['selist-remove'], 'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'i', 'label': 'i, the list index a call names', 'figures': ['sim-rootish', 'sim-selist-add', 'sim-selist-remove']},
        {'id': 'b', 'label': 'b, the block that holds index i', 'figures': ['sim-rootish']},
        {'id': 'n', 'label': 'n, the number of elements stored', 'figures': ['sim-rootish']},
        {'id': 'r', 'label': 'r, the number of blocks', 'figures': ['sim-rootish']},
        {'id': 'x', 'label': 'x, the number whose square root is taken', 'figures': ['sim-fastsqrt']},
        {'id': 's', 'label': 's, the square root as it is found', 'figures': ['sim-fastsqrt']},
        {'id': 'u', 'label': 'u, the node that holds index i', 'figures': ['sim-selist-add', 'sim-selist-remove']},
        {'id': 'w', 'label': 'w, the node the search has reached', 'figures': ['sim-selist-add', 'sim-selist-remove']},
    ],
    'coverage': [
        {'span': 'rootish', 'concept': 'rootish-array-stack', 'verb': 'introduces'},
        {'span': 'rootish', 'concept': 'dynamic-array-cost', 'verb': 'uses'},
        {'span': 'rootish', 'concept': 'amortized-analysis', 'verb': 'uses'},
        {'span': 'sqrt-lower-bound', 'concept': 'sqrt-space-lower-bound', 'verb': 'introduces'},
        {'span': 'sqrt-lower-bound', 'concept': 'rootish-array-stack', 'verb': 'uses'},
        {'span': 'rootish-summary', 'concept': 'rootish-array-stack', 'verb': 'uses'},
        {'span': 'rootish-sqrt', 'concept': 'rootish-index-math', 'verb': 'introduces'},
        {'span': 'rootish-sqrt', 'concept': 'word-ram', 'verb': 'uses'},
        {'span': 'rootish-sqrt', 'concept': 'rootish-array-stack', 'verb': 'uses'},
        {'span': 'selist', 'concept': 'space-efficient-list', 'verb': 'introduces'},
        {'span': 'selist', 'concept': 'doubly-linked-list', 'verb': 'uses'},
        {'span': 'selist', 'concept': 'sqrt-space-lower-bound', 'verb': 'uses'},
        {'span': 'selist-amortized', 'concept': 'selist-spread-gather', 'verb': 'introduces'},
        {'span': 'selist-amortized', 'concept': 'potential-method', 'verb': 'uses'},
        {'span': 'selist-amortized', 'concept': 'space-efficient-list', 'verb': 'uses'},
        {'span': 'selist-summary', 'concept': 'space-efficient-list', 'verb': 'uses'},
    ],
    'footnotes_extra': [
        {'id': 'err-wasting', 'kind': 'correction',
         'html': 'A typo: the data structure is wasting at least $\\sqrt{n}$ space.'},
        {'id': 'err-case2', 'kind': 'correction',
         'html': 'With $b = 3$, Figure 3.5’s middle picture is not Case 2: its three blocks of $b - 1 = 2$ elements are $b$ '
                 'such blocks, so $\\mathrm{remove}(1)$ finds Case 3 and gathers them, leaving a c | d e f. Case 2 needs '
                 'the end of the list within $b - 1$ blocks, as in a b | c d, which becomes a c | d.'},
        {'id': 'err-inittabs', 'kind': 'correction',
         'html': 'As printed, $\\mathrm{inittabs}()$ makes tables of $2^{r/2} = 2^{14}$ entries for $r = 29$, but '
                 '$\\mathrm{sqrt}(x)$ reads $\\mathit{sqrttab}$ at <code>xp&gt;&gt;(r/2)</code>, which reaches $2^{16} - 1$, and the text '
                 'speaks of tables of size $2^{16}$, as ODS’s working code builds them. In the C++ listing, '
                 '<code>logtab[1&lt;&lt;d+k]</code> reads as <code>logtab[1&lt;&lt;(d+k)]</code>; '
                 '<code>logtab[(1&lt;&lt;d)+k]</code> is meant.'},
    ],
    'derivations': [DRV_BLOCKS, DRV_LOWER, DRV_ROOT, DRV_SPREAD],
}
