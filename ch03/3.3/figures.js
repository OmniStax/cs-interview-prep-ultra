/* Figures for section 3.3 Deques. Boots against the section's text article.
   Two debugger figures (code beside the drawing, stepped by block: METHOD §2.3), each opening on the calls of the
   ODS figure it stands for. sim-arraydeque: ODS's ArrayDeque on its circular array, shifting the shorter side of
   position i (ODS Figure 2.3). sim-dualarraydeque: ODS's DualArrayDeque, two ArrayStacks back to back, rebuilt by
   balance() when one outgrows the other threefold (ODS Figure 2.4), with the lemma's potential and its count.
   The panels hold ODS's code: Python (canonical, the trace's lines, shown as ODS prints it), Java and C++ as ODS's
   editions print them, written in below by ch03/3.3/inline_code.py from the source cache; JavaScript is the AI's
   translation (of the Java; DualArrayDeque's balance() of the C++) and carries the AI mark. Each trace is the
   figure's own JS copy of the Python: one frame per statement, one per element a loop copies. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['3.3'] = function (root, F) {
const { C, PAL, alpha, text, arrow, line, begin, topline, measure } = F;
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
  /* an arc from one cell to another, its head at the end: an element copied */
  const mx = (x0 + x1) / 2, my = Math.min(y0, y1) - lift;
  ctx.save(); ctx.strokeStyle = color; ctx.fillStyle = color; ctx.lineWidth = w; ctx.lineCap = 'round';
  ctx.beginPath(); ctx.moveTo(x0, y0); ctx.quadraticCurveTo(mx, my, x1, y1); ctx.stroke();
  const a = Math.atan2(y1 - my, x1 - mx), L = 14;
  ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x1 - L * Math.cos(a - 0.45), y1 - L * Math.sin(a - 0.45));
  ctx.lineTo(x1 - L * Math.cos(a + 0.45), y1 - L * Math.sin(a + 0.45)); ctx.closePath(); ctx.fill(); ctx.restore();
};
/* a point along the arc of curve() at t, for an arc drawn partway */
const arcAt = (x0, y0, x1, y1, lift, t) => {
  const mx = (x0 + x1) / 2, my = Math.min(y0, y1) - lift, u = 1 - t;
  return { x: u * u * x0 + 2 * u * t * mx + t * t * x1, y: u * u * y0 + 2 * u * t * my + t * t * y1 };
};
const partArc = (ctx, x0, y0, x1, y1, lift, t, color, w) => {
  /* the first t of the arc, with its head where it has got to */
  const n = 24, pts = [];
  for (let s = 0; s <= n; s += 1) pts.push(arcAt(x0, y0, x1, y1, lift, (t * s) / n));
  ctx.save(); ctx.strokeStyle = color; ctx.fillStyle = color; ctx.lineWidth = w; ctx.lineCap = 'round';
  ctx.beginPath(); pts.forEach((p, s) => (s ? ctx.lineTo(p.x, p.y) : ctx.moveTo(p.x, p.y))); ctx.stroke();
  const p = pts[n], q = pts[n - 1], a = Math.atan2(p.y - q.y, p.x - q.x), L = 14;
  ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(p.x - L * Math.cos(a - 0.45), p.y - L * Math.sin(a - 0.45));
  ctx.lineTo(p.x - L * Math.cos(a + 0.45), p.y - L * Math.sin(a + 0.45)); ctx.closePath(); ctx.fill(); ctx.restore();
};
/* one line of runs, each in its own colour, centred on x */
const seg = (ctx, parts, y, size = 28, x = 700) => {
  const ws = parts.map(([s, , o]) => measure(ctx, s, { size, weight: (o && o.weight) || 400, italic: !!(o && o.italic) }));
  let x0 = x - ws.reduce((s, w) => s + w, 0) / 2;
  parts.forEach(([s, c, o], j) => { text(ctx, s, x0, y, c, { size, base: 'middle', weight: (o && o.weight) || 400, italic: o && o.italic }); x0 += ws[j]; });
};
const num = (v) => String(v).replace('-', '−');   /* a minus sign, not a hyphen */
const LET = 'abcdefghijklmnopqrstuvwxyz'.split('');
/* the call row shared by both figures: each call in ink when done or current (the current one boxed), muted to come,
   an asterisk on a call that rebuilt, as ODS's figures mark them */
const callRow = (ctx, labels, cur, starred, hits, y0 = 112) => {
  const CS = 26, gap = 24;
  const ls = labels.map((s, j) => s + (starred.includes(j) ? '*' : ''));
  const widths = ls.map((s) => measure(ctx, s, { size: CS }));
  const rows = [[]]; let wsum = 0;
  ls.forEach((s, j) => { if (wsum + widths[j] > 1260 && rows[rows.length - 1].length) { rows.push([]); wsum = 0; } rows[rows.length - 1].push(j); wsum += widths[j] + gap; });
  rows.forEach((row, ri) => {
    const tot = row.reduce((s, j) => s + widths[j] + gap, -gap);
    let x = 700 - tot / 2; const y = y0 + ri * 44;
    row.forEach((j) => {
      const on = j === cur, done = j < cur;
      if (on) rect(ctx, x - 8, y - 20, widths[j] + 16, 40, alpha(PAL.ink, 0.06), PAL.ink, 2);
      text(ctx, ls[j], x, y, on || done ? PAL.ink : PAL.muted, { size: CS, base: 'middle', weight: on ? 600 : 400 });
      hits.push({ x: x + widths[j] / 2, y, r: widths[j] / 2, name: `call ${j + 1}: ${labels[j]}${starred.includes(j) ? ', which rebuilt the stacks' : ''}` });
      x += widths[j] + gap;
    });
  });
  return y0 + rows.length * 44;
};

