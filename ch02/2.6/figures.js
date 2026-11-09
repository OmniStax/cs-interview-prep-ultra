/* 2.6 Doubly linked lists: two Sims over ODS's DLList.
   sim-dllist-ring, a still figure: the list a..e and its dummy linked into one cycle (ODS Figure 3.2), n on a slider
   down to the empty list. sim-dllist, a debugger: getNode(i) and then addBefore(w, x) or remove(w), stepped block by
   block beside ODS's code (its Python, ported where marked, its Java and C++ as ODS prints them, written between the
   generated markers below by inline_code.py; the JavaScript an AI translation, METHOD decision 20). The trace is the
   figure's own JS copy of the Python. Nodes are drawn as ODS draws them, three cells [prev | x | next], next
   references curving over the row and prev references under it; a node out of the cycle (u before it is linked in,
   w once it is unlinked) stands above the row. The library has no linked-list primitive yet (F.ds has strip,
   pointer, region and counts), so the nodes and references are drawn here with text, arrow heads and canvas paths. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['2.6'] = function (root, F) {
const { C, PAL, alpha, text, begin, tex, ctl, choice, register, topline, hover } = F;
const sim = (id, H) => F.sim(root, id, H);
const AI = 'claude-opus-5-5 high';
const LABEL = { 0: '', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 9: 'x' };
const CW = 44, CH = 58;                          /* a cell of a node; a node is three cells wide */
const lerp = (a, b, k) => a + (b - a) * k;
const lp = (p, q, k) => ({ x: lerp(p.x, q.x, k), y: lerp(p.y, q.y, k) });

/* ---------------------------------------------------------------- the list as a table of references
   L is [[id, prev, next], …]; id 0 is the dummy. */
const fresh = (n) => {
  const L = [[0, n ? n : 0, n ? 1 : 0]];
  for (let k = 1; k <= n; k += 1) L.push([k, k - 1, k < n ? k + 1 : 0]);
  return L;
};
const byId = (L) => new Map(L.map((e) => [e[0], e]));
/* the nodes in the order next takes them from the dummy, the dummy first */
const chainOf = (L) => {
  const by = byId(L), out = [0];
  let c = by.get(0)[2], guard = 0;
  while (c !== 0 && c != null && guard < 20) { out.push(c); c = by.get(c)[2]; guard += 1; }
  return out;
};

/* where each node stands: the cycle in a row from the dummy, a node out of it above the gap it belongs to */
function layout(L, vars, row, lift) {
  const by = byId(L), chain = chainOf(L), m = chain.length, sp = m > 6 ? 150 : 168;
  const x0 = 700 - ((m - 1) * sp) / 2, pos = new Map();
  chain.forEach((id, s) => pos.set(id, { x: x0 + s * sp, y: row, slot: s }));
  /* the gap before w; before the dummy, that is after the last node of the cycle */
  const gapBefore = (w) => (w === 0 ? pos.get(chain[m - 1]).x + sp / 2 : pos.get(w).x - sp / 2);
  L.forEach((e) => {
    if (pos.has(e[0])) return;
    const nx = e[2], w = nx != null && pos.has(nx) ? nx : vars.w;
    const x = w != null && pos.has(w) ? gapBefore(w) : x0 + m * sp;
    pos.set(e[0], { x, y: row - lift, float: true });
  });
  return { pos, chain, sp };
}

/* the curve of one reference: next leaves the right cell's dot and comes down into the top of the node it names,
   prev leaves the left cell's dot and comes up into its bottom; between nodes at different heights it runs
   straight across */
