/* 99.3 · dynamic programming · the fewest coins that make an amount.
   STORY: one drawing on one clock. The call tree of the obvious recursion grows, its repeated questions light
   up, the repeats fly together into one node per question, and the row of questions becomes the table.
   STYLE: a blackboard. Its own dark palette whatever the theme, one hue per question (not per type), type far
   larger than a figure's, no code panel (the one line of code that matters is set large at the end). */
(function () {
  const { clamp, lerp, ease, part } = XP;
  const COINS = [1, 3, 4], AMT = 7;
  const INK = '#eef1f6', MUTED = '#8590a3', BG = '#0f131a';
  const hue = (a) => `hsl(${(a * 47 + 200) % 360} 78% 66%)`;
  const dim = (a, al) => `hsl(${(a * 47 + 200) % 360} 60% 60% / ${al})`;
  const COIN = { 1: '#9fb0c8', 3: '#ffd166', 4: '#ff7b72' };

  /* the call tree, in the order the recursion makes its calls */
  const nodes = [];
  (function build(a, depth, parent, coin) {
    const n = { id: nodes.length, a, depth, parent, coin, kids: [] }; nodes.push(n);
    COINS.forEach((c) => { if (a - c >= 0) n.kids.push(build(a - c, depth + 1, n, c)); });
    return n;
  })(AMT, 0, null, 0);
  let leaf = 0;
  const leaves = nodes.filter((n) => !n.kids.length).length;
  (function place(n) {
    n.kids.forEach(place);
    n.x = n.kids.length ? n.kids.reduce((s, k) => s + k.x, 0) / n.kids.length : 90 + (leaf++) * (1420 / (leaves - 1));
    n.y = 210 + n.depth * 84;
  })(nodes[0]);
  const asked = (a, upTo = nodes.length) => nodes.filter((n) => n.a === a && n.id < upTo).length;
  const first = (a) => nodes.find((n) => n.a === a);
  const under = (n, m) => { for (let p = m; p; p = p.parent) if (p === n) return true; return false; };
  const best = [0]; for (let a = 1; a <= AMT; a += 1) best[a] = 1 + Math.min(...COINS.filter((c) => c <= a).map((c) => best[a - c]));
  const from = (a) => COINS.filter((c) => c <= a).find((c) => best[a - c] + 1 === best[a]);
  const repeats = []; for (let a = AMT; a >= 1; a -= 1) if (asked(a) > 1) repeats.push(a);
  const rowX = (a) => 240 + a * 160, ROWY = 500;

  const x = XP.mount(root, F, 'xp-coins', { w: 1600, h: 900, vars: { '--xp-bg': BG, '--xp-fg': INK, '--xp-accent': '#ffd166', '--xp-on-accent': '#1a1300', '--xp-bar': '#161b24', '--xp-font': 'ui-rounded, "SF Pro Rounded", "Nunito", system-ui, sans-serif' } });
  const T = XP.timeline(x, [
    { name: 'The obvious way', dur: 13 },
    { name: 'What it wastes', dur: 9 },
    { name: 'Ask each question once', dur: 7 },
    { name: 'Answer them in order', dur: 15 },
  ]);
  let hover = -1;
  x.c.addEventListener('pointermove', (e) => {
    const [px, py] = x.pt(e); let h = -1;
    if (T.ch < 2) nodes.forEach((n) => { if (Math.hypot(n.x - px, n.y - py) < 30) h = n.a; });
    if (h !== hover) { hover = h; x.c.style.cursor = h >= 0 ? 'pointer' : 'default'; x.redraw(); }
  });
  x.c.addEventListener('pointerleave', () => { hover = -1; x.redraw(); });

  const FONT = 'ui-rounded, "SF Pro Rounded", "Nunito", system-ui, sans-serif', MONO = 'ui-monospace, "SF Mono", Menlo, Consolas, monospace';
  const txt = (ctx, s, px, py, o = {}) => {
    ctx.font = `${o.weight || 500} ${o.size || 26}px ${o.mono ? MONO : FONT}`; ctx.fillStyle = o.color || INK; ctx.textAlign = o.align || 'left';
    ctx.globalAlpha = o.alpha == null ? 1 : o.alpha; ctx.fillText(s, px, py); ctx.globalAlpha = 1;
  };
  const blob = (ctx, px, py, r, sq, fill, stroke, lw) => {          /* a circle (sq = 0) that squares off (sq = 1) */
    const rad = lerp(r, 16, sq), h = lerp(r, 58, sq);
    ctx.beginPath(); ctx.roundRect(px - h, py - h, 2 * h, 2 * h, rad);
    if (fill) { ctx.fillStyle = fill; ctx.fill(); }
    if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw || 3; ctx.stroke(); }
  };
  const arc = (ctx, a, c, color, lw, al) => {                         /* the arc from question a to question a − c */
    const x1 = rowX(a), x2 = rowX(a - c), h = 60 + c * 46;
    ctx.globalAlpha = al; ctx.strokeStyle = color; ctx.lineWidth = lw;
    ctx.beginPath(); ctx.moveTo(x1, ROWY - 62); ctx.bezierCurveTo(x1, ROWY - 62 - h, x2, ROWY - 62 - h, x2, ROWY - 62); ctx.stroke();
    ctx.globalAlpha = 1;
  };

  x.draw = (ctx) => {
    const ch = T.ch, u0 = T.u(0), u1 = T.u(1), u2 = T.u(2), u3 = T.u(3);
    /* the board */
    ctx.fillStyle = BG; ctx.fillRect(0, 0, 1600, 900);
    ctx.fillStyle = 'rgba(255,255,255,.035)';
    for (let gx = 40; gx < 1600; gx += 40) for (let gy = 40; gy < 900; gy += 40) ctx.fillRect(gx - 1, gy - 1, 2, 2);

    const shown = ch === 0 ? Math.max(1, Math.ceil(u0 * 1.08 * nodes.length)) : nodes.length;    /* calls made so far */
    const k = ease(u2), sq = ch === 3 ? part(u3, 0, 0.1) : 0;                                         /* tree → row, circle → cell */
    const focus = ch === 1 ? repeats[Math.min(repeats.length - 1, Math.floor(u1 * repeats.length))] : hover;

    /* titles */
    const title = ['The obvious way: try every coin, then every coin after it', 'The same question, asked again and again',
      'Keep one copy of each question', 'Answer the small questions first'][ch];
    txt(ctx, title, 60, 62, { size: 46, weight: 700 });
    let sub;
    if (ch === 0) sub = `Fewest coins to make ${AMT} from 1, 3 and 4. Each circle is one call: "what is the fewest for this amount?"`;
    else if (ch === 1) sub = `"Fewest coins for ${focus}" is worked out ${asked(focus)} times, and the whole tree under it grows again each time.`;
    else if (ch === 2) sub = `${nodes.length} calls ask only ${AMT + 1} different questions. A question has one answer however it was reached.`;
    else {
      const a = Math.min(AMT, Math.floor(part(u3, 0.1, 0.86) * (AMT + 1) - 1e-9));
      const cs = COINS.filter((c) => c <= a);
      if (u3 < 0.1) sub = 'Each question needs only the answers one, three and four places to its left.';
      else if (u3 >= 0.86) sub = `${AMT} = ${from(AMT)} + ${AMT - from(AMT)}: ${best[AMT]} coins. ${AMT + 1} cells filled, where the tree made ${nodes.length} calls.`;
      else if (a === 0) sub = 'best[0] = 0: no coins make nothing.';
      else sub = `best[${a}] = 1 + min(${cs.map((c) => `best[${a - c}]`).join(', ')}) = 1 + min(${cs.map((c) => best[a - c]).join(', ')}) = ${best[a]}`;
    }
    txt(ctx, sub, 62, 116, { size: 27, color: MUTED, weight: 500, mono: ch === 3 && u3 >= 0.1 && u3 < 0.86 });

    /* the counter, top right */
    const calls = ch === 0 ? shown : nodes.length;
    if (ch < 2) { txt(ctx, String(calls), 1540, 58, { size: 64, weight: 800, align: 'right', color: '#ff7b72' }); txt(ctx, 'calls', 1540, 112, { size: 24, align: 'right', color: MUTED }); }
    else {
      txt(ctx, String(nodes.length), 1380, 58, { size: 64, weight: 800, align: 'right', color: '#ff7b72', alpha: lerp(1, 0.35, k) });
      txt(ctx, 'calls', 1380, 112, { size: 24, align: 'right', color: MUTED });
      txt(ctx, '→', 1425, 58, { size: 44, align: 'center', color: MUTED, alpha: k });
      txt(ctx, String(AMT + 1), 1540, 58, { size: 64, weight: 800, align: 'right', color: '#7ee787', alpha: k });
      txt(ctx, 'questions', 1540, 112, { size: 24, align: 'right', color: MUTED, alpha: k });
    }

    /* the arcs of the row: question a looks at a − 1, a − 3, a − 4 */
    if (ch >= 2) {
      const cur = ch === 3 && u3 >= 0.1 && u3 < 0.86 ? Math.min(AMT, Math.floor(part(u3, 0.1, 0.86) * (AMT + 1) - 1e-9)) : -1;
      const done = ch === 3 && u3 >= 0.86;
      for (let a = 1; a <= AMT; a += 1) COINS.forEach((c) => {
        if (c > a) return;
        const on = a === cur, win = done && onPath(a, c);
        arc(ctx, a, c, COIN[c], on || win ? 7 : 3, (on || win ? 1 : cur >= 0 || done ? 0.12 : 0.5) * part(u2, 0.55, 1));
      });
      const la = part(u2, 0.6, 1);
      COINS.forEach((c, i) => { ctx.fillStyle = COIN[c]; ctx.globalAlpha = la; ctx.fillRect(60, 196 + i * 40, 46, 6); ctx.globalAlpha = 1; txt(ctx, `use a ${c}`, 120, 199 + i * 40, { size: 24, color: MUTED, alpha: la }); });
    }
    function onPath(a, c) { for (let p = AMT; p > 0; p -= from(p)) if (p === a && from(p) === c) return true; return false; }

    const inFocus = (n) => nodes.some((m) => m.a === focus && under(m, n));
    /* tree edges, fading as the tree folds up */
    const ea = 1 - part(u2, 0, 0.5);
    if (ea > 0) nodes.forEach((n) => {
      if (!n.parent || n.id >= shown) return;
      const lit = focus >= 0 && inFocus(n.parent);
      ctx.strokeStyle = COIN[n.coin]; ctx.globalAlpha = ea * (lit ? 0.9 : focus >= 0 ? 0.12 : 0.45); ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(n.parent.x, n.parent.y); ctx.lineTo(n.x, n.y); ctx.stroke(); ctx.globalAlpha = 1;
    });

    /* the nodes: each flies from its place in the tree to its question's place in the row */
    const order = nodes.slice().sort((p, q) => (first(q.a) === q) - (first(p.a) === p));   /* the kept copy drawn last */
    order.forEach((n) => {
      if (n.id >= shown) return;
      const keep = first(n.a) === n, kk = ease(clamp(k * 1.25 - n.depth * 0.03));
      const px = lerp(n.x, rowX(n.a), kk), py = lerp(n.y, ROWY, kk);
      const fresh = ch === 0 ? clamp((u0 * 1.08 * nodes.length - n.id) * 1.2) : 1;
      const al = (keep ? 1 : 1 - part(u2, 0.7, 1)) * (focus >= 0 && !inFocus(n) ? 0.16 : 1) * fresh;
      if (al <= 0.01) return;
      ctx.globalAlpha = al;
      const r = lerp(26, 34, kk) * lerp(1.5, 1, fresh);
      blob(ctx, px, py, r, keep ? sq : 0, focus >= 0 && n.a === focus ? hue(n.a) : dim(n.a, 0.22), hue(n.a), focus >= 0 && n.a === focus ? 5 : 3);
      ctx.globalAlpha = al;
      const filled = ch === 3 && keep && (u3 >= 0.86 || n.a <= Math.floor(part(u3, 0.1, 0.86) * (AMT + 1) - 1e-9)) && u3 >= 0.1;
      if (sq > 0.5 && keep) {
        txt(ctx, `make ${n.a}`, px, py - 84, { size: 22, align: 'center', color: hue(n.a), alpha: al * sq });
        if (filled) txt(ctx, String(best[n.a]), px, py + 2, { size: 60, weight: 800, align: 'center', color: INK });
      } else txt(ctx, String(n.a), px, py + 1, { size: lerp(24, 30, kk), weight: 700, align: 'center', color: focus >= 0 && n.a === focus ? BG : INK, alpha: al });
      ctx.globalAlpha = 1;
    });

    /* the tally of repeats under the tree */
    const ta = 1 - part(u2, 0, 0.4);
    if (ta > 0) {
      txt(ctx, 'times asked', 60, 860, { size: 22, color: MUTED, alpha: ta });
      for (let a = AMT; a >= 0; a -= 1) {
        const n = asked(a, shown), px = 260 + (AMT - a) * 160;
        if (!n) continue;
        ctx.globalAlpha = ta * (focus >= 0 && focus !== a ? 0.3 : 1);
        blob(ctx, px, 860, 17, 0, dim(a, 0.25), hue(a), 3);
        txt(ctx, String(a), px, 861, { size: 18, weight: 700, align: 'center', alpha: ctx.globalAlpha });
        txt(ctx, `×${n}`, px + 28, 861, { size: 30, weight: 800, color: n > 1 ? '#ff7b72' : MUTED, alpha: ta * (focus >= 0 && focus !== a ? 0.3 : 1) });
        ctx.globalAlpha = 1;
      }
    }
    /* the one line of code, once the table is the picture */
    if (ch === 3) {
      const ca = part(u3, 0.04, 0.14);
      ctx.globalAlpha = ca; ctx.fillStyle = '#161b24'; ctx.beginPath(); ctx.roundRect(60, 716, 1480, 120, 18); ctx.fill(); ctx.globalAlpha = 1;
      txt(ctx, 'for a in range(1, amount + 1):', 96, 752, { size: 30, mono: true, color: MUTED, alpha: ca });
      txt(ctx, '    best[a] = 1 + min(best[a - c] for c in coins if c <= a)', 96, 800, { size: 30, mono: true, alpha: ca });
    }
    if (ch < 2 && hover >= 0 && ch !== 1) txt(ctx, `"fewest coins for ${hover}": asked ${asked(hover, shown)} time${asked(hover, shown) === 1 ? '' : 's'} so far`, 800, 162, { size: 26, align: 'center', color: hue(hover), weight: 700 });
  };
})();
