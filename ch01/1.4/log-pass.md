## Pass: section 1.4 Analysing running time and space (2026-11-09)

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
