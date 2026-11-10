/* SANDBOX, not part of the book. Figures for 99.2, the second trial of the lesson shape, on the minimum of
   every window of k numbers (the monotonic queue of 3.4). All three figures draw one scene: the array, the
   window on it, and a strike through every number that can no longer be a minimum. The queue of the fast
   algorithm is the numbers of the window left unstruck, so it is drawn where they stand.
   Both listings are AI-written: cp-algorithms prints the queue's three operations and not the loop over windows. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['99.2'] = function (root, F) {
const { C, PAL, alpha, text, line, topline } = F;
const sim = (id, H) => F.sim(root, id, H);
const J = (a) => a.join('\n');
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2, dash) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};
const rest = (d) => { const bar = d.fig.querySelector('.transport'); if (bar && bar.classList.contains('playing')) bar.querySelector('.tbtn').click(); };
const CW = 92, YA = 230, HA = 72;
const X0 = (n) => 700 - (n * CW) / 2;

/* The scene. o: A, lo, hi (the window, hi < 0 before it starts); state(j) -> 'ahead' | 'gone' | 'live' | 'cand' |
   'struck' | 'mark' | 'min' | 'new'; under(j) -> a small note under the index, or ''; mins: {j: value} drawn under
   the last number of each window; counts */
function scene(ctx, o) {
  const A = o.A, n = A.length, x0 = X0(n), key = C('key'), idx = C('index'), t = YA - HA / 2;
  const S = { l: x0, cell: CW, t, b: t + HA, x: (j) => x0 + (j + 0.5) * CW };
  if (o.hi >= o.lo && o.hi >= 0) F.ds.region(ctx, S, { from: o.lo, to: o.hi, color: idx, alpha: 0.13 });
  A.forEach((v, j) => {
    const st = o.state(j), x = x0 + j * CW;
    const dim = st === 'ahead' || st === 'gone';
    const fill = st === 'cand' || st === 'min' || st === 'new' ? alpha(key, 0.14) : PAL.panel;
    rect(ctx, x, t, CW, HA, fill, dim ? alpha(PAL.ink, 0.22) : PAL.ink, st === 'min' || st === 'new' ? 4 : 2);
    if (st === 'min') rect(ctx, x + 3, t + 3, CW - 6, HA - 6, null, key, 4);
    const faded = dim || st === 'struck';
    text(ctx, String(v), x + CW / 2, YA, faded ? alpha(key, 0.38) : key, { size: 32, align: 'center', weight: st === 'min' || st === 'new' ? 600 : 400 });
    if (st === 'struck') line(ctx, x + 14, t + HA - 12, x + CW - 14, t + 12, alpha(PAL.ink, 0.55), 3);
    if (st === 'mark') line(ctx, x + 14, t + HA - 12, x + CW - 14, t + 12, PAL.bad, 4);
    text(ctx, String(j), x + CW / 2, S.b + 24, dim ? alpha(idx, 0.45) : idx, { size: 26, align: 'center' });
    const u = o.under ? o.under(j) : '';
    if (u) text(ctx, u, x + CW / 2, S.b + 58, PAL.muted, { size: 26, align: 'center' });
  });
  if (o.hi >= o.lo && o.hi >= 0) F.hbracket(ctx, S.x(o.lo) - CW / 2 + 4, S.x(o.hi) + CW / 2 - 4, t - 18, C('size'), `window, k = ${o.k}`, { side: 'above', size: 26 });
  if (o.underName) text(ctx, o.underName, x0 - 20, S.b + 58, PAL.muted, { size: 26, align: 'right' });
  const ym = o.under ? 400 : 368;
  text(ctx, 'minima', x0 - 20, ym, PAL.ink, { size: 26, align: 'right' });
  Object.keys(o.mins || {}).forEach((j) => text(ctx, String(o.mins[j]), S.x(+j), ym, key, { size: 30, align: 'center', weight: +j === o.hi ? 600 : 400 }));
  if (o.counts) {
    const parts = [];
    o.counts.forEach(([w, v], k) => { parts.push((k ? '   ·   ' : '') + w + ' '); parts.push([String(v), C('cost')]); });
    F.rich(ctx, parts, 1340, o.H - 30, { size: 28, align: 'right' });
  }
  return S;
}

