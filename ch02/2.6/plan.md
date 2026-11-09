# Plan: 2.6 Doubly linked lists

Status: **plan, built from in the same run** (`briefs/section-build.md`: no separate review for chapters 2 and 3), 2026-11-09. Read for it: root and book `RULES.md`, `COLOR.md`, METHOD §1–§3, §5 and decisions 1–21, `LOG.md` passes 1–8, `ch02/config.md`, `ch02/exploration.md`, `judgements/ch01-03-reconciled.md` (item 5, the bridge table, the indexing table, the rulings), `judgements/ch02.md` §2.6, `judgements/ch01-03-references.md` (ODS notes), `concept-map/concepts.json` rows `sentinel-node` and `doubly-linked-list`, `ch01/plans-summary.md` and 1.3's plan, spec and figures; and from the source cache `ods/latex/linkedlists.tex` lines 107–239, `ods/latex/snarf-python.py`, `snarf-java.pl`, `snarf-cpp.pl`, `ods/python/ods/dllist.py`, `ods/java/ods/DLList.java`, `ods/cpp/DLList.h`, `ods/latex/figs/dllist2.ipe` and `dllist-addbefore.ipe`, and MIT 6.006 S20 ps1 (questions, template).

One source, ODS (CC BY 2.5 Canada), pseudocode edition (decision 20). No translation. 2 blocks, 2 concepts, 2 Sims (one still, one debugger), 6 four-language code sets, 0 derivations, 0 errata, 1 NC card.

## Lead (AI-marked, 62 words)

> An Essential section on the <span data-concept="doubly-linked-list">doubly linked list</span> and the <span data-concept="sentinel-node">dummy node</span> that spares it special cases at either end. ODS calls the singly linked list of Section 2.5 an SLList, with fields head, tail and n. Its DLList numbers the list's elements from 0 to n − 1, the index i that getNode(i) finds.

Tier: Essential (both concepts `core`). Indexing: 0-based (reconciled table: ODS get(i), O(1 + min{i, n − i})). Bridges: **B10** (the SLList name and its fields), the one the brief calls B-SLList; **B17 is dropped** (Questions 1). No concept of another tier.

