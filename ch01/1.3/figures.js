/* Figures for section 1.3 Asymptotic notation. Boots against the section's text article.
   Three still Sims over graphs (a property, not a procedure: no code panel, RULES "Code beside the visual")
   and one debugger figure, sim-loop-count, whose panel is ODS's Simple.snippet(): its Java and C++ as ODS
   prints them (between the generated markers below, written by inline_code.py from the source cache), its
   Python and JavaScript AI translations (METHOD decision 20). The trace is the figure's own JS copy of the
   Python. Logarithms are to base 2, as ODS writes log. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['1.3'] = function (root, F) {
const { C, PAL, alpha, text, line, dot, begin, tex, ctl, choice, register, fmt, topline, axes, plot } = F;
const sim = (id, H) => F.sim(root, id, H);
const AI = 'claude-opus-5-5 high';
const lg = (x) => Math.log2(x);
const commas = (n) => String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2, dash) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};
/* a dashed line on the graph from (x1, y1) to (x2, y2), clipped to its box */
const dashed = (ctx, ax, f, a, b, color, w = 4) => {
  ctx.save(); ctx.beginPath(); ctx.rect(ax.box.l, ax.box.t, ax.box.r - ax.box.l, ax.box.b - ax.box.t); ctx.clip();
  ctx.strokeStyle = color; ctx.lineWidth = w; ctx.setLineDash([14, 10]); ctx.beginPath();
  for (let k = 0; k <= 160; k += 1) { const x = a + ((b - a) * k) / 160, X = ax.X(x), Y = ax.Y(f(x)); if (k) ctx.lineTo(X, Y); else ctx.moveTo(X, Y); }
  ctx.stroke(); ctx.restore();
};
const kc = (s) => `\\htmlClass{kv-cost}{${s}}`, ks = (s) => `\\htmlClass{kv-size}{${s}}`;
const tn = (n) => commas(n).replace(/,/g, '{,}');

