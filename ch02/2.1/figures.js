/* Figures for section 2.1 Arrays and the list interface. Boots against the section's text article.
   Three Sims, none with a code panel (each idea is a property: the addressing formulas, and the List interface,
   which the book's RULES name as an exception to code beside the visual). sim-address and sim-row-major are
   still (a formula under sliders, no clock); sim-list moves (an operation displaces the values one at a time).
   No referents: B, c, d, i and j are unnamed positions and sizes, so they wear their types' colours. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['2.1'] = function (root, F) {
const { C, PAL, alpha, text, line, arrow, begin, tex, ctl, choice, select, register, topline, hbracket, cycle, hover } = F;
const sim = (id, H) => F.sim(root, id, H);
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2, dash) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};
const SUB = (n) => String(n).split('').map((ch) => '₀₁₂₃₄₅₆₇₈₉'['0123456789'.indexOf(ch)] ?? ch).join('');
const ease = (k) => { const t = Math.max(0, Math.min(1, k)); return t * t * (3 - 2 * t); };

/* ================================================================ sim-address: B + c·i, and where B goes when the
   numbering starts elsewhere (the article's re-basing example, erratum 15) */
(function () {
  const d = sim('sim-address', 560);
  const VALUES = [2, 4, 3, 1, 5];       /* the Pointer article's int a[5] = {2, 4, 3, 1, 5} */
  const A0 = 2000;                      /* the lead's example: the first element at address 2000 */
  const first = choice(d.controls, { label: '\\text{first index}', key: 'first', value: '0',
    options: [{ value: '0', label: '0' }, { value: '1', label: '1' }, { value: '31', label: '31' }],
    onInput: () => { const f = +first.value; sI.range({ min: f, max: f + 4, step: 1, value: f + 3 }); } });
  const sI = ctl(d.controls, { label: 'i', cls: 'index', key: 'i', min: 0, max: 4, step: 1, value: 3, dec: 0 });
  const sC = ctl(d.controls, { label: 'c', cls: 'size', key: 'c', min: 1, max: 8, step: 1, value: 4, fmt: (v) => `${Math.round(v)} byte${Math.round(v) === 1 ? '' : 's'}`,
    detents: [1, 2, 4, 8], snap: true });
  function draw() {
    const { ctx } = begin(d.c);
    const f = +first.value, c = Math.round(sC.v), i = Math.round(sI.v), k = i - f, B = A0 - f * c, addr = B + c * i;
    topline(ctx, `a[${i}] is at ${B} + ${c} · ${i} = ${addr}.`);
    /* the bytes from one element before the array to one after it; each byte the same width whatever c is */
    const lo = A0 - c, hi = A0 + (VALUES.length + 1) * c, x0 = 100, x1 = 1300, bw = (x1 - x0) / (hi - lo);
    const X = (a) => x0 + (a - lo) * bw, y = 190, h = 76;
    const ci = C('index'), ck = C('key'), cs = C('size');
    /* memory outside the array, faint */
    rect(ctx, X(lo), y, X(A0) - X(lo), h, null, alpha(PAL.ink, 0.25), 2, [6, 6]);
    rect(ctx, X(A0 + VALUES.length * c), y, X(hi) - X(A0 + VALUES.length * c), h, null, alpha(PAL.ink, 0.25), 2, [6, 6]);
    VALUES.forEach((v, j) => {
      const a = A0 + j * c, on = j === k;
      rect(ctx, X(a), y, c * bw, h, on ? alpha(ci, 0.16) : PAL.panel, on ? ci : PAL.ink, on ? 4 : 3);
      if (bw >= 7) for (let b = 1; b < c; b += 1) line(ctx, X(a + b), y + h - 14, X(a + b), y + h, alpha(PAL.ink, 0.35), 2);
      text(ctx, String(v), X(a) + (c * bw) / 2, y + h / 2 + 8, ck, { size: 30, align: 'center', weight: 600 });
      text(ctx, String(f + j), X(a) + (c * bw) / 2, y - 18, on ? ci : PAL.muted, { size: 22, align: 'center', weight: on ? 600 : 400 });
      text(ctx, String(a), X(a), y + h + 30, PAL.muted, { size: 17, align: 'center' });
    });
    text(ctx, String(A0 + VALUES.length * c), X(A0 + VALUES.length * c), y + h + 30, PAL.muted, { size: 17, align: 'center' });
    text(ctx, 'index', x0 - 10, y - 18, PAL.muted, { size: 17, align: 'right' });
    text(ctx, 'address', x0 - 10, y + h + 30, PAL.muted, { size: 17, align: 'right' });
    /* c: one element's bytes */
    hbracket(ctx, X(A0 + k * c), X(A0 + (k + 1) * c), y - 50, cs, `c = ${c}`, { side: 'above' });
    /* the address of element i, from below */
    const ax = X(addr);
    arrow(ctx, ax, y + h + 120, ax, y + h + 44, ci, 4);
    text(ctx, `B + c · i = ${addr}`, ax, y + h + 146, ci, { size: 24, align: 'center', weight: 600 });
    /* B: the address element 0 would have; past the left edge when the numbering starts far from 0 */
    const by = y + h + 210;
    if (B >= lo) {
      arrow(ctx, X(B), by + 30, X(B), y + h + 44, ci, 3);
      text(ctx, `B = ${B}`, X(B), by + 56, ci, { size: 22, align: f ? 'left' : 'center', weight: 600 });
    } else {
      arrow(ctx, x0 + 40, by, x0 - 40, by, ci, 3);
      text(ctx, `B = ${B}, ${A0 - B} bytes to the left`, x0 + 52, by + 8, ci, { size: 22, weight: 600 });
    }
    const rb = f ? `\\\\ B = ${A0} - ${f}\\cdot ${c} = ${B}` : '';
    tex(d.readout, `\\text{address} = B + c\\cdot i = ${B} + ${c}\\cdot ${i} = ${addr}${rb}`);
  }
  register(d.fig, { update: () => {}, draw });
})();

