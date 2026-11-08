# Concept map report

Built from the eight inventories in `inventory/` (1301 rows, 136 of them in the gap inventory `inventory/gap.json`). Output: one book of **45 numbered chapters** and **239 sections**, plus two appendices that are not built as text: **Appendix A · Computer systems** (19 curated-links pages, 62 concepts) and **Appendix B · Getting the job** (one reading page, no concepts). **1022 concepts** in all. `python3 tools/check_map.py` passes (0 errors, 0 warnings; no tier inversions remain).

## 1. Counts

### Concepts per chapter range and appendix

Per-chapter counts are in `toc.md` (each chapter heading) and `toc.json` (`tier_counts`).

| Chapters | Sections | core | stretch | contest | total |
|---|---:|---:|---:|---:|---:|
| 1–7 (Algorithms and their cost … Bits and data representation) | 37 | 104 | 30 | 7 | 141 |
| 8–12 (Trees and binary search trees … Tries and other search structures) | 26 | 49 | 46 | 7 | 102 |
| 13–16 (Graphs and graph search … Disjoint sets and minimum spanning trees) | 19 | 39 | 20 | 3 | 62 |
| 17–23 (Backtracking … Lower bounds and intractability) | 35 | 62 | 55 | 25 | 142 |
| 24–29 (Approaching a system design question … Worked designs) | 27 | 86 | 19 | 0 | 105 |
| 30–45 (Range queries … Computational geometry: algorithms) | 95 | 7 | 136 | 265 | 408 |
| **Chapters 1–45** | 239 | **347** | **306** | **307** | **960** |
| Appendix A · Computer systems (links, not built) | 19 pages | 36 | 26 | 0 | 62 |
| **All** | | **383** | **332** | **307** | **1022** |

First build pass: chapters 1. Algorithms and their cost, 2. Arrays and linked lists, 3. Stacks, queues and deques.

Chapter sections by tag: 110 core, 70 stretch, 59 contest; Appendix A pages: 12 core, 7 stretch. Section sizes (concepts: sections): 1: 6, 2: 39, 3: 66, 4: 58, 5: 50, 6: 22, 7: 10, 8: 7.

Kinds: result 453, skill 238, definition 214, idea 116, axiom 1.

### Merging

- 1301 rows in, 5 dropped, 7 rows split over two concepts each, so 1303 treatments in 1022 concepts.
- **192 merged clusters** (concepts with more than one treatment); 188 of them join different sources, the other 4 join two rows of one source. Cluster sizes: 130 with 2 rows, 43 with 3 rows, 14 with 4 rows, 2 with 5 rows, 3 with 6 rows; 830 concepts have one treatment.
- Source combinations in cross-source clusters: ciu + ods (26), cpa + jeffe (16), ciu + cpa (16), ciu + cpa + jeffe (11), ciu + sdp (10), ciu + opendsa + wikipedia (8), ciu + jeffe (8), ciu + wikipedia (8), cpa + notes (8), ciu + notes (6), ciu + wp (6), notes + ods (5), ciu + notes + ods (4), ciu + cpa + notes (4), cpa + ods (3), ciu + jeffe + ods (3), ciu + notes + opendsa + wikipedia (2), notes + wikipedia (2), doocs + wikipedia (2), jeffe + ods (2), ciu + cpa + ods (2), doocs + icc (2), aosa + ciu (2), ciu + dmoi3 + oiwiki (1), ciu + wikibooks + wikipedia (1), doocs + dsa-dummies + oiwiki (1), doocs + dsa-dummies + wikipedia (1), doocs + icc + oiwiki (1), doocs + dsa-dummies + oiwiki + wikipedia (1), doocs + oiwiki + wikipedia (1), doocs + oiwiki (1), ciu + opendsa (1), algo-expl + cpa + oiwiki + wikipedia (1), ciu + wikibooks (1), cpa + doocs + oiwiki + wikipedia (1), csci30 + notes (1), ciu + notes + wikipedia (1), ciu + lt-csbu (1), ciu + jeffe + notes (1), ods + wikipedia (1), ciu + cpa + notes + ods (1), ciu + notes + opendsa (1), jeffe + ods + sdp (1), ciu + cpa + jeffe + ods (1), aspnes + cpa + mcs2018 (1), doocs + icc + oiwiki + opendsa + wikipedia (1), doocs + icc + trekhleb + wikipedia (1), anfp + doocs + icc + wikipedia (1), algo-expl + doocs + icc (1), dmoi3 + doocs + trekhleb + wikipedia (1), anfp + doocs + jeffe + wikipedia (1), ciu + raft-site + wp (1), ciu + notes + wp (1), notes + wp (1), cpa + wikipedia (1).
- Concepts each source treats: cpa 515, ciu 208, ods 113, sdp 113, jeffe 112, notes 102, wikipedia 38, doocs 21, opendsa 13, oiwiki 10, wp 9, icc 7, dsa-dummies 3, dmoi3 2, wikibooks 2, algo-expl 2, trekhleb 2, anfp 2, aosa 2, csci30 1, lt-csbu 1, mcs2018 1, aspnes 1, raft-site 1.
- Hasse reduction removed 106 redundant prerequisite edges; 1329 edges remain.

