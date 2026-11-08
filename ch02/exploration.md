# Chapter 2 exploration: Arrays and linked lists

Status: **agreed**, 2026-11-08 (METHOD §4.4 decision 19). Nothing is built. Written from `concept-map/toc.md` and `concepts.json` (chapter `ch-arrays-lists`), `dossiers/ch02.md`, `judgements/ch02.md`, `judgements/ch01-03-reconciled.md`, `judgements/ch01-03-references.md` and METHOD §4.4. Every locator is the reconciled winner's.

## What the chapter is

Seven sections, 26 concepts (23 Essential, 3 Advanced). Two sections came from the gap inventory (2.3 and 2.4: the interview patterns no spine source teaches). It rests only on chapter 1 (cost, amortized analysis, the List interface's vocabulary of 1.1) and is the first chapter where every section has code to run.

| § | Title | Tier | Concepts (tier where it differs) |
|---|---|---|---|
| 2.1 | Arrays and the list interface | Essential | array, pointer-arithmetic, list-interface |
| 2.2 | Dynamic arrays | Essential | dynamic-array, array-resize, dynamic-array-cost, block-copy (Advanced), implement-vector |
| 2.3 | Two pointers and sliding windows | Essential | two-pointers, three-sum, merge-sorted-sequences, sliding-window-fixed, sliding-window-variable |
| 2.4 | Prefix sums and difference arrays | Essential | prefix-sums, prefix-sums-2d (Advanced), difference-array, difference-array-2d (Advanced) |
| 2.5 | Singly linked lists | Essential | singly-linked-list, pointer-to-pointer, implement-linked-list, linked-list-vs-array |
| 2.6 | Doubly linked lists | Essential | sentinel-node, doubly-linked-list |
| 2.7 | Cycles in linked lists: tortoise and hare | Essential | floyd-cycle-detection, cycle-start, cycle-start-proof |

## Provenance: every block and its source

| § | block | concept | `data-source` | `data-locator` | licence | note |
|---|---|---|---|---|---|---|
| 2.1 | `array` | array | wikipedia | `wikipedia:Array_(data_structure)` lead + #Element identifier and addressing formulas (intro, ===One-dimensional arrays===, ===Multidimensional arrays===) + #Efficiency + the Iliffe-vector paragraph of ===Comparison with other data structures=== | CC BY-SA 4.0 | several blocks, one per heading |
| 2.1 | `pointer-arithmetic` | pointer-arithmetic | wikipedia | `wikipedia:Pointer_(computer_programming)#C arrays` | CC BY-SA 4.0 | the "C29" sentence needs a human check |
| 2.1 | `list-interface` | list-interface | ods | `ods:intro#the-list-interface-linear-sequences` (whole subsection, fig. list) | CC BY 2.5 CA | the List subsection of the §Interfaces whose opening is 1.1's |
| 2.2 | `dynamic-array` | dynamic-array | ods | `ods:arrays#chap:arrays` opening (table, three bullets, amortized paragraph) + `#sec:arraystack` opening + "The Basics" | CC BY 2.5 CA | |
| 2.2 | `resize` | array-resize | ods | `ods:arrays#growing-and-shrinking`, first two paragraphs | CC BY 2.5 CA | |
| 2.2 | `arraystack-cost` | dynamic-array-cost | ods | `ods:arrays#growing-and-shrinking` from "The running time analysis from the previous section ignored…" through `lem:arraystack-amortized` and proof, + "Summary" (`thm:arraystack`) | CC BY 2.5 CA | |
| 2.2 | `fastarraystack` | block-copy | ods | `ods:arrays#sec:fastarraystack` (whole) | CC BY 2.5 CA | |
| 2.2 | — | implement-vector | ods | the ArrayStack class as shown in the blocks above | CC BY 2.5 CA | no prose block of its own; the concept's span is the ArrayStack code |
| 2.3 | `two-pointers` | two-pointers | oiwiki | `oiwiki:misc/two-pointer#引入` + `#利用序列有序性` (过程 only) | CC BY-SA 4.0 + SATA | **translated** (≈330 words); 1-based |
| 2.3 | `three-sum` | three-sum | wikipedia | `wikipedia:3SUM` lead, first sentence + #Quadratic algorithm | CC BY-SA 4.0 | 0-based S[0..n−1] |
| 2.3 | `merge` | merge-sorted-sequences | wikipedia | `wikipedia:Merge_algorithm#Merging two lists` | CC BY-SA 4.0 | |
| 2.3 | `fixed-window` | sliding-window-fixed | wikipedia | `wikipedia:Moving_average#Simple moving average`, opening to "…only 3 arithmetic steps." | CC BY-SA 4.0 | stops before the confused "k = n" sentence |
| 2.3 | `variable-window` | sliding-window-variable | oiwiki | `oiwiki:misc/two-pointer#维护区间信息` opening + 例题 1 过程 | CC BY-SA 4.0 + SATA | **translated** (≈340); the 例题 statement, if LeetCode's, becomes a link |
| 2.4 | `prefix-sums` | prefix-sums | oiwiki | `oiwiki:basic/prefix-sum#引入` (with 规定 box) + `#前缀和` + `### 一维前缀和` | CC BY-SA 4.0 + SATA | **translated** (≈200); 1-based, a₀ = S₀ = 0 |
| 2.4 | `prefix-sums-2d` | prefix-sums-2d | oiwiki | `#### 基于容斥原理` (with 示例 and figure prefix-sum-2d) + `#### 逐维前缀和` | CC BY-SA 4.0 + SATA | **translated** (≈550) |
| 2.4 | `difference-array` | difference-array | oiwiki | `#差分` opening + `### 一维差分` (with 性质 box) | CC BY-SA 4.0 + SATA | **translated** (≈250) |
| 2.4 | `difference-array-2d` | difference-array-2d | oiwiki | `### 二维/多维差分` | CC BY-SA 4.0 + SATA | **translated** (≈160) |
| 2.5 | `singly-linked-list` | singly-linked-list | wikipedia | `wikipedia:Linked_list` lead + #Basic concepts and nomenclature + ===Singly linked list=== | CC BY-SA 4.0 | |
| 2.5 | `pointer-to-pointer` | pointer-to-pointer | wikipedia | `wikipedia:Pointer_(computer_programming)#Multiple indirection` | CC BY-SA 4.0 | the list-head case |
| 2.5 | `list-operations` | implement-linked-list | wikipedia | `wikipedia:Linked_list#Linked list operations` intro + ====Singly linked lists==== | CC BY-SA 4.0 | |
| 2.5 | `lists-vs-arrays` | linked-list-vs-array | wikipedia | `wikipedia:Linked_list#Linked lists vs. dynamic arrays` | CC BY-SA 4.0 | |
| 2.6 | `dummy-node` | sentinel-node | ods | `ods:linkedlists#sec:dllist`, opening through fig. dllist and the DLList() code | CC BY 2.5 CA | |
| 2.6 | `dllist` | doubly-linked-list | ods | `ods:linkedlists#sec:dllist` from getNode(i) through "Adding and Removing" and "Summary" | CC BY 2.5 CA | |
| 2.7 | `tortoise-hare` | floyd-cycle-detection | cpa | `cpa:others/tortoise_and_hare` intro + #proposed-algorithm ###Step 1 + #why-does-it-work ###Step 1 | CC BY-SA 4.0 | Java snippets |
| 2.7 | `cycle-start` | cycle-start | cpa | `#step-2-starting-point-of-the-cycle` (with both Java snippets) | CC BY-SA 4.0 | |
| 2.7 | `cycle-start-proof` | cycle-start-proof | cpa | `#step-2-starting-point-of-the-cycle_1` (with fig. tortoise_hare_proof) | CC BY-SA 4.0 | |

Source count: Wikipedia 9, ODS 8, OI Wiki 6, cpa 3. No doocs explanation wins.

**Folds** (from `toc.md`): OI Wiki's `misc/two-pointer` is split over 2.3 (its sorted-sequence and window sections); its linked-list section (Floyd) is not used, since cpa wins 2.7. OI Wiki's `basic/prefix-sum` is split over 2.4 by its four sections; its tree prefix sums and differences are not taken.

## Apparatus

- **Wikipedia** (2.1, 2.3, 2.5): wikitext; pseudocode (`node.next`, `insertAfter`), formulas, figures licensed per file (Singly-linked-list.svg PD, Dynamic array.svg CC0, ArrayListAmotizedPush.png CC0, Merge sort algorithm diagram and Moving average plot: licences in `dossiers/ch02.md`). Wikipedia's own figure captions are kept as `original_caption` where a figure is replaced.
- **ODS** (2.1, 2.2, 2.6): Java-like pseudocode with `#code#`, the fig. array, list, dllist and growth figures (`.ipe`), lemmas with proofs, "Summary" theorems. The ODS Python classes run on current Python only with shims (ArrayStack, FastArrayStack, SLList, DLList) and are the reference for the ODS harness tests.
- **OI Wiki** (2.3, 2.4): Markdown; formulas kept; code not copied. Runnable code beside the figures comes from TheAlgorithms (MIT: `maths/two_pointer.py`, `data_structures/arrays/prefix_sum.py`) and, for the product window, 2D prefix sums and difference arrays, doocs code (CC BY-SA, decision 18: 0713, 0304, 0370).
- **cpa** (2.7): Markdown, Java snippets, fig. tortoise_hare_proof.
- **Objectives, summaries, introductions**: none printed. ODS's ArrayStack and DLList "Summary" theorems stay in their blocks.

## Bridges

| id | where | what it carries |
|---|---|---|
| B6 | 2.2 lead, before `arraystack-cost` | 1.5 analysed growth only, by three methods, writing m for the capacity and n for the size; ODS writes n and `a.length`, and adds shrinking at a.length ≥ 3n |
| B7 | 2.1 lead, before `list-interface` | stacks, queues and deques come in 3.1–3.3; the Deque mapping in the List subsection is a preview |
| B8 | 2.2 lead | ArrayStack implements List; its name follows the naming rule at the end of 2.1's List passage |
| B9 | 2.3 lead, `three-sum` | the quadratic algorithm sorts first (sorting: chapter 10); the hash-table sentence points to chapter 5; the passage assumes distinct values |
| B10 | 2.6 lead | ODS calls the singly linked list of 2.5 an SLList, with fields head, tail and n |
| B16 | 2.3 lead, `fixed-window` | the example is a running mean; in the exercises the window holds a sum or a count |
| B17 | 2.6 lead | DLList's Summary names Deque operations (3.3) |

2.3's lead carries three things (B9, B16 and the mixed indexing); it may not fit 80 words. If not, the bridge goes back to the user (decision 19), never into the text.

## Errata to attach as correction notes

15. Wikipedia Array, ===One-dimensional arrays===: "B + 30c" should be "B − 30c".
16. Wikipedia Array, ===Multidimensional arrays===: 1-based labels a₁₁, a₁₂ on a 0-based C array.
17. Wikipedia Pointer: "declared obsolescent as of C29" — not verifiable from the cache; the next C revision's working name is C2y. **A person checks this before 2.1 is built.**
18. Wikipedia Pointer #Multiple indirection: the comment "where all earlier elements have lesser or equal value" is loose; the code is a correct sorted insert.
19. ODS `lem:arraystack-amortized`: "at least n_i/2" — the bound proved is n_i/2 − 1.
20. OI Wiki 2D prefix-sum example: the terms read S₂,₃ + S₃,₂ but the numbers are listed 18 + 15; per the figure S₂,₃ = 15 and S₃,₂ = 18 (the sum is unaffected).

(21, Moving average's "k = n" sentence, is outside the locator; no note.)

## Indexing, as each lead must state it

| § | convention |
|---|---|
| 2.1 | 0-based: Wikipedia Array and ODS List x₀ … x_{n−1} (Wikipedia's a₁₁ labels are erratum 16) |
| 2.2 | 0-based: ODS a[0..n−1] |
| 2.3 | mixed: OI Wiki two pointers and the variable window are 1-based (num[1..n], r − l + 1); Wikipedia 3SUM is 0-based (S[0..n−1]); the merge has no indices; the moving average uses time subscripts p_{n−k+1} … p_n |
| 2.4 | 1-based throughout, with a₀ = 0 and S₀ = 0 (OI Wiki's 规定 box, kept) |
| 2.5 | none: nodes and links |
| 2.6 | 0-based: ODS get(i), O(1 + min{i, n − i}) |
| 2.7 | none: step counts a, b, L |

The runnable code beside 2.3 and 2.4 (TheAlgorithms, doocs) is 0-based while the OI Wiki prose is 1-based. The figures draw indices the prose's way and the code panel the code's way, and the readout says which; or the figure shows a 1-based strip with a₀ = 0 drawn as a sentinel cell. The plans choose.

## Derivations (root item 29), candidates

| § | candidate |
|---|---|
| 2.1 | Wikipedia's address formula, address = B + c·i, and its 2D row-major form (short; likely below the bar) |
| 2.2 | ODS `lem:arraystack-amortized` and its proof (a printed proof; erratum 19 inside) |
| 2.4 | OI Wiki's inclusion–exclusion for S_{i,j} and its worked example (erratum 20 inside) |
| 2.7 | cpa's distance argument: a + b + kL = 2(a + b) ⇒ a = kL − b (printed as equations) |

## Exercises that belong elsewhere

- ODS Exercise 2.7 (needs ArrayDeque) → 3.3.
- Kattis subseqhard (needs a hash map) → chapter 5.
- Kattis kayaking (pairs from both ends, with a binary search on the answer) → chapter 6, unless its plan finds a two-pointer statement of it.
- keon and TheAlgorithms merge_two_lists (linked lists), ranked in 2.3 → 2.5.
- MIT 6.006 S20 ps1 1-4 (NC, doubly linked list) is ranked in 2.5 and 2.6 → 2.6.
- MIT 6.006 S20 ps0 0-6 (NC) is ranked for two-pointers and for 1.4's complexity-analysis; it goes with 2.3, and 1.4's notes say so.
- Exercism simple-linked-list (ranked for 2.5) tests a linked stack → 3.1; Exercism linked-list (ranked for 2.6) tests a doubly linked deque → 3.3 (an item goes with the later section of the concepts it tests, decision 19's choice in `config.md`).
- MIT 6.006 S20 prob1 1-3 (NC, ranked for 2.2's dynamic-array-cost) asks for a double-ended sequence → 3.3.

## The chapter's answer to root rule 23: what would make this stunning

This is the chapter where the figure and the code become one object. Every section has a procedure with a state, and every invariant can be shaded.

- **2.1, memory under the array.** A strip of cells over a row of byte addresses: the index slider moves the cell, the address B + c·i updates, the element size c widens every cell at once. A 2D array laid out row-major, the same cell found by the formula; Wikipedia's "B − 30c" erratum shown as the place the formula lands.
- **2.2, the ArrayStack doubling.** ODS's add(i, x) shifting n − i cells right, block by block ("make room", "shift", "store"); a resize copying into an array twice the size; remove shrinking when a.length ≥ 3n. The cost counter against ODS's amortised bound. Inputs: append only, insert at the front (the shifting cost), push and pop alternating at a capacity boundary (the case the 3n rule protects).
- **2.3, two pointers closing.** A sorted array, l and r walking in, the target sum in the readout, the invariant shaded: "no pair outside [l, r] sums to the target". A predict pause at each step: which pointer moves? 3SUM as an outer index with the same closing pair inside. The merge as two input strips feeding an output strip. The moving average as a window sliding over a time series, the sum updated by "add the new, drop the old" (3 steps) against recomputing k.
- **2.3, the variable window.** OI Wiki's 例题 1 stepped: r extends while the window stays valid, l advances when it does not, the window drawn as a bracket that stretches and shrinks, the count of each value shown under it; counter: each index enters and leaves once, ≤ 2n.
- **2.4, prefix sums as differences of areas.** The prefix-sum bars, a query [l, r] drawn as S_r − S_{l−1}; in 2D, OI Wiki's figure live, the four rectangles of inclusion–exclusion added and subtracted with their signs; the difference array as the inverse: a range add touches two cells, and the prefix sum spreads it back.
- **2.5, links re-aimed.** Insert after and remove after with the pointers re-aimed one at a time (kinematic arrows). Wikipedia's pointer-to-pointer sorted insert: the `**` walking down the link fields, and the head handled by the same line as every other node, which is the whole point.
- **2.6, the dummy closes the circle.** ODS's DLList with its dummy node, getNode(i) walking from whichever end is nearer, the cost min(i, n − i) on the counter.
- **2.7, the rho.** A list with a tail of length μ and a cycle of length λ on sliders; slow and fast moving; their meeting; one pointer sent back to the head; both stepping one at a time to the cycle's start. cpa's equation with the live numbers in the readout, true at every state.

Plan lines:

```
sim-address · Sim · array, pointer-arithmetic · variation by slider · arrows: symbolic (address to cell) · still · sliders: i, element size c (1 | 2 | 4 | 8 bytes as detents), base B · choice: layout (1D | 2D row-major) · readout "address = B + c·i = 1000 + 4·3 = 1012" · code: none (a property) · 2D
sim-arraystack · Sim (original: ODS fig. arraystack growth) · dynamic-array, array-resize, dynamic-array-cost · flow by animation · arrows: kinematic (cells shifted; elements copied) · moving · code: ods:arrays ArrayStack add/remove/resize (ODS pseudocode) · blocks: grow "resize if full"; shift "shift a[i..n−1] right"; store "a[i] = x"; shrink "resize if a.length ≥ 3n" · invariant: n ≤ a.length · cost: copies + shifts against the amortised bound · inputs: append | insert at front | push/pop at a capacity boundary · 2D
sim-two-pointers · Sim · two-pointers, three-sum · invariant made visible · arrows: kinematic (l and r move) · moving · code: thealgorithms-python maths/two_pointer.py (0-based; the prose is 1-based, the readout says so) · blocks: compare "compare a[l] + a[r] with the target"; move "advance l or retreat r" · invariant: no pair outside [l, r] sums to the target · cost: steps against n − 1 · inputs: hit | miss | duplicates | adversarial (answer at the middle) · predict pause: which pointer moves · 2D
sim-merge · Sim · merge-sorted-sequences · flow by animation · moving · code: Wikipedia's merge pseudocode · cost: comparisons against m + n − 1 · 2D
sim-moving-window · Sim (original: Wikipedia's moving-average plot) · sliding-window-fixed · flow by animation · moving · slider k · readout "SMA = SMA_prev + (p_new − p_old)/k" · cost: 3 steps per move against k · 2D
sim-variable-window · Sim · sliding-window-variable · invariant made visible · moving · code: doocs or TheAlgorithms greedy_methods/sliding_window.py · blocks: extend "r += 1"; shrink "while invalid: l += 1" · invariant: the window [l, r] is valid · cost: moves of l and r against 2n · 2D
sim-prefix · Sim (original: OI Wiki prefix-sum-2d) · prefix-sums, prefix-sums-2d, difference-array, difference-array-2d · variation by choice · still · choice: 1D query | 2D query | range add · readout "sum(l..r) = S_r − S_{l−1}" and the four-term 2D form · 2D
sim-linked-list · Sim (original: Wikipedia Singly-linked-list.svg) · singly-linked-list, implement-linked-list, pointer-to-pointer · flow by animation · arrows: kinematic (links re-aimed) · moving · code: Wikipedia's insertAfter/removeAfter pseudocode; the pointer-to-pointer insert in C · choice: operation (insert after | remove after | sorted insert with **) · 2D
sim-dllist · Sim (original: ODS fig. dllist) · sentinel-node, doubly-linked-list · flow by animation · moving · code: ODS getNode/addBefore/remove · cost: steps against 1 + min(i, n − i) · 2D
sim-rho · Sim (original: cpa tortoise_hare_proof) · floyd-cycle-detection, cycle-start, cycle-start-proof · flow by animation · arrows: kinematic (slow, fast) · moving · sliders μ (tail), λ (cycle) · code: cpa's Java · blocks: race "slow += 1, fast += 2 until they meet"; reset "slow = head"; walk "both += 1 until they meet" · readout "a = kL − b" with live values · special: μ = 0 · 2D
```

Referents: i, B and c are not referents (unnamed index and sizes) in sim-address; l and r (sim-two-pointers, sim-variable-window); i, l, r (3SUM); slow and fast, head (sim-rho); the new node and `prev` (sim-linked-list); the dummy (sim-dllist). Types drawn: `index`, `key`, `cost`, `size`.
