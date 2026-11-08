# Chapter 1 plans: summary and questions

Status: **for review**, 2026-11-08 (root item 5: each plan is reviewed before its page is written; root item 16: the loop waits for every answer). Six plans, `ch01/1.1/plan.md` to `ch01/1.6/plan.md`, folders named as the model books name theirs. Nothing else was written: no `source.md`, `text.html`, `figures.js` or `section.json`, and no commit.

## The six sections

**1.1 What an algorithm is.** Ten blocks: eight from Erickson's chapter 0 in his own order (0.1, the 0.2 preamble with Lattice Multiplication, Duplation and Mediation, Compass and Straightedge, 0.3 whole, 0.4, 0.5, 0.6's opening with Correctness), then ODS's The Need for Efficiency and Interfaces. Eight concepts, two of them Advanced (lattice multiplication, Huntington–Hill). Four code-beside Sims (`sim-lattice` on the Treviso numbers 934 × 314, `sim-peasant` on 123 × 456 with the invariant prod + x·y, `sim-compass` stepping into RightAngle, `sim-apportion` on the House), one still Sim (`sim-scan-cost`, ODS's 10¹² inspections), and Erickson's two historical scans kept as photographs. Erratum 6; B5 as two links; no derivation passes the bar.

**1.2 Logarithms, factorials and harmonic numbers.** Three ODS blocks, three concepts (harmonic numbers Advanced). Three still Sims (`sim-halving`, `sim-harmonic` folding ODS's two harmonic panels, `sim-stirling`, new). Two derivations: the change of base (printed) and the harmonic bounds (hidden, score 5). Errata 3 and 4. One question on whether the harmonic block keeps its random-BST opening, with a bridge to 8.6 if it does.

**1.3 Asymptotic notation.** ODS's Asymptotic Notation, then OpenDSA's Lower Bounds and Θ and its Multiple Parameters. Three concepts (multivariate Advanced). Four Sims: `sim-crossover` (ODS's two plots of 15n against 2n log n as one zoom), `sim-big-o-witness` (c = 13, n₀ = 2), `sim-loop-count` (moved here from 1.4, since its code and counts are in this block) and `sim-limit-test` (in place of OpenDSA's uncached slideshow). One derivation (ODS's 13 n log n chain). Errata 1, 2, 10. OpenDSA's two code fragments are not cached, and Multiple Parameters does not read without its own.

**1.4 Analysing running time and space.** ODS's word-RAM, Erickson's Running Time, ODS's three guarantees. Three concepts, all Essential; B2 in the lead. One code-beside Sim, `sim-song-count` (Bottles of Beer and The Twelve Days, counts against 3n + 3, n(n + 1)/2 and n(n + 1)(n + 2)/6 on log–log axes). Errata 7, 8, 9. No derivation built: the nested sum needs Σi², which the book never states, and the peasant recurrence is deferred by Erickson to the recursion chapter.

**1.5 Amortized analysis.** All of OI Wiki's page, translated, in five blocks in OI Wiki's own order (amortized analysis with the aggregate method; the accounting method; the potential method; the stack by aggregate and accounting; the stack by potential). Three concepts (potential method Advanced). One moving Sim, `sim-pay-for-doubling`, standing where OI Wiki's unlicensed credit trace stood, with a choice of method. Two derivations (the telescoping sum and the two insert cases). Erratum 14. A new bridge, B-new-a, points to stacks in 3.1. NC cards only.

**1.6 Counting and expected value.** brisk's counting, probability and conditional probability, MCS 19.1 for random variables, ODS for expectation, indicators and the coin-tosses lemma. Seven concepts (indicators Advanced); B3 in the lead with MCS's notation added. Three Sims: `sim-pascal`, `sim-idol-venn` (conditioning fades the outcomes ruled out), `sim-coin-tosses` (indicators stacked run by run, with no p slider). Two derivations (expected heads two ways; the coin-tosses proof, erratum 5 as its node note). Errata 5, 11, 12. Several extent questions on brisk and MCS.

Across the chapter: 31 blocks (32 with brisk’s interlude), 27 concepts, 17 Sims, 2 photographs, 7 derivations, 13 errata notes, bridges B2, B3 and two new ones, and B5 as links. Every check item waits for the OpenDSA converter, every code item for the `code` answer type, and the two trace items for `sequence`.

## Questions for the user

Each has a recommendation; the plans assume it unless told otherwise.

### Source extents and references that point off the page

1. **ODS edition.** ODS prints edition-dependent text and code (`\javaonly`, `\cpponly`; the pseudocode edition prints neither). It decides 1.3's loop snippet and 1.4's last word-RAM paragraph ("the (32-bit) JVM when w = 32" or "modern desktop computers when w = 32 or w = 64"). Which edition does the book use? *Recommended: Java, the edition the judges quoted, for every ODS page.*
2. **ODS efficiency, last paragraph (1.1).** "The remainder of this chapter briefly reviews … Section 1.2 describes the interfaces … should be considered required reading" describes ODS's chapter, not this book's. End the block before it? *Recommended: yes, the locator saying so in words.*
3. **ODS harmonic opening (1.2).** The digression begins "Before we can present our main result about random binary search trees, we must take some time for a short digression…". Start the block at "For a non-negative integer, k, …", or keep it and add the bridge B-new-b ("Harmonic numbers return with random binary search trees in 8.6.")? *Recommended: keep the sentence and the bridge, since the source is kept whole.*
4. **brisk's pointers to its own chapters (1.6).** "As mentioned in section [Total probability], the Σ notation…", "just like in chapter 1 … the domain of discourse", "recall the 'total complement' operator from p. [Sets]". None of the targets is in this book. *Recommended: print the source's words with the reference as plain text (no link), and a correction-style note only where the sentence misleads; ask if a note is wanted for each.*
5. **brisk's set notation (1.6).** brisk leans on its chapter on sets (Ω, ℙ(Ω), Ā, ∪, ∩), and the map has no sets concept. A pointer does not fit the 1.6 lead with B3 (68 words now). Options: (a) accept it, the notation being widely known; (b) add a sets concept and carry brisk's Sets passage as a block; (c) a second lead sentence over 80 words (decision 19 sends this to you). *Recommended: (a).*
6. **brisk's Philosophical interlude (1.6).** "Conditional probability" opens "I mentioned that Bayesians are especially concerned…", which points at the interlude. Carry it whole as context (≈ 640 words, no concept row), the rule that carried Erickson's "Compass and Straightedge"? *Recommended: yes.*
7. **brisk's counting extent (1.6).** Omit "Enumerating permutations" (recursive enumeration of RISK and BRISK, the judge's suggestion)? Keep "Binomial coefficients" (it carries Pascal's triangle, `sim-pascal` and the pascals-triangle code card)? Leave brisk's chapter "Summary" out (outside the locator)? *Recommended: omit, keep, leave out.*
8. **MCS chapter-19 opening (1.6).** Ruling 18 says it "may lead in", but it refers to the Monty Hall game and a medical test from MCS chapters this book does not carry. *Recommended: start at 19.1.*
9. **MCS 19.1.1 against ODS's indicators (1.6).** MCS's random-variable extent includes "Indicator Random Variables", so indicator variables are named twice on the page, and one explanation per concept is at stake. Keep MCS's subsection (ruling 18's extent) with `indicator-variables` introduced at ODS's span (the skill, not the term), or end MCS's block before 19.1.1? *Recommended: keep it, introducing span at ODS.*
10. **OpenDSA's self-references (1.3).** "OpenDSA modules use Θ notation in preference to big-Oh…" and "Recall the sequential search algorithm…" (sequential search is a concept nowhere in the map) stay as printed under kept-whole? *Recommended: yes; the sentence describes sequential search well enough to read.*
11. **Erickson's chapter epigraphs (1.1).** Five epigraphs stand before 0.1, in no locator. *Recommended: not carried.*

### Missing material to fetch

12. **OpenDSA code fragments (1.3).** `codeinclude:: Misc/Anal` tags c3p16 (Multiple Parameters) and Collatz (Lower Bounds) are not cached. Multiple Parameters names `count`, `value(i)`, "the first for loop" and "the call to sort" and does not read without its code. Fetch OpenDSA's `SourceCode/` (MIT, same notice)? *Recommended: yes, before 1.3 is built.*
13. **Erickson's Image Credits (1.1).** The credits for Figures 0.1 (Treviso Arithmetic) and 0.2 (Heiberg's Eutocius) are printed at the end of Erickson's book, which is not cached. *Recommended: fetch the back matter.*
14. **`sim-apportion`'s data (1.1).** Erickson prints no populations. Default to the 2020 census apportionment populations of the 50 states with R = 435 (the text's own n and R; US Census Bureau, public domain; to be fetched), so the figure reproduces the House, with an editable input and a four-state preset taken from the same table? *Recommended: yes.*
15. **Exercism references for pascals-triangle and baffling-birthdays (1.6).** Only the judge's own (AI) references were run. Fetch the Exercism Python examples (MIT), as was done for grains and difference-of-squares? *Recommended: yes.*