const K = 5;
const INPUTS = [
  { value: 'mixed', label: 'mixed', A: [4, 2, 12, 3, 8, 1, 6, 5, 9, 7, 10, 11] },
  { value: 'up', label: 'increasing', A: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] },
  { value: 'down', label: 'decreasing', A: [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] },
];
const bruteCmp = (n) => (n - K + 1) * (K - 1);

/* ================================================================ sim-brute: every window from scratch */
(function () {
  const PY = J([
    'def window_minima_brute(nums, k):',
    '    out = []',
    '    for lo in range(len(nums) - k + 1):',
    '        m = nums[lo]',
    '        for j in range(lo + 1, lo + k):',
    '            if nums[j] < m:',
    '                m = nums[j]',
    '        out.append(m)',
    '    return out',
  ]);
  const run = (A, k) => F.trace((at) => {
    const out = [], reads = A.map(() => 0); let cmp = 0;
    const V = (x) => Object.assign({ out: out.slice(), reads: reads.slice(), cmp }, x);
    at(2, V({}));
    for (let lo = 0; lo + k <= A.length; lo += 1) {
      at(3, V({ lo }));
      let m = A[lo], mi = lo; reads[lo] += 1; at(4, V({ lo, m, mi }));
      for (let j = lo + 1; j < lo + k; j += 1) {
        at(5, V({ lo, j, m, mi }));
        cmp += 1; reads[j] += 1; at(6, V({ lo, j, m, mi }));
        if (A[j] < m) { m = A[j]; mi = j; at(7, V({ lo, j, m, mi })); }
      }
      out.push(m); at(8, V({ lo, m, mi, done: 1 }));
    }
    at(9, V({ end: 1 }));
  });
  const d = sim('sim-brute', 520);
  const code = F.code(d, {
    lang: 'python', src: PY,
    blocks: [
      { id: 'win', lines: [3, 8], label: 'one window: find its minimum from scratch', touches: ['lo', 'm'] },
      { id: 'scan', lines: [5, 7], label: 'compare the next number with the smallest so far', touches: ['j', 'm'] },
    ],
    refs: { m: () => C('key') },
  });
  F.debug(d, {
    code, watch: ['lo', 'j', 'm'],
    inputs: INPUTS.map((x) => ({ value: x.value, label: x.label, trace: run(x.A, K), args: { k: K } })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const inp = INPUTS.find((x) => x.value === g.input) || INPUTS[0], A = inp.A, n = A.length;
      const v = g.frame.vars, L = g.frame.line, lo = typeof v.lo === 'number' ? v.lo : -1, hi = lo < 0 ? -1 : lo + K - 1;
      const mins = {}; (v.out || []).forEach((m, w) => { mins[w + K - 1] = m; });
      const worst = v.reads.reduce((a, b, j) => (b > v.reads[a] ? j : a), 0);
      let head;
      if (v.end) head = `${v.cmp} comparisons for ${n - K + 1} windows. ${A[worst]} was read ${v.reads[worst]} times.`;
      else if (lo < 0) head = `The minimum of every window of ${K} numbers. The obvious way: scan each window from its first number.`;
      else if (v.done) head = `The minimum of A[${lo}..${hi}] is ${v.m}, after ${K - 1} comparisons. The next window shares ${K - 1} of these ${K} numbers.`;
      else if (L === 7) head = `${A[v.j]} is the smallest so far.`;
      else if (L === 6) head = `${A[v.j]} ${A[v.j] < v.m ? '<' : '≥'} ${v.m}: ${A[v.j] < v.m ? 'a new smallest.' : 'the smallest so far stays.'}`;
      else head = `Window A[${lo}..${hi}]: start again from ${A[lo]}, as if nothing were known.`;
      topline(ctx, head);
      scene(ctx, {
        A, k: K, lo, hi, H: 520, mins,
        state: (j) => (v.end ? 'live' : lo >= 0 && j === v.mi ? 'min' : lo >= 0 && j === v.j && !v.done ? 'new' : 'live'),
        under: (j) => (v.reads[j] ? `×${v.reads[j]}` : ''), underName: 'times read',
        counts: [['comparisons', v.cmp], ['of (n − k + 1)(k − 1) =', bruteCmp(n)]],
      });
    },
  });
  rest(d);
})();