## Sub-concept blocks (`<h2>`)

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `dummy-node` | DLList: A Doubly-Linked List (source) | ods | `ods:linkedlists#sec:dllist`, opening through fig. dllist and the DLList() code (`linkedlists.tex` 109–146) | no | the DLList named against the SLList; the special cases; the dummy node and the cycle; Figure 3.2 (→ `sim-dllist-ring`); `\codeimport{DLList.n.dummy.DLList()}` → a code set |
| 2 | `dllist` | Operations on a DLList (OmniStax header, naming the concept's operations) | ods | `ods:linkedlists#sec:dllist` from getNode(i) through "Adding and Removing" and "Summary" (`linkedlists.tex` 148–238) | no | getNode and its O(1 + min{i, n − i}); get/set; "Adding and Removing" as `<h3>` (addBefore → `sim-dllist`, whose panel is the listing; Figure 3.3 → the same Sim; add(i,x), remove(w), remove(i) as code sets); "Summary" as `<h3>` with the theorem as a note and its three paragraphs; `\chapref{arrays}` → "Section 2.2"; the `\javaonly`/`\cpponly` examples are printed by neither edition the book reads, so the last paragraph ends at "through external means." |

Code listings (decision 20): every `\codeimport` is a code set in four languages. Java and C++ are ODS's own, read from `java/ods/DLList.java` and `cpp/DLList.h` by script with the rules ODS's own extractors apply when they print them (`snarf-java.pl`: modifiers dropped, the `IndexOutOfBoundsException` lines dropped; `snarf-cpp.pl`: `typename`, `virtual`, template lines dropped). Python is ODS's own `python/ods/dllist.py`, the methods its pseudocode extractor picks (`snarf-python.py`: `DLList.n.dummy.DLList()` prints `_initialize`), unchanged except one port: `get_node`'s `self.n/2` is `self.n//2`, the integer division the Python 2 source meant and the Java and C++ do, so the Python listing of getNode carries the AI mark (decision 20: "a Python port, AI-marked where changed"; brief). JavaScript is an AI translation of the Java, marked.

## Concepts

| id | kind | tier | statement | introducing span |
|---|---|---|---|---|
| `sentinel-node` | skill | Essential | A DLList keeps a dummy node that holds no data and stands after the last node and before the first, so the nodes form a cycle, every node has a next and a prev, and adding or removing needs no special case for an empty list or for either end. | `dummy-node`, "introduce a dummy node" |
| `doubly-linked-list` | definition | Essential | A linked list whose nodes point both to the node that follows and to the node that precedes them; with a dummy node it reaches the ith node from the nearer end in O(1 + min{i, n − i}) time, and adds or removes a node it holds a reference to in constant time. | `dllist` (the block of its operations; the opening sentence of `dummy-node`, "A DLList (doubly-linked list)", is a `uses` mention, as 1.5's aggregate method was settled in plans-summary question 26) |

Edges (Hasse-reduced, from the map): `sentinel-node → singly-linked-list` (2.5), `doubly-linked-list → list-interface` (2.1), `doubly-linked-list → sentinel-node`. Coverage: `dummy-node` introduces sentinel-node and uses doubly-linked-list; `dllist` introduces doubly-linked-list and uses sentinel-node and big-o (1.3).

## Errata

None. Read against the code: getNode's walk from either end lands on node i (checked for every n ≤ 7 and i by the figure's trace against ODS's Python); addBefore's four assignments, remove(w)'s two and the theorem agree with the listings. The judge's check (n = 5, i = 3) agrees.

## Derivation candidates

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| getNode reaches the ith node in O(1 + min{i, n − i}) | prose, one sentence | 1 (i steps forward or n − i back, the smaller chosen) | 0 + 1 + 0 = 1 | not built; `sim-dllist`'s counter shows it live |
| add(i,x) and remove(i) cost O(1 + min{i, n − i}) | prose | 1 (getNode plus a constant) | 0 | not built |

## Figures

```
sim-dllist-ring · Sim (original: ODS Figure 3.2, "A DLList containing a,b,c,d,e.", behind the toggle) · sentinel-node, doubly-linked-list · variation by slider (the empty list, the case the dummy exists for, is one slide away) · arrows: symbolic (next and prev references) · still: a structure, not a procedure (code: none, a property: Figures, "the list interface" kind of exception) · slider n (size, 0..6, default 5, the book's a–e; dashed circle at n = 0) · headline "With n = 5, the dummy follows e and precedes a: every node has a next and a prev." / at n = 0 "With no elements the dummy's next and prev are the dummy itself." · graph none · readout "dummy.next = a" \\ "dummy.prev = e" (or "= dummy") · labels: values in the nodes (key), indices 0..n − 1 under them (index), "dummy" on its node (referent); hover names on links · 2D
sim-dllist · Sim (original: ODS Figure 3.3, "Adding the node u before the node w in a DLList.", behind the toggle; stands where the addBefore listing and Figure 3.3 stood) · doubly-linked-list, sentinel-node · flow by animation; variation by input · arrows: kinematic (p walking node to node; each reference re-aimed from its old node to its new one) · moving: one block per step, a link swinging, nodes easing into or out of the row · choice: operation (add(i, x) | remove(i)); sliders n (size, 0..6, default 5) and i (index, 0..n for add, 0..n − 1 for remove, default 2; dashed circles at 0, at the end, and at ⌊n/2⌋, the slowest find) · headline per stop, e.g. "getNode(2): i = 2 is not below n/2, so p starts at the dummy and walks back." · graph none · 2D
  code: ods:linkedlists#sec:dllist getNode(i), addBefore(w,x), remove(w); Python canonical (ODS's python/ods/dllist.py get_node, add_before, _remove; get_node ported, AI-marked), Java and C++ ODS's own, JavaScript AI; 24 Python lines
  blocks: find "find node i" 1–10 touches p, i
            fwd "walk forward from dummy.next" 3–5 touches p ⟶ hop "one step forward" 5 touches p
            back "walk back from the dummy" 7–9 touches p ⟶ hopb "one step back" 9 touches p
          link "link u in before w" 12–19 touches u, w
            make "make u and point it at w.prev and w" 13–15 touches u
            splice "point both neighbours at u" 16–17 touches u, w
          unlink "unlink w: its neighbours skip over it" 21–24 touches w
            skipn "w.prev skips forward to w.next" 22 touches w
            skipp "w.next skips back to w.prev" 23 touches w
  default level: the coarsest with three stops (find, then link or unlink); step into opens the walk and the assignments
  invariant: the nodes p has passed, shaded in the index tint, readout "p is node 2, 3 steps back from the dummy"; at rest every node's next.prev is itself
  readout (the watch) i, n, steps; on the canvas "steps 3 ≤ 1 + min(i, n − i) = 3"
  cost: links followed by getNode against 1 + min(i, n − i)
  inputs: add in the middle (the default, a–e, add(2, x)); add(0, x) and add(n, x), the two ends the SLList treats specially (add(n, x) finds the dummy itself); add(0, x) on the empty list; remove(0), remove(n − 1), remove of the only node; i = ⌊n/2⌋ is the bad case, the longest walk
  labels: values in nodes, indices under them, dummy, p, w, u at their nodes in referent colours; the link the step changed drawn heavier; hover names on links
```

**Source figures, keep or drop.** ODS Figure 3.2 (`figs/dllist2`) → `sim-dllist-ring`; ODS Figure 3.3 (`figs/dllist-addbefore`) → `sim-dllist`. Both rendered from ODS's `.ipe` (`render_originals.py`, Ipe's own `iperender`) to `media/ch02/ods-dllist.png` and `ods-dllist-addbefore.png`, the originals behind the toggles. ODS's printed numbers stay in the prose as links to the Sims (RULES, Cross-references).

**Drawing.** No `F.ds.nodes`/`links` exist in the app this book is served from. The 2.5 plan adds them on an app branch (`claude/app-fixes-2.5`), not merged where the dev servers run; 2.6 draws its three-cell nodes ([prev | x | next], as ODS draws them) and curved references with the library's own primitives (`text`, `line`, `arrow`) and canvas paths, in `figures.js`. The chapter pass can move both sections onto `F.ds.nodes`/`links` once merged.

## Extra simulations

None. (A getNode-only cost plot of steps against i for fixed n would repeat the debugger's counter.)

## Exercises

| concept | kind | item | answer shape | status |
|---|---|---|---|---|
| doubly-linked-list | check | OpenDSA ListTFdblimpl | `choice` | waits for the converter of OpenDSA's Khan-format exercises |
| doubly-linked-list | NC card | MIT 6.006 S20 ps1 1-4 "Doubly Linked List" | `open`, keyed by a link to MIT's worked solution | `exercises-nc.json` |
| sentinel-node | exercise | ODS Exercise 3.1 | — | unkeyed: left out |
| doubly-linked-list | code | ODS Exercises 3.5–3.12 | — | no source tests: left out (config) |
| doubly-linked-list | code | Exercism linked-list | — | held for 3.3 (a deque) |

The MIT card's statement is read from the handout's text by script (`build_nc.py`), with the four code names whose underscores pdftotext loses set from the page render. Its template's `tests.py` tests a class, which the `code` answer type (a function entry with args) does not express, so the card is written and keyed only, as config's NC rule says.

## Referents

| id | what | figures | blocks |
|---|---|---|---|
| `dummy` | the dummy node | sim-dllist-ring, sim-dllist | `dummy-node`, `dllist` |
| `p` | getNode's walking reference | sim-dllist | `dllist` |
| `w` | the node to insert before, or to remove | sim-dllist | `dllist` |
| `u` | the new node | sim-dllist | `dllist` |

`i` is the index asked for: a named code variable, but drawn as the position labels already in `index` colour; it is a referent too (`i`, sim-dllist), so its token in the code and its marker are one colour. Values (a–e, x) wear `key`, n `size`, the step count `cost`, node positions and references `index`.

## References item

None: the schema has no field for it yet (1.4's deviation).

## Attribution

- Pat Morin, *Open Data Structures*, https://github.com/patmorin/ods, CC BY 2.5 Canada, adapted (both blocks, the Java and C++ listings, the Python listings, Figures 3.2 and 3.3).
- MIT OpenCourseWare 6.006 Spring 2020, Problem Set 1, CC BY-NC-SA 4.0, in `exercises-nc.json` only.
- `notes`: the Java and C++ editions' closing examples (Java's LinkedHashSet, C++'s USet) and ODS's exercises without published answers are left out. `ai`, `built`.

## Questions (decided here)

1. **B17.** The reconciled table puts "DLList's Summary names Deque operations (3.3)" in this lead. The pseudocode edition's Summary names the List interface, the array-based Lists of Chapter 2 and (in the Java and C++ editions only) a hash table; no Deque. *Decided: B17 is not written; the chapter pass should strike it.*
2. **Block 2's header.** ODS's own headings inside the section are "Adding and Removing" and "Summary"; nothing names the getNode part. *Decided: an OmniStax `<h2>` "Operations on a DLList", ODS's two subsections as `<h3>`.*
3. **The listings beside the debugger.** The addBefore listing is the panel of `sim-dllist` (plans-summary question 17); getNode and remove(w), printed earlier and later, stay as code sets where ODS prints them, since the prose around each reads them there, so they appear twice on the page. *Decided: keep both.*
4. **doubly-linked-list's introducing span.** At block `dllist`, the concept's home, with the opening "A DLList (doubly-linked list)" a mention (plans-summary question 26's rule).
5. **The NC card's tests.** Kept as an `open` card with MIT's key; its class-based tests wait for a `code` answer type that tests a class.
