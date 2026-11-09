"""What tools/build_text.py needs to assemble 1.2 Logarithms, factorials and harmonic numbers (the plan is plan.md
beside this file).

Everything here is placement, markup or a small correction of what the conversion gets wrong; the source's words
come from the ODS converter in tools/build_text.py (pseudocode edition, METHOD decision 20). Each FIXES entry says
why it is there.
"""
TITLE = 'Logarithms, factorials and harmonic numbers'
INTRO = 'sources/_cache/ods/latex/intro.tex'
RBS = 'sources/_cache/ods/latex/rbs.tex'

BLOCKS = [
    # intro.tex 407 is "\subsection{Exponentials and Logarithms}"; 473 "\subsection{Factorials}"; 517 "\subsection{Asymptotic Notation}"
    dict(id='logarithms', source='ods', file=INTRO, lines=(409, 471),
         locator='ods:intro#exponentials-and-logarithms', h2='Exponentials and Logarithms'),
    dict(id='factorials', source='ods', file=INTRO, lines=(474, 515),
         locator='ods:intro#sec:factorials', h2='Factorials'),
    # rbs.tex 76 opens the digression ("Before we can present our main result…"), 110 closes its figure
    # (\figlabel{harmonic-integral}); 113 begins Lemma 7.1, which is the random binary search tree's
    dict(id='harmonic', source='ods', file=RBS, lines=(76, 110),
         locator='ods:rbs#sec:rbst, the digression on harmonic numbers, from “Before we can present our main result” to the end of its figure',
         h2='Harmonic Numbers'),
]

# ODS cross-references, to this book's pages: the source's own figure number, linked to the Sim that stands for
# it (plans-summary question 18).
ODS_REFS = {
    '\\figref{harmonic-integral}': ('<a href="#sim-harmonic">Figure 7.2</a>', 'Figure 7.2'),
}

# A printed chain of equations the derivation replaces (root item 29.2), named by a piece of its TeX.
DISPLAY_AS = {
    '\\ln k = \\frac{\\log k}{\\log e}': 'drv-change-of-base',
}

# (what the conversion gives, what the page prints, why)
FIXES = []

AI = 'claude-opus-5-5 high'


def sim(fid, caption, original=None, original_caption=None):
    attrs = f'class="sim" id="{fid}"'
    if original:
        attrs += f' data-original="{original}" data-original-caption="{original_caption}"'
    return f'<figure {attrs}>\n  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>'


def dv(did):
    return f'<figure class="dv" id="drv-{did}"></figure>'


HTML = {
    'sim-halving': sim(
        'sim-halving',
        'Dividing <em>k</em> by <em>b</em> again and again, on a scale where every division by <em>b</em> is the same '
        'step down: the steps from <em>k</em> to 1 number log<sub><em>b</em></sub> <em>k</em>, which is '
        'ln <em>k</em> / ln <em>b</em>, and the bars are counted until one reaches 1 or less. Halving takes the most '
        'steps and dividing by 10 the fewest, while every base keeps the same shape.'),
    'drv-change-of-base': dv('change-of-base'),
    'sim-stirling': sim(
        'sim-stirling',
        'Stirling’s Approximation against the exact <em>n</em>!: the factor e<sup>α(<em>n</em>)</sup> between them '
        'falls towards 1 as <em>n</em> grows. The bounds 1/(12<em>n</em> + 1) &lt; α(<em>n</em>) &lt; 1/(12<em>n</em>) '
        'say the same as 12<em>n</em> &lt; 1/α(<em>n</em>) &lt; 12<em>n</em> + 1, so the graph plots '
        '1/α(<em>n</em>) − 12<em>n</em>, which must stay strictly between 0 and 1, and it hugs 0: α(<em>n</em>) is '
        'very nearly 1/(12<em>n</em>).'),
    'sim-harmonic': sim(
        'sim-harmonic',
        '<em>H<sub>k</sub></em> as the area of <em>k</em> rectangles of width 1 under or over the curve 1/<em>x</em>, '
        'with ln <em>k</em> the area under the curve from 1 to <em>k</em>. Rectangles standing to the right of 1 '
        'reach above the curve and cover more than ln <em>k</em>; slid one place left, the rectangles after the first '
        'fit under it, so <em>H<sub>k</sub></em> is at most 1 + ln <em>k</em>, with equality only at '
        '<em>k</em> = 1.',
        '/media/ch01/ods-harmonic-2.png, /media/ch01/ods-harmonic-3.png', '{{caption-text harmonic-integral}}'),
    'drv-harmonic-bounds': dv('harmonic-bounds'),
}

