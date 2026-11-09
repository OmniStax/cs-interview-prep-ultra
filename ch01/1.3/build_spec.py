"""What tools/build_text.py needs to assemble 1.3 Asymptotic notation (the plan is plan.md beside this file).

Everything here is placement, markup or a small correction of what the conversion gets wrong; the source's
words come from the converters: ODS's LaTeX through tools/build_text.py (pseudocode edition, METHOD decision
20) and OpenDSA's reStructuredText and code fragments through tools/extract_opendsa.py. The Python and
JavaScript of the two OpenDSA fragments are AI translations (decision 20); their Java and C++ are read from
the opendsa-code cache. Each FIXES entry says why it is there.
"""
TITLE = 'Asymptotic notation'
INTRO = 'sources/_cache/ods/latex/intro.tex'
LOWER = 'sources/_cache/opendsa/RST/en/AlgAnal/AnalLower.rst'
MULTIPLE = 'sources/_cache/opendsa/RST/en/AlgAnal/AnalMultiple.rst'

BLOCKS = [
    # intro.tex 517 is "\subsection{Asymptotic Notation}", 652 closes its figure, 654 begins "In a few cases, we will
    # use asymptotic notation on functions with more than one variable", the multivariate paragraph left out
    dict(id='big-o', source='ods', file=INTRO, lines=(518, 653),
         locator='ods:intro#asymptotic-notation, up to (not including) “In a few cases, we will use asymptotic notation '
                 'on functions with more than one variable”',
         h2='Asymptotic Notation'),
    # AnalLower's three ~~~ subsections; its "Summary Exercise" (an exercise) goes to the Exercises system
    dict(id='omega-theta', source='opendsa', file=LOWER, **{'from': 'Lower Bounds', 'to': 'Summary Exercise'},
         note_id='anallower-fn',
         locator='opendsa:AlgAnal/AnalLower (Lower Bounds, Theta Notation, Classifying Functions)',
         h2='Lower Bounds and Θ Notation'),
    dict(id='multivariate', source='opendsa', file=MULTIPLE, note_id='analmultiple-fn',
         locator='opendsa:AlgAnal/AnalMultiple', h2='Multiple Parameters'),
]

# ODS's figure reference: the source's own number, linked to the Sim that stands for it (plans-summary question 18).
ODS_REFS = {
    '\\figref{intro-asymptotics}': ('<a href="#sim-crossover">Figure 1.5</a>', 'Figure 1.5'),
}
# OpenDSA's :ref: to its NP-Completeness module, to this book's page on it (plans-summary question 23).
OPENDSA_REFS = {
    'NP-Complete': ('<a href="/cs-interview-prep-ultra/ch23/23.2/">NP-Complete</a>', 'NP-Complete'),
}
# The printed chain of inequalities the derivation replaces (root item 29.2), named by a piece of its TeX.
DISPLAY_AS = {
    '\\le 13n\\log n': 'drv-big-o-example',
}
# OpenDSA's slideshow stands as the figure the plan puts in its place.
AV = {'LowerBoundCON': 'sim-limit-test'}

AI = 'claude-opus-5-5 high'

# The two OpenDSA fragments in the languages the source does not print (decision 20), translated line for line
# from its Java: same names, same comments, same order.
CODE_TRANSLATIONS = {
    'Collatz': {
        'python': '''
while n > 1:
    if ODD(n):
        n = 3 * n + 1
    else:
        n = n // 2
''',
        'javascript': '''
while (n > 1)
  if (ODD(n))
    n = 3 * n + 1;
  else
    n = n / 2;
''',
    },
    'c3p16': {
        'python': '''
for i in range(C):      # Initialize count
    count[i] = 0
for i in range(P):      # Look at all of the pixels
    count[value(i)] += 1  # Increment a pixel value count
sort(count)             # Sort pixel value counts
''',
        'javascript': '''
for (let i = 0; i < C; i++) {   // Initialize count
  count[i] = 0;
}
for (let i = 0; i < P; i++) {   // Look at all of the pixels
  count[value(i)]++; // Increment a pixel value count
}
sort(count);          // Sort pixel value counts
''',
    },
}

# (what the conversion gives, what the page prints, why)
FIXES = []


def sim(fid, caption, original=None, original_caption=None):
    attrs = f'class="sim" id="{fid}"'
    if original:
        attrs += f' data-original="{original}" data-original-caption="{original_caption}"'
    return f'<figure {attrs}>\n  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>'


def dv(did):
    return f'<figure class="dv" id="drv-{did}"></figure>'


