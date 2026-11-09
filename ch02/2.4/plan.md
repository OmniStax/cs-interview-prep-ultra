# Plan: 2.4 Prefix sums and difference arrays

Status: **plan, built from in the same run** (brief `briefs/section-build.md`: no separate review for chapters 2 and 3), 2026-11-09. Read for this plan: root `RULES.md`; the book's `RULES.md`, `COLOR.md`, `METHOD.md` (§1–§3, §5, decisions 1–21), `glossary.en.json`, `LOG.md` (passes 1–8); `ch02/exploration.md` and `config.md`; `judgements/ch01-03-reconciled.md` (with "Rulings applied 2026-11-08", ruling 3), `judgements/ch02.md` §2.4, `judgements/ch01-03-references.md`; the four rows of `concept-map/concepts.json`; chapter 1's `plans-summary.md`, `1.5/plan.md` and the built 1.1 and 1.5; and the winning passages: `oiwiki/docs/basic/prefix-sum.md` at the registered pin (c794414), whole, its figure `images/prefix-sum-2d.svg` with its `.tex`, doocs `0304` and `0370` `README_EN.md` (Solution 1 of each), TheAlgorithms `data_structures/arrays/prefix_sum.py`.

One source of prose, OI Wiki (CC BY-SA 4.0 + SATA), **all of it translated** from the Chinese under `docs/prompts/translate.md`, each block AI-marked as a translation. Code from doocs/leetcode (CC BY-SA 4.0, ruling 3 / decision 18: printed in all four languages) and TheAlgorithms/Python (MIT; Java, C++ and JavaScript AI-translated). 4 blocks, 4 concepts, 2 Sims (both debugger figures), 1 code set, 0 derivations, 1 erratum.

## Lead (draft, AI-marked, ≤ 80 words)

> Essential; two-dimensional prefix sums and difference arrays are Advanced. Running totals that answer range-sum queries in constant time, and their inverse, which takes range updates. The text counts from 1, with a₀ = 0 and S₀ = 0 as its Convention box says. The code counts from 0: TheAlgorithms' PrefixSum handles a range that starts at 0 on its own, and the doocs code pads its table with a zero row and column, so s[i + 1][j + 1] is S_{i+1, j+1}, and writes d[r + 1].

Tier: Essential. Of another tier: `prefix-sums-2d`, `difference-array-2d` (Advanced). Indexing: 1-based in the text, 0-based in the code, the shift named. Bridges: none (the reconciled list assigns none to 2.4). The forward pointers OI Wiki makes itself (the inclusion–exclusion principle, the Fenwick tree) are links in the text, not bridges.