function geom(src, dst, field, top, bottom) {
  const sgn = field === 'next' ? 1 : -1, s = { x: src.x + sgn * CW, y: src.y };
  if (Math.abs(dst.y - src.y) < 20) {
    const self = Math.abs(dst.x - src.x) < 1;
    const t = { x: dst.x + (field === 'next' ? -6 : 6), y: dst.y - sgn * CH / 2 };
    const lift = Math.min(field === 'next' ? s.y - CH / 2 - top : bottom - s.y - CH / 2, 55 + 0.17 * Math.abs(t.x - s.x));
    const yy = s.y - sgn * (CH / 2 + (self ? 70 : lift));
    return [s, { x: s.x + sgn * (self ? 70 : 50), y: yy }, { x: t.x + (self ? sgn * 30 : 0), y: yy }, t];
  }
  const down = dst.y > src.y, t = { x: dst.x + sgn * -6, y: dst.y + (down ? -CH / 2 : CH / 2) };
  return [s, { x: s.x + sgn * 50, y: s.y }, { x: t.x, y: t.y + (down ? -70 : 70) }, t];
}
const bez = (P, t) => {
  const u = 1 - t;
  return { x: u * u * u * P[0].x + 3 * u * u * t * P[1].x + 3 * u * t * t * P[2].x + t * t * t * P[3].x,
           y: u * u * u * P[0].y + 3 * u * u * t * P[1].y + 3 * u * t * t * P[2].y + t * t * t * P[3].y };
};
function curveArrow(ctx, P, color, w) {
  ctx.save(); ctx.strokeStyle = color; ctx.fillStyle = color; ctx.lineWidth = w; ctx.lineCap = 'round';
  const end = P[3], before = bez(P, 0.94), a = Math.atan2(end.y - before.y, end.x - before.x), hl = 16 + w;
  const stop = { x: end.x - hl * 0.6 * Math.cos(a), y: end.y - hl * 0.6 * Math.sin(a) };
  ctx.beginPath(); ctx.moveTo(P[0].x, P[0].y); ctx.bezierCurveTo(P[1].x, P[1].y, P[2].x, P[2].y, stop.x, stop.y); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(end.x, end.y);
  ctx.lineTo(end.x - hl * Math.cos(a - 0.42), end.y - hl * Math.sin(a - 0.42));
  ctx.lineTo(end.x - hl * Math.cos(a + 0.42), end.y - hl * Math.sin(a + 0.42)); ctx.closePath(); ctx.fill();
  ctx.beginPath(); ctx.arc(P[0].x, P[0].y, 6, 0, 2 * Math.PI); ctx.fill();
  ctx.restore();
}
function nodeBox(ctx, p, o) {
  ctx.save();
  ctx.globalAlpha = o.faded ? 0.45 : 1;
  if (o.fill) { ctx.fillStyle = o.fill; ctx.fillRect(p.x - 1.5 * CW, p.y - CH / 2, 3 * CW, CH); }
  ctx.strokeStyle = PAL.ink; ctx.lineWidth = 3;
  if (o.dash) ctx.setLineDash([8, 6]);
  for (let c = -1; c <= 1; c += 1) ctx.strokeRect(p.x + c * CW - CW / 2, p.y - CH / 2, CW, CH);
  ctx.restore();
  if (o.label) text(ctx, o.label, p.x, p.y + 2, o.faded ? alpha(C('key'), 0.5) : C('key'), { size: 32, weight: 600, align: 'center', base: 'middle' });
}

