# Plan: 1.2 Logarithms, factorials and harmonic numbers

Status: **plan for review** (root item 5), 2026-11-08. Nothing is built. Read for this plan: as 1.1, plus `ods/latex/intro.tex` lines 397–515 (Mathematical Background, Exponentials and Logarithms, Factorials), `ods/latex/rbs.tex` lines 60–110 and the figure sources `figs/harmonic.ipe`.

One source, ODS (CC BY 2.5 Canada). No translation. 3 blocks, 3 concepts, 3 Sims, 2 derivations.

## Lead (draft, AI-marked, 35 words with the bridge)

> Essential; harmonic numbers are Advanced. Three functions that turn up in running times. log with no base means log₂, and ln is the natural logarithm. *[B-new-b, only if the harmonic block keeps its opening clause:]* Harmonic numbers return with random binary search trees in 8.6.

Tier: Essential. Of another tier: `harmonic-numbers` (Advanced). Indexing: none (no arrays). Bridges: none from the reconciled list; B-new-b is new (see Questions).

## Sub-concept blocks (`<h2>`)

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `logarithms` | Exponentials and Logarithms (source) | ods | `ods:intro#exponentials-and-logarithms` | no | bˣ, log_b k, "the number of times we have to divide k by b", the binary-search count ⌈log₂(n + 1)⌉, e, ∫₁ᵏ 1/x dx = ln k, the two manipulations, the change of base (→ `drv-change-of-base`) |
| 2 | `factorials` | Factorials (source) | ods | `ods:intro#sec:factorials` | no | n!, 0! = 1, Stirling with α(n), ln(n!), the integral remark (erratum 4), binomial coefficients |
| 3 | `harmonic` | Harmonic Numbers (OmniStax header: the passage is an untitled digression inside ODS's random BST section) | ods | `ods:rbs`, the harmonic digression (`latex/rbs.tex` lines 76–110) | no | H_k, ln k < H_k ≤ ln k + 1, the two integrals, `\figref{harmonic-integral}` → `sim-harmonic`. **Extent question:** the first sentence begins "Before we can present our main result about random binary search trees, we must take some time for a short digression…" |

The Mathematical Background preamble (its pointer to "the very good (and free) textbook" by Lehman, Leighton and Meyer) is in no locator and is not carried.

## Concepts

| id | kind | tier | statement | introducing span |
|---|---|---|---|---|
| `logarithms` | definition | Essential | log_b k is the x with bˣ = k; log means log₂ and ln is log_e; log_b k is roughly the number of times k can be divided by b before reaching 1; log_b k = log_a k / log_a b, so ln k = (ln 2)(log k). | `logarithms`, "the *base-b logarithm* of k" |
| `factorials-stirling` | result | Essential | n! = 1·2·…·n counts the orderings of n items, 0! = 1; n! = √(2πn)(n/e)ⁿ e^α(n) with 1/(12n + 1) < α(n) < 1/(12n); binomial coefficients are n!/(k!(n − k)!). | `factorials`, "*Stirling's Approximation*" |
| `harmonic-numbers` | definition | Advanced | H_k = 1 + 1/2 + … + 1/k, with ln k < H_k ≤ ln k + 1 (k ≥ 1). | `harmonic`, "the k-th *harmonic number*" |

## Errata notes

- **3** (`harmonic`): "For a non-negative integer, k": the bound needs k ≥ 1 (ln 0 is undefined). Marker after "ln k < H_k ≤ ln k + 1".
- **4** (`factorials`): "∫₁ⁿ ln n dn = n ln n − n + 1" writes the integration variable as n; read ∫₁ⁿ ln x dx. Marker after the integral.

## Derivation candidates

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| change of base: ln k = log k / log e = log k / ((ln e)/(ln 2)) = (ln 2)(log k) ≈ 0.693147 log k | one display chain after "For example, we can use these two manipulations" | 3 (change of base; change of base again for log e; ln e = 1 and simplify) | printed: qualifies by rule 29.1 (0 + 0 + 0) | **build** `drv-change-of-base`, *Derivation · ln k in terms of log k*; it replaces the display; facts: the change-of-base formula (1.2, the display above it), ln e = 1 |
| harmonic bounds by two integrals | prose first, with the figure | 6 (lower: H_k as rectangle areas ≥ ∫₁^{k+1} 1/x dx, = ln(k + 1), > ln k; upper: H_k = 1 + Σ₂ᵏ 1/i ≤ 1 + ∫₁ᵏ 1/x dx = 1 + ln k) | 1 (the area comparison for a decreasing function) + 3 + 1 (two bounds joined) = 5 | **build** `drv-harmonic-bounds`, *Derivations · the bounds on H_k*, placed after the paragraph that ends "(See Figure … for a graphical explanation.)"; facts: ∫₁ᵏ 1/x dx = ln k (1.2, Exponentials and Logarithms), the rectangles of `sim-harmonic` |
| Stirling "most easily proven by approximating ln(n!) … by the integral" | prose, "most easily proven" | ≥ 6 for the formula as stated | 2 + ≥ 4 + 0 ≥ 6 | **not built** (judgement call, see Questions): the hinted integral only gives ln(n!) ≈ n ln n − n + 1; reaching √(2πn) and the bounds on α(n) needs steps the book never states, so the derivation would put words in its mouth |
| ln(n!) = n ln n − n + ½ ln(2πn) + α(n) from Stirling | one display, no steps | 2 (take ln; expand) | 0 + 2 + 0 = 2 | not built |

## Figures

```
sim-halving · Sim · logarithms · variation by slider · arrows: none · still (each division is drawn as one shorter bar; the slider redraws) · slider k (key-free count, 1..10⁶, log, detents 8, 1000, 10⁶) · choice base b: 2 | e | 10 · headline "1000 halved 10 times is 0.98, the first value at most 1: log₂ 1000 = 9.97." · graph none: a staircase of bars, each 1/b of the last, with the level 1 dashed · 2D · code: none (a property, not a procedure) · readout "log_b k = ln k / ln b = 6.91 / 0.693 = 9.97 · divisions to reach ≤ 1: 10"
sim-harmonic · Sim (originals: ODS harmonic-2 and harmonic-3, the two panels of one figure, both behind the toggle, the caption in original_caption) · harmonic-numbers · variation by slider · arrows: none · still · slider k (1..20, default 5; the figure is drawn for a general k) with a dashed circle at k = 1, where H₁ = ln 1 + 1 meets the upper bound · choice bound: lower (rectangles over 1/x from 1) | upper (1 plus rectangles under 1/x) · headline "H₅ = 2.28 lies between ln 5 = 1.61 and ln 5 + 1 = 2.61." · graph alone, the curve f(x) = 1/x with the rectangles 1, 1/2, …, 1/k and the integral shaded (archetype 2) · 2D · code: none (a bound) · readout "ln k < H_k ≤ ln k + 1: 1.61 < 2.28 ≤ 2.61"
sim-stirling · Sim · factorials-stirling · variation by slider · arrows: none · still · slider n (1..60, the range where α(n)'s bounds were checked) · headline "At n = 10, Stirling's formula is off by a factor e^α(10) = 1.0084." · graph beside: α(n) between its bounds 1/(12n + 1) and 1/(12n), on a log scale · 2D · code: none · readout "n! = 3628800 · √(2πn)(n/e)ⁿ = 3598696 · α(n) = 0.00833 ∈ (1/121, 1/120)"
```

**Source figures, keep or drop.** ODS harmonic-2 and harmonic-3 (one figure, two panels, printed as Figure 7.2 in ODS's numbering) are replaced by `sim-harmonic`. No other figure in these locators. `sim-stirling` replaces nothing; it is the figure root item 14 asks for the result.

## Extra simulations

- `sim-log-area`: ln k drawn as the area under 1/x from 1 to k, with a second shaded area from 1 to 2, so the reader sees ln k = (ln 2)·log k as "how many doublings of the area" (ODS states both the integral and the change of base). Weighed against `sim-harmonic`, which draws the same curve: offered only if the reader should meet the integral before the harmonic numbers.

## Exercises

| concept | kind | items | answer shape | status |
|---|---|---|---|---|
| logarithms | check | opendsa logarithms_1, logarithms_1.5, logarithms_2 + MathLogSumm; MthBgFIBlgbs1, MthBgFIBlgbs2 | `number` (logarithms_* are Khan generators: one fixed instance each, from their own `vars`) | needs the converter |
| logarithms (→ 1.3?) | check | opendsa AlgAnlsFIBsmlintgr2 ("the smallest integer k such that n log n is in O(n^k)", key 2) | `number` | config places it here; it tests Big-O, so root item 12 sends it to 1.3 (see Questions) |
| logarithms | code | exercism grains (11 canonical tests, 3 of them `raises`; the Exercism Python example passes 11/11) | `code` | **waits for the `code` type** |
| logarithms, factorials-stirling | code | kattis howmanydigits (CC BY-SA 3.0; 1 sample; AI tests and AI reference, `generated_by: "ai"`) | `code` (stdin → stdout) | waits for the `code` type |
| factorials-stirling | code | kattis stirlingsapproximation (AI tests, tolerance 1e−8) | `code` with `tol` | waits for the `code` type |
| factorials-stirling | exercise | aspnes-202 A.5.2 (comparing products, keyed) | `open`, the key as solution | ready |
| harmonic-numbers | NC card | mitocw-6-042j-fall2005 ps6 #7 (integral bounds for sums, keyed) | `open` | `exercises-nc.json` |

`exercise_notes`: MCS 14.12–14.17 left out (unkeyed, built on block stacking); aspnes-202 B.1.1 and Erickson's Factorial item held for 4; kattis inversefactorial over the two-code cap; Project Euler 20 and 34 left out (statement only).

## Referents

None. No figure draws a named variable of code; k, b and n are quantities. Types: `cost` only for binary search's ⌈log₂(n + 1)⌉ comparisons; `size` for that n; logarithms, factorials, Stirling's terms and H_k are functions and stay in ink (book `RULES.md`, untyped), as do k and b.

## References item

None from CIU (its lists have nothing on logarithms, factorials or harmonic numbers).

## Attribution

- Pat Morin, *Open Data Structures*, https://github.com/patmorin/ods (9d22c44), CC BY 2.5 Canada, adapted.
- `notes`: "The unkeyed problems on harmonic numbers are not included." `ai`, `built` as usual.
