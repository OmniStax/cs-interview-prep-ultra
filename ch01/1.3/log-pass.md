## Pass: section 1.3 Asymptotic notation (2026-11-09)

Built from the agreed plan (`ch01/1.3/plan.md`, `ch01/plans-summary.md`, METHOD decisions 1–21), on 1.1's pipeline.

**What was fetched.** OpenDSA's code fragments (plan question 12): a sparse checkout of OpenDSA at the registered
pin 40bf936 gave `SourceCode/Java/Misc/Anal.java`, `SourceCode/C++/Misc/Anal.cpp` and `MIT-license.txt` (Misc/Anal
exists in no other language at that commit), cached in `sources/_cache/opendsa-code/` with a `FETCHED.txt`, like
`opendsa` itself, and registered as a new row `opendsa-code` (appended; MIT, the notice quoted). The OpenDSA
slideshow LowerBoundCON was read to see what it held (lower bound against best case for sequential search; not
cached, not registered). ODS's Figure 1.5 was rendered from ODS's own `bigoh-1.gp` and `bigoh-2.gp` by
`ch01/1.3/render_originals.py` (gnuplot's tikz terminal, ODS's colour file, pdflatex) into
`media/ch01/ods-bigoh-1.png` and `-2.png`; gnuplot-nox and texlive-pictures were installed in the container for it.

**How the text was made.** No source passage was typed. A new shared reader, `tools/extract_opendsa.py`, reads
OpenDSA's reStructuredText (section levels by underline order, paragraphs, indented definitions as quotations,
`math`, `topic` boxes, auto-numbered footnotes, `:math:`, `:term:`, `:ref:`, Sphinx's smart quotes) and the
`ODSATag` regions of its code. `tools/build_text.py` gained an `opendsa` block kind (`opendsa_block`: slice by
heading, codeinclude → a four-language code set with the source's Java and C++ and the spec's AI Python and
JavaScript, inlineav → the spec's figure, avembed dropped, footnotes to `footnotes.json`) and, for ODS, what this
block uses: itemize lists, `align*` as an aligned display, `\javaimport`/`\cppimport` dropped as the pseudocode
edition drops them (the paragraph breaks where the code stood, so `sim-loop-count` stands there), any other
`#code#` in maths with `=` as `\gets` and `++` as one operator (the edition's `translate_code`), `\log#n#` spaced,
`\mbox` as `\text` (KaTeX has no `\mbox`), and `tex_plain` spacing `\log` after a letter in plain captions. Every
change is backward-compatible: 1.1's build, run from a frozen copy of its spec before and after each change, gives
byte-identical `source.md`, `text.html`, `footnotes.json` and `captions.json`. The section's `build_spec.py` holds
placement, marks and the Python/JavaScript translations; its FIXES table is empty. `inline_code.py` writes ODS's
`Simple.snippet()` (Java and C++, from the cache) into `figures.js` between generated markers.

**What was built.** Three blocks (ODS Asymptotic Notation; OpenDSA Lower Bounds and Θ Notation with its three
subsections as `<h3>`; OpenDSA Multiple Parameters), the Collatz and c3p16 fragments as code sets (Java and C++
the source's, Python and JavaScript AI-marked), OpenDSA's footnote on the alternate Ω definition as a book note,
errata 1, 2 and 10 as correction notes, the NP-Complete `:ref:` linked to 23.2. Three concepts (`big-o`,
`big-omega-theta`, `multivariate-big-o`; the first two typed `cost`), three forms and three edges (big-o →
logarithms, big-omega-theta → big-o, multivariate-big-o → big-omega-theta) through `ost`. Four Sims:
`sim-big-o-witness` (c and n₀, the failing stretch shaded in `PAL.bad`, the least n₀ as a special),
`sim-loop-count` (debugger: Python canonical, ODS's Java and C++ verbatim, the five counts against 4n + 2),
`sim-crossover` (one zoom over ODS's two plots, its originals behind the toggle, f₁ and f₂ as referents) and
`sim-limit-test` (three pairs, the ratio on a log axis). One derivation, `drv-big-o-example`, replacing ODS's
chain. Referents `i`, `f1`, `f2`, marked in the prose maths with `\htmlData{ref=…}`.

**Checks.** `ost check --section 1.3`: ok. `npm run check:content` (content root `/home/user/OmniStax/omnistax-content`):
no errors, no warning for 1.3. `npm run check:code`: no errors (1.3 has no code card). Every display and inline
formula of `text.html` and the footnote rendered by KaTeX without error. Playwright on port 4403, light and dark at
2×, every figure at its opening state and slider extremes, the debugger stepped (step, into, end, n = 1 and 16,
each language), the derivation stepped, the choice morph caught mid-way: no console errors on the final pass.

**Deviations from the plan.** `sim-loop-count` plots no count-against-n graph (the counts table against 4n + 2
carries it; a log–log plot of n ≤ 16 says little); its Python is a `while` loop so that the C-style loop's test and
increment stay statements. `sim-limit-test` uses a dropdown (three long options wrap as a row). The derivation
starts from the condition n ≥ 2 (node 1: log n ≥ 1, with log 2 = 1 from 1.2) rather than holding it as a fact.
Not built: `sim-pixel-counts` (an extra Sim, not picked), the two Aspnes cards (A.6.2, A.6.3: their mathematics is
in a PDF this pipeline cannot read yet; typing them would be a hand transcription) and the four MIT NC cards (the
app does not read `exercises-nc.json` yet); `exercise_notes` says so.

**For the chapter pass.** `complexity-analysis` (1.4) and `running-time-guarantees` should gain the edge to `big-o`
now that it exists; the plan's `sim-loop-count` "serves complexity-analysis" too. OpenDSA's LowerBoundCON was not
the limit test but lower bound against best case; a figure for that is open. The dev server cannot watch a book
whose `sources/_cache` is in the content root (inotify limit); the pass served a copy without the cache.