AFTER_TEXT = {
    'logarithms': [('before the result is less than or equal to 1', 'sim-halving')],
    'factorials': [('most easily proven', 'sim-stirling')],
    'harmonic': [('for a graphical explanation.', 'sim-harmonic'), ('for a graphical explanation.', 'drv-harmonic-bounds')],
}

FN_K = '<sup class="fn" data-note="err-harmonic-k"></sup>'
FN_INT = '<sup class="fn" data-note="err-integral-n"></sup>'
# (block, text as built, replacement, [count]): concepts, the cost of binary search, the errata markers
MARKS = [
    ('logarithms', '<em>base-$b$ logarithm</em>', '<span data-concept="logarithms"><em>base-$b$ logarithm</em></span>'),
    ('logarithms', '<em>binary logarithms</em>', '<span data-concept="logarithms"><em>binary logarithms</em></span>'),
    ('logarithms', '<em>natural logarithm</em>', '<span data-concept="logarithms"><em>natural logarithm</em></span>'),
    ('logarithms', '$\\lceil\\log_2(n+1)\\rceil$', '<span data-type="cost">$\\lceil\\log_2(n+1)\\rceil$</span>'),
    ('factorials', '<em>factorial</em>', '<span data-concept="factorials-stirling"><em>factorial</em></span>'),
    ('factorials', '<em>Stirling’s Approximation</em>', '<span data-concept="factorials-stirling"><em>Stirling’s Approximation</em></span>'),
    ('factorials', '<em>binomial coefficients</em>', '<span data-concept="factorials-stirling"><em>binomial coefficients</em></span>'),
    ('factorials', 'n\\ln n - n +1$.)', 'n\\ln n - n +1$' + FN_INT + '.)'),
    ('harmonic', '<em>harmonic number</em>', '<span data-concept="harmonic-numbers"><em>harmonic number</em></span>'),
    ('harmonic', 'the natural logarithm of $k$', 'the <span data-concept="logarithms">natural logarithm</span> of $k$'),
    ('harmonic', '\\ln k < H_k \\le \\ln k + 1 \\enspace .$$', '\\ln k < H_k \\le \\ln k + 1 \\enspace .$$' + FN_K),
]

