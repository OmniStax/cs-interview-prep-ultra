# Plan: 1.3 Asymptotic notation

Status: **plan for review** (root item 5), 2026-11-08. Nothing is built. Read for this plan: as 1.1, plus `ods/latex/intro.tex` lines 517–672, `ods/java/junk/Simple.java`, `ods/cpp/Simple.h`, `ods/latex/images/bigoh-1.gp` and `bigoh-2.gp`, `opendsa/RST/en/AlgAnal/AnalLower.rst` and `AnalMultiple.rst`, and the second judge's verdict on `big-o` (ODS stands).

Sources: ODS (CC BY 2.5 Canada) and OpenDSA (MIT). No translation. 3 blocks, 3 concepts, 4 Sims, 1 derivation.

## Lead (draft, AI-marked, 35 words)

> Essential; Big-O in several variables is Advanced. O, Ω and Θ compare how fast functions grow once the constants and the small cases are set aside. The loop example indexes its array from 0, a[0] to a[n−1].

Tier: Essential. Of another tier: `multivariate-big-o` (Advanced). Indexing: 0-based (ODS's loop); OpenDSA has no arrays. Bridges: none.

## Sub-concept blocks (`<h2>`)

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `big-o` | Asymptotic Notation (source) | ods | `ods:intro#asymptotic-notation`, up to (not including) "In a few cases, we will use asymptotic notation on functions with more than one variable" | no | the set definition of O(f(n)), the 5n log n + 8n − 200 proof (→ `drv-big-o-example`), the inclusions (erratum 1), abuse of notation, T(n) = 2 log n + O(1), Bachmann, the loop snippet (→ `sim-loop-count`'s code panel in place) and its five counts, "demonstrably different big-Oh running times" (erratum 2), `\figref{intro-asymptotics}` (→ `sim-crossover`) |
| 2 | `omega-theta` | Lower Bounds and Θ Notation (source), with "Lower Bounds", "Theta Notation" and "Classifying Functions" as `<h3>` | opendsa | `opendsa:AlgAnal/AnalLower` (Lower Bounds, Theta Notation, Classifying Functions) | no | Ω's definition and its example, the footnote on the alternate definition (a book footnote), Θ, "the upper and lower bounds always meet" (erratum 10), the Collatz `codeinclude` (**not cached**), the limit test and its n² against 2n log n example; the LowerBoundCON slideshow (not cached) → `sim-limit-test`; the LowerThetaSumm embed → Exercises |
| 3 | `multivariate` | Multiple Parameters (source) | opendsa | `opendsa:AlgAnal/AnalMultiple` | no | the pixel-colour histogram, Θ(P log P) revised to Θ(P + C log C), 1000 × 1000 pixels against 256 colours; the c3p16 `codeinclude` (**not cached**; the prose names `count`, `value(i)`, "the first `for` loop" and "the final line, the call to `sort`", so it does not read without it) |

ODS's own multivariate paragraph (the formal definition with z) is the runner-up for `multivariate-big-o` and is not carried (one explanation per concept). The `:ref:` to NP-Complete in AnalLower links to 23.2.

## Concepts

| id | kind | tier | statement | introducing span |
|---|---|---|---|---|
| `big-o` | definition | Essential | O(f(n)) is the set of g(n) for which some c > 0 and n₀ give g(n) ≤ c·f(n) for all n ≥ n₀: an upper bound on growth, constants and small n set aside. | `big-o`, "the so-called *big-Oh notation*" |
| `big-omega-theta` | definition | Essential | T(n) is in Ω(g(n)) when T(n) ≥ c·g(n) for all n > n₀ (a lower bound); it is Θ(h(n)) when it is in both O(h(n)) and Ω(h(n)); the limit of f(n)/g(n) (∞, 0 or a constant) classifies two functions. | `omega-theta`, "The *lower bound* for an algorithm … is denoted by the symbol Ω" |
| `multivariate-big-o` | definition | Advanced | When an algorithm's cost depends on several parameters, the analysis keeps each (Θ(P + C log C) for P pixels and C colours) rather than folding them into one. | `multivariate`, "multiple parameters to describe the cost" |

`multivariate-big-o`'s statement in `concepts.json` is ODS's formal definition, which this page does not carry; the statement above is OpenDSA's (see Questions).

## Errata notes

- **1** (`big-o`): "For any constants a, b, c > 0, O(a) ⊂ O(log n) ⊂ O(nᵇ) ⊂ O(cⁿ)": the last inclusion needs c > 1 (for c ≤ 1, n is not in O(cⁿ)). Marker after the display.
- **2** (`big-o`): "if the two algorithms have demonstrably different big-Oh running times, then we can be certain that the one with the smaller running time will be faster": an O bound is only an upper bound; the claim needs Θ (the next block). Marker after "for large enough values of n".
- **10** (`omega-theta`): "Given an algebraic equation describing the time requirement for an algorithm, the upper and lower bounds always meet": the passage's own footnote example (n for odd n, n²/100 for even n) is an equation whose O and Ω bounds differ. Marker after the sentence.

## Derivation candidates

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| ODS: 5n log n + 8n − 200 ≤ 5n log n + 8n ≤ 5n log n + 8n log n ≤ 13 n log n, for n ≥ 2 | an `align` chain after "This is proven as follows" | 3 | printed: qualifies by rule 29.1 | **build** `drv-big-o-example`, *Derivation · 5n log n + 8n − 200 is in O(n log n)*; replaces the display; facts: the definition of O(f(n)) (the display above), log n ≥ 1 for n ≥ 2 (a condition, its own fact); the end result names c = 13, n₀ = 2 |
| ODS: T(n) = a + b(n + 1) + cn + dn + en, then T(n) = O(n) | two displays with a paragraph between | 1 (drop the constants by the definition) | printed, 0 + 0 + 0 | **recommend not built** (one move; `sim-loop-count`'s readout states the same sum live). See Questions on short printed chains |
| OpenDSA: c₁n² + c₂n ≥ c₁n² for n > 1, so T(n) is in Ω(n²) | a math display in a topic box | 1 | printed | **recommend not built** (one move) |
| OpenDSA: n²/(2n log n) = n/(2 log n) → ∞ | two displays | 2 | printed | **recommend not built** (two moves; `sim-limit-test` plots the ratio) |
| OpenDSA multivariate: Θ(C) + Θ(P) + Θ(C log C) = Θ(P + C log C) | prose | 2 | 0 + 1 + 0 = 1 | not built |
| ODS inclusions multiplied by n | prose | 1 | 0 | not built |

## Figures

```
sim-crossover · Sim (originals: ODS bigoh-1 (n to 100) and bigoh-2 (n to 10 000), the two plots of "Plots of 15n versus 2n log n", both behind the toggle) · big-o · variation by slider (one zoom carries the book's two plots as two of its states) · arrows: none · still · slider n_max (100..10 000, log, detents 100 and 10 000, the book's two windows) with a dashed circle at n = 2^7.5 ≈ 181, where 15n = 2n log n (the morph lands the crossing dot) · headline "Up to n = 100, 15n stays above 2n log n; they cross at n ≈ 181, and from there 2n log n is ahead for good." · graph alone, axes rescaling with the slider (the zoom the plan names, interactive-figures.md §2) · 2D · code: none (a growth plot) · readout "15n = 2715 and 2n log n = 2715 at n = 181"
sim-big-o-witness · Sim · big-o · variation by slider · arrows: none · still · sliders c (cost multiplier, 1..20, default 13, dashed circle at 13) and n₀ (size, 1..64, default 2, dashed circle at 2; a second circle at the smallest n₀ that works for the current c, from F.solve) · headline "With c = 13 and n₀ = 2, 5n log n + 8n − 200 stays under c·n log n everywhere past n₀." · graph alone: f(n) and c·n log n, the stretch n ≥ n₀ shaded, the first n ≥ n₀ where f exceeds c·g marked in PAL.bad when there is one · 2D · code: none (a property) · readout "f(n) ≤ c·n log n for all n ≥ n₀: holds" or "fails at n = 40 (f = 1184 > 4·n log n = 851)". Below c = 5 no n₀ works, which the bad marker shows without a special.
sim-loop-count · Sim · big-o, complexity-analysis (from 1.4) · flow by animation · arrows: kinematic (i advancing along the array) · moving: one pass per step · slider n (size, 1..16, default 5) · headline "One assignment, n + 1 comparisons, n increments, n offsets and n stores: T(n) = O(n)." · graph: beside, total count against n on log–log axes with 4n + 2 dashed · 2D · code: ods Simple.snippet() (java/junk/Simple.java lines 6–9, Java; the C++ is the same two lines) · blocks: loop "test i < n (from the second pass, after i++)" line 7 touches i, n; body "compute a[i]'s address and store i" line 8 touches i, a · invariant: a[0..i) holds 0..i−1, shaded in the index tint · readout "assignments 1 · comparisons 6 = n + 1 · increments 5 · offsets 5 · stores 5 · total 22 = 4n + 2" · cost: each primitive against its count in n · inputs: the n slider only (every input of size n costs the same). Note: the debugger steps by whole lines, and the three primitives of line 7 (int i = 0, i < n, i++) share a line, so they tick their own counters from the trace's events rather than as blocks.
sim-limit-test · Sim (no original: the OpenDSA LowerBoundCON slideshow it stands in for is not cached) · big-omega-theta, big-o · variation by choice and slider · arrows: none · still · choice pair: n² against 2n log n (OpenDSA's example) | 5n log n + 8n − 200 against n log n (ODS's, ratio → 5) | 15n against 2n log n (ODS's, ratio → 0) · slider n_max (10..10⁶, log) · headline "n²/(2n log n) = n/(2 log n) keeps growing: n² is in Ω(2n log n)." · graph alone: the ratio f(n)/g(n) against n, its limit dashed where finite · 2D · code: none (a property) · readout "f(n)/g(n) = 7.53 at n = 100 → ∞ · f ∈ Ω(g)" (→ 0: f ∈ O(g); → 5: f = Θ(g))
```

**Source figures, keep or drop.** ODS "Plots of 15n versus 2n log n" (printed as Figure 1.5 in ODS's numbering, two plots) → `sim-crossover`. OpenDSA LowerBoundCON (a JSAV slideshow, not cached, content unknown) → `sim-limit-test` sits where it stood. The two `codeinclude`s are code, not figures (Questions). Exploration's `sim-growth-race` is not planned: its "machine ten times faster" comes from OpenDSA AnalCompvsAlg, which is not a winning passage, so the figure would teach something no block on the page says; `sim-crossover` is the growth figure the ODS block asks for.

## Extra simulations

- `sim-pixel-counts` (only once c3p16 is fetched): sliders P and C, three bars for Θ(C), Θ(P) and Θ(C log C) against the naive P log P, so the reader sees when C log C overtakes P, the passage's last point; code beside, stepping init, count and sort.

## Exercises

| concept | kind | items | answer shape | status |
|---|---|---|---|---|
| big-o | check | opendsa AnalPairMCQ1–AnalPairMCQ11 + UpperBoundsSumm | `choice` | converter |
| big-omega-theta | check | opendsa ThetaUpperMCQ, AlgAnlsTFbgthta + LowerThetaSumm | `choice` | converter |
| big-o (from 1.2, if moved) | check | opendsa AlgAnlsFIBsmlintgr2 (key 2), tagged big-o and logarithms | `number` | converter |
| big-o, big-omega-theta | exercise | aspnes-202 A.6.2 ("an approximate sum", Σ k²2ᵏ = Θ(n²2ⁿ)), A.6.3 ("a stretched function") | `open`, the key as solution | ready |
| big-o (+ big-omega-theta where asked) | NC card | mitocw-6-006-spring2020 ps1 1-1; mitocw-6-046j-fall2005 ps1 1-1; mitocw-6-006-fall2011 ps1 1-1; mitocw-6-042j-fall2005 ps6 #8 | `open` | `exercises-nc.json` |
| big-o | trace | opendsa CompareGrowth, GrowthRatesPRO | `sequence` | **waits for the `sequence` type** |
| multivariate-big-o | — | none | — | — |

`exercise_notes`: MisunderstandingsTF1–6 go with 1.4; MCS 14.18–14.42 and Applied Combinatorics left out (unkeyed); Erickson chapter 0 exercise 2 (songs in Θ(n³), Θ(n log n)) left out (unkeyed).

## Referents

| id | what | figures | blocks |
|---|---|---|---|
| `i` | the loop variable of Simple.snippet() | sim-loop-count | `big-o` |

The five primitive counts wear `cost`; n wears `size`; the cells of `a` wear `key` and their position labels `index`. f(n), c·g(n), the ratio and every O(·), Ω(·), Θ(·) wear `cost`; c and n₀ are in ink (the constant c of a Big-O definition is untyped, book `RULES.md`), as are a, b, c, d, e of T(n).

## References item

- Harvard CS50, "Asymptotic Notation" (video, CIU): a short spoken introduction to O with pictures of growth.
- "Big O Notation (and Omega and Theta), best mathematical explanation" (video, CIU): works through the c-and-n₀ definitions of all three.
- Skiena, CSE 373 lecture on asymptotic notation (video, CIU): the dominance relation and the common classes, at lecture length.

## Attribution

- Pat Morin, *Open Data Structures*, https://github.com/patmorin/ods (9d22c44), CC BY 2.5 Canada, adapted.
- OpenDSA eTextbook modules, Cliff Shaffer and the OpenDSA Project Contributors, https://github.com/OpenDSA/OpenDSA (40bf936), MIT licence, adapted; the MIT notice ("Copyright (c) 2012-2020 by the OpenDSA Project Contributors") reached from the footer.
- `notes`: "OpenDSA's interactive slideshow is replaced by a figure; its code fragments are not included." (if they are not fetched). `ai`, `built`.
