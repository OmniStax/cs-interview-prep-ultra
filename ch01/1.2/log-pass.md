## Pass: section 1.2 Logarithms, factorials and harmonic numbers (2026-11-09)

Built from the agreed plan (`ch01/1.2/plan.md`, `ch01/plans-summary.md`, METHOD decisions 1–21) with 1.1's pipeline.

**How the text was made.** No source passage was typed. Three ODS blocks (`intro.tex` 409–471 and 474–515, `rbs.tex` 76–110),
pseudocode edition, through `tools/build_text.py`. The section's `build_spec.py` holds placement, marks, one cross-reference
(`\figref{harmonic-integral}` → "Figure 7.2", linked to `sim-harmonic`), one display swap (the printed change-of-base chain
→ `drv-change-of-base`) and an empty replacement table (nothing needed correcting). The harmonic block keeps its random-BST
opening (question 3), bridged by B-new-b in the lead.

**Shared tools, changed backward-compatibly** (1.1 rebuilt into a scratch copy: `source.md`, `text.html`, `footnotes.json`,
`captions.json` byte-identical): `build_text.py` gains `ods_macros` (a `\newcommand` the passage defines, ODS's `\hint`,
expanded), `ods_figures` (a figure environment dropped from the prose, its caption kept by `\figlabel` in `captions.json`,
HTML and plain text), `tex_plain` (simple inline maths as Unicode for a caption attribute), a spec `DISPLAY_AS` (a display a
derivation replaces) and `{{caption-text <label>}}` keys beyond numbers; `build_section.py` takes the same wider key.

**Media.** ODS's `figs/harmonic.ipe` views 2 and 3 rendered with `iperender -png -resolution 300` (Ipe 7.2.28 from apt,
with texlive-fonts-extra for kpfonts and ODS's `ods-colors.sty`) to `media/ch01/ods-harmonic-2.png` and `-3.png`, the two
originals behind `sim-harmonic`'s toggle.

**What was built.** Three concepts (`logarithms`, `factorials-stirling`, `harmonic-numbers`) and two edges through `ost`,
eight forms; three still Sims (`sim-halving`, `sim-stirling`, `sim-harmonic`), no code panel (properties, config item 16);
two derivations (`drv-change-of-base`, replacing the printed chain; `drv-harmonic-bounds`, after the paragraph, three nodes:
lower, upper, joined), every line checked numerically by `check_derivations()` in the spec; errata 3 and 4 as correction
notes; three code exercises (Exercism grains, canonical tests; Kattis howmanydigits and stirlingsapproximation, sample
visible, AI tests checked against exact factorials and Decimal arithmetic, AI references).

**Deviations from the plan.** `sim-halving` draws values on a log scale with axes that fit the bars (the plan's linear
staircase is unreadable past k ≈ 1000) and its slider runs on log₁₀ k; `sim-stirling` plots 1/α(n) − 12n, which the bounds
put in (0, 1), since α between its bounds on a log scale cannot separate them (0.14 % apart at n = 60); readouts use `tex`
(KaTeX) as 1.1 does. Erratum 3's marker stands after "For a non-negative integer, k," (after the display it stood on a line
of its own). Aspnes A.5.2 waits for a transcription of its displayed products (no LaTeX source; the PDF text loses them);
the MIT 6.042J NC card waits for the app to read `exercises-nc.json`. Both named in `exercise_notes`.

**Checks.** `ost check --section 1.2`: ok. `check:content`: no errors (two warnings, 1.1 and 1.4). `check:code`: every
Python reference passes. Playwright, light and dark at 2×: every figure at its slider and choice extremes, both derivations
scrubbed through, the original toggle: no console errors.

**For the other sections.** Run a dev server with its own Vite cache (`OMNISTAX_CACHE_DIR=<scratch>`): with the shared
`node_modules/.vite`, servers on other ports re-optimise the deps under each other, and MathJax (readout morphs, derivations)
then throws "Cannot read properties of undefined (reading 'apply')" after "Invalid option macros".
