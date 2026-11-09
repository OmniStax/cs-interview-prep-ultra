"""What ch02/2.3/build.py needs to assemble 2.3 Two pointers and sliding windows (the plan is plan.md beside it).

The OI Wiki blocks come from OI Wiki's page by script (source.md) with their English in translation.md, checked
against the source element for element by tools/build_translation.py's parity check; the Wikipedia blocks come
from the cached wikitext by wikitext.py. Everything here is placement and markup: the blocks and their
headings, the figures and the derivation and where they stand, the links that stand for OI Wiki's LeetCode
boxes, a replacement table with a reason for each entry, and the spans that mark concepts and referents.
"""
TITLE = 'Two pointers and sliding windows'
OIWIKI_FILE = 'sources/_cache/oiwiki/docs/misc/two-pointer.md'
AI = 'claude-opus-5-5 high'
OI = 'oiwiki:misc/two-pointer'

BLOCKS = [
    dict(id='two-pointers', source='oiwiki', locator=f'{OI}#引入', h2='Two pointers',
         **{'from': '## 引入', 'to': '## 维护区间信息'}),
    dict(id='sorted-pair', source='oiwiki', locator=f'{OI}#利用序列有序性 (its opening, 例题 4 as a link, and 过程)',
         boxes=['lc167'], **{'from': '## 利用序列有序性', 'to': '### 实现'}),
    dict(id='three-sum', source='wikipedia', locator='wikipedia:3SUM (the lead’s first sentence) and #Quadratic algorithm',
         file='3SUM.wiki', h2='3SUM', h3={'Quadratic algorithm': 'Quadratic algorithm'},
         parts=[('lead', None, 'sum to zero.'), ('section', 'Quadratic algorithm', None)]),
    dict(id='merge', source='wikipedia', locator='wikipedia:Merge_algorithm#Merging two lists',
         file='Merge_algorithm.wiki', h2='Merging two lists', parts=[('section', 'Merging two lists', None)]),
    dict(id='moving-average', source='wikipedia',
         locator='wikipedia:Moving_average#Simple moving average, from its opening to “…and only 3 arithmetic steps.”',
         file='Moving_average.wiki', h2='Simple moving average',
         parts=[('section', 'Simple moving average', 'only 3 arithmetic steps.')]),
    dict(id='variable-window', source='oiwiki', locator=f'{OI}#维护区间信息 (its opening, 例题 1 as a link, and its 过程)',
         h2='Variable-size sliding window', boxes=['lc713'], **{'from': '## 维护区间信息', 'to': '#### 实现'}),
]


def sim(fid, caption, src=None, loc=None):
    prov = f' data-source="{src}" data-locator="{loc}"' if src else ''
    return (f'<figure class="sim" id="{fid}"{prov}>\n  <div class="sim-head"><span class="eyebrow">Sim</span>'
            f'<span>{caption}</span></div>\n</figure>')


def dv(did):
    return f'<figure class="dv" id="drv-{did}"></figure>'


def ref(rid, inner):
    return f'<span data-ref="{rid}">{inner}</span>'


L_ = ref('pair-l', '<em>l</em>')
R_ = ref('pair-r', '<em>r</em>')
CAPTIONS = {
    'sim-two-pointers': 'CAPTION',
    'sim-three-sum': 'CAPTION',
    'sim-merge': 'CAPTION',
    'sim-moving-window': 'CAPTION',
    'sim-variable-window': 'CAPTION',
}
TA = 'thealgorithms-python'
HTML = {
    # OI Wiki's 例题 boxes restate LeetCode's statements, which are link-only (RULES.md, Source)
    'lc167': '<p>Example: <a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/">LeetCode 167. Two Sum II – Input Array Is Sorted</a></p>',
    'lc713': '<p><a href="https://leetcode.com/problems/subarray-product-less-than-k/">LeetCode 713. Subarray Product Less Than K</a></p>',
    'sim-two-pointers': sim('sim-two-pointers', CAPTIONS['sim-two-pointers'], TA, f'{TA}:maths/two_pointer.py::two_pointer'),
    'sim-three-sum': sim('sim-three-sum', CAPTIONS['sim-three-sum'], TA, f'{TA}:maths/three_sum.py::three_sum'),
    'sim-merge': sim('sim-merge', CAPTIONS['sim-merge'], TA, f'{TA}:data_structures/arrays/merge_sorted.py::merge_sorted_arrays'),
    'sim-moving-window': sim('sim-moving-window', CAPTIONS['sim-moving-window']),
    'sim-variable-window': sim('sim-variable-window', CAPTIONS['sim-variable-window'], 'doocs-leetcode',
                               'doocs-leetcode:0713#Solution 1: Two Pointers'),
    'drv-sma-next': dv('sma-next'),
}