# ---------------------------------------------------------------- derivations (root item 29, docs/prompts/derivations.md)
# Every line is checked numerically by check_derivations() below for k = 1..50 (the bounds) and k = 2..10⁶ (the base).
INT_K = '\\int_1^{k} (1/x)\\,\\mathrm{d}x'
DERIVATIONS = [
    {'id': 'change-of-base', 'what': 'ln k in terms of log k', 'source': '1.2, Exponentials and Logarithms',
     'nodes': [{
         'assumes': [
             {'tex': '\\log_b k = \\frac{\\log_a k}{\\log_a b}'},
             {'text': '$\\log k$ is shorthand for $\\log_2 k$.'},
             {'text': '$\\log_b k$ is the unique value $x$ that satisfies $b^x = k$.'},
         ],
         'then': {'tex': '\\mk{L}{\\ln k} = \\mk{R}{\\log_e k}'},
         'steps': [
             {'tex': '\\mk{L}{\\ln k} = \\frac{\\mk{N}{\\log_2 k}}{\\mk{D}{\\log_2 e}}', 'uses': [0], 'map': {'R': ['N', 'D']},
              'cap': 'Change the base from $e$ to $2$: the rule with $b = e$ and $a = 2$.'},
             {'tex': '\\mk{L}{\\ln k} = \\frac{\\mk{N}{\\log k}}{\\mk{D}{\\log e}}', 'uses': [1]},
             {'tex': '\\mk{L}{\\ln k} = \\frac{\\mk{N}{\\log k}}{\\mk{D}{(\\ln e)/(\\ln 2)}}', 'uses': [0],
              'cap': 'The same rule changes $\\log e$ back to base $e$, with $b = 2$, $a = e$ and $e$ in place of $k$.'},
             {'tex': '\\mk{L}{\\ln k} = \\frac{\\mk{N}{\\log k}}{\\mk{D}{1/(\\ln 2)}}', 'uses': [2], 'cap': 'Since $e^1 = e$, $\\ln e = 1$.'},
             {'tex': '\\mk{L}{\\ln k} = \\mk{D}{(\\ln 2)}\\mk{N}{(\\log k)}'},
             {'tex': '\\mk{L}{\\ln k} \\approx \\mk{D}{0.693147}\\mk{N}{\\log k}'},
         ],
     }]},
    {'id': 'harmonic-bounds', 'what': 'the bounds on Hₖ', 'source': '1.2, Harmonic Numbers',
     'nodes': [
         {   # the lower bound: rectangles over the curve, standing on [i, i + 1]
             'assumes': [
                 {'text': 'An integral can be interpreted as the area between a curve and the $x$-axis.'},
                 {'tex': INT_K + ' = \\ln k', 'src': '1.2, Exponentials and Logarithms'},
             ],
             'then': {'tex': '\\mk{H}{H_k} = \\mk{S}{1 + 1/2 + 1/3 + \\cdots + 1/k}'},
             'steps': [
                 {'tex': '\\mk{H}{H_k} \\ge \\mk{S}{\\int_1^{k+1} (1/x)\\,\\mathrm{d}x}', 'uses': [0],
                  'cap': 'Stand a rectangle of width 1 and height $1/i$ on $[i, i+1]$ for $i = 1, \\ldots, k$. Since $1/x \\le 1/i$ there, the rectangles, of total area $H_k$, cover the area under the curve from $1$ to $k + 1$.'},
                 {'tex': '\\mk{H}{H_k} > \\mk{S}{' + INT_K + '}', 'uses': [0],
                  'cap': 'The area under the curve from $k$ to $k + 1$ is more than zero.'},
                 {'tex': '\\mk{H}{H_k} > \\mk{S}{\\ln k}', 'uses': [1]},
             ],
         },
         {   # the upper bound: the first rectangle, then the rest under the curve, standing on [i − 1, i]
             'assumes': [
                 {'text': 'An integral can be interpreted as the area between a curve and the $x$-axis.'},
                 {'tex': INT_K + ' = \\ln k', 'src': '1.2, Exponentials and Logarithms'},
             ],
             'then': {'tex': '\\mk{H}{H_k} = \\mk{S}{1 + 1/2 + 1/3 + \\cdots + 1/k}'},
             'steps': [
                 {'tex': '\\mk{H}{H_k} = \\mk{one}{1} + \\mk{S}{(1/2 + 1/3 + \\cdots + 1/k)}', 'map': {'S': ['one', 'S']}},
                 {'tex': '\\mk{H}{H_k} \\le \\mk{one}{1} + \\mk{S}{' + INT_K + '}', 'uses': [0],
                  'cap': 'Stand a rectangle of width 1 and height $1/i$ on $[i-1, i]$ for $i = 2, \\ldots, k$. Since $1/x \\ge 1/i$ there, these rectangles fit under the curve from $1$ to $k$.'},
                 {'tex': '\\mk{H}{H_k} \\le \\mk{one}{1} + \\mk{S}{\\ln k}', 'uses': [1]},
             ],
         },
         {   # the two joined, as the book prints them
             'assumes': [{'step': 0}, {'step': 1}],
             'then': {'tex': '\\mk{H}{H_k} > \\mk{S}{\\ln k}'},
             'steps': [
                 {'tex': '\\mk{S}{\\ln k} < \\mk{H}{H_k} \\le \\mk{hi}{\\ln k + 1}', 'uses': [1]},
             ],
         },
     ]},
]


