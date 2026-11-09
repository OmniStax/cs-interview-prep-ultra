"""What tools/build_text.py needs to assemble 2.6 Doubly linked lists (the plan is plan.md beside this file).

Everything here is placement, markup and the code sets' assembly; the source's words come from ODS's LaTeX through
tools/build_text.py (pseudocode edition, METHOD decision 20), and the code from ODS's Java, C++ and Python sources
through tools/ods_listing.py, which applies ODS's own extractors' rules. The one port of ODS's Python and the
JavaScript translations are AI-written and marked (decision 20); each says why below. FIXES is empty.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'tools'))
import ods_listing  # noqa: E402

TITLE = 'Doubly linked lists'
LINKED = 'sources/_cache/ods/latex/linkedlists.tex'

BLOCKS = [
    # linkedlists.tex 107 is "\section{#DLList#: A Doubly-Linked List}"; 146 is the DLList() listing, 148 begins "Finding
    # the node with a particular index", 238 ends the section (239 blank, 240 "\section{#SEList#…")
    dict(id='dummy-node', source='ods', file=LINKED, lines=(109, 146),
         locator='ods:linkedlists#sec:dllist, opening through fig. dllist and the DLList() code',
         h2='DLList: A Doubly-Linked List'),
    dict(id='dllist', source='ods', file=LINKED, lines=(148, 238),
         locator='ods:linkedlists#sec:dllist, from getNode(i) through “Adding and Removing” and “Summary”',
         h2='Operations on a DLList'),
]

# ODS's figure numbers stay as printed and link to the Sims that stand for them; its chapter reference to its
# array-based Lists is this book's Section 2.2 (book RULES, Cross-references).
ODS_REFS = {
    '\\figref{dllist}': ('<a href="#sim-dllist-ring">Figure 3.2</a>', 'Figure 3.2'),
    '\\figref{dllist-addbefore}': ('<a href="#sim-dllist">Figure 3.3</a>', 'Figure 3.3'),
    '\\chapref{arrays}': ('<a href="/cs-interview-prep-ultra/ch02/2.2/">Section 2.2</a>', 'Section 2.2'),
}

AI = 'claude-opus-5-5 high'

# ---------------------------------------------------------------- the code sets (decision 20)
# The listing ODS prints at each \codeimport, by the name it gives: Java and C++ are ODS's, read by
# tools/ods_listing.py; Python is ODS's python/ods/dllist.py, read the same way.
LISTINGS = ['DLList.n.dummy.DLList()', 'DLList.getNode(i)', 'DLList.get(i).set(i,x)', 'DLList.addBefore(w,x)',
            'DLList.add(i,x)', 'DLList.remove(w)', 'DLList.remove(i)']

# The port of ODS's Python (listing, old, new, why). ODS's Python is Python 2: n/2 there is integer division, as in
# its Java and C++ (n / 2 on ints); on Python 3 it is a float, and get_node(i) for i = (n − 1)/2 with n odd would walk
# forward where every other edition walks back. // keeps the listing's meaning.
PORTS = [
    ('DLList.getNode(i)', 'self.n/2', 'self.n//2', 'Python 2 integer division, as the Java and C++ divide'),
]

# JavaScript translations of ODS's Java, line for line (decision 20): the same names, `this.` for a field, `let`
# and `const` for locals; Java's overloaded remove(Node w) is _remove(w), the name ODS's Python gives it, since
# JavaScript cannot overload remove.
JS = {
    'DLList.n.dummy.DLList()': '''
n;
dummy;

constructor() {
  this.dummy = new Node();
  this.dummy.next = this.dummy;
  this.dummy.prev = this.dummy;
  this.n = 0;
}
''',
    'DLList.getNode(i)': '''
getNode(i) {
  let p = null;
  if (i < Math.floor(this.n / 2)) {
    p = this.dummy.next;
    for (let j = 0; j < i; j++)
      p = p.next;
  } else {
    p = this.dummy;
    for (let j = this.n; j > i; j--)
      p = p.prev;
  }
  return p;
}
''',
    'DLList.get(i).set(i,x)': '''
get(i) {
  return this.getNode(i).x;
}

set(i, x) {
  const u = this.getNode(i);
  const y = u.x;
  u.x = x;
  return y;
}
''',
    'DLList.addBefore(w,x)': '''
addBefore(w, x) {
  const u = new Node();
  u.x = x;
  u.prev = w.prev;
  u.next = w;
  u.next.prev = u;
  u.prev.next = u;
  this.n++;
  return u;
}
''',
    'DLList.add(i,x)': '''
add(i, x) {
  this.addBefore(this.getNode(i), x);
}
''',
    'DLList.remove(w)': '''
_remove(w) {
  w.prev.next = w.next;
  w.next.prev = w.prev;
  this.n--;
}
''',
    'DLList.remove(i)': '''
remove(i) {
  const w = this.getNode(i);
  this._remove(w);
  return w.x;
}
''',
}


def listing(name):
    """The four variants of one listing, with the languages that are AI-written named in _ai."""
    cls, members = name.split('.', 1)
    v = {'python': ods_listing.python(cls, members), 'java': ods_listing.java(cls, members),
         'cpp': ods_listing.cpp(cls, members), 'javascript': JS[name].strip('\n')}
    ai = ['javascript']
    for lst, old, new, _why in PORTS:
        if lst == name:
            assert old in v['python'], (name, old)
            v['python'] = v['python'].replace(old, new)
            ai.append('python')
    v['_ai'] = tuple(ai)
    return v


# addBefore's listing is sim-dllist's code panel, where ODS prints it and its Figure 3.3 (plans-summary question 17)
CODEIMPORT = {'DLList.addBefore(w,x)': 'sim-dllist'}
CODE_SETS = {n: listing(n) for n in LISTINGS if n not in CODEIMPORT}


# ---------------------------------------------------------------- figures
def sim(fid, caption, original=None, original_caption=None):
    attrs = f'class="sim" id="{fid}"'
    if original:
        attrs += f' data-original="{original}" data-original-caption="{original_caption}"'
    return f'<figure {attrs}>\n  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>'


R = lambda rid, s: f'<span data-ref="{rid}">{s}</span>'  # noqa: E731
DUMMY, P, W, U, I = R('dummy', 'dummy'), R('p', '<em>p</em>'), R('w', '<em>w</em>'), R('u', '<em>u</em>'), R('i', '<em>i</em>')
N = '<span data-type="size"><em>n</em></span>'
HTML = {
    'sim-dllist-ring': sim(
        'sim-dllist-ring',
        f'Five elements, a to e, and the {DUMMY} node in one cycle. Following next from the {DUMMY} passes a, b, c, d '
        f'and e and comes back to it; following prev passes them in the opposite order. With {N} = 0 the '
        f'{DUMMY} node’s next and prev are the {DUMMY} itself, so even the empty list has no missing reference.',
        '/media/ch02/ods-dllist.png', '{{caption-text dllist}}'),
    'sim-dllist': sim(
        'sim-dllist',
        f'add({I}, x) and remove({I}) on a DLList. getNode starts {P} at whichever end is nearer, so {P} follows '
        f'at most <span data-type="cost">1 + min({I}, {N} − {I})</span> references. Then addBefore points the new node '
        f'{U} at its two neighbours and re-aims their two references at {U}, or remove re-aims the two references '
        f'around {W} so they skip it. At the front, at the back and in an empty list the neighbour is the '
        f'{DUMMY}, and the same lines run.',
        '/media/ch02/ods-dllist-addbefore.png', '{{caption-text dllist-addbefore}}'),
}

AFTER_TEXT = {
    'dummy-node': [('as illustrated in', 'sim-dllist-ring')],
}

# (block, text as built, replacement, [count]): concept spans and the referents the figures draw
REF = lambda rid, s: f'\\htmlData{{ref={rid}}}{{{s}}}'  # noqa: E731
MARKS = [
    # concepts: the span that introduces each, and the other places a sentence names one
    ('dummy-node', 'A DLList (doubly-linked list)', 'A <span data-concept="doubly-linked-list">DLList (doubly-linked list)</span>'),
    ('dummy-node', 'introduce a $dummy$ node', f'introduce a <span data-concept="sentinel-node">${REF("dummy", "dummy")}$ node</span>'),
    ('dllist', 'index in a DLList is easy', 'index in a <span data-concept="doubly-linked-list">DLList</span> is easy'),
    ('dllist', 'Thanks to the dummy node', 'Thanks to the <span data-concept="sentinel-node">dummy node</span>'),
    ('dllist', 'the use of the dummy node', 'the use of the <span data-concept="sentinel-node">dummy node</span>'),
    # the dummy, which both Sims draw
    ('dummy-node', 'with $dummy$ acting', f'with ${REF("dummy", "dummy")}$ acting'),
    ('dllist', '$dummy.next$', f'${REF("dummy", "dummy")}.next$'),
    ('dllist', '$dummy.prev$', f'${REF("dummy", "dummy")}.prev$'),
    # i, the index asked for, and the nodes w and u of addBefore and remove, which sim-dllist draws
    ('dllist', '$i$th', f'${REF("i", "i")}$th', 8),
    ('dllist', '$O(1+\\min\\{i,n-i\\})$', f'$O(1+\\min\\{{{REF("i", "i")},n-{REF("i", "i")}\\}})$', 3),
    ('dllist', '$O(1+\\min\\{i, n-i\\})$', f'$O(1+\\min\\{{{REF("i", "i")}, n-{REF("i", "i")}\\}})$', 2),
    ('dllist', 'a node $w$ in', f'a node ${REF("w", "w")}$ in'),
    ('dllist', 'a node $u$ before $w$', f'a node ${REF("u", "u")}$ before ${REF("w", "w")}$'),
    ('dllist', '$u.next=w$', f'${REF("u", "u")}.next={REF("w", "w")}$'),
    ('dllist', '$u.prev=w.prev$', f'${REF("u", "u")}.prev={REF("w", "w")}.prev$'),
    ('dllist', '$u.prev.next$', f'${REF("u", "u")}.prev.next$'),
    ('dllist', '$u.next.prev$', f'${REF("u", "u")}.next.prev$'),
    ('dllist', '$w.prev$', f'${REF("w", "w")}.prev$', 2),
    ('dllist', '$w.next$', f'${REF("w", "w")}.next$', 2),
    ('dllist', 'new node $u$ that', f'new node ${REF("u", "u")}$ that'),
    ('dllist', 'Removing a node $w$', f'Removing a node ${REF("w", "w")}$'),
    ('dllist', 'skip over $w$', f'skip over ${REF("w", "w")}$'),
    ('dllist', 'with index $i$', f'with index ${REF("i", "i")}$'),
]

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]

SECTION = {
    'id': '2.6', 'chapter': '2', 'title': 'Doubly linked lists', 'short': 'Doubly linked lists',
    'lead': ('An Essential section on the <span data-concept="doubly-linked-list">doubly linked list</span> and the '
             '<span data-concept="sentinel-node">dummy node</span> that spares it special cases at either end. ODS calls '
             'the singly linked list of <a href="/cs-interview-prep-ultra/ch02/2.5/">Section 2.5</a> an SLList, with fields '
             '<em>head</em>, <em>tail</em> and <em>n</em>. Its DLList numbers the list’s elements from 0 to '
             '<em>n</em> − 1, and getNode(<em>i</em>) finds the one numbered <em>i</em>.'),
    'objectives': [], 'summary_html': '',
    'notes': ('The examples that close ODS’s Java and C++ editions of this section, a Java LinkedHashSet and a C++ USet, '
              'are not included here.'),
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'OpenDSA’s true-or-false item on doubly linked list implementations (ListTFdblimpl) waits for the converter of '
        'OpenDSA’s exercises. ODS’s Exercise 3.1, on why a dummy node cannot remove every special case of an SLList, has '
        'no published answer and is left out, as are its Exercises 3.5 to 3.12, which have no tests. Exercism’s '
        'linked-list tests a deque and goes with Section 3.3. MIT 6.006’s Problem 1-4 (Spring 2020) is an NC card, kept in '
        'exercises-nc.json apart from the book’s CC BY-SA content and keyed by a link to MIT’s worked solution; its '
        'template’s tests check a class, which the code answer type cannot run yet.'),
    'figures': [
        {'id': 'sim-dllist-ring', 'kind': 'sim', 'originals': ['/media/ch02/ods-dllist.png'],
         'original_caption': '{{caption-text dllist}}', 'draws': ['index', 'key', 'size'], 'ai': FIG_AI},
        {'id': 'sim-dllist', 'kind': 'sim', 'originals': ['/media/ch02/ods-dllist-addbefore.png'],
         'original_caption': '{{caption-text dllist-addbefore}}', 'draws': ['index', 'key', 'size', 'cost'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'dummy', 'label': 'dummy, the DLList’s dummy node', 'figures': ['sim-dllist-ring', 'sim-dllist']},
        {'id': 'p', 'label': 'p, the node getNode walks to', 'figures': ['sim-dllist']},
        {'id': 'w', 'label': 'w, the node to add before or to remove', 'figures': ['sim-dllist']},
        {'id': 'u', 'label': 'u, the new node', 'figures': ['sim-dllist']},
        {'id': 'i', 'label': 'i, the index of the node asked for', 'figures': ['sim-dllist']},
    ],
    'coverage': [
        {'span': 'dummy-node', 'concept': 'sentinel-node', 'verb': 'introduces'},
        {'span': 'dummy-node', 'concept': 'doubly-linked-list', 'verb': 'uses'},
        {'span': 'dllist', 'concept': 'doubly-linked-list', 'verb': 'introduces'},
        {'span': 'dllist', 'concept': 'sentinel-node', 'verb': 'uses'},
        {'span': 'dllist', 'concept': 'big-o', 'verb': 'uses'},
    ],
    'footnotes_extra': [],
}
