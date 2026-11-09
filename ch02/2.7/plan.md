# Plan: 2.7 Cycles in linked lists: tortoise and hare

Status: **plan, built from in the same run** (brief `briefs/section-build.md`: chapters 2 and 3 have no separate plan review; questions decided below), 2026-11-09. Read for this plan: root `RULES.md`; the book's `RULES.md`, `COLOR.md`, `METHOD.md` (§1–§3, §5, decisions 1–21); `LOG.md` (passes 1, 2 and 8); `ch02/config.md` and `exploration.md`; `judgements/ch01-03-reconciled.md` (winners, bridges, errata, indexing, rulings of 2026-11-08), `judgements/ch02.md` §2.7, `judgements/ch01-03-references.md` (cycle-start rows); the three `concepts.json` rows; `ch01/plans-summary.md`, `ch01/1.1/plan.md`, `ch01/1.5/plan.md` and the built 1.1 and 1.5; and the winning passage, `sources/_cache/cpa/src/others/tortoise_and_hare.md` at the pinned commit d55d3f5, whole, with its three images.

One source, cp-algorithms (`cpa`, CC BY-SA 4.0), in English. 4 blocks, 3 concepts, 3 Sims (one debugger), 1 derivation, 1 code exercise.

## Lead (AI-marked, 63 words)

> An Essential section on telling whether a singly linked list ends or loops back on itself, and on finding the node where the loop begins, with two pointers that move at different speeds. Nothing here is indexed: a and b count steps along the list, L is the length of the cycle, and x and y count the laps each pointer has made.

Tier: Essential; no concept of another tier. Indexing: none (`exploration.md`: "step counts a, b, L"); the lead adds x and y, which the proof uses. Bridges: none (B1–B18 assign none to 2.7). The passage leans only on "linked list", "head", "null" and `next`, which 2.5 teaches.

## Blocks (`<h2>`), in cpa's own order

cpa prints the algorithm (Step 1, Step 2) before its reasons (Step 1, Step 2), so `floyd-cycle-detection`'s passage (`exploration.md`: intro + Step 1 + why Step 1) is not contiguous. It spans two blocks (book `RULES.md`, Source: a long passage may span several), and the page keeps cpa's order.

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `tortoise-hare` | Floyd's Linked List Cycle Finding Algorithm (source, the article's title); "Proposed algorithm" `<h3>`, "Step 1: Presence of the cycle" `<h4>` | cpa | `cpa:others/tortoise_and_hare`, its opening, #proposed-algorithm and its ###Step 1 | no | the problem, the image tortoise_hare_algo (→ `sim-rho-list`), the algorithm's name, the two steps, Step 1's seven items; the image tortoise_hare_cycle_found (folded into `sim-rho`, below) is left out here; "Now, that we have figured out…" |
| 2 | `cycle-start` | Step 2: Starting point of the cycle (source) | cpa | `cpa:others/tortoise_and_hare#step-2-starting-point-of-the-cycle`, with both Java snippets | no | the three items; the two Java snippets become `sim-rho`'s code panel in place (chapter 1 question 17: a listing a Sim shows is shown once) |
| 3 | `why-meet` | Why does it work (source); "Step 1: Presence of the cycle" `<h3>` | cpa | `cpa:others/tortoise_and_hare#why-does-it-work`, its ###Step 1 | no | second block of `floyd-cycle-detection`: twice the distance, the gap growing by 1 (the distance table, a code fence, kept as `<pre>`), the k·L ≥ a argument |
| 4 | `cycle-start-proof` | Why the reset finds the cycle start (OmniStax: the source's heading repeats block 2's, "Step 2: Starting point of the cycle", and two identical headers would stand on one page) | cpa | `cpa:others/tortoise_and_hare#step-2-starting-point-of-the-cycle_1` | no | the image tortoise_hare_proof (→ `sim-rho-proof`), the symbol list, the equations (→ `drv-cycle-start`), "where y − 2x is an integer", the closing paragraph |

Not carried: cpa's front matter and its "Problems" list (four LeetCode links; book `RULES.md`, Apparatus: practice-problem links become References links, never cards).

Source text goes through a script: no Markdown reader exists for English cpa pages (`build_text.py` reads Erickson, ODS and OpenDSA; `build_translation.py` reads OI Wiki and needs a translation), so a new tool, `tools/build_markdown.py`, slices the page by headings and sets it with `build_translation.py`'s own Markdown parser and inline setter (imported, unchanged). It is a new file: no shared tool changes. Cases the page needs beyond OI Wiki's subset: a level-1 heading, a centred `<div><img></div>` (a slot for the spec's figure, or dropped), a fenced block with a language (a code panel's place, or a `<pre>`), a run a derivation replaces, and a heading met twice.

