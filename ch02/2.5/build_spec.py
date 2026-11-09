"""What tools/build_wikitext.py and tools/build_section.py need to assemble 2.5 Singly linked lists (the plan is
plan.md beside this file).

Every block is Wikipedia's, read from the cached wikitext at its pinned revision (sources/_cache/wikipedia/
_meta.json): Linked list at 1382386163, Pointer (computer programming) at 1382564071. Nothing here is the
source's text: the blocks and where each starts and stops, what stands in place of each image frame and each
C listing, the AI translations of the C listings (Python, Java and JavaScript; the C is the C++ variant,
verbatim), the spans, the section record and the exercise. The replacement table is empty: nothing needed
correcting in place (erratum 18 is a note).
"""
import json
import os

TITLE = 'Singly linked lists'
AI = 'claude-opus-5-5 high'
LL = 'sources/_cache/wikipedia/Linked_list.wiki'
PTR = 'sources/_cache/wikipedia/Pointer_computer_programming.wiki'

BLOCKS = [
    dict(id='singly-linked-list', source='wikipedia', file=LL, h2='Linked lists',
         locator='wikipedia:Linked_list lead + #Basic concepts and nomenclature + ===Singly linked list===',
         parts=[{'from': None, 'to': '==History=='}, {'from': '==Basic concepts and nomenclature==', 'to': '===Doubly linked list==='}],
         headings={'Basic concepts and nomenclature': 3, 'Singly linked list': 3}),
    dict(id='pointer-to-pointer', source='wikipedia', file=PTR, h2='Multiple indirection',
         locator='wikipedia:Pointer_(computer_programming)#Multiple indirection, to “…the address of the new item.”, before the argv paragraph',
         parts=[{'from': '====Multiple indirection====', 'to': '====Function pointer====', 'stop_at': 'A basic example is in the [[argv]]'}],
         headings={'Multiple indirection': None}),
    dict(id='list-operations', source='wikipedia', file=LL, h2='Linked list operations',
         locator='wikipedia:Linked_list#Linked list operations (its opening) + ====Singly linked lists====',
         parts=[{'from': '==Linked list operations==', 'to': '===Circularly linked list==='}],
         headings={'Linked list operations': None, 'Linearly linked lists': None, 'Singly linked lists': 3}),
    dict(id='lists-vs-arrays', source='wikipedia', file=LL, h2='Linked lists vs. dynamic arrays',
         locator='wikipedia:Linked_list#Linked lists vs. dynamic arrays, without its comparison table (a template)',
         parts=[{'from': '===Linked lists vs. dynamic arrays===', 'to': '===Singly linked linear lists vs. other lists==='}],
         headings={'Linked lists vs. dynamic arrays': None}),
]

# wikilinks whose subject this book carries (plan, Questions 4); every other wikilink is its text
SEC = '/cs-interview-prep-ultra'
WIKILINKS = {
    'Array data structure': f'{SEC}/ch02/2.1/',
    'List (abstract data type)': f'{SEC}/ch02/2.1/',
    'Dynamic array': f'{SEC}/ch02/2.2/',
    'Amortized analysis': f'{SEC}/ch01/1.5/',
    'Stack (abstract data type)': f'{SEC}/ch03/3.1/',
    'Queue (abstract data type)': f'{SEC}/ch03/3.2/',
}

# each occurrence of a file's frame, in order: what stands there (None: left out)
IMAGES = {
    'Singly-linked-list.svg': ['photo-singly-linked-list', None],      # the lead's frame kept; the same image again dropped
    'CPT-LinkedLists-addingnode.svg': ['sim-list-ops'],               # the Sim stands where the insert diagram stood
    'CPT-LinkedLists-deletingnode.svg': [None],                       # folded into sim-list-ops (its second original)
}

