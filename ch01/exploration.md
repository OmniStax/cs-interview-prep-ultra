# Chapter 1 exploration: Algorithms and their cost

Status: **draft for review**, 2026-11-08. Nothing is built. Written from `concept-map/toc.md` and `concepts.json` (chapter `ch-cost`), `dossiers/ch01.md`, `judgements/ch01.md` (with the second judge on `big-o`), `judgements/ch01-03-reconciled.md`, `judgements/ch01-03-references.md` and METHOD §4.4 decisions 13–18. No source text was re-read for this file; every locator is the reconciled winner's.

## What the chapter is

Six sections, 27 concepts (21 Essential, 5 Advanced, 1 Beyond). It is the only chapter with no prerequisite chapter: every edge from it points into chapters 2–45. It is also the most mathematical of the first pass: 1.2, 1.3 and 1.6 are mathematics prose with proofs, 1.5 is analysis, and only 1.1 has algorithms to run.

| § | Title | Tier | Concepts (tier where it differs) |
|---|---|---|---|
| 1.1 | What an algorithm is | Essential | algorithm, underspecified-algorithm, describing-algorithms, need-for-efficiency, interface-vs-implementation, lattice-multiplication (Advanced), peasant-multiplication |
| 1.2 | Logarithms, factorials and harmonic numbers | Essential | logarithms, factorials-stirling, harmonic-numbers (Advanced) |
| 1.3 | Asymptotic notation | Essential | big-o, big-omega-theta, multivariate-big-o (Advanced) |
| 1.4 | Analysing running time and space | Essential | word-ram, complexity-analysis, running-time-guarantees |
| 1.5 | Amortized analysis | Essential | amortized-analysis, aggregate-accounting, potential-method (Advanced), counter-increment-decrement (Beyond) |
| 1.6 | Counting and expected value | Essential | counting, probability-basics, conditional-probability, random-variable, linearity-of-expectation, indicator-variables (Advanced), geometric-expectation |

`random-variable` is new (decision 18); the map's 1.6 now names the linearity concept "Expected value and linearity of expectation".

## Provenance: every block and its source

The page order inside a section follows the winners' own order where one source leans on another passage of itself (Erickson 0.5 leans on 0.2 and 0.3), else the map's order. Block ids are proposals.