def check_derivations():
    """Each line of each derivation, read as a relation between numbers, holds (k = 1..50; the change of base for
    k = 2..10⁶ at eight points)."""
    import math
    H = lambda k: sum(1 / i for i in range(1, k + 1))
    for k in range(1, 51):
        assert H(k) >= math.log(k + 1) - 1e-12 and H(k) > math.log(k) and H(k) <= 1 + math.log(k) + 1e-12
        assert math.isclose(H(k) - 1, sum(1 / i for i in range(2, k + 1)))
    for k in (2, 3, 10, 1000, 12345, 10 ** 6, 2.5, 7):
        L = math.log(k)
        assert math.isclose(L, math.log2(k) / math.log2(math.e))
        assert math.isclose(L, math.log2(k) / (math.log(math.e) / math.log(2)))
        assert math.isclose(L, math.log(2) * math.log2(k))
        assert abs(L - 0.693147 * math.log2(k)) < 1e-6 * math.log2(k)
    return True

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]
SECTION = {
    'id': '1.2', 'chapter': '1', 'title': 'Logarithms, factorials and harmonic numbers', 'short': 'Logarithms and factorials',
    'lead': ('An Essential section on three functions that turn up in running times, '
             '<span data-concept="logarithms">logarithms</span>, '
             '<span data-concept="factorials-stirling">factorials</span> and '
             '<span data-concept="harmonic-numbers">harmonic numbers</span>; harmonic numbers are Advanced. '
             'log with no base means log<sub>2</sub>, and ln is the natural logarithm. Harmonic numbers return with '
             'random binary search trees in <a href="/cs-interview-prep-ultra/ch08/8.6/">8.6</a>.'),
    'objectives': [], 'summary_html': '',
    'notes': ('The opening of ODS’s Mathematical Background, which points to Lehman, Leighton and Meyer’s textbook, and '
              'the rest of its random binary search tree section are left out here.'),
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'figures': [
        {'id': 'sim-halving', 'kind': 'sim', 'ai': FIG_AI},
        {'id': 'sim-stirling', 'kind': 'sim', 'ai': FIG_AI},
        {'id': 'sim-harmonic', 'kind': 'sim', 'originals': ['/media/ch01/ods-harmonic-2.png', '/media/ch01/ods-harmonic-3.png'],
         'original_caption': '{{caption-text harmonic-integral}}', 'ai': FIG_AI},
    ],
    'referents': [],
    'coverage': [
        {'span': 'logarithms', 'concept': 'logarithms', 'verb': 'introduces'},
        {'span': 'factorials', 'concept': 'factorials-stirling', 'verb': 'introduces'},
        {'span': 'factorials', 'concept': 'logarithms', 'verb': 'uses'},
        {'span': 'harmonic', 'concept': 'harmonic-numbers', 'verb': 'introduces'},
        {'span': 'harmonic', 'concept': 'logarithms', 'verb': 'uses'},
    ],
    'footnotes_extra': [
        {'id': 'err-integral-n', 'kind': 'correction',
         'html': 'The integral is printed with $n$ as its variable of integration as well as its upper limit; it reads '
                 '$\\int_1^n \\ln x\\,\\mathrm{d}x = n\\ln n - n + 1$.'},
        {'id': 'err-harmonic-k', 'kind': 'correction',
         'html': 'The bound holds for every integer $k \\ge 1$. The definition is printed for a non-negative integer $k$, '
                 'but at $k = 0$ the sum is empty and $\\ln 0$ is undefined, so the bound says nothing there.'},
    ],
    'derivations': DERIVATIONS,
}

SECTION['exercise_notes'] = (
    'The OpenDSA items the chapter config lists for this section (logarithms_1, logarithms_1.5 and logarithms_2 with '
    'MathLogSumm, MthBgFIBlgbs1 and MthBgFIBlgbs2) wait for the converter of OpenDSA’s Khan-format exercises; '
    'AlgAnlsFIBsmlintgr2 asks for a Big-O bound and is held for 1.3. Aspnes’s A.5.2, comparing products, waits for a '
    'transcription of its displayed products from the PDF. The keyed MIT 6.042J card on integral bounds for sums '
    '(Fall 2005, problem set 6, problem 7) waits for the app to read a section’s NC card file. MCS problems 14.12–14.17 '
    'have no published answers and are built on block stacking, and are left out; Aspnes’s B.1.1 and Erickson’s '
    'Factorial item are held for chapter 4, Kattis inversefactorial is over the cap of two code items per concept, and '
    'Project Euler 20 and 34 print no answers. The grains tests are Exercism’s canonical data and its references are '
    'written by the AI that built the section; the Kattis items keep their sample as the visible test, and their other '
    'tests and references are written by the same AI.')

