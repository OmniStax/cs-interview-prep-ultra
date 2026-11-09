/* Figures for section 1.2 Logarithms, factorials and harmonic numbers. Boots against the section's text article.
   Three still Sims, each a property and not a procedure, so none has a code panel (config item 16): the
   divisions that count a logarithm, the error factor of Stirling's Approximation, and the two rectangle
   pictures that bound H_k (ODS's Figure 7.2, its two panels behind the original toggle). Logarithms,
   factorials and harmonic numbers are untyped (RULES, Types): everything is in ink, and F.cat(0) tells the
   integral or the exact value apart from the ink it is compared with. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['1.2'] = function (root, F) {
const { PAL, alpha, text, line, dot, begin, tex, ctl, choice, register, fmt, topline, axes, plot, shade, hover, tween } = F;
const sim = (id, H) => F.sim(root, id, H);
const SUP = (s) => String(s).split('').map((c) => '⁰¹²³⁴⁵⁶⁷⁸⁹⁻'['0123456789-'.indexOf(c)] ?? c).join('');
const SUB = (s) => String(s).split('').map((c) => '₀₁₂₃₄₅₆₇₈₉'['0123456789'.indexOf(c)] ?? c).join('');
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};
/* a number to s significant digits, as plain text and without a trailing ".0" */
const sig = (x, s = 3) => {
  if (x === 0) return '0';
  if (Number.isInteger(x) && Math.abs(x) < 1e7) return String(x);
  if (Math.abs(x) >= 10 ** s && Math.abs(x) < 1e7) return String(Math.round(x));
  const e = Math.floor(Math.log10(Math.abs(x)));
  if (e >= 7) { const m = x / 10 ** e; return `${m.toFixed(s - 1)} × 10${SUP(e)}`; }
  return x.toFixed(Math.max(0, s - 1 - e)).replace(/(\.\d*?)0+$/, '$1').replace(/\.$/, '');
};

