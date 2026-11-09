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
         file='3SUM.wiki', h2='3SUM',
         parts=[{'lead': True, 'cut_after': 'sum to zero.'}, {'section': 'Quadratic algorithm', 'h3': 'Quadratic algorithm'}]),
    dict(id='merge', source='wikipedia', locator='wikipedia:Merge_algorithm#Merging two lists',
         file='Merge_algorithm.wiki', h2='Merging two lists', parts=[{'section': 'Merging two lists'}]),
    dict(id='moving-average', source='wikipedia',
         locator='wikipedia:Moving_average#Simple moving average, from its opening to “…and only 3 arithmetic steps.”',
         file='Moving_average.wiki', h2='Simple moving average',
         parts=[{'section': 'Simple moving average', 'cut_after': 'only 3 arithmetic steps.'}]),
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
E_ = lambda x: f'<em>{x}</em>'  # noqa: E731
CAPTIONS = {
    'sim-two-pointers': (
        f'On a sorted array, {L_} starts at the first element and {R_} at the last. When num[{L_}] + num[{R_}] is too big, no pair '
        f'with num[{R_}] can reach the target, so {R_} moves left and its column of the pair-sum table drops out; when it is too '
        f'small, {L_} moves right and its row drops out. The pairs still possible are the triangle between {L_} and {R_}, and at '
        f'most {E_("n")} − 1 checks settle the question. The code calls {L_} and {R_} i and j and counts from 0; the text counts from 1.'),
    'sim-three-sum': (
        f'After the sort, each a = S[{ref("ts-i", E_("i"))}] is fixed in turn, and {ref("ts-start", "start")} and '
        f'{ref("ts-end", "end")} close in on b + c = −a from both sides: at most {E_("n")} − {E_("i")} − 2 checks for each a, '
        f'({E_("n")} − 1)({E_("n")} − 2)/2 in all. Where the array holds equal values the code passes over equal neighbours, so it '
        f'reports (−1, 0, 1) once where the pseudocode reports it twice. The code calls {ref("ts-start", "start")} and '
        f'{ref("ts-end", "end")} low and high.'),
    'sim-merge': (
        f'{ref("list-c", E_("C"))} grows by one element a step: the smaller of the heads of {ref("list-a", E_("A"))} and '
        f'{ref("list-b", E_("B"))}, {ref("list-a", E_("A"))}’s on a tie, so equal keys keep their order. Once one list runs out, '
        f'the rest of the other goes on the end with no more comparisons, so lists of lengths {E_("m")} and {E_("n")} take at most '
        f'{E_("m")} + {E_("n")} − 1. The code calls {ref("list-a", E_("A"))}, {ref("list-b", E_("B"))} and {ref("list-c", E_("C"))} '
        f'nums1, nums2 and merged.'),
    'sim-moving-window': (
        f'The window holds the last {E_("k")} points. Each move adds the point that comes in and subtracts the one that drops out, '
        f'three arithmetic steps whatever {E_("k")} is, against {E_("k")} to add the window up again. A larger {E_("k")} gives a '
        f'smoother line that lags further behind the data.'),
    'sim-variable-window': (
        f'{ref("win-r", E_("r"))} takes in one element a step and multiplies it into the product; while the product is at least '
        f'{E_("k")}, {ref("win-l", E_("l"))} drops elements from the left. For each {ref("win-r", E_("r"))}, {ref("win-l", E_("l"))} '
        f'is then the leftmost start of a window whose product is below {E_("k")}, so {ref("win-r", E_("r"))} − '
        f'{ref("win-l", E_("l"))} + 1 windows end at {ref("win-r", E_("r"))}. Each pointer moves right at most {E_("n")} times, '
        f'2{E_("n")} moves in all, where a double loop tries {E_("n")}({E_("n")} + 1)/2 windows. OI Wiki’s '
        f'{ref("win-tmp", E_("tmp"))} is the code’s p.'),
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
    ('merge', 'see Merge sort §\u00a0Variants for discussion',
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

MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]
LEAD = ('An Essential section on <span data-concept="two-pointers">two pointers</span>: indices that close in on a pair with '
        'a given sum, find 3SUM’s triples, merge two sorted lists, and bound windows of fixed and changing length. OI Wiki '
        'counts from 1 (num[1..n]), the 3SUM pseudocode from 0 (S[0..n−1]), the moving average by time '
        '(p<sub>n−k+1</sub> … p<sub>n</sub>). 3SUM’s sort is a library call (Chapter 10) and its hash table Chapter 5’s. '
        'These windows keep a sum, product or count, never a hash set.')

# the derivation (root rule 29; plan.md "Derivation candidates"): the moving average's update display, line by line
SMA_N = r'\textit{SMA}_{k,\text{next}}'
SMA_P = r'\textit{SMA}_{k,\text{prev}}'
DERIVATIONS = [{
    'id': 'sma-next',
    'what': 'the next simple moving average from the previous one',
    'source': 'Wikipedia, Moving average, Simple moving average',
    'nodes': [{
        'assumes': [
            {'text': rf'The previous mean is the mean over the last $k$ data points, ${SMA_P} = \frac{{1}}{{k}} \sum_{{i=n-k+1}}^{{n}} p_{{i}}$.'},
            {'text': r'The next mean is taken over the range from $n-k+2$ to $n+1$: $p_{n+1}$ comes in and $p_{n-k+1}$ drops out.'},
        ],
        'then': {'tex': rf'\mk{{L}}{{{SMA_N}}} = \mk{{s}}{{\frac{{1}}{{k}} \sum_{{i=n-k+2}}^{{n+1}} p_{{i}}}}', 'uses': [1]},
        'steps': [
            {'tex': rf'\mk{{L}}{{{SMA_N}}} = \mk{{s}}{{\frac{{1}}{{k}} \Big( p_{{n-k+2}} + \dots + p_{{n}} + p_{{n+1}} + p_{{n-k+1}} - p_{{n-k+1}} \Big)}}',
             'uses': []},
            {'tex': rf'\mk{{L}}{{{SMA_N}}} = \mk{{a}}{{\frac{{1}}{{k}} \Big( p_{{n-k+1}} + p_{{n-k+2}} + \dots + p_{{n}} \Big)}} - '
                    rf'\mk{{o}}{{\frac{{p_{{n-k+1}}}}{{k}}}} + \mk{{i}}{{\frac{{p_{{n+1}}}}{{k}}}}',
             'uses': [], 'map': {'s': ['a', 'o', 'i']}},
            {'tex': rf'\mk{{L}}{{{SMA_N}}} = \mk{{a}}{{{SMA_P}}} - \mk{{o}}{{\frac{{p_{{n-k+1}}}}{{k}}}} + \mk{{i}}{{\frac{{p_{{n+1}}}}{{k}}}}',
             'uses': [0]},
            {'tex': rf'\mk{{L}}{{{SMA_N}}} = \mk{{a}}{{{SMA_P}}} + \mk{{d}}{{\frac{{1}}{{k}} \Big( p_{{n+1}} - p_{{n-k+1}} \Big)}}',
             'uses': [], 'map': {'o': 'd', 'i': 'd'}},
        ],
    }],
}]


def _fig(fid, draws):
    return {'id': fid, 'kind': 'sim', 'draws': draws, 'ai': FIG_AI}


SECTION = {
    'id': '2.3', 'chapter': '2', 'title': TITLE, 'short': 'Two pointers',
    'lead': LEAD,
    'objectives': [], 'summary_html': '',
    # the SATA thanks to the OI Wiki Team is printed by the footer from book.json's oiwiki source row (its notice)
    'notes': ('OI Wiki’s code, its LeetCode statements, its second window example and its exercise lists, and the 3SUM '
              'article’s lead after its first sentence, are left out here.'),
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        '3SUM and merging have no open exercise here: keon’s and TheAlgorithms’ versions are tests with no printed statement. '
        'TheAlgorithms’ two_pointer, max_sum_sliding_window and sliding_window, keon’s two_sum and longest_non_repeat, and '
        'tryalgo’s windows_k_distinct are left out for the same reason. The Kattis problems closestsums, cd, hothike and '
        'snowflakes and the ICPC problems tiredterry and slidecount publish only their sample tests. Merging two linked lists '
        'comes in Section 2.5 and Kattis kayaking in Chapter 6. Project Euler 8 has no published tests. The largest-series-product '
        'card asks for linear time, which Exercism does not, and the longest-substring card tests the cases icc’s solution '
        'notebook lists and a few more. The two MIT 6.006 cards are in this section’s NC file.'),
    'figures': [
        _fig('sim-two-pointers', ['index', 'key', 'cost']),
        _fig('sim-three-sum', ['index', 'key', 'cost']),
        _fig('sim-merge', ['index', 'key', 'cost']),
        _fig('sim-moving-window', ['index', 'key', 'cost', 'size']),
        _fig('sim-variable-window', ['index', 'key', 'cost', 'size']),
    ],
    'referents': [
        {'id': 'pair-l', 'label': 'l, the left pointer (i in the code)', 'figures': ['sim-two-pointers']},
        {'id': 'pair-r', 'label': 'r, the right pointer (j in the code)', 'figures': ['sim-two-pointers']},
        {'id': 'ts-i', 'label': 'i, the index of a', 'figures': ['sim-three-sum']},
        {'id': 'ts-start', 'label': 'start, the pointer after i (low in the code)', 'figures': ['sim-three-sum']},
        {'id': 'ts-end', 'label': 'end, the pointer from the right (high in the code)', 'figures': ['sim-three-sum']},
        {'id': 'list-a', 'label': 'A, the first input list', 'figures': ['sim-merge']},
        {'id': 'list-b', 'label': 'B, the second input list', 'figures': ['sim-merge']},
        {'id': 'list-c', 'label': 'C, the merged list', 'figures': ['sim-merge']},
        {'id': 'win-l', 'label': 'l, the window’s left end', 'figures': ['sim-variable-window']},
        {'id': 'win-r', 'label': 'r, the window’s right end', 'figures': ['sim-variable-window']},
        {'id': 'win-tmp', 'label': 'tmp, the product of the window (p in the code)', 'figures': ['sim-variable-window']},
    ],
    'coverage': [
        {'span': 'two-pointers', 'concept': 'two-pointers', 'verb': 'introduces'},
        {'span': 'sorted-pair', 'concept': 'two-pointers', 'verb': 'reinforces'},
        {'span': 'three-sum', 'concept': 'three-sum', 'verb': 'introduces'},
        {'span': 'three-sum', 'concept': 'two-pointers', 'verb': 'uses'},
        {'span': 'merge', 'concept': 'merge-sorted-sequences', 'verb': 'introduces'},
        {'span': 'merge', 'concept': 'two-pointers', 'verb': 'uses'},
        {'span': 'moving-average', 'concept': 'sliding-window-fixed', 'verb': 'introduces'},
        {'span': 'variable-window', 'concept': 'sliding-window-variable', 'verb': 'introduces'},
        {'span': 'variable-window', 'concept': 'two-pointers', 'verb': 'uses'},
    ],
    'footnotes_extra': [],
    'derivations': DERIVATIONS,
}

