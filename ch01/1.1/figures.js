/* Figures for section 1.1 What an algorithm is. Boots against the section's text article.
   Four debugger figures (code beside the drawing, stepped by block: METHOD §2.3) and one still sim.
   The code in every panel is an AI translation of Erickson's pseudocode into Python, Java, C++ and
   JavaScript (METHOD decision 20); his pseudocode as printed is the figure's original, behind the toggle,
   or, for FibonacciMultiply, the first language of the panel. Each trace is the figure's own JS copy of the Python. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['1.1'] = function (root, F) {
const { C, PAL, alpha, text, line, dot, arrow, begin, tex, ctl, choice, register, fmt, topline } = F;
const sim = (id, H) => F.sim(root, id, H);
const AI = 'claude-opus-5-5 high';
const AIS = { python: AI, java: AI, cpp: AI, javascript: AI };
/* a canonical line → the same line, except where a language closes a block with a brace on a line of its own */
const lines = (n, extra) => { const m = {}; for (let i = 1; i <= n; i += 1) m[i] = i; return Object.assign(m, extra || {}); };
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2, dash) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};
const commas = (n) => String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ',');

/* ================================================================ sim-lattice: FibonacciMultiply */
(function () {
  /* Erickson's pseudocode as the PDF prints it (jeffe:0.2), the panel's first language */
  const PSEUDO = [
    "FibonacciMultiply(X[0 .. m − 1], Y[0 .. n − 1]):",
    "  hold ← 0",
    "  for k ← 0 to n + m − 1",
    "      for all i and j such that i + j = k",
    "          hold ← hold + X[i] · Y[j]",
    "      Z[k] ← hold mod 10",
    "      hold ← ⌊hold/10⌋",
    "  return Z[0 .. m + n − 1]",
  ].join('\n');
  const PMAP = { 1: 1, 4: 2, 5: 3, 6: 4, 7: 4, 8: 5, 9: 6, 10: 7, 11: 8 };
  const PY = [
    'def fibonacci_multiply(X, Y):',
    '    m, n = len(X), len(Y)',
    '    Z = [0] * (m + n)',
    '    hold = 0',
    '    for k in range(n + m):',
    '        for i in range(max(0, k - n + 1), min(k, m - 1) + 1):',
    '            j = k - i',
    '            hold = hold + X[i] * Y[j]',
    '        Z[k] = hold % 10',
    '        hold = hold // 10',
    '    return Z',
  ].join('\n');
  const braces = (head, decl, zinit, max, min, div, ret) => [
    head,
    `    ${decl}`,
    `    ${zinit}`,
    '    int hold = 0;',
    '    for (int k = 0; k < n + m; k++) {',
    `        for (int i = ${max}(0, k - n + 1); i <= ${min}(k, m - 1); i++) {`,
    '            int j = k - i;',
    '            hold = hold + X[i] * Y[j];',
    '        }',
    '        Z[k] = hold % 10;',
    `        hold = ${div};`,
    '    }',
    `    ${ret}`,
    '}',
  ].join('\n');
  const JAVA = braces('static int[] fibonacciMultiply(int[] X, int[] Y) {', 'int m = X.length, n = Y.length;', 'int[] Z = new int[m + n];', 'Math.max', 'Math.min', 'hold / 10', 'return Z;');
  const CPP = braces('std::vector<int> fibonacciMultiply(const std::vector<int>& X, const std::vector<int>& Y) {', 'int m = X.size(), n = Y.size();', 'std::vector<int> Z(m + n, 0);', 'std::max', 'std::min', 'hold / 10', 'return Z;');
  const JS = braces('function fibonacciMultiply(X, Y) {', 'const m = X.length, n = Y.length;', 'const Z = new Array(m + n).fill(0);', 'Math.max', 'Math.min', 'Math.floor(hold / 10)', 'return Z;')
    .replace('    int hold = 0;', '    let hold = 0;').replace('for (int k', 'for (let k').replace('for (int i', 'for (let i').replace('int j = k - i;', 'const j = k - i;');
  const MAP = lines(11, { 9: 10, 10: 11, 11: 13 });
  const digits = (s) => s.split('').reverse().map(Number);     /* X[0] is the ones digit */
  const run = (xs, ys) => {
    const X = digits(xs), Y = digits(ys);
    return F.trace((at) => {
      const m = X.length, n = Y.length; at(2, { m, n });
      const Z = new Array(m + n).fill(0); at(3, { m, n, Z });
      let hold = 0; at(4, { m, n, hold, Z });
      let products = 0;
      for (let k = 0; k < n + m; k += 1) {
        at(5, { k, hold, Z, products });
        for (let i = Math.max(0, k - n + 1); i <= Math.min(k, m - 1); i += 1) {
          at(6, { k, i, hold, Z, products });
          const j = k - i; at(7, { k, i, j, hold, Z, products });
          hold += X[i] * Y[j]; products += 1; at(8, { k, i, j, hold, Z, products }, ['add', i, j]);
        }
        Z[k] = hold % 10; at(9, { k, hold, Z, products });
        hold = Math.floor(hold / 10); at(10, { k, hold, Z, products });
      }
      at(11, { Z, products });
    });
  };
  const INPUTS = [['934', '314'], ['123', '456'], ['9999', '99']];
  const d = sim('sim-lattice', 980);
  const code = F.code(d, {
    src: { pseudocode: PSEUDO, python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: AIS,
    lineMap: { pseudocode: PMAP, java: MAP, cpp: MAP, javascript: MAP },
    blocks: [
      { id: 'init', lines: [2, 4], label: 'start with no carry', touches: ['hold'] },
      { id: 'column', lines: [5, 10], label: 'settle digit k of the product', touches: ['k', 'Z'] },
      { id: 'diag', lines: [6, 8], label: 'add one product with i + j = k', touches: ['i', 'j', 'hold'] },
      { id: 'digit', lines: [9, 10], label: 'write the low digit, carry the rest', touches: ['Z', 'hold'] },
    ],
    refs: { k: () => F.ref('lat-k'), i: () => F.ref('lat-i'), j: () => F.ref('lat-j'), hold: () => F.ref('lat-hold') },
  });
  F.debug(d, {
    code, watch: ['k', 'i', 'j', 'hold'],
    inputs: INPUTS.map(([a, b]) => ({ value: `${a}x${b}`, label: `${a} × ${b}`, trace: run(a, b) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const [xs, ys] = g.input.split('x'), X = digits(xs), Y = digits(ys), m = X.length, n = Y.length;
      const f = g.frame.vars, Z = f.Z || [], K = typeof f.k === 'number' ? f.k : (g.frame.line >= 11 ? m + n : -1);
      const done = g.frame.line === 11, products = f.products || 0;
      const cell = Math.min(150, 440 / n, 900 / m), gx = 700 - (m * cell) / 2 - 40, gy = 200;
      const cK = F.ref('lat-k'), cI = F.ref('lat-i'), cJ = F.ref('lat-j'), cH = F.ref('lat-hold'), key = C('key'), idx = C('index');
      const colX = (i) => gx + (m - 1 - i + 0.5) * cell, rowY = (j) => gy + (n - 1 - j + 0.5) * cell;
      topline(ctx, done ? `${xs} × ${ys} = ${Z.slice().reverse().join('').replace(/^0+(?=\d)/, '')}` : `Column k = ${Math.max(0, K)} collects every X[i] · Y[j] with i + j = ${Math.max(0, K)}.`);
      /* X across the top (its ones digit on the right), Y down the right side, as the Treviso lattice sets them */
      /* each digit's position under it; the position i or j is on now is named, in its colour */
      const onI = typeof f.i === 'number' && !done ? f.i : -1, onJ = typeof f.j === 'number' && !done ? f.j : -1;
      for (let i = 0; i < m; i += 1) {
        text(ctx, String(X[i]), colX(i), gy - 34, i === onI ? cI : key, { size: 40, align: 'center', weight: 600 });
        text(ctx, i === onI ? `i = ${i}` : String(i), colX(i), gy - 80, i === onI ? cI : idx, { size: i === onI ? 28 : 24, align: 'center', weight: i === onI ? 600 : 400 });
      }
      for (let j = 0; j < n; j += 1) {
        text(ctx, String(Y[j]), gx + m * cell + 36, rowY(j), j === onJ ? cJ : key, { size: 40, align: 'center', weight: 600 });
        text(ctx, j === onJ ? `j = ${j}` : String(j), gx + m * cell + 80, rowY(j), j === onJ ? cJ : idx, { size: j === onJ ? 28 : 24, weight: j === onJ ? 600 : 400 });
      }
      text(ctx, 'X', gx - 40, gy - 34, PAL.ink, { size: 30, align: 'center', italic: true });
      text(ctx, 'Y', gx + m * cell + 36, gy - 34, PAL.ink, { size: 30, align: 'center', italic: true });
      /* the cells: one partial product each; added ones filled, the diagonal being summed tinted in k's colour */
      for (let i = 0; i < m; i += 1) for (let j = 0; j < n; j += 1) {
        const x0 = colX(i) - cell / 2, y0 = rowY(j) - cell / 2, s = i + j;
        const added = s < K || (s === K && typeof f.i === 'number' && i < f.i) || (s === K && f.i === i && g.frame.line === 8) || (s === K && g.frame.line >= 9) || done;
        rect(ctx, x0, y0, cell, cell, s === K && !done ? alpha(cK, 0.16) : null, PAL.rule, 2);
        ctx.save(); ctx.strokeStyle = alpha(PAL.ink, 0.25); ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(x0 + cell, y0); ctx.lineTo(x0, y0 + cell); ctx.stroke(); ctx.restore();
        const p = X[i] * Y[j], col = added ? key : alpha(PAL.ink, 0.35);
        text(ctx, String(Math.floor(p / 10)), x0 + cell * 0.3, y0 + cell * 0.3, col, { size: 34, align: 'center', weight: added ? 600 : 400 });
        text(ctx, String(p % 10), x0 + cell * 0.7, y0 + cell * 0.7, col, { size: 34, align: 'center', weight: added ? 600 : 400 });
        if (f.i === i && f.j === j && !done) rect(ctx, x0 + 3, y0 + 3, cell - 6, cell - 6, null, cH, 5);
      }
      /* Z along the bottom, its ones digit on the right; the settled digits Z[0 .. k) shaded in the index tint */
      const zy = gy + n * cell + 60, zc = Math.min(100, 1000 / (m + n)), zr = 700 + ((m + n) * zc) / 2;
      text(ctx, 'Z', zr - (m + n) * zc - 40, zy + zc / 2, PAL.ink, { size: 30, align: 'center', italic: true });
      const settled = done ? m + n : (g.frame.line >= 9 && g.frame.line <= 10 ? K + 1 : Math.max(0, K));
      for (let k = 0; k < m + n; k += 1) {
        const x0 = zr - (k + 1) * zc;
        rect(ctx, x0, zy, zc, zc, k < settled ? alpha(idx, 0.14) : null, k === K && !done ? cK : PAL.rule, k === K && !done ? 4 : 2, k < settled ? null : [6, 6]);
        if (k < settled) text(ctx, String(Z[k] ?? 0), x0 + zc / 2, zy + zc / 2, key, { size: 40, align: 'center', weight: 600 });
        text(ctx, String(k), x0 + zc / 2, zy + zc + 26, k === K && !done ? cK : idx, { size: 24, align: 'center', weight: k === K ? 600 : 400 });
      }
      /* hold rides under the column it is carried into */
      if (typeof f.hold === 'number') {
        const hk = g.frame.line === 10 ? K + 1 : Math.max(0, K), hx = zr - (Math.min(hk, m + n - 1) + 0.5) * zc;
        text(ctx, `hold = ${f.hold}`, hx, zy + zc + 66, cH, { size: 30, align: 'center', weight: 600 });
      }
      F.rich(ctx, [`single-digit products `, [String(products), C('cost')], ` of m · n = ${m * n}`], 700, zy + zc + 116, { size: 28, align: 'center' });
      text(ctx, `Z[0 .. ${settled}) settled`, 700, zy + zc + 154, idx, { size: 26, align: 'center' });
    },
  });
})();

/* ================================================================ sim-peasant: PeasantMultiply */
(function () {
  const PY = [
    'def peasant_multiply(x, y):',
    '    prod = 0',
    '    while x > 0:',
    '        if x % 2 == 1:',
    '            prod = prod + y',
    '        x = x // 2',
    '        y = y + y',
    '    return prod',
  ].join('\n');
  const braces = (head, T, half) => [
    head,
    `    ${T} prod = 0;`,
    '    while (x > 0) {',
    '        if (x % 2 == 1) {',
    '            prod = prod + y;',
    '        }',
    `        x = ${half};`,
    '        y = y + y;',
    '    }',
    '    return prod;',
    '}',
  ].join('\n');
  const JAVA = braces('static long peasantMultiply(long x, long y) {', 'long', 'x / 2');
  const CPP = braces('long long peasantMultiply(long long x, long long y) {', 'long long', 'x / 2');
  const JS = braces('function peasantMultiply(x, y) {', 'let', 'Math.floor(x / 2)').replace('x % 2 == 1', 'x % 2 === 1');
  const MAP = lines(8, { 6: 7, 7: 8, 8: 10 });
  const run = (x0, y0) => F.trace((at) => {
    let x = x0, y = y0, prod = 0, rows = 0; at(2, { x, y, prod, rows });
    while (x > 0) {
      rows += 1; at(3, { x, y, prod, rows });
      at(4, { x, y, prod, rows });
      if (x % 2 === 1) { prod += y; at(5, { x, y, prod, rows }, ['add', y]); }
      x = Math.floor(x / 2); at(6, { x, y, prod, rows });
      y = y + y; at(7, { x, y, prod, rows });
    }
    at(8, { x, y, prod, rows });
  });
  const INPUTS = [[123, 456, '123 × 456'], [128, 456, 'x a power of 2'], [456, 123, 'x > y']];
  const d = sim('sim-peasant', 980);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: AIS,
    lineMap: { java: MAP, cpp: MAP, javascript: MAP },
    blocks: [
      { id: 'init', lines: [2, 2], label: 'start with prod = 0', touches: ['prod'] },
      { id: 'row', lines: [3, 7], label: 'one row of the table', touches: ['x', 'y', 'prod'] },
      { id: 'add', lines: [4, 5], label: 'if x is odd, add y to prod', touches: ['x', 'y', 'prod'] },
      { id: 'halve', lines: [6, 7], label: 'halve x, double y', touches: ['x', 'y'] },
    ],
    refs: { x: () => F.ref('x'), y: () => F.ref('y'), prod: () => F.ref('prod') },
  });
  F.debug(d, {
    code, watch: ['x', 'y', 'prod'],
    inputs: INPUTS.map(([a, b, label]) => ({ value: `${a}x${b}`, label, trace: run(a, b) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const [a, b] = g.input.split('x').map(Number);
      const v = g.frame.vars, cx = F.ref('x'), cy = F.ref('y'), cp = F.ref('prod'), key = C('key');
      /* the table's rows as the run has made them: row r holds x and y as they stood when it began */
      const rows = []; { let x = a, y = b, p = 0; while (x > 0) { const odd = x % 2 === 1; if (odd) p += y; rows.push({ x, y, odd, p }); x = Math.floor(x / 2); y += y; } }
      const shown = v.rows || 0, line8 = g.frame.line === 8;
      const added = (r) => r < shown - 1 || (r === shown - 1 && g.frame.line >= 5) || line8;
      const X0 = 330, Y0 = 400, P0 = 1000, top = 200, rh = Math.min(82, 640 / (rows.length + 1));
      const prod = v.prod, x = v.x, y = v.y;
      topline(ctx, line8 ? `When x reaches 0, prod = ${commas(prod)} = ${a} × ${b}.` : `prod + x · y = ${commas(prod)} + ${x} · ${commas(y)} = ${commas(prod + x * y)} = ${a} × ${b}`);
      text(ctx, 'x', X0, top, cx, { size: 34, align: 'right', weight: 600, italic: true });
      text(ctx, 'y', Y0 + 260, top, cy, { size: 34, align: 'right', weight: 600, italic: true });
      text(ctx, 'prod', P0, top, cp, { size: 34, align: 'right', weight: 600, italic: true });
      text(ctx, 'x mod 2', 120, top, PAL.muted, { size: 24, align: 'center' });
      line(ctx, 80, top + 30, 1080, top + 30, PAL.rule, 2);
      rows.forEach((r, i) => {
        if (i >= shown) return;
        const yy = top + 30 + (i + 0.7) * rh, cur = i === shown - 1 && !line8;
        if (cur) rect(ctx, 70, yy - rh / 2, 1020, rh, alpha(PAL.ink, 0.06));
        const counted = added(i) && r.odd;
        text(ctx, String(r.x), X0, yy, cur ? cx : PAL.ink, { size: 34, align: 'right', weight: cur ? 600 : 400 });
        text(ctx, String(r.x % 2), 120, yy, r.odd ? key : alpha(PAL.ink, 0.4), { size: 30, align: 'center', weight: r.odd ? 600 : 400 });
        /* a kept row adds its y; an even row's y is struck, as the book strikes it */
        const yt = (r.odd ? '+ ' : '') + commas(r.y);
        text(ctx, yt, Y0 + 260, yy, r.odd ? (cur ? cy : PAL.ink) : alpha(PAL.ink, 0.4), { size: 34, align: 'right', weight: cur ? 600 : 400 });
        if (!r.odd) line(ctx, Y0 + 260 - F.measure(ctx, yt, { size: 34 }), yy, Y0 + 260, yy, alpha(PAL.ink, 0.5), 3);
        if (added(i)) text(ctx, r.odd ? `= ${commas(r.p)}` : '', P0, yy, cur ? cp : PAL.ink, { size: 34, align: 'right', weight: cur ? 600 : 400 });
        if (counted && cur) arrow(ctx, Y0 + 280, yy, P0 - 170, yy, cy, 4);
      });
      /* the kept rows read from the bottom up are x in binary */
      const bits = rows.slice(0, shown).map((r) => r.x % 2).reverse().join('');
      const yb = top + 30 + (rows.length + 0.9) * rh;
      text(ctx, `x mod 2, bottom to top: ${bits || '—'}${shown === rows.length ? ` = ${a} in binary` : ''}`, 120, yb, PAL.muted, { size: 26 });
      F.rich(ctx, [`rows `, [String(shown), C('cost')], ` of ⌊log₂ x⌋ + 1 = ${rows.length}`], 1080, yb + 50, { size: 28, align: 'right' });
    },
  });
})();

/* ================================================================ sim-compass: MultiplyOrDivide */
(function () {
  const PY = [
    'def right_angle(l, P):',
    '    a = choose_point(l)',
    '    a, b = intersect(circle(P, a), l)',
    '    c, d = intersect(circle(a, b), circle(b, a))',
    '    return line(c, d)',
    '',
    'def multiply_or_divide(A, B, C, D):',
    '    alpha = right_angle(line(A, C), A)',
    '    E = intersect(circle(A, B), alpha)',
    '    F = intersect(circle(A, D), alpha)',
    '    beta = right_angle(line(E, C), F)',
    '    gamma = right_angle(beta, F)',
    '    return intersect(gamma, line(A, C))',
  ].join('\n');
  const braced = (ra, mod, T) => [
    `${ra.head} {`,
    `    ${ra.a}`,
    `    ${ra.b}`,
    `    ${ra.cd}`,
    `    ${ra.ret}`,
    '}',
    '',
    `${mod} {`,
    `    ${T.line} alpha = rightAngle(line(A, C), A);`,
    `    ${T.point} E = intersect(circle(A, B), alpha)[0];`,
    `    ${T.point} F = intersect(circle(A, D), alpha)[0];`,
    `    ${T.line} beta = rightAngle(line(E, C), F);`,
    `    ${T.line} gamma = rightAngle(beta, F);`,
    '    return intersect(gamma, line(A, C))[0];',
    '}',
  ].join('\n');
  const JAVA = braced({ head: 'static Line rightAngle(Line l, Point P)', a: 'Point a = choosePoint(l);', b: 'Point b = intersect(circle(P, a), l)[1];', cd: 'Point[] cd = intersect(circle(a, b), circle(b, a));', ret: 'return line(cd[0], cd[1]);' },
    'static Point multiplyOrDivide(Point A, Point B, Point C, Point D)', { line: 'Line', point: 'Point' });
  const CPP = braced({ head: 'Line rightAngle(Line l, Point P)', a: 'Point a = choosePoint(l);', b: 'Point b = intersect(circle(P, a), l)[1];', cd: 'auto cd = intersect(circle(a, b), circle(b, a));', ret: 'return line(cd[0], cd[1]);' },
    'Point multiplyOrDivide(Point A, Point B, Point C, Point D)', { line: 'Line', point: 'Point' });
  const JS = braced({ head: 'function rightAngle(l, P)', a: 'const a = choosePoint(l);', b: 'const b = intersect(circle(P, a), l)[1];', cd: 'const [c, d] = intersect(circle(a, b), circle(b, a));', ret: 'return line(c, d);' },
    'function multiplyOrDivide(A, B, C, D)', { line: 'const', point: 'const' });
  const MAP = lines(5, { 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14 });

  /* the geometry: A at the origin, C straight up at |AC|, B and D on rays drawn as Figure 0.4 draws them, |AB| = 1; drawn turned, below */
  const P = (x, y) => [x, y];
  const add = (p, q) => [p[0] + q[0], p[1] + q[1]], sub = (p, q) => [p[0] - q[0], p[1] - q[1]], mul = (p, s) => [p[0] * s, p[1] * s];
  const len = (p) => Math.hypot(p[0], p[1]), unit = (p) => mul(p, 1 / len(p)), perp = (p) => [-p[1], p[0]];
  const dotp = (p, q) => p[0] * q[0] + p[1] * q[1];
  const foot = (Lp, Ld, Q) => add(Lp, mul(Ld, dotp(sub(Q, Lp), Ld)));         /* Ld a unit direction */
  const meet = (p1, d1, p2, d2) => { const den = d1[0] * d2[1] - d1[1] * d2[0]; const t = ((p2[0] - p1[0]) * d2[1] - (p2[1] - p1[1]) * d2[0]) / den; return add(p1, mul(d1, t)); };
  const RAD = Math.PI / 180;
  const run = (AC, AD, side) => {
    const A = P(0, 0), B = P(Math.cos(107 * RAD), Math.sin(107 * RAD)), Cp = P(0, AC), Dp = P(AD * Math.cos(125 * RAD), AD * Math.sin(125 * RAD));
    const s = side === 'left' ? -1 : 1;
    const shapes = [];    /* everything drawn so far: {kind, …, who} */
    let ops = 0;
    return F.trace((at) => {
      const snap = (L, extra) => at(L, Object.assign({ ops, shapes: shapes.map((x) => Object.assign({}, x)) }, extra));
      /* RightAngle(ℓ, P): the perpendicular to ℓ through P, by two circles; ℓ is a point and a unit direction */
      const rightAngle = (Lp, Ld, Q, who) => {
        at.enter('right_angle');
        const ft = foot(Lp, Ld, Q), r = 0.55;
        const a = add(ft, mul(Ld, r)); ops += 1; shapes.push({ kind: 'pt', p: a, name: 'a', who, tmp: true }); snap(2, {});
        const b = add(ft, mul(Ld, -r));
        shapes.push({ kind: 'circle', c: Q, r: len(sub(a, Q)), who, tmp: true }); shapes.push({ kind: 'pt', p: b, name: 'b', who, tmp: true }); ops += 2; snap(3, {});
        const h = (2 * r) * Math.sqrt(3) / 2, n = perp(Ld), c = add(ft, mul(n, h)), dd = add(ft, mul(n, -h));
        shapes.push({ kind: 'circle', c: a, r: 2 * r, who, tmp: true }); shapes.push({ kind: 'circle', c: b, r: 2 * r, who, tmp: true });
        shapes.push({ kind: 'pt', p: c, name: 'c', who, tmp: true }); shapes.push({ kind: 'pt', p: dd, name: 'd', who, tmp: true }); ops += 3; snap(4, {});
        shapes.push({ kind: 'line', p: c, d: unit(sub(dd, c)), name: '', who, tmp: true }); ops += 1; snap(5, {});
        for (let i = shapes.length - 1; i >= 0; i -= 1) if (shapes[i].tmp) shapes.splice(i, 1);
        at.leave();
        return n;      /* the direction of the new line, which passes through Q */
      };
      snap(7, {});
      const ACd = unit(sub(Cp, A));
      shapes.push({ kind: 'line', p: A, d: ACd, name: '', who: 'AC' });
      const al = rightAngle(A, ACd, A, 'alpha');
      shapes.push({ kind: 'line', p: A, d: al, name: 'α', who: 'alpha' }); snap(8, {});
      const E = add(A, mul(al, -s)); shapes.push({ kind: 'circle', c: A, r: 1, who: 'E' }); shapes.push({ kind: 'pt', p: E, name: 'E', who: 'E' }); ops += 2; snap(9, {});
      const Fp = add(A, mul(al, -s * AD)); shapes.push({ kind: 'circle', c: A, r: AD, who: 'F' }); shapes.push({ kind: 'pt', p: Fp, name: 'F', who: 'F' }); ops += 2; snap(10, {});
      const ECd = unit(sub(Cp, E)); shapes.push({ kind: 'seg', p: E, q: Cp, who: 'EC' }); ops += 1;
      const be = rightAngle(E, ECd, Fp, 'beta');
      shapes.push({ kind: 'line', p: Fp, d: be, name: 'β', who: 'beta' }); snap(11, {});
      const ga = rightAngle(Fp, be, Fp, 'gamma');
      shapes.push({ kind: 'line', p: Fp, d: ga, name: 'γ', who: 'gamma' }); snap(12, {});
      const Z = meet(Fp, ga, A, ACd); shapes.push({ kind: 'pt', p: Z, name: 'Z', who: 'Z' }); ops += 1; snap(13, { done: true });
    });
  };
  /* The scene turned a quarter clockwise from Figure 0.4, so that the line AC, along which Z travels out to
     |AC| · |AD| = 5, runs across the wide canvas and α down it. One scale for every input (fitScale): the
     extents are every point any slider setting and either side reaches; lines run to the box's edge and the
     circles may leave it. */
  const AC_R = [1, 2.5], AD_R = [0.6, 2];
  const turn = (p) => [p[1], p[0]];             /* world (x, y) → page (right, down), in units of |AB| */
  const ext = {};
  ['right', 'left'].forEach((sd) => {
    const e = { x0: Infinity, x1: -Infinity, y0: Infinity, y1: -Infinity };
    const take = (p) => { const q = turn(p); e.x0 = Math.min(e.x0, q[0]); e.x1 = Math.max(e.x1, q[0]); e.y0 = Math.min(e.y0, q[1]); e.y1 = Math.max(e.y1, q[1]); };
    const span = (r, k) => Array.from({ length: k + 1 }, (_, i) => r[0] + ((r[1] - r[0]) * i) / k);
    span(AC_R, 6).forEach((ac) => span(AD_R, 7).forEach((ad) => {
      take([0, 0]); take([Math.cos(107 * RAD), Math.sin(107 * RAD)]); take([0, ac]); take([ad * Math.cos(125 * RAD), ad * Math.sin(125 * RAD)]);
      run(ac, ad, sd).forEach((f) => (f.vars.shapes || []).forEach((sh) => { if (sh.kind === 'pt') take(sh.p); }));
    }));
    ext[sd] = e;
  });
  /* one scale for both sides, the smaller fit; each side centred in the box on its own extents */
  const TOP = 92, BOT = 70, PADX = 70, PADY = 56;
  const EW = Math.max(ext.right.x1 - ext.right.x0, ext.left.x1 - ext.left.x0), EH = Math.max(ext.right.y1 - ext.right.y0, ext.left.y1 - ext.left.y0);
  const H = Math.round(Math.min(1000, TOP + BOT + 2 * PADY + (EH * (1400 - 2 * PADX)) / EW));
  const box = { x0: 40, x1: 1360, y0: TOP, y1: H - BOT };
  const u = F.fitScale({ l: PADX, r: 1400 - PADX, t: TOP + PADY, b: H - BOT - PADY }, { w: EW, h: EH });
  const ox = (sd) => 700 - ((ext[sd].x0 + ext[sd].x1) / 2) * u, oy = (sd) => (TOP + PADY + H - BOT - PADY) / 2 - ((ext[sd].y0 + ext[sd].y1) / 2) * u;
  const X = (p) => ox(side) + turn(p)[0] * u, Y = (p) => oy(side) + turn(p)[1] * u;
  /* a line through p along dd, cut to the box, in page coordinates */
  const clipLine = (p, dd) => {
    const P0 = [X(p), Y(p)], D = turn(dd), ts = [];
    const try2 = (t) => { const q = [P0[0] + D[0] * t, P0[1] + D[1] * t]; if (q[0] >= box.x0 - 0.5 && q[0] <= box.x1 + 0.5 && q[1] >= box.y0 - 0.5 && q[1] <= box.y1 + 0.5) ts.push(t); };
    [box.x0, box.x1].forEach((x) => { if (D[0]) try2((x - P0[0]) / D[0]); });
    [box.y0, box.y1].forEach((y) => { if (D[1]) try2((y - P0[1]) / D[1]); });
    ts.sort((a, b) => a - b); return ts.length >= 2 ? [[P0[0] + D[0] * ts[0], P0[1] + D[1] * ts[0]], [P0[0] + D[0] * ts[ts.length - 1], P0[1] + D[1] * ts[ts.length - 1]]] : null;
  };
  let AC = 2.0, AD = 1.75, side = 'right', total = 0;
  const d = sim('sim-compass', H);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: AIS,
    lineMap: { java: MAP, cpp: MAP, javascript: MAP },
    blocks: [
      { id: 'ra', lines: [2, 5], label: 'construct a perpendicular with two circles (RightAngle)', touches: ['shapes'] },
      { id: 'ra-a', lines: [2, 2], label: 'choose a point a on the line', touches: ['shapes'] },
      { id: 'ra-b', lines: [3, 3], label: 'the circle about P through a meets the line again at b', touches: ['shapes'] },
      { id: 'ra-cd', lines: [4, 4], label: 'the circles about a and b meet at c and d', touches: ['shapes'] },
      { id: 'ra-line', lines: [5, 5], label: 'the line through c and d is the perpendicular', touches: ['shapes'] },
      { id: 'alpha', lines: [8, 8], label: 'raise the perpendicular α to AC at A', touches: ['shapes'] },
      { id: 'E', lines: [9, 9], label: 'E: mark |AB| along α', touches: ['shapes'] },
      { id: 'F', lines: [10, 10], label: 'F: mark |AD| along α', touches: ['shapes'] },
      { id: 'beta', lines: [11, 11], label: 'β: the perpendicular to EC through F', touches: ['shapes'] },
      { id: 'gamma', lines: [12, 12], label: 'γ: the perpendicular to β through F, parallel to EC', touches: ['shapes'] },
      { id: 'Z', lines: [13, 13], label: 'Z: where γ meets the line AC', touches: ['shapes'] },
    ],
    refs: { python: { C: () => F.ref('C'), D: () => F.ref('D') }, java: { C: () => F.ref('C'), D: () => F.ref('D') }, cpp: { C: () => F.ref('C'), D: () => F.ref('D') }, javascript: { C: () => F.ref('C'), D: () => F.ref('D') } },
  });
  const traced = () => { const fr = run(AC, AD, side); total = fr[fr.length - 1].vars.ops; return fr; };
  const dbg = F.debug(d, {
    code, watch: false, trace: traced(),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const v = g.frame.vars, shapes = v.shapes || [];
      const cC = F.ref('C'), cD = F.ref('D'), cZ = F.ref('Z');
      const Bp = [Math.cos(107 * RAD), Math.sin(107 * RAD)], Cp = [0, AC], Dp = [AD * Math.cos(125 * RAD), AD * Math.sin(125 * RAD)];
      const AZ = AC * AD;
      topline(ctx, v.done ? `|AZ| = |AC| · |AD| / |AB| = ${fmt(AC, 2)} × ${fmt(AD, 2)} / 1 = ${fmt(AZ, 2)}` : 'Z lands where |AZ| = |AC| · |AD| / |AB|.');
      /* the invariant: once Z is placed, the triangles ACE and AZF are similar */
      const E = shapes.find((s) => s.name === 'E'), Fq = shapes.find((s) => s.name === 'F'), Zs = shapes.find((s) => s.name === 'Z');
      if (E && Fq && Zs) {
        ctx.save(); ctx.fillStyle = alpha(PAL.ink, 0.06); ctx.beginPath(); ctx.moveTo(X([0, 0]), Y([0, 0])); ctx.lineTo(X(Zs.p), Y(Zs.p)); ctx.lineTo(X(Fq.p), Y(Fq.p)); ctx.closePath(); ctx.fill();
        ctx.fillStyle = alpha(PAL.ink, 0.1); ctx.beginPath(); ctx.moveTo(X([0, 0]), Y([0, 0])); ctx.lineTo(X(Cp), Y(Cp)); ctx.lineTo(X(E.p), Y(E.p)); ctx.closePath(); ctx.fill(); ctx.restore();
      }
      const latest = g.block ? g.block.id : '';
      ctx.save(); ctx.beginPath(); ctx.rect(box.x0, box.y0, box.x1 - box.x0, box.y1 - box.y0); ctx.clip();
      shapes.forEach((s) => {
        const tmp = !!s.tmp, col = tmp ? alpha(PAL.ink, 0.45) : PAL.ink, w = tmp ? 2 : 3;
        if (s.kind === 'line') { const seg = clipLine(s.p, s.d); if (seg) line(ctx, seg[0][0], seg[0][1], seg[1][0], seg[1][1], col, w); }
        if (s.kind === 'seg') line(ctx, X(s.p), Y(s.p), X(s.q), Y(s.q), alpha(PAL.ink, 0.6), 2, [8, 8]);
        if (s.kind === 'circle') { ctx.save(); ctx.strokeStyle = col; ctx.lineWidth = w; if (tmp) ctx.setLineDash([6, 8]); ctx.beginPath(); ctx.arc(X(s.c), Y(s.c), s.r * u, 0, 2 * Math.PI); ctx.stroke(); ctx.restore(); }
      });
      ctx.restore();
      /* the inputs: A, the segments to B, C and D, as the book draws them */
      line(ctx, X([0, 0]), Y([0, 0]), X(Bp), Y(Bp), PAL.ink, 6);
      line(ctx, X([0, 0]), Y([0, 0]), X(Cp), Y(Cp), cC, 6);
      line(ctx, X([0, 0]), Y([0, 0]), X(Dp), Y(Dp), cD, 6);
      dot(ctx, X([0, 0]), Y([0, 0]), PAL.ink, true, 10); text(ctx, 'A', X([0, 0]) + 22, Y([0, 0]) + 30, PAL.ink, { size: 32 });
      dot(ctx, X(Bp), Y(Bp), PAL.ink, true, 10); text(ctx, 'B', X(Bp) + 24, Y(Bp) + 4, PAL.ink, { size: 32 });
      dot(ctx, X(Cp), Y(Cp), cC, true, 10); text(ctx, 'C', X(Cp) + 22, Y(Cp) - 22, cC, { size: 32, weight: 600 });
      dot(ctx, X(Dp), Y(Dp), cD, true, 10); text(ctx, 'D', X(Dp) + 22, Y(Dp) - 28, cD, { size: 32, weight: 600 });
      shapes.forEach((s) => {
        if (s.kind === 'pt') {
          const isZ = s.name === 'Z', col = isZ ? cZ : s.tmp ? alpha(PAL.ink, 0.6) : PAL.ink;
          dot(ctx, X(s.p), Y(s.p), col, !s.tmp || isZ, isZ ? 12 : 9);
          if (!s.tmp || latest.startsWith('ra')) text(ctx, s.name, X(s.p) + 20, Y(s.p) + (s.tmp ? -24 : 30), col, { size: s.tmp ? 26 : 32, weight: isZ ? 600 : 400, italic: s.tmp });
        }
        if (s.kind === 'line' && s.name) { const seg = clipLine(s.p, s.d); if (seg) { const q = seg[1][1] > seg[0][1] || (seg[1][1] === seg[0][1] && seg[1][0] > seg[0][0]) ? seg[1] : seg[0]; text(ctx, s.name, Math.min(box.x1 - 24, Math.max(box.x0 + 24, q[0] + 24)), Math.min(box.y1 - 20, Math.max(box.y0 + 24, q[1] - 6)), PAL.ink, { size: 32, italic: true }); } }
      });
      F.rich(ctx, [`primitive operations `, [String(v.ops ?? 0), C('cost')], ` of ${total}, the same for every input: O(1)`], 700, H - 34, { size: 26, align: 'center', bg: PAL.panel });
    },
  });
  const rebuild = () => dbg.set(traced());
  const sAC = ctl(d.controls, { label: '|AC|', cls: '', key: 'ac', min: AC_R[0], max: AC_R[1], step: 0.05, value: AC, unit: '', dec: 2, onInput: () => { AC = sAC.v; rebuild(); } });
  const sAD = ctl(d.controls, { label: '|AD|', cls: '', key: 'ad', min: AD_R[0], max: AD_R[1], step: 0.05, value: AD, unit: '', dec: 2, onInput: () => { AD = sAD.v; rebuild(); } });
  choice(d.controls, { label: '\\text{E and F}', key: 'side', value: side, options: [{ value: 'right', label: 'below A' }, { value: 'left', label: 'above A' }], onInput: (val) => { side = val; rebuild(); } });
})();