Rows split over two concepts (a source row whose grain was coarser than "an exercise could test it alone"):

- `ciu:universal-perfect-hashing` → Universal hash families, Perfect hashing (two-level)
- `ciu:bst-search-insert` → BST search and successor search, BST insertion
- `ciu:linear-time-sorts` → Counting sort, Radix sort
- `ciu:union-find-optimisations` → Union by size / rank, Path compression
- `cpa:classic-dp-problems` → Classic DP problems, Longest common subsequence
- `ciu:apsp-dp` → Floyd-Warshall algorithm, APSP by dynamic programming on path length
- `ciu:convex-hull` → Convex hull, Graham's scan

### Dropped rows

| Row | Name | Reason |
|---|---|---|
| `ciu:os-courses` | Operating systems course material | Pointer row for course-length OS lectures; CIU's own note says it is not a single concept. Its links stay available to the side panel of the processes and virtual-memory sections. |
| `ciu:real-world-architectures` | Real-world architecture case studies | Reading list (27 links, "pick a few"), not a concept; candidate references for the worked-designs chapter. |
| `ciu:discrete-math` | Discrete mathematics | Course-length links only; the discrete-math content it points at is covered by counting, induction and probability concepts. |
| `ciu:devops` | DevOps | One reading-list link and a one-line definition; nothing an exercise could test. |
| `ciu:sd-exercises` | System design practice problems | List of practice prompts (unique IDs, key-value store, picture sharing, recommender, URL shortener, cache); the URL shortener and cache are sdp worked designs, the rest are gaps. |

No other row was dropped. ODS's implementation-variant classes (DualArrayDeque, RootishArrayStack, SEList, SkiplistList, XFastTrie, YFastTrie, scapegoat trees) stay as stretch or contest concepts, since each teaches an idea (amortised rebuilding, sqrt-space blocks, indexing by skiplist widths).

## 2. Gaps

### Interview topics no inventory teaches

**Filled by the gap inventory (2026-11-08).** The finder's targeted run (`dossiers/gap-patterns.md`) found open treatments for the interview patterns this table used to list first, and `inventory/gap.json` records them, one row per treatment. They are 22 new concepts: Two pointers (2.3, core); 3SUM in quadratic time (2.3, core); Merging two sorted lists (2.3, core); Fixed-size sliding window (2.3, core); Variable-size sliding window (2.3, core); Prefix sums (2.4, core); Two-dimensional prefix sums (summed-area table) (2.4, stretch); Difference arrays (2.4, core); Two-dimensional difference arrays (2.4, stretch); Kahn's algorithm (14.2, core); Generating all permutations by backtracking (17.2, core); Next permutation in lexicographic order (17.2, core); Heap's algorithm (17.2, stretch); Generating all subsets (17.2, core); Generating k-combinations by backtracking (17.2, core); Coin change: fewest coins by DP (18.3, core); Coin change: counting the ways (18.3, core); Counting grid paths (18.3, core); Counting grid paths around obstacles (18.3, core); Minimum path sum in a grid (18.3, core); Merging overlapping intervals (20.2, core); Interval partitioning: minimum rooms as maximum overlap (20.2, core). Where a gap topic matched a concept the map already had, the new treatments joined it instead: interval scheduling (Erickson 4.2, 20.1), the sliding-window minimum (3.4), tortoise and hare (2.7), three-way partition as the Dutch national flag (10.4), topological order (14.2, the MCS and Aspnes existence proofs) and next k-combination (40.5). The bracketed prerequisites [prefix sums] and [difference array] now resolve to the new concepts, so Fenwick trees, sqrt decomposition, the prefix-minimum maximum subarray and the Fenwick range update rest on chapter 2.

The topics below are still not in the map, because no inventory row teaches them (the rule: never invent a concept). Each is a job for the resource finder (METHOD §6).

