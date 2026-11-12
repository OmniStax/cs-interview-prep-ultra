/* kit: ls */
/* 99.7 · backtracking · four queens, in the app's own style, in six named phases.
   The search space is a wheel: a ring a row (centre out), a wedge a choice of column. What the fast way never
   fills is tinted, so the saving is an area the reader can see. */
(function () {
  const { C, PAL, alpha, text, line, topline } = F;
  const { clamp, ease, part } = LS;
  const NQ = 4;
  const clash = (p) => { for (let i = 0; i < p.length; i += 1) for (let j = i + 1; j < p.length; j += 1) if (p[i] === p[j] || Math.abs(p[i] - p[j]) === j - i) return [i, j]; return null; };
  const idx = (p) => p.reduce((s, c) => s * NQ + c, 0);
  const prefix = (d, i) => { const p = []; for (let k = 0; k < d; k += 1) { p.unshift(i % NQ); i = Math.floor(i / NQ); } return p; };
  const LEAVES = []; for (let i = 0; i < NQ ** NQ; i += 1) LEAVES.push(prefix(NQ, i));
  const VISITS = [];
  (function go(p) { for (let c = 0; c < NQ; c += 1) { const q = p.concat(c), bad = !!clash(q); VISITS.push({ p: q, bad }); if (!bad && q.length < NQ) go(q); } })([]);
  /* the clashing wedges, in the order the search meets them, and how many full boards each one spares */
  const CUTS = VISITS.filter((v) => v.bad).map((v) => ({ p: v.p, spared: NQ ** (NQ - v.p.length) }));
  const EX = [0, 1, 3, 2];                                 /* the failing board of the Observation phase */
  const CX = 470, CY = 580, R0 = 78, RW = 92, BX = 1000, BY = 150, CS = 88;
  const under = (p, q) => q.length <= p.length && q.every((c, i) => p[i] === c);     /* p lies under (or is) q */

  const BRUTE = ['def queens_brute(n):', '    found = []', '    for board in product(range(n), repeat=n):', '        if not clashes(board):', '            found.append(board)', '    return found'].join('\n');
  const FAST = ['def queens(n, board=()):', '    if len(board) == n:', '        return [board]', '    found = []', '    for col in range(n):', '        if clashes(board + (col,)):', '            continue', '        found += queens(n, board + (col,))', '    return found'].join('\n');
  const nBrute = (u) => (u < 0.4 ? Math.floor((u / 0.4) * 6) : Math.min(LEAVES.length, 6 + Math.ceil(ease((u - 0.4) / 0.55) * (LEAVES.length - 6))));
  const nTrace = (u) => Math.min(VISITS.length, Math.floor(u * 1.08 * VISITS.length));
  let hover = null;

  const api = LS.lesson(root, F, 'ls-queens', {
    H: 1060, mode: 'scroll',
    phases: [
      { kind: 'Problem', title: 'Four queens, no two attacking', dur: 8,
        html: '<p>Put one queen in each row of a 4 × 4 board so that no two share a column or a diagonal. Find every way to do it.</p><p>The wheel holds every way to try. Each ring is a row, from the centre out, and each wedge is a choice of column for that row. The outer ring has 256 wedges, one for each way to fill the board.</p><p>Point at any wedge to see the board it stands for.</p>',
        note: () => 'A ring is a row; a wedge is a column chosen for it.' },
      { kind: 'Brute force', title: 'Fill the board, then check it', dur: 10, code: { src: BRUTE },
        html: '<p>Take all 256 full boards one after another and test each. Every board costs four queens put down, 1,024 in all.</p>',
        lines: (u) => { const n = nBrute(u); return n === 0 ? [3] : clash(LEAVES[n - 1]) ? [3, 4] : [4, 5]; },
        note: (u) => (nBrute(u) < 7 ? 'The first boards, one at a time.' : 'The rest go the same way, so they run fast.') },
      { kind: 'Observation', title: 'Where a board goes wrong', dur: 13,
        html: '<p>Take one failing board and ask when it was lost.</p><p class="obs">A clash between two queens is not undone by the queens placed after them.</p><p>So every board that begins with a clash fails, and for the same reason. The 16 boards that begin like this one differ only in rows 3 and 4.</p>',
        tasks: [{ a: 0.04, b: 0.5, prompt: 'This board fails. Press the first queen that could never stay, whatever was placed after it.',
          targets: () => EX.map((c, r) => ({ id: r, x: BX + (c + 0.5) * CS, y: BY + (r + 0.5) * CS, w: CS - 6, h: CS - 6, label: 'the queen in row ' + (r + 1) })),
          check: (r) => (r === 1 ? { ok: true, text: 'Rows 1 and 2 already attack each other. Nothing put in rows 3 and 4 can change that.' } : r === 0 ? 'The queen in row 1 went onto an empty board: it attacked nothing when it was placed.' : `By row ${r + 1} the board was already lost. Look higher up.`) }],
        note: (u, a) => (u < 0.5 && !a.solved(2) ? '' : 'All 16 boards that begin this way fail for the same reason.') },
      { kind: 'Optimization', title: 'Check each queen as it goes down', dur: 10, code: { src: FAST, added: [6, 7] },
        html: '<p>Apply the observation: put down one queen at a time, check it against the ones above, and on a clash stop and try the next column. Everything outside a clashing wedge is never filled.</p>',
        lines: () => [6, 7],
        note: (u) => { const k = Math.min(CUTS.length, Math.floor(u * 1.15 * CUTS.length)); return k ? `${k} clashing wedge${k === 1 ? '' : 's'} cut: ${CUTS.slice(0, k).reduce((s, q) => s + q.spared, 0)} boards never filled.` : 'The same wheel, filled the obvious way.'; } },
      { kind: 'Trace', title: 'One run, queen by queen', dur: 16, code: { src: FAST, added: [6, 7] },
        html: '<p>Follow the search. A red wedge is a queen taken back at once; the tinted area outside it was never touched.</p>',
        lines: (u) => { const n = nTrace(u); if (!n) return [5]; const v = VISITS[n - 1]; return v.bad ? [6, 7] : v.p.length === NQ ? [2, 3] : [8]; },
        note: (u) => { const n = nTrace(u); if (!n) return ''; const v = VISITS[n - 1]; return v.bad ? `Row ${v.p.length}, column ${v.p[v.p.length - 1] + 1}: clash. Taken back.` : v.p.length === NQ ? 'Four queens and no clash: a solution.' : `Row ${v.p.length}, column ${v.p[v.p.length - 1] + 1}: no clash. Go on to the next row.`; } },
      { kind: 'Insight', title: 'Drop what cannot be repaired', dur: 6,
        html: `<p class="obs">A partial answer that already breaks the rule cannot be repaired by adding to it. Drop everything that starts with it.</p><p>${VISITS.length} queens put down, where the obvious way put down 1,024. The same insight prunes Sudoku, subset sums and permutations with constraints: check as early as the rule can be checked.</p>`,
        note: () => 'The tinted area is the work that was never done.' },
    ],
    draw,
  });

  const cv = api && root.querySelector('#ls-queens canvas, figure[id$="ls-queens"] canvas');
  if (cv) {
    cv.addEventListener('pointermove', (e) => {
      const b = cv.getBoundingClientRect(), k = 1400 / b.width, px = (e.clientX - b.left) * k, py = (e.clientY - b.top) * k, r = Math.hypot(px - CX, py - CY), d = Math.floor((r - R0) / RW) + 1;
      let h = null;
      if (d >= 1 && d <= NQ) { let a = Math.atan2(py - CY, px - CX) + Math.PI / 2; if (a < 0) a += 2 * Math.PI; h = prefix(d, Math.floor(a / ((2 * Math.PI) / NQ ** d))); }
      if (JSON.stringify(h) !== JSON.stringify(hover)) { hover = h; api.redraw(); }
    });
    cv.addEventListener('pointerleave', () => { hover = null; api.redraw(); });
  }

  function wedge(ctx, d, i, fill, stroke, lw) {
    const span = (2 * Math.PI) / NQ ** d, a0 = i * span - Math.PI / 2, a1 = a0 + span, r0 = R0 + (d - 1) * RW, r1 = r0 + RW - 4;
    ctx.beginPath(); ctx.arc(CX, CY, r1, a0, a1); ctx.arc(CX, CY, r0, a1, a0, true); ctx.closePath();
    if (fill) { ctx.fillStyle = fill; ctx.fill(); }
    ctx.strokeStyle = stroke; ctx.lineWidth = lw; ctx.stroke();
  }
  function board(ctx, p) {
    for (let r = 0; r < NQ; r += 1) for (let c = 0; c < NQ; c += 1) { ctx.fillStyle = (r + c) % 2 ? PAL.soft2 : PAL.panel; ctx.fillRect(BX + c * CS, BY + r * CS, CS, CS); }
    ctx.strokeStyle = PAL.ink; ctx.lineWidth = 3; ctx.strokeRect(BX, BY, NQ * CS, NQ * CS);
    const bad = clash(p);
    p.forEach((c, r) => text(ctx, '♛', BX + (c + 0.5) * CS, BY + (r + 0.54) * CS, bad && (r === bad[0] || r === bad[1]) ? PAL.bad : PAL.ink, { size: 62, align: 'center' }));
    if (bad) line(ctx, BX + (p[bad[0]] + 0.5) * CS, BY + (bad[0] + 0.5) * CS, BX + (p[bad[1]] + 0.5) * CS, BY + (bad[1] + 0.5) * CS, PAL.bad, 6);
    for (let r = 0; r < NQ; r += 1) text(ctx, 'row ' + (r + 1), BX - 14, BY + (r + 0.5) * CS, r < p.length ? PAL.ink : PAL.muted, { size: 28, align: 'right' });
  }
  function count(ctx, y, n, words, color) {
    text(ctx, String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ','), BX + NQ * CS, y, color, { size: 84, weight: 600, align: 'right' });
    text(ctx, words, BX + NQ * CS, y + 62, PAL.muted, { size: 30, align: 'right' });
  }

  function draw(g) {
    const ctx = g.ctx, ph = g.ph, u = g.u, key = C('key'), cost = C('cost');
    const asked = ph === 2 && (g.solved(2) || u >= 0.5);
    /* what each wedge is: n full boards filled the obvious way, m queens put down the fast way, k wedges cut */
    const rings = ph === 0 ? Math.min(NQ, 1 + Math.floor(u * 1.3 * NQ)) : NQ;
    const n = ph === 1 ? nBrute(u) : ph === 2 || ph === 3 ? LEAVES.length : 0;
    const k = ph === 3 ? Math.min(CUTS.length, Math.floor(u * 1.15 * CUTS.length)) : ph >= 4 ? CUTS.length : 0;
    const m = ph === 4 ? nTrace(u) : ph === 5 ? VISITS.length : 0;
    const cuts = CUTS.slice(0, k), seen = new Map(); VISITS.slice(0, m).forEach((v) => seen.set(v.p.join(''), v.bad));
    for (let d = 1; d <= rings; d += 1) for (let i = 0; i < NQ ** d; i += 1) {
      const p = prefix(d, i), cut = cuts.find((q) => under(p, q.p) && (ph < 4 || seen.get(q.p.join('')) === true));
      let fill = null;
      if (ph >= 4) { const s = seen.get(p.join('')); fill = s === true ? PAL.bad : s === false ? (d === NQ ? key : alpha(PAL.ink, 0.72)) : cut && cut.p.length < d ? alpha(PAL.bad, 0.12) : null; }
      else if (cut) fill = cut.p.length === d ? PAL.bad : alpha(PAL.bad, 0.12);
      else if (d === NQ) { if (i < n) fill = clash(p) ? alpha(PAL.ink, 0.5) : key; }
      else if (n > 0 && idx(p) * NQ ** (NQ - d) < n) fill = alpha(PAL.ink, 0.16);
      if (ph === 2 && asked && under(p, EX.slice(0, 2))) fill = d === 2 ? PAL.bad : alpha(PAL.bad, d === NQ ? 0.55 : 0.3);
      wedge(ctx, d, i, fill, fill ? PAL.panel : PAL.rule, 1.5);
    }
    text(ctx, 'row 1', CX, CY - 12, PAL.muted, { size: 26, align: 'center' });
    text(ctx, 'row 4 outside', CX, CY + 18, PAL.muted, { size: 22, align: 'center' });

    /* the board in question */
    let show, head;
    if (hover && !g.asking) { show = hover; head = clash(hover) ? 'This wedge: a clash.' : hover.length === NQ ? 'This wedge: a board that passes.' : 'This wedge: no clash so far.'; }
    else if (ph === 0) { show = [1, 3, 0, 2].slice(0, rings); head = rings < NQ ? `Ring ${rings} is row ${rings}: four columns to choose from.` : 'One wedge of the outer ring is one full board.'; }
    else if (ph === 1) { show = n ? LEAVES[n - 1] : []; head = n ? `Board ${n} of 256: ${clash(show) ? 'fails' : 'passes'}.` : 'Every full board, one after another.'; }
    else if (ph === 2) { show = asked ? EX.slice(0, 2).concat(prefix(2, Math.min(15, Math.floor(part(u, 0.5, 1) * 16)))) : EX; head = asked ? 'Rows 1 and 2 clash, whatever rows 3 and 4 hold.' : 'A board that fails. When was it lost?'; }
    else if (ph === 3) { show = k ? cuts[k - 1].p : []; head = k ? `A clash after ${show.length} queen${show.length === 1 ? '' : 's'}: the ${cuts[k - 1].spared} boards beyond it are never filled.` : 'The obvious way fills everything. Now cut at each clash.'; }
    else if (ph === 4) { show = m ? VISITS[m - 1].p : []; head = m ? (VISITS[m - 1].bad ? 'Clash: take the queen back.' : show.length === NQ ? 'A solution.' : 'No clash: on to the next row.') : 'Start with an empty board.'; }
    else { show = [1, 3, 0, 2]; head = `${VISITS.length} queens put down, not 1,024.`; }
    topline(ctx, head);
    if (show.length) wedge(ctx, show.length, idx(show), null, PAL.ink, 5);
    board(ctx, show);

    /* the counts */
    if (ph <= 2) {
      const ok = LEAVES.slice(0, n).filter((p) => !clash(p)).length;
      count(ctx, 660, n * NQ, 'queens put down', n ? cost : PAL.rule);
      count(ctx, 840, ok, ok === 1 ? 'board passes' : 'boards pass', ok ? key : PAL.rule);
    } else if (ph === 3) {
      count(ctx, 660, cuts.reduce((s, q) => s + q.spared, 0), 'boards never filled', k ? PAL.bad : PAL.rule);
      count(ctx, 840, k, 'clashing wedges cut', k ? PAL.bad : PAL.rule);
    } else {
      const ok = VISITS.slice(0, m).filter((v) => !v.bad && v.p.length === NQ).length;
      count(ctx, 660, m, 'queens put down, of 1,024', m ? cost : PAL.rule);
      count(ctx, 840, ok, ok === 1 ? 'solution' : 'solutions', ok ? key : PAL.rule);
    }
  }
})();