| § | block | concept | `data-source` | `data-locator` | licence | note |
|---|---|---|---|---|---|---|
| 1.1 | `algorithm` | algorithm | jeffe | `jeffe:0.1` | CC BY 4.0 | Bottles of Beer; ~400 words of etymology footnotes become book footnotes |
| 1.1 | `lattice` | lattice-multiplication | jeffe | `jeffe:0.2` preamble + "Lattice Multiplication" | CC BY 4.0 | digit arrays 0-based |
| 1.1 | `peasant` | peasant-multiplication | jeffe | `jeffe:0.2` "Duplation and Mediation" | CC BY 4.0 | the duplation trace figure |
| 1.1 | `apportionment` | algorithm (worked example) | jeffe | `jeffe:0.3` (whole) | CC BY 4.0 | decision 18: kept whole; 1-based Pop[1..n] |
| 1.1 | `underspecified` | underspecified-algorithm | jeffe | `jeffe:0.4` | CC BY 4.0 | the only direct treatment |
| 1.1 | `describing` | describing-algorithms | jeffe | `jeffe:0.5` (intro, Specifying the Problem, Describing the Algorithm) + `jeffe:0.6` opening and "Correctness" | CC BY 4.0 | two blocks, one per locator |
| 1.1 | `efficiency` | need-for-efficiency | ods | `ods:intro#the-need-for-efficiency` | CC BY 2.5 CA | |
| 1.1 | `interfaces` | interface-vs-implementation | ods | `ods:intro#sec:interfaces`, opening to the first subsection | CC BY 2.5 CA | the subsections go to 2.1, 3.2, 3.3 (and 5, 8) |
| 1.2 | `logarithms` | logarithms | ods | `ods:intro#exponentials-and-logarithms` | CC BY 2.5 CA | log = log₂, ln natural |
| 1.2 | `factorials` | factorials-stirling | ods | `ods:intro#sec:factorials` | CC BY 2.5 CA | |
| 1.2 | `harmonic` | harmonic-numbers | ods | `ods:rbs`, the harmonic digression (`latex/rbs.tex` lines 76–110, with the harmonic-integral figure) | CC BY 2.5 CA | a digression lifted out of random BSTs (chapter 8) |
| 1.3 | `big-o` | big-o | ods | `ods:intro#asymptotic-notation`, up to the multivariate paragraph | CC BY 2.5 CA | both judges: ODS, by continuity |
| 1.3 | `omega-theta` | big-omega-theta | opendsa | `opendsa:AlgAnal/AnalLower` (Lower Bounds, Theta Notation, Classifying Functions) | MIT | its `codeinclude` (Collatz) is not cached |
| 1.3 | `multivariate` | multivariate-big-o | opendsa | `opendsa:AlgAnal/AnalMultiple` | MIT | its `codeinclude` (c3p16) is not cached |
| 1.4 | `word-ram` | word-ram | ods | `ods:intro#sec:model` | CC BY 2.5 CA | |
| 1.4 | `running-time` | complexity-analysis | jeffe | `jeffe:0.6` "Running Time" to the end of 0.6 | CC BY 4.0 | analyses 1.1's algorithms; 1-based |
| 1.4 | `guarantees` | running-time-guarantees | ods | `ods:intro#correctness-time-complexity-and-space-complexity` | CC BY 2.5 CA | |
| 1.5 | `amortized` | amortized-analysis | oiwiki | `oiwiki:basic/amortized-analysis` 引入 + 内容 + 聚合分析 | CC BY-SA 4.0 + SATA | **translated** (≈400 words) |
| 1.5 | `aggregate-accounting` | aggregate-accounting | oiwiki | 记账分析 + 扩展示例：堆栈操作 (聚合分析法, 记账分析法) | CC BY-SA 4.0 + SATA | **translated** (≈480); its code-fenced credit trace is redrawn as a figure |
| 1.5 | `potential` | potential-method | oiwiki | 势能分析 (原理, 示例：动态数组的扩容分析) + 堆栈 势能分析法 | CC BY-SA 4.0 + SATA | **translated** (≈540) |
| 1.5 | — | counter-increment-decrement | none | — | — | no open prose (only jeffe-notes 9.3, NC); see open questions |
| 1.6 | `counting` | counting | brisk | `brisk:counting#The Fundamental Theorem`, `#Permutations` (with Partial permutations), `#Combinations` | CC BY-SA 4.0 | |
| 1.6 | `probability` | probability-basics | brisk | `brisk:probability#Outcomes and events`, `#Probability measures` | CC BY-SA 4.0 | writes Pr(A) |
| 1.6 | `conditional` | conditional-probability | brisk | `brisk:probability#Conditional probability`, `#Independence` | CC BY-SA 4.0 | writes Pr(A\|B) |
| 1.6 | `random-variable` | random-variable | mcs2018 | `mcs2018:19.1` (the definition and its examples; extent fixed at the plan) | CC BY-SA 3.0 | decision 18; writes R, Pr[R = x] |
| 1.6 | `linearity` | linearity-of-expectation | ods | `ods:intro#sec:randomization`, from the start to "…into sums of simpler random variables (the right hand sides)." | CC BY 2.5 CA | writes E[X], Pr{X = i} |
| 1.6 | `indicators` | indicator-variables | ods | `ods:intro#sec:randomization`, from "A useful trick…" to the end of the subsection | CC BY 2.5 CA | |
| 1.6 | `coin-tosses` | geometric-expectation | ods | `ods:skiplists#lem:coin-tosses` (lemma and proof) | CC BY 2.5 CA | lifted out of skip lists (chapter 11) |

Source count: ODS 11, Erickson 6 explanations in 7 blocks (with 0.3), OI Wiki 3, brisk 3, OpenDSA 2, MCS 1, none 1. No fold in this chapter. No doocs write-up wins, so no twin exercise is needed.

## Apparatus

