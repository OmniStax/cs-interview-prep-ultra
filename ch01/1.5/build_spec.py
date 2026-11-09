"""What tools/build_translation.py needs to assemble 1.5 Amortized analysis (the plan is plan.md beside this file).

The Chinese comes from OI Wiki's page by script (source.md); the English is translation.md, written block by
block under translate.md and checked against the source element for element. Everything here is placement
and markup: the blocks and their headings, the figure and the two derivations and where they stand, the
list items and displays the derivations carry, and the spans that mark concepts and the erratum.
"""
TITLE = 'Amortized analysis'
OIWIKI_FILE = 'sources/_cache/oiwiki/docs/basic/amortized-analysis.md'
TRANSLATION = 'translation.md'
AI = 'claude-opus-5-5 high'

LOC = 'oiwiki:basic/amortized-analysis'
BLOCKS = [
    dict(id='amortized', source='oiwiki', locator=f'{LOC}#引入, #内容 (its heading dropped) and #聚合分析',
         h2='Amortized analysis', drop_headings=['内容'], **{'from': '## 引入', 'to': '### 记账分析'}),
    dict(id='accounting', source='oiwiki', locator=f'{LOC}#记账分析', **{'from': '### 记账分析', 'to': '### 势能分析'}),
    dict(id='potential', source='oiwiki', locator=f'{LOC}#势能分析, with #原理 and #示例：动态数组的扩容分析',
         **{'from': '### 势能分析', 'to': '## 扩展示例：堆栈操作'}),
    dict(id='stack-example', source='oiwiki', locator=f'{LOC}#扩展示例：堆栈操作 (its opening and table), #聚合分析法 and #记账分析法',
         **{'from': '## 扩展示例：堆栈操作', 'to': '### 势能分析法'}),
    dict(id='stack-potential', source='oiwiki', locator=f'{LOC}#扩展示例：堆栈操作, its #势能分析法',
         h2='Potential analysis of the stack', **{'from': '### 势能分析法', 'to': '## 参考资料与注释'}),
]


def sim(fid, caption):
    return f'<figure class="sim" id="{fid}">\n  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>'


def dv(did):
    return f'<figure class="dv" id="drv-{did}"></figure>'


N_ = '<span data-ref="n"><em>n</em></span>'
M_ = '<span data-ref="m"><em>m</em></span>'
I_ = '<span data-ref="i"><em>i</em></span>'
HTML = {
    'sim-pay-for-doubling': sim(
        'sim-pay-for-doubling',
        f'A growable array that starts at capacity 1 and doubles when it is full. An insert costs 1 to write its element, '
        f'and an insert into a full array first copies all {N_} elements, one element {I_} at a time, into an array of twice the '
        f'capacity {M_}, so the actual costs spike at every doubling. Counted in aggregate, the total stays under 3{N_}; '
        f'charged 3 an insert, the credit left on the newer half of the array pays for every copy and never runs out; '
        f'as the potential 2{N_} − {M_}, it rises by 2 with each insert that copies nothing and falls by the cost of the copies, '
        f'so every insert has amortized cost 3.'),
    'drv-potential-sum': dv('potential-sum'),
    'drv-doubling-potential': dv('doubling-potential'),
}

# (block, anchor of the first element, anchor of the last, html key): a run of elements a derivation replaces
REPLACE = [
    ('potential', r'p_i = c_i + \Phi(S_i) - \Phi(S_{i-1})', r'\sum_{i=1}^m p_i \geq \sum_{i=1}^m c_i', 'drv-potential-sum'),
]
# (block, text of a list item): items whose lines a derivation now carries (root rule 29.2)
DROP = [
    ('potential', r"$\Phi(h') - \Phi(h) = 2(n + 1) - m - (2n - m) = 2$"),
    ('potential', '**Amortized cost**: $1 + 2 = 3$'),
    ('potential', r"$\Phi(h') - \Phi(h) = 2(n + 1) - 2n - (2n - n) = 2 - n$"),
    ('potential', '**Amortized cost**: $n + 1 + (2 - n) = 3$'),
]
# (block, anchor of an element, html key): what stands after that element
AT = [
    ('potential', '**Insert (no resize needed)**', 'drv-doubling-potential'),
]

