/* ---- the lesson kit, in the app's own style (ch99/_kit/ls.js; build.py copies it into a lesson's figures.js) ----
   One figure tells one lesson in named phases: Problem, Brute force, Observation, Optimization, Trace, Insight.
   It draws through figlib on the app's palette and faces, so it follows the theme and the reader's colours.
   What it adds to a Sim: the pane's width; a text and its code beside the drawing for each phase; a bar that
   names the phases; and tasks, where the reader acts on the drawing itself.
   Two ways to drive it, switched at the top of the figure:
     scroll    the drawing stays put and the phase texts scroll past it; where the reader is in a text is how
               far that phase has run. The bar shows the place and a press on a phase scrolls to it.
     timeline  the bar is a clock with a play button; the text of the current phase stands beside the drawing.
   A task poses a question over part of a phase. What can be pressed pulses in the accent colour. The right
   press moves the story on; a wrong one says what is wrong and moves nothing. Scrolling or playing on past
   the question shows the answer anyway, so a reader is never stuck. */
const LS = (function () {
  const CSS = `
article figure.sim.ls{--lw:min(calc(100cqw - 48px),1560px);width:var(--lw);max-width:none;margin-left:calc((100% - var(--lw)) / 2);margin-right:0;overflow:visible}
.fig-root figure.sim.ls{width:auto;margin-left:0}
figure.sim.ls>.sim-head>span:not(.eyebrow){max-width:110ch}
.ls-mode{display:flex;gap:8px;align-items:center;padding:8px 14px;border-bottom:1px solid var(--rule);font:500 .8rem var(--sans);color:var(--muted)}
.ls-mode button{font:600 .8rem var(--sans);padding:4px 12px;border-radius:14px;border:1px solid var(--rule);background:var(--panel);color:var(--muted);cursor:pointer}
.ls-mode button.on{border-color:var(--accent);color:var(--ink);background:color-mix(in srgb,var(--accent) 12%,var(--panel))}
.ls-grid{display:grid;grid-template-columns:minmax(0,1.7fr) minmax(0,1fr);align-items:start}
.ls-left{position:sticky;top:0;align-self:start;background:var(--panel);border-right:1px solid var(--rule);border-radius:0 0 0 8px}
.ls-stage{position:relative}
.ls-stage canvas{display:block;width:100%}
.ls-bar{display:flex;gap:6px;padding:10px 12px;align-items:center;border-bottom:1px solid var(--rule)}
.ls-seg{flex:1 1 0;min-width:0;position:relative;height:34px;border:1px solid var(--rule);border-radius:17px;background:var(--panel);overflow:hidden;cursor:pointer;font:600 .78rem var(--sans);color:var(--muted);padding:0 6px;white-space:nowrap;text-overflow:ellipsis}
.ls-seg .f{position:absolute;inset:0 auto 0 0;width:0;background:color-mix(in srgb,var(--accent) 20%,transparent);pointer-events:none}
.ls-seg .n{position:relative;pointer-events:none}
.ls-seg.on{color:var(--ink);border-color:var(--accent)}
.ls-seg.task .n::after{content:'';display:inline-block;width:7px;height:7px;border-radius:50%;margin-left:6px;background:var(--accent);vertical-align:1px}
.ls-seg.task.done .n::after{background:var(--ok)}
.ls-play{flex:0 0 auto;width:34px;height:34px;border-radius:50%;border:1px solid var(--accent);background:var(--accent);color:var(--panel);cursor:pointer;font-size:13px}
.ls-seg:focus-visible,.ls-play:focus-visible,.ls-hot:focus-visible,.ls-mode button:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
.ls-turn{display:flex;gap:12px;align-items:baseline;min-height:3.4em;padding:10px 16px 12px;border-top:1px solid var(--rule);font:500 .98rem/1.4 var(--sans);color:var(--muted)}
.ls-turn.ask{background:color-mix(in srgb,var(--accent) 9%,var(--panel));color:var(--ink)}
.ls-turn .k{flex:0 0 auto;font:700 .72rem/1 var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--accent);padding:5px 9px;border:1.5px solid var(--accent);border-radius:12px}
.ls-turn.bad .m{color:var(--bad)}
.ls-turn.ok .k{color:var(--ok);border-color:var(--ok)}
.ls-hot{position:absolute;transform:translate(-50%,-50%);padding:0;border:3px solid var(--accent);background:color-mix(in srgb,var(--accent) 14%,transparent);cursor:pointer;animation:ls-pulse 1.5s ease-out infinite}
.ls-hot:hover{background:color-mix(in srgb,var(--accent) 34%,transparent)}
.ls-hot.sel{background:color-mix(in srgb,var(--accent) 40%,transparent);animation:none}
.ls-hot.no{border-color:var(--bad);animation:ls-shake .3s}
@keyframes ls-pulse{0%{box-shadow:0 0 0 0 color-mix(in srgb,var(--accent) 55%,transparent)}100%{box-shadow:0 0 0 14px transparent}}
@keyframes ls-shake{25%{margin-left:-5px}75%{margin-left:5px}}
@media (prefers-reduced-motion: reduce){.ls-hot{animation:none}}
.ls-steps{padding:0 30px 45vh 30px}
.ls-step{min-height:600px;padding:44px 0 40px;opacity:.32;transition:opacity .2s}
.ls-step.on{opacity:1}
.ls-side{padding:22px 28px 26px}
.ls-side .ls-step{min-height:0;padding:0;opacity:1}
.ls-kind{font:700 .74rem/1 var(--sans);letter-spacing:.09em;text-transform:uppercase;color:var(--accent)}
.ls-step h3{font:600 1.4rem/1.2 var(--sans);margin:.45rem 0 .8rem;color:var(--ink)}
.ls-step p{font:400 1.04rem/1.6 var(--body);margin:0 0 .8rem;max-width:none}
.ls-step p.obs{padding:10px 14px;border-left:3px solid var(--accent);background:color-mix(in srgb,var(--accent) 8%,transparent);font-weight:600}
.ls-code{font:13px/1.65 var(--mono);background:var(--soft);border-radius:6px;padding:9px 0;margin:.9rem 0 0;overflow-x:auto}
.ls-code .ln{display:block;white-space:pre-wrap;padding:0 12px 0 4.2em;text-indent:-4.2em;border-left:3px solid transparent}
.ls-code .ln::before{content:attr(data-n);display:inline-block;width:2.2em;text-align:right;margin-right:1em;color:var(--muted)}
.ls-code .ln.on{background:var(--soft2);font-weight:600}
.ls-code .ln.new{border-left-color:var(--accent)}
.ls-code .ln.new.on{background:color-mix(in srgb,var(--accent) 24%,transparent)}
.ls-step p.ls-codenote{font:500 .8rem var(--sans);color:var(--muted);margin:.45rem 0 0}
.ls-codenote i{display:inline-block;width:0;height:12px;border-left:3px solid var(--accent);margin-right:7px;vertical-align:-2px}
@media (max-width: 860px){.ls-grid{grid-template-columns:1fr}.ls-left{z-index:2;border-right:0}}
`;
  const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
  const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const ease = (k) => { k = clamp(k); return k * k * (3 - 2 * k); };
  const part = (u, a, b) => ease(clamp((u - a) / (b - a)));
  const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');

  function lesson(root, F, id, o) {
    const fig = F.byId(root, id); if (!fig) throw new Error('no figure "' + id + '"');
    if (!document.getElementById('ls-css')) { const s = el('style'); s.id = 'ls-css'; s.textContent = CSS; document.head.appendChild(s); }
    fig.classList.add('ls');
    const P = o.phases, H = o.H;
    P.forEach((p) => { (p.tasks || []).forEach((t) => { t.solved = false; t.passed = false; }); });
    let mode = o.mode || 'scroll', ph = 0, u = 0, t = 0, playing = false, msg = null, hot = [];
    const total = P.reduce((a, p) => a + (p.dur || 8), 0), starts = []; P.reduce((a, p, i) => { starts[i] = a; return a + (p.dur || 8); }, 0);

    /* the parts that stay whatever the mode: the switch, the bar, the stage, the task strip */
    const modeRow = el('div', 'ls-mode', '<span>Sandbox: drive this figure by</span>');
    const mb = { scroll: el('button', null, 'scrolling'), timeline: el('button', null, 'a timeline') };
    Object.entries(mb).forEach(([m, b]) => { b.type = 'button'; b.addEventListener('click', () => setMode(m)); modeRow.appendChild(b); });
    const grid = el('div', 'ls-grid'), left = el('div', 'ls-left'), bar = el('div', 'ls-bar'), stage = el('div', 'ls-stage stage'), turn = el('div', 'ls-turn');
    const play = el('button', 'ls-play'); play.type = 'button';
    const segs = P.map((p, i) => {
      const b = el('button', 'ls-seg' + (p.tasks ? ' task' : ''), '<span class="f"></span><span class="n">' + p.kind + '</span>'); b.type = 'button'; b.title = p.kind + ': ' + p.title;
      b.addEventListener('click', () => jump(i, 0)); return b;
    });
    const c = F.makeCanvas(stage, H);
    left.append(bar, stage, turn); grid.appendChild(left); fig.append(modeRow, grid);
    const cards = P.map((p, i) => {
      const s = el('div', 'ls-step', '<span class="ls-kind">' + (i + 1) + ' · ' + p.kind + '</span><h3>' + p.title + '</h3>' + p.html);
      if (p.code) {
        const pre = el('pre', 'ls-code'); p.code.src.split('\n').forEach((ln, k) => { const sp = el('span', 'ln' + ((p.code.added || []).includes(k + 1) ? ' new' : '')); sp.dataset.n = k + 1; sp.textContent = ln || ' '; pre.appendChild(sp); });
        s.appendChild(pre); p.pre = pre;
        if (p.code.added) s.appendChild(el('p', 'ls-codenote', '<i></i>the lines the observation adds'));
      }
      return s;
    });
    const right = el('div'); grid.appendChild(right);
    /* the element the reader scrolls: looked for when needed, since the page may not be laid out yet */
    const scrollerOf = () => { for (let q = fig.parentElement; q; q = q.parentElement) { const ov = getComputedStyle(q).overflowY; if (ov === 'auto' || ov === 'scroll') return q; } return document.scrollingElement; };
    const tw = F.tween(fig, 0), redraw = () => tw.set(0);

    function setMode(m) {
      mode = m; playing = false;
      Object.entries(mb).forEach(([k, b]) => b.classList.toggle('on', k === m));
      right.className = m === 'scroll' ? 'ls-steps' : 'ls-side';
      bar.replaceChildren(...(m === 'timeline' ? [play] : []), ...segs);
      left.style.position = m === 'scroll' ? 'sticky' : 'static';
      if (m === 'scroll') right.replaceChildren(...cards); else { t = starts[ph] + u * (P[ph].dur || 8); }
      sync(true);
    }
    const task = () => (P[ph].tasks || []).find((k) => !k.solved && u >= k.a && u < k.b) || null;
    function jump(i, v) {
      if (mode === 'timeline') { t = starts[i] + v * (P[i].dur || 8) + 1e-4; playing = false; set(i, v); return; }
      const r = cards[i].getBoundingClientRect(), line = lineY();
      const dy = r.top + v * r.height - line + 2;
      scrollerOf().scrollBy({ top: dy, behavior: 'smooth' });
    }
    const lineY = () => { const sb = left.getBoundingClientRect(); return sb.top + Math.min(sb.height, window.innerHeight) * 0.5; };
    function set(i, v) { const moved = i !== ph; ph = i; u = v; if (moved) msg = null; sync(moved); }
    function sync(force) {
      segs.forEach((b, i) => {
        b.querySelector('.f').style.width = (i < ph ? 100 : i > ph ? 0 : u * 100) + '%'; b.classList.toggle('on', i === ph);
        b.classList.toggle('done', !!P[i].tasks && P[i].tasks.every((k) => k.solved));
      });
      play.textContent = playing ? '❚❚' : '▶'; play.setAttribute('aria-label', playing ? 'Pause' : 'Play');
      if (mode === 'scroll') cards.forEach((s, i) => s.classList.toggle('on', i === ph));
      else if (force || right.firstChild !== cards[ph]) right.replaceChildren(cards[ph]);
      const p = P[ph];
      if (p.pre) { const on = p.lines ? p.lines(u, api) || [] : []; Array.from(p.pre.children).forEach((sp, k) => sp.classList.toggle('on', on.includes(k + 1))); }
      /* the task strip and what can be pressed */
      const k = task();
      turn.className = 'ls-turn' + (k ? ' ask' : '') + (msg && msg.bad ? ' bad' : '') + (msg && msg.ok ? ' ok' : '');
      if (k) turn.innerHTML = '<span class="k">Your turn</span><span class="m">' + (msg ? msg.text : k.prompt) + '</span>';
      else if (msg && msg.ok) turn.innerHTML = '<span class="k">Right</span><span class="m">' + msg.text + '</span>';
      else turn.innerHTML = '<span class="m">' + (p.note ? p.note(u, api) : '') + '</span>';
      const want = k ? k.targets(api) : [], key = (k ? P.indexOf(p) + ':' + p.tasks.indexOf(k) + ':' : '') + want.map((q) => q.id + (q.sel ? '*' : '')).join(',');
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
        k.solved = true; msg = { ok: true, text: (r && r.text) || k.right || '' }; sync();
        if (mode === 'timeline') { t = starts[ph] + k.b * (P[ph].dur || 8) + 1e-3; playing = true; } else jump(ph, Math.min(0.98, k.b + 0.01));
      } else if (r && r.info) { msg = { text: r.info }; sync(); }
      else { msg = { bad: true, text: r }; b.classList.remove('no'); void b.offsetWidth; b.classList.add('no'); sync(); }
    }
    play.addEventListener('click', () => {
      if (!playing && t >= total - 1e-3) t = 0;
      const k = task(); if (!playing && k) k.passed = true;        /* play on past a question: the story shows the answer */
      playing = !playing; sync();
    });
    const api = {
      get ph() { return ph; }, get u() { return u; }, get mode() { return mode; },
      solved: (i, n = 0) => !!(P[i].tasks && P[i].tasks[n] && P[i].tasks[n].solved),
      asking: () => task(), redraw, part, ease, clamp,
    };
    /* the clock: scroll position, or time */
    let last = performance.now(), seen = true;
    new IntersectionObserver((es) => { seen = es[es.length - 1].isIntersecting; }).observe(fig);
    (function loop(now) {
      if (!fig.isConnected && now - last > 3000) return;
      requestAnimationFrame(loop);
      const dt = Math.min(0.1, (now - last) / 1000); last = now;
      if (!seen) return;
      if (mode === 'scroll') {
        const line = lineY(); let i = 0, v = 0;
        cards.forEach((s, n) => { const r = s.getBoundingClientRect(); if (r.top <= line) { i = n; v = clamp((line - r.top) / r.height, 0, 0.999); } });
        if (i !== ph || Math.abs(v - u) > 0.0015) set(i, v);
      } else if (playing) {
        let nt = t + dt;
        const p = P[ph], k = (p.tasks || []).find((q) => !q.solved && !q.passed && starts[ph] + q.a * (p.dur || 8) >= t - 1e-6 && starts[ph] + q.a * (p.dur || 8) < nt);
        if (k) { nt = starts[ph] + k.a * (p.dur || 8) + 1e-3; playing = false; }
        if (nt >= total) { nt = total - 1e-4; playing = false; }
        t = nt; let i = P.length - 1; while (i > 0 && t < starts[i]) i -= 1;
        set(i, clamp((t - starts[i]) / (P[i].dur || 8), 0, 0.999));
      }
    })(last);
    F.register(fig, { update: () => {}, draw: () => { const g = F.begin(c); o.draw(Object.assign({ ctx: g.ctx, H }, { ph, u, kind: P[ph].kind, solved: api.solved, asking: task() })); }, arrive: false });
    (window.__ls = window.__ls || {})[id] = { setMode, jump, seek: (x) => { t = x; playing = false; let i = P.length - 1; while (i > 0 && t < starts[i]) i -= 1; set(i, clamp((t - starts[i]) / (P[i].dur || 8), 0, 0.999)); }, starts, get state() { return { ph, u, mode }; } };
    setMode(mode);
    return api;
  }
  return { lesson, clamp, ease, part, esc };
})();