## Concepts

| id | kind | tier | statement (reworded to cpa) | introducing span |
|---|---|---|---|---|
| `floyd-cycle-detection` | result | Essential | Start two pointers at the head, slow moving one node at a time and fast two; if they ever point to the same node the list has a cycle, and if fast reaches null it has none. Fast's lead grows by one node a step, so once slow has moved a multiple kL ≥ a of the cycle's length both are in the cycle, kL apart, and meet. | `tortoise-hare`, the bold "Floyd’s Cycle Algorithm or Tortoise And Hare algorithm" |
| `cycle-start` | result | Essential | Once slow and fast meet, reset slow to the head and move both one node at a time; they meet at the node where the cycle starts. | `cycle-start`, "The point they will meet at will be the starting point of the cycle." |
| `cycle-start-proof` | result | Essential | With a the steps from the head to the cycle's start C, b from C to the meeting point G, L the cycle's length and x, y the laps of slow and fast, a + yL + b = 2(a + xL + b) gives a = (y − 2x)L − b: a steps from G is whole laps less b, which ends on C, as a steps from the head does. | `cycle-start-proof`, "Let's try to calculate the distance covered by both of the pointers till the point they meet within the cycle." |

Edges as `concepts.json` has them, Hasse-reduced: `floyd-cycle-detection → singly-linked-list` (2.5's), `cycle-start → floyd-cycle-detection`, `cycle-start-proof → cycle-start`. Terms: "Floyd’s Cycle Algorithm", "Tortoise And Hare algorithm", "tortoise and hare" (floyd); "starting point of the cycle" (cycle-start); none for the proof. The map's statement for `floyd-cycle-detection` says "within O(length) steps", which cpa never states; the statement keeps cpa's kL ≥ a argument instead (as chapter 1's question 27 settled).

## Errata

None. The reconciled list (1–34) has none for this page, and a reading of it finds none that changes the meaning: the k·L ≥ a argument is right (the judge's 210-shape check), and the proof's a = (y − 2x)L − b holds at every first meeting, including a = 0, where b = 0 and x = 1. Two things that are not errors stay as printed: the Step 2 snippet assumes slow and fast are left at the meeting point, which `hasCycle` does not return (its own comment says so); and the comment's "are point to" is cpa's grammar, kept in every language of the panel.

## Derivation candidates (root item 29)

| candidate | how printed | moves | score (imported facts + longest unprinted run + joins) | decision |
|---|---|---|---|---|
| Step 2's proof: slowDist = a + xL + b, fastDist = a + yL + b, fastDist = 2·slowDist ⇒ a + yL + b = 2(a + xL + b) ⇒ a = (y − 2x)L − b | equations, one to a line, with words between: a printed proof | 5 (substitute both distances; expand; take a + b from each side; solve for a; factor L) | 1 (fastDist = 2·slowDist, from Step 1's why) + 3 ("Resolving the formula" skips expand, subtract, solve) + 1 (the two distance lines joined) = **5** | **build** `drv-cycle-start`, *Derivation · where the cycle starts*. Printed as equations first, so it replaces them (29.2): the run from "fastDist = 2·(slowDist)" through "a = (y − 2x)L − b", including "Resolving the formula we get:". Its facts are the two distance lines (the figure, `sim-rho-proof`), and fastDist = 2·slowDist (block 3). The two distance lines stand before cpa's list of symbols, and the derivation after it, so the reader meets every symbol before the chain uses it; cpa's lines are kept and the three it skips inserted. "where y − 2x is an integer" and the closing paragraph stay as printed after it |
| Step 1's why: kL ≥ a, slow at kL, fast at 2kL, separation kL ⇒ they meet | prose | 3 | 1 (a multiple of L at least a exists) + 2 + 0 = 3 | not built: under four moves and a score of four |
| the distance table (slow 0, 1, 2…; fast 0, 2, 4…; diff) | a code fence | — | — | never: a table of values, kept as `<pre>` |

## Figures

Plan lines in the `interactive-figures.md` format with the book's debugger fields. Every source image is a sketch of one scene, the list A … H with head and the cycle entered at C.

