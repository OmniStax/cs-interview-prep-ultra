/* Figures for section 3.6 Space-efficient lists. Boots against the section's text article.
   Six Sims over ODS's RootishArrayStack and SEList.
   - sim-rootish (debugger): RootishArrayStack's blocks running add, remove and get, every list index i mapped to its
     block b and place j by i2b's square-root formula; ODS's Figure 2.5's calls on load.
   - sim-gauss (still): the staircase 1 + 2 + ⋯ + r and its turned copy filling an r × (r + 1) rectangle (Figure 2.6).
   - sim-wasted-space (still, a growth plot): the space a RootishArrayStack and an ArrayStack waste after n appends, √n.
   - sim-fastsqrt (debugger): FastSqrt.sqrt(x), the table lookup of ⌊√x⌋ and its at most two corrections.
   - sim-selist-add, sim-selist-remove (debuggers): SEList's add(i, x) with spread(u) and remove(i) with gather(u), b = 3,
     ODS's Figures 3.4 and 3.5's cases on load, and a run of calls that counts the fragile nodes.
   The code panels are ODS's code: Python (canonical, the trace's lines; RootishArrayStack's with the `//` port,
   AI-marked), Java and C++ as ODS's editions print them, written in below by ch03/3.6/inline_code.py from the source
   cache; JavaScript is the AI's translation of the Java, and FastSqrt's Python too (ODS has no Python FastSqrt), both
   AI-marked. Each trace is the figure's own JS copy of the shown Python. The SEList nodes are drawn with figlib's
   rect, line, arrow and text (F.ds has no node primitive on the served app). */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['3.6'] = function (root, F) {
const { C, PAL, alpha, text, arrow, line, topline, measure, hbracket, vbracket, begin, tex, ctl, register, hover, axes, plot, legend } = F;
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
const num = (x) => String(x).replace('-', '−');   /* a minus sign, not a hyphen */
const big = (x) => String(x).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
const seg = (ctx, parts, y, size = 28, cx = 700) => {
  /* one line of runs, each in its own colour, centred on cx */
  const ws = parts.map(([s, , o]) => measure(ctx, s, { size, weight: (o && o.weight) || 400 }));
  let x = cx - ws.reduce((s, w) => s + w, 0) / 2;
  parts.forEach(([s, c, o], j) => { text(ctx, s, x, y, c, { size, base: 'middle', weight: (o && o.weight) || 400 }); x += ws[j]; });
};

/* ================================================================ sim-rootish */
(function () {
  /* BEGIN ODS LISTINGS rootish (ch03/3.6/inline_code.py) */
  const PY = "def _i2b(self, i):\n    return int(ceil((-3.0 + sqrt(9 + 8*i)) / 2.0))\n\ndef get(self, i):\n    b = self._i2b(i)\n    j = i - b*(b+1)//2\n    return self.blocks.get(b)[j]\n\ndef set(self, i, x):\n    b = self._i2b(i)\n    j = i - b*(b+1)//2\n    y = self.blocks.get(b)[j]\n    self.blocks.get(b)[j] = x\n    return y\n\ndef add(self, i, x):\n    r = self.blocks.size()\n    if r*(r+1)//2 < self.n + 1: self.grow()\n    self.n += 1\n    for j in range(self.n-1, i, -1):\n        self.set(j, self.get(j-1))\n    self.set(i, x)\n\ndef grow(self):\n    self.blocks.append(new_array(self.blocks.size()+1))\n\ndef remove(self, i):\n    x = self.get(i)\n    for j in range(i, self.n-1):\n        self.set(j, self.get(j+1))\n    self.n -= 1\n    r = self.blocks.size()\n    if (r-2)*(r-1)//2 >= self.n: self.shrink()\n    return x\n\ndef shrink(self):\n    r = self.blocks.size()\n    while r > 0 and (r-2)*(r-1)//2 >= self.n:\n        self.blocks.remove(self.blocks.size()-1)\n        r -= 1";
  const JAVA = "int i2b(int i) {\n    double db = (-3.0 + Math.sqrt(9 + 8*i)) / 2.0;\n    int b = (int)Math.ceil(db);\n    return b;\n}\n\nT get(int i) {\n    int b = i2b(i);\n    int j = i - b*(b+1)/2;\n    return blocks.get(b)[j];\n}\n\nT set(int i, T x) {\n    int b = i2b(i);\n    int j = i - b*(b+1)/2;\n    T y = blocks.get(b)[j];\n    blocks.get(b)[j] = x;\n    return y;\n}\n\nvoid add(int i, T x) {\n    int r = blocks.size();\n    if (r*(r+1)/2 < n + 1) grow();\n    n++;\n    for (int j = n-1; j > i; j--)\n        set(j, get(j-1));\n    set(i, x);\n}\n\nvoid grow() {\n    blocks.add(newArray(blocks.size()+1));\n}\n\nT remove(int i) {\n    T x = get(i);\n    for (int j = i; j < n-1; j++)\n        set(j, get(j+1));\n    n--;\n    int r = blocks.size();\n    if ((r-2)*(r-1)/2 >= n)    shrink();\n    return x;\n}\n\nvoid shrink() {\n    int r = blocks.size();\n    while (r > 0 && (r-2)*(r-1)/2 >= n) {\n        blocks.remove(blocks.size()-1);\n        r--;\n    }\n}";
  const CPP = "int i2b(int i) {\n    double db = (-3.0 + sqrt(9 + 8*i)) / 2.0;\n    int b = (int)ceil(db);\n    return b;\n}\n\nT get(int i) {\n    int b = i2b(i);\n    int j = i - b*(b+1)/2;\n    return blocks.get(b)[j];\n}\n\nT set(int i, T x) {\n    int b = i2b(i);\n    int j = i - b*(b+1)/2;\n    T y = blocks.get(b)[j];\n    blocks.get(b)[j] = x;\n    return y;\n}\n\nvoid add(int i, T x) {\n    int r = blocks.size();\n    if (r*(r+1)/2 < n + 1) grow();\n    n++;\n    for (int j = n-1; j > i; j--)\n        set(j, get(j-1));\n    set(i, x);\n}\n\nvoid grow() {\n    blocks.add(blocks.size(), new T[blocks.size()+1]);\n}\n\nT remove(int i) {\n    T x = get(i);\n    for (int j = i; j < n-1; j++)\n        set(j, get(j+1));\n    n--;\n    int r = blocks.size();\n    if ((r-2)*(r-1)/2 >= n) shrink();\n    return x;\n}\n\nvoid shrink() {\n    int r = blocks.size();\n    while (r > 0 && (r-2)*(r-1)/2 >= n) {\n            delete [] blocks.remove(blocks.size()-1);\n            r--;\n    }\n}";
  /* END ODS LISTINGS rootish */
  const JS = [
    'i2b(i) {',
    '    const db = (-3.0 + Math.sqrt(9 + 8*i)) / 2.0;',
    '    const b = Math.ceil(db);',
    '    return b;',
    '}',
    '',
    'get(i) {',
    '    const b = this.i2b(i);',
    '    const j = i - b*(b+1)/2;',
    '    return this.blocks.get(b)[j];',
    '}',
    '',
    'set(i, x) {',
    '    const b = this.i2b(i);',
    '    const j = i - b*(b+1)/2;',
    '    const y = this.blocks.get(b)[j];',
    '    this.blocks.get(b)[j] = x;',
    '    return y;',
    '}',
    '',
    'add(i, x) {',
    '    const r = this.blocks.size();',
    '    if (r*(r+1)/2 < this.n + 1) this.grow();',
    '    this.n++;',
    '    for (let j = this.n-1; j > i; j--)',
    '        this.set(j, this.get(j-1));',
    '    this.set(i, x);',
    '}',
    '',
    'grow() {',
    '    this.blocks.add(new Array(this.blocks.size()+1));',
    '}',
    '',
    'remove(i) {',
    '    const x = this.get(i);',
    '    for (let j = i; j < this.n-1; j++)',
    '        this.set(j, this.get(j+1));',
    '    this.n--;',
    '    const r = this.blocks.size();',
    '    if ((r-2)*(r-1)/2 >= this.n) this.shrink();',
    '    return x;',
    '}',
    '',
    'shrink() {',
    '    let r = this.blocks.size();',
    '    while (r > 0 && (r-2)*(r-1)/2 >= this.n) {',
    '        this.blocks.remove(this.blocks.size()-1);',
    '        r--;',
    '    }',
    '}',
  ].join('\n');
  /* Python line → the braced languages' lines: i2b's one line is Java's three, every for loop is two lines */
  const MAP = {
    1: 1, 2: [2, 3, 4], 4: 7, 5: 8, 6: 9, 7: 10, 9: 13, 10: 14, 11: 15, 12: 16, 13: 17, 14: 18,
    16: 21, 17: 22, 18: 23, 19: 24, 20: 25, 21: 26, 22: 27, 24: 30, 25: 31,
    27: 34, 28: 35, 29: 36, 30: 37, 31: 38, 32: 39, 33: 40, 34: 41, 36: 44, 37: 45, 38: 46, 39: 47, 40: 48,
  };
  const L = { start: 3, i2b: 2, defGet: 4, getB: 5, getJ: 6, getR: 7, defAdd: 16, addR: 17, addGrow: 18, addN: 19, addFor: 20,
    addShift: 21, addStore: 22, defGrow: 24, grow: 25, defRem: 27, remTake: 28, remFor: 29, remShift: 30, remN: 31,
    remR: 32, remShrink: 33, remRet: 34, defShrink: 36, shrR: 37, shrDrop: 39, shrDec: 40 };

  const i2b = (i) => Math.ceil((-3.0 + Math.sqrt(9 + 8 * i)) / 2.0);
  const LET = 'abcdefghijklmnopqrstuvwxyz'.split('');
  const FIG = [['a'], ['b', 'c'], ['d', 'e', 'f'], ['g', 'h', null, null], [null, null, null, null, null]];
  const PRESETS = [
    { value: 'figure', label: 'Figure 2.5', blocks: FIG, n: 8, ops: [['add', 2, 'x'], ['remove', 1], ['remove', 7], ['remove', 6]] },
    { value: 'get', label: 'get every index', blocks: FIG, n: 8, ops: Array.from({ length: 8 }, (_, k) => ['get', k]) },
    { value: 'append', label: 'append', blocks: [], n: 0, ops: LET.slice(0, 11).map((x, k) => ['add', k, x]) },
    { value: 'shrink', label: 'grow then shrink', blocks: [], n: 0,
      ops: [...LET.slice(0, 11).map((x, k) => ['add', k, x]), ...LET.slice(0, 11).map((_, k) => ['remove', 10 - k])] },
    { value: 'front', label: 'add at the front', blocks: [], n: 0, ops: LET.slice(0, 8).map((x) => ['add', 0, x]) },
  ];
  const callName = (o) => (o[0] === 'add' ? `add(${o[1]}, ${o[2]})` : `${o[0]}(${o[1]})`);
  const bj = (i) => { const b = i2b(i); return [b, i - b * (b + 1) / 2]; };

  /* One run as frames of the Python. Beside the code's variables (i, x, b, n, r) each frame carries what the
     drawing reads: the blocks, the call under way (k), the copy just made (mv: [from, to] as list indices), the
     copies this call made (moves), the cell a get or set reaches (at: [b, j]), and running counts. */
  const run = (P) => F.trace((at) => {
    const blocks = P.blocks.map((bl) => bl.slice());
    let n = P.n, k = -1, moves = [], shifted = 0, grows = 0, shrinks = 0;
    let i = null, x = null, b = null;
    const flat = () => { const out = []; blocks.forEach((bl) => bl.forEach((v) => out.push(v))); return out; };
    const snap = (extra) => Object.assign({ i, x, b, n, r: blocks.length, blocks: blocks.map((bl) => bl.slice()), k,
      moves: moves.slice(), shifted, grows, shrinks }, extra || {});
    const put = (idx, v) => { const [bb, jj] = bj(idx); blocks[bb][jj] = v; };
    const get = (idx) => { const [bb, jj] = bj(idx); return blocks[bb][jj]; };
    at(L.start, snap());
    P.ops.forEach((o, kk) => {
      k = kk; moves = []; shifted = 0;
      if (o[0] === 'get') {
        i = o[1]; x = null; b = null;
        at(L.defGet, snap());
        at.enter('i2b'); at(L.i2b, snap({ db: (-3 + Math.sqrt(9 + 8 * i)) / 2 })); at.leave();
        b = i2b(i); at(L.getB, snap({ at: [b, null] }));
        const j = i - b * (b + 1) / 2;
        at(L.getJ, snap({ at: [b, j], j }));
        x = blocks[b][j]; at(L.getR, snap({ at: [b, j], j }));
        return;
      }
      if (o[0] === 'add') {
        i = o[1]; x = o[2]; b = null;
        at(L.defAdd, snap());
        const r = blocks.length;
        at(L.addR, snap());
        if (r * (r + 1) / 2 < n + 1) {
          at.enter('grow'); at(L.defGrow, snap()); blocks.push(new Array(blocks.length + 1).fill(null)); grows += 1;
          at(L.grow, snap({ grew: true })); at.leave();
        }
        at(L.addGrow, snap());
        n += 1; at(L.addN, snap());
        for (let j = n - 1; j > i; j -= 1) {
          at(L.addFor, snap());
          put(j, get(j - 1)); shifted += 1; moves.push([j - 1, j]); b = i2b(j);
          at(L.addShift, snap({ mv: [j - 1, j], at: bj(j) }), ['copy', j - 1, j]);
        }
        put(i, x); b = i2b(i);
        at(L.addStore, snap({ at: bj(i) }), ['put', i]);
      } else {
        i = o[1]; b = i2b(i);
        at(L.defRem, snap());
        x = get(i); at(L.remTake, snap({ at: bj(i), taken: x }));
        for (let j = i; j < n - 1; j += 1) {
          at(L.remFor, snap());
          put(j, get(j + 1)); shifted += 1; moves.push([j + 1, j]); b = i2b(j);
          at(L.remShift, snap({ mv: [j + 1, j], at: bj(j) }), ['copy', j + 1, j]);
        }
        n -= 1; put(n, null); at(L.remN, snap());
        let r = blocks.length; at(L.remR, snap());
        if ((r - 2) * (r - 1) / 2 >= n) {
          at.enter('shrink'); at(L.defShrink, snap()); at(L.shrR, snap());
          while (r > 0 && (r - 2) * (r - 1) / 2 >= n) {
            blocks.pop(); shrinks += 1; at(L.shrDrop, snap({ dropped: r - 1 }));
            r -= 1; at(L.shrDec, snap());
          }
          at.leave();
        }
        at(L.remShrink, snap());
        at(L.remRet, snap());
      }
    });
    void flat;
  });

  const d = sim('sim-rootish', 760);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: { python: AI, javascript: AI },
    lineMap: { java: MAP, cpp: MAP, javascript: MAP },
    blocks: [
      { id: 'get', lines: [4, 7], label: 'get(i): find the block and the place in it', touches: ['i', 'b'] },
      { id: 'gb', lines: [5, 5], label: 'b = i2b(i), the smallest b with (b + 1)(b + 2)/2 ≥ i + 1', touches: ['i', 'b'] },
      { id: 'gj', lines: [6, 6], label: 'j = i − b(b + 1)/2, the place in block b', touches: ['b'] },
      { id: 'gr', lines: [7, 7], label: 'read the element there', touches: ['b'] },
      { id: 'add', lines: [16, 22], label: 'add(i, x)', touches: ['i', 'x', 'n', 'r', 'blocks'] },
      { id: 'room', lines: [17, 18], label: 'grow() if all r(r + 1)/2 cells are in use', touches: ['r', 'blocks'] },
      { id: 'shift', lines: [20, 21], label: 'copy one element a place to the right', touches: ['blocks'] },
      { id: 'store', lines: [22, 22], label: 'set(i, x)', touches: ['i', 'x', 'blocks'] },
      { id: 'grow', lines: [24, 25], label: 'grow(): a new block of r + 1 cells', touches: ['r', 'blocks'] },
      { id: 'remove', lines: [27, 34], label: 'remove(i)', touches: ['i', 'x', 'n', 'r', 'blocks'] },
      { id: 'take', lines: [28, 28], label: 'x = get(i)', touches: ['i', 'x'] },
      { id: 'shiftl', lines: [29, 30], label: 'copy one element a place to the left', touches: ['blocks'] },
      { id: 'shrinkq', lines: [31, 33], label: 'count it, and shrink() if two blocks or more are empty', touches: ['n', 'r', 'blocks'] },
      { id: 'shrink', lines: [36, 40], label: 'shrink(): free the empty blocks but one', touches: ['r', 'blocks'] },
      { id: 'drop', lines: [39, 40], label: 'free the last block', touches: ['r', 'blocks'] },
    ],
    refs: { i: () => F.ref('i'), b: () => F.ref('b'), 'self.n': () => F.ref('n'), n: () => F.ref('n'), r: () => F.ref('r') },
  });
  const traces = Object.fromEntries(PRESETS.map((P) => [P.value, run(P)]));
  const byValue = Object.fromEntries(PRESETS.map((P) => [P.value, P]));
  const tip = { hits: [] };

  F.debug(d, {
    code, watch: ['i', 'x', 'b', 'n', 'r'],
    inputs: PRESETS.map((P) => ({ value: P.value, label: P.label, trace: traces[P.value] })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const P = byValue[g.input] || PRESETS[0];
      const v = g.frame.vars, pv = g.prev.vars, k = g.k, ln = g.frame.line;
      const ci = F.ref('i'), cb = F.ref('b'), cn = F.ref('n'), cr = F.ref('r');
      const key = C('key'), size = C('size'), cost = C('cost'), idx = C('index'), ink = PAL.ink, muted = PAL.muted;
      const hits = [];
      const op = v.k >= 0 ? P.ops[v.k] : null;
      const r = v.r, cells = r * (r + 1) / 2;

      /* ---------------- the headline */
      let head;
      if (!op) head = r ? `${r} block${r === 1 ? '' : 's'} hold ${cells} cells, and n = ${v.n} of them are in use.` : 'An empty RootishArrayStack: no blocks yet.';
      else if (op[0] === 'get') {
        head = ln === L.getR || ln === L.getJ ? `get(${op[1]}): index ${op[1]} is block ${v.b}, place ${v.j}, and holds ${v.blocks[v.b][v.j]}.`
          : `get(${op[1]}) first finds the block: b = i2b(${op[1]}) = ${i2b(op[1])}.`;
      } else if (ln === L.defGrow || ln === L.grow) head = `All ${r * (r - 1) / 2} cells are in use, so ${callName(op)} first calls grow(): a block of ${r} cells.`;
      else if (ln === L.shrDrop || ln === L.shrDec || ln === L.defShrink || ln === L.shrR) head = `${callName(op)} leaves two blocks or more empty, so shrink() frees the last blocks but one.`;
      else if (op[0] === 'add') {
        head = v.shifted ? `${callName(op)} shifts ${v.shifted} element${v.shifted === 1 ? '' : 's'} one place right${ln === L.addStore ? ` and stores ${op[2]} in block ${i2b(op[1])}, place ${bj(op[1])[1]}` : ''}.`
          : ln === L.addStore ? `${callName(op)} stores ${op[2]} in block ${i2b(op[1])}, place ${bj(op[1])[1]}; nothing needs to move.` : `${callName(op)}.`;
      } else {
        head = ln >= L.remN ? `${callName(op)} took ${v.x} out and shifted ${v.shifted} element${v.shifted === 1 ? '' : 's'} one place left.`
          : `${callName(op)} takes ${v.x} out${v.shifted ? ` and shifts ${v.shifted} element${v.shifted === 1 ? '' : 's'} one place left` : ''}.`;
      }
      topline(ctx, head);

      /* ---------------- the calls: done in ink, the current one boxed, the rest muted */
      const CS = 24, gap = 18;
      const labels = P.ops.map((o) => callName(o).replace(/, /g, ','));
      const widths = labels.map((s) => measure(ctx, s, { size: CS }));
      const rows = [[]]; let wsum = 0;
      labels.forEach((s, j) => { if (wsum + widths[j] > 1280 && rows[rows.length - 1].length) { rows.push([]); wsum = 0; } rows[rows.length - 1].push(j); wsum += widths[j] + gap; });
      rows.forEach((row, ri) => {
        const tot = row.reduce((s, j) => s + widths[j] + gap, -gap);
        let x = 700 - tot / 2; const y = 108 + ri * 38;
        row.forEach((j) => {
          const cur = j === v.k, done = j < v.k;
          if (cur) rect(ctx, x - 7, y - 18, widths[j] + 14, 36, alpha(ink, 0.06), ink, 2);
          text(ctx, labels[j], x, y, cur || done ? ink : muted, { size: CS, base: 'middle', weight: cur ? 600 : 400 });
          x += widths[j] + gap;
        });
      });
      const top = 108 + rows.length * 38;

      /* ---------------- the blocks: list order left to right, a gap between blocks; above them the blocks list */
      const showR = Math.max(r, 1);
      const totalCells = Math.max(showR * (showR + 1) / 2, 1), GAP = 30;
      const cw = Math.min(70, (1240 - GAP * (showR - 1)) / totalCells), CH = Math.min(62, cw * 0.95);
      const W = totalCells * cw + GAP * (showR - 1), X0 = 700 - W / 2;
      const ROW = top + 250, REFY = top + 60;
      const cellX = (bb, jj) => X0 + (bb * (bb + 1) / 2 + jj) * cw + bb * GAP;
      const ix = (t) => { const [bb, jj] = bj(t); return cellX(bb, jj) + cw / 2; };
      const curAt = v.at || null, curB = curAt ? curAt[0] : (op && op[0] !== 'get' && v.b !== null ? v.b : null);
      /* the blocks list: one reference per block, as ODS draws it (these r references are space too) */
      const rw = Math.min(54, 520 / Math.max(r, 1));
      const RX0 = X0;
      text(ctx, 'blocks', RX0, REFY - 44, ink, { size: 24, weight: 600, base: 'middle' });
      for (let bb = 0; bb < r; bb += 1) {
        const x = RX0 + bb * rw;
        rect(ctx, x, REFY - 22, rw, 44, PAL.panel, ink, 2);
        F.dot(ctx, x + rw / 2, REFY, ink, true, 6);
        const tx = cellX(bb, 0) + 10, ty = ROW - CH / 2 - 6;
        const fresh = v.grew && bb === r - 1 && !pv.grew;
        ctx.save(); ctx.globalAlpha *= fresh ? k : 1;
        ctx.strokeStyle = alpha(ink, 0.55); ctx.lineWidth = 2.5; ctx.beginPath();
        ctx.moveTo(x + rw / 2, REFY); ctx.bezierCurveTo(x + rw / 2, REFY + 80, tx, ty - 90, tx, ty - 12); ctx.stroke();
        arrow(ctx, tx, ty - 14, tx, ty, alpha(ink, 0.55), 3);
        ctx.restore();
      }
      hits.push({ x: RX0 + (r * rw) / 2, y: REFY, r: Math.max(30, (r * rw) / 2), name: `blocks: ${r} reference${r === 1 ? '' : 's'}, one per block` });
      /* the cells */
      let listIdx = 0;
      for (let bb = 0; bb < r; bb += 1) {
        const size_ = bb + 1;
        const isB = curB === bb;
        if (isB) rect(ctx, cellX(bb, 0) - 6, ROW - CH / 2 - 6, size_ * cw + 12, CH + 12, null, cb, 4);
        for (let jj = 0; jj < size_; jj += 1) {
          const used = listIdx < v.n, val = v.blocks[bb] ? v.blocks[bb][jj] : null;
          const x = cellX(bb, jj);
          if (used) rect(ctx, x, ROW - CH / 2, cw, CH, alpha(idx, 0.16), null);
          rect(ctx, x + 1, ROW - CH / 2, cw - 2, CH, null, used ? ink : alpha(ink, 0.4), used ? 2.5 : 2);
          if (curAt && curAt[0] === bb && curAt[1] === jj) rect(ctx, x + 4, ROW - CH / 2 + 4, cw - 8, CH - 8, null, cb, 3);
          if (used && val !== null && val !== undefined) text(ctx, String(val), x + cw / 2, ROW, key, { size: cw < 50 ? 26 : 32, align: 'center', base: 'middle', weight: 600 });
          text(ctx, String(listIdx), x + cw / 2, ROW + CH / 2 + 22, idx, { size: cw < 50 ? 20 : 24, align: 'center', base: 'middle' });
          hits.push({ x: x + cw / 2, y: ROW, r: cw / 2, name: used ? `index ${listIdx}: block ${bb}, place ${jj}, holds ${val}` : `block ${bb}, place ${jj}: not in use` });
          listIdx += 1;
        }
        text(ctx, `${bb}`, cellX(bb, 0) + (size_ * cw) / 2, ROW - CH / 2 - 62, isB ? cb : muted, { size: 22, align: 'center', base: 'middle', weight: isB ? 600 : 400 });
      }
      if (r) text(ctx, 'block', X0 - 12, ROW - CH / 2 - 62, muted, { size: 22, align: 'right', base: 'middle' });
      /* the copies this call made: an arc from each element's old index to its new one, the last drawn as it moves */
      (v.moves || []).forEach((mv) => {
        const cur = v.mv && v.mv[0] === mv[0] && v.mv[1] === mv[1];
        const fresh = cur && !(pv.mv && pv.mv[0] === mv[0] && pv.mv[1] === mv[1]);
        const x0 = ix(mv[0]), x1 = ix(mv[1]), y = ROW - CH / 2 - 4;
        const t = fresh ? Math.max(0.25, k) : 1;
        curve(ctx, x0, y, lerp(x0, x1, t), y, 30, cur ? ci : alpha(ci, 0.4), cur ? 4 : 3);
      });
      /* i under its index; the n cells in use bracketed */
      const iShow = op && op[0] !== 'get' && v.mv ? v.mv[1] : v.i;
      if (op && iShow !== null && iShow !== undefined && iShow < cells) {
        const xi = ix(iShow), yb = ROW + CH / 2 + 46;
        arrow(ctx, xi, yb + 44, xi, yb, ci, 4);
        const lab = v.mv ? `index ${iShow}` : `i = ${v.i}`;
        text(ctx, lab, xi, yb + 66, ci, { size: 26, weight: 600, align: 'center', base: 'middle' });
      }

      /* ---------------- the formula for the index this step reaches, then the counts */
      const Y0 = ROW + 205;
      const fi = iShow !== null && iShow !== undefined && op ? iShow : null;
      if (fi !== null && fi < cells) {
        const fb = i2b(fi), fj = fi - fb * (fb + 1) / 2, raw = (-3 + Math.sqrt(9 + 8 * fi)) / 2;
        seg(ctx, [[`${fi === v.i ? 'i' : 'index'} = ${fi}:  `, fi === v.i ? ci : idx, { weight: 600 }], ['b', cb, { weight: 600 }],
          [` = ⌈(−3 + √(9 + 8·${fi}))/2⌉ = ⌈${raw.toFixed(2)}⌉ = ${fb},   j = ${fi} − ${fb}·${fb + 1}/2 = ${fj}`, ink]], Y0);
      } else seg(ctx, [['i2b(i) = ⌈(−3 + √(9 + 8i))/2⌉ finds the block of index i', muted]], Y0);
      seg(ctx, [['cells in use ', ink], ['n', cn, { weight: 600 }], [` = ${v.n} of r(r + 1)/2 = ${cells}, `, ink], ['r', cr, { weight: 600 }],
        [` = ${r}:  `, ink], [`wasted ${cells - v.n} ≤ 2r − 1 = ${Math.max(0, 2 * r - 1)}`, cost]], Y0 + 46);
      if (op && op[0] !== 'get') {
        const bound = op[0] === 'add' ? `n − i = ${v.n - (ln >= L.addN ? 1 : 0) - op[1]}` : `n − i − 1 = ${(ln >= L.remN ? v.n + 1 : v.n) - op[1] - 1}`;
        seg(ctx, [[`elements shifted by this call: ${v.shifted} ≤ ${bound}  ·  grow ${v.grows}, shrink ${v.shrinks} so far`, cost]], Y0 + 92);
      }
      tip.hits = hits;
    },
  });
  F.hover(d.stage, () => tip.hits, d.c);
})();

