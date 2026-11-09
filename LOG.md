# Log: Data Structures, Algorithms and System Design

The running log of passes over this book (root RULES, "Where things live"). The full-book pass and the
chapter 1 plans are recorded in METHOD.md (§4.4, decisions 1–21), RULES.md and the chapter files; this
log starts with the first built section.

## Pass 1: section 1.1 What an algorithm is, the first template (2026-11-09)

Built from the agreed plan (`ch01/1.1/plan.md`, `ch01/plans-summary.md`, METHOD decisions 1–21).

**How the text was made.** No source passage was typed. `tools/extract_jeffe.py` reads Erickson's
chapter PDF with pdfminer glyph by glyph and decodes each glyph by the name its font's /Differences gives
it (`one.oldstyle`, `b.sc`, `minus`, `a12`), which recovers every digit, minus sign and small-caps letter
that `pdftotext` and the cached `.txt` lose; spacing accents are folded into their letters (Muḥammad,
al-Khwārizmī), a mirrored glyph is read as its mirror (☜). `tools/build_text.py` lays the lines out
(headings by font, footnotes under the footnote rule, pseudocode in its frame, a frame with a caption
under it a figure, quotes, lists, displays), joins words broken at line ends, slices the blocks by
anchor text and writes `source.md` and `text.html`; it reads ODS's LaTeX with a small converter
(pseudocode-edition rule for `#code#`: a capitalised name plain, anything else maths). The section's
`build_spec.py` holds only placement, marks, the four display formulas (the PDF draws them in pieces)
and a 14-entry replacement table, each entry with its reason. `tools/build_section.py` writes
`section.json` once (later corrections go through `ost set`); `tools/crop_jeffe.py` cuts figures from
page renders; `tools/inline_census.py` writes the census rows into `figures.js`.

**What was fetched.** Erickson's back matter (Image Credits, p. 23 of `99-backmatter.pdf`): Figure 0.1
Biblioteca nazionale Braidense, Figure 0.2 Internet Archive, both public domain. The 2020 census: the
proxy refuses census.gov, so `apportionment.csv` was read through the USAFacts .gov fetch; it carries
resident populations, not the apportionment populations (Table 1 is xlsx/pdf only). Huntington–Hill on
the resident populations with R = 435 gives every state exactly its 2020 seats, which the figure checks.
Both registered in `sources/registry.json` (`census-2020` new; `jeffe` pin and credits).

**What was built.** Ten blocks (eight Erickson, two ODS) with per-block `data-source`/`data-locator`;
21 Erickson footnotes and one ODS footnote as book notes; erratum 6 as a correction note; eight concepts
and five edges through `ost` (`tools/mergebook.py` and `merge-state.json` adopted from College Physics
2e, since `ost` needs them); five Sims (four debugger figures with Python, Java, C++ and JavaScript, all
AI translations, and one still), two photographs; one code exercise (Exercism difference-of-squares,
canonical tests, AI references); every OpenDSA check item named in `exercise_notes`, waiting for the
converter.

**Code and pseudocode (decision 20).** Erickson prints pseudocode, which is none of the four languages,
so every variant is an AI translation and carries the mark. His pseudocode stays visible as his words:
the listings he prints in the running text (BottlesOfBeer, FibonacciMultiply, Martin's procedure) stay
as `<pre>` where he prints them, BottlesOfBeer followed by a four-language code set, FibonacciMultiply by
`sim-lattice` whose panel is its translation, Martin's alone (it is not a program); the listings he
prints inside Figures 0.3–0.5 are the Sims' originals behind the toggle. The checker's one warning
(a code set whose variants are all AI) is this, by design.

**App changes** (OmniStax, branch claude/confident-cannon-bl42ph, commit cbdbf2e, tested, not pushed):
`findBooks` follows a book linked into the content root (the symlink was not followed, so the build and
`ost` found no book); a photograph with no number carries no eyebrow (the checker made it an error,
though the stylesheet already provided for it, and this book numbers no figure).

**Checks.** `ost check`: no errors, 1 warning (above). `npm run check:content` with
`OMNISTAX_CONTENT_DIR=/home/user/OmniStax/omnistax-content` (the symlink, followed after the fix): no
errors, the same warning. `npm run check:code`: the Python reference passes. Playwright over the page in
light and dark at 2× with every debugger figure stepped: no console errors.

**Deviations from the plan.** See the pass report; in short: the census data is resident population;
`sim-apportion` opens on four states (R = 12) and offers the House, since 437 stops make the House poor
to step through; no editable inputs and no predict pauses (the library has neither yet); the lead is two
sentences, not four; the difference-of-squares card ships now that the `code` answer type exists;
`sim-compass`'s RightAngle locals are lower-case so that only C, D and Z wear colour (decision 21).

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

## Pass 3: section 1.2 Logarithms, factorials and harmonic numbers (2026-11-09)

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

## Pass 4: section 1.3 Asymptotic notation (2026-11-09)

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

## Pass 5: section 1.4 Analysing running time and space (2026-11-09)

Built from the agreed plan (`ch01/1.4/plan.md`, `ch01/plans-summary.md`, METHOD decisions 1–21), with 1.1 as
the template: same pipeline, same conventions.

**How the text was made.** No source passage was typed. `tools/extract_jeffe.py` read Erickson pp. 15–17
glyph by glyph; `tools/build_text.py` laid out the blocks from `build_spec.py`, which holds placement, marks,
one display (the peasant recurrence's cases, drawn in pieces), two lines dropped (the ∑ signs, drawn on
baselines of their own) and a replacement table of 19 entries, each with its reason: the two inline sums set
as LaTeX, Θ set upright, three small-caps names broken at a line end or at their first capital, the italic
correction read as a space, operator spacing, and the struck-through “running” (a rule too short for the
extractor to keep), set as `<s>`.

**Shared tool changed, backward-compatibly.** `tools/build_text.py`'s ODS reader gained what the two ODS
blocks need: the edition macros (`\javaonly`, `\cpponly`, `\notpcode` dropped and `\pcodeonly` kept, the
pseudocode edition of decision 20), `\paragraph` opening its own paragraph, `description` lists as `<ul>`
with bold labels, `\[ … \]` displays (a dollar sign in one set as `\text{\textdollar}`), `\$` as `&#36;`,
`\,` as a narrow no-break space outside maths, and operator `#code#` (`#+#`, `#%#` …) as the pseudocode
edition sets it. Rebuilding 1.1's spec with the old and the new tool gives byte-identical `source.md`,
`text.html`, `footnotes.json` and `captions.json`.

**What was built.** Three blocks (ODS, Erickson, ODS) with `data-source`/`data-locator`; Erickson's
footnotes 22 and 23 as book notes; errata 7, 8 and 9 as correction notes; three concepts (`word-ram`,
`complexity-analysis`, `running-time-guarantees`, the last typed `cost`) and four edges through `ost`
(`word-ram` → `logarithms`, `complexity-analysis` → `describing-algorithms` and `big-o`,
`running-time-guarantees` → `big-o`, the last two once 1.3 had staged `big-o`), and a later coverage row
(`running-time` uses `big-o`) through `ost add`; one debugger Sim,
`sim-song-count`, after Erickson's NDaysOfChristmas listing, and a four-language code set after Alouette.
Links agreed in plan question 23: “the next chapter” → 10.2, “a binary heap or a heap-ordered array” → 9.2,
ODS's `\secref{randomization}` → 1.6 `#linearity`, written as 1.1 wrote its forward links.

**The figure.** One code panel holds `n_days_of_christmas` and `bottles_of_beer` (the panel cannot swap its
source, so the song choice steps whichever function it names, as `sim-compass` holds two functions). Default
level: one stop per day (13 at n = 12); step into gives the opening line, each gift and the partridge. The
triangle of squares is the invariant (days sung filled, the rest hollow); the counter reads the gift names
and gifts against n(n + 1)/2 and n(n + 1)(n + 2)/6, or “beer” against 3n + 3; the log–log graph beside it
draws all three counts for n = 1..12, the run's live count climbing at x = n. Text 26–34 logical.

**Checks.** `ost check --section 1.4`: no errors, one warning (the Alouette code set has only AI variants,
the same by-design warning as 1.1). `npm run check:content`: no errors, the two by-design warnings.
`npm run check:code`: passes. Playwright on 4404, light and dark at 2×, every stop kind shot (see the
report); no console errors.

**Deviations from the plan.** Alouette gets a four-language code set (decision 20 offers every listing in
four languages, and 1.1 gave BottlesOfBeer one); NDaysOfChristmas stays as `<pre>` with the Sim after it,
as FibonacciMultiply in 1.1 (the panel is a translation). ODS's last model-of-computation paragraph is left
out: in the pseudocode edition it is one sentence cut off mid-way. The Erickson exercises are numbered as the
page prints them (1, 2, 3); the plan and config number them one higher. No References item: the schema has
no field for it yet (1.1 has none either).

## Pass 6: section 1.5 Amortized analysis, the first translated section (2026-11-09)

Built from the agreed plan (`ch01/1.5/plan.md`, `ch01/plans-summary.md`, METHOD decisions 1–21), copying 1.1's conventions.

**How the text was made.** No Chinese was typed. `tools/build_translation.py` (new; no shared tool was changed) cuts
OI Wiki's page (`basic/amortized-analysis.md` at c794414) into the plan's five blocks by heading and writes them to
`source.md` verbatim. The English is `translation.md`, written block by block under `docs/prompts/translate.md`: a
paragraph for a paragraph, a list item for a list item, a display for a display, the sentences in OI Wiki's order.
The tool checks the two halves element for element and the maths of each element character for character, and refuses
to build on any difference; then it writes `text.html` with the plan's headings, the figure and the two derivations, the
concept spans and the erratum marker, and OI Wiki's four reference footnotes to `footnotes.json` in their own words.
`build_spec.py` holds only placement and markup; `tools/build_section.py` wrote `section.json` once (the derivations and
the exercise notes were corrected after with `ost set` and `ost field`).

**Terms** (`glossary.en.json`, every row pending for the chapter pass): amortized analysis, amortized cost, aggregate
analysis / the aggregate method, the accounting method, the potential method, potential function, potential, actual cost,
credit (费用), resize (扩容), capacity, growable array, dynamic array, state / reachable state, push / pop / top of the
stack. OI Wiki prints its own English glosses for the four method names, which decided them; Wikipedia's articles at the
cached revisions back the rest. NIST's DADS could not be reached (rows marked `confirm`). One forced scenario: OI Wiki's
parenthesised English glosses are not repeated after the English terms.

**What was built.** Five blocks, all OI Wiki in translation, each `<section>` carrying `data-source`, `data-locator` and
`data-ai="claude-opus-5-5 high"` (the translation's AI mark, as 1.1's translated code variants carry it). Three concepts
and three edges through `ost`. Erratum 14 as one correction note, which also names m's third use (the number of
operations in the potential method's principle). Lead with B-new-a (78 words, three sentences). One debugger Sim,
`sim-pay-for-doubling`, where OI Wiki's code-fenced credit trace stood: a four-language code panel (all AI, OI Wiki
prints no array code), 9 or 17 inserts from capacity 1, the method a choice (aggregate: bars and the running total under
3n; accounting: coins on the cells and the bank, never below 0; potential: Φ = 2n − m from Φ(h₀) = −1, ĉ = 3), stepped
by insert, by block and copy by copy. Two derivations: `drv-potential-sum` (replacing the principle's three displays and
the words between) and `drv-doubling-potential` (two results, replacing the list's equation lines and its two
"Amortized cost" items). One NC card in `exercises-nc.json` (6.046J S12 6-1, statement and key read by script from the
solution handout, displays set from the page render).

