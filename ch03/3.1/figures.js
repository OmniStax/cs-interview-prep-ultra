/* Figures for section 3.1 Stacks and bracket matching. Boots against the section's text article.
   Three debugger figures (code beside the drawing, stepped by block: METHOD §2.3). sim-array-stack and
   sim-linked-stack run Wikipedia's array and linked-list pseudocode (printed in the text as Wikipedia's words) in a
   four-language translation; sim-brackets runs cp-algorithms' two procedures, which it states in prose only. Every
   variant is an AI translation (METHOD decision 20). Each trace is the figure's own JS copy of the Python, numbered with
   the Python's lines; a call's first frame stands on its def line, so each call is one stop. Indices are drawn from 0,
   as the code counts. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['3.1'] = function (root, F) {
const { C, PAL, alpha, text, line, arrow, topline } = F;
const sim = (id, H) => F.sim(root, id, H);
const AI = 'claude-opus-5-5 high';
const AIS = { python: AI, java: AI, cpp: AI, javascript: AI };
const J = (a) => a.join('\n');
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2, dash) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};
const ease = (a, b, k) => a + (b - a) * k;
const show = (v) => (v === null || v === undefined ? '—' : String(v));

/* ================================================================ sim-array-stack: Wikipedia's array stack */
(function () {
  const PY = J([
    'class Stack:',
    '    def __init__(self, size):',
    '        self.items = [None] * size',
    '        self.maxsize = size',
    '        self.top = 0',
    '',
    '    def push(self, x):',
    '        if self.top == self.maxsize:',
    '            raise OverflowError("overflow")',
    '        else:',
    '            self.items[self.top] = x',
    '            self.top = self.top + 1',
    '',
    '    def pop(self):',
    '        if self.top == 0:',
    '            raise IndexError("underflow")',
    '        else:',
    '            self.top = self.top - 1',
    '            r = self.items[self.top]',
    '            return r',
  ]);
  const braces = (o) => J([
    `${o.kw} Stack {`,
    '    int maxsize;',
    '    int top;',
    `    ${o.items};`,
    '',
    '    Stack(int size) {',
    `        ${o.t}items = new int[size];`,
    `        ${o.t}maxsize = size;`,
    `        ${o.t}top = 0;`,
    '    }',
    '',
    '    void push(int x) {',
    `        if (${o.t}top == ${o.t}maxsize) {`,
    `            throw ${o.over};`,
    '        } else {',
    `            ${o.t}items[${o.t}top] = x;`,
    `            ${o.t}top = ${o.t}top + 1;`,
    '        }',
    '    }',
    '',
    '    int pop() {',
    `        if (${o.t}top == 0) {`,
    `            throw ${o.under};`,
    '        } else {',
    `            ${o.t}top = ${o.t}top - 1;`,
    `            int r = ${o.t}items[${o.t}top];`,
    '            return r;',
    '        }',
    '    }',
    `}${o.semi}`,
  ]);
  const JAVA = braces({ kw: 'class', items: 'int[] items', semi: '', t: 'this.',
    over: 'new IllegalStateException("overflow")', under: 'new IllegalStateException("underflow")' });
  const CPP = braces({ kw: 'struct', items: 'int* items', semi: ';', t: 'this->',
    over: 'std::overflow_error("overflow")', under: 'std::underflow_error("underflow")' });
  const JS = J([
    'class Stack {',
    '    constructor(size) {',
    '        this.items = new Array(size).fill(null);',
    '        this.maxsize = size;',
    '        this.top = 0;',
    '    }',
    '',
    '    push(x) {',
    '        if (this.top === this.maxsize) {',
    '            throw new Error("overflow");',
    '        } else {',
    '            this.items[this.top] = x;',
    '            this.top = this.top + 1;',
    '        }',
    '    }',
    '',
    '    pop() {',
    '        if (this.top === 0) {',
    '            throw new Error("underflow");',
    '        } else {',
    '            this.top = this.top - 1;',
    '            const r = this.items[this.top];',
    '            return r;',
    '        }',
    '    }',
    '}',
  ]);
  const MAPC = { 1: 1, 2: 6, 3: 7, 4: 8, 5: 9, 7: 12, 8: 13, 9: 14, 10: 15, 11: 16, 12: 17, 14: 21, 15: 22, 16: 23, 17: 24, 18: 25, 19: 26, 20: 27 };
  const MAPJ = { 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 14: 17, 15: 18, 16: 19, 17: 20, 18: 21, 19: 22, 20: 23 };
  /* the calls: ['init', size] | ['push', x] | ['pop'] */
  const run = (calls) => F.trace((at) => {
    let items = [], maxsize = 0, top = 0;
    const st = (o) => Object.assign({ top, maxsize, items: items.slice() }, o);
    for (const [op, arg] of calls) {
      if (op === 'init') {
        at(2, st({ size: arg }));
        items = Array(arg).fill(null); at(3, st({ size: arg }));
        maxsize = arg; at(4, st({ size: arg }));
        top = 0; at(5, st({ size: arg }), ['init']);
        continue;
      }
      if (op === 'push') {
        const x = arg;
        at(7, st({ x, 'cells touched': 0 }), ['call', 'push', x]);
        at(8, st({ x, 'cells touched': 0 }));
        if (top === maxsize) { at(9, st({ x, 'cells touched': 0 }), ['overflow', x]); continue; }
        items[top] = x; at(11, st({ x, 'cells touched': 1 }), ['write', top, x]);
        top += 1; at(12, st({ x, 'cells touched': 1 }), ['pushed', x]);
      } else {
        at(14, st({ 'cells touched': 0 }), ['call', 'pop']);
        at(15, st({ 'cells touched': 0 }));
        if (top === 0) { at(16, st({ 'cells touched': 0 }), ['underflow']); continue; }
        top -= 1; at(18, st({ 'cells touched': 0 }));
        const r = items[top]; at(19, st({ r, 'cells touched': 1 }), ['read', top, r]);
        items[top] = null; at(20, st({ r, 'cells touched': 1 }), ['popped', r]);
      }
    }
  });
  /* Wikipedia's GIFs: push 1, 2, 3, 4 into four cells, then 5 (overflow); pop to empty, then once more (underflow) */
  const GIF = [['init', 4], ['push', 1], ['push', 2], ['push', 3], ['push', 4], ['push', 5], ['pop'], ['pop'], ['pop'], ['pop'], ['pop']];
  const MIXED = [['init', 5], ['push', 7], ['push', 3], ['pop'], ['push', 9], ['push', 4], ['pop'], ['pop'], ['push', 6]];
  const EMPTY = [['init', 3], ['pop'], ['push', 8], ['pop'], ['pop']];
  const INPUTS = [
    { value: 'gif', label: 'fill, overflow, empty, underflow', calls: GIF },
    { value: 'mixed', label: 'pushes and pops mixed', calls: MIXED },
    { value: 'empty', label: 'pop an empty stack', calls: EMPTY },
  ];
  const d = sim('sim-array-stack', 560);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: AIS,
    lineMap: { java: MAPC, cpp: MAPC, javascript: MAPJ },
    blocks: [
      { id: 'init', lines: [2, 5], label: 'make an empty stack of maxsize cells', touches: ['items', 'maxsize', 'top'] },
      { id: 'push', lines: [7, 12], label: 'push x' },
      { id: 'full', lines: [8, 9], label: 'top = maxsize: overflow', touches: ['top', 'maxsize'] },
      { id: 'write', lines: [10, 12], label: 'write x at top, then move top up', touches: ['items', 'top'] },
      { id: 'pop', lines: [14, 20], label: 'pop' },
      { id: 'empty', lines: [15, 16], label: 'top = 0: underflow', touches: ['top'] },
      { id: 'read', lines: [17, 20], label: 'move top down, then read the cell', touches: ['top', 'r'] },
    ],
    refs: { 'self.top': () => F.ref('top'), top: () => F.ref('top') },
  });
  F.debug(d, {
    code, watch: ['top', 'maxsize', 'x', 'r', 'cells touched'],
    inputs: INPUTS.map((x) => ({ value: x.value, label: x.label, trace: run(x.calls) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const v = g.frame.vars, pv = (g.prev || g.frame).vars, L = g.frame.line, ev = g.frame.ev || [];
      const max = v.maxsize || 0, top = v.top || 0, items = v.items || [];
      const key = C('key'), idx = C('index'), size = C('size'), cost = C('cost'), ct = F.ref('top');
      /* the headline: the call and what it did */
      let head;
      if (L <= 5) head = max ? `Stack(${max}): ${max} empty cells, top = 0.` : 'Stack(size): an empty stack.';
      else if (L === 7) head = `push(${v.x}): is there a free cell at top = ${top}?`;
      else if (L === 8) head = `top = ${top}${top === max ? ' = maxsize' : ` < maxsize = ${max}`}: ${top === max ? 'the array is full.' : 'there is room.'}`;
      else if (L === 9) head = `push(${v.x}): top = maxsize = ${max}, so overflow. Nothing is written.`;
      else if (L === 11) head = `items[${top}] ← ${v.x}: the new item goes into the free cell.`;
      else if (L === 12) head = `top ${top - 1} → ${top}: ${top} item${top === 1 ? '' : 's'} on the stack, and the next free cell is ${top}.`;
      else if (L === 14) head = `pop(): is anything below top = ${top}?`;
      else if (L === 15) head = top === 0 ? 'top = 0: the stack is empty.' : `top = ${top} > 0: there is an item to pop.`;
      else if (L === 16) head = 'pop(): top = 0, so underflow. Nothing is read.';
      else if (L === 18) head = `top ${top + 1} → ${top}: the top item is in cell ${top}.`;
      else head = `r ← items[${top}] = ${v.r}: the last item pushed is the first popped.`;
      topline(ctx, head);
      /* the array: cells below top are the stack (filled, shaded in the index tint), the rest free (hollow) */
      const cell = 130, n = Math.max(max, 1), l = 700 - (n * cell) / 2, y = 290, h = 92, t = y - h / 2;
      const S = { l, r: l + n * cell, t, b: t + h, cell, n, base: 0, y, x: (i) => l + (i + 0.5) * cell };
      const etop = typeof pv.top === 'number' && pv.maxsize === v.maxsize ? ease(pv.top, top, g.k) : top;
      if (max) F.ds.region(ctx, S, { from: 0, to: etop - 1, color: idx, alpha: 0.16 });
      for (let i = 0; i < max; i += 1) {
        const live = i < top, x0 = l + i * cell;
        rect(ctx, x0, t, cell, h, null, live ? PAL.ink : alpha(PAL.ink, 0.4), 2, live ? undefined : [6, 6]);
        const val = items[i];
        if (val !== null && val !== undefined) text(ctx, String(val), x0 + cell / 2, y, live ? key : alpha(key, 0.35), { size: 38, align: 'center', weight: 600 });
        text(ctx, String(i), x0 + cell / 2, S.b + 26, idx, { size: 26, align: 'center' });
      }
      if (max) {
        /* top: an arrow to the boundary it names, the next free cell; past the last cell when the array is full */
        F.ds.pointer(ctx, S, [{ at: etop, name: 'top', color: ct }], { side: 'above', size: 32 });
        F.hbracket(ctx, l + 4, S.r - 4, S.b + 66, size, `maxsize = ${max}`, { side: 'below' });
        text(ctx, 'bottom', l - 20, y, PAL.muted, { size: 26, align: 'right' });
      }
      /* the item moving: x slides in from the right on a write; r slides out on a read */
      const bx = S.r + 120;
      if (L === 7 || L === 8 || L === 9) {
        const by = 130;
        rect(ctx, bx - 50, by - 36, 100, 72, alpha(key, 0.08), key, 3);
        text(ctx, String(v.x), bx, by, key, { size: 36, align: 'center', weight: 600 });
        text(ctx, 'x', bx, by - 58, PAL.ink, { size: 28, align: 'center', italic: true });
        if (L === 9) { line(ctx, bx - 40, by - 30, bx + 40, by + 30, PAL.bad, 5); line(ctx, bx - 40, by + 30, bx + 40, by - 30, PAL.bad, 5); text(ctx, 'overflow', bx, by + 64, PAL.bad, { size: 28, align: 'center', weight: 600 }); }
      }
      if (ev[0] === 'write' && g.k < 1) {
        const tx = S.x(ev[1]), x = ease(bx, tx, g.k), yy = ease(130, y, g.k);
        rect(ctx, x - 50, yy - 36, 100, 72, alpha(key, 0.08), key, 3);
      }
      if (L === 19 || L === 20) {
        const k = L === 19 ? g.k : 1, from = S.x(top), x = ease(from, bx, k), yy = ease(y, 130, k);
        rect(ctx, x - 50, yy - 36, 100, 72, alpha(key, 0.08), key, 3);
        text(ctx, String(v.r), x, yy, key, { size: 36, align: 'center', weight: 600 });
        if (k > 0.6) text(ctx, 'r', x, yy - 58, PAL.ink, { size: 28, align: 'center', italic: true });
      }
      if (L === 16) text(ctx, 'underflow', 700, 140, PAL.bad, { size: 30, align: 'center', weight: 600 });
      /* the invariant and the cost of the call */
      text(ctx, `the stack is items[0..${top}) · top = ${top} items`, 60, 500, PAL.ink, { size: 26 });
      text(ctx, `cells touched this call ${v['cells touched'] ?? 0} ≤ 1`, 1340, 500, cost, { size: 26, align: 'right' });
    },
  });
})();

