"""What tools/build_translation.py (with tools/oiwiki_boxes.py) needs to assemble 2.4 Prefix sums and difference
arrays (the plan is plan.md beside this file).

The Chinese comes from OI Wiki's page by script (source.md); the English is translation.md, written block by
block under translate.md and checked against the source element for element. Everything here is placement and
markup: the blocks, their headings and the boxes they leave out, the code set and the two figures and where they
stand, and the spans that mark concepts and the erratum. The code set's Python is read from the TheAlgorithms
cache by script; its Java, C++ and JavaScript are the AI's translations (decision 20), run against the Python's
doctests before they were written here (plan.md, log-pass.md).

    python3 -I tools/oiwiki_boxes.py ch02/2.4 --check
"""
import html
import os
import re

TITLE = 'Prefix sums and difference arrays'
OIWIKI_FILE = 'sources/_cache/oiwiki/docs/basic/prefix-sum.md'
TRANSLATION = 'translation.md'
AI = 'claude-opus-5-5 high'
BOOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LOC = 'oiwiki:basic/prefix-sum'
P1387 = '[洛谷 P1387 最大正方形](https://www.luogu.com.cn/problem/P1387)'
BLOCKS = [
    dict(id='prefix-sums', source='oiwiki',
         locator=f'{LOC}#引入 (with its 规定 box), #前缀和 (its heading dropped) and #一维前缀和',
         h2='Prefix sums', drop_headings=['前缀和'], **{'from': '## 引入', 'to': '### 二维/多维前缀和'}),
    # OI Wiki's practice-problem box and the code boxes nothing licensed replaces are left out (plan.md)
    dict(id='prefix-sums-2d', source='oiwiki',
         locator=f'{LOC}#二维/多维前缀和 (its opening), #基于容斥原理 and #逐维前缀和',
         drop_boxes=[P1387, '参考代码', '三维前缀和的参考实现'], **{'from': '### 二维/多维前缀和', 'to': '#### 特例：子集和 DP'}),
    dict(id='difference-array', source='oiwiki', locator=f'{LOC}#差分 (its opening) and #一维差分',
         h2='Difference arrays', **{'from': '## 差分', 'to': '### 二维/多维差分'}),
    dict(id='difference-array-2d', source='oiwiki', locator=f'{LOC}#二维/多维差分',
         h2='Two-dimensional and multidimensional difference arrays', drop_boxes=['参考代码'],
         **{'from': '### 二维/多维差分', 'to': '### 树上差分'}),
]

# ---------------------------------------------------------------- the code set (OI Wiki's 参考实现 box replaced)
TA_FILE = 'sources/_cache/thealgorithms-python/data_structures/arrays/prefix_sum.py'
TA_LOC = 'thealgorithms-python:data_structures/arrays/prefix_sum.py::PrefixSum'


def thealgorithms_python():
    """PrefixSum's __init__ and get_sum as the file prints them. Left out, each for its reason: the module
    docstring (author and date, kept by the credit), the docstrings of the methods (doctests: a test source,
    decision 19), contains_sum (a hash set, chapter 5) and the doctest runner."""
    src = open(os.path.join(BOOK, TA_FILE), encoding='utf-8').read().split('\n')
    a = src.index('class PrefixSum:')
    z = next(i for i, l in enumerate(src) if l.startswith('    def contains_sum'))
    out, doc = [], False
    for l in src[a:z]:
        if l.strip().startswith('"""'):
            doc = not doc if l.strip() == '"""' or l.strip().count('"""') == 1 else doc
            continue
        if not doc:
            out.append(l)
    while out and not out[-1].strip():
        out.pop()
    # a docstring's closing quotes leave the blank line the file puts after them: one blank between
    text = re.sub(r'\n\n\n+', '\n\n', '\n'.join(out))
    return re.sub(r'(-> int:)\n\n', r'\1\n', text)


