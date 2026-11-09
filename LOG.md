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