/* ================================================================ sim-row-major: a two-dimensional array in memory */
(function () {
  const d = sim('sim-row-major', 560);
  const SHAPES = { a: { name: 'a', rows: 2, cols: 3, i: 1, j: 2 }, A: { name: 'A', rows: 3, cols: 4, i: 1, j: 3 } };
  const B = 2000, SIZE = 4;
  const shape = choice(d.controls, { label: '\\text{array}', key: 'shape', value: 'a',
    options: [{ value: 'a', label: 'int a[2][3]' }, { value: 'A', label: 'A[3][4]' }],
    onInput: () => { const s = SHAPES[shape.value]; sI.range({ min: 0, max: s.rows - 1, step: 1, value: s.i }); sJ.range({ min: 0, max: s.cols - 1, step: 1, value: s.j }); } });
  const sI = ctl(d.controls, { label: 'i', cls: 'index', key: 'i', min: 0, max: 1, step: 1, value: 1, dec: 0 });
  const sJ = ctl(d.controls, { label: 'j', cls: 'index', key: 'j', min: 0, max: 2, step: 1, value: 2, dec: 0 });
  function draw() {
    const { ctx } = begin(d.c);
    const s = SHAPES[shape.value], i = Math.round(sI.v), j = Math.round(sJ.v), cr = s.cols * SIZE, addr = B + cr * i + SIZE * j;
    const ci = C('index'), ck = C('key'), cs = C('size');
    topline(ctx, `${s.name}[${i}][${j}] is at ${B} + ${cr} · ${i} + ${SIZE} · ${j} = ${addr}.`);
    const n = s.rows * s.cols, mw = Math.min(100, 1160 / n), mx = 700 - (n * mw) / 2, mh = 60;
    const gw = 96, gh = 56, gx = 700 - (s.cols * gw) / 2, gy = 120, my = gy + s.rows * gh + 150;
    /* where the chosen element lands */
    const tt = i * s.cols + j, fx = gx + j * gw + gw / 2, fy = gy + (i + 1) * gh, tx = mx + tt * mw + mw / 2;
    line(ctx, fx, fy + 4, tx, my - 70, alpha(ci, 0.7), 3, [8, 8]);
    arrow(ctx, tx, my - 70, tx, my - 4, ci, 3);
    /* the array as the program sees it */
    for (let r = 0; r < s.rows; r += 1) {
      text(ctx, String(r), gx - 22, gy + r * gh + gh / 2 + 7, r === i ? ci : PAL.muted, { size: 20, align: 'right', weight: r === i ? 600 : 400 });
      for (let q = 0; q < s.cols; q += 1) {
        const on = r === i && q === j;
        rect(ctx, gx + q * gw, gy + r * gh, gw, gh, on ? alpha(ci, 0.16) : PAL.panel, on ? ci : PAL.ink, on ? 4 : 3);
        text(ctx, String(r * s.cols + q + 1), gx + q * gw + gw / 2, gy + r * gh + gh / 2 + 8, ck, { size: 26, align: 'center', weight: 600 });
      }
    }
    for (let q = 0; q < s.cols; q += 1) text(ctx, String(q), gx + q * gw + gw / 2, gy - 12, q === j ? ci : PAL.muted, { size: 20, align: 'center', weight: q === j ? 600 : 400 });
    text(ctx, 'i', gx - 52, gy + (s.rows * gh) / 2 + 7, PAL.muted, { size: 20, align: 'right' });
    text(ctx, 'j', gx + (s.cols * gw) / 2, gy - 40, PAL.muted, { size: 20, align: 'center' });
    /* the same elements in memory, row after row */
    for (let t = 0; t < n; t += 1) {
      const r = Math.floor(t / s.cols), q = t % s.cols, on = r === i && q === j;
      rect(ctx, mx + t * mw, my, mw, mh, on ? alpha(ci, 0.16) : PAL.panel, on ? ci : PAL.ink, on ? 4 : 3);
      text(ctx, String(t + 1), mx + t * mw + mw / 2, my + mh / 2 + 8, ck, { size: 26, align: 'center', weight: 600 });
      text(ctx, String(B + t * SIZE), mx + t * mw + mw / 2, my + mh + 26, PAL.muted, { size: 17, align: 'center' });
    }
    for (let r = 0; r < s.rows; r += 1) hbracket(ctx, mx + r * s.cols * mw + 4, mx + (r + 1) * s.cols * mw - 4, my - 14, r === i ? cs : PAL.muted, `row ${r}`, { side: 'above' });
    text(ctx, 'address', mx - 12, my + mh + 26, PAL.muted, { size: 17, align: 'right' });
    tex(d.readout, `\\text{address} = B + c\\cdot i + d\\cdot j = ${B} + ${cr}\\cdot ${i} + ${SIZE}\\cdot ${j} = ${addr}`
      + `\\\\ c = ${s.cols}\\cdot ${SIZE} = ${cr}\\\\ d = ${SIZE}`);
  }
  register(d.fig, { update: () => {}, draw });
})();