```
sim-rho-list · Sim (original: cpa tortoise_hare_algo.png, "Linked list with cycle") · floyd-cycle-detection · standardisation only: a faithful copy, the head and C in their referent colours as the text marks them · arrows: symbolic (the links) · still: no time and nothing to vary · no sliders or choices · headline none (the sentence after it names C) · graph none · 2D · code: none (a property: the shape the problem is about)
sim-rho · Sim (original: cpa tortoise_hare_cycle_found.png, "Found cycle"; it stood after Step 1's list and folds in here) · floyd-cycle-detection, cycle-start · flow by animation; invariant made visible; variation by input · arrows: kinematic (slow and fast move along the links; slow sent back to the head) · moving: one pointer move per step, fast's two links eased along the path · choice input: cpa's list (a = 2, L = 6, default: they meet at G) | no cycle (fast reaches null) | long tail (a = 7, L = 3: fast laps the cycle three times before slow enters) | cycle at the head (a = 0, L = 6) · headline per phase: "fast has covered twice slow's distance, 2 · 4 = 8, and is gaining one node a step", at the meeting "slow has moved kL = 6 ≥ a = 2 steps, so both are in the cycle, a whole number of laps apart", in the walk "slow and fast are both 2 steps from C", at the end "they meet at C, a = (y − 2x)L − b = (1 − 0) · 6 − 4 = 2 steps on" · graph none · 2D · code: cpa:others/tortoise_and_hare#step-2-starting-point-of-the-cycle, both Java snippets verbatim as one panel (Java the source's and the trace's canonical lines; Python, C++ and JavaScript AI translations), lines 1–24 · blocks: init "slow and fast start at the head" 3–4 touches slow, fast, head; race "race until they meet or fast runs out" 6–12 ⟶ lap "slow one node, fast two; same node?" 7–11 touches slow, fast; nocycle "fast reached null: no cycle" 14 touches fast; reset "slow back to the head" 18 touches slow, head; walk "both one node a step until they meet" 19–22 ⟶ wstep "slow and fast one node each" 20–21 touches slow, fast; found "the node where they meet starts the cycle" 24 touches slow · opens at level 2 (each lap a stop) · invariant: in the race, the stretch of the cycle fast still has to cover to reach slow, shaded in the index tint, shrinking by one node a step; in the walk, the two equal stretches from slow and from fast to C · readout: the watch (slow, fast as node names), then "fastDist = 2 · slowDist = 2 · 4 = 8" · cost: slow's moves, "race 6 = kL, k = 1 · walk 2 = a" · inputs: as above, the no-cycle case first-class · labels: node letters A, B, … on the nodes (at most ten); slow, fast and head at their arrows; a, b and L on brackets once the race ends; C and G named in their referent colours
sim-rho-proof · Sim (original: cpa tortoise_hare_proof.png, "Proof") · cycle-start-proof · variation by slider · arrows: symbolic (links); the dashed walk of a steps from G, drawn inside the cycle and a little further in at each lap, is a path drawn once, not travelled; b on an arc outside the cycle, a on a bracket under the tail · still (a relation under sliders, no clock) · sliders a (tail, 0..7, the book's 2; size), L (cycle, 1..7, the book's 6; size); special: a = 0 (dashed circle; the cycle starts at the head, b = 0 and they meet at the head) · headline "slow and fast meet at G, b = 4 past C; a = 2 more steps from G is (y − 2x) = 1 lap less b, which ends on C." · readout "slowDist = a + xL + b = 2 + 0 · 6 + 4 = 6 \\ fastDist = a + yL + b = 2 + 1 · 6 + 4 = 12 = 2 · slowDist \\ a = (y − 2x)L − b = (1 − 0) · 6 − 4 = 2" · graph none · 2D · code: none (a property: the proof's distances, not a procedure)
```