# ---------------------------------------------------------------- exercises (config.md; plan.md "Exercises")
EXERCISM = 'sources/_cache/exercism/exercises'
TRACK = 'sources/_cache/exercism-python/exercises/practice'
ICC = 'sources/_cache/icc/recursion_dynamic/longest_substr_k_distinct'

VALUE_ERROR_JS = '''class ValueError extends Error {
  constructor(message) { super(message); this.name = 'ValueError'; }
}

'''
REVERSE_JS = '''function reverse(text) {
  const a = Array.from(text);
  let i = 0, j = a.length - 1;
  while (i < j) {
    [a[i], a[j]] = [a[j], a[i]];
    i += 1;
    j -= 1;
  }
  return a.join('');
}
'''
SLICES_JS = VALUE_ERROR_JS + '''function slices(series, length) {
  if (series.length === 0) throw new ValueError('series cannot be empty');
  if (length === 0) throw new ValueError('slice length cannot be zero');
  if (length < 0) throw new ValueError('slice length cannot be negative');
  if (series.length < length) throw new ValueError('slice length cannot be greater than series length');
  const out = [];
  for (let i = 0; i + length <= series.length; i += 1) out.push(series.slice(i, i + length));
  return out;
}
'''
LSP_PY = '''def largest_product(series, size):
    if size < 0:
        raise ValueError('span must not be negative')
    if size > len(series):
        raise ValueError('span must not exceed string length')
    if any(c not in '0123456789' for c in series):
        raise ValueError('digits input must only contain digits')
    if size == 0:
        return 1
    digits = [int(c) for c in series]
    best = 0
    product = 1  # the product of the window's nonzero digits
    zeros = 0    # how many zeros the window holds
    for r, d in enumerate(digits):
        if d == 0:
            zeros += 1
        else:
            product *= d
        if r >= size:
            out = digits[r - size]
            if out == 0:
                zeros -= 1
            else:
                product //= out
        if r >= size - 1 and zeros == 0 and product > best:
            best = product
    return best
'''
LSP_JS = VALUE_ERROR_JS + '''function largestProduct(series, size) {
  if (size < 0) throw new ValueError('span must not be negative');
  if (size > series.length) throw new ValueError('span must not exceed string length');
  if (!/^[0-9]*$/.test(series)) throw new ValueError('digits input must only contain digits');
  if (size === 0) return 1;
  const digits = Array.from(series, (c) => BigInt(c));
  let best = 0n, product = 1n, zeros = 0;
  for (let r = 0; r < digits.length; r += 1) {
    if (digits[r] === 0n) zeros += 1; else product *= digits[r];
    if (r >= size) {
      const out = digits[r - size];
      if (out === 0n) zeros -= 1; else product /= out;
    }
    if (r >= size - 1 && zeros === 0 && product > best) best = product;
  }
  return Number(best);
}
'''
SUBSTR_HARNESS_PY = '''

def longest_substr(string, k):
    # Calls your method the way icc's tests do. Leave it as it is.
    return Solution().longest_substr(string, k)
'''
SUBSTR_STARTER_JS = '''function longestSubstr(string, k) {
}
'''
SUBSTR_JS = '''function longestSubstr(string, k) {
  if (typeof string !== 'string') throw new TypeError('string must be of type str');
  if (!Number.isInteger(k)) throw new TypeError('k must be of type int');
  const count = new Map();  // how many times each character occurs in the window
  let l = 0, best = 0;
  for (let r = 0; r < string.length; r += 1) {
    count.set(string[r], (count.get(string[r]) ?? 0) + 1);
    while (count.size > k) {
      const c = string[l];
      count.set(c, count.get(c) - 1);
      if (count.get(c) === 0) count.delete(c);
      l += 1;
    }
    best = Math.max(best, r - l + 1);
  }
  return best;
}
'''


