/* Figures for section 1.4 Analysing running time and space. Boots against the section's text article.
   One debugger figure (code beside the drawing, stepped by block: METHOD §2.3). The code in its panel is an AI
   translation of Erickson's pseudocode into Python, Java, C++ and JavaScript (METHOD decision 20): his
   NDaysOfChristmas as printed is the <pre> just above the figure, and BottlesOfBeer is 1.1's. The trace is the
   figure's own JS copy of the Python. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['1.4'] = function (root, F) {
const { C, PAL, alpha, text, line, dot, ctl, choice, topline } = F;
const sim = (id, H) => F.sim(root, id, H);
const AI = 'claude-opus-5-5 high';
const AIS = { python: AI, java: AI, cpp: AI, javascript: AI };
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2, dash) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};

/* ================================================================ sim-song-count: NDaysOfChristmas and BottlesOfBeer */
(function () {
  const PY = [
    'def n_days_of_christmas(gifts):',
    '    n = len(gifts) + 1',
    '    for i in range(1, n + 1):',
    '        print(f"On the {ordinal(i)} day of Christmas, my true love gave to me")',
    '        for j in range(i, 1, -1):',
    '            print(f"{j} {gifts[j - 2]},")',
    '        if i > 1:',
    '            print("and")',
    '        print("a partridge in a pear tree.")',
    '',
    'def bottles_of_beer(n):',
    '    for i in range(n, 0, -1):',
    '        print(f"{i} bottles of beer on the wall, {i} bottles of beer,")',
    '        print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.")',
    '    print("No bottles of beer on the wall, no bottles of beer,")',
    '    print(f"Go to the store, buy some more, {n} bottles of beer on the wall.")',
  ].join('\n');
  /* the braced languages: one shape, each language's own calls; 1.1's BottlesOfBeer after the song of this page */
  const braces = (o) => [
    `${o.head1} {`,
    `    ${o.n}`,
    `    for (${o.int} i = 1; i <= n; i++) {`,
    `        ${o.out('"On the " + ordinal(i) + " day of Christmas, my true love gave to me"', '`On the ${ordinal(i)} day of Christmas, my true love gave to me`')};`,
    `        for (${o.int} j = i; j >= 2; j--) {`,
    `            ${o.out('j + " " + gifts[j - 2] + ","', '`${j} ${gifts[j - 2]},`')};`,
    '        }',
    '        if (i > 1) {',
    `            ${o.out('"and"')};`,
    '        }',
    `        ${o.out('"a partridge in a pear tree."')};`,
    '    }',
    '}',
    '',
    `${o.head2} {`,
    `    for (${o.int} i = n; i >= 1; i--) {`,
    `        ${o.out('i + " bottles of beer on the wall, " + i + " bottles of beer,"', '`${i} bottles of beer on the wall, ${i} bottles of beer,`')};`,
    `        ${o.out('"Take one down, pass it around, " + (i - 1) + " bottles of beer on the wall."', '`Take one down, pass it around, ${i - 1} bottles of beer on the wall.`')};`,
    '    }',
    `    ${o.out('"No bottles of beer on the wall, no bottles of beer,"')};`,
    `    ${o.out('"Go to the store, buy some more, " + n + " bottles of beer on the wall."', '`Go to the store, buy some more, ${n} bottles of beer on the wall.`')};`,
    '}',
  ].join('\n');
  const JAVA = braces({ head1: 'static void nDaysOfChristmas(String[] gifts)', head2: 'static void bottlesOfBeer(int n)', n: 'int n = gifts.length + 1;', int: 'int', out: (s) => `System.out.println(${s})` });
  const CPP = braces({
    head1: 'void nDaysOfChristmas(const std::vector<std::string>& gifts)', head2: 'void bottlesOfBeer(int n)', n: 'int n = gifts.size() + 1;', int: 'int',
    out: (s) => { const t = s.replace(/ \+ /g, ' << '); return `std::cout << ${t.endsWith('"') ? `${t.slice(0, -1)}\\n"` : `${t} << "\\n"`}`; },
  });
  const JS = braces({ head1: 'function nDaysOfChristmas(gifts)', head2: 'function bottlesOfBeer(n)', n: 'const n = gifts.length + 1;', int: 'let', out: (s, tpl) => `console.log(${tpl || s})` });
  /* python line → braced line: the braced languages close each block on a line of its own */
  const MAP = { 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 8, 8: 9, 9: 11, 10: 14, 11: 15, 12: 16, 13: 17, 14: 18, 15: 20, 16: 21 };

  /* the traditional lyric's gifts, gift j brought j at a time (gift 1 the partridge) */
  const GIFTS = ['', 'partridge in a pear tree', 'turtle doves', 'French hens', 'calling birds', 'gold rings', 'geese a-laying',
    'swans a-swimming', 'maids a-milking', 'ladies dancing', 'lords a-leaping', 'pipers piping', 'drummers drumming'];
  const ORD = ['', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'];
  const christmas = (n) => F.trace((at) => {
    let names = 0, given = 0;
    at(2, { n, names, given });
    for (let i = 1; i <= n; i += 1) {
      at(3, { n, i, names, given });
      at(4, { n, i, names, given });
      for (let j = i; j >= 2; j -= 1) {
        at(5, { n, i, j, names, given });
        names += 1; given += j; at(6, { n, i, j, names, given }, ['sing', i, j]);
      }
      at(7, { n, i, names, given });
      if (i > 1) at(8, { n, i, names, given });
      names += 1; given += 1; at(9, { n, i, names, given }, ['sing', i, 1]);
    }
  });
  const bottles = (n) => F.trace((at) => {
    let beer = 0;
    for (let i = n; i >= 1; i -= 1) {
      at(12, { n, i, beer });
      beer += 2; at(13, { n, i, beer });
      beer += 1; at(14, { n, i, beer });
    }
    beer += 2; at(15, { n, beer });
    beer += 1; at(16, { n, beer });
  });

  const d = sim('sim-song-count', 960);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: AIS,
    lineMap: { java: MAP, cpp: MAP, javascript: MAP },
    blocks: [
      { id: 'init', lines: [2, 2], label: 'n is one more than the number of gifts', touches: ['n'] },
      { id: 'day', lines: [3, 9], label: 'sing day i', touches: ['i'] },
      { id: 'open', lines: [4, 4], label: 'open the verse of day i', touches: ['i'] },
      { id: 'gift', lines: [5, 6], label: 'name gift j, j of them', touches: ['j'] },
      { id: 'partridge', lines: [7, 9], label: 'end on the partridge', touches: [] },
      { id: 'verse', lines: [12, 14], label: 'sing verse i: “beer” three times', touches: ['i'] },
      { id: 'coda', lines: [15, 16], label: 'no more bottles: go to the store', touches: [] },
    ],
    refs: { i: () => F.ref('i'), j: () => F.ref('j') },
  });
  let song = 'christmas';
  const DEF = { christmas: 12, bottles: 10 };
  const traced = () => (song === 'christmas' ? christmas(sN.v) : bottles(sN.v));
  const sN = ctl(d.controls, { label: 'n', cls: 'size', key: 'n', min: 1, max: 12, step: 1, value: DEF.christmas, unit: '', dec: 0, onInput: () => dbg.set(traced()) });
  choice(d.controls, {
    label: '\\text{song}', key: 'song', value: song,
    options: [{ value: 'christmas', label: 'The Twelve Days of Christmas' }, { value: 'bottles', label: 'Bottles of Beer' }],
    onInput: (v) => { const was = song; song = v; if (sN.v === DEF[was]) sN.set(DEF[song]); dbg.set(traced()); },
  });

  /* the counts against n, for the graph: each a milestone of one song */
  const COUNTS = [
    { song: 'christmas', name: 'gifts', f: (n) => (n * (n + 1) * (n + 2)) / 6, tex: 'n(n + 1)(n + 2)/6', theta: 'Θ(n³)', dash: null },
    { song: 'christmas', name: 'gift names', f: (n) => (n * (n + 1)) / 2, tex: 'n(n + 1)/2', theta: 'Θ(n²)', dash: [16, 10] },
    { song: 'bottles', name: '“beer”', f: (n) => 3 * n + 3, tex: '3n + 3', theta: 'Θ(n)', dash: [4, 9] },
  ];
  let hits = [];
  F.hover(d.stage, () => hits, d.c);

  const dbg = F.debug(d, {
    code, watch: ['n', 'i', 'j'], trace: traced(), beat: 1.0,
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const v = g.frame.vars, n = v.n, L = g.frame.line, cI = F.ref('i'), cJ = F.ref('j'), cost = C('cost'), size = C('size');
      const blk = g.block ? g.block.id : '';
      const done = g.stop === g.stops - 1 && g.stops > 1;
      hits = [];
      /* ---------------- the song, as squares: one per milestone counted */
      const gx = 150, gy = 150, GW = 560, GH = 620;
      if (song === 'christmas') {
        const names = v.names || 0, given = v.given || 0;
        const cell = Math.min(GW / n, GH / n, 92);
        const i = v.i, j = v.j;
        /* the headline sings the line just sung, or says what the day added */
        if (done) topline(ctx, `${n === 12 ? 'Twelve' : n} day${n === 1 ? '' : 's'}: ${names} gift names sung and ${given} gifts given.`);
        else if (L === 2) topline(ctx, `${n - 1} gift${n === 2 ? '' : 's'} on the list, so the song has n = ${n} day${n === 1 ? '' : 's'}.`);
        else if (blk === 'day') topline(ctx, `Day ${i} sung: ${i} gift name${i === 1 ? '' : 's'} and ${(i * (i + 1)) / 2} gift${i === 1 ? '' : 's'}.`);
        else if (L === 4 || L === 3) topline(ctx, `“On the ${ORD[i]} day of Christmas, my true love gave to me”`);
        else if (L === 6 || L === 5) topline(ctx, `“${j} ${GIFTS[j]},”`);
        else if (L === 8 || L === 7) topline(ctx, i > 1 ? '“and”' : `Day ${i} has no other gift.`);
        else topline(ctx, i === 1 ? '“a partridge in a pear tree.”' : '“… a partridge in a pear tree.”');
        /* row r is day r; its squares, gift r at the right down to the partridge at the left, fill as they are sung */
        text(ctx, 'day', gx - 30, gy - 30, PAL.muted, { size: 26, align: 'right' });
        text(ctx, 'gifts named, from the partridge', gx, gy - 30, PAL.muted, { size: 26 });
        for (let r = 1; r <= n; r += 1) {
          const y0 = gy + (r - 1) * cell, onRow = r === i && !done;
          text(ctx, String(r), gx - 30, y0 + cell / 2, onRow ? cI : PAL.ink, { size: cell > 44 ? 30 : 26, align: 'right', weight: onRow ? 600 : 400 });
          for (let c = 1; c <= r; c += 1) {
            const x0 = gx + (c - 1) * cell, idx = ((r - 1) * r) / 2 + (r - c), sung = idx < names;
            const now = onRow && ((c === j && (L === 5 || L === 6)) || (c === 1 && L === 9));
            rect(ctx, x0 + 2, y0 + 2, cell - 4, cell - 4, sung ? alpha(cost, now ? 0.4 : 0.2) : null, sung ? alpha(cost, 0.55) : alpha(PAL.ink, 0.25), 2);
            if (cell >= 36) text(ctx, String(c), x0 + cell / 2, y0 + cell / 2, sung ? cost : alpha(PAL.ink, 0.35), { size: Math.min(34, Math.max(26, cell * 0.5)), align: 'center', weight: sung ? 600 : 400 });
            if (now) rect(ctx, x0 + 2, y0 + 2, cell - 4, cell - 4, null, c === 1 ? cI : cJ, 5);
            hits.push({ x: x0 + cell / 2, y: y0 + cell / 2, r: cell / 2, name: `day ${r}: ${c === 1 ? (r === 1 ? 'a partridge in a pear tree' : 'and a partridge in a pear tree') : `${c} ${GIFTS[c]}`} (${c} gift${c === 1 ? '' : 's'})` });
          }
          if (onRow) rect(ctx, gx - 4, y0 - 2, r * cell + 8, cell + 4, null, cI, 3, [10, 8]);
        }
        const ended = done || L === 9, daysSung = done ? n : !i ? 0 : ended ? i : i - 1;
        text(ctx, !i ? 'no day sung yet' : ended ? `days 1 .. ${daysSung} sung` : `${daysSung ? `days 1 .. ${daysSung} sung · ` : ''}day i = ${i} in progress`, gx, 830, PAL.muted, { size: 26 });
        text(ctx, `gift names ${names} of n(n + 1)/2 = ${(n * (n + 1)) / 2}   ·   gifts ${given} of n(n + 1)(n + 2)/6 = ${(n * (n + 1) * (n + 2)) / 6}`, 700, 932, cost, { size: 28, align: 'center' });
      } else {
        const beer = v.beer || 0, rows = n + 1, cell = Math.min(GH / rows, 70), cw = 130;
        const i = v.i;
        if (done) topline(ctx, `${n} verse${n === 1 ? '' : 's'} and the end: “beer” ${beer} times = 3n + 3.`);
        else if (blk === 'verse') topline(ctx, `Verse i = ${i} sung: “beer” three more times.`);
        else if (L === 12 || L === 13) topline(ctx, `“${i} bottles of beer on the wall, ${i} bottles of beer,”`);
        else if (L === 14) topline(ctx, `“Take one down, pass it around, ${i - 1} bottles of beer on the wall.”`);
        else if (L === 15) topline(ctx, '“No bottles of beer on the wall, no bottles of beer,”');
        else topline(ctx, `“Go to the store, buy some more, ${n} bottles of beer on the wall.”`);
        text(ctx, 'i', gx - 30, gy - 30, PAL.muted, { size: 26, align: 'right', italic: true });
        text(ctx, '“beer” in each verse', gx, gy - 30, PAL.muted, { size: 26 });
        for (let k = 0; k < rows; k += 1) {
          const y0 = gy + k * cell, ri = n - k, coda = k === n, onRow = !done && (coda ? i === undefined && beer > 3 * n : ri === i);
          text(ctx, coda ? 'end' : String(ri), gx - 30, y0 + cell / 2, onRow && !coda ? cI : PAL.ink, { size: 26, align: 'right', weight: onRow ? 600 : 400 });
          for (let c = 0; c < 3; c += 1) {
            const x0 = gx + c * cw, sung = 3 * k + c < beer;
            rect(ctx, x0 + 3, y0 + 3, cw - 6, cell - 6, sung ? alpha(cost, 0.2) : null, sung ? alpha(cost, 0.55) : alpha(PAL.ink, 0.25), 2);
            text(ctx, 'beer', x0 + cw / 2, y0 + cell / 2, sung ? cost : alpha(PAL.ink, 0.35), { size: 26, align: 'center', weight: sung ? 600 : 400 });
            hits.push({ x: x0 + cw / 2, y: y0 + cell / 2, r: cell / 2, name: coda ? `the end: “beer” ${c + 1} of 3` : `verse ${ri}: “beer” ${c + 1} of 3` });
          }
          if (onRow) rect(ctx, gx - 4, y0, 3 * cw + 8, cell, null, coda ? PAL.ink : cI, 3, [10, 8]);
        }
        const versesSung = done || i === undefined ? Math.min(n, Math.floor(beer / 3)) : n - i + (L === 14 ? 1 : 0);
        text(ctx, `verses sung ${versesSung} of n = ${n}`, gx, 830, PAL.muted, { size: 26 });
        text(ctx, `“beer” ${beer} of 3n + 3 = ${3 * n + 3}`, 700, 932, cost, { size: 28, align: 'center' });
      }

      /* ---------------- the counts against n on log–log axes: n from 1 to 12, counts from 1 to 1000 (fixed) */
      const bx0 = 880, bx1 = 1330, by0 = 160, by1 = 680;
      const X = (x) => bx0 + (Math.log10(x) / Math.log10(12)) * (bx1 - bx0), Y = (y) => by1 - (Math.log10(y) / 3) * (by1 - by0);
      [1, 10, 100, 1000].forEach((t) => { line(ctx, bx0, Y(t), bx1, Y(t), alpha(PAL.ink, 0.12), 2); text(ctx, String(t), bx0 - 14, Y(t), PAL.muted, { size: 26, align: 'right' }); });
      [1, 2, 5, 10].forEach((t) => { line(ctx, X(t), by0, X(t), by1, alpha(PAL.ink, 0.12), 2); text(ctx, String(t), X(t), by1 + 28, PAL.muted, { size: 26, align: 'center' }); });
      line(ctx, bx0, by1, bx1, by1, PAL.ink, 3); line(ctx, bx0, by0, bx0, by1, PAL.ink, 3);
      text(ctx, 'n', (bx0 + bx1) / 2, by1 + 62, size, { size: 30, align: 'center', italic: true, weight: 600 });
      text(ctx, 'count', bx0 - 14, by0 - 34, cost, { size: 26, align: 'right' });
      COUNTS.forEach((K, row) => {
        const mine = K.song === song, col = mine ? cost : alpha(PAL.ink, 0.35);
        ctx.save(); ctx.strokeStyle = col; ctx.lineWidth = mine ? 5 : 3; if (K.dash) ctx.setLineDash(K.dash); ctx.beginPath();
        for (let t = 0; t <= 110; t += 1) { const x = 1 + (11 * t) / 110; const px = X(x), py = Y(K.f(x)); if (t) ctx.lineTo(px, py); else ctx.moveTo(px, py); }
        ctx.stroke(); ctx.restore();
        /* the legend, under the axes */
        const ly = by1 + 112 + row * 42;
        line(ctx, bx0 - 40, ly, bx0 + 10, ly, col, mine ? 5 : 3, K.dash || undefined);
        text(ctx, `${K.name} ${K.tex} = ${K.theta}`, bx0 + 22, ly, mine ? cost : PAL.muted, { size: 26, weight: mine ? 600 : 400 });
        if (mine) for (let m = 1; m <= 12; m += 1) dot(ctx, X(m), Y(K.f(m)), alpha(cost, m === n ? 1 : 0.45), false, m === n ? 11 : 6);
      });
      /* the run in front of the reader: its count climbs at x = n toward the formula's value there (hollow) */
      const live = song === 'christmas' ? [v.given || 0, v.names || 0] : [v.beer || 0];
      live.forEach((c) => { if (c >= 1) { line(ctx, X(n), Y(1), X(n), Y(c), alpha(cost, 0.5), 3); dot(ctx, X(n), Y(c), cost, true, 9); } });
    },
  });
})();
};