**Checks.** `ost check`: ok. `npm run check:content`: no errors; the two warnings are 1.1's and 1.4's by-design
all-AI code sets. `npm run check:code`: no errors. Playwright on a static build (port 4405) in light and dark at 2×:
no console errors; the sim stepped by insert, into a resize copy by copy, at all three methods, at 17 inserts, and
mid-move; both derivations played through.

**Deviations.** The Sim has a code panel (the plan line said none; decision 8's default and decision 20's four languages,
all AI). Referents n, m and i (the plan said none) because the panel's code variables are drawn (COLOR.md, decision 19).
6.046J F05 6-1 (billboard) is not carded: its handout's formulas are Type 3 glyphs that cannot be read by script. No
symbol or variables rows (as 1.1); the maths is ink.

**App gaps.** No block-level translation mark: `data-ai` on a `<section>` renders nothing yet. No per-block attribution
("translated from the Chinese and adapted"): the SATA thanks sit in `notes`. `exercises-nc.json` is not read. The code
panel colours a referent's bare token but not `self.n` in Python.

## Pass 7: section 1.6 Counting and expected value (2026-11-09)

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

## Pass 8: chapter 1 pass (2026-11-09)

Plan phase 3 over 1.1–1.6, from the items the section builders handed on. Model: claude-opus-5-5, high effort.

**Log.** The six `log-pass.md` files are passes 2–7 above, in section order, under this file's own heading
convention (`ost log` numbers `### Pass` headings and would have started again at 1); the files are removed, as
`ost log` removes a merged one.