- **Erickson** (1.1, 1.4): pseudocode in small caps (BottlesOfBeer, PeasantMultiply, ApportionCongress), set as `<pre>` in Erickson's notation, transcribed from the PDF since the `.txt` has lost digits, minus signs and small-caps names ("i 1 bottles" is i − 1, "B O B (n)" is BottlesOfBeer(n)). His footnotes in 0.1 are book footnotes. His chapter 0 figures (the two historical scans, the lattice and duplation traces, the ApportionCongress figure) are taken from the PDF; the scans keep the credits printed at the end of his book.
- **ODS** (1.1–1.4, 1.6): LaTeX with `#code#` names, theorems and lemmas as environments, figures as `.ipe`/`.pdf` in `latex/figs/` and `images/` (bigoh-1, bigoh-2, harmonic-2, harmonic-3). Code from `java/junk/Simple.java` and `cpp/Simple.h` where the prose imports it. ODS cross-references (`\chapref{arrays}`) are mapped to this book's sections (B5).
- **OpenDSA** (1.3): RST with JSAV slideshows and `codeinclude` directives; neither the slideshows nor the code (`SourceCode/`, MIT) is cached. Either the finder fetches them, or the blocks ship without the snippets (the prose explains the code in words) and the slideshows are replaced by OmniStax figures.
- **OI Wiki** (1.5): Markdown with KaTeX; its code blocks are unlicensed and are not copied; the credit trace in 记账分析 sits in a code fence and is redrawn as a figure from the numbers in the prose.
- **brisk** (1.6): LaTeX, examples inline, a question-and-answer exercise table at the end of each chapter.
- **MCS 2018** (1.6): LaTeX via PDF; definitions and examples in "we".
- **Objectives, summaries, introductions**: none printed; `objectives` and `summary_html` empty; no chapter introduction page.

## Bridges this chapter needs (from the reconciled list, updated for decision 18)

| id | where | what it carries |
|---|---|---|
| B1 | 1.1 lead | 0.3 is carried, so the worked example is in place. Still open: Erickson 0.5 mentions the compass-and-straightedge algorithm of `jeffe:0.2` "Compass and Straightedge", which has no concept row. Either that subsection is carried with the 0.2 blocks (609 words, no concept), or the lead names it in one clause |
| B2 | 1.4 lead | the Running Time passage analyses BottlesOfBeer, the two multiplications and ApportionCongress from 1.1; its pseudocode counts from 1 |
| B3 | 1.6 lead | three notations on one page now: brisk Pr(A), Pr(A\|B); MCS Pr[R = x]; ODS Pr{·} and E[·]. The lead says they mean the same |
| B4 | — | replaced by the `random-variable` block (decision 18) |
| B5 | 1.1 | a reference fix, not prose: ODS's `\chapref{arrays}` and `\chapref{linkedlists}` become links to 2.2 and 2.5–2.6 |

## Errata to attach as correction notes

From `judgements/ch01-03-reconciled.md`, numbered as there:

1. ODS asymptotic notation: "for any constants a, b, c > 0" — the last inclusion needs c > 1.
2. ODS asymptotic notation: "demonstrably different big-Oh running times … certain … faster" needs Θ; the note points to `big-omega-theta`.
3. ODS rbs: "for a non-negative integer k" — the bound needs k ≥ 1.
4. ODS factorials: the integration variable is written n.
5. ODS coin-tosses lemma: linearity over an infinite sum without saying the terms are non-negative (valid; a note on the silent step).
6. Erickson 0.3, Figure 0.5: `Pop[i]/√2` should be `Pop[s]`; "n − R" should be R − n. Applies now that 0.3 is carried; the correction goes through the figure row's `figure` field.
7. Erickson 0.6: "T(x, y) ≤ T(⌊x/2⌋, 2y) + 2" — up to 4 operations per step (the O(log x) result stands).
8. Erickson 0.6: "unsorted array" contradicts 0.3's "sorted array".
9. Erickson 0.6: "twice much time" — missing "as".
10. OpenDSA AnalLower: "the upper and lower bounds always meet" — contradicted by its own footnote.
11. brisk counting: the printed digits of 52! are wrong after the eleventh.
12. brisk probability: "total number of events" should be outcomes.
14. OI Wiki amortized analysis: m is the full array's size in 聚合分析 and its capacity in 势能分析 (a notation note).