/* ================================================================ sim-gauss */
(function () {
  const d = sim('sim-gauss', 560);
  const sr = ctl(d.controls, { label: 'r', cls: 'size', key: 'r', min: 1, max: 12, step: 1, value: 5, unit: '', dec: 0 });
  const hits = [];
  hover(d.stage, () => hits);
  function draw() {
    const { ctx } = begin(d.c); if (!ctx) return;
    const r = sr.v, size = C('size'), ink = PAL.ink;
    const tri = r * (r + 1) / 2;
    topline(ctx, `1 + 2 + ⋯ + ${r} = ${tri}, and the copy turned half a turn makes a ${r} × ${r + 1} rectangle.`);
    const cs = Math.min(64, 380 / r, 900 / (r + 1));
    const W = (r + 1) * cs, Hh = r * cs, x0 = 700 - W / 2, y0 = 300 - Hh / 2 + 10;
    hits.length = 0;
    for (let row = 1; row <= r; row += 1) {
      const y = y0 + (row - 1) * cs;
      for (let c = 0; c <= r; c += 1) {
        const white = c < row, x = x0 + c * cs;
        rect(ctx, x, y, cs, cs, white ? alpha(size, 0.18) : PAL.soft, null);
        rect(ctx, x + 1, y + 1, cs - 2, cs - 2, null, white ? ink : alpha(ink, 0.45), white ? 2.5 : 2);
      }
      hits.push({ x: x0 + (row * cs) / 2, y: y + cs / 2, r: Math.max(cs / 2, (row * cs) / 2), name: `row ${row}: ${row} cell${row === 1 ? '' : 's'}, as block ${row - 1} holds ${row} element${row === 1 ? '' : 's'}` });
    }
    vbracket(ctx, x0 - 22, y0, y0 + Hh, size, `r = ${r}`, -1);
    hbracket(ctx, x0, x0 + W, y0 + Hh + 24, size, `r + 1 = ${r + 1}`, { side: 'below' });
    legend(ctx, { l: x0 + W + 30, r: 1380, t: y0, b: y0 + 120 }, [
      { s: '1 + 2 + ⋯ + r', kind: 'swatch', color: alpha(size, 0.35) },
      { s: 'the same, turned', kind: 'swatch', color: PAL.soft },
    ], { corner: 'tl' });
    tex(d.readout, `1 + 2 + \\cdots + ${r} = \\frac{${r}(${r}+1)}{2} = ${tri}`);
  }
  register(d.fig, { update: () => {}, draw });
})();