/* one drawing of the list: nodes, references (eased from one state to the next), labels */
function drawList(ctx, A, B, k, o) {
  const top = o.top, bottom = o.bottom;
  const GA = new Map(), GB = new Map();
  const refs = (S, G) => S.L.forEach((e) => {
    [['prev', e[1]], ['next', e[2]]].forEach(([f, t]) => {
      if (t == null || !S.lay.pos.has(t)) return;
      G.set(`${e[0]}.${f}`, { P: geom(S.lay.pos.get(e[0]), S.lay.pos.get(t), f, top, bottom), to: t });
    });
  });
  refs(A, GA); refs(B, GB);
  const posOf = (id) => {
    const a = A.lay.pos.get(id), b = B.lay.pos.get(id);
    return a && b ? lp(a, b, k) : (b || a);
  };
  /* walk shading first, under everything */
  (o.shade || []).forEach((id) => { const p = posOf(id); if (p) nodeBox(ctx, p, { fill: alpha(C('index'), 0.16) }); });
  const ink = alpha(PAL.ink, 0.8), hot = C('index');
  const keys = new Set([...GA.keys(), ...GB.keys()]);
  keys.forEach((key) => {
    const a = GA.get(key), b = GB.get(key), changed = !a || !b || a.to !== b.to;
    const faded = o.isFaded && o.isFaded(+key.split('.')[0]);
    const col = changed ? hot : faded ? alpha(PAL.ink, 0.35) : ink, w = changed ? 5 : 3;
    if (a && b) curveArrow(ctx, a.P.map((p, j) => lp(p, b.P[j], k)), col, w);
    else if (b) { ctx.save(); ctx.globalAlpha = k; curveArrow(ctx, b.P, col, w); ctx.restore(); }
    else { ctx.save(); ctx.globalAlpha = 1 - k; curveArrow(ctx, a.P, col, w); ctx.restore(); }
  });
  /* the nodes, over their references' tails */
  const ids = new Set([...A.L.map((e) => e[0]), ...B.L.map((e) => e[0])]);
  ids.forEach((id) => {
    const p = posOf(id), isNew = !A.lay.pos.has(id), inB = B.lay.pos.has(id);
    const fl = B.lay.pos.get(id)?.float;
    ctx.save(); ctx.globalAlpha = isNew ? k : !inB ? 1 - k : 1;
    nodeBox(ctx, p, { label: LABEL[id], dash: fl && !(o.isFaded && o.isFaded(id)), faded: o.isFaded && o.isFaded(id),
      fill: id === 0 ? alpha(PAL.ink, 0.06) : null });
    ctx.restore();
    /* the dots of the cells that hold a reference */
    const e = (inB ? B : A).L.find((r) => r[0] === id);
    ctx.save(); ctx.fillStyle = PAL.ink;
    if (e && e[1] != null) { ctx.beginPath(); ctx.arc(p.x - CW, p.y, 6, 0, 2 * Math.PI); ctx.fill(); }
    if (e && e[2] != null) { ctx.beginPath(); ctx.arc(p.x + CW, p.y, 6, 0, 2 * Math.PI); ctx.fill(); }
    ctx.restore();
  });
  /* the kind of each reference, named once: on the first element's next and prev */
  const rk = GB.get(`${o.repFrom}.next`), rp = GB.get(`${o.repFrom}.prev`);
  if (rk && o.repFrom !== 0) { const m = bez(rk.P, 0.5); text(ctx, 'next', m.x, m.y - 18, PAL.muted, { size: 24, align: 'center', bg: PAL.panel }); }
  if (rp && o.repFrom !== 0) { const m = bez(rp.P, 0.5); text(ctx, 'prev', m.x, m.y + 22, PAL.muted, { size: 24, align: 'center', bg: PAL.panel }); }
  return posOf;
}

