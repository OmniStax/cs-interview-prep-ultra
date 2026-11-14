/* Figures for section 3.2 Queues and circular buffers. Boots against the section's text article.
   Two Sims.
   - sim-fifo-queue (moving, no code panel: the Queue interface is a property, the book's RULES' exception for an
     interface): ODS's Figure 1.1, values joining at one end and leaving at the other, one call per beat.
   - sim-arrayqueue (debugger, code beside the drawing, stepped by block: METHOD §2.3): ODS's ArrayQueue drawn as
     the ring modular arithmetic makes of a and as the array itself, j and the next write index
     (j + n) mod length(a) live in both, opening on the calls of ODS's own Figure 2.2. The code panel is ODS's
     add, remove and resize: Python (canonical, the trace's lines), Java and C++ as ODS's editions print them,
     written in below by ch03/3.2/inline_code.py from the source cache; JavaScript is the AI's translation of the
     Java and carries the AI mark. The trace is the figure's own JS copy of the Python: one frame per statement,
     and one per element resize() copies, so stepping into a resize goes copy by copy. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['3.2'] = function (root, F) {
const { C, PAL, alpha, text, arrow, line, begin, topline, measure, hbracket, tex, register, cycle } = F;
const sim = (id, H) => F.sim(root, id, H);
const AI = 'claude-opus-5-5 high';
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2, dash) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};
const lerp = (a, b, k) => a + (b - a) * k;
const ease = (k) => { const t = Math.max(0, Math.min(1, k)); return t * t * (3 - 2 * t); };
const SUBS = '₀₁₂₃₄₅₆₇₈₉';
const sub = (k) => String(k).split('').map((c) => SUBS[+c]).join('');
const num = (x) => String(x).replace('-', '−');   /* a minus sign, not a hyphen */

/* ================================================================ sim-fifo-queue: ODS's Figure 1.1 in motion */
(function () {
  const d = sim('sim-fifo-queue', 420);
  /* the calls, one per beat: three values join, then joins and removals interleave until the queue is empty */
  const OPS = [['add', 'a'], ['add', 'b'], ['add', 'c'], ['remove'], ['add', 'd'], ['remove'], ['add', 'e'], ['remove'],
    ['remove'], ['remove']];
  const T = OPS.length;
  const cy = cycle(() => T, 1.4);
  /* the queue after each call: q[s] is the queue once s calls are done (the front, the oldest, first) */
  const states = [[]];
  const out = [[]];
  OPS.forEach((o) => {
    const q = states[states.length - 1].slice(), r = out[out.length - 1].slice();
    if (o[0] === 'add') q.push(o[1]); else r.push(q.shift());
    states.push(q); out.push(r);
  });
  const SL = 118, XF = 1010, Y = 220, BOX = 84;
  /* slot i (0 the front) stands at XF − i·SL; a value added flies in from the add(x) side, a value removed leaves
     past the remove() side */
  const slotX = (i) => XF - i * SL;
  function draw() {
    const { ctx } = begin(d.c);
    const t = cy.now(), s = Math.min(T - 1, Math.floor(t)), k = ease(t - s), done = t >= T;
    const ck = C('key'), ink = PAL.ink, muted = PAL.muted;
    const step = done ? T - 1 : s, o = OPS[step], before = states[step], after = states[step + 1];
    const kk = done ? 1 : k;
    /* the line's frame: the slots the queue may hold, hollow */
    for (let i = 0; i < 6; i += 1) rect(ctx, slotX(i) - BOX / 2, Y - BOX / 2, BOX, BOX, null, alpha(ink, 0.25), 2, [6, 6]);
    text(ctx, 'add(x) / enqueue(x)', 150, Y + 128, ink, { size: 26, align: 'center', base: 'middle' });
    text(ctx, 'remove() / dequeue()', 1230, Y + 128, ink, { size: 26, align: 'center', base: 'middle' });
    /* the two ends, after ODS's figure: values come in from the add(x) side and leave on the remove() side */
    arrow(ctx, 250, Y + 100, slotX(5) - BOX / 2 - 14, Y + 10, alpha(ink, 0.45), 3);
    arrow(ctx, slotX(0) + BOX / 2 + 14, Y + 10, 1150, Y + 100, alpha(ink, 0.45), 3);
    text(ctx, 'front', slotX(0), Y - 78, muted, { size: 22, align: 'center', base: 'middle' });
    const qb = kk >= 0.5 ? after : before;
    if (qb.length > 1) text(ctx, 'back', slotX(qb.length - 1), Y - 78, muted, { size: 22, align: 'center', base: 'middle' });
    const cell = (v, x, y, a = 1) => {
      ctx.save(); ctx.globalAlpha *= a;
      rect(ctx, x - BOX / 2, y - BOX / 2, BOX, BOX, PAL.panel, ink, 3);
      text(ctx, v, x, y, ck, { size: 36, weight: 600, align: 'center', base: 'middle' });
      ctx.restore();
    };
    if (o[0] === 'add') {
      before.forEach((v, i) => cell(v, slotX(i), Y));
      const i = after.length - 1, x0 = 150, y0 = Y + 80;
      const x = lerp(x0, slotX(i), kk), y = lerp(y0, Y, kk);
      cell(o[1], x, y);
    } else {
      const v = before[0];
      before.slice(1).forEach((w, i) => cell(w, lerp(slotX(i + 1), slotX(i), kk), Y));
      const x = lerp(slotX(0), 1230, kk), y = lerp(Y, Y + 80, kk);
      cell(v, x, y, 1 - 0.6 * kk);
    }
    const head = o[0] === 'add'
      ? (before.length ? `add(${o[1]}) puts ${o[1]} at the back, behind ${before.length} value${before.length === 1 ? '' : 's'}.` : `add(${o[1]}) puts ${o[1]} into the empty queue, at its front.`)
      : `remove() returns ${before[0]}, the oldest value in the queue.`;
    topline(ctx, head);
    const ins = OPS.slice(0, step + 1).filter((p) => p[0] === 'add').map((p) => p[1]);
    const outs = out[step + 1];
    const keys = (xs) => xs.map((v) => `\\text{${v}}`).join(',\\ ');
    tex(d.readout, `\\text{added in the order } ${keys(ins)}` + `\\\\ \\text{removed in the order } ${outs.length ? keys(outs) : '\\text{(none yet)}'}`);
  }
  register(d.fig, { update: (dt) => cy.step(dt, () => 0.7), draw });
})();