# ---------------------------------------------------------------- the C listings
# addNodeToTail: the C is the C++ variant as printed; the other three are AI translations, comments kept
ADD_TAIL = {
    'python': '''# Each node in a linked list is an object. The head node is the first node in the list.

class Node:
    def __init__(self):
        self.value = 0
        self.next = None

def addNodeToTail(head, value):
    # declare a Node reference and initialize it to refer to the new Node being added to the end of the list.
    temp = Node()
    temp.value = value  # Add data to the value field of the new Node.
    temp.next = None  # initialize invalid links to None.

    if not head:
        head = temp  # If the linked list is empty (i.e., head is None), then have head refer to the new Node.
    else:
        p = head  # Assign the head node reference to the Node reference 'p'.
        while p.next:
            p = p.next  # Traverse the list until p is the last Node. The last Node always points to None.
        p.next = temp  # Make the previously last Node point to the new Node.

    return head  # Return the head node reference.
''',
    'java': '''// Each node in a linked list is an object. The head node is the first node in the list.

class Node {
    int value;
    Node next;
}

static Node addNodeToTail(Node head, int value) {
    // declare a Node reference and initialize it to refer to the new Node being added to the end of the list.
    Node temp = new Node();
    temp.value = value; // Add data to the value field of the new Node.
    temp.next = null; // initialize invalid links to null.

    if (head == null) {
        head = temp;     // If the linked list is empty (i.e., head is null), then have head refer to the new Node.
    } else {
        Node p = head;   // Assign the head node reference to the Node reference 'p'.
        while (p.next != null) {
            p = p.next;    // Traverse the list until p is the last Node. The last Node always points to null.
        }
        p.next = temp; // Make the previously last Node point to the new Node.
    }

    return head;    // Return the head node reference.
}
''',
    'javascript': '''// Each node in a linked list is an object. The head node is the first node in the list.

class Node {
    constructor() {
        this.value = 0;
        this.next = null;
    }
}

function addNodeToTail(head, value) {
    // declare a Node reference and initialize it to refer to the new Node being added to the end of the list.
    const temp = new Node();
    temp.value = value; // Add data to the value field of the new Node.
    temp.next = null; // initialize invalid links to null.

    if (!head) {
        head = temp;     // If the linked list is empty (i.e., head is null), then have head refer to the new Node.
    } else {
        let p = head;   // Assign the head node reference to the Node reference 'p'.
        while (p.next) {
            p = p.next;    // Traverse the list until p is the last Node. The last Node always points to null.
        }
        p.next = temp; // Make the previously last Node point to the new Node.
    }

    return head;    // Return the head node reference.
}
''',
}
# the struct and the head pointer of Multiple indirection
STRUCT = {
    'python': '''class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

head = None
''',
    'java': '''class LinkedList {
    int value;
    LinkedList next;
}

LinkedList head = null;
''',
    'javascript': '''class LinkedList {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

let head = null;
''',
}
CODE = [
    ('Node* addNodeToTail(Node* head, int value)', ADD_TAIL),
    ('LinkedList *head = NULL;', STRUCT),
    ('void insert(LinkedList **head, LinkedList *item)', 'sim-sorted-insert'),
]


# ---------------------------------------------------------------- figures
def sim(fid, caption, original=None, original_caption=None):
    attrs = f' data-original="{original}" data-original-caption="{original_caption}"' if original else ''
    return (f'<figure class="sim" id="{fid}"{attrs}>\n  <div class="sim-head"><span class="eyebrow">Sim</span>'
            f'<span>{caption}</span></div>\n</figure>')


def R(ref, word):
    return f'<span data-ref="{ref}">{word}</span>'


CAP_LIST_OPS = (
    f'Each operation changes the list by re-aiming one or two links. To insert, {R("new-node", "newNode")} first takes '
    f'{R("node", "node")}’s next link and only then does {R("node", "node")} point at it; done the other way round, the rest '
    f'of the list would be lost. To remove, {R("obsolete-node", "obsoleteNode")} is held while the link before it skips '
    f'over it, and once nothing reaches it, it is destroyed. '
    f'Each operation writes at most two links, whatever the length of the list, but appending without a reference to the '
    f'tail first follows every link to the last node.')
CAP_SORTED = (
    f'{R("p", "p")} never points at a node: it points at a link, first the caller’s {R("head", "head")}, then one '
    f'node’s next field after another, stopping at the first link whose node is not smaller than {R("item", "item")}. '
    f'The two assignments after the loop are the same whether that link is {R("head", "head")} or a next field in the middle, '
    f'so an insert at the front needs no case of its own. A value equal to one in the list goes in before it.')
HTML = {
    'photo-singly-linked-list': (
        '<figure class="photo" id="photo-singly-linked-list">\n'
        '  <img src="/media/ch02/wp-singly-linked-list.png" alt="">\n'
        '  <figcaption><span>{{caption Singly-linked-list.svg}} Image: Lasindi, Wikimedia Commons, public domain.</span></figcaption>\n'
        '</figure>'),
    'sim-list-ops': sim('sim-list-ops', CAP_LIST_OPS, '/media/ch02/wp-cpt-addingnode.png,/media/ch02/wp-cpt-deletingnode.png',
                        '{{caption-text CPT-LinkedLists-addingnode.svg}}. {{caption-text CPT-LinkedLists-deletingnode.svg}}.'),
    'sim-sorted-insert': sim('sim-sorted-insert', CAP_SORTED),
}

