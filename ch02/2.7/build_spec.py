TITLE = 'Cycles in linked lists: tortoise and hare'
MD_FILE = 'sources/_cache/cpa/src/others/tortoise_and_hare.md'
LOC = 'cpa:others/tortoise_and_hare'
STEP2 = '### Step 2: Starting point of the cycle'
BLOCKS = [
    dict(id='tortoise-hare', source='cpa', locator=f'{LOC}, its opening, #proposed-algorithm and its ###Step 1',
         **{'from': "# Floyd's Linked List Cycle Finding Algorithm", 'to': STEP2}),
    dict(id='cycle-start', source='cpa', locator=f'{LOC}#step-2-starting-point-of-the-cycle, with both Java snippets',
         **{'from': STEP2, 'to': '## Why does it work'}),
    dict(id='why-meet', source='cpa', locator=f'{LOC}#why-does-it-work, its ###Step 1',
         to_nth=2, **{'from': '## Why does it work', 'to': STEP2}),
    dict(id='cycle-start-proof', source='cpa', locator=f'{LOC}#step-2-starting-point-of-the-cycle_1',
         h2='Why the reset finds the cycle start', from_nth=2, **{'from': STEP2, 'to': '# Problems:'}),
]
MEDIA = '/media/ch02'


def ref(rid, word):
    return f'<span data-ref="{rid}">{word}</span>'


def sim(fid, caption, original, original_caption):
    return (f'<figure class="sim" id="{fid}" data-original="{original}" data-original-caption="{original_caption}">\n'
            f'  <div class="sim-head"><span class="eyebrow">Sim</span><span>{caption}</span></div>\n</figure>')


SLOW, FAST, HEAD, C_, G_ = ref('slow', '<em>slow</em>'), ref('fast', '<em>fast</em>'), ref('head', 'head'), ref('C', 'C'), ref('G', 'G')
HTML = {
    'sim-rho-list': sim(
        'sim-rho-list',
        f'A linked list with a cycle: from the {HEAD} the links run through A and B to {C_}, round through D to H, and from H back to '
        f'{C_}, so following them never reaches null.',
        f'{MEDIA}/cpa-tortoise-hare-algo.png', '{{caption-text tortoise_hare_algo.png}}'),
    'sim-rho': sim(
        'sim-rho',
        f'{SLOW} moves one node a step and {FAST} two. Once both are in the cycle, {FAST} gains one node on {SLOW} each step until '
        f'they share a node, {G_}. Then {SLOW} goes back to the {HEAD} and both move one node a step, always the same distance from '
        f'{C_}, so they meet there. On a list with no cycle, {FAST} reaches null first.',
        f'{MEDIA}/cpa-tortoise-hare-cycle-found.png', '{{caption-text tortoise_hare_cycle_found.png}}'),
    'sim-rho-proof': sim(
        'sim-rho-proof',
        f'Whatever the tail’s length <em>a</em> and the cycle’s length <em>L</em>, {SLOW} and {FAST} first meet at a node {G_}, '
        f'<em>b</em> steps past {C_}, after <em>x</em> laps of {SLOW} and <em>y</em> of {FAST}. Because {FAST} has gone twice as far, '
        f'<em>a</em> = (<em>y</em> − 2<em>x</em>)<em>L</em> − <em>b</em>: going <em>a</em> steps on from {G_} makes whole laps less '
        f'<em>b</em> and stops on {C_}, just as <em>a</em> steps from the {HEAD} does.',
        f'{MEDIA}/cpa-tortoise-hare-proof.png', '{{caption-text tortoise_hare_proof.png}}'),
    'drv-cycle-start': '<figure class="dv" id="drv-cycle-start"></figure>',
}
IMAGES = {'tortoise_hare_algo.png': 'sim-rho-list', 'tortoise_hare_cycle_found.png': None, 'tortoise_hare_proof.png': 'sim-rho-proof'}
CODE = [('cycle-start', '// Presence of cycle', 'sim-rho'), ('cycle-start', '// Assuming there is a cycle present', 'sim-rho'),
        ('why-meet', 'slow: 0 --> 1', None)]