FN_M = '<sup class="fn" data-note="err-m"></sup>'
MARKS = [
    # concepts: the introducing spans, then plain mentions
    ('amortized', 'Amortized analysis is a technique', '<span data-concept="amortized-analysis">Amortized analysis</span> is a technique'),
    ('amortized', 'aggregate analysis, the accounting method and the potential method. Each',
     '<span data-concept="aggregate-accounting">aggregate analysis</span>, <span data-concept="aggregate-accounting">the accounting method</span> '
     'and <span data-concept="potential-method">the potential method</span>. Each'),
    ('accounting', 'The accounting method assigns', '<span data-concept="aggregate-accounting">The accounting method</span> assigns'),
    ('potential', 'The potential method defines', '<span data-concept="potential-method">The potential method</span> defines'),
    ('stack-example', 'Stack operations are one of the classic applications of amortized analysis',
     'Stack operations are one of the classic applications of <span data-concept="amortized-analysis">amortized analysis</span>'),
    ('stack-example', 'aggregate analysis, the accounting method and the potential method.',
     '<span data-concept="aggregate-accounting">aggregate analysis</span>, <span data-concept="aggregate-accounting">the accounting method</span> '
     'and <span data-concept="potential-method">the potential method</span>.'),
    ('stack-potential', 'The potential method defines', '<span data-concept="potential-method">The potential method</span> defines'),
    # erratum 14: m is the full array's size here, and the capacity in the potential method
    ('amortized', 'is the current size of the array.', 'is the current size of the array.' + FN_M),
]

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]
LEAD = ('An Essential section on <span data-concept="amortized-analysis">amortized analysis</span>: one dynamic array, doubled when full, '
        'analysed by the aggregate, accounting and potential methods, then a stack analysed the same three ways; '
        '<span data-concept="potential-method">the potential method</span> is Advanced. Here n counts the elements and m the array’s '
        'capacity, except in the aggregate analysis, where m is the size of the full array being copied. The stack’s push, pop and '
        'multi-pop are defined in its own table; stacks are the subject of '
        '<a href="/cs-interview-prep-ultra/ch03/3.1/">Section 3.1</a>.')

# the derivations (root rule 29; plan.md "Derivation candidates"); facts from the block's own words
PHI_SUM = r'\sum_{i=1}^m'
DERIVATIONS = [
    {
        'id': 'potential-sum',
        'what': 'the total time cost of m operations and its upper bound',
        'source': 'OI Wiki, amortized analysis, the potential method (principle)',
        'nodes': [{
            'assumes': [
                {'text': r'The $i$-th operation takes the data structure from the state $S_{i-1}$ to the state $S_i$, at actual cost $c_i$; its amortized cost is written $p_i$.'},
                {'text': r'Every reachable state $S$ satisfies $\Phi(S) \geq \Phi(S_0)$.'},
            ],
            'then': {'tex': r"\mk{p}{\hat{c}} = \mk{c}{c} + \mk{a}{\Phi(S')} - \mk{b}{\Phi(S)}"},
            'steps': [
                {'tex': r'\mk{p}{p_i} = \mk{c}{c_i} + \mk{a}{\Phi(S_i)} - \mk{b}{\Phi(S_{i-1})}', 'uses': [0]},
                {'tex': rf'\mk{{p}}{{{PHI_SUM} p_i}} = \mk{{c}}{{{PHI_SUM} c_i}} + \mk{{d}}{{{PHI_SUM} \bigl(\Phi(S_i) - \Phi(S_{{i-1}})\bigr)}}',
                 'uses': [], 'map': {'a': 'd', 'b': 'd'}},
                {'tex': rf'\mk{{p}}{{{PHI_SUM} p_i}} = \mk{{c}}{{{PHI_SUM} c_i}} + \mk{{e}}{{\Phi(S_m)}} - \mk{{z}}{{\Phi(S_0)}}',
                 'uses': [], 'map': {'d': ['e', 'z']},
                 'cap': r'The sum telescopes: each $\Phi(S_i)$ with $0 < i < m$ is added once and subtracted once, so only $\Phi(S_m) - \Phi(S_0)$ is left.'},
                {'tex': rf'\mk{{c}}{{{PHI_SUM} c_i}} = \mk{{p}}{{{PHI_SUM} p_i}} + \mk{{z}}{{\Phi(S_0)}} - \mk{{e}}{{\Phi(S_m)}}', 'uses': []},
                {'tex': rf'\mk{{p}}{{{PHI_SUM} p_i}} \geq \mk{{c}}{{{PHI_SUM} c_i}}', 'uses': [1],
                 'cap': r'Since $\Phi(S_m) \geq \Phi(S_0)$, the term $\Phi(S_0) - \Phi(S_m)$ is at most $0$.'},
            ],
        }],
    },
    {
        'id': 'doubling-potential',
        'what': 'the amortized cost of an insert',
        'source': 'OI Wiki, amortized analysis, the potential method (example: analysing the resizing of a dynamic array)',
        'nodes': [
            {   # 0: the change in potential, no resize
                'assumes': [
                    {'text': r'An insert that needs no resize adds one element and keeps the capacity: $n$ becomes $n + 1$ and $m$ stays $m$.'},
                ],
                'then': {'tex': r'\mk{L}{\Phi(h)} = \mk{b}{2n - m}'},
                'steps': [
                    {'tex': r"\mk{L}{\Phi(h') - \Phi(h)} = \mk{a}{2(n + 1) - m} - \mk{b}{(2n - m)}", 'uses': [0]},
                    {'tex': r"\mk{L}{\Phi(h') - \Phi(h)} = \mk{r}{2}", 'uses': [], 'map': {'a': 'r', 'b': 'r'}},
                ],
            },
            {   # 1: its amortized cost
                'assumes': [
                    {'text': r'An insert that needs no resize writes one element, at actual cost $1$.'},
                    {'step': 0},
                ],
                'then': {'tex': r"\mk{h}{\hat{c}} = \mk{c}{c} + \mk{d}{\Phi(S') - \Phi(S)}"},
                'steps': [
                    {'tex': r'\mk{h}{\hat{c}} = \mk{c}{1} + \mk{d}{2}', 'uses': [0, 1]},
                    {'tex': r'\mk{h}{\hat{c}} = \mk{r}{3}', 'uses': [], 'map': {'c': 'r', 'd': 'r'}},
                ],
            },
            {   # 2: the change in potential, with a resize
                'assumes': [
                    {'text': r'The insert that triggers a resize finds the capacity $m = n$; after it there are $n + 1$ elements and the capacity is $2n$.'},
                ],
                'then': {'tex': r'\mk{L}{\Phi(h)} = \mk{b}{2n - m}'},
                'steps': [
                    {'tex': r"\mk{L}{\Phi(h') - \Phi(h)} = \mk{a}{2(n + 1) - 2n} - \mk{b}{(2n - n)}", 'uses': [0]},
                    {'tex': r"\mk{L}{\Phi(h') - \Phi(h)} = \mk{r}{2 - n}", 'uses': [], 'map': {'a': 'r', 'b': 'r'}},
                ],
            },
            {   # 3: its amortized cost
                'assumes': [
                    {'text': r'The insert that triggers a resize copies all $n$ elements into the new array and inserts the new one, at actual cost $n + 1$.'},
                    {'step': 2},
                ],
                'then': {'tex': r"\mk{h}{\hat{c}} = \mk{c}{c} + \mk{d}{\Phi(S') - \Phi(S)}"},
                'steps': [
                    {'tex': r'\mk{h}{\hat{c}} = \mk{c}{n + 1} + \mk{d}{(2 - n)}', 'uses': [0, 1]},
                    {'tex': r'\mk{h}{\hat{c}} = \mk{r}{3}', 'uses': [], 'map': {'c': 'r', 'd': 'r'}},
                ],
            },
        ],
    },
]