/* ================================================================ sim-wasted-space */
(function () {
  const d = sim('sim-wasted-space', 600);
  const sn = ctl(d.controls, { label: 'n', cls: 'size', key: 'n', min: 1, max: 200, step: 1, value: 50, unit: '', dec: 0 });
  /* after n appends from empty: a RootishArrayStack has the fewest blocks r with r(r + 1)/2 ≥ n, and wastes its
     unused cells and its r block references; an ArrayStack (resize to 2n when full, from length 1) has length the
     least power of 2 ≥ n and wastes the unused cells */
  const rOf = (n) => Math.ceil((-1 + Math.sqrt(1 + 8 * n)) / 2);
  const rootish = (n) => { const r = rOf(n); return r * (r + 1) / 2 - n + r; };
  const capOf = (n) => { let c = 1; while (c < n) c *= 2; return c; };
  const astack = (n) => capOf(n) - n;
  const hits = [];
  hover(d.stage, () => hits);
  function draw() {
    const { ctx } = begin(d.c); if (!ctx) return;
    const n = Math.round(sn.v), cost = C('cost'), size = C('size'), ink = PAL.ink;
    const rw = rootish(n), aw = astack(n), r = rOf(n), cap = capOf(n);
    topline(ctx, `After ${n} appends a RootishArrayStack wastes ${rw} words and an ArrayStack ${aw}; √${n} ≈ ${Math.sqrt(n).toFixed(1)}.`);
    /* fixed frame: n from 0 to 200, waste from 0 to 130 (an ArrayStack wastes 127 just after its 129th append) */
    const box = { l: 140, r: 1340, t: 110, b: 500 };
    const ax = axes(ctx, box, [0, 200], [0, 130], { nx: 4, ny: 0, xl: 'n, elements appended', yl: 'wasted words', xc: size, yc: cost, nice: false });
    [0, 25, 50, 75, 100, 125].forEach((t) => { text(ctx, String(t), box.l - 12, ax.Y(t), PAL.muted, { size: 18, align: 'right', base: 'middle' }); line(ctx, box.l, ax.Y(t), box.r, ax.Y(t), alpha(ink, 0.08), 1); });
    const step = (f) => { const pts = []; for (let m = 1; m <= 200; m += 1) pts.push([m, f(m)]); return pts; };
    const poly = (pts, color, w, dash) => {
      ctx.save(); ctx.strokeStyle = color; ctx.lineWidth = w; if (dash) ctx.setLineDash(dash); ctx.beginPath();
      pts.forEach(([x, y], j) => (j ? ctx.lineTo(ax.X(x), ax.Y(y)) : ctx.moveTo(ax.X(x), ax.Y(y)))); ctx.stroke(); ctx.restore();
    };
    poly(step(astack), alpha(ink, 0.55), 3);
    poly(step(rootish), cost, 4);
    plot(ctx, ax, (x) => Math.sqrt(x), ink, { w: 3, dash: [10, 10], x: [0, 200] });
    line(ctx, ax.X(n), box.t, ax.X(n), box.b, alpha(ink, 0.35), 2, [4, 8]);
    F.dot(ctx, ax.X(n), ax.Y(aw), alpha(ink, 0.7), true, 9);
    F.dot(ctx, ax.X(n), ax.Y(rw), cost, true, 9);
    F.dot(ctx, ax.X(n), ax.Y(Math.sqrt(n)), ink, false, 8);
    legend(ctx, ax, [
      { s: 'RootishArrayStack', color: cost, w: 4 },
      { s: 'ArrayStack', color: alpha(ink, 0.55), w: 3 },
      { s: '√n', color: ink, w: 3, dash: [10, 10] },
    ], { corner: 'tl' });
    hits.length = 0;
    hits.push({ x: ax.X(n), y: ax.Y(rw), r: 14, name: `RootishArrayStack at n = ${n}: ${r} blocks, ${r * (r + 1) / 2 - n} unused cells and ${r} block references` });
    hits.push({ x: ax.X(n), y: ax.Y(aw), r: 14, name: `ArrayStack at n = ${n}: length ${cap}, ${aw} unused cells` });
    tex(d.readout, `\\text{RootishArrayStack: } \\tfrac{r(r+1)}{2} - n + r = ${r * (r + 1) / 2} - ${n} + ${r} = ${rw} \\le 3r - 1 = ${3 * r - 1}`
      + ` \\\\ \\text{ArrayStack: } \\mathrm{length}(a) - n = ${cap} - ${n} = ${aw} \\\\ \\sqrt{n} = ${Math.sqrt(n).toFixed(2)}`);
  }
  register(d.fig, { update: () => {}, draw });
})();