(13, brisk's Sonic numerator, is outside the locator and does not apply.) The second judge also noted that ODS's T(n) ≤ 2 log n + O(1) is weaker than the equality it means; not false, no note proposed.

## Indexing, as each lead must state it

| § | convention |
|---|---|
| 1.1 | mixed: Erickson's digit arrays are 0-based (X[0..m−1], digit i weighs 10ⁱ); Pop[1..n] and Rep[1..n] in 0.3 are 1-based |
| 1.2 | none; log means log₂, ln is natural |
| 1.3 | 0-based (ODS's loop examples) |
| 1.4 | mixed: Erickson 1-based (for i ← 1 to n); ODS has no arrays |
| 1.5 | none; OI Wiki writes n for the element count and m for the capacity (in 聚合分析, m is the array's size when full) |
| 1.6 | none; tosses and indicators are numbered 1..k |

## Derivations (root item 29), candidates for the plans

| § | candidate | why it qualifies |
|---|---|---|
| 1.2 | ODS change of base and ln k = (ln 2) log k | printed as equations; short, may fall below the bar |
| 1.2 | ODS harmonic bounds by two integrals, ln k < H_k ≤ ln k + 1 | a printed argument with a figure |
| 1.3 | ODS 5n log n + 8n − 200 ≤ 13 n log n for n ≥ 2 | printed as a chain of inequalities |
| 1.4 | Erickson's recurrences for PeasantMultiply and the songs | printed as equations; erratum 7 sits inside |
| 1.5 | OI Wiki aggregate sum ≤ 3n; potential Φ(h) = 2n − m, amortised cost 1 + 2 = 3 | printed as equations (translated) |
| 1.6 | ODS linearity of expectation; the coin-tosses lemma's proof | a printed proof qualifies by rule |

## Exercises that belong elsewhere

- Held for chapter 4 (recursion): Erickson chapter 1's Factorial item (it tests lattice and peasant multiplication as subroutines and factorials, but needs recursion).
- Held for chapters 3, 5 and 8: ODS chapter 1 exercises 1, 5, 6 and 7 (they assume Stack, Queue, Deque, USet and SSet).
- Held for chapter 22: MIT 6.856J homework (NC).
- From chapter 3 into 1.5: MIT 6.046J S15 4-1 "Extreme FIFO Queues" (NC) is also ranked for 3.4's queue-from-two-stacks; it goes with 1.5 (amortized analysis), and 3.4's notes say so.

## The chapter's answer to root rule 23: what would make this stunning

This chapter is usually taught as a wall of notation. The sources' own examples are concrete (a song, a multiplication by hand, Congress's seats, a dynamic array filling up, coin tosses), and each can run in front of the reader with the bound checked against the run.

- **1.1, the multiplications run.** Peasant multiplication beside Erickson's PeasantMultiply, stepping by block ("halve x, double y", "if x is odd, add y"), the halving column revealing x's binary digits as the rows it keeps; the lattice grid filling one digit product per step, the diagonals carrying. One counter on each: rows ⌊log₂ x⌋ + 1, products m·n. Side by side on the same numbers, the reader sees why one is O(log x · log y) and the other O(mn).
- **1.1, Congress apportioned.** ApportionCongress on a small set of states: each seat goes to the state with the largest Pop/√(r(r+1)), the priority queue drawn as a sorted column; the predict pause asks which state takes the next seat. It is the first time the reader meets a priority queue, as a thing that works, nine chapters before its theory.
- **1.2, logarithms as halving.** ODS's "the number of times k can be divided by b before the result is at most 1": a bar halved (or thirded, or divided by e) until it fits, the count matching log_b k on the readout.
- **1.2, the harmonic integral.** ODS's harmonic figure live: bars of height 1/i over 1/x, the two integrals' areas bounding H_k, a slider on k.
- **1.3, Big-O as a witness.** ODS's own example drawn: f(n) = 5n log n + 8n − 200 against c·g(n), sliders on c and n₀, the region where f ≤ c·g shaded and the first n where it fails marked. Setting c below 5 shows that no n₀ works. A second figure: the growth race on log–log axes with OpenDSA's "a machine ten times faster" as a slider, the problem size each class gains printed per curve.
- **1.4, counting a loop.** ODS's `for (i = 0; i < n; i++) a[i] = i` stepping by block, each primitive operation ticking its own counter (1 assignment, n + 1 comparisons, n increments, n offsets, n stores), the totals summing to the bound.
- **1.5, three ways to pay for doubling.** One dynamic array filling up, the method a choice: aggregate (the total copies under the line 3n), accounting (coins on each pushed cell, spent when the array doubles: OI Wiki's credit trace, redrawn from its prose), potential (Φ = 2n − m drawn as a graph under the cost bars, the readout "amortised = actual + ΔΦ = 1 + 2 = 3" true at every step). The reader sees that the three methods give the same 3 by different bookkeeping.
- **1.6, coin tosses until heads.** Many runs at once, the running mean of the number of tosses settling at 2 (ODS's lemma), the per-toss indicators stacked so the sum is visibly the sum of expectations.

Plan lines (root format with the RULES extension):

```
sim-peasant · Sim (original: Erickson's duplation trace) · peasant-multiplication · flow by animation; standardisation · arrows: kinematic (x halves, y doubles) · moving: one row per step · code: jeffe:0.2 PeasantMultiply, Erickson pseudocode · blocks: halve "halve x, double y"; add "if x is odd, add y to the product" · invariant: rows kept so far · readout "prod + x·y = 123 × 456" · cost: rows against ⌊log₂ x⌋ + 1 · inputs: 123 × 456 (Erickson's) | powers of two | editable · headline "x·y never changes" · graph: none · 2D
sim-lattice · Sim (original: Erickson's lattice figure) · lattice-multiplication · flow by animation · arrows: symbolic (carries along a diagonal) · moving: one digit product per step, then the diagonal sums · code: jeffe:0.2 lattice pseudocode, 0-based digit arrays · cost: single-digit products against m·n · inputs: Erickson's numbers | editable · 2D
sim-apportion · Sim · algorithm (worked example), describing-algorithms · variation by input · arrows: kinematic (a seat moving to a state) · moving: one seat per step · code: jeffe:0.3 ApportionCongress · blocks: init "one seat each, priorities Pop/√2"; seat "give the next seat to the largest priority, update its priority" · readout "seat 51 → state s, priority Pop[s]/√(r(r+1))" · inputs: three-state toy | Erickson's | editable · predict pause: which state takes the next seat · 2D
sim-halving · Sim · logarithms · variation by slider · arrows: none · still · slider k (1..10⁶, log), choice base (2 | e | 10) · readout "log_b k = ln k / ln b" · 2D
sim-harmonic · Sim (original: ODS harmonic-2, harmonic-3) · harmonic-numbers · variation by slider · still · slider k · readout "ln k < H_k ≤ ln k + 1" with live values · 2D
sim-big-o-witness · Sim (original: ODS bigoh-1, bigoh-2) · big-o, big-omega-theta · variation by slider · still · sliders c, n₀ · special: c = 5 (below it no n₀ works) · readout "f(n) ≤ c·g(n) for all n ≥ n₀: holds | fails at n = …" · graph: alone · 2D
sim-growth-race · Sim · big-o, need-for-efficiency · variation by slider · still · slider: machine speed-up (1×..1000×), n · graph: alone, log–log · 2D
sim-loop-count · Sim · complexity-analysis, word-ram · flow by animation · moving · code: ods Simple.snippet() (Java) · blocks: init; test; body; step · cost: each primitive against its count in n · inputs: n slider · 2D
sim-pay-for-doubling · Sim · amortized-analysis, aggregate-accounting, potential-method · variation by choice; flow by animation · arrows: kinematic (elements copied into the new array) · moving: one push per step · choice: method (aggregate | accounting | potential) · invariant: credits ≥ 0 | Φ ≥ 0 · readout "amortised = actual + ΔΦ = 1 + 2 = 3" · cost: total copies against 3n · inputs: pushes only | push and pop at the boundary · 2D
sim-coin-tosses · Sim · geometric-expectation, linearity-of-expectation, indicator-variables · variation by slider · moving: runs accumulate · slider: p (0.1..0.9), runs · readout "mean tosses 2.03 · 1/p = 2" · 2D
```

None of these uses `weight` or a system design type. Referents: x and y (sim-peasant), the states (sim-apportion, named by the text), `i` (sim-loop-count). Types drawn: `cost` everywhere, `size` (n, k, m), `key` (the digits and numbers multiplied), `index` (i in the loop).
