/* kit: ls */
/* 99.11 · two pointers · a pair with a given sum in a sorted array. The search space is the table of every
   pair i < j. A sum shows only once the code has added it up; a pair ruled out unseen is tinted and struck. */
(function () {
  const { C, PAL, alpha, text, line, topline } = F;
  const { clamp, ease, part } = LS;
  const A = [2, 4, 5, 7, 9, 12, 14, 18], T = 21, N = A.length, NP = (N * (N - 1)) / 2;
  const BAD = [18, 2, 14, 4, 5, 7, 12, 9];                   /* the same numbers out of order: the rule fails */
  const ord = (r, c) => r * N - (r * (r + 1)) / 2 + (c - r - 1);
  const walk = (a) => { let i = 0, j = a.length - 1; const p = []; while (i < j) { p.push([i, j]); const s = a[i] + a[j]; if (s === T) break; if (s < T) i += 1; else j -= 1; } return p; };
  const PATH = walk(A), PBAD = walk(BAD);
  let found = 0; (function () { for (let r = 0; r < N; r += 1) for (let c = r + 1; c < N; c += 1) { found += 1; if (A[r] + A[c] === T) return; } })();
  const CW = 108, AY = 190, GX = 700 - ((N - 1) * CW) / 2, GY = 400, CH = 66;

  const BRUTE = ['def pair_sum(nums, target):', '    for i in range(len(nums)):', '        for j in range(i + 1, len(nums)):', '            if nums[i] + nums[j] == target:', '                return [i, j]', '    return []'].join('\n');
  const FAST = ['def pair_sum(nums, target):', '    i, j = 0, len(nums) - 1', '    while i < j:', '        s = nums[i] + nums[j]', '        if s == target:', '            return [i, j]', '        if s < target:', '            i += 1', '        else:', '            j -= 1', '    return []'].join('\n');
  const nBrute = (u) => (u < 0.4 ? Math.floor((u / 0.4) * 5) : Math.min(found, 5 + Math.ceil(ease((u - 0.4) / 0.55) * (found - 5))));
  const nFast = (u) => Math.min(PATH.length, 1 + Math.floor(u * 1.05 * PATH.length));
  /* a strip of pairs as one press: the rest of row r, or the rest of column c, inside what is still open */
  const rowHot = (i, j) => ({ id: 'row', x: GX + ((i + j - 1) / 2) * CW, y: GY + (i + 0.5) * CH, w: (j - i - 1) * CW - 8, h: CH - 8, label: 'the rest of row ' + i });
  const colHot = (i, j) => ({ id: 'col', x: GX + (j - 0.5) * CW, y: GY + ((i + j + 1) / 2) * CH, w: CW - 8, h: (j - i - 1) * CH - 8, label: 'the rest of column ' + j });
  const ask = (k) => {
    const [i, j] = PATH[k], s = A[i] + A[j], small = s < T;
    return {
      targets: () => [rowHot(i, j), colHot(i, j)],
      check: (id) => {
        const rowWhy = `Row ${i} pairs ${A[i]} with partners smaller than ${A[j]}, so its other sums are all below ${s}`, colWhy = `Column ${j} pairs ${A[j]} with partners larger than ${A[i]}, so its other sums are all above ${s}`;
        if ((id === 'row') === small) return { ok: true, text: `${small ? rowWhy : colWhy}, and ${s} is already too ${small ? 'small' : 'big'}. None of them was added up.` };
        return `${small ? colWhy : rowWhy}. One of them could be ${T}.`;
      },
    };
  };

  LS.lesson(root, F, 'ls-pair', {
    H: 1000, mode: 'scroll', nav: 'tabs', change: 'boxes',
    code: { brute: BRUTE, bad: [2, 3], badNote: 'every pair, one at a time', fast: FAST, added: [2, 3, 7, 8, 9, 10], addNote: 'one sum, one whole row or column' },
    phases: [
      { kind: 'Problem', title: 'A pair that adds up to 21', dur: 7,
        html: '<p>Eight numbers stand in increasing order. The task is two of them that add up to 21, or the news that no such pair exists.</p><p>The table has one cell for each pair: row <i>i</i> for the first number, column <i>j</i> for the second. A cell shows its sum only after the code has added it up.</p>',
        note: () => '28 pairs, none of them added up yet.' },
      { kind: 'Brute force', title: 'Every pair', dur: 10, show: 'brute',
        html: '<p>Each pair is added up and compared with the target, row by row, until one matches. Nothing here uses the order of the numbers.</p>',
        lines: (u) => (nBrute(u) === found ? [4, 5] : [3, 4]),
        note: (u) => (nBrute(u) < 6 ? 'The first pairs, one at a time.' : 'The rest go the same way, so they run fast.') },
      { kind: 'Observation', title: 'What one sum settles', dur: 14, show: 'bad',
        html: '<p class="obs">In a sorted array, one sum settles a whole row or column. Too small, and the smaller number is out with every pair it is in. Too big, and the larger number is out.</p><p>The loops in the red box add those pairs up anyway.</p>',
        tasks: [
          Object.assign({ a: 0.04, b: 0.4, prompt: '2 + 18 = 20 is less than 21. Press the pairs that this one sum rules out.' }, ask(0)),
          Object.assign({ a: 0.5, b: 0.86, prompt: '4 + 18 = 22 is more than 21. Press the pairs that this sum rules out.' }, ask(1)),
        ],
        note: () => 'A struck cell was ruled out without being added up.' },
      { kind: 'Optimization', title: 'Two ends moving inward', dur: 9, show: 'change',
        html: '<p>The pair to try is always the smallest number left with the largest. Its sum either matches or sends one of the two out, and that end moves inward.</p>',
        note: (u) => `${nFast(u)} sums added up.` },
      { kind: 'Trace', title: 'One run', dur: 13, show: 'fast',
        html: '<p>Any pair that adds up to the target lies between <i>i</i> and <i>j</i> from start to finish. Each step moves one end, so at most <i>n</i> − 1 sums are added up.</p>',
        lines: (u) => { const k = nFast(u), [i, j] = PATH[k - 1], s = A[i] + A[j]; return s === T ? [4, 5, 6] : s < T ? [4, 7, 8] : [4, 9, 10]; },
        note: (u) => { const k = nFast(u), [i, j] = PATH[k - 1], s = A[i] + A[j]; return s === T ? `${A[i]} + ${A[j]} = ${T}. Found.` : `${A[i]} + ${A[j]} = ${s}, too ${s < T ? 'small' : 'big'}: ${s < T ? 'i moves right' : 'j moves left'}.`; } },
      { kind: 'Insight', title: 'Order and elimination', dur: 10,
        html: `<p class="obs">On sorted data, one comparison settles many candidates at once.</p><p>${PATH.length} sums added up, against ${found}.</p><p>The rule depends on the order. Further on, the same eight numbers are shuffled: the code answers that no pair exists, and two pairs that add up to 21 sit among the cells it struck out.</p>`,
        note: (u) => (u < 0.45 ? '7 + 14 = 21.' : 'Unsorted, the struck cells are no longer safe to strike.') },
    ],
    draw,
  });

  function cell(ctx, r, c, st, s) {
    const x0 = GX + (c - 1) * CW, y0 = GY + r * CH, key = C('key');
    ctx.fillStyle = st === 'dead' ? alpha(PAL.bad, 0.1) : st === 'known' || st === 'cur' || st === 'found' ? alpha(key, 0.14) : st === 'missed' ? alpha(PAL.bad, 0.3) : PAL.panel;
    ctx.fillRect(x0, y0, CW, CH); ctx.strokeStyle = alpha(PAL.ink, st === 'dead' ? 0.15 : 0.4); ctx.lineWidth = 2; ctx.strokeRect(x0, y0, CW, CH);
    if (st === 'dead') line(ctx, x0 + 16, y0 + CH - 14, x0 + CW - 16, y0 + 14, alpha(PAL.bad, 0.55), 2.5);
    else if (st !== 'open') text(ctx, String(s), x0 + CW / 2, y0 + CH / 2 + 1, st === 'missed' ? PAL.bad : PAL.ink, { size: 32, align: 'center', weight: st === 'found' || st === 'missed' ? 600 : 400 });
    if (st === 'cur' || st === 'found' || st === 'missed') { ctx.strokeStyle = st === 'missed' ? PAL.bad : st === 'found' ? key : PAL.ink; ctx.lineWidth = 5; ctx.strokeRect(x0 + 3, y0 + 3, CW - 6, CH - 6); }
  }
  /* state(r, c) -> 'open' | 'known' | 'cur' | 'found' | 'dead' | 'missed' */
  function scene(ctx, a, i, j, state) {
    const key = C('key'), idx = C('index');
    a.forEach((v, k) => {
      const x0 = 700 - (N * CW) / 2 + k * CW, out = i != null && (k < i || k > j);
      ctx.fillStyle = !out && i != null ? alpha(idx, 0.12) : PAL.panel; ctx.fillRect(x0, AY - 40, CW, 80);
      ctx.strokeStyle = alpha(PAL.ink, out ? 0.25 : 1); ctx.lineWidth = k === i || k === j ? 5 : 2.5; ctx.strokeRect(x0, AY - 40, CW, 80);
      text(ctx, String(v), x0 + CW / 2, AY + 1, out ? alpha(key, 0.4) : key, { size: 40, align: 'center' });
      text(ctx, String(k), x0 + CW / 2, AY + 66, alpha(idx, out ? 0.45 : 1), { size: 28, align: 'center' });
      if (k === i) text(ctx, 'i', x0 + CW / 2, AY - 66, PAL.ink, { size: 34, weight: 600, align: 'center', italic: true });
      if (k === j) text(ctx, 'j', x0 + CW / 2, AY - 66, PAL.ink, { size: 34, weight: 600, align: 'center', italic: true });
    });
    for (let c = 1; c < N; c += 1) text(ctx, String(c), GX + (c - 0.5) * CW, GY - 26, c === j ? PAL.ink : alpha(idx, 0.8), { size: 28, align: 'center', weight: c === j ? 600 : 400 });
    for (let r = 0; r < N - 1; r += 1) text(ctx, String(r), GX - 20, GY + (r + 0.5) * CH, r === i ? PAL.ink : alpha(idx, 0.8), { size: 28, align: 'right', weight: r === i ? 600 : 400 });
    text(ctx, 'i', GX - 20, GY - 26, PAL.ink, { size: 30, italic: true, align: 'right' }); text(ctx, 'j', GX + (N - 1) * CW + 22, GY - 26, PAL.ink, { size: 30, italic: true });
    for (let r = 0; r < N - 1; r += 1) for (let c = r + 1; c < N; c += 1) cell(ctx, r, c, state(r, c), a[r] + a[c]);
  }
  /* the fast way after k sums on array a along path p */
  function fastScene(ctx, a, p, k, done, miss) {
    const [i, j] = p[Math.min(k, p.length) - 1], hit = a[i] + a[j] === T, seen = (r, c) => p.slice(0, k).some(([x, y]) => x === r && y === c);
    scene(ctx, a, done ? null : i, done ? null : j, (r, c) => {
      if (miss && a[r] + a[c] === T) return 'missed';
      if (r === i && c === j && !done) return hit ? 'found' : 'cur';
      if (seen(r, c)) return 'known';
      return done || r < i || c > j ? 'dead' : 'open';
    });
    let dead = 0; for (let r = 0; r < N - 1; r += 1) for (let c = r + 1; c < N; c += 1) if (!seen(r, c) && (done || r < i || c > j)) dead += 1;
    return dead;
  }
  function counts(ctx, n, dead) {
    const cost = C('cost');
    text(ctx, String(n), 60, 520, cost, { size: 84, weight: 600 }); text(ctx, 'sums added up', 60, 580, PAL.muted, { size: 28 });
    if (dead != null) { text(ctx, String(dead), 60, 700, PAL.bad, { size: 84, weight: 600 }); text(ctx, 'ruled out unseen', 60, 760, PAL.muted, { size: 28 }); }
  }

  function draw(g) {
    const ctx = g.ctx, ph = g.ph, u = g.u;
    if (ph === 0) { topline(ctx, `Which two of these add up to ${T}?`); scene(ctx, A, null, null, () => 'open'); return; }
    if (ph === 1) {
      const n = nBrute(u), hit = n === found; let ci = null, cj = null;
      for (let r = 0; r < N - 1; r += 1) for (let c = r + 1; c < N; c += 1) if (ord(r, c) === n - 1) { ci = r; cj = c; }
      topline(ctx, n ? (hit ? `${A[ci]} + ${A[cj]} = ${T}: found, after ${n} of the ${NP} pairs.` : `${A[ci]} + ${A[cj]} = ${A[ci] + A[cj]}. That says nothing about any other pair.`) : 'Every pair, row by row.');
      scene(ctx, A, ci, cj, (r, c) => { const k = ord(r, c); return k >= n ? 'open' : k === n - 1 ? (hit ? 'found' : 'cur') : 'known'; });
      counts(ctx, n); return;
    }
    if (ph === 2) {
      /* k sums behind us: 1 while the first question stands, 2 once it is answered, 3 after the second */
      const k = u < 0.4 && !g.solved(2, 0) ? 1 : u < 0.86 && !g.solved(2, 1) ? 2 : 3;
      const [i, j] = PATH[k - 1], s = A[i] + A[j];
      topline(ctx, g.asking ? `${A[i]} + ${A[j]} = ${s}, too ${s < T ? 'small' : 'big'}. What else does that settle?` : `${A[i]} + ${A[j]} = ${s}. ${k - 1} sum${k === 2 ? '' : 's'} so far ruled out ${k === 1 ? 'nothing yet' : 'a whole row or column each'}.`);
      counts(ctx, k, fastScene(ctx, A, PATH, k)); return;
    }
    if (ph === 3 || ph === 4) {
      const k = nFast(u), [i, j] = PATH[k - 1], s = A[i] + A[j];
      topline(ctx, s === T ? `${A[i]} + ${A[j]} = ${T}: found with ${k} sums.` : `${A[i]} + ${A[j]} = ${s}: ${s < T ? `row ${i} is out` : `column ${j} is out`}.`);
      counts(ctx, k, fastScene(ctx, A, PATH, k)); return;
    }
    if (u < 0.45) { topline(ctx, `${PATH.length} sums, where the obvious way adds up ${found}.`); counts(ctx, PATH.length, fastScene(ctx, A, PATH, PATH.length)); return; }
    const k = Math.min(PBAD.length, 1 + Math.floor(part(u, 0.5, 0.85) * PBAD.length)), end = u >= 0.85;
    topline(ctx, end ? `It answers "no pair". 14 + 7 and 12 + 9 were struck out unseen.` : 'The same numbers, shuffled. The same code.');
    counts(ctx, k, fastScene(ctx, BAD, PBAD, k, end, end));
  }
})();