## Blocks (`<h2>`), in OI Wiki's order

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `prefix-sums` | Prefix sums (OmniStax: 引入 "Introduction" names no concept; the 前缀和 heading under it, which would repeat the h2, is dropped and its paragraph kept); 一维前缀和 as `<h3>` | oiwiki | `oiwiki:basic/prefix-sum#引入 (with its 规定 box), #前缀和 (its heading dropped) and #一维前缀和` | **yes** (≈230 words) | the one-line introduction to both halves of the page; the 规定 (Convention) box as `div.note` (1-based, a₀ = 0); S_i = Σ a_j, S₀ = 0, S_i = S_{i−1} + a_i, S([l, r]) = S_r − S_{l−1}, O(n) preprocessing for O(1) queries; the 参考实现 box (OI Wiki code, unlicensed) replaced by a four-language code set of TheAlgorithms' `PrefixSum`; the std::partial_sum / std::inclusive_scan paragraph |
| 2 | `prefix-sums-2d` | Two-dimensional and multidimensional prefix sums (source); 基于容斥原理 and 逐维前缀和 as `<h3>` | oiwiki | `oiwiki:basic/prefix-sum#二维/多维前缀和 (its opening), #基于容斥原理 and #逐维前缀和` | **yes** (≈560) | the two methods; S_{i,j} by inclusion–exclusion with its recurrence; the 示例 (Example) box as `div.note` with OI Wiki's numbers (erratum 20 inside), `sim-prefix-2d` after it where its image stood; the submatrix query and its O(1); the O(2^k N) remark; the dimension-by-dimension method and its O(kN) |
| 3 | `difference-array` | Difference arrays (OmniStax: 差分 "Differences" read as the technique); 一维差分 as `<h3>` | oiwiki | `oiwiki:basic/prefix-sum#差分 (its opening) and #一维差分` | **yes** (≈280) | differences as the inverse of prefix sums, updates before queries, the Fenwick-tree pointer (a link to Section 30.2); D_i = a_i − a_{i−1}; std::adjacent_difference; the 性质 (Properties) box as `div.note` (a_i = Σ D_j, S_i = Σ(i − j + 1)D_j); the update D_l ← D_l + v, D_{r+1} ← D_{r+1} − v, O(1) per update and O(n) to recover; the 参考代码 box (OI Wiki code) replaced by `sim-range-add`, whose panel is doocs 0370 |
| 4 | `difference-array-2d` | Two-dimensional and multidimensional difference arrays (OmniStax: the source's 二维/多维差分 with "difference arrays", as block 3) | oiwiki | `oiwiki:basic/prefix-sum#二维/多维差分` | **yes** (≈170) | the 2D difference by inclusion–exclusion, differencing dimension by dimension, the four corner updates, one 2D prefix pass to recover, O(2^k) per update in k dimensions |

Not carried: OI Wiki's 特例：子集和 DP (subset sums, bitmask material for chapter 7 or later), its tree prefix sums and differences (树上前缀和, 树上差分, the USACO 例题), 习题 (practice-problem links), and every code box. Inside the carried locators: the 洛谷 P1387 例题 box (a Luogu problem restated in OI Wiki's words; the rule for LeetCode restatements, links only, applies, and with no References field in the schema it is left out and named in `notes`), its 参考代码 box, the 三维前缀和的参考实现 box and 二维差分's 参考代码 box (OI Wiki code; no licensed code for them is named, so nothing stands in their place).

Terms (`glossary.en.json`, new rows pending for the chapter pass): 前缀和 prefix sum; 一维前缀和 one-dimensional prefix sums; 二维/多维前缀和 two-dimensional and multidimensional prefix sums; 区间 range; 区间和 range sum; 预处理 preprocessing; 递推关系（式） recurrence (relation); 容斥原理 inclusion–exclusion principle; 子矩阵 submatrix; 逐维前缀和 prefix sums dimension by dimension; 差分 difference / taking differences; 差分序列 difference sequence; 差分数组 difference array; 区间修改 range update; 区间加 adding to a range; 矩形加 adding to a rectangle; 树状数组 Fenwick tree; 规定 Convention, 性质 Properties (apparatus labels, `book`); 示例 Example (already in the glossary). Authorities: Wikipedia's Prefix sum, Summed-area table and Fenwick tree at their cached revisions, cp-algorithms' Fenwick tree ("Range Update and Point Query") and Inclusion-exclusion, `book` for ordinary English.

Forced scenarios: (1) OI Wiki's links to zh.cppreference.com point at the same pages of en.cppreference.com (an English reader's reference; the anchor text, `std::partial_sum` and the rest, is unchanged); (2) OI Wiki's links to its own pages (容斥原理, 树状数组) become links to the sections of this book that carry those topics (RULES, Cross-references). Both go to `translation-notes.md` and `ch02/config.md` in the chapter pass (concurrency: this section touches only its folder).

## Concepts