/* ================================================================ sim-big-o-witness: c and n₀ for ODS's example */
(function () {
  const f = (n) => (n <= 0 ? -200 : 5 * n * lg(n) + 8 * n - 200);
  const g = (n) => (n <= 0 ? 0 : n * lg(n));
  /* the first integer n ≥ n0 where f(n) > c·g(n), or null when there is none (f − c·g = (5 − c) n log n + 8n − 200:
     for c > 5 the failures form one stretch that ends where 8 − 200/n = (c − 5) log n, past its peak at n* = 200 ln 2/(c − 5)) */
  const over = (n, c) => f(n) > c * g(n) + 1e-9;
  const firstFail = (c, n0) => {
    for (let n = n0; n <= n0 + 20000; n += 1) if (over(n, c)) return n;
    if (c <= 5) return null;
    const peak = (200 * Math.LN2) / (c - 5);
    if (peak <= n0 + 20000 || !over(Math.round(peak), c)) return null;
    let lo = n0 + 20000, hi = Math.round(peak);
    while (hi - lo > 1) { const m = Math.floor((lo + hi) / 2); if (over(m, c)) hi = m; else lo = m; }
    return hi;
  };
  /* the smallest n0 that works: one past the end of the failing stretch (log₂ n searched up to 200) */
  const leastN0 = (c) => {
    if (c <= 5) return null;
    const phi = (t) => { const n = 2 ** t; return 8 - 200 / n - (c - 5) * t; };
    const tPeak = Math.log2(Math.max(1, (200 * Math.LN2) / (c - 5)));
    if (phi(tPeak) <= 0) { let last = 0; for (let n = 1; n <= 4096; n += 1) if (over(n, c)) last = n; return last + 1; }
    let lo = tPeak, hi = 200;
    if (phi(hi) > 0) return null;
    for (let k = 0; k < 80; k += 1) { const m = (lo + hi) / 2; if (phi(m) > 0) lo = m; else hi = m; }
    const b = 2 ** hi; if (b > 1e6) return null;
    let n = Math.floor(b) + 1; while (n > 2 && !over(n - 1, c)) n -= 1;
    return n;
  };
  const d = sim('sim-big-o-witness', 620);
  const sc = ctl(d.controls, { label: 'c', cls: '', key: 'c', min: 1, max: 20, step: 0.1, value: 13, unit: '', dec: 1,
    detents: [{ v: 5, label: '5' }], specials: [{ at: 13, label: 'c = 13' }] });
  const sn = ctl(d.controls, { label: 'n_0', cls: 'size', key: 'n0', min: 1, max: 64, step: 1, value: 2, unit: '', dec: 0,
    specials: [{ at: 2, label: 'n₀ = 2' }, { at: () => { const m = leastN0(sc.v); return m !== null && m <= 64 && m !== 2 ? m : null; }, label: 'least n₀' }] });
  /* axes fixed: n from 0 to 128 (twice the largest n0), the values from −500 to 12 000 (f(128) ≈ 5300, 13 · 128 log 128 ≈ 11 650) */
  const XR = [0, 128], YR = [-500, 12000];
  function draw() {
    const { ctx } = begin(d.c);
    const c = sc.v, n0 = sn.v, fail = firstFail(c, n0), cost = C('cost'), size = C('size');
    const box = { l: 150, r: 1330, t: 110, b: 520 };
    if (fail === null) topline(ctx, `With c = ${fmt(c, 1)} and n₀ = ${n0}, 5n log n + 8n − 200 stays at or under ${fmt(c, 1)} · n log n for every n ≥ ${n0}.`);
    else topline(ctx, `With c = ${fmt(c, 1)}, 5n log n + 8n − 200 rises above ${fmt(c, 1)} · n log n at n = ${commas(fail)}, so n₀ = ${n0} does not work.`);
    const ax = axes(ctx, box, XR, YR, { nx: 8, ny: 4, nice: true, xl: 'n', xc: size, yl: 'operations', yc: cost, fy: (v) => commas(v) });
    /* the stretch n ≥ n₀ that the definition speaks about */
    ctx.save(); ctx.fillStyle = alpha(size, 0.09); ctx.fillRect(ax.X(n0), box.t, box.r - ax.X(n0), box.b - box.t); ctx.restore();
    line(ctx, ax.X(n0), box.t, ax.X(n0), box.b, size, 3, [6, 8]);
    text(ctx, `n₀ = ${n0}`, Math.min(box.r - 60, ax.X(n0) + 10), box.t + 18, size, { size: 22, weight: 600 });
    /* where f rises above c · n log n past n₀, the gap between them is the broken part, shaded */
    let run = null;
    const runs = [];
    for (let n = Math.max(1, n0); n <= 128; n += 0.25) { if (over(n, c)) { if (!run) run = [n, n]; run[1] = n; } else if (run) { runs.push(run); run = null; } }
    if (run) runs.push(run);
    runs.forEach(([a, b]) => F.shade(ctx, ax, f, (n) => c * g(n), a, Math.max(b, a + 0.25), PAL.bad, { alpha: 0.3 }));
    plot(ctx, ax, f, cost, { w: 5, x: [0.5, 128] });
    dashed(ctx, ax, (n) => c * g(n), 1, 128, cost, 4);
    /* names at the right edge, kept apart */
    /* names at n = 100, f's below its curve and c · n log n's above, or the other way round where they have crossed */
    const yf = ax.Y(f(100)), yg = ax.Y(c * g(100)), fUp = yf < yg;
    text(ctx, 'f(n)', ax.X(100), Math.min(box.b - 14, yf + (fUp ? -30 : 30)), cost, { size: 22, weight: 600, align: 'center', bg: PAL.panel });
    text(ctx, `${fmt(c, 1)} · n log n`, ax.X(100), Math.max(box.t + 14, yg + (fUp ? 30 : -30)), cost, { size: 22, weight: 600, align: 'center', bg: PAL.panel });
    if (fail !== null) {
      const p = F.pinned(ctx, box, ax.X, ax.Y, fail, f(fail), PAL.bad, fail > 128 ? `n = ${commas(fail)}` : undefined);
      if (!p.out) { line(ctx, p.x, p.y, p.x, box.b, PAL.bad, 2, [4, 8]); text(ctx, `first n past n₀ where it fails: ${fail}`, Math.min(box.r - 170, Math.max(box.l + 170, p.x)), Math.max(box.t + 40, p.y - 40), PAL.bad, { size: 22, weight: 600, align: 'center', bg: PAL.panel }); }
    }
    const tail = fail === null
      ? `\\text{for all } ${ks('n \\ge n_0')}:\\ \\text{holds}`
      : `\\text{fails at } n = ${tn(fail)}:\\ ${kc(`f(${tn(fail)}) = ${tn(f(fail))}`)} > ${kc(`${fmt(c, 1)}\\cdot ${tn(fail)}\\log ${tn(fail)} = ${tn(c * g(fail))}`)}`;
    tex(d.readout, `${kc('f(n)')} \\le c\\cdot ${kc('n\\log n')}\\ ${tail}`);
  }
  register(d.fig, { update: () => {}, draw });
})();

