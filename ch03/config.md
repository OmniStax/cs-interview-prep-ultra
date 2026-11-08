# Chapter 3 config: Stacks, queues and deques

Status: **proposed, not agreed** (2026-11-08). One setting per line (root item 10). The loop begins only after the user agrees this list and makes the exercise choice at the end; no default is assumed.

1. Chapter: 3 Stacks, queues and deques, folder `ch03`, sections 3.1–3.6, 24 concepts (`exploration.md`).
2. Start point: 3.1, then in order to 3.6.
3. Loop: one section per page, a stop after each (root item 2); each plan reviewed before building (root item 5).
4. Sources per concept: `judgements/ch01-03-reconciled.md` (final table, chapter 3); per-block `data-source` and `data-locator` as in `exploration.md`.
5. Folds: cpa `dynamic_programming/zero_matrix` into 3.4's home; nothing else.
6. Translation: none.
7. Runnable code: cpa's C++ shown as printed; the Python counterparts listed in `exploration.md` (all MIT); ODS Python under the shims, and the AI-made port for RootishArrayStack and SEList, marked.
8. Bridges: B11, B12, B13, B14a, B14b, B15 in the leads; B18 as links. 3.2's lead may overflow 80 words and goes back to the user if it does.
9. Errata: notes 22–30 as correction footnotes; 31 not noted in the first pass.
10. Leads: the tier (3.1–3.4 Essential with dual-array-deque and largest-zero-submatrix Advanced; 3.5 Advanced with RPN Essential; 3.6 Advanced with rootish-index-math Beyond), indexing, bridges.
11. Objectives, summaries, chapter introduction and summary pages: none.
12. Figures: the nine Sims of `exploration.md` as seeds; source figures behind the original toggle; Sim or photograph labels only, pending the RULES ruling.
13. Code beside the visual: every procedure figure; none in sim-rootish (a property and a growth plot).
14. Depth: 2D throughout.
15. Extra simulations: none beyond the seeds until the plans.
16. Colour: types `index`, `key`, `cost`, `size`; code variables as referents.
17. Derivations: the candidates in `exploration.md`, scored in their plans.
18. References item: at most three CIU links per section (the two Sambol "in 3 minutes" videos are candidates for 3.1 and 3.2; licence unreadable, so link only).
19. Exercise placement: end exercises to the Exercises system; held items as in `exploration.md`.
20. Rejected exercises: icc stack_min (fails a repeated minimum) and icc queue_from_stacks (Θ(n²) on alternating operations) are not used as they stand.
21. Bloom levels and concept tags: AI-judged.
22. `ai`: model id and effort per part; `built` the ISO date.

## Exercise count report (root item 13)

Counted from `dossiers/ch03.md` and `judgements/ch03.md`, with excluded sources removed and held items moved. Proposed new: none (decision 4).

- **Check** (OpenDSA multiple choice and checkpoints): 61 printed and keyed (3.1: 8 multiple choice and 15 checkpoint files; 3.2: 8 and 30). Available as `choice` once converted; the judge notes they live in JSAV pages and must be ported.
- **Trace**: 30 printed and keyed, 29 here: OpenDSA proficiency exercises 10 (3.1: 4 push/pop; 3.2: 4 enqueue/dequeue; 3.5: infix-to-postfix and postfix evaluation, the latter unpublished upstream) and Wikibooks A-level traces 20 (3.1: 7; 3.2: 8, one held for chapter 9; 3.5: 5). The Wikibooks items are available now as `open` with the key as solution (or `number` where the answer is one pointer value); the OpenDSA ones need rebuilding as figures with `sequence`.
- **Exercise** (written): 6 printed, all unkeyed: ODS Exercises 1.2 (Dyck words, prove), 1.3 (matched string in O(n), explain), 1.4 (reverse a stack with a queue, explain), 3.17 (SEList as a stack, prove); Njoroge's assessment 2 (explain). Available only with AI solutions.
- **Code** (implement against tests):
  - with source tests: 9 (Exercism 4: matching-brackets, circular-buffer, forth, wordy; Interactive Coding Challenges 5: stack, set_of_stacks, n_stacks, sort_stack, queue_list), plus Exercism simple-linked-list and linked-list reused from chapter 2 as the stack and deque exercises, plus the 2 rejected icc items. References run and passing: Exercism matching-brackets, circular-buffer (its example cannot store 0 and is not a model reference), forth; icc queue_list. Not run: wordy (the judge calls it not a stack exercise), icc stack, set_of_stacks, n_stacks, sort_stack. Available once the `code` answer type exists.
  - ODS harness (tests for the ODS structure, the ODS section as the only statement): 5 (ArrayQueue, ArrayDeque, DualArrayDeque pass under the shims; RootishArrayStack and SEList pass only with the AI-made port).
  - statement, no tests: 19 (ODS 14: Exercises 1.1 in three parts, 2.3, 2.4, 2.6, 2.8 (may move to chapter 7), 2.9, 2.10–2.13, 3.14, 3.15, 3.16, 3.18; SICP 3.21–3.23, 3, written for Scheme; CIU 2, the queue checklists). Available with AI tests and an AI reference, or with the ODS harness where it applies; the judge ranks ODS 3.14 (MinStack) as the statement for TheAlgorithms' min/max stack tests and ODS 3.15–3.16 (MinQueue, MinDeque) as the only minimum-queue statements.
  - samples only (Kattis, ICPC): 16 here (3.1: 9; 3.2: 1; 3.3: 2; 3.4: 1; 3.5: 3), 3 held. No reference on file; two are ICPC packages (gcpc2023 loopinvariant, gcpc2021 harbour2) whose secret data can be fetched and which carry accepted submissions. Available only with AI tests (or after fetching the ICPC data).
  - test cases whose only statement is a docstring (TheAlgorithms, keon, tryalgo): about 15 ranked by the judge, passing; the same question as in chapter 2.
- **NC cards**: 13 keyed (*pythonds* self-checks 12: 3.1 six, 3.5 six; MIT 6.006 S20 prob1 1-3, 3.3), 16 unkeyed (*pythonds* end-of-chapter exercises: 3.1 two, 3.2 four, 3.3 two, 3.5 eight).
- **Concepts with no open exercise**: rootish-index-math, sqrt-space-lower-bound. Thin: monotonic-queue-minimum (the minimum variant only as ODS's written 3.15–3.16; the tested ones are maximum variants), largest-zero-submatrix (one tested exercise, whose test must compare the area only), selist-spread-gather (one written proof), dual-array-deque (the harness and ODS 2.6).

**The choice the user must make**, per kind (or per section):

- Check: take the 61 after porting, or the judge's ranked first per concept only.
- Trace: the 19 Wikibooks traces now as `open`, and the OpenDSA proficiency exercises later as figures; or wait for `sequence` for all.
- Exercise: key only (the 6 left out and named) or AI solutions.
- Code: (a) source tests only (the 9 and the 2 reused); (b) also the ODS harness items; (c) also the 19 statements with AI tests; (d) also the 16 sample-only items with AI tests, or only the two ICPC ones once their data is fetched; whether docstring-only test sets stand as exercises; and whether the two rejected icc items come back with an AI reference and a duplicates test.
- NC cards: keyed only, keyed and unkeyed with AI solutions, or none.
- New exercises: decision 4 rules them out; reopen only for the concepts listed above.
