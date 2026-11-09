# Plan: 2.3 Two pointers and sliding windows

Status: **plan, built from in the same run** (`briefs/section-build.md`: no separate review for chapters 2 and 3; chapter 1's answered questions settle what they settle, and each new question below takes its recommended answer), 2026-11-09. Read for this plan: root `RULES.md`; the book's `RULES.md`, `COLOR.md`, `METHOD.md` (§1–§3, §5, decisions 1–21), `LOG.md` (passes 1–8); `ch02/config.md` and `exploration.md`; `judgements/ch01-03-reconciled.md` (with "Rulings applied 2026-11-08"), `judgements/ch02.md` §2.3, `judgements/ch01-03-references.md`; the 2.3 rows of `concept-map/concepts.json` and `toc.md`; `ch01/plans-summary.md`, `ch01/1.5/plan.md`, the built 1.1 and 1.5; `docs/design-code-and-debugger.md`, `docs/prompts/interactive-figures.md`, `translate.md`, `derivations.md`; the sources at their pins: `oiwiki/docs/misc/two-pointer.md` (c794414), Wikipedia `3SUM` (rev 1381879419), `Merge_algorithm` (1378002457), `Moving_average` (1383867559), TheAlgorithms `maths/two_pointer.py`, `maths/three_sum.py`, `data_structures/arrays/merge_sorted.py` (574d100), doocs `0713` (2c124ec), Exercism `reverse-string`, `series`, `largest-series-product` and their Python-track files (479f11b), icc `recursion_dynamic/longest_substr_k_distinct`, MIT 6.006 S20 ps0 and ps3 with their templates.

Sources on the page: OI Wiki (`oiwiki`, CC BY-SA 4.0 + SATA, **translated**, three blocks) and Wikipedia (`wikipedia`, CC BY-SA 4.0, three blocks); figure code from TheAlgorithms/Python (`thealgorithms-python`, MIT) and doocs/leetcode (`doocs-leetcode`, CC BY-SA 4.0). 6 blocks, 5 concepts, 5 Sims (4 debugger figures, 1 moving figure without code), 1 derivation, 4 code exercises, 2 NC code cards.

## Lead (draft, AI-marked; final wording after the humanizer passes, at most 80 words)

> Essential. Two indices walk an array, toward each other or in the same direction: to find a pair with a given sum, inside 3SUM, to merge two sorted lists, and as windows of fixed and of changing length. OI Wiki counts from 1 (num[1..n]), the 3SUM pseudocode from 0 (S[0..n−1]), the moving average by time (p_{n−k+1} … p_n). 3SUM's sort is a library call (sorting is Chapter 10), its hash table Chapter 5's, and it assumes distinct values. The moving average keeps a mean; the exercises' windows keep a sum or a count.

Tier: Essential, every concept (`exploration.md`). Indexing: mixed, as the lead says (reconciled "Indexing convention", 2.3). Bridges: **B9** (3SUM: sorts first, a library call, sorting in chapter 10; the hash-table sentence points to chapter 5; the passage assumes distinct values) and **B16** (the moving average is a running mean; the exercises' windows hold a sum or a count). Both fit with the indexing in 80 words, so nothing goes back to the user (decision 19).

## Blocks (`<h2>`), in page order

The page follows the map's order of concepts (two pointers, 3SUM, merging, fixed window, variable window), which is also the order of their prerequisites. OI Wiki's page puts its window section before its sorted-sequence section; the two are separate homes here (`toc.md` fold), and the variable window rests on the fixed one, so it comes last.

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `two-pointers` | Two pointers (OmniStax: the source's 引入 "Introduction" does not name the concept) | oiwiki | `oiwiki:misc/two-pointer#引入` | **yes** | what two pointers are: positions on sequences and lists, nodes on trees and graphs; moving in the same direction or toward each other; "Next we look at several concrete uses". The page's one-line opener ("本页面将简要介绍双指针") is outside the locator |
| 2 | `sorted-pair` | Using the order of the sequence (利用序列有序性, translated); 过程 "Procedure" as `<h3>` | oiwiki | `oiwiki:misc/two-pointer#利用序列有序性` (opening, 例题 4 as a link, 过程) | **yes** | the 例题 4 box restates LeetCode 167 and becomes a link; the procedure from the endpoints num[1], num[n] to the general l < r; then `sim-two-pointers`. The 实现 code (unlicensed), the merge sentence after it and the 习题 link are outside the locator |
| 3 | `three-sum` | 3SUM (the article's own title); "Quadratic algorithm" (source) as `<h3>` | wikipedia | `wikipedia:3SUM` (the lead's first sentence) + `#Quadratic algorithm` | no | the problem; the hash-table and comparison-model paragraphs; the pseudocode as `<pre>` (Wikipedia's words); the example sentence and the trace as printed, its red and magenta kept (see Questions); the correctness paragraph; then `sim-three-sum`. The lead's later sentences (conjectures, the 2026 research news) are not carried |
| 4 | `merge` | Merging two lists (source) | wikipedia | `wikipedia:Merge_algorithm#Merging two lists` (whole) | no | linear time and space; the pseudocode as `<pre>`; `sim-merge` after it; the linked-list paragraph; the merge-sort paragraph, its `{{slink}}` printed as "[*Merge sort* §Variants]" (a passage this book does not carry) |
| 5 | `moving-average` | Simple moving average (source) | wikipedia | `wikipedia:Moving_average#Simple moving average`, from its opening to "…and only 3 arithmetic steps." | no | the SMA over the last k of n data points, its definition display (kept), the update display (→ `drv-sma-next`), the FIFO / circular-buffer sentence; then `sim-moving-window`. Stops before the confused "k = n" sentence (erratum 21: outside the locator, no note) |
| 6 | `variable-window` | Variable-size sliding window (OmniStax: 维护区间信息 "maintaining interval information" names the technique, not the concept); 例题 1 "Example" as `<h3>`, 过程 "Procedure" as `<h4>` | oiwiki | `oiwiki:misc/two-pointer#维护区间信息` (opening, 例题 1 as a link, 过程) | **yes** | when the method applies (monotone information, cheap to add and remove: a sum of positive numbers, a product of positive integers); the 例题 1 box (LeetCode 713) as a link; the procedure and its count r − l + 1; then `sim-variable-window`. The 实现 code, the paragraph after it, 例题 2 (a tree with binary search and tree differences, chapters 6 and 11+) and 习题 are outside the locator |

Translation (blocks 1, 2, 6) under `translate.md`, by `tools/build_translation.py`'s parser and parity check, called from this section's own assembler (Wikipedia and OI Wiki blocks share one page, which neither shared tool assembles): standard English terms looked up in the cached Wikipedia articles (two pointers, sorted, ascending order, binary search, time complexity, interval, monotonicity, contiguous subarray, product, endpoint), set down in a section glossary (`glossary.en.json` beside this plan, rows `pending` for the chapter pass, as 1.5 did). OI Wiki's sentences, order and content kept; the footer line "translated from the Chinese and adapted".

**Wikipedia's wikitext** is read by script (a small reader in this section's folder, `wikitext.py`, since no shared one exists yet and 2.1 and 2.5 need one too): paragraphs, `'''bold'''` and `''italic''`, `[[links]]` as their text, `{{mvar}}`, `{{mono}}`, `{{math}}`, `<math>` (inline and `display="block"`), indented pseudocode as `<pre>`, `<ref>` (named ones resolved over the whole article) as book footnotes in Wikipedia's words, `{{r|…}}{{rp|…}}` as their named refs with the page, and `{{harv}}`, `{{Anchor}}` dropped.

## Concepts

| id | kind | tier | statement (for `book.json`, worded to the winning passage) | introducing span |
|---|---|---|---|---|
| `two-pointers` | idea | Essential | Two pointers point at positions of a sequence or a linked list (or at nodes of a tree or graph) and move in the same direction or toward each other to maintain or count information; on a sorted sequence, one at each end closes in on a pair with a given sum, each step moving the pointer whose element cannot be part of it. | `two-pointers`, "Two pointers is a simple and flexible technique" |
| `three-sum` | result | Essential | After sorting, 3SUM (do three of the n numbers sum to zero?) is solved in worst-case O(n²) time without hashing: for each a = S[i], two pointers start = i + 1 and end = n − 1 move inward, end down when a + b + c > 0 and start up when it is < 0. | `three-sum` |
| `merge-sorted-sequences` | result | Essential | Two sorted lists, linked lists or arrays, merge into one in linear time by repeatedly appending the smaller of their two heads (the head of A on a tie) and dropping it from its list, then appending what remains of the other. | `merge` |
| `sliding-window-fixed` | skill | Essential | A mean over the last k data points is updated as the window moves by adding the value that comes in and subtracting the one that drops out, SMA_next = SMA_prev + (p_{n+1} − p_{n−k+1})/k: three arithmetic steps, not a new sum of k values. | `moving-average` |
| `sliding-window-variable` | skill | Essential | Two pointers l and r bound a window over which a quantity that changes monotonically and is cheap to update (a sum of positive numbers, a product of positive integers) is kept: r moves right one element at a time and l moves right while the window breaks the condition, so for each r, l is the leftmost point the window can reach and the valid windows ending at r number r − l + 1. | `variable-window` |

Edges, as `concepts.json` has them (Hasse-reduced): `two-pointers` → `array`; `three-sum` → `two-pointers`; `merge-sorted-sequences` → `array`; `sliding-window-fixed` → `array`; `sliding-window-variable` → `two-pointers`, `sliding-window-fixed`. `array` is 2.1's concept, built at the same time: the three edges to it are added once it is staged (or listed for the chapter pass if it is not yet). Forms (Formulas and bounds): `sliding-window-fixed`, main SMA_{k,next} = SMA_{k,prev} + (1/k)(p_{n+1} − p_{n−k+1}), and SMA_k = (1/k) Σ_{i=n−k+1}^{n} p_i. No types: none of the five is a category of `RULES.md` (Types).

## Errata

None attached. The reconciled list has none for 2.3; erratum 21 (Moving average's "k = n" sentence) is outside the locator. Read while planning and found sound: the 3SUM trace (every sum checked), the update chain, OI Wiki's two procedures (both run against brute force by the judge, `checks2.py`). Wikipedia's correctness paragraph for 3SUM is a sketch (judge: it does not show that the pointer that moves first cannot skip its partner); that is a gap, not an error, and gets no note.

## Derivation candidates (root item 29)

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| SMA_{k,next} = (1/k) Σ_{n−k+2}^{n+1} p_i = … = SMA_{k,prev} + (1/k)(p_{n+1} − p_{n−k+1}) | a four-line `align` display | 3 (add and subtract p_{n−k+1}; regroup into SMA_{k,prev}; collect the two terms) | printed: qualifies (rule 29.1); 3 moves, the chapter 1 policy (plans-summary question 28) builds printed chains of three or more | **build** `drv-sma-next`, *Derivation · the next simple moving average from the previous one*, replacing the display; facts: the definition SMA_k (the display above it, block 5), the window's range n − k + 2 … n + 1 (the sentence before) |
| SMA_k = (p_{n−k+1} + … + p_n)/k = (1/k) Σ p_i | a two-line display | 1 (notation) | — | not built: a definition written two ways |
| 3SUM correctness ("Since the pointers only move in one direction…") | prose, no equations | — | not a chain of equations | not built; `sim-three-sum` shows the pointers' one-way moves |
| OI Wiki's r − l + 1 valid windows ending at r | prose | 1 | 0 + 1 + 0 = 1 | not built |
| OI Wiki's endpoint argument (num[1] + num[n] > target ⇒ move n's pointer) | prose | 1 per case | under the bar | not built; `sim-two-pointers` draws it |

## Figures

Plan lines in the `interactive-figures.md` format with this book's debugger fields (`RULES.md`, Figures). Every figure is a Sim (decision 19). Canvas text 26–40 logical units; the strip's own index labels (17 units in `F.ds.strip`) are switched off and drawn at 26. Every debugger figure shades its invariant in `index`'s tint, keeps a cost counter in `cost`, and offers the bad case among its inputs. No predict pauses and no editable inputs: the library has neither yet (as 1.1).

```
sim-two-pointers · Sim · two-pointers · invariant made visible; variation by input · arrows: kinematic (l and r move inward) · moving: one pointer move per step · choice input: hit (2 4 5 7 9 12 14 18, target 21) | miss (target 15) | duplicates (1 3 3, target 6, TheAlgorithms' doctest) | adversarial (5 8 12 16 18 19 20 21, target 34: the pair meets in the middle after n − 1 checks) · headline "a[l] + a[r] = 4 + 18 = 22 > 21: no pair with a[r] = 18 is left, so r moves." (live) · graph: below, the sorted array's pair-sum table for l < r (row l, column r): a move rules out a whole row or column, faded, and the cells still in play are the triangle [l, r] · 2D · code: thealgorithms-python maths/two_pointer.py::two_pointer, Python (the source's, its docstring of doctests left out), Java, C++, JavaScript (AI translations), 11 lines · blocks: init "start at both ends" lines 2–3 touches i, j; loop "close in" 5–11; check "found: a[i] + a[j] equals the target" 6–7 touches i, j; move "too small: move i right; too big: move j left" 8–11 touches i, j · level: default (one stop per check) · invariant: no pair outside [l, r] sums to the target (cells outside faded, [l, r] tinted) · readout: the watch (i, j, nums[i] + nums[j], target) · cost: checks k ≤ n − 1 · refs: i → l, j → r (the code's i and j are the text's l and r, said in the caption) · indexing: drawn 0-based, as the code; the caption says the text counts from 1
sim-three-sum · Sim · three-sum, two-pointers · flow by animation; variation by input · arrows: kinematic (start and end move inward; i steps right) · moving · choice input: Wikipedia's example (−25 −10 −7 −3 2 4 8 10, the trace's array) | duplicates (−1 0 1 2 −1 −4, TheAlgorithms' doctest, where Wikipedia's pseudocode reports (−1, 0, 1) twice and the code skips equal neighbours) | no triple (1 2 3 4) · headline "a = −10: start and end close in on b + c = 10." (live) · graph none; the triples found listed under the strip · 2D · code: thealgorithms-python maths/three_sum.py::three_sum, Python (the source's, docstring left out), Java, C++, JavaScript (AI) · blocks: sort "sort the array (a library call)" line 2 touches nums; outer "fix a = nums[i]" 4–21 touches i; inner "close in on −a with low and high" 7–21 touches low, high; found "record the triple, skip equal neighbours" 8–17 touches low, high · level: default (one stop per a); step into gives each check · invariant: for the current a, no pair outside [low, high] completes a triple (faded) · cost: pair checks against (n − 1)(n − 2)/2 · refs: i → i, low → start, high → end (Wikipedia's names in the pseudocode above the figure)
sim-merge · Sim · merge-sorted-sequences · flow by animation · arrows: kinematic (each head copied down into C) · moving: one append per step · choice input: interleaved (A = 1 4 7 9, B = 2 3 5 10 12) | A runs out first (1 2 3 | 4 5 6: the rest of B is copied in one block) | equal keys (2 2 5 | 2 3: a tie takes A's head, so the merge is stable) | B empty (1 3 | —: returned at once) · headline "head(A) = 4 > head(B) = 3: append 3 and drop it from B." (live) · graph none · 2D · code: thealgorithms-python data_structures/arrays/merge_sorted.py::merge_sorted_arrays, Python (the source's, docstring left out), Java, C++, JavaScript (AI) · blocks: check "check both inputs are sorted" 2–5; empty "one input empty: return the other" 6–9; take "append the smaller head and drop it" 12–17 touches i, j, merged; rest "copy what is left of either list" 18–19 touches merged · level: default (one stop per append) · invariant: C is sorted and holds exactly the elements before i in A and before j in B (shaded in index's tint) · cost: comparisons against m + n − 1 · refs: nums1, i → A; nums2, j → B; merged → C (Wikipedia's names)
sim-moving-window · Sim (no original: the section's one image compares the simple and the exponential moving average, which the page does not carry) · sliding-window-fixed · flow by animation; variation by slider · arrows: kinematic (the window slides one data point a step; p_{n+1} enters, p_{n−k+1} leaves) · moving: the window's position is the transport's clock, one step per new data point · slider k (size, 2..8, default 4) · headline "SMA = 14.25 + (17 − 12)/4 = 15.50" (live) · graph: the data points as bars, the window bracketed, the SMA drawn as a line so far · 2D · code: none (the passage gives a formula, not a procedure: config item 14) · invariant: the window holds exactly the last k points (tinted) · readout "SMA_{k,next} = SMA_{k,prev} + (p_{n+1} − p_{n−k+1})/k" with the live numbers, and the count "arithmetic steps 3 per move, against k = 4 to add the window again" · data: 24 closing prices of an invented series (the source names stock prices, gives none)
sim-variable-window · Sim · sliding-window-variable, two-pointers · invariant made visible; variation by input · arrows: kinematic (r extends the window, l shrinks it) · moving: one block per step · choice input: typical (3 2 5 1 4 2 6, k = 20: 15 windows) | k = 1 (no window qualifies: l passes r, which the l ≤ r guard stops) | never shrinks (1 2 1 1 2 1 1, k = 100: every window qualifies, 28 = n(n + 1)/2) | one element too big (2 9 30 1 3, k = 10: the window empties) · headline "p = 3 · 2 · 5 = 30 ≥ 20: l moves right until p < k." (live) · graph none · 2D · code: doocs-leetcode 0713 "Solution 1: Two Pointers", Python3, Java, C++, JavaScript, all four the source's (no AI mark), 11 lines · blocks: init "an empty window, product 1" 3–4 touches l, p; step "one more r" 5–10; extend "take x into the product" 6 touches r, p; shrink "while p ≥ k, drop nums[l] from the left" 7–9 touches l, p; count "r − l + 1 windows end at r" 10 touches l, r, ans · level: default (one stop per r) · invariant: the window [l, r] has product < k (tinted); cells left of l faded · cost: pointer moves of l and r against 2n · refs: l → l, r → r, p → tmp (OI Wiki's tmp is the code's p, said in the caption)
```

Every figure's code is credited by `data-source` and `data-locator` on its `<figure>` (content-format, provenance: a figure inside a block names a work of its own). `thealgorithms-python` and `doocs-leetcode` are not `sources` rows of `book.json` yet, and `ost` writes no `sources` row; see Questions.

**Source figures, keep or drop.**

| source item | decision | reason |
|---|---|---|
| Wikipedia 3SUM, the coloured trace (a text figure, red a, magenta b and c) | **kept in the text as printed** | its sentence names the colours; see Questions. `sim-three-sum` opens on the same array |
| Wikipedia Moving average, "Moving Average Types comparison - Simple and Exponential.png" (no caption) | drop | it compares the SMA with the exponential moving average, which the page does not carry; licence not on file |
| Wikipedia Merge algorithm, "Merge sort algorithm diagram.svg" | not in the locator (#Application) | merge sort is chapter 10's |
| OI Wiki's 实现 code fences | not carried | outside OI Wiki's licence; the code beside each figure comes from TheAlgorithms or doocs |

## Extra simulations (root item 15), none built

- `sim-pair-grid` alone would repeat `sim-two-pointers`'s lower panel; not proposed.
- `sim-window-cost`: the variable window against the brute-force double loop on the same input, step counts on a log–log plot over n, so the reader sees 2n against n²/2 grow apart (the exercises' complexity check, as a picture).

## Exercises (config.md; decision 19)

| id | concept(s) | kind | item | answer shape | tests | reference |
|---|---|---|---|---|---|---|
| `c1` | two-pointers | code | `exercism:reverse-string` | `code`, entry `reverse`, `bound: "n"` with a `grow` of random strings | the 7 canonical cases the Python track includes (the two grapheme-cluster cases are `include = false` on the track: a code-point reversal cannot pass them); source | Python: the track's `example.py` (source); JavaScript: AI |
| `c2` | sliding-window-fixed | code | `exercism:series` | `code`, entry `slices`; no bound (the output itself has (n − k + 1)·k characters) | 11 canonical cases (error cases as `raises: ValueError`); source | Python: track `example.py` (source); JavaScript: AI |
| `c3` | sliding-window-fixed | code | `exercism:largest-series-product` | `code`, entry `largest_product`, `bound: "n"`, `grow` a digit string of length n with span ⌊n/2⌋ (the span-by-span product is then n²/4 multiplications: "correct but too slow") | the canonical cases, latest version of each (superseded `reimplements` dropped, as the references file did), error cases as `raises: ValueError` | Python and JavaScript: AI (the track's example multiplies every span afresh, O(nk), and would fail its own bound); the bound is stated in `changes` |
| `c4` | sliding-window-variable | code | `icc:recursion_dynamic/longest_substr_k_distinct` | `code`, entry `longest_substr`, `bound: "n"`, `grow` a string of n letters over 3 symbols with k = 3 (every window is valid, so the double loop over start and end is quadratic) | icc's 4 asserts (source; None → `TypeError`) + AI tests (k = 0, one character, all one letter, k past the alphabet, a long run) | Python: icc's solution notebook, as a function (source); JavaScript: AI |
| `nc-ps0-6` | two-pointers, complexity-analysis | code (NC) | MIT 6.006 S20 ps0 Problem 0-6 `count_long_subarray` | `code`, entry `count_long_subarray` | the 5 cases of MIT's `tests.py` (source) | MIT's solution (ps0-solutions, source) |
| `nc-ps3-5` | sliding-window-fixed | code (NC) | MIT 6.006 S20 ps3 Problem 3-5(c) `count_anagram_substrings` | `code`, entry `count_anagram_substrings` | the 5 cases of MIT's `tests.py` (source) | MIT's solution (ps3-solutions, source); parts (a) and (b) are in the prompt, their written solutions linked |

Each card's `bound` is the reason the section exists: a correct double loop over the window passes every test and then reads "Correct. Your solution makes ~n² steps; this problem wants n." (checked against a quadratic solution before shipping). Not shipped, named in `exercise_notes`: three-sum and merge have no printed statement with tests (keon and TheAlgorithms are test sources only, decision 19); TheAlgorithms `two_pointer`, `max_sum_sliding_window`, `sliding_window`, keon `two_sum`, `longest_non_repeat`, tryalgo `windows_k_distinct` (test sources, no statement); Kattis closestsums, cd, hothike, snowflakes and ICPC tiredterry, slidecount (samples only, fit not rated good); Exercism series and largest-series-product fill the two code places of `sliding-window-fixed`; keon and TheAlgorithms `merge_two_lists` go to 2.5; Kattis kayaking to chapter 6; Project Euler 8 is statement-only (NC keyed only).

## Referents

Each figure's code variables that it draws (COLOR.md §3, decision 19), unique in the section:

| id | label | figures | text marks |
|---|---|---|---|
| `pair-l` | l, the left pointer (i in the code) | sim-two-pointers | block 2: $l$, "the pointer at 1" |
| `pair-r` | r, the right pointer (j in the code) | sim-two-pointers | block 2: $r$, "the pointer at n" |
| `ts-i` | i, the index of a | sim-three-sum | block 3: "the leftmost pointer" |
| `ts-start` | start (low in the code) | sim-three-sum | block 3: "the remaining pointers" (with end) |
| `ts-end` | end (high in the code) | sim-three-sum | block 3: as above |
| `list-a` | A, the first input list | sim-merge | block 4: {{mvar|A}} |
| `list-b` | B, the second input list | sim-merge | block 4: {{mvar|B}} |
| `list-c` | C, the merged list | sim-merge | block 4: {{mvar|C}} |
| `win-l` | l, the window's left end | sim-variable-window | block 6: $l$ |
| `win-r` | r, the window's right end | sim-variable-window | block 6: $r$ |
| `win-tmp` | tmp, the product of the window (p in the code) | sim-variable-window | block 6: $\mathit{tmp}$ |

Marks inside maths use `\htmlData{ref=…}` as 1.3 does. Types drawn: `index` (unnamed positions, invariant tints), `key` (cell values, sums, the SMA), `cost` (counters), `size` (n, k as a window length).

## References item

The schema has no References field yet (1.1, 1.4); none written.

## Attribution

- OI Wiki Team and contributors, *OI Wiki*, misc/two-pointer (c794414), CC BY-SA 4.0 with the SATA terms: "translated from the Chinese and adapted"; the footer prints the thanks from the `oiwiki` row's notice. A person stars the repository.
- Wikipedia contributors, "3SUM", "Merge algorithm", "Moving average" at the cached revisions, CC BY-SA 4.0, adapted.
- TheAlgorithms and contributors, TheAlgorithms/Python (574d100), MIT, notice kept: the code of `sim-two-pointers`, `sim-three-sum`, `sim-merge`.
- doocs contributors, doocs/leetcode 0713 (2c124ec), CC BY-SA 4.0: the code of `sim-variable-window`.
- Exercism (MIT), Interactive Coding Challenges (Apache 2.0), MIT OpenCourseWare 6.006 (CC BY-NC-SA 4.0, NC cards only) through their `exercise_sources` rows.
- `notes`: OI Wiki's code and its LeetCode example statements are not included. `ai`: text (the translation, the lead) and figures, this model; `built`.

## Questions (new; each decided here, the build follows the decision)

1. **Credit for figure code from a third work.** The figures' code is TheAlgorithms' and doocs', neither of which is a `sources` row, and `ost` writes no `sources` row (it says "edit it by hand", which root rule 19 forbids). *Decided:* add `sources` to the tables `ost` writes in place, with a test, in an app clone (`claude/app-fixes-2.3`), and write the two rows with it; the `<figure>` names `data-source="thealgorithms-python"` / `"doocs-leetcode"`. If that fails, the code is AI-written and marked.
2. **The 3SUM trace's colours.** Wikipedia prints the trace with a in red and b, c in magenta and says so in the sentence before it. *Decided:* keep the trace as printed, colours included (they are the source's words: the sentence names them), as a `<pre>` after the sentence; `sim-three-sum` stands after the correctness paragraph with its own referent colours. Recolouring the trace would make the sentence false, and replacing it would hide the source's own example.
3. **Two pointers' names.** OI Wiki calls them l and r; TheAlgorithms' code i and j; Wikipedia's 3SUM start and end, its code low and high. *Decided:* one referent per pointer, named as the text names it, the code's token mapped to it (`refs`), and the caption saying which name is which; the drawing labels the pointer as the code does, since the code panel is beside it.
4. **OI Wiki's example numbers.** The page carries 例题 4 and 例题 1 but not 2 and 3, and each box becomes a link. *Decided:* forced scenario: the numbers are dropped ("Example"), and the link goes to the English LeetCode page of the same problem; recorded in `translation-notes.md` (as this section's rows, for the chapter pass) and `config.md`'s forced-scenario table via the chapter pass.
5. **The order of the page.** The map's order rather than OI Wiki's (its window section comes before its sorted-sequence section). *Decided:* the map's order, since the variable window rests on the fixed window.
6. **`bound` on largest-series-product.** Exercism's statement asks for no running time. *Decided:* the card states the linear bound in `changes` ("A solution must run in time linear in the length of the input; the source asks for no bound."), so the test adds no requirement the card does not state.
