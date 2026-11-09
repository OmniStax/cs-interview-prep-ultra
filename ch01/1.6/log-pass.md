## Pass: section 1.6 Counting and expected value (2026-11-09)

Built from the agreed plan (`ch01/1.6/plan.md`, `ch01/plans-summary.md`, METHOD decisions 1–21), on 1.1's pipeline.

**How the text was made.** No source passage was typed. Three readers, all new and called from `tools/build_text.py`
through one hook (a block whose spec row names a `reader`; `tools/build_blocks.py` assembles it):

- `tools/read_latex.py` reads a LaTeX passage (Brisk Walk, and ODS where a passage holds display maths, cases,
  a lemma and a proof): sections, paragraphs, `\[ \]`, `align`, `framed`, centred lines, tabulars, numbered lists with
  `[resume]`, figures (caption and label kept), footnotes, and references resolved over the whole chapter file
  (`Rule~\ref{nonegs}` is "Rule 2", `Figure~\ref{venn}` is "Figure 4.1"). Dialects: `brisk` (a straight `"` closes a
  quotation) and `ods` (the pseudocode-edition rule for `#code#`, `\E`).
- `tools/extract_mcs.py` reads MCS 2018 from its PDF glyph by glyph. The MathTime Pro 2 fonts have no Unicode map and
  no /Differences, so pdftotext prints "=" as "D", "{" as "f", "[" as "Œ"; the script decodes each math glyph by font
  and code from a table read off the page renders, sets math runs as inline TeX, and returns displays by key for the
  spec to set (the PDF draws underbraces and fractions in pieces).
- `ch01/1.6/render_originals.py` typesets Brisk Walk's two TikZ figures (Venn diagram, Pascal's triangle) from the
  cached .tex for the Sims' original toggle (`media/ch01/brisk-4-1-venn.png`, `brisk-6-1-pascal.png`).

`build_spec.py` holds placement, marks, nine MCS displays, three derivations, the exercises and the section record;
its FIXES table is empty. `build_nc.py` writes `exercises-nc.json`. Shared tools changed only additively:
`build_text.py` gained the reader hook and skips ODS blocks without `lines` when reading ODS figure captions; 1.1,
1.2 and 1.4 rebuilt in a scratch copy give byte-identical text.html, source.md, footnotes.json and captions.json.

**What was fetched.** The Exercism Python track (MIT, `exercism/python` at 479f11b) for pascals-triangle: its
`example.py` passes the 8 canonical cases and the track's 10 tests, run in a fresh scratch directory with
`python3 -I` (decision 17). baffling-birthdays is not on the Python track, so both its references are the AI's.
Registered as `exercism-python` in `sources/registry.json` (appended).

**What was built.** Eight blocks: brisk counting (Fundamental Theorem with "A simple trick", Permutations,
Partial permutations, Combinations, Binomial coefficients; "Enumerating permutations" left out), brisk outcomes and
probability measures, brisk's Philosophical interlude whole, brisk conditional probability with Independence and
"Whoops!", MCS 19.1–19.1.2 (Definition 19.1.1 as a note), ODS Randomization and Probability to the end of linearity,
ODS's indicator passage, ODS's coin-tosses lemma and proof. Two brisk footnotes as book notes; four corrections
(errata 11, 12, a new P/R one, and the costume item's 300). Seven concepts and seven edges through `ost`. Three
Sims (`sim-pascal`, `sim-idol-venn`, `sim-coin-tosses`), three derivations (`drv-heads-sum`, `drv-heads`,
`drv-coin-tosses`, erratum 5 as the last one's node note). Exercises: 12 brisk written cards, 2 Exercism code
cards; 9 NC cards in `exercises-nc.json`.

**Checks.** `ost check --section 1.6`: ok. `npm run check:content`: no errors (2 warnings, both 1.1/1.4's).
`npm run check:code`: no errors; the two JavaScript references pass their tests under node (8/8, 4/4). Playwright on
port 4406 (dev server with polling: the machine's file watchers are spent), light and dark at 2×: no console errors,
no KaTeX errors, every Sim with a canvas, a transport only on `sim-coin-tosses`; screenshots in
`scratchpad/sec16/`.

**Deviations from the plan.** ODS's two printed chains are two derivations, each where its `align` stood, not one
graph with two lines (one host cannot replace two displays and keep ODS's words between them in order). Brisk's
references to pages this book does not carry print as "[*Brisk Walk* §2.9]" and "[*Brisk Walk* §4.5]". Wikibooks,
Aspnes and Kattis items not built (see `exercise_notes`); NC cards only where pdftotext keeps the statement whole,
keyed by a link to MIT's solution. `sim-coin-tosses` is a story slider over runs (stops 1, 100, 200, 500, 1000);
with reduced motion it opens on 200 runs.