/* ================================================================ sim-apportion: ApportionCongress */
(function () {
  /* DATA census-2020 BEGIN (tools/inline_census.py writes this from sources/_cache/census-2020/res2020.csv) */
  const CENSUS = [
    ["Alabama", 5024279, 7],
    ["Alaska", 733391, 1],
    ["Arizona", 7151502, 9],
    ["Arkansas", 3011524, 4],
    ["California", 39538223, 52],
    ["Colorado", 5773714, 8],
    ["Connecticut", 3605944, 5],
    ["Delaware", 989948, 1],
    ["Florida", 21538187, 28],
    ["Georgia", 10711908, 14],
    ["Hawaii", 1455271, 2],
    ["Idaho", 1839106, 2],
    ["Illinois", 12812508, 17],
    ["Indiana", 6785528, 9],
    ["Iowa", 3190369, 4],
    ["Kansas", 2937880, 4],
    ["Kentucky", 4505836, 6],
    ["Louisiana", 4657757, 6],
    ["Maine", 1362359, 2],
    ["Maryland", 6177224, 8],
    ["Massachusetts", 7029917, 9],
    ["Michigan", 10077331, 13],
    ["Minnesota", 5706494, 8],
    ["Mississippi", 2961279, 4],
    ["Missouri", 6154913, 8],
    ["Montana", 1084225, 2],
    ["Nebraska", 1961504, 3],
    ["Nevada", 3104614, 4],
    ["New Hampshire", 1377529, 2],
    ["New Jersey", 9288994, 12],
    ["New Mexico", 2117522, 3],
    ["New York", 20201249, 26],
    ["North Carolina", 10439388, 14],
    ["North Dakota", 779094, 1],
    ["Ohio", 11799448, 15],
    ["Oklahoma", 3959353, 5],
    ["Oregon", 4237256, 6],
    ["Pennsylvania", 13002700, 17],
    ["Rhode Island", 1097379, 2],
    ["South Carolina", 5118425, 7],
    ["South Dakota", 886667, 1],
    ["Tennessee", 6910840, 9],
    ["Texas", 29145505, 38],
    ["Utah", 3271616, 4],
    ["Vermont", 643077, 1],
    ["Virginia", 8631393, 11],
    ["Washington", 7705281, 10],
    ["West Virginia", 1793716, 2],
    ["Wisconsin", 5893718, 8],
    ["Wyoming", 576851, 1],
  ];
  /* DATA census-2020 END */
  const PY = [
    'def apportion_congress(Pop, R):',
    '    PQ = PriorityQueue()',
    '    n = len(Pop)',
    '    Rep = [0] * n',
    '    for s in range(n):',
    '        Rep[s] = 1',
    '        PQ.insert(s, Pop[s] / math.sqrt(2))',
    '    for i in range(R - n):',
    '        s = PQ.extract_max()',
    '        Rep[s] = Rep[s] + 1',
    '        priority = Pop[s] / math.sqrt(Rep[s] * (Rep[s] + 1))',
    '        PQ.insert(s, priority)',
    '    return Rep',
  ].join('\n');
  const braced = (head, o) => [
    `${head} {`,
    `    ${o.pq}`,
    `    ${o.n}`,
    `    ${o.rep}`,
    `    for (${o.int} s = 0; s < n; s++) {`,
    '        Rep[s] = 1;',
    `        PQ.insert(s, Pop[s] / ${o.sqrt}(2));`,
    '    }',
    `    for (${o.int} i = 0; i < R - n; i++) {`,
    `        ${o.int} s = PQ.${o.extract}();`,
    '        Rep[s] = Rep[s] + 1;',
    `        ${o.dbl} priority = Pop[s] / ${o.sqrt}(Rep[s] * (Rep[s] + 1.0));`,
    '        PQ.insert(s, priority);',
    '    }',
    '    return Rep;',
    '}',
  ].join('\n');
  const JAVA = braced('static int[] apportionCongress(long[] Pop, int R)', { pq: 'PriorityQueue PQ = new PriorityQueue();', n: 'int n = Pop.length;', rep: 'int[] Rep = new int[n];', int: 'int', sqrt: 'Math.sqrt', extract: 'extractMax', dbl: 'double' });
  const CPP = braced('std::vector<int> apportionCongress(const std::vector<long>& Pop, int R)', { pq: 'PriorityQueue PQ;', n: 'int n = Pop.size();', rep: 'std::vector<int> Rep(n, 0);', int: 'int', sqrt: 'std::sqrt', extract: 'extractMax', dbl: 'double' });
  const JS = braced('function apportionCongress(Pop, R)', { pq: 'const PQ = new PriorityQueue();', n: 'const n = Pop.length;', rep: 'const Rep = new Array(n).fill(0);', int: 'let', sqrt: 'Math.sqrt', extract: 'extractMax', dbl: 'const' })
    .replace('let s = PQ.extractMax();', 'const s = PQ.extractMax();');
  const MAP = lines(7, { 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 15 });
  const FOUR = ['California', 'Texas', 'Florida', 'New York'];
  /* four states first, to step through seat by seat; the whole House, to run to its end */
  const SETS = {
    four: { label: '4 states, R = 12', R: 12, states: () => CENSUS.filter((c) => FOUR.includes(c[0])) },
    house: { label: '50 states, R = 435', R: 435, states: () => CENSUS },
  };
  /* the priority queue, kept as the Census Bureau keeps it: one sorted column */
  const run = (states, R) => F.trace((at) => {
    const Pop = states.map((c) => c[1]), n = Pop.length, Rep = new Array(n).fill(0), PQ = [];
    const insert = (s, p) => { PQ.push([s, p]); PQ.sort((a, b) => b[1] - a[1]); };
    const pq = () => PQ.map(([s, p]) => [s, Math.round(p)]);
    at(2, { PQ: [] }); at(3, { n, PQ: [] }); at(4, { n, Rep, PQ: [] });
    for (let s = 0; s < n; s += 1) {
      at(5, { s, Rep, PQ: pq() });
      Rep[s] = 1; at(6, { s, Rep, PQ: pq() });
      insert(s, Pop[s] / Math.SQRT2); at(7, { s, Rep, PQ: pq(), priority: Math.round(Pop[s] / Math.SQRT2) });
    }
    for (let i = 0; i < R - n; i += 1) {
      at(8, { i, Rep, PQ: pq() });
      const [s] = PQ.shift(); at(9, { i, s, Rep, PQ: pq() }, ['extract', s]);
      Rep[s] += 1; at(10, { i, s, Rep, PQ: pq() });
      const priority = Pop[s] / Math.sqrt(Rep[s] * (Rep[s] + 1)); at(11, { i, s, Rep, PQ: pq(), priority: Math.round(priority) });
      insert(s, priority); at(12, { i, s, Rep, PQ: pq(), priority: Math.round(priority) });
    }
    at(13, { Rep, PQ: pq() });
  });
  /* one height for both inputs: the bars run the full height on the left, the queue's head is at the top on the
     right, and the House shows as many rows of its queue as the bars' height holds */
  const AH = 760, ATOP = 92;
  const d = sim('sim-apportion', AH);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: AIS,
    lineMap: { java: MAP, cpp: MAP, javascript: MAP },
    blocks: [
      { id: 'init', lines: [2, 4], label: 'an empty priority queue', touches: ['PQ'] },
      { id: 'first', lines: [5, 7], label: 'give every state its first representative', touches: ['s', 'Rep', 'PQ'] },
      { id: 'seat', lines: [8, 12], label: 'allocate the next seat', touches: ['s', 'Rep', 'PQ'] },
      { id: 'pick', lines: [9, 9], label: 'take the state with the highest priority', touches: ['s', 'PQ'] },
      { id: 'give', lines: [10, 10], label: 'give it a seat', touches: ['Rep'] },
      { id: 'requeue', lines: [11, 12], label: 'recompute its priority and put it back', touches: ['priority', 'PQ'] },
    ],
    refs: { s: () => F.ref('s') },
  });
  F.debug(d, {
    code, watch: ['s', 'i', 'priority'], beat: 0.9,
    inputs: Object.entries(SETS).map(([value, o]) => ({ value, label: o.label, trace: run(o.states(), o.R) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const set = SETS[g.input], states = set.states(), n = states.length, R = set.R;
      const v = g.frame.vars, Rep = v.Rep || new Array(n).fill(0), PQ = v.PQ || [], s = v.s, cs = F.ref('s');
      const seats = Rep.reduce((a, b) => a + b, 0), done = g.frame.line === 13;
      if (!set.final) { const fr = run(states, R); set.final = fr[fr.length - 1].vars.Rep; }
      const max = Math.max(...set.final) + 1;      /* one scale for the whole run: the most seats any state ends with */
      const few = n <= 10, bx0 = 60, bx1 = few ? 760 : 900, by = AH - (few ? 150 : 110), bh = by - ATOP - 56, bw = (bx1 - bx0) / n;
      if (done) {
        const same = states.every((c, k) => c[2] === Rep[k]);
        topline(ctx, n === 50 ? `All 435 seats given out${same ? ': every state has its seats in the 2020 apportionment.' : '.'}` : `All ${R} seats given out.`);
      } else if (typeof v.i === 'number' && typeof s === 'number') topline(ctx, `Seat ${n + v.i + 1} goes to ${states[s][0]}, now ${Rep[s]} seat${Rep[s] === 1 ? '' : 's'}.`);
      else topline(ctx, `Every state first gets one seat: ${seats} of ${R} so far.`);
      /* the House: one bar per state, its seats so far; the state just served in its referent colour */
      line(ctx, bx0, by, bx1, by, PAL.rule, 2);
      states.forEach((c, k) => {
        const h = (Rep[k] / max) * bh, x = bx0 + k * bw, on = k === s && !done;
        rect(ctx, x + bw * 0.15, by - h, bw * 0.7, h, on ? cs : alpha(C('size'), 0.55), null);
        if (few) {
          text(ctx, c[0], x + bw / 2, by + 30, on ? cs : PAL.ink, { size: 28, align: 'center', weight: on ? 600 : 400 });
          text(ctx, String(Rep[k]), x + bw / 2, by - h - 26, on ? cs : PAL.ink, { size: 30, align: 'center', weight: 600 });
        }
      });
      if (n > 10 && typeof s === 'number' && !done) text(ctx, `${states[s][0]} ${Rep[s]}`, Math.min(bx1 - 40, Math.max(bx0 + 60, bx0 + (s + 0.5) * bw)), by - (Rep[s] / max) * bh - 30, cs, { size: 28, align: 'center', weight: 600 });
      text(ctx, 'seats per state', bx0, by + (few ? 74 : 34), C('size'), { size: 24 });
      /* the queue: one sorted column, the head at the top */
      const qx = few ? 820 : 960, qy = ATOP + 26, pitch = few ? 84 : 52, rows = few ? n : Math.floor((by - 20 - qy - 46) / pitch);
      text(ctx, 'priority queue, highest first', qx, qy, PAL.muted, { size: 24 });
      const fs = few ? 32 : 26, rh = few ? 64 : 44;
      PQ.slice(0, rows).forEach(([k, p], r) => {
        const y = qy + 46 + r * pitch, head = r === 0;
        rect(ctx, qx, y - rh / 2, 1340 - qx, rh, head ? alpha(C('key'), 0.12) : null, PAL.rule, 1.5);
        text(ctx, states[k][0], qx + 12, y, PAL.ink, { size: fs, weight: head ? 600 : 400 });
        text(ctx, commas(p), 1330, y, C('key'), { size: fs, align: 'right' });
      });
      if (PQ.length > rows) text(ctx, `… ${PQ.length - rows} more`, qx + 12, qy + 46 + rows * pitch, PAL.muted, { size: 24 });
      const calls = typeof v.i === 'number' ? v.i + (g.frame.line >= 9 ? 1 : 0) : done ? R - n : 0;
      F.rich(ctx, [`ExtractMax calls `, [String(calls), C('cost')], ` of R − n = ${R - n} · seats `, [String(seats), C('cost')], ` of ${R}`], 700, AH - 34, { size: 26, align: 'center' });
    },
  });
})();

