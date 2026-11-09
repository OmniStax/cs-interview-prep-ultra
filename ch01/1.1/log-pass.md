## Pass 2: section 1.1, review fixes (2026-11-09)

Three faults from the user's review of pass 1, fixed and checked again.

**Captions (root RULES item 17).** Every 1.1 caption and headline was read again for words about the figure
or its controls. Four sentences changed, in `text.html` and in `build_spec.py` alike:
`sim-compass` "Drag the two lengths: the triangles ACE and AZF stay similar … and the count of primitives
never changes" now reads "Whatever the two lengths, the triangles ACE and AZF are similar, which is why it
works, and the construction takes the same number of primitives"; `sim-apportion` "The queue is drawn as one
sorted column" is now "The queue is one sorted column"; `sim-scan-cost` "Push either count to the billions …
let each operation inspect about two items" is now "With either count in the billions the time runs to years;
when each operation inspects only about two items, it drops below a second"; `sim-lattice` "each step adds"
is now "each column adds". The headlines (toplines) and the debugger block labels speak of the subject
already and are unchanged.

**Empty space.** `sim-compass` is drawn turned a quarter clockwise from Figure 0.4, so that the line AC, along
which Z travels to |AC| · |AD| = 5, runs across the wide canvas and α down it (the construction is the same;
the "E and F" choice now reads below A | above A). Its scale is fitted once (`F.fitScale`) to the extents of
every point any slider setting reaches, one scale for both sides, each side centred on its own extents;
lines run to the box's edge and circles are clipped to it. The drawing is about 1.6 times its earlier size and
fills the canvas. `sim-apportion` drops from 1000 to 760 logical units: the bars run the full height on the
left from a baseline near the foot, the queue's head stands under the headline on the right, four-state
rows are larger, and the House shows as many queue rows as the bars' height holds, with "… n more" (which
never showed before: the trace kept only 12 entries; it now keeps the whole queue).

**Debugger panel (app).** `.dbg-row>.cp` had `flex-grow: 0`, so when the row wrapped the panel kept its
content width (the widest language's lines, set as the `<pre>`'s min-width) and left a blank strip to its
right. Now both grow, the drawing 1000 times more: side by side the drawing takes the spare width; stacked,
the panel fills its line. OmniStax branch claude/confident-cannon-bl42ph, commit 1ef68db (not pushed);
`tests/code-browser-check.cjs` now measures the row at 1400px and 640px in both themes, and passes.

**Checks.** `ost check`: no errors, the one warning by design (pass 1). `npm run check:content`: no
errors, same warning. `npm run check:code`: the Python reference passes. Playwright at 2× in light and dark,
every figure stepped, the House run to its end and the compass on both sides: no console errors.
Screenshots in the session scratchpad, `sec11-v2/`.