/* ================================================================ sim-fastsqrt */
(function () {
  /* BEGIN ODS LISTINGS fastsqrt (ch03/3.6/inline_code.py) */
  const JAVA = "int sqrt(int x) {\n    int rp = log(x);\n    int upgrade = ((r-rp)/2) * 2;\n    int xp = x << upgrade;  // xp has r or r-1 bits\n    int s = sqrtab[xp>>(r/2)] >> (upgrade/2);\n    while ((s+1)*(s+1) <= x) s++;  // executes at most twice\n    return s;\n}";
  const CPP = "int sqrt(int x) {\n    int rp = log(x);\n    int upgrade = ((r-rp)/2) * 2;\n    int xp = x << upgrade;  // xp has r or r-1 bits\n    int s = sqrtab[xp>>(r/2)] >> (upgrade/2);\n    while ((s+1)*(s+1) <= x) s++;  // executes at most twice\n    return s;\n}";
  /* END ODS LISTINGS fastsqrt */
  /* Python and JavaScript: the AI's translations of ODS's Java (ODS's Python edition has no FastSqrt) */
  const PY = [
    'def sqrt(x):',
    '    rp = log(x)',
    '    upgrade = ((r-rp)//2) * 2',
    '    xp = x << upgrade  # xp has r or r-1 bits',
    '    s = sqrtab[xp>>(r//2)] >> (upgrade//2)',
    '    while (s+1)*(s+1) <= x: s += 1  # executes at most twice',
    '    return s',
  ].join('\n');
  const JS = [
    'sqrt(x) {',
    '    const rp = log(x);',
    '    const upgrade = ((r-rp)>>1) * 2;',
    '    const xp = x << upgrade;  // xp has r or r-1 bits',
    '    let s = sqrtab[xp>>(r>>1)] >> (upgrade/2);',
    '    while ((s+1)*(s+1) <= x) s++;  // executes at most twice',
    '    return s;',
    '}',
  ].join('\n');
  /* ODS's working tables (FastSqrt.java's static block): logtab and sqrtab of 2^16 entries, r = 29 */
  const HALF = 1 << 16, R = 29;
  const logtab = new Int32Array(HALF), sqrtab = new Int32Array(HALF);
  for (let dd = 0; dd < 16; dd += 1) logtab.fill(dd, 1 << dd, 2 << dd);
  { let s = 1 << 7; for (let i = 0; i < HALF; i += 1) { if ((s + 1) * (s + 1) <= i * 16384) s += 1; sqrtab[i] = s; } }
  const log2 = (x) => (x >= HALF ? 16 + logtab[x >>> 16] : logtab[x]);
  const INPUTS = [
    { value: 'square', label: '1,000,000', x: 1000000 },
    { value: 'past', label: '66,049 = 257²', x: 66049 },
    { value: 'big', label: '123,456,789', x: 123456789 },
    { value: 'small', label: '10', x: 10 },
  ];
  const run = (x) => F.trace((at) => {
    let rp = null, upgrade = null, xp = null, s = null, idx = null, entry = null, inc = 0;
    const snap = (e) => Object.assign({ x, rp, upgrade, xp, s, idx, entry, inc }, e || {});
    at(1, snap());
    rp = log2(x); at(2, snap());
    upgrade = Math.floor((R - rp) / 2) * 2; at(3, snap());
    xp = x * 2 ** upgrade; at(4, snap());
    idx = Math.floor(xp / 2 ** Math.floor(R / 2)); entry = sqrtab[idx]; s = entry >> (upgrade / 2); at(5, snap());
    if (!((s + 1) * (s + 1) <= x)) at(6, snap({ tested: true }));
    while ((s + 1) * (s + 1) <= x) { s += 1; inc += 1; at(6, snap(), ['inc', s]); }
    at(7, snap());
  });
  const d = sim('sim-fastsqrt', 640);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: { python: AI, javascript: AI },
    lineMap: Object.fromEntries(['java', 'cpp', 'javascript'].map((l) => [l, { 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7 }])),
    blocks: [
      { id: 'log', lines: [2, 2], label: 'r′ = log(x): the place of the top bit', touches: ['x', 'rp'] },
      { id: 'up', lines: [3, 4], label: 'shift x up an even number of places, to r or r + 1 bits', touches: ['x', 'xp'] },
      { id: 'look', lines: [5, 5], label: 'read sqrtab at the top bits, and halve the shift', touches: ['xp', 's'] },
      { id: 'fix', lines: [6, 6], label: 'add 1 while (s + 1)² ≤ x', touches: ['s'] },
      { id: 'ret', lines: [7, 7], label: 'return s', touches: ['s'] },
    ],
    refs: { x: () => F.ref('x'), s: () => F.ref('s') },
  });
  const byValue = Object.fromEntries(INPUTS.map((I) => [I.value, I]));
  const tip = { hits: [] };
  F.debug(d, {
    code, watch: ['x', 'rp', 'upgrade', 'xp', 's'],
    inputs: INPUTS.map((I) => ({ value: I.value, label: I.label, trace: run(I.x) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const I = byValue[g.input] || INPUTS[0];
      const v = g.frame.vars, ln = g.frame.line, k = g.k;
      const cx = F.ref('x'), cs = F.ref('s'), idx = C('index'), key = C('key'), cost = C('cost'), ink = PAL.ink, muted = PAL.muted;
      const hits = [];
      const root = Math.floor(Math.sqrt(I.x));
      let head;
      if (ln <= 1) head = `⌊√x⌋ for x = ${big(I.x)} without a square-root instruction.`;
      else if (ln === 2) head = `x has ${v.rp + 1} bits: its top bit is bit r′ = ${v.rp}.`;
      else if (ln === 3 || ln === 4) head = `Shifted up ${v.upgrade} places, x′ = ${big(v.xp)} has ${v.rp + v.upgrade + 1} bits, and √x′ = 2^${v.upgrade / 2}·√x.`;
      else if (ln === 5) head = `sqrtab[${big(v.idx)}] = ${v.entry}, halved ${v.upgrade / 2} times: s = ${v.s}, and ⌊√x⌋ is s, s + 1 or s + 2.`;
      else if (ln === 6) head = v.inc ? `(s + 1)² ≤ x, so s rises to ${v.s}.` : `(s + 1)² = ${big((v.s + 1) * (v.s + 1))} > x, so s = ${v.s} needs no correction.`;
      else head = `⌊√${big(I.x)}⌋ = ${v.s}, after ${v.inc} correction${v.inc === 1 ? '' : 's'}.`;
      topline(ctx, head);
      /* the 30 bit places of x and of x′, bit 29 on the left */
      const NB = 30, bw = 38, X0 = 700 - (NB * bw) / 2, bit = (val, b) => Math.floor(val / 2 ** b) % 2;
      const row = (val, y, name, color, shownTop) => {
        for (let b = NB - 1; b >= 0; b -= 1) {
          const x = X0 + (NB - 1 - b) * bw, on = val !== null && bit(val, b) === 1;
          const inIdx = shownTop && b >= 14;
          if (inIdx) rect(ctx, x, y - 26, bw, 52, alpha(idx, 0.16), null);
          rect(ctx, x + 1, y - 26, bw - 2, 52, null, on ? ink : alpha(ink, 0.35), on ? 2.5 : 1.5);
          if (val !== null) text(ctx, on ? '1' : '0', x + bw / 2, y, on ? key : alpha(ink, 0.35), { size: 24, align: 'center', base: 'middle', weight: on ? 600 : 400 });
        }
        text(ctx, name, X0 - 16, y, color, { size: 28, weight: 600, align: 'right', base: 'middle', italic: true });
      };
      const Y1 = 170, Y2 = 300;
      for (let b = NB - 1; b >= 0; b -= 5) text(ctx, String(b), X0 + (NB - 1 - b) * bw + bw / 2, Y1 - 44, muted, { size: 18, align: 'center', base: 'middle' });
      row(I.x, Y1, 'x', cx, false);
      if (v.rp !== null) {
        const xr = X0 + (NB - 1 - v.rp) * bw;
        rect(ctx, xr - 2, Y1 - 30, bw + 4, 60, null, idx, 3);
      }
      hits.push({ x: 700, y: Y1, r: (NB * bw) / 2, name: `x = ${big(I.x)} in binary` });
      if (v.xp !== null) {
        const t = ln === 4 && g.prev.line !== 4 ? k : 1;
        ctx.save(); ctx.globalAlpha *= t;
        row(v.xp, Y2, 'x′', ink, ln >= 5);
        ctx.restore();
        if (v.upgrade) arrow(ctx, X0 + (NB - 1 - v.rp) * bw + bw / 2, Y1 + 30, X0 + (NB - 1 - v.rp - v.upgrade) * bw + bw / 2, Y2 - 30, alpha(ink, 0.5), 3);
        hbracket(ctx, X0, X0 + 16 * bw, Y2 + 44, idx, 'the top 16 bits index sqrtab', { side: 'below' });
        hits.push({ x: 700, y: Y2, r: (NB * bw) / 2, name: `x′ = x · 2^${v.upgrade} = ${big(v.xp)}` });
      }
      const Y3 = 440;
      if (v.s !== null) {
        seg(ctx, [[`sqrtab[${big(v.idx)}] = ${v.entry} = ⌊√(${big(v.idx)}·2¹⁴)⌋,  `, ink], [`s = ${v.entry} >> ${v.upgrade / 2} = ${(v.entry >> (v.upgrade / 2))}`, cs, { weight: 600 }]], Y3);
        const sq = (v.s + 1) * (v.s + 1);
        seg(ctx, [['s', cs, { weight: 600 }], [` = ${v.s}:  (s + 1)² = ${big(sq)} ${sq <= I.x ? '≤' : '>'} `, ink], ['x', cx, { weight: 600 }], [` = ${big(I.x)}`, ink]], Y3 + 50);
        seg(ctx, [[`corrections ${v.inc} ≤ 2  ·  ⌊√x⌋ = ${root}`, cost]], Y3 + 100);
      } else seg(ctx, [['sqrtab[t] holds ⌊√(t·2¹⁴)⌋ for the 2¹⁶ values of the top bits t', muted]], Y3);
      tip.hits = hits;
    },
  });
  F.hover(d.stage, () => tip.hits, d.c);
})();