/* ================================================================ sim-loop-count: ODS's Simple.snippet(), counted */
(function () {
  /* BEGIN generated by inline_code.py: ODS's Simple.snippet() as java/junk/Simple.java and cpp/Simple.h print it */
  const ODS_JAVA = "public static void snippet() {\n    for (int i = 0; i < n; i++)\n        a[i] = i;\n}";
  const ODS_CPP = "template<class T>\nvoid  Simple<T>::snippet() {\n    for (int i = 0; i < n; i++)\n        a[i] = i;\n}";
  /* END generated */
  /* Python's for … in range hides the test and the increment, so the translation keeps the C-style loop's three
     parts as statements of their own */
  const PY = [
    'def snippet(a, n):',
    '    i = 0',
    '    while i < n:',
    '        a[i] = i',
    '        i += 1',
  ].join('\n');
  const JS = [
    'function snippet(a, n) {',
    '  for (let i = 0; i < n; i++)',
    '    a[i] = i;',
    '}',
  ].join('\n');
  const MAP_J = { 1: 1, 2: 2, 3: 2, 4: 3, 5: 2 }, MAP_C = { 1: 2, 2: 3, 3: 3, 4: 4, 5: 3 };
  const run = (n) => F.trace((at) => {
    const a = new Array(n).fill(null);
    let asg = 0, cmp = 0, inc = 0, off = 0, sto = 0;
    let i = 0; asg += 1; at(2, { i, n, a, asg, cmp, inc, off, sto }, ['assign']);
    for (;;) {
      cmp += 1; at(3, { i, n, a, asg, cmp, inc, off, sto }, ['compare', i < n]);
      if (!(i < n)) break;
      a[i] = i; off += 1; sto += 1; at(4, { i, n, a, asg, cmp, inc, off, sto }, ['store', i]);
      i += 1; inc += 1; at(5, { i, n, a, asg, cmp, inc, off, sto }, ['increment']);
    }
  });
  const d = sim('sim-loop-count', 860);
  const code = F.code(d, {
    src: { python: PY, java: ODS_JAVA, cpp: ODS_CPP, javascript: JS }, ai: { python: AI, javascript: AI },
    lineMap: { java: MAP_J, cpp: MAP_C, javascript: MAP_J },
    blocks: [
      { id: 'init', lines: [2, 2], label: 'one assignment, i ← 0', touches: ['i'] },
      { id: 'pass', lines: [3, 5], label: 'one pass of the loop', touches: ['i', 'a'] },
      { id: 'test', lines: [3, 3], label: 'compare i with n', touches: ['i', 'n'] },
      { id: 'store', lines: [4, 4], label: 'find a[i] and store i in it', touches: ['a', 'i'] },
      { id: 'step', lines: [5, 5], label: 'increment i', touches: ['i'] },
    ],
    refs: { i: () => F.ref('i') },
  });
  let dbg = null;
  const sn = ctl(d.controls, { label: 'n', cls: 'size', key: 'n', min: 1, max: 16, step: 1, value: 5, unit: '', dec: 0,
    detents: [{ v: 5, label: '5' }], onInput: () => { if (dbg) dbg.set(run(sn.v)); } });
  const ROWS = [
    ['asg', 'assignments', 'i ← 0', () => '1'],
    ['cmp', 'comparisons', 'i < n', (n) => `n + 1 = ${n + 1}`],
    ['inc', 'increments', 'i++', (n) => `n = ${n}`],
    ['off', 'array offsets', 'a[i]', (n) => `n = ${n}`],
    ['sto', 'indirect assignments', 'a[i] ← i', (n) => `n = ${n}`],
  ];
  const HOT = { assign: 'asg', compare: 'cmp', store: ['off', 'sto'], increment: 'inc' };
  dbg = F.debug(d, {
    code, trace: run(5), watch: ['i', 'n'],
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const v = g.frame.vars, n = v.n, A = v.a || [], ci = F.ref('i'), cost = C('cost'), size = C('size'), idx = C('index'), key = C('key');
      const i = typeof v.i === 'number' ? v.i : 0, ev = g.frame.ev || [], line3 = g.frame.line === 3;
      const done = line3 && ev[1] === false;
      if (g.frame.line === 2) topline(ctx, 'One assignment sets i to 0 before the first test.');
      else if (done) topline(ctx, `i = ${i} is not less than n = ${n}: the last comparison ends the loop after ${n} passes.`);
      else if (line3) topline(ctx, `Comparison ${v.cmp}: i = ${i} < n = ${n}, so pass ${i + 1} runs.`);
      else if (g.frame.line === 4) topline(ctx, `The offset of a[${i}] is computed and ${i} is stored there.`);
      else topline(ctx, `i is incremented to ${i}.`);
      /* the array, its filled prefix a[0..i) shaded in the index tint, i pointing at the cell it is on */
      const filled = A.filter((x) => x !== null).length;
      const S = F.ds.strip(ctx, { y: 230, w: 1240, cell: 84, h: 70, name: 'a', values: A.map((x) => (x === null ? '' : x)), size: 30 });
      if (filled > 0) F.ds.region(ctx, S, { from: 0, to: filled - 1, color: idx, kind: 'shade', alpha: 0.16 });
      const at = Math.min(g.num('i'), n);
      F.ds.pointer(ctx, S, [{ at, name: 'i', color: ci }], { side: 'above', size: 30 });
      if (g.frame.line === 4) rect(ctx, S.x(i) - S.cell / 2 + 3, S.t + 3, S.cell - 6, S.b - S.t - 6, null, key, 5);
      text(ctx, `a[0..${filled}) filled`, 90, S.b + 70, idx, { size: 26 });
      text(ctx, `n = ${n}`, 1310, S.b + 70, size, { size: 26, weight: 600, align: 'right' });
      /* the five counts, each against what it reaches when the loop is done */
      /* the counts the step raised: one at the finest level, every count a whole pass raised at the coarsest */
      const pv = g.prev.vars, hot = ['asg', 'cmp', 'inc', 'off', 'sto'].filter((k) => g.prev !== g.frame && (v[k] || 0) > (pv[k] || 0));
      if (!hot.length) [].concat(HOT[ev[0]] || []).forEach((k) => hot.push(k));
      const y0 = 430, row = 62;
      text(ctx, 'operation', 90, y0 - 50, PAL.muted, { size: 26 });
      text(ctx, 'count', 640, y0 - 50, PAL.muted, { size: 26, align: 'right' });
      text(ctx, 'when the loop ends', 720, y0 - 50, PAL.muted, { size: 26 });
      ROWS.forEach(([k, name, code, end], r) => {
        const y = y0 + r * row, on = hot.includes(k);
        if (on) rect(ctx, 70, y - row / 2 + 4, 1260, row - 8, alpha(cost, 0.12), null);
        text(ctx, name, 90, y, PAL.ink, { size: 28, weight: on ? 600 : 400 });
        text(ctx, code, 420, y, PAL.muted, { size: 26 });
        text(ctx, String(v[k] ?? 0), 640, y, cost, { size: 32, weight: 600, align: 'right' });
        text(ctx, end(n), 720, y, cost, { size: 28 });
      });
      const total = ['asg', 'cmp', 'inc', 'off', 'sto'].reduce((s, k) => s + (v[k] || 0), 0);
      const yt = y0 + ROWS.length * row + 18;
      line(ctx, 70, yt - 30, 1330, yt - 30, PAL.rule, 2);
      text(ctx, 'total', 90, yt + 6, PAL.ink, { size: 30, weight: 600 });
      text(ctx, String(total), 640, yt + 6, cost, { size: 34, weight: 600, align: 'right' });
      text(ctx, `4n + 2 = ${4 * n + 2}`, 720, yt + 6, cost, { size: 30, weight: 600 });
    },
  });
})();