| Topic | Tier it would get | Evidence |
|---|---|---|
| Modular arithmetic basics | core | Assumed by 8 cpa rows (modular exponentiation, inverses, congruences, string hashing); taught nowhere. |
| Longest palindromic subsequence | core | No row; the gap run covered coin change and grid paths only. |
| Subarray sums with a hash map (count subarrays summing to k) | core | doocs 0560 treats it (gap-patterns §4), but it was outside this gap run's topic list and has no row yet. Its home would be chapter 5, resting on prefix sums (2.4) and hash tables. |
| Object-oriented programming basics | core | Assumed by CIU's design patterns and SOLID rows and by sdp's OOD notebooks. |
| Memory and pointers | core | Assumed by CIU arrays and linked lists. |
| Rate limiting | stretch | METHOD §0 already names it; the primer has no section. |
| Unique ID generation | stretch | Only a prompt in CIU's dropped practice list (`ciu:sd-exercises`). |
| MapReduce as a concept | stretch | sdp's worked designs use it (`mapreduce-aggregation` assumes it) but nothing defines it. |
| Queueing (Little's law, utilisation and latency) | stretch | sdp's back pressure links it as further reading only; METHOD §2.4 wants a sim for it. |

One bridge concept **was** added because an inventory names it: **Longest common subsequence** (18.7), split out of cpa's classic-DP table (`cpa:classic-dp-problems`, alias "LCS"). Its only treatment is that table row, so it counts as open prose but has no article behind it: treat it as a prose gap too.

Other assumed knowledge that no row teaches (bracketed prerequisites in the inventories, contest-tier mostly): Boolean formula in CNF, Cramer's rule, DCEL, DFA, Wilson's theorem, birthday paradox, bitmask DP, circles, complex numbers, coordinate geometry, definite integrals, derivatives, determinant, divisibility, equivalence relations, finite automaton, intermediate value theorem, linear independence, matrices, matrix multiplication, multinomial theorem, permutation inversions, pigeonhole principle, planar graphs, prefix products, prime numbers, quad-edge data structure, sets, systems of linear equations, triangulation. Each affected concept says so in its notes ("Assumes, untaught in the map").

### Concepts with no open prose

**Before the gap inventory, 189 concepts had no open prose; 39 of them now have some**, from treatments the finder sweeps listed (`dossiers/sweep-dsa.md`, `sweep-system-design.md`, `gap-patterns.md`) and that were added to `inventory/gap.json` with locators checked against the source caches: Big-Omega and Big-Theta (1.3); Amortized analysis (1.5); Summation, taxation and charging methods (1.5); Factorials, permutations and combinations (1.6); Array (2.1); Implement a linked list (2.5); Queue on a linked list with a tail pointer (3.2); Tail recursion (4.1); The axiom of induction and strong induction (4.3); Hash table (5.1); Table doubling (5.2); Universal hash families (5.4); Cuckoo hashing (5.6); Floating-point representation (7.5); Tree (8.1); Inorder successor in a BST (8.4); Balanced search trees (the general idea) (8.6); Sift up and sift down (9.2); Stability in sorting (10.1); Selection sort (10.1); Insertion sort (10.1); Bubble sort (10.1); AVL tree (11.1); 2-3 search tree (11.1); Splay tree (11.4); K-ary tree (11.6); Trie prefix operations and performance (12.1); Graph representations (13.2); Fallacies of distributed computing (25.1); Consensus: Paxos and Raft (25.2); Scaling a web service: clones, databases, caches, asynchrony (26.3); Consistent hashing (27.3); Distributed hash tables (27.3); NoSQL patterns (27.4); Redis as an in-memory data store (28.1); Bloom filters (36.1); Count-min sketch (36.2); HyperLogLog (36.2); Locality-sensitive hashing (simhash) (36.3). The open-prose sources are those whose licence passes METHOD §0 or METHOD §4.4 items 12 and 15: `algo-explanation`, `anfp`, `aosa`, `appcomb`, `aspnes-202`, `cpa`, `csci30`, `dmoi3`, `doocs-leetcode`, `dsa-dummies`, `holden-acs`, `icc`, `jeffe`, `lt-csbu`, `mcs2018`, `ods`, `oiwiki`, `opendsa`, `raft-site`, `sdp`, `trekhleb-jsalgo`, `wikibooks`, `wikipedia`, `wp-sysdesign`.

**150 concepts** are still taught only by CIU links or by Erickson's NC notes (63 core, 55 stretch, 32 contest). Their prose needs the finder. Whole sections with no open source at all are marked "open prose: none" in toc.md (13 chapter sections; 15 of Appendix A's 19 pages, which is expected for a links appendix).