REPLACE = [('cycle-start-proof', r'$fastDist = 2 \cdot (slowDist)$', '$a=(y-2x)L-b$', 'drv-cycle-start')]
DROP = [('cycle-start-proof', '$slowDist = a + xL + b$'), ('cycle-start-proof', '$fastDist = a + yL + b$')]

S_, F_ = '<span data-ref="slow">$slow$</span>', '<span data-ref="fast">$fast$</span>'
SF = 'data-ref="slow fast"'
MARKS = [
    # block 1: the concept, the head, C, and every mention of the two pointers
    ('tortoise-hare', '<strong>Floyd’s Cycle Algorithm or Tortoise And Hare algorithm</strong>',
     '<strong><span data-concept="floyd-cycle-detection">Floyd’s Cycle Algorithm or Tortoise And Hare algorithm</span></strong>'),
    ('tortoise-hare', '<strong>head</strong>', '<span data-ref="head"><strong>head</strong></span>'),
    ('tortoise-hare', '<strong>C</strong>', '<span data-ref="C"><strong>C</strong></span>', 2),
    ('tortoise-hare', 'point to head of the linked list', 'point to <span data-ref="head">head</span> of the linked list'),
    ('tortoise-hare', '$slow$', S_, 3),
    ('tortoise-hare', '$fast$', F_, 2),
    ('tortoise-hare', 'Both of them', f'<span {SF}>Both of them</span>'),
    ('tortoise-hare', 'at any point they point', f'at any point <span {SF}>they</span> point'),
    ('tortoise-hare', 'If they point to the same node', f'If <span {SF}>they</span> point to the same node'),
    # block 2
    ('cycle-start', '$slow$', S_),
    ('cycle-start', '<strong>head</strong>', '<span data-ref="head"><strong>head</strong></span>'),
    ('cycle-start', 'Move both pointers', f'Move <span {SF}>both pointers</span>'),
    ('cycle-start', 'The point they will meet at will be the starting point of the cycle.',
     '<span data-concept="cycle-start">The point they will meet at will be the starting point of the cycle.</span>'),
    # block 3
    ('why-meet', '$fast$', F_, 3),
    ('why-meet', '$slow$', S_, 2),
    ('why-meet', 'both of these pointers', f'<span {SF}>both of these pointers</span>'),
    ('why-meet', 'for the slow pointer to reach the entry of cycle', 'for <span data-ref="slow">the slow pointer</span> to reach <span data-ref="C">the entry of cycle</span>'),
    ('why-meet', 'When the slow pointer has moved', 'When <span data-ref="slow">the slow pointer</span> has moved'),
    ('why-meet', 'and the fast pointer has covered', 'and <span data-ref="fast">the fast pointer</span> has covered'),
    ('why-meet', 'both pointers find themselves', f'<span {SF}>both pointers</span> find themselves'),
    # block 4
    ('cycle-start-proof', 'Let\'s try to calculate the distance covered by both of the pointers till the point they meet within the cycle.',
     '<span data-concept="cycle-start-proof">Let\'s try to calculate the distance covered by both of the pointers till the point they meet within the cycle.</span>'),
    ('cycle-start-proof', '<strong>C</strong>', '<span data-ref="C"><strong>C</strong></span>', 3),
    ('cycle-start-proof', '<strong>G</strong>', '<span data-ref="G"><strong>G</strong></span>'),
    ('cycle-start-proof', 'covered by slow pointer', 'covered by <span data-ref="slow">slow pointer</span>'),
    ('cycle-start-proof', 'covered by fast pointer', 'covered by <span data-ref="fast">fast pointer</span>'),
    ('cycle-start-proof', 'times the slow pointer has looped', 'times <span data-ref="slow">the slow pointer</span> has looped'),
    ('cycle-start-proof', 'times the fast pointer has looped', 'times <span data-ref="fast">the fast pointer</span> has looped'),
    ('cycle-start-proof', 'Since the fast pointer already is', 'Since <span data-ref="fast">the fast pointer</span> already is'),
    ('cycle-start-proof', 'ahead of the entry of cycle, if fast pointer moves', 'ahead of <span data-ref="C">the entry of cycle</span>, if <span data-ref="fast">fast pointer</span> moves'),
    ('cycle-start-proof', 'end up at the entry of the cycle', 'end up at <span data-ref="C">the entry of the cycle</span>'),
    ('cycle-start-proof', 'we let the slow pointer start', 'we let <span data-ref="slow">the slow pointer</span> start'),
    ('cycle-start-proof', 'also end up at the cycle entry', 'also end up at <span data-ref="C">the cycle entry</span>'),
    ('cycle-start-proof', 'they both will meet the entry of cycle', f'<span {SF}>they both</span> will meet <span data-ref="C">the entry of cycle</span>'),
]

