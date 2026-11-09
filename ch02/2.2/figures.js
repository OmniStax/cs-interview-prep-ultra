/* Figures for section 2.2 Dynamic arrays. Boots against the section's text article.
   One debugger figure (code beside the drawing, stepped by block: METHOD §2.3): ODS's ArrayStack running a
   sequence of calls on its backing array, opening on the calls of ODS's own Figure 2.1. The code panel is ODS's
   set, add, remove and resize: Python (canonical, the trace's lines), Java and C++ as ODS's editions print them,
   written in below by ch02/2.2/inline_code.py from the source cache; JavaScript is the AI's translation of the
   Java and carries the AI mark. The trace is the figure's own JS copy of the Python: one frame per statement,
   and one per element a slice moves, so that stepping into a shift or a resize goes copy by copy. Section 1.5's
   sim-pay-for-doubling counts appends three ways; this one runs ODS's code, inserts anywhere, removes and
   shrinking, and counts the sum of ODS's lemma. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['2.2'] = function (root, F) {
const { C, PAL, alpha, text, arrow, line, begin, topline, measure, hbracket } = F;
const sim = (id, H) => F.sim(root, id, H);
const AI = 'claude-opus-5-5 high';
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2, dash) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};
const lerp = (a, b, k) => a + (b - a) * k;
const curve = (ctx, x0, y0, x1, y1, lift, color, w = 4) => {
  /* an arc from one cell to another, its head at the end: the element copied */
  const mx = (x0 + x1) / 2, my = Math.min(y0, y1) - lift;
  ctx.save(); ctx.strokeStyle = color; ctx.fillStyle = color; ctx.lineWidth = w; ctx.lineCap = 'round';
  ctx.beginPath(); ctx.moveTo(x0, y0); ctx.quadraticCurveTo(mx, my, x1, y1); ctx.stroke();
  const a = Math.atan2(y1 - my, x1 - mx), L = 14;
  ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x1 - L * Math.cos(a - 0.45), y1 - L * Math.sin(a - 0.45));
  ctx.lineTo(x1 - L * Math.cos(a + 0.45), y1 - L * Math.sin(a + 0.45)); ctx.closePath(); ctx.fill(); ctx.restore();
};
const SUBS = '₀₁₂₃₄₅₆₇₈₉';
const num = (x) => String(x).replace('-', '−');   /* a minus sign, not a hyphen */
const sub = (k) => String(k).split('').map((c) => SUBS[+c]).join('');

