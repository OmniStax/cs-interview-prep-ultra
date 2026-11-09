## Pass: section 1.5 Amortized analysis, the first translated section (2026-11-09)

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