/* ================================================================ sim-list: the List interface's operations on
   ODS Figure 1.4's sequence, each one played as the values it moves */
(function () {
  const d = sim('sim-list', 460);
  const XS = ['a', 'b', 'c', 'd', 'e', 'f', 'b', 'k', 'c'], N = XS.length;
  const OPS = {
    get: { label: 'get(i)', base: 'get' }, set: { label: 'set(i, x)', base: 'set' },
    add: { label: 'add(i, x)', base: 'add' }, remove: { label: 'remove(i)', base: 'remove' },
    addFirst: { label: 'add_first(x)', base: 'add', at: 0, call: '\\mathrm{add}(0,x)' },
    removeFirst: { label: 'remove_first()', base: 'remove', at: 0, call: '\\mathrm{remove}(0)' },
    addLast: { label: 'add_last(x)', base: 'add', at: N, call: '\\mathrm{add}(\\mathrm{size}(),x)' },
    removeLast: { label: 'remove_last()', base: 'remove', at: N - 1, call: '\\mathrm{remove}(\\mathrm{size}()-1)' },
  };
  const opSel = select(d.controls, { label: '\\text{operation}', key: 'op', value: 'get',
    options: Object.keys(OPS).map((k) => ({ value: k, label: OPS[k].label })), onInput: setup });
  const sI = ctl(d.controls, { label: 'i', cls: 'index', key: 'i', min: 0, max: N - 1, step: 1, value: 2, dec: 0, onInput: () => cy.reset() });
  function setup() {
    const o = OPS[opSel.value], max = o.base === 'add' ? N : N - 1;
    const v = o.at !== undefined ? o.at : Math.min(Math.round(sI.v), max);
    sI.range({ min: 0, max, step: 1, value: v });
    sI.disable(o.at !== undefined);
    cy.reset();
  }
  /* the beats of the operation: add moves x_{n−1} … x_i one place right, then stores x; remove lifts x_i out,
     then moves x_{i+1} … x_{n−1} one place left; get and set take one beat */
  const beats = () => { const o = OPS[opSel.value], i = Math.round(sI.v); return o.base === 'add' ? N - i + 1 : o.base === 'remove' ? N - i : 1; };
  const cy = cycle(() => beats(), 1.2);
  function draw() {
    const { ctx } = begin(d.c);
    const o = OPS[opSel.value], i = Math.round(sI.v), t = cy.now(), T = beats();
    const ci = C('index'), ck = C('key'), cc = C('cost'), cs = C('size');
    const cell = 104, slots = N + 1, x0 = 700 - (slots * cell) / 2, y = 220, h = 70;
    const cx = (p) => x0 + (p + 0.5) * cell;
    /* moved so far, and where each value stands */
    let moved = 0, n = N;
    const pos = XS.map((_, j) => j), alive = XS.map(() => 1);
    let xAt = null, xAlpha = 0, lifted = null, active = null;
    if (o.base === 'add') {
      for (let j = N - 1; j >= i; j -= 1) {
        const b = N - 1 - j, k = ease(t - b);
        pos[j] = j + k;
        if (t >= b + 1) moved += 1;
        if (t > b && t < b + 1) active = { from: j, to: j + 1 };
      }
      const kb = ease(t - (T - 1));
      xAt = { p: i, lift: 1 - kb }; xAlpha = Math.min(1, 0.5 + kb);
      if (t >= T) n = N + 1;
    } else if (o.base === 'remove') {
      const k0 = ease(t);
      lifted = { p: i, lift: k0 }; alive[i] = 1 - k0;
      for (let j = i + 1; j < N; j += 1) {
        const b = j - i, k = ease(t - b);
        pos[j] = j - k;
        if (t >= b + 1) moved += 1;
        if (t > b && t < b + 1) active = { from: j, to: j - 1 };
      }
      if (t >= T) n = N - 1;
    } else if (o.base === 'get') {
      lifted = { p: i, lift: ease(t), copy: true };
    } else {
      const k = ease(t);
      alive[i] = 1 - k; xAt = { p: i, lift: 1 - k }; xAlpha = 0.35 + 0.65 * k;
    }
    /* the slots: those in the list solid, the slot an add will fill dashed (hollow: not yet reached) */
    for (let p = 0; p < slots; p += 1) {
      const inList = p < n, spare = !inList && (o.base === 'add' || p === N - 1);
      if (!inList && !spare) continue;
      rect(ctx, cx(p) - cell / 2 + 6, y, cell - 12, h, inList ? PAL.panel : null, inList ? PAL.ink : alpha(PAL.ink, 0.35), 3, inList ? null : [6, 6]);
      text(ctx, String(p), cx(p), y + h + 30, p === i ? ci : PAL.muted, { size: 20, align: 'center', weight: p === i ? 600 : 400 });
    }
    text(ctx, 'index', x0 - 6, y + h + 30, PAL.muted, { size: 17, align: 'right' });
    /* the values */
    XS.forEach((v, j) => {
      if (alive[j] <= 0.01) return;
      ctx.save(); ctx.globalAlpha = alive[j];
      text(ctx, v, cx(pos[j]), y + h / 2 + 10, ck, { size: 32, align: 'center', weight: 600 });
      ctx.restore();
    });
    if (active) { const ay = y - 26; arrow(ctx, cx(active.from), ay, cx(active.to), ay, cs, 4); }
    if (xAt) {
      ctx.save(); ctx.globalAlpha = xAlpha;
      const yy = y + h / 2 + 10 - xAt.lift * 120;
      text(ctx, 'x', cx(xAt.p), yy, ck, { size: 34, align: 'center', weight: 700 });
      ctx.restore();
    }
    if (lifted) {
      const yy = y + h / 2 + 10 - lifted.lift * 120;
      text(ctx, XS[lifted.p], cx(lifted.p), yy, ck, { size: 32, align: 'center', weight: 600 });
      if (lifted.lift > 0.95) text(ctx, o.base === 'get' ? 'returned' : 'removed', cx(lifted.p), yy - 40, PAL.muted, { size: 20, align: 'center' });
    }
    hbracket(ctx, cx(0) - cell / 2 + 6, cx(n - 1) + cell / 2 - 6, y + h + 60, cs, `n = ${n}`, { side: 'below' });
    /* headline and readout: what the operation does, and the values it has moved so far against n − i */
    const sub = (p) => `x${SUB(p)}`;
    const head = {
      get: `get(${i}) returns ${sub(i)} = ${XS[i]}; nothing moves.`,
      set: `set(${i}, x) writes x over ${sub(i)} = ${XS[i]}; nothing moves.`,
      add: i === N ? `add(${N}, x) puts x after ${sub(N - 1)}; nothing moves.` : `add(${i}, x) moves ${sub(i)}, …, ${sub(N - 1)} one place right, from the end, then sets ${sub(i)} = x.`,
      remove: i === N - 1 ? `remove(${N - 1}) takes ${sub(N - 1)} = ${XS[N - 1]}; nothing moves.` : `remove(${i}) takes ${sub(i)} = ${XS[i]}, then moves ${sub(i + 1)}, …, ${sub(N - 1)} one place left.`,
    }[o.base];
    topline(ctx, head);
    const call = o.call ? `\\mathrm{${o.label.replace(/\(.*$/, '').replace(/_/g, '\\_')}}(${o.label.includes('x') ? 'x' : ''}) \\Rightarrow ${o.call.replace('(0,x)', '(0,x)')}\\\\ ` : '';
    let rd;
    if (o.base === 'get') rd = `\\mathrm{get}(${i}) = x_{${i}} = ${XS[i]}`;
    else if (o.base === 'set') rd = `x_{${i}} = x`;
    else if (o.base === 'add') rd = (i < N ? `x_{j+1} = x_j \\text{ for } j \\in \\{${N - 1}, \\ldots, ${i}\\}\\\\ ` : '') + `x_{${i}} = x\\\\ \\text{moved } ${moved} \\le n - i = ${N - i}`;
    else rd = (i < N - 1 ? `x_j = x_{j+1} \\text{ for } j \\in \\{${i}, \\ldots, ${N - 2}\\}\\\\ ` : '') + `\\text{moved } ${moved} \\le n - i - 1 = ${N - i - 1}`;
    tex(d.readout, call + rd);
  }
  setup();
  register(d.fig, { update: (dt) => cy.step(dt, () => Math.max(1, beats() / 5)), draw });
})();
};