# ---------------------------------------------------------------- section.json (tools/build_section.py)
MODEL = {'model': 'claude-opus-5-5', 'effort': 'high'}
FIG_AI = [{'model': 'claude-opus-5-5', 'effort': 'high', 'part': 'built'}]
LEAD = ('An Essential section on telling whether a singly linked list ends or loops back on itself, and on finding the node where '
        'the loop begins, using two pointers that move at different speeds. Nothing here is indexed: a and b count steps along the '
        'list, L is the length of the cycle, and x and y count the laps each pointer makes.')

SD, FD = r'\mathit{slowDist}', r'\mathit{fastDist}'
DERIVATIONS = [{
    'id': 'cycle-start',
    'what': 'where the cycle starts',
    'source': 'cp-algorithms, Floyd’s Linked List Cycle Finding Algorithm, why does it work, step 2',
    'nodes': [{
        'assumes': [
            {'tex': SD + ' = a + xL + b'},
            {'tex': FD + ' = a + yL + b'},
        ],
        'then': {'tex': r'\mk{f}{' + FD + r'} = 2 \cdot (\mk{s}{' + SD + '})', 'src': 'why does it work, step 1'},
        'steps': [
            {'tex': r'\mk{a1}{a} + \mk{y}{yL} + \mk{b1}{b} = 2(\mk{a2}{a} + \mk{x}{xL} + \mk{b2}{b})', 'uses': [0, 1],
             'map': {'f': ['a1', 'y', 'b1'], 's': ['a2', 'x', 'b2']}},
            {'tex': r'\mk{a1}{a} + \mk{y}{yL} + \mk{b1}{b} = \mk{a2}{2a} + \mk{x}{2xL} + \mk{b2}{2b}', 'uses': []},
            {'tex': r'\mk{y}{yL} = \mk{a2}{a} + \mk{x}{2xL} + \mk{b2}{b}', 'uses': []},
            {'tex': r'\mk{a2}{a} = \mk{y}{yL} - \mk{x}{2xL} - \mk{b2}{b}', 'uses': []},
            {'tex': r'\mk{a2}{a} = \mk{k}{(y - 2x)L} - \mk{b2}{b}', 'uses': [], 'map': {'y': 'k', 'x': 'k'}},
        ],
    }],
}]

