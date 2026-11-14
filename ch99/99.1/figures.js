/* SANDBOX, not part of the book. Figures for 99.1, a trial of the lesson shape
   "brute force → what it wastes (the reader answers) → the fast algorithm → recap → check" on the sorted-pair problem.
   All three figures draw one scene, the array over the table of every pair i < j, so the reader sees the same
   space searched three ways. A sum is drawn only once the algorithm has added it up: a pair ruled out unseen is
   struck through and never shows its number.
   sim-brute's code is AI-written; sim-fast's is TheAlgorithms/Python's two_pointer (MIT), as 2.3 prints it. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['99.1'] = function (root, F) {
const { C, PAL, alpha, text, line, topline } = F;
const sim = (id, H) => F.sim(root, id, H);
const J = (a) => a.join('\n');
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2, dash) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};
/* a debugger opens at rest: the reader starts it (the trial's answer to "should a figure play by itself?") */
const rest = (d) => { const bar = d.fig.querySelector('.transport'); if (bar && bar.classList.contains('playing')) bar.querySelector('.tbtn').click(); };
function cells(ctx, o) {
  const n = o.values.length, cell = Math.min(120, 1100 / Math.max(1, n)), h = 72;
  const l = 700 - (n * cell) / 2, t = o.y - h / 2;
  const S = { l, r: l + n * cell, t, b: t + h, cell, n, base: 0, y: o.y, x: (i) => l + (i + 0.5) * cell };
  const key = C('key'), idx = C('index');
  o.values.forEach((v, i) => {
    const st = o.state ? o.state(i) : 'live';
    const x0 = l + i * cell;
    rect(ctx, x0, t, cell, h, PAL.panel, st === 'faded' ? alpha(PAL.ink, 0.25) : PAL.ink, st === 'hot' ? 4 : 2);
    text(ctx, String(v), x0 + cell / 2, o.y, st === 'faded' ? alpha(key, 0.35) : key, { size: 32, align: 'center', weight: st === 'hot' ? 600 : 400 });
    text(ctx, String(i), x0 + cell / 2, S.b + 24, st === 'faded' ? alpha(idx, 0.45) : idx, { size: 26, align: 'center' });
  });
  return S;
}
const ptr = (ctx, S, list) => {
  const placed = F.ds.pointer(ctx, S, list.map((p) => Object.assign({}, p, { name: '' })), { side: 'above', size: 30 });
  placed.forEach((q, k) => {
    const lean = q.lean < -1e-6 ? 'right' : q.lean > 1e-6 ? 'left' : 'center';
    text(ctx, list[k].name, q.x + (lean === 'right' ? 6 : lean === 'left' ? -6 : 0), q.y, list[k].color, { size: 30, weight: 600, align: lean });
  });
};
const pairsOf = (n) => (n * (n - 1)) / 2;

/* The scene. o: A, t; I, J the pointers (numbers, may be fractional while moving) or null;
   cell(r, c) -> 'unknown' | 'known' | 'dead' | 'peek' | 'maybe' | 'cur' | 'found' | 'missed';
   strip(k) -> the array cell's state; counts: [[words, number], …] */
