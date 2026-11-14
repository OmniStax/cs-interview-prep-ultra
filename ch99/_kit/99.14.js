/* kit: ls */
/* 99.14 · stacks, harder · the largest rectangle in a histogram. The search space is the table of every stretch
   of bars, from bar l to bar r. The fast way measures one rectangle per bar; the rest of the table is tinted. */
(function () {
  const { C, PAL, alpha, text, line, topline } = F;
  const { clamp, ease, part } = LS;
  const Hh = [2, 1, 5, 6, 2, 3], N = Hh.length;
  const CW = 120, X0 = 110, BASE = 760, UN = 92, GX = 930, GY = 290, GC = 70;
  /* the obvious way: every stretch l..r, with the lowest bar in it */
  const BR = []; (function () { let best = 0; for (let l = 0; l < N; l += 1) { let low = Hh[l]; for (let r = l; r < N; r += 1) { low = Math.min(low, Hh[r]); const area = low * (r - l + 1); best = Math.max(best, area); BR.push({ l, r, low, area, best }); } } })();
  /* the fast way: a stack of bars still growing, each with where its rectangle starts */
  const EV = []; (function () { const st = [], got = []; let best = 0;
    const V = (x) => Object.assign({ st: st.map((s) => s.slice()), got: got.map((s) => Object.assign({}, s)), best }, x);
    Hh.concat([0]).forEach((x, i) => { let start = i;
      while (st.length && st[st.length - 1][1] >= x) { const [s, ht] = st.pop(); start = s; const area = ht * (i - s); best = Math.max(best, area); got.push({ l: s, r: i - 1, h: ht, area }); EV.push(V({ i, kind: 'pop', rect: got[got.length - 1] })); }
      if (i < N) { st.push([start, x]); EV.push(V({ i, kind: 'push' })); } }); })();
  const BEST = BR[BR.length - 1].best, GOT = EV[EV.length - 1].got;
  const TASK = EV.findIndex((e) => e.i === 4);               /* the bar 2 high arrives; 5 and 6 are still growing */

  const BRUTE = ['def largest(h):', '    best = 0', '    for l in range(len(h)):', '        low = h[l]', '        for r in range(l, len(h)):', '            low = min(low, h[r])', '            best = max(best, low * (r - l + 1))', '    return best'].join('\n');
  const FAST = ['def largest(h):', '    best = 0', '    stack = []', '    for i, x in enumerate(h + [0]):', '        start = i', '        while stack and stack[-1][1] >= x:', '            start, height = stack.pop()', '            best = max(best, height * (i - start))', '        stack.append((start, x))', '    return best'].join('\n');
  const nBr = (u) => (u < 0.4 ? Math.floor((u / 0.4) * 6) : Math.min(BR.length, 6 + Math.ceil(ease((u - 0.4) / 0.55) * (BR.length - 6))));
  const nEv = (u) => Math.min(EV.length, 1 + Math.floor(u * 1.05 * EV.length));
  const barHot = (j) => ({ id: j, x: X0 + (j + 0.5) * CW, y: BASE - (Hh[j] * UN) / 2, w: CW - 10, h: Hh[j] * UN - 6, label: 'the bar ' + Hh[j] + ' high' });

  LS.lesson(root, F, 'ls-hist', {
    H: 900, mode: 'timeline', nav: 'tabs', change: 'boxes',
    code: { brute: BRUTE, bad: [3, 7], badNote: 'every stretch of bars', fast: FAST, added: [3, 4, 5, 6, 7, 8, 9], addNote: 'one rectangle per bar' },
    phases: [
      { kind: 'Problem', title: 'The largest rectangle under a histogram', dur: 7,
        html: '<p>Six bars of width 1 stand side by side. A rectangle may span any stretch of neighbouring bars, and it can be no taller than the lowest bar it covers.</p><p>The task is the largest area such a rectangle can have.</p>',
        note: () => 'A rectangle is as tall as its lowest bar.' },
      { kind: 'Brute force', title: 'Every stretch of bars', dur: 10, show: 'brute',
        html: '<p>Every stretch from bar <i>l</i> to bar <i>r</i> is measured: its lowest bar times its width. The table on the right has one cell per stretch.</p>',
        lines: () => [5, 6, 7],
        note: (u) => (nBr(u) < 7 ? 'The first stretches, one at a time.' : 'The rest go the same way, so they run fast.') },
      { kind: 'Observation', title: 'The bar that stops a rectangle', dur: 13, show: 'bad',
        html: '<p class="obs">A bar\'s rectangle grows until a shorter bar arrives. At that moment its width is final, and so is its area.</p><p>So each bar has one rectangle worth measuring. The loops in the red box measure every stretch.</p>',
        tasks: [{ a: 0.04, b: 0.5, prompt: 'A bar 2 high arrives on the right. Press a bar whose rectangle can grow no further.',
          targets: () => [0, 1, 2, 3].map(barHot),
          check: (j) => (j >= 2 ? { ok: true, text: '5 and 6 are both taller than 2, so their rectangles end here: 6 × 1 = 6, and 5 × 2 = 10.' } : j === 1 ? 'The bar 1 high is shorter than 2. Its rectangle runs on under the new bar.' : 'This bar was finished earlier, when the bar 1 high arrived after it.') }],
        note: (u, a) => (a.asking() ? '' : 'A dashed outline is a rectangle still growing.') },
      { kind: 'Optimization', title: 'A stack of growing bars', dur: 9, show: 'change',
        html: '<p>The bars still growing are kept on a stack, shortest at the bottom. An arriving bar closes every bar on top that is at least as tall, measures each once, and takes over where the last of them started.</p>',
        note: () => `${GOT.length} rectangles measured. The tinted cells are stretches never measured.` },
      { kind: 'Trace', title: 'One run', dur: 15, show: 'fast',
        html: '<p>From bottom to top, the stack always goes up. Each bar is pushed once and popped once, so the whole run is one pass.</p>',
        lines: (u) => (EV[nEv(u) - 1].kind === 'pop' ? [6, 7, 8] : [9]),
        note: (u) => { const e = EV[nEv(u) - 1]; return e.kind === 'pop' ? `Closed: height ${e.rect.h}, bars ${e.rect.l} to ${e.rect.r}, area ${e.rect.area}.` : `The bar ${Hh[e.i]} high starts growing from bar ${e.st[e.st.length - 1][0]}.`; } },
      { kind: 'Insight', title: 'One candidate per bar', dur: 6,
        html: `<p class="obs">Each bar has one rectangle that matters, and it is known the moment a shorter bar arrives.</p><p>${GOT.length} rectangles measured, against ${BR.length}. The largest rectangle of ones in a grid is this problem once per row, with each row's histogram built from the rows above it.</p>`,
        note: () => `The largest area is ${BEST}.` },
    ],
    draw,
  });

  /* rects: [{l, r, h, style: 'cur' | 'open' | 'done' | 'best'}]; bar(j) -> 'ahead' | 'live' | 'new' */
  function hist(ctx, upto, rects, newBar) {
    const key = C('key'), idx = C('index');
    line(ctx, X0 - 20, BASE, X0 + N * CW + 20, BASE, PAL.ink, 3);
    Hh.forEach((h, j) => {
      const x = X0 + j * CW, ahead = j > upto;
      ctx.fillStyle = alpha(PAL.ink, ahead ? 0.12 : 0.5); ctx.fillRect(x + 3, BASE - h * UN, CW - 6, h * UN);
      if (j === newBar) { ctx.strokeStyle = PAL.ink; ctx.lineWidth = 6; ctx.strokeRect(x + 3, BASE - h * UN, CW - 6, h * UN); }
      text(ctx, String(h), x + CW / 2, BASE - h * UN - 26, ahead ? PAL.muted : PAL.ink, { size: 34, align: 'center' });
      text(ctx, String(j), x + CW / 2, BASE + 32, idx, { size: 28, align: 'center' });
    });
    rects.forEach((q) => {
      const x = X0 + q.l * CW, w = (q.r - q.l + 1) * CW, y = BASE - q.h * UN;
      ctx.save();
      if (q.style === 'open') { ctx.setLineDash([12, 9]); ctx.strokeStyle = key; ctx.lineWidth = 4; ctx.strokeRect(x + 2, y, w - 4, q.h * UN); }
      else { ctx.fillStyle = alpha(key, q.style === 'best' ? 0.42 : q.style === 'cur' ? 0.32 : 0.14); ctx.fillRect(x, y, w, q.h * UN); ctx.strokeStyle = key; ctx.lineWidth = q.style === 'done' ? 2.5 : 5; ctx.strokeRect(x + 2, y + 2, w - 4, q.h * UN - 4); }
      ctx.restore();
      if (q.style === 'cur' || q.style === 'best') text(ctx, `${q.h} × ${q.r - q.l + 1} = ${q.h * (q.r - q.l + 1)}`, x + w / 2, y + (q.h * UN) / 2, PAL.ink, { size: 36, weight: 600, align: 'center' });
    });
  }
  /* cell(l, r) -> {v, st: 'open' | 'known' | 'cur' | 'never' | 'best'} */
  function table(ctx, cell) {
    const key = C('key'), idx = C('index');
    text(ctx, 'every stretch: bar l to bar r', GX, GY - 76, PAL.muted, { size: 28 });
    for (let r = 0; r < N; r += 1) text(ctx, String(r), GX + (r + 0.5) * GC, GY - 26, idx, { size: 28, align: 'center' });
    text(ctx, 'r', GX + N * GC + 20, GY - 26, PAL.ink, { size: 30, italic: true }); text(ctx, 'l', GX - 22, GY - 26, PAL.ink, { size: 30, italic: true, align: 'right' });
    for (let l = 0; l < N; l += 1) {
      text(ctx, String(l), GX - 22, GY + (l + 0.5) * GC, idx, { size: 28, align: 'right' });
      for (let r = l; r < N; r += 1) {
        const q = cell(l, r), x = GX + r * GC, y = GY + l * GC;
        ctx.fillStyle = q.st === 'never' ? alpha(PAL.bad, 0.12) : q.st === 'open' ? PAL.panel : alpha(key, q.st === 'best' ? 0.45 : 0.16); ctx.fillRect(x, y, GC, GC);
        ctx.strokeStyle = alpha(PAL.ink, q.st === 'never' ? 0.15 : 0.4); ctx.lineWidth = 2; ctx.strokeRect(x, y, GC, GC);
        if (q.st === 'never') line(ctx, x + 14, y + GC - 14, x + GC - 14, y + 14, alpha(PAL.bad, 0.55), 2.5);
        else if (q.st !== 'open') text(ctx, String(q.v), x + GC / 2, y + GC / 2 + 1, PAL.ink, { size: 30, align: 'center', weight: q.st === 'best' ? 600 : 400 });
        if (q.st === 'cur') { ctx.strokeStyle = PAL.ink; ctx.lineWidth = 5; ctx.strokeRect(x + 3, y + 3, GC - 6, GC - 6); }
      }
    }
  }
  function count(ctx, n, words, best) {
    text(ctx, String(n), 1380, 110, C('cost'), { size: 76, weight: 600, align: 'right' }); text(ctx, words, 1380, 164, PAL.muted, { size: 28, align: 'right' });
    text(ctx, 'best ' + best, GX, 790, C('key'), { size: 44, weight: 600 });
  }
  function fast(ctx, e, all, asking) {
    const got = e.got, cur = e.kind === 'pop' && !asking && !all ? e.rect : null;
    hist(ctx, Math.min(e.i, N - 1), got.filter((q) => q !== cur).map((q) => Object.assign({ style: q.area === BEST && all ? 'best' : 'done' }, q)).concat(e.st.map(([s, h]) => ({ l: s, r: Math.min(e.i, N - 1), h, style: 'open' }))).concat(cur ? [Object.assign({ style: 'cur' }, cur)] : []), asking ? 4 : e.kind === 'push' ? e.i : -1);
    table(ctx, (l, r) => { const q = got.find((z) => z.l === l && z.r === r); return q ? { v: q.area, st: q === cur ? 'cur' : q.area === BEST && all ? 'best' : 'known' } : { st: all ? 'never' : 'open' }; });
    count(ctx, got.length, `rectangles measured, of ${BR.length}`, e.best);
  }

  function draw(g) {
    const ctx = g.ctx, ph = g.ph, u = g.u;
    if (ph === 0) { topline(ctx, 'Which rectangle under these bars is largest?'); hist(ctx, N, u > 0.5 ? [{ l: 2, r: 3, h: 5, style: 'best' }] : [{ l: 0, r: 5, h: 1, style: 'cur' }], -1); return; }
    if (ph === 1) {
      const n = nBr(u), s = BR[Math.max(0, n - 1)];
      topline(ctx, n ? `Bars ${s.l} to ${s.r}: lowest ${s.low}, width ${s.r - s.l + 1}, area ${s.area}.` : 'Every stretch, one after another.');
      hist(ctx, N, n ? [{ l: s.l, r: s.r, h: s.low, style: 'cur' }] : [], -1);
      table(ctx, (l, r) => { const k = BR.findIndex((z) => z.l === l && z.r === r); return k >= n ? { st: 'open' } : { v: BR[k].area, st: k === n - 1 ? 'cur' : 'known' }; });
      count(ctx, n, 'stretches measured', n ? s.best : 0); return;
    }
    if (ph === 2) {
      const done = g.solved(2, 0) || u >= 0.5;
      if (!done) { topline(ctx, 'A shorter bar arrives. Which rectangles end here?'); fast(ctx, EV[TASK - 1], false, true); return; }
      const e = EV[Math.min(TASK + 1, TASK + Math.floor(part(u, 0.5, 0.95) * 2))];
      topline(ctx, `The bar ${e.rect.h} high is closed: ${e.rect.h} × ${e.rect.r - e.rect.l + 1} = ${e.rect.area}.`); fast(ctx, e, false); return;
    }
    if (ph === 3) { topline(ctx, `${GOT.length} of the ${BR.length} stretches are ever measured.`); fast(ctx, EV[EV.length - 1], true); return; }
    if (ph === 4) { const e = EV[nEv(u) - 1]; topline(ctx, e.kind === 'pop' ? `A shorter bar closes the bar ${e.rect.h} high: area ${e.rect.area}.` : `The bar ${Hh[e.i]} high joins the stack.`); fast(ctx, e, false); return; }
    topline(ctx, `The largest rectangle has area ${BEST}.`); fast(ctx, EV[EV.length - 1], true);
  }
})();