- **1. Algorithms and their cost** (3; notes only 2, ciu only 1): Incrementing and decrementing counters; Basic probability [core]; Conditional probability and independence [core]
- **2. Arrays and linked lists** (3; ciu only 3): Indexing by pointer arithmetic [core]; Implement a vector [core]; Pointer to pointer [core]
- **4. Recursion and induction** (3; notes only 3): Proof by smallest counterexample [core]; Induction on numbers, summations and tilings [core]; Induction on recursive functions and trees [core]
- **5. Hash tables** (3; notes only 3): Perfect hashing (two-level) [core]; Expected chain length under universal hashing [core]; Balls and bins: maximum chain length
- **6. Binary search** (1; ciu only 1): Implement binary search, iteratively and recursively [core]
- **7. Bits and data representation** (3; ciu only 3): Branch-free bit tricks [core]; Endianness [core]; Unicode and character encodings [core]
- **8. Trees and binary search trees** (3; ciu only 3): BST minimum, maximum and height [core]; Checking whether a binary tree is a BST [core]; Implement a BST [core]
- **9. Heaps and priority queues** (1; ciu only 1): Implement a max-heap [core]
- **10. Divide and conquer and sorting** (9; notes only 7, ciu only 2): Solving recurrences by guess and confirm [core]; The Akra-Bazzi method; Linear recurrences by annihilators; Sorting linked lists versus arrays [core]; The nuts and bolts problem; Implement merge sort and quicksort [core]; Decision-tree lower bounds [core]; Information-theoretic lower bound [core]; Reductions to and from sorting
- **11. Balanced search trees** (3; notes only 3): Random priorities give expected logarithmic depth; Lazy deletion and global rebuilding; Rotations, double rotations and splaying
- **12. Tries and other search structures** (4; ciu only 4): Ternary search trie [core]; van Emde Boas trees; Augmenting data structures; k-d tree
- **13. Graphs and graph search** (1; ciu only 1): Implement BFS and DFS on both representations [core]
- **15. Shortest paths** (1; ciu only 1): A* search
- **16. Disjoint sets and minimum spanning trees** (1; notes only 1): Shallow threaded trees
- **18. Dynamic programming** (2; ciu only 2): Recognising a DP problem [core]; RNA secondary structure [core]
- **20. Greedy algorithms** (2; notes only 2): Matroids and the greedy algorithm; Scheduling unit jobs with deadlines
- **21. String searching** (3; notes only 2, ciu only 1): Brute-force substring search [core]; Boyer-Moore (and Horspool) [core]; String matching with a finite-state machine [core]
- **22. Probability and randomized algorithms** (12; notes only 9, ciu only 3): Common distributions: uniform, Bernoulli, binomial, geometric; Removing bias from coin flips; Coupon collecting (Pokemon collecting); Deterministic vs. randomized algorithms; expected running time; Generating random permutations (shuffling) [core]; Markov's inequality; Chebyshev's inequality; Chernoff bounds; Treap depth with high probability; Markov chains [core]; Random walks; Markov text generation
- **23. Lower bounds and intractability** (16; notes only 13, ciu only 3): Finding the maximum needs n-1 comparisons; Adversary arguments; Finding the minimum and maximum: ceil(3n/2) - 2; Evasive graph properties; Polynomial-time reductions [core]; Recognising NP-complete problems in disguise [core]; Approximation algorithms and ratios [core]; Greedy load balancing; Vertex cover approximation; Greedy set cover and hitting set; Traveling salesman: hardness and metric approximation; k-center clustering; An FPTAS for subset sum; Fixed-parameter algorithms [core]; Faster exponential algorithms for 3SAT; Faster exponential algorithms for maximum independent set
- **27. Databases** (1; ciu only 1): Database normalisation
- **29. Worked designs** (1; ciu only 1): Distributed graph algorithms
- **32. Network flow and matching** (4; notes only 4): Unbalanced flows: supplies and demands; Pseudoflows and augmenting between imbalances; Minimum-cost circulations and cycle canceling; Node potentials and reduced costs
- **33. More graph algorithms** (2; notes only 2): Karger's contraction algorithm; Karger-Stein recursive contraction
- **35. Advanced dynamic programming** (7; notes only 7): Total monotonicity and the SMAWK algorithm; Saving space by divide and conquer (Hirschberg); Saving time with sparseness; The Four Russians speedup; DFA minimization by dynamic programming; NFA acceptance and regular-expression matching; Context-free parsing (CYK)
- **36. Sketches and probabilistic data structures** (1; notes only 1): The streaming model
- **42. Linear algebra, polynomials and the FFT** (2; notes only 2): Polynomial representations; Converting by Vandermonde matrices
- **43. Numerical methods and optimisation** (9; notes only 9): Linear programming; The geometry of linear programs; Formulating problems as linear programs; Linear programming duality; Complementary slackness; The simplex algorithm; Network simplex; Linear expected time in fixed dimension; LP rounding for weighted vertex cover
- **Appendix A, Computers and operating systems** (15; ciu only 15): CPU components: ALU, registers and RAM [core]; How a CPU executes a program [core]; Memory hierarchy and CPU caches [core]; Building a computer from logic gates; How a compiler works; Compiler optimisation; Garbage collection; Processes versus threads [core]; Interrupts and context switching [core]; Paging, segmentation and virtual memory [core]; Fork and copy-on-write [core]; Locks, mutexes, semaphores and monitors [core]; Deadlock and livelock [core]; Concurrency in Python and the GIL [core]; Parallel programming
- **Appendix A, Networking** (6; ciu only 6): OSI and TCP/IP models [core]; Subnetting and CIDR notation [core]; TCP versus UDP [core]; Socket programming [core]; TLS and HTTPS [core]; Serialisation formats [core]
- **Appendix A, Software engineering practice** (16; ciu only 16): Unit testing [core]; Mock objects [core]; Integration testing [core]; Dependency injection [core]; Test-driven development [core]; UML class diagrams [core]; Creational design patterns [core]; Structural design patterns [core]; Behavioural design patterns [core]; Single responsibility principle; Open/closed principle; Liskov substitution principle; Interface segregation principle; Dependency inversion principle; Using vi(m) and Emacs; Unix command-line tools
- **Appendix A, Information, coding and security** (12; ciu only 12): Information theory [core]; Entropy; Parity bits; Hamming code; Lossless compression; LZ77; Cryptographic hash functions [core]; Encryption; Threat models and privilege separation; Control hijacking and buffer overflows; Web security model; Network security and side channels