/* ================================================================ sim-arrayqueue */
(function () {
  /* BEGIN ODS LISTINGS (ch03/3.2/inline_code.py) */
  const PY = "def add(self, x):\n    if self.n + 1 > len(self.a): self._resize()\n    self.a[(self.j+self.n) % len(self.a)] = x\n    self.n += 1\n    return True\n\ndef remove(self):\n    x = self.a[self.j]\n    self.j = (self.j + 1) % len(self.a)\n    self.n -= 1\n    if len(self.a) >= 3*self.n: self._resize()\n    return x\n\ndef _resize(self):\n    b = new_array(max(1, 2*self.n))\n    for k in range(self.n):\n        b[k] = self.a[(self.j+k) % len(self.a)]\n    self.a = b\n    self.j = 0";
  const JAVA = "boolean add(T x) {\n    if (n + 1 > a.length) resize();\n    a[(j+n) % a.length] = x;\n    n++;\n    return true;\n}\n\nT remove() {\n    if (n == 0) throw new NoSuchElementException();\n    T x = a[j];\n    j = (j + 1) % a.length;\n    n--;\n    if (a.length >= 3*n) resize();\n    return x;\n}\n\nvoid resize() {\n    T[] b = newArray(max(1,n*2));\n    for (int k = 0; k < n; k++)\n        b[k] = a[(j+k) % a.length];\n    a = b;\n    j = 0;\n}";
  const CPP = "bool add(T x) {\n    if (n + 1 > a.length) resize();\n    a[(j+n) % a.length] = x;\n    n++;\n    return true;\n}\n\nT remove() {\n    T x = a[j];\n    j = (j + 1) % a.length;\n    n--;\n    if (a.length >= 3*n) resize();\n    return x;\n}\n\nvoid resize() {\n    array<T> b(max(1, 2*n));\n    for (int k = 0; k < n; k++)\n        b[k] = a[(j+k)%a.length];\n    a = b;\n    j = 0;\n}";
  /* END ODS LISTINGS */
  /* JavaScript: the AI's translation of ODS's Java, line for line */
  const JS = [
    'add(x) {',
    '    if (this.n + 1 > this.a.length) this.resize();',
    '    this.a[(this.j+this.n) % this.a.length] = x;',
    '    this.n++;',
    '    return true;',
    '}',
    '',
    'remove() {',
    '    if (this.n === 0) throw new Error("no such element");',
    '    const x = this.a[this.j];',
    '    this.j = (this.j + 1) % this.a.length;',
    '    this.n--;',
    '    if (this.a.length >= 3*this.n) this.resize();',
    '    return x;',
    '}',
    '',
    'resize() {',
    '    const b = new Array(Math.max(1, this.n*2));',
    '    for (let k = 0; k < this.n; k++)',
    '        b[k] = this.a[(this.j+k) % this.a.length];',
    '    this.a = b;',
    '    this.j = 0;',
    '}',
  ].join('\n');
  /* Python line → the braced languages' lines (Java and JavaScript print remove()'s empty check, C++ does not) */
  const JAVA_MAP = { 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 7, 7: [8, 9], 8: 10, 9: 11, 10: 12, 11: 13, 12: 14, 14: 17, 15: 18, 16: 19, 17: 20, 18: 21, 19: 22 };
  const MAP = {
    java: JAVA_MAP, javascript: JAVA_MAP,
    cpp: { 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 14: 16, 15: 17, 16: 18, 17: 19, 18: 20, 19: 21 },
  };
  /* Python's lines: add 1–5, remove 7–12, _resize 14–19; 6 is the blank line the opening state rests on */
  const L = { start: 6, defAdd: 1, grow: 2, store: 3, count: 4, retAdd: 5, defRemove: 7, take: 8, step: 9, dec: 10, shrink: 11, ret: 12,
    defResize: 14, alloc: 15, loop: 16, copy: 17, setA: 18, setJ: 19 };

  /* The inputs. ODS's Figure 2.2 starts from a, b, c at a[2..4] in an array of length 6; the others are a stream that
     runs round a ring of 8 without resizing, a queue grown from empty that wraps before it resizes, and a queue
     drained from a wrapped ring of 8, shrinking as it goes. */
  const E = (len, at) => { const a = new Array(len).fill(null); Object.entries(at).forEach(([i, v]) => { a[+i] = v; }); return a; };
  const PRESETS = [
    { value: 'figure', label: 'Figure 2.2', a: E(6, { 2: 'a', 3: 'b', 4: 'c' }), j: 2, n: 3,
      ops: [['add', 'd'], ['add', 'e'], ['remove'], ['add', 'f'], ['add', 'g'], ['add', 'h'], ['remove']] },
    { value: 'wrap', label: 'wrap around', a: E(8, { 5: 'p', 6: 'q', 7: 'r' }), j: 5, n: 3,
      ops: ['s', 't', 'u', 'v', 'w'].flatMap((x) => [['add', x], ['remove']]) },
    { value: 'grow', label: 'grow from empty', a: E(1, {}), j: 0, n: 0,
      ops: [['add', 'a'], ['add', 'b'], ['add', 'c'], ['remove'], ['add', 'd'], ['add', 'e'], ['add', 'f'], ['add', 'g']] },
    { value: 'drain', label: 'drain', a: E(8, { 6: 'a', 7: 'b', 0: 'c', 1: 'd', 2: 'e', 3: 'f' }), j: 6, n: 6,
      ops: Array.from({ length: 6 }, () => ['remove']) },
  ];
  const callName = (o) => (o[0] === 'remove' ? 'remove()' : `add(${o[1]})`);

  /* One run of a preset as frames of the Python. Beside the code's own variables (x, j, n, len(a), k, a, b) each
     frame carries what the drawing reads: the call under way (c), the index just written or read (w), the copy
     just made (mv: [from, to]), and the running counts: calls (m), resizes (r), elements copied by resize()
     (copies, the sum of nᵢ), calls since the last resize (since), and one record per resize (log). */
  const run = (P) => F.trace((at) => {
    let a = P.a.slice(), j = P.j, n = P.n, b = null, k = null, x = null;
    let c = -1, m = 0, r = 0, copies = 0, since = 0, w = null;
    const log = [], stars = [];
    const snap = (extra) => Object.assign({ x, j, n, 'len(a)': a.length, k, a: a.slice(), c, m, r, copies, since, w,
      log: log.map((e) => ({ ...e })), stars: stars.slice() }, b ? { b: b.slice() } : {}, extra || {});
    const resize = () => {
      at.enter('_resize');
      at(L.defResize, snap());
      b = new Array(Math.max(1, 2 * n)).fill(null); at(L.alloc, snap());
      const ni = n;
      for (k = 0; k < n; k += 1) {
        at(L.loop, snap());
        const from = (j + k) % a.length;
        b[k] = a[from]; copies += 1;
        at(L.copy, snap({ mv: [from, k] }), ['copy', from, k]);
      }
      k = null;
      r += 1; log.push({ ni, since, call: callName(P.ops[c]) }); stars.push(c); since = 0;
      a = b; b = null; at(L.setA, snap({ swapped: true }));
      j = 0; at(L.setJ, snap());
      at.leave();
    };
    at(L.start, snap());
    P.ops.forEach((o, cc) => {
      c = cc; w = null; m += 1; since += 1;
      if (o[0] === 'add') {
        x = o[1];
        at(L.defAdd, snap());
        if (n + 1 > a.length) resize();
        at(L.grow, snap());
        w = (j + n) % a.length; a[w] = x;
        at(L.store, snap({ wrote: [j, n] }), ['put', w]);
        n += 1; at(L.count, snap());
        at(L.retAdd, snap());
      } else {
        x = null;
        at(L.defRemove, snap());
        w = j; x = a[j]; at(L.take, snap({ took: true }));
        const j0 = j; j = (j + 1) % a.length; at(L.step, snap({ stepped: j0 }));
        n -= 1; at(L.dec, snap());
        if (a.length >= 3 * n) resize();
        at(L.shrink, snap());
        at(L.ret, snap());
      }
    });
  });

  const d = sim('sim-arrayqueue', 970);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: { javascript: AI }, lineMap: MAP,
    blocks: [
      { id: 'add', lines: [1, 5], label: 'add(x)', touches: ['a', 'j', 'n', 'x'] },
      { id: 'grow', lines: [2, 2], label: 'resize a if it is full', touches: ['a', 'n'] },
      { id: 'store', lines: [3, 4], label: 'write x at (j + n) mod length(a) and count it', touches: ['a', 'j', 'n', 'x'] },
      { id: 'remove', lines: [7, 12], label: 'remove()', touches: ['a', 'j', 'n', 'x'] },
      { id: 'take', lines: [8, 9], label: 'take a[j], and move j one cell on, mod length(a)', touches: ['a', 'j', 'x'] },
      { id: 'shrink', lines: [10, 12], label: 'count it, and shrink a if length(a) ≥ 3n', touches: ['a', 'n'] },
      { id: 'resize', lines: [14, 19], label: 'resize(): unroll the n elements into b[0], …, b[n − 1]', touches: ['a', 'b', 'j', 'k'] },
      { id: 'alloc', lines: [15, 15], label: 'allocate b of length max(1, 2n)', touches: ['b'] },
      { id: 'copy', lines: [17, 17], label: 'copy a[(j + k) mod length(a)] into b[k]', touches: ['a', 'b', 'k'] },
      { id: 'swap', lines: [18, 19], label: 'b becomes a, and j = 0', touches: ['a', 'b', 'j'] },
    ],
    refs: { 'self.a': () => F.ref('a'), a: () => F.ref('a'), b: () => F.ref('b'), 'self.j': () => F.ref('j'), j: () => F.ref('j'),
      'self.n': () => F.ref('n'), n: () => F.ref('n'), k: () => F.ref('k') },
  });

  const traces = Object.fromEntries(PRESETS.map((P) => [P.value, run(P)]));
  const byValue = Object.fromEntries(PRESETS.map((P) => [P.value, P]));
  const tip = { hits: [] };

  /* the ring: cell c of a ring of len cells spans the angles from −90° + c·360°/len clockwise */
  const RX = 300, RO = 188, RI = 116;
  const ang = (c, len) => -Math.PI / 2 + (c * 2 * Math.PI) / len;
  const wedge = (ctx, cx, cy, c, len, fill, stroke, lw = 2.5, dash) => {
    const a0 = ang(c, len) + 0.012, a1 = ang(c + 1, len) - 0.012;
    ctx.save();
    ctx.beginPath(); ctx.arc(cx, cy, RO, a0, a1); ctx.arc(cx, cy, RI, a1, a0, true); ctx.closePath();
    if (fill) { ctx.fillStyle = fill; ctx.fill(); }
    if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.stroke(); }
    ctx.restore();
  };
  const live = (j, n, len) => { const s = new Set(); for (let i = 0; i < n; i += 1) s.add((j + i) % len); return s; };

  F.debug(d, {
    code, watch: ['x', 'j', 'n', 'len(a)', 'k'],
    inputs: PRESETS.map((P) => ({ value: P.value, label: P.label, trace: traces[P.value] })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const P = byValue[g.input] || PRESETS[0];
      const v = g.frame.vars, pv = g.prev.vars, ke = g.k, ln = g.frame.line;
      const ca = F.ref('a'), cb = F.ref('b'), cj = F.ref('j'), cn = F.ref('n'), ckk = F.ref('k');
      const key = C('key'), size = C('size'), cost = C('cost'), idx = C('index'), ink = PAL.ink, muted = PAL.muted;
      const hits = [];
      const op = v.c >= 0 ? P.ops[v.c] : null;
      const len = v['len(a)'];
      const inResize = ln === L.alloc || ln === L.loop || ln === L.copy || ln === L.defResize;
      const lv = live(v.j, v.n, len);

      /* ---------------- the headline: the call, and the index it used */
      let head;
      if (!op) head = `length(a) = ${len} holds n = ${v.n} element${v.n === 1 ? '' : 's'}, the oldest in a[j] = a[${v.j}].`;
      else if (ln === L.defResize || ln === L.alloc) head = op[0] === 'add'
        ? `a is full, so ${callName(op)} first calls resize(): ${v.n} elements go into an array of ${Math.max(1, 2 * v.n)}.`
        : `length(a) = ${len} ≥ 3n = ${3 * v.n}, so remove() calls resize(): ${v.n} element${v.n === 1 ? ' goes' : 's go'} into an array of ${Math.max(1, 2 * v.n)}.`;
      else if (ln === L.loop || ln === L.copy) head = v.mv
        ? `resize() copies a[(j + k) mod length(a)] = a[(${v.j} + ${v.mv[1]}) mod ${len}] = a[${v.mv[0]}] into b[${v.mv[1]}].`
        : `resize() copies a[(j + k) mod length(a)] into b[k] for k = 0, …, ${v.n - 1}.`;
      else if (ln === L.setA) head = `b, of length ${len}, becomes a: the ring is unrolled, its oldest element in cell 0.`;
      else if (ln === L.setJ) head = `j = 0: the ${v.n} element${v.n === 1 ? '' : 's'} now sit in a[0], …, a[${v.n - 1}].`;
      else if (op[0] === 'add') {
        if ((v.w === null || v.w === undefined) && v.stars.includes(v.c)) head = `a was full, so ${callName(op)} resized it first: now n + 1 = ${v.n + 1} ≤ length(a) = ${len}.`;
        else if (v.w === null || v.w === undefined) head = `${callName(op)}: is a full? n + 1 = ${v.n + 1} > length(a) = ${len} is ${v.n + 1 > len ? 'true' : 'false'}.`;
        else {
          const jn = v.wrote ? v.wrote : [v.j, v.n - 1];
          const raw = jn[0] + jn[1];
          head = `${callName(op)} writes ${op[1]} at (j + n) mod length(a) = (${jn[0]} + ${jn[1]}) mod ${len} = ${v.w}` +
            (raw >= len ? `: past the last cell, back round to ${v.w}.` : '.');
        }
      } else if (ln === L.take || ln === L.defRemove) head = ln === L.take ? `remove() takes a[j] = a[${v.j}] = ${v.x}, the oldest element.` : 'remove(): the oldest element is a[j].';
      else if (ln === L.step) head = `j moves to (j + 1) mod length(a) = (${v.stepped} + 1) mod ${len} = ${v.j}` + (v.stepped + 1 >= len ? ', back round to 0.' : '.');
      else {
        const shrank = v.stars.includes(v.c);
        head = shrank ? `remove() returned ${v.x}; length(a) was ≥ 3n, so a shrank to ${len}.`
          : `remove() returns ${v.x}; length(a) = ${len} < 3n = ${3 * v.n}, so a keeps its length.`;
      }
      topline(ctx, head);

      /* ---------------- the calls: done in ink, the current one boxed, the rest muted; * where a call resized */
      const CS = 26, gap = 24;
      const labels = P.ops.map((o, q) => callName(o) + (v.stars.includes(q) ? '*' : ''));
      const widths = labels.map((s) => measure(ctx, s, { size: CS }));
      const rows = [[]]; let wsum = 0;
      labels.forEach((s, q) => { if (wsum + widths[q] > 1260 && rows[rows.length - 1].length) { rows.push([]); wsum = 0; } rows[rows.length - 1].push(q); wsum += widths[q] + gap; });
      rows.forEach((row, ri) => {
        const tot = row.reduce((s, q) => s + widths[q] + gap, -gap);
        let x = 700 - tot / 2; const y = 112 + ri * 44;
        row.forEach((q) => {
          const cur = q === v.c, done = q < v.c;
          if (cur) rect(ctx, x - 8, y - 20, widths[q] + 16, 40, alpha(ink, 0.06), ink, 2);
          text(ctx, labels[q], x, y, cur || done ? ink : muted, { size: CS, base: 'middle', weight: cur ? 600 : 400 });
          hits.push({ x: x + widths[q] / 2, y, r: widths[q] / 2, name: `call ${q + 1}: ${callName(P.ops[q])}${v.stars.includes(q) ? ', which called resize()' : ''}` });
          x += widths[q] + gap;
        });
      });
      const top = 112 + rows.length * 44;

      /* ---------------- the ring (left) and the array (right). While resize() copies, the ring is a's and b fills below
         the array; on b becomes a, the old ring and array fade as the new ones arrive */
      const RY = top + 250, AY = top + 130, BY = AY + 236, CH = 62;
      const layout = (cells, y) => { const cw = Math.min(66, 640 / cells), x0 = 1035 - (cw * cells) / 2; return { cw, x0, x1: x0 + cw * cells, y, x: (q) => x0 + q * cw + cw / 2 }; };
      const swapK = ln === L.setA ? (g.prev.line === L.setA ? 1 : ke) : 1;
      const prevLen = (ln === L.setA && pv && pv['len(a)']) ? pv['len(a)'] : len;
      const ringOf = (vals, ln2, liveSet, op2) => {
        ctx.save(); ctx.globalAlpha *= op2;
        for (let c = 0; c < ln2; c += 1) {
          const on = liveSet.has(c);
          wedge(ctx, RX, RY, c, ln2, on ? alpha(idx, 0.18) : PAL.panel, on ? ink : alpha(ink, 0.4), on ? 2.5 : 2);
          const mid = (ang(c, ln2) + ang(c + 1, ln2)) / 2, rm = (RO + RI) / 2;
          if (on && vals[c] !== null && vals[c] !== undefined) text(ctx, String(vals[c]), RX + rm * Math.cos(mid), RY + rm * Math.sin(mid), key, { size: ln2 > 12 ? 26 : 32, weight: 600, align: 'center', base: 'middle' });
          text(ctx, String(c), RX + (RO + 24) * Math.cos(mid), RY + (RO + 24) * Math.sin(mid), muted, { size: 22, align: 'center', base: 'middle' });
          hits.push({ x: RX + rm * Math.cos(mid), y: RY + rm * Math.sin(mid), r: 30, name: on ? `a[${c}] = ${vals[c]}, in the queue` : `a[${c}], free` });
        }
        ctx.restore();
      };
      const stripOf = (Lr, vals, liveSet, name, color, op2, showVals = true) => {
        ctx.save(); ctx.globalAlpha *= op2;
        vals.forEach((val, q) => {
          const on = liveSet.has(q);
          rect(ctx, Lr.x0 + q * Lr.cw + 2, Lr.y - CH / 2, Lr.cw - 4, CH, on ? alpha(idx, 0.18) : PAL.panel, on ? ink : alpha(ink, 0.4), on ? 2.5 : 2);
          if (on && showVals && val !== null && val !== undefined) text(ctx, String(val), Lr.x(q), Lr.y, key, { size: Lr.cw < 50 ? 26 : 32, align: 'center', base: 'middle', weight: 600 });
          text(ctx, String(q), Lr.x(q), Lr.y + CH / 2 + 20, muted, { size: 22, align: 'center', base: 'middle' });
          hits.push({ x: Lr.x(q), y: Lr.y, r: Lr.cw / 2, name: on ? `${name}[${q}] = ${val}` : `${name}[${q}], free` });
        });
        text(ctx, name, Lr.x0 - 22, Lr.y, color, { size: 34, weight: 600, align: 'right', base: 'middle', italic: true });
        ctx.restore();
      };

      if (ln === L.setA && swapK < 1) {
        /* the old a fades as b, unrolled, takes its place */
        const oldA = pv.a || v.a, oldLive = live(pv.j, pv.n, prevLen);
        ringOf(oldA, prevLen, oldLive, 1 - swapK);
        stripOf(layout(prevLen, AY), oldA, oldLive, 'a', ca, 1 - swapK);
        const newLive = live(v.j, v.n, len);
        ringOf(v.a, len, newLive, swapK);
        stripOf(layout(len, lerp(BY, AY, swapK)), v.a, newLive, swapK > 0.5 ? 'a' : 'b', swapK > 0.5 ? ca : cb, 1);
      } else {
        ringOf(v.a, len, lv, 1);
        const La = layout(len, AY);
        stripOf(La, v.a, lv, 'a', ca, 1);
        if (v.b) {
          /* b, filling as the copies land, and the copies made so far */
          const Lb = layout(v.b.length, BY);
          const filled = new Set(); v.b.forEach((y, q) => { if (y !== null) filled.add(q); });
          stripOf(Lb, v.b, filled, 'b', cb, ln === L.alloc && g.prev.line !== L.alloc ? ke : 1);
          hbracket(ctx, Lb.x0, Lb.x1, BY + CH / 2 + 46, size, `length(b) = max(1, 2n) = ${v.b.length}`, { side: 'below' });
          for (let q = 0; q < v.b.length; q += 1) {
            if (v.b[q] === null) continue;
            const from = (v.j + q) % len;
            const cur = v.mv && v.mv[1] === q;
            const fresh = cur && !(pv.mv && pv.mv[1] === q);
            const x0 = La.x(from), y0 = AY + CH / 2 + 34, x1 = Lb.x(q), y1 = BY - CH / 2 - 4, t = fresh ? Math.max(0.2, ke) : 1;
            if (cur) arrow(ctx, x0, y0, lerp(x0, x1, t), lerp(y0, y1, t), ckk, 5);
            else line(ctx, x0, y0, x1, y1, alpha(ckk, 0.35), 3);
          }
          if (v.mv) {
            /* the cell being read, in k's colour, on the ring and in a; k under b's cell */
            wedge(ctx, RX, RY, v.mv[0], len, null, ckk, 5);
            rect(ctx, La.x0 + v.mv[0] * La.cw + 2, AY - CH / 2, La.cw - 4, CH, null, ckk, 5);
            text(ctx, `k = ${v.mv[1]}`, Lb.x(v.mv[1]), BY - CH / 2 - 22, ckk, { size: 26, weight: 600, align: 'center', base: 'middle' });
          }
        }
        /* j: an arrow from the ring's centre into cell j, and under the array; it turns forward when remove() moves it */
        const jFrom = ln === L.step && g.prev.line !== L.step ? v.stepped : v.j;
        const turn = ln === L.step && g.prev.line !== L.step ? ke : 1;
        const jAng = lerp((ang(jFrom, len) + ang(jFrom + 1, len)) / 2, (ang(jFrom + 1, len) + ang(jFrom + 2, len)) / 2, ln === L.step ? turn : 0);
        const jMid = ln === L.step ? jAng : (ang(v.j, len) + ang(v.j + 1, len)) / 2;
        if (v.n > 0 || ln === L.step) {
          arrow(ctx, RX + 26 * Math.cos(jMid), RY + 26 * Math.sin(jMid), RX + (RI - 8) * Math.cos(jMid), RY + (RI - 8) * Math.sin(jMid), cj, 5);
          const jx = ln === L.step ? lerp(La.x(jFrom), jFrom + 1 >= len ? La.x(len - 1) + La.cw : La.x(jFrom + 1), turn) : La.x(v.j);
          const jxx = ln === L.step && jFrom + 1 >= len && turn >= 1 ? La.x(0) : jx;
          arrow(ctx, jxx, AY + CH / 2 + 96, jxx, AY + CH / 2 + 40, cj, 5);
          text(ctx, `j = ${v.j}`, jxx, AY + CH / 2 + 118, cj, { size: 28, weight: 600, align: 'center', base: 'middle' });
        }
        text(ctx, 'j', RX - 4, RY + 4, cj, { size: 30, weight: 600, align: 'center', base: 'middle', italic: true });
        /* the next write, (j + n) mod length(a): a dashed outline on both, in the index colour of a position */
        if (!v.b && v.n < len) {
          const nw = (v.j + v.n) % len;
          wedge(ctx, RX, RY, nw, len, null, idx, 3.5, [8, 6]);
          rect(ctx, La.x0 + nw * La.cw + 2, AY - CH / 2, La.cw - 4, CH, null, idx, 3.5, [8, 6]);
          hits.push({ x: La.x(nw), y: AY - CH / 2 - 10, r: 20, name: `(j + n) mod length(a) = ${nw}: where add(x) writes next` });
        }
        /* the element just written or taken */
        if (v.w !== null && v.w !== undefined && (ln === L.store || ln === L.take)) {
          wedge(ctx, RX, RY, v.w, len, null, key, 5);
          rect(ctx, La.x0 + v.w * La.cw + 2, AY - CH / 2, La.cw - 4, CH, null, key, 5);
        }
        hbracket(ctx, La.x0, La.x1, AY - CH / 2 - 26, size, `length(a) = ${len}`, { side: 'above' });
      }

      /* ---------------- the counts: the invariant, the next write, then the copies against their bound */
      const Y0 = top + 566;
      const seg = (parts, y) => {
        const ws = parts.map(([s, , o]) => measure(ctx, s, { size: 28, weight: (o && o.weight) || 400 }));
        let x = 700 - ws.reduce((s, w2) => s + w2, 0) / 2;
        parts.forEach(([s, c, o], q) => { text(ctx, s, x, y, c, { size: 28, base: 'middle', weight: (o && o.weight) || 400 }); x += ws[q]; });
      };
      const lastLive = v.n ? (v.j + v.n - 1) % len : null;
      seg(v.n
        ? [['the queue: ', ink], ['a', ca, { weight: 600 }], ['[', ink], ['j', cj, { weight: 600 }], [`] = a[${v.j}], …, a[(j + n − 1) mod ${len}] = a[${lastLive}]`, ink], ['   n', cn, { weight: 600 }], [` = ${v.n} ≤ length(a) = ${len}`, ink]]
        : [['the queue is empty: ', ink], ['n', cn, { weight: 600 }], [` = 0, length(a) = ${len}`, ink]], Y0);
      if (!v.b && v.n < len) seg([['next add writes a[(j + n) mod length(a)] = ', ink], [`a[(${v.j} + ${v.n}) mod ${len}] = a[${(v.j + v.n) % len}]`, idx, { weight: 600 }]], Y0 + 44);
      else if (!v.b) seg([['a is full: the next add calls resize() first', ink]], Y0 + 44);
      seg([[`calls m = ${v.m}, resizes r = ${v.r}: copies Σnᵢ = `, PAL.ink], [String(v.copies), cost], [` ≤ 2m + 2r = ${2 * v.m + 2 * v.r}`, PAL.ink]], Y0 + 88);
      const show = v.log.slice(-2);
      show.forEach((e, q) => {
        const i = v.log.length - show.length + q + 1;
        seg([[`resize ${i}, in ${e.call}: n${sub(i)} = `, PAL.ink], [String(e.ni), cost], [' copied, ', PAL.ink], [String(e.since), cost], [` call${e.since === 1 ? '' : 's'} since the last ≥ n${sub(i)}/2 − 1 = ${num(e.ni / 2 - 1)}`, PAL.ink]], Y0 + 132 + q * 44);
      });
      tip.hits = hits;
    },
  });
  F.hover(d.stage, () => tip.hits, d.c);
})();
};
