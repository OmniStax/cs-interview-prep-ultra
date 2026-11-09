# Plan: 2.5 Singly linked lists

Status: **plan, built from in the same run** (brief `briefs/section-build.md`: chapters 2 and 3 have no separate plan review), 2026-11-09. Read for this plan: the root and book rules, `COLOR.md`, `METHOD.md`, `ch02/config.md` and `exploration.md`, `judgements/ch01-03-reconciled.md` (item 5, the bridge table, erratum 18, "Rulings applied"), `judgements/ch02.md` §2.5, `judgements/ch01-03-references.md`, the concept rows, chapter 1's plans and built pages, and the cached wikitext `sources/_cache/wikipedia/Linked_list.wiki` (revision 1382386163) and `Pointer_computer_programming.wiki` (revision 1382564071).

Sources: Wikipedia only (CC BY-SA 4.0; the three figure files public domain). No translation. 4 blocks, 4 concepts, 2 Sims (both debuggers), 1 photograph, 0 derivations, 1 code exercise.

## Lead (draft, AI-marked, 66 words)

> An Essential section on the singly linked list: its nodes and links, the in-place operations at a node and at the front of the list, and where it beats or loses to a dynamic array. The passage on multiple indirection is C, in the pointer notation of Section 2.1. No node has an index here: a node is reached by following links from the first.

Tier: Essential, every concept (all four are `core`). Indexing: none, nodes and links (reconciled table). Bridges: **none assigned to 2.5.** The reconciled file (item 5 and the bridge table) puts the SLList name, with its fields head, tail and n, in **B10, the 2.6 lead**, and its use in chapter 3 in B11 (3.2); this section's Wikipedia passages never say "SLList", so the lead says nothing about it. One back-pointer is new (B-new-c, "in the pointer notation of Section 2.1"; see Questions).