function scene(ctx, o) {
  const A = o.A, n = A.length, cl = F.ref('pair-l'), cr = F.ref('pair-r'), idx = C('index'), key = C('key');
  const S = cells(ctx, { values: A, y: 220, state: o.strip });
  if (o.window) F.ds.region(ctx, S, { from: o.window[0], to: o.window[1], color: idx, alpha: 0.14 });
  const ps = [];
  if (o.I != null) ps.push({ at: o.I, name: 'i', color: cl });
  if (o.J != null) ps.push({ at: o.J, name: 'j', color: cr });
  if (ps.length) ptr(ctx, S, ps);
  const m = n - 1, cw = Math.min(110, 840 / m), ch = 50, gx = 700 - (m * cw) / 2, gy = 420;
  text(ctx, 'every pair i < j: row i, column j', gx, gy - 66, PAL.muted, { size: 26 });
  const Ir = o.I == null ? -1 : Math.round(o.I), Jr = o.J == null ? -1 : Math.round(o.J);
  for (let c = 1; c < n; c += 1) text(ctx, String(c), gx + (c - 0.5) * cw, gy - 22, c === Jr ? cr : alpha(idx, 0.8), { size: 26, align: 'center', weight: c === Jr ? 600 : 400 });
  text(ctx, 'j', gx + m * cw + 26, gy - 22, cr, { size: 28, weight: 600, italic: true });
  text(ctx, 'i', gx - 18, gy - 22, cl, { size: 28, weight: 600, italic: true, align: 'right' });
  for (let r = 0; r < n - 1; r += 1) {
    text(ctx, String(r), gx - 18, gy + (r + 0.5) * ch, r === Ir ? cl : alpha(idx, 0.8), { size: 26, align: 'right', weight: r === Ir ? 600 : 400 });
    for (let c = r + 1; c < n; c += 1) {
      const x0 = gx + (c - 1) * cw, y0 = gy + r * ch, st = o.cell(r, c), s = A[r] + A[c];
      if (st === 'unknown') rect(ctx, x0, y0, cw, ch, null, alpha(PAL.ink, 0.3), 2);
      else if (st === 'dead') {
        rect(ctx, x0, y0, cw, ch, null, alpha(PAL.ink, 0.12), 2);
        line(ctx, x0 + 14, y0 + ch - 12, x0 + cw - 14, y0 + 12, alpha(PAL.ink, 0.22), 2);
      } else if (st === 'peek' || st === 'maybe') {
        rect(ctx, x0, y0, cw, ch, st === 'maybe' ? alpha(idx, 0.12) : null, alpha(PAL.ink, 0.4), 2, [6, 6]);
        text(ctx, String(s), x0 + cw / 2, y0 + ch / 2, PAL.muted, { size: 26, align: 'center' });
        if (st === 'peek') line(ctx, x0 + 14, y0 + ch - 12, x0 + cw - 14, y0 + 12, alpha(PAL.ink, 0.22), 2);
      } else {
        rect(ctx, x0, y0, cw, ch, alpha(idx, 0.10), alpha(PAL.ink, 0.45), 2);
        text(ctx, String(s), x0 + cw / 2, y0 + ch / 2, st === 'missed' ? PAL.bad : key, { size: 26, align: 'center', weight: st === 'found' || st === 'missed' || s === o.t ? 600 : 400 });
        if (st === 'cur') rect(ctx, x0 + 2, y0 + 2, cw - 4, ch - 4, null, PAL.ink, 4);
        if (st === 'found') rect(ctx, x0 + 2, y0 + 2, cw - 4, ch - 4, null, key, 4);
        if (st === 'missed') rect(ctx, x0 + 2, y0 + 2, cw - 4, ch - 4, null, PAL.bad, 4);
      }
    }
  }
  if (o.counts) {
    const parts = [];
    o.counts.forEach(([w, v], k) => { parts.push((k ? '   ·   ' : '') + w + ' '); parts.push([String(v), C('cost')]); });
    F.rich(ctx, parts, 1340, 830, { size: 28, align: 'right' });
  }
  return { gx, gy, cw, ch };
}

const BOOK = [2, 4, 5, 7, 9, 12, 14, 18];

