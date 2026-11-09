/* Figures for section 2.4 Prefix sums and difference arrays. Boots against the section's text article.
   Two debugger figures (code beside the drawing, stepped by block: METHOD §2.3). Their code panels are doocs/leetcode's
   Solution 1 of 0304 and of 0370 (CC BY-SA 4.0, ruling 3 / decision 18), which doocs prints in all four languages,
   read from the cache by inline_code.py into the generated block below. Each trace is the figure's own JS copy of the
   canonical language's code (Python for 0304; Java for 0370, whose prefix pass is a loop of lines where Python's is
   one call). OI Wiki's own code is outside its licence and is not shown.
   sim-prefix-2d draws its two blocks blue and red because the text names them so (F.fact; the figure row's facts). */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['2.4'] = function (root, F) {
const { C, PAL, alpha, text, measure, line, arrow, topline } = F;
const sim = (id, H) => F.sim(root, id, H);
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2, dash) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};
const num = (x) => String(x).replace('-', '−');                     /* a minus sign, not a hyphen */
const signed = (x) => (x < 0 ? `− ${-x}` : `+ ${x}`);
/* a line of coloured runs, centred on cx: parts are [text, colour, weight?] */
const runs = (ctx, parts, cx, y, size) => {
  const ws = parts.map((p) => measure(ctx, p[0], { size, weight: p[2] || 400 }));
  let x = cx - ws.reduce((a, b) => a + b, 0) / 2;
  parts.forEach((p, k) => { text(ctx, p[0], x, y, p[1], { size, weight: p[2] || 400, align: 'left' }); x += ws[k]; });
};

/* @generated doocs: inline_code.py */
const DOOCS_0304 = {
  "python": "class NumMatrix:\n    def __init__(self, matrix: List[List[int]]):\n        m, n = len(matrix), len(matrix[0])\n        self.s = [[0] * (n + 1) for _ in range(m + 1)]\n        for i, row in enumerate(matrix):\n            for j, v in enumerate(row):\n                self.s[i + 1][j + 1] = (\n                    self.s[i][j + 1] + self.s[i + 1][j] - self.s[i][j] + v\n                )\n\n    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:\n        return (\n            self.s[row2 + 1][col2 + 1]\n            - self.s[row2 + 1][col1]\n            - self.s[row1][col2 + 1]\n            + self.s[row1][col1]\n        )",
  "java": "class NumMatrix {\n    private int[][] s;\n\n    public NumMatrix(int[][] matrix) {\n        int m = matrix.length, n = matrix[0].length;\n        s = new int[m + 1][n + 1];\n        for (int i = 0; i < m; ++i) {\n            for (int j = 0; j < n; ++j) {\n                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + matrix[i][j];\n            }\n        }\n    }\n\n    public int sumRegion(int row1, int col1, int row2, int col2) {\n        return s[row2 + 1][col2 + 1] - s[row2 + 1][col1] - s[row1][col2 + 1] + s[row1][col1];\n    }\n}",
  "cpp": "class NumMatrix {\npublic:\n    vector<vector<int>> s;\n\n    NumMatrix(vector<vector<int>>& matrix) {\n        int m = matrix.size(), n = matrix[0].size();\n        s.resize(m + 1, vector<int>(n + 1));\n        for (int i = 0; i < m; ++i) {\n            for (int j = 0; j < n; ++j) {\n                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + matrix[i][j];\n            }\n        }\n    }\n\n    int sumRegion(int row1, int col1, int row2, int col2) {\n        return s[row2 + 1][col2 + 1] - s[row2 + 1][col1] - s[row1][col2 + 1] + s[row1][col1];\n    }\n};",
  "javascript": "/**\n * @param {number[][]} matrix\n */\nvar NumMatrix = function (matrix) {\n    const m = matrix.length;\n    const n = matrix[0].length;\n    this.s = new Array(m + 1).fill(0).map(() => new Array(n + 1).fill(0));\n    for (let i = 0; i < m; ++i) {\n        for (let j = 0; j < n; ++j) {\n            this.s[i + 1][j + 1] =\n                this.s[i + 1][j] + this.s[i][j + 1] - this.s[i][j] + matrix[i][j];\n        }\n    }\n};\n\n/**\n * @param {number} row1\n * @param {number} col1\n * @param {number} row2\n * @param {number} col2\n * @return {number}\n */\nNumMatrix.prototype.sumRegion = function (row1, col1, row2, col2) {\n    return (\n        this.s[row2 + 1][col2 + 1] -\n        this.s[row2 + 1][col1] -\n        this.s[row1][col2 + 1] +\n        this.s[row1][col1]\n    );\n};"
};
const DOOCS_0370 = {
  "python": "class Solution:\n    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:\n        d = [0] * length\n        for l, r, c in updates:\n            d[l] += c\n            if r + 1 < length:\n                d[r + 1] -= c\n        return list(accumulate(d))",
  "java": "class Solution {\n    public int[] getModifiedArray(int length, int[][] updates) {\n        int[] d = new int[length];\n        for (var e : updates) {\n            int l = e[0], r = e[1], c = e[2];\n            d[l] += c;\n            if (r + 1 < length) {\n                d[r + 1] -= c;\n            }\n        }\n        for (int i = 1; i < length; ++i) {\n            d[i] += d[i - 1];\n        }\n        return d;\n    }\n}",
  "cpp": "class Solution {\npublic:\n    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {\n        vector<int> d(length);\n        for (const auto& e : updates) {\n            int l = e[0], r = e[1], c = e[2];\n            d[l] += c;\n            if (r + 1 < length) {\n                d[r + 1] -= c;\n            }\n        }\n        for (int i = 1; i < length; ++i) {\n            d[i] += d[i - 1];\n        }\n        return d;\n    }\n};",
  "javascript": "/**\n * @param {number} length\n * @param {number[][]} updates\n * @return {number[]}\n */\nvar getModifiedArray = function (length, updates) {\n    const d = Array(length).fill(0);\n    for (const [l, r, c] of updates) {\n        d[l] += c;\n        if (r + 1 < length) {\n            d[r + 1] -= c;\n        }\n    }\n    for (let i = 1; i < length; ++i) {\n        d[i] += d[i - 1];\n    }\n    return d;\n};"
};
/* @end generated */