EXERCISE_FILES = {
    'grains': 'sources/_cache/exercism/exercises/grains',
    'howmanydigits': 'sources/_cache/kattis/problems/howmanydigits.html',
    'stirlingsapproximation': 'sources/_cache/kattis/problems/stirlingsapproximation.html',
}
KATTIS_SAMPLES = 'sources/_cache/kattis/samples'

GRAINS_PY = '''def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)
'''
GRAINS_JS = '''class ValueError extends Error {
  constructor(message) { super(message); this.name = 'ValueError'; }
}

function square(number) {
  if (!(number >= 1 && number <= 64)) throw new ValueError('square must be between 1 and 64');
  return 2 ** (number - 1);
}
'''
DIGITS_PY = '''import math
import sys


def digits_of_factorial(n):
    # n! has floor(log10 n!) + 1 digits; lgamma(n + 1) is ln n!
    if n <= 1:
        return 1
    return math.floor(math.lgamma(n + 1) / math.log(10)) + 1


for token in sys.stdin.read().split():
    print(digits_of_factorial(int(token)))
'''
DIGITS_JS = '''const fs = require('fs');
const ns = fs.readFileSync(0, 'utf8').split(/\\s+/).filter(Boolean).map(Number);
// log10 n! for every n up to the largest asked, summed with compensation so the floor is exact
const top = Math.max(1, ...ns);
const log10Fact = new Float64Array(top + 1);
let sum = 0, carry = 0;
for (let i = 2; i <= top; i++) {
  const y = Math.log10(i) - carry, t = sum + y;
  carry = (t - sum) - y; sum = t; log10Fact[i] = sum;
}
console.log(ns.map((n) => (n <= 1 ? 1 : Math.floor(log10Fact[n]) + 1)).join('\\n'));
'''
STIRLING_PY = '''import math
import sys


def ratio(n):
    # n! / S(n) = e^alpha(n): alpha from lgamma for small n, from its series for large n
    if n <= 100:
        alpha = math.lgamma(n + 1) - (0.5 * math.log(2 * math.pi * n) + n * math.log(n) - n)
    else:
        alpha = 1 / (12 * n) - 1 / (360 * n ** 3) + 1 / (1260 * n ** 5)
    return math.exp(alpha)


for token in sys.stdin.read().split():
    n = int(token)
    if n == 0:
        break
    print(f"{ratio(n):.12f}")
'''
STIRLING_JS = '''const fs = require('fs');
const ns = fs.readFileSync(0, 'utf8').split(/\\s+/).filter(Boolean).map(Number);
const out = [];
for (const n of ns) {
  if (n === 0) break;
  let alpha;
  if (n <= 100) {
    let lnFact = 0;
    for (let i = 2; i <= n; i++) lnFact += Math.log(i);
    alpha = lnFact - (0.5 * Math.log(2 * Math.PI * n) + n * Math.log(n) - n);
  } else {
    alpha = 1 / (12 * n) - 1 / (360 * n ** 3) + 1 / (1260 * n ** 5);
  }
  out.push(Math.exp(alpha).toFixed(12));
}
console.log(out.join('\\n'));
'''


