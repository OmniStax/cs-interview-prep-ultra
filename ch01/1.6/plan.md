# Plan: 1.6 Counting and expected value

Status: **plan for review** (root item 5), 2026-11-08. Nothing is built. Read for this plan: as 1.1, plus `brisk/counting.tex` (whole), `brisk/probability.tex` (whole), `brisk/countingEx.tex` and `probabilityEx.tex`, MCS 2018 pp. 857–859 from the PDF (§19 opening, 19.1, 19.1.1, 19.1.2; the cached `.txt` renders "=" as "D"), `ods/latex/intro.tex` lines 673–762 and `ods/latex/skiplists.tex` lines 307–332.

Sources: brisk (CC BY-SA 4.0), MCS 2018 (CC BY-SA 3.0), ODS (CC BY 2.5 Canada). No translation. 7 blocks (8 if the Philosophical interlude is carried), 7 concepts, 3 Sims, 2 derivations.

## Lead (draft, AI-marked, carries B3, 68 words)

> Essential; indicator random variables are Advanced. Counting, then probability, conditional probability, random variables and expectation. The three sources write probability three ways that mean the same thing: Pr(A) and Pr(A|K), with sample space Ω; then Pr[C = 2] for the event that C equals 2, with sample space S; then Pr{X = i}, with E[X] for an expected value. Coin tosses and indicator variables are numbered from 1.

Tier: Essential. Of another tier: `indicator-variables` (Advanced). Indexing: none (tosses and indicators 1..k). Bridge **B3** (decision 19: one lead sentence on the notations), extended with MCS's notation and the two names of the sample space (ruling 18). brisk also leans on its own chapter on sets (Ω as the domain of discourse, ℙ(Ω), Ā, ∪, ∩), which this book has no concept for; a pointer would not fit in the 80 words (Questions).