/* ================================================================ sim-prefix-2d: doocs 0304, OI Wiki's matrix */
(function () {
  const A = [[1, 2, 4, 3], [5, 1, 2, 4], [6, 3, 5, 9]];     /* OI Wiki's example (images/prefix-sum-2d.tex) */
  const M = A.length, N = A[0].length;
  /* canonical Python line → line of the other languages */
  const MAP = {
    java: { 1: 1, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 9, 9: 9, 10: 13, 11: 14, 12: 15, 13: 15, 14: 15, 15: 15, 16: 15, 17: 15 },
    cpp: { 1: 1, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9, 7: 10, 8: 10, 9: 10, 10: 14, 11: 15, 12: 16, 13: 16, 14: 16, 15: 16, 16: 16, 17: 16 },
    javascript: { 1: 4, 2: 4, 3: [5, 6], 4: 7, 5: 8, 6: 9, 7: [10, 11], 8: 11, 9: 11, 10: 15, 11: 23, 12: 24, 13: 25, 14: 26, 15: 27, 16: 28, 17: 29 },
  };
  /* the build and one query, as frames of the Python: s is the padded table (s[i][j] is the text's S_{i,j}) */
  const run = (q) => F.trace((at) => {
    const s = Array.from({ length: M + 1 }, () => new Array(N + 1).fill(0));
    at(3, { m: M, n: N });
    at(4, { m: M, n: N, s });
    for (let i = 0; i < M; i += 1) {
      at(5, { i, s });
      for (let j = 0; j < N; j += 1) {
        const v = A[i][j];
        at(6, { i, j, v, s });
        s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + v;
        at(7, { i, j, v, s }, ['fill', i + 1, j + 1]);
      }
    }
    const [row1, col1, row2, col2] = q;
    const t = [s[row2 + 1][col2 + 1], -s[row2 + 1][col1], -s[row1][col2 + 1], s[row1][col1]];
    let acc = 0;
    [13, 14, 15, 16].forEach((L, k) => { acc += t[k]; at(L, { row1, col1, row2, col2, s, acc, term: k }); });
    at(17, { row1, col1, row2, col2, s, acc, term: 4 });
  });
  const QUERIES = [
    { value: 'cell', label: 'the cell A₃,₃', q: [2, 2, 2, 2] },
    { value: 'block', label: 'rows 2–3, columns 2–3', q: [1, 1, 2, 2] },
    { value: 'all', label: 'the whole matrix', q: [0, 0, 2, 3] },
  ];

  const d = sim('sim-prefix-2d', 720);
  const code = F.code(d, {
    src: DOOCS_0304, lineMap: MAP,
    blocks: [
      { id: 'pad', lines: [3, 4], label: 'a table of zeros, one row and one column larger', touches: ['s'] },
      { id: 'row', lines: [5, 9], label: 'row i of the matrix', touches: ['i'] },
      { id: 'cell', lines: [6, 9], label: 'add v to the blocks above and to the left, less their overlap', touches: ['s', 'i', 'j', 'v'] },
      { id: 'query', lines: [12, 17], label: 'four cells of the table', touches: ['s', 'row1', 'col1', 'row2', 'col2'] },
      { id: 'q1', lines: [13, 13], label: 'the rectangle from the corner to (row2, col2)', touches: ['s'] },
      { id: 'q2', lines: [14, 14], label: 'less the columns left of col1', touches: ['s'] },
      { id: 'q3', lines: [15, 15], label: 'less the rows above row1', touches: ['s'] },
      { id: 'q4', lines: [16, 16], label: 'plus the corner taken away twice', touches: ['s'] },
    ],
  });

  /* the two grids: A on the left with the text's indices 1..m, 1..n; S on the right with its row and column 0 */
  const CELL = 88, AX = 150, AY = 236, SX = 1400 - 120 - (N + 1) * CELL, SY = AY - CELL;
  const ax = (j) => AX + (j - 1) * CELL, ay = (i) => AY + (i - 1) * CELL;     /* A_{i,j}, 1-based */
  const sx = (j) => SX + j * CELL, sy = (i) => SY + i * CELL;                 /* S_{i,j}, 0-based = the text's */
  const sub = (i, j) => `${i},${j}`;
  const S_ = (i, j) => `S_{${sub(i, j)}}`, A_ = (i, j) => `A_{${sub(i, j)}}`;
  const tip = { hits: [] };
  F.hover(d.stage, () => tip.hits, d.c);

  F.debug(d, {
    code, level: 1, watch: ['i', 'j', 'v', 'row1', 'col1', 'row2', 'col2', 'acc'],
    inputs: QUERIES.map((o) => ({ value: o.value, label: o.label, trace: run(o.q) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const v = g.frame.vars, ln = g.frame.line, k = g.k;
      const key = C('key'), cost = C('cost'), BLUE = F.fact('#2f6fd6'), RED = F.fact('#d64538');
      const s = v.s || null, hits = [];
      const building = ln >= 5 && ln <= 9, querying = ln >= 13;   /* lines 13–17: the query */
      /* the cell being filled (the text's indices), and the cells written so far in row order */
      const I = building && v.j !== undefined ? v.i + 1 : null, J = building && v.j !== undefined ? v.j + 1 : null;
      const order = (i, j) => (i - 1) * N + j;
      const written = (i, j) => querying || (I !== null && (order(i, j) < order(I, J) || (order(i, j) === order(I, J) && ln === 7)));

      /* ---------- the blocks on A: a tint per term, the text's colours */
      const block = (i, j, color, op = 1) => {          /* rows 1..i, columns 1..j */
        if (i < 1 || j < 1) return;
        rect(ctx, ax(1) + 3, ay(1) + 3, j * CELL - 6, i * CELL - 6, alpha(color, 0.22 * op), alpha(color, 0.9 * op), 3);
      };
      let headline = '', eq = null, counter = '';
      if (I !== null) {
        block(I, J - 1, BLUE, ln === 7 ? 1 : k);
        block(I - 1, J, RED, ln === 7 ? 1 : k);
        rect(ctx, ax(1) - 4, ay(1) - 4, J * CELL + 8, I * CELL + 8, null, PAL.ink, 3, [10, 8]);
      }
      let Q = null;
      if (querying) {
        const I1 = v.row1 + 1, J1 = v.col1 + 1, I2 = v.row2 + 1, J2 = v.col2 + 1, t = v.term;
        Q = { I1, J1, I2, J2, t };
        if (t >= 1) block(I2, J1 - 1, BLUE, ln === 14 && g.prev.line !== 14 ? k : 1);
        if (t >= 2) block(I1 - 1, J2, RED, ln === 15 && g.prev.line !== 15 ? k : 1);
        rect(ctx, ax(1) - 4, ay(1) - 4, J2 * CELL + 8, I2 * CELL + 8, null, alpha(PAL.ink, 0.5), 2);
        rect(ctx, ax(J1) + 1, ay(I1) + 1, (J2 - J1 + 1) * CELL - 2, (I2 - I1 + 1) * CELL - 2, alpha(key, 0.12), PAL.ink, 3, [10, 8]);
      }

      /* ---------- A's cells */
      text(ctx, 'A', AX - 70, ay(1) + (M * CELL) / 2, PAL.ink, { size: 34, weight: 600, italic: true, align: 'center' });
      for (let j = 1; j <= N; j += 1) text(ctx, String(j), ax(j) + CELL / 2, AY - 22, PAL.muted, { size: 26, align: 'center' });
      for (let i = 1; i <= M; i += 1) {
        text(ctx, String(i), AX - 24, ay(i) + CELL / 2, PAL.muted, { size: 26, align: 'center' });
        for (let j = 1; j <= N; j += 1) {
          const here = I === i && J === j;
          rect(ctx, ax(j), ay(i), CELL, CELL, null, alpha(PAL.ink, 0.3), 1.5);
          if (here) rect(ctx, ax(j) + 6, ay(i) + 6, CELL - 12, CELL - 12, alpha(key, 0.2), key, 3);
          text(ctx, String(A[i - 1][j - 1]), ax(j) + CELL / 2, ay(i) + CELL / 2, here ? key : PAL.ink, { size: 34, align: 'center', weight: here ? 600 : 400 });
          hits.push({ x: ax(j) + CELL / 2, y: ay(i) + CELL / 2, r: CELL / 2, name: `A${sub(i, j)} = ${A[i - 1][j - 1]}` });
        }
      }

      /* ---------- S's cells: the padding dashed, the cells written so far filled, the rest still 0 */
      text(ctx, 'S', SX - 52, sy(0) + ((M + 1) * CELL) / 2, PAL.ink, { size: 34, weight: 600, italic: true, align: 'center' });
      for (let j = 0; j <= N; j += 1) text(ctx, String(j), sx(j) + CELL / 2, SY - 22, PAL.muted, { size: 26, align: 'center' });
      for (let i = 0; i <= M; i += 1) text(ctx, String(i), SX - 20, sy(i) + CELL / 2, PAL.muted, { size: 26, align: 'center' });
      const look = {};                                      /* the cells this step reads: S cell → colour and dash */
      if (I !== null) {
        look[sub(I, J - 1)] = [BLUE];
        look[sub(I - 1, J)] = [RED];
        look[sub(I - 1, J - 1)] = [PAL.ink, [6, 6]];
      }
      if (Q) {
        look[sub(Q.I2, Q.J2)] = [PAL.ink];
        if (Q.t >= 1) look[sub(Q.I2, Q.J1 - 1)] = [BLUE];
        if (Q.t >= 2) look[sub(Q.I1 - 1, Q.J2)] = [RED];
        if (Q.t >= 3) look[sub(Q.I1 - 1, Q.J1 - 1)] = [PAL.ink, [6, 6]];
      }
      for (let i = 0; i <= M; i += 1) {
        for (let j = 0; j <= N; j += 1) {
          const pad = i === 0 || j === 0, val = s ? s[i][j] : null;
          const done = !pad && s && (written(i, j));
          rect(ctx, sx(j), sy(i), CELL, CELL, pad ? null : done ? alpha(key, 0.14) : null, alpha(PAL.ink, pad ? 0.35 : 0.3), 1.5, pad ? [5, 6] : null);
          const L = look[sub(i, j)];
          if (L) rect(ctx, sx(j) + 5, sy(i) + 5, CELL - 10, CELL - 10, null, L[0], 4, L[1]);
          if (I === i && J === j) rect(ctx, sx(j) + 2, sy(i) + 2, CELL - 4, CELL - 4, alpha(key, 0.25 * (ln === 7 ? k : 0)), PAL.ink, 3, [10, 8]);
          if (val !== null) {
            const shown = I === i && J === j && ln === 7 ? (k < 0.5 ? 0 : val) : val;
            text(ctx, num(shown), sx(j) + CELL / 2, sy(i) + CELL / 2, pad || !done ? PAL.muted : key, { size: 32, align: 'center', weight: done ? 600 : 400 });
          }
          const what = pad ? `S${sub(i, j)} = 0, the padding` : `S${sub(i, j)}${val !== null ? ` = ${num(val)}` : ''}, the sum of rows 1–${i}, columns 1–${j}${done || !s ? '' : ' (not written yet)'}`;
          hits.push({ x: sx(j) + CELL / 2, y: sy(i) + CELL / 2, r: CELL / 2, name: what });
        }
      }

      /* ---------- headline, the relation with its numbers, the counter */
      const sv = (i, j) => (s ? s[i][j] : 0);
      if (ln <= 4) {
        headline = 'The table s starts as zeros, one row and one column larger than A: row 0 and column 0 stay 0.';
        eq = [['S_{0,j} = S_{i,0} = 0', PAL.ink]];
        counter = `cells to fill: mn = ${M}·${N} = ${M * N}`;
      } else if (I !== null) {
        const a = A[I - 1][J - 1], up = sv(I - 1, J), left = sv(I, J - 1), ov = sv(I - 1, J - 1), res = a + up + left - ov;
        if (I > 1 && J > 1) headline = `$${S_(I, J)}$ adds $${A_(I, J)} = ${a}$ to the red block $${S_(I - 1, J)}$ and the blue block $${S_(I, J - 1)}$, less their overlap $${S_(I - 1, J - 1)}$, which both count.`;
        else if (I === 1 && J === 1) headline = `$${S_(1, 1)} = ${A_(1, 1)}$: above it and to its left there is only the padding.`;
        else if (I === 1) headline = `$${S_(1, J)}$ adds $${A_(1, J)} = ${a}$ to the blue block $${S_(1, J - 1)}$; the row above is the padding.`;
        else headline = `$${S_(I, 1)}$ adds $${A_(I, 1)} = ${a}$ to the red block $${S_(I - 1, 1)}$; the column to its left is the padding.`;
        eq = [[`${S_(I, J)} = ${A_(I, J)} + `, PAL.ink], [S_(I - 1, J), RED, 600], [' + ', PAL.ink], [S_(I, J - 1), BLUE, 600], [` − ${S_(I - 1, J - 1)} = ${a} + `, PAL.ink],
          [num(up), RED, 600], [' + ', PAL.ink], [num(left), BLUE, 600], [` − ${num(ov)} = `, PAL.ink], [num(ln === 7 ? res : '?'), key, 600]];
        const filled = (I - 1) * N + J - (ln === 7 ? 0 : 1);
        counter = `lookups: 3 a cell, ${3 * filled} for the ${filled} of mn = ${M * N} cells written · summing this cell's rectangle afresh: ${I * J - 1} addition${I * J - 1 === 1 ? '' : 's'}`;
      } else if (Q) {
        const { I1, J1, I2, J2, t } = Q;
        const terms = [[S_(I2, J2), PAL.ink, sv(I2, J2), '+'], [S_(I2, J1 - 1), BLUE, sv(I2, J1 - 1), '−'], [S_(I1 - 1, J2), RED, sv(I1 - 1, J2), '−'], [S_(I1 - 1, J1 - 1), PAL.ink, sv(I1 - 1, J1 - 1), '+']];
        const upto = Math.min(3, t), shown = terms.slice(0, upto + 1);
        const rows = I1 === I2 ? `row ${I1}` : `rows ${I1}–${I2}`, cols = J1 === J2 ? `column ${J1}` : `columns ${J1}–${J2}`;
        const edge = I1 === 1 || J1 === 1;
        headline = t >= 4 ? `The sum over ${rows}, ${cols} is ${v.acc}: four cells of the table${edge ? ', two of them the padding' : ''}.`
          : [`Start from $${S_(I2, J2)}$, the block from the corner to the query's far corner.`,
            `Take away the blue block $${S_(I2, J1 - 1)}$, the columns left of the query${J1 === 1 ? ': padding, 0' : ''}.`,
            `Take away the red block $${S_(I1 - 1, J2)}$, the rows above it${I1 === 1 ? ': padding, 0' : ''}.`,
            `Add back $${S_(I1 - 1, J1 - 1)}$, the corner both blocks took away.`][t];
        eq = [['sum = ', PAL.ink]];
        shown.forEach(([nm, col, , sg], q) => { eq.push([q ? ` ${sg} ` : '', PAL.ink]); eq.push([nm, col, 600]); });
        eq.push([' = ', PAL.ink]);
        shown.forEach(([, col, val, sg], q) => { eq.push([q ? ` ${sg} ` : '', PAL.ink]); eq.push([num(val), col, 600]); });
        eq.push([` = ${num(v.acc)}`, key, 600]);
        const cells = (I2 - I1 + 1) * (J2 - J1 + 1);
        counter = `lookups: ${upto + 1} of 4 · adding the ${cells} cell${cells === 1 ? '' : 's'} one by one: ${cells - 1} addition${cells === 2 ? '' : 's'}`;
      }
      topline(ctx, headline);
      if (eq) runs(ctx, eq, 700, 600, 30);
      text(ctx, counter, 700, 652, cost, { size: 26, align: 'center' });
      text(ctx, 'filled: written · faint: still 0 · dashed: the zero padding', 700, 696, PAL.muted, { size: 26, align: 'center' });
      tip.hits = hits;
    },
  });
})();

/* ================================================================ sim-range-add: doocs 0370, a range add as two writes */
(function () {
  const LEN = 8;
  /* canonical Java line → line of the other languages */
  const MAP = {
    python: { 1: 1, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 7, 9: 7, 10: 7, 11: 8, 12: 8, 13: 8, 14: 8, 15: 8, 16: 8 },
    cpp: { 1: 1, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17 },
    javascript: { 1: 6, 2: 6, 3: 7, 4: 8, 5: 8, 6: 9, 7: 10, 8: 11, 9: 12, 10: 13, 11: 14, 12: 15, 13: 16, 14: 17, 15: 18, 16: 18 },
  };
  /* the updates, then the prefix pass, as frames of the Java; A is the array the updates so far make (not a code
     variable: what a prefix pass over d would give now, which the drawing shows above d) */
  const prefix = (d) => d.reduce((o, x, k) => (o.push((k ? o[k - 1] : 0) + x), o), []);
  const run = (updates) => F.trace((at) => {
    const d = new Array(LEN).fill(0);
    let writes = 0, direct = 0;
    at(3, { length: LEN, d, A: prefix(d), writes, direct });
    updates.forEach(([l, r, c], u) => {
      at(5, { l, r, c, d, A: prefix(d), writes, direct, u });
      d[l] += c; writes += 1; direct += r - l + 1;
      at(6, { l, r, c, d, A: prefix(d), writes, direct, u }, ['add', l, c]);
      at(7, { l, r, c, d, A: prefix(d), writes, direct, u, guard: r + 1 < LEN });
      if (r + 1 < LEN) { d[r + 1] -= c; writes += 1; at(8, { l, r, c, d, A: prefix(d), writes, direct, u }, ['add', r + 1, -c]); }
    });
    const A = prefix(d);
    at(11, { i: 1, d, A, writes, direct, pass: 0 });
    for (let i = 1; i < LEN; i += 1) { d[i] += d[i - 1]; at(12, { i, d, A, writes, direct, pass: i }, ['carry', i]); }
    at(14, { d, A, writes, direct, pass: LEN - 1, done: true });
  });
  const INPUTS = [
    { value: 'overlap', label: 'overlapping adds', updates: [[1, 4, 3], [3, 6, 2], [0, 2, -1]] },
    { value: 'end', label: 'adds that run to the end', updates: [[2, 7, 4], [0, 7, 1], [0, 5, 2]] },
  ];

  const d = sim('sim-range-add', 700);
  const code = F.code(d, {
    src: DOOCS_0370, canonical: 'java', lineMap: MAP,
    blocks: [
      { id: 'init', lines: [3, 3], label: 'an array of zeros', touches: ['d'] },
      { id: 'update', lines: [5, 9], label: 'add c at l and take it away after r', touches: ['l', 'r', 'c', 'd'] },
      { id: 'left', lines: [6, 6], label: 'add c at l', touches: ['l', 'c', 'd'] },
      { id: 'right', lines: [7, 9], label: 'take c away at r + 1, unless r is the last index', touches: ['r', 'c', 'd'] },
      { id: 'pass', lines: [11, 13], label: 'prefix sums of d', touches: ['i', 'd'] },
      { id: 'carry', lines: [12, 12], label: 'carry the running total into d[i]', touches: ['i', 'd'] },
    ],
    refs: { l: () => F.ref('l'), r: () => F.ref('r'), c: () => F.ref('c'), i: () => F.ref('i') },
  });

  const CELL = 112, X0 = (1400 - (LEN + 1) * CELL) / 2, AY = 210, DY = 390, H = 76;
  const cx = (k) => X0 + (k + 0.5) * CELL;
  const tip = { hits: [] };
  F.hover(d.stage, () => tip.hits, d.c);

  F.debug(d, {
    code, watch: ['l', 'r', 'c', 'i', 'd'],
    inputs: INPUTS.map((o) => ({ value: o.value, label: o.label, trace: run(o.updates) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const v = g.frame.vars, pv = g.prev.vars, ln = g.frame.line, k = g.k, hits = [];
      const key = C('key'), cost = C('cost'), cl = F.ref('l'), cr = F.ref('r'), cc = F.ref('c'), ci = F.ref('i');
      const dv = v.d, A = v.A, inPass = ln >= 11, upd = ln >= 5 && ln <= 8;
      const passed = inPass ? (v.done ? LEN - 1 : v.pass) : -1;   /* d[0..passed] now hold the array */

      /* ---------- a: the array the adds so far make; dashed while it is only implied by d, filled once the pass writes it */
      text(ctx, 'a', X0 - 34, AY, PAL.ink, { size: 34, weight: 600, italic: true, align: 'center' });
      for (let q = 0; q < LEN; q += 1) {
        const real = q <= passed;
        rect(ctx, X0 + q * CELL + 4, AY - H / 2, CELL - 8, H, real ? alpha(key, 0.16) : null, real ? key : alpha(PAL.ink, 0.45), real ? 3 : 2, real ? null : [8, 7]);
        const was = pv.A ? pv.A[q] : A[q], now = A[q];
        const show = was !== now && k < 0.5 ? was : now;
        text(ctx, num(show), cx(q), AY, real ? key : PAL.muted, { size: 32, align: 'center', weight: real ? 600 : 400 });
        hits.push({ x: cx(q), y: AY, r: CELL / 2, name: `a[${q}] = ${num(now)}${real ? '' : ', what a prefix pass over d gives now'}` });
      }
      /* the range the update adds c to, bracketed over a */
      if (upd) {
        const y = AY - H / 2 - 16;
        F.hbracket(ctx, X0 + v.l * CELL + 8, X0 + (v.r + 1) * CELL - 8, y, cc, `+ ${num(v.c)}`.replace('+ −', '− '), { side: 'above' });
      }

      /* ---------- d: the difference array, with the cell past the end where a guard skips the write */
      text(ctx, 'd', X0 - 34, DY, PAL.ink, { size: 34, weight: 600, italic: true, align: 'center' });
      for (let q = 0; q <= LEN; q += 1) {
        const past = q === LEN, real = q <= passed;
        rect(ctx, X0 + q * CELL + 4, DY - H / 2, CELL - 8, H, real ? alpha(key, 0.16) : null, past ? alpha(PAL.ink, 0.35) : PAL.ink, past ? 2 : 2.5, past ? [6, 6] : null);
        text(ctx, String(q), cx(q), DY + H / 2 + 26, PAL.muted, { size: 26, align: 'center' });
        if (past) { hits.push({ x: cx(q), y: DY, r: CELL / 2, name: `index ${LEN}: past the end of d, where the guard r + 1 < length skips the write` }); continue; }
        const was = pv.d ? pv.d[q] : dv[q], now = dv[q];
        text(ctx, num(was !== now && k < 0.5 ? was : now), cx(q), DY, real ? key : PAL.ink, { size: 32, align: 'center', weight: 600 });
        hits.push({ x: cx(q), y: DY, r: CELL / 2, name: `d[${q}] = ${num(now)}` });
      }
      /* the two writes of an update: + c at l, − c at r + 1 (or past the end) */
      const mark = (q, s, on) => {
        const x = cx(q), y = DY - H / 2 - 30;
        ctx.save(); ctx.globalAlpha *= on; text(ctx, s, x, y, cc, { size: 28, weight: 600, align: 'center' }); ctx.restore();
      };
      if (upd) {
        const kl = ln === 6 && g.prev.line !== 6 ? k : ln >= 6 ? 1 : 0;
        mark(v.l, `+${num(v.c)}`.replace('+−', '−'), kl);
        if (ln >= 7) {
          const kr = ln === 8 && g.prev.line !== 8 ? k : 1;
          const s = `−${num(v.c)}`.replace('−−', '+');
          if (v.r + 1 < LEN) mark(v.r + 1, s, ln === 8 ? kr : 0.35);
          else mark(LEN, 'skipped', 0.6);
        }
        F.ds.pointer(ctx, { x: cx, cell: CELL, t: DY - H / 2, b: DY + H / 2 + 10 }, [{ at: v.l, name: 'l', color: cl }, { at: v.r, name: 'r', color: cr }], { side: 'below', size: 28 });
      }
      /* the prefix pass: the running total carried from d[i − 1] into d[i] */
      if (inPass && !v.done && ln === 12) {
        const i = v.i, t = g.prev.line === 12 && pv.i === i - 1 ? k : 1;
        const x0 = cx(i - 1) + 20, x1 = cx(i) - 20, y = DY - H / 2 - 22;
        arrow(ctx, x0, y, x0 + (x1 - x0) * Math.max(0.2, t), y, ci, 4);
        F.ds.pointer(ctx, { x: cx, cell: CELL, t: DY - H / 2, b: DY + H / 2 + 10 }, [{ at: i, name: 'i', color: ci }], { side: 'below', size: 28 });
      }

      /* ---------- headline, the rule with its numbers, the counter */
      let head, rule = null;
      const range = (l, r) => (l === r ? `a[${l}]` : `a[${l}..${r}]`);
      if (ln === 3) head = 'd starts as zeros, and so does the array a its prefix sums give.';
      else if (upd) {
        const two = v.r + 1 < LEN;
        head = two ? `Add ${num(v.c)} to ${range(v.l, v.r)}: d[${v.l}] gains ${num(v.c)} and d[${v.r + 1}] loses it, two writes for ${v.r - v.l + 1} cells.`
          : `Add ${num(v.c)} to ${range(v.l, v.r)}: d[${v.l}] gains ${num(v.c)}; r + 1 = ${LEN} is past the end, so nothing loses it.`;
        rule = [['D_l ← D_l + c', PAL.ink], [two ? ',   D_{r+1} ← D_{r+1} − c' : '   (D_{r+1} is past the end)', two ? PAL.ink : PAL.muted],
          ['      ', PAL.ink], [`l = ${v.l}`, cl, 600], [',  ', PAL.ink], [`r = ${v.r}`, cr, 600], [',  ', PAL.ink], [`c = ${num(v.c)}`, cc, 600]];
      } else if (inPass && !v.done) {
        const i = v.i;
        head = ln === 11 ? 'Every add is written. The prefix pass now turns d into the array, left to right.'
          : `d[${i}] = d[${i}] + d[${i - 1}] = ${num(dv[i] - dv[i - 1])} + ${dv[i - 1] < 0 ? `(${num(dv[i - 1])})` : dv[i - 1]} = ${num(dv[i])}, which is a[${i}].`;
        if (ln === 12) rule = [['a_i = a_{i−1} + D_i', key, 600], [`      i = ${i}`, ci, 600]];
      } else head = 'd now holds the array: each add is spread back over its range.';
      topline(ctx, head);
      if (rule) runs(ctx, rule, 700, 572, 30);
      const W = v.writes, D = v.direct;
      const counter = inPass ? `writes to d: ${W}, where adding to every cell of each range takes ${D} · prefix pass: ${Math.max(0, passed)} of n − 1 = ${LEN - 1} additions`
        : `writes to d: ${W} (at most 2 an add) · adding to every cell of each range: ${D} writes`;
      text(ctx, counter, 700, 624, cost, { size: 26, align: 'center' });
      text(ctx, 'dashed a: what a prefix pass over d would give now · indices from 0, as the code', 700, 668, PAL.muted, { size: 26, align: 'center' });
      tip.hits = hits;
    },
  });
})();
};
