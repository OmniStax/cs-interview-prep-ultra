# Plan: 2.1 Arrays and the list interface

Status: **plan, built from in the same run** (brief `briefs/section-build.md`: no separate review for chapters 2 and 3), 2026-11-09. Read for this plan: root `RULES.md`; the book's `RULES.md`, `COLOR.md`, `METHOD.md` (§1–§3, §5, decisions 1–21), `LOG.md` (passes 1–8); `ch02/config.md` and `exploration.md`; `judgements/ch01-03-reconciled.md` (with "Rulings applied 2026-11-08"), `judgements/ch02.md` (2.1), `judgements/ch01-03-references.md`; the 2.1 rows of `concept-map/concepts.json` and `toc.md`; `ch01/plans-summary.md`, `ch01/1.1/plan.md`, 1.1's and 1.5's builds; the winning passages in the cache: `wikipedia/Array_data_structure.wiki` (revision 1375967624), `wikipedia/Pointer_computer_programming.wiki` (revision 1382564071), `ods/latex/intro.tex` 257–306.

Sources on the page: Wikipedia (`wikipedia`, CC BY-SA 4.0; two articles) and ODS (`ods`, CC BY 2.5 Canada). No translation. 6 blocks, 3 concepts, 3 Sims, 1 photograph, 0 derivations.

## Lead (AI-marked, 66 words)

> An Essential section on the array, whose elements all have one size so that each one's address can be computed from its index; on how C defines indexing as pointer arithmetic; and on the List interface. Indices start at 0 throughout, as in x₀, …, x<sub>n−1</sub>. Stacks, queues and deques come in Sections 3.1–3.3, so the List passage's Deque operations are a preview.

Tier: Essential, all three concepts. Indexing: 0-based (Wikipedia Array and C; ODS x₀ … x<sub>n−1</sub>); Wikipedia's 1-based labels a₁₁ … a₂₃ on a C array are erratum 16, a note, not a lead sentence. Bridge B7 (the last sentence; reconciled.md, `config.md` item 9). The lead went through `/humanizer:humanizer` and the repository's `humanizer` skill.

## Sub-concept blocks (`<h2>`), in page order

Wikipedia's Array article in its own order, then its Pointer article's C arrays, then ODS. Every block carries `data-source` and `data-locator`; none is translated.