| id | kind | tier | type | statement | introducing span |
|---|---|---|---|---|---|
| `prefix-sums` | definition | Essential | `key` (RULES Types: "a prefix sum S_i") | The prefix sums of a sequence a₁, …, aₙ (with a₀ = 0) are S_i = a₁ + ⋯ + a_i, computed one after another by S₀ = 0, S_i = S_{i−1} + a_i; after this O(n) preprocessing the sum of any range [l, r] is S_r − S_{l−1}, an O(1) query. | `prefix-sums` |
| `prefix-sums-2d` | result | Advanced | none | S_{i,j} = A_{i,j} + S_{i−1,j} + S_{i,j−1} − S_{i−1,j−1} fills the table of two-dimensional prefix sums in one pass, the subtraction removing the overlap the two sums count twice (inclusion–exclusion); the sum of a submatrix is then four lookups, S_{i₂,j₂} − S_{i₁−1,j₂} − S_{i₂,j₁−1} + S_{i₁−1,j₁−1}. In k dimensions, summing along one dimension at a time costs O(kN), where inclusion–exclusion costs O(2^k N). | `prefix-sums-2d` |
| `difference-array` | skill | Essential | none | The difference sequence D_i = a_i − a_{i−1} (a₀ = 0) is the inverse of the prefix sum: adding v to every a_i with l ≤ i ≤ r becomes D_l ← D_l + v and D_{r+1} ← D_{r+1} − v, O(1) per update, and one O(n) prefix-sum pass after all the updates recovers the array. | `difference-array` |
| `difference-array-2d` | skill | Advanced | none | Adding v to every entry of the submatrix with corners (x₁, y₁) and (x₂, y₂) becomes four updates of the two-dimensional difference array, +v at (x₁, y₁) and (x₂ + 1, y₂ + 1) and −v at (x₁, y₂ + 1) and (x₂ + 1, y₁); one two-dimensional prefix-sum pass afterwards recovers the array. In k dimensions an update touches 2^k entries. | `difference-array-2d` |

