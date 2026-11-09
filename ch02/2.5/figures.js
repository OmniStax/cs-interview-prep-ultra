/* Figures for section 2.5 Singly linked lists. Boots against the section's text article.
   Two debugger figures (code beside the drawing, stepped by block: METHOD §2.3), drawn with F.ds.nodes,
   F.ds.links and F.ds.nodePointer:
   - sim-sorted-insert: Wikipedia's double-indirection sorted insert (Pointer, #Multiple indirection), its C
     verbatim as the panel (C++ is the one language of the four that can take a pointer's address; plan,
     Questions 1–2), p drawn as a pointer to a link field.
   - sim-list-ops: Wikipedia's four in-place operations (Linked list, #Singly linked lists), translated from
     its pseudocode into Python, Java, C++ and JavaScript by the AI (all four AI-marked, the names kept as
     Wikipedia's), with a five-line walk to the last node for the append input.
   Each trace is the figure's own JS copy of the code shown. Node values wear `key`, list.firstNode `index`
   (the head, COLOR.md), the counters `cost` and n `size`; the code's pointer variables are referents. A node
   no link from the head reaches is dashed, a destroyed one faded to ink (status is decoration, COLOR.md). */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['2.5'] = function (root, F) {
const { C, PAL, alpha, text, topline, arrow } = F;
const sim = (id, H) => F.sim(root, id, H);
const AI = 'claude-opus-5-5 high';
const lerp = (a, b, k) => a + (b - a) * k;
const lerpPt = (a, b, k) => ({ x: lerp(a.x, b.x, k), y: lerp(a.y, b.y, k) });
const ROW = 330, CELL = 78, NH = 58;

/* the nodes a link from `start` reaches, in order, through `next` */
const chain = (start, next) => { const out = [], seen = new Set(); let id = start; while (id && !seen.has(id)) { seen.add(id); out.push(id); id = next[id]; } return out; };

/* a link that changes target between two frames swings from the old landing point to the new one; one that
   jumps over nodes of its row curves above them */
function drawLinks(ctx, N, from, prevTo, curTo, k, color, w, alphaOf, nullLabel) {
  const between = (a, b) => {
    const A = N.at(a), B = b ? N.at(b) : null; if (!A || !B || Math.abs(A.y - B.y) > 4) return 0;
    const lo = Math.min(A.x, B.x), hi = Math.max(A.x, B.x);
    return N.boxes.some((x) => x.id !== a && x.id !== b && Math.abs(x.y - A.y) < 4 && x.x > lo + 1 && x.x < hi - 1) ? -84 : 0;
  };
  const end = (id) => {
    const A = N.at(from);
    if (id === null || id === undefined) return { x: A.link.x + N.cell * 1.1, y: A.y };
    return N.entry(id, A.link);
  };
  const same = prevTo === curTo, kk = same ? 1 : k;
  if (curTo === undefined) return null;
  if (same || kk >= 1) {
    return F.ds.links(ctx, N, { from, to: curTo, color, w, bend: between(from, curTo), alpha: alphaOf }, { nullLabel })[0];
  }
  const to = lerpPt(prevTo === undefined ? N.at(from).link : end(prevTo), end(curTo), kk);
  const bend = lerp(between(from, prevTo), between(from, curTo), kk);
  return F.ds.links(ctx, N, { from, to, color, w, bend, alpha: alphaOf })[0];
}

/* ================================================================ sim-list-ops */
(function () {
  const PY = [
    'def insertAfter(node, newNode):',
    '    newNode.next = node.next',
    '    node.next = newNode',
    '',
    'def insertBeginning(list, newNode):',
    '    newNode.next = list.firstNode',
    '    list.firstNode = newNode',
    '',
    'def removeAfter(node):',
    '    obsoleteNode = node.next',
    '    node.next = node.next.next',
    '    del obsoleteNode',
    '',
    'def removeBeginning(list):',
    '    obsoleteNode = list.firstNode',
    '    list.firstNode = list.firstNode.next',
    '    del obsoleteNode',
    '',
    'def lastNode(list):',
    '    node = list.firstNode',
    '    while node.next is not None:',
    '        node = node.next',
    '    return node',
  ].join('\n');
  /* Java, C++ and JavaScript: the same lines, each function closed by a brace and the loop by one more */
  const braced = (o) => [
    `${o.void}insertAfter(${o.N}node, ${o.N}newNode) {`,
    `    newNode${o.d}next = node${o.d}next;`,
    `    node${o.d}next = newNode;`,
    '}',
    '',
    `${o.void}insertBeginning(${o.L}list, ${o.N}newNode) {`,
    `    newNode${o.d}next = list${o.d}firstNode;`,
    `    list${o.d}firstNode = newNode;`,
    '}',
    '',
    `${o.void}removeAfter(${o.N}node) {`,
    `    ${o.local}obsoleteNode = node${o.d}next;`,
    `    node${o.d}next = node${o.d}next${o.d}next;`,
    `    ${o.free}`,
    '}',
    '',
    `${o.void}removeBeginning(${o.L}list) {`,
    `    ${o.local}obsoleteNode = list${o.d}firstNode;`,
    `    list${o.d}firstNode = list${o.d}firstNode${o.d}next;`,
    `    ${o.free}`,
    '}',
    '',
    `${o.ret}lastNode(${o.L}list) {`,
    `    ${o.local}node = list${o.d}firstNode;`,
    `    while (node${o.d}next != ${o.nil}) {`,
    `        node = node${o.d}next;`,
    '    }',
    '    return node;',
    '}',
  ].join('\n');
  const JAVA = braced({ void: 'void ', ret: 'Node ', N: 'Node ', L: 'List ', d: '.', local: 'Node ', nil: 'null', free: 'obsoleteNode = null; // nothing refers to it: the collector frees it' });
  const CPP = braced({ void: 'void ', ret: 'Node* ', N: 'Node* ', L: 'List* ', d: '->', local: 'Node* ', nil: 'nullptr', free: 'delete obsoleteNode;' });
  const JS = braced({ void: 'function ', ret: 'function ', N: '', L: '', d: '.', local: 'let ', nil: 'null', free: 'obsoleteNode = null; // nothing refers to it: the collector frees it' });
  const MAP = { 1: 1, 2: 2, 3: 3, 4: 5, 5: 6, 6: 7, 7: 8, 8: 10, 9: 11, 10: 12, 11: 13, 12: 14, 13: 16, 14: 17, 15: 18, 16: 19, 17: 20, 18: 22, 19: 23, 20: 24, 21: 25, 22: 26, 23: 28 };

  /* the inputs: Wikipedia's diagrams (12, 99 and 37), the edge case the text notices and the bad case */
  const INPUTS = [
    { value: 'after', label: 'insert after', list: [12, 99], newVal: 37, op: 'insertAfter', at: 12,
      pos: { L: 150, 12: 420, 99: 880, 37: [650, 190] },
      head: 'insertAfter(node, newNode): 37 goes in after 12, and two links change.' },
    { value: 'front', label: 'insert at the front', list: [12, 99], newVal: 37, op: 'insertBeginning',
      pos: { L: 150, 12: 560, 99: 940, 37: [360, 190] },
      head: 'insertBeginning(list, newNode): 37 becomes the first node, and firstNode changes.' },
    { value: 'remove', label: 'remove after', list: [12, 99, 37], op: 'removeAfter', at: 12,
      pos: { L: 150, 12: 420, 99: 700, 37: 980 },
      head: 'removeAfter(node): the node after 12 goes, and one link changes.' },
    { value: 'remove-first', label: 'remove the first', list: [12, 99, 37], op: 'removeBeginning',
      pos: { L: 150, 12: 420, 99: 700, 37: 980 },
      head: 'removeBeginning(list): the first node goes, and firstNode changes.' },
    { value: 'only', label: 'remove the only node', list: [12], op: 'removeBeginning',
      pos: { L: 150, 12: 480 },
      head: 'removeBeginning(list) on a one-node list: firstNode becomes null.' },
    { value: 'append', label: 'append, no tail', list: [12, 99, 37], newVal: 42, op: 'append',
      pos: { L: 150, 12: 380, 99: 620, 37: 860, 42: [1090, 190] },
      head: 'Appending 42 with no reference to the tail: walk to the last node, then insert after it.' },
  ];

  /* one input's run, as frames of the Python. Besides the code's variables, each frame carries the list as
     the drawing reads it (`S`: firstNode, every node's next, the destroyed nodes) and the counts. */
  const run = (inp) => F.trace((at) => {
    const next = {}, gone = [];
    inp.list.forEach((v, j) => { next[v] = j + 1 < inp.list.length ? inp.list[j + 1] : null; });
    let first = inp.list[0];
    if (inp.newVal !== undefined) next[inp.newVal] = null;
    let hops = 0, writes = 0;
    const obj = (v) => (v === null || v === undefined ? null : { data: v, next: next[v] });
    const S = () => ({ first, next: Object.assign({}, next), gone: gone.slice(), hops, writes });
    const insertAfter = (node, newNode) => {
      at(1, { node: obj(node), newNode: obj(newNode), S: S() });
      next[newNode] = next[node]; writes += 1; at(2, { node: obj(node), newNode: obj(newNode), S: S() }, ['link', newNode]);
      next[node] = newNode; writes += 1; at(3, { node: obj(node), newNode: obj(newNode), S: S() }, ['link', node]);
    };
    const L = () => ({ firstNode: first });
    if (inp.op === 'insertAfter') insertAfter(inp.at, inp.newVal);
    else if (inp.op === 'insertBeginning') {
      const nn = inp.newVal;
      at(5, { list: L(), newNode: obj(nn), S: S() });
      next[nn] = first; writes += 1; at(6, { list: L(), newNode: obj(nn), S: S() }, ['link', nn]);
      first = nn; writes += 1; at(7, { list: L(), newNode: obj(nn), S: S() }, ['head']);
    } else if (inp.op === 'removeAfter') {
      const node = inp.at;
      at(9, { node: obj(node), S: S() });
      const ob = next[node]; at(10, { node: obj(node), obsoleteNode: obj(ob), S: S() }, ['hold', ob]);
      next[node] = next[ob]; writes += 1; at(11, { node: obj(node), obsoleteNode: obj(ob), S: S() }, ['link', node]);
      gone.push(ob); at(12, { node: obj(node), S: S() }, ['free', ob]);
    } else if (inp.op === 'removeBeginning') {
      at(14, { list: L(), S: S() });
      const ob = first; at(15, { list: L(), obsoleteNode: obj(ob), S: S() }, ['hold', ob]);
      first = next[ob]; writes += 1; at(16, { list: L(), obsoleteNode: obj(ob), S: S() }, ['head']);
      gone.push(ob); at(17, { list: L(), S: S() }, ['free', ob]);
    } else {
      /* append with no tail: lastNode, then insertAfter on what it returns */
      at(19, { list: L(), S: S() });
      let node = first; at(20, { list: L(), node: obj(node), S: S() });
      for (;;) {
        at(21, { list: L(), node: obj(node), S: S() }, ['test', next[node] !== null]);
        if (next[node] === null) break;
        node = next[node]; hops += 1; at(22, { list: L(), node: obj(node), S: S() }, ['hop', node]);
      }
      at(23, { list: L(), node: obj(node), S: S() });
      insertAfter(node, inp.newVal);
    }
  });
  const traces = Object.fromEntries(INPUTS.map((inp) => [inp.value, run(inp)]));

  const d = sim('sim-list-ops', 520);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS },
    ai: { python: AI, java: AI, cpp: AI, javascript: AI },
    lineMap: { java: MAP, cpp: MAP, javascript: MAP },
    blocks: [
      { id: 'insert-after', lines: [1, 3], label: 'insert newNode after node', touches: ['node', 'newNode'] },
      { id: 'ia-aim', lines: [2, 2], label: 'newNode takes node’s next link', touches: ['newNode'] },
      { id: 'ia-link', lines: [3, 3], label: 'node now points at newNode', touches: ['node'] },
      { id: 'insert-beginning', lines: [5, 7], label: 'insert newNode at the front', touches: ['newNode'] },
      { id: 'ib-aim', lines: [6, 6], label: 'newNode takes the first node as its next', touches: ['newNode'] },
      { id: 'ib-head', lines: [7, 7], label: 'firstNode now points at newNode', touches: ['newNode'] },
      { id: 'remove-after', lines: [9, 12], label: 'remove the node after node', touches: ['node', 'obsoleteNode'] },
      { id: 'ra-hold', lines: [10, 10], label: 'hold on to the node after node', touches: ['obsoleteNode'] },
      { id: 'ra-skip', lines: [11, 11], label: 'node’s link skips over it', touches: ['node'] },
      { id: 'ra-free', lines: [12, 12], label: 'nothing reaches it: destroy it', touches: ['obsoleteNode'] },
      { id: 'remove-beginning', lines: [14, 17], label: 'remove the first node', touches: ['obsoleteNode'] },
      { id: 'rb-hold', lines: [15, 15], label: 'hold on to the first node', touches: ['obsoleteNode'] },
      { id: 'rb-skip', lines: [16, 16], label: 'firstNode moves past it', touches: ['obsoleteNode'] },
      { id: 'rb-free', lines: [17, 17], label: 'nothing reaches it: destroy it', touches: ['obsoleteNode'] },
      { id: 'last-node', lines: [19, 23], label: 'walk to the last node', touches: ['node'] },
      { id: 'ln-start', lines: [20, 20], label: 'start at the first node', touches: ['node'] },
      { id: 'ln-hop', lines: [21, 22], label: 'follow one link', touches: ['node'] },
      { id: 'ln-last', lines: [23, 23], label: 'this node’s next is null: it is the last', touches: ['node'] },
    ],
    refs: { node: () => F.ref('node'), newNode: () => F.ref('new-node'), obsoleteNode: () => F.ref('obsolete-node') },
  });

  const tip = { hits: [] };
  F.hover(d.stage, () => tip.hits, d.c);

  F.debug(d, {
    code, level: 1, watch: ['list', 'node', 'newNode', 'obsoleteNode'],
    inputs: INPUTS.map((inp) => ({ value: inp.value, label: inp.label, trace: traces[inp.value] })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const inp = INPUTS.find((x) => x.value === g.input) || INPUTS[0];
      const S = g.frame.vars.S, P = g.prev.vars.S || S, k = g.k;
      const cIdx = C('index'), cKey = C('key'), cCost = C('cost'), cSize = C('size');
      const hits = [];
      topline(ctx, inp.head);

      /* the nodes where the input places them; the list record's firstNode a box of one link cell */
      const ids = Object.keys(S.next).map(Number);
      const reach = new Set(chain(S.first, S.next));
      const items = [{ id: 'L', x: inp.pos.L, y: ROW, name: 'list.firstNode', nameSide: 'below', nameColor: cIdx, color: cIdx }];
      ids.forEach((v) => {
        const p = inp.pos[v], x = Array.isArray(p) ? p[0] : p, y = Array.isArray(p) ? p[1] : ROW;
        const status = S.gone.includes(v) ? 'discarded' : reach.has(v) ? 'live' : 'unreached';
        items.push({ id: String(v), x, y, value: v, valueColor: cKey, status });
      });
      const N = F.ds.nodes(ctx, { items, cell: CELL, h: NH });

      /* the links, each swinging to its new target over the step that writes it */
      const firstLink = drawLinks(ctx, N, 'L', P.first === null ? null : String(P.first), S.first === null ? null : String(S.first), k, cIdx, 4, 1, 'null');
      if (firstLink) hits.push({ x: firstLink.mid.x, y: firstLink.mid.y, r: 22, name: `list.firstNode → ${S.first === null ? 'null' : S.first}` });
      ids.forEach((v) => {
        const was = P.next[v], now = S.next[v];
        const faded = S.gone.includes(v) ? 0.3 : 1;
        const lk = drawLinks(ctx, N, String(v), was === undefined ? undefined : was === null ? null : String(was), now === null ? null : String(now), k, PAL.ink, 3, faded, 'null');
        const B = N.at(String(v));
        hits.push({ x: B.valueX, y: B.y, r: 30, name: `the node holding ${v}${S.gone.includes(v) ? ', destroyed' : reach.has(v) ? '' : ', which no link from firstNode reaches'}` });
        if (lk) hits.push({ x: B.link.x, y: B.y, r: 18, name: `its next link → ${now === null ? 'null' : now}` });
      });

      /* the pointer variables at their nodes, in their referent colours; the walk's node slides along */
      const vNow = g.frame.vars, vWas = g.prev.vars;
      const at = (o) => (o && o.data !== undefined ? String(o.data) : null);
      const point = (name, color, id, wasId, side) => {
        if (!id) return;
        const B = N.at(id), A = wasId ? N.at(wasId) : B; if (!B) return;
        const x = lerp(A.valueX, B.valueX, wasId && wasId !== id ? k : 1);
        const up = side === 'above', edge = up ? B.t - 8 : B.b + 8, tail = up ? edge - 34 : edge + 34;
        arrow(ctx, x, tail, x, edge, color, 4);
        text(ctx, name, x, up ? tail - 18 : tail + 18, color, { size: 24, weight: 600, align: 'center' });
        hits.push({ x, y: up ? tail - 18 : tail + 18, r: 26, name: `${name} → the node holding ${id}` });
      };
      point('node', F.ref('node'), at(vNow.node), at(vWas.node), 'below');
      point('obsoleteNode', F.ref('obsolete-node'), at(vNow.obsoleteNode), at(vWas.obsoleteNode), 'below');
      point('newNode', F.ref('new-node'), at(vNow.newNode), at(vWas.newNode), 'above');

      /* the invariant and the counts: the chain from firstNode, links followed and written, against n */
      const n = chain(S.first, S.next).length;
      const ch = chain(S.first, S.next).join(' → ');
      text(ctx, `from list.firstNode: ${ch ? ch + ' → ' : ''}null`, 70, 470, PAL.muted, { size: 20, align: 'left' });
      const counts = `links followed ${S.hops} · links written ${S.writes}`;
      text(ctx, counts, 1330 - 120, 470, cCost, { size: 22, weight: 600, align: 'right' });
      text(ctx, `n = ${n}`, 1330, 470, cSize, { size: 22, weight: 600, align: 'right' });
      tip.hits = hits;
    },
  });
})();