/* ================================================================ sim-linked-stack: Wikipedia's linked-list stack */
(function () {
  const PY = J([
    'class Frame:',
    '    data = None',
    '    next = None',
    '',
    'class Stack:',
    '    def __init__(self):',
    '        self.head = None',
    '        self.size = 0',
    '',
    '    def push(self, x):',
    '        newhead = Frame()',
    '        newhead.data = x',
    '        newhead.next = self.head',
    '        self.head = newhead',
    '        self.size = self.size + 1',
    '',
    '    def pop(self):',
    '        if self.head is None:',
    '            raise IndexError("underflow")',
    '        else:',
    '            r = self.head.data',
    '            self.head = self.head.next',
    '            self.size = self.size - 1',
    '            return r',
  ]);
  const braces = (o) => J([
    `${o.kw} Frame {`,
    '    int data;',
    `    ${o.ptr} next;`,
    `}${o.semi}`,
    '',
    `${o.kw} Stack {`,
    `    ${o.ptr} head;`,
    '    int size;',
    '',
    '    Stack() {',
    `        ${o.t}head = ${o.nil};`,
    `        ${o.t}size = 0;`,
    '    }',
    '',
    '    void push(int x) {',
    `        ${o.ptr} newhead = new Frame();`,
    `        newhead${o.dot}data = x;`,
    `        newhead${o.dot}next = ${o.t}head;`,
    `        ${o.t}head = newhead;`,
    `        ${o.t}size = ${o.t}size + 1;`,
    '    }',
    '',
    '    int pop() {',
    `        if (${o.t}head == ${o.nil}) {`,
    `            throw ${o.under};`,
    '        } else {',
    `            int r = ${o.t}head${o.dot}data;`,
    `            ${o.t}head = ${o.t}head${o.dot}next;`,
    `            ${o.t}size = ${o.t}size - 1;`,
    '            return r;',
    '        }',
    '    }',
    `}${o.semi}`,
  ]);
  const JAVA = braces({ kw: 'class', semi: '', ptr: 'Frame', t: 'this.', nil: 'null', dot: '.', under: 'new IllegalStateException("underflow")' });
  const CPP = braces({ kw: 'struct', semi: ';', ptr: 'Frame*', t: 'this->', nil: 'nullptr', dot: '->', under: 'std::underflow_error("underflow")' });
  const JS = J([
    'class Frame {',
    '    data = null;',
    '    next = null;',
    '}',
    '',
    'class Stack {',
    '    constructor() {',
    '        this.head = null;',
    '        this.size = 0;',
    '    }',
    '',
    '    push(x) {',
    '        const newhead = new Frame();',
    '        newhead.data = x;',
    '        newhead.next = this.head;',
    '        this.head = newhead;',
    '        this.size = this.size + 1;',
    '    }',
    '',
    '    pop() {',
    '        if (this.head === null) {',
    '            throw new Error("underflow");',
    '        } else {',
    '            const r = this.head.data;',
    '            this.head = this.head.next;',
    '            this.size = this.size - 1;',
    '            return r;',
    '        }',
    '    }',
    '}',
  ]);
  const MAPC = { 1: 1, 2: 2, 3: 3, 5: 6, 6: 10, 7: 11, 8: 12, 10: 15, 11: 16, 12: 17, 13: 18, 14: 19, 15: 20, 17: 23, 18: 24, 19: 25,
    20: 26, 21: 27, 22: 28, 23: 29, 24: 30 };
  const MAPJ = { 1: 1, 2: 2, 3: 3, 5: 6, 6: 7, 7: 8, 8: 9, 10: 12, 11: 13, 12: 14, 13: 15, 14: 16, 15: 17, 17: 20, 18: 21, 19: 22,
    20: 23, 21: 24, 22: 25, 23: 26, 24: 27 };
  /* the state: the frames on the stack, top first (values), and a frame being pushed or popped beside them */
  const run = (calls) => F.trace((at) => {
    let list = [], size = 0;
    const st = (o) => Object.assign({ head: list.length ? list[0] : null, size, frames: list.slice() }, o);
    at(6, st({}));
    at(7, st({})); at(8, st({}), ['init']);
    for (const [op, x] of calls) {
      if (op === 'push') {
        at(10, st({ x, 'links written': 0 }), ['call', 'push', x]);
        at(11, st({ x, newhead: '(new)', 'links written': 0 }), ['new']);
        at(12, st({ x, newhead: x, 'links written': 0 }), ['new']);
        at(13, st({ x, newhead: x, 'links written': 1 }), ['link']);
        list = [x].concat(list); at(14, st({ x, newhead: x, 'links written': 2 }), ['head']);
        size += 1; at(15, st({ x, newhead: x, 'links written': 2 }), ['pushed']);
      } else {
        at(17, st({ 'links written': 0 }), ['call', 'pop']);
        at(18, st({ 'links written': 0 }));
        if (!list.length) { at(19, st({ 'links written': 0 }), ['underflow']); continue; }
        const r = list[0]; at(21, st({ r, 'links written': 0 }), ['take']);
        list = list.slice(1); at(22, st({ r, 'links written': 1 }), ['moved', r]);
        size -= 1; at(23, st({ r, 'links written': 1 }), ['moved', r]);
        at(24, st({ r, 'links written': 1 }), ['popped', r]);
      }
    }
  });
  const INPUTS = [
    { value: 'gif', label: 'push three, pop three', calls: [['push', 11], ['push', 22], ['push', 33], ['pop'], ['pop'], ['pop']] },
    { value: 'mixed', label: 'pushes and pops mixed', calls: [['push', 5], ['push', 8], ['pop'], ['push', 2], ['push', 7], ['pop']] },
    { value: 'empty', label: 'pop an empty stack', calls: [['pop'], ['push', 4], ['pop'], ['pop']] },
  ];
  const d = sim('sim-linked-stack', 460);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: AIS,
    lineMap: { java: MAPC, cpp: MAPC, javascript: MAPJ },
    blocks: [
      { id: 'init', lines: [6, 8], label: 'an empty stack: head is nil', touches: ['head', 'size'] },
      { id: 'push', lines: [10, 15], label: 'push x at the head' },
      { id: 'make', lines: [11, 12], label: 'a new frame holding x', touches: ['newhead'] },
      { id: 'link', lines: [13, 13], label: 'the new frame points at the old head', touches: ['newhead', 'head'] },
      { id: 'set', lines: [14, 15], label: 'the new frame becomes the head', touches: ['head', 'size'] },
      { id: 'pop', lines: [17, 24], label: 'pop the head' },
      { id: 'empty', lines: [18, 19], label: 'head is nil: underflow', touches: ['head'] },
      { id: 'take', lines: [20, 24], label: 'take the head’s data, then move head one link on', touches: ['head', 'r', 'size'] },
    ],
    refs: { newhead: () => F.ref('newhead'), 'self.head': () => F.ref('head'), head: () => F.ref('head') },
  });
  F.debug(d, {
    code, watch: ['x', 'newhead', 'head', 'size', 'r', 'links written'],
    inputs: INPUTS.map((x) => ({ value: x.value, label: x.label, trace: run(x.calls) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const v = g.frame.vars, L = g.frame.line, ev = g.frame.ev || [];
      const key = C('key'), cost = C('cost'), ch = F.ref('head'), cn = F.ref('newhead');
      const frames = v.frames || [];
      let head;
      if (L <= 8) head = 'Stack(): head is nil and size is 0.';
      else if (L === 10) head = `push(${v.x}): the new item goes in front of the head.`;
      else if (L === 11 || L === 12) head = `newhead is a new frame holding ${v.x}, linked to nothing yet.`;
      else if (L === 13) head = `newhead.next ← head: the new frame points at ${frames.length ? `the frame holding ${frames[0]}` : 'nil'}.`;
      else if (L === 14) head = `head ← newhead: the frame holding ${v.x} is the top now.`;
      else if (L === 15) head = `size ${v.size - 1} → ${v.size}. Two links written, however long the list.`;
      else if (L === 17) head = 'pop(): is there a frame at the head?';
      else if (L === 18) head = frames.length ? `head holds ${frames[0]}: there is a frame to pop.` : 'head is nil: the stack is empty.';
      else if (L === 19) head = 'pop(): head is nil, so underflow.';
      else if (L === 21) head = `r ← head.data = ${v.r}: the last item pushed.`;
      else if (L === 22 || L === 23) head = `head ← head.next: the frame holding ${v.r} is off the stack${L === 23 ? `, size ${v.size}` : ''}.`;
      else head = `pop returns ${v.r}.`;
      topline(ctx, head);
      /* frames in a row, the head first; a frame being pushed stands raised on the left until head takes it */
      const fw = 170, fh = 76, gap = 70, y = 250, x0 = 300;
      const pushing = L >= 11 && L <= 13, popping = L >= 21 && L <= 24 && ev[0] !== 'underflow';
      const row = popping && L === 21 ? frames : frames;
      const fx = (i) => x0 + i * (fw + gap);
      const drawFrame = (x, yy, val, faded, nextTo) => {
        const ink = faded ? alpha(PAL.ink, 0.3) : PAL.ink, kc = faded ? alpha(key, 0.35) : key;
        rect(ctx, x, yy - fh / 2, fw, fh, null, ink, 2);
        line(ctx, x + fw * 0.6, yy - fh / 2, x + fw * 0.6, yy + fh / 2, ink, 2);
        text(ctx, show(val), x + fw * 0.3, yy, kc, { size: 34, align: 'center', weight: 600 });
        if (nextTo === 'nil') text(ctx, 'nil', x + fw * 0.8, yy, PAL.muted, { size: 26, align: 'center' });
        else if (nextTo) arrow(ctx, x + fw * 0.8, yy, nextTo[0], nextTo[1], ink, 3);
      };
      /* the popped frame (after head has moved on) fades to ink above the row */
      if (popping && L >= 22) {
        const k = L === 22 ? g.k : 1;
        drawFrame(ease(fx(0) - fw - gap, fx(0) - fw - gap, k), ease(y, y - 130, k), v.r, true, row.length ? [fx(0), y] : 'nil');
      }
      row.forEach((val, i) => drawFrame(fx(i), y, val, false, i + 1 < row.length ? [fx(i + 1), y] : 'nil'));
      if (pushing) {
        const nx = fx(0) - fw - gap, ny = y - 140;
        rect(ctx, nx - 6, ny - fh / 2 - 6, fw + 12, fh + 12, null, cn, 3, [8, 6]);
        drawFrame(nx, ny, L >= 12 ? v.x : null, false, L >= 13 ? (row.length ? [fx(0) + 10, y - fh / 2] : 'nil') : null);
        text(ctx, 'newhead', nx + fw / 2, ny - fh / 2 - 30, cn, { size: 30, weight: 600, align: 'center' });
      }
      /* head: a pointer box left of the row, its arrow to the first frame or to nil */
      const hx = 90, hy = y + 120;
      rect(ctx, hx, hy - 30, 120, 60, null, ch, 3);
      text(ctx, 'head', hx + 60, hy + 58, ch, { size: 30, weight: 600, align: 'center' });
      if (row.length) {
        const tx = fx(0) + fw * 0.3;
        line(ctx, hx + 60, hy, tx, hy, ch, 4); arrow(ctx, tx, hy, tx, y + fh / 2, ch, 4);
      } else text(ctx, 'nil', hx + 60, hy, PAL.muted, { size: 26, align: 'center' });
      if (L === 19) text(ctx, 'underflow', 700, 120, PAL.bad, { size: 30, align: 'center', weight: 600 });
      text(ctx, `size = ${v.size}`, 1340, 400, C('size'), { size: 26, align: 'right' });
      text(ctx, `links written this call ${v['links written'] ?? 0} ≤ 2`, 1340, 435, cost, { size: 26, align: 'right' });
    },
  });
})();

