# Chapter 3 config: Stacks, queues and deques

Status: **agreed** (2026-11-08, METHOD §4.4 decision 19: every recommendation accepted). One setting per line (root item 10). The loop may begin; the exercise choice is at the end.

1. Chapter: 3 Stacks, queues and deques, folder `ch03`, sections 3.1–3.6, 24 concepts (`exploration.md`).
2. Start point: 3.1, then in order to 3.6.
3. Loop: one section per page, a stop after each (root item 2); each plan reviewed before building (root item 5).
4. Sources per concept: `judgements/ch01-03-reconciled.md` (final table, chapter 3); per-block `data-source` and `data-locator` as in `exploration.md`.
5. Folds: cpa `dynamic_programming/zero_matrix` into 3.4's home; nothing else.
6. Translation: none.
7. Runnable code: cpa's C++ shown as printed; the Python counterparts listed in `exploration.md` (all MIT); ODS Python under the shims, and the AI-made port for RootishArrayStack and SEList, marked.
8. Bridges: B11, B12, B13, B14a, B14b, B15 in the leads; B18 as links. 3.2's lead may overflow 80 words, and if it does the bridge goes back to the user (decision 19).
9. Errata: notes 22–30 as correction footnotes; 31 not noted in the first pass.
10. Leads: the tier (3.1–3.4 Essential with dual-array-deque and largest-zero-submatrix Advanced; 3.5 Advanced with RPN Essential; 3.6 Advanced with rootish-index-math Beyond), indexing, bridges.
11. Objectives, summaries, chapter introduction and summary pages: none.
12. Figures: the nine Sims of `exploration.md` as seeds; source figures behind the original toggle; Sim or photograph labels only, no figure numbers (decision 19).
13. Code beside the visual: every procedure figure; none in sim-rootish (a property and a growth plot).
14. Depth: 2D throughout.
15. Extra simulations: none beyond the seeds until the plans.
16. Colour: types `index`, `key`, `cost`, `size`; named code variables as referents, the `index` colour for unnamed positions (decision 19).
17. Derivations: the candidates in `exploration.md`, scored in their plans.
18. References item: at most three CIU links per section (the two Sambol "in 3 minutes" videos are candidates for 3.1 and 3.2; licence unreadable, so link only).
19. Exercise placement: end exercises to the Exercises system; no inline Try Its; a figure's predict pause is a figure control only (decision 19). Held items as in `exploration.md`; from chapter 2: Exercism simple-linked-list → 3.1, Exercism linked-list → 3.3, MIT 6.006 S20 prob1 1-3 (NC) → 3.3.
20. Rejected exercises: icc stack_min (fails a repeated minimum) and icc queue_from_stacks (Θ(n²) on alternating operations) stay out (decision 19).
21. Bloom levels and concept tags: AI-judged.
22. `ai`: model id and effort per part; `built` the ISO date.

## Exercise count report (root item 13)

Counted from `dossiers/ch03.md` and `judgements/ch03.md`, with excluded sources removed and held items moved. Proposed new: none (decision 4).