/* ================================================================ sim-halving: log_b k as a count of divisions (still) */
(function () {
  const d = sim('sim-halving', 640);
  /* the slider moves k over six decades, so it runs on log₁₀ k; the detents are the plan's 8, 1000 and 10⁶ */
  const sK = ctl(d.controls, { label: '\\log_{10} k', cls: '', key: 'k', min: 0, max: 6, step: 0.01, value: 3, unit: '', dec: 2,
    detents: [{ v: Math.log10(8), label: '8' }, { v: 3, label: '1000' }, { v: 6, label: '10⁶' }] });
  const BASES = { two: { b: 2, name: '2', tex: '2', verb: 'halved' }, e: { b: Math.E, name: 'e', tex: 'e', verb: 'divided by e' }, ten: { b: 10, name: '10', tex: '10', verb: 'divided by 10' } };
  const base = choice(d.controls, { label: 'b', key: 'base', value: 'two',
    options: [{ value: 'two', label: '2' }, { value: 'e', label: 'e' }, { value: 'ten', label: '10' }] });
  const xs = tween(d, 11), ys = tween(d, 3.6), want = { x: 0, y: 0 };
  let hits = [], first = true;
  hover(d.stage, () => hits);
  function draw() {
    const { ctx } = begin(d.c);
    const k = Math.max(1, Math.round(10 ** sK.v)), B = BASES[base.value], b = B.b;
    const vals = [k];
    while (vals[vals.length - 1] > 1 + 1e-12) vals.push(vals[vals.length - 1] / b);
    const n = vals.length - 1, L = Math.log(k) / Math.log(b), last = vals[n];
    const times = n === 1 ? 'once' : `${n} times`;
    topline(ctx, k === 1
      ? `1 is already at most 1: no division is needed, and log${SUB(B.name === 'e' ? '' : B.name)}${B.name === 'e' ? 'ₑ' : ''} 1 = 0.`
      : `${k} ${B.verb} ${times} is ${sig(last, 3)}, the first value at most 1: log${B.name === 'e' ? 'ₑ' : SUB(B.name)} ${k} = ${fmt(L, 2)}.`);

    /* the frame: values on a log scale, so every division by b is the same step down. It fits the bars drawn:
       the x-axis runs one slot past the last division and the y-axis just over k, easing when either changes. */
    const wx = Math.max(3, n + 1), wy = Math.max(1, Math.log10(k)) + 0.8;
    if (wx !== want.x) { want.x = wx; if (first) xs.set(wx); else xs.to(wx, 450); }
    if (wy !== want.y) { want.y = wy; if (first) ys.set(wy); else ys.to(wy, 450); }
    first = false;
    const box = { l: 130, r: 1340, t: 110, b: 540 };
    const ax = axes(ctx, box, [0, xs.v + 0.2], [-1.15, ys.v], { nx: 0, ny: 0, xl: 'divisions by b', yl: 'value (log scale)' });
    const X = (i) => ax.X(i + 0.6), Y = ax.Y;
    for (let e = -1; e <= Math.floor(ys.v); e += 1) {
      if (e > -1) line(ctx, box.l, Y(e), box.r, Y(e), PAL.rule, 1.5);
      text(ctx, e === 0 ? '1' : e === 1 ? '10' : e === 2 ? '100' : e === 3 ? '1000' : `10${SUP(e)}`, box.l - 14, Y(e), PAL.muted, { size: 17, align: 'right' });
    }
    const every = xs.v > 14 ? 2 : 1;
    for (let i = 0; i <= Math.floor(xs.v - 0.4); i += every) text(ctx, String(i), X(i), box.b + 26, PAL.muted, { size: 17, align: 'center' });
    /* the level 1, dashed */
    line(ctx, box.l, Y(0), box.r, Y(0), PAL.ink, 2.5, [10, 10]);

    /* the bars: value k / bⁱ after i divisions, standing on the level 1 (the last one at or below it) */
    const slot = X(1) - X(0), w = Math.min(90, slot * 0.62), top = (v) => Y(Math.log10(v));
    hits = [];
    const labelAll = n <= 10;
    vals.forEach((v, i) => {
      const x = X(i) - w / 2, y0 = Y(0), y1 = top(v), isLast = i === n;
      rect(ctx, x, Math.min(y0, y1), w, Math.max(2, Math.abs(y1 - y0)), alpha(PAL.ink, isLast ? 0.42 : 0.12), PAL.ink, 2);
      const name = `${i === 0 ? 'k' : `k / ${B.name}${i > 1 ? SUP(i) : ''}`} = ${sig(v, 3)}`;
      hits.push({ x: X(i), y: (y0 + y1) / 2, r: Math.max(w / 2, 18), name });
      if (labelAll || i === 0 || isLast) {
        const above = v > 1;
        text(ctx, sig(v, 3), X(i), above ? y1 - 18 : Math.max(y0, y1) + 22, PAL.ink, { size: 20, align: 'center', weight: isLast ? 600 : 400, bg: PAL.panel });
      }
    });
    /* the same fall as a straight line, crossing the level 1 at x = log_b k; its value is written below the
       level, left of the crossing, clear of the last bar's label */
    if (k > 1) {
      const col = F.cat(0);
      line(ctx, X(0), top(k), X(L), Y(0), col, 3, [6, 8]);
      dot(ctx, X(L), Y(0), col, true, 9);
      const lab = `log${B.name === 'e' ? 'ₑ' : SUB(B.name)} k = ${fmt(L, 2)}`;
      text(ctx, lab, Math.min(X(L) - 14, X(n) - 48), Y(0) + 34, col, { size: 22, weight: 600, align: 'right', bg: PAL.panel });
    }
    const lk = Math.log(k), lb = Math.log(b);
    tex(d.readout, `\\log_{${B.tex}} ${k} = \\frac{\\ln ${k}}{\\ln ${B.tex}} = \\frac{${sig(lk, 4)}}{${sig(lb, 4)}} = ${fmt(L, 2)},\\qquad \\lceil ${fmt(L, 2)} \\rceil = ${n} \\text{ division${n === 1 ? '' : 's'}}`);
  }
  register(d.fig, { update: () => {}, draw });
})();

