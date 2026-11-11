/* 99.6 · bit manipulation · the number without a twin (XOR).
   STORY: one panel, six steps, no clock and no play button. Each step ends with something for the reader to
   do (count a column, press the key that folds the next number in, predict a result), and the story does not
   move on until it is done.
   STYLE: a panel of lamps. Black whatever the theme, glowing lamps, one monospaced face for everything, and
   the three lines of code set as large as the drawing. */
(function () {
  const { clamp, el } = XP;
  const BG = '#040705', ON = '#3dff8f', OFF = '#0e2618', AMBER = '#ffb000', DIMTXT = '#5f7a6a', TXT = '#c9f5da', RED = '#ff5d5d';
  const MONO = 'ui-monospace, "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace';
  const BASE = [5, 9, 3, 5, 12, 3, 9], W = [8, 4, 2, 1];
  const bit = (v, b) => (v & W[b] ? 1 : 0);
  const bin = (v) => W.map((w) => (v & w ? '1' : '0')).join('');
  /* the obvious way: for each number, look through the others for its twin */
  const CMP = [];
  (function () { for (let i = 0; i < BASE.length; i += 1) { let twin = false; for (let j = 0; j < BASE.length && !twin; j += 1) { if (j === i) continue; twin = BASE[i] === BASE[j]; CMP.push({ i, j, eq: twin }); } if (!twin) return; } })();
  const STEPS = ['The obvious way', 'One column', 'Another column', 'All four', 'Fold them in', 'Three lines'];

  const x = XP.mount(root, F, 'xp-twin', { w: 1600, h: 900, vars: { '--xp-bg': BG, '--xp-fg': TXT, '--xp-accent': ON, '--xp-on-accent': '#02160a', '--xp-bar': '#0a120d', '--xp-font': MONO } });
  const bar = el('div', 'xp-bar'); bar.style.cssText = 'align-items:center;flex-wrap:wrap;min-height:68px'; x.wrap.appendChild(bar);
  const st = { step: 0, t: 0, col: {}, said: '', bad: false, fold: 0, pred: false, extra: false, done: {} };
  const nums = () => (st.extra ? BASE.concat(3) : BASE);
  const acc = (n) => nums().slice(0, n).reduce((a, v) => a ^ v, 0);
  const lit = (b) => BASE.filter((v) => bit(v, b)).length;
  const btn = (label, act, cls) => { const b = el('button', 'xp-btn' + (cls ? ' ' + cls : '')); b.type = 'button'; b.textContent = label; b.style.fontFamily = MONO; b.addEventListener('click', act); return b; };
  const go = (s) => { st.step = clamp(s, 0, STEPS.length - 1); st.t = 0; st.said = ''; st.bad = false; ui(); };
  function ui() {
    bar.replaceChildren();
    const back = btn('< back', () => go(st.step - 1), 'ghost'); back.disabled = st.step === 0; bar.appendChild(back);
    const mid = el('div'); mid.style.cssText = 'flex:1 1 auto;display:flex;gap:10px;justify-content:center;flex-wrap:wrap'; bar.appendChild(mid);
    const s = st.step;
    if (s === 1 || s === 2) {
      const b = s === 1 ? 3 : 1, odd = lit(b) % 2 === 1;
      if (st.col[b] == null) ['odd', 'even'].forEach((w) => mid.appendChild(btn(w, () => {
        if ((w === 'odd') === odd) { st.col[b] = odd ? 1 : 0; st.bad = false; st.said = `${lit(b)} lit. Each pair lights a column twice or not at all, so the pairs add an even number${odd ? ', and the one left over is the loner\'s: its lamp here is ON.' : ' and nothing is left over: the loner\'s lamp here is OFF.'}`; st.done[s] = true; }
        else { st.bad = true; st.said = `Count again: ${BASE.filter((v) => bit(v, b)).join(', ')} are lit.`; }
        ui();
      })));
    }
    if (s === 4) {
      const n = nums();
      if (st.fold === 3 && !st.pred) ['1111', '1010', '0101'].forEach((w) => mid.appendChild(btn(w, () => {
        if (w === bin(acc(4))) { st.pred = true; st.bad = false; st.said = 'Right. XOR flips exactly the lamps that 5 lights. The first 5 switched them, the second switches them back: the pair has gone.'; st.fold = 4; }
        else { st.bad = true; st.said = w === '1111' ? 'XOR with 5 changes something: it flips every lamp that 5 lights.' : 'XOR flips the lamps that 5 lights (the 4 and the 1) and leaves the others as they were.'; }
        ui();
      })));
      else if (st.fold < n.length) mid.appendChild(btn(`acc ^= ${n[st.fold]}`, () => { st.fold += 1; st.said = st.fold === n.length ? `Seven XORs, one pass. The pairs have all cancelled and ${acc(n.length)} is left.` : ''; if (st.fold === n.length) st.done[4] = true; ui(); }));
    }
    if (s === 5) mid.appendChild(btn(st.extra ? 'take the third 3 away' : 'give 3 a third copy', () => { st.extra = !st.extra; ui(); }, 'ghost'));
    const ready = s === 0 ? st.t > CMP.length * 0.24 + 0.4 || st.done[0] : s === 3 ? st.t > 3.2 || st.done[3] : s === 5 ? true : !!st.done[s];
    const next = btn(s === 0 && !ready ? 'skip >' : 'next >', () => { st.done[s] = true; if (s === 3) { st.col[0] = lit(0) % 2; st.col[2] = lit(2) % 2; } go(s + 1); });
    next.disabled = s === STEPS.length - 1 || (!ready && s !== 0); bar.appendChild(next);
    x.redraw();
  }
  let wasReady = false;
  x.tick = (dt) => {
    st.t += dt;
    const anim = (st.step === 0 && st.t < CMP.length * 0.24 + 0.6) || (st.step === 3 && st.t < 3.4);
    const ready = (st.step === 0 && st.t > CMP.length * 0.24 + 0.4) || (st.step === 3 && st.t > 3.2);
    if (ready && !wasReady) { if (st.step === 3) { st.col[0] = lit(0) % 2; st.col[2] = lit(2) % 2; } ui(); }
    wasReady = ready;
    return anim;
  };

  const txt = (ctx, s, px, py, o = {}) => {
    ctx.font = `${o.weight || 500} ${o.size || 28}px ${MONO}`; ctx.fillStyle = o.color || TXT; ctx.textAlign = o.align || 'left';
    ctx.globalAlpha = o.alpha == null ? 1 : o.alpha; if (o.glow) { ctx.shadowColor = o.color || TXT; ctx.shadowBlur = o.glow; }
    ctx.fillText(s, px, py); ctx.shadowBlur = 0; ctx.globalAlpha = 1;
  };
  const wrap = (ctx, s, px, py, w, o = {}) => {
    ctx.font = `${o.weight || 500} ${o.size || 26}px ${MONO}`; let ln = '', y = py;
    s.split(' ').forEach((wd) => { if (ctx.measureText(ln + wd).width > w && ln) { txt(ctx, ln, px, y, o); ln = ''; y += (o.size || 26) * 1.45; } ln += wd + ' '; });
    txt(ctx, ln, px, y, o); return y + (o.size || 26) * 1.45;
  };
  const lamp = (ctx, px, py, on, color, r = 22, al = 1) => {
    ctx.globalAlpha = al; ctx.beginPath(); ctx.arc(px, py, r, 0, 7);
    if (on) { ctx.shadowColor = color; ctx.shadowBlur = 34; ctx.fillStyle = color; ctx.fill(); ctx.shadowBlur = 0; ctx.fillStyle = 'rgba(255,255,255,.55)'; ctx.beginPath(); ctx.arc(px - r * 0.3, py - r * 0.3, r * 0.28, 0, 7); ctx.fill(); }
    else { ctx.fillStyle = OFF; ctx.fill(); ctx.strokeStyle = 'rgba(61,255,143,.22)'; ctx.lineWidth = 2; ctx.stroke(); }
    ctx.globalAlpha = 1;
  };
  const ROWY = (i) => 236 + i * 60, COLX = (b) => 500 + b * 118, RESY = 760;

  x.draw = (ctx) => {
    const s = st.step, n = nums();
    ctx.fillStyle = BG; ctx.fillRect(0, 0, 1600, 900);
    /* the rail: where the reader is in the story */
    STEPS.forEach((name, i) => {
      const px = 60 + i * 250, cur = i === s;
      ctx.fillStyle = i < s ? ON : cur ? AMBER : '#16301f'; ctx.fillRect(px, 40, 232, 8);
      txt(ctx, `${i + 1} ${name}`, px, 72, { size: 20, color: cur ? AMBER : i < s ? DIMTXT : '#2c4a39', weight: cur ? 700 : 500 });
    });
    txt(ctx, 'FIND THE NUMBER WITHOUT A TWIN', 60, 134, { size: 38, weight: 700, color: ON, glow: 18 });

    const lamps = s >= 1, la = s === 1 ? clamp(st.t / 0.8) : 1;
    const hot = s === 1 ? 3 : s === 2 ? 1 : s === 3 ? (st.t < 1.6 ? 2 : 0) : -1;
    if (lamps) W.forEach((w, b) => txt(ctx, String(w), COLX(b), 184, { size: 24, align: 'center', color: b === hot ? AMBER : DIMTXT, alpha: la }));
    if (hot >= 0) { ctx.fillStyle = 'rgba(255,176,0,.10)'; ctx.strokeStyle = 'rgba(255,176,0,.7)'; ctx.lineWidth = 2; ctx.beginPath(); ctx.roundRect(COLX(hot) - 44, 204, 88, n.length * 60 + 6, 16); ctx.fill(); ctx.stroke(); }
    /* the obvious way's two fingers */
    const k = s === 0 ? Math.min(CMP.length, Math.floor(st.t / 0.24)) : 0, c = k ? CMP[k - 1] : null, found = s === 0 && k === CMP.length;
    n.forEach((v, i) => {
      const y = ROWY(i), folded = s === 4 && i < st.fold, nextUp = s === 4 && i === st.fold;
      const isI = c && c.i === i, isJ = c && c.j === i;
      const col = found && i === 4 ? AMBER : isI ? AMBER : isJ ? (c.eq ? ON : RED) : folded ? '#2c4a39' : TXT;
      txt(ctx, String(v).padStart(2, ' '), 300, y, { size: 44, weight: 700, align: 'right', color: col, glow: isI || isJ || nextUp ? 16 : 0 });
      if (isI) txt(ctx, 'this one', 120, y, { size: 22, color: AMBER });
      if (isJ) txt(ctx, c.eq ? '= twin' : '≠', 330, y, { size: 24, color: c.eq ? ON : RED });
      if (nextUp) txt(ctx, 'next >', 120, y, { size: 22, color: AMBER });
      if (st.extra && i === n.length - 1) txt(ctx, 'extra', 120, y, { size: 22, color: RED });
      if (lamps) W.forEach((w, b) => lamp(ctx, COLX(b), y, bit(v, b), ON, 21, la * (folded ? 0.25 : hot >= 0 && b !== hot ? 0.3 : 1)));
    });

    /* the bottom row: the loner's lamps as they are worked out, or acc as numbers are folded in */
    if (s >= 1) {
      ctx.strokeStyle = '#1c3a28'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(100, RESY - 52); ctx.lineTo(960, RESY - 52); ctx.stroke();
      if (s <= 3) {
        txt(ctx, 'loner', 300, RESY, { size: 30, align: 'right', color: AMBER });
        W.forEach((w, b) => { const kn = st.col[b] != null || (s === 3 && ((b === 2 && st.t > 1.3) || (b === 0 && st.t > 2.9))); if (kn) lamp(ctx, COLX(b), RESY, lit(b) % 2, AMBER, 24); else txt(ctx, '?', COLX(b), RESY, { size: 34, align: 'center', color: DIMTXT }); });
        if (s === 3 && st.t > 3.1) txt(ctx, '= 12', COLX(3) + 70, RESY, { size: 40, weight: 700, color: AMBER, glow: 14 });
      } else {
        const a = s === 4 ? acc(st.fold) : acc(n.length);
        txt(ctx, 'acc', 300, RESY, { size: 30, align: 'right', color: AMBER });
        W.forEach((w, b) => lamp(ctx, COLX(b), RESY, bit(a, b), st.extra ? RED : AMBER, 24));
        txt(ctx, `= ${a}`, COLX(3) + 70, RESY, { size: 40, weight: 700, color: st.extra ? RED : AMBER, glow: 14 });
      }
    }

    /* the right side: what to do, and what came of it */
    const RX = 1030, RW = 520;
    let y = 220;
    const say = (t, o) => { y = wrap(ctx, t, RX, y, RW, Object.assign({ size: 26 }, o)) + 16; };
    if (s === 0) {
      say('Seven numbers. Six are in pairs and one has no twin.');
      say('The obvious way: take each number in turn and look through the others for its twin.', { color: DIMTXT });
      txt(ctx, String(k), RX, 520, { size: 120, weight: 700, color: found ? AMBER : RED, glow: 20 });
      txt(ctx, 'comparisons', RX, 600, { size: 26, color: DIMTXT });
      if (found) { y = 660; say('12 has no twin. For n numbers this is about n × n comparisons.', { color: AMBER }); }
    } else if (s === 1) {
      say('Each number is four lamps: its 8, its 4, its 2 and its 1.');
      say('Look at the column of 1s only. Is the number of lit lamps odd or even?', { color: AMBER });
    } else if (s === 2) {
      say('Now the column of 4s. Odd or even?', { color: AMBER });
    } else if (s === 3) {
      say('The other two columns go the same way.');
      say('2s: two lit, even, so OFF. 8s: three lit, odd, so ON.', { color: DIMTXT });
      if (st.t > 3.1) say('ON ON OFF OFF is 12. Keeping only "odd or even" of a column is what XOR does to a bit.', { color: AMBER });
    } else if (s === 4) {
      say('No need to count columns. Start acc at 0 and XOR each number into it: a lamp flips each time a number lights it.');
      if (st.fold === 3 && !st.pred) say('acc is 1111. What is it after XOR with the second 5, which is 0101?', { color: AMBER });
      else if (st.fold < n.length) say('Press the key to fold the next number in.', { color: AMBER });
    } else {
      ctx.fillStyle = '#0a160f'; ctx.beginPath(); ctx.roundRect(RX - 30, 190, RW + 60, 250, 18); ctx.fill();
      txt(ctx, 'acc = 0', RX, 240, { size: 46, weight: 700, color: ON, glow: 12 });
      txt(ctx, 'for x in nums:', RX, 312, { size: 46, weight: 700, color: ON, glow: 12 });
      txt(ctx, '    acc ^= x', RX, 384, { size: 46, weight: 700, color: ON, glow: 12 });
      y = 500;
      if (!st.extra) { say(`${n.length} XORs against ${CMP.length} comparisons, and no memory but acc.`); say('x ^ x = 0, and the order does not matter: every pair cancels itself.', { color: AMBER }); }
      else say('With three 3s the answer is 15, a number that is not even in the list. The trick stands on every other number coming exactly twice.', { color: RED });
    }
    if (st.said) { y = Math.max(y, 520); say(st.said, { color: st.bad ? RED : ON }); }
    /* the glass */
    ctx.fillStyle = 'rgba(0,0,0,.16)'; for (let gy = 0; gy < 900; gy += 4) ctx.fillRect(0, gy, 1600, 1);
  };
  ui();
})();
