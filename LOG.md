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