- **Check** (OpenDSA multiple choice and checkpoints): 61 printed and keyed (3.1: 8 multiple choice and 15 checkpoint files; 3.2: 8 and 30). Available as `choice` once converted; the judge notes they live in JSAV pages and must be ported.
- **Trace**: 30 printed and keyed, 29 here: OpenDSA proficiency exercises 10 (3.1: 4 push/pop; 3.2: 4 enqueue/dequeue; 3.5: infix-to-postfix and postfix evaluation, the latter unpublished upstream) and Wikibooks A-level traces 20 (3.1: 7; 3.2: 8, one held for chapter 9; 3.5: 5). The Wikibooks items could ship as `open` with the key as solution (or `number` where the answer is one pointer value), and the OpenDSA ones need rebuilding as figures with `sequence`; under decision 19 all trace items wait for `sequence`.
- **Exercise** (written): 6 printed, all unkeyed: ODS Exercises 1.2 (Dyck words, prove), 1.3 (matched string in O(n), explain), 1.4 (reverse a stack with a queue, explain), 3.17 (SEList as a stack, prove); Njoroge's assessment 2 (explain). Available only with AI solutions.
- **Code** (implement against tests):
  - with source tests: 9 (Exercism 4: matching-brackets, circular-buffer, forth, wordy; Interactive Coding Challenges 5: stack, set_of_stacks, n_stacks, sort_stack, queue_list), plus Exercism simple-linked-list and linked-list reused from chapter 2 as the stack and deque exercises, plus the 2 rejected icc items. References run and passing: Exercism matching-brackets, circular-buffer (its example cannot store 0 and is not a model reference), forth; icc queue_list. Not run: wordy (the judge calls it not a stack exercise), icc stack, set_of_stacks, n_stacks, sort_stack. Available once the `code` answer type exists.
  - ODS harness (tests for the ODS structure, the ODS section as the only statement): 5 (ArrayQueue, ArrayDeque, DualArrayDeque pass under the shims; RootishArrayStack and SEList pass only with the AI-made port).
  - statement, no tests: 19 (ODS 14: Exercises 1.1 in three parts, 2.3, 2.4, 2.6, 2.8 (may move to chapter 7), 2.9, 2.10–2.13, 3.14, 3.15, 3.16, 3.18; SICP 3.21–3.23, 3, written for Scheme; CIU 2, the queue checklists). Available with AI tests and an AI reference, or with the ODS harness where it applies; the judge ranks ODS 3.14 (MinStack) as the statement for TheAlgorithms' min/max stack tests and ODS 3.15–3.16 (MinQueue, MinDeque) as the only minimum-queue statements.
  - samples only (Kattis, ICPC): 16 here (3.1: 9; 3.2: 1; 3.3: 2; 3.4: 1; 3.5: 3), 3 held. No reference on file; two are ICPC packages (gcpc2023 loopinvariant, gcpc2021 harbour2) whose secret data can be fetched and which carry accepted submissions. Available only with AI tests (or after fetching the ICPC data).
  - test cases whose only statement is a docstring (TheAlgorithms, keon, tryalgo): about 15 ranked by the judge, passing. Test sources, not exercises (decision 19): used only as the tests of a printed statement.
