# Chapter 3 exploration: Stacks, queues and deques

Status: **agreed**, 2026-11-08 (METHOD §4.4 decision 19). Nothing is built. Written from `concept-map/toc.md` and `concepts.json` (chapter `ch-stacks-queues`), `dossiers/ch03.md`, `judgements/ch03.md`, `judgements/ch01-03-reconciled.md`, `judgements/ch01-03-references.md` and METHOD §4.4. Every locator is the reconciled winner's.

## What the chapter is

Six sections, 24 concepts (15 Essential, 8 Advanced, 1 Beyond). It rests on chapters 1 and 2: ODS's queue, deque and space-efficient structures all cite ArrayStack's resize and DLList from 2.2 and 2.6, and the amortised arguments of 3.3 and 3.6 use 1.5's potential method in a counting form. No translation is needed.

| § | Title | Tier | Concepts (tier where it differs) |
|---|---|---|---|
| 3.1 | Stacks and bracket matching | Essential | stack, balanced-brackets, bracket-validation |
| 3.2 | Queues and circular buffers | Essential | queue, circular-buffer, queue-linked-list, array-queue |
| 3.3 | Deques | Essential | deque, array-deque, dual-array-deque (Advanced) |
| 3.4 | Min-stacks and monotonic queues | Essential | min-stack, queue-from-two-stacks, monotonic-queue-minimum, sliding-window-minimum, nearest-smaller-element, largest-zero-submatrix (Advanced) |
| 3.5 | Stack applications: expression evaluation | Advanced | rpn-evaluation (Essential), expression-parsing, unary-right-assoc |
| 3.6 | Space-efficient lists | Advanced | rootish-array-stack, rootish-index-math (Beyond), sqrt-space-lower-bound, space-efficient-list, selist-spread-gather |

## Provenance: every block and its source

