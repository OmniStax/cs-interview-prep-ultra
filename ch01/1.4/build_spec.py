"""What tools/build_text.py needs to assemble 1.4 Analysing running time and space (the plan is plan.md beside this file).

Everything here is placement, markup or a small correction of what the extraction gets wrong; the source's
words come from the converters. Each FIXES entry says why it is there.
"""
TITLE = 'Analysing running time and space'
JEFFE_PDF = 'sources/_cache/jeffe/00-intro.pdf'
JEFFE_PAGES = range(15, 18)

BLOCKS = [
    # ODS from its pseudocode edition (METHOD decision 20): the last paragraph of "The Model of Computation" is
    # \javaonly and \cpponly text round one shared sentence, which the pseudocode edition prints cut off before
    # its end ("…not implementable"), so the block stops before it (tools/build_text.py, ODS_EDITION)
    dict(id='word-ram', source='ods', file='sources/_cache/ods/latex/intro.tex', lines=(764, 804),
         locator='ods:intro#sec:model, to “occupies one word of memory”, before the last paragraph, which the pseudocode edition prints cut short',
         h2='The Model of Computation'),
    dict(id='running-time', source='jeffe', locator='jeffe:0.6, from “Running Time” to the end of 0.6', h2='Running Time',
         drop_first_heading=True, **{'from': 'Running Time', 'to': 'Exercises'}),
    dict(id='guarantees', source='ods', file='sources/_cache/ods/latex/intro.tex', lines=(812, 920),
         locator='ods:intro#correctness-time-complexity-and-space-complexity', h2='Correctness, Time Complexity, and Space Complexity'),
]

# Display formulas: the PDF draws each in pieces (brace parts on lines of their own), so each is set here in
# LaTeX from the page render, keyed by page and order on the page.
DISPLAYS = {
    'p16#1': r'x\cdot y = \begin{cases} 0 & \text{if } x = 0\\ \lfloor x/2\rfloor\cdot(y+y) & \text{if } x \text{ is even}\\ \lfloor x/2\rfloor\cdot(y+y)+y & \text{if } x \text{ is odd} \end{cases}',
}
# Lines the classifier would read wrongly: (page, baseline, kind).
KIND_OVERRIDES = [
    (15, 105.3, 'drop'),   # the ∑ and its upper limit n of the gift-name count, drawn on a baseline of their own; FIXES sets the sum
    (15, 78.1, 'drop'),    # the two ∑ and their upper limits n and i of the gift count, the same
]

# (what the extraction gives, what the page prints, why)
FIXES = [
    ('<sub><em>i</em> = 1</sub> <em>i</em> = <em>n</em>(<em>n</em> + 1)<em>/</em>2 times',
     r'$\sum_{i=1}^{n} i = n(n+1)/2$ times', 'the sum sign and its upper limit sit on a baseline of their own (KIND_OVERRIDES); the page prints the sum inline'),
    ('~*i*~~=1~ *i* = *n*(*n* + 1)*/*2 times', r'$\sum_{i=1}^{n} i = n(n+1)/2$ times', 'the same, in source.md'),
    ('<sub><em>i</em> = 1</sub> <sub><em>j</em> = 1</sub> <em>j</em> = <em>n</em>(<em>n</em> + 1)(<em>n</em> + 2)<em>/</em>6 = <em>Θ</em>(<em>n</em><sup>3</sup>) gifts',
     r'$\sum_{i=1}^{n}\sum_{j=1}^{i} j = n(n+1)(n+2)/6 = \Theta(n^3)$ gifts', 'the same for the double sum'),
    ('~*i*~~=1~ ~*j*~~=1~ *j* = *n*(*n* + 1)(*n* + 2)*/*6 = *Θ*(*n*^3^) gifts', r'$\sum_{i=1}^{n}\sum_{j=1}^{i} j = n(n+1)(n+2)/6 = \Theta(n^3)$ gifts', 'the same, in source.md'),
    ('<em>Θ</em>', 'Θ', 'the page sets Θ upright; the math font\'s Theta reads as italic'),
    ('*Θ*', 'Θ', 'the same, in source.md'),
    ('<span style="font-variant:small-caps">BottlesOf</span>- <span style="font-variant:small-caps">Beer</span>',
     '<span style="font-variant:small-caps">BottlesOfBeer</span>', 'a name broken at a line end after a small-caps run, which the joiner does not see'),
    ('BottlesOf- Beer', 'BottlesOfBeer', 'the same, in source.md'),
    ('<span style="font-variant:small-caps">NewPriority</span>- <span style="font-variant:small-caps">Queue</span>',
     '<span style="font-variant:small-caps">NewPriorityQueue</span>', 'the same for NewPriorityQueue'),
    ('NewPriority- Queue', 'NewPriorityQueue', 'the same, in source.md'),
    ('N<span style="font-variant:small-caps">DaysOfChristmas</span>', '<span style="font-variant:small-caps">NDaysOfChristmas</span>',
     'two roman capitals start the name, and only the second joins the small-caps run'),
    ('Sing “ j gifts[j],”', 'Sing “j gifts[j],”', 'the italic correction after the opening quote reads as a space'),
    ('⌊<em>x/</em>2⌋,2<em>y</em>', '⌊<em>x</em>/2⌋, 2<em>y</em>', 'the slash is set in the math italic font but is not a variable; the argument comma spaced as in T(x, y)'),
    ('⌊*x/*2⌋,2*y*', '⌊*x*/2⌋, 2*y*', 'the same, in source.md'),
    ('<em>N</em> +<em>RI</em> +(<em>R</em> − <em>n</em>)<em>E</em>', '<em>N</em> + <em>RI</em> + (<em>R</em> − <em>n</em>)<em>E</em>', 'an operator at a style break keeps its spaces'),
    ('*N* +*RI* +(*R*− *n*)*E*', '*N* + *RI* + (*R* − *n*)*E*', 'the same, in source.md'),
    ('<em>R</em> log<em>n</em>', '<em>R</em> log <em>n</em>', 'the math font sets "log n" with a thin space the reader takes for none'),
    ('their running singing times', 'their <s>running</s> singing times', 'the page strikes "running" through; the strike is a rule too short for the extraction to keep'),
    ('*x* · *y* .', '*x* · *y*.', 'no space before a full stop after a formula'),
]