/* ================================================================ the SEList figures */
/* A list is [{id, d: [elements]}, …] in next order; the dummy is not stored. b = 3: a block holds at most 4. */
const SB = 3;
const fragile = (list) => list.filter((nd) => nd.d.length !== SB).length;
/* the location of index i, as _get_location finds it: [node position, j] */
const locate = (list, i) => {
  const n = list.reduce((s, nd) => s + nd.d.length, 0);
  if (i < Math.floor(n / 2)) { let p = 0, j = i; while (j >= list[p].d.length) { j -= list[p].d.length; p += 1; } return [p, j]; }
  let p = list.length, idx = n; while (i < idx) { p -= 1; idx -= list[p].d.length; } return [p, i - idx];
};
const copyList = (list) => list.map((nd) => ({ id: nd.id, d: nd.d.slice() }));
const CW = 62, CH = 72, NODE = (SB + 1) * CW, NGAP = 52;
/* where each node stands: rows of up to six, centred; a node is (b + 1) cells */
const layoutOf = (list, top) => {
  const per = 4, rows = Math.ceil(Math.max(list.length, 1) / per), pos = new Map();
  list.forEach((nd, p) => {
    const row = Math.floor(p / per), inRow = Math.min(per, list.length - row * per);
    const W = inRow * NODE + (inRow - 1) * NGAP + (row === rows - 1 ? NGAP + 90 : 0);
    const x0 = 700 - W / 2;
    pos.set(nd.id, { x: x0 + (p - row * per) * (NODE + NGAP), y: top + row * 190, row });
  });
  const last = list.length ? pos.get(list[list.length - 1].id) : { x: 700 - NODE - NGAP, y: top, row: 0 };
  return { pos, dummy: { x: last.x + NODE + NGAP, y: last.y }, rows };
};
/* draw one frame of a SEList figure: the nodes, the moves of the call so far, u, w and i, and the counts */
function drawSEList(g, P, F_, opts) {
  const ctx = g.ctx; if (!ctx) return [];
  const v = g.frame.vars, pv = g.prev.vars, k = g.k;
  const cu = F_.ref('u'), cw = F_.ref('w'), ci = F_.ref('i'), key = C('key'), size = C('size'), cost = C('cost'), idx = C('index');
  const ink = PAL.ink, muted = PAL.muted, hits = [];
  const TOP = opts.top;
  const L1 = layoutOf(v.list, TOP), L0 = layoutOf(pv.list || v.list, TOP);
  const at = (id) => {
    const a = L1.pos.get(id), b = L0.pos.get(id);
    if (!a) return b; if (!b || b.row !== a.row) return a;
    return { x: lerp(b.x, a.x, k), y: lerp(b.y, a.y, k), row: a.row };
  };
  const cellX = (id, j) => at(id).x + j * CW + CW / 2;
  /* the nodes, fragile ones (not exactly b elements) dashed; a node about to be unlinked fades */
  let gi = 0;
  v.list.forEach((nd, p) => {
    const q = at(nd.id), frag = nd.d.length !== SB;
    const born = pv.list && !pv.list.some((o) => o.id === nd.id);
    ctx.save(); ctx.globalAlpha *= born ? k : 1;
    rect(ctx, q.x, q.y - CH / 2, NODE, CH, PAL.panel, ink, frag ? 3 : 2.5, frag ? [10, 7] : null);
    for (let j = 0; j <= SB; j += 1) {
      const x = q.x + j * CW;
      if (j) line(ctx, x, q.y - CH / 2, x, q.y + CH / 2, alpha(ink, 0.45), 1.5);
      if (j < nd.d.length) {
        rect(ctx, x + 2, q.y - CH / 2 + 2, CW - 4, CH - 4, alpha(idx, 0.14), null);
        const moving = v.mv && v.mv.to === nd.id && v.mv.j === j && !(pv.mv && pv.mv.to === nd.id && pv.mv.j === j && pv.mv.el === v.mv.el);
        if (!moving || k > 0.6) text(ctx, String(nd.d[j]), x + CW / 2, q.y, key, { size: 34, align: 'center', base: 'middle', weight: 600 });
        hits.push({ x: x + CW / 2, y: q.y, r: CW / 2, name: `index ${gi}: ${nd.d[j]}, in block ${p} at ${j}` });
        gi += 1;
      }
    }
    hits.push({ x: q.x + NODE / 2, y: q.y - CH / 2 - 6, r: NODE / 2, name: `block ${p}: ${nd.d.length} element${nd.d.length === 1 ? '' : 's'}${frag ? ', fragile' : ', rugged'}` });
    ctx.restore();
    /* the next and prev references to the following node, or to the dummy after the last */
    const nx = p + 1 < v.list.length ? at(v.list[p + 1].id) : null;
    if (nx && nx.row === q.row) {
      arrow(ctx, q.x + NODE + 4, q.y - 8, nx.x - 4, nx.y - 8, alpha(ink, 0.6), 3);
      arrow(ctx, nx.x - 4, q.y + 8, q.x + NODE + 4, q.y + 8, alpha(ink, 0.6), 3);
    } else if (nx) {
      line(ctx, q.x + NODE + 4, q.y, q.x + NODE + 22, q.y, alpha(ink, 0.6), 3);
      text(ctx, '…', q.x + NODE + 30, q.y, muted, { size: 26, base: 'middle' });
      text(ctx, '…', nx.x - 40, nx.y, muted, { size: 26, base: 'middle' });
      line(ctx, nx.x - 22, nx.y, nx.x - 4, nx.y, alpha(ink, 0.6), 3);
    }
  });
  /* the dummy after the last node: where a search that runs off the end arrives */
  const dm = L1.dummy;
  if (v.list.length) {
    const lq = at(v.list[v.list.length - 1].id);
    arrow(ctx, lq.x + NODE + 4, lq.y - 8, dm.x - 4, dm.y - 8, alpha(ink, 0.6), 3);
    arrow(ctx, dm.x - 4, dm.y + 8, lq.x + NODE + 4, lq.y + 8, alpha(ink, 0.6), 3);
  }
  rect(ctx, dm.x, dm.y - CH / 2, 100, CH, alpha(ink, 0.05), alpha(ink, 0.5), 2, [4, 6]);
  text(ctx, 'dummy', dm.x + 50, dm.y, muted, { size: 24, align: 'center', base: 'middle' });
  /* the moves this call made: an arc from an element's old cell to its new one, the last as it moves */
  (v.moves || []).forEach((mv, q) => {
    const a = L1.pos.get(mv.to);
    if (!a) return;
    const cur = q === v.moves.length - 1 && v.mv && v.mv.el === mv.el && v.mv.to === mv.to;
    const fresh = cur && !(pv.mv && pv.mv.el === mv.el && pv.mv.to === mv.to);
    const src = mv.fromPos, x1 = cellX(mv.to, mv.j), y1 = at(mv.to).y - CH / 2 - 2;
    const x0 = src.x, y0 = src.y - CH / 2 - 2;
    const t = fresh ? Math.max(0.2, k) : 1;
    if (Math.abs(y0 - y1) < 5) curve(ctx, x0, y0, lerp(x0, x1, t), y1, 34, cur ? cw : alpha(cw, 0.35), cur ? 4 : 3);
    else if (cur) arrow(ctx, x0, y0, lerp(x0, x1, t), lerp(y0, y1, t), cw, 4);
  });
  /* u and w above their nodes; w only while the search or a spread or gather runs, else it is u */
  const tag = (id, name, color, dx) => {
    if (id === null || id === undefined) return;
    if (id === 'dummy') { const x = dm.x + 50 + dx; arrow(ctx, x, dm.y - CH / 2 - 52, x, dm.y - CH / 2 - 6, color, 4); text(ctx, name, x, dm.y - CH / 2 - 70, color, { size: 32, weight: 600, align: 'center', base: 'middle', italic: true }); return; }
    const q = at(id); if (!q) return;
    const x = q.x + NODE / 2 + dx;
    arrow(ctx, x, q.y - CH / 2 - 52, x, q.y - CH / 2 - 6, color, 4);
    text(ctx, name, x, q.y - CH / 2 - 70, color, { size: 32, weight: 600, align: 'center', base: 'middle', italic: true });
  };
  const same = v.u !== null && v.u === v.w;
  tag(v.u, 'u', cu, same ? -26 : 0);
  if (v.w !== null && v.w !== undefined) tag(v.w, 'w', cw, same ? 26 : 0);
  /* i under the cell where the call works */
  if (v.ipos) {
    const q = at(v.ipos[0]);
    if (q) {
      const x = q.x + v.ipos[1] * CW + CW / 2, y = q.y + CH / 2 + 8;
      arrow(ctx, x, y + 40, x, y, ci, 4);
      text(ctx, `i = ${v.i}`, x, y + 62, ci, { size: 26, weight: 600, align: 'center', base: 'middle' });
    }
  }
  /* the counts */
  const Y0 = TOP + (L1.rows - 1) * 190 + 160;
  seg(ctx, [[`Φ = fragile nodes (dashed) = ${fragile(v.list)}  ·  `, cost], ['b', size, { weight: 600 }], [` = ${SB}, so a block holds ${SB - 1} to ${SB + 1}, the last fewer`, ink]], Y0);
  opts.counts(ctx, v, Y0 + 46);
  legend(ctx, { l: 40, r: 1360, t: Y0 + 80, b: Y0 + 130 }, [
    { s: 'rugged: b elements', color: ink, w: 3 },
    { s: 'fragile: not b', color: ink, w: 3, dash: [10, 7] },
  ], { corner: 'top' });
  return hits;
}
/* one SEList figure: its presets run through the trace body `body(at, list, op, snap)` */
function selistFigure(o) {
  const traces = Object.fromEntries(o.presets.map((P) => [P.value, F.trace((at) => {
    const list = copyList(P.list);
    let nextId = list.length + 1;
    const st = { k: -1, moves: [], calls: 0, cases: [0, 0, 0, 0], big: 0, moved: 0, i: null, x: null, j: null, r: null, u: null, w: null, ipos: null, mv: null, cse: null };
    const snap = (e) => Object.assign({ list: copyList(list), k: st.k, moves: st.moves.map((m) => ({ ...m, fromPos: { ...m.fromPos } })), calls: st.calls,
      cases: st.cases.slice(), big: st.big, moved: st.moved, i: st.i, x: st.x, j: st.j, r: st.r, u: st.u, w: st.w, ipos: st.ipos, mv: st.mv, cse: st.cse }, e || {});
    const lay = () => layoutOf(list, o.top);
    /* move one element: from node a's end or front into node b's front or end, the arc's start taken before */
    const move = (from, to, fromEnd, toFront) => {
      const L = lay(), fa = L.pos.get(list[from].id);
      const fj = fromEnd ? list[from].d.length - 1 : 0;
      const fromPos = { x: fa.x + fj * CW + CW / 2, y: fa.y };
      const el = fromEnd ? list[from].d.pop() : list[from].d.shift();
      if (toFront) list[to].d.unshift(el); else list[to].d.push(el);
      const mv = { el, to: list[to].id, j: toFront ? 0 : list[to].d.length - 1, fromPos };
      st.moves.push(mv); st.mv = mv; st.moved += 1;
      return mv;
    };
    const newNode = (before) => { const nd = { id: nextId++, d: [] }; list.splice(before, 0, nd); return nd; };
    at(o.startLine, snap());
    P.ops.forEach((op, kk) => {
      st.k = kk; st.moves = []; st.mv = null; st.calls += 1; st.i = op[1]; st.x = op[2] === undefined ? null : op[2];
      st.u = null; st.w = null; st.j = null; st.r = null; st.ipos = null; st.cse = null;
      o.body(at, list, op, snap, st, { move, newNode, lay });
    });
  })]));
  return traces;
}

