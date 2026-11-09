# Plan: 3.3 Deques

Status: **plan, built from in the same run** (`briefs/section-build.md`: no separate review for chapters 2 and 3), 2026-11-09. Read for it: root and book `RULES.md`, `COLOR.md`, METHOD §1–§3, §5 and decisions 1–21, `LOG.md` passes 1–8, `ch03/config.md`, `ch03/exploration.md`, `judgements/ch01-03-reconciled.md` (items 9 and 10, the final table, B13, B14a, B18, errata 22, 23, 26, the indexing table, the rulings), `judgements/ch03.md` §3.3 and its builder notes, `judgements/ch01-03-references.md` (ODS notes; deque, array-deque, dual-array-deque rows), `concept-map/concepts.json` rows `deque`, `array-deque`, `dual-array-deque`, `ch01/plans-summary.md`, the built 2.2 and 2.6 (plan, spec, figures, log) as the nearest models; and from the source cache `ods/latex/intro.tex` 169–255, `ods/latex/arrays.tex` 392–650, `ods/latex/ods.tex` (the reference macros), `ods/python/ods/arraydeque.py`, `dualarraydeque.py`, `ods/java/ods/ArrayDeque.java`, `DualArrayDeque.java`, `ods/cpp/ArrayDeque.h`, `DualArrayDeque.h`, `figs/arraydeque.ipe` and `dualarraydeque.ipe` (rendered), Exercism `linked-list` (problem specification and the Python track's example and tests), Kattis `integerlists`, MIT 6.006 S20 Problem Session 1 and its solutions.

One source for the text, ODS (CC BY 2.5 Canada), pseudocode edition for the prose (decision 20), its Java, C++ and Python sources for the code. No translation. 3 blocks, 3 concepts, 2 debugger Sims, 1 derivation, 5 correction notes, 2 code exercises, 1 NC card.

## Lead (AI-marked, B13 and B14a)

> An Essential section on the <span data-concept="deque">deque</span>, a sequence that grows and shrinks at both ends, and on two ways to keep one in arrays; the <span data-concept="dual-array-deque">DualArrayDeque</span> is Advanced. Lists are indexed from 0. ODS's “LIFO Queue” is the stack of Section 3.1. Its lemma on balance() uses Section 1.5's <span data-concept="potential-method">potential method</span> as a counter: each call that does not rebalance raises Φ by at most 1, so the calls before a costly balance() pay for it.

Tier: Essential (`deque`, `array-deque` core); `dual-array-deque` is Advanced (stretch). Indexing: 0-based (reconciled table: ODS). Bridges: **B13** (sentence 3; "Section 3.1" links to 3.1) and **B14a** (sentence 4, linking 1.5's block `potential`, as the brief asks). B18 is a reference fix in the text (below), not lead prose. The lead is under 80 words (counted by the spec).

## Blocks (`<h2>`), in ODS's order

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `deque` | The Deque interface (OmniStax: the source's heading is "The Queue, Stack, and Deque Interfaces", whose other paragraphs are 3.1's and 3.2's) | ods | `ods:intro#the-queue-stack-and-deque-interfaces`, the Deque paragraph ("A Deque is a generalization of both…" to "…addLast(x) and removeFirst().") | no | the Deque, its four operations, a Stack and a FIFO Queue from two of them |
| 2 | `arraydeque` | ArrayDeque: Fast Deque Operations Using an Array (source) | ods | `ods:arrays#sec:arraydeque`, the whole section with thm:arraydeque | no | the circular array a, j, n; get/set at a[(j+i) mod length(a)]; add(i,x) shifting the shorter side; `\figref{arraydeque}` → "Figure 2.3", linked to `sim-arraydeque`, which stands where the figure and the add(i,x) listing stood; remove(i); Summary as `<h3>` with the theorem as a note; code sets for a.j.n, get/set and remove(i) |
| 3 | `dualarraydeque` | DualArrayDeque: Building a Deque from Two Stacks (source) | ods | `ods:arrays#sec:dualarraydeque`, the whole section with lem:dualarraydeque-amortized and thm:dualarraydeque | no | front and back back to back; size, get/set; `\figref{dualarraydeque}` → "Figure 2.4", linked to `sim-dualarraydeque`, standing where the figure and the add(i,x) listing stood; the cost of add(i,x), equations (2.1) and (2.2) and the cases display; remove(i); Balancing as `<h3>` with balance(), the lemma (a note), its proof with `drv-balance-potential` in place of the two `eqnarray*` displays; Summary as `<h3>` with the theorem; code sets for front.back, size(), get/set, remove(i) and balance() |

**Code (decision 20).** Every `\codeimport` is a four-language code set: Python, Java and C++ read by `tools/ods_listing.py` (`printed=True`, as 2.2), JavaScript an AI translation of the Java, marked. The two listings that the Sims' panels hold (each class's add(i,x)) are the panels where they stood (plans-summary question 17); remove(i) and balance(), which the prose reads where ODS prints them, stay as code sets there too, as 2.2 and 2.6 keep theirs (2.6 question 3).

**ODS's Python as printed.** ArrayDeque's add and remove compare `i < self.n/2`. On Python 3 that is the real division the prose describes ("we check if i < n/2") and the one Figure 2.3 draws; ODS's Java and C++ divide in integers. The Python is shown as ODS prints it, so it carries no AI mark (Questions 1). DualArrayDeque's Python runs unchanged too.

**References in the text** (book RULES, Cross-references): `\figref` keeps ODS's number and links to the Sim; `\lemref{arraystack-amortized}` keeps "Lemma 2.1" and links to 2.2's block `arraystack-cost` (B18, Questions 5); "the previous section" in the ArrayDeque opening wraps the source's words and links to 3.2's ArrayQueue block (`/ch03/3.2/#arrayqueue`); `\myeqref` prints ODS's equation numbers (2.1) and (2.2), which the two displays carry as `\tag` (root item 29: the book's equation numbers stay).

**Reader.** `tools/read_latex.py` (dialect `ods`) through `build_text.py`'s reader hook, as 2.2. It needs, backward-compatibly: a space between a control word and a following `#code#` in maths (`\ge#n#` was read `\gen`), `eqnarray*` as an aligned display, `\eqlabel` numbered per chapter as LaTeX numbers equations and set as `\tag`, `\myeqref` as "(2.1)". 1.1–1.6 and 2.x are rebuilt from frozen copies before and after to show their output unchanged.

## Concepts

| id | kind | tier | statement | introducing span |
|---|---|---|---|---|
| `deque` | definition | Essential | A Deque is a sequence of elements with a front and a back, where elements can be added and removed at either end: addFirst(x), removeFirst(), addLast(x) and removeLast(). It generalizes both the FIFO Queue and the LIFO Queue: a Stack needs only addFirst(x) and removeFirst(), a FIFO Queue addLast(x) and removeFirst(). | `deque`, "A Deque is a generalization of both the FIFO Queue and LIFO Queue (Stack)" |
| `array-deque` | result | Essential | An ArrayDeque keeps a list in a circular array, its element i at a[(j + i) mod length(a)], and on add(i,x) or remove(i) shifts whichever side of position i is shorter, so get(i) and set(i,x) take O(1) time and add(i,x) and remove(i) O(1 + min{i, n − i}), ignoring resize(); m calls from empty spend O(m) time in all calls to resize(). | `arraydeque`, "The ArrayDeque data structure allows for efficient addition and removal at both ends." |
| `dual-array-deque` | result | Advanced | A DualArrayDeque keeps a list in two ArrayStacks back to back, front holding elements 0, …, front.size() − 1 in reverse order and back the rest; balance() rebuilds them with ⌊n/2⌋ and ⌈n/2⌉ elements whenever one holds more than three times the other. get and set take O(1) time, add(i,x) and remove(i) O(1 + min{i, n − i}) ignoring balance() and resize(), and m calls from empty spend O(m) time in all calls to balance(). | `dualarraydeque`, "places two ArrayStacks, called front and back, back-to-back so that operations are fast at either end" |

Forms: `array-deque` `O(1+\min\{i,n-i\})` (the formulas list names it); `dual-array-deque` `\Phi = |\mathrm{front.size}() - \mathrm{back.size}()|` (the lemma's potential). Terms: deque (deque, double-ended queue), array-deque (ArrayDeque), dual-array-deque (DualArrayDeque). No type: a structure is not a category (COLOR.md).

Edges (Hasse-reduced, the map's): `deque → stack` (3.1), `deque → queue` (3.2), `array-deque → array-queue` (3.2), `array-deque → deque`, `dual-array-deque → dynamic-array-cost` (2.2), `dual-array-deque → deque`. The edges to 3.1's and 3.2's concepts are written once those concepts exist in `book.json`; until then they go to the chapter pass.

Coverage beside the introductions: `deque` uses stack, queue; `arraydeque` uses deque, array-queue, list-interface; `dualarraydeque` uses deque, dynamic-array, dynamic-array-cost, potential-method, array-deque. (Rows on 3.1/3.2 concepts as the edges.)

## Errata (correction notes, AI-marked)

- **22** (`dualarraydeque`, marker after "front.add(front.size()−i−1,x)"): the code calls front.add(front.size() − i, x); the prose's index would put x one place too late; the cost O(i + 1) is unchanged.
- **23** (`dualarraydeque`, marker after "a technique knows as"): read "known as".
- **26** (`arraydeque`, marker after the first "left by one position"): a[0], …, a[i−1] are list positions, the elements at a[j], …, a[(j + i − 1) mod length(a)], as get(i) reads them; the same holds for the other ranges named in this and the next paragraph.
- **New, 26b** (`arraydeque`, marker after "never has to shift more than min{i, n−i} elements"): ODS's Java and C++ compute n/2 in integers, so with n odd and i = (n − 1)/2 they shift the right side, (n + 1)/2 elements, one more than min{i, n − i}; the Python listing and Figure 2.3 (its last step) shift the left side. The bound O(1 + min{i, n − i}) holds either way.
- **New, 26c** (`arraydeque`, marker after "operations on an ArrayDeque." in "#add(i,x)# and #remove(x)#"): the second operation is remove(i), as the figure's caption says.

Not noted: "the list elements that whose indices" (a slip that does not change the meaning); ODS's editions differ on when remove(i) shrinks (Python at length(a) ≥ 3n, Java and C++ at length(a) > 3n), which the prose never states; the Sim's inputs never reach the case where they differ (checked by script).

## Derivation candidates

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| lem:dualarraydeque-amortized, the proof's two `eqnarray*`: n = front.size() + back.size() < back.size()/3 + back.size() = (4/3) back.size(); Φ₁ = back.size() − front.size() > back.size() − back.size()/3 = (2/3) back.size() > (2/3)(3/4) n = n/2 | displays inside a printed proof | 6 | printed proof: qualifies (29.1) | **build** `drv-balance-potential`, *Derivation · the potential before a balance that shifts elements*; two nodes (n against back.size(); Φ₁ against n/2), joined; replaces both displays and the connective "Furthermore, the potential at this point in time is" between them; the proof's prose before and after stays |
| (2.1) and (2.2), the cost of add(i,x) in front and in back | two one-line displays | 1 each | printed, but one move each; chapter 1's policy builds printed chains of three moves or more | not built |
| Φ₀ = \|⌊n/2⌋ − ⌈n/2⌉\| ≤ 1 | display | 1 | as above | not built |
| ArrayDeque's O(1 + min{i, n − i}) | prose | 1 | 0 + 1 + 0 = 1 | not built; `sim-arraydeque`'s counter shows it live |

`check_derivations()` in the spec checks every line over all front/back sizes up to 400 with 3·front.size() < back.size().

## Figures

```
sim-arraydeque · Sim (original: ODS Figure 2.3, figs/arraydeque.ipe, "A sequence of add(i,x) and remove(i) operations on an ArrayDeque. Arrows denote elements being copied.", behind the toggle; stands where Figure 2.3 and the add(i,x) listing stood) · array-deque, deque · flow by animation (elements shifted a cell, j stepping round the circular array); invariant made visible; variation by input · arrows: kinematic (an element copied to the neighbouring cell, from slot 0 round to the last slot when j wraps; j moving) · moving: one call per step, copy by copy one level in · choice (select): Figure 2.3 (default: a…h in an array of 12 at j = 0; remove(2), add(4, x), add(3, y), add(4, z)) | at both ends (the Deque operations as add(0, x), add(n, x), remove(0), remove(n − 1): nothing shifts) | in the middle (add(n/2, x) again and again: the most shifts, the bad case) | grow from a wrapped start (j at 5 of 8, appends until a is full: resize() copies from j into the front of the new array) · headline: the call and what it shifted, "remove(2): i = 2 < n/2 = 4, so a[0] and a[1] shift right one place and j steps forward to 1." · graph: none · 2D
  code: ods:arrays#sec:arraydeque add(i,x), remove(i), resize(); Python canonical (ODS's arraydeque.py as printed: the raising lines hidden, nothing ported), Java and C++ ODS's, JavaScript AI; 31 Python lines
  blocks: add "add(i, x)" 1–11 touches a, i, j, n
            grow "resize a if it is full" 2 touches a, n
            left "i < n/2: step j back and shift the first i elements left" 4–6 touches a, j ⟶ shl "copy one element a cell left" 6
            right "otherwise shift a[i], …, a[n − 1] right" 8–9 touches a ⟶ shr "copy one element a cell right" 9
            store "store x at list position i and count it" 10–11 touches a, i, n
          remove "remove(i)" 13–24 touches a, i, j, n
            take "read x at list position i" 14 touches a, i
            rl "i < n/2: shift the first i elements right and step j forward" 16–18 touches a, j ⟶ shrl "copy one element a cell right" 17
            rr "otherwise shift a[i + 1], …, a[n − 1] left" 20–21 touches a ⟶ shrr "copy one element a cell left" 21
            shrink "count it, and shrink a if length(a) ≥ 3n" 22–23 touches a, n
          resize "resize(): copy the list, from a[j] on, into the front of an array of size 2n" 26–31 touches a, b, j
            alloc "allocate b of size 2n" 27 · copy "copy one element into b" 28–29 · swap "b becomes a, and j = 0" 30–31
  default level: one stop per call, and one per resize inside it; step into gives the side chosen and each copy
  invariant: the n cells a[j], …, a[(j + n − 1) mod length(a)] shaded in the index tint (two runs where they wrap), list positions 0 … n − 1 written over them; readout "list position k sits at a[(j + k) mod length(a)] · j = 1 · n = 7"
  readout (the watch) i, x, j, n, len(a)
  cost: elements shifted by the call against min(i, n − i), "shifted 2 ≤ min(i, n − i) = 2"; shifts so far; copies by resize()
  inputs: as above; in the middle is the bad case (each add shifts about n/2), at both ends the good one
  labels: values in the cells (key), slot numbers under them (index), list positions over the live cells (index, muted), j and i at their cells (referents), a and b at their rows; hover names on cells and calls
sim-dualarraydeque · Sim (original: ODS Figure 2.4, figs/dualarraydeque.ipe, "A sequence of add(i,x) and remove(i) operations on a DualArrayDeque. Arrows denote elements being copied. Operations that result in a rebalancing by balance() are marked with an asterisk.", behind the toggle; stands where Figure 2.4 and the add(i,x) listing stood) · dual-array-deque, deque · flow by animation (elements shifted inside front or back; every element copied into its new stack by balance()); invariant made visible; variation by input · arrows: kinematic (copies) · moving: one call per step, balance() copy by copy one level in · choice (select): Figure 2.4 (default: front holds a, b and back c, d; add(3, x), add(4, y), remove(0), the last one rebalancing) | add at the back (twelve add(n, x) from empty: back outgrows front again and again) | add at the front (twelve add(0, x)) | drain the front (eight elements, then remove(0) six times) | alternate ends (add at the front and the back in turn: no balance at all) · headline per stop, e.g. "remove(0) takes a from front; now 3·front.size() = 3 < back.size() = 4, so balance() rebuilds both stacks around the middle." · graph: none · 2D
  code: ods:arrays#sec:dualarraydeque add(i,x), remove(i), balance(); Python canonical (ODS's dualarraydeque.py as printed), Java and C++ ODS's (their balance() is written differently; its blocks give their own lines), JavaScript AI; 27 Python lines
  blocks: add "add(i, x)" 1–6 touches front, back, i
            pick "add x to front or to back" 2–5 touches front, back, i
            bal "balance()" 6
          remove "remove(i)" 8–14 touches front, back, i
            pickr "remove it from front or from back" 9–12 · balr "balance()" 13
          balance "balance()" 16–27 touches front, back, n
            test "is one stack more than three times the other?" 17–19 touches front, back
            rebuild "rebuild both stacks around the middle" 20–27 touches front, back
              ff "copy list position mid − i − 1 into the new front" 21–22 (per copy) · bb "copy list position mid + i into the new back" 24–25 (per copy) · swap "the new stacks replace the old" 26–27
  default level: one stop per call and one for a balance() that shifts; step into opens the side chosen, the test and each copy
  invariant: unless n < 2, 3·front.size() ≥ back.size() and 3·back.size() ≥ front.size() (the cells of both stacks filled, the divider between them); the readout "Φ = |front.size() − back.size()| = |2 − 2| = 0", and the test shown failing in PAL.bad at the stop before a rebalance
  readout (the watch) i, x, n
  cost: calls since the last balance that shifted, against Φ − Φ₀ (the lemma's count, true at every stop); elements copied by balance() Σnₖ against 2m + 2r
  inputs: as above; add at the back is the case the lemma counts, alternate ends the case that never pays
  labels: values in the cells (key), each stack's own index under its cells (index: 4 3 2 1 0 | 0 1 2 3 4, as Figure 2.4 numbers them), list positions over the cells, front and back named over their halves (referents), i at its cell; hover names on cells and calls
```

Both figures open on ODS's own numbers (root item 14) and reproduce the source figure call by call; their traces are checked by script against ODS's own Python ArrayDeque and DualArrayDeque, run isolated (`python3 -I`, a scratch copy, the `numpy.object` shim).

**Source figures, keep or drop.** ODS Figure 2.3 (`figs/arraydeque`) → `sim-arraydeque`; ODS Figure 2.4 (`figs/dualarraydeque`) → `sim-dualarraydeque`. Both rendered by `render_originals.py` (iperender, 300 dpi) to `media/ch03/ods-arraydeque.png` and `ods-dualarraydeque.png`. No other figure in the three passages.

## Extra simulations

None. (A ring view of the ArrayDeque is 3.2's `sim-ring-queue`; repeating it here adds nothing the strip with wrap-around does not show.)

## Exercises

| concept | kind | item | answer shape | status |
|---|---|---|---|---|
| deque (and doubly-linked-list) | code | Exercism `linked-list` (held from 2.6) | `code`, a run(ops) driver in the starter playing each case's operations on the reader's LinkedList; 18 canonical cases; Python reference the Exercism Python track's example (MIT), JavaScript reference AI | ships |
| deque | code | Kattis `integerlists` (CC BY-SA 3.0; the judge: "a good applied exercise") | `code`, stdin/stdout; the sample visible (source), AI tests, `bound: "n"` with a grow input that defeats a list reversed at every R; AI references | ships |
| deque, dynamic-array-cost, dual-array-deque | NC card | MIT 6.006 S20 Problem Session 1, Problem 1-3 "Double-Ended Sequence Operations" (held from 2.2) | `open`, keyed by a link to MIT's worked solution | `exercises-nc.json` |
| array-deque | code | ODS Exercises 2.6 (rotate), 2.8, 2.9 and Exercise 2.7 (held from 2.2) | — | no source tests: left out (config) |
| array-deque, dual-array-deque | — | ODS `test_arraydeque.py`, `test_dualarraydeque.py`; trekhleb deque tests; TheAlgorithms `double_ended_queue.py` | — | test sources with no printed statement |
| deque | — | SICP 3.23 (Scheme, written); pythonds exercises 20 and 32 (NC, unkeyed); Kattis teque (stretch) | — | left out |

Exercism `linked-list`: the canonical case "delete does not modify the list if the element is not found" is left out, since the Python track excludes it and raises `ValueError` where the canonical data expects nothing (references file); the other 18 cases are the canonical data's. A canonical operation whose value the case does not check is written `["pop", "unchecked"]`, and the driver calls it without reporting it. Kattis `integerlists`: its statement is read from the cached page by script; the AI tests cover what it implies (an empty list, D on an empty list, R alone, many R, a program longer than the list, the largest sizes), and none adds a requirement.

## Referents

| id | what | figures | blocks marked |
|---|---|---|---|
| `a` | ArrayDeque's backing array | sim-arraydeque | `arraydeque` |
| `b` | the array resize() fills | sim-arraydeque | — |
| `j` | the slot holding list position 0 | sim-arraydeque | `arraydeque` |
| `n` | the number of elements | sim-arraydeque, sim-dualarraydeque | `arraydeque` |
| `i` | the list position a call names | sim-arraydeque, sim-dualarraydeque | `arraydeque` |
| `front` | DualArrayDeque's front ArrayStack | sim-dualarraydeque | `dualarraydeque` |
| `back` | DualArrayDeque's back ArrayStack | sim-dualarraydeque | `dualarraydeque` |

Values wear `key`, slot numbers and stack indices `index`, length(a) `size`, shift and copy counts `cost`, Φ `cost` (RULES types: a potential is `cost`).

## References item

None: the schema has no field for it yet (as chapter 1 and 2).

## Attribution

- Pat Morin, *Open Data Structures*, CC BY 2.5 Canada, adapted: the three blocks, the Java, C++ and Python listings, Figures 2.3 and 2.4.
- Exercism problem specifications and Python track (MIT), Kattis integerlists (CC BY-SA 3.0, BAPC 2012), credited by their exercise sources.
- MIT OpenCourseWare 6.006 Spring 2020, CC BY-NC-SA 4.0, in `exercises-nc.json` only.
- `notes`: ODS's other Queue, Stack and List paragraphs are 3.1's, 3.2's and 2.1's; its Java- and C++-only remarks are not in the pseudocode edition. `ai`, `built`.

## Questions (decided here)

1. **ArrayDeque's `i < n/2` in Python.** ODS's Python is Python 2, where `/` on integers floors, as the Java and C++ do; 2.6 ported its `n/2` to `n//2`. Here the prose ("we check if i < n/2") and Figure 2.3 (add(4, z) with n = 9 shifts the left side) both use the real n/2, which Python 3's `/` computes. *Decided:* show ODS's Python unchanged (no port, no mark) so the Sim reproduces Figure 2.3; note the Java and C++ difference as a correction (26b). The trace follows the Python; on that one odd case the Java panel's band stands on the branch the Python takes.
2. **Two new errata** (26b, 26c above), beyond the reconciled list. *Decided:* noted; listed for the chapter pass.
3. **Where the Sims stand.** Each stands where its source figure and its add(i,x) listing stood (plans-summary question 17); remove(i) and balance() stay as code sets too. *Decided:* as 2.2 and 2.6.
4. **Block 1's header.** The source's heading names three interfaces. *Decided:* an OmniStax `<h2>` "The Deque interface".
5. **`\lemref{arraystack-amortized}`.** RULES' rule reads "Section N.M" for a numbered reference, but "As in the proof of Section 2.2" does not read; a lemma is a numbered item like a figure, whose number stays. *Decided:* "Lemma 2.1" as printed, linked to 2.2's `#arraystack-cost` (B18). The chapter pass may prefer another reading.
6. **Equation numbers.** ODS numbers (2.1) and (2.2) and refers to them by number. *Decided:* kept, as `\tag` on the displays and as the printed references.
7. **The Exercism not-found case.** *Decided:* left out (above), so the Python reference is the source's own.
8. **Kattis integerlists' fit.** Config rated it good; it tests a deque used with a lazy reverse. *Decided:* ships, with a linear bound.
