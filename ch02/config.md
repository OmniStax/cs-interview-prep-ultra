# Chapter 2 config: Arrays and linked lists

Status: **agreed** (2026-11-08, METHOD §4.4 decision 19: every recommendation accepted). One setting per line (root item 10). The loop may begin; the exercise choice is at the end.

1. Chapter: 2 Arrays and linked lists, folder `ch02`, sections 2.1–2.7, 26 concepts (`exploration.md`).
2. Start point: 2.3 first if the app's trace engine and code runner are ready (the book's first template), else 2.2 first; then the rest in order (decision 19, `RULES.md`, Template sections).
3. Loop: one section per page, a stop after each (root item 2); each plan reviewed before building (root item 5).
4. Sources per concept: `judgements/ch01-03-reconciled.md` (final table, chapter 2); per-block `data-source` and `data-locator` as in `exploration.md`.
5. Folds: OI Wiki two-pointer and prefix-sum pages split over 2.3 and 2.4 as listed; nothing else folded.
6. Translation: the six OI Wiki blocks of 2.3 and 2.4 (≈1,830 words), AI-marked as translations; OI Wiki code never copied; a 例题 that restates a LeetCode problem becomes a link.
7. Runnable code where the winner's is unlicensed or not runnable: TheAlgorithms (MIT) for two pointers and prefix sums; doocs code (CC BY-SA, decision 18) for the product window (0713), 2D prefix sums (0304) and the difference array (0370); credited per block.
8. ODS Python: run through the shims of `judgements/ch01-03-references.md` (no edit to ODS files).
9. Bridges: B6, B7, B8, B9, B10, B16, B17 in the leads; 2.3's lead may overflow 80 words, and if it does the bridge goes back to the user (decision 19).
10. Errata: notes 15, 16, 18, 19, 20 as correction footnotes; note 17 ("C29") only after a person checks it.
    **Open: C29 check.** A person checks Wikipedia Pointer's "declared obsolescent as of C29" before 2.1 is built (decision 19).
