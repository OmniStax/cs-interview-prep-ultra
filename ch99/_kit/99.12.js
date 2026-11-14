/* kit: ls */
/* 99.12 · queues · the minimum of every window of k numbers (the monotonic queue). A number that can never be
   a minimum again is struck where it stands, so the queue is the unstruck numbers of the window. */
(function () {
  const { C, PAL, alpha, text, line, topline } = F;
  const { clamp, ease, part } = LS;
  const A = [4, 2, 12, 3, 8, 1, 6, 5, 9, 7, 10, 11], K = 5, N = A.length, NW = N - K + 1;
  const CW = 90, X0 = 760 - (N * CW) / 2, AY = 330, HA = 84;
  /* the obvious way: each window scanned from its first number */
  const BR = []; (function () { const reads = A.map(() => 0); let cmp = 0; const out = [];
    for (let lo = 0; lo < NW; lo += 1) { let mi = lo; reads[lo] += 1; BR.push({ lo, j: lo, mi, cmp, reads: reads.slice(), out: out.slice() });
      for (let j = lo + 1; j < lo + K; j += 1) { cmp += 1; reads[j] += 1; if (A[j] < A[mi]) mi = j; BR.push({ lo, j, mi, cmp, reads: reads.slice(), out: out.slice() }); }
      out.push(A[mi]); BR.push({ lo, j: lo + K - 1, mi, cmp, reads: reads.slice(), out: out.slice(), done: true }); } })();
  /* the queue: indices of the numbers still standing, oldest first */
  const EV = []; (function () { const q = [], out = [], struck = []; let cmp = 0;
    const V = (x) => Object.assign({ q: q.slice(), out: out.slice(), struck: struck.slice(), cmp }, x);
    for (let i = 0; i < N; i += 1) {
      while (q.length) { cmp += 1; if (!(A[q[q.length - 1]] > A[i])) { EV.push(V({ i, kind: 'keep' })); break; } const c = q.pop(); struck.push(c); EV.push(V({ i, kind: 'cut', c })); }
      q.push(i); EV.push(V({ i, kind: 'push' }));
      if (q[0] <= i - K) { const c = q.shift(); EV.push(V({ i, kind: 'left', c })); }
      if (i >= K - 1) { out.push(A[q[0]]); EV.push(V({ i, kind: 'read' })); }
    } })();
  const CMPB = BR[BR.length - 1].cmp, CMPF = EV[EV.length - 1].cmp;
  const beater = (j, hi) => { for (let q = j + 1; q <= hi; q += 1) if (A[q] < A[j]) return q; return -1; };

  const BRUTE = ['def window_minima(nums, k):', '    out = []', '    for lo in range(len(nums) - k + 1):', '        m = nums[lo]', '        for j in range(lo + 1, lo + k):', '            m = min(m, nums[j])', '        out.append(m)', '    return out'].join('\n');
  const FAST = ['def window_minima(nums, k):', '    out = []', '    q = deque()', '    for i in range(len(nums)):', '        while q and nums[q[-1]] > nums[i]:', '            q.pop()', '        q.append(i)', '        if q[0] <= i - k:', '            q.popleft()', '        if i >= k - 1:', '            out.append(nums[q[0]])', '    return out'].join('\n');
  const nBr = (u) => (u < 0.4 ? Math.floor((u / 0.4) * 7) : Math.min(BR.length, 7 + Math.ceil(ease((u - 0.4) / 0.55) * (BR.length - 7))));
  const nEv = (u) => Math.min(EV.length, 1 + Math.floor(u * 1.04 * EV.length));
  const cellHot = (j) => ({ id: j, x: X0 + (j + 0.5) * CW, y: AY, w: CW - 8, h: HA - 8, label: 'the number ' + A[j] });

  LS.lesson(root, F, 'ls-window', {
    H: 820, mode: 'timeline', nav: 'rail', change: 'edit',
    code: { brute: BRUTE, bad: [4, 6], badNote: 'starts again for every window', fast: FAST, added: [3, 5, 6, 7, 8, 9, 11], addNote: 'only the numbers still standing' },
    phases: [
      { kind: 'Problem', title: 'The minimum of every window', dur: 7,
        html: '<p>A window of five numbers slides along a row of twelve, one place at a time. The task is the smallest number in the window at each of its eight positions.</p>',
        note: () => 'Eight windows, eight minima.' },
      { kind: 'Brute force', title: 'Every window from scratch', dur: 10, show: 'brute',
        html: '<p>Each window is scanned from its first number to its last. Under each number is a count of how often it has been read.</p>',
        lines: (u) => { const s = BR[Math.max(0, nBr(u) - 1)]; return s.done ? [7] : s.j === s.lo ? [3, 4] : [5, 6]; },
        note: (u) => (nBr(u) < 8 ? 'The first window, one number at a time.' : 'The other windows go the same way, so they run fast.') },
      { kind: 'Observation', title: 'A number with a smaller one after it', dur: 14, show: 'bad',
        html: '<p class="obs">A number with a smaller one to its right can never be a minimum again. The smaller one beats it now and stays in the window longer.</p><p>The loop in the red box reads such numbers again in every window that holds them.</p>',
        tasks: [
          { a: 0.04, b: 0.4, prompt: 'This window is about to slide right. Press a number in it that can never be a minimum, now or later.',
            targets: () => [0, 1, 2, 3, 4].map(cellHot),
            check: (j) => { const b = beater(j, 4); return b >= 0 ? { ok: true, text: `${A[j]} has ${A[b]} to its right, which is smaller and leaves later. The same goes for ${j === 0 ? 12 : 4}.` } : j === 1 ? '2 is the minimum of this window.' : `Nothing to the right of ${A[j]} in the window is smaller. Once the numbers before it have left, ${A[j]} is the minimum.`; } },
          { a: 0.5, b: 0.86, prompt: '1 arrives. Press a number still standing that 1 finishes off.',
            targets: () => [1, 3, 4, 5].map(cellHot),
            check: (j) => (j === 5 ? '1 is the new arrival. Nothing is to its right yet.' : j === 2 ? '12 was struck already.' : { ok: true, text: `${A[j]} is larger than 1 and leaves the window first. So do the other two still standing: 1 strikes all three.` }) },
        ],
        note: () => 'A struck number is never read again.' },
      { kind: 'Optimization', title: 'A queue of the numbers still standing', dur: 9, show: 'change',
        html: '<p>The numbers still standing are kept in a queue, oldest first. An arriving number strikes every larger one at the back and joins. The oldest leaves when the window passes it. The minimum is whatever stands first.</p>',
        note: (u) => `${EV[nEv(u) - 1].struck.length} numbers struck so far.` },
      { kind: 'Trace', title: 'One run', dur: 16, show: 'fast',
        html: '<p>Read from oldest to newest, the numbers still standing always go up, so the first of them is the minimum. Each number joins the queue once and is struck at most once.</p>',
        lines: (u) => ({ cut: [5, 6], keep: [5], push: [7], left: [8, 9], read: [10, 11] }[EV[nEv(u) - 1].kind]),
        note: (u) => { const e = EV[nEv(u) - 1], v = A[e.i]; return e.kind === 'cut' ? `${A[e.c]} is larger than ${v} and leaves first: struck.` : e.kind === 'keep' ? `${A[e.q[e.q.length - 1]]} is not larger than ${v}: it stays.` : e.kind === 'push' ? `${v} joins at the back.` : e.kind === 'left' ? `${A[e.c]} was the oldest standing, and the window has passed it.` : `The minimum is the oldest number standing: ${A[e.q[0]]}.`; } },
      { kind: 'Insight', title: 'Beaten candidates', dur: 6,
        html: `<p class="obs">A candidate beaten by a newer one can be dropped for good.</p><p>${CMPF} comparisons, against ${CMPB}, and the count stays under twice the length of the row however wide the window is. The nearest smaller value to the left of each number is found the same way, with a stack in place of the queue.</p>`,
        note: () => 'The minima: ' + EV[EV.length - 1].out.join(', ') + '.' },
    ],
    draw,
  });

  /* st(j) -> 'ahead' | 'gone' | 'live' | 'stand' | 'struck' | 'min' | 'new' */
  function scene(ctx, lo, hi, st, under, mins) {
    const key = C('key'), idx = C('index');
    if (hi >= lo) { ctx.fillStyle = alpha(idx, 0.12); ctx.fillRect(X0 + lo * CW, AY - HA / 2 - 8, (hi - lo + 1) * CW, HA + 16); }
    A.forEach((v, j) => {
      const s = st(j), x = X0 + j * CW, dim = s === 'ahead' || s === 'gone';
      ctx.fillStyle = s === 'struck' ? alpha(PAL.bad, 0.1) : s === 'stand' || s === 'min' || s === 'new' ? alpha(key, 0.2) : PAL.panel; ctx.fillRect(x, AY - HA / 2, CW, HA);
      ctx.strokeStyle = alpha(PAL.ink, dim ? 0.25 : 1); ctx.lineWidth = s === 'min' || s === 'new' ? 6 : 2.5; ctx.strokeRect(x, AY - HA / 2, CW, HA);
      text(ctx, String(v), x + CW / 2, AY + 1, dim || s === 'struck' ? alpha(key, 0.4) : key, { size: 42, align: 'center', weight: s === 'min' ? 600 : 400 });
      if (s === 'struck') line(ctx, x + 16, AY + HA / 2 - 14, x + CW - 16, AY - HA / 2 + 14, alpha(PAL.bad, 0.7), 3.5);
      text(ctx, String(j), x + CW / 2, AY + HA / 2 + 30, alpha(idx, dim ? 0.45 : 1), { size: 28, align: 'center' });
      const w = under ? under(j) : ''; if (w) text(ctx, w, x + CW / 2, AY + HA / 2 + 70, PAL.muted, { size: 28, align: 'center' });
    });
    if (hi >= lo) { const x1 = X0 + lo * CW + 4, x2 = X0 + (hi + 1) * CW - 4, y = AY - HA / 2 - 26; line(ctx, x1, y, x2, y, PAL.ink, 3); line(ctx, x1, y - 10, x1, y + 10, PAL.ink, 3); line(ctx, x2, y - 10, x2, y + 10, PAL.ink, 3); text(ctx, `window, k = ${K}`, (x1 + x2) / 2, y - 30, PAL.ink, { size: 30, align: 'center' }); }
    if (under) text(ctx, 'times read', X0 - 16, AY + HA / 2 + 70, PAL.muted, { size: 26, align: 'right' });
    const ym = under ? 560 : 520;
    text(ctx, 'minima', X0 - 16, ym, PAL.ink, { size: 30, align: 'right' });
    (mins || []).forEach((m, w) => text(ctx, String(m), X0 + (w + K - 0.5) * CW, ym, key, { size: 40, align: 'center', weight: 600 }));
  }
  function count(ctx, n, words) { text(ctx, String(n), 1340, 690, C('cost'), { size: 84, weight: 600, align: 'right' }); text(ctx, words, 1340, 750, PAL.muted, { size: 28, align: 'right' }); }
  function fast(ctx, e, extraStruck) {
    const struck = new Set(e.struck.concat(extraStruck || [])), i = e.i, lo = Math.max(0, i - K + 1);
    scene(ctx, lo, i, (j) => (j > i ? 'ahead' : struck.has(j) ? 'struck' : !e.q.includes(j) ? (j === i ? 'new' : 'gone') : e.kind === 'read' && j === e.q[0] ? 'min' : j === i ? 'new' : 'stand'), null, e.out);
    text(ctx, 'queue', X0 - 16, 640, PAL.ink, { size: 30, align: 'right' });
    text(ctx, e.q.length ? e.q.map((j) => A[j]).join('   ') : 'empty', X0 + 10, 640, C('key'), { size: 40, weight: 600 });
    if (e.q.length) text(ctx, 'oldest first', X0 + 10, 690, PAL.muted, { size: 26 });
  }

  function draw(g) {
    const ctx = g.ctx, ph = g.ph, u = g.u;
    if (ph === 0) { topline(ctx, 'What is the smallest number in each window of five?'); scene(ctx, 0, K - 1, () => 'live', null, []); return; }
    if (ph === 1) {
      const n = nBr(u), s = BR[Math.max(0, n - 1)];
      topline(ctx, n === BR.length ? `${CMPB} comparisons. The numbers in the middle were read five times each.` : s.done ? `The minimum of this window is ${A[s.mi]}. The next window shares four of its five numbers.` : `Window ${s.lo + 1} of ${NW}: smallest so far ${A[s.mi]}.`);
      scene(ctx, s.lo, s.lo + K - 1, (j) => (j === s.mi ? 'min' : j === s.j && !s.done ? 'new' : 'live'), (j) => (s.reads[j] ? '×' + s.reads[j] : ''), s.out);
      count(ctx, s.cmp, 'comparisons'); return;
    }
    if (ph === 2) {
      const one = g.solved(2, 0) || u >= 0.4, two = g.solved(2, 1) || u >= 0.86, slid = u >= 0.5;
      const struck = (one ? [0, 2] : []).concat(two ? [1, 3, 4] : []), hi = slid ? 5 : 4, lo = slid ? 1 : 0;
      topline(ctx, g.asking ? (slid ? '1 arrives at the right.' : 'Which of these five can never be a minimum again?') : two ? 'Only 1 is left standing, and it is the minimum.' : slid ? '1 arrives.' : 'Still standing: 2, 3, 8. They go up from left to right, so the first is the minimum.');
      scene(ctx, lo, hi, (j) => (j > hi ? 'ahead' : struck.includes(j) ? 'struck' : j < lo ? 'gone' : j === 5 ? 'new' : 'stand'), null, slid ? [2] : one ? [2] : []);
      return;
    }
    if (ph === 3 || ph === 4) {
      const e = EV[nEv(u) - 1];
      topline(ctx, e.kind === 'cut' ? `${A[e.i]} arrives and strikes ${A[e.c]}.` : e.kind === 'read' ? `The minimum is the oldest number standing: ${A[e.q[0]]}.` : e.kind === 'left' ? `${A[e.c]} leaves at the front.` : e.kind === 'push' ? `${A[e.i]} joins the queue.` : `${A[e.i]} arrives.`);
      fast(ctx, e); count(ctx, e.cmp, `comparisons, of ${CMPB}`); return;
    }
    const e = EV[EV.length - 1];
    topline(ctx, `${CMPF} comparisons, not ${CMPB}.`); fast(ctx, e); count(ctx, e.cmp, `comparisons, of ${CMPB}`);
  }
})();