I = '<span data-ref="i"><em>i</em></span>'
HTML = {
    'drv-big-o-example': dv('big-o-example'),
    'sim-big-o-witness': sim(
        'sim-big-o-witness',
        '<span data-type="cost"><em>f</em>(<em>n</em>) = 5<em>n</em> log <em>n</em> + 8<em>n</em> − 200</span> against '
        '<span data-type="cost"><em>c</em> · <em>n</em> log <em>n</em></span>: past <em>n</em><sub>0</sub>, the tinted stretch, '
        'the line <em>c</em> · <em>n</em> log <em>n</em> must stay on or above <em>f</em>, and any gap where <em>f</em> rises '
        'above it is shaded as a failure. With <em>c</em> = 13 it does from '
        '<em>n</em><sub>0</sub> = 2 on. A smaller <em>c</em> needs a larger <em>n</em><sub>0</sub>, and for <em>c</em> = 5 or less '
        'no <em>n</em><sub>0</sub> works, because <em>f</em>(<em>n</em>) − 5<em>n</em> log <em>n</em> = 8<em>n</em> − 200 is '
        'positive for every <em>n</em> from 26 on.'),
    'sim-loop-count': sim(
        'sim-loop-count',
        'The loop filling <em>a</em>[0], …, <em>a</em>[<span data-type="size"><em>n</em></span> − 1], one pass of '
        f'{I} at a time: <span data-type="cost">1 assignment, <em>n</em> + 1 comparisons, <em>n</em> increments, '
        '<em>n</em> offsets and <em>n</em> stores</span>, which sum to 4<em>n</em> + 2 primitive operations. The shaded cells '
        f'are the part of the array the loop has filled, <em>a</em>[0..{I}). Each count grows in step with '
        '<span data-type="size"><em>n</em></span>, so whatever each kind of operation costs, the total is '
        '<span data-type="cost"><em>O</em>(<em>n</em>)</span>.'),
    'sim-crossover': sim(
        'sim-crossover',
        '<span data-ref="f1">15<em>n</em></span> against <span data-ref="f2">2<em>n</em> log <em>n</em></span> on a '
        'window that widens from <span data-type="size"><em>n</em></span> = 100 to 10 000. On the first window 15<em>n</em> '
        'is ahead all the way; the two meet where log <em>n</em> = 7.5, at <em>n</em> = 2<sup>7.5</sup> ≈ 181, and past '
        'that <span data-ref="f2">2<em>n</em> log <em>n</em></span> is larger and the gap keeps widening.',
        '/media/ch01/ods-bigoh-1.png, /media/ch01/ods-bigoh-2.png', '{{caption-text intro-asymptotics}}'),
    'sim-limit-test': sim(
        'sim-limit-test',
        'The ratio <span data-type="cost"><em>f</em>(<em>n</em>)/<em>g</em>(<em>n</em>)</span> as <em>n</em> grows, for three '
        'pairs: <em>n</em><sup>2</sup> against 2<em>n</em> log <em>n</em>, whose ratio <em>n</em>/(2 log <em>n</em>) climbs '
        'without bound; 5<em>n</em> log <em>n</em> + 8<em>n</em> − 200 against <em>n</em> log <em>n</em>, whose ratio settles '
        'towards 5; and 15<em>n</em> against 2<em>n</em> log <em>n</em>, whose ratio 7.5/log <em>n</em> sinks towards 0. '
        'Where the ratio goes decides between Ω, Θ and <em>O</em>.'),
}

AFTER_TEXT = {
    'big-o': [('using the constants', 'sim-big-o-witness'),
              ('Consider the following piece of code:', 'sim-loop-count'),
              ('told us that this would happen', 'sim-crossover')],
}