| § | block | concept | `data-source` | `data-locator` | licence | note |
|---|---|---|---|---|---|---|
| 3.1 | `stack` | stack | wikipedia | `wikipedia:Stack_(abstract_data_type)` lead, #Non-essential operations, #Implementation, #Array, #Linked list | CC BY-SA 4.0 | its own array and linked-list pseudocode |
| 3.1 | `balanced` | balanced-brackets | cpa | `cpa:combinatorics/bracket_sequences#balanced-bracket-sequences` | CC BY-SA 4.0 | |
| 3.1 | `validation` | bracket-validation | cpa | `cpa:combinatorics/bracket_sequences#balance-validation` | CC BY-SA 4.0 | |
| 3.2 | `queue` | queue | ods | `ods:intro#the-queue-stack-and-deque-interfaces`: opening paragraph + FIFO paragraph + fig. queue | CC BY 2.5 CA | the LIFO paragraph is unused (stack is Wikipedia's); the priority-queue paragraph waits for chapter 9 |
| 3.2 | `circular` | circular-buffer | ods | `ods:arrays#sec:arrayqueue`, from "Notice that an ArrayStack is a poor choice" to "…does not exceed the size of a." | CC BY 2.5 CA | |
| 3.2 | `arrayqueue` | array-queue | ods | `ods:arrays#sec:arrayqueue`, from the first code import (`ArrayQueue.a.j.n`) to the end of "Summary" | CC BY 2.5 CA | adjacent to `circular`; the two halves of one ODS section |
| 3.2 | `linked-queue` | queue-linked-list | ods | `ods:linkedlists#sec:sllist` "Queue Operations" + the closing paragraph after thm:sllist | CC BY 2.5 CA | uses SLList's head, tail, n (B11) |
| 3.3 | `deque` | deque | ods | `ods:intro#the-queue-stack-and-deque-interfaces`, Deque paragraph | CC BY 2.5 CA | |
| 3.3 | `arraydeque` | array-deque | ods | `ods:arrays#sec:arraydeque` (whole, with thm:arraydeque) | CC BY 2.5 CA | |
| 3.3 | `dualarraydeque` | dual-array-deque | ods | `ods:arrays#sec:dualarraydeque` (whole, with lem:dualarraydeque-amortized) | CC BY 2.5 CA | "potential method" in a counting form (B14a) |
| 3.4 | `min-stack` | min-stack | cpa | `cpa:data_structures/stack_queue_modification` lead + #stack-modification | CC BY-SA 4.0 | C++ |
| 3.4 | `monotonic-queue` | monotonic-queue-minimum | cpa | `…#queue-modification-method-1` + `#queue-modification-method-2` | CC BY-SA 4.0 | |
| 3.4 | `two-stack-queue` | queue-from-two-stacks | cpa | `…#queue-modification-method-3` | CC BY-SA 4.0 | |
| 3.4 | `window-minimum` | sliding-window-minimum | cpa | `…#finding-the-minimum-for-all-subarrays-of-fixed-length` | CC BY-SA 4.0 | |
| 3.4 | `nearest-smaller` | nearest-smaller-element | wikipedia | `wikipedia:All_nearest_smaller_values` lead, #Example, #Sequential algorithm | CC BY-SA 4.0 | 1-based, sentinel A[0] |
| 3.4 | `zero-submatrix` | largest-zero-submatrix | cpa | `cpa:dynamic_programming/zero_matrix` (whole) | CC BY-SA 4.0 | folded into this home (`toc.md`) |
| 3.5 | `rpn` | rpn-evaluation | cpa | `cpa:string/expression_parsing` lead + #reverse-polish-notation | CC BY-SA 4.0 | |
| 3.5 | `parsing` | expression-parsing | cpa | `#parsing-of-simple-expressions` | CC BY-SA 4.0 | |
| 3.5 | `unary-right` | unary-right-assoc | cpa | `#unary-operators` + `#right-associativity` | CC BY-SA 4.0 | |
| 3.6 | `rootish` | rootish-array-stack | ods | `ods:arrays#sec:rootisharraystack` through "Analysis of Growing and Shrinking", + "Summary" | CC BY 2.5 CA | |
| 3.6 | `rootish-sqrt` | rootish-index-math | ods | `ods:arrays#sec:rootisharraystack` "Computing Square Roots" (lem:root) | CC BY 2.5 CA | `\notpcode`: in the Java and C++ editions only; code is FastSqrt.java/.cpp |
| 3.6 | `sqrt-lower-bound` | sqrt-space-lower-bound | ods | `ods:arrays#sec:rootishspaceusage` | CC BY 2.5 CA | |
| 3.6 | `selist` | space-efficient-list | ods | `ods:linkedlists#sec:selist` through "Removing an Element", + "Summary" | CC BY 2.5 CA | |
| 3.6 | `selist-amortized` | selist-spread-gather | ods | `ods:linkedlists#lem:selist-amortized` | CC BY 2.5 CA | (B14b) |

Source count: ODS 12, cpa 10, Wikipedia 2. 3.4's page order follows cpa's article (method 1 and 2 before method 3), not the map's concept order; the plan may reorder only where cpa's text allows.

**ODS passages split across concepts**, each piece used whole: the intro subsection "The Queue, Stack, and Deque Interfaces" (3.2 queue, 3.3 deque; its List subsection went to 2.1); ArrayQueue (3.2 circular-buffer, then array-queue); RootishArrayStack (3.6, three concepts).

## Apparatus

- **ODS**: Java-like pseudocode, the figures stack, queue, arrayqueue, arraydeque, dualarraydeque, rootisharraystack, gauss, selist-add-*, selist-remove-* (`.ipe` in `latex/figs/`, CC BY), lemmas with proofs, "Summary" theorems kept in their blocks. The Python ArrayQueue, ArrayDeque and DualArrayDeque run under the shims; RootishArrayStack and SEList need the AI-made mechanical port (`judgements/ch01-03-references.md`) and are marked where they run.
- **cpa**: Markdown and C++. Runnable Python counterparts, all MIT and all passing their tests: TheAlgorithms `stack_tracking_min_max.py` (min-stack), `queue_by_two_stacks.py` or tryalgo `our_queue` (queue-from-two-stacks), `monotonic_queue.py` and `other/sliding_window_maximum.py` (maximum variants), `postfix_evaluation.py` (RPN, with two quirk doctests dropped), `dijkstras_two_stack_algorithm.py` (parsing), tryalgo `rectangles_from_grid` (zero submatrix).
- **Wikipedia**: wikitext and pseudocode; figures under per-file licences (Lifo stack.svg CC0, Data stack.svg PD, Data Queue.svg CC BY-SA 3.0, the Cburnett circular-buffer SVGs CC BY-SA 3.0, Circular Buffer Animation.gif CC BY-SA 4.0, Stockspan.svg CC BY-SA 3.0, Shunting yard.svg CC BY-SA 3.0, Postfix-dia.svg PD).
- **Objectives, summaries, introductions**: none printed.

## Bridges

| id | where | what it carries |
|---|---|---|
| B11 | 3.2 lead, `linked-queue` | ODS's SLList (named in 2.6); its pop() removes the head node, as 3.1's linked stack does; the closing paragraph's Deque is 3.3 |
| B12 | 3.1 lead | 2.2's ArrayStack is an array-backed stack; Wikipedia's array pseudocode here is the same idea |
| B13 | 3.3 lead | "LIFO Queue" in the Deque paragraph means the stack of 3.1 |
| B14a | 3.3 lead, `dualarraydeque` | ODS's "potential method" here is 1.5's method used as a counter: each cheap operation raises Φ by at most 1, so balance() is paid for by the operations before it |
| B14b | 3.6 lead, `selist-amortized` | the same, with Φ the number of fragile nodes |
| B15 | 3.2 lead, `circular` | ODS's ArrayQueue resizes rather than bounding; the bounded buffer with overwrite in the exercises is the fixed-size variant the concept names |
| B18 | 3.2, 3.3, 3.6 | a reference fix, not prose: ODS's `\lemref{arraystack-amortized}` and "the resize() of ArrayStack" link to 2.2 |

3.2 needs B11 and B15 in one lead; it may not fit 80 words.

## Errata to attach as correction notes

22. ODS DualArrayDeque prose: `front.add(front.size()-i-1, x)`; the code is `front.size()-i`.
23. ODS DualArrayDeque lemma: "a technique knows as" should be "known as".
24. ODS ArrayQueue theorem: "m add(i,x) and remove(i) operations"; the Queue has add(x) and remove().
25. ODS ArrayQueue prose: resize to "size 2n"; the code uses max(1, 2n).
26. ODS ArrayDeque: "shift the elements a[0],…,a[i−1] left" means list positions, not raw slots (harmless; a short note).
27. ODS RootishArrayStack space usage: "wasting at least in √n" (typo).
28. cpa zero_matrix step 1: d[i][j] "from 0 to i − 1"; the code includes row i.
29. cpa queue-from-two-stacks: the minimum of an empty queue reads `s2.top()`, undefined. A note, and an edge case the exercise's tests must not require.
30. cpa unary operators: unary priority above `^` gives −2^2 = 4. A note; no exercise may combine the two.
31. cpa's C++ negates a `char` to flag a unary operator, implementation-defined where `char` is unsigned. Matters only when C++ runs; no note in the first pass.

## Indexing, as each lead must state it

| § | convention |
|---|---|
| 3.1 | 0-based (Wikipedia's stack, top starts at 0) |
| 3.2 | 0-based (ODS a[(j + i) mod a.length]) |
| 3.3 | 0-based (ODS) |
| 3.4 | mixed: cpa 0-based (minimum over A[0..M−1], …, A[N−M..N−1]); Wikipedia's nearest smaller values 1-based (A[1..n], sentinel A[0]) |
| 3.5 | none: tokens |
| 3.6 | 0-based (ODS blocks 0, 1, …; i2b(i)) |

## Derivations (root item 29), candidates

| § | candidate |
|---|---|
| 3.3 | ODS lem:dualarraydeque-amortized and its proof |
| 3.6 | ODS i2b: b(b+1)/2 ≤ i < (b+1)(b+2)/2 solved by the quadratic formula (printed as equations) |
| 3.6 | ODS lem:root (Computing Square Roots) |
| 3.6 | ODS's √n lower bound by the pigeonhole argument |
| 3.6 | ODS lem:selist-amortized |

## Exercises that belong elsewhere

- Into 3.3 from chapter 2: ODS Exercise 2.7 (needs ArrayDeque).
- Out of this chapter: Kattis guessthedatastructure (needs priority queues) → chapter 9; Kattis polish (prefix expressions, recursive) → chapter 4; ICPC NWERC 2024 flowingfountain (needs union-find) → chapter 16; keon heap/sliding_window_max (a heap) → chapter 9; Wikibooks' queue question on priority queues → chapter 9; ODS Exercise 2.8 (no `%`, power-of-two length) assumes bits → chapter 7, unless the plan judges its statement readable here.
- MIT 6.046J S15 4-1 (NC) is ranked for 3.4 and goes with 1.5; MIT 6.006 S20 ps1 1-4 (NC) is ranked for 3.2 and goes with 2.6.
- Into 3.1 and 3.3 from chapter 2: Exercism simple-linked-list (a linked stack) and Exercism linked-list (a doubly linked deque); into 3.3: MIT 6.006 S20 prob1 1-3 (NC, a double-ended sequence).

## The chapter's answer to root rule 23: what would make this stunning

Stacks and queues are where most visualisers stop at boxes going in and out. The sources here are about why a structure is fast, and that is what to draw: the ring under ArrayQueue, the balance of two stacks, the candidates a monotonic deque throws away, the √n blocks.

- **3.1, the bracket depth.** A bracket string read left to right, the stack beside it, cpa's balance counter drawn as a depth line under the string that must never go below zero and must end at zero. Inputs: balanced, an early mismatch, too many closers, deep nesting.
- **3.2, the ring and the strip.** ODS's ArrayQueue drawn twice at once: as the ring the index arithmetic suggests and as the actual array, j and n moving, a[(j + i) mod a.length] lighting the same cell in both; a resize unrolls the ring into a new strip starting at 0.
- **3.3, two stacks back to back.** DualArrayDeque's front and back ArrayStacks meeting in the middle, balance() firing when one grows to three times the other, Φ = |front.size() − back.size()| in the readout, so the reader sees the counting argument of B14a pay for each rebalance.
- **3.4, candidates thrown away.** The sliding-window minimum with the deque of candidates under the window: each new value pops every larger candidate from the back, the front leaves when it falls out of the window, each element entering and leaving once (counter ≤ 2n). The same picture, run over a whole array with a stack, is the nearest smaller value; run over histogram heights row by row, it is the largest zero submatrix.
- **3.4, the lazy queue.** Two stacks, the transfer happening only when the out-stack is empty, a counter showing each element moved at most twice. Inputs: bursts of pushes then pops, alternating.
- **3.5, the two-stack parser.** cpa's operator and value stacks under the expression, each operator waiting while one of higher precedence sits on top; the predict pause asks "pop or push?". Unary minus and right-associative ^ as inputs, and −2^2 as the case where cpa's priority rule gives 4 (erratum 30), shown and noted.
- **3.6, √n blocks.** RootishArrayStack's blocks of sizes 1, 2, 3, … growing as n grows, i2b(i) computed live from the quadratic formula, the wasted space beside ArrayStack's on one axis; SEList's blocks of b − 1 to b + 1 spreading and gathering, Φ the number of fragile blocks.

Plan lines:

```
sim-brackets · Sim · balanced-brackets, bracket-validation, stack · invariant made visible · arrows: kinematic (push, pop) · moving: one character per step · code: cpa bracket_sequences (C++) · blocks: open "push / depth += 1"; close "pop and match / depth −= 1" · invariant: depth ≥ 0 · readout "depth 2 · never negative · ends at 0?" · inputs: balanced | early mismatch | too many closers | deep nesting · predict pause: does the string stay balanced · 2D
sim-ring-queue · Sim (original: ODS fig. arrayqueue) · circular-buffer, array-queue, queue · flow by animation · arrows: kinematic (j and the tail advance) · moving · code: ODS ArrayQueue add/remove/resize · blocks: add "a[(j+n) mod a.length] = x"; remove "x = a[j]; j = (j+1) mod a.length"; resize "copy into a new array from j" · invariant: the n live cells are j … j+n−1 mod a.length · cost: copies against the amortised bound · inputs: fill and drain | wrap around | grow past capacity · 2D
sim-dual-deque · Sim (original: ODS fig. dualarraydeque) · dual-array-deque, deque, array-deque · flow by animation · moving · code: ODS DualArrayDeque · blocks: add; remove; balance "rebuild both halves around the middle" · readout "Φ = |front − back| = 4 · balance when 3·front < back" · cost: copies against the operations since the last balance · 2D
sim-monotonic-window · Sim · monotonic-queue-minimum, sliding-window-minimum, nearest-smaller-element · invariant made visible · arrows: kinematic (candidates popped, the window slides) · moving · code: cpa method 1 (C++) beside TheAlgorithms' Python · blocks: drop "pop larger candidates from the back"; push "append the new value"; expire "pop the front if it left the window" · invariant: the deque is increasing and holds only window elements · cost: pushes + pops against 2n · choice: task (window minimum | nearest smaller to the left) · slider: window length M · 2D
sim-two-stack-queue · Sim · queue-from-two-stacks, min-stack · flow by animation · moving · code: cpa method 3 · cost: moves per element against 2 · inputs: bursts | alternating · 2D
sim-zero-submatrix · Sim · largest-zero-submatrix · flow by animation · moving: one row per step, then the stack scan · code: cpa zero_matrix · readout "best area 6 at rows 2–3, columns 1–3" · 2D
sim-two-stack-parser · Sim (original: Wikipedia Shunting yard.svg) · rpn-evaluation, expression-parsing, unary-right-assoc · flow by animation · moving: one token per step · code: cpa expression_parsing (C++) · blocks: operand "push value"; operator "pop while top has higher priority, then push"; close "pop to the open bracket" · inputs: cpa's examples | unary minus | right-associative ^ | −2^2 · predict pause: pop or push · 2D
sim-rootish · Sim (original: ODS fig. rootisharraystack) · rootish-array-stack, rootish-index-math, sqrt-space-lower-bound · variation by slider · still (redraw on n) · slider n, i · readout "i2b(i) = ⌈(−3 + √(9 + 8i))/2⌉ = 4 · wasted ≤ √n" · graph: beside, wasted space against n for ArrayStack and RootishArrayStack · 2D
sim-selist · Sim (original: ODS figs. selist-add, selist-remove) · space-efficient-list, selist-spread-gather · flow by animation · moving · slider b · readout "Φ = fragile blocks = 3" · 2D
```

Referents: top (3.1); j and n (3.2); front and back (3.3); the deque's front and back, l and r of the window (3.4); the two stacks in and out (3.4); the operator and value stacks (3.5). Types drawn: `index`, `key`, `cost`, `size`.