/* ================================================================ sim-stirling: the factor e^α(n) and α(n)'s bounds (still) */
(function () {
  const d = sim('sim-stirling', 600);
  const sN = ctl(d.controls, { label: 'n', cls: '', key: 'n', min: 1, max: 60, step: 1, value: 10, unit: '', dec: 0 });
  /* ln n! summed exactly enough (the last bit of 189 is 3·10⁻¹⁴, against an α of 1.4·10⁻³ at n = 60) */
  const lnFact = [0];
  for (let i = 1; i <= 60; i += 1) lnFact.push(lnFact[i - 1] + Math.log(i));
  const lnS = (n) => 0.5 * Math.log(2 * Math.PI * n) + n * Math.log(n) - n;
  const alphaOf = (n) => lnFact[n] - lnS(n);
  /* 1/(12n + 1) < α(n) < 1/(12n) is 12n < 1/α(n) < 12n + 1: the graph plots 1/α(n) − 12n, which lies in (0, 1) */
  const gap = (n) => 1 / alphaOf(n) - 12 * n;
  let hits = [];
  hover(d.stage, () => hits);
  const big = (lnv) => {
    const e = Math.floor(lnv / Math.LN10), m = Math.exp(lnv - e * Math.LN10);
    return e < 7 ? String(Number(Math.exp(lnv).toPrecision(7))) : `${m.toFixed(4)} × 10${SUP(e)}`;
  };
  function draw() {
    const { ctx } = begin(d.c);
    const n = Math.round(sN.v), a = alphaOf(n), factor = Math.exp(a);
    let f = 1n; for (let i = 2n; i <= BigInt(n); i += 1n) f *= i;     /* n! exactly, written out up to 20! */
    const exact = n <= 20 ? String(f) : big(lnFact[n]);
    topline(ctx, `At n = ${n}, Stirling’s formula gives ${big(lnS(n))} for ${n}! = ${exact}, off by a factor e^{α(${n})} = ${factor.toFixed(4)}.`);

    const box = { l: 130, r: 1080, t: 130, b: 510 };
    const ax = axes(ctx, box, [0, 61], [-0.1, 1.1], { nx: 0, ny: 0, xl: 'n', yl: '1/α(n) − 12n' });
    const { X, Y } = ax;
    [0, 10, 20, 30, 40, 50, 60].forEach((v) => { line(ctx, X(v), box.t, X(v), box.b, PAL.rule, 1.5); text(ctx, String(v), X(v), box.b + 26, PAL.muted, { size: 17, align: 'center' }); });
    [0, 0.5, 1].forEach((v) => text(ctx, fmt(v, v === 0.5 ? 1 : 0), box.l - 14, Y(v), PAL.muted, { size: 17, align: 'right' }));
    /* the band the bounds allow, and its two edges named by the bound each one is */
    rect(ctx, box.l, Y(1), box.r - box.l, Y(0) - Y(1), alpha(PAL.ink, 0.06));
    line(ctx, box.l, Y(0), box.r, Y(0), PAL.ink, 2.5, [10, 10]);
    line(ctx, box.l, Y(1), box.r, Y(1), PAL.ink, 2.5, [10, 10]);
    text(ctx, 'α(n) = 1/(12n)', box.r + 16, Y(0), PAL.ink, { size: 22, weight: 600 });
    text(ctx, 'α(n) = 1/(12n + 1)', box.r + 16, Y(1), PAL.ink, { size: 22, weight: 600 });
    text(ctx, 'α(n) lies strictly between', box.r + 16, Y(0.5), PAL.muted, { size: 20 });

    hits = [];
    const col = F.cat(0);
    for (let m = 1; m <= 60; m += 1) {
      const g = gap(m);
      hits.push({ x: X(m), y: Y(g), r: 12, name: `n = ${m}: α(n) = ${alphaOf(m).toPrecision(5)}` });
      if (m !== n) dot(ctx, X(m), Y(g), alpha(PAL.ink, 0.55), true, 5);
    }
    const g = gap(n);
    line(ctx, X(n), Y(g), X(n), box.b, alpha(PAL.ink, 0.4), 2, [4, 8]);
    dot(ctx, X(n), Y(g), col, true, 10);
    const lab = `${fmt(g, 3)}`, right = X(n) + 90 < box.r;
    text(ctx, lab, right ? X(n) + 16 : X(n) - 16, Y(g) - 22, col, { size: 22, weight: 600, align: right ? 'left' : 'right', bg: PAL.panel });

    /* one display, two rows: the ratio, then α(n) between its bounds with enough digits to see it inside them */
    tex(d.readout, `\\begin{gathered}\\frac{${n}!}{\\sqrt{2\\pi\\cdot ${n}}\\,(${n}/e)^{${n}}} = e^{\\alpha(${n})} = ${factor.toFixed(7)} \\\\[4pt]`
      + ` \\tfrac{1}{${12 * n + 1}} = ${(1 / (12 * n + 1)).toPrecision(7)} < \\alpha(${n}) = ${a.toPrecision(7)} < \\tfrac{1}{${12 * n}} = ${(1 / (12 * n)).toPrecision(7)}\\end{gathered}`, true);
  }
  register(d.fig, { update: () => {}, draw });
})();

