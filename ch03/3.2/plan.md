# Plan: 3.2 Queues and circular buffers

Status: **plan, built in the same run** (`briefs/section-build.md`: chapters 2 and 3 have no separate plan review; chapter 1's answered questions settle what they settle; new questions are decided below and listed at the end), 2026-11-09. Read for it: root and book `RULES.md`, `COLOR.md`, METHOD §1–§3, §5 and decisions 1–21, `LOG.md` passes 1–8, `ch03/config.md`, `ch03/exploration.md`, `judgements/ch01-03-reconciled.md` (items 5 and 6, the winner table, B11, B15, B18, errata 24–25, the indexing table, the rulings), `judgements/ch03.md` §3.2, `judgements/ch01-03-references.md` (circular-buffer, queue_list), `concept-map/concepts.json` rows `queue`, `circular-buffer`, `queue-linked-list`, `array-queue`, `ch01/plans-summary.md`, the built 2.2 and 2.6 (spec, figures, log); from the source cache `ods/latex/intro.tex` 169–196, `arrays.tex` 260–390, `linkedlists.tex` 71–105, `snarf-python.py`, `snarf-java.pl`, `snarf-cpp.pl`, `ods/{python,java,cpp}` ArrayQueue and SLList, `figs/queue.ipe` and `arrayqueue.ipe` (rendered), Exercism `circular-buffer` and icc `stacks_queues/queue_list`.

One source, *Open Data Structures* (`ods`, CC BY 2.5 Canada), pseudocode edition for the prose (decision 20), its Java, C++ and Python sources for the code. No translation. 4 blocks, 4 concepts, 2 Sims (one moving, one debugger), 6 four-language code sets, 0 derivations, 3 corrections (errata 24 and 25, and the figure caption), 2 code exercises.

## Lead (AI-marked, 73 words, B11 and B15)

> An Essential section on the FIFO queue and two ways to build it. Arrays are indexed from 0. ODS’s ArrayQueue grows and shrinks its circular array as Section 2.2’s ArrayStack does; the circular buffer of the exercises is the fixed-size kind, which overwrites its oldest element. The linked queue is Section 2.6’s SLList, whose pop() removes the head node as Section 3.1’s linked stack does; the Deque it nearly implements is Section 3.3’s.

Tier: Essential (all four concepts `core`). Indexing: 0-based (ODS a[(j + i) mod length(a)]). **B15** is sentence 3 (ArrayQueue resizes; the bounded, overwriting buffer is the exercise's). **B11** is sentence 4 (SLList named in 2.6, whose lead gives head, tail and n; pop() is the head removal 3.1's linked stack does; the closing paragraph's Deque is 3.3). Both fit, so nothing goes back to the user (config item 8).

## Blocks (`<h2>`), in page order

| # | block id | `<h2>` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|
| 1 | `queue` | The Queue Interface (OmniStax: ODS's heading also names Stack and Deque, which this block does not carry) | `ods:intro#the-queue-stack-and-deque-interfaces`, the opening paragraph and its list, the FIFO paragraph and fig. queue | no | add(x), remove(), queueing discipline, FIFO; `\figref{queue}` → "Figure 1.1", linked to `sim-fifo-queue`, which stands where the figure stood. Priority (chapter 9), LIFO (3.1 is Wikipedia's) and Deque (3.3) paragraphs not carried |
| 2 | `circular` | ArrayQueue: An Array-Based Queue (source) | `ods:arrays#sec:arrayqueue`, from the opening through "…does not exceed the size of a." | no | the section's one-sentence opening (Questions 1), ArrayStack a poor queue, the infinite array, modular arithmetic, the circular array |
| 3 | `arrayqueue` | ArrayQueue’s add(x), remove() and resize() (OmniStax: the source's section runs on) | `ods:arrays#sec:arrayqueue`, from the first code import to the end of "Summary" | no | four code sets (a.j.n, add, remove, resize), `\figref{arrayqueue}` → "Figure 2.2", linked to `sim-arrayqueue` where the figure stood; "the resize() operation of ArrayStack" linked to 2.2 (B18); Summary as `<h3>` with the theorem as a note; errata 24 and 25 |
| 4 | `linked-queue` | Queue Operations (source) | `ods:linkedlists#sec:sllist`, "Queue Operations" and the paragraph after thm:sllist | no | remove() as pop(), add(x) at the tail with the n = 0 case, two code sets; the tail-removal paragraph (n − 2 steps). The SLList Summary heading and theorem between them are not carried (the reconciled locator) |

**Code (decision 20).** Each `\codeimport` is a four-language code set: Python, Java and C++ by `tools/ods_listing.py` with `printed=True` (as 2.2), JavaScript the AI's translation of the Java, marked. ODS's Python SLList prints `remove()` as `_remove`, which returns `self.pop()`: that is ODS's code as its pseudocode extractor prints it, and the prose says the same. Two backward-compatible tool changes were needed (see Questions 4 and 5).

## Bridges

- **B11** and **B15**: lead, sentences 3–4 (above), AI-marked with the lead.
- **B18**: "the resize() operation of ArrayStack" → `/cs-interview-prep-ultra/ch02/2.2/#resize` (a link wrapping the source's words); the Sim's caption links the resize bound to 2.2's `#arraystack-cost`.

## Concepts

| id | kind | tier | statement (to ODS's words) | introducing span |
|---|---|---|---|---|
| `queue` | definition | Essential | A Queue is a collection with add(x) and remove(); its queueing discipline decides which value comes next, and a FIFO Queue removes values in the order they were added; enqueue(x) and dequeue() are the other names. | `queue`, "FIFO (first-in-first-out) Queue" |
| `circular-buffer` | definition | Essential | A circular array keeps n elements at a[j mod length(a)], …, a[(j+n−1) mod length(a)]; modular arithmetic wraps an index past length(a) − 1 to the start, so a finite array simulates an infinite one while the elements fit. | `circular`, "circular array" |
| `array-queue` | result | Essential | ArrayQueue: j and n in a circular array; add(x) writes a[(j+n) mod length(a)], remove() takes a[j] and advances j, O(1) ignoring resize(); resize() unrolls into b[0..n−1] of size 2n and sets j = 0; O(m) resize time over m operations. | `arrayqueue`, the theorem's first sentence |
| `queue-linked-list` | skill | Essential | An SLList: remove() takes the head (as pop()), add(x) links after tail or sets head = tail when n = 0, both O(1); tail removal needs the node before tail, n − 2 steps from head. | `linked-queue`, "An SLList can also implement the FIFO queue operations" |

Edges (Hasse-reduced, the map's): `queue → interface-vs-implementation`; `circular-buffer → dynamic-array`, `circular-buffer → queue`; `array-queue → dynamic-array-cost`, `array-queue → circular-buffer`; `queue-linked-list → singly-linked-list`, `queue-linked-list → queue`. Coverage `uses`: `queue` uses interface-vs-implementation; `circular` uses queue and dynamic-array; `arrayqueue` uses circular-buffer, array-resize and dynamic-array-cost; `linked-queue` uses singly-linked-list and queue. Terms pass: 43 candidates, 40 marked (`terms.jsonl`); left in ink: the grocery "queue (or line-up)" and the two "head/tail of the list" in the SLList block.

## Errata

- **24** (`arrayqueue`, marker after the theorem's "add(i,x) and remove(i) operations"): a Queue's operations are add(x) and remove().
- **25** (`arrayqueue`, marker after "of size 2n"): the code allocates max(1, 2n).
- **New: the figure caption** (ODS Figure 2.2, "A sequence of add(x) and remove(i) operations on an ArrayQueue"): remove(i) should be remove(). A correction row with `figure: sim-arrayqueue` (no marker; the app numbers it under the original caption). For the chapter pass to add to the reconciled list.
- Not noted: "the mod operate is represented" (a typo that does not change the meaning).

## Derivation candidates

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| 10 + 5 = 15 ≡ 3 (mod 12); 15 mod 12 = 3 | two displays, one move each | 1 | 0 | not built (an example, not a chain) |
| the theorem's O(m) resize time | stated, proof "very similar to ArrayStack" | 5 (2.2's lemma) | 1 fact imported + 5 unprinted = 6 | not built: the proof is 2.2's `drv-arraystack-sum` for the same resize rule; the caption links it, and `sim-arrayqueue` checks Σnᵢ ≤ 2m + 2r live |
| tail removal takes n − 2 steps | prose | 1 | 1 | not built |

## Figures

```
sim-fifo-queue · Sim (original: ODS Figure 1.1, figs/queue.ipe, "A FIFO Queue.", behind the toggle) · queue · flow by animation · arrows: kinematic (a value entering at the back, the front value leaving) · moving: one call per beat, 10 calls (three adds, then adds and removes interleaved until empty), cycle with the app's transport · no sliders (the calls are the idea; FIFO is the only discipline the block carries) · headline: the call, "remove() returns a, the oldest value in the queue." · readout: "added in the order a, b, c, d, e \\ removed in the order a, b, c" · graph: none · 2D · code: none (the Queue interface is an interface, the book's RULES' exception) · text 22–36 logical
sim-arrayqueue · Sim (original: ODS Figure 2.2, figs/arrayqueue.ipe, behind the toggle, its caption corrected by err-caption-ops) · circular-buffer, array-queue, queue · flow by animation (copies into b); invariant made visible (the live cells j … j+n−1 mod length(a) shaded in the index tint on the ring and the strip); variation by input · arrows: kinematic (j turning one cell on, a copy from a[(j+k) mod length(a)] to b[k]) · moving: one stop per call and one per resize, copy by copy stepped into · choice (four inputs): Figure 2.2's calls (default: a b c at a[2..4] of 6, add(d), add(e), remove(), add(f), add(g), add(h)*, remove()) | wrap around (ring of 8, five add/remove pairs, no resize) | grow from empty (wraps at length 4, then resizes unrolling from j = 1: the adversarial resize case) | drain (a wrapped ring of 8 emptied, shrinking three times) · headline: the call and its index, "add(e) writes e at (j + n) mod length(a) = (2 + 4) mod 6 = 0: past the last cell, back round to 0." · graph: none; the ring left and the array right, b below the array during resize, and three count lines · 2D · code: ods ArrayQueue add(x), remove(), resize() (Python from arrayqueue.py, canonical, printed=True; Java and C++ as ODS prints them; JavaScript AI) · blocks: add [1–5] "add(x)" touches a, j, n, x: grow [2] "resize a if it is full"; store [3–4] "write x at (j + n) mod length(a) and count it" · remove [7–12] "remove()": take [8–9] "take a[j], and move j one cell on, mod length(a)"; shrink [10–12] "count it, and shrink a if length(a) ≥ 3n" · resize [14–19] "resize(): unroll the n elements into b[0], …, b[n − 1]": alloc [15] "allocate b of length max(1, 2n)", copy [17] "copy a[(j + k) mod length(a)] into b[k]", per k, swap [18–19] "b becomes a, and j = 0" · level: default (one stop per call, and per resize inside it) · invariant: the queue a[j], …, a[(j + n − 1) mod length(a)] shaded; readout lines "the queue: a[j] = a[3], …, a[(j + n − 1) mod 6] = a[0]   n = 4 ≤ length(a) = 6" and "next add writes a[(j + n) mod length(a)] = a[(3 + 4) mod 6] = a[1]" (the dashed cell, index colour) · cost: copies Σnᵢ against 2m + 2r (2.2's lemma, true at every stop), and per resize "calls since the last ≥ nᵢ/2 − 1" · referents: a, b, j, n, k · text 22–34 logical
```

The debugger is the centrepiece: the wraparound index (j + n) mod length(a) is written out with its live numbers at every add, and remove()'s (j + 1) mod length(a) at every step of j; the ring and the strip light the same cell. The trace agrees with ODS's own Python ArrayQueue call by call on all four inputs (`scratchpad/sec32/check_trace.py`, ODS's Python under the AI port numpy.object → object, run `python3 -I`).

**Source figures, keep or drop.** ODS Figure 1.1 (queue.ipe) → `sim-fifo-queue`; ODS Figure 2.2 (arrayqueue.ipe) → `sim-arrayqueue`; both rendered by `render_originals.py` to `media/ch03/`. ODS's SLList figure (sllist.ipe) belongs to the SLList opening, which is not carried: dropped. ODS's "% TODO: figure" under the circular array: nothing to keep.

**Extra simulation, not built (root item 15):** `sim-linked-queue`, SLList add(x)/remove() with head and tail pointers and the n = 0 case, plus the n − 2 step walk that tail removal would need. The two code sets and the exercise carry it; built only if picked.

## Exercises

| concept | item | shape | status |
|---|---|---|---|
| circular-buffer, queue | `exercism:circular-buffer` (14 canonical cases) | `code`: run(capacity, operations) given; references Python and JavaScript AI-written (Exercism's example cannot store 0), marked; 2 AI tests (storing and overwriting 0, several laps), marked | ships (c1) |
| queue-linked-list, queue | `icc:stacks_queues/queue_list` (1 test, 5 asserts) | `code`: run(ops) given; Python reference icc's; JavaScript AI; 2 AI tests (drain then reuse, interleaved), marked | ships (c2) |
| queue | OpenDSA StackQMCQ q* (8 MC) | `choice` | waits for the OpenDSA converter (as every chapter 2 section) |
| queue | OpenDSA enqueue/dequeue proficiency (4), Wikibooks A-level queue traces (8, one held for ch. 9) | `sequence` | wait for the answer type |
| array-queue | ODS harness `test_arrayqueue.py`; ODS Exercise 2.3 (RandomQueue) | — | no printed statement / no tests: left out |
| queue-linked-list | SICP 3.21, 3.22; pythonds exercises (NC, unkeyed) | — | left out |
| queue | icc queue_from_stacks | — | rejected (decision 19) |
| circular-buffer | ODS Exercise 2.8 | — | held for chapter 7 (bits) |

Both references were run isolated (copied to a fresh scratch directory, `python3 -I`; JavaScript under node): c1 16/16 in both languages, c2 3/3 in both.

## Referents

`a` (the backing array), `b` (the array resize() fills), `j` (the index of the next element to remove), `n` (the number of elements), `k` (the element resize() is copying): the code variables `sim-arrayqueue` draws, each in its colour in the code panel, the drawing and the caption, and marked in the maths of `circular` and `arrayqueue` (`\htmlData{ref=…}`), never ODS's "integer a" or its k and m of the mod definition. Positions without a name (the next write index, the index labels) wear `index`; values `key`; length(a) and length(b) `size`; copies `cost`.

## References item

None written: the schema has no field yet (as chapters 1 and 2).

## Attribution

- Pat Morin, *Open Data Structures*, §1.2 (The Queue interface), §2.3 ArrayQueue and §3.1 SLList (Queue Operations), pseudocode edition and its Java, C++ and Python sources, CC BY 2.5 Canada: "adapted". Figures 1.1 and 2.2 are ODS's own (rendered from its .ipe).
- Exercism (MIT) and Interactive Coding Challenges (Apache 2.0), credited on the cards from `exercise_sources`.
- `notes`: what is left out. `ai`: text and figures, this model; `built` 2026-11-09.

## Questions (decided here, new to this section)

1. **ArrayQueue's opening sentence** ("In this section, we present the ArrayQueue data structure, which implements a FIFO queue…") stands before the reconciled locator's start ("Notice that an ArrayStack…"). *Decided:* carried at the head of `circular`, under the source's own heading: it is the section's opening, the block is kept whole, and it names the structure the block's later sentences use. The locator says so.
2. **Two OmniStax headers.** ODS's "The Queue, Stack, and Deque Interfaces" names two structures the block does not carry; ArrayQueue's code half has no heading. *Decided:* "The Queue Interface" (ODS's own form, as its "The List Interface") and "ArrayQueue’s add(x), remove() and resize()".
3. **The SLList Summary theorem** between "Queue Operations" and the tail-removal paragraph. *Decided:* not carried (the reconciled locator; it states Stack operations that 3.1 gives from Wikipedia).
4. **`%` inside ODS's #code#.** `tools/read_latex.py` stripped it as a TeX comment, cutting `#a[(j+n)%a.length]#` and the paragraph after it. *Decided:* a `%` inside a space-free `#…#` run is kept, and set as the edition's `\bmod`; a field `#tail.next#` as `\mathit{tail}.\mathit{next}`, and `#tail#`, `#head#`, `#null#` in maths as the edition sets them (`\mathit{nil}` for null). Every earlier section rebuilt byte-identical.
5. **ODS's C++ SLList** defines its methods inside the class, which `tools/ods_listing.py` did not read (the listings came out empty); and three one-line fields (`a.j.n`) printed with a blank line before the third. *Decided:* both fixed, as snarf-cpp.pl reads them; every earlier listing unchanged except listings that were empty or split before (ArrayDeque.a.j.n, SEList's C++, etc., for 3.3 and 3.6).
6. **The figure caption's remove(i).** *Decided:* a correction row on the figure (root item 13), listed for the reconciled errata.
7. **A figure for the linked queue.** *Decided:* not built; offered as an extra (above).