| # | block id | `<h2>` | `data-source` | `data-locator` | what it holds |
|---|---|---|---|---|---|
| 1 | `array` | Arrays (OmniStax: the lead has no heading) | wikipedia | `wikipedia:Array_(data_structure)`, the lead | the definition, the 2000 … 2036 example, why arrays matter, the senses of "array"; its 5 citations |
| 2 | `addressing` | Element identifier and addressing formulas (source) | wikipedia | `wikipedia:Array_(data_structure)#Element identifier and addressing formulas`, its opening, ===One-dimensional arrays=== and ===Multidimensional arrays===, to the end of the latter | 0-, 1- and n-based indexing, B + c·i, re-basing (erratum 15), B + c·i + d·j, the k-dimensional formula as a display, `int a[2][3]` (erratum 16); `sim-address` after the re-basing paragraph, `sim-row-major` after the `a[2][3]` paragraph |
| 3 | `efficiency` | Efficiency (source) | wikipedia | `wikipedia:Array_(data_structure)#Efficiency`, its opening, before ===Comparison with other data structures=== | constant-time store and select, O(n) space, cache lines, memcpy, packed arrays |
| 4 | `iliffe` | Iliffe vectors (OmniStax: the paragraph's own subject; its heading, "Comparison with other data structures", names the four paragraphs not carried) | wikipedia | `wikipedia:Array_(data_structure)#Comparison with other data structures`, the Iliffe-vector paragraph and its image | jagged arrays, the vector of row pointers; `photo-iliffe` where the article sets its image |
| 5 | `c-arrays` | C arrays (source) | wikipedia | `wikipedia:Pointer_(computer_programming)#C arrays` | a[i] ≡ \*(a + i), the two C listings, `i[a]` and C29 (Questions), sizeof, the little-endian byte table, the four bullets on `a`, `a + 1`, `*a`, `a[i]` |
| 6 | `list-interface` | The List Interface: Linear Sequences (source) | ods | `ods:intro#the-list-interface-linear-sequences` (whole subsection, fig. list) | the five operations with their semantics, the Deque mapping as an aligned display, `sim-list` where ODS sets Figure 1.4, the naming paragraph (ArrayDeque) |

Not carried: the Array article's History, Applications, Dope vectors, Compact layouts, Resizing, Non-linear formulas, the other four paragraphs of Comparison, Dimension, See also; the Pointer article outside C arrays. Wikipedia's links are kept as their text, not as links (the book links only to its own sections; nothing in these passages points at a section by name). ODS's `\figref{list}` prints "Figure 1.4", linked to `sim-list` (RULES Cross-references).

**How the text is made.** `tools/build_text.py` with the section's `build_spec.py`, as 1.1. No shared tool reads wikitext yet, so the section brings `readers.py` (a wikitext reader for these two passages; and the ODS block through `tools/read_latex.py`, whose ODS dialect already sets `#code#` as the pseudocode edition does, with an `eqnarray*` read as an aligned display first). `build_text.py` gains one backward-compatible branch: a block whose `reader` is a function is read by it. 1.1 rebuilt from a frozen copy is byte-identical. Wikipedia's `<ref>` citations are book footnotes under the numbers the article prints them under (named refs keep their first number; a second use of one is a note of its own with the same number, so each note has one marker).

## Concepts

| id | kind | tier | statement (for `book.json`) | the one span that introduces it |
|---|---|---|---|---|
| `array` | definition | Essential | An array is a collection of elements of one memory size, each identified by an index (or a tuple of indices), stored so that each element's address is computed from its index by a formula: B + c·i in one dimension, B + c·i + d·j in two. Store and select take constant time and the array takes O(n) space. | `array`, "an **array** is a data structure" |
| `pointer-arithmetic` | skill | Essential | In C, a[i] is defined as \*(a + i): an array's name evaluates to a pointer to its first element, and adding i to a pointer moves it i elements on, i times the element's size in bytes. | `c-arrays`, "array indexing is formally defined in terms of pointer arithmetic" |
| `list-interface` | definition | Essential | A List represents a sequence x₀, …, x<sub>n−1</sub> with size(), get(i), set(i, x), add(i, x), which shifts x<sub>i</sub>, …, x<sub>n−1</sub> one place right, and remove(i), which shifts the later values left. These subsume the Deque: addFirst(x) is add(0, x), removeLast() is remove(size() − 1). | `list-interface`, "A List … represents a sequence" |

Edges: `pointer-arithmetic → array` (the map's); `list-interface → interface-vs-implementation` (1.1), **new**: the passage names the List an interface in the sense 1.1 defines, and the judge's builder note says it rests on it (the map has no prerequisite for it; the chapter pass adds the edge to `tools/map/map.spec`). Hasse-reduced: neither reaches the other's prerequisite another way.

Forms (the book's Formulas list names "address = B + c·i"): `array` → `eq-address-1d` `\text{address} = B + c\cdot i` (main), `eq-address-2d` `B + c\cdot i + d\cdot j`, `eq-address-kd` `B + c_1 i_1 + c_2 i_2 + \dots + c_k i_k`; `pointer-arithmetic` → `eq-c-subscript` `a[i] \equiv {*}(a + i)`. No variables rows and no `\k` macros: the maths stays in ink, as in chapter 1 (LOG pass 8, "open").

Coverage: `array` introduces array; `addressing`, `efficiency`, `iliffe` reinforce array; `c-arrays` introduces pointer-arithmetic and uses array; `efficiency` uses `big-o` (O(n)); `list-interface` introduces list-interface and uses interface-vs-implementation.

## Errata (correction notes, AI-marked)

- **15** (`addressing`, ===One-dimensional arrays===): "the base address B is replaced by B + 30c" should be B − 30c. The marker stands after "B + 30c". `sim-address` shows it: moving the first index from 1 to 31 moves B by −30c.
- **16** (`addressing`, ===Multidimensional arrays===): "a₁₁, a₁₂, a₁₃, a₂₁, a₂₂, a₂₃" names a C array's elements from 1; C counts from 0 (a[0][0] … a[1][2]). The marker after "a₂₃.".
- **New: ODS Exercise 2.5** (`c1`'s prompt): "for all i ∈ {0, …, a.length}" should end at a.length − 1. A correction in the card's prompt (content-format: "a correction may also stand in an exercise's prompt").
- **17** ("declared obsolescent as of C29"): not corrected. It is checked as far as this session can reach (Questions, 1), and nothing found says it is wrong.
- 18 (Pointer #Multiple indirection) is 2.5's.

## Derivation candidates (root item 29)

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| address = B + c·i | stated, not derived | 0 | 0 | not a derivation |
| re-basing: (B − 30c) + c·(i + 30) = B + c·i | one sentence, hidden | 1 | 0 + 1 + 0 = 1 | not built (one move; the erratum's note carries the line) |
| 2D re-basing: B + c₁ − 3c₂ renumbers rows 1..10 to 0..9 and columns 1..20 to 4..23 | one sentence | 2 | 0 + 2 + 0 = 2 | not built |
| a[i] ≡ \*(a + i) ≡ \*(i + a) ≡ i[a] | code comments | 2 | 1 + 0 + 0 = 1 | not built |

## Figures

Plan lines in the `interactive-figures.md` format. No figure has code beside it: each idea is a property (the addressing formula; the List interface, which the book's RULES name as an exception), and the passages print no algorithm.

```
sim-address · Sim (original: Wikipedia "1D array diagram.svg", "Diagram of a typical 1D array", CC BY 4.0 Tropwine) · array, pointer-arithmetic · variation by slider; the formula made visible on the bytes · arrows: symbolic (B and the address, pointing at a byte) · still: a property under sliders, no clock · sliders: i (index, 0..4 counted from the first index), c (size, detents 1 | 2 | 4 | 8 bytes, default 4) · choice: first index 0 | 1 | 31 (the passage's three numberings; 31 is its re-basing example) · headline "a[3] is at 2000 + 4 · 3 = 2012." (the live numbers) · readout "address = B + c·i = 2000 + 4·3 = 2012", and when the first index is f ≠ 0, a second line "B = 2000 − f·c" · code: none (a property) · inputs: none · graph none · 2D
sim-row-major · Sim (original: Wikipedia "2D array diagram.svg", "Diagram of a typical 2D array", CC BY 4.0 Tropwine) · array · variation by slider · arrows: symbolic (grid cell to its place in memory) · still · sliders: i (row), j (column) · choice: int a[2][3] | A[3][4] (the passage's two examples; A[1][3] is the intro's) · headline "a[1][2] is at 2000 + 12 · 1 + 4 · 2 = 2020." · readout "address = B + c·i + d·j = 2000 + 12·1 + 4·2 = 2020" with c = (columns)·4, d = 4 · code: none (a property) · graph none · 2D
sim-list · Sim (original: ODS Figure 1.4, "A List represents a sequence indexed by 0, 1, 2, …, n − 1 …", rendered from figs/list.ipe as the pseudocode edition prints it) · list-interface · flow by animation; standardisation · arrows: kinematic (values displaced one place right by add, left by remove) · moving: one displaced value per beat, from the end for add and from i + 1 for remove, then x written; a get or set lifts or writes one cell · select: operation get(i) | set(i, x) | add(i, x) | remove(i) | addFirst(x) | removeFirst() | addLast(x) | removeLast(); slider i (index; for a Deque operation it takes the position the mapping gives and is held) · headline the operation and what it moves ("add(2, x) moves x₂, …, x₈ one place right, from the end, then sets x₂ = x.") · readout "add(i, x): x_{j+1} = x_j for j = n − 1, …, i · n = 9 → 10" and the values moved against n − i · code: none (the list interface, a property: RULES Figures) · opens on get(2) → c, the caption's call, on the figure's values a b c d e f b k c (n = 9; its "⋯" stands for nothing) · graph none · 2D
```

Labels: `sim-address` labels the cells' values and indices, B and the address (two pointers), the byte ticks unlabelled except at cell boundaries (five addresses at most, never colliding: the strip widens with c); `sim-row-major` labels the grid's cells a[i][j] and the memory cells by their row brackets ("row 0", "row 1"); `sim-list` labels indices and values, x on the new value. No referents: B, c, i and j are unnamed positions and sizes (exploration.md, "i, B and c are not referents"), and the List passage has no code variables. Types drawn: `index` (indices, addresses, B), `key` (values), `size` (c, d, n), `cost` (values moved, sim-list).

**Source figures, keep or drop.**

| source item | decision | reason |
|---|---|---|
| Wikipedia "1D array diagram.svg" (===One-dimensional arrays===) | replaced by `sim-address`, image behind the original toggle | a sketch of four cells; the Sim adds the addresses and the formula the text states |
| Wikipedia "2D array diagram.svg" (end of ===One-dimensional arrays===) | replaced by `sim-row-major`, image behind the toggle | a sketch of a grid; the Sim adds where each cell lies in memory |
| Wikipedia "3D array diagram.svg" (===Multidimensional arrays===) | **dropped** | the text never refers to it, and it shows nothing the 2D Sim does not (a cube of cells with no addresses) |
| Wikipedia "Array of array storage.svg" (Iliffe paragraph, 120 px, PD) | **kept, photograph** with the article's caption and the file's credit | it is the paragraph's own picture of the structure it names; nothing moves or varies in it |
| ODS Figure 1.4 (list) | replaced by `sim-list`, image behind the toggle | a sketch figure; the operations move values, which the still cannot show |
| the Pointer article's byte table | kept as a table (text) | a table of the passage, not a figure |

Images that are not cached are fetched from Wikimedia's thumbnail service at a standard width (the original files return 429 to scripts) and saved under `media/ch02/`.

## Extra simulations (root item 15), one line each, none built

- `sim-c-bytes`: the Pointer article's five ints at 0x1000 as bytes, a slider on i stepping `a + i` four bytes at a time and `*(a + i)` reading the little-endian word: the table, made to move. Not built: `sim-address` already shows the step of c bytes, and the table is printed beside it.

## Exercises (config.md, decision 19)

| id | concept | kind | item | answer | status |
|---|---|---|---|---|---|
| k1–k3 | array | check | LibreTexts Busbee 6.17 true/false, items 2, 3 and 5 (dimensions; loops over members; arrays rarely used) | `choice` True / False, keyed | ship |
| c1 | array | code | ODS Exercise 2.5, rotate(a, r), in place | `code`: the starter's `rotated(a, r)` calls the reader's `rotate` and returns a; AI tests (r = 0, 1, n − 1, n, > n, one element, repeats), AI references, cross-checked against keon `rotate` and TheAlgorithms `rotate_array` run isolated | ship; the erratum in its prompt |
| c2 | array | code | Exercism matrix (canonical data, 8 cases) | `code`: the starter's `answer(matrix_string, method, index)` calls the reader's `Matrix(…).row(index)` or `.column(index)`; source tests, AI references | ship |
| c3 | list-interface | code | ODS Exercise 1.6, the List part | `code`: the starter's `run(ops)` drives the reader's `ArrayList` and returns what each get and size returns; AI tests (fixed sequences, a seeded random one checked against a Python list), AI references | ship |
| nc-ps1-2 | list-interface | NC card | MIT 6.006 S20 Problem Set 1, Problem 1-2 | open, MIT's solution linked | `exercises-nc.json` |

`exercise_notes` names: Busbee items 1, 4 and 6–10 left out (C++ declarations, searching and sorting, which other chapters teach); the OpenDSA List MCQs waiting for the converter (each to be read against the current-position model when converted); ODS Exercise 1.7 (no tests) and the USet and SSet parts of 1.6 (chapters 5 and 8); Exercism list-ops (its operations take functions as arguments, which a JSON test cannot carry); Kattis nsum (rated trivial); TheAlgorithms `index_2d_array_in_1d` and `reverse_array` (test sources with no printed statement); no exercise for pointer-arithmetic (none open).

## Referents

None (above).

## References item

None: the schema has no field for it yet (1.1, 1.4).

## Attribution (footer, from `data-source`)

- Wikipedia contributors, "Array (data structure)" (revision 1375967624) and "Pointer (computer programming)" (revision 1382564071), CC BY-SA 4.0, adapted; the book's `wikipedia` row.
- Pat Morin, *Open Data Structures*, CC BY 2.5 Canada, adapted.
- Figure credits: the two Commons diagrams (CC BY 4.0, Tropwine) in the Sims' original captions; "Array of array storage.svg" (public domain) in the photograph's caption.
- `notes`: "The Array article's history, applications, other layouts and comparisons, and the Pointer article outside its section on C arrays, are not included." `ai`: text and figures, claude-opus-5-5 high; `built` 2026-11-09.

## Questions (decided here; the chapter pass may revisit)

1. **C29 (erratum 17).** The brief: keep the sentence as printed with a correction note only if it can be shown wrong. Checked: Wikipedia's "C29 (C standard revision)" (revision 1382563440, 2026-10-29, fetched in this session) names the revision after C23, informally C2Y, planned for 2029, and lists "for the array subscripting operator, the form i[a], where i has integer type, is marked obsolescent but remains supported", citing WG14 N3517 ("Array subscripting without decay", 10 March 2025). The primary source (open-std.org, and the Wayback Machine) is refused by this session's proxy, so the paper itself was not read. *Decided: no note; the sentence stands as printed.* A person should still read N3517 or the current working draft to confirm, and RULES' "Open: C29 check" stays open until then.
2. **The C listings.** C is none of the four languages, and Python, Java and JavaScript have no pointer arithmetic to translate into; C++ accepts the code, but labelling it C++ misnames it. *Decided: two lone `<pre>` (root item 19: a lone `<pre>` stays as it is), as 1.1 kept Martin's procedure.*
3. **Wikipedia's citations.** *Decided: carried as book footnotes under the article's own numbers* (the source prints them; RULES Apparatus), set from the citation templates' fields. 2.3 and 2.5 use Wikipedia too; the chapter pass should make them agree.
4. **ODS's names in the pseudocode edition.** The edition's script writes camel case with underscores (add_first(x)); `tools/read_latex.py` (changed by a concurrent section) keeps addFirst(x). *Decided: follow the shared tool, so chapter 2's ODS pages agree; the chapter pass decides which is right.*
5. **"the ArrayDeque class"** (ODS) names a class 3.3 carries. *Decided: no link* (B7 in the lead says where deques come; a class name is not a reference to a passage).
6. **Exercises whose entry is a method.** The code answer calls one function. *Decided: the starter holds a small driver the tests call (`rotated`, `answer`, `run`), and `changes` says so.*
7. **The tests of ODS Exercise 2.5.** `config.md` names keon's and TheAlgorithms' tests; their MIT notices would have no place to travel (a card's credit is its origin's). *Decided: AI tests of the statement, with keon's and TheAlgorithms' functions run against them isolated as a cross-check.*