Edges (Hasse-reduced, as the map): `prefix-sums → array` (2.1); `prefix-sums-2d → prefix-sums`; `difference-array → prefix-sums`; `difference-array-2d → prefix-sums-2d`, `difference-array-2d → difference-array`. Forms (the Formulas and bounds list): S_i = Σ_{j=1}^i a_j; S₀ = 0, S_i = S_{i−1} + a_i; S([l, r]) = S_r − S_{l−1}; the 2D recurrence and the submatrix query; D_i = a_i − a_{i−1}; a_i = Σ D_j; the range update; the 2D difference. Coverage: each block introduces its concept; blocks 2 and 3 use `prefix-sums`; block 4 uses `prefix-sums-2d` and `difference-array`. No variables rows (chapter 1's convention: the maths stays in ink).

## Errata

- **20** (block 2, the 示例 box): "S_{3,3} = A_{3,3} + S_{2,3} + S_{3,2} − S_{2,2} = 5 + 18 + 15 − 9 = 29" lists the numbers of S_{3,2} and S_{2,3} in the other order: by the figure S_{2,3} = 15 and S_{3,2} = 18. The sum is right. Marker at "so we should have", before the display (a marker after a display stands on a line of its own, 1.2's experience). `sim-prefix-2d` writes the terms in the text's order with their own numbers.

## Derivation candidates (root item 29)

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| the 2D recurrence from the definition: S_{i,j} = A_{i,j} + (the rows above) + (the columns to the left) − (their overlap) | prose then one display | 3 (split the rectangle; inclusion–exclusion; name the parts as S) | 1 (inclusion–exclusion, imported) + 2 + 0 = 3 | not built: under four moves and a score of four |
| the 示例 box's S_{3,3} = … = 5 + 18 + 15 − 9 = 29 | one display | substitution | — | never (a worked substitution); the figure computes it live |
| 性质: S_i = Σ_j Σ_k D_k = Σ_j (i − j + 1) D_j | one display, two members | 1 (swap the order of summation) | 1 + 1 + 0 = 2 | not built |
| 1D query S_r − S_{l−1} | one display | 1 | — | not built |

## Figures

Exploration's seed `sim-prefix` (one still figure with a 1D / 2D / range-add choice) becomes two debugger figures, one per procedure with code (decision 8: code beside the visual), as the brief asks: 2D inclusion–exclusion, and a range update by the difference array. The 1D prefix sum keeps its listing as a code set where OI Wiki's 参考实现 stood (its two formulas are the idea; a third figure would repeat the first row of `sim-prefix-2d`).

```
sim-prefix-2d · Sim (original: OI Wiki images/prefix-sum-2d.svg, rendered to PNG) · prefix-sums-2d · invariant made visible; variation by input · arrows: none (cells are highlighted, nothing moves along a path) · still between stops, stepped (the transport scrubs the trace; one cell per stop) · choice: query (A₂..₃,₂..₃ | one cell, A₃,₃ | the whole matrix, which reads the zero row and column) · headline: the cell being filled or the query, with its numbers ("S₃,₃ = A₃,₃ + S₂,₃ + S₃,₂ − S₂,₂: the blue and red blocks overlap in S₂,₂, which is counted twice") · graph: none · 2D
  · code: doocs-leetcode:0304#Solution 1: Two-dimensional Prefix Sum, Python3 / Java / C++ / JavaScript, all four the source's (the LeetCode harness comments after each class dropped) · canonical Python, 17 lines
  · blocks: pad "a table of zeros one row and one column larger" [3–4] touches s; row "row i of the matrix" [5–9]; cell "the sums above and to the left, less their overlap, plus v" [6–9] touches s, i, j, v; query "four lookups" [12–17] touches s; ⤷ q1 "the rectangle from the corner to (row2, col2)" [13]; q2 "less the columns left of col1" [14]; q3 "less the rows above row1" [15]; q4 "plus the corner taken away twice" [16]
  · level: cell (14 stops: pad, 12 cells, the query; step into the query for its four terms; the default rule would pick the coarser row level, 5 stops, which hides the recurrence)
  · invariant: every S_{i′,j′} before (i + 1, j + 1) in row order is filled (filled cells; the rest hollow); the zero row and column drawn as padding (dashed) · readout (canvas) "S_{i,j} = A_{i,j} + S_{i−1,j} + S_{i,j−1} − S_{i−1,j−1} = 5 + 15 + 18 − 9 = 29" and, for the query, the four-term sum with its numbers
  · cost: lookups, 3 per cell and 4 per query, against the mn = 12 cells filled and the cells a direct sum of the query adds · inputs: the three queries above, the whole matrix the edge case (row1 = col1 = 0 reads s[0][…] and s[…][0], the padding an unpadded table lacks)
  · colours: S_{i,j−1} (the block to the left) blue and S_{i−1,j} (the block above) red, as facts (`facts`), because the text names them by colour ("the blue submatrix", "the red submatrix"); their overlap shows where the two tints cross; the cell being filled outlined dashed in ink, as OI Wiki's dashed box; values `key`; the counter `cost`. No referents: the figure draws cells, not the code's i, j or row1 … col2, so those tokens stay ink
  · labels: row and column indices 1-based as the text (S with its row and column 0); a cell's value in the cell; hover names on every cell ("S₂,₃ = 15, the sum of rows 1–2, columns 1–3")
sim-range-add · Sim (no original: OI Wiki prints no figure for the difference array; it stands where OI Wiki's 参考代码 box stood) · difference-array · flow by animation; invariant made visible · arrows: kinematic (during the recovery, each running total carried one cell right) and symbolic (+c and −c marks at the two ends of an update) · moving: one update per stop, the prefix pass cell by cell (step into) · choice: updates (overlapping adds | adds that run to the end) · headline: the update and what it writes, or the prefix pass ("Add 3 to a[1..4]: d[1] += 3, d[5] −= 3") · graph: none · 2D
  · code: doocs-leetcode:0370#Solution 1: Difference Array, Python3 / Java / C++ / JavaScript, all four the source's · canonical Java (its prefix pass is a loop; Python's is `list(accumulate(d))`, one line that every stop of the pass bands)
  · blocks: init "an array of zeros" [3]; update "add c at l and take it away after r" [5–9] touches l, r, c, d; ⤷ left "d[l] += c" [6]; right "d[r + 1] −= c, unless r is the last index" [7–9]; recover "prefix sums of d" [11–13] touches d, i; ⤷ cell "d[i] += d[i − 1]" [12]
  · level: default (init, one stop per update, the pass; into for each cell of the pass)
  · invariant: a prefix pass over d gives the array with every update so far applied (the row a above, hollow while it is implied, filled as the pass writes it) · readout (canvas) "prefix sums of d = a" with the values, and the update rule D_l ← D_l + c, D_{r+1} ← D_{r+1} − c with the live l, r, c
  · cost: writes to d, 2 per update, against Σ(r − l + 1) a loop over each range would make; the pass n − 1 additions · inputs: overlapping adds (length 8: [1, 4, 3], [3, 6, 2], [0, 2, −1]); adds that run to the end (the guard r + 1 < length skips the write past the last cell, drawn as a dashed cell n beyond the end; every add spans most of the array, the case where a loop over each range costs most: [2, 7, 4], [0, 7, 1], [0, 5, 2])
  · referents: l, r (pointers under d), c (the +c / −c marks and the bracket over a), i (the pass's pointer); d and a are the strips' names, in ink · indices 0-based as the code (the readout's rule writes the text's D_l and D_{r+1}, with "the code counts from 0")
```

**Source figures.** OI Wiki's `prefix-sum-2d` (示例): replaced by `sim-prefix-2d`, the image kept behind the original toggle (rendered from the SVG to a PNG on white, `media/ch02/oiwiki-prefix-sum-2d.png`, since the SVG is black on transparent); its caption is its alt text, translated: "Example of a two-dimensional prefix sum". `prefix-sum1.svg` and `prefix-sum2.svg` belong to the tree sections, not carried.

## Extra simulations

None proposed: the 1D prefix sum is the first row of `sim-prefix-2d`'s table, and the 2D difference array would be `sim-range-add` with four corners, which the text's display already states.

## Exercises

None ship (config.md, 2.4 rows: none for any of the four concepts). `exercise_notes`: TheAlgorithms' PrefixSum and equilibrium-index doctests and keon's sum_sub_squares tests are test sources with no printed statement (decision 19); the Kattis items (sumoftheothers, commercials, shortsell, pivot, freefood) have samples only and none was rated a good fit; Kattis subseqhard needs a hash map and is held for chapter 5.

## Referents

`l`, `r`, `c`, `i` (sim-range-add). None in `sim-prefix-2d` (its colours are facts).

## Attribution

- OI Wiki Team and contributors, *OI Wiki*, basic/prefix-sum (c794414), CC BY-SA 4.0 + SATA: "translated from the Chinese and adapted" (the footer, from the `oiwiki` row's notice).
- doocs contributors, *doocs/leetcode*, 0304 and 0370 Solution 1, CC BY-SA 4.0 (new `sources` row `doocs-leetcode`; the figures carry `data-source`).
- TheAlgorithms contributors, *TheAlgorithms/Python*, `data_structures/arrays/prefix_sum.py`, MIT, its copyright line (new `sources` row `thealgorithms-python`; the code set carries `data-source`).
- `notes`: OI Wiki's code, its Luogu P1387 example and its sections on subset sums and on trees are not included. `ai`: text (the translation) and figures, this model; `built`.

## Questions (decided here, recommendation taken)

1. **Two figures, not exploration's one.** `sim-prefix` with a 1D / 2D / range-add choice becomes `sim-prefix-2d` and `sim-range-add`, both debugger figures with the doocs code beside them; the 1D prefix sum gets a code set. *Decided: yes* (the brief's two figures; decision 8).
2. **The figure of the 示例 box stands after the box**, not inside the `div.note` (no page of any book puts a Sim inside a note). *Decided: after it.*
3. **The 洛谷 P1387 box** restates a Luogu problem, not a LeetCode one; the same rule (statements are not ours to copy) applies, and there is no References field to hold the link. *Decided: left out, named in `notes`.*
4. **cppreference links** go to en.cppreference.com (forced scenario 1). *Decided: yes.*
5. **TheAlgorithms excerpt.** The code set shows `__init__` and `get_sum` without their docstrings (doctests, a test source) and without `contains_sum` (a hash set, chapter 5). *Decided: yes; the replacement table says so.*
6. **doocs harness comments.** The "Your NumMatrix object will be instantiated and called as such" comments after 0304's classes are LeetCode's template, not code. *Decided: dropped, recorded in the replacement table.*
7. **Blue and red as facts** in `sim-prefix-2d`, since the text names the two blocks by colour. *Decided: yes.*
8. **Typing.** `prefix-sums` takes `key`; the other three, a result and two skills, stay untyped. *Decided: yes.*
9. **h2 headers.** "Prefix sums" for 引入 (with 前缀和's heading dropped, as 1.5 dropped 内容), "Difference arrays" for 差分 and "Two-dimensional and multidimensional difference arrays" for 二维/多维差分, so the two halves of the page read alike. *Decided: yes.*