/* ================================================================ sim-scan-cost: the need for efficiency (still) */
(function () {
  const d = sim('sim-scan-cost', 560);
  const sup = (e) => String(e).split('').map((c) => '⁰¹²³⁴⁵⁶⁷⁸⁹'['0123456789'.indexOf(c)] ?? (c === '.' ? '·' : c)).join('');
  const sci = (x) => { const e = Math.floor(Math.log10(x) + 1e-9), m = x / 10 ** e; return Math.abs(m - 1) < 0.005 ? `10${sup(e)}` : `${fmt(m, m < 10 ? 2 : 1).replace(/\.?0+$/, '')} × 10${sup(e)}`; };
  const texSci = (x) => { const e = Math.floor(Math.log10(x) + 1e-9), m = x / 10 ** e; return Math.abs(m - 1) < 0.005 ? `10^{${e}}` : `${fmt(m, 2).replace(/\.?0+$/, '')}\\times 10^{${e}}`; };
  const human = (t) => {
    if (t < 1e-6) return `${fmt(t * 1e9, 1)} ns`; if (t < 1e-3) return `${fmt(t * 1e6, 1)} µs`; if (t < 1) return `${fmt(t * 1e3, 1)} ms`;
    if (t < 60) return `${fmt(t, 1)} s`;
    if (t < 3600) { const m = Math.floor(t / 60), s = Math.round(t - 60 * m); return `${m} min ${s} s`; }
    if (t < 86400) return `${fmt(t / 3600, 1)} hours`; if (t < 3.156e7) return `${fmt(t / 86400, 1)} days`;
    return `${fmt(t / 3.156e7, 1)} years`;
  };
  const sN = ctl(d.controls, { label: '\\log_{10} n', cls: 'size', key: 'n', min: 3, max: 10, step: 0.01, value: 6, unit: '', dec: 2, detents: [{ v: 6, label: '10⁶' }, { v: Math.log10(8.5e9), label: '8.5 × 10⁹' }] });
  const sM = ctl(d.controls, { label: '\\log_{10} m', cls: 'size', key: 'm', min: 3, max: 10, step: 0.01, value: 6, unit: '', dec: 2, detents: [{ v: 6, label: '10⁶' }] });
  const sV = ctl(d.controls, { label: '\\log_{10}\\text{ speed}', cls: '', key: 'speed', min: 8, max: 10, step: 0.01, value: 9, unit: '', dec: 2, detents: [{ v: 9, label: '10⁹ per second' }] });
  const how = choice(d.controls, { label: '\\text{inspects}', key: 'scan', value: 'all', options: [{ value: 'all', label: 'every item' }, { value: 'two', label: 'two items' }] });
  const MARKS = [[1e-9, '1 ns'], [1e-6, '1 µs'], [1e-3, '1 ms'], [1, '1 s'], [60, '1 min'], [3600, '1 h'], [86400, '1 day'], [3.156e7, '1 year'], [3.156e9, '1 century']];
  function draw() {
    const { ctx } = begin(d.c);
    const n = 10 ** sN.v, m = 10 ** sM.v, speed = 10 ** sV.v, per = how.value === 'all' ? n : 2, ins = per * m, t = ins / speed;
    topline(ctx, `${sci(m)} operations ${how.value === 'all' ? `over ${sci(n)} items` : 'inspecting about two items each'}: ${sci(ins)} inspections, ${human(t)}.`);
    /* a time line from a nanosecond to a century, log scale, the run's time marked on it */
    const x0 = 110, x1 = 1290, y = 300, lo = Math.log10(1e-10), hi = Math.log10(1e11), X = (s) => x0 + ((Math.log10(s) - lo) / (hi - lo)) * (x1 - x0);
    line(ctx, x0, y, x1, y, PAL.ink, 3);
    MARKS.forEach(([s, l], k) => { line(ctx, X(s), y - 12, X(s), y + 12, PAL.ink, 2); text(ctx, l, X(s), y + (k % 2 ? 70 : 40), PAL.muted, { size: 22, align: 'center' }); });
    const tx = Math.min(x1, Math.max(x0, X(Math.max(t, 1e-12)))), col = C('cost');
    ctx.save(); ctx.fillStyle = alpha(col, 0.18); ctx.fillRect(x0, y - 24, tx - x0, 48); ctx.restore();
    dot(ctx, tx, y, col, true, 12);
    text(ctx, human(t), tx, y - 56, col, { size: 34, align: 'center', weight: 600 });
    text(ctx, 'time the run takes', x0, y - 110, PAL.muted, { size: 24 });
    /* the count it is made of */
    text(ctx, `${sci(ins)} inspections = ${how.value === 'all' ? `${sci(n)} items` : 'about 2 items'} × ${sci(m)} operations`, 700, 450, C('size'), { size: 30, align: 'center' });
    tex(d.readout, `t = \\frac{${how.value === 'all' ? 'n' : '2'}\\cdot m}{\\text{speed}} = \\frac{${texSci(ins)}}{${texSci(speed)}} = ${texSci(t).replace(/^10\^\{0\}$/, '1')}\\ \\text{s}${t >= 60 ? `\\approx \\text{${human(t)}}` : ''}`);
  }
  register(d.fig, { update: () => {}, draw });
})();
};