/* ================================================================ sim-dllist-ring: the cycle, n elements and the dummy */
(function () {
  const d = sim('sim-dllist-ring', 520);
  const sn = ctl(d.controls, { label: 'n', cls: 'size', key: 'n', min: 0, max: 6, step: 1, value: 5, unit: '', dec: 0,
    detents: [{ v: 5, label: 'a–e' }], specials: [{ at: 0, label: 'empty' }] });
  const ROW = 270, TOP = 96, BOTTOM = 500;
  let hits = [];
  hover(d.stage, () => hits);
  function draw() {
    const { ctx } = begin(d.c);
    const n = Math.round(sn.v), L = fresh(n), lay = layout(L, {}, ROW, 0), S = { L, lay };
    const last = n ? LABEL[n] : null;
    if (n === 0) topline(ctx, 'With no elements, the dummy’s next and prev are the dummy itself.');
    else if (n === 1) topline(ctx, 'With one element, the dummy follows a and precedes it: a’s next and prev are both the dummy.');
    else topline(ctx, `With n = ${n}, the dummy follows ${last} and precedes a: every node has a next and a prev.`);
    const posOf = drawList(ctx, S, S, 1, { top: TOP, bottom: BOTTOM, repFrom: n ? 1 : 0 });
    hits = [];
    lay.chain.forEach((id, s) => {
      const p = posOf(id);
      if (id === 0) text(ctx, 'dummy', p.x, p.y + 56, F.ref('dummy'), { size: 28, weight: 600, align: 'center', bg: PAL.panel });
      else text(ctx, String(s - 1), p.x, p.y + 52, C('index'), { size: 24, align: 'center', bg: PAL.panel });
      hits.push({ x: p.x, y: p.y, r: 66, name: id === 0 ? 'the dummy node, which holds no data' : `node ${s - 1}, holding ${LABEL[id]}` });
    });
    const nm = (id) => (id === 0 ? '\\text{dummy}' : `\\text{${LABEL[id]}}`);
    const by = byId(L).get(0);
    tex(d.readout, `\\htmlData{ref=dummy}{\\text{dummy}}\\text{.next} = ${nm(by[2])} \\\\ \\htmlData{ref=dummy}{\\text{dummy}}\\text{.prev} = ${nm(by[1])}`);
  }
  register(d.fig, { update: () => {}, draw });
})();

