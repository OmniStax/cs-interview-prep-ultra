# Chapter 2 config: Arrays and linked lists

Status: **proposed, not agreed** (2026-11-08). One setting per line (root item 10). The loop begins only after the user agrees this list and makes the exercise choice at the end; no default is assumed.

1. Chapter: 2 Arrays and linked lists, folder `ch02`, sections 2.1–2.7, 26 concepts (`exploration.md`).
2. Start point: 2.1, then in order to 2.7 (or 2.3 first, if it becomes the first template: `RULES.md`, Template sections).
3. Loop: one section per page, a stop after each (root item 2); each plan reviewed before building (root item 5).
4. Sources per concept: `judgements/ch01-03-reconciled.md` (final table, chapter 2); per-block `data-source` and `data-locator` as in `exploration.md`.
5. Folds: OI Wiki two-pointer and prefix-sum pages split over 2.3 and 2.4 as listed; nothing else folded.
6. Translation: the six OI Wiki blocks of 2.3 and 2.4 (≈1,830 words), AI-marked as translations; OI Wiki code never copied; a 例题 that restates a LeetCode problem becomes a link.
7. Runnable code where the winner's is unlicensed or not runnable: TheAlgorithms (MIT) for two pointers and prefix sums; doocs code (CC BY-SA, decision 18) for the product window (0713), 2D prefix sums (0304) and the difference array (0370); credited per block.
8. ODS Python: run through the shims of `judgements/ch01-03-references.md` (no edit to ODS files).
9. Bridges: B6, B7, B8, B9, B10, B16, B17 in the leads; 2.3's lead may overflow 80 words and goes back to the user if it does.
10. Errata: notes 15, 16, 18, 19, 20 as correction footnotes; note 17 ("C29") only after a person checks it.
11. Leads: the tier (all Essential; 2.2 block-copy Advanced; 2.4's 2D concepts Advanced), the indexing convention per section, the bridges.
12. Objectives, summaries, chapter introduction and summary pages: none.
13. Figures: the ten Sims of `exploration.md` as seeds; source figures behind the original toggle; Sim or photograph labels only, pending the RULES ruling.
14. Code beside the visual: every procedure figure (sim-arraystack, sim-two-pointers, sim-merge, sim-variable-window, sim-linked-list, sim-dllist, sim-rho); none in sim-address (a property), sim-moving-window and sim-prefix (formulas).
15. Depth: 2D throughout.
16. Extra simulations: none beyond the seeds until the plans.
17. Colour: types `index`, `key`, `cost`, `size`; the code variables as referents (`COLOR.md` §3).
18. Derivations: the candidates in `exploration.md`, scored in their plans.
19. References item: at most three CIU links per section.
20. Exercise placement: end exercises to the Exercises system; held items as in `exploration.md` (ODS 2.7 → 3.3; subseqhard → 5; kayaking → 6; merge_two_lists → 2.5; MIT ps1 1-4 → 2.6; MIT ps0 0-6 → 2.3).
21. Bloom levels and concept tags: AI-judged.
22. `ai`: model id and effort per part; `built` the ISO date.

## Exercise count report (root item 13)

Counted from `dossiers/ch02.md` and `judgements/ch02.md`, with excluded sources removed and held items moved. Proposed new: none (decision 4).

- **Check** (OpenDSA multiple choice and true/false, LibreTexts review): 37 printed and keyed (2.1: OpenDSA 6, Busbee 10 true/false; 2.2: 6; 2.5: 14, one of them parameterised; 2.6: 1). Available as `choice` and `number` once converted. The judge notes that OpenDSA's list questions use a current-position list model this book does not teach (2.1), and that its array list never resizes (2.2). Busbee's short-answer items are unkeyed and not counted.
- **Trace** (OpenDSA JSAV proficiency exercises: array-list insert and remove, linked-list insert and remove): 4 printed and keyed (2.2: 2; 2.5: 2); available only after they are rebuilt as figures with the `sequence` or `pick` answer types.
- **Exercise** (written): 3 printed, all unkeyed (ODS 2.1 on the stale value after remove, 2.2 on repeated add for addAll, 3.1 on why a dummy cannot remove every SLList special case); all three are explain; available only with AI solutions.
- **Code** (implement against tests):
  - with source tests: 22 (Exercism 12: list-ops, matrix, transpose, saddle-points, spiral-matrix, reverse-string, sublist, pythagorean-triplet, series, largest-series-product, simple-linked-list, linked-list; Interactive Coding Challenges 9: linked_list, kth_to_last_elem, palindrome, partition, remove_duplicates, delete_mid, add_reverse, find_loop_start, longest_substr_k_distinct; ICPC documentdimensions 1). References run and passing: 7 (Exercism list-ops, series, simple-linked-list, linked-list; icc linked_list, find_loop_start, longest_substr_k_distinct). The other 15 have no reference run yet and need one (Exercism ships none in the cache; the judge's AI reference passed largest-series-product). Available once the `code` answer type exists.
  - statement, no tests: 16 (ODS 14: Exercises 1.6, 1.7, 2.5, 3.2–3.4, 3.5–3.12; CIU 2: "implement a vector", "implement a linked list"); available with the ODS harness where it covers the task (listtest.py, test_arraystack, test_sllist, test_dllist, which pass under the shims) or with AI tests and an AI reference.
  - samples only (Kattis, ICPC): 16 (2.1: 1; 2.3: 7; 2.4: 6; 2.5: 2), no reference on file except the two ICPC Rocky Mountain packages (tiredterry, slidecount), whose accepted submissions pass their samples. Available only with AI tests. The judge flags nsum as trivial and freefood's small bounds as letting a naive solution pass.
  - test cases whose only statement is a docstring (TheAlgorithms, keon, tryalgo): 17 ranked first or second by the judge, all passing their doctests or tests. Under METHOD §6.3 these are test cases for a printed statement, not exercises; whether a docstring may serve as the statement is for the user.
- **NC cards**: 4 keyed (MIT 6.006 S20 ps1 1-2, prob1 1-3, ps3 3-5 with tests, ps1 1-4 with tests), 1 statement-only (Project Euler 8).
- **Concepts with no open exercise**: pointer-arithmetic (only CIU's checklist names it), pointer-to-pointer, difference-array-2d, cycle-start-proof (written by nature, none found); thin: prefix-sums-2d (keon test cases only, whose reference is not a prefix-sum solution), difference-array (one Kattis item, samples only), linked-list-vs-array (one check), sentinel-node (one written).

**The choice the user must make**, per kind (or per section):

- Check: take the 37, or drop the OpenDSA items whose model differs (2.1's current-position list, 2.2's fixed-size list).
- Trace: wait for the rebuilt proficiency figures, or leave the 4 out for now.
- Exercise: key only (the 3 left out and named in `exercise_notes`) or AI solutions for the 3.
- Code: (a) source tests only — the 22, with AI references where none is on file; (b) also the 16 statements with the ODS harness or AI tests; (c) also the 16 sample-only items with AI tests; and whether docstring-only test sets may stand as exercises.
- NC cards: include (keyed only, or with Project Euler 8 too) or leave out.
- New exercises: decision 4 rules them out; reopen only for the concepts listed above.