- **NC cards**: 7 keyed (*pythonds* self-checks 6: 3.1 three, 3.5 three, of which two ship, as the cache holds three per page and not six (corrected in the chapter 2–3 pass); MIT 6.006 S20 prob1 1-3, 3.3), 16 unkeyed (*pythonds* end-of-chapter exercises: 3.1 two, 3.2 four, 3.3 two, 3.5 eight).
- **Concepts with no open exercise**: rootish-index-math, sqrt-space-lower-bound. Thin: monotonic-queue-minimum (the minimum variant only as ODS's written 3.15–3.16; the tested ones are maximum variants), largest-zero-submatrix (one tested exercise, whose test must compare the area only), selist-spread-gather (one written proof), dual-array-deque (the harness and ODS 2.6).

## The exercise choice (decision 19)

Per kind: **check** items, the judge's top three ranked entries per concept (the OpenDSA items live in JSAV pages and are ported; only their multiple-choice items are check items); **trace** items wait for the `sequence` answer type (the 10 OpenDSA proficiency exercises and the 20 Wikibooks A-level traces are deferred); **written** items keyed only, at most about five per concept (all 6 here are unkeyed, so none ships); **code** items with source tests or Exercism track tests now, Kattis or ICPC with AI tests only where the judge rated the fit good, at most two code items per concept; **NC cards** keyed only. A docstring-only test file is a test source, never an exercise. New exercises: none (decision 4).

The judge's fit, as read for Kattis and ICPC here: good where its note says so without a caveat (delimitersoup "a good variant", integerlists "a good applied exercise", bracketsequence "a good stack drill", calculator "serves both concepts", throwns "a nice stack use", backspace "a clear statement"); not good where it is flagged ("less direct": evenup, pairingsocks, gcpc2021 harbour2; "contest level": gcpc2023 loopinvariant), deferred, stretch with a dependency (brackets, teque, bungeebuilder), or noted only as samples (bracketmatching, circuitmath, ferryloading4). throwns and backspace are over the cap of 3.1's stack, which has two source-tested items.

| § | concept | check | code | NC cards (keyed) |
|---|---|---|---|---|
| 3.1 | stack | opendsa stack MC questions (the multiple-choice items of the judge's rank-8 entry) | exercism simple-linked-list (29 cases; the Exercism example passes; from 2.5); icc `stacks_queues/stack` (12 asserts; its reference is run before it ships) | pythonds self-checks, 3.1's three (the cache holds three, not six; chapter 2–3 pass) |
| 3.1 | balanced-brackets | none | none (ODS intro exc-2 unkeyed; kattis brackets and gcpc2023 loopinvariant not rated good) | none |
| 3.1 | bracket-validation | none | exercism matching-brackets (20 cases; the Exercism example passes; trekhleb's 12 expects not used: they contradict Exercism's statement (3.1's build; chapter 2–3 pass), so the JavaScript runs Exercism's cases); kattis delimitersoup (CC BY-SA 3.0, AI tests) | none |
| 3.2 | queue | opendsa StackQMCQ q* (8 MC) | none (kattis ferryloading4 not rated) | none |
| 3.2 | circular-buffer | none | exercism circular-buffer (14 cases; the Exercism example cannot store 0, so the shipped reference is AI-written and marked) | none |
| 3.2 | queue-linked-list | none | icc `stacks_queues/queue_list` (5 asserts, reference passes; an AI test adds dequeue-to-empty-then-enqueue, marked) | none |
| 3.2 | array-queue | none | none (the ODS harness has no printed statement; ODS exc-3 RandomQueue needs AI tests) | none |
| 3.3 | deque | none | exercism linked-list (19 cases; the Exercism example passes, though it raises on "not found"; from 2.6, tagged with doubly-linked-list); kattis integerlists (CC BY-SA 3.0, AI tests) | 6.006 S20 prob1 1-3 (from 2.2, tagged with dynamic-array-cost) |
| 3.3 | array-deque | none | none (ODS exc-6, 8, 9 and ODS Exercise 2.7 from 2.2 need AI tests) | none |
| 3.3 | dual-array-deque | none | none (harness only) | none |
| 3.4 | min-stack | none | ODS Exercise 3.14 (MinStack) with TheAlgorithms `stack_tracking_min_max.py` doctests as its tests, less the two that fix its quirks (default size 10, −inf on empty) | none |
| 3.4 | queue-from-two-stacks | none | none (TheAlgorithms and tryalgo are test sources with no printed statement; icc queue_from_stacks rejected) | none (6.046J S15 4-1 is in 1.5) |
| 3.4 | monotonic-queue-minimum | none | none (ODS exc-15, 16 need AI tests) | none |
| 3.4 | sliding-window-minimum | none | none (maximum-variant test sources only) | none |
| 3.4 | nearest-smaller-element | none | none (test sources only; kattis bungeebuilder stretch) | none |
| 3.4 | largest-zero-submatrix | none | cp-algorithms' own problem sentence ("Find the largest submatrix consisting of only zeros", origin `cpa`) with tryalgo `rectangles_from_grid` tests, comparing the area only and passing `black=0`; AI tests add the all-ones, all-zeros, 1×m and n×1 grids, marked | none |
| 3.5 | rpn-evaluation | none | exercism forth (55 cases; the cases on user-defined words are a stretch part) | pythonds self-checks, 3.5's three, of which two ship (postfix1, postfix2; the cache holds three, not six; chapter 2–3 pass) |
| 3.5 | expression-parsing | none | kattis calculator (CC BY-SA 3.0, AI tests; tagged with unary-right-assoc); kattis bracketsequence (CC BY-SA 3.0, AI tests) | none |
| 3.5 | unary-right-assoc | none | kattis calculator (above) | none |
| 3.6 | rootish-array-stack, rootish-index-math, sqrt-space-lower-bound, space-efficient-list, selist-spread-gather | none | none (harness only, or ODS exc-10–13, 17, 18 unkeyed or needing AI tests) | none |

Left out and named in `exercise_notes`: the 6 unkeyed written items; the statements without source tests (ODS 14, SICP 3, CIU 2); the ODS harness items with no printed statement; the Kattis and ICPC items not rated good or over the cap; the two rejected icc items; the 16 unkeyed *pythonds* exercises.