/* ================================================================ sim-dllist: getNode, then addBefore or remove */
(function () {
  /* BEGIN generated by inline_code.py: ODS's getNode(i), addBefore(w,x) and remove(w) */
  const ODS_PYTHON = "def get_node(self, i):\n    if i < self.n//2:\n        p = self.dummy.next\n        for _ in range(i):\n            p = p.next\n    else:\n        p = self.dummy\n        for _ in range(self.n, i, -1):\n            p = p.prev\n    return p\n\ndef add_before(self, w, x):\n    u = DLList.Node(x)\n    u.prev = w.prev\n    u.next = w\n    u.next.prev = u\n    u.prev.next = u\n    self.n += 1\n    return u\n\ndef _remove(self, w):\n    w.prev.next = w.next\n    w.next.prev = w.prev\n    self.n -= 1";
  const ODS_JAVA = "Node getNode(int i) {\n    Node p = null;\n    if (i < n / 2) {\n        p = dummy.next;\n        for (int j = 0; j < i; j++)\n            p = p.next;\n    } else {\n        p = dummy;\n        for (int j = n; j > i; j--)\n            p = p.prev;\n    }\n    return p;\n}\n\nNode addBefore(Node w, T x) {\n    Node u = new Node();\n    u.x = x;\n    u.prev = w.prev;\n    u.next = w;\n    u.next.prev = u;\n    u.prev.next = u;\n    n++;\n    return u;\n}\n\nvoid remove(Node w) {\n    w.prev.next = w.next;\n    w.next.prev = w.prev;\n    n--;\n}";
  const ODS_CPP = "DLList<T>::Node* DLList<T>::getNode(int i) {\n    Node* p;\n    if (i < n / 2) {\n        p = dummy.next;\n        for (int j = 0; j < i; j++)\n            p = p->next;\n    } else {\n        p = &dummy;\n        for (int j = n; j > i; j--)\n            p = p->prev;\n    }\n    return (p);\n}\n\nDLList<T>::Node* DLList<T>::addBefore(Node *w, T x) {\n    Node *u = new Node;\n    u->x = x;\n    u->prev = w->prev;\n    u->next = w;\n    u->next->prev = u;\n    u->prev->next = u;\n    n++;\n    return u;\n}\n\nvoid DLList<T>::remove(Node *w) {\n    w->prev->next = w->next;\n    w->next->prev = w->prev;\n    delete w;\n    n--;\n}";
  const ODS_JAVASCRIPT = "getNode(i) {\n  let p = null;\n  if (i < Math.floor(this.n / 2)) {\n    p = this.dummy.next;\n    for (let j = 0; j < i; j++)\n      p = p.next;\n  } else {\n    p = this.dummy;\n    for (let j = this.n; j > i; j--)\n      p = p.prev;\n  }\n  return p;\n}\n\naddBefore(w, x) {\n  const u = new Node();\n  u.x = x;\n  u.prev = w.prev;\n  u.next = w;\n  u.next.prev = u;\n  u.prev.next = u;\n  this.n++;\n  return u;\n}\n\n_remove(w) {\n  w.prev.next = w.next;\n  w.next.prev = w.prev;\n  this.n--;\n}";
  /* END generated */
  /* The trace numbers the Python panel's lines: get_node 1–10, add_before 12–19, _remove 21–24. Java, C++ and
     JavaScript map line for line (their getNode has a declaration line and closing braces of its own). */
  const MAP_J = { 1: 1, 2: 3, 3: 4, 4: 5, 5: 6, 7: 8, 8: 9, 9: 10, 10: 12, 12: 15, 13: [16, 17], 14: 18, 15: 19, 16: 20, 17: 21,
    18: 22, 19: 23, 21: 26, 22: 27, 23: 28, 24: 29 };
  const MAP_C = Object.assign({}, MAP_J, { 24: [29, 30] });
  const span = (py, j, c) => ({ python: py, java: j, cpp: c || j, javascript: j });
  const run = (op, n, i) => F.trace((at) => {
    const L = fresh(n), by = byId(L);
    const snap = () => L.map((e) => e.slice());
    let steps = 0, p = null, w = null, u = null;
    const seen = [];
    const V = (extra) => Object.assign({ i, n, steps, p, w, u, seen: seen.slice(), L: snap(), op }, extra || {});
    at(1, V(), ['call']);
    const half = Math.floor(n / 2);
    if (i < half) {
      at(2, V(), ['compare', true]);
      p = by.get(0)[2]; seen.push(p); at(3, V());
      for (let k = 0; k < i; k += 1) { at(4, V()); p = by.get(p)[2]; steps += 1; seen.push(p); at(5, V(), ['hop', p]); }
    } else {
      at(2, V(), ['compare', false]);
      p = 0; seen.push(p); at(7, V());
      for (let j = n; j > i; j -= 1) { at(8, V()); p = by.get(p)[1]; steps += 1; seen.push(p); at(9, V(), ['hop', p]); }
    }
    at(10, V(), ['return', p]);
    w = p;
    if (op === 'add') {
      at(12, V(), ['call']);
      const nu = [9, null, null]; L.push(nu); by.set(9, nu); u = 9; at(13, V());
      nu[1] = by.get(w)[1]; at(14, V());
      nu[2] = w; at(15, V());
      by.get(nu[2])[1] = u; at(16, V());
      by.get(nu[1])[2] = u; at(17, V());
      n += 1; at(18, V());
      at(19, V(), ['return', u]);
    } else {
      at(21, V(), ['call']);
      const e = by.get(w);
      by.get(e[1])[2] = e[2]; at(22, V());
      by.get(e[2])[1] = e[1]; at(23, V());
      n -= 1; at(24, V());
    }
  });

  const d = sim('sim-dllist', 760);
  const code = F.code(d, {
    src: { python: ODS_PYTHON, java: ODS_JAVA, cpp: ODS_CPP, javascript: ODS_JAVASCRIPT },
    ai: { python: AI, javascript: AI },
    lineMap: { java: MAP_J, cpp: MAP_C, javascript: MAP_J },
    blocks: [
      { id: 'find', lines: span([1, 10], [1, 13]), label: 'find node i', touches: ['p', 'i'] },
      { id: 'fwd', lines: span([3, 5], [4, 6]), label: 'walk forward from dummy.next', touches: ['p', 'steps'] },
      { id: 'hop', lines: span([5, 5], [6, 6]), label: 'one step forward', touches: ['p', 'steps'] },
      { id: 'back', lines: span([7, 9], [8, 10]), label: 'walk back from the dummy', touches: ['p', 'steps'] },
      { id: 'hopb', lines: span([9, 9], [10, 10]), label: 'one step back', touches: ['p', 'steps'] },
      { id: 'link', lines: span([12, 19], [15, 24]), label: 'link u in before w', touches: ['u', 'w', 'n'] },
      { id: 'make', lines: span([13, 15], [16, 19]), label: 'make u and point it at w.prev and w', touches: ['u'] },
      { id: 'splice', lines: span([16, 17], [20, 21]), label: 'point both neighbours at u', touches: ['u', 'w'] },
      { id: 'unlink', lines: span([21, 24], [26, 30], [26, 31]), label: 'unlink w: its neighbours skip over it', touches: ['w', 'n'] },
      { id: 'skipn', lines: span([22, 22], [27, 27]), label: 'w.prev skips forward to w.next', touches: ['w'] },
      { id: 'skipp', lines: span([23, 23], [28, 28]), label: 'w.next skips back to w.prev', touches: ['w'] },
    ],
    refs: {
      python: { p: () => F.ref('p'), w: () => F.ref('w'), u: () => F.ref('u'), i: () => F.ref('i'), 'self.dummy': () => F.ref('dummy') },
      java: { p: () => F.ref('p'), w: () => F.ref('w'), u: () => F.ref('u'), i: () => F.ref('i'), dummy: () => F.ref('dummy') },
      cpp: { p: () => F.ref('p'), w: () => F.ref('w'), u: () => F.ref('u'), i: () => F.ref('i'), dummy: () => F.ref('dummy') },
      javascript: { p: () => F.ref('p'), w: () => F.ref('w'), u: () => F.ref('u'), i: () => F.ref('i'), 'self.dummy': () => F.ref('dummy') },
    },
  });

  let dbg = null;
  const op = choice(d.controls, { label: '\\text{operation}', key: 'op', value: 'add',
    options: [{ value: 'add', label: 'add(i, x)' }, { value: 'remove', label: 'remove(i)' }], onInput: () => rebuild() });
  const sn = ctl(d.controls, { label: 'n', cls: 'size', key: 'n', min: 0, max: 6, step: 1, value: 5, unit: '', dec: 0,
    detents: [{ v: 5, label: 'a–e' }], specials: [{ at: 0, label: 'empty' }], onInput: () => rebuild() });
  const si = ctl(d.controls, { label: 'i', cls: 'index', key: 'i', min: 0, max: 5, step: 1, value: 2, unit: '', dec: 0,
    specials: [{ at: 0, label: 'front' }, { at: () => Math.round(sn.v) - (op.value === 'remove' ? 1 : 0), label: 'end' },
      { at: () => Math.floor(Math.round(sn.v) / 2), label: 'slowest' }], onInput: () => rebuild() });
  /* add takes i from 0 to n, remove from 0 to n − 1 and needs a list of at least one */
  let want = { n: 5, i: 2, op: 'add' };
  function rebuild() {
    const isAdd = op.value === 'add';
    let n = Math.round(sn.v);
    if (!isAdd && n < 1) { n = 1; sn.set(1); }
    const hi = isAdd ? n : n - 1, i = Math.max(0, Math.min(hi, Math.round(si.v)));
    if (hi !== want.hi) si.range({ min: 0, max: Math.max(hi, 1), step: 1, value: i });
    else if (i !== Math.round(si.v)) si.set(i);
    want = { n, i, op: op.value, hi };
    if (dbg) dbg.set(run(op.value, n, i));
  }
  want.hi = 5;

  let hits = [];
  hover(d.stage, () => hits);
  const ROW = 400, LIFT = 190, TOP = 110, BOTTOM = 650;
  const said = (id) => (id === 0 ? 'the dummy' : LABEL[id]);
  function headline(f, v) {
    const n0 = v.op === 'add' ? v.n - (f.line >= 18 ? 1 : 0) : v.n + (f.line >= 24 ? 1 : 0);
    const half = Math.floor(n0 / 2), ev = f.ev || [];
    switch (f.line) {
      case 1: return `${v.op}(${v.i}${v.op === 'add' ? ', x' : ''}) first calls getNode(${v.i}) on a list of ${n0}.`;
      case 2: return ev[1] ? `i = ${v.i} is less than ⌊n/2⌋ = ${half}, so p starts from the front.`
        : `i = ${v.i} is not less than ⌊n/2⌋ = ${half}, so p starts from the back.`;
      case 3: return `p starts at dummy.next, the node at index 0.`;
      case 4: case 5: return `p steps forward to index ${v.steps}.`;
      case 7: return `p starts at the dummy, one place past index ${n0 - 1}.`;
      case 8: case 9: return `p steps back to index ${n0 - v.steps}.`;
      case 10: return v.p === 0 ? `getNode returns the dummy itself: index ${v.i} is one past the last node.`
        : `getNode returns p, the node at index ${v.i}, after ${v.steps} step${v.steps === 1 ? '' : 's'}.`;
      case 12: return `addBefore(w, x) with w = ${said(v.w)}.`;
      case 13: return 'A new node u holds x; its prev and next are still empty.';
      case 14: { const pv = byId(v.L).get(9)[1]; return `u.prev = w.prev, which is ${said(pv)}${pv === 0 && v.w === 0 ? ': the list was empty' : ''}.`; }
      case 15: return `u.next = w, which is ${said(v.w)}.`;
      case 16: return `${v.w === 0 ? 'The dummy’s' : `${said(v.w)}’s`} prev now points back at u.`;
      case 17: { const pv = byId(v.L).get(9)[1]; return `${pv === 0 ? 'The dummy’s' : `${said(pv)}’s`} next now points at u: u is in the list.`; }
      case 18: case 19: return `n is now ${v.n}, and every node again has a next and a prev.`;
      case 21: return `remove(w) with w = ${said(v.w)}, the node at index ${v.i}.`;
      case 22: { const e = byId(v.L).get(v.w); return `${e[1] === 0 ? 'The dummy’s' : `${said(e[1])}’s`} next skips over w to ${said(e[2])}.`; }
      case 23: { const e = byId(v.L).get(v.w); return `${e[2] === 0 ? 'The dummy’s' : `${said(e[2])}’s`} prev skips back over w to ${said(e[1])}: w is out of the list.`; }
      case 24: return `n is now ${v.n}${v.n === 0 ? ': only the dummy is left, linked to itself' : ''}.`;
      default: return '';
    }
  }

  dbg = F.debug(d, {
    code, trace: run('add', 5, 2), watch: ['i', 'n', 'steps'],
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const f = g.frame, v = f.vars, pv = g.prev.vars;
      topline(ctx, headline(f, v));
      const A = { L: pv.L, lay: layout(pv.L, pv, ROW, LIFT) }, B = { L: v.L, lay: layout(v.L, v, ROW, LIFT) };
      const out = (S, id) => S.lay.pos.get(id)?.float && S.L.find((e) => e[0] === id && e[1] != null && e[2] != null);
      const finding = f.line <= 10;
      const chainB = B.lay.chain;
      const posOf = drawList(ctx, A, B, g.k, {
        top: TOP, bottom: BOTTOM, repFrom: chainB.length > 1 ? chainB[1] : 0,
        shade: finding ? v.seen : [],
        isFaded: (id) => v.op === 'remove' && id === v.w && !!out(B, id),
      });
      /* labels under the row: indices of the nodes in the cycle, the dummy's name */
      hits = [];
      const n0 = v.op === 'add' ? v.n - (f.line >= 18 ? 1 : 0) : v.n + (f.line >= 24 ? 1 : 0);
      chainB.forEach((id, s) => {
        const p = posOf(id), idx = s - 1;
        if (id === 0) text(ctx, 'dummy', p.x, p.y + 52, F.ref('dummy'), { size: 28, weight: 600, align: 'center', bg: PAL.panel });
        else {
          const isI = finding && idx === v.i;
          text(ctx, isI ? `i = ${idx}` : String(idx), p.x, p.y + 52, isI ? F.ref('i') : C('index'), { size: isI ? 28 : 26, weight: isI ? 600 : 400, align: 'center', bg: PAL.panel });
        }
        hits.push({ x: p.x, y: p.y, r: 66, name: id === 0 ? 'the dummy node, which holds no data' : `node ${idx}, holding ${LABEL[id]}` });
      });
      B.lay.pos.forEach((p, id) => { if (p.float) hits.push({ x: posOf(id).x, y: posOf(id).y, r: 66, name: id === 9 ? 'u, the new node holding x' : `w, the node removed, holding ${LABEL[id]}` }); });
      /* the pointer variables at their nodes: under the row, or over a node that stands above it */
      const tags = [];
      const tag = (name, id, from) => {
        if (id == null) return;
        const to = B.lay.pos.get(id), fr = from != null ? A.lay.pos.get(from) : null;
        tags.push({ name, id, at: fr ? lp(fr, to, g.k) : posOf(id), up: !!to.float });
      };
      if (finding) tag('p', v.p, pv.p);
      else { tag('w', v.w, v.w); if (v.u != null) tag('u', v.u, v.u); }
      tags.forEach((t, j) => {
        const same = tags.filter((s) => s.id === t.id), off = same.length > 1 ? (same.indexOf(t) - (same.length - 1) / 2) * 44 : 0;
        const x = t.at.x + off, col = F.ref(t.name);
        if (t.up) { F.arrow(ctx, x, t.at.y - CH / 2 - 58, x, t.at.y - CH / 2 - 8, col, 4); text(ctx, t.name, x, t.at.y - CH / 2 - 76, col, { size: 32, weight: 600, align: 'center', bg: PAL.panel }); }
        else { F.arrow(ctx, x, t.at.y + CH / 2 + 104, x, t.at.y + CH / 2 + 44, col, 4); text(ctx, t.name, x, t.at.y + CH / 2 + 128, col, { size: 32, weight: 600, align: 'center', bg: PAL.panel }); }
      });
      /* the invariant of the walk and the cost against the bound */
      const yb = 712, bound = 1 + Math.min(v.i, n0 - v.i);
      const walk = v.i < Math.floor(n0 / 2) ? v.i : n0 - v.i;
      let inv;
      if (finding) {
        const at = v.p == null ? -1 : chainOf(v.L).indexOf(v.p);
        inv = f.line <= 2 ? `getNode(${v.i}) will follow ${walk} reference${walk === 1 ? '' : 's'} from the ${v.i < Math.floor(n0 / 2) ? 'front' : 'back'}`
          : at > 0 ? `p is the node at index ${at - 1}, ${v.steps} step${v.steps === 1 ? '' : 's'} from where it started`
            : `p is the dummy, ${v.steps} step${v.steps === 1 ? '' : 's'} from where it started`;
      } else {
        const by = byId(v.L), bad = chainOf(v.L).find((id) => by.get(by.get(id)[2])[1] !== id);
        inv = bad == null ? 'for every node in the cycle, next.prev is the node itself'
          : `half relinked: the node after ${said(bad)} does not yet point back to it`;
      }
      text(ctx, inv, 60, yb - 42, finding ? C('index') : PAL.ink, { size: 26 });
      text(ctx, `steps ${v.steps} ≤ 1 + min(i, n − i) = ${bound}`, 60, yb, C('cost'), { size: 28, weight: 600 });
      text(ctx, `n = ${v.n}`, 1340, yb, C('size'), { size: 28, weight: 600, align: 'right' });
    },
  });
})();
};
