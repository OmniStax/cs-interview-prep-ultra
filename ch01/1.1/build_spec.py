"""What tools/build_text.py needs to assemble 1.1 What an algorithm is (the plan is plan.md beside this file).

Everything here is placement, markup or a small correction of what the extraction gets wrong; the source's
words come from the converters. Each FIXES entry says why it is there.
"""
TITLE = 'What an algorithm is'
JEFFE_PDF = 'sources/_cache/jeffe/00-intro.pdf'
JEFFE_PAGES = range(1, 16)

BLOCKS = [
    dict(id='algorithm', source='jeffe', locator='jeffe:0.1', h2='What is an algorithm?',
         **{'from': 'An algorithm is an explicit', 'to': '0.2 Multiplication'}),
    dict(id='lattice', source='jeffe', locator='jeffe:0.2, the preamble and “Lattice Multiplication”', h2='Lattice Multiplication',
         drop_first_heading=True, drop_headings=['Lattice Multiplication'], **{'from': '0.2 Multiplication', 'to': 'Duplation and Mediation'}),
    dict(id='peasant', source='jeffe', locator='jeffe:0.2, “Duplation and Mediation”', h2='Duplation and Mediation',
         drop_first_heading=True, **{'from': 'Duplation and Mediation', 'to': 'Compass and Straightedge'}),
    dict(id='compass', source='jeffe', locator='jeffe:0.2, “Compass and Straightedge”', h2='Compass and Straightedge',
         drop_first_heading=True, **{'from': 'Compass and Straightedge', 'to': '0.3 Congressional Apportionment'}),
    dict(id='apportionment', source='jeffe', locator='jeffe:0.3', h2='Congressional Apportionment',
         drop_first_heading=True, **{'from': '0.3 Congressional Apportionment', 'to': '0.4 A Bad Example'}),
    dict(id='underspecified', source='jeffe', locator='jeffe:0.4', h2='A Bad Example',
         drop_first_heading=True, **{'from': '0.4 A Bad Example', 'to': '0.5 Describing Algorithms'}),
    dict(id='describing', source='jeffe', locator='jeffe:0.5', h2='Describing Algorithms',
         drop_first_heading=True, **{'from': '0.5 Describing Algorithms', 'to': '0.6 Analyzing Algorithms'}),
    dict(id='correctness', source='jeffe', locator='jeffe:0.6, from its opening to the end of “Correctness”', h2='Analyzing Algorithms',
         drop_first_heading=True, **{'from': '0.6 Analyzing Algorithms', 'to': 'Running Time'}),
    dict(id='efficiency', source='ods', file='sources/_cache/ods/latex/intro.tex', lines=(49, 123),
         locator='ods:intro#the-need-for-efficiency, to the end of “The solution”, before “The remainder of this chapter”',
         h2='The Need for Efficiency'),
    dict(id='interfaces', source='ods', file='sources/_cache/ods/latex/intro.tex', lines=(141, 168),
         locator='ods:intro#sec:interfaces, its opening, before “The Queue, Stack, and Deque Interfaces”',
         h2='Interfaces'),
]

# Display formulas: the PDF draws each in pieces (limits, sum signs and brace parts on lines of their own),
# so each is set here in LaTeX from the page render, keyed by page and order on the page.
DISPLAYS = {
    'p4#1': r'x = \sum_{i=0}^{m-1} X[i]\cdot 10^i \quad\text{and}\quad y = \sum_{j=0}^{n-1} Y[j]\cdot 10^j,',
    'p4#2': r'z = x\cdot y = \sum_{k=0}^{m+n-1} Z[k]\cdot 10^k.',
    'p4#3': r'x\cdot y = \sum_{i=0}^{m-1}\sum_{j=0}^{n-1}\bigl(X[i]\cdot Y[j]\cdot 10^{i+j}\bigr).',
    'p6#1': r'x\cdot y = \begin{cases} 0 & \text{if } x = 0\\ \lfloor x/2\rfloor\cdot(y+y) & \text{if } x \text{ is even}\\ \lfloor x/2\rfloor\cdot(y+y)+y & \text{if } x \text{ is odd} \end{cases}',
}
# Lines the classifier would read wrongly: (page, baseline, kind).
KIND_OVERRIDES = [
    (9, 507.9, 'drop'),   # the radical sign of P/√(r(r+1)), drawn on a baseline of its own; FIXES sets the formula
]
# A word broken at a line end that keeps its hyphen.
KEEP_HYPHEN = ['Well-']