### Figures

16. **Changes to the seed list.** `sim-loop-count` moves from 1.4 to 1.3 (ODS's snippet and its five counts are in 1.3's `big-o` block); `sim-growth-race` is dropped (its "machine ten times faster" is OpenDSA AnalCompvsAlg, not a winner) and replaced by `sim-scan-cost` in 1.1 and `sim-crossover` in 1.3; new required figures: `sim-compass` (Figure 0.4 is a sketch figure), `sim-stirling`, `sim-limit-test`, `sim-pascal`, `sim-idol-venn`, `sim-song-count`. Approve?
17. **Code listings that become code panels.** FibonacciMultiply (printed in the prose), PeasantMultiply and ApportionCongress (inside Figures 0.3 and 0.5), MultiplyOrDivide (Figure 0.4), ODS's snippet and NDaysOfChristmas are shown once, as the Sim's code panel where the listing stood, not again as `<pre>`. Approve?
18. **Source figure numbers in kept prose.** The sources cite their own numbers ("as shown on the right in Figure 0.1", "Figure 0.5", ODS's Figure 1.5 and 7.2, brisk's Figure 4.1), and this book numbers no figure (decision 19). *Recommended: keep the printed number as a link to the Sim or photograph, whose original toggle shows the source's caption with that number.*
19. **Erratum 6 inside a code panel (1.1).** The errors are in ApportionCongress's pseudocode, which stays verbatim in `sim-apportion`'s panel. *Recommended: the numbered note's marker after the prose sentence that cites Figure 0.5; the trace computes with Pop[s] and R − n.*
20. **Generalisations dropped.** `sim-coin-tosses` loses the exploration's p slider (the page states nothing for a biased coin, so 1/p would be a result the text never gives); `sim-pay-for-doubling` loses "push and pop at the boundary" (OI Wiki never shrinks the array). Approve?
21. **`sim-compass` referents.** All ten named points and lines (A–F, Z, α, β, γ) are code variables, so the colour rule makes each a referent, one group of ten. Accept, or colour only C, D and Z (the inputs and the answer) and label the rest in ink?