`sim-rho` draws the meeting the folded image shows (G on cpa's list) and the walk the second snippet runs; its code panel is where the two snippets stood. `sim-rho-proof` opens on cpa's own list, so its first state is the proof image with the distances worked.

**Source images, keep or drop.**

| image | where cpa prints it | decision |
|---|---|---|
| tortoise_hare_algo.png | the opening, after "For instance:" | replaced by `sim-rho-list`, behind its original toggle; the sentence after it names C, so a figure must stand there |
| tortoise_hare_cycle_found.png | after Step 1's list | folded into `sim-rho` (its original), which stands a few paragraphs on, where the code is; nothing in the text points at the image |
| tortoise_hare_proof.png | Step 2's proof, before the equations | replaced by `sim-rho-proof`, behind its original toggle |

## Exercises (config.md, decision 19)

| concept | kind | item | answer shape | status |
|---|---|---|---|---|
| floyd-cycle-detection, cycle-start | code | icc `linked_lists/find_loop_start` (Apache-2.0): its statement and constraints from the challenge notebook, its 5 asserts as source tests, its solution (with `linked_list.py`'s Node) as the Python reference | `code`; Python and JavaScript; the tests build the list from its values and the position the last node links back to (−1 for none), and compare the data of the node returned; 5 AI tests for what the statement implies (a cycle at the head, a one-node cycle, a self-loop at the end, a long tail on a short cycle, a two-node cycle); bound n, grown on a list of n with its cycle at n/2 | ships |
| cycle-start-proof | — | none (written by nature; no open exercise) | — | — |

`exercise_notes`: keon `is_cyclic` and `first_cyclic_node`, TheAlgorithms `has_loop`, `floyds_cycle_detection` and `happy_number` are test sources with no printed statement (decision 19), so no card; no check, trace or NC item exists for these concepts.

## Referents

| id | what | figures | blocks that mark it |
|---|---|---|---|
| `slow` | the pointer that moves one node at a time | sim-rho | `tortoise-hare`, `cycle-start`, `why-meet` |
| `fast` | the pointer that moves two | sim-rho | `tortoise-hare`, `cycle-start`, `why-meet` |
| `head` | the head of the list | sim-rho-list, sim-rho, sim-rho-proof | `tortoise-hare`, `cycle-start` |
| `C` | the node where the cycle starts (a named element, `COLOR.md` §3) | sim-rho-list, sim-rho, sim-rho-proof | `tortoise-hare`, `cycle-start-proof` |
| `G` | the node where slow and fast meet | sim-rho, sim-rho-proof | `cycle-start-proof` |

One group of five. Types drawn: `index` (the shaded stretches, unnamed nodes' positions), `size` (a, b, L as brackets), `cost` (the move counter). Maths in the text stays in ink, as in chapter 1 (no variables rows).

## References item (at most three; no `section.json` field carries them yet)

- LeetCode "Linked List Cycle" and "Linked List Cycle II" (cpa's Problems list): the two steps as judge problems.
- LeetCode "Find the Duplicate Number" (cpa's Problems list): the same two phases on a function on an array instead of a list.

## Attribution

- cp-algorithms contributors, *Algorithms for Competitive Programming*, others/tortoise_and_hare, https://github.com/cp-algorithms/cp-algorithms (d55d3f5), CC BY-SA 4.0, adapted; its three images behind the Sims' original toggles.
- Donne Martin, *Interactive Coding Challenges*, find_loop_start (Apache-2.0, the exercise source's copyright and notice).
- `notes`: "cp-algorithms’ list of practice problems is left out here." `ai`: text and figures, this model; `built`: the build date.

## Questions (decided here; the brief asks for no stop)

1. **The source's code languages.** The brief describes cpa's code as C++ and Java; the pinned page prints Java only (two snippets). *Decided:* Java is the source's variant; Python, C++ and JavaScript are AI translations with the mark.
2. **Two blocks for one concept, out of a neat order.** `floyd-cycle-detection`'s passage is split by Step 2, so it spans blocks 1 and 3 in cpa's order rather than being gathered. *Decided:* cpa's order (1.5's precedent).
3. **Block 4's header.** cpa repeats "Step 2: Starting point of the cycle" under "Why does it work". *Decided:* the OmniStax header "Why the reset finds the cycle start" (the concept's name), so two identical `<h2>`s do not stand on one page.
4. **Where the derivation stands.** cpa prints two distance lines, then its symbol list, then the chain. *Decided:* the derivation replaces the chain after the list and takes the two lines as its facts; the two lines themselves are dropped from before the list, since they are the derivation's first facts and the page would otherwise show them twice.
5. **The folded image.** tortoise_hare_cycle_found stands in block 1; `sim-rho` stands in block 2 with the code. *Decided:* fold it into `sim-rho`; nothing in the prose points at it.
6. **The exercise's interface.** icc tests a method on its LinkedList class, and the code answer type passes JSON. *Decided:* the tests call a small harness in the starter that builds the list from values and a back-link position and returns the found node's data; the reader writes `find_loop_start(head)`; `changes` says so.
7. **A Markdown reader.** *Decided:* a new tool, `tools/build_markdown.py`, rather than a change to `build_text.py` or `build_translation.py` (other sections build with those concurrently).
