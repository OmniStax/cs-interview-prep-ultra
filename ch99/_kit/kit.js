/* ---- the sandbox stage kit (ch99/_kit/kit.js; build.py copies it into each experiment's figures.js) ----
   These experiments deliberately step outside the app's figure rules: they do not draw through figlib, they
   leave the text column for the pane's width, hide the Sim head, bring their own palette whatever the theme,
   and build their own controls. XP.mount gives a figure a canvas in logical units and a frame loop;
   XP.timeline gives it one clock cut into named chapters, with a bar to play and scrub it. */
const XP = (function () {
  const CSS = `
article figure.sim.xp{--xw:min(calc(100cqw - 32px),1680px);width:var(--xw);max-width:none;margin:28px 0 28px calc((100% - var(--xw)) / 2);padding:0;border:0;border-radius:14px;overflow:hidden;background:none;box-shadow:0 1px 0 rgba(0,0,0,.08),0 12px 40px rgba(0,0,0,.18)}
.fig-root figure.sim.xp{width:auto;margin-left:0}
figure.sim.xp>.sim-head{display:none}
figure.sim.xp .xp-wrap{position:relative;background:var(--xp-bg);color:var(--xp-fg);font-family:var(--xp-font,ui-sans-serif,system-ui,sans-serif)}
figure.sim.xp canvas{display:block;width:100%;touch-action:manipulation}
figure.sim.xp .xp-bar{display:flex;align-items:stretch;gap:10px;padding:10px 14px 12px;background:var(--xp-bar,rgba(127,127,127,.12))}
figure.sim.xp .xp-play{flex:0 0 auto;width:44px;height:44px;border-radius:50%;border:0;background:var(--xp-accent);color:var(--xp-on-accent,#fff);font-size:18px;cursor:pointer;display:grid;place-items:center}
figure.sim.xp .xp-play:focus-visible,figure.sim.xp .xp-seg:focus-visible,figure.sim.xp .xp-btn:focus-visible{outline:3px solid var(--xp-fg);outline-offset:2px}
figure.sim.xp .xp-segs{flex:1 1 auto;display:flex;gap:4px;min-width:0}
figure.sim.xp .xp-seg{position:relative;min-width:0;border:0;padding:0;background:none;color:inherit;font:inherit;text-align:left;cursor:pointer}
figure.sim.xp .xp-seg .xp-track{display:block;height:8px;border-radius:4px;background:var(--xp-track,rgba(127,127,127,.35));overflow:hidden}
figure.sim.xp .xp-seg .xp-fill{display:block;height:100%;width:0;background:var(--xp-accent)}
figure.sim.xp .xp-seg .xp-name{display:block;margin-top:7px;font-size:13px;line-height:1.2;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;opacity:.6}
figure.sim.xp .xp-seg.on .xp-name{opacity:1;font-weight:600}
figure.sim.xp .xp-btn{border:0;border-radius:10px;padding:10px 18px;font:inherit;font-size:16px;font-weight:600;cursor:pointer;background:var(--xp-accent);color:var(--xp-on-accent,#fff)}
figure.sim.xp .xp-btn.ghost{background:none;color:inherit;box-shadow:inset 0 0 0 2px currentColor;opacity:.85}
figure.sim.xp .xp-btn:disabled{opacity:.35;cursor:default}
`;
  const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
  const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const lerp = (a, b, k) => a + (b - a) * k;
  const ease = (k) => { k = clamp(k); return k * k * (3 - 2 * k); };
  /* progress of the part [a, b] of a 0..1 run, eased */
  const part = (u, a, b) => ease(clamp((u - a) / (b - a)));

  function mount(root, F, id, o) {
    const fig = F.byId(root, id); if (!fig) throw new Error('no figure "' + id + '"');
    if (!document.getElementById('xp-css')) { const s = el('style'); s.id = 'xp-css'; s.textContent = CSS; document.head.appendChild(s); }
    fig.classList.add('xp');
    const wrap = el('div', 'xp-wrap'); Object.entries(o.vars || {}).forEach(([k, v]) => wrap.style.setProperty(k, v));
    fig.appendChild(wrap);
    const c = el('canvas'); c.style.aspectRatio = o.w + ' / ' + o.h; (o.host ? o.host(wrap) : wrap).appendChild(c);
    const LW = o.w, LH = o.h;
    let dirty = true, vis = true, last = performance.now();
    const x = {
      fig, wrap, c, LW, LH, draw: null, tick: null,
      redraw() { dirty = true; },
      /* a pointer event in logical units */
      pt(e) { const b = c.getBoundingClientRect(), k = LW / b.width; return [(e.clientX - b.left) * k, (e.clientY - b.top) * k]; },
    };
    new IntersectionObserver((es) => { vis = es[es.length - 1].isIntersecting; if (vis) dirty = true; }).observe(fig);
    new ResizeObserver(() => { dirty = true; }).observe(c);
    (function loop(now) {
      if (!fig.isConnected && now - last > 2000) return;          /* the page has gone: stop */
      requestAnimationFrame(loop);
      const dt = Math.min(0.1, (now - last) / 1000); last = now;
      if (!vis) return;
      if (x.tick && x.tick(dt)) dirty = true;
      if (!dirty || !x.draw || !c.clientWidth) return;
      dirty = false;
      const dpr = Math.min(2, window.devicePixelRatio || 1), bw = Math.round(c.clientWidth * dpr), bh = Math.round((c.clientWidth * LH / LW) * dpr);
      if (c.width !== bw || c.height !== bh) { c.width = bw; c.height = bh; }
      const ctx = c.getContext('2d'); ctx.setTransform(bw / LW, 0, 0, bw / LW, 0, 0); ctx.clearRect(0, 0, LW, LH);
      ctx.lineCap = 'round'; ctx.lineJoin = 'round'; ctx.textBaseline = 'middle';
      x.draw(ctx);
    })(last);
    (window.__xp = window.__xp || {})[id] = x;      /* a handle for the console and for tests */
    return x;
  }

  /* One clock, cut into chapters [{name, dur}] (seconds at 1×). The bar: play, one segment a chapter. */
  function timeline(x, chapters, o = {}) {
    const total = chapters.reduce((a, c) => a + c.dur, 0), starts = []; chapters.reduce((a, c, i) => { starts[i] = a; return a + c.dur; }, 0);
    const bar = el('div', 'xp-bar'), play = el('button', 'xp-play'), segs = el('div', 'xp-segs');
    play.type = 'button'; bar.append(play, segs); x.wrap.appendChild(bar);
    const T = {
      t: 0, playing: false, total, starts,
      get ch() { let i = chapters.length - 1; while (i > 0 && T.t < starts[i]) i -= 1; return i; },
      /* 0..1 inside chapter i (0 before it, 1 after) */
      u(i) { return clamp((T.t - starts[i]) / chapters[i].dur); },
      seek(t) { T.t = clamp(t, 0, total); sync(); x.redraw(); },
      play() { if (T.t >= total - 1e-6) T.t = 0; T.playing = true; sync(); },
      pause() { T.playing = false; sync(); },
      /* a gate: the clock will not pass t until open() is called (the reader must do something first) */
      gates: [],
    };
    const fills = chapters.map((ch, i) => {
      const b = el('button', 'xp-seg'); b.type = 'button'; b.style.flex = ch.dur + ' 1 0';
      b.innerHTML = '<span class="xp-track"><span class="xp-fill"></span></span><span class="xp-name">' + (i + 1) + '. ' + ch.name + '</span>';
      const at = (e) => { const r = b.querySelector('.xp-track').getBoundingClientRect(); T.seek(starts[i] + clamp((e.clientX - r.left) / r.width) * ch.dur); };
      let down = false;
      b.addEventListener('pointerdown', (e) => { down = true; b.setPointerCapture(e.pointerId); T.pause(); at(e); });
      b.addEventListener('pointermove', (e) => { if (down) at(e); });
      b.addEventListener('pointerup', () => { down = false; });
      b.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); T.seek(starts[i]); T.play(); } });
      segs.appendChild(b); return b;
    });
    function sync() {
      play.textContent = T.playing ? '❚❚' : '▶'; play.setAttribute('aria-label', T.playing ? 'Pause' : 'Play');
      const ch = T.ch;
      fills.forEach((b, i) => { b.querySelector('.xp-fill').style.width = (T.u(i) * 100) + '%'; b.classList.toggle('on', i === ch); });
    }
    play.addEventListener('click', () => (T.playing ? T.pause() : T.play()));
    x.wrap.tabIndex = 0;
    x.wrap.addEventListener('keydown', (e) => {
      if (e.target !== x.wrap) return;
      if (e.key === ' ') { e.preventDefault(); T.playing ? T.pause() : T.play(); }
      if (e.key === 'ArrowRight') { e.preventDefault(); T.pause(); T.seek(T.t + (e.shiftKey ? 2 : 0.4)); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); T.pause(); T.seek(T.t - (e.shiftKey ? 2 : 0.4)); }
    });
    const tick = x.tick;
    x.tick = (dt) => {
      const more = tick ? tick(dt) : false;
      if (!T.playing) return more;
      let t = T.t + dt * (o.speed || 1);
      const g = T.gates.find((q) => !q.open && T.t <= q.t && t > q.t);
      if (g) { t = g.t; T.playing = false; }
      if (t >= total) { t = total; T.playing = false; }
      T.t = t; sync(); return true;
    };
    sync();
    x.T = T;
    return T;
  }
  return { mount, timeline, el, clamp, lerp, ease, part };
})();
