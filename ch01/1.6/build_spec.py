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
              'cap': 'Fact 4 with $k - 1$ in place of $k$.'},
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
