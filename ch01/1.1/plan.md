# Plan: 1.1 What an algorithm is

Status: **plan for review** (root item 5), 2026-11-08. Nothing is built: no `source.md`, `text.html`, `figures.js` or `section.json` yet. Read for this plan: root `RULES.md`, the book's `RULES.md`, `COLOR.md` and `METHOD.md` (§1–§3, decisions 1–19), `ch01/config.md` and `exploration.md`, `judgements/ch01.md`, `ch01-03-reconciled.md`, `ch01-03-references.md`, the 1.1 rows of `concept-map/concepts.json`, and the winning passages: Erickson chapter 0 from the PDF (`sources/_cache/jeffe/00-intro.pdf`, text and page renders of pp. 5–9; the digits and small-caps names are lost in both the `.txt` and `pdftotext`, so every number and procedure name below was read off the rendered pages) and `ods/latex/intro.tex` lines 49–167.

Sources on the page: Erickson (`jeffe`, CC BY 4.0) and ODS (`ods`, CC BY 2.5 Canada). No translation. 10 blocks, 8 concepts, 5 Sims, 2 photographs, 0 derivations.

## Lead (draft, AI-marked, 57 words)

> Essential. What makes a procedure an algorithm, how to describe one, and why its cost matters, told through a song, three ways to multiply and the apportionment of Congress. Lattice multiplication and the Huntington–Hill method are Advanced. The digit arrays count from 0 (X[0..m−1], digit i worth 10ⁱ); Pop[1..n] and Rep[1..n] in the apportionment count from 1.

Tier: Essential. Concepts of another tier: `lattice-multiplication` (Advanced), `apportionment` (Advanced). Indexing: mixed, as above. No bridge (B1 is settled by carrying 0.3 and "Compass and Straightedge" whole; B5 is a link, below).

## Sub-concept blocks (`<h2>`), in page order