/* ================================================================ sim-arraystack */
(function () {
  /* BEGIN ODS LISTINGS (ch02/2.2/inline_code.py) */
  const PY = "def set(self, i, x):\n    y = self.a[i]\n    self.a[i] = x\n    return y\n\ndef add(self, i, x):\n    if self.n == len(self.a): self._resize()\n    self.a[i+1:self.n+1] = self.a[i:self.n]\n    self.a[i] = x\n    self.n += 1\n\ndef remove(self, i):\n    x = self.a[i]\n    self.a[i:self.n-1] = self.a[i+1:self.n]\n    self.n -= 1\n    if len(self.a) >= 3*self.n: self._resize()\n    return x\n\ndef _resize(self):\n    b = new_array(max(1, 2*self.n))\n    b[0:self.n] = self.a[0:self.n]\n    self.a = b";
  const JAVA = "T set(int i, T x) {\n    T y = a[i];\n    a[i] = x;\n    return y;\n}\n\nvoid add(int i, T x) {\n    if (n + 1 > a.length) resize();\n    for (int j = n; j > i; j--)\n        a[j] = a[j-1];\n    a[i] = x;\n    n++;\n}\n\nT remove(int i) {\n    T x = a[i];\n    for (int j = i; j < n-1; j++)\n        a[j] = a[j+1];\n    n--;\n    if (a.length >= 3*n) resize();\n    return x;\n}\n\nvoid resize() {\n    T[] b = newArray(max(n*2,1));\n    for (int i = 0; i < n; i++) {\n        b[i] = a[i];\n    }\n    a = b;\n}";
  const CPP = "T set(int i, T x) {\n    T y = a[i];\n    a[i] = x;\n    return y;\n}\n\nvoid add(int i, T x) {\n    if (n + 1 > a.length) resize();\n    for (int j = n; j > i; j--)\n        a[j] = a[j - 1];\n    a[i] = x;\n    n++;\n}\n\nT remove(int i) {\n    T x = a[i];\n    for (int j = i; j < n - 1; j++)\n        a[j] = a[j + 1];\n    n--;\n    if (a.length >= 3 * n) resize();\n    return x;\n}\n\nvoid resize() {\n    array<T> b(max(2 * n, 1));\n    for (int i = 0; i < n; i++)\n        b[i] = a[i];\n    a = b;\n}";
  /* END ODS LISTINGS */
  /* JavaScript: the AI's translation of ODS's Java, line for line */
  const JS = [
    'set(i, x) {',
    '    const y = this.a[i];',
    '    this.a[i] = x;',
    '    return y;',
    '}',
    '',
    'add(i, x) {',
    '    if (this.n + 1 > this.a.length) this.resize();',
    '    for (let j = this.n; j > i; j--)',
    '        this.a[j] = this.a[j-1];',
    '    this.a[i] = x;',
    '    this.n++;',
    '}',
    '',
    'remove(i) {',
    '    const x = this.a[i];',
    '    for (let j = i; j < this.n-1; j++)',
    '        this.a[j] = this.a[j+1];',
    '    this.n--;',
    '    if (this.a.length >= 3*this.n) this.resize();',
    '    return x;',
    '}',
    '',
    'resize() {',
    '    const b = new Array(Math.max(this.n*2, 1));',
    '    for (let i = 0; i < this.n; i++) {',
    '        b[i] = this.a[i];',
    '    }',
    '    this.a = b;',
    '}',
  ].join('\n');
  /* Python line → the braced languages' lines (a method's closing brace, and the for loop's two lines) */
  const BRACED = { 1: 1, 2: 2, 3: 3, 4: 4, 6: 7, 7: 8, 8: [9, 10], 9: 11, 10: 12, 12: 15, 13: 16, 14: [17, 18], 15: 19, 16: 20, 17: 21, 19: 24, 20: 25 };
  const MAP = {
    java: { ...BRACED, 21: [26, 27, 28], 22: 29 },
    cpp: { ...BRACED, 21: [26, 27], 22: 28 },
    javascript: { ...BRACED, 21: [26, 27, 28], 22: 29 },
  };
  /* Python's lines: set 1–4, add 6–10, remove 12–17, _resize 19–22 */
  const L = { start: 5, setY: 2, setA: 3, setR: 4, grow: 7, shift: 8, store: 9, count: 10, take: 13, close: 14, dec: 15, shrink: 16, ret: 17, alloc: 20, copy: 21, swap: 22 };

  /* The inputs. Figure 2.1 of ODS starts from b r e d in an array of length 6; the rest start empty, at length 1. */
  const LET = 'abcdefghijklmnop'.split('');
  const PRESETS = [
    { value: 'figure', label: 'Figure 2.1', a: ['b', 'r', 'e', 'd', null, null], n: 4,
      ops: [['add', 2, 'e'], ['add', 5, 'r'], ['add', 5, 'e'], ['remove', 4], ['remove', 4], ['remove', 4], ['set', 2, 'i']] },
    { value: 'append', label: 'append', a: [null], n: 0, ops: LET.slice(0, 12).map((x, k) => ['add', k, x]) },
    { value: 'front', label: 'add at the front', a: [null], n: 0, ops: LET.slice(0, 8).map((x) => ['add', 0, x]) },
    { value: 'shrink', label: 'grow then shrink', a: [null], n: 0,
      ops: [...LET.slice(0, 8).map((x, k) => ['add', k, x]), ...LET.slice(0, 8).map((_, k) => ['remove', 7 - k])] },
    { value: 'boundary', label: 'at the boundary', a: [null], n: 0,
      ops: [...LET.slice(0, 4).map((x, k) => ['add', k, x]), ...Array.from({ length: 6 }, () => [['add', 4, 'e'], ['remove', 4]]).flat()] },
  ];
  const callName = (o) => (o[0] === 'remove' ? `remove(${o[1]})` : `${o[0]}(${o[1]}, ${o[2]})`);

  /* One run of a preset as frames of the Python. Beside the code's own variables (i, x, n, len(a), a, b) each
     frame carries what the drawing reads: the call under way (k), the copy just made (mv: [from, to, row]),
     the copies made by this call so far (moves), and the running counts: calls to add or remove (m), resizes
     (r), elements copied by resize() (copies, the lemma's sum of nᵢ), elements shifted (shifts), calls since
     the last resize (since), and one record per resize (log: the call, nᵢ, the calls before it). */
  const run = (P) => F.trace((at) => {
    let a = P.a.slice(), n = P.n, b = null;
    let k = -1, m = 0, r = 0, copies = 0, shifts = 0, since = 0, moves = [];
    const log = [], stars = [];
    let i = null, x = null;
    const snap = (extra) => Object.assign({ i, x, n, 'len(a)': a.length, a: a.slice(), k, m, r, copies, shifts, since,
      moves: moves.slice(), log: log.map((e) => ({ ...e })), stars: stars.slice() }, b ? { b: b.slice() } : {}, extra || {});
    const resize = () => {
      at.enter('_resize');
      b = new Array(Math.max(1, 2 * n)).fill(null); at(L.alloc, snap());
      const ni = n;
      if (!n) at(L.copy, snap());
      for (let j = 0; j < n; j += 1) { b[j] = a[j]; copies += 1; moves.push([j, j, 'b']); at(L.copy, snap({ mv: [j, j, 'b'] }), ['copy', j]); }
      r += 1; log.push({ k, ni, since: since - 0, call: callName(P.ops[k]) }); stars.push(k); since = 0;
      a = b; b = null; at(L.swap, snap({ swapped: true }));
      at.leave();
    };
    at(L.start, snap());
    P.ops.forEach((o, kk) => {
      k = kk; moves = [];
      if (o[0] === 'set') {
        i = o[1]; x = o[2];
        at(L.setY, snap({ y: a[i] }));
        a[i] = x; at(L.setA, snap(), ['put', i]);
        at(L.setR, snap());
        return;
      }
      m += 1; since += 1;
      if (o[0] === 'add') {
        i = o[1]; x = o[2];
        if (n === a.length) resize();
        at(L.grow, snap());
        if (n === i) at(L.shift, snap());
        for (let j = n; j > i; j -= 1) { a[j] = a[j - 1]; shifts += 1; moves.push([j - 1, j, 'a']); at(L.shift, snap({ mv: [j - 1, j, 'a'] }), ['shift', j - 1, j]); }
        a[i] = x; at(L.store, snap(), ['put', i]);
        n += 1; at(L.count, snap());
      } else {
        i = o[1]; x = a[i];
        at(L.take, snap());
        if (i === n - 1) at(L.close, snap());
        for (let j = i; j < n - 1; j += 1) { a[j] = a[j + 1]; shifts += 1; moves.push([j + 1, j, 'a']); at(L.close, snap({ mv: [j + 1, j, 'a'] }), ['shift', j + 1, j]); }
        n -= 1; a[n] = null; at(L.dec, snap());
        if (a.length >= 3 * n) resize();
        at(L.shrink, snap());
        at(L.ret, snap());
      }
    });
  });

  const d = sim('sim-arraystack', 930);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: { javascript: AI }, lineMap: MAP,
    blocks: [
      { id: 'set', lines: [1, 4], label: 'set(i, x) overwrites a[i]', touches: ['a', 'i'] },
      { id: 'add', lines: [6, 10], label: 'add(i, x)', touches: ['a', 'i', 'x', 'n'] },
      { id: 'room', lines: [7, 8], label: 'make room for x', touches: ['a', 'i', 'n'] },
      { id: 'grow', lines: [7, 7], label: 'resize a if it is full', touches: ['a', 'n'] },
      { id: 'shift', lines: [8, 8], label: 'copy one element a cell to the right', touches: ['a'] },
      { id: 'store', lines: [9, 10], label: 'store x in a[i] and count it', touches: ['a', 'x', 'n'] },
      { id: 'remove', lines: [12, 17], label: 'remove(i)', touches: ['a', 'i', 'x', 'n'] },
      { id: 'close', lines: [13, 14], label: 'take a[i] out and close the gap', touches: ['a', 'i', 'x'] },
      { id: 'shiftl', lines: [14, 14], label: 'copy one element a cell to the left', touches: ['a'] },
      { id: 'shrink', lines: [15, 17], label: 'count it, and shrink a if length(a) ≥ 3n', touches: ['a', 'n'] },
      { id: 'resize', lines: [19, 22], label: 'resize(): copy the n elements into an array of size 2n', touches: ['a', 'b'] },
      { id: 'alloc', lines: [20, 20], label: 'allocate b of size 2n', touches: ['b'] },
      { id: 'copy', lines: [21, 21], label: 'copy one element into b', touches: ['b'] },
      { id: 'swap', lines: [22, 22], label: 'b becomes a', touches: ['a', 'b'] },
    ],
    refs: { 'self.a': () => F.ref('a'), a: () => F.ref('a'), b: () => F.ref('b'), i: () => F.ref('i'), 'self.n': () => F.ref('n'), n: () => F.ref('n') },
  });

  const traces = Object.fromEntries(PRESETS.map((P) => [P.value, run(P)]));
  const byValue = Object.fromEntries(PRESETS.map((P) => [P.value, P]));
  const tip = { hits: [] };

  F.debug(d, {
    code, watch: ['i', 'x', 'n', 'len(a)'],
    inputs: PRESETS.map((P) => ({ value: P.value, label: P.label, trace: traces[P.value] })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const P = byValue[g.input] || PRESETS[0];
      const v = g.frame.vars, pv = g.prev.vars, k = g.k, ln = g.frame.line;
      const ca = F.ref('a'), cb = F.ref('b'), ci = F.ref('i'), cn = F.ref('n');
      const key = C('key'), size = C('size'), cost = C('cost'), idx = C('index'), ink = PAL.ink, muted = PAL.muted;
      const hits = [];
      const op = v.k >= 0 ? P.ops[v.k] : null;
      const inResize = ln === L.alloc || ln === L.copy || ln === L.swap;

      /* ---------------- the headline: the call, and what it moved */
      let head;
      const cap = v['len(a)'];
      if (!op) head = v.n ? `length(a) = ${cap} holds n = ${v.n} elements.` : 'An empty ArrayStack: length(a) = 1 and n = 0.';
      else if (inResize) {
        head = ln === L.swap
          ? `resize() has copied ${v.log[v.log.length - 1].ni} elements, and b, of length ${cap}, becomes a.`
          : op[0] === 'add' ? `a is full, so ${callName(op)} first calls resize(): ${v.n} elements go into an array of ${Math.max(1, 2 * v.n)}.`
            : `length(a) = ${cap} ≥ 3n = ${3 * v.n}, so ${callName(op)} calls resize(): ${v.n} element${v.n === 1 ? '' : 's'} go into an array of ${Math.max(1, 2 * v.n)}.`;
      } else if (op[0] === 'set') head = `${callName(op)} overwrites a[${op[1]}]; nothing moves.`;
      else if (op[0] === 'add') {
        const sh = v.moves.filter((mv) => mv[2] === 'a').length, full = P.ops[v.k] && v.stars.includes(v.k);
        head = `${callName(op)}${full ? ', after the resize,' : ''} shifts ${sh} element${sh === 1 ? '' : 's'} right and stores ${op[2]} in a[${op[1]}].`;
      } else {
        const sh = v.moves.filter((mv) => mv[2] === 'a').length, shrank = v.stars.includes(v.k);
        head = shrank ? `${callName(op)} shifts ${sh} element${sh === 1 ? '' : 's'} left; length(a) was ≥ 3n, so a shrank to ${cap}.`
          : ln >= L.shrink || ln === L.ret
            ? `${callName(op)} shifts ${sh} element${sh === 1 ? '' : 's'} left; length(a) = ${cap} < 3n = ${3 * v.n}, so a keeps its length.`
            : `${callName(op)} shifts ${sh} element${sh === 1 ? '' : 's'} left.`;
      }
      topline(ctx, head);

      /* ---------------- the calls: done in ink, the current one boxed, the rest muted; * where a call resized */
      const CS = 26, gap = 22;
      const labels = P.ops.map((o, j) => callName(o).replace(/, /g, ',') + (v.stars.includes(j) ? '*' : ''));
      const widths = labels.map((s) => measure(ctx, s, { size: CS }));
      const rows = [[]]; let wsum = 0;
      labels.forEach((s, j) => { if (wsum + widths[j] > 1260 && rows[rows.length - 1].length) { rows.push([]); wsum = 0; } rows[rows.length - 1].push(j); wsum += widths[j] + gap; });
      rows.forEach((row, ri) => {
        const tot = row.reduce((s, j) => s + widths[j] + gap, -gap);
        let x = 700 - tot / 2; const y = 112 + ri * 44;
        row.forEach((j) => {
          const cur = j === v.k, done = j < v.k;
          if (cur) rect(ctx, x - 8, y - 20, widths[j] + 16, 40, alpha(ink, 0.06), ink, 2);
          text(ctx, labels[j], x, y, cur || done ? ink : muted, { size: CS, base: 'middle', weight: cur ? 600 : 400 });
          hits.push({ x: x + widths[j] / 2, y, r: widths[j] / 2, name: `call ${j + 1}: ${callName(P.ops[j])}${v.stars.includes(j) ? ', which called resize()' : ''}` });
          x += widths[j] + gap;
        });
      });
      const top = 112 + rows.length * 44;

      /* ---------------- the arrays: a above; while resize() runs, b below it, and on the swap b rises into a's place */
      const ROWA = top + 190, ROWB = ROWA + 180, CH = 64;
      const layout = (cells, y) => { const cw = Math.min(80, 1240 / cells), x0 = 700 - (cw * cells) / 2; return { cw, x0, x1: x0 + cw * cells, y, x: (j) => x0 + j * cw + cw / 2 }; };
      const cellRow = (Lr, vals, nFill, name, color, op = 1, shade = true) => {
        ctx.save(); ctx.globalAlpha *= op;
        if (shade && nFill > 0) { ctx.fillStyle = alpha(idx, 0.18); ctx.fillRect(Lr.x0 - 4, Lr.y - CH / 2 - 6, Lr.cw * nFill + 8, CH + 12); }
        vals.forEach((val, j) => {
          const has = val !== null && val !== undefined;
          rect(ctx, Lr.x0 + j * Lr.cw + 2, Lr.y - CH / 2, Lr.cw - 4, CH, PAL.panel, has ? ink : alpha(ink, 0.4), has ? 2.5 : 2);
          if (has) text(ctx, String(val), Lr.x(j), Lr.y, key, { size: Lr.cw < 50 ? 28 : 34, align: 'center', base: 'middle', weight: 600 });
          text(ctx, String(j), Lr.x(j), Lr.y + CH / 2 + 22, muted, { size: Lr.cw < 50 ? 22 : 26, align: 'center', base: 'middle' });
          hits.push({ x: Lr.x(j), y: Lr.y, r: Lr.cw / 2, name: has ? `${name}[${j}] = ${val}` : `${name}[${j}], empty` });
        });
        text(ctx, name, Lr.x0 - 24, Lr.y, color, { size: 34, weight: 600, align: 'right', base: 'middle', italic: true });
        ctx.restore();
      };
      const swapK = ln === L.swap ? (g.prev.line === L.swap ? 1 : k) : 0;
      const La = layout(cap, ROWA);
      if (inResize && ln !== L.swap) {
        /* a, and b filling as the copies land */
        cellRow(La, v.a, v.n, 'a', ca);
        const Lb = layout(v.b.length, ROWB);
        const nb = v.b.filter((y) => y !== null).length;
        cellRow(Lb, v.b, nb, 'b', cb, ln === L.alloc && g.prev.line !== L.alloc ? k : 1, false);
        hbracket(ctx, Lb.x0, Lb.x1, ROWB + CH / 2 + 50, size, `length(b) = 2n = ${v.b.length}`, { side: 'below' });
        v.moves.filter((mv) => mv[2] === 'b').forEach((mv) => {
          const cur = v.mv && v.mv[0] === mv[0] && v.mv[2] === 'b';
          const t = cur && !(g.prev.vars.mv && g.prev.vars.mv[0] === mv[0]) ? k : 1;
          const x0 = La.x(mv[0]), x1 = Lb.x(mv[1]), y0 = ROWA + CH / 2 + 38, y1 = ROWB - CH / 2 - 4;
          if (cur) arrow(ctx, x0, y0, lerp(x0, x1, Math.max(0.2, t)), lerp(y0, y1, Math.max(0.2, t)), cb, 5);
          else line(ctx, x0, y0, x1, y1, alpha(cb, 0.35), 3);
        });
      } else if (ln === L.swap) {
        /* the old a fades; b rises into its place */
        const oldCap = (pv['len(a)'] && pv.b) ? pv['len(a)'] : cap / 2;
        const Lo = layout(oldCap, ROWA);
        cellRow(Lo, (pv.a || v.a).slice(0, oldCap), v.n, 'a', ca, 1 - swapK);
        const Ln = layout(cap, lerp(ROWB, ROWA, swapK));
        cellRow(Ln, v.a, v.n, swapK > 0.5 ? 'a' : 'b', swapK > 0.5 ? ca : cb, 1, swapK > 0.5);
      } else {
        cellRow(La, v.a, v.n, 'a', ca);
        /* the copies this call made within a: an arc from each element's old cell to its new one, the last one drawn
           as it moves; at rest every arc of the call stays, as Figure 2.1 draws them */
        v.moves.filter((mv) => mv[2] === 'a').forEach((mv) => {
          const cur = v.mv && v.mv[0] === mv[0] && v.mv[1] === mv[1] && v.mv[2] === 'a';
          const fresh = cur && !(pv.mv && pv.mv[0] === mv[0] && pv.mv[1] === mv[1]);
          const x0 = La.x(mv[0]), x1 = La.x(mv[1]), y = ROWA - CH / 2 - 4;
          const t = fresh ? Math.max(0.25, k) : 1;
          curve(ctx, x0, y, lerp(x0, x1, t), y, 34, cur ? ci : alpha(ci, 0.45), cur ? 4 : 3);
        });
      }

      /* ---------------- the brackets and the pointer: length(a) over the whole array, n over a[0..n−1], i under its cell */
      if (ln !== L.swap) {
        const Lc = La;
        hbracket(ctx, Lc.x0, Lc.x1, ROWA - CH / 2 - 112, size, `length(a) = ${cap}`, { side: 'above' });
        if (v.n > 0) hbracket(ctx, Lc.x0, Lc.x0 + v.n * Lc.cw, ROWA - CH / 2 - 56, cn, `n = ${v.n}`, { side: 'above' });
        else text(ctx, 'n = 0', Lc.x0, ROWA - CH / 2 - 70, cn, { size: 26, weight: 600, base: 'middle' });
        if (op && !inResize && v.i !== null && v.i !== undefined) {
          const xi = Lc.x(Math.min(v.i, cap - 1)), yb = ROWA + CH / 2 + 44;
          arrow(ctx, xi, yb + 56, xi, yb, ci, 4);
          text(ctx, `i = ${v.i}`, xi, yb + 80, ci, { size: 30, weight: 600, align: 'center', base: 'middle' });
        }
      }

      /* ---------------- the counts: the invariant, then the lemma's sum against its bound */
      const Y0 = ROWA + 330;
      const seg = (parts, y) => {
        /* one line of runs, each in its own colour, centred */
        const ws = parts.map(([s, , o]) => measure(ctx, s, { size: 28, weight: (o && o.weight) || 400 }));
        let x = 700 - ws.reduce((s, w) => s + w, 0) / 2;
        parts.forEach(([s, c, o], j) => { text(ctx, s, x, y, c, { size: 28, base: 'middle', weight: (o && o.weight) || 400 }); x += ws[j]; });
      };
      seg([['a[0..n − 1] holds the list: ', ink], ['n', cn, { weight: 600 }], [` = ${v.n} ≤ length(`, ink], ['a', ca, { weight: 600 }], [`) = ${cap}`, ink]], Y0);
      seg([[`calls m = ${v.m}, resizes r = ${v.r}: copies Σnᵢ = ${v.copies} ≤ 2m + 2r = ${2 * v.m + 2 * v.r}`, cost]], Y0 + 44);
      seg([[`elements shifted by add and remove: ${v.shifts}`, cost]], Y0 + 88);
      const show = v.log.slice(-2);
      show.forEach((e, j) => {
        const q = v.log.length - show.length + j + 1;
        seg([[`resize ${q}, in ${e.call}: n${sub(q)} = ${e.ni} copied, ${e.since} call${e.since === 1 ? '' : 's'} since the last ≥ n${sub(q)}/2 − 1 = ${num(e.ni / 2 - 1)}`, cost]], Y0 + 132 + j * 44);
      });
      tip.hits = hits;
    },
  });
  F.hover(d.stage, () => tip.hits, d.c);
})();
};
