/* kit: ls */
/* 99.13 · two pointers, harder · trapping rain water. Bars of height h stand in a row; water settles between
   them. The obvious way scans the whole row twice for every bar; the fast way reads each bar once. */
(function () {
  const { C, PAL, alpha, text, line, topline } = F;
  const { clamp, ease, part } = LS;
  const Hh = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], N = Hh.length;
  const CW = 96, X0 = 700 - (N * CW) / 2, BASE = 640, UN = 104;
  const LM = Hh.map((_, i) => Math.max(...Hh.slice(0, i + 1))), RM = Hh.map((_, i) => Math.max(...Hh.slice(i)));
  const WAT = Hh.map((h, i) => Math.min(LM[i], RM[i]) - h), TOTAL = WAT.reduce((a, b) => a + b, 0);
  /* the obvious way: for bar i, scan left, scan right, then the water */
  const BR = []; (function () { const reads = Hh.map(() => 0); let n = 0, w = 0;
    for (let i = 0; i < N; i += 1) { for (let j = 0; j <= i; j += 1) reads[j] += 1; n += i + 1; BR.push({ i, side: 'left', n, w, reads: reads.slice() });
      for (let j = i; j < N; j += 1) reads[j] += 1; n += N - i; BR.push({ i, side: 'right', n, w, reads: reads.slice() });
      w += WAT[i]; BR.push({ i, side: 'done', n, w, reads: reads.slice() }); } })();
  /* the fast way: one end moves at each step */
  const EV = []; (function () { let l = 0, r = N - 1, L = 0, R = 0, w = 0; const done = [];
    EV.push({ l, r, L, R, w, done: [], at: -1 });
    while (l < r) { if (Hh[l] < Hh[r]) { L = Math.max(L, Hh[l]); w += L - Hh[l]; done.push(l); l += 1; EV.push({ l, r, L, R, w, done: done.slice(), at: l - 1, side: 'l', add: L - Hh[l - 1] }); }
      else { R = Math.max(R, Hh[r]); w += R - Hh[r]; done.push(r); r -= 1; EV.push({ l, r, L, R, w, done: done.slice(), at: r + 1, side: 'r', add: R - Hh[r + 1] }); } } })();
  const READS = BR[BR.length - 1].n;

  const BRUTE = ['def trap(h):', '    water = 0', '    for i in range(len(h)):', '        left = max(h[:i + 1])', '        right = max(h[i:])', '        water += min(left, right) - h[i]', '    return water'].join('\n');
  const FAST = ['def trap(h):', '    water = 0', '    l, r = 0, len(h) - 1', '    left = right = 0', '    while l < r:', '        if h[l] < h[r]:', '            left = max(left, h[l])', '            water += left - h[l]', '            l += 1', '        else:', '            right = max(right, h[r])', '            water += right - h[r]', '            r -= 1', '    return water'].join('\n');
  const nBr = (u) => (u < 0.45 ? Math.floor((u / 0.45) * 7) : Math.min(BR.length, 7 + Math.ceil(ease((u - 0.45) / 0.5) * (BR.length - 7))));
  const nEv = (u) => Math.min(EV.length - 1, Math.floor(u * 1.06 * EV.length));
  const barHot = (j) => ({ id: j, x: X0 + (j + 0.5) * CW, y: BASE - 2 * UN, w: CW - 8, h: 4 * UN - 20, label: 'bar ' + j });

  LS.lesson(root, F, 'ls-rain', {
    H: 900, mode: 'scroll', nav: 'stepper', change: 'edit',
    code: { brute: BRUTE, bad: [4, 5], badNote: 'two scans of the row for every bar', fast: FAST, added: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], addNote: 'each bar read once' },
    phases: [
      { kind: 'Problem', title: 'Trapped rain water', dur: 8,
        html: '<p>Twelve bars of different heights stand side by side. Rain falls, and water stays wherever a lower bar has taller bars on both sides.</p><p>The task is the total amount of water held, counted in squares.</p>',
        note: (u) => (u < 0.45 ? 'The bars before the rain.' : `${TOTAL} squares of water stay.`) },
      { kind: 'Brute force', title: 'Two scans per bar', dur: 11, show: 'brute',
        html: '<p>The water over a bar rises to the lower of its two walls: the tallest bar to its left and the tallest to its right. For each bar, both walls are found by scanning the row.</p>',
        lines: (u) => { const s = BR[Math.max(0, nBr(u) - 1)]; return s.side === 'left' ? [4] : s.side === 'right' ? [5] : [6]; },
        note: (u) => (nBr(u) < 8 ? 'The first bars, one scan at a time.' : 'The other bars go the same way, so they run fast.') },
      { kind: 'Observation', title: 'The lower wall decides', dur: 14, show: 'bad',
        html: '<p class="obs">Only the lower of a bar\'s two walls matters. If a bar at least as tall as the left wall stands anywhere to the right, the left wall is the lower one, and the water over the bar is settled.</p><p>The two lines in the red box find both walls exactly, by reading the whole row again for every bar.</p>',
        tasks: [
          { a: 0.04, b: 0.4, prompt: 'The tallest bar left of bar 2 is 1 high. Bar 10, to its right, is 2 high. Press the bar whose water is now certain.',
            targets: () => [2, 10].map(barHot),
            check: (j) => (j === 2 ? { ok: true, text: 'Its left wall is 1, and something at least 2 high stands to its right. The lower wall is the left one: 1 − 0 = 1 square, whatever lies between.' } : 'Nothing is known about what stands to the left of bar 10 beyond bar 2. A taller bar may be hiding in the middle.') },
          { a: 0.5, b: 0.86, prompt: 'The tallest bar right of bar 9 is 2 high. Bar 3, to its left, is 2 high. Press the bar whose water is now certain.',
            targets: () => [3, 9].map(barHot),
            check: (j) => (j === 9 ? { ok: true, text: 'Its right wall is 2, and bar 3 on its left is at least as tall. The lower wall is the right one: 2 − 1 = 1 square.' } : 'The right wall of bar 3 depends on bars not read yet.') },
        ],
        note: () => 'A dashed line is the wall seen so far from that end.' },
      { kind: 'Optimization', title: 'Two ends, one pass', dur: 9, show: 'change',
        html: '<p>One pointer starts at each end, each with the tallest bar it has passed. The end with the lower bar is settled against its own wall and moves inward.</p>',
        note: (u) => `${EV[nEv(u)].done.length} of ${N} bars settled.` },
      { kind: 'Trace', title: 'One run', dur: 15, show: 'fast',
        html: '<p>At each step the lower of the two end bars is settled. Its wall is the tallest bar passed on its own side, and the other end guarantees a wall at least that tall.</p>',
        lines: (u) => { const e = EV[nEv(u)]; return e.at < 0 ? [3, 4] : e.side === 'l' ? [6, 7, 8, 9] : [10, 11, 12, 13]; },
        note: (u) => { const e = EV[nEv(u)]; if (e.at < 0) return 'One pointer at each end.'; const wall = e.side === 'l' ? e.L : e.R; return `Bar ${e.at}: wall ${wall}, height ${Hh[e.at]}, so ${e.add} square${e.add === 1 ? '' : 's'}.`; } },
      { kind: 'Insight', title: 'The lower side', dur: 6,
        html: `<p class="obs">When only the smaller of two quantities matters, the side that is already smaller can be settled without knowing the other exactly.</p><p>${N - 1} bars read, against ${READS} reads. The container that holds the most water is solved by the same move: the shorter side can never do better, so it is the one to give up.</p>`,
        note: () => `${TOTAL} squares of water.` },
    ],
    draw,
  });

  /* water(i) -> squares shown over bar i, or -1 for unknown; mark(i) -> '' | 'cur' | 'done' | 'end' */
  function scene(ctx, water, mark, under, walls) {
    const key = C('key'), idx = C('index');
    line(ctx, X0 - 20, BASE, X0 + N * CW + 20, BASE, PAL.ink, 3);
    Hh.forEach((h, i) => {
      const x = X0 + i * CW, m = mark(i), w = water(i);
      if (w > 0) { ctx.fillStyle = alpha(idx, 0.3); ctx.fillRect(x, BASE - (h + w) * UN, CW, w * UN); }
      if (h > 0) { ctx.fillStyle = m === 'done' ? alpha(PAL.ink, 0.32) : alpha(PAL.ink, 0.6); ctx.fillRect(x + 2, BASE - h * UN, CW - 4, h * UN); }
      if (m === 'cur' || m === 'end') { ctx.strokeStyle = m === 'cur' ? key : PAL.ink; ctx.lineWidth = 6; ctx.strokeRect(x + 3, BASE - Math.max(h, 0.12) * UN, CW - 6, Math.max(h, 0.12) * UN); }
      text(ctx, String(i), x + CW / 2, BASE + 30, alpha(idx, 1), { size: 28, align: 'center' });
      const s = under ? under(i) : ''; if (s) text(ctx, s, x + CW / 2, BASE + 72, PAL.muted, { size: 28, align: 'center' });
      if (w > 0) text(ctx, String(w), x + CW / 2, BASE - (h + w / 2) * UN, idx, { size: 34, weight: 600, align: 'center' });
    });
    (walls || []).forEach(([x1, x2, lv, lab]) => { if (lv <= 0) return; ctx.save(); ctx.setLineDash([12, 9]); ctx.strokeStyle = PAL.ink; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(x1, BASE - lv * UN); ctx.lineTo(x2, BASE - lv * UN); ctx.stroke(); ctx.restore(); text(ctx, lab, (x1 + x2) / 2, BASE - lv * UN - 24, PAL.ink, { size: 28, align: 'center' }); });
  }
  function counts(ctx, n, words, w) {
    text(ctx, String(n), 60, 150, C('cost'), { size: 76, weight: 600 }); text(ctx, words, 60, 204, PAL.muted, { size: 28 });
    text(ctx, String(w), 1340, 150, C('index'), { size: 76, weight: 600, align: 'right' }); text(ctx, 'squares of water', 1340, 204, PAL.muted, { size: 28, align: 'right' });
  }
  function fast(ctx, e) {
    const done = new Set(e.done);
    scene(ctx, (i) => (done.has(i) ? WAT[i] : 0), (i) => (i === e.at ? 'cur' : i === e.l || i === e.r ? 'end' : done.has(i) ? 'done' : ''), (i) => (i === e.l && i === e.r ? 'l r' : i === e.l ? 'l' : i === e.r ? 'r' : ''),
      [[X0, X0 + e.l * CW, e.L, 'left wall ' + e.L], [X0 + (e.r + 1) * CW, X0 + N * CW, e.R, 'right wall ' + e.R]]);
  }

  function draw(g) {
    const ctx = g.ctx, ph = g.ph, u = g.u;
    if (ph === 0) { const wet = u >= 0.45; topline(ctx, wet ? `Water stays between taller bars: ${TOTAL} squares here.` : 'How much rain do these bars hold?'); scene(ctx, (i) => (wet ? WAT[i] : 0), () => ''); return; }
    if (ph === 1) {
      const n = nBr(u), s = BR[Math.max(0, n - 1)], i = s.i;
      topline(ctx, !n ? 'Bar by bar.' : s.side === 'left' ? `Bar ${i}: scan left for the tallest bar. It is ${LM[i]}.` : s.side === 'right' ? `Bar ${i}: scan right for the tallest bar. It is ${RM[i]}.` : `Bar ${i}: min(${LM[i]}, ${RM[i]}) − ${Hh[i]} = ${WAT[i]}.`);
      scene(ctx, (j) => (j < i || (j === i && s.side === 'done') ? WAT[j] : 0), (j) => (n && j === i ? 'cur' : ''), (j) => (s.reads[j] && n ? '×' + s.reads[j] : ''),
        n && s.side !== 'done' ? [s.side === 'left' ? [X0, X0 + (i + 1) * CW, LM[i], 'tallest on the left'] : [X0 + i * CW, X0 + N * CW, RM[i], 'tallest on the right']] : []);
      text(ctx, 'times read', X0 - 14, BASE + 72, PAL.muted, { size: 26, align: 'right' });
      counts(ctx, n ? s.n : 0, 'bars read', n ? s.w : 0); return;
    }
    if (ph === 2) {
      /* the run stands before bar 2 is settled, then before bar 9 */
      const one = g.solved(2, 0) || u >= 0.4, two = g.solved(2, 1) || u >= 0.86, k = u < 0.5 ? (one ? 4 : 3) : two ? 6 : 5, e = EV[k];
      topline(ctx, g.asking ? 'Which bar is settled?' : `Bar ${e.at} is settled: ${e.add} square${e.add === 1 ? '' : 's'} of water.`);
      fast(ctx, g.asking ? Object.assign({}, e, { at: -1 }) : e); counts(ctx, e.done.length, 'bars read', e.w); return;
    }
    const e = ph === 5 ? EV[EV.length - 1] : EV[nEv(u)];
    topline(ctx, ph === 5 ? `${N - 1} bars read, not ${READS}.` : e.at < 0 ? 'One pointer at each end.' : `Bar ${e.at} is the lower end: settled against its own wall.`);
    fast(ctx, e); counts(ctx, e.done.length, `bars read, of ${READS}`, e.w);
  }
})();