The order is Erickson's own (0.1 → 0.6 opening), then ODS's (efficiency, then interfaces, which its first sentence announces). `exploration.md` listed `compass` before `peasant`; Erickson prints Lattice, Duplation and Mediation, then Compass and Straightedge, and 0.5 refers back to all three, so the page keeps his order.

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `algorithm` | What is an algorithm? (source) | jeffe | `jeffe:0.1` | no | the definition, BottlesOfBeer as `<pre>` in Erickson's notation (transcribed from the page: "i − 1 bottles", small-caps name), the etymology; Erickson's footnotes as book footnotes under his numbers |
| 2 | `lattice` | Lattice Multiplication (source) | jeffe | `jeffe:0.2` preamble ("Although they have been a topic…") + "Lattice Multiplication" | no | the history, the digit-array specification and the double-sum formula, FibonacciMultiply (becomes `sim-lattice`'s code panel in place), Figures 0.1 and 0.2 (photographs), the O(mn) paragraph |
| 3 | `peasant` | Duplation and Mediation (source) | jeffe | `jeffe:0.2` "Duplation and Mediation" | no | the four primitives, Figure 0.3 (→ `sim-peasant`), the recursive identity, the O(log x · log y) and O(mn) analysis, the Egyptian-variant footnote |
| 4 | `compass` | Compass and Straightedge (source) | jeffe | `jeffe:0.2` "Compass and Straightedge" (whole) | no | context for 0.5, no concept row (decision 19); Figure 0.4 (→ `sim-compass`) |
| 5 | `apportionment` | Congressional Apportionment (source) | jeffe | `jeffe:0.3` (whole) | no | Article I §2 quoted, the Huntington–Hill method, Figure 0.5 (→ `sim-apportion`), the D'Hondt and Webster footnotes |
| 6 | `underspecified` | A Bad Example (source) | jeffe | `jeffe:0.4` | no | Martin's "algorithm" as `<pre>`, the reduction remark, its footnotes |
| 7 | `describing` | Describing Algorithms (source) | jeffe | `jeffe:0.5` (intro, "Specifying the Problem", "Describing the Algorithm" as `<h3>`) | no | the four components; footnotes |
| 8 | `correctness` | Analyzing Algorithms (source), "Correctness" as `<h3>` | jeffe | `jeffe:0.6` opening + "Correctness" | no | second block of `describing-algorithms`; its footnote ("If induction is not your friend…"). "Running Time" is 1.4's |
| 9 | `efficiency` | The Need for Efficiency (source) | ods | `ods:intro#the-need-for-efficiency` | no | the paragraph heads (Number of operations, Processor speeds, Bigger data sets, The solution) as run-in bold; the processor-speed footnote as a book footnote. **Extent question:** end before "The remainder of this chapter briefly reviews…" (see Questions) |
| 10 | `interfaces` | Interfaces (source) | ods | `ods:intro#sec:interfaces`, opening to the first subsection | no | B5: `\chapref{arrays}` → link to 2.2, `\chapref{linkedlists}` → link to 2.5–2.6 |

Not carried: Erickson's chapter-0 epigraphs (Villa Dei, Chekhov, Brackett, Chandler, Doctor Who) stand before 0.1 and are in no locator.

## Concepts

| id | kind | tier | statement (for `book.json`) | the one span that introduces it |
|---|---|---|---|---|
| `algorithm` | definition | Essential | An algorithm is an explicit, precise, unambiguous, mechanically executable sequence of elementary instructions, usually intended to accomplish a specific purpose. | `algorithm`, first sentence, "An algorithm is …" |
| `lattice-multiplication` | result | Advanced | Multiplying an m-digit number by an n-digit number by summing the digit products X[i]·Y[j]·10^(i+j) takes O(mn) time, dominated by the single-digit multiplications. | `lattice`, "the lattice algorithm" in its first paragraph |
| `peasant-multiplication` | result | Essential | x·y can be computed with only parity tests, addition, doubling and halving: halve x and double y, adding y whenever x is odd; O(log x) such steps, O(log x · log y) = O(mn) digit operations. | `peasant`, bold "peasant multiplication" |
| `apportionment` | result | Advanced | Huntington–Hill gives each state one seat, then each next seat to the state of highest priority P/√(r(r+1)), held in a priority queue used only through NewPriorityQueue, Insert and ExtractMax; the output does not depend on how the queue is implemented. | `apportionment`, bold "Huntington-Hill method" |
| `underspecified-algorithm` | idea | Essential | Martin's "become a millionaire" procedure is not an algorithm, because its first step is not an elementary, unambiguous instruction; it is a good reduction. | `underspecified`, "a sequence of instructions that is not actually an algorithm" |
| `describing-algorithms` | skill | Essential | A complete description gives what (the problem), how (the algorithm, loops as loops and recursion as recursion), why (a correctness proof) and how fast (a running-time analysis). | `describing`, "a complete description of any algorithm has four components" |
| `need-for-efficiency` | idea | Essential | Scanning every item does not scale: 10⁶ searches over 10⁶ items is 10¹² inspections, about 1000 s at 10⁹ operations a second, so data must be organised so that most operations inspect few items. | `efficiency`, "the obvious implementations of data structures do not scale well" |
| `interface-vs-implementation` | definition | Essential | An interface (abstract data type) names a structure's operations and their meaning; an implementation gives its representation and algorithms; one interface can have many implementations. | `interfaces`, "An interface describes what a data structure does, while an implementation describes how" |

Prerequisite edges as in `concepts.json` (Hasse-reduced already). Statements as the map has them, with `peasant-multiplication` and `apportionment` reworded to the passages.

## Errata notes (correction footnotes, AI-marked)

- **6** (Erickson Figure 0.5, the ApportionCongress pseudocode): `Insert(PQ, s, Pop[i]/√2)` should read `Pop[s]`; the comment "Allocate the remaining n − R representatives" and `for i ← 1 to n − R` should read R − n. The pseudocode stays verbatim in `sim-apportion`'s code panel (the figure's trace computes with Pop[s] and R − n). The numbered marker goes after the prose sentence "The algorithm is described in pseudocode in Figure 0.5"; the original toggle's caption is the book's and needs no correction.

## Derivation candidates (root item 29)