# ODS cross-references, to this book's pages (plans-summary question 23): the reference, its link and its Markdown.
ODS_REFS = {
    '\\secref{randomization}': ('<a href="/cs-interview-prep-ultra/ch01/1.6/#linearity">Section 1.6</a>', 'Section 1.6'),
}

AI = 'claude-opus-5-5 high'


def _code(s):
    import html
    return html.escape(s.strip('\n'), quote=False).replace('$', '&#36;')


# Alouette as Erickson prints it is pseudocode in French; the four languages are translations of it, its lyrics
# (his “allouette” included) and his comment ⟨⟨à rebours⟩⟩ kept as he prints them
ALOUETTE = {
    'python': '''
def alouette(lapart):
    print("Alouette, gentille alouette, alouette, je te plumerai.")
    for i in range(len(lapart)):
        print(f"Je te plumerai {lapart[i]}. Je te plumerai {lapart[i]}.")
        for j in range(i, -1, -1):  # à rebours
            print(f"Et {lapart[j]} ! Et {lapart[j]} !")
        print("Alouette! Alouette! Aaaaaa...")
        print("... alouette, gentille allouette, alouette, je te plumerai.")
''',
    'java': '''
static void alouette(String[] lapart) {
    System.out.println("Alouette, gentille alouette, alouette, je te plumerai.");
    for (int i = 0; i < lapart.length; i++) {
        System.out.println("Je te plumerai " + lapart[i] + ". Je te plumerai " + lapart[i] + ".");
        for (int j = i; j >= 0; j--) {  // à rebours
            System.out.println("Et " + lapart[j] + " ! Et " + lapart[j] + " !");
        }
        System.out.println("Alouette! Alouette! Aaaaaa...");
        System.out.println("... alouette, gentille allouette, alouette, je te plumerai.");
    }
}
''',
    'cpp': '''
void alouette(const std::vector<std::string>& lapart) {
    std::cout << "Alouette, gentille alouette, alouette, je te plumerai.\\n";
    for (int i = 0; i < (int)lapart.size(); i++) {
        std::cout << "Je te plumerai " << lapart[i] << ". Je te plumerai " << lapart[i] << ".\\n";
        for (int j = i; j >= 0; j--) {  // à rebours
            std::cout << "Et " << lapart[j] << " ! Et " << lapart[j] << " !\\n";
        }
        std::cout << "Alouette! Alouette! Aaaaaa...\\n";
        std::cout << "... alouette, gentille allouette, alouette, je te plumerai.\\n";
    }
}
''',
    'javascript': '''
function alouette(lapart) {
  console.log("Alouette, gentille alouette, alouette, je te plumerai.");
  for (let i = 0; i < lapart.length; i++) {
    console.log(`Je te plumerai ${lapart[i]}. Je te plumerai ${lapart[i]}.`);
    for (let j = i; j >= 0; j--) {  // à rebours
      console.log(`Et ${lapart[j]} ! Et ${lapart[j]} !`);
    }
    console.log("Alouette! Alouette! Aaaaaa...");
    console.log("... alouette, gentille allouette, alouette, je te plumerai.");
  }
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


I_ = '<span data-ref="i"><em>i</em></span>'
J_ = '<span data-ref="j"><em>j</em></span>'
HTML = {
    'sim-song-count': sim(
        'sim-song-count',
        f'The Twelve Days of Christmas, day by day: on day {I_} the singer names the gifts from day {I_} down to the '
        f'partridge, so row {I_} of the triangle holds {I_} gift names, and the name of gift {J_} brings {J_} gifts. '
        'The rows pile up to <span data-type="cost"><em>n</em>(<em>n</em> + 1)/2</span> gift names and '
        '<span data-type="cost"><em>n</em>(<em>n</em> + 1)(<em>n</em> + 2)/6</span> gifts. On log–log axes the gifts climb '
        'fastest, as <span data-type="cost">Θ(<em>n</em><sup>3</sup>)</span>, the gift names as <span data-type="cost">Θ(<em>n</em><sup>2</sup>)</span>, '
        'and the <span data-type="cost">3<em>n</em> + 3</span> times Bottles of Beer mentions beer only as <span data-type="cost">Θ(<em>n</em>)</span>.'),
    'alouette-code': code_set(ALOUETTE),
}

AFTER_PRE = {
    'NDaysOfChristmas(gifts[2 .. n]):': ['sim-song-count'],
    'Alouette(lapart[1 .. n]):': ['alouette-code'],
}

FN = lambda nid: f'<sup class="fn" data-note="{nid}"></sup>'  # noqa: E731
CS = lambda s: f'<span data-type="cost">{s}</span>'  # noqa: E731
# (block, text as built, replacement, [count]): the errata's markers, the links the plan agreed for references
# that point off the page, the spans that introduce each concept and mention others, and the costs and sizes.
MARKS = [
    # errata 7, 8, 9 (correction notes)
    ('running-time', 'twice much time', 'twice much time' + FN('err-twice')),
    ('running-time', 'underlying data structure of subroutine.', 'underlying data structure of subroutine.' + FN('err-or')),
    ('running-time', '+ 2 with base case', '+ 2' + FN('err-peasant') + ' with base case'),
    ('running-time', 'runs in <strong><em>O</em>(<em>Rn</em>) <em>time</em></strong>.',
     'runs in ' + CS('<strong><em>O</em>(<em>Rn</em>) <em>time</em></strong>') + '.' + FN('err-census')),
    # references off the page, as links (plans-summary question 23)
    ('running-time', 'in the next chapter imply', 'in <a href="/cs-interview-prep-ultra/ch10/10.2/">the next chapter</a> imply'),
    ('running-time', 'a binary heap or a heap-ordered array', '<a href="/cs-interview-prep-ultra/ch09/9.2/">a binary heap or a heap-ordered array</a>'),
    # concepts introduced
    ('word-ram', '<em>$w$-bit word-RAM</em>', '<span data-concept="word-ram"><em>$w$-bit word-RAM</em></span>'),
    ('running-time', 'We can measure time by counting how many times the algorithm executes a certain instruction or reaches a certain milestone',
     '<span data-concept="complexity-analysis">We can measure time by counting how many times the algorithm executes a certain instruction or reaches a certain milestone</span>'),
    ('guarantees', 'three different kinds of running time guarantees', '<span data-concept="running-time-guarantees">three different kinds of running time guarantees</span>'),
    # concepts of 1.1 the passage comes back to
    ('running-time', 'the peasant multiplication algorithm', 'the <span data-concept="peasant-multiplication">peasant multiplication</span> algorithm'),
    ('running-time', 'the Huntington-Hill apportionment algorithm', 'the <span data-concept="apportionment">Huntington-Hill apportionment</span> algorithm'),
    ('running-time', 'lattice multiplication of two', '<span data-concept="lattice-multiplication">lattice multiplication</span> of two'),
    ('guarantees', 'correctly implement its interface', 'correctly implement its <span data-concept="interface-vs-implementation">interface</span>'),
    # running times and other costs (COLOR.md: T(n), O, Θ and the counts are cost)
    ('running-time', 'the asymptotic singing time Θ(<em>n</em>)', 'the asymptotic singing time ' + CS('Θ(<em>n</em>)')),
    ('running-time', 'exactly 3<em>n</em> + 3 times', 'exactly ' + CS('3<em>n</em> + 3') + ' times'),
    ('running-time', 'the singing time is Θ(<em>n</em><sup>2</sup>)', 'the singing time is ' + CS('Θ(<em>n</em><sup>2</sup>)')),
    ('running-time', r'$\sum_{i=1}^{n} i = n(n+1)/2$', CS(r'$\sum_{i=1}^{n} i = n(n+1)/2$')),
    ('running-time', r'$\sum_{i=1}^{n}\sum_{j=1}^{i} j = n(n+1)(n+2)/6 = \Theta(n^3)$', CS(r'$\sum_{i=1}^{n}\sum_{j=1}^{i} j = n(n+1)(n+2)/6 = \Theta(n^3)$')),
    ('running-time', 'takes Θ(2<sup><em>n</em></sup>) time', 'takes ' + CS('Θ(2<sup><em>n</em></sup>) time')),
    ('running-time', '<em>T</em>(<em>x</em>, <em>y</em>) ≤ <em>T</em>(⌊<em>x</em>/2⌋, 2<em>y</em>) + 2', CS('<em>T</em>(<em>x</em>, <em>y</em>) ≤ <em>T</em>(⌊<em>x</em>/2⌋, 2<em>y</em>) + 2')),
    ('running-time', '<em>N</em> = <em>I</em> = Θ(1) and <em>E</em> = Θ(<em>n</em>)', CS('<em>N</em> = <em>I</em> = Θ(1)') + ' and ' + CS('<em>E</em> = Θ(<em>n</em>)')),
    ('running-time', '<em>N</em> = Θ(1) and <em>I</em> = <em>E</em> = <em>O</em>(log <em>n</em>)', CS('<em>N</em> = Θ(1)') + ' and ' + CS('<em>I</em> = <em>E</em> = <em>O</em>(log <em>n</em>)')),
    ('running-time', 'the upper bound <em>T</em>(<em>x</em>, <em>y</em>) = <em>O</em>(log <em>x</em>)', 'the upper bound ' + CS('<em>T</em>(<em>x</em>, <em>y</em>) = <em>O</em>(log <em>x</em>)')),
    ('running-time', '<em>O</em>(<em>N</em> + <em>RI</em> + (<em>R</em> − <em>n</em>)<em>E</em>) time', CS('<em>O</em>(<em>N</em> + <em>RI</em> + (<em>R</em> − <em>n</em>)<em>E</em>) time')),
    ('running-time', '<em>O</em>(<em>N</em> + <em>R</em>(<em>I</em> + <em>E</em>))', CS('<em>O</em>(<em>N</em> + <em>R</em>(<em>I</em> + <em>E</em>))')),
    ('running-time', '<strong><em>O</em>(<em>R</em> log <em>n</em>)</strong> time', CS('<strong><em>O</em>(<em>R</em> log <em>n</em>)</strong> time')),
    ('running-time', 'requires <em>O</em>(<em>n</em><sup>2</sup>) space', 'requires ' + CS('<em>O</em>(<em>n</em><sup>2</sup>) space')),
    ('running-time', '<em>O</em>(<em>n</em>) space', CS('<em>O</em>(<em>n</em>) space')),
    ('word-ram', 'takes $O(k)$ time', 'takes ' + CS('$O(k)$ time')),
    ('word-ram', 'The word-size $w$', 'The <span data-type="size">word-size $w$</span>'),
]

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]
SECTION = {
    'id': '1.4', 'chapter': '1', 'title': 'Analysing running time and space', 'short': 'Running time',
    'lead': ('An Essential section on the <span data-concept="word-ram">model of computation</span>, on '
             '<span data-concept="complexity-analysis">measuring running time and space by counting</span>, and on the '
             '<span data-concept="running-time-guarantees">three kinds of running-time guarantee</span>. Erickson’s Running Time '
             'passage returns to BottlesOfBeer, peasant multiplication, ApportionCongress and lattice multiplication from 1.1; '
             'his pseudocode counts from 1 (for <em>i</em> ← 1 to <em>n</em>, <em>gifts</em>[2 .. <em>n</em>]), while the Python, '
             'Java, C++ and JavaScript translations count from 0.'),
    'objectives': [], 'summary_html': '',
    'notes': ('Erickson’s chapter 0 exercises, with his Figure 0.6, and the last paragraph of ODS’s model of computation, '
              'which its pseudocode edition prints cut short, are left out here.'),
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'The OpenDSA items the chapter config lists for this section (AnlsIntroMCQszip with FasterCorASumm, tagged with '
        'need-for-efficiency too; MthBgMCQrmacc and MthBgMCQdskacc; AnalProgramMCQtheta1–9 with AnalProgramSumm; AnalProblemTF1, '
        'TF2 and TF4–TF7 with AnalProblemSumm; AlgAnlsMCQsqlsrch, AlgAnlsTFsqlsrch1 and AlgAnlsTFsqlsrch2; MisunderstandingsTF1–6 '
        'with MisSumm, tagged with big-o and big-omega-theta too) wait for the converter of OpenDSA’s Khan-format exercises and '
        'are not here yet. Erickson’s chapter 0 exercises 1, 2 and 3 (songs of other running times, singing time counted in '
        'syllables, and The Barley Mow with his Figure 0.6) and Applied Combinatorics’ basics exercises have no published '
        'answers and are left out. OpenDSA AnalProblemTF10–12, which assume sorting, are held for chapter 10, MIT 6.006 S20 '
        'ps0 0-6 for 2.3 and MIT 6.006 F11 ps1 1-3 to 1-6 for chapter 6.'),
    'figures': [
        {'id': 'sim-song-count', 'kind': 'sim', 'draws': ['cost', 'size'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'i', 'label': 'i, the day NDaysOfChristmas sings (the verse of BottlesOfBeer)', 'figures': ['sim-song-count']},
        {'id': 'j', 'label': 'j, the gift NDaysOfChristmas names', 'figures': ['sim-song-count']},
    ],
    'coverage': [
        {'span': 'word-ram', 'concept': 'word-ram', 'verb': 'introduces'},
        {'span': 'running-time', 'concept': 'complexity-analysis', 'verb': 'introduces'},
        {'span': 'running-time', 'concept': 'peasant-multiplication', 'verb': 'reinforces'},
        {'span': 'running-time', 'concept': 'apportionment', 'verb': 'reinforces'},
        {'span': 'running-time', 'concept': 'lattice-multiplication', 'verb': 'reinforces'},
        {'span': 'guarantees', 'concept': 'running-time-guarantees', 'verb': 'introduces'},
        {'span': 'guarantees', 'concept': 'interface-vs-implementation', 'verb': 'uses'},
    ],
    'footnotes_extra': [
        {'id': 'err-twice', 'kind': 'correction',
         'html': '“requires about twice much time” should read “requires about twice <em>as</em> much time”.'},
        {'id': 'err-peasant', 'kind': 'correction',
         'html': 'The inequality undercounts the work of one step. A step of the recursion makes a parity test, a mediation '
                 '⌊<em>x</em>/2⌋, a duplation <em>y</em> + <em>y</em> and, when <em>x</em> is odd, one more addition + <em>y</em>: '
                 'up to four of the operations <em>T</em> counts, so it should read '
                 '<em>T</em>(<em>x</em>, <em>y</em>) ≤ <em>T</em>(⌊<em>x</em>/2⌋, 2<em>y</em>) + 4. The bound '
                 '<em>T</em>(<em>x</em>, <em>y</em>) = <em>O</em>(log <em>x</em>) is unchanged.'},
        {'id': 'err-census', 'kind': 'correction',
         'html': 'Here the Census Bureau’s priority queue is an <em>unsorted</em> array; in Erickson’s '
                 '<a href="/cs-interview-prep-ultra/ch01/1.1/#apportionment">Congressional Apportionment</a> (Section 1.1) '
                 'the Bureau uses a <em>sorted</em> array, stored in a single column of an Excel spreadsheet and recalculated '
                 'from scratch at every iteration. With the unsorted array, ExtractMax scans all <em>n</em> states and the '
                 '<em>O</em>(<em>Rn</em>) bound follows as stated; recalculating the sorted column for every seat takes '
                 'Ω(<em>n</em>) time a seat as well, so either way the Bureau’s implementation takes Ω(<em>Rn</em>) time.'},
        {'id': 'err-or', 'kind': 'correction',
         'html': '“some underlying data structure of subroutine” should read “some underlying data structure '
                 '<em>or</em> subroutine”.'},
    ],
}