SECTION = {
    'id': '2.7', 'chapter': '2', 'title': 'Cycles in linked lists: tortoise and hare', 'short': 'Tortoise and hare',
    'lead': LEAD,
    'objectives': [], 'summary_html': '',
    'notes': 'cp-algorithms’ list of practice problems is left out here.',
    'built': '2026-11-09',
    'ai': {'text': [MODEL], 'figures': [MODEL]},
    'exercise_notes': (
        'The code exercise is Interactive Coding Challenges’ find_loop_start, with its own five tests and its solution as the Python '
        'reference; the five further tests, the harness that builds each list and the JavaScript reference are written by the AI that '
        'built the section. keon’s is_cyclic and first_cyclic_node and TheAlgorithms’ has_loop, floyds_cycle_detection and happy_number '
        'carry tests but print no exercise statement, so they have no card. No open exercise tests why the reset finds the start of '
        'the cycle, and none of the chapter’s check, trace or NC items covers this section.'),
    'figures': [
        {'id': 'sim-rho-list', 'kind': 'sim', 'originals': [f'{MEDIA}/cpa-tortoise-hare-algo.png'],
         'original_caption': '{{caption-text tortoise_hare_algo.png}}', 'draws': [], 'ai': FIG_AI},
        {'id': 'sim-rho', 'kind': 'sim', 'originals': [f'{MEDIA}/cpa-tortoise-hare-cycle-found.png'],
         'original_caption': '{{caption-text tortoise_hare_cycle_found.png}}', 'draws': ['index', 'size', 'cost'], 'ai': FIG_AI},
        {'id': 'sim-rho-proof', 'kind': 'sim', 'originals': [f'{MEDIA}/cpa-tortoise-hare-proof.png'],
         'original_caption': '{{caption-text tortoise_hare_proof.png}}', 'draws': ['size'], 'ai': FIG_AI},
    ],
    'referents': [
        {'id': 'slow', 'label': 'slow, the pointer that moves one node at a time', 'figures': ['sim-rho']},
        {'id': 'fast', 'label': 'fast, the pointer that moves two nodes at a time', 'figures': ['sim-rho']},
        {'id': 'head', 'label': 'the head of the list', 'figures': ['sim-rho-list', 'sim-rho', 'sim-rho-proof']},
        {'id': 'C', 'label': 'C, the node where the cycle starts', 'figures': ['sim-rho-list', 'sim-rho', 'sim-rho-proof']},
        {'id': 'G', 'label': 'G, the node where slow and fast meet', 'figures': ['sim-rho', 'sim-rho-proof']},
    ],
    'coverage': [
        {'span': 'tortoise-hare', 'concept': 'floyd-cycle-detection', 'verb': 'introduces'},
        {'span': 'cycle-start', 'concept': 'cycle-start', 'verb': 'introduces'},
        {'span': 'cycle-start', 'concept': 'floyd-cycle-detection', 'verb': 'uses'},
        {'span': 'why-meet', 'concept': 'floyd-cycle-detection', 'verb': 'reinforces'},
        {'span': 'cycle-start-proof', 'concept': 'cycle-start-proof', 'verb': 'introduces'},
        {'span': 'cycle-start-proof', 'concept': 'cycle-start', 'verb': 'uses'},
    ],
    'footnotes_extra': [],
    'derivations': DERIVATIONS,
}

# ---------------------------------------------------------------- the code exercise: icc find_loop_start
ICC = 'sources/_cache/icc/linked_lists'
HARNESS_PY = """

def loop_start(values, back_to):
    # Builds the list a test describes and returns the data of the node find_loop_start finds. Leave it as it is.
    nodes = [Node(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if back_to >= 0:
        nodes[-1].next = nodes[back_to]
    found = find_loop_start(nodes[0] if nodes else None)
    return None if found is None else found.data
"""
NODE_JS = """class Node {
  constructor(data, next = null) {
    this.next = next;
    this.data = data;
  }
}
"""
HARNESS_JS = """
// Builds the list a test describes and returns the data of the node findLoopStart finds. Leave it as it is.
function loopStart(values, backTo) {
  const nodes = values.map((v) => new Node(v));
  for (let i = 0; i + 1 < nodes.length; i += 1) nodes[i].next = nodes[i + 1];
  if (backTo >= 0) nodes[nodes.length - 1].next = nodes[backTo];
  const found = findLoopStart(nodes.length ? nodes[0] : null);
  return found === null ? null : found.data;
}
"""
REF_JS = NODE_JS + """
function findLoopStart(head) {
  if (head === null || head.next === null) {
    return null;
  }
  let slow = head;
  let fast = head;
  while (fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
    if (fast === null) {
      return null;
    }
    if (slow === fast) {
      break;
    }
  }
  slow = head;
  while (slow !== fast) {
    slow = slow.next;
    fast = fast.next;
    if (fast === null) {
      return null;
    }
  }
  return slow;
}
""" + HARNESS_JS


