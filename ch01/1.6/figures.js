/* Figures for section 1.6 Counting and expected value. Boots against the section's text article.
   Three Sims: sim-pascal (still: Pascal's triangle, Brisk Walk's Figure 6.1 as its original), sim-idol-venn (still,
   morphing on each choice: Brisk Walk's Figure 4.1 as its original) and sim-coin-tosses (a story slider over the
   runs, every run drawn from one seeded generator so that scrubbing is exact). No code panel: brisk and ODS print
   no code for these ideas (config item 16). */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['1.6'] = function (root, F) {
const { C, PAL, alpha, text, line, dot, arrow, begin, tex, ctl, choice, register, fmt, topline, measure } = F;
const sim = (id, H) => F.sim(root, id, H);
const binom = (n, k) => { if (k < 0 || k > n) return 0; let r = 1; for (let i = 1; i <= k; i += 1) r = (r * (n - k + i)) / i; return Math.round(r); };
const fact = (n) => { let r = 1; for (let i = 2; i <= n; i += 1) r *= i; return r; };
const WORDS = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'];
const word = (n) => (n < WORDS.length ? WORDS[n] : String(n));
/* a probability as Brisk Walk writes it: .4, .25, 1, 0 */
const pr = (x) => { const s = fmt(Math.round(x * 1000) / 1000, 3).replace(/0+$/, '').replace(/\.$/, ''); return s.startsWith('0.') ? s.slice(1) : s; };

/* ================================================================ sim-pascal: Pascal's triangle (still) */
(function () {
  const H = 900;
  const d = sim('sim-pascal', H);
  const sK = ctl(d.controls, { label: 'k', cls: 'size', key: 'k', min: 0, max: 4, step: 1, value: 2, unit: '', dec: 0,
    specials: [{ at: 0, label: 'k = 0' }, { at: () => sN.v / 2, label: 'k = n/2' }, { at: () => sN.v, label: 'k = n' }] });
  const sN = ctl(d.controls, { label: 'n', cls: 'size', key: 'n', min: 0, max: 12, step: 1, value: 4, unit: '', dec: 0,
    onInput: () => { sK.range({ min: 0, max: sN.v, step: 1, value: Math.min(sK.v, sN.v), unit: '', dec: 0 }); } });
  /* the n slider first, as the text sets n before k */
  d.controls.insertBefore(sN.el, sK.el);
  const ro = F.readout(d);
  function draw() {
    const { ctx } = begin(d.c);
    const n = Math.round(sN.v), k = Math.min(n, Math.round(sK.v)), v = binom(n, k);
    const row = Array.from({ length: n + 1 }, (_, j) => binom(n, j)).join(', ');
    const say = (x) => (v <= 12 ? word(x) : String(x));
    topline(ctx, `Row ${n} reads ${row}: ${v === 1 ? 'one way' : `${say(v)} ways`} to take ${say(k)} of ${say(n)}.`);
    /* the triangle, rows 0..n, scaled so that row 12 fits the width and the rows fill the height */
    const span = H - 60 - 140, dy = Math.min(84, span / Math.max(n, 1)), dx = Math.min(122, 1240 / (n + 1));
    const top = 140 + (span - n * dy) / 2;
    const size = Math.max(18, Math.min(30, dx * 0.31));
    const at = (r, j) => [700 + (j - r / 2) * dx, top + r * dy];
    const col = C('size');
    /* the two entries above the chosen one, which add up to it */
    if (n >= 1) {
      const [x, y] = at(n, k);
      [[n - 1, k - 1], [n - 1, k]].forEach(([r, j]) => {
        if (j < 0 || j > r) return;
        const [px, py] = at(r, j), len = Math.hypot(x - px, y - py), ux = (x - px) / len, uy = (y - py) / len, gap = size * 0.95;
        arrow(ctx, px + ux * gap, py + uy * gap, x - ux * gap, y - uy * gap, PAL.muted, 3);
      });
    }
    for (let r = 0; r <= n; r += 1) {
      for (let j = 0; j <= r; j += 1) {
        const [x, y] = at(r, j), val = binom(r, j);
        const chosen = r === n && j === k, mirror = r === n && j === n - k && j !== k, parent = r === n - 1 && (j === k - 1 || j === k);
        if (chosen || mirror) {
          ctx.save(); ctx.beginPath(); ctx.arc(x, y, size * 0.95, 0, 2 * Math.PI);
          if (chosen) { ctx.fillStyle = alpha(col, 0.18); ctx.fill(); }
          ctx.strokeStyle = col; ctx.lineWidth = 3; if (mirror) ctx.setLineDash([8, 7]); ctx.stroke(); ctx.restore();
        }
        text(ctx, String(val), x, y, chosen || mirror ? col : parent ? PAL.ink : r === n ? PAL.ink : PAL.muted,
          { size: Math.round(size * (String(val).length > 2 ? 0.86 : 1)), align: 'center', base: 'middle', weight: chosen || parent ? 600 : 400 });
      }
      /* the row's number at the left, for the rows the eye has to count */
      if ((r === n || r === 0) && at(r, 0)[0] - size * 1.2 > 160) text(ctx, `row ${r}`, 70, at(r, 0)[1], r === n ? col : PAL.muted, { size: 20, base: 'middle' });
    }
    const parents = n >= 1 ? (k === 0 || k === n ? `\\binom{${n - 1}}{${k === 0 ? 0 : n - 1}}` : `\\binom{${n - 1}}{${k - 1}} + \\binom{${n - 1}}{${k}}`) : '';
    const f = `\\binom{${n}}{${k}} = \\frac{${n}!}{${n - k}!\\,${k}!} = ${v}` + (parents ? ` = ${parents}` : '');
    const note = k !== n - k ? `$\\binom{${n}}{${Math.min(k, n - k)}} = \\binom{${n}}{${Math.max(k, n - k)}} = ${v}$` : '';
    ro.set(f, note);
  }
  register(d.fig, { update: () => {}, draw });
})();

/* ================================================================ sim-idol-venn: All-time Idol's events (still, morphing) */
(function () {
  const H = 800;
  const d = sim('sim-idol-venn', H);
  /* the outcomes as Brisk Walk's Figure 4.1 places them, and their probabilities */
  const OUT = [
    { id: 'kelly', name: 'Kelly', p: 0.2, x: 610, y: 470 },
    { id: 'fantasia', name: 'Fantasia', p: 0.2, x: 850, y: 270 },
    { id: 'david', name: 'David', p: 0.5, x: 330, y: 680 },
    { id: 'carrie', name: 'Carrie', p: 0.1, x: 1060, y: 690 },
  ];
  /* the events as ellipses round the outcomes they hold: [cx, cy, rx, ry, rotation] */
  const EV = {
    U: { set: ['kelly', 'fantasia'], e: [732, 365, 255, 120, -0.70], name: 'underage', lab: [545, 245] },
    F: { set: ['kelly', 'fantasia', 'carrie'], e: [870, 480, 340, 300, 0.35], name: 'a woman', lab: [1290, 320] },
    R: { set: ['kelly', 'david'], e: [470, 575, 265, 125, -0.64], name: 'rock', lab: [215, 470] },
    C: { set: ['carrie'], e: [1060, 690, 105, 70, 0], name: 'country', lab: [1060, 805] },
  };
  const evOpts = ['F', 'R', 'U', 'C'].map((v) => ({ value: v, label: v }));
  const cA = choice(d.controls, { label: 'A', key: 'a', value: 'U', options: evOpts });
  const cOp = choice(d.controls, { label: '\\text{operation}', key: 'op', value: 'given', options: [
    { value: 'or', label: 'or' }, { value: 'and', label: 'and' }, { value: 'given', label: 'given' }] });
  const cB = choice(d.controls, { label: 'B', key: 'b', value: 'F', options: evOpts });
  const ro = F.readout(d);
  const P = (s) => OUT.filter((o) => s.includes(o.id)).reduce((t, o) => t + o.p, 0);
  /* what the state shows, as numbers that can be blended: per outcome its weight (1 counted, 0.25 in play, 0 ruled out),
     per event its presence and its fill */
  const state = (a, op, b) => {
    const A = EV[a].set, B = EV[b].set;
    const inA = (o) => A.includes(o), inB = (o) => B.includes(o);
    const counted = (o) => (op === 'or' ? inA(o) || inB(o) : inA(o) && inB(o));
    const alive = (o) => (op === 'given' ? inB(o) : true);
    const w = OUT.map((o) => (!alive(o.id) ? 0 : counted(o.id) ? 1 : 0.35));
    const ev = ['F', 'R', 'U', 'C'].map((e) => (e === a || e === b ? 1 : e === 'C' ? 0 : 0.35));
    return w.concat(ev);
  };
  const blended = () => {
    const now = state(cA.value, cOp.value, cB.value);
    if (cA.k < 1) return cA.mix((v) => state(v, cOp.value, cB.value));
    if (cOp.k < 1) return cOp.mix((v) => state(cA.value, v, cB.value));
    if (cB.k < 1) return cB.mix((v) => state(cA.value, cOp.value, v));
    return now;
  };
  const ellipse = (ctx, [cx, cy, rx, ry, rot]) => { ctx.beginPath(); ctx.ellipse(cx, cy, rx, ry, rot, 0, 2 * Math.PI); };
  function draw() {
    const { ctx } = begin(d.c);
    const a = cA.value, op = cOp.value, b = cB.value, S = blended();
    const A = EV[a].set, B = EV[b].set, inter = A.filter((o) => B.includes(o)), uni = [...new Set(A.concat(B))];
    const pa = P(A), pb = P(B), pi = P(inter), pu = P(uni);
    const names = (s) => OUT.filter((o) => s.includes(o.id)).map((o) => o.name);
    const list = (s) => { const x = names(s); return x.length < 2 ? x.join('') : `${x.slice(0, -1).join(', ')} and ${x[x.length - 1]}`; };
    if (op === 'given') {
      const out = OUT.filter((o) => !B.includes(o.id)).map((o) => o.name);
      topline(ctx, `Given that ${EV[b].name === 'a woman' ? 'a woman wins' : `the winner is ${EV[b].name}`}, ${out.length ? `${out.join(' and ')} ${out.length > 1 ? 'are' : 'is'} out, and ` : ''}${inter.length ? `${list(inter)} hold${inter.length > 1 ? '' : 's'} ${pr(pi)} of the ${pr(pb)} that is left` : `nothing of the ${pr(pb)} that is left is in ${a}`}.`);
    } else if (op === 'or') {
      topline(ctx, `${list(uni)} make up ${a} ∪ ${b}: ${pr(pa)} + ${pr(pb)}${pi ? ` − ${pr(pi)}, since ${list(inter)} would count twice` : ''}, which is ${pr(pu)}.`);
    } else {
      topline(ctx, inter.length ? `${list(inter)} ${inter.length > 1 ? 'are' : 'is'} in both ${a} and ${b}, so Pr(${a} ∩ ${b}) = ${pr(pi)}.` : `No outcome is in both ${a} and ${b}, so Pr(${a} ∩ ${b}) = 0.`);
    }
    /* the scene sits under the headline: everything below is drawn 60 units up from the coordinates above */
    ctx.save(); ctx.translate(0, -60);
    /* the events: an ellipse each, in its referent's colour; the chosen ones solid and tinted, the rest faint */
    const evs = ['F', 'R', 'U', 'C'];
    evs.forEach((e, i) => {
      const pres = S[OUT.length + i]; if (pres < 0.02) return;
      const col = F.ref(e);
      ctx.save(); ellipse(ctx, EV[e].e);
      if (e === a || e === b) { ctx.fillStyle = alpha(col, 0.07 * pres); ctx.fill(); }
      ctx.globalAlpha = Math.min(1, pres); ctx.strokeStyle = col; ctx.lineWidth = e === a || e === b ? 4 : 2.5;
      if (!(e === a || e === b)) ctx.setLineDash([3, 7]);
      ctx.stroke(); ctx.restore();
      ctx.save(); ctx.globalAlpha = Math.min(1, pres);
      text(ctx, `${e}: ${EV[e].name}`, EV[e].lab[0], EV[e].lab[1], col, { size: 24, weight: 600, align: 'center', base: 'middle', bg: PAL.panel });
      ctx.restore();
    });
    /* the region the operation keeps, shaded: A ∩ B by clipping one ellipse to the other, A ∪ B both, A given B its part of B */
    ctx.save();
    const shadeCol = alpha(PAL.ink, 0.1);
    if (op === 'or') { ellipse(ctx, EV[a].e); ctx.fillStyle = shadeCol; ctx.fill(); if (b !== a) { ellipse(ctx, EV[b].e); ctx.fill(); } }
    else { ellipse(ctx, EV[a].e); ctx.clip(); ellipse(ctx, EV[b].e); ctx.fillStyle = shadeCol; ctx.fill(); }
    ctx.restore();
    /* the outcomes: counted ones filled, the others hollow, the ruled-out ones faded to ink */
    OUT.forEach((o, i) => {
      const w = S[i], col = F.mixColor(PAL.muted, F.ref(o.id), Math.min(1, w * 1.4));
      ctx.save(); ctx.globalAlpha = 0.25 + 0.75 * Math.min(1, w * 2.2);
      dot(ctx, o.x, o.y, col, w > 0.6, 11);
      text(ctx, `${o.name} (${pr(o.p)})`, o.x, o.y - 34, col, { size: 26, weight: w > 0.6 ? 600 : 400, align: 'center', base: 'middle', bg: PAL.panel });
      ctx.restore();
    });
    ctx.restore();
    if (op === 'given') {
      ro.set(`\\Pr(${a}|${b}) = \\frac{\\Pr(${a} \\cap ${b})}{\\Pr(${b})} = \\frac{${pr(pi)}}{${pr(pb)}} = ${pr(pi / pb)}`, `$\\Pr(${a}) = ${pr(pa)}$, before ${b} is known`);
    } else if (op === 'or') {
      ro.set(`\\Pr(${a} \\cup ${b}) = \\Pr(${a}) + \\Pr(${b}) - \\Pr(${a} \\cap ${b}) = ${pr(pa)} + ${pr(pb)} - ${pr(pi)} = ${pr(pu)}`, '');
    } else {
      ro.set(`\\Pr(${a} \\cap ${b}) = ${pr(pi)}`, '');
    }
  }
  register(d.fig, { update: () => {}, draw });
})();

/* ================================================================ sim-coin-tosses: indicators, run by run (a story over the runs) */
(function () {
  const H = 940, RUNS = 1000, KMAX = 20, COLS = 8;
  const d = sim('sim-coin-tosses', H);
  /* one seeded generator, so that run r is the same run whichever way the slider reaches it */
  const rng = (seed) => () => { seed |= 0; seed = (seed + 0x6D2B79F5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
  const r1 = rng(20261109), r2 = rng(1729);
  const HEADS = Array.from({ length: RUNS }, () => Array.from({ length: KMAX }, () => (r1() < 0.5 ? 1 : 0)));
  const TOSSES = Array.from({ length: RUNS }, () => { let t = 1; while (r2() >= 0.5) t += 1; return t; });
  const q = choice(d.controls, { label: '\\text{count}', key: 'question', value: 'first', options: [
    { value: 'heads', label: 'heads in k tosses' }, { value: 'first', label: 'tosses until the first head' }] });
  const sK = ctl(d.controls, { label: 'k', cls: 'size', key: 'k', min: 1, max: KMAX, step: 1, value: 10, unit: '', dec: 0 });
  /* the story plays from one run; with reduced motion it opens at rest on 200 runs, the stop the text's numbers settle by */
  const sR = ctl(d.controls, { label: '\\text{runs}', cls: '', key: 'runs', min: 1, max: RUNS, step: 1, value: F.REDUCED ? 200 : 1, unit: '', dec: 0 });
  F.story(d, sR, { stops: [{ v: 1, label: '1' }, { v: 100, label: '100' }, { v: 200, label: '200' }, { v: 500, label: '500' }, { v: 1000, label: '1000' }] });
  const ro = F.readout(d);
  /* the indicators of run r: heads, I_i = 1 if toss i is heads; first head, I_i = 1 if the coin is tossed i or more times */
  const cells = (heads, k, r) => (heads ? HEADS[r].slice(0, k) : Array.from({ length: Math.max(COLS, TOSSES[r]) }, (_, i) => (i < TOSSES[r] ? 1 : 0)));
  const value = (heads, k, r) => (heads ? HEADS[r].slice(0, k).reduce((s, x) => s + x, 0) : TOSSES[r]);
  function draw() {
    const { ctx } = begin(d.c);
    const heads = q.value === 'heads', k = Math.round(sK.v), R = Math.max(1, Math.round(sR.v));
    sK.show(heads);
    const E = heads ? k / 2 : 2, ncol = heads ? k : COLS, fmtE = fmt(E, Number.isInteger(E) ? 0 : 1);
    let sum = 0; const colSum = new Array(ncol).fill(0);
    for (let r = 0; r < R; r += 1) { sum += value(heads, k, r); const c = cells(heads, k, r); for (let i = 0; i < ncol; i += 1) colSum[i] += c[i] || 0; }
    const mean = sum / R;
    topline(ctx, heads
      ? `After ${R} run${R > 1 ? 's' : ''} of ${k} tosses the mean number of heads is ${fmt(mean, 2)}; k/2 is ${fmtE}.`
      : `After ${R} run${R > 1 ? 's' : ''} the mean number of tosses is ${fmt(mean, 2)}; the lemma says 2.`);
    /* left: the last runs, one row each, a cell per indicator */
    const SHOW = 12, x0 = 70, y0 = 150, cw = Math.min(30, 480 / ncol), ch = 26;
    text(ctx, 'run', x0, y0 - 34, PAL.muted, { size: 20 });
    for (let i = 0; i < ncol; i += 1) if (ncol <= 10 || i === 0 || (i + 1) % 5 === 0) text(ctx, `I_{${i + 1}}`, x0 + 70 + i * cw + cw / 2, y0 - 34, PAL.muted, { size: 19, align: 'center' });
    const first = Math.max(0, R - SHOW);
    for (let r = first; r < R; r += 1) {
      const y = y0 + (r - first) * (ch + 8), c = cells(heads, k, r);
      text(ctx, String(r + 1), x0 + 50, y + ch / 2, PAL.muted, { size: 19, align: 'right', base: 'middle' });
      for (let i = 0; i < ncol; i += 1) {
        const x = x0 + 70 + i * cw;
        ctx.save(); ctx.strokeStyle = alpha(PAL.ink, 0.45); ctx.lineWidth = 1.5; ctx.strokeRect(x + 2, y, cw - 4, ch);
        if (c[i]) { ctx.fillStyle = PAL.ink; ctx.fillRect(x + 5, y + 3, cw - 10, ch - 6); }
        ctx.restore();
      }
      if (!heads && TOSSES[r] > ncol) text(ctx, '…', x0 + 70 + ncol * cw + 4, y + ch / 2, PAL.ink, { size: 20, base: 'middle' });
      text(ctx, `${heads ? 'X' : 'T'} = ${value(heads, k, r)}`, x0 + 70 + ncol * cw + 34, y + ch / 2, PAL.ink, { size: 20, base: 'middle' });
    }
    /* right: each column's mean against its expectation */
    const bx = 860, bw = 490, by = 120, bh = 300, ax = F.axes(ctx, { l: bx, r: bx + bw, t: by, b: by + bh }, [0.5, ncol + 0.5], [0, 1],
      { nx: 0, ny: 2, yl: 'mean of I_i', fy: (v) => fmt(v, 1) });
    const gap = (bw / ncol) * 0.22;
    for (let i = 0; i < ncol; i += 1) {
      const m = colSum[i] / R, e = heads ? 0.5 : 1 / 2 ** i, xa = ax.X(i + 0.5) + gap, xb = ax.X(i + 1.5) - gap;
      ctx.save(); ctx.fillStyle = alpha(PAL.ink, 0.28); ctx.fillRect(xa, ax.Y(m), xb - xa, ax.Y(0) - ax.Y(m)); ctx.restore();
      line(ctx, xa - 4, ax.Y(e), xb + 4, ax.Y(e), PAL.ink, 3, [10, 6]);
      if (ncol <= 12 || i % 2 === 0) text(ctx, String(i + 1), (xa + xb) / 2, ax.Y(0) + 22, PAL.muted, { size: 17, align: 'center' });
    }
    text(ctx, heads ? 'dashed: E[I_i] = 1/2' : 'dashed: E[I_i] = 1/2^{i−1}', bx + bw, by - 14, PAL.muted, { size: 19, align: 'right' });
    /* below: the running mean over the runs, on a log scale of runs, against the expectation */
    const gx = 160, gw = 1170, gy = 615, gh = 230, ymax = heads ? k : 4;
    const lx = (r) => gx + (Math.log10(r) / 3) * gw, Y = (v) => gy + gh - (v / ymax) * gh;
    line(ctx, gx, gy + gh, gx + gw, gy + gh, PAL.ink, 2); line(ctx, gx, gy, gx, gy + gh, PAL.ink, 2);
    [1, 10, 100, 1000].forEach((r) => { line(ctx, lx(r), gy + gh, lx(r), gy + gh + 8, PAL.ink, 2); text(ctx, String(r), lx(r), gy + gh + 30, PAL.muted, { size: 17, align: 'center' }); });
    text(ctx, 'runs', gx + gw, gy + gh + 56, PAL.muted, { size: 19, align: 'right' });
    const ticks = heads ? [0, k / 2, k] : [0, 1, 2, 3, 4];
    ticks.forEach((v) => { line(ctx, gx - 8, Y(v), gx, Y(v), PAL.ink, 2); text(ctx, fmt(v, Number.isInteger(v) ? 0 : 1), gx - 14, Y(v), PAL.muted, { size: 17, align: 'right', base: 'middle' }); });
    text(ctx, heads ? 'mean of X' : 'mean of T', gx, gy - 22, PAL.muted, { size: 19 });
    line(ctx, gx, Y(E), gx + gw, Y(E), PAL.ink, 3, [10, 10]);
    text(ctx, heads ? `E[X] = k/2 = ${fmtE}` : 'E[T] = 2', gx + gw - 30, Y(E) - 22, PAL.ink, { size: 20, align: 'right', bg: PAL.panel });
    ctx.save(); ctx.beginPath(); let s = 0;
    for (let r = 1; r <= R; r += 1) { s += value(heads, k, r - 1); const y = Math.max(gy, Math.min(gy + gh, Y(s / r))); if (r === 1) ctx.moveTo(lx(r), y); else ctx.lineTo(lx(r), y); }
    ctx.strokeStyle = PAL.ink; ctx.lineWidth = 4; ctx.stroke(); ctx.restore();
    dot(ctx, lx(R), Math.max(gy, Math.min(gy + gh, Y(mean))), PAL.ink, true, 9);
    if (heads) ro.set(`\\mathrm{E}[X] = \\sum_{i=1}^{${k}} \\mathrm{E}[I_i] = ${k}\\cdot\\tfrac12 = ${fmtE}`, `mean of ${R} run${R > 1 ? 's' : ''}: ${fmt(mean, 2)}`);
    else ro.set('\\mathrm{E}[T] = \\sum_{i=1}^{\\infty} \\mathrm{E}[I_i] = 1 + \\tfrac12 + \\tfrac14 + \\cdots = 2', `mean of ${R} run${R > 1 ? 's' : ''}: ${fmt(mean, 2)}`);
  }
  register(d.fig, { update: () => {}, draw });
})();
};
