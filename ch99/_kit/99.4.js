/* 99.4 · graphs · the shortest way between two towns (Dijkstra's algorithm).
   STORY: one clock, two panels. The obvious way and the fast way race on the same map; the split then closes
   on the fast side, which is replayed with the reader choosing each town that is finished (the clock waits
   for the click); last, one road is changed so that the rule the fast way stands on is false.
   STYLE: a transit map. Paper background whatever the theme, thick rounded lines, geometric type, colour by
   what a town's distance is worth (final, provisional, wrong) and not by type. No code at all. */
(function () {
  const { clamp, lerp, ease, part } = XP;
  const PAPER = '#f3efe6', NAVY = '#1c2740', GREY = '#b9b3a6', TEAL = '#0f9d8a', AMBER = '#f08c1a', PINK = '#e0257a', RED = '#d7263d', GREEN = '#2e9e4f';
  const FONT = 'Futura, "Century Gothic", "Avenir Next", "Trebuchet MS", system-ui, sans-serif';
  const N = 'ABCDEFG'.split('');
  const POS = { A: [0.05, 0.5], B: [0.28, 0.16], C: [0.28, 0.84], D: [0.52, 0.5], E: [0.76, 0.16], F: [0.76, 0.84], G: [0.97, 0.5] };
  const PILL = { A: [0, -1], B: [0, -1], C: [0, 1], D: [0, -1], E: [0, -1], F: [0, 1], G: [0, -1] };
  const ROADS = [['A', 'B', 4], ['A', 'C', 2], ['B', 'C', 1], ['B', 'D', 5], ['C', 'D', 8], ['C', 'F', 9], ['D', 'E', 2], ['D', 'F', 3], ['E', 'G', 4], ['F', 'G', 6], ['B', 'E', 10], ['E', 'F', 7]];
  const BROKEN = ROADS.map((r) => (r[0] === 'E' && r[1] === 'F' ? ['E', 'F', -6] : r));
  const adj = (R) => { const a = {}; N.forEach((n) => { a[n] = []; }); R.forEach(([u, v, w]) => { a[u].push([v, w]); a[v].push([u, w]); }); return a; };
  const key = (u, v) => (u < v ? u + v : v + u);

  /* the obvious way: every route that visits no town twice, one road at a time */
  const brute = (function () {
    const a = adj(ROADS), looks = []; let best = Infinity, bestPath = null, routes = 0;
    (function go(u, seen, len, path) {
      if (u === 'G') { routes += 1; if (len < best) { best = len; bestPath = path.slice(); } looks[looks.length - 1] = Object.assign({}, looks[looks.length - 1], { best, bestPath, routes, arrived: len }); return; }
      a[u].forEach(([v, w]) => {
        if (seen.has(v)) return;
        looks.push({ path: path.concat(v), len: len + w, best, bestPath, routes });
        seen.add(v); go(v, seen, len + w, path.concat(v)); seen.delete(v);
      });
    })('A', new Set(['A']), 0, ['A']);
    return looks;
  })();
  /* the fast way: finish the nearest unfinished town, look along its roads, never return to a finished town */
  const fast = (R) => {
    const a = adj(R), d = {}, via = {}, done = [], steps = [];
    N.forEach((n) => { d[n] = Infinity; }); d.A = 0;
    while (done.length < N.length) {
      let u = null; N.forEach((n) => { if (!done.includes(n) && (u === null || d[n] < d[u])) u = n; });
      done.push(u); steps.push({ settle: u, d: Object.assign({}, d), via: Object.assign({}, via), done: done.slice() });
      if (u === 'G') break;
      a[u].forEach(([v, w]) => {
        if (done.includes(v)) return;
        const old = d[v]; if (d[u] + w < d[v]) { d[v] = d[u] + w; via[v] = u; }
        steps.push({ look: [u, v], w, old, d: Object.assign({}, d), via: Object.assign({}, via), done: done.slice() });
      });
    }
    return steps;
  };
  const S1 = fast(ROADS), S3 = fast(BROKEN);
  const looksOf = (S) => S.filter((s) => s.look);
  const NL = looksOf(S1).length, NB = brute.length;
  const settles = S1.map((s, i) => (s.settle ? i : -1)).filter((i) => i >= 0);
  const routeOf = (S, n) => { const last = S[S.length - 1], p = [n]; while (p[0] !== 'A') p.unshift(last.via[p[0]]); return p; };

  const x = XP.mount(root, F, 'xp-roads', { w: 1600, h: 900, vars: { '--xp-bg': PAPER, '--xp-fg': NAVY, '--xp-accent': NAVY, '--xp-on-accent': PAPER, '--xp-bar': '#e7e1d3', '--xp-track': '#cfc8b8', '--xp-font': FONT } });
  const T = XP.timeline(x, [{ name: 'The race', dur: 16 }, { name: 'Why it never looks back', dur: 21 }, { name: 'Break the rule', dur: 14 }]);
  /* chapter 2 gives each of the seven towns a slot; the clock waits at the first three for the reader's click */
  const SLOT = 1 / settles.length, GATED = 3;
  for (let i = 1; i <= GATED; i += 1) T.gates.push({ t: T.starts[1] + T.total * 0 + 21 * (i * SLOT + 0.002), i, open: false });
  let wrong = null;
  const FULL = { x: 250, y: 310, w: 1100, h: 450 }, LEFT = { x: 50, y: 250, w: 720, h: 520 }, RIGHT = { x: 830, y: 250, w: 720, h: 520 };
  const at = (R, n) => [R.x + POS[n][0] * R.w, R.y + POS[n][1] * R.h];
  x.c.addEventListener('click', (e) => {
    const g = T.gates.find((q) => !q.open && Math.abs(T.t - q.t) < 0.02); if (!g) return;
    const [px, py] = x.pt(e); let hit = null;
    N.forEach((n) => { const [nx, ny] = at(FULL, n); if (Math.hypot(nx - px, ny - py) < 54) hit = n; });
    if (!hit) return;
    const st = S1[settles[g.i] - 1], want = S1[settles[g.i]].settle;
    if (hit === want) { g.open = true; wrong = null; T.play(); }
    else if (st.done.includes(hit)) wrong = `${hit} is finished already.`;
    else if (st.d[hit] === Infinity) wrong = `No road from a finished town reaches ${hit} yet, so nothing is known about it.`;
    else wrong = `${hit} stands at ${st.d[hit]} for now, but ${want} is nearer at ${st.d[want]}, so a shorter way to ${hit} could still run through ${want}.`;
    x.redraw();
  });

  const txt = (ctx, s, px, py, o = {}) => {
    ctx.font = `${o.weight || 500} ${o.size || 26}px ${FONT}`; ctx.fillStyle = o.color || NAVY; ctx.textAlign = o.align || 'left';
    ctx.globalAlpha = o.alpha == null ? 1 : o.alpha; ctx.fillText(s, px, py); ctx.globalAlpha = 1;
  };
  const pill = (ctx, s, px, py, fill, color, size = 26, al = 1) => {
    ctx.font = `700 ${size}px ${FONT}`; const w = Math.max(size * 1.7, ctx.measureText(s).width + size), h = size * 1.5;
    ctx.globalAlpha = al; ctx.fillStyle = fill; ctx.beginPath(); ctx.roundRect(px - w / 2, py - h / 2, w, h, h / 2); ctx.fill();
    ctx.fillStyle = color; ctx.textAlign = 'center'; ctx.fillText(s, px, py + 1); ctx.globalAlpha = 1;
  };
  /* the map in rect R. road(u, v) -> {color, w, al, dash}; town(n) -> {fill, ring, label: [text, fill] | null} */
  function map(ctx, R, roads, road, town, al = 1, mid) {
    const sc = R.w / 720;
    ctx.globalAlpha = al;
    roads.forEach(([u, v]) => {
      const [x1, y1] = at(R, u), [x2, y2] = at(R, v), s = road(u, v);
      ctx.strokeStyle = s.color; ctx.lineWidth = (s.w || 12) * sc; ctx.globalAlpha = al * (s.al == null ? 1 : s.al); ctx.setLineDash(s.dash || []);
      ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke(); ctx.setLineDash([]);
    });
    if (mid) { ctx.globalAlpha = 1; mid(); }
    roads.forEach(([u, v, w]) => {
      const [x1, y1] = at(R, u), [x2, y2] = at(R, v), s = road(u, v);
      pill(ctx, w < 0 ? 'pays ' + (-w) : String(w), (x1 + x2) / 2, (y1 + y2) / 2, w < 0 ? GREEN : PAPER, w < 0 ? '#fff' : s.label || NAVY, 22 * Math.max(0.85, sc), al);
    });
    N.forEach((n) => {
      const [nx, ny] = at(R, n), s = town(n), r = 30 * Math.max(0.85, sc);
      ctx.globalAlpha = al; ctx.beginPath(); ctx.arc(nx, ny, r, 0, 7); ctx.fillStyle = s.fill || '#fff'; ctx.fill();
      ctx.strokeStyle = s.ring || NAVY; ctx.lineWidth = 7 * sc; ctx.stroke();
      txt(ctx, n, nx, ny + 1, { size: 28 * Math.max(0.85, sc), weight: 700, align: 'center', color: s.ink || NAVY, alpha: al });
      if (s.label) pill(ctx, s.label[0], nx + PILL[n][0] * 60 * sc, ny + PILL[n][1] * 62 * Math.max(0.85, sc), s.label[1], '#fff', 26 * Math.max(0.85, sc), al);
    });
    ctx.globalAlpha = 1;
  }
  const inPath = (p, u, v) => { for (let i = 1; i < p.length; i += 1) if (key(p[i - 1], p[i]) === key(u, v)) return true; return false; };
  /* the fast way's map after step s of S */
  const fastMap = (ctx, R, S, i, roads, al, bad, mid) => {
    const s = S[clamp(i, 0, S.length - 1)], started = i >= 0;
    map(ctx, R, roads, (u, v) => {
      const cur = started && s.look && key(s.look[0], s.look[1]) === key(u, v);
      const tree = started && N.some((n) => s.via[n] && key(n, s.via[n]) === key(u, v) && s.done.includes(n));
      return cur ? { color: AMBER, w: 16 } : tree ? { color: TEAL, w: 14 } : { color: GREY, w: 10 };
    }, (n) => {
      if (!started) return n === 'A' ? { label: ['0', AMBER] } : {};
      const fin = s.done.includes(n), d = s.d[n];
      if (bad && bad.includes(n) && fin) return { fill: RED, ring: RED, ink: '#fff', label: [String(d), RED] };
      if (fin) return { fill: TEAL, ring: TEAL, ink: '#fff', label: [String(d), TEAL] };
      return d === Infinity ? { ring: GREY, ink: GREY } : { ring: AMBER, label: [String(d), AMBER] };
    }, al, mid);
  };

  x.draw = (ctx) => {
    ctx.fillStyle = PAPER; ctx.fillRect(0, 0, 1600, 900);
    const ch = T.ch, u0 = T.u(0), u1 = T.u(1), u2 = T.u(2);
    txt(ctx, 'THE SHORTEST WAY FROM A TO G', 50, 56, { size: 24, weight: 700, color: AMBER });
    const title = ['Try every route, or never look back?', 'The nearest unfinished town is finished', 'One road that pays you, and the rule is false'][ch];
    txt(ctx, title, 50, 108, { size: 50, weight: 700 });

    if (ch === 0) {
      /* both sides count roads looked at; the fast side stops at NL, the obvious side runs on to NB */
      const sec = u0 * 16, kR = Math.min(NL, Math.floor(sec / 0.55)), kL = sec <= 7 ? Math.min(NB, Math.floor(sec / 0.55)) : Math.round(lerp(Math.floor(7 / 0.55), NB, ease((sec - 7) / 8.4)));
      const b = kL ? brute[kL - 1] : { path: ['A'], best: Infinity, bestPath: null, routes: 0 };
      txt(ctx, 'Every route', LEFT.x, 178, { size: 32, weight: 700, color: PINK });
      txt(ctx, 'Follow each route to its end, keep the shortest.', LEFT.x, 214, { size: 22, color: '#5c6477' });
      txt(ctx, String(kL), LEFT.x + LEFT.w, 184, { size: 64, weight: 700, align: 'right', color: PINK });
      txt(ctx, 'roads looked at', LEFT.x + LEFT.w, 232, { size: 20, align: 'right', color: '#5c6477' });
      map(ctx, LEFT, ROADS, (u, v) => (inPath(b.path, u, v) ? { color: PINK, w: 16 } : b.bestPath && inPath(b.bestPath, u, v) ? { color: GREEN, w: 12, al: 0.75 } : { color: GREY, w: 10 }),
        (n) => (b.path.includes(n) ? { ring: PINK, label: n === b.path[b.path.length - 1] ? [String(b.len == null ? 0 : b.len), PINK] : null } : {}));
      txt(ctx, b.bestPath ? `shortest so far: ${b.best}  ·  ${b.routes} of 34 routes finished` : 'no route finished yet', LEFT.x, 826, { size: 24, weight: 600, color: b.bestPath ? GREEN : '#5c6477' });

      txt(ctx, 'Never look back', RIGHT.x, 178, { size: 32, weight: 700, color: TEAL });
      txt(ctx, 'Finish the nearest town, look along its roads, repeat.', RIGHT.x, 214, { size: 22, color: '#5c6477' });
      txt(ctx, String(kR), RIGHT.x + RIGHT.w, 184, { size: 64, weight: 700, align: 'right', color: TEAL });
      txt(ctx, 'roads looked at', RIGHT.x + RIGHT.w, 232, { size: 20, align: 'right', color: '#5c6477' });
      let i = -1; if (kR > 0) { let seen = 0; i = S1.findIndex((s) => s.look && (seen += 1) === kR); if (kR === NL) i = S1.length - 1; }
      fastMap(ctx, RIGHT, S1, i, ROADS, 1);
      txt(ctx, kR === NL ? `done: the shortest way is ${S1[S1.length - 1].d.G}` : 'amber: could still get shorter  ·  teal: final', RIGHT.x, 826, { size: 24, weight: 600, color: kR === NL ? TEAL : '#5c6477' });
      ctx.strokeStyle = '#d9d2c2'; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(800, 170); ctx.lineTo(800, 840); ctx.stroke();
      return;
    }

    if (ch === 1) {
      /* the split closes on the fast side, then one town a slot */
      const open = part(u1, 0, SLOT * 0.6), R = { x: lerp(RIGHT.x, FULL.x, open), y: lerp(RIGHT.y, FULL.y, open), w: lerp(RIGHT.w, FULL.w, open), h: lerp(RIGHT.h, FULL.h, open) };
      const slot = Math.min(settles.length - 1, Math.floor(u1 / SLOT)), v = (u1 - slot * SLOT) / SLOT;
      const from = settles[slot], to = slot + 1 < settles.length ? settles[slot + 1] : S1.length;
      const i = slot === 0 && v < 0.6 ? -1 : Math.min(to - 1, from + Math.floor(clamp((v - (slot === 0 ? 0.6 : 0.25)) / (slot === 0 ? 0.4 : 0.7)) * (to - from)));
      const gate = T.gates.find((q) => !q.open && Math.abs(T.t - q.t) < 0.02);
      fastMap(ctx, R, S1, gate ? settles[gate.i] - 1 : i, ROADS, 1);
      const s = S1[Math.max(0, i)], n = S1[from].settle;
      let line;
      if (gate) line = wrong || 'Click the town whose distance can no longer get shorter.';
      else if (i < 0) line = 'A is 0 from itself. Nothing else is known yet.';
      else if (s.settle) line = n === 'A' ? 'A is finished at 0.' : `${n} is the nearest town not yet finished. Any other way to it starts by going somewhere at least as far, and every road costs something. ${s.d[n]} is final.`;
      else line = s.d[s.look[1]] < s.old ? `From ${s.look[0]}: ${s.d[s.look[0]]} + ${s.w} = ${s.d[s.look[1]]} to ${s.look[1]}${s.old === Infinity ? '' : ', shorter than ' + s.old}.` : `From ${s.look[0]}: ${s.d[s.look[0]]} + ${s.w} = ${s.d[s.look[0]] + s.w} to ${s.look[1]}, no better than ${s.old}.`;
      wrapText(ctx, line, 50, 162, 1500, gate && wrong ? RED : gate ? AMBER : '#3c4660');
      if (u1 > 0.985) {
        const p = routeOf(S1, 'G');
        txt(ctx, `${p.join(' → ')}: ${S1[S1.length - 1].d.G}. Each town finished once, ${NL} roads looked at, against ${NB}.`, 800, 840, { size: 28, weight: 700, align: 'center', color: TEAL });
      } else txt(ctx, 'amber: could still get shorter  ·  teal: final', 800, 840, { size: 22, align: 'center', color: '#5c6477' });
      return;
    }

    /* chapter 3: the road E–F now pays 6 */
    const k = Math.min(S3.length - 1, Math.floor(part(u2, 0.08, 0.5) * S3.length)), late = u2 > 0.56;
    const truth = ['A', 'C', 'B', 'D', 'F', 'E', 'G'], sums = [0, 2, 3, 8, 11, 5, 9], shown = late ? Math.min(truth.length, 1 + Math.floor(part(u2, 0.58, 0.9) * truth.length)) : 0;
    fastMap(ctx, FULL, S3, u2 < 0.08 ? -1 : k, BROKEN, 1, shown >= 6 ? ['E', 'G'] : null, () => {
      if (!late) return;
      [['#fff', 18, []], [PINK, 10, [2, 20]]].forEach(([col, lw, dash]) => {
        ctx.strokeStyle = col; ctx.lineWidth = lw; ctx.setLineDash(dash);
        ctx.beginPath(); truth.slice(0, shown).forEach((n, j) => { const [px, py] = at(FULL, n); if (j) ctx.lineTo(px, py); else ctx.moveTo(px, py); }); ctx.stroke(); ctx.setLineDash([]);
      });
    });
    if (late) { const [px, py] = at(FULL, truth[shown - 1]); pill(ctx, String(sums[shown - 1]), px + 74, py + 52, PINK, '#fff', 30); }
    const said = S3[S3.length - 1].d.G;
    let line;
    if (u2 < 0.08) line = 'The road between E and F now pays 6 to whoever takes it. Same method, same map otherwise.';
    else if (!late) line = `The fast way finishes E at ${S3.find((s) => s.settle === 'E').d.E}, and never looks at E again.`;
    else if (shown < 6) line = 'Now walk one route by hand: A, C, B, D, then F, then back along the road that pays.';
    else line = `That route reaches E at 5, not 10, and G at 9. The fast way answered ${said}. "Finished" was only safe while every road cost something.`;
    wrapText(ctx, line, 50, 162, 1500, shown >= 6 ? RED : '#3c4660');
  };
  function wrapText(ctx, s, px, py, w, color) {
    ctx.font = `500 27px ${FONT}`; const words = s.split(' '); let ln = '', y = py;
    words.forEach((wd) => { if (ctx.measureText(ln + wd).width > w && ln) { txt(ctx, ln, px, y, { size: 27, color }); ln = ''; y += 36; } ln += wd + ' '; });
    txt(ctx, ln, px, y, { size: 27, color });
  }
})();
