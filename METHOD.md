# Method proposal: one OmniBook from three CS sources

Status: draft for iteration, 2026-11-08. Nothing has been built. This file
comes before the book's `RULES.md` and `COLOR.md`, which the full-book pass
(root rule 18) writes once we agree on what is below.

Every OmniStax book so far is one open textbook, transformed with its words
kept. This one is different in three ways, and each section below follows
from them:

1. **Several sources, overlapping.** BFS is taught by Coding Interview
   University's links, by cp-algorithms, and by any textbook we bring in.
   "Keep the book's words" has to become "keep each source's words, block by
   block, and say which source each block came from".
2. **The subject runs.** An algorithm is a procedure with a state that
   changes over time. A physics figure has to simulate its world. A DSA figure
   can run the actual code. So the figure, the code and the exercise should be
   one object.
3. **Each source is a different kind of material.** CIU is a syllabus of
   links, cp-algorithms is a set of articles, and the Alex Xu book is a
   copyrighted commercial book (see §0).

---

## 0. Licences first, because one source can't be used

| Source | What it is | Licence | Usable? |
|---|---|---|---|
| jwasham/coding-interview-university | A study plan: topic checklist in interview order, each topic a list of links (mostly YouTube, Coursera, blogs) | CC BY-SA 4.0 (LICENSE.txt) | Yes, but there is little prose to keep. Its value is the **order** and the **link lists**. The linked videos are other people's work and can only be linked. |
| cp-algorithms/cp-algorithms | ~163 Markdown articles under `src/`, 10 categories (Graphs 47, Algebra 29, Geometry 26, Misc 13, Strings 12, Data Structures 10, Combinatorics 10, DP 7, Numerical 5, Linear Algebra 4), C++ code, practice-problem links at the end | CC BY-SA 4.0 (LICENSE) | Yes, fully. This is the only source of real prose among the three. |
| *System Design Interview* by Alex Xu (PDF in aasthas2022/SDE-Interview-and-Prep-Roadmap) | A commercial book (Byte Code LLC / ByteByteGo) | All rights reserved. The hosting repo has no LICENSE and says nothing about permission. | **No.** The PDF there is almost certainly an unauthorised copy. Transforming it and publishing to omnistax.org would distribute a copyrighted book. We shouldn't even use it as a private working source in this repo. |

**What replaces Alex Xu (decided: primer only).** donnemartin/system-design-primer
(CC BY 4.0) is the system design source, and no system design prose is
AI-written. It has the same arc as Xu's chapter 1 (scaling from one server to
millions of users: DNS, CDN, load balancers, reverse proxies, application
layer, SQL vs NoSQL, caching, async and queues, communication, security,
back-of-envelope numbers). It also has worked designs: Pastebin/bit.ly,
Twitter timeline, web crawler, key-value cache, social graph, sales rank,
scaling on AWS. Topics the primer lacks (rate limiting, consistent hashing in
depth, unique IDs) go to the resource finder (§6) like any other gap. If
nothing open is good enough, the topic stays out.

**The DSA basics have the same gap.** CIU is links, and cp-algorithms is
advanced (it barely explains a linked list or a hash table). The core topics
need an open textbook. Candidates, licences to confirm in exploration:

- *Open Data Structures*, Pat Morin (CC BY): arrays, lists, hash tables,
  BSTs, heaps, sorting, graphs. It has exercises, unkeyed.
- *Algorithms*, Jeff Erickson (CC BY 4.0): recursion, backtracking, DP,
  greedy, graph algorithms, written for intuition. It has hundreds of
  exercises, mostly unkeyed.
- Wikipedia (CC BY-SA) as the fallback for small gaps (endianness, Unicode).

**Combined licence:** CC BY-SA 4.0 for the whole book. BY content can be
adapted into a BY-SA work, and BY-SA from CIU and cp-algorithms requires
it. Every block names its source in the footer attribution.

**Exercises can't be copied from the practice links.** LeetCode, Codeforces
and SPOJ statements are copyrighted, so they stay links. **Decided:** no
AI-written code exercises in the book (those belong to the app's Exercises
tab). Code exercises are pulled from open sources first (§6.3). Erickson's
and ODS's printed exercises are unkeyed, so they need rule 13's choice.

**Decided: CC BY-SA 4.0 for everything except NC exercise cards.**
CC BY-SA and CC BY-NC-SA conflict on commercial use: one requires an
adaptation to allow it, the other to forbid it. So the two never mix in one
unit. The rules:

- **Prose, figures and OmniStax's own additions are CC BY-SA 4.0.** That
  covers figures, block labels, bridging sentences, the concept map, and
  AI-written tests for BY-SA exercises. NC prose (MIT OCW notes,
  transcripts) is link-only. The judge never weighs licence boundaries.