/* ================================================================ sim-selist-add */
(function () {
  /* BEGIN ODS LISTINGS seladd (ch03/3.6/inline_code.py) */
  const PY = "def add(self, i, x):\n    if i == self.n:\n        self.append(x)\n        return\n    u, j = self._get_location(i)\n    r = 0\n    w = u\n    while r < self.b and w is not self.dummy and w.d.size() == self.b+1:\n        w = w.next\n        r += 1\n    if r == self.b:  # b blocks, each with b+1 elements\n        self._spread(u)\n        w = u\n    if w == self.dummy: # ran off the end - add new node\n        w = self._add_before(w)\n    while w is not u: # work backwards, shifting elements as we go\n         w.d.add_first(w.prev.d.remove_last())\n         w = w.prev\n    w.d.add(j, x)\n    self.n += 1\n\ndef _spread(self, u):\n    w = u\n    for j in range(self.b):\n        w = w.next\n    w = self._add_before(w)\n    while w is not u:\n        while w.d.size() < self.b:\n            w.d.add_first(w.prev.d.remove_last())\n        w = w.prev";
  const JAVA = "void add(int i, T x) {\n    if (i == n) {\n        add(x);\n        return;\n    }\n    Location l = getLocation(i);\n    Node u = l.u;\n    int r = 0;\n    while (r < b && u != dummy && u.d.size() == b+1) {\n        u = u.next;\n        r++;\n    }\n    if (r == b) {      // b blocks each with b+1 elements\n        spread(l.u);\n        u = l.u;\n    }\n    if (u == dummy) {  // ran off the end - add new node\n        u = addBefore(u);\n    }\n    while (u != l.u) { // work backwards, shifting elements\n        u.d.add(0, u.prev.d.remove(u.prev.d.size()-1));\n        u = u.prev;\n    }\n    u.d.add(l.j, x);\n    n++;\n}\n\nvoid spread(Node u) {\n    Node w = u;\n    for (int j = 0; j < b; j++) {\n        w = w.next;\n    }\n    w = addBefore(w);\n    while (w != u) {\n        while (w.d.size() < b)\n            w.d.add(0,w.prev.d.remove(w.prev.d.size()-1));\n        w = w.prev;\n    }\n}";
  const CPP = "void add(int i, T x) {\n    if (i == n) {\n        add(x);\n        return;\n    }\n    Location l; getLocation(i, l);\n    Node *u = l.u;\n    int r = 0;\n    while (r < b && u != &dummy && u->d.size() == b+1) {\n        u = u->next;\n        r++;\n    }\n    if (r == b) {// b blocks each with b+1 elements\n        spread(l.u);\n        u = l.u;\n    }\n    if (u == &dummy) { // ran off the end - add new node\n        u = addBefore(u);\n    }\n    while (u != l.u) { // work backwards, shifting elements\n        u->d.add(0, u->prev->d.remove(u->prev->d.size()-1));\n        u = u->prev;\n    }\n    u->d.add(l.j, x);\n    n++;\n}\n\nvoid spread(Node *u) {\n    Node *w = u;\n    for (int j = 0; j < b; j++) {\n        w = w->next;\n    }\n    w = addBefore(w);\n    while (w != u) {\n        while (w->d.size() < b)\n            w->d.add(0, w->prev->d.remove(w->prev->d.size()-1));\n        w = w->prev;\n    }\n}";
  /* END ODS LISTINGS seladd */
  const JS = [
    'addAt(i, x) {',
    '    if (i === this.n) {',
    '        this.add(x);',
    '        return;',
    '    }',
    '    const l = this.getLocation(i);',
    '    let u = l.u;',
    '    let r = 0;',
    '    while (r < this.b && u !== this.dummy && u.d.size() === this.b+1) {',
    '        u = u.next;',
    '        r++;',
    '    }',
    '    if (r === this.b) {      // b blocks each with b+1 elements',
    '        this.spread(l.u);',
    '        u = l.u;',
    '    }',
    '    if (u === this.dummy) {  // ran off the end - add new node',
    '        u = this.addBefore(u);',
    '    }',
    '    while (u !== l.u) { // work backwards, shifting elements',
    '        u.d.add(0, u.prev.d.remove(u.prev.d.size()-1));',
    '        u = u.prev;',
    '    }',
    '    u.d.add(l.j, x);',
    '    this.n++;',
    '}',
    '',
    'spread(u) {',
    '    let w = u;',
    '    for (let j = 0; j < this.b; j++) {',
    '        w = w.next;',
    '    }',
    '    w = this.addBefore(w);',
    '    while (w !== u) {',
    '        while (w.d.size() < this.b)',
    '            w.d.add(0, w.prev.d.remove(w.prev.d.size()-1));',
    '        w = w.prev;',
    '    }',
    '}',
  ].join('\n');
  /* Python line → Java's, C++'s and JavaScript's (the same 39 lines in all three) */
  const MAP = { 1: 1, 2: 2, 3: 3, 4: 4, 5: [6, 7], 6: 8, 7: 7, 8: 9, 9: 10, 10: 11, 11: 13, 12: 14, 13: 15, 14: 17, 15: 18, 16: 20, 17: 21, 18: 22,
    19: 24, 20: 25, 22: 28, 23: 29, 24: 30, 25: 31, 26: 33, 27: 34, 28: 35, 29: 36, 30: 37 };
  const LT = (s) => s.split('');
  const PRESETS = [
    { value: 'case1', label: 'Case 1', list: [{ id: 1, d: LT('abcd') }, { id: 2, d: LT('efgh') }, { id: 3, d: LT('ij') }], ops: [['add', 1, 'x']] },
    { value: 'case2', label: 'Case 2', list: [{ id: 1, d: LT('abcd') }, { id: 2, d: LT('efgh') }], ops: [['add', 1, 'x']] },
    { value: 'case3', label: 'Case 3', list: [{ id: 1, d: LT('abcd') }, { id: 2, d: LT('efgh') }, { id: 3, d: LT('ijkl') }], ops: [['add', 1, 'x']] },
    { value: 'run', label: '16 adds at the front', list: [], ops: LT('abcdefghijklmnop').map((x) => ['add', 0, x]) },
  ];
  const body = (at, list, op, snap, st, h) => {
    const i = op[1], x = op[2];
    const n = list.reduce((s, nd) => s + nd.d.length, 0);
    at(1, snap());
    if (i === n) {
      at(2, snap());
      let last = list.length - 1;
      if (last < 0 || list[last].d.length === SB + 1) { h.newNode(list.length); last = list.length - 1; st.cse = 'new'; } else st.cse = 'end';
      list[last].d.push(x); st.u = list[last].id; st.ipos = [list[last].id, list[last].d.length - 1];
      at(3, snap(), ['append', x]);
      at(4, snap());
      return;
    }
    const [p, j] = locate(list, i);
    st.u = list[p].id; st.j = j; st.ipos = [list[p].id, j];
    at(5, snap());
    let r = 0, wp = p; st.r = 0; st.w = st.u;
    at(6, snap()); at(7, snap());
    while (r < SB && wp < list.length && list[wp].d.length === SB + 1) {
      wp += 1; st.w = wp < list.length ? list[wp].id : 'dummy'; at(9, snap());
      r += 1; st.r = r; at(10, snap());
    }
    let cse = r === SB ? 3 : wp === list.length ? 2 : 1;
    st.cse = cse;
    if (r === SB) {
      /* _spread(u), recorded one call deeper */
      at.enter('spread');
      at(22, snap()); let w = p; st.w = list[w].id; at(23, snap());
      for (let jj = 0; jj < SB; jj += 1) { at(24, snap()); w += 1; st.w = w < list.length ? list[w].id : 'dummy'; at(25, snap()); }
      h.newNode(w); st.w = list[w].id; at(26, snap(), ['node']);
      while (w !== p) {
        at(27, snap());
        while (list[w].d.length < SB) { at(28, snap()); h.move(w - 1, w, true, true); at(29, snap(), ['move']); }
        w -= 1; st.w = list[w].id; at(30, snap());
      }
      at.leave();
      st.big += 1;
      at(12, snap());
      wp = p; st.w = st.u; at(13, snap());
    }
    if (wp === list.length) { h.newNode(list.length); st.w = list[wp].id; at(15, snap(), ['node']); }
    while (wp !== p) {
      h.move(wp - 1, wp, true, true); at(17, snap(), ['move']);
      wp -= 1; st.w = list[wp].id; at(18, snap());
    }
    st.mv = null;
    list[p].d.splice(j, 0, x); st.cases[cse] += 1;
    at(19, snap(), ['put', x]);
    at(20, snap());
  };
  const traces = selistFigure({ presets: PRESETS, body, startLine: 21, top: 230 });
  const d = sim('sim-selist-add', 800);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: { javascript: AI },
    lineMap: { java: MAP, cpp: MAP, javascript: MAP },
    blocks: [
      { id: 'add', lines: [1, 20], label: 'add(i, x)', touches: ['list', 'u', 'w'] },
      { id: 'append', lines: [2, 4], label: 'at the end: append(x)', touches: ['list'] },
      { id: 'locate', lines: [5, 5], label: 'find u, the block that holds index i, and j, the place in it', touches: ['u', 'j'] },
      { id: 'scan', lines: [6, 10], label: 'look at most b blocks on for one with room', touches: ['w', 'r'] },
      { id: 'hop', lines: [9, 10], label: 'w is full: go on to the next block', touches: ['w', 'r'] },
      { id: 'spreadcall', lines: [11, 13], label: 'b full blocks: spread(u)', touches: ['list', 'w'] },
      { id: 'newnode', lines: [14, 15], label: 'ran off the end: a new block', touches: ['list', 'w'] },
      { id: 'shift', lines: [16, 18], label: 'move one element back into each block from w to u', touches: ['list', 'w'] },
      { id: 'back', lines: [17, 18], label: 'the last element of the block before w goes to w’s front', touches: ['list', 'w'] },
      { id: 'insert', lines: [19, 20], label: 'add x to u’s block at j', touches: ['list'] },
      { id: 'spread', lines: [22, 30], label: 'spread(u): b + 1 blocks of b', touches: ['list', 'w'] },
      { id: 'walk', lines: [23, 26], label: 'go b blocks on and add an empty block there', touches: ['list', 'w'] },
      { id: 'fill', lines: [28, 29], label: 'move one element back into w', touches: ['list'] },
    ],
    refs: { python: { u: () => F.ref('u'), w: () => F.ref('w'), i: () => F.ref('i') }, java: { w: () => F.ref('w'), i: () => F.ref('i') },
      cpp: { w: () => F.ref('w'), i: () => F.ref('i') }, javascript: { w: () => F.ref('w'), i: () => F.ref('i') } },
  });
  const byValue = Object.fromEntries(PRESETS.map((P) => [P.value, P]));
  const tip = { hits: [] };
  F.debug(d, {
    code, watch: ['i', 'x', 'j', 'r'],
    inputs: PRESETS.map((P) => ({ value: P.value, label: P.label, trace: traces[P.value] })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const P = byValue[g.input] || PRESETS[0];
      const v = g.frame.vars, ln = g.frame.line;
      const op = v.k >= 0 ? P.ops[v.k] : null;
      let head;
      if (!op) head = P.list.length ? `An SEList with b = ${SB}: ${P.list.length} blocks; add(${P.ops[0][1]}, ${P.ops[0][2]}) puts x at index ${P.ops[0][1]}.` : `An empty SEList with b = ${SB}; each add puts its element at index 0.`;
      else if (ln >= 22 && ln <= 30) head = `${SB} blocks from u on hold b + 1 = ${SB + 1} each, so spread(u) deals their elements into ${SB + 1} blocks of ${SB}.`;
      else if (ln === 2 || ln === 3 || ln === 4) head = `add(${op[1]}, ${op[2]}) is at the end: append puts ${op[2]} in the last block${v.cse === 'new' ? ', a new one' : ''}.`;
      else if (ln === 5) head = `Index ${op[1]} is in block u, at place j = ${v.j}.`;
      else if (ln >= 6 && ln <= 10) head = v.w === 'dummy' ? `Every block from u to the end is full: the search ran off the end after r = ${v.r}.` : v.r ? `${v.r} full block${v.r === 1 ? '' : 's'} so far; w is the next one to look at.` : 'The search starts at u.';
      else if (ln === 12 || ln === 13) head = `After the spread u has room: Case 3.`;
      else if (ln === 15) head = 'Case 2: a new last block gives the room.';
      else if (ln === 17 || ln === 18) head = `Case ${v.cse}: elements move back one block at a time, from w towards u.`;
      else head = `${op[2]} goes into u’s block at j = ${v.j}: Case ${v.cse}.`;
      topline(ctx, head);
      tip.hits = drawSEList(g, P, F, {
        top: 230,
        counts: (c, vv, y) => {
          const m = vv.calls, s = vv.big;
          /* the lemma's bound counts from an empty SEList, so only the run, which starts empty, states it */
          const bound = P.list.length ? `spreads ${s}` : `spreads s = ${s} ≤ m/b = ${(m / SB).toFixed(1)}`;
          seg(c, [[`add calls m = ${m}  ·  ${bound}  ·  elements moved ${vv.moved}`, C('cost')]], y);
        },
      });
    },
  });
  F.hover(d.stage, () => tip.hits, d.c);
})();