def _inline(s):
    import html
    import re
    s = html.escape(s, quote=False).replace('$', '＄')
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    return re.sub(r'(?<![\w])_([^_]+)_(?![\w])', r'<em>\1</em>', s)


def md_prompt(path):
    """An Exercism instructions.md as the card's prompt: paragraphs, and lists (nested by two spaces) as <ul>."""
    import re
    md = re.sub(r'^# Instructions\s*', '', open(path, encoding='utf-8').read()).strip()
    out = []
    for blk in re.split(r'\n\s*\n', md):
        lines = blk.split('\n')
        if lines[0].lstrip().startswith('- '):
            html_, depth = '', -1
            for l in lines:
                d = (len(l) - len(l.lstrip())) // 2
                if not l.lstrip().startswith('- '):  # a continuation line of the item before
                    html_ += ' ' + _inline(l.strip())
                    continue
                if d > depth:
                    html_ += '<ul>'
                else:
                    html_ += '</li>' + '</ul></li>' * (depth - d)
                depth = d
                html_ += '<li>' + _inline(l.strip()[2:])
            out.append(html_ + '</li>' + '</ul></li>' * depth + '</ul>')
        else:
            out.append(_inline(' '.join(x.strip() for x in lines)))
    return '\n\n'.join(out)


def track_cases(book, slug, prop):
    """The canonical cases the Python track runs: every case of the property its tests.toml does not set include = false."""
    import json
    import os
    import re
    toml = open(os.path.join(book, TRACK, slug, '.meta/tests.toml'), encoding='utf-8').read()
    off = set(re.findall(r'\[([0-9a-f-]+)\]\ndescription = "[^"]*"\ninclude = false', toml))
    on = set(re.findall(r'^\[([0-9a-f-]+)\]', toml, flags=re.M)) - off
    data = json.load(open(os.path.join(book, EXERCISM, slug, 'canonical-data.json'), encoding='utf-8'))
    out = []

    def walk(c):
        for x in c['cases']:
            if 'cases' in x:
                walk(x)
            elif x['property'] == prop and x['uuid'] in on:
                out.append(x)
    walk(data)
    return out


