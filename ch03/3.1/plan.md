# Plan: 3.1 Stacks and bracket matching

Status: **plan, built from in the same run** (brief `briefs/section-build.md`: chapters 2 and 3 have no separate plan review), 2026-11-09. Read for this plan: the root and book rules, `COLOR.md`, `METHOD.md` (§1–§3, §5, decisions 1–21), `LOG.md` (passes 1–8), `ch03/config.md` and `exploration.md`, `judgements/ch03.md` §3.1, `judgements/ch01-03-reconciled.md` (final table, B12, indexing, errata, "Rulings applied"), `judgements/ch01-03-references.md`, the concept rows, chapter 1's and chapter 2's built pages (2.3 and 2.5 as the nearest models: Wikipedia wikitext, debugger figures, Exercism and icc cards), and the cached sources: `sources/_cache/wikipedia/Stack_abstract_data_type.wiki` (revision 1376688119) and `sources/_cache/cpa/src/combinatorics/bracket_sequences.md`.

Sources: Wikipedia (CC BY-SA 4.0; figure files CC0 and CC BY-SA 4.0) and cp-algorithms (CC BY-SA 4.0). No translation. 4 blocks, 3 concepts, 3 Sims (all debuggers), 1 photograph, 0 derivations, 4 code exercises, 3 NC cards.

## Lead (draft, AI-marked, 75 words)

> An Essential section on the stack, the last-in, first-out collection, and on its classic first use: checking that a string's brackets balance. Indexing is 0-based: the array stack's top counts the items on it and names the next free cell. The array-backed stack is the ArrayStack of Section 2.2 in another notation; the linked-list stack pushes and pops at the head of the singly linked list of Section 2.5.

Tier: Essential, every concept (`stack`, `balanced-brackets`, `bracket-validation` are all `core`). Indexing: 0-based (reconciled table: "Wikipedia stack, top starts at 0"). Bridge **B12** (the ArrayStack sentence). One back-pointer, B-new-d, to 2.5's singly linked list (Questions 2). No tier exceptions.