- **NC material is allowed only as exercise cards** (MIT OCW problem sets
  with their solutions, Project Euler). A card is a self-contained item
  with its own licence line, and the book is a collection of units. AI
  tests and hints written for an NC card are adaptations of it, so they
  are CC BY-NC-SA too.
- **The separation is mechanical:**
  - NC cards live in their own file per section, `exercises-nc.json`.
  - The content check refuses an NC locator anywhere else.
  - The build can drop those files to give a clean BY-SA export for
    commercial reuse.
- **NC sources are tagged by licence.** Each NC row in `exercise_sources`
  carries `license` and `license_url`, as Modern AMO II already does for
  MIT 8.422.
- **Attribution goes per block in each section's footer:** author, title,
  URL, licence, "adapted". MIT-licensed code keeps its MIT notice.

---

## 1. Tools to unlock

What the platform has today: exercise answers of types `number`, `multi`,
`choice` and `open`; the figlib drawing layer; derivations; Pyodide already
loaded in a worker for the CAS (`src/lib/cas/worker.ts`); CodeMirror already
in the notes editor. So a code runner costs little. These are the additions,
in priority order.

### 1.1 The trace engine (the foundation for everything else)

One mechanism that turns "run this algorithm on this input" into a list of
states: `trace = [{line, vars, event}]`. Events are things like
`compare(i,j)`, `swap(i,j)`, `push(v)`, `visit(u)` and `relax(u,v)`.

- In **figures**, the figure's own JS implementation emits the events,
  each tagged with the line number of the code shown on the page. Figures
  stay deterministic and fast, and work offline before Pyodide loads.
- In **exercises**, the reader's Python runs in Pyodide under
  `sys.settrace`, which records the same `{line, vars}` states. So the
  reader's own code can drive the same figure. "Run my solution and watch
  it" is the moment where the exercise and the figure become one object.
- A trace is a pure array, so the transport (play, scrub, step dots)
  reaches exact states in both directions, as manim-style item 6 already
  requires of derivations.

### 1.2 A `code` answer type, checked against tests

```
{ type: "code", lang: "python", signature: "def search(a: list[int], x: int) -> int",
  starter, tests: [{args, expect, visible}], reference, bound?: "n log n",
  hint?, solution?, generated_by }
```

- **Visible tests** run on "Run", **hidden tests** on "Submit". Passing
  every hidden test is the correct evidence of rule 20. Partial passes give
  no evidence. They show which test failed and on what input.
- **Complexity check, deterministic.** Timing in a browser is noisy, so
  count executed lines instead: `sys.settrace` line events on inputs of
  size n, 2n, 4n, 8n, then fit the exponent. The verdict reads like *"Correct.
  Your solution makes ~n² steps; this problem wants n log n."* This catches
  the most common interview failure, the correct but too-slow answer, with
  no AI grader. One caveat: builtins (`sorted`, `in` on a list) count as a
  single line. The check can patch the few that matter (`list.__contains__`,
  `list.index`, `list.insert`) to count their real cost.
- **The key is the reference solution.** Before a code exercise ships, the
  build runs `reference` against every test and the complexity check.
  That's the deterministic check root rule 13 asks of an AI solution.
- **Language.** See §1.5.

### 1.3 Checkable answer types that cost no code

- **`sequence`**: an exact ordered answer, such as a BFS visit order, the
  array after the second pass of insertion sort, or the order of pops from
  a heap. The reader types it or clicks it out on a figure.
- **`pick`**: click the thing on a figure in a given state, such as the
  next node Dijkstra settles, the bucket key 17 lands in, the bottleneck in
  an architecture. The answer is an id in the figure's scene, checked
  exactly.
- **`parsons`**: drag shuffled lines of a correct solution into order,
  indentation included. It is well studied for novice programmers and
  tests Understand without the friction of typing. The answer is the
  permutation.