## Sub-concept blocks (`<h2>`)

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `counting` | Counting (OmniStax: three brisk sections in one block need one name) with The Fundamental Theorem, Permutations, Partial permutations, Combinations and Binomial coefficients as `<h3>` | brisk | `brisk:counting#The Fundamental Theorem` (with "A simple trick"), `#Permutations` (with "Partial permutations"; "Enumerating permutations" omitted?), `#Combinations` (with "Binomial coefficients"?) | no | the Fundamental Theorem of Counting (framed), Lamborghini, PINs, licence plates, the complement trick; n! and 0! = 1, KRIBS, 52! (erratum 11); n to the k falling, golfers, NASCAR; combinations, 45·44·43/3! = 14,190, (n choose k); binomial coefficients and Pascal's triangle (→ `sim-pascal`). brisk's footnotes (the "Fundamental Theorems", War) as book footnotes. **Extent questions:** "Enumerating permutations" (recursive enumeration, ≈ 600 words), "Binomial coefficients" (keeps `sim-pascal` and the pascals-triangle code card) and brisk's chapter "Summary" (outside the locator) |
| 2 | `probability` | Outcomes and events (source), Probability measures as `<h3>` | brisk | `brisk:probability#Outcomes and events`, `#Probability measures` | no | outcome, sample space Ω, event, ℙ(Ω), probability measure, All-time Idol (.2, .2, .1, .5), the three rules and three more, the Venn figure (→ `sim-idol-venn`), equally likely outcomes (erratum 12) |
| (2a) | `interlude` | Philosophical interlude (source) | brisk | `brisk:probability#Philosophical interlude` (whole, ≈ 640 words) | no | **only if carried** (Questions): frequentist and Bayesian views; the next block opens "I mentioned that Bayesians are especially concerned…", which points here. No concept row, as Erickson's "Compass and Straightedge" (book `RULES.md`, Apparatus: an aside a later passage refers to is carried whole) |
| 3 | `conditional` | Conditional probability (source), Independence and "Whoops!" as `<h3>` | brisk | `brisk:probability#Conditional probability`, `#Independence` | no | Pr(A\|K), the prior, Pr(U\|F) = .8, Pr(R\|F) = .4, the restricted world, Pr(X\|Y) ≠ Pr(Y\|X); independence as Pr(A\|B) = Pr(A), the handedness table (kept as a table), mutually exclusive is not independent |
| 4 | `random-variable` | Random Variable Examples (source), Indicator Random Variables and Random Variables and Events as `<h3>` | mcs2018 | `mcs2018:19.1` through 19.1.2, ending before §19.2 | no | Definition 19.1.1 as `div.note` ("Definition 19.1.1"), the three coins, C and M as functions, indicator variables (M), events [C = 2], Pr[C = 2] = 3/8, [C ≤ 1]. Transcribed from the PDF. The chapter-19 opening (Monty Hall, a medical test) is not carried (Questions) |
| 5 | `linearity` | Randomization and Probability (source) | ods | `ods:intro#sec:randomization`, from the start to "…into sums of simpler random variables (the right hand sides)." | no | randomized structures, expected running time, E[X] = Σ x·Pr{X = x}, linearity of expectation. 1.4's `\secref{randomization}` links here |
| 6 | `indicators` | Indicator random variables (OmniStax: the passage continues ODS's subsection without a heading) | ods | `ods:intro#sec:randomization`, from "A useful trick…" to the end of the subsection | no | k fair tosses the hard way (→ `drv-heads`), then with indicators |
| 7 | `coin-tosses` | Tosses until the first head (OmniStax: a lemma lifted from ODS's skiplists) | ods | `ods:skiplists#lem:coin-tosses` (lemma and proof) | no | Lemma as `div.note` (eyebrow "Lemma"), its proof (→ `drv-coin-tosses`), erratum 5 |

Cross-references inside brisk that point outside the page (Questions): "As mentioned in section [Total probability], the Σ notation is essentially a loop with a counter" (block 1), "just like in chapter 1 every conceivable element was a member of the domain of discourse" (block 2), "recall the 'total complement' operator from p. [sets]" (block 2), "Looking back at Figure [venn]" (block 3, resolves to `sim-idol-venn`).

## Concepts

| id | kind | tier | statement | introducing span |
|---|---|---|---|---|
| `counting` | result | Essential | If a whole has k parts with n_i choices each, there are n₁ × … × n_k ways; so n! orderings of n items, n!/(n − k)! ordered selections of k, and (n choose k) = n!/((n − k)! k!) unordered ones. | `counting`, "*The Fundamental Theorem of Counting*" |
| `probability-basics` | definition | Essential | Outcomes form the sample space Ω, an event is a subset of it, and a probability measure Pr assigns each event a number in [0, 1] with Pr(Ω) = 1, Pr(A) ≥ 0 and Pr(A ∪ B) = Pr(A) + Pr(B) − Pr(A ∩ B); with N equally likely outcomes, Pr(A) = \|A\|/N. | `probability`, "is called an *outcome*" |
| `conditional-probability` | definition | Essential | Pr(A\|K) = Pr(A ∩ K)/Pr(K), the probability of A once K is known to have occurred; A and B are independent when Pr(A\|B) = Pr(A). | `conditional`, "*conditional probability*" |
| `random-variable` | definition | Essential | A random variable R on a probability space is a total function whose domain is the sample space, usually real-valued; an assertion about its value, such as [C = 2], is an event. | `random-variable`, Definition 19.1.1 |
| `linearity-of-expectation` | result | Essential | E[X] = Σ_x x·Pr{X = x}; for any random variables, E[X + Y] = E[X] + E[Y] and E[Σ X_i] = Σ E[X_i], so a complicated random variable can be split into simpler ones. | `linearity`, "*linearity of expectation*" |
| `indicator-variables` | skill | Advanced | Write a count as a sum of indicator variables I_i (1 if the i-th event happens, else 0); then E[Σ I_i] = Σ Pr{I_i = 1}, as for the k/2 expected heads in k fair tosses. | `indicators`, "*indicator random variables*" (MCS's block 4 names indicator variables first; see Questions) |
| `geometric-expectation` | result | Essential | If T counts fair coin tosses up to and including the first head, E[T] = 2. | `coin-tosses`, the lemma's statement |

Four statements are reworded from `concepts.json` to what the winning passage says: `probability-basics` (brisk never states the product rule for independent events), `conditional-probability` (brisk's independence is Pr(A\|B) = Pr(A)), `linearity-of-expectation` (ODS has no constants aᵢ and never says "no independence required"), `random-variable` unchanged. See Questions.

## Errata notes

- **5** (`coin-tosses`, as the derivation's node `note`; the printed proof is replaced by the derivation): the step E[Σ_{i=1}^∞ I_i] = Σ_{i=1}^∞ E[I_i] applies linearity, stated for finite sums, to an infinite sum; it holds here because every I_i is non-negative.
- **11** (`counting`): the printed value of 52! is wrong after its eleventh digit; 52! = 80,658,175,170,943,878,571,660,636,856,403,766,975,289,505,440,883,277,824,000,000,000,000. Marker after the printed number.
- **12** (`probability`): "the ratio of this number to the total number of events" should read "outcomes" (N = \|Ω\|). Marker after the sentence.

## Derivation candidates

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| ODS: E[X] = Σ i·Pr{X = i} = Σ i·C(k, i)/2ᵏ = k·Σ C(k − 1, i)/2ᵏ = k/2 (the hard way) | an `align` block | 4 printed, 2 inserted (the index shift, Σ C(k − 1, i) = 2^{k−1}) | printed: qualifies | **build** `drv-heads`, *Derivations · the expected number of heads in k tosses*, two independent lines to the one result k/2: the hard way (facts: the definition of E[X] (block 5); Pr{X = i} = C(k, i)/2ᵏ; i·C(k, i) = k·C(k − 1, i − 1); Σ C(k, i) = 2ᵏ, all three stated in the next ODS sentence) and the indicator way (facts: X = Σ I_i; E[I_i] = 1/2; linearity, result of block 5). It replaces both `align` blocks; ODS's words between them stay |
| ODS coin-tosses lemma: E[T] = E[Σ I_i] = Σ E[I_i] = Σ 1/2^{i−1} = 1 + 1/2 + 1/4 + … = 2 | a printed proof | 4 | printed proof: qualifies by rule | **build** `drv-coin-tosses`, *Derivation · the expected number of tosses until the first head*, replacing the proof's `align`; facts: I_i = 1 iff the first i − 1 tosses are tails, E[I_i] = 1/2^{i−1}, T = Σ I_i (the proof's own), linearity (result, links to `drv-heads`'s source block); erratum 5 as the node note on the linearity step |
| brisk partial permutations: n × (n − 1) × … × (n − k + 1) = n!/(n − k)! | an `align` block | 2 | printed: qualifies | **recommend not built** (two moves; see Questions on short printed chains) |
| brisk Pr(U ∪ C) = .4 + .1 − 0 = .5; Pr(U\|F) = .4/.5 = .8; Pr(R\|F) = .2/.5 = .4; 45·44·43/6 = 14,190; Pr(F) = 12/52 | printed | — | — | never: worked examples that substitute numbers into the section's formula |
| MCS Pr[C = 2] = 1/8 + 1/8 + 1/8 = 3/8 | one display | — | — | never (substitution) |

## Figures

```
sim-pascal · Sim (original: brisk "The first six rows of Pascal's triangle", printed as Figure 6.1) · counting · variation by slider · arrows: symbolic (the two entries above feeding the chosen one, drawn once per change) · still · sliders n (size, 0..12, default 4, the text's worked row) and k (0..n, default 2) with dashed circles at k = 0 and k = n (both always 1, the text's endpoints) and at k = n/2 (the largest, the text's "k half of n") · headline "Row 4 reads 1, 4, 6, 4, 1: six ways to take two of four." · graph none: the triangle, rows 0..n, the chosen entry and its mirror (n choose n − k) marked · 2D · code: none (brisk prints no code; a property) · readout "C(4, 2) = 4!/(2!·2!) = 6 = C(3, 1) + C(3, 2)", with a note line for the mirror when k ≠ n/2 ("C(4, 1) = C(4, 3) = 4")
sim-idol-venn · Sim (original: brisk "Various events, and their overlap", Figure 4.1) · probability-basics, conditional-probability · variation by choice · arrows: none · still, morphing on each choice (the conditioned-away outcomes fade to ink: brisk's "mentally block out everything except that") · choice A: F | R | U | C; choice B: F | R | U | C; choice operation: A ∪ B | A ∩ B | A given B · headline "Given a woman wins, David is out, and Kelly and Fantasia hold .4 of the .5 that is left." · graph none: the four outcomes with their probabilities, the three events as closed curves, the fourth (C = {Carrie}) drawn when chosen · 2D · code: none · readout "Pr(U ∪ R) = .4 + .7 − .2 = .9" or "Pr(U|F) = Pr(U ∩ F)/Pr(F) = .4/.5 = .8"
sim-coin-tosses · Sim · geometric-expectation, linearity-of-expectation, indicator-variables · flow by animation; variation by choice and slider · arrows: none · moving: tosses accumulate run by run (a seeded run, so scrubbing is exact) · choice question: heads in k tosses | tosses until the first head · sliders k (size, 1..20, default 10; the heads question only) and runs (1..1000) · headline "After 200 runs the mean number of tosses is 2.03; the lemma says 2." · graph beside: each run as a row of indicator cells I₁, I₂, … (1 filled, 0 hollow), the column means E[I_i] as bars beside 1/2^{i−1} (or 1/2), and the running mean against runs with the expectation dashed · 2D · code: none (config item 16) · readout "E[T] = Σ E[I_i] = 1 + 1/2 + 1/4 + … = 2 · mean of 200 runs = 2.03" or "E[X] = Σ E[I_i] = k · 1/2 = 5 · mean of 200 runs = 4.97". No p slider: ODS's coin is fair and the page states no formula for a biased one, so a p slider would show a result (1/p) the text never gives.
```

**Source figures, keep or drop.** brisk's Venn diagram → `sim-idol-venn`; brisk's Pascal's triangle → `sim-pascal` (only if "Binomial coefficients" is carried); the handedness contingency table stays a table; the boxed RISK/BRISK lists (if "Enumerating permutations" is carried) stay as lists. MCS's partition displays (underbraced blocks of outcomes) stay as display maths. ODS's blocks have no figures.

## Extra simulations

- `sim-three-coins`: MCS's three coins, the eight outcomes in a row, C and M drawn as arrows from each outcome to its value, a choice of assertion ([C = 2], [C ≤ 1], [C·M is odd]) lighting the event it defines and its probability, so "a random variable is a function" is seen rather than read.
- `sim-golf-trios`: the 3! = 6 orderings of Bubba, Phil and Tiger collapsing into one trio, then 45³ falling ordered finishes collapsing by 3! into 14,190 trios, for brisk's "divide out the overcount".

## Exercises

| concept | kind | items | answer shape | status |
|---|---|---|---|---|
| counting | exercise | brisk countingEx items 1–5 (keyed: 180, 300, 10,240, 2,580, 8,250) | `number`, brisk's answer as the solution | ready; item 2's "skip one or more of the items" admits the empty costume, which 300 counts: a correction note under its card |
| counting | code | exercism pascals-triangle (8 tests) | `code` | **waits for the `code` type**; the reference is the judge's own (AI) unless the Exercism Python example is fetched as for grains |
| counting | code | kattis anagramcounting (CC BY-SA 3.0, AI tests and reference) | `code` | waits for the `code` type |
| counting | NC card | mitocw-6-042j-fall2005 ps7 #1–#5 | `open` | `exercises-nc.json` |
| probability-basics | exercise | brisk probabilityEx items 1, 4, 6, 7, 8 | `choice` (1, 4: yes/no), `choice` (6), `number` (7: .1; 8: .8) | ready |
| probability-basics | code | exercism baffling-birthdays (17 tests; the estimate cases need `tol`) | `code` | waits for the `code` type; reference as for pascals-triangle |
| probability-basics | code | kattis dicecup (AI tests) | `code` | waits for the `code` type |
| probability-basics, conditional-probability | NC card | mitocw-6-042j-fall2005 ps9 #1–#7 | `open` | `exercises-nc.json` |
| conditional-probability | exercise | brisk probabilityEx items 16, 17 (item 9's set-up on each card); item 18 | `number` (.143, .75); 18: `number` (.5) | 16 and 17 ready; **item 18 needs Bayes' Theorem**, which no carried block states (Questions) |
| conditional-probability | exercise | wikibooks Probability/Conditional_Probability, its first two keyed exercises | `number` or `open` per the key | ready |
| linearity-of-expectation | exercise | aspnes-202 C.9.3, F.5.3, F.5.4 | `open`, the key as solution | ready (check at build that they need nothing beyond this page, Aspnes writes E[·] and Pr[·]) |
| linearity-of-expectation, random-variable | exercise | wikibooks Probability/Random_Variables, its first two keyed exercises | per the key | ready |
| linearity-of-expectation (#1 + geometric-expectation, #8 + indicator-variables) | NC card | mitocw-6-042j-fall2005 ps10 #1–#8; mitocw-6-006-spring2020 ps0 0-2 | `open` | `exercises-nc.json` |
| indicator-variables | code | kattis fruitbaskets (AI tests) | `code` | waits for the `code` type |
| random-variable | — | none ranked | — | — |

`exercise_notes`: the partly keyed Levin (dmoi3) and Applied Combinatorics sets, MCS 15–19's problems, OpenIntro's and the unkeyed Erickson-notes probability exercises left out; Project Euler 15 and 53 left out (statement only); kattis expectedearnings (a weak fit) and the six flagged Kattis items not used; no `trace` item.

## Referents

| id | what | figures | blocks |
|---|---|---|---|
| `kelly`, `fantasia`, `carrie`, `david` | the four All-time Idol finalists, the outcomes | sim-idol-venn | `probability`, `conditional` |
| `F`, `R`, `U`, `C` | the events "a woman wins", "a rock singer wins", "an underage winner", "a country singer wins" | sim-idol-venn | `probability`, `conditional` |

One group of eight. No referent in `sim-coin-tosses` or `sim-pascal` (no named code variable; T, X and I_i are random variables, untyped, except that a random variable that is a running time would be `cost`, and none is here). Probabilities, events, outcomes, counts of orderings and E[·] stay in ink (book `RULES.md`, untyped); n and k as sizes of a set wear `size`.

## References item

- "Math Skills: How to find Factorial, Permutation, and Combination (Choose)" (video, CIU): a short drill on the three counting formulas.
- MIT 6.042J, "Random Variables" and "Expectation I" (videos, CC BY-NC-SA, CIU): the MCS authors' own lectures on blocks 4–7.
- Khan Academy, "Basic Theoretical Probability" (CIU): short practice on equally likely outcomes.

## Attribution

- Stephen Davies, *A Cool Brisk Walk Through Discrete Mathematics*, https://github.com/divilian/cool-brisk-walk (4b9934b), CC BY-SA 4.0, adapted.
- Eric Lehman, F. Thomson Leighton and Albert R. Meyer, *Mathematics for Computer Science* (2018), https://courses.csail.mit.edu/6.042/spring18/mcs.pdf, CC BY-SA 3.0, adapted.
- Pat Morin, *Open Data Structures*, https://github.com/patmorin/ods (9d22c44), CC BY 2.5 Canada, adapted.
- `notes`: "The unkeyed and partly keyed problem sets on counting and probability are not included." `ai`, `built`.