SECTION = {
    'id': '1.5', 'chapter': '1', 'title': 'Amortized analysis', 'short': 'Amortized analysis',
    'lead': LEAD,
    'objectives': [], 'summary_html': '',
    'notes': ('OI Wiki’s prerequisite line, its list of further reading and its code are not included here; with thanks to the '
              '<a href="https://github.com/OI-wiki/OI-wiki/graphs/contributors">OI Wiki Team and its contributors</a>.'),
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'No open exercise tests this section’s concepts. Its one exercise is an MIT OpenCourseWare problem with its published solution, '
        'under CC BY-NC-SA and kept apart from the book’s CC BY-SA content: 6.046J Spring 2012 problem 6-1 (Amortization in Balanced '
        'Binary Trees). 6.046J Fall 2005 problem 6-1 (Electronic Billboard) waits until its formulas, which its handout sets in fonts '
        'that cannot be read as text, are transcribed and checked. 6.046J Spring 2015 problem 4-1 (Extreme FIFO Queues), which needs '
        'queues, is held for Section 3.4. The exercises of Erickson’s lecture notes on amortized analysis have no published answers and '
        'are left out.'),
    'figures': [
        {'id': 'sim-pay-for-doubling', 'kind': 'sim', 'draws': ['key', 'cost'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'n', 'label': 'n, the number of elements in the array', 'figures': ['sim-pay-for-doubling']},
        {'id': 'm', 'label': 'm, the capacity of the array', 'figures': ['sim-pay-for-doubling']},
        {'id': 'i', 'label': 'i, the element being copied', 'figures': ['sim-pay-for-doubling']},
    ],
    'coverage': [
        {'span': 'amortized', 'concept': 'amortized-analysis', 'verb': 'introduces'},
        {'span': 'amortized', 'concept': 'aggregate-accounting', 'verb': 'uses'},
        {'span': 'accounting', 'concept': 'aggregate-accounting', 'verb': 'introduces'},
        {'span': 'accounting', 'concept': 'amortized-analysis', 'verb': 'uses'},
        {'span': 'potential', 'concept': 'potential-method', 'verb': 'introduces'},
        {'span': 'potential', 'concept': 'amortized-analysis', 'verb': 'uses'},
        {'span': 'stack-example', 'concept': 'amortized-analysis', 'verb': 'reinforces'},
        {'span': 'stack-example', 'concept': 'aggregate-accounting', 'verb': 'reinforces'},
        {'span': 'stack-potential', 'concept': 'potential-method', 'verb': 'reinforces'},
    ],
    'footnotes_extra': [
        {'id': 'err-m', 'kind': 'correction',
         'html': 'Here <em>m</em> is the size of the full array, the number of elements a resize copies. Later in the section <em>m</em> '
                 'stands for other things: the capacity of the array, beside <em>n</em> for the number of elements, in the potential '
                 'method’s example and in its starting value <em>m</em> = 1 above, and the number of operations in the potential '
                 'method’s principle. Where a resize happens the full array’s size and its capacity are equal, so every count in the '
                 'section is right in each reading.'},
    ],
    'derivations': DERIVATIONS,
}