# ---------------------------------------------------------------- spans
FN_COMMENT = '<sup class="fn" data-note="err-sorted-comment"></sup>'
MARKS = [
    # the concepts where each passage names them first
    ('singly-linked-list', '<strong>linked list</strong>', '<span data-concept="singly-linked-list"><strong>linked list</strong></span>'),
    ('singly-linked-list', 'Singly linked lists contain nodes', '<span data-concept="singly-linked-list">Singly linked lists</span> contain nodes'),
    ('pointer-to-pointer', 'using double indirection', 'using <span data-concept="pointer-to-pointer">double indirection</span>'),
    ('lists-vs-arrays', 'Linked lists have several advantages over dynamic arrays',
     '<span data-concept="linked-list-vs-array">Linked lists have several advantages over dynamic arrays</span>'),
    # erratum 18: the comment of the listing (now the code panel of sim-sorted-insert) is loose
    ('pointer-to-pointer', 'insertions at the front of the list:', 'insertions at the front of the list:' + FN_COMMENT),
    # the cost bounds the prose prints in plain text (as 1.1 and 1.4 mark Erickson's)
    ('list-operations', 'running time of O(n).', 'running time of <span data-type="cost">O(n)</span>.'),
    ('lists-vs-arrays', 'it is O(n))', 'it is <span data-type="cost">O(n)</span>)'),
    ('lists-vs-arrays', '</a> O(1).', '</a> <span data-type="cost">O(1)</span>.'),
    ('lists-vs-arrays', 'taking O(log n) time instead of O(n)',
     'taking <span data-type="cost">O(log n)</span> time instead of <span data-type="cost">O(n)</span>'),
    # referents: the caller's head and the item, as the passage names them
    ('pointer-to-pointer', '<code>head</code>', '<span data-ref="head"><code>head</code></span>', 3),
    ('pointer-to-pointer', '<code>item</code>', '<span data-ref="item"><code>item</code></span>'),
]
FIXES = []

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]
LEAD = ('An Essential section on the <span data-concept="singly-linked-list">singly linked list</span>: its nodes and links, '
        'the in-place operations at a node and at the front of the list, and where it beats or loses to a dynamic array. '
        '<span data-concept="pointer-to-pointer">Multiple indirection</span> is shown in C, in the pointer notation of '
        f'<a href="{SEC}/ch02/2.1/">Section 2.1</a>. No node has an index here: a node is reached by following links from the first.')

EXERCISE_NOTES = (
    'The interactive coding challenge is Donne Martin’s, with his tests; it is run through a small driver that the starter '
    'holds, and its JavaScript version and reference are the AI’s. OpenDSA’s ListOverhead question waits for the converter '
    'of OpenDSA’s exercises, and its two linked-list proficiency exercises for an answer type that takes a sequence. '
    'Exercism’s simple-linked-list tests a linked stack and is held for Section 3.1; MIT 6.006’s problem 1-4 is on doubly '
    'linked lists and is held for Section 2.6. ODS Exercises 3.2–3.4 and Coding Interview University’s “implement a linked '
    'list” checklist have no tests of their own, and Kattis’s joinstrings and sim only sample cases, so they are left out; '
    'the keon, TheAlgorithms and trekhleb linked-list files, merge_two_lists among them, are tests without a printed '
    'statement. No exercise was found for multiple indirection.')