Most of the CIU-only concepts are in Appendix A (operating systems, networking basics, testing, design patterns, security), which is now a curated links appendix: its pages need good links, not open prose. Among the numbered chapters the heaviest gaps are the probability, adversary and approximation chapters, whose only treatment is Erickson's NC notes. METHOD §0 already expects Wikipedia (CC BY-SA) for small systems gaps such as endianness and Unicode; the cached Wikipedia articles have no section on either.

## 3. Rulings (decided 2026-11-08)

1. **One book, flat chapters, no parts.** OmniStax books are book → chapters → sections, so the map has no parts: `toc.json` holds 45 chapters numbered 1 to 45 and a list of appendices; concept rows carry no part field; `toc.md` and `chapters.mmd` have no part headings or subgraphs. The old part lines in `tools/map/map.spec` are `#` comments now; the spec's chapter order is the book order.
2. **Appendix A · Computer systems is a curated links appendix.** The four computer-systems chapters (Computers and operating systems, Networking, Software engineering practice, Information, coding and security) are not numbered book chapters and are not built as text. Their 19 sections are the appendix's pages A.1 to A.19, each a list of curated links for its concepts. The 62 concepts stay in the map, with `"appendix": "A"` and their old chapter and section ids (the chapter id names the page group), so prerequisite edges into them still resolve: 11 edges run from a chapter concept to an Appendix A concept, and the chapter page points the reader to the appendix for those. Chapter numbering skips the appendix, so the system design chapters (24 to 29) follow the paradigm chapters directly. Getting the job is Appendix B (one reading page, no concepts).
3. **System design concepts take their own tiers.** The cap that held every system design concept at stretch is gone. They take the tiers the inventories give, reconciled as for any other concept: the system design chapters now hold 86 core and 19 stretch concepts. Where an sdp row merged with a CIU row from CIU's optional system design list, the CIU-first rule still said stretch; those that core concepts rest on were set to core under ruling 4.
4. **Union-find is core, and so is every prerequisite a core concept rests on.** Union-find is set core in the spec (Kruskal, core, rests on it). Every other case where a core concept rested on a stretch one was settled the same way, by setting tier=core in the spec (14 concepts, each with a note saying which core concept needs it): Conditional probability and independence (1); Random variables and linearity of expectation (1); Floyd-Warshall algorithm (19); Polynomial rolling hash of a string (21); Serialisation formats (Appendix A); Remote procedure call (RPC) (Appendix A); Information theory (Appendix A); Cryptographic hash functions (Appendix A); Four-step system design interview approach (24); Back-of-the-envelope estimation (24); CAP theorem (25); Scaling a web service: clones, databases, caches, asynchrony (26); Sharding (27); Message queues (28). None looked like a CIU mistake in the other direction, so none was settled by lowering the dependant. The propagation rule then raised the concepts with no CIU row under them (each noted "Tier raised"). The B-tree cascade this ruling once caused is undone by ruling 6 below. No tier inversions remain.
5. **First pass stays chapters 1 to 3.** The first build pass is 1. Algorithms and their cost, 2. Arrays and linked lists, 3. Stacks, queues and deques. Chapter 2 gained two sections from the gap inventory (2.3 Two pointers and sliding windows, 2.4 Prefix sums and difference arrays).
6. **B-tree internals are Advanced (METHOD §4.4 item 14).** The spec drops the edge database-indexes → b-tree (NOEDGE, "knowing an index is a B-tree is Essential; its operations are Advanced", user ruling 2026-11-08) and no longer sets tier=core on B-tree, k-ary tree, 2-3 tree and 2-3-4 tree, which it did only because of that edge. Those take CIU's optional-list verdict again, and the concepts that had been raised under them fall back with them: B-tree (stretch), K-ary tree (stretch), 2-3 search tree (stretch), 2-3-4 tree (stretch), Adding and removing leaves in a 2-4 tree (stretch), External memory model (stretch), B-tree structure (stretch), B-tree search (stretch), B-tree insertion with splits (stretch), B-tree deletion with borrow and merge (stretch), The potential method (stretch). Database indexes stays core and now rests only on ACID. Tier inversions were re-checked after the change: none.
7. **OI Wiki and doocs/leetcode are usable (METHOD §4.4 item 15), and the open-prose set widens.** OI Wiki (CC BY-SA 4.0 + SATA) is used in translation, AI-marked; its rows say so and carry the SATA attribution note. doocs solution write-ups (CC BY-SA 4.0) are used, the LeetCode statements above them are not, and each write-up is paired with an open exercise. A concept counts as having open prose when one of its treatments comes from: `algo-explanation`, `anfp`, `aosa`, `appcomb`, `aspnes-202`, `cpa`, `csci30`, `dmoi3`, `doocs-leetcode`, `dsa-dummies`, `holden-acs`, `icc`, `jeffe`, `lt-csbu`, `mcs2018`, `ods`, `oiwiki`, `opendsa`, `raft-site`, `sdp`, `trekhleb-jsalgo`, `wikibooks`, `wikipedia`, `wp-sysdesign`. MIT and Apache 2.0 prose (OpenDSA, TheAlgorithms explanations, Interactive Coding Challenges notebooks, the Algorithms sections of trekhleb READMEs) counts under METHOD §4.4 item 12; icc's online_judges and trekhleb's other README text stay link-only, and no row uses them.
8. **A gap inventory, `inventory/gap.json`.** It has 136 rows in the FORMAT.md shape with `source` "gap"; each row's id and locator start with its real source's locator prefix (wikipedia:, doocs-leetcode:, oiwiki:, opendsa:, mcs2018:, ...), and the id is the locator with spaces as underscores. `build.py` reads it like the other inventories and takes each row's source from the registry row whose locator scheme has that prefix; the spec names its rows with the prefix `g:`. `check_map.py` checks that every gap row's prefix is a registry prefix, that its source is open, and that its locator resolves in `sources/_cache/<id>/` (the file, and the heading or section number where the locator names one).