def _kattis_prompt(path):
    """A Kattis statement as the card's prompt: its paragraphs, its Input and Output headings, its maths as $…$;
    the sample table is the card's visible test."""
    import html as H
    import re
    s = open(path, encoding='utf-8').read()
    body = s[s.index('<div class="problembody">'):]
    body = body[:body.index('<table class="sample"')]
    body = re.sub(r'<span class="tex2jax_process">\\\[(.*?)\\\]</span>', lambda m: '<p>$$' + m.group(1) + '$$</p>', body, flags=re.S)
    body = re.sub(r'<span class=\s*"tex2jax_process">(.*?)</span>', lambda m: m.group(1), body, flags=re.S)
    parts = re.findall(r'<(p|h2)>(.*?)</\1>', body, flags=re.S)
    out = []
    for tag, t in parts:
        t = ' '.join(H.unescape(t).split())
        t = re.sub(r'(\d)\\, (\d)', r'\1\\,\2', t)          # "10\, 000" as the statement sets it, without the line break's space
        # the text is HTML again: a < inside maths is written \lt, so that no bare < stands in the prompt
        t = t.replace(' < ', ' \\lt ') if '$' in t else H.escape(t, quote=False)
        out.append(f'<strong>{t}</strong>' if tag == 'h2' else t)
    return '\n\n'.join(out)


def _sample(slug):
    import os
    import zipfile
    z = zipfile.ZipFile(os.path.join(BOOK_ROOT, KATTIS_SAMPLES, slug + '.zip'))
    return z.read('sample.in').decode(), z.read('sample.ans').decode()


def _run(src, stdin):
    import subprocess
    import sys
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = d + '/ref.py'
        open(p, 'w').write(src)
        return subprocess.run([sys.executable, '-I', p], input=stdin, capture_output=True, text=True, cwd=d, check=True).stdout


def _stirling_exact(n, digits=40):
    """n!/S(n) in Decimal arithmetic, to check the AI tests."""
    from decimal import Decimal, getcontext
    import math
    getcontext().prec = digits + 20
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239)
    def atan_inv(x):
        x = Decimal(x); t = 1 / x; s = t; k = 1; x2 = x * x
        while True:
            t = t / x2; term = t / (2 * k + 1)
            if term == 0 or abs(term) < Decimal(10) ** (-(digits + 15)): break
            s += -term if k % 2 else term; k += 1
        return s
    pi = 16 * atan_inv(5) - 4 * atan_inv(239)
    N = Decimal(n)
    S = (2 * pi * N).sqrt() * ((N.ln() - 1) * N).exp()      # sqrt(2 pi n) (n/e)^n
    return Decimal(math.factorial(n)) / S


BOOK_ROOT = None