- **`estimate`**: a `number` checked in log space, "within a factor of 2"
  (or 10), for back-of-envelope system design questions ("how many TB a
  year?"). The existing `tol` is relative and can't express this.
- **`rubric`** (system design): an `open` answer with a checklist the
  reader ticks against their own design ("named the read/write ratio",
  "put a cache in front of the hot reads", "said what happens when a shard
  dies"). It is self-graded like `open` and gives no evidence until we have
  AI grading (README roadmap item 4).

### 1.4 New figlib primitives

DSA: `strip` (array cells with indices), `pointer` (a labelled arrow under
a cell, coloured as its referent), `region` (a shaded span between two
pointers: the invariant), `nodes`/`links` (linked list), `tree` (tidy
layout, Reingold–Tilford, stable under insert so nodes don't jump),
`graph` (fixed coordinates from the source, never force-directed at
runtime, because a layout that moves while you read it is extraneous
load), `grid` (DP table with dependency arrows), `stack`/`queue`/`heap`
(the heap shown as tree and array together), `buckets` (hash table),
`bits`, and a `code` panel with the current line marked.

### 1.5 Which languages run, and why C++ costs more

The runner is one interface, `load() · run(code, tests) · count(code, sizes) ·
trace(code, input)`, with one adapter per language. The adapters differ in
download size and in whether `count` and `trace` can be built at all, and
`trace` is what drives the figures:

| | Python (Pyodide) | JavaScript | C++ (clang in wasm) |
|---|---|---|---|
| Download | ~10 MB, already cached by the calculator | 0, the browser runs it | 30–60 MB toolchain plus libc++ headers |
| Time to first run | ~2 s cold, then instant | instant | several seconds to compile each submission |
| Step count (§1.2) | `sys.settrace` line events | AST rewrite (acorn): a counter at every statement and loop head | no hook; would need coverage instrumentation in a wasm clang. Falls back to timing, which is fairly stable in wasm since it runs near native speed |
| Variable trace (§1.1) | `sys.settrace` gives the frame's locals | the same AST rewrite snapshots locals | needs a debugger over wasm; not practical now |
| Interview fit | most common interview language | common, but the standard library has no heap, deque, or ordered map | standard for contests |
| Integers | arbitrary precision | 2⁵³ doubles: `a*b % (1e9+7)` with a, b near 10⁹ comes out **wrong** unless written with BigInt | 64-bit, as cp-algorithms assumes |

So C++ is heavier for three reasons. It is compiled, so a whole compiler has
to be shipped to the browser. Each run waits for a compile. And the two
instruments the book relies on, step counting and variable tracing, have no
cheap hook, so C++ exercises would get pass/fail plus a timing-based
complexity check and no "watch your code run".

JavaScript is the cheapest runner of the three and gets every instrument,
because the figures' own trace code is already JS. Its weak spot is the
number theory in Part IV: silent precision loss there is worse than a
missing feature.

Proposal: **Python and JavaScript in the first pass**, the reader picks a
language per book, and every open-sourced exercise runs in whichever of the
two its tests are written for (§6.3 often supplies both). **C++ later**,
lazy-loaded only on Part IV pages and run with timing-based checks. Code the
source prints stays in the source's language (cp-algorithms' C++) and isn't
translated.

System design: `component(kind)` boxes (client, DNS, CDN, LB, server, cache,
DB primary/replica, queue, worker, object store) with one icon per kind,
`edge` with animated request packets, `meter` (utilisation on a component),
and `ring` (consistent hashing).

---

## 2. Figures

### 2.1 What lowers friction in a DSA figure

Physics figures win by putting the equation, its symbols and the scene
in one place. DSA has the same opportunity, and more of it, because the
"equation" is code that literally runs. Seven commitments:

1. **Code and state in lockstep.** The code panel sits beside the drawing
   and one transport drives both. The current line is marked, and every
   variable the drawing shows (`lo`, `mid`, `hi`) wears the same colour in
   the code, the prose and the drawing. The reader never has to work out
   which arrow is `j`.
2. **Draw the invariant, not just the motion.** Animated sorting bars
   show that things move. They don't show why the algorithm is correct.
   Every loop figure shades its invariant regions: the sorted prefix in
   insertion sort; the `[lo, hi]` window that must hold `x` if anything
   does; Lomuto's `< p | ≥ p | unseen` bands; Dijkstra's settled set.
   This is the DSA equivalent of the readout that states the relation
   with live numbers (rule 24.7). The readout states the invariant:
   *"a[0..i) is sorted · i = 4"*.
3. **One idea per step.** A step is one named block of code (§2.3), and
   the drawing changes once, for that idea (a swap, a pointer advance, one
   relaxation). A swap morphs (manim transition). It doesn't jump.
4. **A cost counter is always on.** It reads *"comparisons 3 ≤ ⌊log₂ n⌋ + 1 = 4"*
   or *"comparisons 21 of n(n−1)/2 = 28"*, so the bound is checked against the
   run in front of you.
5. **Input is a choice, and the bad case is one of the choices.** Presets
   are `random | sorted | reversed | adversarial`, plus an editable input.
   The worst case is where most interview complexity questions come from,
   so it is never more than one click away.
6. **Pause at the decision, and let the reader predict it.** At each
   branch the figure can stop and ask "which side does `mid` move to?" as
   an inline Try It, a `pick` with no persisted evidence (rule 20). This is
   retrieval practice inside the figure.
7. **Connect one run to the growth curve.** An `n` slider replays the
   count on a log–log plot beside the bound. That one figure ties a single
   trace to asymptotic analysis.

### 2.2 First example figures (DSA), as plan lines

```
sim-binary-search · Sim · binary-search, loop-invariant · invariant made visible; variation by input · arrows: kinematic (lo, mid, hi move) · moving: one pointer per step · choice: input (random sorted | x absent | x at edge), slider: x (key), n (size, 8..64) · headline: "x is in a[lo..hi] if it is anywhere" · graph: none; readout "lo=3 mid=5 hi=7 · comparisons 2 ≤ ⌊log₂ n⌋+1 = 4" · 2D
```
The window `[lo, hi]` is a shaded region in `index`'s tint, and the part
discarded each step fades to ink. The classic off-by-one becomes visible
in a variant toggle, `hi = mid` vs `hi = mid − 1` under `while lo < hi` vs
`lo ≤ hi`. One wrong combination loops forever on the "x at edge" input,
and the figure shows the pointers frozen. People memorise that bug. Here
they can see it.

```
sim-partition · Sim · quicksort, partition-lomuto, partition-hoare · invariant made visible; variation by scheme and input · arrows: kinematic (i, j; swapped cells) · moving · choice: scheme (Lomuto | Hoare), input (random | sorted | all equal) · headline: the scheme's invariant · graph: beside, recursion-depth bar · 2D
```
"All equal" plus Lomuto shows the n² recursion depth. That's the real
reason three-way partitioning exists, and it takes one click to see.

```
sim-dijkstra · Sim · dijkstra, priority-queue, relaxation · flow by animation; the heap and the graph side by side · arrows: kinematic (relax along an edge) · moving · choice: graph (book's example | negative edge) · headline: "settled nodes never change" · graph: none; heap drawn as tree+array beside the graph · 2D
```
On "negative edge", a settled node's distance is shown to be wrong,
flagged in `PAL.bad`. The invariant breaks on screen.

```
sim-lcs-table · Sim · dynamic-programming, lcs · the table's dependency order made visible · arrows: symbolic (dependency arrows into a cell) · moving: one cell per step, then the traceback · choice: strings (book's | user's) · headline: "each cell needs only its three neighbours" · 2D
```
Hovering a cell shows its three dependencies and the subproblem it
stands for (`LCS("ABC", "AB")`). That's the "what does dp[i][j] mean"
sentence, the hardest part of DP to learn, attached to every cell.

```
sim-dsu · Sim · disjoint-set-union, path-compression, union-by-rank (cp-algorithms) · variation by choice · arrows: kinematic (parent pointers re-aimed) · moving · choice: heuristics (none | rank | compression | both) · readout: tree height and total find steps · 2D
```

### 2.3 The figure as a debugger, stepping by block

Whenever an algorithm has code, the default is **code beside the visual**,
and one step highlights the code that ran and the part of the drawing it
changed. The plan line has to argue against the pairing, never for it. But
a line-by-line debugger is the wrong model: `i += 1` is not a thought
anyone has. The unit of a step is a **block**: a few lines that do one
thing, with a name for that thing.

- **Blocks are named in the figure's row, not in the code.** The source's
  code stays verbatim. The figure row lists
  `blocks: [{id, lines: [a, b], label, touches: [...]}]`:
  - `label` is the name of the step ("find the smallest remaining",
    "swap it into place", "relax every edge out of u");
  - `touches` lists the structures and referents the block reads or
    writes.
- **One step runs one block.** The block's lines are marked as one band
  with its label. On the drawing, what the block touched lights up in the
  same moment, and its label is the figure's note. Code and picture
  change together, once per idea.
- **The transport works like a debugger, by block.** Blocks nest (a loop
  body is a block made of blocks), so the controls are the debugger's:
  - *step* runs the next block at the current level;
  - *step into* opens a block's sub-blocks;
  - *step out* finishes the enclosing one.

  The default level is the coarsest one that still changes the picture
  every step. A reader who wants the detail steps into it.
- **The rest of the debugger maps over too.** The *watch* panel is the
  readout, with variables in their referent colours. The *call stack* is a
  stack of frame cards for recursion, each with its own pointers on the
  drawing. A *breakpoint* is a predict pause (§2.1.6), and *run to*
  jumps to the next interesting moment (the next settle, the next merge).
- **Long code is folded.** Over ~25 lines, the panel shows the block
  outline (labels only) with the current block expanded, so the panel
  never scrolls. On a narrow pane the code sits above the drawing and
  shows only the current block.
- **When code doesn't sit beside the figure:** when the idea is a
  property, not a procedure (the BST order property, a heap's shape);
  system design diagrams; and growth plots. The plan line names which
  case applies.

To be refined as we design the real figures.

### 2.4 System design: should we show it step by step? Yes, with one change

Primer chapters and Xu-style case studies are incremental by nature:
one server, then a load balancer, then a replica, then a cache, then a CDN,
then stateless web tier, then a queue, then shards. Each step is a **diff to
one architecture graph**. So the figure is that graph, pinned, and the steps
are states of it:

- **One pinned diagram per chapter, prose scrolls past it.** The diagram
  stays on screen while the text scrolls (scrollytelling). Each prose block
  maps to a step. Entering the block moves the diagram to that state: the
  new component morphs in, a changed edge is drawn in emphasis, the rest
  dims.
- **The change from "show only this step's text":** don't hide the other
  steps. Show them as one-line collapsed headers above and below the
  current one. Fully hiding them cuts the reader off from review and
  skimming, and system design is reread more than it's read. The friction
  we want to remove is scrolling between a diagram and its paragraph, not
  the existence of other paragraphs.
- **Each step says what problem it solves.** The step header is the
  failure that forced it ("the one database is a single point of
  failure"). If the reader drags the step back, the figure shows that
  failure (the request goes red at the dead DB). Interviews reward
  reasoning about why a component is there, and this teaches it.

Diagrams alone won't do it, though. System design has a few quantitative
cores, and those get real sims:

```
sim-queueing · Sim · utilisation, latency, load-balancing · variation by slider · arrows: kinematic (requests) · moving · slider: arrival rate λ (traffic), servers k · headline: "latency explodes near full utilisation" · graph: beside, latency vs ρ with the live point · 2D
```
The 1/(1−ρ) curve is the reason for "don't run above 70%". Readout:
*"ρ = λ/(kμ) = 0.86 · mean wait ≈ 6.1 × service time"* (one server,
ρ/(1−ρ); with k servers the readout uses Erlang C).

```
sim-consistent-hashing · Sim · consistent-hashing, virtual-nodes · variation by choice · arrows: kinematic (keys moving to a new owner) · moving on add/remove · choice: add node | remove node, slider: virtual nodes per server (1..200) · readout: "keys moved 9% (ideal 1/N = 10%) · load spread max/mean 1.4" · 2D ring
```
Beside it, the same action under `hash mod N` moves ~90% of keys. That
comparison is the lesson.

Others worth building: token-bucket rate limiter (bucket level, burst
slider); cache hit ratio vs mean latency; quorum N/R/W with a replica
killed; replication lag with a read from a stale replica.

**Back-of-envelope estimates are derivations** (root rule 29). Each one
is a chain of facts ("300M DAU", "2 writes/user/day", "a tweet ≈ 300 B")
joined into a result ("~180 GB/day"). The derivation graph is a good fit,
and the facts can carry the primer's latency-numbers table as their
source.

---

## 3. Colour

Root rule 7's order (fact, convention, referent, category) still holds.
What changes is where most of the colour goes.

**Hue is for identity. Decoration is for status.** This is the one rule
I'd make book-wide. In a DSA figure the reader's main question is which
of two things a given mark is (`i` or `j`? this pointer or that?), and
that is what hue answers. Status (unvisited, in frontier, settled;
unsorted, sorted) is a variant of the same kind, so rule 7 already says it
is decoration: hollow, dashed ring, filled. Most visualisers do the
opposite (frontier yellow, visited green). With six statuses in six hues
there is no hue left for identity, and the reader has to keep a legend in
their head.

**No syntax highlighting.** Keyword colouring is the extraneous colour a
programmer is so used to that they stop seeing it. In this book's code
panels, keywords are in ink at medium weight. Only the variables the
figure draws are coloured, each as its referent, so colour in code means
the same as colour in the figure. A reader who wants their editor theme
can turn it on per book (a highlights flag, `syntax`).

**Categories (types), DSA**, kept few:

| type | what it covers | why it's a type |
|---|---|---|
| `index` | positions into a structure: i, j, lo, hi, a pointer, a node reference | it gets its own type in any typed language and is the most confused thing in the subject |
| `key` | the values stored and compared | "compare keys, move indices": the two are confused constantly (`a[i]` vs `i`) |
| `cost` | step counts, T(n), O(·), the counter | complexity is a kind of quantity with its own algebra |
| `weight` | edge weights, distances, dist[] | graphs need distance kept apart from index and key |
| `size` | n, m, capacity, height | the variable of every bound |

The `index` vs `key` split lets the page colour `a[i]`: `i` in index colour,
the cell's value in key colour. That one distinction resolves a large share
of beginner bugs.

**Referents.** In an algorithm figure the referents are the variables of
that code (lo, mid, hi; slow and fast; u and v), each its own colour by
rule 7's smart assignment and kept the same in code, prose and drawing. A
variable's letter is its referent colour, so these follow the
referent-wins order. Elements of an input array are usually unnamed
(`F.cat`), unless the text points at one ("the pivot, 5").

**Categories, system design:**

| type | covers |
|---|---|
| `stateless` | web/app servers, workers: scale by adding copies |
| `stateful` | databases, caches, object stores: where data lives and scaling is hard |
| `async` | queues, streams, pub/sub |
| `traffic` | requests, QPS, the packets on the wire |
| `latency` | time per request, p99 |
| `bytes` | storage, bandwidth |

Stateless vs stateful is the central distinction of the subject. When the
two are coloured apart in every diagram, the reader sees the difference
before reading the explanation. In architecture diagrams, components are
coloured by kind (category) and named by label. A specific component the
text keeps pointing at ("the primary", "replica 2") is a referent.

**Conventions and facts.** Few, but real: red-black tree nodes are
literally red and black (a convention, painted as such, with the type hues
kept away from that red); heatmaps of key load or cache hotness are one
false-colour scale with a legend.

**Highlights.** Words on for both halves: "invariant", "amortised",
"sharding" and "quorum" are vocabulary the reader is here to learn.
Symbols on. Underlines on.

---

## 4. Organisation and pipeline

I agree with your order (ToC, then concept map, then fill chapters) with
one change: **build the concept map before the ToC, and derive the ToC
from it.** With three overlapping sources, a ToC made by merging three
ToCs goes wrong in predictable ways: BFS ends up in three places, and the
order follows whichever source was merged first. A DAG settles both,
because prerequisites force the order and each concept gets one home.

### 4.1 Phases

0. **Corpus** (licences settled per §0). Clone cp-algorithms and the
   primer, convert Erickson/ODS (LaTeX sources are public), snapshot CIU's
   README. Each source gets a `sources/<id>/` folder, a converter in
   `tools/`, and a stable locator scheme: `cpa:graph/dijkstra.md#h2-3`,
   `erickson:ch08§3`, `ciu:#trees`.
1. **Inventory per source.** For each source separately, list its
   concepts (root rule 6's five kinds) with locators. A source's list is
   facts about that source. No merging yet, which makes the merge
   reviewable.
2. **Align and merge into one DAG.** Cluster same-concept rows across
   sources and pick a **home** for each concept with a rubric: open licence
   OK → the treatment that states the idea most completely → the one with
   exercises → the one closer to interview level. Other treatments become
   candidates for §5. Hasse-reduce. **Checkpoint: you review the DAG.**
3. **ToC from the DAG.** Parts, then chapters as connected clusters in
   topological order, then sections as concept homes. Tag every section
   by tier: `core` (CIU's required list), `stretch` (CIU's optional list,
   common cp-algorithms topics like DSU, segment tree, KMP), `contest`
   (most of cp-algorithms' Algebra, Geometry and Numerical). **Checkpoint.**
4. **Per section** (root rules 2 to 29), with two new rules below.

### 4.2 A first ToC to react to

- **Part I · Foundations** (ODS/Erickson, ordered by CIU): complexity and
  Big-O; arrays and dynamic arrays (amortised doubling); linked lists;
  stacks and queues; hash tables; binary search; bit manipulation.
- **Part II · Trees and graphs**: trees and traversals; BSTs; heaps and
  priority queues; balanced trees (AVL/red-black, intuition level); tries;
  graph representations; BFS/DFS; topological sort; shortest paths;
  minimum spanning trees.
- **Part III · Paradigms**: recursion and backtracking; divide and conquer
  and sorting; greedy; dynamic programming; two pointers and sliding
  window (CIU has no section for these, but they are core interview
  patterns; cp-algorithms touches them).
- **Part IV · Beyond the interview** (cp-algorithms, `stretch` then
  `contest`): DSU, Fenwick and segment trees, sparse tables, string
  algorithms (prefix function, Z, hashing, suffix structures), number
  theory, advanced graphs (flows, SCC, bridges, LCA), geometry.
- **Part V · System design** (primer spine): scaling step by step;
  building blocks (DNS, CDN, LB, cache, DB, replication, sharding, queues,
  consistent hashing); estimation; case studies.
- **Appendix**: CIU's "Getting the Job" (interview process, what to
  practise) as a reading page, and CIU's daily plan as a checklist driven
  by the concept DAG's attainment, not a static list.

### 4.3 Two root rules this book has to bend

- **"Keep the book's words"** becomes **keep each block's source words, with
  provenance**. Every `<section>` block in `text.html` carries
  `data-source` and a locator. A concept's explanation is one source's
  writing, whole (§5). Where a section joins concepts from two sources,
  a bridging sentence between them is OmniStax's and AI-marked.
- **"Don't fold sections together"** (rule 11) assumes the source's
  sections are the units. Here the unit is the concept home from §4.1.
  A cp-algorithms article that is mostly a duplicate of a Part II home is
  folded into that home as a depth block and isn't a page of its own. Fold
  it only when the article really is a duplicate. Each fold is listed in
  the chapter's `exploration.md`.

### 4.4 Decisions so far

1. System design: the primer only. No AI-written prose.
2. Erickson and ODS come in, and so does anything else the finder turns up.
   The judge (§6) picks per topic: lucidity first, then cohesive style,
   then comprehensiveness.
3. Languages: Python and JavaScript in the first pass, C++ later (§1.5).
4. Code exercises: pulled from open sources first. No exercise is
   AI-written. Tests and reference solutions may be AI-written, and are
   marked (§6.3).
6. Licence: CC BY-SA 4.0, except NC exercise cards kept in separate files (§0).
7. Judge: lucidity concept by concept, with continuity between neighbours
   deciding close calls. Only escalated verdicts go to you.
8. Figures: code beside the visual by default, stepping by named block
   like a debugger (§2.3).
9. Structure (2026-11-08): one book, flat chapters, no parts. The former
   Computer systems chapters become Appendix A, a curated links appendix
   (unbuilt); Getting the job is Appendix B.
10. Tiers: system design concepts take their own tiers (core where the
    primer says so); union-find is core.
11. One explanation per concept, one source, its writing kept whole (§5).
12. MIT and Apache 2.0 prose allowed with notices; versions chosen per page;
    *Computer Networks: A Systems Approach* excluded entirely (§6.1).
13. Tiers are shown to the reader as **Essential, Advanced, Beyond** (the
    concept map's `core`, `stretch`, `contest`), with no app change:
    - **The book's introduction** (an OmniStax-written page, AI-marked)
      says what each word means and lists which chapters are which. A
      chapter with sections of mixed tiers is listed under its most common
      tier, and its exceptions are named.
    - **Each section's lead** (the OmniStax-written sentence or two under
      the title, root rule 21.5) says the section's tier, and names any
      concept in it whose tier differs.
    - Nothing else in the app changes. Practice sessions don't filter by
      tier.
14. B-tree internals are Advanced: the database-indexes → B-tree edge is
    cut (knowing an index is a B-tree is Essential; its operations aren't).
15. OI Wiki (CC BY-SA 4.0 + SATA) is usable, translated from Chinese under
    `docs/prompts/translate.md` and AI-marked as a translation. Its SATA
    terms need the authors thanked in the attribution and the repo starred
    from the owner's account (a person does that, not Claude). doocs/leetcode
    solution write-ups are usable, each paired with an open exercise that
    poses the same problem, since LeetCode's statements can't be copied.
5. First pass: the concept map and the ToC for the whole book, then the
   first three chapters.

---

## 5. One explanation per concept

**Decided:** every concept is explained once, by one source, in that
source's original writing, kept whole. There is no "Another angle" block,
no second treatment on a missed exercise, and no stitching passages from
two sources into one concept's explanation. The judge (§6.2) picks the
source. A section may still hold concepts from different sources, since
a section is a page of several concepts.

CIU's video and article links don't count as explanations. The curated
ones (at most three per section, each with one sentence on what it is
good for) live in the shell's References item, never in the text.

---

## 6. The resource finder and the resource judge

Two subagents with separate powers. The finder fetches and never ranks
quality. The judge ranks and never fetches. So the judge only sees what is
on file, every verdict can be traced back to evidence, and nothing gets
picked just because it was easy to get.

### 6.1 The finder

**Input:** one chapter of the concept map: its concepts, their statements
and prerequisite edges, and the tier tags.

**Licence gate first.** A candidate goes into the dossier only if its
licence is compatible with CC BY-SA 4.0: public domain, CC0, CC BY,
CC BY-SA, MIT, BSD or Apache 2.0. MIT and Apache prose keep their
licence notice in the section's attribution. GPL, MPL, GFDL, ND and
"no licence" are out. The evidence goes on file: the
licence file's URL and the quoted line. Pages on one site can carry
different licences (LibreTexts does this), so the check is per page, not
per site. Anything else is recorded as **link-only** with the reason and
never enters the text.

**Which version of a page:** the current one, unless that page is marked
AI-assisted (front matter such as `ai-usage: ai-assisted`, or an edit
summary saying so). In that case use its last version before the mark.
Decide page by page, never by pinning a whole site to a date.

**Excluded outright:** *Computer Networks: A Systems Approach* (Peterson
and Davie). Not used, not linked.

**Where it looks, in order:**
1. The registered corpus: cp-algorithms, the primer, Erickson, ODS, CIU.
   This is a cheap local search.
2. Known open collections: OpenDSA, Wikibooks, Wikipedia, the Open
   Textbook Library, open university lecture notes with a stated licence,
   arXiv papers under CC BY for the advanced topics.
3. The links in CIU's lists, followed one by one and kept when their
   licence passes.
4. Open web and GitHub search for the concept, filtered by licence.

**How it obtains things:** clone the repo, get LaTeX or Markdown sources
before falling back to PDFs (`pdftotext` keeps math worse than the source
does), and pull captions for videos whose licence passes (YouTube's CC BY
flag). Few interview videos are CC BY, and a transcript reads like speech,
so expect videos to end up as link-only side-panel references (§5).
Every fetched item is saved under `sources/<id>/` with its URL, the date,
the licence evidence, and a locator scheme.

**Output:** a dossier per chapter, `dossiers/<chapter>.md`. Each candidate
gets a row: locator, licence and evidence, kind (prose | code exercise with
tests | figure | dataset), the concepts it covers, length, and
prerequisites it assumes that the concept map puts later. The finder
writes no opinion on quality.

**Network:** this cloud environment has a network policy, and
YouTube, PDF hosts or some universities may be blocked. The finder
records each blocked host in the dossier. Opening a host is a change the
user approves.

### 6.2 The judge

Your three criteria, applied in that order, with the steps that keep an LLM
judge honest:

- **Lucidity (decides).** Checked against concrete signs, not a general
  impression:
  - each term is defined before it is used;
  - an example sits next to the abstraction;
  - the passage says why the idea is needed before giving it;
  - it avoids unexplained jumps ("it is easy to see", skipped steps);
  - every claim is correct.

  Correctness is checked, not assumed: the judge runs the passage's code on
  small inputs, works one example by hand, and checks the stated
  complexity. A clear passage that is wrong loses.
- **Cohesive style (counts when lucidity is close).** Lucidity is judged
  concept by concept. Each pairwise verdict says "clearly better",
  "slightly better" or "even".
  - "Clearly better" decides outright.
  - Otherwise continuity decides: the candidate whose source is also the
    source for the concept's neighbours (its prerequisites and dependants
    in the concept map, and the adjacent sections) wins.

  Since neighbours depend on each other's choices, this runs in two
  passes:
  1. Pick by lucidity alone.
  2. Revisit only the close calls, moving each toward its neighbours'
     majority source. Repeat until nothing changes.

  Notation is part of style: 0- or 1-indexed arrays, pseudocode or real
  code, "we" or "you". A clash with the neighbours counts against a
  candidate in a close call.
- **Comprehensiveness (last).** Measured against the concept map, not the
  judge's taste: does the passage cover the concept's statement, its edge
  cases, its cost, and the sub-concepts the map hangs under it?

**Procedure:**
- **Pairwise and blind.** Source names and URLs are stripped from the
  passages, which removes prestige bias. Each pair is judged in both
  orders, which removes position bias.
- **Disagreement escalates.** If the two orders disagree, the pair is
  judged by a second independent judge. If the judges still disagree, it
  goes to you. Only escalated verdicts come to you; the rest are on file.
- **Verdicts are written down.** Each one goes to
  `judgements/<chapter>.md` with the winner, a ranked list, quoted
  passages for each reason, and the correctness checks it ran.
- **Exercises get their own pass.** The same blind procedure ranks them,
  on whether the tests cover the edge cases, whether the statement is
  clear, and how well the exercise fits the concepts. Its reference
  solution is run against its own tests before the exercise is accepted.

Both judges use the `the-judge` skill's stance: no deference to how
famous a source is.

### 6.3 Where open code exercises come from

The finder's first stops for code exercises (licences to confirm):

- **Exercism `problem-specifications`** (MIT): problem descriptions plus
  language-neutral test cases in `canonical-data.json`. It covers binary
  search, linked lists, binary search trees, a circular buffer,
  word-search and more. The tests port to Python and JS mechanically, so
  one exercise runs in both runners.
- **ICPC regional problem packages published under CC BY-SA** (several
  regionals publish statements, test data and reference solutions), for
  Part IV.
- **Kattis open problems** whose page states a CC BY-SA licence.
- **TheAlgorithms/Python** (MIT): implementations with doctests, not
  exercises. Their doctests are a source of test cases for a printed book
  exercise. **TheAlgorithms/JavaScript is GPL-3.0**, so it is link-only;
  `trekhleb/javascript-algorithms` (MIT, jest tests) supplies JS tests
  instead.
- **Kattis** states CC BY 3.0, CC BY-SA 3.0, CC0 or public domain on each
  problem page. BY-SA 3.0 allows adaptation under 4.0. Problems marked
  "For educational use only" are link-only. Only sample tests are public.

**Decided: tests may be AI-written, exercises may not.** Every exercise
statement comes from a source. Where the source has no tests, the tests
are AI-written: `tests_by: "ai"`, AI-marked on the card. The same goes for
the reference solution, unless the source supplies one (ICPC reference solutions,
Exercism example solutions). The reference must pass every test and the
complexity check before the exercise ships. Tests should cover what the
statement implies: the empty input, one element, duplicates, the worst
case at the stated bound. A test may never add a requirement the
statement doesn't make.

---

## Next step I'd propose

1. Phase 0 and 1 (§4.1): register the corpus, and inventory the concepts
   in each source.
2. Merge them into the concept map, then derive the ToC. You review both.
3. For chapters 1 to 3: finder dossiers, then judge verdicts. You review
   those.
4. In parallel with 2 and 3, since neither depends on the other: the
   `sim-binary-search` prototype, the step-by-step scaling diagram, and
   the `code` answer type with the Python and JS runners.