/* ================================================================ sim-arraydeque */
(function () {
  /* BEGIN ODS LISTINGS ARRAYDEQUE (ch03/3.3/inline_code.py) */
  const PY = "def add(self, i, x):\n    if self.n == len(self.a): self._resize()\n    if i < self.n/2:\n        self.j = (self.j-1) % len(self.a)\n        for k in range(i):\n            self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k+1)%len(self.a)]\n    else:\n        for k in range(self.n, i, -1):\n            self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k-1)%len(self.a)]\n    self.a[(self.j+i)%len(self.a)] = x\n    self.n += 1\n\ndef remove(self, i):\n    x = self.a[(self.j+i)%len(self.a)]\n    if i < self.n / 2:\n        for k in range(i, 0, -1):\n            self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k-1)%len(self.a)]\n        self.j = (self.j+1) % len(self.a)\n    else:\n        for k in range(i, self.n-1):\n            self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k+1)%len(self.a)]\n    self.n -= 1\n    if len(self.a) >= 3*self.n: self._resize()\n    return x\n\ndef _resize(self):\n    b = new_array(max(1, 2*self.n))\n    for k in range(self.n):\n        b[k] = self.a[(self.j+k)%len(self.a)]\n    self.a = b\n    self.j = 0";
  const JAVA = "void add(int i, T x) {\n    if (n+1 > a.length) resize();\n    if (i < n/2) { // shift a[0],..,a[i-1] left one position\n        j = (j == 0) ? a.length - 1 : j - 1; //(j-1)mod a.length\n        for (int k = 0; k <= i-1; k++)\n            a[(j+k)%a.length] = a[(j+k+1)%a.length];\n    } else { // shift a[i],..,a[n-1] right one position\n        for (int k = n; k > i; k--)\n            a[(j+k)%a.length] = a[(j+k-1)%a.length];\n    }\n    a[(j+i)%a.length] = x;\n    n++;\n}\n\nT remove(int i) {\n    T x = a[(j+i)%a.length];\n    if (i < n/2) {  // shift a[0],..,[i-1] right one position\n        for (int k = i; k > 0; k--)\n            a[(j+k)%a.length] = a[(j+k-1)%a.length];\n        j = (j + 1) % a.length;\n    } else { // shift a[i+1],..,a[n-1] left one position\n        for (int k = i; k < n-1; k++)\n            a[(j+k)%a.length] = a[(j+k+1)%a.length];\n    }\n    n--;\n    if (3*n < a.length) resize();\n    return x;\n}\n\nvoid resize() {\n    T[] b = newArray(max(2*n,1));\n    for (int k = 0; k < n; k++)\n        b[k] = a[(j+k) % a.length];\n    a = b;\n    j = 0;\n}";
  const CPP = "void add(int i, T x) {\n    if (n + 1 > a.length)    resize();\n    if (i < n/2) { // shift a[0],..,a[i-1] left one position\n        j = (j == 0) ? a.length - 1 : j - 1;\n        for (int k = 0; k <= i-1; k++)\n            a[(j+k)%a.length] = a[(j+k+1)%a.length];\n    } else { // shift a[i],..,a[n-1] right one position\n        for (int k = n; k > i; k--)\n            a[(j+k)%a.length] = a[(j+k-1)%a.length];\n    }\n    a[(j+i)%a.length] = x;\n    n++;\n}\n\nT remove(int i) {\n    T x = a[(j+i)%a.length];\n    if (i < n/2) { // shift a[0],..,[i-1] right one position\n        for (int k = i; k > 0; k--)\n            a[(j+k)%a.length] = a[(j+k-1)%a.length];\n        j = (j + 1) % a.length;\n    } else { // shift a[i+1],..,a[n-1] left one position\n        for (int k = i; k < n-1; k++)\n            a[(j+k)%a.length] = a[(j+k+1)%a.length];\n    }\n    n--;\n    if (3*n < a.length) resize();\n    return x;\n}\n\nvoid resize() {\n    array<T> b(max(1, 2*n));\n    for (int k = 0; k < n; k++)\n        b[k] = a[(j+k)%a.length];\n    a = b;\n    j = 0;\n}";
  /* END ODS LISTINGS ARRAYDEQUE */
  /* JavaScript: the AI's translation of ODS's Java, line for line (Java's integer n/2 as Math.floor) */
  const JS = [
    'add(i, x) {',
    '    if (this.n+1 > this.a.length) this.resize();',
    '    if (i < Math.floor(this.n/2)) { // shift a[0],..,a[i-1] left one position',
    '        this.j = (this.j == 0) ? this.a.length - 1 : this.j - 1; //(j-1)mod a.length',
    '        for (let k = 0; k <= i-1; k++)',
    '            this.a[(this.j+k)%this.a.length] = this.a[(this.j+k+1)%this.a.length];',
    '    } else { // shift a[i],..,a[n-1] right one position',
    '        for (let k = this.n; k > i; k--)',
    '            this.a[(this.j+k)%this.a.length] = this.a[(this.j+k-1)%this.a.length];',
    '    }',
    '    this.a[(this.j+i)%this.a.length] = x;',
    '    this.n++;',
    '}',
    '',
    'remove(i) {',
    '    const x = this.a[(this.j+i)%this.a.length];',
    '    if (i < Math.floor(this.n/2)) {  // shift a[0],..,[i-1] right one position',
    '        for (let k = i; k > 0; k--)',
    '            this.a[(this.j+k)%this.a.length] = this.a[(this.j+k-1)%this.a.length];',
    '        this.j = (this.j + 1) % this.a.length;',
    '    } else { // shift a[i+1],..,a[n-1] left one position',
    '        for (let k = i; k < this.n-1; k++)',
    '            this.a[(this.j+k)%this.a.length] = this.a[(this.j+k+1)%this.a.length];',
    '    }',
    '    this.n--;',
    '    if (3*this.n < this.a.length) this.resize();',
    '    return x;',
    '}',
    '',
    'resize() {',
    '    const b = new Array(Math.max(2*this.n, 1));',
    '    for (let k = 0; k < this.n; k++)',
    '        b[k] = this.a[(this.j+k) % this.a.length];',
    '    this.a = b;',
    '    this.j = 0;',
    '}',
  ].join('\n');
  /* Python line → the braced languages' line (Java, C++ and the JavaScript share one layout) */
  const BRACED = { 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 11, 11: 12, 13: 15, 14: 16, 15: 17, 16: 18, 17: 19,
    18: 20, 19: 21, 20: 22, 21: 23, 22: 25, 23: 26, 24: 27, 26: 30, 27: 31, 28: 32, 29: 33, 30: 34, 31: 35 };
  const MAP = { java: BRACED, cpp: BRACED, javascript: BRACED };
  /* Python's lines: add 1–11, remove 13–24, _resize 26–31 */
  const L = { defAdd: 1, grow: 2, jback: 4, shl: 6, forR: 8, shr: 9, store: 10, count: 11, start: 12, defRem: 13, take: 14,
    shrl: 17, jfwd: 18, forRR: 20, shrr: 21, dec: 22, shrink: 23, ret: 24, defRes: 26, alloc: 27, forC: 28, copy: 29, setA: 30, setJ: 31 };

  /* The inputs. ODS's Figure 2.3 starts from a…h at j = 0 in an array of 12. The Deque's four operations are add(0, x),
     add(n, x), remove(0) and remove(n − 1), resolved against n when the call is made. */
  const ring = (len, j, vals) => { const a = new Array(len).fill(null); vals.forEach((v, k) => { a[(j + k) % len] = v; }); return a; };
  const PRESETS = [
    { value: 'figure', label: 'Figure 2.3', a: ring(12, 0, LET.slice(0, 8)), j: 0, n: 8,
      ops: [['remove', 2], ['add', 4, 'x'], ['add', 3, 'y'], ['add', 4, 'z']] },
    { value: 'ends', label: 'at both ends', a: ring(8, 0, LET.slice(0, 5)), j: 0, n: 5,
      ops: [['addFirst', 'p'], ['addLast', 'q'], ['removeFirst'], ['removeLast'], ['addFirst', 'r'], ['addFirst', 's'], ['removeLast']] },
    { value: 'middle', label: 'in the middle', a: ring(16, 13, LET.slice(0, 6)), j: 13, n: 6,
      ops: 'stuvwxyz'.split('').map((x) => ['addMiddle', x]) },
    { value: 'grow', label: 'grow from a wrapped start', a: ring(8, 5, LET.slice(0, 6)), j: 5, n: 6,
      ops: [['addLast', 'g'], ['addLast', 'h'], ['addLast', 'i'], ['addFirst', 'z']] },
  ];
  /* a Deque operation as the add or remove call it makes on a list of n elements */
  const resolve = (o, n) => {
    if (o[0] === 'addFirst') return ['add', 0, o[1]];
    if (o[0] === 'addLast') return ['add', n, o[1]];
    if (o[0] === 'addMiddle') return ['add', Math.ceil(n / 2), o[1]];
    if (o[0] === 'removeFirst') return ['remove', 0];
    if (o[0] === 'removeLast') return ['remove', n - 1];
    return o;
  };
  const callName = (o) => (o[0] === 'remove' ? `remove(${o[1]})` : `add(${o[1]}, ${o[2]})`);

  /* One run of a preset as frames of the Python. Beside the code's own variables (i, x, j, n, len(a), a, b) each
     frame carries what the drawing reads: the call under way (k) and every call resolved (calls), the side shifted
     (side), the copy just made (mv: [from slot, to slot, row]), this call's copies (moves), the shifts this call made
     (sh) and its bound min(i, n − i) (bound), and the totals: shifts, copies by resize(), calls m, resizes r. */
  const run = (P) => {
    /* the calls as they resolve against n, found by a dry run first so the call row can name them all */
    const calls = []; { let n = P.n; P.ops.forEach((o) => { const c = resolve(o, n); calls.push(c); n += c[0] === 'add' ? 1 : -1; }); }
    return { calls, trace: F.trace((at) => {
      let a = P.a.slice(), j = P.j, n = P.n, b = null;
      let k = -1, m = 0, r = 0, shifts = 0, copies = 0, sh = 0, bound = 0, side = null, moves = [];
      let i = null, x = null;
      const stars = [];
      const snap = (extra) => Object.assign({ i, x, j, n, 'len(a)': a.length, a: a.slice(), k, side, sh, bound, shifts, copies, m, r,
        moves: moves.map((mv) => mv.slice()), stars: stars.slice() }, b ? { b: b.slice() } : {}, extra || {});
      const resize = () => {
        at.enter('_resize');
        at(L.defRes, snap());
        b = new Array(Math.max(1, 2 * n)).fill(null); at(L.alloc, snap());
        if (!n) at(L.forC, snap());
        for (let q = 0; q < n; q += 1) {
          const from = (j + q) % a.length; b[q] = a[from]; copies += 1; moves.push([from, q, 'b']);
          at(L.copy, snap({ mv: [from, q, 'b'] }), ['copy', from, q]);
        }
        r += 1; stars.push(k);
        a = b; b = null; at(L.setA, snap({ swapped: true }));
        j = 0; at(L.setJ, snap({ swapped: true }));
        at.leave();
      };
      at(L.start, snap());
      calls.forEach((o, kk) => {
        k = kk; moves = []; sh = 0; side = null; m += 1;
        i = o[1];
        bound = Math.min(i, n - i);
        if (o[0] === 'add') {
          x = o[2];
          at(L.defAdd, snap());
          if (n === a.length) resize();
          at(L.grow, snap());
          const len = a.length;
          if (i < n / 2) {
            side = 'left';
            j = (j - 1 + len) % len; at(L.jback, snap());
            for (let q = 0; q < i; q += 1) {
              const to = (j + q) % len, from = (j + q + 1) % len;
              a[to] = a[from]; sh += 1; shifts += 1; moves.push([from, to, 'a']);
              at(L.shl, snap({ mv: [from, to, 'a'] }), ['shift', from, to]);
            }
          } else {
            side = 'right';
            if (n === i) at(L.forR, snap());
            for (let q = n; q > i; q -= 1) {
              const to = (j + q) % len, from = (j + q - 1) % len;
              a[to] = a[from]; sh += 1; shifts += 1; moves.push([from, to, 'a']);
              at(L.shr, snap({ mv: [from, to, 'a'] }), ['shift', from, to]);
            }
          }
          a[(j + i) % len] = x; at(L.store, snap({ put: (j + i) % len }), ['put', (j + i) % len]);
          n += 1; at(L.count, snap());
        } else {
          x = null;
          at(L.defRem, snap());
          const len = a.length;
          x = a[(j + i) % len]; at(L.take, snap({ took: (j + i) % len }));
          if (i < n / 2) {
            side = 'left';
            for (let q = i; q > 0; q -= 1) {
              const to = (j + q) % len, from = (j + q - 1) % len;
              a[to] = a[from]; sh += 1; shifts += 1; moves.push([from, to, 'a']);
              at(L.shrl, snap({ mv: [from, to, 'a'] }), ['shift', from, to]);
            }
            j = (j + 1) % len; at(L.jfwd, snap());
          } else {
            side = 'right';
            if (i === n - 1) at(L.forRR, snap());
            for (let q = i; q < n - 1; q += 1) {
              const to = (j + q) % len, from = (j + q + 1) % len;
              a[to] = a[from]; sh += 1; shifts += 1; moves.push([from, to, 'a']);
              at(L.shrr, snap({ mv: [from, to, 'a'] }), ['shift', from, to]);
            }
          }
          n -= 1; at(L.dec, snap());
          if (a.length >= 3 * n) resize();
          at(L.shrink, snap());
          at(L.ret, snap());
        }
      });
    }) };
  };

  const d = sim('sim-arraydeque', 770);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: { javascript: AI }, lineMap: MAP,
    blocks: [
      { id: 'add', lines: [1, 11], label: 'add(i, x)', touches: ['a', 'i', 'x', 'j', 'n'] },
      { id: 'grow', lines: [2, 2], label: 'resize a if it is full', touches: ['a', 'n'] },
      { id: 'left', lines: [4, 6], label: 'i < n/2: step j back and shift the first i elements left', touches: ['a', 'j'] },
      { id: 'shl', lines: [6, 6], label: 'copy one element a cell to the left', touches: ['a'] },
      { id: 'right', lines: [8, 9], label: 'otherwise shift a[i], …, a[n − 1] a cell to the right', touches: ['a'] },
      { id: 'shr', lines: [9, 9], label: 'copy one element a cell to the right', touches: ['a'] },
      { id: 'store', lines: [10, 11], label: 'store x at list position i and count it', touches: ['a', 'x', 'n'] },
      { id: 'remove', lines: [13, 24], label: 'remove(i)', touches: ['a', 'i', 'x', 'j', 'n'] },
      { id: 'take', lines: [14, 14], label: 'read x at list position i', touches: ['a', 'x'] },
      { id: 'rl', lines: [16, 18], label: 'i < n/2: shift the first i elements right and step j forward', touches: ['a', 'j'] },
      { id: 'shrl', lines: [17, 17], label: 'copy one element a cell to the right', touches: ['a'] },
      { id: 'rr', lines: [20, 21], label: 'otherwise shift a[i + 1], …, a[n − 1] a cell to the left', touches: ['a'] },
      { id: 'shrr', lines: [21, 21], label: 'copy one element a cell to the left', touches: ['a'] },
      { id: 'shrink', lines: [22, 24], label: 'count it, shrink a if length(a) ≥ 3n, and return x', touches: ['a', 'n'] },
      { id: 'resize', lines: [26, 31], label: 'resize(): copy the list, from a[j] on, into the start of an array of 2n', touches: ['a', 'b', 'j'] },
      { id: 'alloc', lines: [27, 27], label: 'allocate b of length 2n', touches: ['b'] },
      { id: 'copy', lines: [29, 29], label: 'copy one element into b', touches: ['b'] },
      { id: 'swap', lines: [30, 31], label: 'b becomes a, and j = 0', touches: ['a', 'b', 'j'] },
    ],
    refs: { 'self.a': () => F.ref('a'), a: () => F.ref('a'), b: () => F.ref('b'), i: () => F.ref('i'),
      'self.j': () => F.ref('j'), j: () => F.ref('j'), 'self.n': () => F.ref('n'), n: () => F.ref('n') },
  });

  const runs = Object.fromEntries(PRESETS.map((P) => [P.value, run(P)]));
  const tip = { hits: [] };

  F.debug(d, {
    code, watch: ['i', 'x', 'j', 'n', 'len(a)'],
    inputs: PRESETS.map((P) => ({ value: P.value, label: P.label, trace: runs[P.value].trace })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const R = runs[g.input] || runs.figure;
      const v = g.frame.vars, pv = g.prev.vars, k = g.k, ln = g.frame.line;
      const ca = F.ref('a'), cb = F.ref('b'), ci = F.ref('i'), cj = F.ref('j'), cn = F.ref('n');
      const key = C('key'), size = C('size'), cost = C('cost'), idx = C('index'), ink = PAL.ink, muted = PAL.muted;
      const hits = [];
      const op = v.k >= 0 ? R.calls[v.k] : null;
      const inResize = ln === L.defRes || ln === L.alloc || ln === L.forC || ln === L.copy;
      const swapping = ln === L.setA || ln === L.setJ;
      const len = v['len(a)'];

      /* ---------------- the headline: the call, the side it shifts, and what moved */
      let head;
      const plural = (c, w) => `${c || 'no'} element${c === 1 ? '' : 's'}${w ? ' ' + w : ''}`;
      if (!op) head = `The list holds n = ${v.n} elements, list position 0 at a[j], j = ${v.j}, in an array of length ${len}.`;
      else if (inResize || swapping) {
        head = swapping ? `resize() has copied the list into the start of b, which becomes a; now j = ${v.j}.`
          : op[0] === 'add' ? `a is full, so ${callName(op)} first calls resize(): ${plural(v.n)} copied, from a[j] on, into an array of ${Math.max(1, 2 * v.n)}.`
            : `length(a) = ${len} ≥ 3n = ${3 * v.n}, so ${callName(op)} calls resize(): ${plural(v.n)} into an array of ${Math.max(1, 2 * v.n)}.`;
      } else {
        const n0 = op[0] === 'add' ? (ln >= L.count ? v.n - 1 : v.n) : (ln >= L.dec && ln <= L.ret ? v.n + 1 : v.n);
        const half = num(n0 / 2), lt = op[1] < n0 / 2;
        const test = `i = ${op[1]} ${lt ? '<' : '≥'} n/2 = ${half}`;
        if (op[0] === 'add') {
          head = lt ? `${callName(op)}: ${test}, so j steps back to ${v.j} and ${plural(op[1], 'shift')} left before x goes in.`
            : `${callName(op)}: ${test}, so ${plural(n0 - op[1], 'shift')} right to make room for x.`;
        } else {
          head = lt ? `${callName(op)}: ${test}, so ${plural(op[1], 'shift')} right over the gap and j steps forward.`
            : `${callName(op)}: ${test}, so ${plural(n0 - op[1] - 1, 'shift')} left over the gap.`;
        }
      }
      const lines = topline(ctx, head) || 1;

      /* ---------------- the calls */
      const top = callRow(ctx, R.calls.map(callName), v.k, v.stars, hits, lines > 1 ? 140 : 112);

      /* ---------------- the circular array: live cells shaded in the index tint, each with its list position in its
         corner; slot numbers under the cells; while resize() runs, b below a; on the swap b rises into a's place */
      const ROWA = top + 230, ROWB = ROWA + 180, CH = 84;
      const layout = (cells, y) => { const cw = Math.min(80, 1240 / cells), x0 = 700 - (cw * cells) / 2; return { cw, x0, x1: x0 + cw * cells, y, x: (q) => x0 + q * cw + cw / 2 }; };
      const live = (jj, nn, cells, q) => ((q - jj + cells) % cells) < nn;
      const cellRow = (Lr, vals, jj, nn, name, color, op = 1) => {
        ctx.save(); ctx.globalAlpha *= op;
        vals.forEach((val, q) => {
          const on = live(jj, nn, vals.length, q), x = Lr.x0 + q * Lr.cw;
          if (on) ctx.fillStyle = alpha(idx, 0.18), ctx.fillRect(x, Lr.y - CH / 2 - 6, Lr.cw, CH + 12);
          rect(ctx, x + 2, Lr.y - CH / 2, Lr.cw - 4, CH, PAL.panel, on ? ink : alpha(ink, 0.35), on ? 2.5 : 2);
          if (on) {
            text(ctx, String(val), Lr.x(q), Lr.y + 10, key, { size: 34, align: 'center', base: 'middle', weight: 600 });
            text(ctx, String((q - jj + vals.length) % vals.length), x + 8, Lr.y - CH / 2 + 18, idx, { size: 26, base: 'middle' });
          }
          text(ctx, String(q), Lr.x(q), Lr.y + CH / 2 + 24, muted, { size: 26, align: 'center', base: 'middle' });
          const lp = (q - jj + vals.length) % vals.length;
          hits.push({ x: Lr.x(q), y: Lr.y, r: Lr.cw / 2, name: on ? `${name}[${q}] = ${val}, list position ${lp}` : `${name}[${q}], not in the list` });
        });
        text(ctx, name, Lr.x0 - 26, Lr.y, color, { size: 34, weight: 600, align: 'right', base: 'middle', italic: true });
        ctx.restore();
      };
      const La = layout(len, ROWA);
      const swapK = ln === L.setA ? (g.prev.line === L.setA ? 1 : k) : (ln === L.setJ ? 1 : 0);
      if (inResize) {
        cellRow(La, v.a, v.j, v.n, 'a', ca);
        const Lb = layout(v.b.length, ROWB);
        const nb = v.moves.filter((mv) => mv[2] === 'b').length;
        cellRow(Lb, v.b, 0, nb, 'b', cb, ln === L.alloc && g.prev.line !== L.alloc ? k : 1);
        v.moves.filter((mv) => mv[2] === 'b').forEach((mv) => {
          const cur = v.mv && v.mv[0] === mv[0] && v.mv[2] === 'b';
          const t = cur && !(pv.mv && pv.mv[0] === mv[0] && pv.mv[2] === 'b') ? k : 1;
          const x0 = La.x(mv[0]), x1 = Lb.x(mv[1]), y0 = ROWA + CH / 2 + 44, y1 = ROWB - CH / 2 - 6;
          if (cur) arrow(ctx, x0, y0, lerp(x0, x1, Math.max(0.2, t)), lerp(y0, y1, Math.max(0.2, t)), cb, 5);
          else line(ctx, x0, y0, x1, y1, alpha(cb, 0.35), 3);
        });
      } else if (swapping) {
        /* the old a fades; b rises into its place */
        if (swapK < 1 && pv.a && pv.b) {
          const Lo = layout(pv.a.length, ROWA);
          cellRow(Lo, pv.a, pv.j, v.n, 'a', ca, 1 - swapK);
          const Ln = layout(len, lerp(ROWB, ROWA, swapK));
          cellRow(Ln, v.a, 0, v.n, swapK > 0.5 ? 'a' : 'b', swapK > 0.5 ? ca : cb, 1);
        } else cellRow(La, v.a, v.j, v.n, 'a', ca);
      } else {
        cellRow(La, v.a, v.j, v.n, 'a', ca);
        /* the copies this call made within a: an arc from each element's old cell to its new one, the last one drawn
           as it moves; at rest every arc of the call stays, as Figure 2.3 draws them. A copy round the end of the
           array (cell 0 to the last cell, or back) arcs over the whole row. */
        v.moves.filter((mv) => mv[2] === 'a').forEach((mv) => {
          const cur = v.mv && v.mv[0] === mv[0] && v.mv[1] === mv[1] && v.mv[2] === 'a';
          const fresh = cur && !(pv.mv && pv.mv[0] === mv[0] && pv.mv[1] === mv[1]);
          const x0 = La.x(mv[0]), x1 = La.x(mv[1]), y = ROWA - CH / 2 - 8;
          const lift = Math.abs(mv[1] - mv[0]) > 1 ? 90 : 34;
          if (fresh) partArc(ctx, x0, y, x1, y, lift, Math.max(0.2, k), ci, 4);
          else curve(ctx, x0, y, x1, y, lift, cur ? ci : alpha(ci, 0.45), cur ? 4 : 3);
        });
        if (v.took !== undefined && ln === L.take) rect(ctx, La.x0 + v.took * La.cw + 2, ROWA - CH / 2, La.cw - 4, CH, null, ci, 5);
        if (v.put !== undefined && ln === L.store) rect(ctx, La.x0 + v.put * La.cw + 2, ROWA - CH / 2, La.cw - 4, CH, null, ci, 5);
      }

      /* ---------------- the pointers: j under its cell (it eases one cell at a time, and jumps when it wraps); i over
         the cell of list position i while a call runs */
      if (!inResize && (!swapping || swapK >= 1)) {
        const pj = pv.j, jj = (pj !== undefined && Math.abs(pj - v.j) === 1 && pv['len(a)'] === len) ? lerp(pj, v.j, k) : v.j;
        const xj = La.x0 + (jj + 0.5) * La.cw, yb = ROWA + CH / 2 + 54;
        arrow(ctx, xj, yb + 52, xj, yb, cj, 4);
        text(ctx, `j = ${v.j}`, xj, yb + 76, cj, { size: 30, weight: 600, align: 'center', base: 'middle' });
        if (op && v.i !== null && v.i !== undefined && ln !== L.ret) {
          const nn = op[0] === 'add' && ln >= L.store ? v.n : v.n;
          const q = (v.j + Math.min(v.i, Math.max(0, nn))) % len, xi = La.x(q), yt = ROWA - CH / 2 - (v.moves.some((mv) => mv[2] === 'a' && Math.abs(mv[1] - mv[0]) > 1) ? 110 : 64);
          arrow(ctx, xi, yt - 44, xi, yt, ci, 4);
          text(ctx, `i = ${v.i}`, xi, yt - 64, ci, { size: 30, weight: 600, align: 'center', base: 'middle' });
        }
      }

      /* ---------------- the counts: where the list lives, the call's shifts against min(i, n − i), the totals */
      const Y0 = ROWB + 96;
      seg(ctx, [['list position k sits at ', ink], ['a', ca, { weight: 600, italic: true }], ['[(', ink], ['j', cj, { weight: 600, italic: true }],
        [' + k) mod length(', ink], ['a', ca, { weight: 600, italic: true }], [')]  ·  ', ink], ['j', cj, { weight: 600, italic: true }],
        [` = ${v.j}  ·  `, ink], ['n', cn, { weight: 600, italic: true }], [` = ${v.n}  ·  `, ink], [`length(a) = ${len}`, size]], Y0);
      if (op) seg(ctx, [[`${callName(op)} shifted `, PAL.ink], [String(v.sh), cost], [` ≤ min(i, n − i) = ${v.bound}`, PAL.ink]], Y0 + 44);
      seg(ctx, [['all calls: ', PAL.ink], [String(v.shifts), cost], [' shifted, ', PAL.ink], [String(v.copies), cost], [' copied by resize()', PAL.ink]], Y0 + 88);
      tip.hits = hits;
    },
  });
  F.hover(d.stage, () => tip.hits, d.c);
})();

