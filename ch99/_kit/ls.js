/* ---- the lesson kit, in the app's own style (ch99/_kit/ls.js; build.py copies it into a lesson's figures.js) ----
   One figure tells one lesson in named phases: Problem, Brute force, Observation, Optimization, Trace, Insight.
   It draws through figlib on the app's palette and faces, so it follows the theme and the reader's colours.

   The code is one thread through the phases. Brute force prints the obvious code. Observation prints the same
   code with the lines that do the wasted work boxed in red. Optimization shows what replaces them, either as
   the new code with its new lines boxed in green, or as an edit of the old code (red lines struck, green
   lines put in). Trace runs the new code.

   A task poses a question on the drawing. What can be pressed pulses in the accent colour. The right press
   moves the story on; a wrong one says what is wrong. Scrolling and the play button both stop at an open
   task. Only the phase bar goes past one: press a later phase, or drag ahead.

   Three switches at the top of the figure are for the sandbox only: how the figure is driven (scrolling or a
   timeline), how the phases are shown (steps, a scrubber, or a rail down the side), and how the change to
   the code is shown (boxes or an edit). */
const LS = (function () {
  const CSS = `
article figure.sim.ls{--lw:min(calc(100cqw - 48px),1560px);width:var(--lw);max-width:none;margin-left:calc((100% - var(--lw)) / 2);margin-right:0;overflow:visible}
.fig-root figure.sim.ls{width:auto;margin-left:0}
figure.sim.ls>.sim-head>span:not(.eyebrow){max-width:110ch}
.ls-opts{display:flex;flex-wrap:wrap;gap:6px 22px;align-items:center;padding:8px 14px;border-bottom:1px solid var(--rule);font:500 .78rem var(--sans);color:var(--muted)}
.ls-opts span{display:inline-flex;gap:5px;align-items:center}
.ls-opts button{font:600 .76rem var(--sans);padding:3px 10px;border-radius:12px;border:1px solid var(--rule);background:var(--panel);color:var(--muted);cursor:pointer}
.ls-opts button.on{border-color:var(--accent);color:var(--ink);background:color-mix(in srgb,var(--accent) 12%,var(--panel))}
.ls-grid{display:grid;grid-template-columns:minmax(0,1.7fr) minmax(0,1fr);align-items:start}
.ls-grid.rail{grid-template-columns:132px minmax(0,1.7fr) minmax(0,1fr)}
.ls-left,.ls-railcol{position:sticky;top:0;align-self:start;background:var(--panel)}
.ls-left{border-right:1px solid var(--rule)}
.ls-railcol{border-right:1px solid var(--rule);padding:18px 0 18px 16px;display:none}
.ls-grid.rail .ls-railcol{display:block}
.ls-grid.static .ls-left,.ls-grid.static .ls-railcol{position:static}
.ls-stage{position:relative}
.ls-stage canvas{display:block;width:100%}
/* the phase bar: one structure, three looks */
.ls-nav{display:flex;gap:12px;align-items:flex-start;padding:14px 18px 10px;border-bottom:1px solid var(--rule);user-select:none}
.ls-play{flex:0 0 auto;width:30px;height:30px;border-radius:50%;border:0;background:var(--accent);color:var(--panel);cursor:pointer;font-size:12px;line-height:30px;padding:0}
.ls-track{position:relative;flex:1 1 auto;height:52px;cursor:pointer;touch-action:none}
.ls-line{position:absolute;left:0;right:0;top:13px;height:3px;border-radius:2px;background:var(--rule)}
.ls-fill{position:absolute;left:0;top:0;bottom:0;width:0;border-radius:2px;background:var(--accent)}
.ls-node{position:absolute;top:0;display:flex;flex-direction:column;align-items:flex-start;gap:5px;padding:0;border:0;background:none;cursor:pointer;font:600 .76rem/1.1 var(--sans);color:var(--muted);text-align:left}
.ls-dot{display:grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--panel);border:2px solid var(--rule);font:700 .78rem var(--sans);color:var(--muted)}
.ls-node.done .ls-dot{background:var(--accent);border-color:var(--accent);color:var(--panel)}
.ls-node.on .ls-dot{border-color:var(--accent);color:var(--accent);box-shadow:0 0 0 4px color-mix(in srgb,var(--accent) 18%,transparent)}
.ls-node.on,.ls-node.done{color:var(--ink)}
.ls-lab i{font-style:normal;display:inline-block;margin-left:5px;font-size:.7rem;font-weight:700;color:var(--accent)}
.ls-node.solved .ls-lab i{color:var(--ok)}
.ls-node.skipped .ls-lab i{color:var(--muted)}
.ls-thumb{display:none}
/* look 2: a scrubber. A thin track with a thumb, the phase names under it */
.ls-nav.tabs .ls-track{height:40px}
.ls-nav.tabs .ls-line{top:6px;height:4px}
.ls-nav.tabs .ls-dot{width:2px;height:16px;border:0;border-radius:0;background:var(--rule);color:transparent;font-size:0;box-shadow:none}
.ls-nav.tabs .ls-node.done .ls-dot,.ls-nav.tabs .ls-node.on .ls-dot{background:var(--accent);box-shadow:none}
.ls-nav.tabs .ls-node{gap:4px;font-size:.8rem}
.ls-nav.tabs .ls-node.on .ls-lab{box-shadow:inset 0 -2px 0 var(--accent)}
.ls-nav.tabs .ls-thumb{display:block;position:absolute;top:0;width:16px;height:16px;margin-left:-8px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 3px var(--panel),0 1px 4px rgba(0,0,0,.3)}
.ls-nav.tabs .ls-lab{padding:0 0 2px 7px}
/* look 3: a rail down the side */
.ls-nav.rail{flex-direction:column;padding:0;border:0;gap:14px}
.ls-nav.rail .ls-track{width:100%;height:340px;flex:0 0 auto}
.ls-nav.rail .ls-line{left:13px;right:auto;top:0;bottom:0;width:3px;height:auto}
.ls-nav.rail .ls-fill{right:0;bottom:auto;width:auto;height:0}
.ls-nav.rail .ls-node{left:0!important;flex-direction:row;align-items:center;gap:9px}
.ls-play:focus-visible,.ls-node:focus-visible,.ls-hot:focus-visible,.ls-opts button:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
/* the task strip and what can be pressed */
.ls-turn{display:flex;gap:12px;align-items:baseline;min-height:3.4em;padding:10px 16px 12px;border-top:1px solid var(--rule);font:500 .98rem/1.4 var(--sans);color:var(--muted)}
.ls-turn.ask{background:color-mix(in srgb,var(--accent) 9%,var(--panel));color:var(--ink)}
.ls-turn .k{flex:0 0 auto;font:700 .72rem/1 var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--accent);padding:5px 9px;border:1.5px solid var(--accent);border-radius:12px}
.ls-turn.bad .m{color:var(--bad)}
.ls-turn.ok .k{color:var(--ok);border-color:var(--ok)}
.ls-turn small{display:block;margin-top:3px;font:500 .8rem var(--sans);color:var(--muted)}
.ls-turn.nudge{animation:ls-shake .3s}
.ls-hot{position:absolute;transform:translate(-50%,-50%);padding:0;border:3px solid var(--accent);background:color-mix(in srgb,var(--accent) 14%,transparent);cursor:pointer;animation:ls-pulse 1.5s ease-out infinite}
.ls-hot:hover{background:color-mix(in srgb,var(--accent) 34%,transparent)}
.ls-hot.sel{background:color-mix(in srgb,var(--accent) 40%,transparent);animation:none}
.ls-hot.no{border-color:var(--bad);animation:ls-shake .3s}
@keyframes ls-pulse{0%{box-shadow:0 0 0 0 color-mix(in srgb,var(--accent) 55%,transparent)}100%{box-shadow:0 0 0 14px transparent}}
@keyframes ls-shake{25%{margin-left:-5px}75%{margin-left:5px}}
@media (prefers-reduced-motion: reduce){.ls-hot{animation:none}}
/* the texts */
.ls-steps{padding:0 30px 45vh 30px}
.ls-step{min-height:600px;padding:44px 0 40px;opacity:.32;transition:opacity .2s}
.ls-step.on{opacity:1}
.ls-side{padding:22px 28px 26px}
.ls-side .ls-step{min-height:0;padding:0;opacity:1}
.ls-kind{font:700 .74rem/1 var(--sans);letter-spacing:.09em;text-transform:uppercase;color:var(--accent)}
.ls-step h3{font:600 1.4rem/1.2 var(--sans);margin:.45rem 0 .8rem;color:var(--ink)}
.ls-step p{font:400 1.04rem/1.6 var(--body);margin:0 0 .8rem;max-width:none}
.ls-step p.obs{padding:10px 14px;border-left:3px solid var(--accent);background:color-mix(in srgb,var(--accent) 8%,transparent);font-weight:600}
.ls-lock{margin:8px 0 0;padding:12px 14px;border:1.5px dashed var(--accent);border-radius:8px;font:500 .9rem/1.45 var(--sans);color:var(--muted)}
.ls-lock b{color:var(--accent)}
/* the code */
.ls-code{font:12.5px/1.65 var(--mono);background:var(--soft);border-radius:6px;padding:9px 6px 9px 0;margin:.9rem 0 0;overflow-x:auto}
.ls-code .ln{display:block;white-space:pre-wrap;padding:0 8px 0 4.2em;text-indent:-4.2em}
.ls-code .ln::before{content:attr(data-n);display:inline-block;width:2.2em;text-align:right;margin-right:1em;color:var(--muted);text-indent:0}
.ls-code .ln.on{background:var(--soft2);font-weight:600}
.ls-code .bx{display:block;position:relative;margin:14px 0 5px 6px;padding-top:8px;border:2px solid var(--bad);border-radius:6px;background:color-mix(in srgb,var(--bad) 7%,transparent)}
.ls-code .bx.add{border-color:var(--ok);background:color-mix(in srgb,var(--ok) 8%,transparent)}
.ls-code .bx .ln{padding-left:calc(4.2em - 8px)}
.ls-code .bx>em{position:absolute;right:8px;top:-11px;font:700 .68rem/1 var(--sans);font-style:normal;letter-spacing:.03em;padding:4px 8px;border-radius:9px;background:var(--bad);color:var(--panel);text-indent:0;white-space:nowrap}
.ls-code .bx.add>em{background:var(--ok)}
.ls-code .ln.del{color:var(--bad);text-decoration:line-through;background:color-mix(in srgb,var(--bad) 9%,transparent)}
.ls-code .ln.ins{background:color-mix(in srgb,var(--ok) 13%,transparent)}
.ls-code .ln.del::before{content:'−';color:var(--bad);text-decoration:none}
.ls-code .ln.ins::before{content:'+';color:var(--ok)}
.ls-step p.ls-codenote{font:500 .8rem/1.4 var(--sans);color:var(--muted);margin:.5rem 0 0}
.ls-codenote b.r{color:var(--bad)}.ls-codenote b.g{color:var(--ok)}
@media (max-width: 860px){.ls-grid,.ls-grid.rail{grid-template-columns:1fr}.ls-left{z-index:2;border-right:0}.ls-grid.rail .ls-railcol{display:none}}
`;
  const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
  const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const ease = (k) => { k = clamp(k); return k * k * (3 - 2 * k); };
  const part = (u, a, b) => ease(clamp((u - a) / (b - a)));
  /* a line diff of two listings: [{t: ' ' | '-' | '+', s}] */
  function diff(a, b) {
    const n = a.length, m = b.length, L = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(0));
    for (let i = n - 1; i >= 0; i -= 1) for (let j = m - 1; j >= 0; j -= 1) L[i][j] = a[i].trim() === b[j].trim() ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1]);
    const out = []; let i = 0, j = 0;
    while (i < n || j < m) {
      if (i < n && j < m && a[i].trim() === b[j].trim()) { out.push({ t: ' ', s: b[j] }); i += 1; j += 1; }
      else if (i < n && (j >= m || L[i + 1][j] >= L[i][j + 1])) { out.push({ t: '-', s: a[i] }); i += 1; }
      else { out.push({ t: '+', s: b[j] }); j += 1; }
    }
    return out;
  }
  /* a level of indentation is drawn two columns wide, so a deep line still fits the text column */
  const narrow = (s) => s.replace(/^( {4})+/, (m) => ' '.repeat(m.length / 2));
  const runs = (ls) => { const r = []; ls.slice().sort((x, y) => x - y).forEach((n) => { const q = r[r.length - 1]; if (q && q[1] === n - 1) q[1] = n; else r.push([n, n]); }); return r; };

  function lesson(root, F, id, o) {
    const fig = F.byId(root, id); if (!fig) throw new Error('no figure "' + id + '"');
    if (!document.getElementById('ls-css')) { const s = el('style'); s.id = 'ls-css'; s.textContent = CSS; document.head.appendChild(s); }
    fig.classList.add('ls');
    const P = o.phases, H = o.H, NP = P.length, K = o.code;
    const TASKS = []; P.forEach((p, i) => (p.tasks || []).forEach((t, n) => { t.solved = false; t.passed = false; t.ph = i; t.n = n; TASKS.push(t); }));
    let mode = o.mode || 'scroll', nav = o.nav || 'stepper', change = o.change || 'boxes';
    let ph = 0, u = 0, t = 0, playing = false, msg = null, hot = [], held = false;
    const DUR = (i) => P[i].dur || 8, starts = []; let total = 0; P.forEach((p, i) => { starts[i] = total; total += DUR(i); });

    /* the sandbox's switches */
    const opts = el('div', 'ls-opts');
    const group = (label, list, get, set) => {
      const s = el('span', null, label + ' '); const bs = list.map(([v, name]) => { const b = el('button', null, name); b.type = 'button'; b.addEventListener('click', () => { set(v); mark(); }); s.appendChild(b); return [v, b]; });
      const mark = () => bs.forEach(([v, b]) => b.classList.toggle('on', v === get())); mark(); opts.appendChild(s); return mark;
    };
    /* the parts */
    const grid = el('div', 'ls-grid'), railcol = el('div', 'ls-railcol'), left = el('div', 'ls-left'), stage = el('div', 'ls-stage stage'), turn = el('div', 'ls-turn'), right = el('div');
    const navEl = el('div', 'ls-nav'), play = el('button', 'ls-play'), track = el('div', 'ls-track', '<span class="ls-line"><span class="ls-fill"></span></span><span class="ls-thumb"></span>');
    play.type = 'button';
    const nodes = P.map((p, i) => {
      const b = el('button', 'ls-node', '<span class="ls-dot">' + (i + 1) + '</span><span class="ls-lab">' + p.kind + (p.tasks ? '<i></i>' : '') + '</span>'); b.type = 'button'; b.title = p.title;
      b.addEventListener('click', (e) => { e.stopPropagation(); go(i, 0, true); }); track.appendChild(b); return b;
    });
    const c = F.makeCanvas(stage, H);
    left.append(stage, turn); grid.append(railcol, left, right); fig.append(opts, grid);
    const lock = el('div', 'ls-lock', '<b>Your turn.</b> The answer goes on the drawing. To leave it unanswered, press a later phase on the bar.');
    const cards = P.map((p, i) => { const s = el('div', 'ls-step', '<span class="ls-kind">' + (i + 1) + ' · ' + p.kind + '</span><h3>' + p.title + '</h3>' + p.html); if (p.show) { p.codeEl = el('div'); s.appendChild(p.codeEl); } return s; });
    const scrollerOf = () => { for (let q = fig.parentElement; q; q = q.parentElement) { const ov = getComputedStyle(q).overflowY; if (ov === 'auto' || ov === 'scroll') return q; } return document.scrollingElement; };
    const tw = F.tween(fig, 0), redraw = () => tw.set(0);

    /* the code of a phase: 'brute', 'bad' (brute with the wasteful lines boxed), 'change', 'fast' */
    function listing(src, boxes, cls) {
      const pre = el('pre', 'ls-code'), lines = src.split('\n'); let k = 0;
      const ln = (n) => { const sp = el('span', 'ln'); sp.dataset.n = n; sp.dataset.line = n; sp.textContent = narrow(lines[n - 1]) || ' '; return sp; };
      (boxes || []).forEach(([a, b, note]) => { while (k + 1 < a) { k += 1; pre.appendChild(ln(k)); } const bx = el('span', 'bx' + (cls ? ' ' + cls : '')); if (note) bx.appendChild(el('em', null, note)); while (k < b) { k += 1; bx.appendChild(ln(k)); } pre.appendChild(bx); });
      while (k < lines.length) { k += 1; pre.appendChild(ln(k)); }
      return pre;
    }
    function fillCode() {
      P.forEach((p) => {
        if (!p.codeEl) return;
        let pre, note = '';
        if (p.show === 'brute') pre = listing(K.brute);
        else if (p.show === 'bad') { pre = listing(K.brute, [[K.bad[0], K.bad[1], K.badNote]], ''); }
        else if (p.show === 'fast') pre = listing(K.fast);
        else if (change === 'boxes') { pre = listing(K.fast, runs(K.added).map((r, i) => [r[0], r[1], i === 0 ? K.addNote || 'new' : null]), 'add'); note = 'The <b class="g">green</b> lines replace the loop boxed in <b class="r">red</b> in the obvious code.'; }
        else {
          pre = el('pre', 'ls-code');
          diff(K.brute.split('\n'), K.fast.split('\n')).forEach((d) => { const sp = el('span', 'ln' + (d.t === '-' ? ' del' : d.t === '+' ? ' ins' : '')); sp.dataset.n = ''; sp.textContent = narrow(d.s) || ' '; pre.appendChild(sp); });
          note = 'The obvious code, edited: <b class="r">red</b> lines go, <b class="g">green</b> lines come in.';
        }
        p.pre = pre; p.codeEl.replaceChildren(pre); if (note) p.codeEl.appendChild(el('p', 'ls-codenote', note));
      });
    }

    /* tasks: the first one neither answered nor skipped holds the story */
    const gate = () => TASKS.find((k) => !k.solved && !k.passed) || null;
    const task = () => { const k = gate(); return k && k.ph === ph && u >= k.a && u < k.b ? k : null; };
    const passTo = (i, v) => TASKS.forEach((k) => { if (!k.solved && (k.ph < i || (k.ph === i && k.a < v))) k.passed = true; });
    const lineY = () => { const sb = left.getBoundingClientRect(); return sb.top + Math.min(sb.height, window.innerHeight) * 0.5; };
    /* go to phase i at v. From the bar (skip = true) this goes past any open task on the way. */
    function go(i, v, skip, smooth = true) {
      if (skip) passTo(i, v);
      const g = gate(); if (g && (i > g.ph || (i === g.ph && v > g.a))) { i = g.ph; v = g.a + 5e-4; }
      if (mode === 'timeline') { t = starts[i] + v * DUR(i) + 1e-4; playing = false; set(i, v); return; }
      sync();                                                    /* later texts may have just been let in */
      const r = cards[i].getBoundingClientRect(); scrollerOf().scrollBy({ top: r.top + v * r.height - lineY() + 2, behavior: smooth ? 'smooth' : 'auto' });
    }
    function set(i, v) { const moved = i !== ph; ph = i; u = v; if (moved) msg = null; sync(moved); }
    function setNav() {
      navEl.className = 'ls-nav ' + nav; grid.classList.toggle('rail', nav === 'rail');
      navEl.replaceChildren(...(mode === 'timeline' ? [play] : []), track);
      if (nav === 'rail') railcol.replaceChildren(navEl); else { railcol.replaceChildren(); left.insertBefore(navEl, stage); }
      nodes.forEach((b, i) => { b.style.left = nav === 'rail' ? '0' : (i / NP) * 100 + '%'; b.style.top = nav === 'rail' ? (i / NP) * 100 + '%' : '0'; });
    }
    function setMode(m) {
      mode = m; playing = false; grid.classList.toggle('static', m !== 'scroll');
      right.className = m === 'scroll' ? 'ls-steps' : 'ls-side';
      if (m === 'scroll') right.replaceChildren(...cards); else t = starts[ph] + u * DUR(ph);
      setNav(); sync(true);
    }
    function sync(force) {
      const pos = (ph + u) / NP, g = gate(), fill = track.querySelector('.ls-fill'), thumb = track.querySelector('.ls-thumb');
      if (nav === 'rail') { fill.style.height = pos * 100 + '%'; fill.style.width = ''; } else { fill.style.width = pos * 100 + '%'; fill.style.height = ''; thumb.style.left = pos * 100 + '%'; }
      nodes.forEach((b, i) => {
        const ts = P[i].tasks || [];
        b.classList.toggle('on', i === ph); b.classList.toggle('done', i < ph);
        b.classList.toggle('solved', ts.length > 0 && ts.every((k) => k.solved)); b.classList.toggle('skipped', ts.some((k) => k.passed && !k.solved));
        const m = b.querySelector('i'); if (m) m.textContent = ts.every((k) => k.solved) ? '✓' : ts.some((k) => k.passed && !k.solved) ? '○' : '●'; if (m) m.title = ts.every((k) => k.solved) ? 'answered' : ts.some((k) => k.passed && !k.solved) ? 'skipped' : 'a question waits here';
      });
      play.textContent = playing ? '❚❚' : '▶'; play.setAttribute('aria-label', playing ? 'Pause' : 'Play');
      if (mode === 'scroll') {
        cards.forEach((s, i) => { s.classList.toggle('on', i === ph); s.hidden = !!g && i > g.ph; });
        if (g) { if (lock.previousSibling !== cards[g.ph]) cards[g.ph].after(lock); } else lock.remove();
      } else { lock.remove(); cards.forEach((s) => { s.hidden = false; }); if (force || right.firstChild !== cards[ph]) right.replaceChildren(cards[ph]); }
      const p = P[ph];
      if (p.pre && p.lines && (p.show === 'brute' || p.show === 'fast')) { const on = p.lines(u, api) || []; p.pre.querySelectorAll('.ln').forEach((sp) => sp.classList.toggle('on', on.includes(+sp.dataset.line))); }
      const k = task();
      turn.className = 'ls-turn' + (k ? ' ask' : '') + (msg && msg.bad ? ' bad' : '') + (msg && msg.ok ? ' ok' : '');
      if (k) turn.innerHTML = '<span class="k">Your turn</span><span class="m">' + (msg ? msg.text : k.prompt) + (held ? '<small>The story waits here. To skip the question, press a later phase on the bar.</small>' : '') + '</span>';
      else if (msg && msg.ok) turn.innerHTML = '<span class="k">Right</span><span class="m">' + msg.text + '</span>';
      else turn.innerHTML = '<span class="m">' + (p.note ? p.note(u, api) : '') + '</span>';
      const want = k ? k.targets(api) : [], key = (k ? k.ph + ':' + k.n + ':' : '') + want.map((q) => q.id + (q.sel ? '*' : '')).join(',');
      if (key !== hot.key) {
        hot.forEach((b) => b.remove()); hot = want.map((q) => {
          const b = el('button', 'ls-hot' + (q.sel ? ' sel' : '')); b.type = 'button'; b.setAttribute('aria-label', q.label || String(q.id));
          const w = q.w || 2 * q.r, h = q.h || 2 * q.r;
          b.style.cssText = `left:${(q.x / 1400) * 100}%;top:${(q.y / H) * 100}%;width:${(w / 1400) * 100}%;height:${(h / H) * 100}%;border-radius:${q.w ? '10px' : '50%'}`;
          b.addEventListener('click', () => answer(k, q.id, b)); stage.appendChild(b); return b;
        }); hot.key = key;
      }
      redraw();
    }
    function answer(k, idv, b) {
      const r = k.check(idv, api);
      if (r === true || (r && r.ok)) {
        k.solved = true; held = false; msg = { ok: true, text: (r && r.text) || '' }; sync();
        if (mode === 'timeline') { t = starts[ph] + k.b * DUR(ph) + 1e-3; playing = true; } else go(ph, Math.min(0.98, k.b + 0.01), false);
      } else if (r && r.info) { msg = { text: r.info }; sync(); }
      else { msg = { bad: true, text: r }; b.classList.remove('no'); void b.offsetWidth; b.classList.add('no'); sync(); }
    }
    const nudge = () => { held = true; sync(); turn.classList.remove('nudge'); void turn.offsetWidth; turn.classList.add('nudge'); };
    play.addEventListener('click', () => { if (!playing && task()) { nudge(); return; } if (!playing && t >= total - 1e-3) t = 0; playing = !playing; sync(); });
    /* drag along the bar: this is the one way past an open task */
    let drag = false;
    const at = (e) => { const r = track.getBoundingClientRect(), f = clamp(nav === 'rail' ? (e.clientY - r.top) / r.height : (e.clientX - r.left) / r.width, 0, 0.9999), i = Math.floor(f * NP); go(i, f * NP - i, true, false); };
    track.addEventListener('pointerdown', (e) => { if (e.target.closest('.ls-node')) return; drag = true; track.setPointerCapture(e.pointerId); at(e); });
    track.addEventListener('pointermove', (e) => { if (drag) at(e); });
    track.addEventListener('pointerup', () => { drag = false; });

    const api = {
      get ph() { return ph; }, get u() { return u; }, get mode() { return mode; },
      /* a question that is behind us, answered or skipped: the drawing shows its answer */
      solved: (i, n = 0) => !!(P[i].tasks && P[i].tasks[n] && (P[i].tasks[n].solved || P[i].tasks[n].passed)),
      asking: () => task(), redraw, part, ease, clamp,
    };
    group('Drive by', [['scroll', 'scrolling'], ['timeline', 'a timeline']], () => mode, (v) => setMode(v));
    group('Phases as', [['stepper', 'steps'], ['tabs', 'a scrubber'], ['rail', 'a side rail']], () => nav, (v) => { nav = v; setNav(); sync(true); });
    if (K) group('Code change as', [['boxes', 'boxes'], ['edit', 'an edit']], () => change, (v) => { change = v; fillCode(); sync(true); });

    /* the clock: scroll position, or time. Both stop at an open task. */
    let last = performance.now(), seen = true;
    new IntersectionObserver((es) => { seen = es[es.length - 1].isIntersecting; }).observe(fig);
    (function loop(now) {
      if (!fig.isConnected && now - last > 3000) return;
      requestAnimationFrame(loop);
      const dt = Math.min(0.1, (now - last) / 1000); last = now;
      if (!seen) return;
      const g = gate();
      if (mode === 'scroll') {
        const line = lineY(); let i = 0, v = 0;
        cards.forEach((s, n) => { if (s.hidden) return; const r = s.getBoundingClientRect(); if (r.top <= line) { i = n; v = clamp((line - r.top) / r.height, 0, 0.999); } });
        const stop = !!g && (i > g.ph || (i === g.ph && v > g.a + 5e-4));
        if (stop) { i = g.ph; v = g.a + 5e-4; }
        if (stop !== held) { held = stop; sync(); }
        if (i !== ph || Math.abs(v - u) > 0.0015) set(i, v);
      } else if (playing) {
        let nt = t + dt;
        if (g) { const gt = starts[g.ph] + g.a * DUR(g.ph) + 1e-3; if (nt >= gt) { nt = gt; playing = false; } }
        if (nt >= total) { nt = total - 1e-4; playing = false; }
        t = nt; let i = NP - 1; while (i > 0 && t < starts[i]) i -= 1;
        set(i, clamp((t - starts[i]) / DUR(i), 0, 0.999));
      }
    })(last);
    F.register(fig, { update: () => {}, draw: () => { const g = F.begin(c); o.draw({ ctx: g.ctx, H, ph, u, kind: P[ph].kind, solved: api.solved, asking: task() }); }, arrive: false });
    (window.__ls = window.__ls || {})[id] = {
      setMode, go, setNav: (v) => { nav = v; setNav(); sync(true); }, setChange: (v) => { change = v; fillCode(); sync(true); },
      seek: (x) => { let i = NP - 1; while (i > 0 && x < starts[i]) i -= 1; go(i, clamp((x - starts[i]) / DUR(i), 0, 0.999), true, false); },
      starts, get state() { return { ph, u, mode, nav, change, held, gate: gate() && gate().ph }; },
    };
    if (K) fillCode();
    setMode(mode);
    return api;
  }
  return { lesson, clamp, ease, part };
})();