/* ================================================================ sim-crossover: 15n against 2n log n, one zoom */
(function () {
  const f1 = (n) => 15 * n, f2 = (n) => 2 * n * lg(n), CROSS = 2 ** 7.5;
  const d = sim('sim-crossover', 600);
  const sw = ctl(d.controls, { label: '\\log_{10} n_{\\max}', cls: 'size', key: 'window', min: 2, max: 4, step: 0.01, value: 2, unit: '', dec: 2,
    detents: [{ v: 2, label: '100' }, { v: 4, label: '10 000' }], specials: [{ at: Math.log10(CROSS), label: 'n ≈ 181' }] });
  function draw() {
    const { ctx } = begin(d.c);
    const N = 10 ** sw.v, c1 = F.ref('f1'), c2 = F.ref('f2'), size = C('size');
    const top = Math.max(f1(N), f2(N));
    if (N < CROSS - 0.5) topline(ctx, `Up to n = ${commas(N)}, 15n stays above 2n log n.`);
    else if (N < CROSS + 0.5) topline(ctx, 'At n = 2^{7.5} ≈ 181, 15n and 2n log n are equal: log n = 7.5.');
    else topline(ctx, `15n and 2n log n cross at n ≈ 181; by n = ${commas(N)}, 2n log n is ${fmt(f2(N) / f1(N), 2)} times 15n.`);
    const box = { l: 170, r: 1330, t: 100, b: 500 };
    /* the zoom: both axes follow the window (interactive-figures §2, a zoom the plan line names) */
    const ax = axes(ctx, box, [1, N], [0, top * 1.05], { nx: 5, ny: 4, nice: true, xl: 'n', xc: size, yl: 'f(n)', yc: C('cost'), fx: (v) => commas(v), fy: (v) => commas(v) });
    plot(ctx, ax, f1, c1, { w: 5 });
    plot(ctx, ax, f2, c2, { w: 5 });
    if (CROSS <= N) {
      const x = ax.X(CROSS), y = ax.Y(f1(CROSS));
      ctx.save(); ctx.setLineDash([6, 6]); ctx.strokeStyle = PAL.ink; ctx.lineWidth = 2.5; ctx.beginPath(); ctx.arc(x, y, 16, 0, 2 * Math.PI); ctx.stroke(); ctx.restore();
      line(ctx, x, y + 16, x, box.b, alpha(PAL.ink, 0.35), 2, [4, 8]);
      const right = x > box.r - 160;
      line(ctx, x + (right ? -12 : 12), y - 12, x + (right ? -40 : 40), y - 60, alpha(PAL.ink, 0.5), 2);
      text(ctx, 'n ≈ 181', x + (right ? -46 : 46), Math.max(box.t + 16, y - 72), PAL.ink, { size: 22, weight: 600, align: right ? 'right' : 'left', bg: PAL.panel });
    }
    /* each curve named at 70 % of the window, the upper one above its curve and the lower one below */
    const nx = 1 + 0.7 * (N - 1), up1 = f1(nx) >= f2(nx), lx = ax.X(nx);
    text(ctx, '15n', lx, ax.Y(f1(nx)) + (up1 ? -36 : 36), c1, { size: 24, weight: 600, align: 'center', bg: PAL.panel });
    text(ctx, '2n log n', lx, ax.Y(f2(nx)) + (up1 ? 36 : -36), c2, { size: 24, weight: 600, align: 'center', bg: PAL.panel });
    const rel = f1(N) > f2(N) + 0.5 ? '>' : f1(N) < f2(N) - 0.5 ? '<' : '=';
    tex(d.readout, `\\text{at } ${ks(`n = ${tn(N)}`)}:\\ ${kc(`f_1(n) = 15n = ${tn(f1(N))}`)}\\ ${rel}\\ ${kc(`f_2(n) = 2n\\log n = ${tn(f2(N))}`)}`);
  }
  register(d.fig, { update: () => {}, draw });
})();

