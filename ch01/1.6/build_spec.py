"""What tools/build_text.py needs to assemble 1.6 Counting and expected value (the plan is plan.md beside this file).

Everything here is placement, markup or a small correction of what the extraction gets wrong; the source's
words come from the converters: Brisk Walk and Open Data Structures from their LaTeX (tools/read_latex.py),
MCS 2018 from its PDF glyph by glyph (tools/extract_mcs.py). Each FIXES entry says why it is there.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BOOK = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_BOOK, 'tools'))
import read_latex  # noqa: E402

TITLE = 'Counting and expected value'
BRISK = 'sources/_cache/brisk/'
ODS = 'sources/_cache/ods/latex/'

BLOCKS = [
    dict(id='counting', source='brisk', reader='latex', dialect='brisk', file=BRISK + 'counting.tex', chapter=6,
         parts=[('\\section{The Fundamental Theorem}', '\\subsection{Enumerating permutations}'),
                ('\\subsection{Partial permutations}', '\\section{Summary}')],
         locator='brisk:counting#The Fundamental Theorem (with “A simple trick”), #Permutations (with “Partial permutations”; '
                 '“Enumerating permutations” left out), #Combinations (with “Binomial coefficients”)',
         h2='Counting'),
    dict(id='probability', source='brisk', reader='latex', dialect='brisk', file=BRISK + 'probability.tex', chapter=4,
         parts=[('\\section{Outcomes and events}', '\\section{Philosophical interlude}')], drop_first_heading=True,
         locator='brisk:probability#Outcomes and events, #Probability measures', h2='Outcomes and events'),
    dict(id='interlude', source='brisk', reader='latex', dialect='brisk', file=BRISK + 'probability.tex', chapter=4,
         parts=[('\\section{Philosophical interlude}', '\\section{Conditional probability}')], drop_first_heading=True,
         locator='brisk:probability#Philosophical interlude', h2='Philosophical interlude'),
    dict(id='conditional', source='brisk', reader='latex', dialect='brisk', file=BRISK + 'probability.tex', chapter=4,
         parts=[('\\section{Conditional probability}', '\\section{Total probability}'), ('\\section{Independence}', None)],
         drop_first_heading=True,
         locator='brisk:probability#Conditional probability, #Independence (with “Whoops!”)', h2='Conditional probability'),
    dict(id='random-variable', source='mcs2018', reader='mcs', pdf='sources/_cache/mcs2018/mcs.pdf', pages=[865, 866, 867],
         **{'from': '19.1 Random Variable Examples', 'to': '19.2 Independence'}, drop_first_heading=True,
         locator='mcs2018:19.1, from Definition 19.1.1 through 19.1.2, before 19.2 (the chapter 19 opening left out)',
         h2='Random Variable Examples'),
    dict(id='linearity', source='ods', reader='latex', dialect='ods', file=ODS + 'intro.tex', chapter=1,
         parts=[('\\subsection{Randomization and Probability}', 'A useful trick, that we will use')], drop_first_heading=True,
         locator='ods:intro#sec:randomization, from the start to “…into sums of simpler random variables (the right hand sides).”',
         h2='Randomization and Probability'),
    dict(id='indicators', source='ods', reader='latex', dialect='ods', file=ODS + 'intro.tex', chapter=1,
         parts=[('A useful trick, that we will use', '\\section{The Model of Computation}')],
         locator='ods:intro#sec:randomization, from “A useful trick…” to the end of the subsection',
         h2='Indicator random variables'),
    dict(id='coin-tosses', source='ods', reader='latex', dialect='ods', file=ODS + 'skiplists.tex', chapter=4,
         parts=[('\\begin{lem}\\lemlabel{coin-tosses}', 'The next two lemmata')],
         locator='ods:skiplists#lem:coin-tosses, the lemma and its proof', h2='Tosses until the first head'),
]


# References to places this page does not carry (plans-summary question 4: the source's words, the reference
# as plain text, no link). \ref prints Brisk Walk's own number; a page this book has no copy of is named by
# the Brisk Walk section that holds it, in square brackets.
LATEX_REFS = {
    'complement': ('[<em>Brisk Walk</em> §2.9]', '[Brisk Walk §2.9]'),
    'totalprob': ('[<em>Brisk Walk</em> §4.5]', '[Brisk Walk §4.5]'),
}

# The printed chains the derivations replace (plans-summary question 28; the plan's Derivation candidates).
REPLACE = [
    ('indicators', r'\sum_{i=0}^k i\cdot\Pr\{X=i\}', 'drv-heads-sum'),
    ('indicators', r'\sum_{i=1}^k 1/2', 'drv-heads'),
    ('coin-tosses', r'1 + 1/2 + 1/4 + 1/8', 'drv-coin-tosses'),
]
ENV_EYEBROW = {('counting', 'framed'): 'The Fundamental Theorem of Counting'}
FIGURE_AT = {'venn': 'sim-idol-venn', 'pascal': 'sim-pascal'}

# MCS's displays: the PDF draws the underbraces and fractions in pieces, so each is set here in LaTeX from the
# page render (PDF pp. 865–867, printed 857–859), keyed by page and order on the page.
DISPLAYS = {
    'p865#1': r'\mathcal{S} = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}.',
    'p865#2': r'\begin{aligned} C(HHH) &= 3 &\qquad C(THH) &= 2\\ C(HHT) &= 2 & C(THT) &= 1\\ C(HTH) &= 2 & C(TTH) &= 1\\ C(HTT) &= 1 & C(TTT) &= 0. \end{aligned}',
    'p866#1': r'\begin{aligned} M(HHH) &= 1 &\qquad M(THH) &= 0\\ M(HHT) &= 0 & M(THT) &= 0\\ M(HTH) &= 0 & M(TTH) &= 0\\ M(HTT) &= 0 & M(TTT) &= 1. \end{aligned}',
    'p866#2': r'\underbrace{HHH\quad TTT}_{M=1}\quad \underbrace{HHT\quad HTH\quad HTT\quad THH\quad THT\quad TTH}_{M=0}.',
    'p866#3': r'\underbrace{TTT}_{C=0}\quad \underbrace{TTH\quad THT\quad HTT}_{C=1}\quad \underbrace{THH\quad HTH\quad HHT}_{C=2}\quad \underbrace{HHH}_{C=3}.',
    'p866#4': r'[C = 2] = \{THH, HTH, HHT\},',
    'p867#1': r'\Pr[C = 2] = \Pr[THH] + \Pr[HTH] + \Pr[HHT] = \frac{1}{8} + \frac{1}{8} + \frac{1}{8} = 3/8.',
    'p867#2': r'[C \le 1] = \{TTT, TTH, THT, HTT\},',
    'p867#3': r'[C \cdot M \text{ is odd}] = \{HHH\}.',
}

# (what the extraction gives, what the page prints, why)
FIXES = []

AI = 'claude-opus-5-5 high'


def sim(fid, caption, original=None, original_caption=None):
    import html
    attrs = f'class="sim" id="{fid}"'
    if original:
        attrs += f' data-original="{original}" data-original-caption="{html.escape(original_caption, quote=True)}"'
    return f'<figure {attrs}>\n  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>'


CAPTIONS = {}
for _f, _ch in (('probability.tex', 4), ('counting.tex', 6)):
    CAPTIONS.update(read_latex.figure_captions(os.path.join(_BOOK, BRISK, _f), _ch, 'brisk'))

N = '<span data-type="size"><em>n</em></span>'
K = '<span data-type="size"><em>k</em></span>'
HTML = {
    'sim-pascal': sim(
        'sim-pascal',
        f'Pascal’s triangle down to row {N}. Each entry is the sum of the two entries above it, and the entry at place {K} of row '
        f'{N} is the number of ways to choose {K} things out of {N}: <em>n</em>!/((<em>n</em> − <em>k</em>)! <em>k</em>!). '
        'Every row starts and ends with 1, reads the same from either end, and is largest in the middle.',
        '/media/ch01/brisk-6-1-pascal.png', CAPTIONS['pascal']['text']),
    'sim-idol-venn': sim(
        'sim-idol-venn',
        'The four outcomes of <em>All-time Idol</em>, '
        '<span data-ref="kelly">Kelly</span>, <span data-ref="fantasia">Fantasia</span>, <span data-ref="carrie">Carrie</span> '
        'and <span data-ref="david">David</span>, with their probabilities, and the events <span data-ref="F"><em>F</em></span>, '
        '<span data-ref="R"><em>R</em></span>, <span data-ref="U"><em>U</em></span> and <span data-ref="C"><em>C</em></span> '
        'as closed curves round the outcomes they hold. A union counts an outcome in the overlap once. Given an event, only '
        'its own outcomes are left, and a conditional probability is the share of what is left.',
        '/media/ch01/brisk-4-1-venn.png', CAPTIONS['venn']['text']),
    'drv-heads-sum': '<figure class="dv" id="drv-heads-sum"></figure>',
    'drv-heads': '<figure class="dv" id="drv-heads"></figure>',
    'drv-coin-tosses': '<figure class="dv" id="drv-coin-tosses"></figure>\n' + sim(
        'sim-coin-tosses',
        'Fair coin tosses run after run, each run a row of indicator variables <em>I</em><sub>1</sub>, <em>I</em><sub>2</sub>, …, '
        'a filled cell for 1. Averaged over the runs, each column settles near its expectation, and the mean count near the sum '
        'of those expectations: half the tosses come up heads, and the first head takes two tosses on average.'),
}

ERR = lambda nid: f'<sup class="fn" data-note="{nid}"></sup>'   # noqa: E731
# (block, text as built, replacement, [count]): links to the figures the prose cites by the source's number,
# the errata's markers, the spans that introduce each concept and the referents the figures draw.
MARKS = [
    # the figures the prose cites, linked (plans-summary question 18)
    ('counting', 'as in Figure 6.1.', 'as in <a href="#sim-pascal">Figure 6.1</a>.'),
    ('probability', 'Consider Figure 4.1,', 'Consider <a href="#sim-idol-venn">Figure 4.1</a>,'),
    ('conditional', 'Looking back at Figure 4.1,', 'Looking back at <a href="#sim-idol-venn">Figure 4.1</a>,'),
    # errata
    ('counting', '283,290,685,487,972,352</p>', '283,290,685,487,972,352' + ERR('err-52') + '</p>'),
    ('probability', 'the total number of events is the probability.', 'the total number of events is the probability.' + ERR('err-outcomes')),
    ('probability', 'Pr($P$) = .7, since this is the sum of Kelly’s and David’s probabilities.',
     'Pr($P$) = .7' + ERR('err-p-r') + ', since this is the sum of Kelly’s and David’s probabilities.'),
    # concepts
    ('counting', '<strong>The Fundamental Theorem of Counting</strong>', '<strong><span data-concept="counting">The Fundamental Theorem of Counting</span></strong>'),
    ('counting', '<strong>permutation</strong>', '<strong><span data-concept="counting">permutation</span></strong>'),
    ('counting', '<strong>partial permutation</strong>', '<strong><span data-concept="counting">partial permutation</span></strong>'),
    ('counting', '<strong>combination</strong>', '<strong><span data-concept="counting">combination</span></strong>'),
    ('counting', '<strong>binomial coefficients</strong>', '<strong><span data-concept="counting">binomial coefficients</span></strong>'),
    ('probability', '<strong>outcome</strong>', '<strong><span data-concept="probability-basics">outcome</span></strong>'),
    ('probability', '<strong>sample space</strong>', '<strong><span data-concept="probability-basics">sample space</span></strong>'),
    ('probability', '<strong>event</strong>', '<strong><span data-concept="probability-basics">event</span></strong>'),
    ('probability', '<strong>probability measure</strong>', '<strong><span data-concept="probability-basics">probability measure</span></strong>'),
    ('conditional', '<strong>conditional probability</strong>', '<strong><span data-concept="conditional-probability">conditional probability</span></strong>'),
    ('conditional', '<strong>independent</strong>', '<strong><span data-concept="conditional-probability">independent</span></strong>'),
    ('random-variable', '<em>random variable</em>', '<span data-concept="random-variable"><em>random variable</em></span>'),
    ('linearity', '<em>expected value</em>', '<span data-concept="linearity-of-expectation"><em>expected value</em></span>'),
    ('linearity', '<em>linearity of expectation</em>', '<span data-concept="linearity-of-expectation"><em>linearity of expectation</em></span>'),
    ('indicators', '<em>indicator random variables</em>', '<span data-concept="indicator-variables"><em>indicator random variables</em></span>'),
    ('coin-tosses', 'the number of times a fair coin is tossed up to and including the first time the coin comes up heads',
     '<span data-concept="geometric-expectation">the number of times a fair coin is tossed up to and including the first time the coin comes up heads</span>'),
    # referents sim-idol-venn draws
    ('probability', 'Kelly Clarkson (20)', '<span data-ref="kelly">Kelly Clarkson</span> (20)'),
    ('probability', 'Fantasia Barrino (20)', '<span data-ref="fantasia">Fantasia Barrino</span> (20)'),
    ('probability', 'Carrie Underwood (22)', '<span data-ref="carrie">Carrie Underwood</span> (22)'),
    ('probability', 'David Cook (26)', '<span data-ref="david">David Cook</span> (26)'),
    ('probability', 'Define $F$ as the event', 'Define <span data-ref="F">$F$</span> as the event'),
    ('probability', '$R$ is the event that the winner is a rock musician', '<span data-ref="R">$R$</span> is the event that the winner is a rock musician'),
    ('probability', '$U$ is the event that the winner is underage', '<span data-ref="U">$U$</span> is the event that the winner is underage'),
    ('probability', 'defined the event $C$ as a country singer', 'defined the event <span data-ref="C">$C$</span> as a country singer'),
    ('conditional', 'eliminates Dave from consideration', 'eliminates <span data-ref="david">Dave</span> from consideration'),
    ('conditional', 'In this case $F$ is the background knowledge', 'In this case <span data-ref="F">$F$</span> is the background knowledge'),
]

# ---------------------------------------------------------------- derivations (docs/prompts/derivations.md)
LIN = r'\mathrm{E}\left[\sum_{i=1}^k X_i\right] = \sum_{i=1}^k \mathrm{E}[X_i]'
DERIVATIONS = [
    {'id': 'heads-sum', 'what': 'the expected number of heads in k tosses, from the definition of expected value',
     'source': 'Open Data Structures, 1.3.4 Randomization and Probability',
     'nodes': [{
         'assumes': [
             {'tex': r'\mathrm{E}[X] = \sum_{x\in U} x\cdot\Pr\{X=x\}', 'src': 'Randomization and Probability'},
             {'tex': r'\Pr\{X=i\} = \binom{k}{i}/2^k'},
             {'tex': r'i\binom{k}{i} = k\binom{k-1}{i-1}'},
             {'tex': r'\sum_{i=0}^{k}\binom{k}{i} = 2^{k}'},
         ],
         'then': {'tex': r'\mk{E}{\mathrm{E}[X]} = \mk{S}{\sum_{i=0}^k i\cdot\Pr\{X=i\}}', 'uses': [0],
                  'why': 'The number of heads $X$ takes the values $0, 1, \\ldots, k$.'},
         'steps': [
             {'tex': r'\mk{E}{\mathrm{E}[X]} = \mk{S}{\sum_{i=0}^k i\cdot\binom{k}{i}/2^k}', 'uses': [1]},
             {'tex': r'\mk{E}{\mathrm{E}[X]} = \mk{S}{\sum_{i=1}^k k\binom{k-1}{i-1}/2^k}', 'uses': [2],
              'cap': 'The term for $i = 0$ is zero, so the sum may start at $i = 1$.'},
             {'tex': r'\mk{E}{\mathrm{E}[X]} = \mk{k}{k}\cdot \mk{S}{\sum_{i=0}^{k-1}\binom{k-1}{i}/2^k}', 'uses': [],
              'cap': 'The factor $k$ comes out of the sum, and the index is shifted down by one.', 'map': {'S': ['k', 'S']}},
             {'tex': r'\mk{E}{\mathrm{E}[X]} = \mk{k}{k}\cdot \mk{S}{2^{k-1}/2^k}', 'uses': [3],
              'cap': 'With $k - 1$ in place of $k$.'},
             {'tex': r'\mk{E}{\mathrm{E}[X]} = \mk{S}{k/2}', 'uses': [], 'map': {'k': 'S'}},
         ],
         'src': 'Randomization and Probability'}]},
    {'id': 'heads', 'what': 'the expected number of heads in k tosses, with indicator variables',
     'source': 'Open Data Structures, 1.3.4 Randomization and Probability',
     'nodes': [{
         'assumes': [
             {'text': '$X = \\sum_{i=1}^k I_i$, where $I_i$ is 1 if the $i$th toss is heads and 0 otherwise.'},
             {'tex': r'\mathrm{E}[I_i] = (1/2)1 + (1/2)0 = 1/2'},
             {'tex': LIN, 'src': 'Randomization and Probability, linearity of expectation'},
         ],
         'then': {'tex': r'\mk{E}{\mathrm{E}[X]} = \mk{S}{\mathrm{E}\left[\sum_{i=1}^k I_i\right]}', 'uses': [0]},
         'steps': [
             {'tex': r'\mk{E}{\mathrm{E}[X]} = \mk{S}{\sum_{i=1}^k \mathrm{E}[I_i]}', 'uses': [2]},
             {'tex': r'\mk{E}{\mathrm{E}[X]} = \mk{S}{\sum_{i=1}^k 1/2}', 'uses': [1]},
             {'tex': r'\mk{E}{\mathrm{E}[X]} = \mk{S}{k/2}', 'uses': []},
         ],
         'src': 'Randomization and Probability'}]},
    {'id': 'coin-tosses', 'what': 'the expected number of tosses until the first head',
     'source': 'Open Data Structures, 4.4 Analysis of Skiplists, the coin-tosses lemma',
     'nodes': [{
         'assumes': [
             {'text': '$T = \\sum_{i=1}^{\\infty} I_i$, where $I_i$ is 1 if the coin is tossed $i$ or more times and 0 otherwise.'},
             {'text': '$I_i = 1$ if and only if the first $i - 1$ coin tosses are tails, so $\\mathrm{E}[I_i] = \\Pr\\{I_i = 1\\} = 1/2^{i-1}$.'},
             {'tex': LIN, 'src': 'Randomization and Probability, linearity of expectation'},
         ],
         'then': {'tex': r'\mk{E}{\mathrm{E}[T]} = \mk{S}{\mathrm{E}\left[\sum_{i=1}^\infty I_i\right]}', 'uses': [0]},
         'steps': [
             {'tex': r'\mk{E}{\mathrm{E}[T]} = \mk{S}{\sum_{i=1}^\infty \mathrm{E}\left[I_i\right]}', 'uses': [2],
              'cap': 'Linearity is stated for finitely many random variables; it carries over to this infinite sum because every $I_i$ is non-negative.'},
             {'tex': r'\mk{E}{\mathrm{E}[T]} = \mk{S}{\sum_{i=1}^\infty 1/2^{i-1}}', 'uses': [1]},
             {'tex': r'\mk{E}{\mathrm{E}[T]} = \mk{S}{1 + 1/2 + 1/4 + 1/8 + \cdots}', 'uses': []},
             {'tex': r'\mk{E}{\mathrm{E}[T]} = \mk{S}{2}', 'uses': [],
              'cap': 'A geometric series with first term 1 and ratio $1/2$ sums to $1/(1 - 1/2) = 2$.'},
         ],
         'src': '4.4, the coin-tosses lemma',
         'note': 'Open Data Structures takes the second line from the first by linearity of expectation, which it states for '
                 'finitely many random variables, without remarking that the sum here is infinite. The step holds because every '
                 '$I_i$ is non-negative, so the expectation of the sum is the sum of the expectations (monotone convergence); '
                 'the work keeps the step and says why.'}]},
]


# ---------------------------------------------------------------- exercises (tools/build_section.py)
def _brisk_items(fname):
    """Brisk Walk's exercise table, item by item: (question HTML, answer HTML, footnotes), read by tools/read_latex.py.
    Each row of the longtable is `\\item question & answer`, rows parted by \\hline."""
    import re
    path = os.path.join(_BOOK, BRISK, fname)
    s = read_latex.strip_comments(open(path, encoding='utf-8').read())
    a = s.index('\\begin{longtable}')
    b = s.index('\\end{longtable}')
    body = s[s.index('\\hline', a):b]
    labels, _ = read_latex.scan_labels(path, 0)
    refs = {'license plates': (' [the license plates, under “The Fundamental Theorem”]', ''),
            'one minus trick': ('[“A simple trick”]', ''), 'prj': ('10', ''), 'prnotu': ('11', ''), 'pru': ('9', '')}
    out = []
    for row in re.split(r'\\hline', body):
        row = row.replace('\\vspace{-.2in}', '').strip()
        if '\\item' not in row:
            continue
        row = row[row.index('\\item') + len('\\item'):]
        # the column separator: the first & outside braces and maths
        depth, inmath, cut = 0, False, None
        for i, c in enumerate(row):
            if c == '\\':
                continue
            if i and row[i - 1] == '\\':
                continue
            if c == '$':
                inmath = not inmath
            elif c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
            elif c == '&' and depth == 0 and not inmath:
                cut = i
                break
        q, ans = row[:cut], row[cut + 1:]
        ans = re.sub(r'\\\\\s*$', '', ans.strip()).strip()
        q = re.sub(r'\\label\{[^}]*\}', '', q)
        ctx = read_latex.Ctx('brisk', labels, refs)
        qh = re.sub(r'(<br>\s*)+', '\n\n', read_latex.inline(q, ctx, [])).strip()
        ah = read_latex.inline(ans, ctx, ['*'] * ans.count('\\footnote{'))
        ah = re.sub(r'(\s*<br>)+\s*$', '', ah)
        out.append({'q': qh, 'a': ah, 'notes': ctx.notes})
    return out


def _para(h):
    return h.strip()


EXERCISM = 'sources/_cache/exercism/exercises/'
EXERCISM_PY = 'sources/_cache/exercism-python/exercises/practice/'

PASCAL_JS = '''function rows(count) {
  const out = [];
  for (let n = 0; n < count; n++) {
    const prev = out[n - 1] || [];
    const row = [];
    for (let k = 0; k <= n; k++) row.push(k === 0 || k === n ? 1 : prev[k - 1] + prev[k]);
    out.push(row);
  }
  return out;
}
'''
BIRTHDAY_PY = '''import random


def estimated_probability_of_shared_birthday(group_size):
    """The percentage of many random groups of group_size people in which two share a birthday."""
    trials = 20000
    shared = 0
    for _ in range(trials):
        seen = set()
        for _ in range(group_size):
            day = random.randrange(365)
            if day in seen:
                shared += 1
                break
            seen.add(day)
    return 100 * shared / trials
'''
BIRTHDAY_JS = '''function estimatedProbabilityOfSharedBirthday(groupSize) {
  const trials = 20000;
  let shared = 0;
  for (let t = 0; t < trials; t++) {
    const seen = new Set();
    for (let p = 0; p < groupSize; p++) {
      const day = Math.floor(Math.random() * 365);
      if (seen.has(day)) { shared++; break; }
      seen.add(day);
    }
  }
  return (100 * shared) / trials;
}
'''


def _exercism_prompt(slug):
    import html
    import re
    t = open(os.path.join(_BOOK, EXERCISM, slug, 'instructions.md'), encoding='utf-8').read()
    t = re.sub(r'^# Instructions\s*', '', t)
    t = re.sub(r'^\[[^\]]+\]: \S+\s*$', '', t, flags=re.M)             # link definitions
    t = re.sub(r'\[([^\]]+)\]\[[^\]]*\]', r'\1', t)                      # [text][ref] -> text
    t = re.sub(r'~~~~exercism/(note|caution)\n(.*?)~~~~', lambda m: m.group(2), t, flags=re.S)
    blocks = []
    for p in re.split(r'\n\s*\n', t.strip()):
        if p.startswith('```'):
            code = re.sub(r'^```\w*\n|\n?```$', '', p)
            blocks.append('<pre>' + html.escape(code, quote=False) + '</pre>')
        elif re.match(r'^- ', p):
            items = [html.escape(x[2:].strip(), quote=False) for x in p.split('\n') if x.startswith('- ')]
            blocks.append('<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>')
        else:
            x = html.escape(' '.join(p.split()), quote=False)
            x = re.sub(r'`([^`]+)`', r'<code>\1</code>', x)
            x = re.sub(r'_([^_]+)_', r'<em>\1</em>', x)
            blocks.append(x.replace('$', '&#36;'))
    return '\n\n'.join(blocks)


def _canonical(slug, prop):
    import json
    d = json.load(open(os.path.join(_BOOK, EXERCISM, slug, 'canonical-data.json'), encoding='utf-8'))
    out = []

    def walk(c):
        for x in c.get('cases', []):
            if 'cases' in x:
                walk(x)
            elif x['property'] == prop:
                out.append(x)
    walk(d)
    return out


def EXERCISES(exercism, book):
    ex, con = [], []
    C = _brisk_items('countingEx.tex')
    P = _brisk_items('probabilityEx.tex')

    def card(i, cid, num, src_file, prompt, answer, concepts, bloom='Apply', changes=None, cite=None):
        row = {'id': cid, 'source_id': f'brisk:{src_file}#{num}', 'source_number': f'Exercise {num}', 'origin': 'brisk',
               'kind': 'exercise', 'bloom': bloom, 'place': {'at': 'end'}, 'cite': cite, 'prompt': prompt, 'answer': answer}
        if changes:
            row['changes'] = changes
        if not cite:
            row.pop('cite')
        ex.append(row)
        con.extend({'exercise': cid, 'concept': c} for c in concepts)

    def num(v, sol, tol=None):
        a = {'type': 'number', 'value': v, 'solution': sol, 'generated_by': 'source'}
        if tol:
            a['tol'] = tol
        return a

    def yesno(correct, sol):
        return {'type': 'choice', 'options': ['Yes', 'No'], 'correct': correct, 'solution': sol, 'generated_by': 'source'}
    with_setup = 'Brisk Walk asks it after the set-up of its item 1, which is printed before it.'
    # counting: items 1–5 (the judge's order; config.md)
    card(0, 'b1', 1, 'countingEx', C[0]['q'], num(180, C[0]['a']), ['counting'], cite='counting')
    sol2 = C[1]['a'].replace('<sup class="fn" data-note="fn-*"></sup>', '').replace('= 300$', '= 300$<sup class="fn" data-note="err-costume"></sup>', 1)
    sol2 += '\n\n' + C[1]['notes'][0]['html']
    card(1, 'b2', 2, 'countingEx', C[0]['q'] + '\n\n' + C[1]['q'], num(300, sol2), ['counting'],
         changes=with_setup + ' Its footnote to the answer is printed after the answer.', cite='counting')
    card(2, 'b3', 3, 'countingEx', C[0]['q'] + '\n\n' + C[2]['q'], num(10240, C[2]['a']), ['counting'], changes=with_setup, cite='counting')
    card(3, 'b4', 4, 'countingEx', C[0]['q'] + '\n\n' + C[2]['q'] + '\n\n' + C[3]['q'], num(2580, C[3]['a']), ['counting'],
         changes='Brisk Walk asks it after its items 1 and 3, which are printed before it.', cite='counting')
    card(4, 'b5', 5, 'countingEx', C[4]['q'], num(8250, C[4]['a']), ['counting'], bloom='Analyze', cite='counting')
    # probability-basics: items 1, 4, 6, 7, 8
    setup = P[0]['q'].split('\n\n')[0]
    card(5, 'p1', 1, 'probabilityEx', P[0]['q'], yesno(0, P[0]['a']), ['probability-basics'], bloom='Remember', cite='probability')
    card(6, 'p4', 4, 'probabilityEx', setup + '\n\n' + P[3]['q'], yesno(0, P[3]['a']), ['probability-basics'], bloom='Understand',
         changes=with_setup, cite='probability')
    card(7, 'p6', 6, 'probabilityEx', setup + '\n\n' + P[5]['q'], yesno(1, P[5]['a']), ['probability-basics'], bloom='Understand',
         changes=with_setup, cite='probability')
    card(8, 'p7', 7, 'probabilityEx', setup + '\n\n' + P[6]['q'], num(0.1, P[6]['a']), ['probability-basics'],
         changes=with_setup, cite='probability')
    card(9, 'p8', 8, 'probabilityEx', setup + '\n\n' + P[6]['q'] + '\n\n' + P[7]['q'], num(0.8, P[7]['a']), ['probability-basics'],
         changes='Brisk Walk asks it after its items 1 and 7, which are printed before it.', cite='probability')
    # conditional-probability: items 16 and 17 with item 9's set-up (item 18 needs Bayes' Theorem: left out)
    s9 = P[8]['q'].rsplit('\n\n', 1)[0]
    card(10, 'p16', 16, 'probabilityEx', s9 + '\n\n' + P[15]['q'], num(1 / 7, P[15]['a'], tol=0.01), ['conditional-probability'],
         changes='Brisk Walk asks it after the set-up of its item 9, which is printed before it; its key is 1/7 ≈ .143.', cite='conditional')
    card(11, 'p17', 17, 'probabilityEx', s9 + '\n\n' + P[16]['q'], num(0.75, P[16]['a']), ['conditional-probability'],
         changes='Brisk Walk asks it after the set-up of its item 9, which is printed before it.', cite='conditional')
    # code: Exercism pascals-triangle (canonical data; the Python track's example as reference) and baffling-birthdays
    pas = _canonical('pascals-triangle', 'rows')
    py = open(os.path.join(_BOOK, EXERCISM_PY, 'pascals-triangle/.meta/example.py'), encoding='utf-8').read()
    ex.append({
        'id': 'c1', 'source_id': 'exercism:pascals-triangle', 'source_number': 'pascals-triangle', 'origin': 'exercism',
        'kind': 'code', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'counting',
        'prompt': _exercism_prompt('pascals-triangle'),
        'answer': {'type': 'code',
                   'python': {'entry': 'rows', 'starter': 'def rows(row_count):\n    pass\n', 'reference': py, 'generated_by': 'source'},
                   'javascript': {'entry': 'rows', 'starter': 'function rows(count) {\n}\n', 'reference': PASCAL_JS, 'generated_by': 'ai'},
                   'tests': [{'args': list(c['input'].values()), 'expect': c['expected'], 'visible': i == 0, 'generated_by': 'source'}
                             for i, c in enumerate(pas)],
                   'generated_by': 'source'}})
    con.append({'exercise': 'c1', 'concept': 'counting'})
    bd = _canonical('baffling-birthdays', 'estimatedProbabilityOfSharedBirthday')
    ex.append({
        'id': 'c2', 'source_id': 'exercism:baffling-birthdays', 'source_number': 'baffling-birthdays', 'origin': 'exercism',
        'kind': 'code', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'probability',
        'changes': 'Only the estimate is asked for and tested, as a percentage; the canonical data’s cases for the shared-birthday '
                   'check and the random birthdates are left out, and the estimate is checked to within 10 percent of the canonical value.',
        'prompt': _exercism_prompt('baffling-birthdays'),
        'answer': {'type': 'code', 'tol': 0.1,
                   'python': {'entry': 'estimated_probability_of_shared_birthday',
                              'starter': 'def estimated_probability_of_shared_birthday(group_size):\n    pass\n',
                              'reference': BIRTHDAY_PY, 'generated_by': 'ai'},
                   'javascript': {'entry': 'estimatedProbabilityOfSharedBirthday',
                                  'starter': 'function estimatedProbabilityOfSharedBirthday(groupSize) {\n}\n',
                                  'reference': BIRTHDAY_JS, 'generated_by': 'ai'},
                   'tests': [{'args': list(c['input'].values()), 'expect': c['expected'], 'visible': i == 0, 'generated_by': 'source'}
                             for i, c in enumerate(bd)],
                   'generated_by': 'source'}})
    con.append({'exercise': 'c2', 'concept': 'probability-basics'})
    return ex, con


# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]
SECTION = {
    'id': '1.6', 'chapter': '1', 'title': 'Counting and expected value', 'short': 'Counting and expectation',
    'lead': ('An Essential section on <span data-concept="counting">counting</span>, probability, conditional probability, '
             'random variables and expectation; <span data-concept="indicator-variables">indicator random variables</span> are '
             'Advanced. The three sources write probability three ways that mean the same thing: Pr(<em>A</em>) and '
             'Pr(<em>A</em>|<em>K</em>), with sample space Ω; then Pr[<em>C</em> = 2] for the event that <em>C</em> equals 2, '
             'with sample space 𝒮; then Pr{<em>X</em> = <em>i</em>}, with E[<em>X</em>] for an expected value. Coin tosses and '
             'indicator variables are numbered from 1.'),
    'objectives': [], 'summary_html': '',
    'notes': ('Brisk Walk’s chapter openings, its “Enumerating permutations”, “Total probability” and “Bayes’ Theorem” sections and '
              'its counting summary, the opening of MCS chapter 19 and the rest of its 19.2, and the skip-list analysis around '
              'ODS’s coin-tosses lemma are left out here.'),
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'The written exercises are Brisk Walk’s, with its answers: counting items 1–5 and probability items 1, 4, 6, 7, 8, 16 and 17, '
        'each printed after the set-up it is asked under; item 18 is left out, since it needs Bayes’ Theorem, which this page does '
        'not carry. Wikibooks’ keyed exercises on conditional probability and random variables and Aspnes’s C.9.3, F.5.3 and F.5.4 '
        'are not here yet: the Wikibooks items lean on worked examples of their own pages, and two of Aspnes’s use conditional '
        'expectation, which this page does not define. The pascals-triangle tests are Exercism’s canonical data and its Python '
        'reference the Exercism Python track’s example (MIT); its JavaScript reference is written by the AI that built the '
        'section. The baffling-birthdays tests are the canonical data’s estimates, checked to within 10 percent; both its '
        'references are the AI’s, since the Python track has no example for it. The Kattis items the judge ranked '
        '(anagramcounting, dicecup, fruitbaskets) wait for their AI-written tests. The NC cards are kept in exercises-nc.json: '
        'MIT 6.042J (Fall 2005) problem set 7 problem 1, problem set 9 problems 2–5 and problem set 10 problems 1, 3, 4 and 5, '
        'each keyed by a link to MIT’s worked solution; the other problems the plan names from those sets (7: 2–5; 9: 1, 6, 7; '
        '10: 2, 6–8) and MIT 6.006 (Spring 2020) problem set 0, problem 0-2, wait for a reading of their PDFs, since the cached '
        'text loses their mathematics. The partly keyed Levin and Applied Combinatorics sets, MCS’s unkeyed problems '
        'for chapters 15–19, OpenIntro’s exercises and the unkeyed Erickson-notes probability exercises are left out, as are '
        'Project Euler 15 and 53 (statement only).'),
    'figures': [
        {'id': 'sim-pascal', 'kind': 'sim', 'originals': ['/media/ch01/brisk-6-1-pascal.png'], 'original_caption': CAPTIONS['pascal']['text'],
         'draws': ['size'], 'ai': FIG_AI},
        {'id': 'sim-idol-venn', 'kind': 'sim', 'originals': ['/media/ch01/brisk-4-1-venn.png'], 'original_caption': CAPTIONS['venn']['text'],
         'draws': [], 'ai': FIG_AI},
        {'id': 'sim-coin-tosses', 'kind': 'sim', 'draws': ['size'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'kelly', 'label': 'Kelly, an outcome of All-time Idol', 'figures': ['sim-idol-venn']},
        {'id': 'fantasia', 'label': 'Fantasia, an outcome of All-time Idol', 'figures': ['sim-idol-venn']},
        {'id': 'carrie', 'label': 'Carrie, an outcome of All-time Idol', 'figures': ['sim-idol-venn']},
        {'id': 'david', 'label': 'David, an outcome of All-time Idol', 'figures': ['sim-idol-venn']},
        {'id': 'F', 'label': 'F, the event that a woman wins', 'figures': ['sim-idol-venn']},
        {'id': 'R', 'label': 'R, the event that a rock singer wins', 'figures': ['sim-idol-venn']},
        {'id': 'U', 'label': 'U, the event that an underage singer wins', 'figures': ['sim-idol-venn']},
        {'id': 'C', 'label': 'C, the event that a country singer wins', 'figures': ['sim-idol-venn']},
    ],
    'coverage': [
        {'span': 'counting', 'concept': 'counting', 'verb': 'introduces'},
        {'span': 'probability', 'concept': 'probability-basics', 'verb': 'introduces'},
        {'span': 'interlude', 'concept': 'probability-basics', 'verb': 'reinforces'},
        {'span': 'conditional', 'concept': 'conditional-probability', 'verb': 'introduces'},
        {'span': 'conditional', 'concept': 'probability-basics', 'verb': 'uses'},
        {'span': 'random-variable', 'concept': 'random-variable', 'verb': 'introduces'},
        {'span': 'random-variable', 'concept': 'probability-basics', 'verb': 'uses'},
        {'span': 'linearity', 'concept': 'linearity-of-expectation', 'verb': 'introduces'},
        {'span': 'linearity', 'concept': 'random-variable', 'verb': 'uses'},
        {'span': 'indicators', 'concept': 'indicator-variables', 'verb': 'introduces'},
        {'span': 'indicators', 'concept': 'linearity-of-expectation', 'verb': 'uses'},
        {'span': 'indicators', 'concept': 'counting', 'verb': 'uses'},
        {'span': 'coin-tosses', 'concept': 'geometric-expectation', 'verb': 'introduces'},
        {'span': 'coin-tosses', 'concept': 'indicator-variables', 'verb': 'uses'},
        {'span': 'coin-tosses', 'concept': 'linearity-of-expectation', 'verb': 'uses'},
    ],
    'footnotes_extra': [
        {'id': 'err-52', 'kind': 'correction',
         'html': 'The number printed for 52! is right only in its first thirteen digits. 52! = 80,658,175,170,943,878,571,660,636,856,'
                 '403,766,975,289,505,440,883,277,824,000,000,000,000.'},
        {'id': 'err-p-r', 'kind': 'correction',
         'html': 'Here the event that a rock singer wins is called <em>P</em>; from the next paragraph on, and in Figure 4.1, the same '
                 'event is called <em>R</em>.'},
        {'id': 'err-outcomes', 'kind': 'correction',
         'html': 'The book prints “the total number of events”; it means the total number of outcomes, <em>N</em> = |Ω|.'},
        {'id': 'err-costume', 'kind': 'correction',
         'html': 'The 300 counts one choice that is no costume at all: skipping the outfit, the headgear and the accessory together. '
                 'If “skip one or more of the items” is read as keeping at least one, the count is 299.'},
    ],
    'derivations': DERIVATIONS,
}