def icc_parts(book):
    """The challenge's statement and constraints, and its solution as a function of the head, read from the notebooks."""
    import json
    import os
    import re
    import textwrap
    nb = json.load(open(os.path.join(book, ICC, 'find_loop_start/find_loop_start_challenge.ipynb'), encoding='utf-8'))
    md = [''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'markdown']
    problem = next(m for m in md if m.startswith('## Problem:'))
    statement = problem.split('\n')[0].replace('## Problem:', '').strip()
    cons = next(m for m in md if m.startswith('## Constraints'))
    qa, cur = [], None
    for l in cons.split('\n')[1:]:
        if l.startswith('* '):
            cur = l[2:].strip()
        elif l.strip().startswith('* ') and cur:
            qa.append(f'{cur} {l.strip()[2:].strip()}.')
            cur = None
    sol = json.load(open(os.path.join(book, ICC, 'find_loop_start/find_loop_start_solution.ipynb'), encoding='utf-8'))
    code = next(''.join(c['source']) for c in sol['cells'] if c['cell_type'] == 'code' and 'def find_loop_start' in ''.join(c['source']))
    body = code[code.index('    def find_loop_start(self):'):]
    func = textwrap.dedent(body).replace('def find_loop_start(self):', 'def find_loop_start(head):').replace('self.head', 'head')
    ll = open(os.path.join(book, ICC, 'linked_list/linked_list.py'), encoding='utf-8').read()
    node = ll[ll.index('class Node(object):'):ll.index('    def __str__')].rstrip() + '\n'
    return statement, qa, node, func.rstrip() + '\n'


def EXERCISES(exercism, book):
    statement, qa, node, func = icc_parts(book)
    prompt = statement + '\n\n' + '\n\n'.join(qa)
    starter_py = node + '\n\ndef find_loop_start(head):\n    pass\n' + HARNESS_PY
    starter_js = NODE_JS + '\nfunction findLoopStart(head) {\n}\n' + HARNESS_JS
    ref_py = node + '\n\n' + func + HARNESS_PY
    src = lambda args, expect, visible=False: {'args': args, 'expect': expect, 'visible': visible, 'generated_by': 'source'}
    ai = lambda args, expect: {'args': args, 'expect': expect, 'visible': False, 'generated_by': 'ai'}
    tests = [
        src([[], -1], None, True), src([[1], -1], None), src([[1, 2], -1], None), src([[1, 2, 3], -1], None),
        src([list(range(11)), 3], 3, True),
        ai([list(range(6)), 0], 0), ai([[7], 0], 7), ai([[0, 1, 2, 3], 3], 3), ai([list(range(10)), 7], 7), ai([[5, 6], 0], 5),
    ]
    ex = {
        'id': 'c1', 'source_id': 'icc:linked_lists/find_loop_start', 'source_number': 'find_loop_start', 'origin': 'icc',
        'changes': ('find_loop_start takes the head as its argument instead of being a method of the list class, and each test builds '
                    'its list from the values and the position the last node links back to (−1 for none) and compares the data of '
                    'the node returned.'),
        'kind': 'code', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'cycle-start', 'prompt': prompt,
        'answer': {
            'type': 'code',
            'python': {'entry': 'loop_start', 'starter': starter_py, 'reference': ref_py, 'generated_by': 'source'},
            'javascript': {'entry': 'loopStart', 'starter': starter_js, 'reference': REF_JS, 'generated_by': 'ai'},
            'tests': tests, 'bound': 'n', 'grow': '(n) => [Array.from({ length: n }, (_, i) => i), Math.floor(n / 2)]',
            'generated_by': 'source',
        },
    }
    return [ex], [{'exercise': 'c1', 'concept': 'floyd-cycle-detection'}, {'exercise': 'c1', 'concept': 'cycle-start'}]