# (what the extraction gives, what the page prints, why)
FIXES = [
    ('multiplication</em></strong>.A variant', 'multiplication</em></strong>. A variant', 'the page break falls after "A"; the space is narrower than the reader takes for a word space'),
    ('multiplication***.A variant', 'multiplication***. A variant', 'the same, in source.md'),
    ('1172 <sub>8</sub><sup>1</sup>', '1172⅛', 'a stacked fraction reads as a subscript and a superscript'),
    ('1373877 <sub>6</sub><sup>1</sup><sub>4</sub>', '1373877¹⁄₆₄', 'the same, 1/64'),
    ('logmin{', 'log min{', 'the math font sets "log min" with a thin space the reader takes for none'),
    ('logmax{', 'log max{', 'the same, "log max"'),
    ('<em>x y</em>', '<em>xy</em>', 'the italic correction after x reads as a space; the page prints log(xy)'),
    ('*x y*', '*xy*', 'the same, in source.md'),
    ('<em>m</em>+ <em>n</em>', '<em>m</em> + <em>n</em>', 'an operator at a style break keeps its spaces'),
    ('<em>P/ r</em>(<em>r</em> + 1), where', '$P/\\sqrt{r(r+1)}$, where', 'the radical is drawn apart from its radicand; the page prints P/√(r(r + 1))'),
    ('*P/ r*(*r* + 1), where', '$P/\\sqrt{r(r+1)}$, where', 'the same, in source.md'),
    ('skeptical novice! √', 'skeptical novice!', 'the √ of the next footnote is drawn on this footnote\'s baseline'),
    ('sing “ 2 Bottles', 'sing “√2 Bottles', 'the √ of "√2 Bottles" is drawn a line up (see the previous entry)'),
    ('<em>P/</em>(', '<em>P</em>/(', 'the slash is set in the math italic font but is not a variable'),
    ('<em>/</em>|', '/|', 'the same slash in |AC||AD|/|AB|'),
]

# ODS cross-references, to this book's pages (bridge B5): the reference, its link and its Markdown.
ODS_REFS = {
    '\\chapref{arrays}': ('<a href="/cs-interview-prep-ultra/ch02/2.2/">Section 2.2</a>', 'Section 2.2'),
    '\\chapref{linkedlists}': ('<a href="/cs-interview-prep-ultra/ch02/2.5/">Sections 2.5–2.6</a>', 'Sections 2.5–2.6'),
    '\\secref{interfaces}': ('the next section', 'the next section'),
}

AI = 'claude-opus-5-5 high'


def _code(s):
    import html
    return html.escape(s.strip('\n'), quote=False).replace('$', '&#36;')


BOTTLES = {
    'python': '''
def bottles_of_beer(n):
    for i in range(n, 0, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer,")
        print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.")
    print("No bottles of beer on the wall, no bottles of beer,")
    print(f"Go to the store, buy some more, {n} bottles of beer on the wall.")
''',
    'java': '''
static void bottlesOfBeer(int n) {
    for (int i = n; i >= 1; i--) {
        System.out.println(i + " bottles of beer on the wall, " + i + " bottles of beer,");
        System.out.println("Take one down, pass it around, " + (i - 1) + " bottles of beer on the wall.");
    }
    System.out.println("No bottles of beer on the wall, no bottles of beer,");
    System.out.println("Go to the store, buy some more, " + n + " bottles of beer on the wall.");
}
''',
    'cpp': '''
void bottlesOfBeer(int n) {
    for (int i = n; i >= 1; i--) {
        std::cout << i << " bottles of beer on the wall, " << i << " bottles of beer,\\n";
        std::cout << "Take one down, pass it around, " << i - 1 << " bottles of beer on the wall.\\n";
    }
    std::cout << "No bottles of beer on the wall, no bottles of beer,\\n";
    std::cout << "Go to the store, buy some more, " << n << " bottles of beer on the wall.\\n";
}
''',
    'javascript': '''
function bottlesOfBeer(n) {
  for (let i = n; i >= 1; i--) {
    console.log(`${i} bottles of beer on the wall, ${i} bottles of beer,`);
    console.log(`Take one down, pass it around, ${i - 1} bottles of beer on the wall.`);
  }
  console.log("No bottles of beer on the wall, no bottles of beer,");
  console.log(`Go to the store, buy some more, ${n} bottles of beer on the wall.`);
}
''',
}