/* ================================================================ sim-brute: every pair, one at a time */
(function () {
  const PY = J([
    'def pair_sum_brute(nums, target):',
    '    for i in range(len(nums)):',
    '        for j in range(i + 1, len(nums)):',
    '            if nums[i] + nums[j] == target:',
    '                return [i, j]',
    '    return []',
  ]);
  const run = (A, t) => F.trace((at) => {
    let checks = 0;
    for (let i = 0; i < A.length; i += 1) {
      at(2, { i, checks });
      for (let j = i + 1; j < A.length; j += 1) {
        at(3, { i, j, checks });
        checks += 1;
        const s = A[i] + A[j];
        at(4, { i, j, 'nums[i] + nums[j]': s, checks });
        if (s === t) { at(5, { i, j, 'nums[i] + nums[j]': s, checks }, ['found', i, j]); return; }
      }
    }
    at(6, { checks }, ['none']);
  });
  const INPUTS = [
    { value: 'hit', label: 'target 21', A: BOOK, t: 21 },
    { value: 'miss', label: 'target 15 (no pair)', A: BOOK, t: 15 },
  ];
  const d = sim('sim-brute', 860);
  const code = F.code(d, {
    lang: 'python', src: PY,
    blocks: [
      { id: 'row', lines: [2, 5], label: 'take nums[i] and try every partner to its right', touches: ['i'] },
      { id: 'one', lines: [3, 5], label: 'add up one pair and compare it with the target', touches: ['j', 'nums[i] + nums[j]'] },
    ],
    refs: { i: () => F.ref('pair-l'), j: () => F.ref('pair-r') },
  });
  F.debug(d, {
    code, watch: ['i', 'j', 'nums[i] + nums[j]'],
    inputs: INPUTS.map((x) => ({ value: x.value, label: x.label, trace: run(x.A, x.t), args: { target: x.t } })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const inp = INPUTS.find((x) => x.value === g.input) || INPUTS[0], A = inp.A, n = A.length, t = inp.t;
      const v = g.frame.vars, ev = g.frame.ev || [], checks = v.checks || 0, N = pairsOf(n);
      const ord = (r, c) => r * n - (r * (r + 1)) / 2 + (c - r - 1);   /* row-major place of pair (r, c) */
      const found = ev[0] === 'found', none = ev[0] === 'none';
      const I = typeof v.i === 'number' ? v.i : null, Jn = typeof v.j === 'number' ? v.j : null;
      let head;
      if (checks === 0) head = `Is there a pair that adds up to ${t}? The obvious way: add up every pair and look.`;
      else if (found) head = `${A[I]} + ${A[Jn]} = ${t}: found, after adding up ${checks} of the ${N} pairs.`;
      else if (none) head = `All ${N} pairs added up, and none is ${t}.`;
      else head = `${checks} of ${N} pairs added up so far. Each sum tells us about that one pair and nothing else.`;
      topline(ctx, head);
      scene(ctx, {
        A, t, I: none ? null : I, J: none || Jn == null ? null : Jn,
        strip: (k) => (!none && (k === I || k === Jn) ? 'hot' : 'live'),
        cell: (r, c) => { const k = ord(r, c); return k >= checks ? 'unknown' : found && r === I && c === Jn ? 'found' : k === checks - 1 && !none ? 'cur' : 'known'; },
        counts: [['sums added up', checks], ['pairs', N]],
      });
    },
  });
  rest(d);
})();

