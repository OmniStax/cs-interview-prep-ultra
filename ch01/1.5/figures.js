/* Figures for section 1.5 Amortized analysis. Boots against the section's text article.
   One debugger figure (code beside the drawing, stepped by block: METHOD §2.3): the growable array of
   OI Wiki's prose, filled from capacity 1 and doubled when full, its cost read three ways. OI Wiki's own
   code-fenced credit trace is outside its licence and is not shown; the figure is drawn from the numbers
   of the prose (charge 3: 1 now and 2 banked; Φ(h) = 2n − m). OI Wiki prints no code for the array, so
   all four languages of the panel are written by the AI from the prose's description (METHOD decision 20)
   and carry the AI mark. The trace is the figure's own JS copy of the Python. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['1.5'] = function (root, F) {
const { C, PAL, alpha, text, line, dot, arrow, begin, choice, topline, hbracket, axes } = F;
const sim = (id, H) => F.sim(root, id, H);
const AI = 'claude-opus-5-5 high';
const AIS = { python: AI, java: AI, cpp: AI, javascript: AI };
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2, dash) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};
const lerp = (a, b, k) => a + (b - a) * k;

/* ================================================================ sim-pay-for-doubling */
(function () {
  const PY = [
    'class DynamicArray:',
    '    def __init__(self):',
    '        self.n = 0',
    '        self.m = 1',
    '        self.a = [None]',
    '',
    '    def insert(self, x):',
    '        if self.n == self.m:',
    '            b = [None] * (2 * self.m)',
    '            for i in range(self.n):',
    '                b[i] = self.a[i]',
    '            self.a = b',
    '            self.m = 2 * self.m',
    '        self.a[self.n] = x',
    '        self.n = self.n + 1',
  ].join('\n');
  /* Java, C++ and JavaScript: the same lines, with a closing brace after the copy loop and after the
     resize, so canonical lines 12 to 15 sit one or two lines lower */
  const braces = (head, fields, sig, alloc, swap, self) => [
    head,
    ...fields.map((f) => `    ${f}`),
    '',
    `    ${sig} {`,
    `        if (${self}n == ${self}m) {`,
    `            ${alloc}`,
    `            for (${self ? 'let' : 'int'} i = 0; i < ${self}n; i++) {`,
    `                b[i] = ${self}a[i];`,
    '            }',
    `            ${swap}`,
    `            ${self}m = 2 * ${self}m;`,
    '        }',
    `        ${self}a[${self}n] = x;`,
    `        ${self}n = ${self}n + 1;`,
    '    }',
    head.startsWith('struct') ? '};' : '}',
  ].join('\n');
  const JAVA = braces('class DynamicArray {', ['int n = 0;', 'int m = 1;', 'int[] a = new int[1];'],
    'void insert(int x)', 'int[] b = new int[2 * m];', 'a = b;', '');
  const CPP = braces('struct DynamicArray {', ['int n = 0;', 'int m = 1;', 'int* a = new int[1];'],
    'void insert(int x)', 'int* b = new int[2 * m];', 'delete[] a; a = b;', '');
  const JS = braces('class DynamicArray {', ['n = 0;', 'm = 1;', 'a = new Array(1);'],
    'insert(x)', 'const b = new Array(2 * this.m);', 'this.a = b;', 'this.')
    .replace('if (this.n == this.m)', 'if (this.n === this.m)');
  /* Python line → line in the braced languages (the class head and fields are one line higher: no def __init__) */
  const MAP = { 1: 1, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 12, 13: 13, 14: 15, 15: 16 };

  /* One run of N inserts from the empty array of capacity 1, as frames of the Python above. Besides the
     code's own variables, each frame carries what the drawing reads: the actual cost of every insert so far
     (`cost`, the one in progress last), the credit banked on each element (`coins`, the accounting method:
     an insert pays 3, 1 for writing its element and 2 left on it; a copy spends 1, taken from the elements
     inserted since the last resize, two copies from each) and the elements copied so far into b. */
  const run = (N) => F.trace((at) => {
    let n = 0, m = 1, a = [null], b = null;
    const cost = [], coins = [];
    let since = 0;                       /* the first element inserted since the last resize (0-based) */
    const snap = (x, extra) => Object.assign({ x, n, m, a: a.slice(), cost: cost.slice(), coins: coins.slice() }, extra || {});
    at(5, snap(null));
    for (let x = 1; x <= N; x += 1) {
      cost.push(0);
      at(8, snap(x), ['test', n === m]);
      if (n === m) {
        b = new Array(2 * m).fill(null); at(9, snap(x, { b: b.slice() }));
        const payers = []; for (let j = since; j < n; j += 1) payers.push(j);
        for (let i = 0; i < n; i += 1) {
          at(10, snap(x, { i, b: b.slice() }));
          b[i] = a[i]; cost[cost.length - 1] += 1;
          const p = payers[Math.min(payers.length - 1, Math.floor(i / 2))]; coins[p] -= 1;
          at(11, snap(x, { i, b: b.slice(), payer: p }), ['copy', i]);
        }
        const old = a; a = b; b = null; at(12, snap(x, { old }));
        m = 2 * m; at(13, snap(x, { old }));
        since = n;
      }
      a[n] = x; cost[cost.length - 1] += 1; coins[n] = 2; at(14, snap(x), ['put', n]);
      n = n + 1; at(15, snap(x));
    }
  });

  const d = sim('sim-pay-for-doubling', 1000);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: AIS,
    lineMap: { java: MAP, cpp: MAP, javascript: MAP },
    blocks: [
      { id: 'insert', lines: [8, 15], label: 'insert x', touches: ['x', 'n', 'm'] },
      { id: 'grow', lines: [9, 13], label: 'the array is full: double it', touches: ['m', 'i'] },
      { id: 'alloc', lines: [9, 9], label: 'make an array of twice the capacity', touches: ['m'] },
      { id: 'copy', lines: [10, 11], label: 'copy element i across', touches: ['i'] },
      { id: 'swap', lines: [12, 13], label: 'the new array replaces the old', touches: ['m'] },
      { id: 'put', lines: [14, 14], label: 'write x into cell n', touches: ['x', 'n'] },
      { id: 'count', lines: [15, 15], label: 'one more element', touches: ['n'] },
    ],
    refs: { n: () => F.ref('n'), m: () => F.ref('m'), i: () => F.ref('i') },
  });

  const INPUTS = [9, 17];
  const traces = Object.fromEntries(INPUTS.map((N) => [String(N), run(N)]));
  let method = null;

  /* the costs of a whole run, by insert k = 1 … N: actual cost, capacity after, potential, credit banked */
  const ledger = (N) => {
    const rows = []; let m = 1, total = 0;
    for (let k = 1; k <= N; k += 1) {
      const copies = k - 1 === m ? k - 1 : 0; if (copies) m *= 2;
      const c = 1 + copies; total += c;
      rows.push({ k, c, copies, m, total, phi: 2 * k - m, bank: 3 * k - total });
    }
    return rows;
  };
  const LEDGER = Object.fromEntries(INPUTS.map((N) => [String(N), ledger(N)]));

  F.debug(d, {
    code, watch: ['x', 'n', 'm', 'i'],
    inputs: INPUTS.map((N) => ({ value: String(N), label: `${N} inserts`, trace: traces[String(N)] })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx || !method) return;
      const N = +g.input, L = LEDGER[g.input];
      const v = g.frame.vars, pv = g.prev.vars, k = g.k, ln = g.frame.line;
      const cn = F.ref('n'), cm = F.ref('m'), ci = F.ref('i'), cost = C('cost'), key = C('key');
      const meth = method.value;
      const done = v.n;                                   /* inserts completed */
      const last = done ? L[done - 1] : null;
      const hits = [];

      /* ---------------- the headline */
      const growing = ln >= 9 && ln <= 13;
      const cur = v.x ? L[v.x - 1] : null;
      let head;
      if (!v.x) head = 'An empty array of capacity m = 1: Φ(h₀) = 2·0 − 1 = −1.';
      else if (meth === 'aggregate') head = growing || (cur && cur.copies && ln >= 14)
        ? `Insert ${v.x} copies all ${cur.copies} elements: the copies so far are the powers of two below ${v.x}.`
        : `${done} insert${done === 1 ? '' : 's'} cost ${last ? last.total : 0} in all, under 3n = ${3 * done}.`;
      else if (meth === 'accounting') head = cur && cur.copies
        ? `Insert ${v.x} pays 3, and the credit banked by the newer half pays for its ${cur.copies} cop${cur.copies === 1 ? 'y' : 'ies'}.`
        : `Insert ${v.x} pays 3: 1 for itself and 2 banked; the bank never runs dry.`;
      else head = cur && cur.copies
        ? `Insert ${v.x}: actual cost ${cur.c}, potential change 2 − n = ${2 - cur.copies}, amortized cost 3.`
        : `Insert ${v.x}: actual cost 1, potential change 2, amortized cost 3.`;
      topline(ctx, head);

      /* ---------------- the array: m cells, the first n filled; while it grows, the old above the new */
      const ROW = 240, NEW = 380, CH = 60;
      const layout = (cells, y) => {
        const cw = Math.min(76, 1240 / cells), x0 = 700 - (cw * cells) / 2;
        return { cw, x: (j) => x0 + j * cw, y, cells, x0, x1: x0 + cw * cells };
      };
      const oldA = v.a || [null];
      const drawRow = (Lr, vals, op, filledTo, { name, coins: coinRow } = {}) => {
        ctx.save(); ctx.globalAlpha *= op;
        const h = Math.min(CH, Lr.cw - 4 > 30 ? CH : 44);
        for (let j = 0; j < Lr.cells; j += 1) {
          const has = vals[j] !== null && vals[j] !== undefined;
          rect(ctx, Lr.x(j) + 2, Lr.y - h / 2, Lr.cw - 4, h, has ? alpha(key, 0.16) : null, has ? key : alpha(PAL.ink, 0.45), has ? 2.5 : 2);
          if (has) text(ctx, String(vals[j]), Lr.x(j) + Lr.cw / 2, Lr.y, key, { size: Lr.cw < 44 ? 20 : 26, align: 'center', base: 'middle', weight: 600 });
          if (name) hits.push({ x: Lr.x(j) + Lr.cw / 2, y: Lr.y, r: Lr.cw / 2, name: has ? `${name} cell ${j}: element ${vals[j]}` : `${name} cell ${j}: empty` });
          /* the credit banked on the element, as coins stacked over its cell (the accounting method) */
          if (coinRow && has) {
            const c = coinRow[j] || 0;
            for (let q = 0; q < c; q += 1) {
              const cy = Lr.y - h / 2 - 16 - q * 22;
              dot(ctx, Lr.x(j) + Lr.cw / 2, cy, cost, true, Math.min(9, Lr.cw / 4));
              hits.push({ x: Lr.x(j) + Lr.cw / 2, y: cy, r: 10, name: `1 unit of credit banked by insert ${vals[j]}` });
            }
          }
        }
        ctx.restore();
        return h;
      };
      const showCoins = (meth === 'accounting' ? method.a('accounting') : 0);
      if (growing) {
        /* the old array, faded once the new one replaces it, and the new one below, filling as copies land */
        const cap = ln === 13 ? v.m / 2 : v.m;              /* the old capacity: line 13 has already doubled m */
        const Lo = layout(cap, ROW);
        const swapK = ln === 12 ? (g.prev.line === 12 ? 1 : k) : ln > 12 ? 1 : 0;
        const upK = ln === 13 ? (g.prev.line === 13 ? 1 : k) : 0;
        const inK = ln === 9 && g.prev.line !== 9 ? k : 1;
        const Ln = layout(2 * cap, lerp(NEW, ROW, upK));
        const oldVals = ln <= 11 ? oldA : (v.old || []);
        drawRow(Lo, Array.from({ length: cap }, (_, j) => oldVals[j] ?? null), Math.max(0, 1 - 0.6 * swapK - 0.4 * upK), v.n,
          { name: 'old array', coins: ln < 12 && showCoins ? v.coins : null });
        const nb = ln <= 11 ? (v.b || []) : (v.a || []);
        drawRow(Ln, Array.from({ length: 2 * cap }, (_, j) => nb[j] ?? null), inK, v.n,
          { name: ln >= 12 ? 'array' : 'new array', coins: ln >= 12 && showCoins ? v.coins : null });
        /* the copy of element i travels from its old cell to its new one */
        if (ln >= 10 && ln <= 11 && v.i !== undefined) {
          const i = v.i, t = ln === 11 ? (g.prev.line === 10 && pv.i === i ? k : 1) : 0;
          const x0 = Lo.x(i) + Lo.cw / 2, y0 = ROW + CH / 2 + 4, x1 = Ln.x(i) + Ln.cw / 2, y1 = Ln.y - CH / 2 - 4;
          arrow(ctx, x0, y0, lerp(x0, x1, Math.max(0.15, t)), lerp(y0, y1, Math.max(0.15, t)), ci, 4);
          text(ctx, 'i', x0 - 16, y0 + 18, ci, { size: 24, weight: 600, italic: true, align: 'right' });
          if (ln === 10) dot(ctx, x0, ROW, ci, false, 12);
        }
        /* the capacities */
        hbracket(ctx, Lo.x0, Lo.x1, ROW - CH / 2 - (showCoins ? 66 : 14), cm, ln < 13 ? `m = ${v.m}` : `m = ${v.m}`, { side: 'above' });
        if (ln < 13) text(ctx, `2m = ${2 * v.m}`, Ln.x1 + 14, Ln.y, cm, { size: 22, weight: 600, base: 'middle' });
      } else {
        /* one row; between two inserts the cells slide from the old layout to the new */
        const mPrev = pv.m ?? v.m, Lb = layout(mPrev, ROW), La = layout(v.m, ROW);
        const kk = mPrev !== v.m ? k : 1;
        const Lr = { cw: lerp(Lb.cw, La.cw, kk), cells: v.m, y: ROW, x: (j) => lerp(j < mPrev ? Lb.x(j) : La.x(j), La.x(j), kk), x0: lerp(Lb.x0, La.x0, kk), x1: lerp(Lb.x1, La.x1, kk) };
        const h = drawRow(Lr, oldA.concat(Array(Math.max(0, v.m - oldA.length)).fill(null)).slice(0, v.m), 1, v.n, { name: 'array', coins: showCoins ? v.coins : null });
        hbracket(ctx, Lr.x0, Lr.x1, ROW - h / 2 - (showCoins ? 66 : 14), cm, `m = ${v.m}`, { side: 'above' });
        if (v.n > 0) hbracket(ctx, Lr.x0, Lr.x(v.n - 1) + Lr.cw, ROW + h / 2 + 14, cn, `n = ${v.n}`, { side: 'below' });
        else text(ctx, 'n = 0', Lr.x0, ROW + h / 2 + 40, cn, { size: 22, weight: 600 });
      }

      /* ---------------- the ledger: each insert's actual cost as a bar, and what each method keeps */
      const box = { l: 150, r: 1300, t: 560, b: 900 };
      const ys = { aggregate: [0, 3 * N], accounting: [0, N + 1], potential: [-2, N + 1] };
      const yr = method.mix((x) => ys[x]);
      const ax = axes(ctx, box, [0, N], yr, { xl: 'insert k', yl: meth === 'aggregate' ? 'cost, and the total so far' : meth === 'accounting' ? 'cost, and the credit in the bank' : 'cost, and the potential Φ', yc: cost, nx: N, ny: meth === 'aggregate' ? 3 : (N + 1 > 12 ? 3 : 4), nice: true });
      const { X, Y } = ax;
      const bw = Math.min(46, (X(1) - X(0)) * 0.55);
      const costs = v.cost || [];
      costs.forEach((c, j) => {
        const was = (pv.cost || [])[j] ?? 0, cc = lerp(was, c, k);
        if (cc <= 0) return;
        const x = X(j + 1);
        rect(ctx, x - bw / 2, Y(cc), bw, Y(0) - Y(cc), alpha(cost, 0.35), cost, 2);
        hits.push({ x, y: (Y(cc) + Y(0)) / 2, r: bw / 2 + 4, name: `insert ${j + 1}: actual cost ${c}${j < done ? '' : ' so far'}` });
      });
      const upto = L.slice(0, done);
      const poly = (pts, w, dash) => { ctx.save(); ctx.strokeStyle = cost; ctx.lineWidth = w; if (dash) ctx.setLineDash(dash); ctx.beginPath(); pts.forEach(([x, y], j) => (j ? ctx.lineTo(x, y) : ctx.moveTo(x, y))); ctx.stroke(); ctx.restore(); };
      method.only(ctx, 'aggregate', () => {
        poly([[X(0), Y(0)], [X(N), Y(3 * N)]], 3, [10, 10]);
        text(ctx, '3n', X(N) - 10, Y(3 * N) + 6, cost, { size: 22, weight: 600, align: 'right', base: 'top' });
        const pts = [[X(0), Y(0)], ...upto.map((r) => [X(r.k), Y(r.total)])];
        if (pts.length > 1) poly(pts, 5);
        upto.forEach((r) => { dot(ctx, X(r.k), Y(r.total), cost, true, 7); hits.push({ x: X(r.k), y: Y(r.total), r: 10, name: `total actual cost after ${r.k} inserts: ${r.total}` }); });
      });
      method.only(ctx, 'accounting', () => {
        poly([[X(0), Y(3)], [X(N), Y(3)]], 3, [10, 10]);
        text(ctx, 'charge 3', X(N) + 8, Y(3), cost, { size: 20, base: 'middle' });
        const pts = [[X(0), Y(0)], ...upto.map((r) => [X(r.k), Y(r.bank)])];
        if (pts.length > 1) poly(pts, 5);
        upto.forEach((r) => { dot(ctx, X(r.k), Y(r.bank), cost, true, 7); hits.push({ x: X(r.k), y: Y(r.bank), r: 10, name: `credit in the bank after ${r.k} inserts: ${r.bank}` }); });
      });
      method.only(ctx, 'potential', () => {
        poly([[X(0), Y(3)], [X(N), Y(3)]], 3, [10, 10]);
        text(ctx, 'ĉ = 3', X(N) + 8, Y(3), cost, { size: 20, base: 'middle' });
        poly([[X(0), Y(-1)], [X(N), Y(-1)]], 2, [4, 8]);
        text(ctx, 'Φ(h₀) = −1', X(N) + 8, Y(-1), cost, { size: 20, base: 'middle' });
        const pts = [[X(0), Y(-1)], ...upto.map((r) => [X(r.k), Y(r.phi)])];
        if (pts.length > 1) poly(pts, 5);
        dot(ctx, X(0), Y(-1), cost, false, 7);
        upto.forEach((r) => { dot(ctx, X(r.k), Y(r.phi), cost, true, 7); hits.push({ x: X(r.k), y: Y(r.phi), r: 10, name: `Φ after ${r.k} inserts: 2·${r.k} − ${r.m} = ${r.phi}` }); });
      });

      /* ---------------- the readout: the method's relation with the numbers of the inserts completed */
      let ro;
      if (!done) ro = meth === 'potential' ? 'Φ(h₀) = 2·0 − 1 = −1' : meth === 'accounting' ? 'charged 0 · spent 0 · banked 0 ≥ 0' : 'no inserts yet: total 0';
      else if (meth === 'aggregate') {
        const copies = last.total - done, lg = Math.ceil(Math.log2(done));
        ro = `inserts ${done} · copies ${copies} = 2^{⌈log₂ ${done}⌉} − 1 < 2n = ${2 * done} · total ${last.total} ≤ 3n = ${3 * done}`;
        if (copies !== 2 ** lg - 1) ro = `inserts ${done} · copies ${copies} · total ${last.total} ≤ 3n = ${3 * done}`;
      } else if (meth === 'accounting') ro = `charged 3·${done} = ${3 * done} · spent ${last.total} · banked ${last.bank} ≥ 0`;
      else {
        const dPhi = last.phi - (done > 1 ? L[done - 2].phi : -1);
        ro = last.copies
          ? `ĉ = c + ΔΦ = (n + 1) + (2 − n) = ${last.c} + (${dPhi}) = 3 · Φ = 2·${done} − ${last.m} = ${last.phi} ≥ −1`
          : `ĉ = c + ΔΦ = 1 + ${dPhi} = ${1 + dPhi} · Φ = 2·${done} − ${last.m} = ${last.phi} ≥ −1`;
      }
      text(ctx, ro, 700, 975, cost, { size: 24, align: 'center', bg: PAL.panel });
      tip.hits = hits;
    },
  });
  const tip = { hits: [] };
  F.hover(d.stage, () => tip.hits, d.c);
  method = choice(d.controls, {
    label: '\\text{method}', key: 'method', value: 'accounting',
    options: [{ value: 'aggregate', label: 'aggregate' }, { value: 'accounting', label: 'accounting' }, { value: 'potential', label: 'potential' }],
  });
})();
};