def EXERCISES(exercism, book):
    import json
    import math
    import os
    import re
    global BOOK_ROOT
    BOOK_ROOT = book
    exs, concepts = [], []

    # Exercism grains: the square property only, the canonical data as its tests
    g = os.path.join(book, EXERCISE_FILES['grains'])
    instr = open(os.path.join(g, 'instructions.md'), encoding='utf-8').read()
    instr = re.sub(r'^# Instructions\s*', '', instr).strip()
    paras = []
    for p in re.split(r'\n\s*\n', instr):
        lines = p.split('\n')
        if all(l.startswith('- ') for l in lines):
            paras.append('<ul>' + ''.join(f'<li>{l[2:].strip()}</li>' for l in lines) + '</ul>')
        else:
            paras.append(' '.join(l.strip() for l in lines))
    data = json.load(open(os.path.join(g, 'canonical-data.json'), encoding='utf-8'))
    cases = []

    def walk(c):
        for x in c.get('cases', []):
            if 'cases' in x:
                walk(x)
            elif x['property'] == 'square':
                cases.append(x)
    walk(data)
    tests = []
    for i, c in enumerate(cases):
        t = {'args': [c['input']['square']], 'visible': i == 0 or c['input']['square'] == 0, 'generated_by': 'source'}
        if isinstance(c['expected'], dict):
            t['raises'] = 'ValueError'
        else:
            t['expect'] = c['expected']
        tests.append(t)
    exs.append({
        'id': 'c1', 'source_id': 'exercism:grains', 'source_number': 'grains', 'origin': 'exercism', 'kind': 'code',
        'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'logarithms',
        'changes': 'Only the number of grains on a given square is asked for and tested; the total is left out.',
        'prompt': '\n\n'.join(paras),
        'answer': {'type': 'code',
                   'python': {'entry': 'square', 'starter': 'def square(number):\n    pass\n', 'reference': GRAINS_PY, 'generated_by': 'ai'},
                   'javascript': {'entry': 'square', 'starter': 'function square(number) {\n}\n', 'reference': GRAINS_JS, 'generated_by': 'ai'},
                   'tests': tests, 'generated_by': 'source'}})
    concepts.append({'exercise': 'c1', 'concept': 'logarithms'})

    # Kattis howmanydigits: the sample, then the AI's tests (checked against exact factorials where they are small)
    sin, sout = _sample('howmanydigits')
    ai_in = ['2\n4\n5\n6\n9\n11\n100\n1000\n', '1000000\n', '549545\n999999\n123456\n']
    for s in ai_in[:1]:
        for n in map(int, s.split()):
            assert int(_run(DIGITS_PY, f'{n}\n')) == len(str(math.factorial(n)))
    dtests = [{'stdin': sin, 'stdout': sout, 'visible': True, 'generated_by': 'source'}] + \
             [{'stdin': s, 'stdout': _run(DIGITS_PY, s), 'generated_by': 'ai'} for s in ai_in]
    assert _run(DIGITS_PY, sin).split() == sout.split()
    exs.append({
        'id': 'c2', 'source_id': 'kattis:howmanydigits', 'source_number': 'How Many Digits?', 'origin': 'kattis-by-sa',
        'kind': 'code', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'factorials',
        'prompt': _kattis_prompt(os.path.join(book, EXERCISE_FILES['howmanydigits'])),
        'answer': {'type': 'code',
                   'python': {'starter': 'import sys\n\nfor token in sys.stdin.read().split():\n    n = int(token)\n', 'reference': DIGITS_PY, 'generated_by': 'ai'},
                   'javascript': {'starter': "const fs = require('fs');\nconst ns = fs.readFileSync(0, 'utf8').split(/\\s+/).filter(Boolean).map(Number);\n", 'reference': DIGITS_JS, 'generated_by': 'ai'},
                   'tests': dtests, 'compare': 'tokens', 'generated_by': 'ai'}})
    concepts += [{'exercise': 'c2', 'concept': 'logarithms'}, {'exercise': 'c2', 'concept': 'factorials-stirling'}]

    # Kattis stirlingsapproximation: the sample, then the AI's tests, checked in Decimal arithmetic to 1e-10
    sin, sout = _sample('stirlingsapproximation')
    ai_in = ['2\n3\n4\n5\n0\n', '100\n101\n1000\n0\n', '99999\n100000\n0\n', '7\n0\n']
    stests = [{'stdin': sin, 'stdout': sout, 'visible': True, 'generated_by': 'source'}]
    for s in ai_in:
        got = _run(STIRLING_PY, s)
        ns = [int(t) for t in s.split()][:-1]
        for n, v in zip(ns, got.split()):
            if n <= 3000:
                assert abs(float(_stirling_exact(n)) - float(v)) < 1e-10, (n, v)
        stests.append({'stdin': s, 'stdout': got, 'generated_by': 'ai'})
    for a, b in zip(_run(STIRLING_PY, sin).split(), sout.split()):
        assert abs(float(a) - float(b)) < 1e-10
    exs.append({
        'id': 'c3', 'source_id': 'kattis:stirlingsapproximation', 'source_number': 'Stirling’s Approximation', 'origin': 'kattis-by-sa',
        'kind': 'code', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'factorials',
        'prompt': _kattis_prompt(os.path.join(book, EXERCISE_FILES['stirlingsapproximation'])),
        'answer': {'type': 'code',
                   'python': {'starter': 'import sys\n\nfor token in sys.stdin.read().split():\n    n = int(token)\n    if n == 0:\n        break\n', 'reference': STIRLING_PY, 'generated_by': 'ai'},
                   'javascript': {'starter': "const fs = require('fs');\nconst ns = fs.readFileSync(0, 'utf8').split(/\\s+/).filter(Boolean).map(Number);\n", 'reference': STIRLING_JS, 'generated_by': 'ai'},
                   'tests': stests, 'compare': 'tokens', 'tol': 1e-8, 'generated_by': 'ai'}})
    concepts.append({'exercise': 'c3', 'concept': 'factorials-stirling'})
    return exs, concepts