/* ================================================================ sim-dualarraydeque */
(function () {
  /* BEGIN ODS LISTINGS DUAL (ch03/3.3/inline_code.py) */
  const PY = "def add(self, i, x):\n    if i < self.front.size():\n        self.front.add(self.front.size()-i, x)\n    else:\n        self.back.add(i-self.front.size(), x)\n    self._balance()\n\ndef remove(self, i):\n    if i < self.front.size():\n        x = self.front.remove(self.front.size()-i-1)\n    else:\n        x = self.back.remove(i-self.front.size())\n    self._balance()\n    return x\n\ndef _balance(self):\n    n = self.size()\n    mid = n//2\n    if 3*self.front.size() < self.back.size() or 3*self.back.size() < self.front.size():\n        f = ArrayStack()\n        for i in range(mid):\n            f.add(i, self.get(mid-i-1))\n        b = ArrayStack()\n        for i in range(n-mid):\n            b.add(i, self.get(mid+i))\n        self.front = f\n        self.back = b";
  const JAVA = "void add(int i, T x) {\n    if (i < front.size()) {\n        front.add(front.size()-i, x);\n    } else {\n        back.add(i-front.size(), x);\n    }\n    balance();\n}\n\nT remove(int i) {\n    T x;\n    if (i < front.size()) {\n        x = front.remove(front.size()-i-1);\n    } else {\n        x = back.remove(i-front.size());\n    }\n    balance();\n    return x;\n}\n\nvoid balance() {\n    int n = size();\n    if (3*front.size() < back.size()) {\n        int s = n/2 - front.size();\n        List<T> l1 = newStack();\n        List<T> l2 = newStack();\n        l1.addAll(back.subList(0,s));\n        Collections.reverse(l1);\n        l1.addAll(front);\n        l2.addAll(back.subList(s, back.size()));\n        front = l1;\n        back = l2;\n    } else if (3*back.size() < front.size()) {\n        int s = front.size() - n/2;\n        List<T> l1 = newStack();\n        List<T> l2 = newStack();\n        l1.addAll(front.subList(s, front.size()));\n        l2.addAll(front.subList(0, s));\n        Collections.reverse(l2);\n        l2.addAll(back);\n        front = l1;\n        back = l2;\n    }\n}";
  const CPP = "void add(int i, T x) {\n    if (i < front.size()) {\n        front.add(front.size() - i, x);\n    } else {\n        back.add(i - front.size(), x);\n    }\n    balance();\n}\n\nT remove(int i) {\n    T x;\n    if (i < front.size()) {\n            x = front.remove(front.size()-i-1);\n    } else {\n            x = back.remove(i-front.size());\n    }\n    balance();\n    return x;\n}\n\nvoid balance() {\n    if (3*front.size() < back.size()\n            || 3*back.size() < front.size()) {\n        int n = front.size() + back.size();\n        int nf = n/2;\n        array<T> af(max(2*nf, 1));\n        for (int i = 0; i < nf; i++) {\n            af[nf-i-1] = get(i);\n        }\n        int nb = n - nf;\n        array<T> ab(max(2*nb, 1));\n        for (int i = 0; i < nb; i++) {\n            ab[i] = get(nf+i);\n        }\n        front.a = af;\n        front.n = nf;\n        back.a = ab;\n        back.n = nb;\n    }\n}";
  /* END ODS LISTINGS DUAL */
  /* JavaScript: the AI's translation of ODS's Java (add, remove) and of its C++ (balance(), which in Java leans on
     java.util's List), line for line */
  const JS = [
    'add(i, x) {',
    '    if (i < this.front.size()) {',
    '        this.front.add(this.front.size()-i, x);',
    '    } else {',
    '        this.back.add(i-this.front.size(), x);',
    '    }',
    '    this.balance();',
    '}',
    '',
    'remove(i) {',
    '    let x;',
    '    if (i < this.front.size()) {',
    '        x = this.front.remove(this.front.size()-i-1);',
    '    } else {',
    '        x = this.back.remove(i-this.front.size());',
    '    }',
    '    this.balance();',
    '    return x;',
    '}',
    '',
    'balance() {',
    '    if (3*this.front.size() < this.back.size()',
    '            || 3*this.back.size() < this.front.size()) {',
    '        const n = this.front.size() + this.back.size();',
    '        const nf = Math.floor(n/2);',
    '        const af = new Array(Math.max(2*nf, 1));',
    '        for (let i = 0; i < nf; i++) {',
    '            af[nf-i-1] = this.get(i);',
    '        }',
    '        const nb = n - nf;',
    '        const ab = new Array(Math.max(2*nb, 1));',
    '        for (let i = 0; i < nb; i++) {',
    '            ab[i] = this.get(nf+i);',
    '        }',
    '        this.front.a = af;',
    '        this.front.n = nf;',
    '        this.back.a = ab;',
    '        this.back.n = nb;',
    '    }',
    '}',
  ].join('\n');
  /* Python line → line(s): add and remove share one layout in every language; balance() follows the C++ (and the
     JavaScript made from it) line for line, and the Java, which is written differently, as nearly as its lines allow */
  const HEAD = { 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 7, 8: 10, 9: 12, 10: 13, 11: 14, 12: 15, 13: 17, 14: 18 };
  const CBAL = { 16: 21, 17: 24, 18: 25, 19: [22, 23], 20: 26, 21: 27, 22: 28, 23: 31, 24: 32, 25: 33, 26: [35, 36], 27: [37, 38] };
  const JBAL = { 16: 21, 17: 22, 18: 22, 19: [23, 33], 20: [25, 26, 35, 36], 21: [27, 37], 22: [27, 28, 29, 37, 38, 39], 23: [30, 40],
    24: [30, 40], 25: [30, 40], 26: [31, 41], 27: [32, 42] };
  const MAP = { java: { ...HEAD, ...JBAL }, cpp: { ...HEAD, ...CBAL }, javascript: { ...HEAD, ...CBAL } };
  const L = { defAdd: 1, toFront: 3, toBack: 5, bal: 6, start: 7, defRem: 8, fromFront: 10, fromBack: 12, balr: 13, ret: 14,
    n: 17, mid: 18, test: 19, newF: 20, copyF: 22, newB: 23, copyB: 25, setF: 26, setB: 27 };

  /* The inputs. ODS's Figure 2.4 starts with a, b in front (stored b, a: front's index 0 is list position 1) and c, d in
     back. A stack's array holds its elements from its index 0, which stands next to the middle. */
  const PRESETS = [
    { value: 'figure', label: 'Figure 2.4', front: ['b', 'a'], back: ['c', 'd'], ops: [['add', 3, 'x'], ['add', 4, 'y'], ['remove', 0]] },
    { value: 'back', label: 'add at the back', front: [], back: [], ops: LET.slice(0, 12).map((x) => ['addLast', x]) },
    { value: 'front', label: 'add at the front', front: [], back: [], ops: LET.slice(0, 12).map((x) => ['addFirst', x]) },
    { value: 'drain', label: 'drain the front', front: ['d', 'c', 'b', 'a'], back: ['e', 'f', 'g', 'h'], ops: Array.from({ length: 6 }, () => ['removeFirst']) },
    { value: 'alternate', label: 'alternate ends', front: ['b', 'a'], back: ['c', 'd'],
      ops: ['p', 'q', 'r', 's', 't', 'u'].map((x, q) => [q % 2 ? 'addLast' : 'addFirst', x]) },
  ];
  const resolve = (o, n) => {
    if (o[0] === 'addFirst') return ['add', 0, o[1]];
    if (o[0] === 'addLast') return ['add', n, o[1]];
    if (o[0] === 'removeFirst') return ['remove', 0];
    return o;
  };
  const callName = (o) => (o[0] === 'remove' ? `remove(${o[1]})` : `add(${o[1]}, ${o[2]})`);
  /* where list position p lives: front's index fs − 1 − p, or back's index p − fs */
  const where = (fs, p) => (p < fs ? ['front', fs - 1 - p] : ['back', p - fs]);

  /* One run as frames of the Python. Beside i, x and the two stacks (front, back, as arrays from their index 0) each
     frame carries the call (k), the stack it touched (side) and the copies inside that stack (moves: [from, to]), the
     stacks balance() is building (f, b) and its copies (bmoves: [stack, index] → [new stack, index]), and the counts:
     Φ, Φ₀ (Φ just after the last balance, or at the start), the calls since then (since), elements copied by
     balance() (copied), calls m and balances r. */
  const run = (P) => {
    const calls = []; { let n = P.front.length + P.back.length; P.ops.forEach((o) => { const c = resolve(o, n); calls.push(c); n += c[0] === 'add' ? 1 : -1; }); }
    return { calls, trace: F.trace((at) => {
      let front = P.front.slice(), back = P.back.slice(), f = null, b = null;
      let k = -1, side = null, moves = [], bmoves = [], m = 0, r = 0, copied = 0, since = 0, mid = null, nn = null;
      let phi0 = Math.abs(front.length - back.length);
      let i = null, x = null;
      const stars = [];
      const phi = () => Math.abs(front.length - back.length);
      const snap = (extra) => Object.assign({ i, x, 'front.size()': front.length, 'back.size()': back.length, front: front.slice(), back: back.slice(),
        k, side, moves: moves.map((q) => q.slice()), bmoves: bmoves.map((q) => q.slice()), m, r, copied, since, phi: phi(), phi0, stars: stars.slice() },
      f ? { f: f.slice() } : {}, b ? { b: b.slice() } : {}, mid !== null ? { mid, n: nn } : {}, extra || {});
      const list = () => front.slice().reverse().concat(back);
      const balance = () => {
        if (!(3 * front.length < back.length || 3 * back.length < front.length)) return;
        at.enter('_balance');
        nn = front.length + back.length; at(L.n, snap());
        mid = Math.floor(nn / 2); at(L.mid, snap());
        at(L.test, snap({ phi1: phi(), firing: true }), ['test']);
        const lst = list();
        f = []; at(L.newF, snap());
        for (let q = 0; q < mid; q += 1) {
          const p = mid - q - 1; f.push(lst[p]); copied += 1; bmoves.push([...where(front.length, p), 'f', q]);
          at(L.copyF, snap({ mv: bmoves[bmoves.length - 1] }), ['copy', p]);
        }
        b = []; at(L.newB, snap());
        for (let q = 0; q < nn - mid; q += 1) {
          const p = mid + q; b.push(lst[p]); copied += 1; bmoves.push([...where(front.length, p), 'b', q]);
          at(L.copyB, snap({ mv: bmoves[bmoves.length - 1] }), ['copy', p]);
        }
        const fresh = { f: f.slice(), b: b.slice() };
        front = f; f = null; at(L.setF, snap({ swapped: true, fresh }));
        back = b; b = null;
        r += 1; stars.push(k); since = 0; phi0 = phi();
        at(L.setB, snap({ swapped: true, fresh }));
        mid = null; nn = null;
        at.leave();
      };
      at(L.start, snap());
      calls.forEach((o, kk) => {
        k = kk; moves = []; bmoves = []; side = null; m += 1; since += 1;
        i = o[1];
        if (o[0] === 'add') {
          x = o[2];
          at(L.defAdd, snap());
          if (i < front.length) {
            const p = front.length - i; side = 'front';
            for (let q = front.length - 1; q >= p; q -= 1) moves.push([q, q + 1]);
            front.splice(p, 0, x); at(L.toFront, snap({ put: ['front', p] }), ['put']);
          } else {
            const p = i - front.length; side = 'back';
            for (let q = back.length - 1; q >= p; q -= 1) moves.push([q, q + 1]);
            back.splice(p, 0, x); at(L.toBack, snap({ put: ['back', p] }), ['put']);
          }
          balance();
          at(L.bal, snap());
        } else {
          x = null;
          at(L.defRem, snap());
          if (i < front.length) {
            const p = front.length - i - 1; side = 'front'; x = front[p];
            for (let q = p + 1; q < front.length; q += 1) moves.push([q, q - 1]);
            front.splice(p, 1); at(L.fromFront, snap({ took: ['front', p] }), ['take']);
          } else {
            const p = i - front.length; side = 'back'; x = back[p];
            for (let q = p + 1; q < back.length; q += 1) moves.push([q, q - 1]);
            back.splice(p, 1); at(L.fromBack, snap({ took: ['back', p] }), ['take']);
          }
          balance();
          at(L.balr, snap());
          at(L.ret, snap());
        }
      });
    }) };
  };

  const d = sim('sim-dualarraydeque', 830);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: { javascript: AI }, lineMap: MAP,
    blocks: [
      { id: 'add', lines: [1, 6], label: 'add(i, x)', touches: ['front', 'back', 'i', 'x'] },
      { id: 'pick', lines: [2, 5], label: 'add x to front or to back, wherever list position i lives', touches: ['front', 'back', 'i', 'x'] },
      { id: 'bal', lines: [6, 6], label: 'balance()', touches: ['front', 'back'] },
      { id: 'remove', lines: [8, 14], label: 'remove(i)', touches: ['front', 'back', 'i', 'x'] },
      { id: 'pickr', lines: [9, 12], label: 'remove list position i from front or from back', touches: ['front', 'back', 'i', 'x'] },
      { id: 'balr', lines: [13, 14], label: 'balance(), then return x', touches: ['front', 'back'] },
      { id: 'balance', lines: [16, 27], label: 'balance(): rebuild both stacks around the middle', touches: ['front', 'back'] },
      { id: 'test', lines: { python: [17, 19], java: [22, 23] }, label: 'one stack holds more than three times the other', touches: ['front', 'back'] },
      { id: 'ff', lines: { python: [22, 22], java: [27, 29] }, label: 'copy list position mid − i − 1 into the new front', touches: ['f'] },
      { id: 'bb', lines: { python: [25, 25], java: [30, 30] }, label: 'copy list position mid + i into the new back', touches: ['b'] },
      { id: 'swap', lines: { python: [26, 27], java: [31, 32] }, label: 'the new stacks replace front and back', touches: ['front', 'back'] },
    ],
    refs: { 'self.front': () => F.ref('front'), front: () => F.ref('front'), 'self.back': () => F.ref('back'), back: () => F.ref('back'),
      i: () => F.ref('i'), n: () => F.ref('n') },
  });

  const runs = Object.fromEntries(PRESETS.map((P) => [P.value, run(P)]));
  /* the slots each half draws: the most either stack, old or new, holds in any run, and one more */
  const SLOTS_OF = Object.fromEntries(Object.entries(runs).map(([key, R]) => [key, Math.max(5, ...R.trace.map((fr) => Math.max(fr.vars.front.length,
    fr.vars.back.length, (fr.vars.f || []).length, (fr.vars.b || []).length) + 1))]));
  const tip = { hits: [] };

  F.debug(d, {
    code, watch: ['i', 'x', 'front.size()', 'back.size()'],
    inputs: PRESETS.map((P) => ({ value: P.value, label: P.label, trace: runs[P.value].trace })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const R = runs[g.input] || runs.figure;
      const v = g.frame.vars, pv = g.prev.vars, k = g.k, ln = g.frame.line;
      const cf = F.ref('front'), cbk = F.ref('back'), ci = F.ref('i'), cn = F.ref('n');
      const key = C('key'), cost = C('cost'), idx = C('index'), ink = PAL.ink, muted = PAL.muted, bad = PAL.bad || ink;
      const hits = [];
      const op = v.k >= 0 ? R.calls[v.k] : null;
      const fs = v['front.size()'], bs = v['back.size()'], n = fs + bs, SLOTS = SLOTS_OF[g.input] || SLOTS_OF.figure;
      const inBal = ln >= L.n && ln <= L.copyB;
      const swapping = ln === L.setF || ln === L.setB;

      /* ---------------- the headline */
      let head;
      if (!op) head = n ? `front holds list positions 0 to ${fs - 1} in reverse order and back holds ${fs} to ${n - 1}.` : 'An empty DualArrayDeque: both stacks are empty.';
      else if (ln === L.n || ln === L.mid || ln === L.test) {
        const big = 3 * fs < bs ? `3·front.size() = ${3 * fs} < back.size() = ${bs}` : `3·back.size() = ${3 * bs} < front.size() = ${fs}`;
        head = `${big}, so balance() rebuilds both stacks; Φ₁ = ${v.phi} ${v.phi > n / 2 ? '>' : '≤'} n/2 = ${num(n / 2)}.`;
      } else if (inBal || ln === L.newF || ln === L.newB) head = `balance() copies list positions ${v.mid - 1 >= 0 ? `${v.mid - 1} down to 0` : 'none'} into a new front and ${v.mid} to ${v.n - 1} into a new back.`;
      else if (swapping) head = `The new stacks replace the old: front.size() = ${fs} and back.size() = ${bs}, so Φ₀ = ${v.phi}.`;
      else {
        const st = v.side === 'front' ? 'front' : 'back';
        const what = op[0] === 'add' ? `${callName(op)} adds x to ${st}` : `${callName(op)} takes ${v.x} from ${st}`;
        const shifted = v.moves.length ? `, shifting ${v.moves.length} element${v.moves.length === 1 ? '' : 's'} inside it` : '';
        if (ln === L.bal || ln === L.balr || ln === L.ret) {
          head = v.stars.includes(v.k) ? `${what}${shifted}; balance() then rebuilt both stacks.`
            : `${what}${shifted}; each stack holds at least a third of the other, so balance() leaves them.`;
        } else head = `${what}${shifted}.`;
      }
      const lines = topline(ctx, head) || 1;

      /* ---------------- the calls */
      const top = callRow(ctx, R.calls.map(callName), v.k, v.stars, hits, lines > 1 ? 140 : 112);

      /* ---------------- the two stacks back to back: front's index 0 next to the middle, growing left, back's growing
         right, as Figure 2.4 draws them; each cell with its list position in its corner, the stack's own index under it */
      const ROW = top + 190, ROWN = ROW + 170, CH = 84;
      const cw = Math.min(80, 600 / SLOTS), GAP = 10;
      const X = (st, t) => (st === 'front' || st === 'f' ? 700 - GAP - (t + 0.5) * cw : 700 + GAP + (t + 0.5) * cw);
      const half = (st, vals, y, listStart, opA = 1, named = true) => {
        /* listStart: the list position of the stack's index 0 when its order is reversed (front), or of index 0 (back) */
        ctx.save(); ctx.globalAlpha *= opA;
        const isFront = st === 'front' || st === 'f';
        for (let t = 0; t < SLOTS; t += 1) {
          const on = t < vals.length, x = X(st, t) - cw / 2;
          rect(ctx, x + 2, y - CH / 2, cw - 4, CH, PAL.panel, on ? ink : alpha(ink, 0.25), on ? 2.5 : 1.5);
          if (on) {
            const p = isFront ? vals.length - 1 - t : listStart + t;
            text(ctx, String(vals[t]), X(st, t), y + 10, key, { size: 34, align: 'center', base: 'middle', weight: 600 });
            text(ctx, String(p), x + 8, y - CH / 2 + 18, idx, { size: 26, base: 'middle' });
            hits.push({ x: X(st, t), y, r: cw / 2, name: `${st}[${t}] = ${vals[t]}, list position ${p}` });
          }
          if (named) text(ctx, String(t), X(st, t), y + CH / 2 + 24, muted, { size: 26, align: 'center', base: 'middle' });
        }
        ctx.restore();
      };
      /* the middle */
      line(ctx, 700, ROW - CH / 2 - 132, 700, ROW + CH / 2 + 40, ink, 3);
      const swapK = ln === L.setF ? (g.prev.line === L.setF ? 1 : k) : (ln === L.setB ? 1 : 0);
      if (swapping && swapK < 1 && v.fresh) {
        /* the old stacks fade, the new ones rise into their place */
        half('front', pv.front || v.front, ROW, 0, 1 - swapK);
        half('back', pv.back || v.back, ROW, (pv.front || v.front).length, 1 - swapK);
        const y = lerp(ROWN, ROW, swapK);
        half('front', v.fresh.f, y, 0, 1, false); half('back', v.fresh.b, y, v.fresh.f.length, 1, false);
      } else {
        half('front', v.front, ROW, 0); half('back', v.back, ROW, fs);
      }
      text(ctx, 'front', 700 - GAP - cw * Math.min(2.5, SLOTS / 2), ROW - CH / 2 - 112, cf, { size: 32, weight: 600, align: 'center', base: 'middle' });
      text(ctx, 'back', 700 + GAP + cw * Math.min(2.5, SLOTS / 2), ROW - CH / 2 - 112, cbk, { size: 32, weight: 600, align: 'center', base: 'middle' });

      if (!swapping) {
        /* the copies inside the stack this call touched: an arc from each element's old cell to its new one, as
           ArrayStack's add and remove shift them */
        v.moves.forEach(([from, to]) => {
          const x0 = X(v.side, from), x1 = X(v.side, to), y = ROW - CH / 2 - 8;
          if (ln === L.toFront || ln === L.toBack || ln === L.fromFront || ln === L.fromBack) {
            const fresh = g.prev.line !== ln;
            if (fresh) partArc(ctx, x0, y, x1, y, 30, Math.max(0.2, k), ci, 4); else curve(ctx, x0, y, x1, y, 30, ci, 4);
          } else curve(ctx, x0, y, x1, y, 30, alpha(ci, 0.45), 3);
        });
        if (v.put && (ln === L.toFront || ln === L.toBack)) rect(ctx, X(v.put[0], v.put[1]) - cw / 2 + 2, ROW - CH / 2, cw - 4, CH, null, ci, 5);
        /* i over the cell of list position i, while a call runs and before balance() rebuilds */
        if (op && !inBal && ln !== L.newF && ln !== L.newB) {
          const p = Math.min(v.i, Math.max(0, n - 1));
          if (n > 0) {
            const [st, t] = where(fs, p), xi = X(st, t), yt = ROW - CH / 2 - 52;
            arrow(ctx, xi, yt - 40, xi, yt, ci, 4);
            text(ctx, `i = ${v.i}`, xi + (st === 'front' ? -46 : 46), yt - 30, ci, { size: 28, weight: 600, align: 'center', base: 'middle' });
          }
        }
      }
      /* balance(): the new stacks fill below, each copy an arrow from its old cell to its new one */
      if (inBal || ln === L.newF || ln === L.newB) {
        if (v.f) half('f', v.f, ROWN, 0, 1, false);
        if (v.b) half('b', v.b, ROWN, v.f ? v.f.length : v.mid, 1, false);
        text(ctx, 'new front', 700 - GAP - cw * 2.5, ROWN + CH / 2 + 30, muted, { size: 26, align: 'center', base: 'middle' });
        text(ctx, 'new back', 700 + GAP + cw * 2.5, ROWN + CH / 2 + 30, muted, { size: 26, align: 'center', base: 'middle' });
        v.bmoves.forEach((mv) => {
          const cur = v.mv && v.mv[2] === mv[2] && v.mv[3] === mv[3];
          const t = cur && g.prev.line !== ln ? k : (cur && !(pv.mv && pv.mv[2] === mv[2] && pv.mv[3] === mv[3]) ? k : 1);
          const x0 = X(mv[0], mv[1]), y0 = ROW + CH / 2 + 40, x1 = X(mv[2], mv[3]), y1 = ROWN - CH / 2 - 6;
          if (cur) arrow(ctx, x0, y0, lerp(x0, x1, Math.max(0.2, t)), lerp(y0, y1, Math.max(0.2, t)), mv[2] === 'f' ? cf : cbk, 5);
          else line(ctx, x0, y0, x1, y1, alpha(mv[2] === 'f' ? cf : cbk, 0.35), 3);
        });
      }

      /* ---------------- the counts: the balance condition, the potential, the lemma's count and its sum */
      const Y0 = ROWN + 96;
      const okF = 3 * fs >= bs, okB = 3 * bs >= fs, small = n < 2;
      seg(ctx, [['3·front.size() = ', ink], [`${3 * fs}`, okF || small ? ink : bad, { weight: 600 }], [okF ? ' ≥ ' : ' < ', okF || small ? ink : bad],
        [`back.size() = ${bs}  ·  3·back.size() = `, ink], [`${3 * bs}`, okB || small ? ink : bad, { weight: 600 }], [okB ? ' ≥ ' : ' < ', okB || small ? ink : bad],
        [`front.size() = ${fs}`, ink]], Y0);
      seg(ctx, [['Φ', cost, { weight: 600 }], [` = |front.size() − back.size()| = |${fs} − ${bs}| = ${v.phi}  ·  `, ink], ['n', cn, { weight: 600, italic: true }], [` = ${n}`, ink]], Y0 + 44);
      seg(ctx, [['calls since the last balance ', PAL.ink], [String(v.since), cost], [` ≥ Φ − Φ₀ = ${v.phi} − ${v.phi0}`, PAL.ink]], Y0 + 88);
      seg(ctx, [['copied by balance(): ', PAL.ink], [String(v.copied), cost], [` ≤ 2m + 2r = ${2 * v.m + 2 * v.r}  (m = ${v.m} calls, r = ${v.r} balances)`, PAL.ink]], Y0 + 132);
      tip.hits = hits;
    },
  });
  F.hover(d.stage, () => tip.hits, d.c);
})();
};