11. Leads: the tier (all Essential; 2.2 block-copy Advanced; 2.4's 2D concepts Advanced), the indexing convention per section, the bridges.
12. Objectives, summaries, chapter introduction and summary pages: none.
13. Figures: the ten Sims of `exploration.md` as seeds; source figures behind the original toggle; Sim or photograph labels only, no figure numbers (decision 19).
14. Code beside the visual: every procedure figure (sim-arraystack, sim-two-pointers, sim-merge, sim-variable-window, sim-linked-list, sim-dllist, sim-rho); none in sim-address (a property), sim-moving-window and sim-prefix (formulas).
15. Depth: 2D throughout.
16. Extra simulations: none beyond the seeds until the plans.
17. Colour: types `index`, `key`, `cost`, `size`; the named code variables as referents, the `index` colour for unnamed positions (`COLOR.md` §3, decision 19).
18. Derivations: the candidates in `exploration.md`, scored in their plans.
19. References item: at most three CIU links per section.
20. Exercise placement: end exercises to the Exercises system; no inline Try Its; a figure's predict pause is a figure control only (decision 19). Held items as in `exploration.md` (ODS 2.7 → 3.3; subseqhard → 5; kayaking → 6; merge_two_lists → 2.5; MIT ps1 1-4 → 2.6; MIT ps0 0-6 → 2.3; Exercism simple-linked-list → 3.1; Exercism linked-list → 3.3; MIT prob1 1-3 → 3.3). An item that tests concepts of two sections goes with the later one.
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
  - test cases whose only statement is a docstring (TheAlgorithms, keon, tryalgo): 17 ranked first or second by the judge, all passing their doctests or tests. They are test sources, not exercises (decision 19): used only as the tests of a printed statement.
- **NC cards**: 4 keyed (MIT 6.006 S20 ps1 1-2, prob1 1-3, ps3 3-5 with tests, ps1 1-4 with tests), 1 statement-only (Project Euler 8).
- **Concepts with no open exercise**: pointer-arithmetic (only CIU's checklist names it), pointer-to-pointer, difference-array-2d, cycle-start-proof (written by nature, none found); thin: prefix-sums-2d (keon test cases only, whose reference is not a prefix-sum solution), difference-array (one Kattis item, samples only), linked-list-vs-array (one check), sentinel-node (one written).

## The exercise choice (decision 19)

Per kind: **check** items, the judge's top three ranked entries per concept; **trace** items wait for the `sequence` answer type (the 4 OpenDSA proficiency exercises are deferred); **written** items keyed only, at most about five per concept (all 3 here are unkeyed, so none ships; they are named in `exercise_notes`); **code** items with source tests or Exercism track tests now, Kattis or ICPC with AI tests only where the judge rated the fit good (none in this chapter: the judge rates no Kattis or ICPC item good here, flags nsum as trivial and freefood's bounds, and notes the rest as samples only), at most two code items per concept; **NC cards** keyed only (Project Euler 8 is statement-only and left out). A docstring-only test file is a test source, never an exercise; it ships only as the tests of a printed statement. New exercises: none (decision 4).

The OpenDSA check items whose model the book does not teach (2.1's current-position list, 2.2's fixed-size array list) are read one by one at the plan: an item that needs that model is left out and named in `exercise_notes`.

| § | concept | check | code | NC cards (keyed) |
|---|---|---|---|---|
| 2.1 | array | lt-busbee 6.17 true/false | ODS Exercise 2.5, `rotate(a, r)` (ODS's statement; tests: keon TestRotateArray and TheAlgorithms `rotate_array.py` doctests, both passing); exercism matrix (canonical data; an AI reference is needed, Exercism ships none in the cache) | none |
| 2.1 | pointer-arithmetic | none | none | none |
| 2.1 | list-interface | opendsa List MCQs (current-position model: read per item) | ODS Exercise 1.6 with ODS `listtest.py` (passes under the shims); exercism list-ops (29 cases, the judge's weaker fit; the Exercism example passes) | 6.006 S20 ps1 1-2 |
| 2.2 | dynamic-array | none | none (CIU "Implement a vector" has no source tests; TheAlgorithms `dynamic_array.py` and the ODS ArrayStack harness have no printed statement) | none |
| 2.2 | array-resize | none | none (as dynamic-array) | none |
| 2.2 | dynamic-array-cost | opendsa AL MCQs (fixed-size array list: read per item) | none | none here (6.006 S20 prob1 1-3 → 3.3) |
| 2.2 | block-copy | none | none (ODS `test_fastarraystack.py` has no statement; ODS Exercise 2.7 → 3.3) | none |
| 2.2 | implement-vector | none | none (as dynamic-array) | none |
| 2.3 | two-pointers | none | exercism reverse-string (9 cases) | 6.006 S20 ps0 0-6 (`count_long_subarray`, with its tests; tagged with 1.4's complexity-analysis) |
| 2.3 | three-sum | none | none (keon and TheAlgorithms are test sources with no printed statement) | none |
| 2.3 | merge-sorted-sequences | none | none (TheAlgorithms and tryalgo test sources only; kattis cd not rated) | none |
| 2.3 | sliding-window-fixed | none | exercism series (11 cases); exercism largest-series-product (18 cases; keep only the latest version of each case) | 6.006 S20 ps3 3-5 (`count_anagram_substrings`, with its tests) |
| 2.3 | sliding-window-variable | none | icc `recursion_dynamic/longest_substr_k_distinct` (its solution notebook passes the 4 asserts) | none |
| 2.4 | prefix-sums | none | none (TheAlgorithms test sources only; Kattis items not rated) | none |
| 2.4 | prefix-sums-2d | none | none | none |
| 2.4 | difference-array | none | none (kattis freefood flagged) | none |
| 2.4 | difference-array-2d | none | none | none |
| 2.5 | singly-linked-list | none | icc `linked_lists/linked_list` (16 asserts, solution passes; tagged with implement-linked-list) | none |
| 2.5 | pointer-to-pointer | none | none | none |
| 2.5 | implement-linked-list | none | icc `linked_list` (above) | none |
| 2.5 | linked-list-vs-array | opendsa ListOverhead (parameterised: one fixed instance) | none | none |
| 2.6 | doubly-linked-list | opendsa ListTFdblimpl | none here (Exercism linked-list → 3.3; ODS Exercises 3.5–3.12 need AI tests) | 6.006 S20 ps1 1-4 (with its tests) |
| 2.6 | sentinel-node | none | none | none |
| 2.7 | floyd-cycle-detection | none | icc `find_loop_start` (below, tagged with both) | none |
| 2.7 | cycle-start | none | icc `linked_lists/find_loop_start` (5 asserts, solution passes) | none |
| 2.7 | cycle-start-proof | none | none | none |

Written items left out (unkeyed): ODS Exercises 2.1, 2.2, 3.1. Code items left out under this choice and named in `exercise_notes`: the statements without source tests (ODS Exercises 1.7, 3.2–3.12; CIU's two checklists), Exercism spiral-matrix, transpose, saddle-points, sublist and pythagorean-triplet (over the cap or unranked), and every Kattis and ICPC item.
