# Plan: 2.2 Dynamic arrays

Status: **plan, built in the same run** (brief `briefs/section-build.md`: chapters 2 and 3 have no separate plan review; chapter 1's answered questions settle what they settle, and new questions are decided below and listed at the end). Read for this plan: as chapter 1's plans, plus `ods/latex/arrays.tex` lines 1–258 (the chapter opening, §ArrayStack, §FastArrayStack), `ods/latex/snarf-python.py`, `snarf-java.pl` and `snarf-cpp.pl` (how each edition prints `#code#` and `\codeimport`), `ods/java/ods/ArrayStack.java`, `FastArrayStack.java`, `ods/cpp/ArrayStack.h`, `FastArrayStack.h`, `ods/python/ods/arraystack.py`, `fastarraystack.py`, `utils.py`, `figs/arraystack.ipe` (rendered), `judgements/ch02.md` §2.2, `judgements/ch01-03-reconciled.md` item 2, B6, B8, B18, erratum 19, and `judgements/ch01-03-references.md` (ODS notes).

One source, *Open Data Structures* (`ods`, CC BY 2.5 Canada), pseudocode edition for the prose (METHOD decision 20), its Java, C++ and Python sources for the code. No translation. 5 blocks, 5 concepts, 1 Sim, 2 derivations, 1 erratum, no shipped exercise.

## Lead (AI-marked, 78 words, B6 and B8)

> An Essential section on the array that grows and shrinks behind a list, with ODS's ArrayStack; block copying is Advanced. Arrays are indexed from 0. ArrayStack implements Section 2.1's List interface and is named by the rule at the end of that passage. Section 1.5 doubled an array only as it grew and wrote m for its capacity; here length(a), a.length in Java, is the capacity, m counts operations, and the array also shrinks when length(a) ≥ 3n.

Tier: Essential. Of another tier: `block-copy` (Advanced). Indexing: 0-based, `a[0], …, a[n−1]` (reconciled table). Bridges: **B8** (sentence 3) and **B6** (sentence 4). B6 is worded with the pseudocode edition's spelling: its `snarf-python.py` prints `#a.length#` as length(a), so the page reads length(a) where the judges quoted the Java edition's a.length; the lead names both. m is ODS's number of `add`/`remove` calls in the chapter opening, the lemma and the theorem, which is the third of the uses 1.5's erratum 14 lists.

## Blocks (`<h2>`), in ODS's order

| # | block id | `<h2>` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|
| 1 | `arrays-intro` | Array-Based Lists (source: the chapter title) | `ods:arrays#chap:arrays`, the chapter opening (the table, the three points and the amortized paragraph) | no | the running-time table (ArrayStack, ArrayDeque, DualArrayDeque, RootishArrayStack), the three points on arrays, "the total cost of growing and shrinking … is O(m)". The `\cpponly` paragraphs on ODS's C++ `array` class are not in the pseudocode edition and are not carried |
| 2 | `arraystack` | ArrayStack: Fast Stack Operations Using an Array (source), with The Basics as `<h3>` | `ods:arrays#sec:arraystack`, the opening and The Basics | no | the backing array a, n, a[0], …, a[n−1], length(a) ≥ n; get/set; add(i,x) and remove(i) with their O(n − i) costs; `\figref{arraystack}` → "Figure 2.1", linked to `sim-arraystack`, which stands where the figure stood; four code sets (fields and size, get/set, add, remove) |
| 3 | `resize` | Growing and Shrinking (source) | `ods:arrays#growing-and-shrinking`, the first two paragraphs and resize() | no | resize() allocates 2n and copies n elements; O(n); one code set |
| 4 | `arraystack-cost` | Amortized cost of resizing (OmniStax: the source's subsection runs on under "Growing and Shrinking"), with Summary as `<h3>` | `ods:arrays#growing-and-shrinking`, from "The running time analysis from the previous section ignored…" to the end of the section: `lem:arraystack-amortized` with its proof, and the Summary (`thm:arraystack` and the push/pop paragraph) | no | the lemma (a note, eyebrow "Lemma"), its proof as running text with its footnote (a book note), the two derivations in place of the printed displays, erratum 19, the theorem (a note, eyebrow "Theorem"), push(x) as add(n, x) and pop() as remove(n − 1) |
| 5 | `fastarraystack` | FastArrayStack: An Optimized ArrayStack (source) | `ods:arrays#sec:fastarraystack` | no | for loops against memcpy/memmove, std::copy, System.arraycopy; the speed-up of 2 to 3; one code set where the Java and C++ editions print FastArrayStack's code |

**Code (decision 20).** ODS's `\codeimport{ods/Class.method…}` prints, in each edition, the named methods of that edition's source. Each becomes a four-language code set: Python from `python/ods/<class>.py` (verbatim; the shown methods do not touch `numpy.object`, so none carries the AI mark), Java from `java/ods/<Class>.java` and C++ from `cpp/<Class>.h`, each as ODS's own snarf scripts print them (the bounds checks dropped, `public`/`protected` and `Math.`/`f.` hidden, the class prefix taken off a C++ method), and JavaScript as an AI translation of the Java, marked. A new reader, `tools/ods_code.py`, does the selection. The pseudocode edition prints no FastArrayStack code, but the Java and C++ editions do at the `\javaimport`, and the prose then speaks of "our C++ and Java implementations", so the set stands there (Python from `fastarraystack.py`, whose slices are Python's block moves; JavaScript `copyWithin`, AI).

**Inline code in the prose** follows the pseudocode edition's `translate_code`: a call is set upright (get(i), resize(), System.arraycopy(s,i,d,j,n)), `a.length` reads length(a), a variable ending in a digit takes a subscript (a₀). One departure: the edition's script strips every colon, so `std::copy(a0,a1,b)` would print "stdcopy"; the page keeps the C++ name, `std::copy`, as the Java and C++ editions print it (the converter's rule, listed in the spec).

Not carried: ODS's `\cpponly` text and `\cppimport` listings of its C++ `array` class (no pseudocode-edition text), everything from §ArrayQueue on (chapter 3).

## Bridges

- **B6** (lead): "Section 1.5 doubled an array only as it grew and wrote m for its capacity; here length(a), a.length in Java, is the capacity, m counts operations, and the array also shrinks when length(a) ≥ 3n." AI-marked with the lead.
- **B8** (lead): "ArrayStack implements Section 2.1's List interface and is named by the rule at the end of that passage."
- B18 (chapter 3's pointers to this lemma) lands on block `arraystack-cost` (`/cs-interview-prep-ultra/ch02/2.2/#arraystack-cost`); chapter 3's builders link there.

## Concepts

| id | kind | tier | statement (reworded to ODS where the map's is CIU's) | introducing span |
|---|---|---|---|---|
| `dynamic-array` | definition | Essential | A list kept in a backing array a that is usually larger than it needs to be: n counts the elements, stored in a[0], …, a[n−1], and length(a) ≥ n at all times; when the array is full a larger one is allocated and the elements copied into it. | `arraystack`, "An ArrayStack implements the list interface using an array a, called the backing array" |
| `array-resize` | skill | Essential | resize() allocates an array b of size 2n, copies the n elements of a into its first n positions and makes b the new a, in O(n) time; add(i,x) calls it when a is full and remove(i) when length(a) ≥ 3n. | `resize`, its first sentence |
| `dynamic-array-cost` | result | Essential | Ignoring resizing, get(i) and set(i,x) take O(1) time and add(i,x) and remove(i) O(1 + n − i); from an empty ArrayStack, any m calls to add(i,x) and remove(i) spend O(m) time in all calls to resize(), so push and pop at the end run in O(1) amortized time. | `arraystack-cost`, the lemma's statement |
| `block-copy` | skill | Advanced | Shifting and copying with a platform's block-move functions (memcpy and memmove in C, std::copy in C++, System.arraycopy in Java) in place of for loops leaves the asymptotic running times unchanged but can be several times faster; ODS measured a factor between 2 and 3. | `fastarraystack`, "specific functions that are very efficient at copying and moving blocks of data" |
| `implement-vector` | skill | Essential | Build a resizable array: fields a and n, size, get, set, add(i,x) and remove(i) that shift the elements after i, and a private resize that doubles the array when it is full and shrinks it when it is two-thirds empty; ODS's ArrayStack is such a class. | `arraystack-code`, the id on the first ArrayStack code set (fields a and n and size()) |

Edges (Hasse-reduced, as the map has them): `dynamic-array` → `running-time-guarantees` (1.4), `array`, `list-interface` (2.1); `array-resize` → `dynamic-array`; `dynamic-array-cost` → `amortized-analysis` (1.5), `array-resize`; `block-copy` → `dynamic-array`; `implement-vector` → `pointer-arithmetic` (2.1), `dynamic-array`. The 2.1 prerequisites are written once 2.1's concepts exist; until then they are handed to the chapter pass.

Coverage beside the introductions: `arrays-intro` uses `dynamic-array` and `amortized-analysis`; `arraystack` uses `list-interface`; `resize` uses `dynamic-array`; `arraystack-cost` uses `amortized-analysis` and `array-resize`; `fastarraystack` uses `dynamic-array`.

## Errata

- **19** (`arraystack-cost`, marker after "is at least n_i/2." in the proof): the claim the proof needs, the one its sum uses and the one its second case proves, is n_i/2 − 1; the first case gives n_i/2, the second only n_i/2 − 1. No other erratum: the chapter's list assigns none else here.

## Derivation candidates

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| the proof's three displays: Σ(nᵢ/2 − 1) ≤ m, "which is equivalent to" Σnᵢ ≤ 2m + 2r, "On the other hand" Σ O(nᵢ) ≤ O(m + r) = O(m) | displays with words between, inside a printed proof | 5 (expand the sum; move r; double; bound the resize time by the sum; r ≤ m) | printed proof: qualifies (29.1) | **build** `drv-arraystack-sum`, *Derivation · all calls to resize() take O(m) time*; replaces the three displays and the two phrases between them; facts: the per-resize bound (proved below in the same proof), the m calls in all, r ≤ m, resize() costs O(n) (block `resize`) |
| the second case's chain R ≥ length(a)/2 − 1 − length(a)/3 = length(a)/6 − 1 = (length(a)/3)/2 − 1 ≥ nᵢ/2 − 1 | an `align*` | 3 | printed: qualifies; chapter 1's policy builds printed chains of three moves or more | **build** `drv-shrink-case`, *Derivation · at least nᵢ/2 − 1 removes since the last resize*; replaces the align; facts: at least length(a)/2 − 1 elements after the previous resize (with the footnote's case), nᵢ ≤ length(a)/3 |
| resize() costs O(n) | prose | 1 | 0 | not built |

`check_derivations()` in the spec checks every line numerically over random operation sequences (the lemma's inequality, the per-resize bound, the align's identities).

## Figures

```
sim-arraystack · Sim (original: ODS Figure 2.1, figs/arraystack.ipe, "A sequence of add(i,x) and remove(i) operations on an ArrayStack…", behind the toggle) · dynamic-array, array-resize, dynamic-array-cost, implement-vector · flow by animation (elements shifted and copied); invariant made visible; variation by input · arrows: kinematic (an element copied one cell right or left, or down into b) · moving: one call per step, copy by copy when stepped into · choice (select, five inputs): Figure 2.1's calls (default: b r e d in length 6, add(2,e), add(5,r), add(5,e), remove(4) three times, set(2,i)) | append from empty (add(n, x) twelve times) | add at the front (add(0, x) eight times: the shifting worst case) | grow then shrink (eight appends, eight removes from the end) | at the boundary (four appends, then add and remove six times at length(a) = 4, the case the 3n rule protects) · headline: the call and what it moved, "a is full, so add(5, e) first calls resize(): 6 elements copied into an array of 12" · graph: none; below the arrays, the calls so far with an asterisk on each that resized (as Figure 2.1 marks them) and one line per resize: "resize 1 in add(5, e): n₁ = 6 copies, 3 calls since the last resize ≥ n₁/2 − 1 = 2" · 2D · code: ods ArrayStack set(i,x), add(i,x), remove(i), resize() (Python from arraystack.py, canonical, bounds checks dropped as ODS prints them; Java and C++ as ODS prints them; JavaScript AI) · blocks: set [1–4] "set(i, x) overwrites a[i]" touches a, i; add [6–10] "add(i, x)" touches i, x, n: room [7–8] "make room for x" (grow [7] "resize a if it is full", shift [8] "copy one element a cell to the right", per copy); store [9–10] "store x in a[i] and count it" · remove [12–17] "remove(i)": close [13–14] "take a[i] out and close the gap" (shiftl [14] "copy one element a cell to the left", per copy); shrink [15–17] "count it, and shrink a if length(a) ≥ 3n" · resize [19–22] "resize(): copy the n elements into an array of size 2n": alloc [20] "allocate b of size 2n", copy [21] "copy one element into b", per copy, swap [22] "b becomes a" · level: default (one stop per call, and one per resize inside it) · invariant: a[0..n−1] shaded in the index tint, the rest of a hollow; readout "n = 7 ≤ length(a) = 12" · cost: copies in resize() Σnᵢ against 2m + 2r (the lemma's sum, true at every stop), and shifts per call against n − i · inputs: as above, adversarial first-class (add at the front for shifting; the boundary for resizing) · referents: a, b, i, n (code variables the drawing names) · text 26–34 logical
```

The figure stands where ODS's Figure 2.1 stood (after the add(i,x) paragraph of The Basics), and opens on the figure's own calls (root 14: the book's numbers on load). It is kept apart from 1.5's `sim-pay-for-doubling`, which counts appends only, three ways: this one runs ODS's own code with inserts anywhere, removes and shrinking, and counts the lemma's sum; its caption links to 1.5's Sim for the three methods instead of repeating them.

**Source figures, keep or drop.** ODS Figure 2.1 (arraystack.ipe) → `sim-arraystack`, its image rendered with `iperender` to `media/ch02/ods-arraystack.png` behind the toggle, its caption as `original_caption` (plain text). No other figure in the passage (two "% TODO: Add figure" comments only).

## Exercises

None ships (config: the chapter's exercise choice).

| concept | item | shape it would take | why not now |
|---|---|---|---|
| dynamic-array-cost | OpenDSA ALMCQinsarb, ALMCQdelarb, ALMCQsucc (keyed, position-i model, fit) | `choice` | wait for the OpenDSA converter |
| dynamic-array-cost | OpenDSA ALMCQinscurr, ALMCQdelcurr, ALTFpred | — | need the current-position list model the book does not teach: left out |
| dynamic-array-cost | OpenDSA AlistInsertPRO, AlistRemovePRO | `sequence` | wait for the `sequence` answer type |
| dynamic-array, implement-vector | CIU "Implement a vector" | `code` | no source tests (decision 19 ships code items with source tests only) |
| dynamic-array | ODS Exercise 2.1 (written) | `open` | unkeyed |
| dynamic-array-cost | ODS Exercise 2.2 (written) | `open` | unkeyed |
| block-copy | ODS Exercise 2.7 | — | needs ArrayDeque: held for 3.3 |
| dynamic-array-cost | MIT 6.006 S20 prob1 1-3 (NC) | `open` | double-ended sequence: held for 3.3 |

Test sources with no printed statement (TheAlgorithms `dynamic_array.py`, ODS `test_arraystack.py`, `test_fastarraystack.py`) are named as such.

## Referents

`a` (the backing array), `b` (the new array resize() fills), `i` (the index of the call), `n` (the number of elements): the code variables the drawing names, each in its referent colour in the code panel, the drawing, the watch and the caption, and `i` and `n` in the maths of the `arraystack` block where the figure stands (as 1.3 marks its `i`). length(a) and 2n wear `size`; copies, shifts and the bound wear `cost`; the elements wear `key`; the shading of a[0..n−1] is the `index` tint.

## References item

None written: the schema has no field yet (as chapter 1).

## Attribution

- Pat Morin, *Open Data Structures*, Array-Based Lists (§2.1 ArrayStack, §2.2 FastArrayStack), pseudocode edition and its Java, C++ and Python sources, CC BY 2.5 Canada: "adapted". Figure 2.1 is ODS's own (rendered from its .ipe).
- `notes`: what is left out (the C++ edition's `array` class, the chapter's later sections, which are chapter 3's). `ai`: text (lead, header, notes, the JavaScript, the correction) and figures, this model; `built`.

## Questions (decided here, new to this section)

1. **ODS's `\codeimport` listings.** The pseudocode edition prints pseudocode generated from the Python; decision 20 gives ODS's code from its Java and C++ plus Python. *Decided:* each listing is a four-language code set (Python, Java, C++ as ODS's sources and snarf scripts print them; JavaScript AI), with the bounds checks dropped in every language as each of ODS's editions drops them.
2. **FastArrayStack's code.** The pseudocode edition shows none; the Java and C++ editions do, and the prose names them. *Decided:* show the set at the `\javaimport`, Python from ODS's `fastarraystack.py`.
3. **`std::copy`.** The edition's script prints "stdcopy". *Decided:* keep the C++ name; a converter rule, not a correction note.
4. **B6's spelling.** The pseudocode edition prints length(a). *Decided:* the lead says "length(a), a.length in Java".
5. **The chapter opening's table** names three chapter-3 structures. *Decided:* kept as printed (the source's passage, kept whole); no link (no reference in words).
6. **implement-vector's span.** It has no prose; its explanation is the ArrayStack code. *Decided:* an id on the first ArrayStack code set, `arraystack-code`.
7. **An "implement a vector" code card** now that the runner exists (RULES, Template sections). *Decided:* not shipped: CIU's checklist has no source tests and decision 19 ships code items with source tests only; named in `exercise_notes`.