/* ================================================================ sim-insight: the reader rules pairs out */
(function () {
  const d = sim('sim-insight', 860);
  const fb = document.createElement('p');
  fb.style.cssText = 'margin:0;padding:14px 22px 18px;min-height:4.6em;font:inherit;line-height:1.5';
  const row = document.createElement('div'); row.className = 'ctlseg'; row.style.cssText = 'display:flex;flex-wrap:wrap;gap:8px;margin:0 auto';
  d.controls.appendChild(row); d.fig.appendChild(fb);
  let seed = 11;
  const rnd = () => { seed = (seed * 1103515245 + 12345) % 2147483648; return seed / 2147483648; };
  const fresh = () => {
    const set = new Set(); while (set.size < 8) set.add(1 + Math.floor(rnd() * 24));
    const A = Array.from(set).sort((a, b) => a - b);
    let t;
    if (rnd() < 0.7) { const a = 1 + Math.floor(rnd() * 5), b = a + 1 + Math.floor(rnd() * (6 - a)); t = A[a] + A[b]; }
    else { t = A[2] + A[5] + 1; }
    return { A, t };
  };
  let st;
  const start = (A, t) => { st = { A, t, i: 0, j: A.length - 1, seen: [[0, A.length - 1]], phase: 'ask', pick: null, done: null }; settle(); };
  const sum = () => st.A[st.i] + st.A[st.j];
  function settle() { const s = sum(); if (s === st.t) st.done = 'found'; }
  const brute = () => { const n = st.A.length; let k = 0; for (let r = 0; r < n; r += 1) for (let c = r + 1; c < n; c += 1) { k += 1; if (st.A[r] + st.A[c] === st.t) return k; } return k; };
  const btn = (label, act, primary) => {
    const b = document.createElement('button'); b.type = 'button'; b.className = 'segbtn' + (primary ? ' on' : ''); b.textContent = label;
    b.style.cssText = 'padding:6px 14px;border-radius:6px'; b.addEventListener('click', act); return b;
  };
  function ui() {
    const { A, t, i, j } = st, s = sum(), a = A[i], b = A[j], small = s < t;
    row.replaceChildren();
    if (st.done) {
      const n = A.length, N = pairsOf(n), k = st.seen.length;
      fb.textContent = st.done === 'found'
        ? `${a} + ${b} = ${t}. You found it by adding up ${k} pairs; the obvious way adds up ${brute()} before it gets there. ${deadCount()} pairs were thrown out without ever being added up: each move took a whole row or column on the strength of one sum.`
        : `i and j have met, so no pair is left: nothing adds up to ${t}. That took ${k} sums, where the obvious way needs all ${N}. You have just run the fast algorithm by hand.`;
      row.append(btn('Start over', () => { start(A, t); ui(); }), btn('Another array', () => { const x = fresh(); start(x.A, x.t); ui(); }, true));
    } else if (st.phase === 'ask') {
      fb.textContent = '';
      row.append(
        btn(`Row ${i}: every other pair with ${a}`, () => answer('row')),
        btn(`Column ${j}: every other pair with ${b}`, () => answer('col')),
        btn('Nothing but this pair', () => answer('one')),
      );
    } else {
      const good = small ? 'row' : 'col';
      const rowWhy = `its other sums pair ${a} with something smaller than ${b}, so all are below ${s}`;
      const colWhy = `its other sums pair ${b} with something larger than ${a}, so all are above ${s}`;
      const where = small ? `Row ${i}` : `Column ${j}`, other = small ? `Column ${j}` : `Row ${i}`;
      const safe = small ? rowWhy : colWhy, unsafe = small ? colWhy : rowWhy, verdict = small ? 'too small' : 'too big';
      if (st.pick === good) fb.textContent = `Right. ${where}: ${safe}, and ${s} is already ${verdict}. None of them can be ${t}, and none had to be added up.`;
      else if (st.pick === 'one') fb.textContent = `Safe, but that is the obvious way again, one pair at a time. ${where}: ${safe}, and ${s} is already ${verdict}. All of it can go.`;
      else fb.textContent = `Not safe. ${other}: ${unsafe}, and ${s} is ${verdict}, so one of them could be ${t}. ${where} is what can go: ${safe}.`;
      row.append(btn(small ? `Cross out row ${i} and move i right` : `Cross out column ${j} and move j left`, next, true));
    }
    F.redrawAll();
  }
  function answer(p) { st.pick = p; st.phase = 'told'; ui(); }
  function next() {
    if (sum() < st.t) st.i += 1; else st.j -= 1;
    st.phase = 'ask'; st.pick = null;
    if (st.i >= st.j) st.done = 'none'; else { st.seen.push([st.i, st.j]); settle(); }
    ui();
  }
  function draw() {
    const { ctx } = F.begin(d.c);
    const { A, t, i, j } = st, n = A.length, s = A[i] + A[j < 0 ? 0 : j], small = s < t;
    const seen = (r, c) => st.seen.some(([x, y]) => x === r && y === c);
    let head;
    if (st.done === 'found') head = `nums[${i}] + nums[${j}] = ${A[i]} + ${A[j]} = ${t}: found.`;
    else if (st.done === 'none') head = `No pair adds up to ${t}.`;
    else head = `nums[${i}] + nums[${j}] = ${A[i]} + ${A[j]} = ${s}, ${small ? 'less' : 'more'} than ${t}. Which pairs can you rule out without adding them up?`;
    topline(ctx, head);
    const told = st.phase === 'told' && !st.done;
    const g = scene(ctx, {
      A, t, I: st.done === 'none' ? null : i, J: st.done === 'none' ? null : j,
      window: st.done === 'none' ? null : [i, j],
      strip: (k) => (st.done === 'none' || k < i || k > j ? 'faded' : st.done === 'found' && (k === i || k === j) ? 'hot' : 'live'),
      cell: (r, c) => {
        if (st.done === 'none') return seen(r, c) ? 'known' : 'dead';
        if (r === i && c === j) return st.done === 'found' ? 'found' : 'cur';
        if (seen(r, c)) return 'known';
        if (r < i || c > j) return 'dead';
        if (told && r === i) return small ? 'peek' : 'maybe';       /* the rest of row i: smaller sums */
        if (told && c === j) return small ? 'maybe' : 'peek';       /* the rest of column j: larger sums */
        return 'unknown';
      },
      counts: [['sums added up', st.seen.length], ['ruled out unseen', deadCount()], ['pairs', pairsOf(n)]],
    });
    if (told) {
      /* what the two lines through the current pair hold, written at their far ends */
      if (j - i > 1) {
        text(ctx, `all smaller than ${s}`, g.gx + i * g.cw - 14, g.gy + (i + 0.5) * g.ch, PAL.muted, { size: 26, align: 'right' });
        text(ctx, `all larger than ${s}`, g.gx + (j - 0.5) * g.cw, g.gy + j * g.ch + 24, PAL.muted, { size: 26, align: 'center' });
      }
    }
  }
  function deadCount() {
    const n = st.A.length; let k = 0;
    for (let r = 0; r < n; r += 1) for (let c = r + 1; c < n; c += 1) {
      const out = st.done === 'none' ? true : r < st.i || c > st.j;
      if (out && !st.seen.some(([x, y]) => x === r && y === c)) k += 1;
    }
    return k;
  }
  start(BOOK, 21);
  F.register(d.fig, { update: () => {}, draw, arrive: false });
  ui();
})();