/* ================================================================ sim-harmonic: H_k between ln k and ln k + 1 (still) */
(function () {
  const d = sim('sim-harmonic', 640);
  const sK = ctl(d.controls, { label: 'k', cls: '', key: 'k', min: 1, max: 20, step: 1, value: 5, unit: '', dec: 0,
    specials: [{ at: 1, label: 'H₁ = ln 1 + 1' }] });
  const bound = choice(d.controls, { label: '\\text{bound}', key: 'bound', value: 'lower',
    options: [{ value: 'lower', label: 'lower' }, { value: 'upper', label: 'upper' }] });
  /* the x-axis runs to k + 1, where the last lower-bound rectangle ends; it eases to a new k rather than jumping */
  const xr = tween(d, 6);
  let want = 6, hits = [];
  hover(d.stage, () => hits);
  const H = (k) => { let s = 0; for (let i = 1; i <= k; i += 1) s += 1 / i; return s; };
  function draw() {
    const { ctx } = begin(d.c);
    const k = Math.round(sK.v), Hk = H(k), lk = Math.log(k);
    if (k + 1 !== want) { want = k + 1; xr.to(want, 450); }
    topline(ctx, k === 1
      ? 'H₁ = 1 lies above ln 1 = 0 and meets ln 1 + 1 = 1, the one k where the upper bound is reached.'
      : `H${SUB(k)} = ${fmt(Hk, 2)} lies between ln ${k} = ${fmt(lk, 2)} and ln ${k} + 1 = ${fmt(lk + 1, 2)}.`);

    const box = { l: 110, r: 1340, t: 110, b: 540 };
    const ax = axes(ctx, box, [0, xr.v + 0.15], [0, 1.12], { nx: 0, ny: 0, xl: 'x' });
    const { X, Y } = ax;
    const every = xr.v > 12 ? 2 : 1;
    for (let i = 0; i <= Math.floor(xr.v + 0.15); i += 1) if (i % every === 0 || i === 1) text(ctx, String(i), X(i), box.b + 26, PAL.muted, { size: 17, align: 'center' });
    [[1, '1'], [0.5, '1/2'], [1 / 3, '1/3']].forEach(([v, s]) => { line(ctx, box.l, Y(v), box.r, Y(v), PAL.rule, 1.5); text(ctx, s, box.l - 14, Y(v), PAL.muted, { size: 17, align: 'right' }); });

    /* ln k: the area under 1/x from 1 to k */
    const col = F.cat(0), f = (x) => 1 / x;
    if (k > 1) shade(ctx, ax, f, 0, 1, k, col, { alpha: 0.3 });
    plot(ctx, ax, f, col, { x: [1, xr.v + 0.15] });
    /* H_k: k rectangles of width 1 and heights 1, 1/2, …, 1/k; the lower bound stands them on [i, i + 1], over the
       curve, the upper on [i − 1, i], under it after the first. Choosing the other slides them one place. */
    const off = bound.mix((v) => (v === 'lower' ? 1 : 0));
    hits = [];
    for (let i = 1; i <= k; i += 1) {
      const x0 = X(i - 1 + off), x1 = X(i + off), y = Y(1 / i);
      rect(ctx, x0, y, x1 - x0, Y(0) - y, alpha(PAL.ink, 0.07), PAL.ink, 2.5);
      hits.push({ x: (x0 + x1) / 2, y: (y + Y(0)) / 2, r: Math.max(14, (x1 - x0) / 2), name: `rectangle ${i}: width 1, height 1/${i}` });
    }
    /* what the two kinds of area are, once each */
    const lx = box.r - 380, ly = box.t + 8;
    rect(ctx, lx, ly, 34, 24, alpha(PAL.ink, 0.07), PAL.ink, 2.5);
    text(ctx, `rectangles: total area H${SUB(k)}`, lx + 48, ly + 12, PAL.ink, { size: 22 });
    rect(ctx, lx, ly + 40, 34, 24, alpha(col, 0.3), null);
    text(ctx, `shaded: area ln ${k}`, lx + 48, ly + 52, col, { size: 22, weight: 600 });
    const cx = Math.min(1.6, xr.v * 0.2) + 1;
    text(ctx, 'y = 1/x', X(cx) + 12, Y(1 / cx) - 14, col, { size: 22, weight: 600, bg: PAL.panel });

    tex(d.readout, bound.value === 'lower'
      ? `H_{${k}} = ${fmt(Hk, 2)} > \\int_1^{${k}} \\frac{\\mathrm{d}x}{x} = \\ln ${k} = ${fmt(lk, 2)}`
      : `H_{${k}} = 1 + ${fmt(Hk - 1, 2)} \\le 1 + \\int_1^{${k}} \\frac{\\mathrm{d}x}{x} = 1 + \\ln ${k} = ${fmt(1 + lk, 2)}`);
  }
  register(d.fig, { update: () => {}, draw });
})();
};
