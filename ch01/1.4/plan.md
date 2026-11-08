# Plan: 1.4 Analysing running time and space

Status: **plan for review** (root item 5), 2026-11-08. Nothing is built. Read for this plan: as 1.1, plus `ods/latex/intro.tex` lines 764–920 (The Model of Computation; Correctness, Time Complexity, and Space Complexity) and Erickson 0.6 "Running Time" from the PDF (pp. 15–17).

Sources: ODS (CC BY 2.5 Canada) and Erickson (CC BY 4.0). No translation. 3 blocks, 3 concepts, 1 Sim, 0 derivations.

## Lead (draft, AI-marked, carries B2, 50 words)

> Essential. The running-time passage analyses algorithms from 1.1: the Bottles of Beer song, peasant multiplication and ApportionCongress, with lattice multiplication for space, and adds songs of its own. Its pseudocode counts from 1 (for i ← 1 to n, Pop[1..n]); the word-RAM and the three kinds of guarantee use no arrays.

Tier: Essential, every concept. Indexing: mixed (Erickson 1-based; ODS none). Bridge **B2** in the lead, as above.

## Sub-concept blocks (`<h2>`)

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `word-ram` | The Model of Computation (source) | ods | `ods:intro#sec:model` | no | w-bit words, constant-time word operations, O(k) allocation, w ≥ log n, space in words. Its last paragraph is edition-dependent (`\javaonly`: "a fairly close match for the (32-bit) Java Virtual Machine (JVM) when w = 32"; `\cpponly`: "modern desktop computers when w = 32 or w = 64"; the pseudocode edition prints neither); see Questions |
| 2 | `running-time` | Running Time (source; it is the second subsection of Erickson's "Analyzing Algorithms", whose opening and "Correctness" are 1.1's) | jeffe | `jeffe:0.6` "Running Time" to the end of 0.6 | no | singing time, "beer" 3n + 3 times, NDaysOfChristmas and Alouette as `<pre>` (Alouette stays in Erickson's French), the quadratic-song list, the TELNET song, the peasant recurrence (erratum 7), ApportionCongress's O(N + RI + (R − n)E) and the Census Bureau's array (erratum 8), space for lattice multiplication; "twice much time" (erratum 9); Erickson's footnotes as book footnotes. NDaysOfChristmas becomes `sim-song-count`'s code panel in place |
| 3 | `guarantees` | Correctness, Time Complexity, and Space Complexity (source) | ods | `ods:intro#correctness-time-complexity-and-space-complexity` | no | correctness, time and space; worst-case, amortized and expected running times; the mortgage and fire-insurance examples (dollar signs as `&#36;`); `\secref{randomization}` → link to 1.6's `linearity` block |

Two reference fixes on printed words (links, not prose): Erickson's "Techniques described in the next chapter imply the upper bound T(x, y) = O(log x)" links "the next chapter" to 10.2 (recurrences); "a binary heap or a heap-ordered array" links to 9.2.

## Concepts

| id | kind | tier | statement | introducing span |
|---|---|---|---|---|
| `word-ram` | definition | Essential | Memory is cells holding w-bit words; arithmetic, comparisons and bitwise operations on words take constant time, allocating k words takes O(k) time, and the only assumption is w ≥ log n; space is counted in words. | `word-ram`, "the *w-bit word-RAM* model" |
| `complexity-analysis` | skill | Essential | Measure running time by counting how often an algorithm executes an instruction or reaches a milestone, as a function of the input: nested loops give nested sums, recursion a recurrence, and the cost may depend on the data structure underneath. | `running-time`, "We can measure time by counting how many times the algorithm executes a certain instruction or reaches a certain milestone" |
| `running-time-guarantees` | definition | Essential | Worst-case f(n): no operation takes longer. Amortized f(n): any m operations take at most m·f(n). Expected f(n): the running time is a random variable, over the structure's own random choices, with mean at most f(n). | `guarantees`, "three different kinds of running time guarantees" |

## Errata notes

- **7** (`running-time`): "T(x, y) ≤ T(⌊x/2⌋, 2y) + 2": each step does a parity test, a halving, the doubling y + y and possibly prod + y, up to four operations; the conclusion T(x, y) = O(log x) stands. Marker after the inequality.
- **8** (`running-time`): "The Census Bureau implements the priority queue as an unsorted array" contradicts 1.1's apportionment passage, "The Census Bureau uses a sorted array … recalculated from scratch at every iteration"; either way ExtractMax costs Θ(n) per seat there, so O(Rn) stands. Marker after the sentence.
- **9** (`running-time`): "requires about twice much time" lacks "as". Marker after the phrase.

## Derivation candidates

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| Σ_{i=1}^n Σ_{j=1}^i j = n(n + 1)(n + 2)/6 = Θ(n³) (gifts given) | inline, stated without steps | 4 (inner sum; split i(i + 1)/2; Σi² and Σi; factor) | 1 (Σ i² = n(n + 1)(2n + 1)/6) + 4 + 1 = 6 | **not built** (judgement call): the move needs Σ i², which the book states nowhere, so the derivation would import an unsourced fact (root item 29.3) |
| Σ_{i=1}^n i = n(n + 1)/2 (gift names sung) | inline | 1 (Gauss's sum, unstated) | 1 + 1 + 0 = 2 | not built |
| peasant recurrence T(x, y) ≤ T(⌊x/2⌋, 2y) + 2 ⇒ O(log x) | inline; "Techniques described in the next chapter imply …" | 4 (unroll; count the halvings, ⌊log₂ x⌋ + 1 from 1.2; multiply; drop constants) | 1 + 4 + 0 = 5 | **not built** (judgement call): the book defers the step to its recursion chapter on purpose; a derivation here would teach recurrence solving ahead of 10.2, and erratum 7 changes its constant |
| ApportionCongress: O(N + RI + (R − n)E) → O(N + R(I + E)) (R ≥ 2n) → O(Rn) or O(R log n) | prose with inline bounds | 3 | 0 + 2 + 1 = 3 | not built |
| "beer" exactly 3n + 3 times | stated | 1 | 0 | not built |
| ODS: $120 000 / 120 months = $1 000 per month | one display | 1, numbers only | — | never (a substitution) |

## Figures

```
sim-song-count · Sim · complexity-analysis · flow by animation; variation by choice and slider · arrows: none (the verse counter advances; nothing travels) · moving: one verse per step · choice song: BottlesOfBeer (jeffe:0.1) | NDaysOfChristmas (jeffe:0.6) · slider n (size, 1..12, default 12 for the Christmas song, 10 for the bottles) · headline "Twelve days: 78 gift names sung and 364 gifts given." · graph: beside, on log–log axes, the counts for n = 1..12 against 3n + 3, n(n + 1)/2 and n(n + 1)(n + 2)/6, the current n marked (METHOD §2.1.7: one run tied to its growth curve) · 2D · code: jeffe:0.6 NDaysOfChristmas, Erickson pseudocode, lines 1–8 (1-based, gifts[2..n] the traditional lyric's gifts); jeffe:0.1 BottlesOfBeer, lines 1–6, when that song is chosen · blocks (Christmas): verse "sing day i" lines 3–8 touches i; ⟶ countdown "name the gifts from day i down to day 2" lines 4–5 touches j; ⟶ partridge "and a partridge in a pear tree" lines 6–8 · blocks (Bottles): verse "sing verse i" lines 3–4 touches i; coda "no bottles, go to the store" lines 5–6 · invariant: days 1..i sung, filled; the rest hollow · readout "gift names 78 = n(n + 1)/2 · gifts 364 = n(n + 1)(n + 2)/6" or "beer 33 = 3n + 3" · cost: the milestone counted (gift names, gifts, "beer") against its formula · inputs: the two songs; no adversarial case (a song's count depends only on n)
```

**Source figures, keep or drop.** Erickson's Figure 0.6 ("The Barley Mow") belongs to exercise 4, which is left out (unkeyed), so it is not on the page. NDaysOfChristmas and Alouette are unnumbered listings: NDaysOfChristmas becomes the code panel, Alouette stays as `<pre>`. ODS's blocks have no figures.

**Where `sim-loop-count` went.** `exploration.md` seeded it here, for complexity-analysis and word-ram. Its code (`Simple.snippet()`) and the five counts it ticks are printed in ODS's Asymptotic Notation passage, which is 1.3's `big-o` block, so it is planned there (see Questions). This section's figure is `sim-song-count`, Erickson's own counting example.

No figure for `word-ram` or `running-time-guarantees` in the required set: one is a model stated in words, the other three definitions illustrated by money; both are offered below as extras.

## Extra simulations

- `sim-pq-cost`: ApportionCongress run with the priority queue as the Census Bureau's array (Θ(n) per ExtractMax) or a binary heap (O(log n)), an n slider replaying the operation count on log–log axes against Rn and R log n, so the reader sees the text's O(Rn) against O(R log n) diverge.
- `sim-word-size`: a w-bit word drawn as w cells, sliders w and n, the largest count it holds (2ʷ − 1) against n, failing in `PAL.bad` when w < log n, for ODS's "otherwise a word is not even big enough to count the number of elements".

Weighed and dropped: a mortgage-and-insurance chart for the guarantees (three bars of monthly cost); it restates the passage's arithmetic and adds no view.

## Exercises

| concept | kind | items | answer shape | status |
|---|---|---|---|---|
| word-ram, need-for-efficiency (1.1) | check | opendsa AnlsIntroMCQszip + FasterCorASumm | `choice` | converter |
| word-ram | check | opendsa MthBgMCQrmacc, MthBgMCQdskacc (the judge calls rmacc a weak fit; kept as ranked) | `choice` | converter |
| complexity-analysis | check | opendsa AnalProgramMCQtheta1–9 + AnalProgramSumm (each carries its own Java fragment) | `choice` | converter |
| complexity-analysis | check | opendsa AnalProblemTF1, TF2, TF4–TF7 + AnalProblemSumm | `choice` | converter |
| running-time-guarantees | check | opendsa AlgAnlsMCQsqlsrch, AlgAnlsTFsqlsrch1, AlgAnlsTFsqlsrch2 | `choice` | converter |
| running-time-guarantees, big-o, big-omega-theta | check | opendsa MisunderstandingsTF1–6 + MisSumm | `choice` | converter |

No written, code or NC item. `exercise_notes`: Erickson chapter 0 exercises 2, 3 and 4 (songs in other Θ, singing in syllables, The Barley Mow) and Applied Combinatorics' basics exercises left out (unkeyed); AnalProblemTF10–12 held for 10 (they assume sorting); MIT 6.006 S20 ps0 0-6 held for 2.3 and 6.006 F11 ps1 1-3 to 1-6 for 6 (NC).

## Referents

| id | what | figures | blocks |
|---|---|---|---|
| `i`, `j` | NDaysOfChristmas's (and BottlesOfBeer's) loop variables | sim-song-count | `running-time` |

The counts wear `cost`, n, w and R `size`. T(x, y) and every bound wear `cost`. N, I and E of the apportionment bound are running times (`cost`).

## References item

- TopCoder, "Computational Complexity" sections 1 and 2 (CIU): counting loops into sums and the master theorem, worked at more length.
- "Analyzing Algorithms in 18 minutes" (video playlist, CIU): a fast review of loop and recurrence analysis.

## Attribution

- Jeff Erickson, *Algorithms* (1st edition, June 2019), https://jeffe.cs.illinois.edu/teaching/algorithms/, CC BY 4.0, adapted.
- Pat Morin, *Open Data Structures*, https://github.com/patmorin/ods (9d22c44), CC BY 2.5 Canada, adapted.
- `notes`: "Erickson's end-of-chapter exercises are not included." `ai`, `built`.
