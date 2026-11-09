# Reconciliation: chapters 1 to 3

Reconciliation pass of 2026-11-08 across `judgements/ch01.md`, `ch02.md` and `ch03.md`.
Inputs: `.claude/agents/resource-judge.md`, METHOD.md §4.4, §5 and §6.2,
`concept-map/toc.md` and `concepts.json` (chapters `ch-cost`, `ch-arrays-lists`,
`ch-stacks-queues`), the three dossiers, and the cached ODS, OI Wiki, Erickson and
Wikipedia files named below. Nothing was fetched, and the three per-chapter files are
not edited.

**Rules applied.**
- This pass revisits only the close calls and the cross-chapter items the three files
  list. Each one moves toward its neighbours' majority source: concept-map prerequisites
  and dependants first, then the adjacent sections.
- "Clearly better" verdicts are never overturned for continuity.
- One source per concept, used whole (§5). Where a winner leans on a term or name that
  another source introduced, the fix is an OmniStax bridging sentence in the section
  lead. Bridges are listed here, not written.
- Never candidates: anything with an `excluded` field in `sources/registry.json`
  (`eh-dsa`, `algowiki`, `openstax-introcs`, `openstax-introcs-ex`) and doocs
  "Thinking" blocks. `dsa-dummies` is pending a provenance ruling, so it is not picked.
  It is not a winner anywhere in chapters 1 to 3, so the ruling changes nothing here.
- `big-o` is with a second independent judge. ODS is treated as its provisional winner
  and is not re-judged. The last item of the next section checks whether either outcome
  moves any neighbour.

**Result.** The pass ran to a fixed point in one iteration. **No winner changed.** Every
close call already sat with its neighbours' majority, or its only rival had no neighbour
at all. Three continuity reasons recorded in the chapter files were out of date once all
three chapters were known; each outcome still holds, for the corrected reason given
below.

---

## Items revisited

Neighbours are named with their final winners. W = Wikipedia.

### 1. array and pointer-arithmetic (W) against Aspnes 223 §4.9.5 + 4.9.5.1: keep both

- Margin as judged: W slightly better **in both orders** for each concept, so Aspnes
  was never ahead on lucidity.
- Neighbours of `array`: pointer-arithmetic (W), dynamic-array (ODS), two-pointers (OI
  Wiki), merge-sorted-sequences (W), sliding-window-fixed (W), prefix-sums (OI Wiki).
  Neighbours of `pointer-arithmetic`: array (W), implement-vector (ODS), and in the
  same article pointer-to-pointer (W, clearly better).
- Aspnes 223 wins nothing in chapters 1 to 3, so moving the pair toward it goes against
  the majority. The other equilibrium that ch02.md mentions (Aspnes for both) would
  need a lucidity edge that Aspnes does not have.
- ch02.md's condition ("if `word-ram` is taught from a source that covers memory and
  addresses") does not apply. `word-ram` is ODS §The Model of Computation, which
  covers w-bit words, not addresses.

### 2. dynamic-array (ODS) and chapter 1's amortized choice (OI Wiki): keep

- Margin as judged: W slightly better A-then-B, even B-then-A. Close.
- Neighbours: running-time-guarantees (ODS), list-interface (ODS), array (W),
  array-resize, dynamic-array-cost, block-copy and implement-vector (ODS),
  linked-list-vs-array (W), stack (W), circular-buffer (ODS). ODS has 7 of 10. Chapter
  3's array-queue, array-deque and rootish-array-stack also cite ArrayStack's resize()
  by name.
- ch02.md's condition ("if chapter 1's `amortized-analysis` is not ODS, continuity
  weakens slightly") is met: it is OI Wiki. But `amortized-analysis` is a prerequisite
  of `dynamic-array-cost`, not of `dynamic-array`, so the majority above is unchanged.