/* ================================================================ sim-insight: the reader strikes numbers out */
(function () {
  const A = INPUTS[0].A, n = A.length, ROUNDS = 5, H = 500;
  const d = sim('sim-insight', H);
  const fb = document.createElement('p');
  fb.style.cssText = 'margin:0;padding:14px 22px 18px;min-height:4.6em;font:inherit;line-height:1.5';
  const row = document.createElement('div'); row.className = 'ctlseg'; row.style.cssText = 'display:flex;flex-wrap:wrap;gap:8px;margin:0 auto';
  d.controls.appendChild(row); d.fig.appendChild(fb);
  const btn = (label, act, primary) => {
    const b = document.createElement('button'); b.type = 'button'; b.className = 'segbtn' + (primary ? ' on' : ''); b.textContent = label;
    b.style.cssText = 'padding:6px 14px;border-radius:6px'; b.addEventListener('click', act); return b;
  };
  let st;
  const start = () => { st = { r: 0, struck: new Set(), marks: new Set(), phase: 'ask', mins: {}, right: 0, asked: 0 }; };
  const lo = () => st.r, hi = () => st.r + K - 1;
  const cands = () => { const out = []; for (let j = lo(); j <= hi(); j += 1) if (!st.struck.has(j)) out.push(j); return out; };
  /* a candidate is hopeless when a smaller number stands to its right in the window */
  const beater = (j) => { for (let q = j + 1; q <= hi(); q += 1) if (A[q] < A[j]) return q; return -1; };
  const truth = () => new Set(cands().filter((j) => beater(j) >= 0));
  const list = (js) => js.map((j) => A[j]).join(', ');
  function ui() {
    row.replaceChildren();
    if (st.phase === 'end') {
      fb.textContent = `In ${ROUNDS} windows you never went back to a struck number, and the minimum was always the leftmost number still standing. Keep the standing numbers in a queue, oldest first, and that is the whole algorithm.`;
      row.append(btn('Start over', () => { start(); ui(); }, true));
    } else if (st.phase === 'ask') {
      fb.textContent = st.r === 0
        ? 'Click a number in the window to strike it out, click again to bring it back. Then check.'
        : `${A[hi()]} has arrived and ${A[lo() - 1]} has left. Click the numbers ${A[hi()]} finishes off, if any. Then check.`;
      row.append(btn('Check', check, true));
    } else {
      row.append(btn(st.r + 1 < ROUNDS ? 'Slide the window one step' : 'What was that?', slide, true));
    }
    F.redrawAll();
  }
  function check() {
    const T = truth(), M = st.marks;
    const missed = [...T].filter((j) => !M.has(j)), extra = [...M].filter((j) => !T.has(j));
    T.forEach((j) => st.struck.add(j)); st.marks = new Set(); st.phase = 'told'; st.asked += 1;
    const left = cands(), up = left.length > 1 ? ` Left standing: ${list(left)}, going up from left to right, so the minimum is the first, ${A[left[0]]}.` : ` Only ${A[left[0]]} is left standing, and it is the minimum.`;
    st.mins[hi()] = A[left[0]];
    if (!missed.length && !extra.length) {
      st.right += 1;
      fb.textContent = (T.size ? `Right. Each struck number has a smaller one to its right, which beats it now and stays in the window longer.` : `Right: nothing goes. ${A[hi()]} is larger than every number still standing, so each of them will leave before it can be beaten by ${A[hi()]}.`) + up;
    } else if (extra.length) {
      const j = extra[0];
      fb.textContent = `${A[j]} has to stay: no number to its right in the window is smaller, so once the smaller numbers before it have slid out, ${A[j]} is the minimum.` + (missed.length ? ` And ${A[missed[0]]} goes: ${A[beater(missed[0])]} to its right is smaller and stays longer.` : '') + up;
    } else {
      const j = missed[0];
      fb.textContent = `${A[j]} goes too: ${A[beater(j)]} to its right is smaller and stays in the window longer, so ${A[j]} never gets a turn.` + (missed.length > 1 ? ` The same for ${list(missed.slice(1))}.` : '') + up;
    }
    ui();
  }
  function slide() {
    if (st.r + 1 >= ROUNDS) { st.phase = 'end'; ui(); return; }
    st.r += 1; st.phase = 'ask'; ui();
  }
  d.c.style.cursor = 'pointer';
  d.c.addEventListener('click', (e) => {
    if (st.phase !== 'ask') return;
    const bb = d.c.getBoundingClientRect(), k = 1400 / bb.width, x = (e.clientX - bb.left) * k, y = (e.clientY - bb.top) * k;
    if (y < YA - HA / 2 - 10 || y > YA + HA / 2 + 40) return;
    const j = Math.floor((x - X0(n)) / CW);
    if (j < lo() || j > hi() || st.struck.has(j)) return;
    if (st.marks.has(j)) st.marks.delete(j); else st.marks.add(j);
    F.redrawAll();
  });
  function draw() {
    const { ctx } = F.begin(d.c);
    const end = st.phase === 'end';
    let head;
    if (end) head = 'A number with a smaller one to its right is finished for good.';
    else if (st.r === 0) head = st.phase === 'ask' ? 'This window is about to slide right, one step at a time. Which of its numbers can never be a minimum, now or later?' : `The minimum of A[0..${K - 1}] is ${st.mins[hi()]}.`;
    else head = st.phase === 'ask' ? `${A[hi()]} arrives. Which of the numbers still standing can never be a minimum again?` : `The minimum of A[${lo()}..${hi()}] is ${st.mins[hi()]}.`;
    topline(ctx, head);
    const left = cands();
    scene(ctx, {
      A, k: K, lo: lo(), hi: hi(), H, mins: st.mins,
      state: (j) => {
        if (j > hi()) return 'ahead';
        if (st.marks.has(j)) return 'mark';
        if (st.struck.has(j)) return 'struck';
        if (j < lo()) return 'gone';
        if (st.phase !== 'ask' && j === left[0]) return 'min';
        if (st.phase === 'ask' && st.r > 0 && j === hi()) return 'new';
        return 'cand';
      },
      counts: [['windows', st.asked], ['numbers struck for good', st.struck.size]],
    });
  }
  start();
  F.register(d.fig, { update: () => {}, draw, arrive: false });
  ui();
})();