FN_INCL = '<sup class="fn" data-note="err-inclusions"></sup>'
FN_FASTER = '<sup class="fn" data-note="err-faster"></sup>'
FN_MEET = '<sup class="fn" data-note="err-bounds-meet"></sup>'
# (block, text as built, replacement, [count]): concepts, the errata markers, the loop variable
MARKS = [
    # concepts: the span that introduces each, and the other places a sentence names one
    ('big-o', '<em>big-Oh notation</em>', '<span data-concept="big-o"><em>big-Oh notation</em></span>'),
    ('omega-theta', 'Big-Oh notation describes an upper bound', '<span data-concept="big-o">Big-Oh notation</span> describes an upper bound'),
    ('omega-theta', 'The lower bound for an algorithm', 'The <span data-concept="big-omega-theta">lower bound</span> for an algorithm'),
    ('omega-theta', '(big-Theta) notation', '(<span data-concept="big-omega-theta">big-Theta</span>) notation'),
    ('multivariate', 'multiple parameters to describe the cost', '<span data-concept="multivariate-big-o">multiple parameters to describe the cost</span>'),
    # errata (exploration notes 1, 2 and 10), each marker right after the words it corrects
    ('big-o', 'O(n^{b}) \\subset O({c}^n) \\enspace .$$', 'O(n^{b}) \\subset O({c}^n) \\enspace .$$' + FN_INCL),
    ('big-o', 'for large enough values of $n$</em>.', 'for large enough values of $n$</em>.' + FN_FASTER),
    ('omega-theta', 'the upper and lower bounds always meet.', 'the upper and lower bounds always meet.' + FN_MEET),
    # the loop variable sim-loop-count draws, in the counts of the bulleted list
    ('big-o', '$int\\, i\\,\\gets\\, 0$', '$int\\, \\htmlData{ref=i}{i}\\,\\gets\\, 0$'),
    ('big-o', '$i &lt; n$', '$\\htmlData{ref=i}{i} &lt; n$'),
    ('big-o', '$i{+}{+}$', '$\\htmlData{ref=i}{i}{+}{+}$'),
    ('big-o', '$a[i]$', '$a[\\htmlData{ref=i}{i}]$'),
    ('big-o', '$a[i]\\gets i$', '$a[\\htmlData{ref=i}{i}]\\gets \\htmlData{ref=i}{i}$'),
    # the two functions sim-crossover draws, wherever the paragraph names them
    ('big-o', '$f_1(n)=15n$', '$\\htmlData{ref=f1}{f_1}(n)=15n$'),
    ('big-o', '$f_2(n)=2n\\log n$', '$\\htmlData{ref=f2}{f_2}(n)=2n\\log n$'),
    ('big-o', '$f_1(n)$', '$\\htmlData{ref=f1}{f_1}(n)$', 3),
    ('big-o', '$f_2(n)$', '$\\htmlData{ref=f2}{f_2}(n)$', 2),
]

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]

# The derivation that replaces ODS's chain 5n log n + 8n − 200 ≤ … ≤ 13n log n (plan, derivation candidates; root
# item 29.2). The book's three lines are node 1's steps; node 0 is its condition "for n ≥ 2 (so that log n ≥ 1)", which
# it states in a parenthesis; node 2 is the sentence after the chain ("using the constants c = 13 and n_0 = 2").
DRV_BIG_O = {
    'id': 'big-o-example',
    'what': '5n log n + 8n − 200 is in O(n log n)',
    'source': 'Open Data Structures, Asymptotic Notation',
    'nodes': [
        {
            'assumes': [
                {'tex': '\\log 2 = 1', 'src': '1.2'},
            ],
            'then': {'tex': '\\mk{l}{n} \\ge \\mk{r}{2}'},
            'steps': [
                {'tex': '\\mk{l}{\\log n} \\ge \\mk{r}{\\log 2}', 'uses': [],
                 'cap': 'The logarithm grows with its argument, so taking it of both sides keeps the inequality.'},
                {'tex': '\\mk{l}{\\log n} \\ge \\mk{r}{1}', 'uses': [0]},
            ],
        },
        {
            'assumes': [{'step': 0}],
            'then': {'tex': '\\mk{f}{f(n)} = \\mk{a}{5n\\log n} + \\mk{b}{8n} - \\mk{k}{200}'},
            'steps': [
                {'tex': '\\mk{f}{f(n)} \\le \\mk{a}{5n\\log n} + \\mk{b}{8n}', 'uses': []},
                {'tex': '\\mk{f}{f(n)} \\le \\mk{a}{5n\\log n} + \\mk{b}{8n\\log n}', 'uses': [0],
                 'cap': 'Multiplying $8n$ by $\\log n$, which is at least 1, cannot make it smaller.'},
                {'tex': '\\mk{f}{f(n)} \\le \\mk{a}{13n\\log n}', 'uses': [], 'map': {'b': 'a'}},
            ],
        },
        {
            'assumes': [
                {'tex': 'O(f(n)) = \\{\\, g(n) : \\text{there exists } c > 0 \\text{ and } n_0 \\text{ such that } '
                        'g(n) \\le c\\cdot f(n) \\text{ for all } n \\ge n_0 \\,\\}'},
                {'step': 1},
            ],
            'then': {'tex': '\\mk{f}{f(n)} \\le \\mk{a}{13n\\log n}'},
            'steps': [
                {'tex': '\\mk{f}{f(n)} \\in O(\\mk{a}{n\\log n})', 'uses': [0],
                 'cap': 'The inequality holds for every $n \\ge 2$, so the definition is met with $c = 13$ and $n_0 = 2$.'},
            ],
        },
    ],
}