| candidate | how printed | moves | score (imported facts + longest unprinted run + joins) | decision |
|---|---|---|---|---|
| peasant: the recursive identity proves the algorithm "by induction" | identity printed, proof hidden | 3 (write x = 2⌊x/2⌋ + (x mod 2); distribute; regroup) | 1 + 3 + 0 = 4 | **not built**: under the four-move bar |
| lattice: x·y = Σ_i Σ_j X[i]·Y[j]·10^(i+j) | one display | 2 (product of the two digit sums) | 0 + 2 + 0 = 2 | not built |
| peasant cost: O(log min) · O(log max) = O(log x · log y) | prose | 2 | 0 + 1 + 0 = 1 | not built |
| compass: |AZ| = |AC||AD|/|AB| from the similar triangles ACE and AZF | one sentence | 3 (ratio of similar triangles; |AE| = |AB|, |AF| = |AD| from the circles; solve) | 1 + 3 + 1 = 5 | **not built**: three moves |

## Figures

Plan lines in the `interactive-figures.md` format, with this book's debugger fields where code sits beside the drawing. A code listing that a Sim shows becomes its code panel in place, so the reader does not read it twice (see Questions).

```
sim-lattice · Sim (no source sketch; the lattice Erickson describes is drawn in the Treviso scan, Figure 0.1, which stays a photograph) · lattice-multiplication · flow by animation; variation by input · arrows: kinematic (the carry moving from column k to column k + 1), the diagonals symbolic · moving: one partial product per step, then the digit written and the carry passed · input choice: 934 × 314 (the Treviso numbers, Figure 0.1) | 123 × 456 (Figure 0.3's, to compare with sim-peasant) | editable (up to 6 digits each) · headline "Column k collects every X[i]·Y[j] with i + j = k." · graph none · 2D · code: jeffe:0.2 FibonacciMultiply, Erickson pseudocode, lines 1–8 (0-based digit arrays) · blocks: init "start with no carry" line 2 touches hold; column "settle digit k" lines 3–7 touches k, Z; ⟶ diag "add the products on diagonal k" lines 4–5 touches i, j, hold; ⟶ digit "write the low digit, carry the rest" lines 6–7 touches Z, hold · invariant: Z[0..k) final, shaded in the index tint along the bottom row of the lattice · readout "Z[0..k) = 6, 7, 2 · hold = 13 · x·y = 293276" · cost: single-digit products against m·n = 9 · inputs: as above, no adversarial case (every input costs exactly m·n products, which the counter shows) · labels: the digits of X and Y on their edges, k under its column; i, j and hold on hover where the diagonal crowds
sim-peasant · Sim (original: Erickson Figure 0.3, "Multiplication by duplation and mediation") · peasant-multiplication · flow by animation; standardisation · arrows: kinematic (x halving down the left column, y doubling down the right) · moving: one row per step · input choice: 123 × 456 (Figure 0.3) | x a power of two (one row added) | x > y (the swap the text suggests: the rows follow min{x, y}) | editable · headline "prod + x·y never changes; when x reaches 0, prod is the product." · graph none · 2D · code: jeffe:0.2 PeasantMultiply, Erickson pseudocode, lines 1–8 · blocks: init "prod ← 0" line 2 touches prod; row "one row of the table" lines 3–7; ⟶ add "if x is odd, add y to prod" lines 4–5 touches x, y, prod; ⟶ halve "halve x, double y" lines 6–7 touches x, y · invariant: prod + x·y = 123 × 456, the kept rows filled, the skipped (even) rows faded to ink as Figure 0.3 strikes them · readout "prod + x·y = 5016 + 15·3648 = 56088 = 123 × 456" · cost: rows against ⌊log₂ x⌋ + 1 = 7 · inputs: as above; the odd rows read top to bottom are x's binary digits, labelled once on the column · predict pause (figure control only): "is x odd?" before each add
sim-compass · Sim (original: Erickson Figure 0.4, "Multiplication by compass and straightedge") · (no concept: context for describing-algorithms, decision 19) · flow by animation (each primitive draws its line or circle: Create); variation by slider · arrows: none (lines and circles are constructions, drawn once) · moving: one primitive per step · sliders |AC| and |AD| (untyped lengths, |AB| = 1 the unit; defaults read from the figure) · headline "Z lands where |AZ| = |AC|·|AD|/|AB|." · graph none · 2D · code: jeffe:0.2 RightAngle and MultiplyOrDivide, Erickson pseudocode, lines 1–14 · blocks: alpha "raise the perpendicular α at A" line 9, step into RightAngle lines 3–6; E "mark |AB| on α" line 10; F "mark |AD| on α" line 11; beta "β ⟂ EC through F" line 12 (step into); gamma "γ ⟂ β through F" line 13 (step into); Z "Z where γ meets AC" line 14 · invariant: triangles ACE and AZF similar, shaded once both exist · readout "|AZ| = |AC|·|AD|/|AB| = 2.0 × 1.5 / 1.0 = 3.0" · cost: primitive operations (lines, circles, intersections), the same count for every input, against O(1) · inputs: the two sliders; the ambiguous intersections (the text's "no matter which intersection points are chosen") as a choice E, F: upper | lower
sim-apportion · Sim (original: Erickson Figure 0.5, "The Huntington-Hill apportionment algorithm") · apportionment, algorithm (its worked example) · variation by input; flow by animation · arrows: kinematic (a seat moving to the state taken from the queue) · moving: one seat per step · input choice: the 50 states, 2020 census, R = 435 (default, the text's own n = 50 and R = 435; data to fetch, see Questions) | four states | editable · headline "Seat 51 goes to the state with the highest priority P/√(r(r+1))." · graph: beside, the priority queue drawn as one sorted column (the Census Bureau's sorted array, as 0.3 says) · 2D · code: jeffe:0.3 ApportionCongress (Figure 0.5), Erickson pseudocode, lines 1–13, verbatim with erratum 6 · blocks: init "an empty priority queue" line 2 touches PQ; first "give every state its first representative" lines 4–6 touches s, Rep, PQ; seat "allocate the next seat" lines 8–12; ⟶ pick "take the state with the highest priority" line 9 touches s, PQ; ⟶ give "give it a seat" line 10 touches Rep; ⟶ requeue "recompute its priority and put it back" lines 11–12 touches PQ · invariant: every state holds at least one seat (Rep[s] ≥ 1), shown by the first seat drawn hollow-outlined under each state · readout "seat 51 → s · Rep[s] = 2 · next priority Pop[s]/√(2·3)" · cost: ExtractMax calls against R − n · inputs: as above · predict pause (figure control only): which state takes the next seat
sim-scan-cost · Sim · need-for-efficiency · variation by slider · arrows: none · still (a calculation under sliders, no clock) · sliders n (items, 10³..10¹⁰, log, detents 10⁶ and 8.5×10⁹, the text's), m (operations, 10³..10¹⁰, log, detent 10⁶), speed (operations a second, 10⁸..10¹⁰, detent 10⁹) · choice: each operation inspects every item | about two items on average (the text's) · headline "10⁶ searches over 10⁶ items: 10¹² inspections, 16 minutes 40 seconds." · graph none: a clock dial and a bar for n × m · 2D · code: none (the passage prints no code) · readout "n·m / speed = 10¹² / 10⁹ = 1000 s ≈ 16 min 40 s"
```