SECTION = {
    'id': '2.5', 'chapter': '2', 'title': 'Singly linked lists', 'short': 'Singly linked lists',
    'lead': LEAD, 'objectives': [], 'summary_html': '',
    'notes': 'Wikipedia’s comparison table of list structures, its citations and the argv example of multiple indirection are left out.',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'built': '2026-11-09',
    'exercise_notes': EXERCISE_NOTES,
    'figures': [
        {'id': 'photo-singly-linked-list', 'kind': 'photo'},
        {'id': 'sim-sorted-insert', 'kind': 'sim', 'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
        {'id': 'sim-list-ops', 'kind': 'sim',
         'originals': ['/media/ch02/wp-cpt-addingnode.png', '/media/ch02/wp-cpt-deletingnode.png'],
         'original_caption': '{{caption-text CPT-LinkedLists-addingnode.svg}}. {{caption-text CPT-LinkedLists-deletingnode.svg}}.',
         'draws': ['index', 'key', 'cost', 'size'], 'ai': FIG_AI},
    ],
    'coverage': [
        {'span': 'singly-linked-list', 'concept': 'singly-linked-list', 'verb': 'introduces'},
        {'span': 'pointer-to-pointer', 'concept': 'pointer-to-pointer', 'verb': 'introduces'},
        {'span': 'pointer-to-pointer', 'concept': 'singly-linked-list', 'verb': 'uses'},
        {'span': 'list-operations', 'concept': 'implement-linked-list', 'verb': 'introduces'},
        {'span': 'list-operations', 'concept': 'singly-linked-list', 'verb': 'uses'},
        {'span': 'lists-vs-arrays', 'concept': 'linked-list-vs-array', 'verb': 'introduces'},
        {'span': 'lists-vs-arrays', 'concept': 'singly-linked-list', 'verb': 'uses'},
    ],
    'referents': [
        {'id': 'p', 'label': 'p, the pointer to a link', 'figures': ['sim-sorted-insert']},
        {'id': 'item', 'label': 'item, the element being inserted', 'figures': ['sim-sorted-insert']},
        {'id': 'head', 'label': 'head, the caller’s pointer to the first element', 'figures': ['sim-sorted-insert']},
        {'id': 'node', 'label': 'node, the node the operation works after', 'figures': ['sim-list-ops']},
        {'id': 'new-node', 'label': 'newNode, the node being inserted', 'figures': ['sim-list-ops']},
        {'id': 'obsolete-node', 'label': 'obsoleteNode, the node being removed', 'figures': ['sim-list-ops']},
    ],
    'footnotes_extra': [
        {'id': 'err-sorted-comment', 'kind': 'correction',
         'html': ('The comment at the head of the listing says the item goes in at the first place “where all earlier elements '
                  'have lesser or equal value”. The loop stops at the first element whose value is not less than the item’s, so '
                  'every earlier element is strictly less, and the item goes in before any element equal to it. The code is a '
                  'correct sorted insert; only the comment is loose.')},
    ],
}


# ---------------------------------------------------------------- the exercise
ICC = 'sources/_cache/icc/linked_lists/linked_list'
RUN_PY = '''

def run(ops):
    """Given: plays the tests' operations on a LinkedList and returns what the queries give."""
    out, lst = [], None
    for op, *args in ops:
        if op == 'new':
            lst = LinkedList(Node(args[0]) if args else None)
        elif op == 'len':
            out.append(len(lst))
        elif op == 'find':
            node = lst.find(*args)
            out.append(None if node is None else str(node))
        elif op == 'get_all_data':
            out.append(lst.get_all_data())
        else:
            getattr(lst, op)(*args)
    return out
'''
RUN_JS = '''

// Given: plays the tests' operations on a LinkedList and returns what the queries give.
function run(ops) {
    const out = [];
    let lst = null;
    const call = { insert_to_front: 'insertToFront', append: 'append', delete: 'delete' };
    for (const [op, ...args] of ops) {
        if (op === 'new') lst = new LinkedList(args.length ? new Node(args[0]) : null);
        else if (op === 'len') out.push(lst.length());
        else if (op === 'find') { const node = lst.find(args[0]); out.push(node === null ? null : String(node)); }
        else if (op === 'get_all_data') out.push(lst.getAllData());
        else lst[call[op]](...args);
    }
    return out;
}
'''
STARTER_JS = '''class Node {
    constructor(data, next = null) {
        // TODO: Implement me
    }

    toString() {
        // TODO: Implement me
    }
}

class LinkedList {
    constructor(head = null) {
        // TODO: Implement me
    }

    length() {
        // TODO: Implement me
    }

    insertToFront(data) {
        // TODO: Implement me
    }

    append(data) {
        // TODO: Implement me
    }

    find(data) {
        // TODO: Implement me
    }

    delete(data) {
        // TODO: Implement me
    }

    printList() {
        // TODO: Implement me
    }

    getAllData() {
        // TODO: Implement me
    }
}'''
REF_JS = '''class Node {
    constructor(data, next = null) {
        this.next = next;
        this.data = data;
    }

    toString() {
        return String(this.data);
    }
}

class LinkedList {
    constructor(head = null) {
        this.head = head;
    }

    length() {
        let curr = this.head;
        let counter = 0;
        while (curr !== null) {
            counter += 1;
            curr = curr.next;
        }
        return counter;
    }

    insertToFront(data) {
        if (data === null || data === undefined) return null;
        const node = new Node(data, this.head);
        this.head = node;
        return node;
    }

    append(data) {
        if (data === null || data === undefined) return null;
        const node = new Node(data);
        if (this.head === null) {
            this.head = node;
            return node;
        }
        let curr = this.head;
        while (curr.next !== null) curr = curr.next;
        curr.next = node;
        return node;
    }

    find(data) {
        if (data === null || data === undefined) return null;
        let curr = this.head;
        while (curr !== null) {
            if (curr.data === data) return curr;
            curr = curr.next;
        }
        return null;
    }

    delete(data) {
        if (data === null || data === undefined) return;
        if (this.head === null) return;
        if (this.head.data === data) {
            this.head = this.head.next;
            return;
        }
        let prev = this.head;
        let curr = this.head.next;
        while (curr !== null) {
            if (curr.data === data) {
                prev.next = curr.next;
                return;
            }
            prev = curr;
            curr = curr.next;
        }
    }

    printList() {
        let curr = this.head;
        while (curr !== null) {
            console.log(curr.data);
            curr = curr.next;
        }
    }

    getAllData() {
        const data = [];
        let curr = this.head;
        while (curr !== null) {
            data.push(curr.data);
            curr = curr.next;
        }
        return data;
    }
}'''
# icc's test_linked_list.py, one test per test method, its asserts as the queries of one operation list (in order)
TESTS = [
    ([['new'], ['insert_to_front', 10], ['get_all_data'], ['insert_to_front', None], ['get_all_data'],
      ['insert_to_front', 'a'], ['insert_to_front', 'bc'], ['get_all_data']], [[10], [10], ['bc', 'a', 10]]),
    ([['new'], ['append', 10], ['get_all_data'], ['append', None], ['get_all_data'],
      ['append', 'a'], ['append', 'bc'], ['get_all_data']], [[10], [10], [10, 'a', 'bc']]),
    ([['new'], ['find', 'a'], ['new', 10], ['find', None], ['new', 10], ['insert_to_front', 'a'], ['insert_to_front', 'bc'],
      ['find', 'a'], ['find', 'aaa']], [None, None, 'a', None]),
    ([['new'], ['delete', 'a'], ['get_all_data'], ['new', 10], ['delete', None], ['get_all_data'],
      ['new', 10], ['insert_to_front', 'a'], ['insert_to_front', 'bc'], ['delete', 'a'], ['get_all_data'],
      ['delete', 'aa'], ['get_all_data']], [[], [10], ['bc', 10], ['bc', 10]]),
    ([['new'], ['len'], ['new', 10], ['insert_to_front', 'a'], ['insert_to_front', 'bc'], ['len']], [0, 3]),
]


def icc_prompt(book):
    nb = json.load(open(os.path.join(book, ICC, 'linked_list_challenge.ipynb'), encoding='utf-8'))
    cells = [''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'markdown']
    problem = next(c for c in cells if c.startswith('## Problem:')).split('\n')[0][len('## Problem: '):].strip()
    cons = next(c for c in cells if c.startswith('## Constraints')).split('\n')[1:]
    qa, out = [], []
    for line in cons:
        line = line.rstrip()
        if line.startswith('* '):
            qa.append([line[2:].strip(), None])
        elif line.strip().startswith('* ') and qa:
            qa[-1][1] = line.strip()[2:].strip()
    out.append(problem)
    out.append('Constraints:\n\n' + '\n'.join(f'- {q} {a}' for q, a in qa))
    return '\n\n'.join(out)


def icc_starter_py(book):
    nb = json.load(open(os.path.join(book, ICC, 'linked_list_challenge.ipynb'), encoding='utf-8'))
    code = next(''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'code' and 'class LinkedList' in ''.join(c['source']))
    return code.rstrip() + '\n'


def EXERCISES(exercism_code, book):
    ref_py = open(os.path.join(book, ICC, 'linked_list.py'), encoding='utf-8').read().rstrip() + '\n'
    tests = [{'args': [ops], 'expect': exp, 'visible': i < 2, 'generated_by': 'source'} for i, (ops, exp) in enumerate(TESTS)]
    ex = {
        'id': 'c1', 'source_id': 'icc:linked_lists/linked_list', 'source_number': 'linked_list', 'origin': 'icc',
        'kind': 'code', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'list-operations',
        'changes': ('The tests are the source’s unit tests, each test method one list of operations that a given run(ops) '
                    'plays on your LinkedList; print_list is not tested, as in the source.'),
        'prompt': icc_prompt(book),
        'answer': {
            'type': 'code',
            'python': {'entry': 'run', 'starter': icc_starter_py(book) + RUN_PY, 'reference': ref_py + RUN_PY, 'generated_by': 'source'},
            'javascript': {'entry': 'run', 'starter': STARTER_JS + RUN_JS, 'reference': REF_JS + RUN_JS, 'generated_by': 'ai'},
            'tests': tests, 'generated_by': 'source'},
    }
    return [ex], [{'exercise': 'c1', 'concept': 'singly-linked-list'}, {'exercise': 'c1', 'concept': 'implement-linked-list'}]