/* ================================================================ sim-fast: the queue of numbers left standing */
(function () {
  const PY = J([
    'from collections import deque',
    '',
    'def window_minima(nums, k):',
    '    q = deque()',
    '    out = []',
    '    for i in range(len(nums)):',
    '        while q and nums[q[-1]] > nums[i]:',
    '            q.pop()',
    '        q.append(i)',
    '        if q[0] <= i - k:',
    '            q.popleft()',
    '        if i >= k - 1:',
    '            out.append(nums[q[0]])',
    '    return out',
  ]);
  const run = (A, k) => F.trace((at) => {
    const q = [], out = [], struck = []; let cmp = 0, cut = -1, left = -1;
    const V = (x) => Object.assign({ q: q.slice(), out: out.slice(), struck: struck.slice(), cmp, cut, left }, x);
    at(4, V({ i: -1 })); at(5, V({ i: -1 }));
    for (let i = 0; i < A.length; i += 1) {
      cut = -1; left = -1;
      at(6, V({ i }));
      while (q.length) {
        cmp += 1; at(7, V({ i }));
        if (!(A[q[q.length - 1]] > A[i])) break;
        cut = q.pop(); struck.push(cut); at(8, V({ i }));
      }
      if (!q.length) at(7, V({ i }));
      q.push(i); at(9, V({ i }));
      at(10, V({ i }));
      if (q[0] <= i - k) { left = q.shift(); at(11, V({ i })); }
      at(12, V({ i }));
      if (i >= k - 1) { out.push(A[q[0]]); at(13, V({ i, read: 1 })); }
    }
    at(14, V({ i: A.length - 1, end: 1 }));
  });
  const d = sim('sim-fast', 560);
  const code = F.code(d, {
    lang: 'python', src: PY,
    blocks: [
      { id: 'step', lines: [6, 13], label: 'one number arrives', touches: ['i'] },
      { id: 'cut', lines: [7, 8], label: 'the newcomer strikes out every larger number before it', touches: ['q'] },
      { id: 'push', lines: [9, 9], label: 'the newcomer stands, at the back of the queue', touches: ['q'] },
      { id: 'expire', lines: [10, 11], label: 'the oldest standing number leaves if the window has passed it', touches: ['q'] },
      { id: 'read', lines: [12, 13], label: 'the minimum is the oldest number still standing', touches: ['out'] },
    ],
    refs: { q: () => C('key'), i: () => C('index') },
  });
  F.debug(d, {
    code, level: 0, watch: ['i'],
    inputs: INPUTS.map((x) => ({ value: x.value, label: x.label, trace: run(x.A, K), args: { k: K } })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const inp = INPUTS.find((x) => x.value === g.input) || INPUTS[0], A = inp.A, n = A.length;
      const v = g.frame.vars, L = g.frame.line, i = v.i, hi = i, lo = Math.max(0, i - K + 1);
      const mins = {}; (v.out || []).forEach((m, w) => { mins[w + K - 1] = m; });
      const struck = new Set(v.struck), q = v.q;
      let head;
      if (v.end) head = `${v.cmp} comparisons, where the obvious way makes ${bruteCmp(n)}. Each number joined the queue once and was struck at most once.`;
      else if (i < 0) head = 'No number has arrived yet. The queue q will hold the numbers still standing, oldest first.';
      else if (L === 8) head = `${A[v.cut]} > ${A[i]}, and ${A[i]} stays in the window longer: ${A[v.cut]} is struck for good.`;
      else if (L === 7) head = q.length ? `${A[q[q.length - 1]]} ≤ ${A[i]}: the numbers still standing are all smaller than ${A[i]}, so none is struck.` : `Nothing is left standing before ${A[i]}.`;
      else if (L === 9) head = `${A[i]} stands at the back. Left to right the standing numbers go up: ${q.map((j) => A[j]).join(', ')}.`;
      else if (L === 11) head = `${A[v.left]} was the oldest standing, and the window has passed it.`;
      else if (L === 13) head = `The minimum of A[${lo}..${hi}] is the oldest number standing: ${A[q[0]]}. No scan.`;
      else if (L === 6) head = `${A[i]} arrives.`;
      else head = q.length ? `Standing: ${q.map((j) => A[j]).join(', ')}.` : '';
      topline(ctx, head);
      const S = scene(ctx, {
        A, k: K, lo: i < 0 ? 0 : lo, hi: i < 0 ? -1 : hi, H: 560, mins,
        state: (j) => {
          if (j > i) return 'ahead';
          if (struck.has(j)) return 'struck';
          if (!q.includes(j)) return j === i ? 'new' : 'gone';
          if (v.read && j === q[0]) return 'min';
          return j === i && L <= 9 ? 'new' : 'cand';
        },
        counts: [['comparisons', v.cmp], ['obvious way', bruteCmp(n)]],
      });
      /* the queue, written where the code reads it: indices, oldest first */
      text(ctx, 'q', S.l - 20, 460, C('key'), { size: 30, weight: 600, align: 'right' });
      text(ctx, q.length ? `indices ${q.join(', ')}  →  values ${q.map((j) => A[j]).join(', ')}` : 'empty', S.l, 460, PAL.ink, { size: 28, align: 'left' });
      if (q.length) text(ctx, 'oldest first; the first is the minimum', S.l, 496, PAL.muted, { size: 26, align: 'left' });
    },
  });
  rest(d);
})();
};