/* ================================================================ sim-limit-test: where f(n)/g(n) goes */
(function () {
  const PAIRS = {
    sq: { label: 'n² vs 2n log n', f: (n) => n * n, g: (n) => 2 * n * lg(n), lim: Infinity,
      ft: 'n^2', gt: '2n\\log n', head: 'n²/(2n log n) = n/(2 log n) keeps growing: n² is in Ω(2n log n).' },
    ods: { label: '5n log n + 8n − 200 vs n log n', f: (n) => 5 * n * lg(n) + 8 * n - 200, g: (n) => n * lg(n), lim: 5,
      ft: '5n\\log n + 8n - 200', gt: 'n\\log n', head: '(5n log n + 8n − 200)/(n log n) settles towards 5: the two are Θ of each other.' },
    lin: { label: '15n vs 2n log n', f: (n) => 15 * n, g: (n) => 2 * n * lg(n), lim: 0,
      ft: '15n', gt: '2n\\log n', head: '15n/(2n log n) = 7.5/log n sinks towards 0: 15n is in O(2n log n).' },
  };
  const d = sim('sim-limit-test', 600);
  const pick = F.select(d.controls, { label: '\\text{pair}', key: 'pair', value: 'sq',
    options: Object.entries(PAIRS).map(([value, p]) => ({ value, label: p.label })) });
  const sw = ctl(d.controls, { label: '\\log_{10} n_{\\max}', cls: 'size', key: 'window', min: 1, max: 6, step: 0.01, value: 2, unit: '', dec: 2,
    detents: [{ v: 2, label: '100' }, { v: 6, label: '10⁶' }] });
  const T0 = Math.log10(2);
  const ratioAt = (p) => (t) => { const n = 10 ** t; return p.f(n) / p.g(n); };
  function draw() {
    const { ctx } = begin(d.c);
    const p = PAIRS[pick.value], T1 = sw.v, N = 10 ** T1, cost = C('cost'), size = C('size');
    topline(ctx, p.head);
    /* y follows the window: the ratio's largest value on it, and the limit where it is finite */
    let hi = 0, lo = 0;
    for (let k = 0; k <= 200; k += 1) { const t = T0 + ((T1 - T0) * k) / 200, r = ratioAt(p)(t); if (Number.isFinite(r)) { hi = Math.max(hi, r); lo = Math.min(lo, r); } }
    if (Number.isFinite(p.lim)) hi = Math.max(hi, p.lim * 1.2);
    lo = Math.max(lo, -10);
    const box = { l: 170, r: 1330, t: 100, b: 500 };
    const ax = axes(ctx, box, [T0, T1], [lo, hi * 1.08 || 1], { nx: Math.max(1, Math.round(T1 - T0)), ny: 4, nice: true, xl: 'n', xc: size, yl: 'f(n)/g(n)', yc: cost,
      fx: (t) => { const v = 10 ** t; return v >= 1e3 ? `10${'⁰¹²³⁴⁵⁶⁷⁸⁹'[Math.round(t)] || ''}` : commas(v); }, fy: (v) => (hi >= 10 ? commas(v) : fmt(v, 1)) });
    if (Number.isFinite(p.lim)) {
      dashed(ctx, ax, () => p.lim, T0, T1, cost, 3);
      text(ctx, `limit ${p.lim}`, box.l + 0.82 * (box.r - box.l), ax.Y(p.lim) + (p.lim === 0 ? -22 : 24), cost, { size: 22, weight: 600, align: 'center', bg: PAL.panel });
    }
    ctx.save(); ctx.beginPath(); ctx.rect(box.l, box.t - 6, box.r - box.l, box.b - box.t + 6); ctx.clip();
    pick.curve(ctx, (v) => ratioAt(PAIRS[v]), T0, T1, ax.X, ax.Y, cost, 5, 200);
    ctx.restore();
    const r = p.f(N) / p.g(N);
    dot(ctx, ax.X(T1), ax.Y(Math.max(lo, Math.min(r, hi * 1.08))), cost, true, 9);
    const goes = `\\text{tending to } ${p.lim === Infinity ? '\\infty' : p.lim}`;
    const verdict = p.lim === Infinity ? `${kc('f(n)')} \\in \\Omega(${kc('g(n)')})` : p.lim === 0 ? `${kc('f(n)')} \\in O(${kc('g(n)')})` : `${kc('f(n)')} = \\Theta(${kc('g(n)')})`;
    tex(d.readout, `${kc('\\tfrac{f(n)}{g(n)}')} = ${r < 100 ? fmt(r, 2) : tn(r)} \\text{ at } ${ks(`n = ${tn(N)}`)},\\ ${goes}:\\quad ${verdict}`);
  }
  register(d.fig, { update: () => {}, draw });
})();
};
