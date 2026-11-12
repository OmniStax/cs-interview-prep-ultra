/* kit: ls */
/* 99.9 · graphs · the shortest way between two towns (Dijkstra's algorithm), in the app's own style, in six
   named phases. Two tasks in the Observation phase: the reader presses the town that is finished. */
(function () {
  const { C, PAL, alpha, text, line, topline } = F;
  const { clamp, ease, part } = LS;
  const N = 'ABCDEFG'.split('');
  const POS = { A: [0.03, 0.5], B: [0.27, 0.12], C: [0.27, 0.88], D: [0.52, 0.5], E: [0.76, 0.12], F: [0.76, 0.88], G: [0.98, 0.5] };
  const UP = { A: -1, B: -1, C: 1, D: -1, E: -1, F: 1, G: -1 };
  const ROADS = [['A', 'B', 4], ['A', 'C', 2], ['B', 'C', 1], ['B', 'D', 5], ['C', 'D', 8], ['C', 'F', 9], ['D', 'E', 2], ['D', 'F', 3], ['E', 'G', 4], ['F', 'G', 6], ['B', 'E', 10], ['E', 'F', 7]];
  const BROKEN = ROADS.map((r) => (r[0] === 'E' && r[1] === 'F' ? ['E', 'F', -6] : r));
  const adj = (R) => { const a = {}; N.forEach((n) => { a[n] = []; }); R.forEach(([u, v, w]) => { a[u].push([v, w]); a[v].push([u, w]); }); return a; };
  const key2 = (u, v) => (u < v ? u + v : v + u);
  const brute = (function () {
    const a = adj(ROADS), looks = []; let best = Infinity, bestPath = null, routes = 0;
    (function go(u, seen, len, path) {
      if (u === 'G') { routes += 1; if (len < best) { best = len; bestPath = path.slice(); } looks[looks.length - 1] = Object.assign({}, looks[looks.length - 1], { best, bestPath, routes, arrived: true }); return; }
      a[u].forEach(([v, w]) => { if (seen.has(v)) return; looks.push({ path: path.concat(v), len: len + w, best, bestPath, routes }); seen.add(v); go(v, seen, len + w, path.concat(v)); seen.delete(v); });
    })('A', new Set(['A']), 0, ['A']);
    return looks;
  })();
  const fast = (R) => {
    const a = adj(R), d = {}, via = {}, done = [], steps = [];
    N.forEach((n) => { d[n] = Infinity; }); d.A = 0;
    while (done.length < N.length) {
      let u = null; N.forEach((n) => { if (!done.includes(n) && (u === null || d[n] < d[u])) u = n; });
      done.push(u); steps.push({ settle: u, d: Object.assign({}, d), via: Object.assign({}, via), done: done.slice() });
      if (u === 'G') break;
      a[u].forEach(([v, w]) => { if (done.includes(v)) return; const old = d[v]; if (d[u] + w < d[v]) { d[v] = d[u] + w; via[v] = u; } steps.push({ look: [u, v], w, old, d: Object.assign({}, d), via: Object.assign({}, via), done: done.slice() }); });
    }
    return steps;
  };
  const S1 = fast(ROADS), S3 = fast(BROKEN), NB = brute.length, NL = S1.filter((s) => s.look).length;
  const settles = S1.map((s, i) => (s.settle ? i : -1)).filter((i) => i >= 0);
  const R = { x: 130, y: 250, w: 1140, h: 560 };
  const at = (n) => [R.x + POS[n][0] * R.w, R.y + POS[n][1] * R.h];
  const inPath = (p, u, v) => { for (let i = 1; i < p.length; i += 1) if (key2(p[i - 1], p[i]) === key2(u, v)) return true; return false; };

  const BRUTE = ['def shortest(u, seen, length):', '    if u == goal:', '        return length', '    best = inf', '    for v, w in roads[u]:', '        if v not in seen:', '            best = min(best, shortest(v, seen | {v}, length + w))', '    return best'].join('\n');
  const FAST = ['dist = {start: 0}', 'done = set()', 'while goal not in done:', '    u = min((t for t in dist if t not in done), key=dist.get)', '    done.add(u)', '    for v, w in roads[u]:', '        if v not in done and dist[u] + w < dist.get(v, inf):', '            dist[v] = dist[u] + w'].join('\n');
  const nLook = (u) => (u < 0.45 ? Math.floor((u / 0.45) * 9) : Math.min(NB, 9 + Math.ceil(ease((u - 0.45) / 0.5) * (NB - 9))));
  const nStep = (u) => Math.min(S1.length - 1, Math.floor(u * 1.06 * S1.length));
  /* the Observation phase: where the fast way stands at u, given which questions are behind us */
  const obsStep = (u, solved) => {
    const through = (a, b, from, to) => Math.min(to - 1, from + Math.floor(clamp((u - a) / (b - a)) * (to - from)));
    if (u < 0.4 && !solved(2, 0)) return settles[1] - 1;
    if (u < 0.52) return through(0.4, 0.52, settles[1], settles[2]);
    if (u < 0.85 && !solved(2, 1)) return settles[2] - 1;
    return through(0.85, 1, settles[2], settles[3]);
  };
  const ask = (which) => ({
    targets: () => N.map((n) => ({ id: n, x: at(n)[0], y: at(n)[1], r: 52, label: 'town ' + n })),
    check: (n) => {
      const st = S1[settles[which] - 1], want = S1[settles[which]].settle;
      if (n === want) return { ok: true, text: `${want} is the nearest town not yet finished, so no other way to it can be shorter than ${st.d[want]}.` };
      if (st.done.includes(n)) return `${n} is finished already.`;
      if (st.d[n] === Infinity) return `No road from a finished town reaches ${n} yet, so nothing is known about it.`;
      return `${n} stands at ${st.d[n]} for now, but ${want} is nearer at ${st.d[want]}, so a shorter way to ${n} could still run through ${want}.`;
    },
  });

  LS.lesson(root, F, 'ls-roads', {
    H: 1000, mode: 'scroll',
    phases: [
      { kind: 'Problem', title: 'The shortest way from A to G', dur: 7,
        html: '<p>Seven towns and the roads between them, each with its length. What is the shortest way from A to G, and how long is it?</p><p>A route may pass through any towns it likes. The fewest roads is not the same as the shortest: A to B is one road of length 4, and A to C to B is two roads of length 3.</p>',
        note: () => 'The number on a road is its length.' },
      { kind: 'Brute force', title: 'Walk every route', dur: 11, code: { src: BRUTE },
        html: '<p>Follow every route from A that visits no town twice, add up its roads, and keep the shortest that reaches G.</p>',
        lines: (u) => { const k = nLook(u); return k && brute[k - 1].arrived ? [2, 3] : [5, 6, 7]; },
        note: (u) => (nLook(u) < 10 ? 'The first roads, one at a time.' : 'The other routes go the same way, so they run fast.') },
      { kind: 'Observation', title: 'One town is already settled', dur: 14,
        html: '<p>Look from A along its roads and write on each town the best length found so far. Some of these numbers can still get smaller. One cannot.</p><p class="obs">The nearest unfinished town is finished: any other way to it starts by going somewhere at least as far, and every road costs something.</p>',
        tasks: [
          Object.assign({ a: 0.04, b: 0.4, prompt: 'A has looked along its roads. Press the town whose number can no longer get smaller.' }, ask(1)),
          Object.assign({ a: 0.52, b: 0.85, prompt: 'C has looked along its roads. Press the next town whose number is final.' }, ask(2)),
        ],
        note: () => 'A filled town is finished. A dashed number could still get smaller.' },
      { kind: 'Optimization', title: 'Finish the nearest town, never return to it', dur: 9, code: { src: FAST, added: [4, 5] },
        html: '<p>Apply the observation: pick the nearest unfinished town, mark it finished, look along its roads, and repeat. A finished town is never looked at again, so each road is looked at once from each end at most.</p>',
        lines: () => [4, 5],
        note: (u) => `${S1.slice(0, nStep(u) + 1).filter((s) => s.settle).length} of 7 towns finished.` },
      { kind: 'Trace', title: 'One run, town by town', dur: 16, code: { src: FAST, added: [4, 5] },
        html: '<p>Follow the run. Each step either finishes a town or looks along one road from the town just finished.</p>',
        lines: (u) => (S1[nStep(u)].settle ? [4, 5] : S1[nStep(u)].d[S1[nStep(u)].look[1]] < S1[nStep(u)].old ? [6, 7, 8] : [6, 7]),
        note: (u) => { const s = S1[nStep(u)]; if (s.settle) return `${s.settle} is the nearest unfinished town: finished at ${s.d[s.settle]}.`; const [a, b] = s.look; return s.d[b] < s.old ? `From ${a}: ${s.d[a]} + ${s.w} = ${s.d[b]} to ${b}${s.old === Infinity ? '' : ', shorter than ' + s.old}.` : `From ${a}: ${s.d[a]} + ${s.w} = ${s.d[a] + s.w} to ${b}, no better than ${s.old}.`; } },
      { kind: 'Insight', title: 'What is nearest cannot be improved', dur: 10,
        html: `<p class="obs">What is nearest can no longer be improved, so finish it and never look back.</p><p>${NL} roads looked at, where walking every route takes ${NB}.</p><p>The rule stands on every road costing something. Scroll on: the road between E and F now <em>pays</em> 6. The method still finishes E at 10, but a route through F reaches E at 5, and the answer it gives is wrong.</p>`,
        note: (u) => (u < 0.4 ? 'A, C, B, D, E, G: 14.' : 'With a road that pays, "finished" is no longer safe.') },
    ],
    draw,
  });

  function tag(ctx, s, x, y, color, fill, dash) {
    const w = Math.max(64, F.measure(ctx, s, { size: 36, weight: 600 }) + 30);
    ctx.save(); ctx.beginPath(); ctx.roundRect(x - w / 2, y - 26, w, 52, 26); ctx.fillStyle = fill; ctx.fill(); ctx.strokeStyle = color; ctx.lineWidth = 3; if (dash) ctx.setLineDash([8, 6]); ctx.stroke(); ctx.restore();
    text(ctx, s, x, y + 1, color, { size: 36, weight: 600, align: 'center' });
  }
  /* road(u, v) -> {color, w}; town(n) -> {fill, ring, tag: [text, color, fill, dashed]} */
  function map(ctx, roads, road, town, mid) {
    roads.forEach(([u, v]) => { const [x1, y1] = at(u), [x2, y2] = at(v), s = road(u, v); line(ctx, x1, y1, x2, y2, s.color, s.w); });
    if (mid) mid();
    roads.forEach(([u, v, w]) => {
      const [x1, y1] = at(u), [x2, y2] = at(v), mx = (x1 + x2) / 2, my = (y1 + y2) / 2, s = w < 0 ? 'pays ' + (-w) : String(w), ww = F.measure(ctx, s, { size: 32 }) + 22;
      ctx.fillStyle = PAL.panel; ctx.beginPath(); ctx.roundRect(mx - ww / 2, my - 22, ww, 44, 22); ctx.fill();
      text(ctx, s, mx, my + 1, w < 0 ? PAL.bad : PAL.ink, { size: 32, align: 'center', weight: w < 0 ? 600 : 400 });
    });
    N.forEach((n) => {
      const [x, y] = at(n), s = town(n);
      ctx.beginPath(); ctx.arc(x, y, 44, 0, 7); ctx.fillStyle = PAL.panel; ctx.fill(); if (s.fill) { ctx.fillStyle = s.fill; ctx.fill(); } ctx.strokeStyle = s.ring || PAL.ink; ctx.lineWidth = s.lw || 4; ctx.stroke();
      text(ctx, n, x, y + 1, s.ink || PAL.ink, { size: 40, weight: 600, align: 'center' });
      if (s.tag) tag(ctx, s.tag[0], x, y + UP[n] * 84, s.tag[1], s.tag[2], s.tag[3]);
    });
  }
  function fastMap(ctx, S, i, roads, bad, mid) {
    const s = S[clamp(i, 0, S.length - 1)], key = C('key'), cost = C('cost');
    map(ctx, roads, (u, v) => {
      const cur = s.look && key2(s.look[0], s.look[1]) === key2(u, v), tree = N.some((n) => s.via[n] && key2(n, s.via[n]) === key2(u, v) && s.done.includes(n));
      return cur ? { color: cost, w: 12 } : tree ? { color: key, w: 10 } : { color: alpha(PAL.ink, 0.25), w: 7 };
    }, (n) => {
      const fin = s.done.includes(n), d = s.d[n];
      if (bad && bad.includes(n) && fin) return { fill: alpha(PAL.bad, 0.25), ring: PAL.bad, tag: [String(d), PAL.bad, PAL.panel] };
      if (fin) return { fill: alpha(key, 0.3), ring: key, lw: 6, tag: [String(d), key, alpha(key, 0.18)] };
      return d === Infinity ? { ring: alpha(PAL.ink, 0.35), ink: PAL.muted } : { tag: [String(d), PAL.ink, PAL.panel, true] };
    }, mid);
  }

  function draw(g) {
    const ctx = g.ctx, ph = g.ph, u = g.u, cost = C('cost'), key = C('key'), idx = C('index');
    const big = (n, words, color) => { text(ctx, String(n), 1360, 110, color, { size: 76, weight: 600, align: 'right' }); text(ctx, words, 1360, 164, PAL.muted, { size: 28, align: 'right' }); };
    if (ph === 0) {
      topline(ctx, 'Seven towns. Which way from A to G is shortest?');
      map(ctx, ROADS, () => ({ color: alpha(PAL.ink, 0.35), w: 8 }), (n) => (n === 'A' ? { tag: ['start', PAL.ink, PAL.panel] } : n === 'G' ? { tag: ['goal', PAL.ink, PAL.panel] } : {}));
    } else if (ph === 1) {
      const k = nLook(u), b = k ? brute[k - 1] : { path: ['A'], len: 0, best: Infinity, bestPath: null, routes: 0 };
      topline(ctx, b.bestPath ? `Shortest so far: ${b.best}, after ${b.routes} of 34 routes.` : 'No route has reached G yet.');
      map(ctx, ROADS, (p, q) => (inPath(b.path, p, q) ? { color: idx, w: 12 } : b.bestPath && inPath(b.bestPath, p, q) ? { color: alpha(key, 0.8), w: 9 } : { color: alpha(PAL.ink, 0.25), w: 7 }),
        (n) => (b.path.includes(n) ? { ring: idx, lw: 6, tag: n === b.path[b.path.length - 1] ? [String(b.len), idx, PAL.panel] : null } : {}));
      big(k, 'roads walked', cost);
    } else if (ph === 2) {
      const i = obsStep(u, g.solved), s = S1[i];
      topline(ctx, g.asking ? 'Which number is final?' : s.settle ? `${s.settle} is finished at ${s.d[s.settle]}.` : `From ${s.look[0]}: ${s.d[s.look[0]]} + ${s.w} to ${s.look[1]}.`);
      fastMap(ctx, S1, i, ROADS);
    } else if (ph === 3 || ph === 4) {
      const i = nStep(u), s = S1[i];
      topline(ctx, s.settle ? `${s.settle} is the nearest unfinished town: finished at ${s.d[s.settle]}.` : `Look along the road from ${s.look[0]} to ${s.look[1]}.`);
      fastMap(ctx, S1, i, ROADS);
      big(S1.slice(0, i + 1).filter((q) => q.look).length, `roads looked at, of ${NB} walked`, cost);
    } else if (u < 0.4) {
      topline(ctx, `The shortest way is 14, found with ${NL} looks.`);
      fastMap(ctx, S1, S1.length - 1, ROADS);
      big(NL, `roads looked at, of ${NB} walked`, cost);
    } else {
      const truth = ['A', 'C', 'B', 'D', 'F', 'E', 'G'], sums = [0, 2, 3, 8, 11, 5, 9], shown = Math.min(truth.length, 1 + Math.floor(part(u, 0.5, 0.9) * truth.length));
      topline(ctx, shown >= 6 ? 'This route reaches E at 5 and G at 9. The method answered 10.' : 'The road between E and F now pays 6. Walk one route by hand.');
      fastMap(ctx, S3, S3.length - 1, BROKEN, shown >= 6 ? ['E', 'G'] : null, () => {
        ctx.save(); ctx.setLineDash([4, 18]); ctx.strokeStyle = PAL.ink; ctx.lineWidth = 9; ctx.lineCap = 'round'; ctx.beginPath();
        truth.slice(0, shown).forEach((n, j) => { const [x, y] = at(n); if (j) ctx.lineTo(x, y); else ctx.moveTo(x, y); }); ctx.stroke(); ctx.restore();
      });
      const [x, y] = at(truth[shown - 1]); tag(ctx, String(sums[shown - 1]), x + 84, y + 50, PAL.ink, PAL.panel);
    }
  }
})();
