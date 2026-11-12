/* kit: ls */
/* 99.10 · trees · the sum of the values in a range, in a binary search tree. In the app's own style, in six
   named phases. The subtrees the fast way never enters are tinted and struck. */
(function () {
  const { C, PAL, alpha, text, line, topline } = F;
  const { clamp, ease, part } = LS;
  const VAL = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93], LO = 30, HI = 60;     /* heap order: i's children are 2i + 1, 2i + 2 */
  const T = VAL.map((v, i) => { const d = Math.floor(Math.log2(i + 1)), k = i - (2 ** d - 1); return { i, v, d, x: 700 + (k - (2 ** d - 1) / 2) * (1240 / 2 ** d), y: 190 + d * 150, l: 2 * i + 1 < VAL.length ? 2 * i + 1 : -1, r: 2 * i + 2 < VAL.length ? 2 * i + 2 : -1 }; });
  const inR = (v) => v >= LO && v <= HI;
  const sub = (i) => (i < 0 ? [] : [i].concat(sub(T[i].l), sub(T[i].r)));
  const ALL = sub(0);                                        /* the obvious way's order: every node */
  /* the fast way: the nodes entered, and the subtrees skipped at each */
  const EV = [];
  (function go(i) { if (i < 0) return; const n = T[i], e = { i, skip: [] }; EV.push(e); if (n.v > LO) go(n.l); else if (n.l >= 0) e.skip.push(n.l); if (n.v < HI) go(n.r); else if (n.r >= 0) e.skip.push(n.r); })(0);
  /* a skip is decided when its node is entered, so order the events to show it then */
  const CUTS = EV.filter((e) => e.skip.length).map((e) => ({ at: e.i, root: e.skip[0], side: e.skip[0] === T[e.i].l ? 'left' : 'right' }));
  const SUM = VAL.filter(inR).reduce((a, b) => a + b, 0);
  const AX = (v) => 110 + (v / 100) * 1180, AY = 880;

  const BRUTE = ['def range_sum(node, lo, hi):', '    if node is None:', '        return 0', '    total = node.val if lo <= node.val <= hi else 0', '    total += range_sum(node.left, lo, hi)', '    total += range_sum(node.right, lo, hi)', '    return total'].join('\n');
  const FAST = ['def range_sum(node, lo, hi):', '    if node is None:', '        return 0', '    total = node.val if lo <= node.val <= hi else 0', '    if node.val > lo:', '        total += range_sum(node.left, lo, hi)', '    if node.val < hi:', '        total += range_sum(node.right, lo, hi)', '    return total'].join('\n');
  const nAll = (u) => Math.min(ALL.length, Math.floor(u * 1.1 * (ALL.length + 1)));
  const nEv = (u) => Math.min(EV.length, Math.floor(u * 1.1 * (EV.length + 1)));
  const press = (at, want, low) => ({
    targets: () => [T[at].l, T[at].r].map((c) => ({ id: c, x: T[c].x, y: T[c].y, r: 54, label: 'the subtree under ' + T[c].v })),
    check: (c) => {
      const v = T[at].v;
      if (c === want) return { ok: true, text: low ? `Everything to the left of ${v} is smaller than ${v}, so smaller than ${LO}. None of it can be in the range.` : `Everything to the right of ${v} is larger than ${v}, so larger than ${HI}. None of it can be in the range.` };
      return low ? `Everything to the right of ${v} is larger than ${v}, so some of it may be ${LO} or more. It has to be looked at.` : `Everything to the left of ${v} is smaller than ${v}, so some of it may be ${HI} or less. It has to be looked at.`;
    },
  });

  LS.lesson(root, F, 'ls-range', {
    H: 960, mode: 'timeline',
    phases: [
      { kind: 'Problem', title: 'Add up the values from 30 to 60', dur: 7,
        html: '<p>A binary search tree holds fifteen numbers. At every node, everything in its left subtree is smaller and everything in its right subtree is larger.</p><p>Add up all the values that lie between 30 and 60. The strip under the tree marks the range.</p>',
        note: () => 'Left of a node is smaller; right of it is larger.' },
      { kind: 'Brute force', title: 'Visit every node', dur: 9, code: { src: BRUTE },
        html: '<p>Walk the whole tree. At each node, add its value if it is in the range, then go on into both subtrees.</p><p>This would work on any tree. It never uses the order.</p>',
        lines: (u) => { const k = nAll(u); return k ? (inR(T[ALL[k - 1]].v) ? [4] : [4, 5, 6]) : [1]; },
        note: (u) => { const k = nAll(u); return k ? `${T[ALL[k - 1]].v} is ${inR(T[ALL[k - 1]].v) ? 'in the range: added' : 'outside the range'}.` : ''; } },
      { kind: 'Observation', title: 'One comparison, a whole subtree', dur: 14,
        html: '<p>Stop at a node that is outside the range and ask what it says about its subtrees.</p><p class="obs">A node below the range rules out its whole left subtree, and a node above the range rules out its whole right subtree.</p>',
        tasks: [
          Object.assign({ a: 0.04, b: 0.42, prompt: '25 is below 30. Press the child of 25 whose whole subtree can be skipped.' }, press(1, 3, true)),
          Object.assign({ a: 0.5, b: 0.88, prompt: '75 is above 60. Press the child of 75 whose whole subtree can be skipped.' }, press(2, 6, false)),
        ],
        note: (u, a) => (a.asking() ? '' : u < 0.5 ? 'The left subtree of 25 holds only values below 25.' : 'The right subtree of 75 holds only values above 75.') },
      { kind: 'Optimization', title: 'Only go where the range can be', dur: 9, code: { src: FAST, added: [5, 7] },
        html: '<p>Apply the observation: go left only if the node is above the bottom of the range, and right only if it is below the top. Two comparisons, and whole subtrees are never entered.</p>',
        lines: (u) => { const k = Math.min(CUTS.length, Math.floor(u * 1.2 * (CUTS.length + 1))); return k ? (CUTS[k - 1].side === 'left' ? [5] : [7]) : [5, 7]; },
        note: (u) => { const k = Math.min(CUTS.length, Math.floor(u * 1.2 * (CUTS.length + 1))); return k ? `At ${T[CUTS[k - 1].at].v}: the ${CUTS[k - 1].side} subtree is never entered.` : 'The same tree, walked the obvious way.'; } },
      { kind: 'Trace', title: 'One run, node by node', dur: 14, code: { src: FAST, added: [5, 7] },
        html: '<p>Follow the walk. A tinted subtree was skipped when its parent was reached.</p>',
        lines: (u) => { const k = nEv(u); if (!k) return [1]; const e = EV[k - 1]; return e.skip.length ? (e.skip[0] === T[e.i].l ? [4, 5] : [4, 7]) : [4]; },
        note: (u) => { const k = nEv(u); if (!k) return ''; const e = EV[k - 1], n = T[e.i]; return `${n.v} is ${inR(n.v) ? 'in the range: added' : n.v < LO ? 'below the range' : 'above the range'}${e.skip.length ? `; its ${e.skip.length === 2 ? 'subtrees are' : (e.skip[0] === n.l ? 'left' : 'right') + ' subtree is'} skipped` : ''}.`; } },
      { kind: 'Insight', title: 'Order turns one comparison into many', dur: 6,
        html: `<p class="obs">On ordered data, one comparison rules out a whole subtree.</p><p>${EV.length} nodes entered where the obvious way enters ${ALL.length}. On a balanced tree with a narrow range the saving grows with the tree: the walk follows the two edges of the range and little else. Binary search is the same insight with a range of one value.</p>`,
        note: () => `The sum is ${SUM}.` },
    ],
    draw,
  });

  function draw(g) {
    const ctx = g.ctx, ph = g.ph, u = g.u, key = C('key'), cost = C('cost');
    /* which nodes have been entered, and which subtrees are skipped */
    let entered = [], cuts = [], cur = -1;
    if (ph === 1) { entered = ALL.slice(0, nAll(u)); cur = entered[entered.length - 1]; }
    else if (ph === 2) {
      const first = g.solved(2, 0) || u >= 0.42, second = g.solved(2, 1) || u >= 0.88;
      entered = u < 0.5 ? [0, 1] : [0, 1, 4, 9, 10, 2]; cur = u < 0.5 ? 1 : 2;
      if (first) cuts.push(CUTS[0]); if (u >= 0.5 && second) cuts.push(CUTS[1]);
    } else if (ph === 3) { entered = ALL.slice(); cuts = CUTS.slice(0, Math.min(CUTS.length, Math.floor(u * 1.2 * (CUTS.length + 1)))); }
    else if (ph >= 4) { const k = ph === 4 ? nEv(u) : EV.length; entered = EV.slice(0, k).map((e) => e.i); cur = ph === 4 && k ? entered[k - 1] : -1; cuts = CUTS.filter((c) => entered.includes(c.at)); }
    const cutSet = new Set(); cuts.forEach((c) => sub(c.root).forEach((i) => cutSet.add(i)));
    const total = entered.filter((i) => !cutSet.has(i) && inR(T[i].v)).reduce((a, i) => a + T[i].v, 0);

    /* the range strip */
    ctx.fillStyle = alpha(key, 0.22); ctx.fillRect(AX(LO), AY - 24, AX(HI) - AX(LO), 48);
    line(ctx, AX(0), AY, AX(100), AY, PAL.ink, 2.5);
    [LO, HI].forEach((v) => { line(ctx, AX(v), AY - 30, AX(v), AY + 30, key, 4); text(ctx, String(v), AX(v), AY + 52, key, { size: 32, weight: 600, align: 'center' }); });
    T.forEach((n) => { ctx.beginPath(); ctx.arc(AX(n.v), AY, 7, 0, 7); ctx.fillStyle = cutSet.has(n.i) ? alpha(PAL.bad, 0.5) : inR(n.v) ? key : alpha(PAL.ink, 0.45); ctx.fill(); });
    /* the tree */
    T.forEach((n) => [n.l, n.r].forEach((c) => { if (c >= 0) line(ctx, n.x, n.y, T[c].x, T[c].y, cutSet.has(c) ? alpha(PAL.bad, 0.3) : alpha(PAL.ink, entered.includes(c) || ph === 0 ? 0.6 : 0.25), 3); }));
    T.forEach((n) => {
      const cut = cutSet.has(n.i), on = entered.includes(n.i) && !cut, hit = on && inR(n.v);
      ctx.beginPath(); ctx.arc(n.x, n.y, 44, 0, 7);
      ctx.fillStyle = PAL.panel; ctx.fill(); if (cut || hit) { ctx.fillStyle = cut ? alpha(PAL.bad, 0.12) : alpha(key, 0.32); ctx.fill(); }
      ctx.strokeStyle = cut ? alpha(PAL.bad, 0.5) : on || ph === 0 ? PAL.ink : alpha(PAL.ink, 0.3); ctx.lineWidth = n.i === cur ? 7 : on ? 4 : 2.5; ctx.stroke();
      text(ctx, String(n.v), n.x, n.y + 1, cut ? alpha(PAL.ink, 0.4) : on || ph === 0 ? PAL.ink : PAL.muted, { size: 36, weight: on ? 600 : 400, align: 'center' });
      if (cut) line(ctx, n.x - 30, n.y + 30, n.x + 30, n.y - 30, alpha(PAL.bad, 0.7), 3);
    });
    /* the counts */
    if (ph >= 1) {
      text(ctx, String(entered.filter((i) => !cutSet.has(i)).length), 60, 150, cost, { size: 76, weight: 600 });
      text(ctx, `nodes entered, of ${ALL.length}`, 60, 204, PAL.muted, { size: 28 });
      text(ctx, String(total), 1340, 150, key, { size: 76, weight: 600, align: 'right' });
      text(ctx, 'sum so far', 1340, 204, PAL.muted, { size: 28, align: 'right' });
    }
    let head;
    if (ph === 0) head = `Which values lie between ${LO} and ${HI}, and what do they add up to?`;
    else if (ph === 1) head = cur >= 0 ? `At ${T[cur].v}: ${inR(T[cur].v) ? 'in the range, added' : 'not in the range'}. Then into both subtrees.` : 'Walk the whole tree.';
    else if (ph === 2) head = g.asking ? `${T[cur].v} is ${T[cur].v < LO ? 'below' : 'above'} the range. What does that rule out?` : `${T[cur].v} is ${T[cur].v < LO ? 'below' : 'above'} the range, so its ${T[cur].v < LO ? 'left' : 'right'} subtree holds nothing in it.`;
    else if (ph === 3) head = cuts.length ? `${cutSet.size} nodes sit in subtrees that are never entered.` : 'Every node is entered. Now use the order.';
    else if (ph === 4) head = cur >= 0 ? `At ${T[cur].v}.` : 'Start at the root.';
    else head = `${EV.length} nodes entered, not ${ALL.length}. The sum is ${SUM}.`;
    topline(ctx, head);
  }
})();