def tests_of(cases, visible):
    out = []
    for i, c in enumerate(cases):
        t = {'args': list(c['input'].values())}
        if isinstance(c['expected'], dict) and 'error' in c['expected']:
            t['raises'] = 'ValueError'
        else:
            t['expect'] = c['expected']
        t.update(visible=i in visible, generated_by='source')
        out.append(t)
    return out


def icc_parts(book):
    """icc's statement and constraints from the challenge notebook, and its solution class from the solution notebook."""
    import json
    import os
    nb = json.load(open(os.path.join(book, ICC, 'longest_substr_challenge.ipynb'), encoding='utf-8'))
    md = [''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'markdown']
    statement = next(m for m in md if m.startswith('## Problem:')).split('\n')[0].replace('## Problem:', '').strip()
    cons = next(m for m in md if m.startswith('## Constraints'))
    qa, cur = [], None
    for l in cons.split('\n')[1:]:
        if l.startswith('* '):
            cur = l[2:].strip()
        elif l.strip().startswith('* ') and cur:
            qa.append(f'{cur} {l.strip()[2:].strip()}.')
            cur = None
    sol = json.load(open(os.path.join(book, ICC, 'longest_substr_solution.ipynb'), encoding='utf-8'))
    code = next(''.join(c['source']) for c in sol['cells'] if c['cell_type'] == 'code' and 'def longest_substr' in ''.join(c['source']))
    return statement, qa, code.rstrip() + '\n'