/* ================================================================ sim-sorted-insert */
(function () {
  /* Wikipedia's listing, verbatim (Pointer (computer programming), #Multiple indirection) */
  const SRC = [
    '// Given a sorted list at *head, insert the element item at the first',
    '// location where all earlier elements have lesser or equal value.',
    'void insert(LinkedList **head, LinkedList *item) {',
    '    // p points to a pointer to an element',
    '    LinkedList **p = head;',
    '    while (*p && (*p)->value < item->value) {',
    '        p = &(*p)->next;',
    '    }',
    '    item->next = *p;',
    '    *p = item;',
    '}',
    '',
    '// Caller does this:',
    'insert(&head, item);',
  ].join('\n');
  const LIST = [1, 5, 7, 9];
  const XS = { head: 150, 1: 380, 5: 600, 7: 820, 9: 1040 };
  /* the item sits above the gap it will close */
  const INPUTS = [
    { value: '6', label: 'insert 6', item: 6, x: 710, head: '6 goes in between 5 and 7: the loop stops at the link that leads to 7.' },
    { value: '0', label: 'insert 0, a new head', item: 0, x: 265, head: '0 is smaller than the head, so p never moves, and *p = item changes the caller’s head.' },
    { value: '10', label: 'insert 10, past the end', item: 10, x: 1240, head: '10 is larger than every value, so p walks to the last next field, which is null.' },
    { value: '5', label: 'insert 5, equal', item: 5, x: 490, head: '5 goes in before the 5 already there: the loop stops at the first value that is not smaller.' },
  ];
  /* a link field is named by the node that owns it ('head' for the caller's pointer) */
  const run = (inp) => F.trace((at) => {
    const next = { head: LIST[0] }; LIST.forEach((v, j) => { next[v] = j + 1 < LIST.length ? LIST[j + 1] : null; });
    const IT = 'item';
    next[IT] = null;
    let p = 'head', hops = 0;
    const item = () => ({ value: inp.item, next: next[IT] });
    const S = () => ({ p, next: Object.assign({}, next), hops });
    at(5, { item: item(), S: S() });
    for (;;) {
      const node = next[p];
      const go = node !== null && node < inp.item;
      at(6, { item: item(), S: S() }, ['test', go]);
      if (!go) break;
      p = String(node); hops += 1; at(7, { item: item(), S: S() }, ['hop', p]);
    }
    next[IT] = next[p]; at(9, { item: item(), S: S() }, ['link', 'item']);
    next[p] = IT; at(10, { item: item(), S: S() }, ['link', p]);
    at(14, { item: item(), S: S() });
  });
  const traces = Object.fromEntries(INPUTS.map((inp) => [inp.value, run(inp)]));

  const d = sim('sim-sorted-insert', 520);
  const code = F.code(d, {
    src: { cpp: SRC }, canonical: 'cpp',
    blocks: [
      { id: 'insert', lines: [3, 11], label: 'insert item into the sorted list', touches: ['p', 'item'] },
      { id: 'start', lines: [5, 5], label: 'p points at the caller’s head', touches: ['p', 'head'] },
      { id: 'walk', lines: [6, 8], label: 'while *p leads to a smaller value, move p to that node’s next', touches: ['p'] },
      { id: 'splice', lines: [9, 10], label: 'link item in where *p pointed', touches: ['item', 'p'] },
      { id: 'aim', lines: [9, 9], label: 'item takes the node *p leads to', touches: ['item'] },
      { id: 'set', lines: [10, 10], label: '*p now leads to item', touches: ['p'] },
    ],
    refs: { p: () => F.ref('p'), item: () => F.ref('item'), head: () => F.ref('head') },
  });

  const tip = { hits: [] };
  F.hover(d.stage, () => tip.hits, d.c);

  F.debug(d, {
    code, level: 1, watch: ['item'],
    inputs: INPUTS.map((inp) => ({ value: inp.value, label: inp.label, trace: traces[inp.value] })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const inp = INPUTS.find((x) => x.value === g.input) || INPUTS[0];
      const S = g.frame.vars.S, P = g.prev.vars.S || S, k = g.k;
      const cP = F.ref('p'), cItem = F.ref('item'), cHead = F.ref('head'), cIdx = C('index'), cKey = C('key'), cCost = C('cost'), cSize = C('size');
      const hits = [];
      topline(ctx, inp.head);

      /* the nodes the walk has passed hold values less than item's: the invariant, tinted */
      const order = chain(S.next.head, S.next);
      const upto = S.p === 'head' ? [] : order.slice(0, order.findIndex((v) => String(v) === S.p) + 1).filter((v) => v !== 'item');

      const items = [{ id: 'head', x: XS.head, y: ROW, name: 'head', nameSide: 'below', nameColor: cHead, color: cHead }];
      LIST.forEach((v) => items.push({ id: String(v), x: XS[v], y: ROW, value: v, valueColor: cKey }));
      const linked = order.includes('item');
      items.push({ id: 'item', x: inp.x, y: 175, value: inp.item, valueColor: cKey, color: cItem, status: linked ? 'live' : 'unreached' });
      /* the tint goes under the nodes, so draw it first with the same layout */
      const pre = F.ds.layout(items, CELL, NH);
      if (upto.length) {
        const A = pre.at(String(upto[0])), B = pre.at(String(upto[upto.length - 1]));
        ctx.save(); ctx.fillStyle = alpha(cIdx, 0.12); ctx.fillRect(A.l - 14, A.t - 14, B.r - A.l + 28, NH + 28); ctx.restore();
        text(ctx, `every value here < ${inp.item}`, (A.l + B.r) / 2, A.t - 30, cIdx, { size: 18, align: 'center' });
      }
      const N = F.ds.nodes(ctx, { items, cell: CELL, h: NH });

      /* the links; the one *p is drawn in p's colour, heavier */
      const sid = (v) => (v === null || v === undefined ? null : String(v));
      ['head', ...LIST.map(String), 'item'].forEach((id) => {
        const now = S.next[id], was = P.next[id];
        if (id === 'item' && now === null && !order.includes('item')) return;   /* an item not yet linked has no link to draw */
        const isP = id === S.p;
        const lk = drawLinks(ctx, N, id, sid(was), sid(now), k, isP ? cP : id === 'head' ? cHead : PAL.ink, isP ? 5 : 3, 1, 'NULL');
        if (lk) hits.push({ x: lk.mid.x, y: lk.mid.y, r: 20, name: `${id === 'head' ? 'head' : id === 'item' ? 'item->next' : `the next field of ${id}`} → ${now === null ? 'NULL' : now === 'item' ? 'item' : now}${isP ? ' (this is *p)' : ''}` });
      });
      LIST.forEach((v) => { const B = N.at(String(v)); hits.push({ x: B.valueX, y: B.y, r: 30, name: `the element holding ${v}` }); });

      /* p: an arrow up to the link field it points at, sliding from field to field */
      const fieldX = (id) => N.at(id).link.x;
      const px = lerp(fieldX(P.p), fieldX(S.p), P.p === S.p ? 1 : k);
      const pb = ROW + NH / 2 + 8, ptail = pb + 40;
      arrow(ctx, px, ptail, px, pb, cP, 4);
      text(ctx, 'p', px, ptail + 20, cP, { size: 26, weight: 600, align: 'center' });
      hits.push({ x: px, y: ptail + 10, r: 24, name: `p → ${S.p === 'head' ? 'head' : `the next field of ${S.p}`}` });
      /* item: its own pointer, from above */
      const IB = N.at('item');
      arrow(ctx, IB.valueX, IB.t - 42, IB.valueX, IB.t - 8, cItem, 4);
      text(ctx, 'item', IB.valueX - 40, IB.t - 42, cItem, { size: 24, weight: 600, align: 'right' });
      hits.push({ x: IB.valueX, y: IB.y, r: 30, name: `item, holding ${inp.item}` });

      /* the invariant and the count */
      const target = S.next[S.p];
      text(ctx, `*p → ${target === null ? 'NULL' : target === 'item' ? 'item' : target}`, 70, 470, cP, { size: 22, weight: 600, align: 'left' });
      text(ctx, `links followed ${S.hops} ≤ n`, 1330 - 100, 470, cCost, { size: 22, weight: 600, align: 'right' });
      text(ctx, `n = ${LIST.length}`, 1330, 470, cSize, { size: 22, weight: 600, align: 'right' });
      tip.hits = hits;
    },
  });
})();
};