## Sub-concept blocks (`<h2>`), in page order

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `singly-linked-list` | Linked lists (OmniStax: the article's lead has no heading); then the source's own `<h3>` "Basic concepts and nomenclature" and "Singly linked list" | wikipedia | `wikipedia:Linked_list` lead + #Basic concepts and nomenclature + ===Singly linked list=== | no | the lead's four paragraphs and its figure (kept as `photo-singly-linked-list`); node, next link, payload, head, tail, Lisp's car/cdr; the singly linked list; the C `addNodeToTail` listing as a four-language code set (C++ the source's C, verbatim, which compiles as C++; Python, Java and JavaScript AI). The same image printed again under ===Singly linked list=== is dropped (one image, shown once) |
| 2 | `pointer-to-pointer` | Multiple indirection (source) | wikipedia | `wikipedia:Pointer_(computer_programming)#Multiple indirection`, to the end of "…the address of the new item.", before the argv paragraph | no | the struct and `head` listing as a code set (C++ the source's, the other three AI); the sorted `insert(LinkedList **head, …)` listing becomes `sim-sorted-insert`'s code panel where it stands (C only, see Questions); erratum 18 |
| 3 | `list-operations` | Linked list operations (source); `<h3>` Singly linked lists (source); the empty ===Linearly linked lists=== heading dropped | wikipedia | `wikipedia:Linked_list#Linked list operations` intro + ====Singly linked lists==== | no | Node and List records, traversal, insertAfter, insertBeginning, removeAfter, removeBeginning as Wikipedia's pseudocode (`<pre>`, the source's words); `sim-list-ops` where the insert diagram stood (it folds both diagrams); the one-way limit, O(n) append without a tail, the dummy element |
| 4 | `lists-vs-arrays` | Linked lists vs. dynamic arrays (source) | wikipedia | `wikipedia:Linked_list#Linked lists vs. dynamic arrays`, without the `{{List data structure comparison}}` table (a template, not in the cache) | no | constant-time insertion at a known node, reallocation, random against sequential access, locality, storage overhead (its note on control data K + Bn as a book footnote), unrolled lists and CDR coding, the Josephus problem, list ranking, balanced trees |

**Wikitext.** Read by a new reader, `tools/read_wikitext.py` (wikitext is the third source format of the book after LaTeX and the PDFs; 2.1 and 2.3 need it too). Bold, italics, `<code>`, `<math>`, `{{IPA}}`, `<syntaxhighlight>` and the one-space-indented pseudocode are read as the article prints them. Citations (`<ref>` without `group="note"`) are not carried; a `group="note"` ref is the article's own explanatory note and becomes a book footnote. Wikilinks print as their text, except where the book carries the target (Questions): *dynamic array* → Section 2.2, *amortized* → Section 1.5, *array* (the article Array data structure) → Section 2.1, *stacks* → 3.1, *queues* → 3.2.

## Concepts

| id | kind | tier | statement | introducing span | prereqs (the map's, Hasse-reduced) |
|---|---|---|---|---|---|
| `singly-linked-list` | definition | Essential | A linked list is a sequence of nodes whose order is not given by their place in memory: each node holds its data and a link (the next pointer) to the next node; the head is the first node, the last node links to a terminator, and a singly linked list's nodes hold a value field and a next field. | `singly-linked-list` | none |
| `pointer-to-pointer` | skill | Essential | Pass a function the address of a pointer (double indirection, `LinkedList **`), so that it can change where the caller's pointer points: a list insert then updates the caller's head correctly, with no special case for inserting at the front. | `pointer-to-pointer` | none |
| `implement-linked-list` | skill | Essential | Change a singly linked list in place: traverse by following next links from firstNode; insert or remove after a given node by re-aiming its link, in constant time; insert or remove at the beginning by updating firstNode; inserting before a node, or appending without a reference to the tail, needs a traversal (O(n)); a dummy first node removes the special cases. | `list-operations` | singly-linked-list, pointer-to-pointer |
| `linked-list-vs-array` | result | Essential | A linked list inserts or deletes in constant time at a node already in hand (O(n) to find it) and grows without reallocation, but allows only sequential access, uses extra storage for links and has poorer locality of reference; a dynamic array gives constant-time random access and faster sequential access but moves elements to insert or delete in the middle. | `lists-vs-arrays` | dynamic-array (2.2), singly-linked-list |

`terms` per concept: singly linked list / linked list / node; pointer to a pointer / double indirection; (implement) none of its own words (its operations are named by the code); linked list versus dynamic array (no separate word). Types: none of the four is typed (a data structure is no category, `COLOR.md` §4); `cost` marks O(n), O(1), O(log n) as values (`data-type="cost"`) and `index` "a node reference" words where they name one in the prose (judged in the terms pass).

## Errata notes (correction footnotes, AI-marked)

- **18** (`pointer-to-pointer`): the listing's comment "insert the element item at the first location where all earlier elements have lesser or equal value" is loose: the loop stops at the first element whose value is not less than the item's, so every earlier element is strictly less and the item goes before any element equal to it. The code is a correct sorted insert. The comment stands in the code panel, which holds no marker (as erratum 6 in 1.1), so the marker stands after the sentence that introduces the listing ("…insertions at the front of the list:"). `sim-sorted-insert`'s "equal value" input shows it.

No other error found in the four passages (checked: the lead, the operations and their O(n) claims, the K + Bn note, the Josephus paragraph). `addNodeToTail` compiles and builds 0 1 4 9 16 (the judge's check); the `insert` listing gives 0 1 5 5 7 9 for 5, 1, 9, 5, 0, 7 (rechecked in this build).

## Derivation candidates (root item 29)

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| appending two lists of length n is O(n) | one sentence | 1 | 0 | not built |
| the K + Bn control-data note | a note, one formula, no chain | 0 | 0 | not built |

None qualifies: the four passages print no chain of equations.

## Figures

```
sim-list-ops · Sim (originals: Wikipedia CPT-LinkedLists-addingnode.svg and CPT-LinkedLists-deletingnode.svg, folded) · implement-linked-list, singly-linked-list · flow by animation; variation by input · arrows: kinematic (a link re-aimed from one node to another; the walk's node pointer) · moving: one assignment per step, a link swinging from its old target to its new · headline: the operation and what it changes ("insert_after: 37 goes in after 12; two links change.") · graph none · 2D · code: an AI translation of Wikipedia's four pseudocode functions (insertAfter, insertBeginning, removeAfter, removeBeginning, kept as printed in the text) into Python, Java, C++ and JavaScript, plus a five-line last_node walk for the append input; Python canonical, 23 lines · blocks: insert-after "insert after node" lines 1–3 ⟶ aim "new_node takes node's next" 2 touches new_node, node ⟶ relink "node points at new_node" 3 touches node; insert-beginning "insert at the front" 5–7 ⟶ aim 6 ⟶ head "first_node points at new_node" 7; remove-after "remove the node after node" 9–12 ⟶ mark "obsolete_node is node's next" 10 ⟶ bypass "node skips over it" 11 ⟶ free "destroy obsolete_node" 12; remove-beginning "remove the first node" 14–17 ⟶ mark 15 ⟶ head "first_node moves past it" 16 ⟶ free 17; last-node "walk to the last node" 19–23 ⟶ start 20 ⟶ hop "follow one link" 21–22 touches node · default level: the single assignments (at least three stops, every one changes a link or a pointer) · invariant: every node is reachable from first_node by following next links, until a removal fades the obsolete node to ink (COLOR.md: discarded is faded to ink); the reachable chain drawn solid, a node no link reaches drawn dashed · readout (the watch) "node = 12 · new_node = 37" with "links written 2 · links followed 0 (constant time)" · cost: links followed against n − 1 and links written against 2 · inputs: insert after 12 (Wikipedia's 12 → 99 with 37, the adding diagram) | insert at the beginning | remove after 12 (Wikipedia's 12 → 99 → 37, the deleting diagram) | remove the first node | remove the only node (firstNode becomes null, as the text notices) | append 37 with no tail reference (the bad case: the walk follows n − 1 links before one constant-time insert) · labels: values in the nodes, the pointer variables at their nodes in their referent colours, first_node at the List record; hover names on nodes and links
sim-sorted-insert · Sim (replaces the listing only; Wikipedia prints no figure for it) · pointer-to-pointer · flow by animation; variation by input · arrows: kinematic (p moving from one link field to the next; the two links re-aimed by the splice) · moving: one loop iteration per step · headline "p points at a link, not a node: the caller's head is just the first link." · graph none · 2D · code: wikipedia:Pointer_(computer_programming)#Multiple indirection, `insert` and its call, C, verbatim (lines 1–14, comments included) · blocks: start "p points at the caller's head" line 5 touches p, head; walk "move p to the next link while its node is smaller" lines 6–8 touches p ⟶ (one instance per iteration); splice "link item in where *p pointed" lines 9–10 ⟶ aim "item takes *p's node" 9 touches item ⟶ set "*p now points at item" 10 touches p, head · default level: start, each walk iteration, aim, set · invariant: every node before *p holds a value less than item's (shaded in the index tint) · readout "*p → 7 · item → 6 · links followed 2 ≤ n = 4" · cost: links followed against n · inputs: 6 into 1 → 5 → 7 → 9 (middle) | 0 (smaller than the head: the caller's head changes, through the same line) | 10 (past the end: the walk crosses every node, the bad case) | 5, equal to a value present (it goes in before the equal element: erratum 18) · labels: head, p and item at their marks, values in nodes; hover names on link fields
```

Both open on the source's numbers: `sim-list-ops` on Wikipedia's diagrams (12, 99, 37), `sim-sorted-insert` on the judge's checked sequence (the list 1, 5, 7, 9 is a prefix of its result 0 1 5 5 7 9 without the repeats).

**Drawing primitives.** Both draw with new `F.ds.nodes` and `F.ds.links` (a node as a value cell beside a next cell, a link as an arrow from the next cell's dot to the node it names or to a terminator, curving over the nodes it bypasses; a pointer variable as a one-cell box), added to `omnistax-web/src/lib/fig/dsa.ts` backward-compatibly, with tests, on an app branch (`claude/app-fixes-2.5`); the decision is the brief's. `F.ds.nodePointer` labels a node with a pointer variable, as `F.ds.pointer` does a strip cell.

**Source figures, keep or drop.**

| figure | where | decision |
|---|---|---|
| Singly-linked-list.svg (lead frame, caption "A linked list is a sequence of nodes…") | `singly-linked-list` | **kept** as `photo-singly-linked-list`, the lead's caption, credit "Lasindi, public domain, via Wikimedia Commons": a still picture of the structure the text defines, which nothing moves in (root item 14: a sketch stays as drawn where motion adds nothing) |
| Singly-linked-list.svg again (===Singly linked list===, caption "A singly linked list whose nodes contain two fields…") | `singly-linked-list` | **dropped**: the same image, one block apart |
| CPT-LinkedLists-addingnode.svg | `list-operations` | replaced by `sim-list-ops` (original 1, its caption the row's `original_caption`) |
| CPT-LinkedLists-deletingnode.svg | `list-operations` | folded into `sim-list-ops` (original 2); the text's "The diagram demonstrates the former" reads against the Sim above it |

## Extra simulations (root item 15), none built

- `sim-access-cost`: the same n values in an array strip and a linked list, a slider for the position asked for: the array reads it in one step, the list follows k links; and a locality strip showing the list's nodes scattered over memory. It would show the vs-arrays passage's random-against-sequential claim, which no required figure draws.
- `sim-josephus`: the circle of the Josephus paragraph, run with a circular list (cheap removal, a walk to find the next) and with an array (cheap find, a shift to remove), the two counters side by side.

## Exercises (config.md, decision 19)

| concept | kind | item | answer shape | status |
|---|---|---|---|---|
| singly-linked-list, implement-linked-list | code | icc `linked_lists/linked_list` (Apache-2.0): implement insert_to_front, append, find, delete and length on a head-only singly linked list | `code`, Python (the source's notebook skeleton as starter; a given `run(ops)` driver) and JavaScript (AI starter and reference); the tests are icc's 16 asserts, each test case of `test_linked_list.py` as one operation list; references: icc's own `linked_list.py` (source) and an AI JavaScript port | ships |
| linked-list-vs-array | check | opendsa ListOverhead (parameterised, one instance) | `choice` | waits for the OpenDSA converter; named in `exercise_notes` |

`exercise_notes` also names: Exercism simple-linked-list (a linked stack, held for 3.1) and MIT 6.006 ps1 1-4 (doubly linked, 2.6); ODS Exercises 3.2–3.4 and CIU's "implement a linked list" checklist (statements without source tests); Kattis joinstrings and sim (samples only); keon, TheAlgorithms and trekhleb linked-list files (test sources with no printed statement, among them merge_two_lists, which 2.3's ranking passed here); OpenDSA's two linked-list proficiency exercises (wait for `sequence`). pointer-to-pointer has no exercise (none found).

## Referents

| id | what | figures | blocks |
|---|---|---|---|
| `node` | node, the node the operation works after (the walk's cursor in last_node) | sim-list-ops | `list-operations` |
| `new-node` | new_node, the node being inserted | sim-list-ops | `list-operations` |
| `obsolete-node` | obsolete_node, the node being removed | sim-list-ops | `list-operations` |
| `p` | p, the pointer to a link field | sim-sorted-insert | `pointer-to-pointer` |
| `item` | item, the element being inserted | sim-sorted-insert | `pointer-to-pointer` |
| `head` | head, the caller's pointer to the first element | sim-sorted-insert | `pointer-to-pointer` |

`first_node` (the List record's field, `list.firstNode`) is an attribute, not a variable the code names bare, so it is drawn in the `index` colour, as "the head" is in `COLOR.md`. Node values wear `key`; the counters `cost`; n `size`.

## References item (at most three)

None: the schema has no field for it yet (as 1.1–1.6).

## Attribution

- Wikipedia contributors, "Linked list" (revision 1382386163) and "Pointer (computer programming)" (revision 1382564071), CC BY-SA 4.0, adapted.
- Figures: Singly-linked-list.svg (Lasindi), CPT-LinkedLists-addingnode.svg and CPT-LinkedLists-deletingnode.svg, Wikimedia Commons, public domain (dossiers/ch02.md).
- Exercise: Donne Martin, Interactive Coding Challenges, Apache-2.0 (the `icc` exercise source row carries its notice).
- `notes`: "Wikipedia's comparison table of list structures, its citations and the argv example of multiple indirection are left out." `ai`, `built`.

## Questions (decided here; the brief says to choose and go on)

1. **C listings under the C++ button.** Wikipedia prints C (`addNodeToTail`, the struct, `insert`). C is none of decision 20's four languages, but each listing compiles unchanged as C++ (checked with g++). *Decided: the C stands verbatim as the C++ variant, unmarked (it is the source's code); Python, Java and JavaScript are AI translations.*
2. **The double-indirection insert in Python, Java and JavaScript.** None of them can take the address of a variable, so a translation would replace the technique by another (a dummy node, a returned head). *Decided: `sim-sorted-insert`'s panel is C only, the one language that can show it; the struct listing before it still gets all four.* (Root item 19 allows a set without Python where `data-no-python` says why; the panel needs no attribute.)
3. **Wikipedia's pseudocode.** The six operation listings are Wikipedia's words and stay as `<pre>`; `sim-list-ops`'s panel is their four-language translation (1.1's FibonacciMultiply precedent). The records and the traversal stay pseudocode only: they declare fields and sketch a loop with "(do something with node.data)", and are no program. *Decided so.*
4. **Wikilinks.** Print as text; link to this book's section only where the book carries the article's subject (2.1, 2.2, 1.5, 3.1, 3.2). *Decided so; the chapter pass should make 2.1 and 2.3 agree.*
5. **The argv paragraph** of Multiple indirection (strings, not lists; the judge left it to the builder). *Decided: left out, the locator saying so.*
6. **B-new-c.** The pointer-to-pointer passage leans on C's `*`, `&` and `->`, taught with Wikipedia's C arrays in 2.1. *Decided: a back-pointer in the lead ("in the pointer notation of Section 2.1"), within 80 words.*
7. **The comparison table** `{{List data structure comparison}}` is a transcluded template, not in the cache. *Decided: left out; `notes` says so.*