def EXERCISES(exercism, book):
    import os
    ex, concepts = [], []
    meta = lambda i, src, n, origin, cite: {  # noqa: E731
        'id': i, 'source_id': src, 'source_number': n, 'origin': origin, 'kind': 'code', 'bloom': 'Apply',
        'place': {'at': 'end'}, 'cite': cite}
    example = lambda slug: open(os.path.join(book, TRACK, slug, '.meta/example.py'), encoding='utf-8').read().rstrip() + '\n'  # noqa: E731
    # c1 Exercism reverse-string: the track's example and its seven cases (the two grapheme-cluster cases are off on the track)
    ex.append(dict(meta('c1', 'exercism:reverse-string', 'reverse-string', 'exercism', 'two-pointers'),
                   prompt=md_prompt(os.path.join(book, EXERCISM, 'reverse-string/instructions.md')),
                   answer={'type': 'code',
                           'python': {'entry': 'reverse', 'starter': 'def reverse(text):\n    pass\n', 'reference': example('reverse-string'),
                                      'generated_by': 'source'},
                           'javascript': {'entry': 'reverse', 'starter': 'function reverse(text) {\n}\n', 'reference': REVERSE_JS,
                                          'generated_by': 'ai'},
                           'tests': tests_of(track_cases(book, 'reverse-string', 'reverse'), {1, 3}),
                           'bound': 'n',
                           'grow': "(n, rand) => [Array.from({ length: n }, () => String.fromCharCode(rand.int(97, 122))).join('')]",
                           'generated_by': 'source'}))
    concepts.append({'exercise': 'c1', 'concept': 'two-pointers'})
    # c2 Exercism series
    ex.append(dict(meta('c2', 'exercism:series', 'series', 'exercism', 'moving-average'),
                   changes=('The tests expect a ValueError for an empty series and for a length that is zero, negative or longer '
                            'than the series.'),
                   prompt=md_prompt(os.path.join(book, EXERCISM, 'series/description.md')),
                   answer={'type': 'code',
                           'python': {'entry': 'slices', 'starter': 'def slices(series, length):\n    pass\n', 'reference': example('series'),
                                      'generated_by': 'source'},
                           'javascript': {'entry': 'slices', 'starter': VALUE_ERROR_JS + 'function slices(series, length) {\n}\n',
                                          'reference': SLICES_JS, 'generated_by': 'ai'},
                           'tests': tests_of(track_cases(book, 'series', 'slices'), {3, 8}),
                           'generated_by': 'source'}))
    concepts.append({'exercise': 'c2', 'concept': 'sliding-window-fixed'})
    # c3 Exercism largest-series-product: the track's cases, the AI's linear references
    ex.append(dict(meta('c3', 'exercism:largest-series-product', 'largest-series-product', 'exercism', 'moving-average'),
                   changes=('A solution must run in time linear in the length of the input; the source asks for no bound. The '
                            'tests expect a ValueError for a negative span, a span longer than the input and a character that is '
                            'not a digit.'),
                   prompt=md_prompt(os.path.join(book, EXERCISM, 'largest-series-product/instructions.md')),
                   answer={'type': 'code',
                           'python': {'entry': 'largest_product', 'starter': 'def largest_product(series, size):\n    pass\n',
                                      'reference': LSP_PY, 'generated_by': 'ai'},
                           'javascript': {'entry': 'largestProduct', 'starter': VALUE_ERROR_JS + 'function largestProduct(series, size) {\n}\n',
                                          'reference': LSP_JS, 'generated_by': 'ai'},
                           'tests': tests_of(track_cases(book, 'largest-series-product', 'largestProduct'), {1, 6}),
                           'bound': 'n',
                           'grow': ("(n, rand) => [Array.from({ length: n }, () => (rand() < 0.9 ? '1' : String(rand.int(2, 9)))).join(''), "
                                    "Math.floor(n / 2)]"),
                           'generated_by': 'source'}))
    concepts.append({'exercise': 'c3', 'concept': 'sliding-window-fixed'})
    # c4 icc longest_substr_k_distinct: icc's four asserts and its solution, and AI tests
    statement, qa, cls = icc_parts(book)
    src = lambda args, expect, visible=False: {'args': args, 'expect': expect, 'visible': visible, 'generated_by': 'source'}  # noqa: E731
    ai = lambda args, expect: {'args': args, 'expect': expect, 'visible': False, 'generated_by': 'ai'}  # noqa: E731
    tests = [
        {'args': [None, 3], 'raises': 'TypeError', 'visible': False, 'generated_by': 'source'},
        src(['', 3], 0), src(['abcabcdefgghiij', 3], 6, True), src(['abcabcdefgghighij', 3], 7),
        ai(['abc', 0], 0), ai(['a', 1], 1), ai(['aaaa', 1], 4), ai(['abcab', 10], 5), ai(['aabbbbbbcc', 1], 6), ai(['eceba', 2], 3),
    ]
    starter = 'class Solution(object):\n\n    def longest_substr(self, string, k):\n        pass\n' + SUBSTR_HARNESS_PY
    ex.append(dict(meta('c4', 'icc:recursion_dynamic/longest_substr_k_distinct', 'longest_substr_k_distinct', 'icc', 'variable-window'),
                   changes=('The tests call longest_substr(string, k), which the starter defines over your Solution class, and a '
                            'string that is not a str raises a TypeError.'),
                   prompt=statement + '\n\n' + '\n\n'.join(qa),
                   answer={'type': 'code',
                           'python': {'entry': 'longest_substr', 'starter': starter, 'reference': cls + SUBSTR_HARNESS_PY,
                                      'generated_by': 'source'},
                           'javascript': {'entry': 'longestSubstr', 'starter': SUBSTR_STARTER_JS, 'reference': SUBSTR_JS,
                                          'generated_by': 'ai'},
                           'tests': tests, 'bound': 'n',
                           'grow': "(n, rand) => [Array.from({ length: n }, () => 'abc'[rand.int(0, 2)]).join(''), 3]",
                           'generated_by': 'source'}))
    concepts.append({'exercise': 'c4', 'concept': 'sliding-window-variable'})
    return ex, concepts

# each occurrence of a file's frame in the Wikipedia blocks: what stands there (None: left out, the plan decides every
# figure, and the moving-average chart is not kept)
IMAGES = {
    'Moving Average Types comparison - Simple and Exponential.png': [None],
}