## Sub-concept blocks (`<h2>`), in page order

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `stack` | Stacks (OmniStax: the article's lead has no heading); `<h3>` Non-essential operations (source) | wikipedia | `wikipedia:Stack_(abstract_data_type)` lead + #Non-essential operations | no | the lead's five paragraphs (push, pop, peek; LIFO with its note; top and bottom; bounded capacity and overflow) with Lifo stack.svg kept as `photo-lifo-stack`; peek as a non-essential operation, underflow, convenience operations |
| 2 | `stack-implementation` | Implementation (source; its parent heading "Software stacks" holds only a UML image and is dropped); `<h3>` Array, `<h3>` Linked list (source) | wikipedia | `wikipedia:Stack_(abstract_data_type)#Implementation` + ====Array==== + ====Linked list==== | no | the six pseudocode listings as `<pre>` (Wikipedia's words); `sim-array-stack` after the array pop listing (it folds the two array GIFs), `sim-linked-stack` after the linked-list pop listing (the two linked-list GIFs); the dynamic-array paragraph (amortised O(1)) |
| 3 | `balanced` | Balanced bracket sequences (source, cpa's level-1 title) | cpa | `cpa:combinatorics/bracket_sequences#balanced-bracket-sequences`, its definition, example and multiple-types sentence, to "…in a similar fashion."; the article's roadmap paragraph after it left out | no | the three-rule definition, (())() and ())( |
| 4 | `validation` | Balance validation (source) | cpa | `cpa:combinatorics/bracket_sequences#balance-validation` | no | the depth counter for one bracket type; the stack for several; `sim-brackets` after the last paragraph |

**Readers.** Wikipedia is read with `ch02/2.3/wikitext.py` (imported, unchanged: `lead`, `section`, `named_refs`, `inline_text`, `pre_text`); a section-local `build.py` adds what this article needs and that reader lacks (`*` list items, the list-defined `<ref group="nb" name=… />` note, case-insensitive `[[file:` frames, the `{{Introduction to Algorithms}}` citation template, stand-alone templates dropped and named). cpa is read with `tools/build_translation.py`'s Markdown parser and inline setter (as `tools/build_markdown.py` uses them). Both halves assembled block by block as 2.3's `build.py` does. Citations become book footnotes (2.1 and 2.3 do so; 2.5 drops them: chapter pass). Wikilinks print as their text, except where the book carries the target: *dynamic array* → Section 2.2, *singly linked list* / *linked list* → Section 2.5, *queue* → Section 3.2, *amortized* none in this passage.

## Concepts

| id | kind | tier | statement | introducing span | prereqs (the map's, Hasse-reduced) |
|---|---|---|---|---|---|
| `stack` | definition | Essential | A stack is a collection with two main operations, push (add an element) and pop (remove the most recently added one), so elements leave last in, first out; peek returns the top element without removing it. Both operations act at one end, the top; popping or peeking an empty stack is underflow, and pushing onto a full bounded stack is overflow. An array (top counting the items) or a singly linked list (top at the head) gives O(1) push and pop, a dynamic array amortized O(1). | `stack` | dynamic-array |
| `balanced-brackets` | definition | Essential | A balanced bracket sequence is a string of brackets defined by three rules: the empty string is balanced; if s is balanced, so is (s); if s and t are balanced, so is st. (())() is balanced, ())( is not. | `balanced` | none |
| `bracket-validation` | skill | Essential | With one bracket type, keep depth, the number of open brackets: add 1 at an opening bracket, subtract 1 at a closing one; the string is balanced exactly when depth never goes negative and ends at 0. With several types, push every opening bracket on a stack; at a closing bracket the stack must be non-empty with an opening bracket of the same type on top, which is popped; the string is balanced when every check passes and the stack ends empty. | `validation` | stack, balanced-brackets |

`terms`: stack / stacks / LIFO / last in, first out; balanced bracket sequence / balanced bracket sequences; balance validation. Types: none of the three is typed (`COLOR.md` §4: a data structure is no category; a bracket balance is a plain count, RULES Types "Untyped"). In the prose, `O(1)` is marked `data-type="cost"`; "size", "maxsize" as concepts? no concept names them: left in ink (the terms pass judges "size").

## Errata notes (correction footnotes, AI-marked)

None is listed for 3.1 in the reconciled file. One found while reading, added here:

- **err-top** (`stack-implementation`, Array): "a variable *top* that records the number of items pushed so far" is loose: each pop decrements top, so it counts the items on the stack now (pushed less popped), which is also where the next push writes. The marker stands after that sentence's "pushed so far". The figure's readout states top = number of items on the stack.

Checked and correct: the array pseudocode (top from 0, push writes then increments, pop decrements then reads; empty at top = 0, full at top = maxsize), the linked-list push and pop at the head, the amortised O(1) of the dynamic array (Section 2.2), cpa's three rules on its two examples, the depth counter and the typed stack against brute force (the judge's checks, rerun in this build on all strings over `()` up to length 10 and over `()[]{}` up to length 8).

## Derivation candidates (root item 29)

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| peek as pop followed by push | one sentence | 1 | 0 | not built |
| the depth counter's correctness | stated, not argued | 0 | 0 | not built |

None qualifies: no chain of equations is printed or skipped.

## Figures

```
sim-array-stack · Sim (originals: Wikipedia Stack Push operation-en.gif and Stack Pop Operation-en.gif, folded) · stack · flow by animation; variation by input (the bad cases overflow and underflow) · arrows: kinematic (top moves up and down the array; an item slides in or out) · moving: one stop per push or pop, one per line stepped into · headline: the call and what it does ("push(stk, 4): items[3] ← 4, top 3 → 4.") · graph none · 2D · code: an AI translation into Python, Java, C++ and JavaScript of Wikipedia's array pseudocode (structure, initialize, push, pop), Python canonical, about 22 lines; the pseudocode stays printed as `<pre>` above · blocks: init "make an empty stack of maxsize cells" lines 8–11 touches items, maxsize, top; push "push x" 13–18 ⟶ full "top = maxsize: overflow" 14–15 touches top ⟶ write "items[top] ← x, then top + 1" 17–18 touches items, top; pop "pop" 20–26 ⟶ empty "top = 0: underflow" 21–22 ⟶ read "top − 1, then r ← items[top]" 24–26 touches top, r · default level: one call (push or pop) per stop · invariant: items[0..top) are the stack, bottom at 0 (shaded in the index tint); cells at top and above hollow · readout (the watch) "top = 3 · maxsize = 5 · x = 4" · cost: cells written and read per call against 1 ("cells touched 1 per call, whatever top") · inputs: Wikipedia's GIFs (push from empty until overflow; pop from full until underflow) | push and pop interleaved | push onto a full stack (overflow, the bad case) | pop from an empty stack (underflow) · labels: top as a pointer under its cell in its referent colour; index labels under the cells in `index`; values in `key`; maxsize as a bracket in `size`
sim-linked-stack · Sim (originals: Wikipedia Linked-list-based Stack Push operation-en.gif and Linked-list-based Stack Pop Operation-en.gif, folded) · stack · flow by animation · arrows: kinematic (a new frame's next link aimed at the old head, head re-aimed) · moving: one stop per call, one per assignment stepped into · headline: the call and the link it changes · graph none · 2D · code: an AI translation of Wikipedia's linked-list pseudocode (frame, stack, initialize, push, pop) into the four languages, Python canonical · blocks: push "push x at the head" ⟶ make "newhead ← new frame holding x" touches newhead ⟶ link "newhead.next ← head" touches newhead ⟶ head "head ← newhead, size + 1" touches head; pop "pop the head" ⟶ empty "head = nil: underflow" ⟶ take "r ← head.data, head ← head.next, size − 1" touches head, r · default level: one call per stop · invariant: every frame on the stack is reached from head (solid); a popped frame fades to ink · readout "size = 3 · head → 7" · cost: links written per call against 2 ("links written 2, whatever the size") · inputs: Wikipedia's (push 4 values, then pop them all) | pop from an empty stack (underflow; no overflow is possible) | push and pop interleaved · labels: head and newhead as pointer boxes in their referent colours; values in `key`; hover names on links
sim-brackets · Sim (no source figure) · bracket-validation, balanced-brackets, stack · invariant made visible; variation by input · arrows: kinematic (an opening bracket pushed, a matched one popped; the read position advances) · moving: one character per step · headline: the character read and what it does to depth or the stack ("')' at 3: depth 1 → 0.") · graph: the depth line under the string (depth after each character, the 0 line drawn, the part below 0 in `PAL.bad`) · 2D · code: an AI translation of cpa's two procedures (cpa prints none) into the four languages, Python canonical, two functions in one panel (`balanced_one_type`, the depth counter; `balanced`, the stack), the input choice saying which runs · blocks: (counter) start "depth ← 0"; read "one character" ⟶ count "opening: depth + 1; closing: depth − 1" touches depth ⟶ check "depth < 0: not balanced" touches depth; end "depth = 0?" · (stack) start "an empty stack"; read "one character" ⟶ push "an opening bracket goes on the stack" touches stack ⟶ match "a closing bracket needs its opening one on top" touches stack ⟶ pop "remove it"; end "is the stack empty?" · default level: one character per stop · invariant: depth ≥ 0 at every prefix (the depth line above 0; the stack's height is the same line) · readout (watch) "depth = 1" or "stack = ( [" with "characters read 3 of n = 6" · cost: characters read against n · inputs: counter: (())() (cpa's balanced example) | ())( (cpa's unbalanced one: depth −1 at the third character) | (() (ends at depth 1) ; stack: ([]{}) | ([)] (the bad case for the counter: depth never negative and ends at 0, but the stack finds ) on [ ) | {[] (the stack is not empty at the end) · labels: the string's characters in `key`, positions under them in `index`, the read cursor as `i` (a referent); depth in ink (a plain count)
```

All three open on the source's own numbers where it has them (the GIFs' pushes to overflow and pops to underflow, cpa's two examples).

**Drawing.** Cells, frames and links with `F` primitives (`line`, `arrow`, `text`, a filled `rect` helper as 2.3 draws its cells), `F.ds.strip` / `F.ds.pointer` / `F.ds.region` for the array and the string. No new library primitive (2.5's `F.ds.nodes` is on an unmerged app branch).

**Source figures, keep or drop.**

| figure | where | decision |
|---|---|---|
| Tallrik - Ystad-2018.jpg (a stack of plates) | lead | **dropped**: decoration; the text names the analogy in words, and the page does not point at the photograph |
| Lifo stack.svg (CC0; "Simple representation of a stack runtime with push and pop operations") | lead | **kept** as `photo-lifo-stack`, its caption the article's, credit "Vectorization: Alhadis, CC0, via Wikimedia Commons": a still picture of the LIFO idea the lead defines; nothing in it moves that the two Sims below do not move better |
| Stack UML class diagram.svg | Software stacks | **dropped**: UML is not taught in this book; the interface it shows is in the text |
| Stack Push operation-en.gif, Stack Pop Operation-en.gif (CC BY-SA 4.0, Michel Bakni) | Array | folded into `sim-array-stack` (originals 1 and 2, their captions the row's `original_caption`) |
| Linked-list-based Stack Push operation-en.gif, … Pop … (CC BY-SA 4.0, Michel Bakni) | Linked list | folded into `sim-linked-stack` (originals 1 and 2) |

## Extra simulations (root item 15), none built

- `sim-stack-cost`: the same pushes on a bounded array, a dynamic array and a linked list, side by side, with the cost of each push: the dynamic array's occasional copy of every element against its amortised O(1), the list's constant two links. It would show the Implementation paragraph's comparison, which no required figure draws.

## Exercises (config.md, decision 19)

| concept | kind | item | answer shape | status |
|---|---|---|---|---|
| stack (+ singly-linked-list) | code | Exercism simple-linked-list (MIT): a LIFO linked list with push, pop, peek, count, toList and reverse | `code`, Python and JavaScript; the canonical cases (the 3 "toList FIFO" cases left out, as the Python track does: the list is LIFO) as `run(initial, operations)` calls on the reader's LinkedList, a given driver in the starter; pop or peek on an empty list raises `EmptyListException`; references: the Python track's `example.py` (source) with the driver, an AI JavaScript port | ships |
| stack | code | icc `stacks_queues/stack` (Apache-2.0): implement a stack with push, pop, peek and is_empty using a linked list | `code`; icc's 12 asserts as three operation lists played by a given `run(ops)`; references: icc's `stack.py` (source, run isolated first) and an AI JavaScript port | ships |
| bracket-validation | code | Exercism matching-brackets (MIT) | `code`, `is_paired(input_string)` / `isPaired`; the 20 canonical cases; Python reference the track's `example.py` (source), JavaScript AI; bound `n` with a nested-bracket `grow` | ships |
| bracket-validation | code | Kattis delimitersoup (CC BY-SA 3.0, IDI Open 2019, Jean Niklas L'orange) | `code`, a stdin program; the five samples visible-first, AI tests (a closing bracket with an empty stack, a mismatch at position 0, only openers, the 200-character bound, spaces), checked against a brute-force reading of the statement; AI references | ships |
| stack | check | OpenDSA stack MC questions | `choice` | waits for the OpenDSA converter; named in `exercise_notes` |
| stack, bracket-validation | NC | pythonds self-checks: `stack_1`, `stack_2` (multiple choice, keyed) and `stack_stringrev` (rev_string with its three `testEqual` tests) | `choice`, `choice`, `code` (AI reference, marked) | ships in `exercises-nc.json` |

`exercise_notes` also names: OpenDSA's push/pop proficiency exercises and Wikibooks' seven A-level stack traces (wait for `sequence`); ODS intro Exercise 1.2 (Dyck words) and 1.3 (unkeyed written); Kattis brackets and GCPC 2023 loopinvariant (not rated good), Kattis bracketmatching (samples only, not rated good), backspace and throwns (over the cap of two for `stack`); TheAlgorithms' stack and balanced-parentheses doctests (test sources without a printed statement); trekhleb's valid-parentheses tests (they read an empty string as unbalanced and a space as a wrong closer, against Exercism's statement); pythonds' end-of-chapter exercises 19 and 30 (unkeyed).

## Referents

| id | what | figures | blocks |
|---|---|---|---|
| `top` | top, the array stack's count of items, the next free cell | sim-array-stack | `stack-implementation` |
| `head` | head, the frame on top of the linked stack | sim-linked-stack | `stack-implementation` |
| `newhead` | newhead, the frame being pushed | sim-linked-stack | `stack-implementation` |
| `i` | the position of the character being read | sim-brackets | `validation` |

The prose marks *top* (`<em>top</em>` in the Array paragraphs) and `stk.head`'s "head" where the passage names the variable. `depth` is cpa's counter and a plain count (RULES Types: a bracket balance is untyped), drawn in ink; the stack in sim-brackets is the structure, in ink.

## References item (at most three)

None: the schema has no field for it yet (as 1.1–2.7).

## Attribution

- Wikipedia contributors, "Stack (abstract data type)" (revision 1376688119), CC BY-SA 4.0, adapted.
- cp-algorithms contributors, "Balanced bracket sequences" (`combinatorics/bracket_sequences`), CC BY-SA 4.0, adapted.
- Figures: Lifo stack.svg (vectorization: Alhadis, CC0); the four GIFs (Michel Bakni, CC BY-SA 4.0), in their originals' captions.
- Exercises: Exercism (MIT, the `exercism` source row's notice), Interactive Coding Challenges (Apache-2.0), Kattis delimitersoup (CC BY-SA 3.0), pythonds (CC BY-NC-SA 4.0, NC file).
- `notes`: "The stack article's history, hardware stacks, applications and security sections, its photograph of plates and its UML diagram are left out, as are the bracket article's counting and enumeration problems." `ai`, `built`.

## Questions (decided here; the brief says to choose and go on)

1. **Which Wikipedia reader.** The book has three: `tools/build_wikitext.py` (2.5; drops citations, reads only `group="note"`), `ch02/2.1/readers.py` and `ch02/2.3/wikitext.py` (both carry citations). *Decided: import 2.3's `wikitext.py` unchanged and add the four missing readings in a section-local `build.py`; the chapter pass picks one reader for `tools/`.*
2. **The linked-list stack and Section 2.5.** Wikipedia's linked-list stack is a singly linked list pushed and popped at its head. *Decided: a back-pointer in the lead (B-new-d), within 80 words.*
3. **cpa's roadmap paragraph** ("In this article we discuss … number of sequences, …"). It lists problems this page does not carry (they belong to chapter 34's combinatorics). *Decided: the block stops before it; the locator says so.*
4. **The bracket code.** cpa prints no code for validation; the judge names TheAlgorithms' `balanced_parentheses.py` (it needs its own Stack class and ignores other characters) and trekhleb's (a hash table, an empty string false). Neither is cpa's procedure. *Decided: an AI translation of cpa's two procedures, AI-marked in all four languages (as 1.5's panel, the by-design all-AI warning).*
5. **Wikipedia's pseudocode** stays as `<pre>` (its words); each Sim's panel is its four-language translation (2.5 Question 3).
6. **trekhleb's tests** for matching-brackets (config line 3.1) contradict Exercism's statement on the empty string and on spaces. *Decided: not used; named in `exercise_notes`.*
7. **pythonds self-checks.** config counts six for 3.1; the cached chapter has three in 3.1's pages (`stack_1`, `stack_2`, `stack_stringrev`); the parentheses pages hold only listings. *Decided: the three ship; the count is reported.*