/* ================================================================ sim-selist-remove */
(function () {
  /* BEGIN ODS LISTINGS selrem (ch03/3.6/inline_code.py) */
  const PY = "def remove(self, i):\n    u, j = self._get_location(i)\n    y = u.d.get(j)\n    w = u\n    r = 0\n    while r < self.b and w is not self.dummy and w.d.size() == self.b-1:\n        w = w.next\n        r += 1\n    if r == self.b: # b blocks, each with b-1 elements\n        self._gather(u)\n    u.d.remove(j)\n    while u.d.size() < self.b-1 and u.next is not self.dummy:\n        u.d.add_last(u.next.d.remove_first())\n        u = u.next\n    if u.d.size() == 0: self._remove_node(u)\n    self.n -= 1\n\ndef _gather(self, u):\n    w = u\n    for j in range(self.b-1):\n        while w.d.size() < self.b:\n            w.d.add_last(w.next.d.remove_first())\n        w = w.next\n    self._remove_node(w)";
  const JAVA = "T remove(int i) {\n    Location l = getLocation(i);\n    T y = l.u.d.get(l.j);\n    Node u = l.u;\n    int r = 0;\n    while (r < b && u != dummy && u.d.size() == b-1) {\n        u = u.next;\n        r++;\n    }\n    if (r == b) {  // b blocks each with b-1 elements\n        gather(l.u);\n    }\n    u = l.u;\n    u.d.remove(l.j);\n    while (u.d.size() < b-1 && u.next != dummy) {\n        u.d.add(u.next.d.remove(0));\n        u = u.next;\n    }\n    if (u.d.isEmpty()) remove(u);\n    n--;\n    return y;\n}\n\nvoid gather(Node u) {\n    Node w = u;\n    for (int j = 0; j < b-1; j++) {\n        while (w.d.size() < b)\n            w.d.add(w.next.d.remove(0));\n        w = w.next;\n    }\n    remove(w);\n}";
  const CPP = "T remove(int i) {\n    Location l; getLocation(i, l);\n    T y = l.u->d.get(l.j);\n    Node *u = l.u;\n    int r = 0;\n    while (r < b && u != &dummy && u->d.size() == b - 1) {\n        u = u->next;\n        r++;\n    }\n    if (r == b) { // found b blocks each with b-1 elements\n        gather(l.u);\n    }\n    u = l.u;\n    u->d.remove(l.j);\n    while (u->d.size() < b - 1 && u->next != &dummy) {\n        u->d.add(u->next->d.remove(0));\n        u = u->next;\n    }\n    if (u->d.size() == 0)\n        remove(u);\n    n--;\n    return y;\n}\n\nvoid gather(Node *u) {\n    Node *w = u;\n    for (int j = 0; j < b-1; j++) {\n        while (w->d.size() < b)\n            w->d.add(w->next->d.remove(0));\n        w = w->next;\n    }\n    remove(w);\n}";
  /* END ODS LISTINGS selrem */
  const JS = [
    'remove(i) {',
    '    const l = this.getLocation(i);',
    '    const y = l.u.d.get(l.j);',
    '    let u = l.u;',
    '    let r = 0;',
    '    while (r < this.b && u !== this.dummy && u.d.size() === this.b-1) {',
    '        u = u.next;',
    '        r++;',
    '    }',
    '    if (r === this.b) {  // b blocks each with b-1 elements',
    '        this.gather(l.u);',
    '    }',
    '    u = l.u;',
    '    u.d.remove(l.j);',
    '    while (u.d.size() < this.b-1 && u.next !== this.dummy) {',
    '        u.d.add(u.next.d.remove(0));',
    '        u = u.next;',
    '    }',
    '    if (u.d.isEmpty()) this.removeNode(u);',
    '    this.n--;',
    '    return y;',
    '}',
    '',
    'gather(u) {',
    '    let w = u;',
    '    for (let j = 0; j < this.b-1; j++) {',
    '        while (w.d.size() < this.b)',
    '            w.d.add(w.next.d.remove(0));',
    '        w = w.next;',
    '    }',
    '    this.removeNode(w);',
    '}',
  ].join('\n');
  /* Python line → Java's and JavaScript's; C++ writes the empty-block test on two lines (19–20) and so runs one
     line longer from there */
  const MAP = { 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 10, 10: 11, 11: [13, 14], 12: 15, 13: 16, 14: 17, 15: 19, 16: 20,
    18: 24, 19: 25, 20: 26, 21: 27, 22: 28, 23: 29, 24: 31 };
  const MAPC = { ...MAP, 15: [19, 20], 16: 21, 18: 25, 19: 26, 20: 27, 21: 28, 22: 29, 23: 30, 24: 32 };
  const LT = (s) => s.split('');
  const R8 = Array.from({ length: 8 }, (_, q) => ({ id: q + 1, d: LT('abcdefghijklmnopqrstuvwx'.slice(3 * q, 3 * q + 3)) }));
  const PRESETS = [
    { value: 'case1', label: 'Case 1', list: [{ id: 1, d: LT('ab') }, { id: 2, d: LT('cd') }, { id: 3, d: LT('efg') }], ops: [['remove', 1]] },
    { value: 'case2', label: 'Case 2', list: [{ id: 1, d: LT('ab') }, { id: 2, d: LT('cd') }], ops: [['remove', 1]] },
    { value: 'case3', label: 'Case 3', list: [{ id: 1, d: LT('ab') }, { id: 2, d: LT('cd') }, { id: 3, d: LT('ef') }, { id: 4, d: LT('gh') }], ops: [['remove', 1]] },
    { value: 'run', label: '12 removes at the front', list: R8, ops: Array.from({ length: 12 }, () => ['remove', 0]) },
  ];
  const body = (at, list, op, snap, st, h) => {
    const i = op[1];
    at(1, snap());
    const [p, j] = locate(list, i);
    st.u = list[p].id; st.j = j; st.ipos = [list[p].id, j]; at(2, snap());
    st.x = list[p].d[j]; at(3, snap());
    let wp = p, r = 0; st.w = st.u; st.r = 0; at(4, snap()); at(5, snap());
    while (r < SB && wp < list.length && list[wp].d.length === SB - 1) {
      wp += 1; st.w = wp < list.length ? list[wp].id : 'dummy'; at(7, snap());
      r += 1; st.r = r; at(8, snap());
    }
    const cse = r === SB ? 3 : wp === list.length ? 2 : 1;
    st.cse = cse;
    if (r === SB) {
      at.enter('gather');
      at(18, snap()); let w = p; st.w = list[w].id; at(19, snap());
      for (let jj = 0; jj < SB - 1; jj += 1) {
        at(20, snap());
        while (list[w].d.length < SB) { at(21, snap()); h.move(w + 1, w, false, false); at(22, snap(), ['move']); }
        w += 1; st.w = list[w].id; at(23, snap());
      }
      list.splice(w, 1); st.w = null; at(24, snap(), ['unlink']);
      at.leave();
      st.big += 1;
      at(10, snap());
    }
    st.w = null; st.mv = null;
    list[p].d.splice(j, 1); st.ipos = null; at(11, snap(), ['take', st.x]);
    let up = p;
    while (list[up].d.length < SB - 1 && up + 1 < list.length) {
      at(12, snap());
      h.move(up + 1, up, false, false); at(13, snap(), ['move']);
      up += 1; st.u = list[up].id; at(14, snap());
    }
    if (list[up].d.length === 0) { list.splice(up, 1); st.u = null; }
    at(15, snap());
    st.cases[cse] += 1;
    at(16, snap());
  };
  const traces = selistFigure({ presets: PRESETS, body, startLine: 17, top: 230 });
  const d = sim('sim-selist-remove', 800);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: { javascript: AI },
    lineMap: { java: MAP, cpp: MAPC, javascript: MAP },
    blocks: [
      { id: 'remove', lines: [1, 16], label: 'remove(i)', touches: ['list', 'u', 'w'] },
      { id: 'locate', lines: [2, 3], label: 'find u, the block that holds index i, and the element y there', touches: ['u', 'j'] },
      { id: 'scan', lines: [4, 8], label: 'look at most b blocks on for one with more than b − 1', touches: ['w', 'r'] },
      { id: 'hop', lines: [7, 8], label: 'w holds only b − 1: go on to the next block', touches: ['w', 'r'] },
      { id: 'gathercall', lines: [9, 10], label: 'b blocks of b − 1: gather(u)', touches: ['list'] },
      { id: 'take', lines: [11, 11], label: 'take the element out of u’s block', touches: ['list'] },
      { id: 'borrow', lines: [12, 14], label: 'borrow from the next block while u holds fewer than b − 1', touches: ['list', 'u'] },
      { id: 'one', lines: [13, 14], label: 'the first element of the next block goes to u’s end', touches: ['list', 'u'] },
      { id: 'empty', lines: [15, 16], label: 'an empty last block goes', touches: ['list'] },
      { id: 'gather', lines: [18, 24], label: 'gather(u): b − 1 blocks of b', touches: ['list', 'w'] },
      { id: 'fill', lines: [21, 22], label: 'move one element forward into w', touches: ['list'] },
      { id: 'unlink', lines: [24, 24], label: 'remove the empty block', touches: ['list'] },
    ],
    refs: { python: { u: () => F.ref('u'), w: () => F.ref('w'), i: () => F.ref('i') }, java: { w: () => F.ref('w'), i: () => F.ref('i') },
      cpp: { w: () => F.ref('w'), i: () => F.ref('i') }, javascript: { w: () => F.ref('w'), i: () => F.ref('i') } },
  });
  const byValue = Object.fromEntries(PRESETS.map((P) => [P.value, P]));
  const tip = { hits: [] };
  F.debug(d, {
    code, watch: ['i', 'x', 'j', 'r'],
    inputs: PRESETS.map((P) => ({ value: P.value, label: P.label, trace: traces[P.value] })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const P = byValue[g.input] || PRESETS[0];
      const v = g.frame.vars, ln = g.frame.line;
      const op = v.k >= 0 ? P.ops[v.k] : null;
      let head;
      if (!op) head = `An SEList with b = ${SB}: ${P.list.length} blocks; remove(${P.ops[0][1]}) takes out ${P.list[0].d[P.ops[0][1]]}.`;
      else if (ln >= 18 && ln <= 24) head = `${SB} blocks from u on hold only b − 1 = ${SB - 1} each, so gather(u) fills ${SB - 1} of them to ${SB} and drops the last.`;
      else if (ln <= 3) head = `Index ${op[1]} is in block u, at place j = ${v.j}: the element ${v.x}.`;
      else if (ln <= 8) head = v.w === 'dummy' ? `The search ran off the end after r = ${v.r} block${v.r === 1 ? '' : 's'} of ${SB - 1}.` : v.r ? `${v.r} block${v.r === 1 ? '' : 's'} of ${SB - 1} so far; w is the next one to look at.` : 'The search starts at u.';
      else if (ln === 10) head = 'After the gather u holds b elements: Case 3.';
      else if (ln === 11) head = `${v.x} leaves u’s block.`;
      else if (ln >= 12 && ln <= 14) head = 'u holds fewer than b − 1, so it borrows the next block’s first element.';
      else head = `remove(${op[1]}) took out ${v.x}: Case ${v.cse}.`;
      topline(ctx, head);
      tip.hits = drawSEList(g, P, F, {
        top: 230,
        counts: (c, vv, y) => {
          /* the run starts from blocks of exactly b, so Φ = 0 there and the lemma's bound applies */
          const bound = P.value === 'run' ? `gathers ${vv.big} ≤ m/b = ${(vv.calls / SB).toFixed(1)}` : `gathers ${vv.big}`;
          seg(c, [[`remove calls m = ${vv.calls}  ·  ${bound}  ·  elements moved ${vv.moved}`, C('cost')]], y);
        },
      });
    },
  });
  F.hover(d.stage, () => tip.hits, d.c);
})();
};