# (block, anchor in the element's source text, html key): what stands after that element
AT = [
    ('sorted-pair', 'each of them has closed in', 'sim-two-pointers'),
    ('three-sum', 'giving the affirmative solution', 'sim-three-sum'),
    ('merge', 'return C', 'sim-merge'),
    ('moving-average', 'only 3 arithmetic steps.', 'sim-moving-window'),
    ('variable-window', 'r-l+1', 'sim-variable-window'),
]
# (block, a piece of a display's TeX, html key): a display a derivation replaces (root rule 29.2)
REPLACE = [
    ('moving-average', r'\textit{SMA}_{k, \text{next}} &= \frac{1}{k} \sum_{i=n-k+2}^{n+1} p_{i}', 'drv-sma-next'),
]
# (block, what the reader gives, what the page prints, why)
FIXES = [
    ('merge', 'see Merge sort §&nbsp;Variants for discussion',
     'see [<em>Merge sort</em> §Variants] for discussion',
     'a reference to a passage the book does not carry prints as its title in italics and its own section, in '
     'brackets and with no link (RULES.md, Cross-references); Wikipedia\'s {{slink}} links its Merge sort article'),
]
# referents inside maths (\htmlData, as 1.3): the two pointers of each OI Wiki block, and tmp
MATH_REFS = [
    ('sorted-pair', {'l': 'pair-l', 'r': 'pair-r'}),
    ('variable-window', {'l': 'win-l', 'r': 'win-r', r'\mathit{tmp}': 'win-tmp'}),
]
CONCEPT = lambda cid, words: f'<span data-concept="{cid}">{words}</span>'  # noqa: E731
MARKS = [
    # concepts, one mention in each block's home; tools/apply_terms.py marks the rest from terms.jsonl
    ('two-pointers', 'Two pointers is a simple', CONCEPT('two-pointers', 'Two pointers') + ' is a simple'),
    ('three-sum', '<strong>3SUM</strong> problem', '<strong>' + CONCEPT('three-sum', '3SUM') + '</strong> problem'),
    ('merge', 'Merging two sorted lists into one', CONCEPT('merge-sorted-sequences', 'Merging two sorted lists') + ' into one'),
    ('moving-average', '<strong>simple moving average</strong>', '<strong>' + CONCEPT('sliding-window-fixed', 'simple moving average') + '</strong>'),
    ('variable-window', 'maintaining information over an interval with them',
     CONCEPT('sliding-window-variable', 'maintaining information over an interval') + ' with them'),
    # referents in words
    ('sorted-pair', 'the pointer at $n$', ref('pair-r', 'the pointer at $n$')),
    ('sorted-pair', 'the pointer at 1', ref('pair-l', 'the pointer at 1')),
    ('sorted-pair', 'our two pointers', ref('pair-l pair-r', 'our two pointers')),
    ('three-sum', 'the leftmost pointer', ref('ts-i', 'the leftmost pointer')),
    ('three-sum', 'one of the remaining pointers', ref('ts-start ts-end', 'one of the remaining pointers')),
    ('three-sum', 'the last pointer', ref('ts-start ts-end', 'the last pointer')),
    ('merge', '<em>A</em> and <em>B</em> into a new list <em>C</em>',
     ref('list-a', '<em>A</em>') + ' and ' + ref('list-b', '<em>B</em>') + ' into a new list ' + ref('list-c', '<em>C</em>')),
    ('variable-window', 'Let the two pointers be', 'Let ' + ref('win-l win-r', 'the two pointers') + ' be'),
]