## 4. Judgement calls to check

1. **Recursion and induction moved early (chapter 4).** METHOD puts recursion later, but recursive binary search, tree traversals and DFS rest on it in the inventories, so the DAG pulls it forward. Correctness proofs and induction (Erickson, notes) come with it. Backtracking, DP and greedy stay in chapters 17 to 20.
2. **All-pairs shortest paths and DAG shortest paths live in "Dynamic programming on graphs" (chapter 19), not in Shortest paths.** Erickson's Floyd-Warshall, APSP-by-path-length and DAG shortest paths rest on his DP pattern; merged with cpa's rows they inherit that edge. Dijkstra and Bellman-Ford stay in Shortest paths (chapter 15). Floyd-Warshall is now **core** (cpa says core; CIU's row is in its optional Additional Detail), because path reconstruction, core, rests on it.
3. **Tier propagation.** A concept with no CIU row takes the most basic tier of the concepts that rest on it (36 raised, each noted: e.g. MST definition and SCC definition to core because Prim and Kosaraju are core; decision-tree lower bounds to core under the sorting lower bound). Concepts with a CIU row keep CIU's verdict unless the spec sets a tier (ruling 4).
4. **Probability split between chapter 1 and chapter 22.** Counting, basic probability, conditional probability, expectation and indicator variables are in 1.6 because hashing, heapify's analysis and skip lists need them; distributions, tail bounds, Markov chains and randomized algorithms are chapter 22. "Random variables and linearity of expectation" and conditional probability are now **core** (ruling 4: hashing analysis rests on them), although CIU lists them as optional.
5. **Rows split by granularity (7).** CIU rows that cover two testable concepts were split, and the CIU row treats both: BST search/insertion, universal/perfect hashing, counting/radix sort, union by rank/path compression, Floyd-Warshall/APSP DP, convex hull/Graham scan; cpa's classic-DP table also treats the new LCS concept.
6. **Joins across sources that might look loose.** ODS's resizing ArrayQueue with CIU's fixed-size array queue; SPFA (cpa) with Moore's queue-based Bellman-Ford (Erickson); the master theorem (CIU) with recursion trees (Erickson, notes); ODS polynomial hashing, cpa polynomial rolling hash and CIU rolling hash; CIU powers of two with sdp's powers-of-two table; CIU's LRU cache with sdp's query-cache implementation and OOD LRU notebook; CIU's Fourier transform idea with cpa's DFT; sdp's OOD hash map with CIU's implement-a-hash-table; CIU two's complement into cpa's binary representation.
7. **Kept apart although the names are close.** DP as overlapping subproblems (cpa, CIU) vs DP as smart recursion (Erickson): merging them made a cycle with memoization. Hashing with chaining (structure, core) vs expected chain length (notes' analysis). Erickson's string-matching automaton vs cpa's KMP automaton (also a cycle if merged). Erickson's general reduction vs CIU's polynomial-time reductions. CIU's "recognise NP-complete problems" vs Erickson's NP-hard catalog (merging dragged Cook-Levin into core). TCP, UDP and CIU's TCP-vs-UDP comparison. jeffe-notes' definition of unbalanced flows (vertex balances, edge bounds) vs cpa's reduction of edge demands to one max flow: a definition and a result that overlap, kept as two concepts in one section.
8. **Prerequisite edges dropped (12) and added (6).** Each is recorded in the concept's notes. Dropped, mostly where a source's presentation order posed as a dependency: stack → queue and list → deque (ODS defines them through each other), singly linked list → stack/queue (ODS's SLList implements them), potential method → array resizing, chaining → multiplicative hashing, BFS distances → Ford's relaxation, Huffman → compression, database indexes → B-tree (ruling 6), and three that broke cycles (max-flow min-cut ↔ Ford-Fulkerson, two's complement ↔ bitwise operators, random-walk lemma ↔ meldable heap). Added: binary tree → tree, Ford's relaxation → edge relaxation, sparse DP → LCS, and three for the gap concepts: merge sort → merging two sorted lists, sliding-window minimum → fixed-size window, lattice paths avoiding obstacles → grid paths.
9. **Order of chapters 8 to 12: trees and BSTs, heaps, sorting, then balanced trees and tries.** Treaps need heaps, quicksort's analysis needs random BSTs, and core sorting should not wait behind balanced trees. CIU's order (trees intro, BST, heap, balanced, sorting) is kept except that balanced trees move after sorting.
10. **Core number theory stays in chapter 37.** cpa marks GCD, Euclid, LCM, the sieve and trial division core; they open the number-theory chapter (chapter 37) instead of getting an early chapter. Seven core concepts therefore sit among the beyond-the-interview chapters (30 to 45). The alternative is a short "Number theory essentials" chapter after bits.
11. **Placements of a few CIU core rows.** Distributed hash tables (CIU: under Hash table, core) sit with consistent hashing in the databases chapter's partitioning section (chapter 27). The LRU cache stays in chapter 5 as an interview staple. Huffman is taught as greedy (chapter 20), not on Appendix A's compression page. Tries (CIU: Even More Knowledge) are in chapter 12 with the search trees, as METHOD proposes.
12. **Single-concept sections (6) and thin chapters.** The LRU cache, three worked designs (query cache, sales rank, scaling on AWS: each is one sdp solution page), Bloom filters and simhash are one concept each. They are pages because each is a separate thing a reader looks up; joining them would break rule 11's "a section is a page". 7 chapters have exactly three sections, the floor of the 3-to-8 range; none is outside it.
13. **Where the gap concepts sit.** Two pointers, sliding windows and prefix sums are array techniques, so they are chapter 2 (2.3, 2.4), in the first build pass. Two costs follow. 3SUM sorts first, and the map does not make it rest on sorting (chapter 10): the sort is a library call. Several variable-window write-ups keep the window in a hash set or map (chapter 5), so the section should open with a window whose state is a sum or a count array. Kahn's algorithm sits beside the DFS topological sort (14.2); MCS 10.5.1 and Aspnes 9.5.5.1, which the dossier files under Kahn, prove existence by repeatedly taking a minimal element and skip efficiency, so they treat topological order, not Kahn. Merging intervals and meeting rooms are a new greedy section (20.2) beside interval scheduling; the meeting-rooms concept also stands for the sweep line over intervals, and cpa's union of segments (44.3) stays where it is. Generation is a backtracking section (17.2), with next permutation and Heap's algorithm in it although neither backtracks. Coin change and grid paths are a DP section (18.3) before knapsack: doocs frames coin change as the complete knapsack, but Wikipedia and ANFP teach it directly, so it does not rest on knapsack. Grid paths joins the DP recurrence and the binomial count of lattice paths in one concept.
14. **Tiers of the gap concepts.** All are core (Essential) except three. 2D prefix sums and 2D difference arrays are stretch: matrix range sums come up at harder interviews and in contests, and no open exercise with tests was found for them. Heap's algorithm is stretch: backtracking and next permutation are what interviews ask. 1D difference arrays are core: car pooling and flight bookings are common mediums, and the meeting-rooms concept rests on them.
15. **System design prose from the sweep.** METHOD §4.4 item 1 reads "System design: the primer only". The open-prose pass nevertheless took treatments that `dossiers/sweep-system-design.md` lists (Wikipedia articles fetched with pre-2023 revisions, AOSA chapters, the Raft website) for system design concepts that had none, because the task asked for every concept the sweeps cover. If item 1 means no other system design prose at all, drop those rows from `inventory/gap.json` and the spec: they are the gap rows with prefixes wp:, aosa: and raft-site:.
16. **Folds and what stayed apart.** Thin or duplicate cp-algorithms articles were folded into the home of the concept they duplicate (each section lists its folds in toc.json/toc.md): e.g. mst_kruskal_with_dsu into Kruskal, finding-negative-cycle into Floyd-Warshall, dijkstra_sparse into Dijkstra, sequences/k-th into Selection, string/rabin-karp into string hashing, factorial-divisors into factorials mod p, randomized_heap into ODS's meldable heap. cpa's treap article, by contrast, shares the Treaps home with ODS and notes but keeps its own split/merge concepts.

## 5. Chapter dependencies

Chapter → the chapters whose concepts it uses directly (any prerequisite edge that crosses chapters); "A" is Appendix A. The Mermaid graph in `chapters.mmd` shows the Hasse-reduced version.

- 1. Algorithms and their cost → none
- 2. Arrays and linked lists → 1
- 3. Stacks, queues and deques → 1, 2
- 4. Recursion and induction → 1
- 5. Hash tables → 1, 2
- 6. Binary search → 1, 2, 4
- 7. Bits and data representation → 1
- 8. Trees and binary search trees → 1, 3, 4, 5
- 9. Heaps and priority queues → 1, 2, 3, 8
- 10. Divide and conquer and sorting → 1, 2, 4, 8
- 11. Balanced search trees → 1, 2, 8, 9
- 12. Tries and other search structures → 1, 2, 5, 8, 11
- 13. Graphs and graph search → 2, 3, 5, 8
- 14. Depth-first structure → 3, 13
- 15. Shortest paths → 3, 8, 9, 13
- 16. Disjoint sets and minimum spanning trees → 1, 8, 9, 10, 13
- 17. Backtracking → 1, 4, 7, 8
- 18. Dynamic programming → 1, 2, 3, 4, 6, 8, 17
- 19. Dynamic programming on graphs → 4, 13, 14, 15, 18
- 20. Greedy algorithms → 2, 4, 9, 10, 18
- 21. String searching → 5, 6, 10
- 22. Probability and randomized algorithms → 1, 11
- 23. Lower bounds and intractability → 1, 4, 10, 16, 17, 18
- 24. Approaching a system design question → 7
- 25. Availability and consistency → none
- 26. Scaling the web tier → 24, 25, A
- 27. Databases → 5, 25, 26
- 28. Caching and asynchrony → 5, 26, 27
- 29. Worked designs → 5, 9, 13, 24, 26, 27, 28, A
- 30. Range queries → 2, 3, 6, 7, 8, 10, 16, 18
- 31. Tree algorithms → 3, 7, 8, 10, 13, 14, 16, 30
- 32. Network flow and matching → 6, 13, 15
- 33. More graph algorithms → 1, 13, 14, 16, 30, 31, 32
- 34. Advanced string algorithms → 10, 12, 13, 19, 21, 30
- 35. Advanced dynamic programming → 7, 10, 18
- 36. Sketches and probabilistic data structures → 5, 22, A
- 37. Number theory: divisibility and primes → 1, 7, 18
- 38. Number theory: modular arithmetic → 2, 4, 37
- 39. Number theory: representations and fast arithmetic → 4, 7, 18, 37, 38
- 40. Combinatorics → 1, 3, 7, 13, 18, 37, 38
- 41. Game theory → 7, 13, 30
- 42. Linear algebra, polynomials and the FFT → 7, 10, 30, 37, 38
- 43. Numerical methods and optimisation → 22, 23, 32
- 44. Computational geometry: primitives → 10, 16, 22, 37, 39
- 45. Computational geometry: algorithms → 3, 5, 6, 8, 10, 18, 22, 30, 44
- Appendix A · Computer systems → 1