/* ================================================================ sim-fast: TheAlgorithms two_pointer */
(function () {
  const PY = J([
    'def two_pointer(nums: list[int], target: int) -> list[int]:',
    '    i = 0',
    '    j = len(nums) - 1',
    '',
    '    while i < j:',
    '        if nums[i] + nums[j] == target:',
    '            return [i, j]',
    '        elif nums[i] + nums[j] < target:',
    '            i = i + 1',
    '        else:',
    '            j = j - 1',
    '',
    '    return []',
  ]);
  const walk = (A, t) => { let i = 0, j = A.length - 1; const p = []; while (i < j) { p.push([i, j]); const s = A[i] + A[j]; if (s === t) break; if (s < t) i += 1; else j -= 1; } return p; };
  const run = (A, t) => F.trace((at) => {
    let i = 0, checks = 0; at(2, { i, checks });
    let j = A.length - 1; at(3, { i, j, checks });
    while (i < j) {
      at(5, { i, j, checks });
      const s = A[i] + A[j]; checks += 1;
      at(6, { i, j, 'nums[i] + nums[j]': s, checks });
      if (s === t) { at(7, { i, j, 'nums[i] + nums[j]': s, checks }, ['found', i, j]); return; }
      at(8, { i, j, 'nums[i] + nums[j]': s, checks });
      if (s < t) { i = i + 1; at(9, { i, j, 'nums[i] + nums[j]': s, checks }, ['up', i - 1]); }
      else { at(10, { i, j, 'nums[i] + nums[j]': s, checks }); j = j - 1; at(11, { i, j, 'nums[i] + nums[j]': s, checks }, ['down', j + 1]); }
    }
    at(13, { i, j, checks }, ['none']);
  });
  const bruteCount = (A, t) => { let k = 0; for (let r = 0; r < A.length; r += 1) for (let c = r + 1; c < A.length; c += 1) { k += 1; if (A[r] + A[c] === t) return k; } return k; };
  const INPUTS = [
    { value: 'hit', label: 'target 21', A: BOOK, t: 21 },
    { value: 'miss', label: 'target 15 (no pair)', A: BOOK, t: 15 },
    { value: 'worst', label: 'worst case', A: [5, 8, 12, 16, 18, 19, 20, 21], t: 34 },
    { value: 'unsorted', label: 'not sorted', A: [18, 2, 14, 4, 5, 7, 12, 9], t: 21, broken: true },
  ].map((x) => Object.assign(x, { path: walk(x.A, x.t), brute: bruteCount(x.A, x.t) }));
  const d = sim('sim-fast', 860);
  const code = F.code(d, {
    lang: 'python', src: PY,
    blocks: [
      { id: 'init', lines: [2, 3], label: 'start with the first and the last: every pair is still possible', touches: ['i', 'j'] },
      { id: 'loop', lines: [5, 11], label: 'one sum, and a whole row or column goes' },
      { id: 'check', lines: [6, 7], label: 'add up the pair at the corner of what is left', touches: ['nums[i] + nums[j]'] },
      { id: 'move', lines: [8, 11], label: 'too small: every pair with nums[i] is out; too big: every pair with nums[j]', touches: ['i', 'j'] },
    ],
    refs: { i: () => F.ref('pair-l'), j: () => F.ref('pair-r') },
  });
  F.debug(d, {
    code, watch: ['i', 'j', 'nums[i] + nums[j]'],
    inputs: INPUTS.map((x) => ({ value: x.value, label: x.label, trace: run(x.A, x.t), args: { target: x.t } })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const inp = INPUTS.find((x) => x.value === g.input) || INPUTS[0], A = inp.A, n = A.length, t = inp.t;
      const v = g.frame.vars, L = g.frame.line, ev = g.frame.ev || [], checks = v.checks || 0;
      const I = typeof v.i === 'number' ? v.i : 0, Jn = typeof v.j === 'number' ? v.j : n - 1;
      const found = ev[0] === 'found', none = ev[0] === 'none';
      const seenAt = (r, c) => inp.path.findIndex(([x, y]) => x === r && y === c);
      let head;
      if (L <= 3) head = `i = 0 and j = ${n - 1}: no sum added up yet, and every pair still possible.`;
      else if (L === 5) head = `Any pair that adds up to ${t} lies between i = ${I} and j = ${Jn}.`;
      else if (L === 6 || L === 8 || L === 10) { const s = A[I] + A[Jn]; head = `nums[${I}] + nums[${Jn}] = ${A[I]} + ${A[Jn]} = ${s} ${s === t ? '=' : s < t ? '<' : '>'} ${t}`; }
      else if (L === 7) head = `${A[I]} + ${A[Jn]} = ${t}: found with ${checks} sums. The obvious way adds up ${inp.brute}.`;
      else if (L === 9) head = `${A[I - 1]} + ${A[Jn]} < ${t}, and ${A[Jn]} is the largest partner left: row ${I - 1} is out, unseen.`;
      else if (L === 11) head = `${A[I]} + ${A[Jn + 1]} > ${t}, and ${A[I]} is the smallest partner left: column ${Jn + 1} is out, unseen.`;
      else if (inp.broken) head = `It answers "no pair", but ${A[2]} + ${A[5]} = ${t} was there. The rule threw it out unseen: it only holds on a sorted array.`;
      else head = `i and j have met: no pair adds up to ${t}, settled with ${checks} sums. The obvious way adds up ${inp.brute}.`;
      topline(ctx, head);
      const ei = g.num('i'), ej = g.num('j');
      const dead = (r, c) => r < I || c > Jn || none;
      let unseen = 0;
      for (let r = 0; r < n; r += 1) for (let c = r + 1; c < n; c += 1) { const k = seenAt(r, c); if (dead(r, c) && !(k >= 0 && k < checks)) unseen += 1; }
      scene(ctx, {
        A, t, I: L > 1 ? (isNaN(ei) ? 0 : ei) : null, J: L > 2 && !isNaN(ej) ? ej : null,
        window: [isNaN(ei) ? 0 : ei, isNaN(ej) ? n - 1 : ej],
        strip: (k) => (k < I || k > Jn ? 'faded' : found && (k === I || k === Jn) ? 'hot' : 'live'),
        cell: (r, c) => {
          const k = seenAt(r, c), known = k >= 0 && k < checks;
          if (none && inp.broken && A[r] + A[c] === t) return 'missed';
          if (known) return found && r === I && c === Jn ? 'found' : r === I && c === Jn && (L === 6 || L === 8 || L === 10) ? 'cur' : 'known';
          return dead(r, c) ? 'dead' : 'unknown';
        },
        counts: [['sums added up', checks], ['ruled out unseen', unseen], ['pairs', pairsOf(n)]],
      });
    },
  });
  rest(d);
})();
};