**Concepts.** `complexity-analysis → big-o` and `running-time-guarantees → big-o` were already in `book.json`
(staged by 1.4) and in the map. The concept map now agrees with `book.json`: `tools/map/map.spec` carries every
chapter 1 concept's built name and statement (`name=`, `stmt=`) and a new `EDGE multivariate-big-o → big-omega-theta`
(the build Hasse-reduces the map's old edge to `big-o`); `build.py`, `report.py` and `check_map.py` run clean
(1022 concepts, 1330 edges, 0 errors). Every chapter 1 concept has exactly one introducing span; the edges are
Hasse-reduced and acyclic (checked by script over `concept_prereqs`).

**Errata.** New correction `err-or` in 1.4 (Erickson's "data structure of subroutine"); 1.4's `err-census`
reworded to Erickson's 0.3 words (a sorted array in a single Excel column, recalculated at every iteration) with
a link back to 1.1's block, and its bound written Ω(Rn). `judgements/ch01-03-reconciled.md`: erratum 8 worded the
same way, erratum 11 corrected (brisk's 52! is right in its first thirteen digits, as 1.6's note says), and
errata 32–34 added (`err-or`, brisk's P/R, the costume item's 300). 1.1's `exercise_notes` now use Erickson's printed
exercise numbers (0 and 4); `config.md` notes that its own numbers run one higher.

**Cross-section consistency.** Every lead names its tier and its indexing (or notation, where a section has no
arrays) and carries its agreed bridges (B2 in 1.4, B3 with MCS's notation in 1.6, B-new-a in 1.5, B-new-b in 1.2,
B5 as links in 1.1). The m/n notation agrees: 1.5's lead and erratum 14 name m's three uses, 1.4's ODS block uses m
for a number of operations, and B6 (2.2) will bridge to ODS's `a.length`. 1.2's lead now names "Section 8.6" as the
other leads and notes do. `RULES.md` gains **Cross-references** (links to carried passages read "Section N.M" or
wrap the source's words; a passage the book does not carry prints as "[*Brisk Walk* §2.9]", adopted from 1.6) and
**Links to sections not yet built**, the one list of the seven forward links (2.2, 2.5, 3.1, 8.6, 9.2, 10.2, 23.2)
to check when their targets are built. Until then a click on one opens the app's "Not found" page. The `#linearity`
link from 1.4 lands on 1.6's block (checked headless: `1.6-linearity`, 36 px from the top).

**Glossary.** `ch01/1.5/glossary.en.json` is folded into the book's `glossary.en.json` (translate.md §6), every row
decided: 预存 is now "save" ("saved *n* units", "the saved credit"; Wikipedia's Amortized analysis: "a saved
'credit'"), replacing "prestore" in 1.5's translation; the headings Principle / Example / Extended example are
kept; "amortized analysis" and "amortized cost" are confirmed against the cached Wikipedia article. The forced
scenario is in `translation-notes.md` (new, book root) and in `ch01/config.md`.

**Terms.** `terms_pass.py` listed 544 unmarked mentions of concept words across the chapter; 533 are marked
`data-concept`, 11 left in ink as another sense (credits, a combination lock, "in any event", the potential energy
of the metaphor, choices independent of each other in counting). The decisions are kept per section as
`terms.jsonl`, applied by `tools/apply_terms.py` after `build_text.py` or `build_translation.py` writes the page, so a
rebuild keeps them; a spec change that moves the page makes the build say the rows must be listed again. 1.1's
peasant passage marks its four cost bounds `data-type="cost"`, as 1.4 marks Erickson's. Maths stays in ink in every
section: chapter 1 has no variables rows or `\k` macros (open).

**Colour.** The book's default colours were never stored; `npm run colours:default` now has written `colours`
(categories by the smart assignment, the referent walk order), and no referent group is dealt farthest apart.
sim-idol-venn's R and David were #443303 and #677806, a dark greyish yellow and an olive 32° apart, two families
by hue: the app now counts two referent colours whose tints (OKLab a–b) stand within 0.08 as one family, and the
smart walk steps back where a first fit strands a later referent (root RULES item 7; OmniStax commit b70690d).
R is now violet and David mauve.

**App** (OmniStax, branch claude/confident-cannon-bl42ph, not pushed): the Original toggle on an unnumbered Sim
keeps the eyebrow "Sim" (8dd7e2a, with a test); the dev server ignores `sources/_cache` and `__pycache__`
(a1e417f, with a test); the referent families (b70690d); `ost` accepts `copyright` and `notice` on exercise sources
and writes a section's `notes` (eeb6df2); the attribution branch merged (ce66d8f). With it: `exercise_sources`
exercism, icc and opendsa-exercises carry their copyright lines and licence notices, and 1.5's `notes` drop the
SATA thanks the footer now prints.

**NC cards.** 1.2's MIT 6.042J F05 ps6 #7 and 1.3's four MIT cards (6.006 S20 ps1 1-1, 6.046J F05 ps1 1-1, 6.006 F11
ps1 1-1, 6.042J F05 ps6 #8) are in `exercises-nc.json`, statements set from the handouts' page renders, keys linked
to MIT's solutions as 1.6's are (`tools/nc_cards.py`, each section's `build_nc.py`); both sections' notes say so.

**Not done.** 1.4's long Java and C++ lyric lines: the strings are Erickson's lyrics, which the translations keep
whole, so they were not shortened; the song-count panel scrolls 35–42 px at 1400 px wide, and a soft wrap in the
code panel is the better fix (an app item). Erickson's plain `<pre>` listings (1.1, 1.4) also overflow the text
column by up to 69 px at that width.

**Checks.** `ost check`: no errors, the two by-design warnings. `npm run check:content`: the same. `npm run
check:code`: 6 Python references, no errors. `check_map.py`: clean. `npm test`: 1124 pass, 3 fail, all needing
cloned books (hover, sheets, symbols); a fourth, data-original paths, failed on 1.2's and 1.3's "a.png, b.png"
and is fixed by writing the lists without spaces. Headless (dev server, own cache, port 4420): all six pages in
light and dark, every figure and the whole prose shot, no console errors, no failed requests, no KaTeX errors;
the footer and an NC card read in both themes. Screenshots in the session scratchpad, `ch01pass/`.

**Open.** The light theme's referent yellow (#443303) reads near ink on small marks (Fantasia's dot, `i` in
sim-lattice's code); sim-idol-venn's eight referents sit near the palette's limit (R and David 0.13 apart in the
dark theme). Symbols in maths are not typed (no variables rows). The OpenDSA, Aspnes and Kattis items still wait as
the sections' notes say. The owner's review of the translation (translate.md §10).

## Pass 9: section 2.1 Arrays and the list interface (2026-11-09)

Planned and built in one run (`briefs/section-build.md`), from `ch02/2.1/plan.md`, with chapter 1's pipeline. Model: claude-opus-5-5, high effort.

**How the text was made.** No source passage was typed. No shared tool read wikitext, so the section brings `readers.py`:
a wikitext reader for its two Wikipedia passages (headings, paragraphs joined over single newlines as MediaWiki renders them,
`;` and `*` lists, `:` lines, wikitables, `<syntaxhighlight>`, image lines, links kept as text, `nowrap`, `mono`, `ISBN`,
and `<ref>` citations set from their templates' fields as book footnotes), and the ODS block through `tools/read_latex.py`
with one step first (`eqnarray*` read as an aligned display). Wikipedia's citation numbers were computed over each whole
article and checked against the rendered revisions (Array 1–5 and 8; Pointer 12 and 13); a named citation used twice is a
second note with the same number, so every note has one marker. `tools/build_text.py` gained one backward-compatible branch:
a block whose `reader` is a function is read by it. 1.1 rebuilt from a frozen copy of the tools, before and after: `source.md`,
`text.html`, `footnotes.json`, `captions.json` byte-identical. `build_spec.py` holds placement, marks, three correction notes,
one display (the k-dimensional formula, which the article sets on an indented line) and an empty replacement table.

**What was fetched.** Wikimedia Commons refuses scripts the original files (429), so the three diagrams came from its
thumbnail service at 960 px: `media/ch02/wp-1d-array-diagram.png`, `wp-2d-array-diagram.png` (CC BY 4.0, Tropwine, credited
in the Sims' original captions) and `wp-array-of-array-storage.png` (public domain, credited in the photograph's caption).
ODS's `figs/list.ipe`, converted as the pseudocode edition's `figs-python/snarf-fig.py` converts it, rendered with
`iperender` to `media/ch02/ods-1-4-list.png`. Wikipedia's "C29 (C standard revision)" (revision 1382563440) for the C29
check; open-std.org and the Wayback Machine are refused by the proxy. Nothing appended to `sources/registry.json`.

**What was built.** Six blocks (Wikipedia Array: lead, addressing formulas with its two subsections, Efficiency, the
Iliffe paragraph; Wikipedia Pointer: C arrays; ODS: The List Interface), each with `data-source`/`data-locator`; ten
Wikipedia citations as book notes; errata 15 and 16 as correction notes and a new one in ODS Exercise 2.5's prompt
("{0, …, a.length}"). Three concepts (`array`, `pointer-arithmetic`, `list-interface`), two edges
(`pointer-arithmetic → array`; `list-interface → interface-vs-implementation`, new) and four forms (address = B + c·i in one,
two and k dimensions; a[i] ≡ *(a + i)) through `ost`. Three Sims, no code panel (properties): `sim-address` (still: i, c,
first index 0 | 1 | 31, B moving off the array; erratum 15 visible), `sim-row-major` (still: int a[2][3] | A[3][4], the grid
and its row-major memory), `sim-list` (moving: the eight List and Deque operations on ODS Figure 1.4's values, one
displaced value per beat, values moved against n − i). One photograph (the Iliffe vector). The terms pass: 104 mentions,
94 marked, 10 left in ink (another sense: "lists and strings", "the term "array"", "array data type", associative and
abstract arrays, a language's implementation, a library's, bit array, combinations). Exercises: three Busbee true/false
cards, three code cards (ODS 2.5 rotate, AI tests that keon's three rotates and TheAlgorithms' pass when run isolated;
Exercism matrix, canonical tests; ODS 1.6's List part, AI tests from a seeded sequence answered by a Python list), each
starter holding the function its tests call; one NC card (MIT 6.006 S20 ps1 1-2) in `exercises-nc.json`.

**Checks.** `ost check --section 2.1`: ok. `npm run check:content` (this book): no errors, the two by-design warnings
(1.1, 1.4). `npm run check:code` (this book): 2.1's three Python references pass; the one error is 1.6's c2 reference
running past its time limit (not this section's; the machine was loaded by parallel builds). The JavaScript references
pass all their tests under node. Playwright on port 4501 (own Vite cache), light and dark at 2×: every figure at its
opening state, its choices and slider extremes, `sim-list` mid-move and at rest for each kind of operation, its original
toggle; no console errors, no failed images, no KaTeX errors. Screenshots in the session scratchpad, `sec02.1/`.

**Deviations from the plan.** None of substance: `sim-row-major`'s link from the grid is drawn under the grid; the C
listings are lone `<pre>` (plan question 2).

**For the chapter pass.** The wikitext reader belongs in `tools/` once 2.3 and 2.5 show what their passages need; whether
Wikipedia's citations are book notes should be one decision for the chapter. ODS camel case: the edition writes add_first,
`read_latex.py` keeps addFirst (plan question 4). The `list-interface → interface-vs-implementation` edge goes into
`tools/map/map.spec`. 1.1's notes say ODS Exercise 6 is held for chapters 3, 5 and 8; its List part is now in 2.1. ODS
Exercise 2.5 comes from ODS's arrays chapter, which is 2.2's. The C29 sentence stands; a person should still read WG14
N3517. App: the article's `<table>` has no style (the byte table and 1.6's table render without rules or padding).


## Pass 10: section 2.2 Dynamic arrays (2026-11-09)

Planned and built in one run (`briefs/section-build.md`; `ch02/2.2/plan.md`, its Questions decided there), on chapter 1's pipeline. Model: claude-opus-5-5, high effort.

**How the text was made.** No source passage was typed. Five ODS blocks from `latex/arrays.tex`, pseudocode edition, read by `tools/read_latex.py` (dialect `ods`) through `tools/build_text.py`'s reader hook: the chapter opening (table, three points, the amortized paragraph), ArrayStack's opening and The Basics, Growing and Shrinking's first two paragraphs, the rest of that subsection under an OmniStax header ("Amortized cost of resizing": the lemma, its proof, the Summary theorem and the push/pop paragraph), and FastArrayStack. `build_spec.py` holds placement, marks, the JavaScript translations, two derivations and the section record; no FIXES table.

**Code (decision 20).** Every `\codeimport` is a four-language code set: Python, Java and C++ read by `tools/ods_listing.py` (2.6's reader) as ODS's editions print them, JavaScript the AI's translation of the Java, marked. FastArrayStack's set stands at its `\javaimport` (the pseudocode edition prints none; the Java and C++ editions do, and the prose names them). The JavaScript of every set was run against a plain array (300 runs of 300 random calls each, ArrayStack and FastArrayStack).

**Shared tools, changed backward-compatibly** (1.1, 1.2, 1.3, 1.4 and 1.6 rebuilt in a scratch copy with the old and the new tools: `source.md`, `text.html`, `footnotes.json`, `captions.json` byte-identical):
- `read_latex.py`: in dialect `ods`, the edition macros (`\pcodeonly` kept, `\javaonly`, `\cpponly`, `\notpcode` dropped, a dropped macro on its own line taking the line with it), `\newlength`/`\setlength`/`\addtolength` dropped, a `#code#` run that is not one word set as the edition's `translate_code` sets it (calls upright, `a.length` as length(a), `=` as `\gets`, a0 as a₀; `std::copy` kept, where the edition's script prints "stdcopy"), a one-word keyword in bold and a longer name in `\mathit`; `\codeimport`/`\javaimport`/`\cppimport` as a `code` element for a new `code_hook`; a figure's `\figlabel` and a `\caption[…]{…}` with its optional argument.
- `build_blocks.py`: the spec's `CODE_HOOK` (none: the listing is dropped).
- `ods_listing.py` (2.6's): `printed=True` applies what ODS's extractors hide (Java's `f.` and `Math.`, C++'s class prefix, Python's raising lines); the default output is unchanged (checked on 2.6's members); a C++ definition whose brace opens on the next line (FastArrayStack's `remove`) is no longer cut after its signature.

**Media.** ODS's `figs/arraystack.ipe` rendered with `iperender -png -resolution 300` to `media/ch02/ods-arraystack.png`, the original behind `sim-arraystack`.

**What was built.** Five concepts (`dynamic-array`, `array-resize`, `dynamic-array-cost` typed `cost`, `block-copy` Advanced, `implement-vector`, its span the first ArrayStack code set) and nine edges through `ost` (Hasse-reduced, checked by script); the lead with B6 and B8 (78 words); one debugger Sim, `sim-arraystack`, opening on Figure 2.1's calls (b r e d → b r i e), with four more inputs (append, add at the front, grow then shrink, at the boundary): one stop per call and per resize, copy by copy one level in; a[0..n−1] shaded, length(a) and n bracketed, the lemma's Σnᵢ ≤ 2m + 2r and each resize's "calls since the last ≥ nᵢ/2 − 1" live. Its trace agrees with ODS's own Python ArrayStack and FastArrayStack on all five inputs (run under the AI port: `numpy.object` → `object` in a scratch copy of `utils.py`, `python3 -I`). Two derivations replacing the proof's printed displays (`drv-arraystack-sum`, `drv-shrink-case`), every line checked by `check_derivations()`. Erratum 19 as a correction note. ODS's proof footnote as a book note. 44 concept mentions judged in `terms.jsonl` (two left in ink: "potential call", the STL "algorithm").

**Checks.** `ost check --section 2.2`: ok. `npm run check:content`: no errors; the book's two warnings are 1.1's and 1.4's by-design all-AI code sets. `npm run check:code`: no errors. Playwright on port 4502 (own Vite cache), light and dark at 2×: no console errors, no KaTeX errors; the Sim stepped call by call, into a resize copy by copy, mid-move, every input at its end, every language; both derivations played.

**Deviations from the plan.** None of substance; the caption's boundary sentence says the array resizes once and then keeps its length.

**For the chapter pass.** RULES' forward-link row "1.1 interfaces → 2.2" can be struck (the arrays chapter's passage is here). 2.6's listings could take `ods_listing(..., printed=True)` so the chapter's C++ reads as ODS prints it (no `DLList<T>::`). Chapter 3 (B18) links to `/cs-interview-prep-ultra/ch02/2.2/#arraystack-cost` for the lemma. The lead links to 2.1 by "Section 2.1". OpenDSA ALMCQinsarb, ALMCQdelarb and ALMCQsucc fit the book's model and ship with the converter.


## Pass 11: section 2.3 Two pointers and sliding windows (2026-11-09)

Planned and built from `ch02/2.3/plan.md` (`briefs/section-build.md`; its Questions decided there). A first agent wrote the plan, the translation, `wikitext.py`, `build.py`, most of `build_spec.py`, the five figures and the book rows, and stopped; a second finished the section. Model: claude-opus-5-5, high effort.

**How the text was made.** No source passage was typed. Three OI Wiki blocks (`misc/two-pointer`, c794414) are cut from the page by `build.py`, translated in `translation.md` and checked element by element by `tools/build_translation.py`'s parity check; the two 例题 boxes are slots the spec fills with links. Three Wikipedia blocks (3SUM, Merge algorithm, Moving average, at their cached revisions) are read from the wikitext by `wikitext.py` (section-local: paragraphs, emphasis, links as text, `{{mvar}}`, `{{math}}`, `<math>`, pseudocode as `<pre>`, refs as book footnotes). `build_spec.py` holds placement (`AT`), the derivation's place (`REPLACE`), one FIX (Merge sort §Variants in brackets), the concept and referent marks, maths referents (`\htmlData`), the lead, the five captions, the derivation, the section record and the exercises. `terms.jsonl` (46 rows judged, 23 marked) is applied by `tools/apply_terms.py` at the end of `build.py`.

**Lead and captions.** Written about the subject, then through `/humanizer:humanizer` and the repository's `humanizer` skill (root rule 17). The lead is 78 words: tier, the three indexings (OI Wiki from 1, the 3SUM pseudocode from 0, the moving average by time), 3SUM's sort as a library call (Chapter 10) and its hash table (Chapter 5), and windows that keep a sum, product or count, never a hash set (bridges B9 and B16).

**Derivation.** `drv-sma-next` replaces Wikipedia's four-line update display: facts are the previous mean over the last k points and the next window's range; the steps are Wikipedia's lines with the regrouping and the substitution of SMA_prev as two moves.

**Exercises.** c1 Exercism reverse-string (the track's example, the 7 cases the Python track runs, `bound: "n"`); c2 Exercism series (11 cases, errors as `raises: ValueError`, no bound); c3 Exercism largest-series-product (the 13 cases the track runs; AI references in O(n) with a zero count; `bound: "n"`, grow of mostly-1 digits with span n/2; the bound stated in `changes`); c4 icc longest_substr_k_distinct (icc's solution class and its 4 asserts plus 6 AI tests, `bound: "n"`, grow over 3 letters with k = 3). The Python track files (example.py, tests.toml, the test file) for the three Exercism slugs were added to `sources/_cache/exercism-python/` at 479f11b (FETCHED.txt appended). Every reference, Python and JavaScript, was run isolated (a fresh temp dir, `python3 -I` / node): all pass. A quadratic solution of c3 and of c4, swapped into a scratch copy of the book, passes every test and is reported by `check:code` as growing as n², past the bound n.

**NC cards** (`exercises-nc.json`, `build_nc.py`): MIT 6.006 S20 ps0 0-6 `count_long_subarray` and ps3 3-5(c) `count_anagram_substrings`, as code cards: statements read from the handouts' text layer with a replacement table (each entry with its reason), tests from the `tests` tuple of the template zip's tests.py (`ast.literal_eval`, nothing run), the starter the template's file, the reference MIT's solution listing read from the solutions handout, the solution field linking MIT's worked solution. Python only (MIT prints no other language). Both references pass MIT's 5 tests each, run isolated.

**Shared tools, changed backward-compatibly.** `tools/nc_cards.py`: a card may bring its own `answer`, `kind` and `changes`; without them a card is written as before (2.1's `build_nc.py` re-run: its `exercises-nc.json` byte-identical).

**Shared files.** `glossary.en.json`: 14 rows for 2.3, `pending`. `translation-notes.md`: two forced-scenario rows (the dropped 例题 numbers; the boxes as links to LeetCode's English pages).

**Checks.** `ost check --section 2.3`: ok. `check:content` (the book): no errors; 2 warnings, both chapter 1's. `check:code`: with the main app, 2.3's c4 fails ("NameError: name '_Solution__omnistax_cost'", the app bug below); with the runner fixed in the app clone, no errors and no warnings for the book.

**App bug, fixed in a clone.** Count mode's rewrite calls a helper named `__omnistax_cost`; inside a class body Python mangles that name, so any method of a class that calls a costed builtin fails under count mode (icc-style `Solution` classes). Fixed by naming it `__omnistax_cost__`, with a test in `tests/code_check.py` that counts a method of a class: `/tmp/claude-0/-home-user/249e18c8-3562-5258-9ce2-fd057404a6b0/scratchpad/app-2.3`, branch `claude/app-fixes-2.3`, commit e81fe94 (after 190edca, `ost` writing `sources` rows). Until it is merged, 2.3's c4 fails `check:code` and its "Submit" in the browser.

**Browser pass** (port 4503, private Vite cache, `--force`), shots in `/tmp/claude-0/-home-user/249e18c8-3562-5258-9ce2-fd057404a6b0/scratchpad/sec02-2.3/`. Fixed after looking: the pair-sum table's title ran into the strip's index row (table moved down, canvas taller); the table's axis name i stood beside row 3 and read as the current row (moved to the corner, as j); merge's j pointer and name ran into A's index row (B and C moved down); low and high on one element ran their names together ("lowhigh"; the section's pointer helper now sets the names to either side of the pair); the two-pointer caption said a[l] where the text says num[l]; merge's invariant line read "A[0..2)" after the rest of A had been copied (it now counts from what C holds); the variable window's last stop lost r and showed the window empty (Python leaves r at n − 1); 3SUM drew b and c on one element once low met high (no pair is drawn then). Because other agents' writes to the shared content reloaded the dev server mid-run, the final shots were taken from a frozen copy of the book (`scratchpad/root23`) served on 4503. One code card in the browser (c3, in a practice session): a wrong solution names its failing test, a correct double loop reads "Correct. Your solution makes about n² steps; this problem wants n.", and the linear solution passes "in about n steps" (`ex-c3-*.png`).

**For the chapter pass.** 区间 is "interval" here and "range" in 2.4 (glossary rows for both, pending). The three edges to 2.1's `array`. The `F.ds.pointer` name collision for long names sharing a cell is worked around in 2.3's figures.js; the library could set names aside itself. Whether NC code cards should carry JavaScript (MIT prints only Python). Wikipedia's 3SUM trace is kept with its own red and magenta (plan Question 2).


## Pass 12: section 2.4 Prefix sums and difference arrays (2026-11-09)

Planned and built in one run (`briefs/section-build.md`; `ch02/2.4/plan.md`, its nine questions decided there), on 1.5's
pipeline. Model: claude-opus-5-5, high effort.

**How the text was made.** No Chinese was typed. OI Wiki's `basic/prefix-sum.md` (pin c794414) is cut by
`tools/build_translation.py` into four blocks; the English is `translation.md`, element for element, parity clean. The page
writes MkDocs boxes (`???+ tip "规定"`), tabbed code and an image, which 1.5's page did not, so a new shared module,
`tools/oiwiki_boxes.py`, installs their reading into build_translation without changing it: a box is a `div.note` with its
title as eyebrow and is compared element for element; a box of code only is a code element (a `[[slot]]` in the
translation); an image is a slot, lifted after its box with any slot inside it; a block may leave out boxes by title
(`drop_boxes`); a link whose text is inline code is a link. `build_translation.py` itself is untouched; 1.5 built through
the module in a scratch copy gives byte-identical `text.html`, `source.md`, `footnotes.json` and `captions.json`. Run it as
`python3 -I tools/oiwiki_boxes.py ch02/2.4`.

**Code.** TheAlgorithms `PrefixSum` (`__init__`, `get_sum`; docstrings and `contains_sum` left out, the spec says why) is
read from the cache into a code set where OI Wiki's 参考实现 box stood; Java, C++ and JavaScript are AI translations,
compiled and run against the Python's doctest cases (all 7 match). doocs 0304 and 0370 Solution 1 in all four languages
(doocs prints them) are written into `figures.js` by `inline_code.py` (LeetCode's harness comment after 0304's classes
dropped). The doocs Python and TheAlgorithms' doctests (13/13) were run isolated (decision 17); 0304 on OI Wiki's matrix
gives the figure's S table exactly.

**What was built.** Four translated blocks with `data-ai`; the Convention, Example and Properties boxes as notes; erratum 20
as correction `err-2d-example`; links to Sections 40.4 (inclusion–exclusion) and 30.2 (Fenwick tree), both unbuilt.
Concepts `prefix-sums` (typed `key`), `prefix-sums-2d`, `difference-array`, `difference-array-2d`, nine forms, five edges
(`prefix-sums → array` added once 2.1 had staged `array`). Two debugger Sims: `sim-prefix-2d` (OI Wiki's figure behind the
original toggle, rendered to `media/ch02/oiwiki-prefix-sum-2d.png`; blue and red as facts; 12 cells then a query stepped
into its four terms; three queries, the whole matrix the padding case) and `sim-range-add` (canonical Java so the prefix
pass steps cell by cell; two inputs, one where the guard skips the write past the end). Referents l, r, c, i. Terms pass:
48 mentions marked, 1 left in ink ("an implementation"), two "difference array" mentions in the 2D block marked
`difference-array-2d`. No exercises (config: none for any concept).

**Checks.** `ost check --section 2.4`: ok. `npm run check:content` (content dir `/home/user/OmniStax/omnistax-content`):
no errors; the two warnings are 1.1's and 1.4's. `npm run check:code`: no errors (2.4 has no code card). Playwright on
port 4504 (own Vite cache), light and dark at 2×: both figures stepped (every stop kind: pad, cells with and without
padding, query terms, updates with and without the guard, the pass into each cell, the end), the original toggle; no
console errors. Shots in the session scratchpad, `sec24/`.

**Deviations from the plan.** None of substance: the 2D figure's legend line and the range figure's rule line are canvas
text, as 1.5's readout; block labels avoid `+=`/`−=` (the note sets them as maths).

**For the chapter pass.** Fold `tools/oiwiki_boxes.py` into `build_translation.py` (2.3 may need the same boxes). Add the
two forced scenarios to `translation-notes.md` and `ch02/config.md` (zh.cppreference → en.cppreference; OI Wiki's own
links → this book's sections) and the new glossary rows (plan.md, Terms) to `glossary.en.json`. Add 30.2 and 40.4 to
RULES' "Links to sections not yet built". `book.json` `authors` does not yet name doocs or TheAlgorithms (their `sources`
rows exist).


## Pass 13: section 2.5 Singly linked lists (2026-11-09)

Planned and built in one run (`briefs/section-build.md`; plan `ch02/2.5/plan.md`), on chapter 1's conventions. Model: claude-opus-5-5, high effort.

**How the text was made.** No source passage was typed. Wikipedia is wikitext, which no tool read, so a new shared tool, `tools/build_wikitext.py`, reads the cached `.wiki` files at their pinned revisions (Linked list 1382386163, Pointer (computer programming) 1382564071): headings, paragraphs, bold and italics, wikilinks, `<code>`, `<math>`, `{{IPA}}`, `<syntaxhighlight>` listings, one-space pseudocode, image frames; citations are not carried, a `group="note"` ref is a book footnote, and stand-alone templates are left out and named. It is a standalone script beside `build_markdown.py`; no existing tool was changed, so 1.1's build needed no re-run. The section's `build_spec.py` holds the blocks, the image and listing decisions, the AI translations of the C listings, the wikilinks the book carries (2.1, 2.2, 1.5, 3.1, 3.2), the marks and the record; its FIXES table is empty.

**What was built.** Four Wikipedia blocks: the Linked list lead with Basic concepts and Singly linked list; Pointer's Multiple indirection (to before the argv paragraph); Linked list operations with Singly linked lists; Linked lists vs. dynamic arrays (its comparison-table template left out). Four concepts (`singly-linked-list`, `pointer-to-pointer`, `implement-linked-list`, `linked-list-vs-array`, all Essential) and four edges through `ost`, including `linked-list-vs-array → dynamic-array` (2.2). Wikipedia's note on control data as a book footnote; erratum 18 as a correction note. Two four-language code sets (the C as the C++ variant verbatim, checked with g++; Python, Java and JavaScript AI, each run). One photograph (Singly-linked-list.svg, the lead's caption, Lasindi, public domain; its repeat dropped). Two debugger Sims: `sim-list-ops` (Wikipedia's four operations translated into four languages, six inputs: Wikipedia's insert and delete diagrams as originals, the one-node removal, and append with no tail as the bad case; unreachable nodes dashed, destroyed ones faded; links followed and written against n) and `sim-sorted-insert` (Wikipedia's double-indirection insert, C only, p drawn as a pointer to a link field, the passed nodes tinted as the invariant; inputs middle, new head, past the end, equal value). One code card: icc `linked_lists/linked_list` with its 16 asserts as 5 operation-list tests through a given `run(ops)` driver; icc's own solution and an AI JavaScript port pass, run isolated. Terms pass: 97 mentions judged, 54 marked (`terms.jsonl`).

**App** (branch `claude/app-fixes-2.5` in the scratch clone `app-2.5`, commit 1280032, not pushed): `F.ds.nodes`, `F.ds.links`, `F.ds.nodePointer` (and `F.ds.layout`) in `src/lib/fig/dsa.ts`, additive, with three tests in `tests/figlib.test.ts` (37/37 pass). Both Sims need it: on an app without it they throw.

**Checks.** `ost check`: no errors, the two by-design warnings (1.1, 1.4). `npm run check:content`: no errors. `npm run check:code`: no errors (11 Python references for the book). Playwright against the clone's dev server (port 4505, own cache, polling), light and dark at 2×: every input of both Sims stepped to its end, mid-move shots, the photograph and the scrolled page: no console errors. Screenshots in the scratchpad's `sec25/`.

**Deviations from the plan.** One caption sentence about the drawing (dashed nodes) was cut in the humanizer review; the lead's "The passage on multiple indirection is C" became "Multiple indirection is shown in C". The sorted insert's item sits at x = 1150 for the past-the-end input so its NULL label fits. Debugger inputs render as a dropdown (six choices) in `sim-list-ops`.

**For the chapter pass.** Wikitext is now read by `tools/build_wikitext.py`; 2.1 and 2.3 (also Wikipedia) should use or reconcile with it, and agree on the wikilink policy (link only where the book carries the subject). New forward links from 2.5 to 3.1 and 3.2 (the lead paragraph's "stacks", "queues") belong in RULES.md's "Links to sections not yet built". 2.6 and 2.7 also need nodes and links: they should build on commit 1280032 rather than add their own. `pointer-to-pointer` has no prerequisite in the map though its passage leans on C pointers (2.1's `pointer-arithmetic`); an edge may be wanted. The figure-row `draws` and the referent colours were not checked against a stored `colours` rerun (`npm run colours:default`).


## Pass 14: section 2.6 Doubly linked lists (2026-11-09)

Planned and built in one run (`briefs/section-build.md`; `ch02/2.6/plan.md`), on chapter 1's pipeline. Model: claude-opus-5-5, high effort.

**How the text was made.** No source passage was typed. Two ODS blocks (`linkedlists.tex` 109–146 and 148–238, pseudocode edition) through `tools/build_text.py`. `build_spec.py` holds placement, marks, the three cross-references (Figure 3.2 → `sim-dllist-ring`, Figure 3.3 → `sim-dllist`, `\chapref{arrays}` → Section 2.2), the code sets' assembly and an empty FIXES table. The Java edition's LinkedHashSet and the C++ edition's USet examples are printed by neither edition the book reads, so the section's last paragraph ends at "through external means" (`notes` says so).

**Shared tools, changed backward-compatibly.** `tools/build_text.py`'s ODS reader gained `\subsection` as `<h3>`, a whole-paragraph `thm`/`lem` as a note under its eyebrow, `\codeimport{…}` as the spec's code set (`CODE_SETS`) or HTML key (`CODEIMPORT`), a dotted field in maths (`$#u.next#=#w#$`), and a figure caption with a short form (`\caption[A DLList]{…}`). New `tools/ods_listing.py` reads an ODS listing from the Java, C++ and Python sources by ODS's own extractors' rules (snarf-java.pl, snarf-cpp.pl, snarf-python.py); the 2.2 builder has since added a `printed=True` option to it. 1.1, 1.2, 1.3, 1.4 and 1.6 rebuilt in a scratch copy with the tools before and after give byte-identical `text.html`, `source.md`, `footnotes.json` and `captions.json`.

**Code (decision 20).** Seven listings: six code sets and the addBefore listing as `sim-dllist`'s panel (plans-summary question 17). Java and C++ are ODS's as its extractors print them; Python is ODS's `dllist.py` with one port (`get_node`'s `self.n/2` → `self.n//2`, Python 2's integer division), so only getNode's Python carries the AI mark; JavaScript is an AI translation (`_remove(w)` for Java's overloaded `remove(Node w)`). The ported `get_node` and `add` were run isolated (`python3 -I`, a scratch copy) for every n < 8 and i: no failures.

**Media.** ODS's `figs/dllist2.ipe` and `dllist-addbefore.ipe` rendered by `render_originals.py` (iperender, private `IPELATEXDIR`, `TEXINPUTS` at ODS's latex directory) to `media/ch02/ods-dllist.png` and `ods-dllist-addbefore.png`.

**What was built.** Two concepts (`sentinel-node`, `doubly-linked-list`) and three edges through `ost` (→ `singly-linked-list`, → `list-interface`, → `sentinel-node`); five coverage rows; terms pass (25 candidates, 18 marked, `terms.jsonl`). Two Sims: `sim-dllist-ring` (still; n from 0 to 6, the cycle and the empty list's self-linked dummy) and `sim-dllist` (debugger: getNode then addBefore or remove, operation choice and n, i sliders with specials front, end and slowest; blocks find › fwd/back › hop, link › make/splice, unlink › skipn/skipp; walk shaded in the index tint; counter "steps ≤ 1 + min(i, n − i)"; nodes drawn as ODS's three-cell boxes, references as eased curves, a node outside the cycle above the row, a removed node faded). Five referents (dummy, p, w, u, i). One NC card (MIT 6.006 S20 ps1 1-4) in `exercises-nc.json`, statement read from the handout text with a 23-entry table checked against the page render.

**Checks.** `ost check --section 2.6`: ok. `npm run check:content`: no errors (the book's two by-design warnings, 1.1 and 1.4). `npm run check:code`: 1.6's references pass on rerun (the first run timed out under load); the one error is 2.3's c4, not this section's. The figure's trace checked by script against ODS's semantics for every op, n ≤ 6 and i (49 cases, 0 failures). Playwright on port 4506 (own Vite cache), light and dark at 2×: both Sims, the ring at n = 5, 1, 0, 6, the debugger at seven presets, stepped at the default level and stepped into, a mid-move frame, every language, both original toggles; no console errors (one aborted page request in dark during an HMR reload from another section's write). Screenshots in `scratchpad/secch022.6/`.

**Deviations from the plan.** None of substance. The index labels and the dummy's name stand above the box's left cell (under the box they collided with the prev references). The readout's "dummy" is not set in its referent colour (the readout's TeX does not colour `\htmlData{ref=…}`).

**For the chapter pass.** Strike B17 (the pseudocode edition's Summary names no Deque operation). Move 2.5's and 2.6's node drawings onto `F.ds.nodes`/`links` once 2.5's app branch is merged (2.5 draws two-cell nodes, 2.6 three-cell). RULES' "Links to sections not yet built": 2.6 links Section 2.2 (`\chapref{arrays}`) and Section 2.5 (lead). getNode and remove(w) appear twice on the page (code set and panel; plan question 3). The template tests of the MIT card wait for a class-testing `code` answer.


## Pass 15: section 2.7 Cycles in linked lists: tortoise and hare (2026-11-09)

Planned and built in one run from `briefs/section-build.md` (`ch02/2.7/plan.md`, questions decided there). Model: claude-opus-5-5, high effort.

**How the text was made.** One source, cp-algorithms `others/tortoise_and_hare` at d55d3f5, in English. No converter read English Markdown, so a new tool, `tools/build_markdown.py`, slices the page by heading lines (a heading met twice named by `from_nth`/`to_nth`) and sets it with `build_translation.py`'s own parser and inline setter, imported unchanged; it adds level-1 headings, centred `<div><img>` (the spec's IMAGES: a figure key or None; the alt text is the original caption), fenced blocks (CODE: a figure key or a `<pre>`), REPLACE/DROP/AT and MARKS as `build_translation.py` has them. No shared tool was changed, so 1.1's build is unaffected (no re-run was needed). `ch02/2.7/inline_code.py` writes cpa's two Java snippets into `figures.js` from the cache (tabs as four spaces, as 1.3 did for ODS).

**What was built.** Four blocks in cpa's order (`floyd-cycle-detection` spans blocks 1 and 3, since cpa prints Step 2 between its algorithm and its reasons); block 4's header is OmniStax's, "Why the reset finds the cycle start", since cpa repeats block 2's heading. Three concepts through `ost` (statements reworded to cpa; the map's "within O(length) steps" is not cpa's) and the edges cycle-start → floyd-cycle-detection and cycle-start-proof → cycle-start. Three Sims: `sim-rho-list` (still copy of the opening sketch, C in its referent colour), `sim-rho` (debugger: Java canonical, the source's; Python, C++, JavaScript AI; opens at the lap level; the race shades the stretch fast still has to cover to reach slow, the walk shades the two equal stretches to C; inputs cpa's list, no cycle, long tail a = 7 L = 3, cycle at the head), `sim-rho-proof` (a and L sliders 0..7 and 1..7, special a = 0; the readout writes slowDist, fastDist and a = (y − 2x)L − b with live values). One derivation, `drv-cycle-start` (score 5; cpa's three lines kept, three inserted). One code card, icc `find_loop_start`: its five asserts as source tests, five AI tests, its solution as the Python reference (made a function of the head), an AI JavaScript reference and harness, bound n. No errata.

**Checks.** `ost check --section 2.7`: ok. `npm run check:content`: no errors for 2.7 (the book's errors during the run were 2.2's, being built at the same time). `npm run check:code`: the Python reference passes with the bound. References run isolated (`python3 -I`, node) against all ten tests: 10/10 each. Headless at 2× in light and dark (dev server port 4507, own cache, HMR socket cut because sibling builds reload the page): every figure, every input of `sim-rho` stepped through, `sim-rho-proof` at its extremes, the derivation played; no console errors. Screenshots in the session scratchpad, `sec027/`.

**For the chapter pass.** The edge floyd-cycle-detection → singly-linked-list (2.5's concept) could not be merged yet: the merge refuses an edge to a concept not in `book.json`, and a refused row stays staged and blocks every later ch02 merge, so it was taken out again. Add it once 2.5 is merged. Whether `build_markdown.py` should serve chapter 3's cpa sections too.


## Pass 16: section 3.1 Stacks and bracket matching (2026-11-09)

Planned and built in one run (`briefs/section-build.md`; `ch03/3.1/plan.md`, its Questions decided there), on chapter 1's pipeline with 2.3 and 2.5 as the nearest models. Model: claude-opus-5-5, high effort.

**How the text was made.** No source passage was typed. A section-local `build.py` joins two sources block by block, as 2.3's does: Wikipedia's "Stack (abstract data type)" (revision 1376688119) read with `ch02/2.3/wikitext.py`, imported unchanged, and cp-algorithms' `combinatorics/bracket_sequences.md` read with `tools/build_translation.py`'s Markdown parser and inline setter (as `tools/build_markdown.py` uses them). What this article needs and 2.3's reader lacks is done in `build.py` around it: `*` list items, the list-defined `<ref group="nb" name=… />` note (a book note "nb 1"), `[[file:…]]` frames in either case, CS1's `author-last`/`author-first`, `<code>` inline, sub-headings inside a section, stand-alone templates dropped and named, and the one non-`cite` citation template (`{{Introduction to Algorithms|3|…}}`) set from the spec's `CITE_TEMPLATES`. `build_spec.py` holds placement, links, marks, the section record and the exercises; its FIXES table is empty. No shared tool changed, so 1.1's build was not rerun.

**What was fetched.** From Wikimedia's thumbnail service (the originals return 429): Lifo stack.svg at 960 px (`media/ch03/wp-lifo-stack.png`, CC0, vectorization by Alhadis) and the four push/pop GIFs at 330 px (`wp-stack-push.gif`, `wp-stack-pop.gif`, `wp-linked-stack-push.gif`, `wp-linked-stack-pop.gif`, CC BY-SA 4.0, Michel Bakni). The Exercism Python track's matching-brackets and simple-linked-list (`example.py`, `tests.toml`, the stub, the test file, and simple-linked-list's `.docs/instructions.append.md`) at 479f11b, into `sources/_cache/exercism-python/` (FETCHED.txt appended; no registry change).

**What was built.** Four blocks (Wikipedia: the lead with Non-essential operations, Implementation with Array and Linked list; cpa: the definition to "…in a similar fashion.", Balance validation), each with `data-source`/`data-locator`; three Wikipedia citations and its nb note as book notes; one new correction, `err-top` (top counts the items on the stack now, not those pushed so far). Three concepts (`stack`, `balanced-brackets`, `bracket-validation`) and three edges through `ost`; 62 concept mentions judged in `terms.jsonl` (6 left in ink: a stack of plates, a stack of physical objects, `array[0]`, three "list"s that mean the linked list). Lead with B12 and a back-pointer to 2.5 (68 words). One photograph (Lifo stack.svg) and three debugger Sims, every panel an AI translation in four languages: `sim-array-stack` (the GIFs' run, push to overflow, pop to underflow; one stop per call, a cell counter against 1), `sim-linked-stack` (one stop per call, links written against 2), `sim-brackets` (cpa's depth counter and stack in one panel, six inputs, the depth line under the string with the merged-types depth dashed under the stack's). Exercises: Exercism simple-linked-list (24 canonical cases the track runs, a given `run` driver), icc stack (its end-to-end test in three parts), Exercism matching-brackets (20 cases, bound n), Kattis delimitersoup (5 samples, 13 AI tests checked against a second reading of the statement); 3 pythonds NC cards in `exercises-nc.json`.

**References run** (decision 17, fresh scratch dirs, `python3 -I`): icc `stack.py` with its `test_stack.py` passes; the Exercism examples pass their track tests (matching-brackets 20/20, simple-linked-list 20/20); every Python and JavaScript reference of the four cards and the NC code card passes its tests (24, 3, 20, 18, 3).

**Checks.** `ost check --section 3.1`: ok. `npm run check:content`: no errors; the two warnings are not 3.1's. `npm run check:code`: 3.1's references pass; the two errors are 2.3 c4 and 3.4 c1 (class references under a bound: the step counter's name-mangling bug, being fixed elsewhere). Playwright on port 4511 (own Vite cache), light and dark at 2×: no console errors; every Sim stepped, stepped into, at its end, at every input's middle and end, and with its original shown. Screenshots in the session scratchpad, `secch033.1/`.

**Deviations from the plan.** The stack panels are classes, so that `self.top`/`self.head` wear their referent colours; `sim-brackets` has no referent `i`; citations numbered in page order. See plan.md, "Built".

**For the chapter pass.** Three Wikipedia readers now exist (`tools/build_wikitext.py`, `ch02/2.1/readers.py`, `ch02/2.3/wikitext.py`, plus this `build.py`'s additions); one should move to `tools/`, and the footnote numbering (page order or article order) and whether citations are carried (2.5 drops them) should agree. RULES.md's forward-link row "1.5 lead → 3.1" can be struck: 3.1 is built and is the stacks page. trekhleb's valid-parentheses tests (config) contradict Exercism's statement and were not used; config counted six pythonds self-checks for 3.1, the cache has three. The code panel colours attributes only after `self.`/`this.`; a `stk.top` receiver would need an app change. `build_section.py`'s `{{caption-text …}}` key does not match file names with spaces (the two original captions were set with `ost set`).


## Pass 17: section 3.2 Queues and circular buffers (2026-11-09)

Planned and built in one run (`briefs/section-build.md`; `ch03/3.2/plan.md`, its Questions decided there), on chapter 1's pipeline. Model: claude-opus-5-5, high effort.

**How the text was made.** No source passage was typed. Four ODS blocks, pseudocode edition, read by `tools/read_latex.py` through `tools/build_text.py`'s reader hook: `intro.tex` §The Queue, Stack, and Deque Interfaces (opening, list, FIFO paragraph, fig. queue), `arrays.tex` §ArrayQueue in two blocks (the circular array; the code through Summary), `linkedlists.tex` "Queue Operations" and the tail-removal paragraph. `build_spec.py` holds placement, marks (concept spans, referents in the maths of `circular` and `arrayqueue` by context, never ODS's "integer a"), two figure references (Figure 1.1, Figure 2.2), B18's link to 2.2, the JavaScript translations, the exercises and the section record; no FIXES table.

**Shared tools, changed backward-compatibly** (1.1–1.6 and 2.1–2.7 rebuilt in a scratch copy with the frozen and the new tools, each by its own build script: `text.html`, `source.md`, `footnotes.json`, `captions.json` byte-identical):
- `read_latex.py`: a `%` inside a space-free ODS `#…#` run is no longer stripped as a TeX comment (it cut `#a[(j+n)%a.length]#` and the rest of its paragraph) and is set as the edition's `\bmod`; a node field `#tail.next#` as `\mathit{tail}.\mathit{next}`; `#tail#`, `#head#`, `#null#` inside maths as the edition sets them (`\mathit{nil}`).
- `ods_listing.py`: C++ methods defined inside the class body (SLList.h) are read, as snarf-cpp.pl reads them; a run of three or more one-line fields stays one paragraph. Compared over every `\codeimport` in ODS's LaTeX: the only listings that change were empty or split before (ArrayDeque/ArrayQueue/SLList/BTree/LinearHashTable fields; SLList, SEList, SkiplistList, BTree and other in-class C++).

**Media.** `render_originals.py` (iperender, as 2.6) → `media/ch03/ods-queue.png`, `ods-arrayqueue.png`.

**What was built.** Four concepts (`queue`, `circular-buffer`, `array-queue`, `queue-linked-list`) and seven edges through `ost`; twelve coverage rows; terms pass 43 candidates, 40 marked (`terms.jsonl`). Lead with B11 and B15 (73 words). Six four-language code sets (Python, Java, C++ ODS's; JavaScript AI). Two Sims: `sim-fifo-queue` (moving, ODS Figure 1.1: ten calls, values in at the back and out at the front, readout of the orders in and out) and `sim-arrayqueue` (debugger, ODS Figure 2.2: ring and array side by side, j and the next write index (j + n) mod length(a) live in both with their numbers in the headline, resize() unrolling the ring into b copy by copy; four inputs Figure 2.2 | wrap around | grow from empty | drain; counter Σnᵢ ≤ 2m + 2r and per-resize "calls since ≥ nᵢ/2 − 1"). Its trace agrees with ODS's own Python ArrayQueue call by call on every input (ODS's Python under the AI port numpy.object → object, `python3 -I`). Errata 24 and 25 as correction notes, and a new one on Figure 2.2's caption (remove(i) for remove()) through the row's `figure`. Two code exercises: Exercism circular-buffer (14 canonical cases + 2 AI tests storing 0 and lapping the ring; AI references, Exercism's example cannot store 0) and icc queue_list (its test + 2 AI tests; icc's Python reference, AI JavaScript); references run isolated: 16/16 and 3/3 in Python and JavaScript.

**Checks.** `ost check --section 3.2`: ok. `npm run check:content`: no errors; the book's two by-design warnings (1.1, 1.4). `npm run check:code`: the 3.2 references pass; the one error is 2.3's c4, not this section's. Playwright on port 4512 (own Vite cache), light and dark at 2×: no console or page errors (two preload warnings during an HMR reload); both Sims shot, the debugger stepped at the default level and into a resize copy by copy, at every input, mid-move, to its end; the page scrolled screen by screen. Screenshots in `scratchpad/secch033.2/`.

**Deviations from the plan.** None of substance. ArrayQueue's one-sentence opening is carried at the head of `circular` (plan question 1). No linked-queue Sim (offered as an extra).

**For the chapter pass.** Add the Figure 2.2 caption correction to the reconciled errata list. 3.3's and 3.6's ODS listings now print where they were empty or split (ArrayDeque.a.j.n on one paragraph; SEList's C++). RULES' forward-link row "1.5 lead → Section 3.1" stays until 3.1 is built; 3.2's lead links Sections 3.1 and 3.3. `queue`'s terms include "Queue interface", so 3.3's Deque passage ("FIFO Queue and LIFO Queue") will list candidates for it. OpenDSA's StackQMCQ items wait for the converter.


## Pass 18: section 3.3 Deques (2026-11-09)

Planned and built in one run (`briefs/section-build.md`; `ch03/3.3/plan.md`, its Questions decided there), on chapter 1's pipeline with 2.2 and 2.6 as the nearest models. Model: claude-opus-5-5, high effort.

**How the text was made.** No source passage was typed. Three ODS blocks, pseudocode edition, read by `tools/read_latex.py` (dialect `ods`) through `build_text.py`'s reader hook: the Deque paragraph of `intro.tex`'s interfaces subsection (OmniStax `<h2>` "The Deque interface"), `arrays.tex` §ArrayDeque whole and §DualArrayDeque whole. `build_spec.py` holds placement, marks (concept spans, referent marks in the blocks' maths, five correction markers, the link "the previous section" → 3.2's `#arrayqueue`), `\figref` → Figures 2.3 and 2.4 linked to the Sims, `\lemref{arraystack-amortized}` → "Lemma 2.1" linked to 2.2's `#arraystack-cost` (B18), the code sets' assembly and JavaScript, one derivation and the section record; no FIXES table.

**Shared tools, changed backward-compatibly** (1.1, 1.2, 1.3, 1.4, 1.6, 2.1, 2.2, 2.4 and 2.6 rebuilt from a frozen scratch copy with the tools before and after: `text.html`, `source.md`, `footnotes.json`, `captions.json` byte-identical):
- `read_latex.py`: `eqnarray`/`eqnarray*` as an aligned display (`lhs & rel & rhs` → `lhs &rel rhs`); every `equation` numbered per chapter, its `\eqlabel{x}` stored as label `eq:x` (a key no other label uses) and set as `\tag{2.1}`; `\myeqref{x}` printed "(2.1)"; in ODS maths a control word straight before a one-word `#name#` keeps a space (`\ge#n#` was read `\gen`, `\lfloor#n#` `\lfloorn`).
- `build_text.py`: a MARKS row may carry a fifth field `'plain'` to replace in the whole block text, as a row whose old string holds a tag already does: a block whose maths holds a bare `<` (`$i<n/2$`) made `outside_tags` read the rest of the paragraph as a tag and miss every mark in it. No earlier spec has a fifth field.

**Code (decision 20).** Eleven listings: nine code sets (ArrayDeque a.j.n, get/set, remove; DualArrayDeque front.back, size, get/set, remove, balance) and each class's add(i,x) as its Sim's panel, where the source figure and the listing stood. Python, Java and C++ by `tools/ods_listing.py` (`printed=True`); ODS's Python unchanged (its `i < self.n/2` is, on Python 3, the real comparison the prose and Figure 2.3 make; plan question 1), so no Python carries the AI mark; JavaScript the AI's, from the Java, and DualArrayDeque's balance() from the C++. Every JavaScript set was run against a plain array (300 runs of 300 random calls each, both classes; an ArrayStack as 2.2 translated it under DualArrayDeque): no failure.

**Media.** ODS's `figs/arraydeque.ipe` and `dualarraydeque.ipe` rendered by `render_originals.py` (iperender, 300 dpi, private IPELATEXDIR) to `media/ch03/ods-arraydeque.png` and `ods-dualarraydeque.png`.

**What was built.** Three concepts (`deque`, `array-deque`, `dual-array-deque` Advanced), two forms (ArrayDeque's O(1 + min{i, n − i}), the lemma's Φ) and six edges through `ost` (→ stack, queue, array-queue, deque, dynamic-array-cost), all Hasse-reduced as the map has them; thirteen coverage rows; terms pass (51 candidates, 45 marked; "implementation" and "list" left in ink). Two debugger Sims, each opening on its ODS figure's calls and reproducing it call by call: `sim-arraydeque` (four inputs: Figure 2.3, both ends, the middle, grow from a wrapped start; blocks add › grow/left › shl/right › shr/store, remove › take/rl › shrl/rr › shrr/shrink, resize › alloc/copy/swap; live cells shaded in the index tint with their list positions in the corners, j and i as pointers, shift arcs including the wrap from cell 0 to the last cell; counter "shifted ≤ min(i, n − i)" and totals) and `sim-dualarraydeque` (five inputs: Figure 2.4, add at the back, add at the front, drain the front, alternate ends; front drawn leftward and back rightward from the middle as Figure 2.4 draws them; balance() copy by copy into new stacks below; the balance condition, PAL.bad where it fails; Φ, the lemma's count "calls since the last balance ≥ Φ − Φ₀" and its sum "copied ≤ 2m + 2r"). Both traces checked by script against ODS's own Python ArrayDeque and DualArrayDeque run isolated (copied files, `numpy.object` shim, `python3 -I`): 62 states after each call agree; the count and the sum hold at every frame; Φ₁ > n/2 at all 11 rebalances. One derivation, `drv-balance-potential`, replacing the proof's two `eqnarray*` and the words between, checked by `check_derivations()`. Corrections: errata 22, 23, 26 and two new ones (26b: ODS's Java and C++ divide n/2 in integers and shift one more than min{i, n − i} for odd n, i = (n − 1)/2, where Figure 2.3 and the Python shift left; 26c: "remove(x)" for remove(i)). Exercises: Exercism linked-list (18 canonical cases through a run(ops) driver; Python reference the Python track's example, MIT, fetched at the pin into `sources/_cache/exercism-python/…/linked-list` and recorded in its FETCHED.txt; JavaScript reference AI), Kattis integerlists (sample + 8 AI tests checked against a direct simulation, `bound: "n"` with a grow input, AI references); MIT 6.006 S20 Problem Session 1, 1-3 as an NC card in `exercises-nc.json`. All references run isolated: 18/18 and 9/9 in both languages.

**Checks.** `ost check --section 3.3`: ok. `npm run check:content`: no errors; no warning for 3.3 (the book's warnings are 1.1's, 1.4's and 3.6's). `npm run check:code`: 3.3's references pass; the run's three errors are 1.6 c2 (time limit under load) and 2.3 c4 and 3.4 c1 (`_Class__omnistax_cost` NameError: the cost counter's injected name is mangled inside a class, an app bug). Playwright on port 4513 (own Vite cache), light and dark at 2×: every input of both debuggers stepped to its end, stepped into, a mid-move frame, the Java panel, the derivation played through; no console errors. Screenshots in `scratchpad/secch033.3/`.

**Deviations from the plan.** `sim-arraydeque`'s "in the middle" input adds at ⌈n/2⌉, so that ODS's Java and Python take the same branch every call (at ⌊n/2⌋ they differ on every odd n); the bad case is the same, about n/2 shifts a call. The balance() code panel's Java lines follow its own (differently written) balance as nearly as its lines allow. The loop variable `i` of balance() wears the referent colour of `i` in the panel (the panel colours tokens by name).

**For the chapter pass.** RULES' "Links to sections not yet built": 3.3 links Section 3.1 (lead) and 3.2's `#arrayqueue`; 1.5 lead's link to 3.1 is now built. Errata list: add 26b and 26c. B18's reading "Lemma 2.1" kept as printed and linked (plan question 5): 3.2 and 3.6 should agree. The `potential-method` concept row may note that 3.3's lemma uses it as a counter (B14a). The app: a `'plain'` MARKS field exists now if other sections' maths hold `<`.


## Pass 19: section 3.4 Min-stacks and monotonic queues (2026-11-09)

Planned and built in one run from `briefs/section-build.md` (`ch03/3.4/plan.md`, questions decided there). Model: claude-opus-5-5, high effort.

**How the text was made.** Two cp-algorithms articles (`data_structures/stack_queue_modification`, `dynamic_programming/zero_matrix` at d55d3f5, C++ only) and Wikipedia's "All nearest smaller values" (revision 1377501815). No source text was typed. A section-local assembler, `ch03/3.4/build.py` (as 2.3's `build.py`), cuts the cpa blocks with `tools/build_markdown.py`'s `front_matter_end`, `slice_block` and `prepare` and sets them with `tools/build_translation.py`'s parser, and reads the Wikipedia block with `ch02/2.3/wikitext.py`, all imported unchanged; what these pages print beyond 2.3's and 2.7's (cpa's `*` bullets; `{{harvtxt}}`, `{{sfnp}}`, `{{citation}}`, `<code>`, `<sup>`, `:` lines) is rewritten in the assembler before the readers read it. No shared tool was changed, so 1.1's build is unaffected (not re-run). `inline_code.py` writes cpa's three snippet sets into `figures.js` from the cache. `build_spec.py` holds placement, marks, the code-set translations and the section record; there is no replacement table.

**What was built.** Seven blocks (cpa ×5, Wikipedia, cpa). Six concepts and six edges through `ost` (`monotonic-queue-minimum → deque` left out: 3.3's `deque` is not in `book.json` yet). Four debugger Sims, all with four-language panels: `sim-min-stack`, `sim-min-queue` (method 1 driven by the fixed-length window, with an M slider), `sim-two-stack-queue` (method 3, step into one transfer move) on cpa's C++ (canonical; Python, Java, JavaScript AI), and `sim-nearest-smaller` on an all-AI translation of Wikipedia's pseudocode (kept as `<pre>` in the text). Method 2 and the zero-submatrix code as code sets (C++ the source's). Errata 28, 29 and a new one (35: `d[i], i = 1...m − 1`) as correction notes; Wikipedia's five citations as book footnotes. Two code cards (ODS Exercise 3.14 with TheAlgorithms' doctests; cpa's zero-submatrix sentence with tryalgo's grids, 0 and 1 swapped), one NC card (6.046J S15 ps4 4-1, chapter 1 question 31). Terms pass: 80 mentions, 75 marked.

**Checks.** `ost check --section 3.4`: ok. `npm run check:content`: no errors (warnings are 1.1's, 1.4's and 3.5's). `npm run check:code`: one error for 3.4 c1 (and the same for 2.3 c4): an app bug, below; with the fix both references pass their tests and grow linearly (run against the fixed runner and under node, isolated). Headless on port 4514 (own Vite cache, HMR socket cut), light and dark at 2×, every input of every Sim stepped: no console errors. Screenshots in the session scratchpad, `secch033.4/`.

**App fix.** Count mode's cost helper was named `__omnistax_cost`; inside a class body Python mangles it, so any reference with a class failed the complexity check (NameError `_MinStack__omnistax_cost`). Renamed `__omnistax_cost__`, with a test in `tests/code_check.py`: clone `scratchpad/app-3.4`, branch `claude/app-fixes-3.4`, commit 5843515 (not pushed).

**For the chapter pass.** Add `monotonic-queue-minimum → deque` once 3.3 is merged. Erratum 35 for `judgements/ch01-03-reconciled.md`. 1.5's `exercise_notes` should say 6.046J S15 4-1 is set in 3.4. Credits for tests taken from TheAlgorithms and tryalgo are in each card's `changes`; whether `exercise_sources` should carry them with their MIT notices. A zero-submatrix Sim (exploration's seed) is not built.


## Pass 20: section 3.5 Stack applications: expression evaluation (2026-11-09)

Planned and built in one run from `briefs/section-build.md` (`ch03/3.5/plan.md`, questions decided there). Model: claude-opus-5-5, high effort.

**How the text was made.** One source, cp-algorithms `string/expression_parsing` at d55d3f5, in English, through 2.7's `tools/build_markdown.py`, unchanged (no shared tool was changed, so 1.1's build is unaffected). Four blocks in cpa's order: `rpn` (the lead and Reverse Polish notation), `parsing`, `unary`, `right-assoc`. The exploration's one `unary-right` block became two, since cpa prints Unary operators and Right-associativity as sibling headings and one block would hold two `<h2>`s. The pinned page prints C++ only, so its two listings and two `while` fragments are four-language code sets with the C++ read from the cache by `build_spec.py` and Python, Java and JavaScript as AI translations in `code/`. Every translation was checked against cpa's C++ (compiled with g++) on about 1,150 random expressions per listing: Python, Java and JavaScript agree on every case. Erratum 30 is a correction note after "higher than all of the binary operators."; erratum 31 is not noted (config).

**What was built.** Three concepts (`rpn-evaluation`, `expression-parsing`, `unary-right-assoc`) and the edges rpn-evaluation → stack, expression-parsing → rpn-evaluation, unary-right-assoc → expression-parsing, through `ost` (merged). Terms pass: 34 candidates, 31 marked, the three uses of "implementation" (meaning code) left in ink. One debugger Sim, `sim-two-stack-parser`, after cpa's unary listing: its panel is cpa's `evaluate` with cpa's own general `while` (`left_assoc`), C++ canonical, all four languages AI-marked (the C++ is changed); `inline_code.py` writes the panel from the cache. It opens at level 1 (read the operator, execute each operator on top that outranks it, push), 13 to 33 stops per input; inputs (2*5-1*2)/(11-9), -(3-5)*-2, 2^3^2, 8-3-2 and −2^2 (cpa's priorities give 4: the bad case, in `PAL.bad`); the RPN emitted so far under the string; the invariant (op above its last "(" in rising priority) tinted and written with live values; the cost as characters read and operators executed of those pushed. Referents st, op, i (marked in the lead) and cur_op. Exercises: Exercism forth (the track's 54 cases, the track's example as Python reference, AI JavaScript), Kattis calculator and bracketsequence (samples as source tests, AI tests checked against exact fractions and an independent recursive reading, AI references, bound n); two pythonds NC cards (postfix1 open with its key, postfix2 number 9) in `exercises-nc.json` by `build_nc.py`.

**What was fetched.** The Exercism Python track's forth (`.meta/example.py`, `.meta/tests.toml`, `forth_test.py`, `.docs/instructions.append.md`) at 479f11b, into `sources/_cache/exercism-python/` (FETCHED.txt appended). The example passes all 54 track tests, run isolated (`python3 -I`, fresh scratch directory).

**Checks.** `ost check --section 3.5`: ok. `npm run check:content`: no errors for 3.5 (the book's warnings are 1.1/1.4's by-design code sets and 3.6's referents). `npm run check:code`: the 3.5 Python references pass, with the bound on both Kattis cards (the two errors in the run are 2.3's and 3.4's, the runner's name-mangling bug that 3.4's builder fixed in `app-3.4`, commit 5843515). JavaScript references under node: 54/54, 6/6, 13/13. Headless at 2× in light and dark (dev server port 4515, own cache, HMR socket cut): every input stepped to its end, a move caught mid-way, the four code languages; no console errors.

**Deviations from the plan.** The block split above. pythonds prints three Self Checks on this page, not the six `config.md` counts; two ship. The Sim draws exponentiation as ∧, as cpa writes it in its maths, since the figure font sets a lone ^ too small to read. No predict pause (the library has none).

**For the chapter pass.** The op referent's light-theme colour (a dark olive) reads near ink on the text, as 1.x's referent yellow did. `F.ds` has no stack primitive; this Sim draws its two wells by hand, as 3.1–3.4 will want too. figlib's `text` has no escape for a literal underscore (the Sim writes `cur_​op`). Whether the RPN block (Essential) wants its own small one-stack Sim, considered and not built.


## Pass 21: section 3.6 Space-efficient lists (2026-11-09)

Planned and built in one run (`briefs/section-build.md`; `ch03/3.6/plan.md`, its Questions decided there), on chapter 1's pipeline with 2.2 as the model. Model: claude-opus-5-5, high effort.

**How the text was made.** No source passage was typed. Seven ODS blocks (`arrays.tex` §RootishArrayStack, Space Usage, Summary, Computing Square Roots; `linkedlists.tex` §SEList through Removing an Element, Amortized Analysis of Spreading and Gathering, Summary) through `tools/read_latex.py` (dialect `ods`). "Computing Square Roots" is `\notpcode` (Java and C++ editions only): it is read with the edition switch `notpcode` on for that block alone, in the pseudocode edition's typography. `build_spec.py` holds placement, marks (concept spans, B18 links, referents in the two debugger blocks' maths, three converter gaps set by mark: `u.next.next`, `sqrttab[i]`), the JavaScript and FastSqrt-Python translations, four derivations with `check_derivations()`, and the section record; no FIXES table.

**Shared tools, changed backward-compatibly.** `read_latex.passage(..., edition=None)` and `ods_edition(text, table=None)`; `build_blocks.py` passes a block's `edition`; `ods_listing.cpp` reads a field whose type is a template of pointers (`ArrayStack<T*> blocks;`). With only these changes over a frozen copy of the tools, 1.1, 1.2, 1.3, 1.4, 1.6, 2.2 and 2.6 rebuild byte-identical (`source.md`, `text.html`, `footnotes.json`, `captions.json`). Note: with the current shared tools (which also carry 3.3's read_latex changes), 2.2's `source.md`/`text.html` change by one space (`n_i\le \mathrm{length}`), from 3.3's "control word before #code# keeps a space" rule, not from this section.

**Code (decision 20).** Every `\codeimport`/`\pcodeimport` is a four-language code set; SEList's two `\pcodeimport`s take the Java/C++ members the other editions print there (getLocation, add(x)). RootishArrayStack's Python listings that divide an int with `/` show the `//` port and carry the AI mark. FastSqrt's four listings stand at the Java edition's `\javaimport`s; Java and C++ are ODS's (including the "fake code" in comments the snarf scripts print), Python and JavaScript AI. ODS's Python ran isolated (`python3 -I`, scratch copy, `numpy.object` shim, `//` and `print()` ports): `test_rootisharraystack` and `test_selist` pass; the figures' traces agree with ODS's Python on every preset (Figure 2.5's calls, the SEList cases and both runs) and `build_spec._selist_add` agrees with `selist.py` block for block over 160 random runs.

**Media.** `render_originals.py` renders Figures 2.5, 2.6, 3.4 (a, b, c) and 3.5 (a, b, c) with iperender to `media/ch03/ods-*.png`.

**What was built.** Five concepts (`rootish-array-stack`, `rootish-index-math` Beyond, `sqrt-space-lower-bound`, `space-efficient-list`, `selist-spread-gather` typed `cost`) and six edges through `ost`; 16 coverage rows; eight referents; the lead with B14b (78 words). Six Sims: `sim-rootish` (debugger, ODS's seven RootishArrayStack methods, five inputs incl. Figure 2.5's calls and "get every index", the i2b formula live under the blocks, waste against 2r − 1), `sim-gauss` (still, r slider), `sim-wasted-space` (still growth plot, n slider), `sim-fastsqrt` (debugger, FastSqrt.sqrt(x) on four inputs, the bits of x and x′), `sim-selist-add` and `sim-selist-remove` (debuggers, ODS's add+spread and remove+gather, the three cases and a 16-add / 12-remove run, Φ and spreads ≤ m/b). Nodes drawn with figlib primitives (not 2.5's unmerged `F.ds.nodes`). Four derivations (`drv-rootish-blocks`, `drv-sqrt-lower-bound`, `drv-root`, `drv-selist-spread`). Errata 27, a new one on Figure 3.5(b) (with b = 3 the code gathers; Case 2 needs at most b − 1 blocks), and a new one on FastSqrt's printed `inittabs()` (2^{r/2} tables against the 2^16 the text and sqrt(x) need; C++ `1<<d+k`). Terms pass: 139 candidates, 116 marked (`terms.jsonl`).

**Checks.** `ost check --section 3.6`: ok. `npm run check:content`: no errors; the book's two by-design warnings (1.1, 1.4). `npm run check:code`: no errors. Playwright on port 4516 (own Vite cache, polling), light and dark at 2×: see the report.

**Deviations from the plan.** The SEList runs are 16 adds and 12 removes (the plan's 30 gave hundreds of stops). In Java, C++ and JavaScript the SEList panels colour only `w` and `i`: Java's `u` is the scanning node in add (Python's `w`) and `l.u` the located one, which the panel cannot colour.

**For the chapter pass.** Edge `space-efficient-list → array-deque` once 3.3's concept exists (staged then removed: an edge to a missing concept stops the chapter's merge). The link "Section 3.3" goes to `/ch03/3.3/#arraydeque` (exploration's block id; check it). B14b's wording should match B14a's in 3.3. Python SEList `remove(i)` returns nothing (Java and C++ return y); not noted. Extra Sim offered: a b slider on the SEList runs.

## Pass 22: chapters 2 and 3 pass (2026-11-09)

Plan phase 3 over 2.1–2.7 and 3.1–3.6, from the "for the chapter pass" lists of passes 9–21 and the plans'
Questions. Model: claude-opus-5-5, high effort.

**Log.** The thirteen `log-pass.md` files are passes 9–21 above, in section order, under this file's heading
convention; the files are removed.

**Rebuilds and the terms rows.** Every section of chapters 1–3 was rebuilt from the current tools. The terms rows
(`terms.jsonl`) named their mention by its number among every mention of every built concept's terms, so chapter 2's
and 3's new concepts (array, stack, queue, deque …) shifted the numbers in every earlier section and a rebuild marked
the wrong words or refused. `tools/apply_terms.py` now finds each row again by its term, its sentence and its place
among mentions with both (`term`, `context`, `nth`, given to every chosen row once, from the committed pages), and
wraps the mentions in the section's own folder, so a scratch copy no longer writes the book. With that, every page
rebuilt byte-identical. 2.2's one-space change (3.3's `\le` rule) does not occur with the current tools; 2.5 and 2.7
build, in place and in a scratch copy. The new concepts' mentions in earlier pages were judged: 105 marked (1.1's
arrays and "List interface", 1.3's and 1.5's arrays, 1.5's dynamic array, resizes and stack, 2.1's Stack, Queue and
Deque, 2.2's "Queue interfaces" and Stack, 2.3's circular buffer, 2.5's unrolled linked lists, 2.7's linked lists and
two pointers, 3.2's LIFO and Deque); priority queues, "list" as a word, and the like stay in ink.

**One Wikipedia reader.** `tools/wikitext.py` replaces 2.1's `readers.py` wikitext part, 2.3's `wikitext.py`, the
readings 3.1's and 3.4's `build.py` added around it and the reader inside `tools/build_wikitext.py`; 2.1 builds
through `build_text.py`'s reader hook (`wikitext.text_block`), 2.5 through `build_wikitext.py`, 2.3, 3.1 and 3.4
through their assemblers calling `wikitext.block`. Every spec's `parts` are now one form (dicts: lead, section,
from/to, start/stop; `cut_after`, `stop_at`, `h3`). Decided once (RULES.md, Wikipedia): citations are book notes,
numbered in page order, a named one reused keeping its number; explanatory notes keep their group label; a wikilink
is a link only where WIKILINKS map it (2.5, 3.1). Intended differences only: 2.1's notes renumbered 1–8 (were the
article's 1–5, 8, 12, 13), 2.3's reused Skiena citation keeps number 2, citations set in one CS1/CS2 style (curly
quotes, edition after the title, CS2 without its own full stop), 2.5's link tail inside its link, 3.4's doubled spaces
collapsed; footnote rows synced into `section.json` through `ost`. `tools/oiwiki_boxes.py` is folded into
`build_translation.py` (1.5 and 2.4 byte-identical); 3.1's cp-algorithms blocks are sliced by `build_markdown.py`'s
functions (byte-identical), and a page of cp-algorithms alone builds with it (2.7, 3.5). Text tables from OI Wiki and
Wikipedia now stand in `div.book-table` as ODS's do (1.5's stack table and 2.1's byte table had no rules or padding).

**ODS names.** The pseudocode edition snake-cases ODS's names; `read_latex.py` now does too (2.1's and 3.3's
add_first, remove_first, add_last, remove_last; 2.1's `sim-list` labels). 2.6 and chapter 1 still use the older ODS
reader (open, RULES.md).

**Concepts.** The five edges left out mid-build are merged (floyd-cycle-detection → singly-linked-list,
monotonic-queue-minimum → deque, space-efficient-list → array-deque, pointer-to-pointer → pointer-arithmetic;
list-interface → interface-vs-implementation was in `book.json` and is now an EDGE in `map.spec`). `map.spec` carries
every chapter 2–3 concept's built name and statement; `build.py`, `report.py`, `check_map.py` clean (1022 concepts,
1332 edges). All 77 concepts agree with the map in name, statement and edges; each has one introducing span, in its
home section; the 90 edges are Hasse-reduced and acyclic (checked by script).

**Errata, bridges, glossary.** `judgements/ch01-03-reconciled.md`: errata 35–42 (3.4's d-index, 2.1's rotate index set,
3.1's top, 3.2's Figure 2.2 caption, 3.3's 26b and 26c, 3.6's Figure 3.5(b) and inittabs) and every chapter 2–3 note id;
erratum 17 (C29) stands unnoted. B17 struck; B14a and B14b worded alike in the 3.3 and 3.6 leads (both mark
`potential-method`); B18 printed one way ("Lemma 2.1" as ODS prints it, linked; "resize() of ArrayStack" wrapped).
Every glossary row decided: 区间 is "range" in 2.3 and 2.4 (2.3's three "interval"s changed); the forced scenarios of
2.3 and 2.4 in `translation-notes.md` and `ch02/config.md`. RULES.md: the links table struck for 2.2, 2.5 and 3.1 and
extended with 30.2 and 40.4; every chapter 2–3 cross-link checked by script. `ch03/config.md`'s pythonds counts (three per
page, not six) and the trekhleb line corrected; 1.1's, 1.4's, 1.5's and 2.2's notes say where held cards are set.

**Colour.** `npm run colours:default` kept every type's colour, but 39 of 97 referents wore the palette's first red,
0.03 from PAL.bad in the dark theme (3.5's `st`), and the dark olive and dark green stood 0.12 from the light ink
(3.5's `op`, chapter 1's yellow). The app now lets a book store `referentAvoid`: no smart referent within 0.10 of
PAL.bad or 0.15 of ink, and farthest-apart dealing wears one only last; `colours:default --reorder-referents` sets it
and works the order out again. Other books store no flag and deal as before. Now the nearest referent stands 0.109 from
PAL.bad and 0.158 from ink; 5 groups are dealt farthest apart (2 before), the worst pair in a group 0.123 (0.083 before).

**App** (OmniStax, branch claude/confident-cannon-bl42ph, not pushed): referents clear of PAL.bad and ink (ea775d0,
with tests); article `<pre>` scrolls inside the column, adjacent footnote markers read 1,2,3 (2f325da, with a test).

**Checks.** `ost check`: no errors, the two by-design warnings. `npm run check:content`: the same. `npm run check:code`:
28 Python references, no errors. `npm test`: 1193 pass, 0 fail. Headless (dev server, own cache, port 4520): all 13
pages in light and dark, every figure at its opening state, the lead and the footer: no console errors, no failed
requests, no KaTeX errors, every figure eyebrow "Sim", every internal link resolving (the two to 30.2 and 40.4 listed).
Screenshots in the session scratchpad, `ch0203pass/`.

**Open.** 2.6 and chapter 1's ODS prose in the older reader (italic calls, camel case). `book.json` `authors` names
neither doocs nor TheAlgorithms (ost cannot write it; the footer credits them from `sources`). 3.3's derivation cites
"2.4 DualArrayDeque", ODS's own section number. NC cards were not shot (they show only in a practice session). The
`F.ds.pointer` name collision and a `stack` primitive are still for figlib; 2.5–2.6 still draw nodes by hand rather than
with `F.ds.nodes`. The owner's review of the translations; a person's reading of WG14 N3517.
