# Chapter 1 config: Algorithms and their cost

Status: **proposed, not agreed** (2026-11-08). One setting per line (root item 10). The per-section loop begins only after the user agrees this list and makes the exercise choice at the end; no default is assumed for that choice.

1. Chapter: 1 Algorithms and their cost, folder `ch01`, sections 1.1–1.6, 27 concepts (`exploration.md`).
2. Start point: 1.1, then in order to 1.6.
3. Loop: one section per page, with a stop after each section for review (root item 2); the plan of each section is reviewed before it is built (root item 5).
4. Sources per concept: the winners in `judgements/ch01-03-reconciled.md` (final table, chapter 1) plus `random-variable` from `mcs2018:19.1` (decision 18); one source per concept, its words kept whole; per-block `data-source` and `data-locator` as listed in `exploration.md`.
5. Worked example: `jeffe:0.3` (ApportionCongress) carried whole in 1.1 (decision 18).
6. Erickson text: transcribed from the PDF, never from the cached `.txt`.
7. Translation: the three 1.5 blocks from OI Wiki (≈1,420 words) under `docs/prompts/translate.md`, AI-marked as translations; no OI Wiki code copied.
8. Bridges: B1 (pending the Compass question), B2, B3, B5 in the leads as listed in `exploration.md`; no bridge in the text.
9. Errata: notes 1–12 and 14 of `exploration.md` as correction footnotes, AI-marked; the source text unchanged.
10. Leads: one or two sentences, AI-marked, naming the section's tier (all six sections Essential) and the concepts of another tier (1.1 lattice Advanced; 1.2 harmonic Advanced; 1.3 multivariate Big-O Advanced; 1.5 potential Advanced and counters Beyond; 1.6 indicators Advanced), the indexing convention, and the section's bridges, within 80 words.
11. Objectives and summaries: none (no source prints them).
12. Chapter introduction and summary pages: none.
13. Figures: the ten Sims of `exploration.md` as seeds; each plan argues its own lines. Source figures (ODS bigoh and harmonic plots, Erickson's traces) are originals behind the toggle; Erickson's two historical scans kept as photographs with their credits where the text points at them.
14. Figure label: Sim or photograph only, no figure numbers, pending the RULES ruling.
15. Code beside the visual: in sim-peasant, sim-lattice, sim-apportion and sim-loop-count; none in the property and growth figures (sim-halving, sim-harmonic, sim-big-o-witness, sim-growth-race) and none in sim-coin-tosses.
16. Code shown: the source's own (Erickson pseudocode, ODS Java); runnable Python/JS counterparts only where an exercise needs them.
17. Depth: 2D throughout; no 3D scene.
18. Extra simulations (root item 15): none proposed beyond the seeds until the plans.
19. Colour: types `cost`, `size`, `key`, `index`; referents per figure (`exploration.md`); probabilities untyped.
20. Derivations: the candidates in `exploration.md`, each scored in its plan.
21. References item: at most three CIU links per section, each with one sentence; all CIU videos are link-only (their licences could not be read).
22. `counter-increment-decrement`: held unbuilt as a placeholder concept, pending the user (no open prose).
23. Exercise placement: end exercises to the Exercises system; no inline Try Its from the sources; the figures' predict pauses pending the user's ruling.
24. Exercises held elsewhere: Erickson ch. 1 Factorial item → 4; ODS ch. 1 ex. 1, 5, 6, 7 → 3, 5, 8; MIT 6.856J → 22.
25. Bloom levels and concept tags: AI-judged.
26. `ai`: the building agent's model id and effort per part; `built` the ISO date.

## Exercise count report (root item 13)

Counted from `dossiers/ch01.md` (Exercises tables) and `judgements/ch01.md` (ranked exercises), with excluded sources removed. "Items" are the sources' own items; a source row that gives no number is counted as one row and said so. Proposed new: none, under METHOD decision 4 (no AI-written exercises).

- **Check** (keyed multiple choice, true/false, fill-in; OpenDSA): 88 printed (1.1: 30, 1.2: 6, 1.3: 23, 1.4: 28, 1.6: 1), plus 10 OpenDSA summary sets that redraw the same items; 87 keyed and usable (the judge drops AlgAnlsMCQalgdfn, whose key contradicts Erickson). Available now as `choice` or `number` once a converter reads OpenDSA's Khan-format HTML; 6 of the 1.2 items are parameterised generators and become one fixed instance each.
- **Trace** (keyed interactive ordering; OpenDSA CompareGrowth, GrowthRatesPRO, 1.3): 2 printed, 2 keyed; available with the `sequence` answer type (shared library, not yet built), or now as `open` with the key as solution.
- **Exercise** (written):
  - keyed in the source: 130 (1.2: Aspnes 2; 1.3: Aspnes 2; 1.6: brisk 25, Wikibooks 87, Aspnes 14), available now;
  - partly keyed: 80 (1.6: Levin 46, of which the first file keys 10 of 16 and the rest are not yet counted; Applied Combinatorics 34, of which 28 have a hint or answer);
  - unkeyed: 209 in the chapter (1.1: Erickson ch. 0, 5; 1.2: MCS 14.12–14.17, 6; 1.3: MCS 14.18–14.42, 25, and Applied Combinatorics, 6; 1.6: MCS ch. 15–19, about 115, Applied Combinatorics 7, OpenIntro 45), available only with AI solutions. By what writing them takes, counted by source and not yet item by item: about 5 explain or design (Erickson), about 31 prove (MCS 14.x), about 173 compute (MCS 15–19, Applied Combinatorics, OpenIntro), some of MCS 15–19 being proofs. Erickson's ex. 5 needs a priority queue named only in 0.3.
- **Code** (implement against tests):
  - with source tests: 4 (difference-of-squares 9 tests, grains 11, baffling-birthdays 17, pascals-triangle 8); references run: the Exercism examples for difference-of-squares and grains pass, the judge's own references for the other two pass. Available once the `code` answer type and runners exist (app);
  - samples only (Kattis, statement plus 1–3 samples, no reference on file): 13 (1.2: 5; 1.6: 8), available only with AI tests and an AI reference (`tests_by: "ai"`). The judge rates 6 a good fit (howmanydigits, stirlingsapproximation, inversefactorial, dicecup, anagramcounting, fruitbaskets) and flags 7 (loworderzeros and factorialpower are number theory; subcommittees is factorisation; catalan never defines Cₓ; diceyfrequencies misstates its sum; estimatingtheareaofacircle is arithmetic; expectedearnings tests one expectation, not linearity);
  - test cases with no statement: peasant multiplication (TheAlgorithms 13 doctests; trekhleb 2 jest suites, run and passing): no exercise unless a statement is found (Erickson's prose is not one, per the judge).
- **NC cards** (`exercises-nc.json`): 34 keyed (1.2: 1; 1.3: 4; 1.4: 5, one a code exercise with tests; 1.5: 3; 1.6: 21), 30 unkeyed (Erickson's notes: 14 on amortized analysis, 16 on probability), 4 statement-only (Project Euler 15, 20, 34, 53, answers unpublished).
- **Concepts with no open exercise**: underspecified-algorithm, multivariate-big-o, amortized-analysis, aggregate-accounting, potential-method and counter-increment-decrement (the whole of 1.5 has NC cards only), peasant-multiplication (tests, no statement), lattice-multiplication (its only exercise is held for chapter 4); running-time-guarantees has no exercise that separates amortized from expected time; word-ram has none on w ≥ log n; random-variable not yet searched (MCS 19.x likely).

**The choice the user must make**, per kind (or per section):

- Check: take all 87, or the judge's ranked first per concept only.
- Trace: wait for `sequence`, or ship the 2 now as `open`.
- Exercise: (a) key only — the 130 keyed now, the partly keyed counted item by item and their unkeyed items named in `exercise_notes`, the 209 unkeyed left out; or (b) AI solutions for some or all of the 209 (say which sources or sections); and whether to cap 1.6, which alone has about 373 written items (126 keyed, 80 partly keyed, about 167 unkeyed).
- Code: (a) source tests only — the 4; or (b) also the Kattis items with AI tests and an AI reference (all 13, or the judge's 6).
- NC cards: include in `exercises-nc.json` (keyed only, or keyed and unkeyed with AI solutions), or leave out. For 1.5 they are the only exercises.
- New exercises: decision 4 rules them out; reopen only if the user wants exercises for the concepts listed above.