JAVA = '''class PrefixSum {
    private final int[] prefixSum;

    PrefixSum(int[] array) {
        int lenArray = array.length;
        prefixSum = new int[lenArray];

        if (lenArray > 0) {
            prefixSum[0] = array[0];
        }

        for (int i = 1; i < lenArray; i++) {
            prefixSum[i] = prefixSum[i - 1] + array[i];
        }
    }

    int getSum(int start, int end) {
        if (prefixSum.length == 0) {
            throw new IllegalArgumentException("The array is empty.");
        }

        if (start < 0 || end >= prefixSum.length || start > end) {
            throw new IllegalArgumentException("Invalid range specified.");
        }

        if (start == 0) {
            return prefixSum[end];
        }

        return prefixSum[end] - prefixSum[start - 1];
    }
}'''
CPP = '''class PrefixSum {
    std::vector<int> prefix_sum;

public:
    explicit PrefixSum(const std::vector<int>& array) {
        std::size_t len_array = array.size();
        prefix_sum.assign(len_array, 0);

        if (len_array > 0) {
            prefix_sum[0] = array[0];
        }

        for (std::size_t i = 1; i < len_array; i++) {
            prefix_sum[i] = prefix_sum[i - 1] + array[i];
        }
    }

    int get_sum(int start, int end) const {
        if (prefix_sum.empty()) {
            throw std::invalid_argument("The array is empty.");
        }

        if (start < 0 || end >= static_cast<int>(prefix_sum.size()) || start > end) {
            throw std::invalid_argument("Invalid range specified.");
        }

        if (start == 0) {
            return prefix_sum[end];
        }

        return prefix_sum[end] - prefix_sum[start - 1];
    }
};'''
JS = '''class PrefixSum {
    constructor(array) {
        const lenArray = array.length;
        this.prefixSum = new Array(lenArray).fill(0);

        if (lenArray > 0) {
            this.prefixSum[0] = array[0];
        }

        for (let i = 1; i < lenArray; i++) {
            this.prefixSum[i] = this.prefixSum[i - 1] + array[i];
        }
    }

    getSum(start, end) {
        if (this.prefixSum.length === 0) {
            throw new RangeError("The array is empty.");
        }

        if (start < 0 || end >= this.prefixSum.length || start > end) {
            throw new RangeError("Invalid range specified.");
        }

        if (start === 0) {
            return this.prefixSum[end];
        }

        return this.prefixSum[end] - this.prefixSum[start - 1];
    }
}'''


def code_set():
    e = lambda s: html.escape(s, quote=False)
    pres = [f'<pre data-lang="python"><code>{e(thealgorithms_python())}</code></pre>',
            f'<pre data-lang="java" data-ai="{AI}"><code>{e(JAVA)}</code></pre>',
            f'<pre data-lang="cpp" data-ai="{AI}"><code>{e(CPP)}</code></pre>',
            f'<pre data-lang="javascript" data-ai="{AI}"><code>{e(JS)}</code></pre>']
    return f'<div class="code-set" data-source="thealgorithms-python" data-locator="{TA_LOC}">\n' + '\n'.join(pres) + '\n</div>'


# ---------------------------------------------------------------- the two figures
def sim(fid, caption, attrs=''):
    return (f'<figure class="sim" id="{fid}"{attrs}>\n'
            f'  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>')


ORIGINAL_2D = '/media/ch02/oiwiki-prefix-sum-2d.png'
ORIGINAL_2D_CAPTION = 'Example of a two-dimensional prefix sum'   # OI Wiki's alt text, 二维前缀和示例, translated
HTML = {
    'code-prefix-sum': code_set(),
    'sim-prefix-2d': sim(
        'sim-prefix-2d',
        'The example’s matrix <em>A</em>, and beside it its prefix sums <em>S</em>, with a row and a column of zeros in front. '
        'Each cell of <em>S</em> is the cell of <em>A</em> plus the red block above it and the blue block to its left, less their '
        'overlap, which both blocks count. A query reads four cells of <em>S</em> the same way.',
        ' data-source="doocs-leetcode" data-locator="doocs-leetcode:0304#Solution 1: Two-dimensional Prefix Sum"'
        f' data-original="{ORIGINAL_2D}" data-original-caption="{ORIGINAL_2D_CAPTION}"'),
    'sim-range-add': sim(
        'sim-range-add',
        'Adding <span data-ref="c"><em>c</em></span> to a[<span data-ref="l"><em>l</em></span>..<span data-ref="r"><em>r</em></span>] '
        'writes two cells of the difference array d: <span data-ref="c"><em>c</em></span> at <span data-ref="l"><em>l</em></span>, '
        'and −<span data-ref="c"><em>c</em></span> just past <span data-ref="r"><em>r</em></span>, unless '
        '<span data-ref="r"><em>r</em></span> is the last cell. The prefix pass over d, cell <span data-ref="i"><em>i</em></span> by cell, spreads each add back over its range, '
        'and d turns into the array.',
        ' data-source="doocs-leetcode" data-locator="doocs-leetcode:0370#Solution 1: Difference Array"'),
}