def code_set(src):
    pres = [f'<pre data-lang="{l}" data-ai="{AI}"><code>{_code(src[l])}</code></pre>' for l in ('python', 'java', 'cpp', 'javascript')]
    return '<div class="code-set">\n' + '\n'.join(pres) + '\n</div>'


def sim(fid, caption, original=None, original_caption=None):
    attrs = f'class="sim" id="{fid}"'
    if original:
        attrs += f' data-original="{original}" data-original-caption="{original_caption}"'
    return f'<figure {attrs}>\n  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>'


def photo(fid, src, caption, credit):
    return (f'<figure class="photo" id="{fid}">\n  <img src="{src}" alt="">\n'
            f'  <figcaption><span>{caption} {credit}</span></figcaption>\n</figure>')


HTML = {
    'bottles-code': code_set(BOTTLES),
    'sim-lattice': sim(
        'sim-lattice',
        'The lattice for <span data-ref="lat-k">column</span> after column: each column adds the products '
        '<em>X</em>[<span data-ref="lat-i"><em>i</em></span>] · <em>Y</em>[<span data-ref="lat-j"><em>j</em></span>] '
        'whose positions sum to <span data-ref="lat-k"><em>k</em></span>, writes the low digit of '
        '<span data-ref="lat-hold"><em>hold</em></span> as <em>Z</em>[<span data-ref="lat-k"><em>k</em></span>] '
        'and carries the rest. The settled digits of the product fill in from the right; the count of '
        'single-digit products ends at exactly <em>m</em> · <em>n</em> whatever the digits are.'),
    'photo-treviso': photo(
        'photo-treviso', '/media/ch01/jeffe-0-1-treviso.png',
        '{{caption 0.1}}',
        'Image: Biblioteca nazionale Braidense (Milano), public domain, as credited in Erickson’s Image Credits.'),
    'photo-eutocius': photo(
        'photo-eutocius', '/media/ch01/jeffe-0-2-eutocius.png',
        '{{caption 0.2}}',
        'Image: Internet Archive, public domain, as credited in Erickson’s Image Credits.'),
    'sim-peasant': sim(
        'sim-peasant',
        'Peasant multiplication as a table: each row halves <span data-ref="x"><em>x</em></span>, rounding down, '
        'and doubles <span data-ref="y"><em>y</em></span>, and a row adds <span data-ref="y"><em>y</em></span> to '
        '<span data-ref="prod"><em>prod</em></span> only when <span data-ref="x"><em>x</em></span> is odd. '
        'Through every row <span data-ref="prod"><em>prod</em></span> + <span data-ref="x"><em>x</em></span> · '
        '<span data-ref="y"><em>y</em></span> stays equal to the product asked for, so when '
        '<span data-ref="x"><em>x</em></span> reaches 0, <span data-ref="prod"><em>prod</em></span> is the answer. '
        'The kept rows, read from the bottom up, spell <span data-ref="x"><em>x</em></span> in binary.',
        '/media/ch01/jeffe-0-3-peasant.png', '{{caption-text 0.3}}'),
    'sim-compass': sim(
        'sim-compass',
        'Euclid’s construction, one primitive at a time: from <span data-ref="C">C</span> and '
        '<span data-ref="D">D</span> it draws only lines and circles, and the point <span data-ref="Z">Z</span> '
        'lands at the distance |AC| · |AD| / |AB| from A along the line AC. Whatever the two lengths, the triangles '
        'ACE and AZF are similar, which is why it works, and the construction takes the same number of primitives.',
        '/media/ch01/jeffe-0-4-compass.png', '{{caption-text 0.4}}'),
    'sim-apportion': sim(
        'sim-apportion',
        'Huntington–Hill on the 2020 census: every state starts with one seat, and each later seat goes to the '
        'state <span data-ref="s"><em>s</em></span> at the head of the priority queue, whose priority is then '
        'recomputed from its new number of seats. The queue is one sorted column, as the Census Bureau '
        'keeps it. On the 50 states with 435 seats the run gives every state the seats the House has had since 2023.',
        '/media/ch01/jeffe-0-5-apportion.png', '{{caption-text 0.5}}'),
    'sim-scan-cost': sim(
        'sim-scan-cost',
        'How long a structure that inspects every item takes: <span data-type="size">the number of items</span> '
        'times <span data-type="size">the number of operations</span>, divided by the speed of the machine. With '
        'either count in the billions the time runs to years; when each operation inspects only about two items, it '
        'drops below a second.'),
}

