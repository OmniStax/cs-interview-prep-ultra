/* kit: ls */
/* 99.8 · dynamic programming · the fewest coins, in the app's own style, in six named phases.
   The search space is the tree of calls, each written as the question it asks, dp(3). Once the memo is in,
   the calls it makes unnecessary are tinted and struck, so the saving is a part of the tree the reader sees. */
(function () {
  const { C, PAL, alpha, text, line, topline } = F;
  const { clamp, ease, part } = LS;
  const COINS = [1, 3, 4], AMT = 6;
  const nodes = [];
  (function build(a, depth, parent, coin) { const n = { id: nodes.length, a, depth, parent, coin, kids: [] }; nodes.push(n); COINS.forEach((c) => { if (a - c >= 0) n.kids.push(build(a - c, depth + 1, n, c)); }); return n; })(AMT, 0, null, 0);
  let leaf = 0; const leaves = nodes.filter((n) => !n.kids.length).length;
  (function place(n) { n.kids.forEach(place); n.x = n.kids.length ? n.kids.reduce((s, k) => s + k.x, 0) / n.kids.length : 110 + (leaf++) * (1180 / (leaves - 1)); n.y = 170 + n.depth * 98; })(nodes[0]);
  const asked = (a) => nodes.filter((n) => n.a === a).length;
  const best = [0]; for (let a = 1; a <= AMT; a += 1) best[a] = 1 + Math.min(...COINS.filter((c) => c <= a).map((c) => best[a - c]));
  /* the run with a memo: which calls are made, which are answered from the memo, which are never made */
  const EV = [], done = new Set();
  (function visit(n) {
    if (n.a === 0) { n.kind = 'base'; EV.push({ n }); return; }
    if (done.has(n.a)) { n.kind = 'hit'; EV.push({ n }); (function skip(m) { m.kids.forEach((k) => { k.kind = 'skipped'; skip(k); }); })(n); return; }
    n.kind = 'run'; EV.push({ n }); n.kids.forEach(visit); done.add(n.a); EV.push({ n, ret: true });
  })(nodes[0]);
  const HITS = nodes.filter((n) => n.kind === 'hit'), SKIPPED = nodes.filter((n) => n.kind === 'skipped').length;
  const MADE = nodes.length - SKIPPED;
  const W = 124, HH = 52;

  const BRUTE = ['def dp(a):', '    if a == 0:', '        return 0', '    return 1 + min(dp(a - c) for c in coins if c <= a)'].join('\n');
  const MEMO = ['memo = {}', 'def dp(a):', '    if a == 0:', '        return 0', '    if a in memo:', '        return memo[a]', '    memo[a] = 1 + min(dp(a - c) for c in coins if c <= a)', '    return memo[a]'].join('\n');
  const nGrow = (u) => (u < 0.4 ? 1 + Math.floor((u / 0.4) * 6) : Math.min(nodes.length, 7 + Math.ceil(ease((u - 0.4) / 0.55) * (nodes.length - 7))));
  const nEv = (u) => Math.min(EV.length, Math.floor(u * 1.08 * EV.length));
  let pick = null;

  LS.lesson(root, F, 'ls-coins', {
    H: 1000, mode: 'timeline', nav: 'tabs', change: 'edit',
    code: { brute: BRUTE, bad: [4, 4], badNote: 'worked out again on every call', fast: MEMO, added: [1, 5, 6, 7, 8], addNote: 'look in the memo first' },
    phases: [
      { kind: 'Problem', title: 'The fewest coins for 6', dur: 8,
        html: '<p>Coins come in 1, 3 and 4, with no limit on how many of each. The task is the smallest number of coins that add up to 6.</p><p>Taking the largest coin first gives 4 + 1 + 1, three coins, while 3 + 3 needs two. So every choice of first coin has to be weighed.</p>',
        note: () => 'Largest first is not always fewest.' },
      { kind: 'Brute force', title: 'The recursion', dur: 10, show: 'brute',
        html: '<p><code>dp(a)</code> is the fewest coins that make <code>a</code>. Whichever coin goes first, what remains is the same question for a smaller amount, so each coin is tried and the best kept.</p>',
        lines: () => [4],
        note: (u) => (nGrow(u) < 8 ? 'Each box is one call, written as the question it asks.' : 'The rest of the tree grows the same way, so it runs fast.') },
      { kind: 'Observation', title: 'Repeated questions', dur: 13, show: 'bad',
        html: '<p class="obs">dp(a) depends only on a. However the call was reached, the answer is the same.</p><p>The line in the red box works it out again on every call, along with the whole tree under it.</p>',
        tasks: [{ a: 0.04, b: 0.5, prompt: 'Press two calls that ask the same question.',
          targets: () => nodes.map((n) => ({ id: n.id, x: n.x, y: n.y, w: W, h: HH, label: 'dp(' + n.a + ')', sel: pick === n.id })),
          check: (id) => {
            const n = nodes[id];
            if (pick == null) { if (asked(n.a) === 1) return `dp(${n.a}) is asked only once. Pick a call that appears more than once.`; pick = id; return { info: `dp(${n.a}). Now press another call that asks the same question.` }; }
            const m = nodes[pick]; pick = null;
            if (m.id === n.id) return { info: 'Press two calls that ask the same question.' };
            return m.a === n.a ? { ok: true, text: `dp(${n.a}) is asked ${asked(n.a)} times, and the tree under it is worked out each time.` } : `dp(${m.a}) and dp(${n.a}) are different questions. Find two with the same number.`;
          } }],
        note: (u, a) => { if (u < 0.5 && !a.solved(2)) return ''; const r = rep(u); return `dp(${r}) is asked ${asked(r)} times.`; } },
      { kind: 'Optimization', title: 'A memo', dur: 10, show: 'change',
        html: '<p>Each answer is stored the first time it is worked out. A later call for the same amount returns the stored answer, and the tree under it is never grown.</p>',
        note: (u) => { const k = Math.min(HITS.length, Math.floor(u * 1.15 * HITS.length)); return k ? `${k} repeated question${k === 1 ? '' : 's'} answered from the memo.` : 'The same tree, grown the obvious way.'; } },
      { kind: 'Trace', title: 'One run with the memo', dur: 16, show: 'fast',
        html: '<p>A dashed box is a call answered from the memo. The tinted boxes under it are calls that were never made.</p>',
        lines: (u) => { const k = nEv(u); if (!k) return [2]; const e = EV[k - 1]; return e.ret ? [7, 8] : e.n.kind === 'base' ? [3, 4] : e.n.kind === 'hit' ? [5, 6] : [7]; },
        note: (u) => { const k = nEv(u); if (!k) return ''; const e = EV[k - 1], a = e.n.a; return e.ret ? `dp(${a}) = ${best[a]}, stored in the memo.` : e.n.kind === 'base' ? 'dp(0) = 0. No coins make nothing.' : e.n.kind === 'hit' ? `dp(${a}) is in the memo: ${best[a]}, with no work.` : `dp(${a}) is not in the memo yet.`; } },
      { kind: 'Insight', title: 'One answer per question', dur: 6,
        html: `<p class="obs">When the same question comes up again and again, answer it once and keep the answer.</p><p>${MADE} calls, against ${nodes.length}, and the gap widens quickly as the amount grows. Read left to right, the memo is the table of the bottom-up version, where each cell is filled from the cells one, three and four places back.</p>`,
        note: () => `6 = 3 + 3: ${best[AMT]} coins.` },
    ],
    draw,
  });
  function rep(u) { const rs = []; for (let a = AMT; a >= 1; a -= 1) if (asked(a) > 1) rs.push(a); return rs[Math.min(rs.length - 1, Math.floor(part(u, 0.5, 1) * rs.length))]; }

  function box(ctx, n, o) {
    ctx.save(); ctx.globalAlpha = o.al == null ? 1 : o.al;
    ctx.beginPath(); ctx.roundRect(n.x - W / 2, n.y - HH / 2, W, HH, 12);
    ctx.fillStyle = o.fill || PAL.panel; ctx.fill(); ctx.strokeStyle = o.stroke || PAL.ink; ctx.lineWidth = o.lw || 2.5; if (o.dash) ctx.setLineDash([9, 7]); ctx.stroke();
    ctx.restore();
    text(ctx, o.label || `dp(${n.a})`, n.x, n.y + 1, o.ink || PAL.ink, { size: 30, align: 'center', weight: o.bold ? 600 : 400 });
    if (o.strike) line(ctx, n.x - W / 2 + 10, n.y + HH / 2 - 8, n.x + W / 2 - 10, n.y - HH / 2 + 8, alpha(PAL.bad, 0.7), 3);
  }
  function coin(ctx, x, y, v, al) { ctx.save(); ctx.globalAlpha = al; ctx.beginPath(); ctx.arc(x, y, 58, 0, 7); ctx.fillStyle = alpha(C('key'), 0.16); ctx.fill(); ctx.strokeStyle = C('key'); ctx.lineWidth = 5; ctx.stroke(); ctx.restore(); if (al > 0.5) text(ctx, String(v), x, y + 2, C('key'), { size: 60, weight: 600, align: 'center' }); }

  function draw(g) {
    const ctx = g.ctx, ph = g.ph, u = g.u, key = C('key'), cost = C('cost');
    if (ph === 0) {
      topline(ctx, 'Make 6 from coins of 1, 3 and 4, with as few coins as possible.');
      text(ctx, 'largest coin first', 150, 330, PAL.muted, { size: 36 });
      [4, 1, 1].forEach((v, i) => coin(ctx, 560 + i * 150, 330, v, part(u, 0.05 + i * 0.12, 0.2 + i * 0.12)));
      text(ctx, '3 coins', 1060, 330, PAL.ink, { size: 44, weight: 600 }, );
      text(ctx, 'the fewest', 150, 600, PAL.muted, { size: 36 });
      [3, 3].forEach((v, i) => coin(ctx, 560 + i * 150, 600, v, part(u, 0.5 + i * 0.12, 0.65 + i * 0.12)));
      if (u > 0.75) text(ctx, '2 coins', 1060, 600, key, { size: 44, weight: 600 });
      return;
    }
    const shown = ph === 1 ? nGrow(u) : nodes.length;
    const asking = ph === 2 && !(g.solved(2) || u >= 0.5), r = ph === 2 && !asking ? rep(u) : -1;
    const hits = ph === 3 ? HITS.slice(0, Math.min(HITS.length, Math.floor(u * 1.15 * HITS.length))) : [];
    const k = ph === 4 ? nEv(u) : ph === 5 ? EV.length : 0;
    const seen = new Map(); EV.slice(0, k).forEach((e) => { seen.set(e.n.id, e.ret ? 'ret' : seen.get(e.n.id) || 'in'); });
    const under = (n, m) => { for (let p = m.parent; p; p = p.parent) if (p === n) return true; return false; };
    const cutBy = (n) => (ph === 3 ? hits : ph >= 4 ? HITS.filter((h) => seen.has(h.id)) : []).some((h) => under(h, n));
    const isHit = (n) => (ph === 3 ? hits.includes(n) : ph >= 4 && n.kind === 'hit' && seen.has(n.id));
    /* the links */
    nodes.forEach((n) => { if (!n.parent || n.id >= shown) return; const cut = cutBy(n); line(ctx, n.parent.x, n.parent.y + HH / 2, n.x, n.y - HH / 2, alpha(cut ? PAL.bad : PAL.ink, cut ? 0.25 : ph >= 4 && !seen.has(n.id) ? 0.2 : 0.55), 2.5); });
    nodes.forEach((n) => {
      if (n.id >= shown) return;
      const cut = cutBy(n), hit = isHit(n);
      if (cut) { box(ctx, n, { fill: alpha(PAL.bad, 0.1), stroke: alpha(PAL.bad, 0.45), ink: alpha(PAL.ink, 0.4), strike: true }); return; }
      if (hit) { box(ctx, n, { dash: true, stroke: PAL.bad, lw: 3.5, fill: alpha(PAL.bad, 0.06), bold: true }); text(ctx, 'memo', n.x, n.y + HH / 2 + 20, PAL.bad, { size: 24, align: 'center' }); return; }
      if (ph === 2) { const on = asking ? pick === n.id : n.a === r; box(ctx, n, { fill: on ? alpha(key, 0.3) : PAL.panel, lw: on ? 4.5 : 2.5, bold: on, al: !asking && !on ? 0.3 : 1 }); return; }
      if (ph >= 4) { const s = seen.get(n.id), cur = k && EV[k - 1].n === n; box(ctx, n, { fill: s === 'ret' || (s && n.kind === 'base') ? alpha(key, 0.22) : PAL.panel, lw: cur ? 5 : 2.5, bold: cur, al: s ? 1 : 0.28 }); return; }
      box(ctx, n, { lw: ph === 1 && n.id === shown - 1 ? 5 : 2.5 });
    });
    /* the memo, a cell an amount */
    if (ph >= 3) {
      text(ctx, 'memo', 190, 900, PAL.ink, { size: 34, weight: 600, align: 'right' });
      for (let a = 0; a <= AMT; a += 1) {
        const x0 = 230 + a * 130, have = ph === 5 || (ph === 4 && (a === 0 ? k > 0 && EV.slice(0, k).some((e) => e.n.a === 0) : EV.slice(0, k).some((e) => e.ret && e.n.a === a)));
        ctx.fillStyle = have ? alpha(key, 0.2) : PAL.panel; ctx.fillRect(x0, 862, 120, 76); ctx.strokeStyle = PAL.ink; ctx.lineWidth = 2.5; ctx.strokeRect(x0, 862, 120, 76);
        text(ctx, `dp(${a})`, x0 + 60, 962, PAL.muted, { size: 26, align: 'center' });
        if (have) text(ctx, String(best[a]), x0 + 60, 902, key, { size: 44, weight: 600, align: 'center' });
      }
    }
    /* the count */
    const made = ph === 1 ? shown : ph === 3 ? nodes.length - nodes.filter(cutBy).length : ph >= 4 ? EV.slice(0, k).filter((e) => !e.ret).length : nodes.length;
    text(ctx, String(made), 60, 190, cost, { size: 84, weight: 600 });
    text(ctx, ph >= 3 ? `calls, of ${nodes.length}` : 'calls', 60, 250, PAL.muted, { size: 30 });
    let head;
    if (ph === 1) head = shown < nodes.length ? `dp(${nodes[shown - 1].a}) is called.` : `${nodes.length} calls to answer dp(${AMT}).`;
    else if (ph === 2) head = asking ? 'Which of these calls ask the same thing?' : `dp(${r}) appears ${asked(r)} times, with the same tree under it each time.`;
    else if (ph === 3) head = hits.length ? `dp(${hits[hits.length - 1].a}) is already known: the calls under it are never made.` : 'Now answer each question only the first time it is asked.';
    else if (ph === 4) head = k ? (EV[k - 1].ret ? `dp(${EV[k - 1].n.a}) = ${best[EV[k - 1].n.a]}` : EV[k - 1].n.kind === 'hit' ? `dp(${EV[k - 1].n.a}) comes straight from the memo.` : `dp(${EV[k - 1].n.a}) is called.`) : 'Start at dp(6) with an empty memo.';
    else head = `${MADE} calls, not ${nodes.length}. dp(6) = ${best[AMT]}.`;
    topline(ctx, head);
  }
})();