**Source figures and photographs, keep or drop.**

| source item | decision | reason |
|---|---|---|
| Erickson Figure 0.1, *L'Arte dell'Abbaco* (Treviso, 1478), long and lattice multiplication of 934 × 314 | **keep, photograph**, with its caption and its image credit | the text points at it twice ("as shown on the right in Figure 0.1"); a historical scan, not a sketch. The credit is printed in Erickson's Image Credits, which are not in the cache (see Questions) |
| Erickson Figure 0.2, Eutocius's calculation (Heiberg's transcription, 1891) | **keep, photograph**, caption and credit | the text points at it ("as shown in Figure 0.2") |
| Erickson Figure 0.3, PeasantMultiply and its trace table | replaced by `sim-peasant`, image behind the original toggle | a sketch figure (root item 14) |
| Erickson Figure 0.4, RightAngle, MultiplyOrDivide and the construction | replaced by `sim-compass`, image behind the toggle | a sketch figure; the text walks through it |
| Erickson Figure 0.5, ApportionCongress | replaced by `sim-apportion` (its code panel), image behind the toggle | an algorithm listing printed as a figure |
| BottlesOfBeer and Martin's "algorithm" (unnumbered listings) | kept in the text as `<pre>` | listings, not figures; BottlesOfBeer is counted in 1.4's `sim-song-count` |