# Pseudocode and its code are one listing: BottlesOfBeer is the first variant of its code set, and
# FibonacciMultiply the first language of sim-lattice's code panel (figures.js carries it, as the PDF prints it).
PSEUDO = {
    'BottlesOfBeer(n):': ('set', 'bottles-code'),
    'FibonacciMultiply(X[0 .. m − 1], Y[0 .. n − 1]):': ('sim', 'sim-lattice'),
}
AFTER_PRE = {
    'BottlesOfBeer(n):': ['bottles-code'],
    'FibonacciMultiply(X[0 .. m − 1], Y[0 .. n − 1]):': ['sim-lattice'],
}
AFTER_TEXT = {
    'peasant': [('rounding down).', 'sim-peasant')],
    'lattice': [('mathematics book in the West.', 'photo-treviso'), ('mathematics book in the West.', 'photo-eutocius')],
    'compass': [('chosen for', 'sim-compass')],
    'apportionment': [('allocated to each state.', 'sim-apportion')],
    'efficiency': [('16 minutes and 40 seconds', 'sim-scan-cost')],
}

FN_APPORTION = '<sup class="fn" data-note="err-apportion"></sup>'
# (block, text as built, replacement, [count]): links to the figures the prose cites by the source's number,
# the erratum's marker, the spans that introduce each concept and the referents the figures draw.
MARKS = [
    # the figures the prose cites, linked (plans-summary question 18)
    ('lattice', 'on the right in Figure 0.1', 'on the right in <a href="#photo-treviso">Figure 0.1</a>'),
    ('lattice', 'on the left in Figure 0.1', 'on the left in <a href="#photo-treviso">Figure 0.1</a>'),
    ('lattice', 'as shown in Figure 0.2', 'as shown in <a href="#photo-eutocius">Figure 0.2</a>'),
    ('compass', 'Figure 0.4 shows', '<a href="#sim-compass">Figure 0.4</a> shows'),
    ('apportionment', 'in pseudocode in Figure 0.5.', 'in pseudocode in <a href="#sim-apportion">Figure 0.5</a>.' + FN_APPORTION),
    # concepts
    ('algorithm', 'An algorithm is', '<span data-concept="algorithm">An algorithm</span> is'),
    ('lattice', 'lattice algorithm</em></strong>', '<span data-concept="lattice-multiplication">lattice algorithm</span></em></strong>'),
    ('peasant', 'peasant multiplication</em></strong>', '<span data-concept="peasant-multiplication">peasant multiplication</span></em></strong>'),
    ('apportionment', 'Huntington-Hill method</em></strong>', '<span data-concept="apportionment">Huntington-Hill method</span></em></strong>'),
    ('underspecified', 'is <em>not</em> actually an algorithm', 'is <span data-concept="underspecified-algorithm"><em>not</em> actually an algorithm</span>'),
    ('describing', 'a complete description of any algorithm has four components', '<span data-concept="describing-algorithms">a complete description of any algorithm has four components</span>'),
    ('efficiency', 'do not scale well', '<span data-concept="need-for-efficiency">do not scale well</span>'),
    ('interfaces', 'An <em>interface</em>', 'An <span data-concept="interface-vs-implementation"><em>interface</em></span>'),
    ('interfaces', '<em>implementation</em>', '<span data-concept="interface-vs-implementation"><em>implementation</em></span>'),
    # running times, which are costs
    ('lattice', '<strong><em>O</em>(<em>mn</em>) <em>time</em></strong>', '<span data-type="cost"><strong><em>O</em>(<em>mn</em>) <em>time</em></strong></span>'),
    ('peasant', '<strong><em>O</em>(<em>mn</em>) <em>time</em></strong>', '<span data-type="cost"><strong><em>O</em>(<em>mn</em>) <em>time</em></strong></span>'),
    # the other cost bounds of the peasant passage, as 1.4 marks Erickson's (chapter 1 pass)
    ('peasant', 'performs <em>O</em>(log <em>x</em>) parity', 'performs <span data-type="cost"><em>O</em>(log <em>x</em>)</span> parity'),
    ('peasant', 'this bound to <em>O</em>(log min{<em>x</em>, <em>y</em>})', 'this bound to <span data-type="cost"><em>O</em>(log min{<em>x</em>, <em>y</em>})</span>'),
    ('peasant', 'at most <em>O</em>(log(<em>xy</em>)) = <em>O</em>(log max{<em>x</em>, <em>y</em>}) single-digit operations', 'at most <span data-type="cost"><em>O</em>(log(<em>xy</em>)) = <em>O</em>(log max{<em>x</em>, <em>y</em>}) single-digit operations</span>'),
    ('peasant', 'algorithm is <em>O</em>(log min{<em>x</em>, <em>y</em>} · log max{<em>x</em>, <em>y</em>}) = <em>O</em>(log <em>x</em> · log <em>y</em>).', 'algorithm is <span data-type="cost"><em>O</em>(log min{<em>x</em>, <em>y</em>} · log max{<em>x</em>, <em>y</em>}) = <em>O</em>(log <em>x</em> · log <em>y</em>)</span>.'),
    # referents the figures draw
    ('peasant', 'non-negative integers <em>x</em> and <em>y</em>', 'non-negative integers <span data-ref="x"><em>x</em></span> and <span data-ref="y"><em>y</em></span>'),
    ('compass', '<em>C</em>, and <em>D</em>, and the goal is to construct a point <em>Z</em>',
     '<span data-ref="C"><em>C</em></span>, and <span data-ref="D"><em>D</em></span>, and the goal is to construct a point <span data-ref="Z"><em>Z</em></span>'),
]

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]
SECTION = {
    'id': '1.1', 'chapter': '1', 'title': 'What an algorithm is', 'short': 'Algorithms',
    'lead': ('An Essential section on what makes a procedure an <span data-concept="algorithm">algorithm</span>, how to '
             'describe one and why its cost matters, told through a song, three ways to multiply and the apportionment of '
             'Congress; <span data-concept="lattice-multiplication">lattice multiplication</span> and the '
             '<span data-concept="apportionment">Huntington–Hill method</span> are Advanced. Erickson’s digit arrays count '
             'from 0 (X[0 .. m − 1], digit i worth 10<sup>i</sup>) and his Pop[1 .. n] and Rep[1 .. n] from 1, while the '
             'Python, Java, C++ and JavaScript beside the figures count from 0.'),
    'objectives': [], 'summary_html': '',
    'notes': 'Erickson’s chapter-opening epigraphs, the rest of his chapter 0 from “Running Time” on, and ODS’s overview of its own chapter are left out here.',
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'The OpenDSA items the chapter config lists for this section (ProblemAlgorithmProgramTF1–TF11 with AnalPrelimSumm, '
        'AlgAnlsMCQrelalgprb, IntroMCQeff and IntroMCQeff2, ADTMCQadt, ADTMCQinter and ADTMCQds with IntroADTSumm) wait for the '
        'converter of OpenDSA’s Khan-format exercises and are not here yet; AlgAnlsMCQalgdfn is not used, since its key contradicts '
        'Erickson’s definition. Erickson’s chapter 0 exercises 0 and 4 (the chess player, and Huntington–Hill by divisor) have no published answers and are left out. ODS chapter 1 '
        'exercises 1, 5, 6 and 7 are held for chapters 3, 5 and 8, which define the interfaces they use, and Erickson’s chapter 1 '
        'Factorial item, which uses lattice and peasant multiplication, for chapter 4. Peasant multiplication has open test cases '
        '(TheAlgorithms, trekhleb) but no open exercise statement, so it has no card. The difference-of-squares tests are '
        'Exercism’s canonical data; its references are written by the AI that built the section.'),
    'figures': [
        {'id': 'sim-lattice', 'kind': 'sim', 'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
        {'id': 'photo-treviso', 'kind': 'photo'},
        {'id': 'photo-eutocius', 'kind': 'photo'},
        {'id': 'sim-peasant', 'kind': 'sim', 'originals': ['/media/ch01/jeffe-0-3-peasant.png'], 'original_caption': '{{caption-text 0.3}}',
         'draws': ['key', 'cost'], 'ai': FIG_AI},
        {'id': 'sim-compass', 'kind': 'sim', 'originals': ['/media/ch01/jeffe-0-4-compass.png'], 'original_caption': '{{caption-text 0.4}}',
         'draws': ['cost'], 'ai': FIG_AI},
        {'id': 'sim-apportion', 'kind': 'sim', 'originals': ['/media/ch01/jeffe-0-5-apportion.png'], 'original_caption': '{{caption-text 0.5}}',
         'draws': ['key', 'cost', 'size'], 'ai': FIG_AI},
        {'id': 'sim-scan-cost', 'kind': 'sim', 'draws': ['size', 'cost'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'lat-k', 'label': 'k, the column FibonacciMultiply settles', 'figures': ['sim-lattice']},
        {'id': 'lat-i', 'label': 'i, the position in X', 'figures': ['sim-lattice']},
        {'id': 'lat-j', 'label': 'j, the position in Y', 'figures': ['sim-lattice']},
        {'id': 'lat-hold', 'label': 'hold, the running sum and carry', 'figures': ['sim-lattice']},
        {'id': 'x', 'label': 'x, the number PeasantMultiply halves', 'figures': ['sim-peasant']},
        {'id': 'y', 'label': 'y, the number PeasantMultiply doubles', 'figures': ['sim-peasant']},
        {'id': 'prod', 'label': 'prod, the product so far', 'figures': ['sim-peasant']},
        {'id': 'C', 'label': 'the point C', 'figures': ['sim-compass']},
        {'id': 'D', 'label': 'the point D', 'figures': ['sim-compass']},
        {'id': 'Z', 'label': 'the point Z, the answer', 'figures': ['sim-compass']},
        {'id': 's', 'label': 's, the state that takes the next seat', 'figures': ['sim-apportion']},
    ],
    'coverage': [
        {'span': 'algorithm', 'concept': 'algorithm', 'verb': 'introduces'},
        {'span': 'lattice', 'concept': 'lattice-multiplication', 'verb': 'introduces'},
        {'span': 'lattice', 'concept': 'algorithm', 'verb': 'uses'},
        {'span': 'peasant', 'concept': 'peasant-multiplication', 'verb': 'introduces'},
        {'span': 'peasant', 'concept': 'lattice-multiplication', 'verb': 'uses'},
        {'span': 'compass', 'concept': 'algorithm', 'verb': 'reinforces'},
        {'span': 'apportionment', 'concept': 'apportionment', 'verb': 'introduces'},
        {'span': 'apportionment', 'concept': 'algorithm', 'verb': 'reinforces'},
        {'span': 'underspecified', 'concept': 'underspecified-algorithm', 'verb': 'introduces'},
        {'span': 'underspecified', 'concept': 'algorithm', 'verb': 'uses'},
        {'span': 'describing', 'concept': 'describing-algorithms', 'verb': 'introduces'},
        {'span': 'describing', 'concept': 'lattice-multiplication', 'verb': 'uses'},
        {'span': 'describing', 'concept': 'peasant-multiplication', 'verb': 'uses'},
        {'span': 'correctness', 'concept': 'describing-algorithms', 'verb': 'reinforces'},
        {'span': 'efficiency', 'concept': 'need-for-efficiency', 'verb': 'introduces'},
        {'span': 'interfaces', 'concept': 'interface-vs-implementation', 'verb': 'introduces'},
    ],
    'footnotes_extra': [
        {'id': 'err-apportion', 'kind': 'correction',
         'html': 'Figure 0.5 as printed has two slips. Its first loop inserts each state with priority <em>Pop</em>[<em>i</em>]/√2, '
                 'which should read <em>Pop</em>[<em>s</em>]/√2, and its second loop’s comment and bound read '
                 '“the remaining <em>n</em> − <em>R</em> representatives” and “for <em>i</em> ← 1 to <em>n</em> − <em>R</em>”, '
                 'which should read <em>R</em> − <em>n</em>: there are <em>R</em> seats and <em>n</em> of them are given out first. '
                 'The code beside the figure has both corrected.'},
    ],
}
EXERCISE_FILES = {'dos': 'sources/_cache/exercism/exercises/difference-of-squares'}

DOS_PY = '''def difference_of_squares(number):
    square_of_sum = (number * (number + 1) // 2) ** 2
    sum_of_squares = number * (number + 1) * (2 * number + 1) // 6
    return square_of_sum - sum_of_squares
'''
DOS_JS = '''function differenceOfSquares(number) {
  const squareOfSum = ((number * (number + 1)) / 2) ** 2;
  const sumOfSquares = (number * (number + 1) * (2 * number + 1)) / 6;
  return squareOfSum - sumOfSquares;
}
'''


def EXERCISES(exercism, book):
    import os
    ex = exercism(os.path.join(book, EXERCISE_FILES['dos']), 'difference_of_squares', 'differenceOfSquares', 'differenceOfSquares',
                  DOS_PY, DOS_JS, {
                      'id': 'c1', 'source_id': 'exercism:difference-of-squares', 'source_number': 'difference-of-squares',
                      'origin': 'exercism', 'kind': 'code', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'efficiency',
                      'changes': 'Only the difference itself is asked for and tested; the canonical data’s cases for the square of the sum and the sum of the squares are left out.'})
    return [ex], [{'exercise': 'c1', 'concept': 'need-for-efficiency'}]