SECTION = {
    'id': '1.3', 'chapter': '1', 'title': 'Asymptotic notation', 'short': 'Asymptotic notation',
    'lead': ('An Essential section on <span data-concept="big-o">big-O</span>, <span data-concept="big-omega-theta">Ω and Θ</span>, '
             'the notations that compare how fast functions grow once constant factors and small inputs are set aside; '
             '<span data-concept="multivariate-big-o">analysis with several parameters</span> is Advanced. ODS’s loop example '
             'fills its array from <em>a</em>[0] to <em>a</em>[<em>n</em> − 1].'),
    'objectives': [], 'summary_html': '',
    'notes': ('ODS’s definition of asymptotic notation in several variables, OpenDSA’s slideshow on lower bounds and best cases '
              'of sequential search, and OpenDSA’s summary exercises are left out here.'),
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'The OpenDSA items the chapter config lists for this section (AnalPairMCQ1–AnalPairMCQ11 with UpperBoundsSumm; '
        'ThetaUpperMCQ and AlgAnlsTFbgthta with LowerThetaSumm; AlgAnlsFIBsmlintgr2 from 1.2, tagged with big-o and '
        'logarithms) wait for the converter of OpenDSA’s Khan-format exercises, and its CompareGrowth and GrowthRatesPRO '
        'wait for the sequence answer type; MisunderstandingsTF1–6 go with 1.4. Aspnes’s keyed A.6.2 (an approximate sum) '
        'and A.6.3 (a stretched function) wait for a reader of his PDF’s mathematics, and the four MIT OpenCourseWare cards '
        '(6.006 S20 ps1 1-1, 6.046J F05 ps1 1-1, 6.006 F11 ps1 1-1, 6.042J F05 ps6 #8) for the app to read exercises-nc.json. '
        'MCS 14.18–14.42, the Applied Combinatorics items and Erickson’s chapter 0 exercise 2 have no published answers and '
        'are left out. No open exercise tests analysis with several parameters.'),
    'figures': [
        {'id': 'sim-big-o-witness', 'kind': 'sim', 'draws': ['cost', 'size'], 'ai': FIG_AI},
        {'id': 'sim-loop-count', 'kind': 'sim', 'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
        {'id': 'sim-crossover', 'kind': 'sim', 'originals': ['/media/ch01/ods-bigoh-1.png', '/media/ch01/ods-bigoh-2.png'],
         'original_caption': '{{caption-text intro-asymptotics}}', 'draws': ['cost', 'size'], 'ai': FIG_AI},
        {'id': 'sim-limit-test', 'kind': 'sim', 'draws': ['cost', 'size'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'i', 'label': 'i, the loop variable of the snippet', 'figures': ['sim-loop-count']},
        {'id': 'f1', 'label': 'f₁(n) = 15n, a complicated linear time algorithm', 'figures': ['sim-crossover']},
        {'id': 'f2', 'label': 'f₂(n) = 2n log n, a simpler divide-and-conquer algorithm', 'figures': ['sim-crossover']},
    ],
    'coverage': [
        {'span': 'big-o', 'concept': 'big-o', 'verb': 'introduces'},
        {'span': 'omega-theta', 'concept': 'big-omega-theta', 'verb': 'introduces'},
        {'span': 'omega-theta', 'concept': 'big-o', 'verb': 'uses'},
        {'span': 'multivariate', 'concept': 'multivariate-big-o', 'verb': 'introduces'},
        {'span': 'multivariate', 'concept': 'big-omega-theta', 'verb': 'uses'},
    ],
    'footnotes_extra': [
        {'id': 'err-inclusions', 'kind': 'correction',
         'html': 'The chain holds as printed only for $c > 1$. For $c \\le 1$ the function $c^n$ does not grow (it is 1, or it '
                 'falls towards 0), so $n^b$ is not in $O(c^n)$ and the last inclusion fails; the same goes for the last '
                 'inclusion of the chain multiplied by $n$.'},
        {'id': 'err-faster', 'kind': 'correction',
         'html': 'A big-Oh running time is only an upper bound, so two different big-Oh bounds do not show which algorithm is '
                 'faster: an algorithm whose running time is in $O(n)$ is in $O(n^2)$ too. The conclusion holds when each '
                 'running time is known to within a constant factor from above and below, which is $\\Theta$ notation '
                 '(<a href="#omega-theta">Lower Bounds and Θ Notation</a>).'},
        {'id': 'err-bounds-meet', 'kind': 'correction',
         'html': 'Not every such equation has matching bounds. The footnote’s own example, $\\mathbf{T}(n) = n$ for odd $n$ and '
                 '$n^2/100$ for even $n$, is an algebraic equation for the time requirement whose upper bound is $O(n^2)$ '
                 'and whose lower bound, by the first definition, is only $\\Omega(n)$, so it has no $\\Theta$ bound.'},
    ],
    'derivations': [DRV_BIG_O],
}