/* ================================================================ sim-brackets: cp-algorithms' depth counter and stack */
(function () {
  const PY = J([
    'def balanced_one_type(s):',
    '    depth = 0',
    '    for c in s:',
    "        if c == '(':",
    '            depth += 1',
    '        else:',
    '            depth -= 1',
    '        if depth < 0:',
    '            return False',
    '    return depth == 0',
    '',
    "OPENING = {')': '(', ']': '[', '}': '{'}",
    '',
    'def balanced(s):',
    '    stack = []',
    '    for c in s:',
    "        if c in '([{':",
    '            stack.append(c)',
    '        elif not stack or stack[-1] != OPENING[c]:',
    '            return False',
    '        else:',
    '            stack.pop()',
    '    return not stack',
  ]);
  const braces = (o) => J([
    `${o.fn('balancedOneType')} {`,
    '    int depth = 0;',
    `    for (${o.each}) {`,
    "        if (c == '(') {",
    '            depth += 1;',
    '        } else {',
    '            depth -= 1;',
    '        }',
    '        if (depth < 0) {',
    '            return false;',
    '        }',
    '    }',
    `    return depth ${o.eq} 0;`,
    '}',
    '',
    o.opening,
    '',
    `${o.fn('balanced')} {`,
    `    ${o.stack};`,
    `    for (${o.each}) {`,
    `        if (${o.isOpen}) {`,
    `            ${o.push};`,
    `        } else if (${o.mismatch}) {`,
    '            return false;',
    '        } else {',
    `            ${o.pop};`,
    '        }',
    '    }',
    `    return ${o.empty};`,
    '}',
  ]);
  const JAVA = braces({ fn: (n) => `static boolean ${n}(String s)`, each: 'char c : s.toCharArray()', eq: '==',
    opening: "static final Map<Character, Character> OPENING = Map.of(')', '(', ']', '[', '}', '{');",
    stack: 'Deque<Character> stack = new ArrayDeque<>()', isOpen: '"([{".indexOf(c) >= 0', push: 'stack.push(c)',
    mismatch: 'stack.isEmpty() || !stack.peek().equals(OPENING.get(c))', pop: 'stack.pop()', empty: 'stack.isEmpty()' });
  const CPP = braces({ fn: (n) => `bool ${n}(const std::string& s)`, each: 'char c : s', eq: '==',
    opening: "const std::map<char, char> OPENING = {{')', '('}, {']', '['}, {'}', '{'}};",
    stack: 'std::vector<char> stack', isOpen: 'std::string("([{").find(c) != std::string::npos', push: 'stack.push_back(c)',
    mismatch: 'stack.empty() || stack.back() != OPENING.at(c)', pop: 'stack.pop_back()', empty: 'stack.empty()' });
  const JS = braces({ fn: (n) => `function ${n}(s)`, each: 'const c of s', eq: '===',
    opening: "const OPENING = { ')': '(', ']': '[', '}': '{' };",
    stack: 'const stack = []', isOpen: "'([{'.includes(c)", push: 'stack.push(c)',
    mismatch: 'stack.length === 0 || stack[stack.length - 1] !== OPENING[c]', pop: 'stack.pop()', empty: 'stack.length === 0' })
    .replace('    int depth = 0;', '    let depth = 0;');
  const MAP = { 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 9, 9: 10, 10: 13, 12: 16, 14: 18, 15: 19, 16: 20, 17: 21, 18: 22,
    19: 23, 20: 24, 21: 25, 22: 26, 23: 29 };
  const OPEN = { ')': '(', ']': '[', '}': '{' };
  const runCounter = (s) => F.trace((at) => {
    let depth = 0, read = 0, path = [0];
    const st = (o) => Object.assign({ depth, 'characters read': read, path: path.slice() }, o);
    at(1, st({}));
    at(2, st({}));
    for (let i = 0; i < s.length; i += 1) {
      const c = s[i];
      read += 1;
      at(3, st({ c, at: i }), ['read', i]);
      at(4, st({ c, at: i }));
      if (c === '(') { depth += 1; path.push(depth); at(5, st({ c, at: i }), ['up', i]); }
      else { at(6, st({ c, at: i })); depth -= 1; path.push(depth); at(7, st({ c, at: i }), ['down', i]); }
      at(8, st({ c, at: i }));
      if (depth < 0) { at(9, st({ c, at: i }), ['fail', i]); return; }
    }
    at(10, st({ at: s.length }), [depth === 0 ? 'ok' : 'open']);
  });
  const runStack = (s) => F.trace((at) => {
    const stack = [], path = [0];
    let read = 0;
    const st = (o) => Object.assign({ stack: stack.join(' '), 'characters read': read, path: path.slice(), items: stack.slice() }, o);
    at(14, st({}));
    at(15, st({}));
    for (let i = 0; i < s.length; i += 1) {
      const c = s[i];
      read += 1;
      at(16, st({ c, at: i }), ['read', i]);
      at(17, st({ c, at: i }));
      if ('([{'.includes(c)) { stack.push(c); path.push(stack.length); at(18, st({ c, at: i }), ['up', i]); continue; }
      at(19, st({ c, at: i }));
      if (!stack.length || stack[stack.length - 1] !== OPEN[c]) { at(20, st({ c, at: i }), ['fail', i]); return; }
      at(21, st({ c, at: i }));
      stack.pop(); path.push(stack.length); at(22, st({ c, at: i }), ['down', i]);
    }
    at(23, st({ at: s.length }), [stack.length === 0 ? 'ok' : 'open']);
  });
  const INPUTS = [
    { value: 'c1', label: '(())()', s: '(())()', fn: 'counter' },
    { value: 'c2', label: '())(', s: '())(', fn: 'counter' },
    { value: 'c3', label: '(()', s: '(()', fn: 'counter' },
    { value: 's1', label: '([]{})', s: '([]{})', fn: 'stack' },
    { value: 's2', label: '([)]', s: '([)]', fn: 'stack' },
    { value: 's3', label: '{[]', s: '{[]', fn: 'stack' },
  ];
  const d = sim('sim-brackets', 600);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: AIS,
    lineMap: { java: MAP, cpp: MAP, javascript: MAP },
    blocks: [
      { id: 'c-start', lines: [2, 2], label: 'depth ← 0', touches: ['depth'] },
      { id: 'c-read', lines: [3, 9], label: 'read one character' },
      { id: 'c-count', lines: [4, 7], label: 'opening: depth + 1; closing: depth − 1', touches: ['depth'] },
      { id: 'c-check', lines: [8, 9], label: 'depth below 0: not balanced', touches: ['depth'] },
      { id: 'c-end', lines: [10, 10], label: 'balanced if depth ends at 0', touches: ['depth'] },
      { id: 's-start', lines: [15, 15], label: 'an empty stack', touches: ['stack'] },
      { id: 's-read', lines: [16, 22], label: 'read one character' },
      { id: 's-push', lines: [17, 18], label: 'an opening bracket goes on the stack', touches: ['stack'] },
      { id: 's-match', lines: [19, 20], label: 'a closing bracket needs its opening one on top', touches: ['stack'] },
      { id: 's-pop', lines: [21, 22], label: 'take the opening bracket off', touches: ['stack'] },
      { id: 's-end', lines: [23, 23], label: 'balanced if the stack ends empty', touches: ['stack'] },
    ],
  });
  F.debug(d, {
    code, watch: ['c', 'depth', 'stack', 'characters read'],
    inputs: INPUTS.map((x) => ({ value: x.value, label: x.label, trace: x.fn === 'counter' ? runCounter(x.s) : runStack(x.s) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const inp = INPUTS.find((x) => x.value === g.input) || INPUTS[0], s = inp.s, n = s.length;
      const v = g.frame.vars, L = g.frame.line, ev = g.frame.ev || [];
      const key = C('key'), idx = C('index'), cost = C('cost');
      const isStack = inp.fn === 'stack', path = v.path || [0], read = v['characters read'] || 0;
      const at = typeof v.at === 'number' ? v.at : -1, lvl = path[path.length - 1];
      const fail = ev[0] === 'fail', done = ev[0] === 'ok' || ev[0] === 'open';
      /* the headline */
      let head;
      const fnName = isStack ? 'balanced' : 'balanced_one_type';
      if (L === 1 || L === 2 || L === 14 || L === 15) head = `${fnName}("${s}"): ${isStack ? 'an empty stack' : 'depth = 0'}, nothing read yet.`;
      else if (fail && !isStack) head = `'${v.c}' at ${at}: depth −1. A closing bracket with nothing open: not balanced.`;
      else if (fail) head = `'${v.c}' at ${at}: ${v.stack ? `the top is '${v.stack.slice(-1)}', not '${OPEN[v.c]}'` : 'the stack is empty'}, so not balanced.`;
      else if (done) head = ev[0] === 'ok' ? `All ${n} read and ${isStack ? 'the stack is empty' : 'depth is 0'}: balanced.`
        : `All ${n} read, but ${isStack ? `'${v.stack}' is still open` : `depth is ${v.depth}`}: not balanced.`;
      else if (ev[0] === 'up') head = isStack ? `'${v.c}' at ${at} opens: onto the stack.` : `'${v.c}' at ${at} opens: depth ${lvl - 1} → ${lvl}.`;
      else if (ev[0] === 'down') head = isStack ? `'${v.c}' at ${at} closes the '${OPEN[v.c]}' on top: off the stack.` : `'${v.c}' at ${at} closes: depth ${lvl + 1} → ${lvl}.`;
      else head = `'${v.c}' at ${at}: ${'([{'.includes(v.c) ? 'an opening bracket' : 'a closing bracket'}.`;
      topline(ctx, head);
      /* the string: characters read filled, the rest hollow; the one being read marked */
      const cell = 110, l = 140, y = 150, h = 80, t = y - h / 2;
      const S = { l, r: l + n * cell, t, b: t + h, cell, n, base: 0, y, x: (i) => l + (i + 0.5) * cell };
      if (read) F.ds.region(ctx, S, { from: 0, to: read - 1, color: idx, alpha: 0.14 });
      for (let i = 0; i < n; i += 1) {
        const x0 = l + i * cell, seen = i < read, bad = fail && i === at;
        rect(ctx, x0, t, cell, h, null, bad ? PAL.bad : seen ? PAL.ink : alpha(PAL.ink, 0.4), bad ? 4 : 2, seen ? undefined : [6, 6]);
        text(ctx, s[i], x0 + cell / 2, y, bad ? PAL.bad : seen ? key : alpha(key, 0.5), { size: 40, align: 'center', weight: 600 });
        text(ctx, String(i), x0 + cell / 2, S.b + 26, idx, { size: 26, align: 'center' });
      }
      if (at >= 0 && at < n) arrow(ctx, S.x(at), t - 50, S.x(at), t - 8, idx, 4);
      /* the depth line: the depth (or the stack's height) after each character, never below 0 if balanced */
      const gx0 = l, gx1 = l + n * cell, gy0 = 470, unit = 52;
      const Y = (dv) => gy0 - dv * unit;
      /* with several types, the depth the counter would keep with the types merged, dashed under the stack's line */
      if (isStack) {
        let dd = 0;
        const ghost = [0].concat([...s].map((ch) => (dd += '([{'.includes(ch) ? 1 : -1)));
        for (let k = 1; k < ghost.length; k += 1) line(ctx, l + (k - 1) * cell, Y(ghost[k - 1]), l + k * cell, Y(ghost[k]), alpha(PAL.ink, 0.35), 3, [8, 8]);
        text(ctx, 'depth, the types merged', l + n * cell + 20, Y(ghost[ghost.length - 1]) - 22, PAL.muted, { size: 26 });
      }
      line(ctx, gx0, Y(0), gx1 + 30, Y(0), PAL.muted, 2, [10, 10]);
      text(ctx, '0', gx0 - 14, Y(0), PAL.muted, { size: 26, align: 'right' });
      text(ctx, isStack ? 'stack height' : 'depth', gx0 - 14, Y(2), PAL.ink, { size: 26, align: 'right' });
      for (let k = 1; k < path.length; k += 1) {
        const xa = l + (k - 1) * cell, xb = l + k * cell, a = path[k - 1], b = path[k];
        const kk = k === path.length - 1 && (ev[0] === 'up' || ev[0] === 'down') ? g.k : 1;
        const col = b < 0 ? PAL.bad : PAL.ink;
        line(ctx, xa, Y(a), ease(xa, xb, kk), Y(ease(a, b, kk)), col, 5);
      }
      const last = path.length - 1;
      F.dot(ctx, l + last * cell, Y(lvl), lvl < 0 ? PAL.bad : PAL.ink, true, 8);
      /* the right panel: the stack of open brackets, bottom up, or the depth as a number */
      const px = 1230, pb = 470;
      if (isStack) {
        const items = v.items || [];
        text(ctx, 'stack', px, pb + 40, PAL.ink, { size: 28, align: 'center', weight: 600 });
        line(ctx, px - 60, pb, px + 60, pb, PAL.ink, 3);
        items.forEach((b, i) => {
          const top = i === items.length - 1;
          rect(ctx, px - 50, pb - (i + 1) * 58, 100, 54, null, fail && top ? PAL.bad : PAL.ink, top ? 3 : 2);
          text(ctx, b, px, pb - (i + 0.5) * 58 - 2, key, { size: 36, align: 'center', weight: 600 });
        });
      } else {
        text(ctx, 'depth', px, pb + 40, PAL.ink, { size: 28, align: 'center', weight: 600 });
        text(ctx, String(v.depth).replace('-', '−'), px, pb - 60, v.depth < 0 ? PAL.bad : PAL.ink, { size: 40, align: 'center', weight: 600 });
      }
      /* the invariant, and the cost */
      const ok = Math.min(...path) >= 0;
      text(ctx, ok ? `never below 0 so far · now ${lvl}` : 'went below 0', 60, 560, ok ? PAL.ink : PAL.bad, { size: 26 });
      text(ctx, `characters read ${read} ≤ n = ${n}`, 1340, 560, cost, { size: 26, align: 'right' });
    },
  });
})();
};