- **dynamic-array-cost (ODS) against the OI Wiki trio.**
  - Margin as judged: ODS slightly better in both orders.
  - Its prerequisite amortized-analysis is OI Wiki. But OI Wiki is not a candidate
    here: its dynamic-array analysis is already the 1.5 passage and cannot be used twice.
  - The runner-up (W #Performance with Amortized_analysis#Dynamic array) has no
    neighbour.
  - The dependants (array-queue, dual-array-deque, rootish-array-stack) are ODS and cite
    `lem:arraystack-amortized`. Keep.
- **Notation clash (verified in the cache).** It counts against ODS, but cannot move
  the call, since the only rival is no closer:
  - OI Wiki 势能分析 writes n for the number of elements and m for the capacity:
    "其中，n 是数组中的元素数量，m 是数组的当前容量" ("where n is the number of
    elements and m the current capacity").
  - OI Wiki 聚合分析 uses m for the array's size when it is full, and n for the number
    of inserts.
  - ODS writes n for the size and `a.length` for the capacity, and adds shrinking at
    `a.length ≥ 3n`, which 1.5 never covers.
  - Bridge B6 handles this.

### 3. logarithms (ODS) against OpenDSA: keep

- Margin as judged: OpenDSA slightly better in both orders. Not clear.
- Neighbours: factorials-stirling (ODS), harmonic-numbers (ODS), word-ram (ODS),
  big-o (ODS, provisional). That is 4 of 4, or 3 of 4 if big-o changes.
- ch01.md's condition ("if chapter 2's word-RAM-dependent concepts end up non-ODS")
  does not apply. word-ram's dependants (multiplicative-hashing, external-memory-model,
  binary-trie) are in chapters 5, 7 and 12, not chapter 2.
- Comprehensiveness also favours ODS (ln k = (ln 2) log k is only in ODS).

### 4. linearity-of-expectation (ODS) against mcs2018 19.5: keep, with a gap to bridge

- Margin as judged: even A-then-B, MCS slightly better B-then-A. The two orders do
  not oppose each other, so there is no escalation.
- Neighbours: prerequisite conditional-probability (brisk), and the dependants
  indicator-variables (ODS, clearly better) and geometric-expectation (ODS). Later
  dependants are chaining-analysis, random-bst and skiplist-structure (chapters 5, 8
  and 12, not judged yet; the map's sources for them are ODS-led). ODS has 2 of the 3
  judged neighbours.
- Notation counts against MCS:
  - MCS writes `Ex[R]` and `Pr[...]`.
  - The indicator passage that follows (ODS, the same subsection, cut at "A useful
    trick") writes `E[X]`, `Pr{X=i}` and refers back to "the definition of expected
    value" in ODS's own first part.
  - Splitting the subsection between MCS and ODS would put the indicator passage after
    a definition in another notation.
- **The gap, verified in `ods/latex/intro.tex` lines 673–764.** The row's name is
  "Random variables and linearity of expectation", and its statement includes constants
  aᵢ and "no independence required".
  - ODS uses the term before defining it: "Formally, the running time of an operation
    on a randomized data structure is a random variable".
  - ODS states linearity for sums without the constants aᵢ, and never says
    "no independence".
  - brisk has no random-variable section (none of `sources/_cache/brisk/*.tex` contains
    the phrase).
  - So no chapter 1 winner defines "random variable".
  - These are comprehensiveness gaps, the last criterion. They do not override a
    continuity decision.
- Fix: bridge B4 in the 1.6 lead. That is an OmniStax-written definition of a term in
  the concept's own name, which is why it is listed for the user below.
- The alternative is to move both linearity-of-expectation and indicator-variables to
  MCS 19.1 + 19.4 + 19.5. It is rejected:
  - indicator-variables is "clearly better" ODS, which cannot be overturned for
    continuity;
  - MCS alone would then leave the notation clash with geometric-expectation (ODS).

### 5. The SLList bridging question (2.5 Wikipedia; 2.6 and 3.2 ODS): keep 2.5, bridge

- Margin as judged: `singly-linked-list` and `implement-linked-list` both W, slightly
  better in both orders.
- Neighbours of singly-linked-list: implement-linked-list (W), linked-list-vs-array (W),
  section sibling pointer-to-pointer (W), sentinel-node (ODS), queue-linked-list (ODS),
  floyd-cycle-detection (cpa). That is W 3, ODS 2, cpa 1, so the majority holds W.
- Moving 2.5 to ODS SLList would reverse two "slightly better in both orders" calls
  against the majority. It would also bring in Stack vocabulary before chapter 3: the
  SLList section opens with "An SLList can efficiently implement the Stack operations
  push() and pop()" (`linkedlists.tex` line 54).
- **What the bridge must carry (checked in `ods/latex/linkedlists.tex`).** More than the
  name is missing:
  - DLList opening, lines 113–122 (sentinel-node): "very similar to an SLList except…";
    "When implementing an SLList, we saw that there were always several special
    cases".
  - Queue Operations, lines 71–87 (queue-linked-list): "Removals are done from the head
    of the list, and are identical to the pop() operation". It shows only `remove()`
    and `add(x)` code, and uses the fields `head`, `tail` and `n` from the SLList
    opening, which the book does not use.
  - Closing paragraph, lines 99–105 (queue-linked-list): "An SLList nearly implements
    the full set of Deque operations". Deque comes in 3.3, after 3.2.

  So two bridges are needed, B10 (2.6) and B11 (3.2). One sentence alone does not cover
  `pop()` and the fields.
- **sentinel-node (ODS) against W's ===Sentinel nodes===: keep.**
  - Margin as judged: ODS slightly better A-then-B, even B-then-A. W was never ahead.
  - The direct map edges tie: prerequisite singly-linked-list (W), dependant
    doubly-linked-list (ODS).
  - Two things break the tie for ODS:
    - the same-section sibling, doubly-linked-list, is ODS, and its passage is the
      continuation of this one;
    - its code uses `dummy`, which W's sentinel sections do not name. That is a
      notation clash against W with the section's other concept.
  - The adjacent section 2.5 is W, but 2.7 is cpa, so adjacency does not give W a
    majority over the dependant and the section sibling.
- **queue-linked-list (ODS) against Aspnes 5.4.2: keep, for a corrected reason.**
  - ch03.md's continuity reason was "ODS SLList is a treatment of chapter 2's
    singly-linked-list". That no longer holds, since 2.5 is W.
  - The remaining neighbours: prerequisites queue (ODS) and singly-linked-list (W),
    and section siblings circular-buffer and array-queue (ODS). The majority is ODS.
  - Notation also counts against Aspnes (C with pointers, against the section's ODS
    code), and Aspnes's figures are not cached.

### 6. list-interface takes the List subsection of the same ODS section: confirmed

- ODS `intro.tex` §Interfaces is split three ways, with no overlap:
  - the opening (lines 141–167) goes to `interface-vs-implementation` (1.1);
  - §The Queue, Stack, and Deque Interfaces (169–256) goes to `queue` and `deque`
    (3.2, 3.3);
  - §The List Interface (257–306) goes to `list-interface` (2.1), clearly better.
- The book reads them in the order 1.1, 2.1, 3.x. So the List subsection's first
  sentence, "This book will talk very little about the FIFO Queue, Stack, or Deque
  interfaces", points at a subsection the reader has not seen yet. Bridge B7.
- The List subsection's last paragraph explains why list classes carry Stack and Deque
  in their names ("the ArrayDeque class is an implementation of the List interface").
  That already answers ch02.md's note on the name ArrayStack. Bridge B8 only points
  back to it.
- The 1.1 opening says "in \chapref{arrays} … and in \chapref{linkedlists}". These are
  ODS chapter references, which the builder maps to book §2.2 and §2.5–2.6 (a
  reference fix, not a bridge).
- Two ODS paragraphs stay unused: the LIFO paragraph (stack went to W) and the priority
  queue paragraph (left for chapter 9).

### 7. three-sum (W) against doocs 0015: keep

- Margin as judged: W slightly better A-then-B, even B-then-A.
- Neighbours: prerequisite two-pointers (OI Wiki), and section siblings
  merge-sorted-sequences and sliding-window-fixed (W) and sliding-window-variable (OI
  Wiki). doocs has no neighbour anywhere in chapters 1 to 3, because no doocs
  write-up won.
- Notation: W writes `S[0..n-1]`, 0-based like its W siblings. OI Wiki's two-pointers
  is 1-based, but doocs is 0-based as well, so indexing does not separate the pair.
- The duplicate-handling advantage of doocs is comprehensiveness, which is last. The
  exercise card carries the "skip equal neighbours" hint (ch02.md).

### 8. sliding-window-variable (OI Wiki) against doocs 0003: keep

- Margin as judged: OI Wiki slightly better in both orders.
- Neighbours: two-pointers (OI Wiki, the same page, clearly better) and
  sliding-window-fixed (W). doocs has none.
- The indexing matches its same-page neighbour (1-based, r − l + 1).

### 9. Chapter 3 close calls: keep all

| concept | margin as judged | neighbours (final) | decision |
|---|---|---|---|
| queue | even / ODS slightly | interface-vs-implementation (ODS), circular-buffer, queue-linked-list, deque (ODS) | keep ODS; ch03.md's condition (1.1 is ODS) is met |
| circular-buffer | even / ODS slightly | queue, array-queue (ODS), dynamic-array (ODS) | keep ODS; ch03.md's condition (dynamic-array is ODS) is met. The bounded and overwrite part of the row stays a comprehensiveness gap, covered by the Exercism exercise and bridge B15 |
| deque | W slightly / even | stack (W), queue, array-deque, dual-array-deque (ODS) | keep ODS. W's `add(left, x)` clashes with the addFirst/addLast names that both dependants use |
| sliding-window-minimum | OI Wiki slightly / even | sliding-window-fixed (W), monotonic-queue-minimum (cpa, same article) | keep cpa; neither OI Wiki nor W is a winner in 3.4 apart from W's nearest-smaller-element. ch03.md item 5 is settled: no doocs winner in 2.3 |
| largest-zero-submatrix | even / cpa slightly | nearest-smaller-element (W), section majority cpa | keep cpa; doocs 0085 has no neighbour |
| bracket-validation, rpn-evaluation, expression-parsing, sqrt-space-lower-bound | cpa or ODS in both orders or by continuity | same-article neighbours | keep |

### 10. potential-method (OI Wiki) against ODS's DualArrayDeque lemma: keep, bridge

- Margin as judged: OI Wiki slightly better A-then-B, even B-then-A. The ODS lemma
  ranked fourth.
- The ODS lemma is the whole of chapter 3's `dual-array-deque` passage
  (`ods:arrays#sec:dualarraydeque`). Using it for `potential-method` too would put one
  passage under two concepts, so it is not available.
- The prerequisite aggregate-accounting is OI Wiki (clearly better), so continuity
  agrees. ch03.md item 4 is settled: there is no double use. Its suggestion of
  jeffe-notes is not possible, because jeffe-notes is NC.
- **Wording, checked in `arrays.tex` lines 595–627 and `linkedlists.tex` lines
  494–529.**
  - DualArrayDeque: "We will perform our analysis using a technique knows as the
    *potential method*… Φ = |front.size() − back.size()|… can increase the potential by
    at most 1". It then counts: "the number of calls… is at least Φ₁ − Φ₀ > n/2 − 1".
  - SEList (`selist-spread-gather`): "We will use the potential method of amortized
    analysis", where Φ is the number of fragile nodes. It argues the same way: Φ rises
    by at most 1 per cheap operation and drops by b − 1 per spread.
  - Neither writes amortized cost = actual cost + ΔΦ, the form 1.5 teaches (OI Wiki:
    "Φ(h) = 2n − m", amortized cost "1 + 2 = 3").
  - Both arguments are valid instances of the method: charge each operation a constant
    times its possible rise in Φ. But a reader will meet "potential" used two ways.
    Bridges B14a (3.3) and B14b (3.6).
- New erratum found: "knows as" should be "known as" (`arrays.tex` line 596).

### 11. Indexing: Erickson, OI Wiki and the 0-based neighbours

Indexing decides no concept.
- Every OI Wiki win in 2.4 was clearly better.
- Two-pointers was clearly better.
- Sliding-window-variable matches its same-page neighbour.
- complexity-analysis (Erickson, 1-based): its prerequisite describing-algorithms is
  Erickson (clearly better), and its other prerequisite big-o is ODS. A tie on
  continuity falls to comprehensiveness: Erickson covers space, recurrences and data-
  structure dependence, and aspnes-223 5.1.3 covers none of them. Keep, as in ch01.md
  item 7.
- Erickson is mixed inside itself (checked in `jeffe/00-intro.txt`). The digit arrays are
  0-based, `X[0..m−1]`, `Y[0..n−1]`, `Z[0..m+n−1]`, because digit i weighs 10^i. The
  data arrays are 1-based (`Pop[1..n]`, `Rep[1..n]`), and so are the later chapters
  (`A[1..n]` in MergeSort).

The section leads must state the convention for each passage; see "Indexing convention
per section".

### 12. big-o's pending ruling: no knock-on in either outcome

I checked what an aspnes-223 result would do to each neighbour:
- logarithms: still 3 of 4 neighbours ODS.
- complexity-analysis: the prerequisites would tie, Erickson and aspnes. Comprehensiveness
  still favours Erickson (item 11).
- big-omega-theta: aspnes-223 5.1.4 defines Θ wrongly ("both O(f(n)) and Ω(g(n))").
  OpenDSA's section sibling multivariate-big-o is OpenDSA, and won clearly. So OpenDSA
  stays, with continuity now on its side rather than neutral.
- running-time-guarantees and multivariate-big-o were clear.

If aspnes-223 wins, only these follow: its C examples sit beside ODS's Java/C++ and
OpenDSA's Java (compatible, as ch01.md says), and ODS's two big-o errata drop off the
errata list.

---

## Final winner table

"Changed" = whether this pass changed the winner. All rows read **no**.

### Chapter 1: Algorithms and their cost

| concept | § | source | locator | changed |
|---|---|---|---|---|
| algorithm | 1.1 | Erickson | `jeffe:0.1` (with `jeffe:0.3` as its worked example, a builder call) | no |
| underspecified-algorithm | 1.1 | Erickson | `jeffe:0.4` | no |
| describing-algorithms | 1.1 | Erickson | `jeffe:0.5` (intro, Specifying the Problem, Describing the Algorithm) + `jeffe:0.6` opening and "Correctness" | no |
| need-for-efficiency | 1.1 | ODS | `ods:intro#the-need-for-efficiency` | no |
| interface-vs-implementation | 1.1 | ODS | `ods:intro#sec:interfaces`, section opening to the first subsection | no |
| lattice-multiplication | 1.1 | Erickson | `jeffe:0.2` preamble + "Lattice Multiplication" | no |
| peasant-multiplication | 1.1 | Erickson | `jeffe:0.2` "Duplation and Mediation" | no |
| logarithms | 1.2 | ODS | `ods:intro#exponentials-and-logarithms` | no |
| factorials-stirling | 1.2 | ODS | `ods:intro#sec:factorials` | no |
| harmonic-numbers | 1.2 | ODS | `ods:rbs` harmonic digression (`latex/rbs.tex` lines 76–110, with the harmonic-integral figure) | no |
| big-o | 1.3 | ODS (**provisional**, second judge pending) | `ods:intro#asymptotic-notation`, up to the multivariate paragraph | no (not re-judged) |
| big-omega-theta | 1.3 | OpenDSA | `opendsa:AlgAnal/AnalLower` (Lower Bounds, Theta Notation, Classifying Functions) | no |
| multivariate-big-o | 1.3 | OpenDSA | `opendsa:AlgAnal/AnalMultiple` | no |
| word-ram | 1.4 | ODS | `ods:intro#sec:model` | no |
| complexity-analysis | 1.4 | Erickson | `jeffe:0.6` "Running Time" to the end of 0.6 | no |
| running-time-guarantees | 1.4 | ODS | `ods:intro#correctness-time-complexity-and-space-complexity` | no |
| amortized-analysis | 1.5 | OI Wiki (translate) | `oiwiki:basic/amortized-analysis` 引入 + 内容 + 聚合分析 | no |
| aggregate-accounting | 1.5 | OI Wiki (translate) | `oiwiki:basic/amortized-analysis` 记账分析 + 扩展示例：堆栈操作 (聚合分析法, 记账分析法) | no |
| potential-method | 1.5 | OI Wiki (translate) | `oiwiki:basic/amortized-analysis` 势能分析 (原理, 示例：动态数组的扩容分析) + 堆栈 势能分析法 | no |
| counter-increment-decrement | 1.5 | **none** (gap) | jeffe-notes 9.3 as a References link only (NC) | no |
| counting | 1.6 | brisk | `brisk:counting#The Fundamental Theorem`, `#Permutations` (with Partial permutations), `#Combinations` | no |
| probability-basics | 1.6 | brisk | `brisk:probability#Outcomes and events`, `#Probability measures` | no |
| conditional-probability | 1.6 | brisk | `brisk:probability#Conditional probability`, `#Independence` | no |
| linearity-of-expectation | 1.6 | ODS | `ods:intro#sec:randomization`, from the start to "…into sums of simpler random variables (the right hand sides)." | no |
| indicator-variables | 1.6 | ODS | `ods:intro#sec:randomization`, from "A useful trick…" to the end of the subsection | no |
| geometric-expectation | 1.6 | ODS | `ods:skiplists#lem:coin-tosses` (lemma and proof) | no |

### Chapter 2: Arrays and linked lists

| concept | § | source | locator | changed |
|---|---|---|---|---|
| array | 2.1 | Wikipedia | `wikipedia:Array_(data_structure)` lead + #Element identifier and addressing formulas (intro, ===One-dimensional arrays===, ===Multidimensional arrays===) + #Efficiency + the Iliffe-vector paragraph of ===Comparison with other data structures=== | no |
| pointer-arithmetic | 2.1 | Wikipedia | `wikipedia:Pointer_(computer_programming)#C arrays` | no |
| list-interface | 2.1 | ODS | `ods:intro#the-list-interface-linear-sequences` (whole subsection, fig. list) | no |
| dynamic-array | 2.2 | ODS | `ods:arrays#chap:arrays` opening (table, three bullets, amortized paragraph) + `#sec:arraystack` opening + "The Basics" | no |
| array-resize | 2.2 | ODS | `ods:arrays#growing-and-shrinking`, first two paragraphs | no |
| dynamic-array-cost | 2.2 | ODS | `ods:arrays#growing-and-shrinking` from "The running time analysis from the previous section ignored…" through `lem:arraystack-amortized` and proof, + "Summary" (`thm:arraystack`, push/pop paragraph) | no |
| block-copy | 2.2 | ODS | `ods:arrays#sec:fastarraystack` (whole) | no |
| implement-vector | 2.2 | ODS | the ArrayStack class as shown in the 2.2 passages (no separate prose block) | no |
| two-pointers | 2.3 | OI Wiki (translate) | `oiwiki:misc/two-pointer#引入` + `#利用序列有序性` (过程 only) | no |
| three-sum | 2.3 | Wikipedia | `wikipedia:3SUM` lead, first sentence + #Quadratic algorithm | no |
| merge-sorted-sequences | 2.3 | Wikipedia | `wikipedia:Merge_algorithm#Merging two lists` | no |
| sliding-window-fixed | 2.3 | Wikipedia | `wikipedia:Moving_average#Simple moving average`, opening to "…only 3 arithmetic steps." | no |
| sliding-window-variable | 2.3 | OI Wiki (translate) | `oiwiki:misc/two-pointer#维护区间信息` opening + 例题 1 过程 | no |
| prefix-sums | 2.4 | OI Wiki (translate) | `oiwiki:basic/prefix-sum#引入` (with 规定 box) + `#前缀和` + `### 一维前缀和` (prose, formulas, std::partial_sum note) | no |
| prefix-sums-2d | 2.4 | OI Wiki (translate) | `oiwiki:basic/prefix-sum` `#### 基于容斥原理` (with 示例, figure prefix-sum-2d) + `#### 逐维前缀和` | no |
| difference-array | 2.4 | OI Wiki (translate) | `oiwiki:basic/prefix-sum#差分` opening + `### 一维差分` (with 性质 box) | no |
| difference-array-2d | 2.4 | OI Wiki (translate) | `oiwiki:basic/prefix-sum### 二维/多维差分` | no |
| singly-linked-list | 2.5 | Wikipedia | `wikipedia:Linked_list` lead + #Basic concepts and nomenclature + ===Singly linked list=== | no |
| pointer-to-pointer | 2.5 | Wikipedia | `wikipedia:Pointer_(computer_programming)#Multiple indirection` | no |
| implement-linked-list | 2.5 | Wikipedia | `wikipedia:Linked_list#Linked list operations` intro + ====Singly linked lists==== | no |
| linked-list-vs-array | 2.5 | Wikipedia | `wikipedia:Linked_list#Linked lists vs. dynamic arrays` | no |
| sentinel-node | 2.6 | ODS | `ods:linkedlists#sec:dllist`, opening through fig. dllist and the DLList() code import | no |
| doubly-linked-list | 2.6 | ODS | `ods:linkedlists#sec:dllist` from getNode(i) through "Adding and Removing" and "Summary" | no |
| floyd-cycle-detection | 2.7 | cpa | `cpa:others/tortoise_and_hare` intro + #proposed-algorithm ###Step 1 + #why-does-it-work ###Step 1 | no |
| cycle-start | 2.7 | cpa | `cpa:others/tortoise_and_hare#step-2-starting-point-of-the-cycle` (with both Java snippets) | no |
| cycle-start-proof | 2.7 | cpa | `cpa:others/tortoise_and_hare#step-2-starting-point-of-the-cycle_1` (with fig. tortoise_hare_proof) | no |

### Chapter 3: Stacks, queues and deques

| concept | § | source | locator | changed |
|---|---|---|---|---|
| stack | 3.1 | Wikipedia | `wikipedia:Stack_(abstract_data_type)` lead, #Non-essential operations, #Implementation, #Array, #Linked list | no |
| balanced-brackets | 3.1 | cpa | `cpa:combinatorics/bracket_sequences#balanced-bracket-sequences` | no |
| bracket-validation | 3.1 | cpa | `cpa:combinatorics/bracket_sequences#balance-validation` | no |
| queue | 3.2 | ODS | `ods:intro#the-queue-stack-and-deque-interfaces`: opening paragraph + FIFO paragraph + fig. queue | no |
| circular-buffer | 3.2 | ODS | `ods:arrays#sec:arrayqueue`, from "Notice that an ArrayStack is a poor choice" to "…does not exceed the size of a." | no |
| queue-linked-list | 3.2 | ODS | `ods:linkedlists#sec:sllist` subsection "Queue Operations" + the closing paragraph after thm:sllist | no |
| array-queue | 3.2 | ODS | `ods:arrays#sec:arrayqueue`, from the first code import (`ArrayQueue.a.j.n`) to the end of "Summary" | no |
| deque | 3.3 | ODS | `ods:intro#the-queue-stack-and-deque-interfaces`, Deque paragraph | no |
| array-deque | 3.3 | ODS | `ods:arrays#sec:arraydeque` (whole, with thm:arraydeque) | no |
| dual-array-deque | 3.3 | ODS | `ods:arrays#sec:dualarraydeque` (whole, with lem:dualarraydeque-amortized) | no |
| min-stack | 3.4 | cpa | `cpa:data_structures/stack_queue_modification` lead + #stack-modification | no |
| queue-from-two-stacks | 3.4 | cpa | `cpa:data_structures/stack_queue_modification#queue-modification-method-3` | no |
| monotonic-queue-minimum | 3.4 | cpa | `…#queue-modification-method-1` + `#queue-modification-method-2` | no |
| sliding-window-minimum | 3.4 | cpa | `…#finding-the-minimum-for-all-subarrays-of-fixed-length` | no |
| nearest-smaller-element | 3.4 | Wikipedia | `wikipedia:All_nearest_smaller_values` lead, #Example, #Sequential algorithm | no |
| largest-zero-submatrix | 3.4 | cpa | `cpa:dynamic_programming/zero_matrix` (whole article) | no |
| rpn-evaluation | 3.5 | cpa | `cpa:string/expression_parsing` lead + #reverse-polish-notation | no |
| expression-parsing | 3.5 | cpa | `cpa:string/expression_parsing#parsing-of-simple-expressions` | no |
| unary-right-assoc | 3.5 | cpa | `#unary-operators` + `#right-associativity` | no |
| rootish-array-stack | 3.6 | ODS | `ods:arrays#sec:rootisharraystack` through "Analysis of Growing and Shrinking", + "Summary" | no |
| rootish-index-math | 3.6 | ODS | `ods:arrays#sec:rootisharraystack` "Computing Square Roots" (lem:root) | no |
| sqrt-space-lower-bound | 3.6 | ODS | `ods:arrays#sec:rootishspaceusage` | no |
| space-efficient-list | 3.6 | ODS | `ods:linkedlists#sec:selist` through "Removing an Element", + "Summary" | no |
| selist-spread-gather | 3.6 | ODS | `ods:linkedlists#lem:selist-amortized` | no |

### Source counts

| chapter | counts | total |
|---|---|---|
| 1 | ODS 11 (1 provisional), Erickson 6, OI Wiki 3, brisk 3, OpenDSA 2, none 1 | 26 |
| 2 | Wikipedia 9, ODS 8, OI Wiki 6, cpa 3 | 26 |
| 3 | ODS 12, cpa 10, Wikipedia 2 | 24 |
| all | ODS 31, cpa 13, Wikipedia 11, OI Wiki 9, Erickson 6, brisk 3, OpenDSA 2, none 1 | 76 |

No doocs write-up won, so no explanation needs a twin exercise.

---

## Bridging sentences the builder will need (listed, not written)

Each one is an OmniStax lead sentence, AI-marked, under root rule 21.5. None of them
explains a concept; each supplies a name, notation or forward pointer that a kept-whole
winner leans on.

| id | where | what it must carry | why |
|---|---|---|---|
| B1 | 1.1 lead | if `jeffe:0.3` is carried: it is the worked example for `algorithm`; otherwise a pointer for 0.5's compass-and-straightedge mention (or include the 0.2 Compass subsection with lattice-multiplication) | ch01.md builder facts: 0.5 and 0.6 lean on 0.2 Compass and 0.3 |
| B2 | 1.4 lead | complexity-analysis analyses BottlesOfBeer, the multiplication algorithms and ApportionCongress from 1.1; its pseudocode counts from 1 | Erickson 0.6 |
| B3 | 1.6 lead | probability notation: brisk writes Pr(A), Pr(A\|B); ODS writes Pr{·} and E[·] | notation clash inside one section |
| B4 | 1.6 lead, before linearity | what a random variable is (a number determined by the random outcome) | ODS uses the term undefined; it is in the row's own name (item 4). **Needs the user (below).** |
| B5 | 1.1, interface-vs-implementation | map ODS's \chapref{arrays} and \chapref{linkedlists} to book §2.2 and §2.5–2.6 | a reference fix, not prose |
| B6 | 2.2 lead, before dynamic-array-cost | 1.5 analysed growth only, by three methods, writing m for the capacity and n for the size; ODS writes n and `a.length`, and adds shrinking at a.length ≥ 3n | notation clash with the 1.5 prerequisite (item 2) |
| B7 | 2.1 lead, before list-interface | stacks, queues and deques come in 3.1–3.3; the Deque mapping here is a preview | ODS's first sentence assumes the Queue subsection, which is chapter 3's |
| B8 | 2.2 lead | ArrayStack implements List; its name follows the naming rule at the end of 2.1's list-interface passage | ch02.md builder note |
| B9 | 2.3 lead, three-sum | the quadratic algorithm sorts first (sorting: ch. 10); the hash-table sentence points to ch. 5; the passage assumes distinct values | forward references in the 3SUM passage |
| B10 | 2.6 lead | ODS calls the singly linked list of 2.5 an SLList, with fields head, tail and n | DLList opening (item 5) |
| B11 | 3.2 lead, queue-linked-list | SLList (see 2.6); its pop() removes the head node, as in 3.1's linked-list stack; the closing paragraph's Deque is 3.3 | Queue Operations and closing paragraph (item 5) |
| B12 | 3.1 lead | 2.2's ArrayStack is an array-backed stack; Wikipedia's array pseudocode here is the same idea | ch03.md item 7 |
| B13 | 3.3 lead | "LIFO Queue" in the Deque paragraph means the stack of 3.1 (ODS's LIFO paragraph is not used) | ODS Deque paragraph |
| B14a | 3.3 lead, dual-array-deque | ODS's "potential method" here is 1.5's method used as a counter: each cheap operation raises Φ by at most 1, so the expensive balance() is paid for by the operations before it. Built (chapter 2–3 pass, worded as B14b): "The DualArrayDeque lemma's “potential method” is Section 1.5's method used as a counter: each call that does not rebalance raises Φ by at most 1, and so the calls before a costly balance() pay for it." | two uses of "potential" (item 10) |
| B14b | 3.6 lead, selist-spread-gather | the same, for Φ = the number of fragile nodes. Built: "The SEList proof's “potential method” is Section 1.5's method used as a counter: Φ is the number of fragile nodes, each add that does not spread raises it by at most 1, and so the adds before a spread pay for it." Both leads mark "method" `potential-method` and link Section 1.5's `#potential` | as B14a |
| B15 | 3.2 lead, circular-buffer | ODS's ArrayQueue resizes rather than bounding; the exercise's bounded buffer with overwrite is the fixed-size variant the row names | comprehensiveness gap (ch03.md) |
| B16 | 2.3 lead, sliding-window-fixed | the example is a running mean; in the exercises the window holds a sum or a count | ch02.md builder note |
| ~~B17~~ | ~~2.6 lead~~ | ~~DLList's Summary names Deque operations (3.3)~~ Struck in the chapter 2–3 pass: the pseudocode edition's Summary names no Deque operation (2.6's build), so no bridge is needed | forward reference |
| B18 | 3.2, 3.3, 3.6 | map ODS's \lemref{arraystack-amortized} and the "resize() of ArrayStack" mentions to book §2.2. Built (chapter 2–3 pass, one rule for the three): a `\lemref` prints as ODS prints it, "Lemma 2.1" (its own number, as a source's figure number stays as printed, RULES Cross-references), linked to the lemma's note, `/ch02/2.2/#arraystack-cost` (3.3; 3.6's "Lemma 2.3" is its own lemma, `#rootish-sqrt`); a "resize() of ArrayStack" mention wraps ODS's words in a link to `/ch02/2.2/#resize` (3.2 "the resize() operation of ArrayStack", 3.6 "a resize() operation on an ArrayStack" and "the ArrayStack.resize() operation") | reference fix; ch03.md item 3 is resolved, since the lemma is in 2.2 |

---

## Indexing convention each section lead must state

| § | convention | detail |
|---|---|---|
| 1.1 | **mixed** | Erickson's digit arrays are 0-based (X[0..m−1], digit i weighs 10^i); Pop[1..n] and Rep[1..n] in 0.3 are 1-based, if 0.3 is carried |
| 1.2 | none | log means log₂, ln is natural (ODS) |
| 1.3 | 0-based | ODS's loop examples (provisional with big-o); OpenDSA has no arrays |
| 1.4 | **mixed** | Erickson's complexity-analysis is 1-based (for i ← 1 to n, Pop[1..n]); ODS has no arrays |
| 1.5 | none | OI Wiki: n = number of elements and m = capacity in 势能分析; in 聚合分析, m is the full array's size and n the number of inserts |
| 1.6 | none | coin tosses and indicators are numbered i = 1..k (ODS) |
| 2.1 | 0-based | Wikipedia Array and ODS List x₀..x_{n−1}; Wikipedia's a₁₁ labels on a C array are an erratum note |
| 2.2 | 0-based | ODS a[0..n−1] |
| 2.3 | **mixed** | OI Wiki two-pointers and the variable window are 1-based (num[1..n], r − l + 1); Wikipedia 3SUM is 0-based (S[0..n−1]); merge has no indices; the moving average uses time subscripts p_{n−k+1}..p_n |
| 2.4 | 1-based | throughout, with a₀ = 0 and S₀ = 0 (OI Wiki's 规定 box, kept) |
| 2.5 | none | nodes and links |
| 2.6 | 0-based | ODS get(i), O(1 + min{i, n−i}) |
| 2.7 | none | step counts a, b, L |
| 3.1 | 0-based | Wikipedia stack, top starts at 0 |
| 3.2 | 0-based | ODS a[(j+n) mod a.length] |
| 3.3 | 0-based | ODS |
| 3.4 | **mixed** | cpa is 0-based (min over A[0..M−1], …, A[N−M..N−1]); Wikipedia's nearest-smaller-element is 1-based (A[1..n], sentinel A[0]) |
| 3.5 | none | tokens |
| 3.6 | 0-based | ODS blocks 0, 1, …; i2b(i) |

---

## Errata to attach as notes (all three files plus this pass)

These are notes on kept-whole text. The source words are not changed silently.

**Chapter 1**
1. ODS asymptotic notation, "O(a) ⊂ … ⊂ O(cⁿ), for any constants a,b,c > 0": c must be
   > 1. Provisional with big-o.
2. ODS asymptotic notation, "demonstrably different big-Oh running times… certain… faster":
   needs Θ. Provisional with big-o.
3. ODS rbs, "For a non-negative integer, k": the bound needs k ≥ 1.
4. ODS factorials: the integration variable is written n (a notation slip).
5. ODS coin-tosses lemma: it applies linearity to an infinite sum without noting that
   the terms are non-negative (a silent step; valid).
6. Erickson 0.3, Figure 0.5 (PDF p. 9): `Pop[i]/√2` should be `Pop[s]`; "n − R" and
   `for i ← 1 to n − R` should be R − n. Only if 0.3 is carried.
7. Erickson 0.6, "T(x, y) ≤ T(⌊x/2⌋, 2y) + 2": up to 4 operations per step (the O(log x)
   conclusion stands).
8. Erickson 0.6, "The Census Bureau implements the priority queue as an *unsorted* array"
   contradicts 0.3's "the Census Bureau uses a sorted array, stored in a single column of an
   Excel spreadsheet, which is recalculated from scratch at every iteration" (worded so in
   1.4's note, which links back to 1.1's block).
9. Erickson 0.6, "twice much time": missing "as".
10. OpenDSA AnalLower, "the upper and lower bounds always meet": contradicted by its own
    footnote example.
11. brisk counting: the printed digits of 52! are right in their first thirteen digits
    (80,658,175,170,94…) and wrong from the fourteenth on (corrected in the chapter 1 pass;
    1.6's note had it right).
12. brisk probability, "total number of events": should be outcomes.
13. brisk "Pr(Sonic) = 1500/…": the numerator should be 1000. Only if #Total probability
    is added; it is not in the locator.
14. OI Wiki amortized-analysis: m means the array size in 聚合分析 and the capacity in
    势能分析 (a notation note, new in this pass).

**Chapter 1, found while building (added in the chapter 1 pass, 2026-11-09)**

32. Erickson 0.6, "some underlying data structure of subroutine": should be "or" (1.4,
    note `err-or`).
33. brisk probability, "Pr(P) = .7" names the event that a rock singer wins *P*; from the
    next paragraph on, and in its Figure 4.1, it is *R* (1.6, note `err-p-r`).
34. brisk counting exercise (costume): the key's 300 counts skipping all three items; read as
    "keep at least one" it is 299 (1.6, note `err-costume`).

**Chapter 2**

15. Wikipedia Array, ===One-dimensional arrays===: "B + 30c" should be "B − 30c". (2.1, `err-rebase`)
16. Wikipedia Array, ===Multidimensional arrays===: 1-based labels a₁₁, a₁₂ on a 0-based
    C array. (2.1, `err-a11`)
17. Wikipedia Pointer, "declared obsolescent as of C29": unverifiable from the cache, and
    the next C revision's working name is C2y. Needs a human check. 2.1's build read Wikipedia's
    "C29 (C standard revision)" (revision 1382563440), which supports the sentence; it stands
    unnoted. A person should still read WG14 N3517 (open-std.org is refused by the proxy).
18. Wikipedia Pointer #Multiple indirection, the comment "where all earlier elements have
    lesser or equal value": loose; the code is a correct sorted insert. (2.5, `err-sorted-comment`)
19. ODS `lem:arraystack-amortized`, "at least n_i/2": the bound proved is n_i/2 − 1. (2.2, `err-half`)
20. OI Wiki prefix-sum 2D example: the terms read S_{2,3} + S_{3,2} but the numbers are
    listed as 18 + 15. Per the figure, S_{2,3} = 15 and S_{3,2} = 18. The sum is
    unaffected (2.4, `err-2d-example`, worded: "The numbers are listed in the other order
    from the terms: by the figure, S2,3 = 15 and S3,2 = 18. The sum, 29, is right.").
21. Wikipedia Moving average: the locator stops before the confused "k = n" sentence (2.3:
    the block is cut after "…and only 3 arithmetic steps.", so no note).

**Chapter 3**

22. ODS DualArrayDeque prose, `front.add(front.size()-i-1,x)`: the code is
    `front.size()-i`. (3.3, `err-front-add`)
23. ODS DualArrayDeque lemma, "a technique knows as": should be "known as" (new in this
    pass, `arrays.tex` line 596). (3.3, `err-knows`)
24. ODS ArrayQueue theorem, "m add(i,x) and remove(i) operations": the Queue has add(x)
    and remove(). (3.2, `err-theorem-ops`)
25. ODS ArrayQueue prose, resize to "size 2n": the code uses max(1, 2n). (3.2, `err-resize-size`)
26. ODS ArrayDeque, "shift the elements a[0],…,a[i−1] left": means list positions, not
    raw slots (harmless). (3.3, `err-positions`)
27. ODS RootishArrayStack space usage, "wasting at least in √n": a typo. (3.6, `err-wasting`)
28. cpa zero_matrix step 1, d[i][j] "from 0 to i − 1": the code includes row i. (3.4, `err-d-row`)
29. cpa queue-from-two-stacks: the minimum on an empty queue reads `s2.top()`, which is
    undefined. An edge case for the exercise. (3.4, `err-empty-min`)
30. cpa unary operators: unary priority above `^` gives −2^2 = 4. An exercise must not
    combine the two. (3.5, `err-unary-pow`)
31. cpa C++ negating a `char` to flag unary operators: implementation-defined where `char`
    is unsigned. Matters only for the C++ pass. Not noted (3.5's config).

**Chapters 2 and 3, found while building (added in the chapter 2–3 pass, 2026-11-09)**

35. cpa zero_matrix, "d[i], i = 1...m − 1" for the array of the stack step: it is indexed by
    the column, d[j] for j = 0, …, m − 1, as the code's `vector<int> d(m, -1)` declares it
    (3.4, `err-d-index`; numbered 35 by 3.4's builder).
36. ODS Exercise 2.5 (rotate), the index set "{0, …, a.length}": the last index of a is
    a.length − 1 (2.1, `err-rotate`, in the card's prompt).
37. Wikipedia Stack, Array implementation, "top … the number of items pushed so far": top
    counts the items on the stack now, the number pushed less the number popped, which is
    also the cell the next push writes to (3.1, `err-top`).
38. ODS Figure 2.2's caption, "add(x) and remove(i) operations": the calls drawn are add(x)
    and remove(), the Queue's operations (3.2, `err-caption-ops`, through the figure row's
    `figure` field).
39. (26b) ODS ArrayDeque, "shift … min{i, n − i}": holds where n/2 is the real quotient, as in
    the prose, Figure 2.3 and the Python listing; ODS's Java and C++ divide n by 2 in whole
    numbers and, for odd n and i = (n − 1)/2, shift (n + 1)/2 elements, one more than
    min{i, n − i} (3.3, `err-half`).
40. (26c) ODS Figure 2.4's prose, "remove(x)": the operation is remove(i), as the figure's own
    caption says (3.3, `err-remove-x`).
41. ODS Figure 3.5(b) (SEList remove, Case 2): with b = 3 its three blocks of b − 1 = 2
    elements are b such blocks, so remove(1) finds Case 3 and gathers; Case 2 needs the end of
    the list within b − 1 blocks (3.6, `err-case2`).
42. ODS FastSqrt `inittabs()` as printed: tables of 2^(r/2) = 2^14 entries for r = 29, but
    sqrt(x) reads sqrttab at xp >> (r/2), up to 2^16 − 1, and the text speaks of tables of size
    2^16, as ODS's working code builds them; the C++ `1<<d+k` parses as 1 << (d + k) (3.6,
    `err-inittabs`).

Every correction note of chapters 1–3 is in this list under its number (chapters 2–3: 15,
16, 18–20, 22–30 and 35–42; 17, 21 and 31 carry no note, as their items say).

---

## Translation list (OI Wiki, `docs/prompts/translate.md`, AI-marked)

The word estimates use about 0.6 English words per CJK character, with code fences
excluded and formulas extra. The chapter 2 figures are ch02.md's own.

| § | concept | locator | CJK chars | ≈ English words |
|---|---|---|---|---|
| 1.5 | amortized-analysis | basic/amortized-analysis 引入 + 内容 + 聚合分析 | 245 + 113 + 307 = 665 | 400 |
| 1.5 | aggregate-accounting | 记账分析 + 扩展示例 intro + 聚合分析法 + 记账分析法 | 331 + 113 + 176 + 181 = 801 | 480 |
| 1.5 | potential-method | 势能分析 + 原理 + 示例 + 堆栈 势能分析法 | 99 + 317 + 286 + 191 = 893 | 540 |
| 2.3 | two-pointers | misc/two-pointer 引入 + 利用序列有序性 (过程) | 131 + 428 | 330 |
| 2.3 | sliding-window-variable | 维护区间信息 opening + 例题 1 过程 | ≈582 | 340 |
| 2.4 | prefix-sums | basic/prefix-sum 引入 + 前缀和 + 一维前缀和 | ≈270 | 200 |
| 2.4 | prefix-sums-2d | 基于容斥原理 + 逐维前缀和 | — | 550 |
| 2.4 | difference-array | 差分 opening + 一维差分 | — | 250 |
| 2.4 | difference-array-2d | 二维/多维差分 | — | 160 |
| | **total** | 9 passages | | **≈3,250** (ch. 1 ≈1,420; ch. 2 ≈1,830) |

Chapter 3 needs no translation.
- **Code is link-only.** OI Wiki's README excludes 代码部分 (the code parts) from the
  licence. That includes the ```text credit-trace block in 记账分析: redraw it from the
  numbers in the prose, or confirm its status first.
- **例题 boxes.** Those that restate LeetCode statements become links.
- **SATA.** The attribution thanks the authors, and a person stars the repo from the
  owner's account.

---

## Concept-map corrections

**Found by the finder runs:**
1. `probability-basics`: `open_prose` false → true. Open candidates: brisk (the winner),
   mcs2018, aspnes-202, aspnes-469, appcomb, openintro-stats, Wikibooks, Wikipedia, OI
   Wiki (dossiers/ch01.md 1.6 and Gaps). The toc.md 1.6 "(no open prose)" mark goes.
2. `conditional-probability`: the same correction, with the same set of sources
   (winner brisk).
3. `pointer-arithmetic`: `open_prose` false → true. Eight open passages; the winner is
   Wikipedia Pointer #C arrays (dossiers/ch02.md Gaps). The toc.md 2.1 mark goes.
4. `pointer-to-pointer`: `open_prose` false → true. Wikipedia Pointer #Multiple
   indirection is exactly the list-head case. The toc.md 2.5 mark goes.
5. `jeffe:0.2` "Compass and Straightedge" has no concept row, though jeffe 0.5 refers
   to it (dossiers/ch01.md). Either add a row or leave it as context (bridge B1).

**Confirmed unchanged by the finder runs:**
- `implement-vector`: stays "no open prose" (implementations only). The ch02.md
  explanation is the ArrayStack code; the row's notes could say so.
- `counter-increment-decrement`: stays "no open prose" (only jeffe-notes 9.3, NC).

**Added by this pass (stale after judging, not finder findings):**
- toc.md "Sources" lines that omit a winning source:
  - 1.5 lacks oiwiki;
  - 1.6 lacks brisk;
  - 2.5 lacks wikipedia;
  - 3.1 lacks wikipedia;
  - 3.2 and 3.3 lack nothing.
- `potential-method` lists `ods:arrays#lem:dualarraydeque-amortized` as a treatment.
  That passage is now `dual-array-deque`'s, so a note on the row would stop a later run
  from picking it twice.
- `queue-linked-list` lists only ciu and wikibooks treatments. The winner is ODS SLList
  "Queue Operations".

---

## ESCALATE

None new. `big-o` (ODS against aspnes-223) is with the second judge, and either outcome
moves no other winner (item 12).

## For the user

1. **The random-variable definition (B4).** No chapter 1 winner defines "random
   variable", a term in the name of `linearity-of-expectation`.
   - Recommended: a one-sentence, AI-marked definition in the 1.6 lead.
   - The only source-based fix is to move linearity and indicators to MCS 19.1/19.4/19.5.
     It is blocked: indicators is "clearly better" ODS, and MCS's notation clashes.
   - A ruling is needed on whether a section lead may define a term in that way.
2. **The dsa-dummies provenance ruling** is still pending. It affects no winner here; it
   appears only low in the ranked lists.
3. **Erickson 0.3.** Carry it as the worked example for `algorithm`, or not? B1, B2 and
   erratum 6 depend on it. ch01.md calls it a builder decision; it is listed here because
   it decides how much Erickson the book holds.
4. **Carried over, for the orchestrator rather than the user:**
   - doocs code without a twin (0713, 0304, 0370) for the OI Wiki 2.3 and 2.4 winners,
     or AI-written code;
   - chapter 3's cached references, still not run (ch02.md showed they can be);
   - the ODS Python port for the runners;
   - the human check on Wikipedia's "C29";
   - starring the OI Wiki repo (SATA).

---

## Rulings applied 2026-11-08

The user's rulings on this file (METHOD §4.4 item 18), applied to the concept map in
`tools/map/map.spec`, `inventory/gap.json` and `inventory/ods.json`; the map was rebuilt and
`tools/check_map.py` passes. The tables above are left as they were.

1. **random-variable → mcs2018.** A new concept in 1.6 (definition, Essential), placed
   before `linearity-of-expectation`, which now rests on it, as do `las-vegas-monte-carlo`
   and `linear-probing-analysis`.
   - Locator: `mcs2018:19.1`, from Definition 19.1.1 ("A random variable R on a
     probability space is a total function whose domain is the sample space.", PDF p. 857;
     `mcs-2018.txt` line 38724) through 19.1.1 Indicator Random Variables and 19.1.2
     Random Variables and Events, ending before §19.2 Independence. The chapter 19 opening
     paragraph may lead in. Checked against `sources/_cache/mcs2018/`. The cached text
     renders "=" as "D", so quote from the PDF.
   - B4 is settled by the concept, not by a lead sentence. B3 gains MCS's notation
     (Pr[·], [C = 2] for an event) beside brisk's Pr(·) and ODS's Pr{·} and E[·]. Indexing
     for 1.6 stays "none".
   - The other open treatments recorded for the judge as gap rows: `wikibooks:Probability/Random_Variables#Definition`,
     `aspnes-202:12.2`, `aspnes-469:3` (chapter opening), `wikipedia:Random_variable`,
     `openintro-stats:3.4`, `appcomb:s_probability_discrete-random-variables`,
     `oiwiki:math/probability/random-variable#随机变量`. brisk has no random-variable passage.
2. **Erickson §0.3 kept whole as `algorithm`'s worked example.** B1 takes its first
   branch. B2 and erratum 6 apply, and the 1.1 "mixed" indexing (Pop[1..n], Rep[1..n])
   stands. 0.2 "Compass and Straightedge" gets **no concept row**: it is an aside on
   Euclid's constructions that no exercise would test on its own and no interview asks
   about. 0.5's mention of it is handled by carrying the subsection with
   `lattice-multiplication`'s 0.2 block (same source and section, kept whole) or by a
   one-sentence bridge. That is the builder's call, recorded in the note on
   `describing-algorithms`.
3. **doocs code is allowed without a twin exercise.** The twin rule covers doocs
   explanations only, and no doocs explanation won. The three chapter 2 concepts that
   had no open code take doocs code (CC BY-SA 4.0, credited to doocs/leetcode). The code
   is in each problem's `README_EN.md` under `sources/_cache/doocs-leetcode/solution/`.
   The cache has no separate `Solution.*` files.

   | concept | winner (prose) | doocs code | block |
   |---|---|---|---|
   | sliding-window-variable (the product window, OI Wiki 例题 1) | OI Wiki | `0700-0799/0713.Subarray Product Less Than K/README_EN.md` | "Solution 1: Two Pointers", Python3 and JavaScript |
   | prefix-sums-2d | OI Wiki | `0300-0399/0304.Range Sum Query 2D - Immutable/README_EN.md` | "Solution 1: Two-dimensional Prefix Sum", Python3 and JavaScript |
   | difference-array | OI Wiki | `0300-0399/0370.Range Addition/README_EN.md` | "Solution 1: Difference Array" (not Solution 2, the Fenwick version), Python3 and JavaScript |

   - The three named files are kept. 0713 is the problem OI Wiki's own example works.
     0370 is the bare template for 一维差分, while 1094 and 1109 wrap the same update in a
     story, and 1109 is 1-based.
   - The Python blocks assume LeetCode's implicit imports (`List`; `accumulate` in 0370).
     Add them when the code is run, isolated as ruling 17 says.
   - The doocs code is 0-based. Section 2.4's OI Wiki text is 1-based with S₀ = 0. 0304
     pads its table to (m+1)×(n+1), and 0370 writes `d[r + 1]`. The 2.4 lead should name
     the shift.
4. **dsa-dummies excluded (no winner affected).** Its three gap rows are gone, from
   two-pointers, sliding-window-fixed and prefix-sums. Each of those concepts keeps
   other open prose. The map scripts now treat any registry row with an `excluded` field
   as not open, and `check_map.py` fails on a treatment from one. The "pending a
   provenance ruling" line under **Rules applied** is settled.

**Concept-map corrections applied** (from the section above): probability-basics,
conditional-probability, pointer-arithmetic and pointer-to-pointer have `open_prose: true`
from the treatments the dossiers name, so their "(no open prose)" marks are gone. Every
chapter 1–3 winner is now among its concept's treatments, so the toc "Sources" lines name
oiwiki in 1.5, brisk in 1.6 and wikipedia in 2.5 and 3.1. The winners for
multivariate-big-o (OpenDSA AnalMultiple), nearest-smaller-element (Wikipedia) and
queue-linked-list (ODS SLList "Queue Operations", new row `ods:sllist-queue`) were added
too. potential-method and queue-linked-list carry the notes this file asked for.
implement-vector and counter-increment-decrement still have no open prose.