FN_20 = '<sup class="fn" data-note="err-2d-example"></sup>'
MARKS = [
    # the introducing spans of the four concepts
    ('prefix-sums', 'A prefix sum can be understood', '<span data-concept="prefix-sums">A prefix sum</span> can be understood'),
    ('prefix-sums-2d', 'case gives multidimensional prefix sums.',
     'case gives <span data-concept="prefix-sums-2d">multidimensional prefix sums</span>.'),
    ('difference-array', 'Taking differences is a strategy', '<span data-concept="difference-array">Taking differences</span> is a strategy'),
    ('difference-array-2d', 'the two-dimensional difference is defined as',
     'the <span data-concept="difference-array-2d">two-dimensional difference</span> is defined as'),
    # erratum 20: the numbers of S_{2,3} and S_{3,2} are listed in the other order
    ('prefix-sums-2d', 'and we should have', 'and we should have' + FN_20),
]

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]
LEAD = ('Essential; the <span data-concept="prefix-sums-2d">two-dimensional prefix sums</span> and '
        '<span data-concept="difference-array-2d">differences</span> are Advanced. Running totals for range-sum queries, and their '
        'inverse, differences, for range updates. The text counts from 1, with a<sub>0</sub> = S<sub>0</sub> = 0 (its Convention box); '
        'the code counts from 0. TheAlgorithms’ PrefixSum treats a range starting at 0 apart, and the doocs code pads its table '
        'with a zero row and column, so s[i + 1][j + 1] is S<sub>i+1, j+1</sub>, and writes d[r + 1].')

SECTION = {
    'id': '2.4', 'chapter': '2', 'title': TITLE, 'short': 'Prefix sums',
    'lead': LEAD,
    'objectives': [], 'summary_html': '',
    'notes': 'OI Wiki’s code, its Luogu P1387 example and its sections on subset sums and on trees are not included here.',
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'No exercise with a printed statement and tests poses a prefix-sum or difference-array problem yet. TheAlgorithms’ '
        'PrefixSum and equilibrium-index doctests and keon’s sum_sub_squares tests are tests with no statement of their own; the '
        'Kattis problems sumoftheothers, commercials, shortsell, pivot and freefood come with sample data only; and Kattis '
        'subseqhard, which needs a hash map, is held for chapter 5.'),
    'figures': [
        {'id': 'sim-prefix-2d', 'kind': 'sim', 'originals': [ORIGINAL_2D], 'original_caption': ORIGINAL_2D_CAPTION,
         'draws': ['key', 'cost'], 'facts': ['#2f6fd6', '#d64538'], 'ai': FIG_AI},
        {'id': 'sim-range-add', 'kind': 'sim', 'draws': ['key', 'cost'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'l', 'label': 'l, the first index of an update', 'figures': ['sim-range-add']},
        {'id': 'r', 'label': 'r, the last index of an update', 'figures': ['sim-range-add']},
        {'id': 'c', 'label': 'c, the number an update adds', 'figures': ['sim-range-add']},
        {'id': 'i', 'label': 'i, the cell of the prefix pass', 'figures': ['sim-range-add']},
    ],
    'coverage': [
        {'span': 'prefix-sums', 'concept': 'prefix-sums', 'verb': 'introduces'},
        {'span': 'prefix-sums-2d', 'concept': 'prefix-sums-2d', 'verb': 'introduces'},
        {'span': 'prefix-sums-2d', 'concept': 'prefix-sums', 'verb': 'uses'},
        {'span': 'difference-array', 'concept': 'difference-array', 'verb': 'introduces'},
        {'span': 'difference-array', 'concept': 'prefix-sums', 'verb': 'uses'},
        {'span': 'difference-array-2d', 'concept': 'difference-array-2d', 'verb': 'introduces'},
        {'span': 'difference-array-2d', 'concept': 'prefix-sums-2d', 'verb': 'uses'},
        {'span': 'difference-array-2d', 'concept': 'difference-array', 'verb': 'uses'},
    ],
    'footnotes_extra': [
        {'id': 'err-2d-example', 'kind': 'correction',
         'html': 'The numbers are listed in the other order from the terms: by the figure, <em>S</em><sub>2,3</sub> = 15 and '
                 '<em>S</em><sub>3,2</sub> = 18. The sum, 29, is right.'},
    ],
    'derivations': [],
}