No figure for `describing-algorithms`, `underspecified-algorithm` or `interface-vs-implementation`: there is nothing to vary (a four-part checklist, a non-example, and a definition whose two implementations, arrays and linked lists, are taught in 2.2 and 2.5).

**Labels.** sim-peasant labels x, y and prod once at their column heads; sim-lattice labels X, Y on their edges and k under its column; sim-apportion names states on hover (50 would collide) and labels only the state just served; sim-compass labels A–F and Z at their points and α, β, γ at the line ends.

## Extra simulations (root item 15), one line each, none built until picked

- `sim-binary-equivalence`: lattice and peasant multiplication run side by side on the same pair written in binary, rows lighting up together, so the reader sees the text's "the two algorithms are equivalent when numbers are represented in binary".
- `sim-divisor-methods`: the same states apportioned by Huntington–Hill, D'Hondt (P/(r + 1)) and Webster–Sainte-Laguë (P/(2r + 1)), the priorities 0.3's footnoted paragraph names, with the seats that differ flagged.

## Exercises (config.md, decision 19)

| concept | kind | items | answer shape | status |
|---|---|---|---|---|
| algorithm, describing-algorithms | check | opendsa ProblemAlgorithmProgramTF1–TF11 + AnalPrelimSumm (tagged with both) | `choice` (true/false) | needs the OpenDSA Khan-format converter |
| algorithm | check | opendsa AlgAnlsMCQrelalgprb | `choice` | same; AlgAnlsMCQalgdfn not used (its key contradicts the winner) |
| need-for-efficiency | check | opendsa IntroMCQeff, IntroMCQeff2 | `choice` | converter |
| need-for-efficiency | code | exercism difference-of-squares (9 canonical tests; Exercism Python example passes 9/9; it returns floats, so a JS reference must use integer division) | `code` | **waits for the `code` answer type** |
| interface-vs-implementation | check | opendsa ADTMCQadt, ADTMCQinter, ADTMCQds + IntroADTSumm | `choice` | converter |
| underspecified-algorithm, lattice-multiplication, peasant-multiplication, apportionment | — | none | — | — |

`exercise_notes`: Erickson chapter 0 exercises 1 and 5 left out (unkeyed); ODS chapter 1 exercises 1, 5, 6 and 7 held for 3, 5 and 8; Erickson's chapter 1 Factorial item held for 4 (it uses lattice and peasant multiplication as subroutines); peasant multiplication has test cases (TheAlgorithms 13 doctests, trekhleb 2 suites) but no open statement, so no card; no `trace` item in this section.

## Referents

| id | what | figures | blocks that mark it |
|---|---|---|---|
| `x`, `y`, `prod` | PeasantMultiply's variables | sim-peasant | `peasant` |
| `k`, `i`, `j`, `hold` | FibonacciMultiply's variables | sim-lattice | `lattice` |
| `s` | ApportionCongress's current state | sim-apportion | `apportionment` |
| `A`, `B`, `C`, `D`, `E`, `F`, `Z`, `alpha`, `beta`, `gamma` | MultiplyOrDivide's points and lines | sim-compass | `compass` |

Groups never meet, so colours repeat across them. The arrays X, Y, Z, Pop and Rep are structures, not referents: their cells wear `key` (digits, populations) and their position labels `index`. Types on the page: `cost` (O(mn), O(log x · log y), running time), `size` (m, n as digit counts and as the number of states, R), `key` (digits, x and y as numbers, Pop[s], priorities), `index` (unnamed positions). Probability-free; nothing untyped beyond counts.

## References item (at most three)

- Algorithm design canvas (hiredintech, from CIU's interview-process list): a worksheet for the what / how / why / how-fast write-up the "Describing Algorithms" passage asks for.

## Attribution (footer, generated from `data-source`)

- Jeff Erickson, *Algorithms* (1st edition, June 2019), https://jeffe.cs.illinois.edu/teaching/algorithms/, CC BY 4.0, adapted. Figures 0.1 and 0.2 keep the credits printed in Erickson's Image Credits.
- Pat Morin, *Open Data Structures*, https://github.com/patmorin/ods (9d22c44), CC BY 2.5 Canada, adapted.
- `notes`: "Erickson's chapter-opening epigraphs and end-of-chapter exercises are not included." `ai`: text and figures, this model; `built`: the build date.