### Bridges and leads

22. **New bridges.** B-new-a (1.5 lead: "The stack's push, pop and multi-pop are defined in its own table; stacks are the subject of 3.1.") and B-new-b (1.2 lead, with question 3). Both fit in 80 words. Approve the wording?
23. **Reference fixes as links.** Erickson's "the next chapter" (1.4) → 10.2; "a binary heap or a heap-ordered array" (1.4) → 9.2; ODS's `\secref{randomization}` (1.4) → 1.6; OpenDSA's NP-Complete `:ref:` (1.3) → 23.2; B5 (1.1) → 2.2 and 2.5–2.6. Approve?

### Structure

24. **1.5's block order.** Five blocks in OI Wiki's own order rather than `exploration.md`'s three, which would move the stack example's aggregate and accounting parts ahead of the potential method. Approve?
25. **Erickson's order in 1.1.** Compass and Straightedge after Duplation and Mediation, as Erickson prints it (`exploration.md` listed it before). Approve?
26. **`aggregate-accounting`'s introducing span (1.5).** The aggregate method is first named and worked in block 1 (the locator gives 聚合分析 to `amortized-analysis`), the accounting method in block 2. *Recommended: the span at the start of block 2, where the concept's home begins, with block 1's "aggregate analysis" a plain concept mention.*

### Concepts

27. **Statements reworded to the winning passage.** `multivariate-big-o` (the map's statement is ODS's formal definition, which the page does not carry; OpenDSA's is "keep each parameter"), `probability-basics` (brisk never states the product rule), `conditional-probability` (brisk's independence is Pr(A|B) = Pr(A)), `linearity-of-expectation` (ODS has no constants aᵢ and never says "no independence required"), and small rewordings of `peasant-multiplication` and `apportionment`. Approve?

### Derivations

28. **Short printed chains.** Root item 29.1 qualifies every derivation printed as a block of equations. *Recommended policy: build printed chains of three or more moves (change of base, ODS's 13 n log n, OI Wiki's telescoping sum and its two insert cases, ODS's expected heads, the coin-tosses proof) and leave one- and two-move chains as printed (ODS's T(n) = a + b(n + 1) + … = O(n); OpenDSA's Ω and limit examples; brisk's n!/(n − k)!).* Approve?
29. **Judgement calls not built.** Stirling (the hinted integral does not reach the stated formula; 1.2), the gifts sum n(n + 1)(n + 2)/6 (needs Σi², stated nowhere in the book; 1.4), the peasant recurrence (Erickson defers it to the recursion chapter; 1.4). Agree?

### Exercises

30. **AlgAnlsFIBsmlintgr2.** It asks for the smallest k with n log n in O(nᵏ); config places it in 1.2, root item 12 sends it to 1.3 (it tests Big-O). *Recommended: 1.3, tagged with both.*
31. **6.046J S15 ps4 4-1 "Extreme FIFO Queues".** It needs queues (3.2). Config item 24 and `exploration.md` place it in 1.5; config item 23 sends an item spanning two sections to the later one (3.4). Which? *Recommended: 3.4, tagged amortized-analysis and potential-method, with 1.5's notes saying so.*
32. **brisk probabilityEx item 18.** It is solved by Bayes' Theorem, which no carried block states. *Recommended: leave it out and name it in `exercise_notes` (or carry brisk's "Bayes' Theorem" and "Total probability" sections, which brings erratum 13 back).*

### Spelling

33. **"amortized" or "amortised".** The book's `RULES.md` and `COLOR.md` write "amortised" in places; the sources, the chapter title and the field's standard term write "amortized". *Recommended: "amortized" in translations and OmniStax text, the sources' spelling kept as printed.*
