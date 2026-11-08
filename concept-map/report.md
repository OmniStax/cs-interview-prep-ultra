# Concept map report

Built from the seven inventories in `inventory/` (1165 rows). Output: one book of **45 numbered chapters** and **234 sections**, plus two appendices that are not built as text: **Appendix A · Computer systems** (19 curated-links pages, 62 concepts) and **Appendix B · Getting the job** (one reading page, no concepts). **1000 concepts** in all. `python3 tools/check_map.py` passes (0 errors, 0 warnings; no tier inversions remain).

## 1. Counts

### Concepts per chapter range and appendix

Per-chapter counts are in `toc.md` (each chapter heading) and `toc.json` (`tier_counts`).

| Chapters | Sections | core | stretch | contest | total |
|---|---:|---:|---:|---:|---:|
| 1–7 (Algorithms and their cost … Bits and data representation) | 35 | 98 | 27 | 7 | 132 |
| 8–12 (Trees and binary search trees … Tries and other search structures) | 26 | 59 | 36 | 7 | 102 |
| 13–16 (Graphs and graph search … Disjoint sets and minimum spanning trees) | 19 | 38 | 20 | 3 | 61 |
| 17–23 (Backtracking … Lower bounds and intractability) | 32 | 51 | 54 | 25 | 130 |
| 24–29 (Approaching a system design question … Worked designs) | 27 | 86 | 19 | 0 | 105 |
| 30–45 (Range queries … Computational geometry: algorithms) | 95 | 7 | 136 | 265 | 408 |
| **Chapters 1–45** | 234 | **339** | **292** | **307** | **938** |
| Appendix A · Computer systems (links, not built) | 19 pages | 36 | 26 | 0 | 62 |
| **All** | | **375** | **318** | **307** | **1000** |

First build pass: chapters 1. Algorithms and their cost, 2. Arrays and linked lists, 3. Stacks, queues and deques.

Chapter sections by tag: 107 core, 68 stretch, 59 contest; Appendix A pages: 12 core, 7 stretch. Section sizes (concepts: sections): 1: 6, 2: 38, 3: 67, 4: 56, 5: 47, 6: 22, 7: 10, 8: 7.

Kinds: result 441, skill 230, definition 213, idea 115, axiom 1.

### Merging

- 1165 rows in, 5 dropped, 7 rows split over two concepts each, so 1167 treatments in 1000 concepts.
- **135 merged clusters** (concepts with more than one treatment); 133 of them join different sources, the other 2 join two rows of one source. Cluster sizes: 106 with 2 rows, 26 with 3 rows, 3 with 4 rows; 865 concepts have one treatment.
- Source combinations in cross-source clusters: ciu + ods (26), cpa + jeffe (16), ciu + cpa (16), ciu + notes (11), ciu + cpa + jeffe (11), ciu + sdp (10), ciu + jeffe (8), cpa + notes (8), notes + ods (5), ciu + notes + ods (4), ciu + cpa + notes (4), cpa + ods (3), ciu + jeffe + ods (3), jeffe + ods (2), ciu + cpa + ods (2), ciu + jeffe + notes (1), ciu + cpa + notes + ods (1), jeffe + ods + sdp (1), ciu + cpa + jeffe + ods (1).
- Concepts each source treats: cpa 515, ciu 208, ods 113, sdp 113, jeffe 112, notes 102.
- Hasse reduction removed 105 redundant prerequisite edges; 1295 edges remain.

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

None of these is in the map, because no inventory row teaches it (the rule: never invent a concept). Each is a job for the resource finder (METHOD §6).

| Topic | Tier it would get | Evidence |
|---|---|---|
| Two pointers | core | No inventory names it. Closest rows: cpa's tortoise and hare (2.5) and Kadane (18.4). |
| Sliding window (variable-size) | core | cpa teaches only the fixed-window minimum with a monotonic deque (3.4, `sliding-window-minimum`). The general expand/shrink window has no row. |
| Kahn's algorithm (topological sort by in-degrees) | core | cpa graph/topological-sort says outright "Kahn's algorithm is not covered"; Erickson and CIU teach only the DFS method. |
| Prefix sums and difference arrays | core | Assumed by cpa (Fenwick trees, sqrt decomposition, maximum subarray, range updates) but taught nowhere. |
| Modular arithmetic basics | core | Assumed by 8 cpa rows (modular exponentiation, inverses, congruences, string hashing); taught nowhere. |
| Interval problems (merge intervals, meeting rooms) | core | Only interval scheduling (Erickson 4.2) and the contest-tier union of segments (cpa). |
| Generating permutations and subsets by backtracking | core | CIU links only; Erickson's backtracking examples are n queens, subset sum and segmentation; cpa covers k-combinations and bracket sequences. |
| Classic DP problems: coin change, grid paths, longest palindromic subsequence | core | Grid paths is an alias in cpa's classic-DP table; the others have no row. |
| Object-oriented programming basics | core | Assumed by CIU's design patterns and SOLID rows and by sdp's OOD notebooks. |
| Memory and pointers | core | Assumed by CIU arrays and linked lists. |
| Rate limiting | stretch | METHOD §0 already names it; the primer has no section. |
| Unique ID generation | stretch | Only a prompt in CIU's dropped practice list (`ciu:sd-exercises`). |
| MapReduce as a concept | stretch | sdp's worked designs use it (`mapreduce-aggregation` assumes it) but nothing defines it. |
| Queueing (Little's law, utilisation and latency) | stretch | sdp's back pressure links it as further reading only; METHOD §2.4 wants a sim for it. |

One bridge concept **was** added because an inventory names it: **Longest common subsequence** (18.6), split out of cpa's classic-DP table (`cpa:classic-dp-problems`, alias "LCS"). Its only treatment is that table row, so it counts as open prose but has no article behind it: treat it as a prose gap too.

Other assumed knowledge that no row teaches (bracketed prerequisites in the inventories, contest-tier mostly): Boolean formula in CNF, Cramer's rule, DCEL, DFA, Wilson's theorem, birthday paradox, bitmask DP, circles, complex numbers, coordinate geometry, definite integrals, derivatives, determinant, divisibility, equivalence relations, finite automaton, intermediate value theorem, linear independence, matrices, matrix multiplication, multinomial theorem, permutation inversions, pigeonhole principle, planar graphs, prefix products, prime numbers, quad-edge data structure, sets, systems of linear equations, triangulation. Each affected concept says so in its notes ("Assumes, untaught in the map").

### Concepts with no open prose

**189 concepts** are taught only by CIU links or by Erickson's NC notes (90 core, 66 stretch, 33 contest). Their prose needs the finder. Whole sections with no open source at all are marked "open prose: none" in toc.md (17 chapter sections; 15 of Appendix A's 19 pages, which is expected for a links appendix).

- **1. Algorithms and their cost** (7; ciu only 3, notes only 4): Big-Omega and Big-Theta [core]; Amortized analysis [core]; Summation, taxation and charging methods [core]; Incrementing and decrementing counters; Factorials, permutations and combinations [core]; Basic probability [core]; Conditional probability and independence [core]
- **2. Arrays and linked lists** (5; ciu only 5): Array [core]; Indexing by pointer arithmetic [core]; Implement a vector [core]; Pointer to pointer [core]; Implement a linked list [core]
- **3. Stacks, queues and deques** (1; ciu only 1): Queue on a linked list with a tail pointer [core]
- **4. Recursion and induction** (5; ciu only 1, notes only 4): Tail recursion [core]; Proof by smallest counterexample [core]; The axiom of induction and strong induction [core]; Induction on numbers, summations and tilings [core]; Induction on recursive functions and trees [core]
- **5. Hash tables** (7; notes only 6, ciu only 1): Hash table [core]; Table doubling [core]; Universal hash families [core]; Perfect hashing (two-level) [core]; Expected chain length under universal hashing [core]; Balls and bins: maximum chain length; Cuckoo hashing
- **6. Binary search** (1; ciu only 1): Implement binary search, iteratively and recursively [core]
- **7. Bits and data representation** (4; ciu only 4): Branch-free bit tricks [core]; Floating-point representation [core]; Endianness [core]; Unicode and character encodings [core]
- **8. Trees and binary search trees** (6; ciu only 6): Tree [core]; BST minimum, maximum and height [core]; Inorder successor in a BST [core]; Checking whether a binary tree is a BST [core]; Implement a BST [core]; Balanced search trees (the general idea) [core]
- **9. Heaps and priority queues** (2; ciu only 2): Sift up and sift down [core]; Implement a max-heap [core]
- **10. Divide and conquer and sorting** (13; ciu only 6, notes only 7): Stability in sorting [core]; Selection sort [core]; Insertion sort [core]; Bubble sort [core]; Solving recurrences by guess and confirm [core]; The Akra-Bazzi method; Linear recurrences by annihilators; Sorting linked lists versus arrays [core]; The nuts and bolts problem; Implement merge sort and quicksort [core]; Decision-tree lower bounds [core]; Information-theoretic lower bound [core]; Reductions to and from sorting
- **11. Balanced search trees** (7; ciu only 3, notes only 4): AVL tree; 2-3 search tree [core]; Random priorities give expected logarithmic depth; Lazy deletion and global rebuilding; Rotations, double rotations and splaying; Splay tree; K-ary tree [core]
- **12. Tries and other search structures** (5; ciu only 5): Trie prefix operations and performance [core]; Ternary search trie [core]; van Emde Boas trees; Augmenting data structures; k-d tree
- **13. Graphs and graph search** (2; ciu only 2): Graph representations [core]; Implement BFS and DFS on both representations [core]
- **15. Shortest paths** (1; ciu only 1): A* search
- **16. Disjoint sets and minimum spanning trees** (1; notes only 1): Shallow threaded trees
- **18. Dynamic programming** (2; ciu only 2): Recognising a DP problem [core]; RNA secondary structure [core]
- **20. Greedy algorithms** (2; notes only 2): Matroids and the greedy algorithm; Scheduling unit jobs with deadlines
- **21. String searching** (3; notes only 2, ciu only 1): Brute-force substring search [core]; Boyer-Moore (and Horspool) [core]; String matching with a finite-state machine [core]
- **22. Probability and randomized algorithms** (12; notes only 9, ciu only 3): Common distributions: uniform, Bernoulli, binomial, geometric; Removing bias from coin flips; Coupon collecting (Pokemon collecting); Deterministic vs. randomized algorithms; expected running time; Generating random permutations (shuffling) [core]; Markov's inequality; Chebyshev's inequality; Chernoff bounds; Treap depth with high probability; Markov chains [core]; Random walks; Markov text generation
- **23. Lower bounds and intractability** (16; notes only 13, ciu only 3): Finding the maximum needs n-1 comparisons; Adversary arguments; Finding the minimum and maximum: ceil(3n/2) - 2; Evasive graph properties; Polynomial-time reductions [core]; Recognising NP-complete problems in disguise [core]; Approximation algorithms and ratios [core]; Greedy load balancing; Vertex cover approximation; Greedy set cover and hitting set; Traveling salesman: hardness and metric approximation; k-center clustering; An FPTAS for subset sum; Fixed-parameter algorithms [core]; Faster exponential algorithms for 3SAT; Faster exponential algorithms for maximum independent set
- **25. Availability and consistency** (2; ciu only 2): Fallacies of distributed computing; Consensus: Paxos and Raft
- **26. Scaling the web tier** (1; ciu only 1): Scaling a web service: clones, databases, caches, asynchrony [core]
- **27. Databases** (4; ciu only 4): Database normalisation; Consistent hashing; Distributed hash tables [core]; NoSQL patterns
- **28. Caching and asynchrony** (1; ciu only 1): Redis as an in-memory data store
- **29. Worked designs** (1; ciu only 1): Distributed graph algorithms
- **32. Network flow and matching** (4; notes only 4): Unbalanced flows: supplies and demands; Pseudoflows and augmenting between imbalances; Minimum-cost circulations and cycle canceling; Node potentials and reduced costs
- **33. More graph algorithms** (2; notes only 2): Karger's contraction algorithm; Karger-Stein recursive contraction
- **35. Advanced dynamic programming** (7; notes only 7): Total monotonicity and the SMAWK algorithm; Saving space by divide and conquer (Hirschberg); Saving time with sparseness; The Four Russians speedup; DFA minimization by dynamic programming; NFA acceptance and regular-expression matching; Context-free parsing (CYK)
- **36. Sketches and probabilistic data structures** (5; notes only 3, ciu only 2): Bloom filters; The streaming model; Count-min sketch; HyperLogLog; Locality-sensitive hashing (simhash)
- **42. Linear algebra, polynomials and the FFT** (2; notes only 2): Polynomial representations; Converting by Vandermonde matrices
- **43. Numerical methods and optimisation** (9; notes only 9): Linear programming; The geometry of linear programs; Formulating problems as linear programs; Linear programming duality; Complementary slackness; The simplex algorithm; Network simplex; Linear expected time in fixed dimension; LP rounding for weighted vertex cover
- **Appendix A, Computers and operating systems** (15; ciu only 15): CPU components: ALU, registers and RAM [core]; How a CPU executes a program [core]; Memory hierarchy and CPU caches [core]; Building a computer from logic gates; How a compiler works; Compiler optimisation; Garbage collection; Processes versus threads [core]; Interrupts and context switching [core]; Paging, segmentation and virtual memory [core]; Fork and copy-on-write [core]; Locks, mutexes, semaphores and monitors [core]; Deadlock and livelock [core]; Concurrency in Python and the GIL [core]; Parallel programming
- **Appendix A, Networking** (6; ciu only 6): OSI and TCP/IP models [core]; Subnetting and CIDR notation [core]; TCP versus UDP [core]; Socket programming [core]; TLS and HTTPS [core]; Serialisation formats [core]
- **Appendix A, Software engineering practice** (16; ciu only 16): Unit testing [core]; Mock objects [core]; Integration testing [core]; Dependency injection [core]; Test-driven development [core]; UML class diagrams [core]; Creational design patterns [core]; Structural design patterns [core]; Behavioural design patterns [core]; Single responsibility principle; Open/closed principle; Liskov substitution principle; Interface segregation principle; Dependency inversion principle; Using vi(m) and Emacs; Unix command-line tools
- **Appendix A, Information, coding and security** (12; ciu only 12): Information theory [core]; Entropy; Parity bits; Hamming code; Lossless compression; LZ77; Cryptographic hash functions [core]; Encryption; Threat models and privilege separation; Control hijacking and buffer overflows; Web security model; Network security and side channels

Most of the CIU-only concepts are in Appendix A (operating systems, networking basics, testing, design patterns, security), which is now a curated links appendix: its pages need good links, not open prose. Among the numbered chapters the heaviest gaps are the probability, adversary and approximation chapters, whose only treatment is Erickson's NC notes. METHOD §0 already expects Wikipedia (CC BY-SA) for small systems gaps such as endianness and Unicode.

## 3. Rulings (decided 2026-11-08)

1. **One book, flat chapters, no parts.** OmniStax books are book → chapters → sections, so the map has no parts: `toc.json` holds 45 chapters numbered 1 to 45 and a list of appendices; concept rows carry no part field; `toc.md` and `chapters.mmd` have no part headings or subgraphs. The old part lines in `tools/map/map.spec` are `#` comments now; the spec's chapter order is the book order.
2. **Appendix A · Computer systems is a curated links appendix.** The four computer-systems chapters (Computers and operating systems, Networking, Software engineering practice, Information, coding and security) are not numbered book chapters and are not built as text. Their 19 sections are the appendix's pages A.1 to A.19, each a list of curated links for its concepts. The 62 concepts stay in the map, with `"appendix": "A"` and their old chapter and section ids (the chapter id names the page group), so prerequisite edges into them still resolve: 11 edges run from a chapter concept to an Appendix A concept, and the chapter page points the reader to the appendix for those. Chapter numbering skips the appendix, so the system design chapters (24 to 29) follow the paradigm chapters directly. Getting the job is Appendix B (one reading page, no concepts).
3. **System design concepts take their own tiers.** The cap that held every system design concept at stretch is gone. They take the tiers the inventories give, reconciled as for any other concept: the system design chapters now hold 86 core and 19 stretch concepts. Where an sdp row merged with a CIU row from CIU's optional system design list, the CIU-first rule still said stretch; those that core concepts rest on were set to core under ruling 4.
4. **Union-find is core, and so is every prerequisite a core concept rests on.** Union-find is set core in the spec (Kruskal, core, rests on it). Every other case where a core concept rested on a stretch one was settled the same way, by setting tier=core in the spec (18 concepts, each with a note saying which core concept needs it): Conditional probability and independence (1); Random variables and linearity of expectation (1); 2-3 search tree (11); 2-3-4 tree (11); K-ary tree (11); B-tree (11); Floyd-Warshall algorithm (19); Polynomial rolling hash of a string (21); Serialisation formats (Appendix A); Remote procedure call (RPC) (Appendix A); Information theory (Appendix A); Cryptographic hash functions (Appendix A); Four-step system design interview approach (24); Back-of-the-envelope estimation (24); CAP theorem (25); Scaling a web service: clones, databases, caches, asynchrony (26); Sharding (27); Message queues (28). None looked like a CIU mistake in the other direction, so none was settled by lowering the dependant. The propagation rule then raised the concepts with no CIU row under them (each noted "Tier raised"). The widest cascade comes from database indexes (sdp, core) resting on B-trees: B-trees, k-ary trees, 2-3 trees, 2-3-4 trees and, by propagation, ODS's B-tree and 2-4 tree operations and the external-memory model are core. If B-trees should stay stretch, dropping the edge database-indexes → b-tree with a NOEDGE line undoes the whole cascade. No tier inversions remain.
5. **First pass stays chapters 1 to 3.** The first build pass is 1. Algorithms and their cost, 2. Arrays and linked lists, 3. Stacks, queues and deques.

## 4. Judgement calls to check

1. **Recursion and induction moved early (chapter 4).** METHOD puts recursion later, but recursive binary search, tree traversals and DFS rest on it in the inventories, so the DAG pulls it forward. Correctness proofs and induction (Erickson, notes) come with it. Backtracking, DP and greedy stay in chapters 17 to 20.
2. **All-pairs shortest paths and DAG shortest paths live in "Dynamic programming on graphs" (chapter 19), not in Shortest paths.** Erickson's Floyd-Warshall, APSP-by-path-length and DAG shortest paths rest on his DP pattern; merged with cpa's rows they inherit that edge. Dijkstra and Bellman-Ford stay in Shortest paths (chapter 15). Floyd-Warshall is now **core** (cpa says core; CIU's row is in its optional Additional Detail), because path reconstruction, core, rests on it.
3. **Tier propagation.** A concept with no CIU row takes the most basic tier of the concepts that rest on it (44 raised, each noted: e.g. MST definition and SCC definition to core because Prim and Kosaraju are core; decision-tree lower bounds to core under the sorting lower bound). Concepts with a CIU row keep CIU's verdict unless the spec sets a tier (ruling 4).
4. **Probability split between chapter 1 and chapter 22.** Counting, basic probability, conditional probability, expectation and indicator variables are in 1.6 because hashing, heapify's analysis and skip lists need them; distributions, tail bounds, Markov chains and randomized algorithms are chapter 22. "Random variables and linearity of expectation" and conditional probability are now **core** (ruling 4: hashing analysis rests on them), although CIU lists them as optional.
5. **Rows split by granularity (7).** CIU rows that cover two testable concepts were split, and the CIU row treats both: BST search/insertion, universal/perfect hashing, counting/radix sort, union by rank/path compression, Floyd-Warshall/APSP DP, convex hull/Graham scan; cpa's classic-DP table also treats the new LCS concept.
6. **Joins across sources that might look loose.** ODS's resizing ArrayQueue with CIU's fixed-size array queue; SPFA (cpa) with Moore's queue-based Bellman-Ford (Erickson); the master theorem (CIU) with recursion trees (Erickson, notes); ODS polynomial hashing, cpa polynomial rolling hash and CIU rolling hash; CIU powers of two with sdp's powers-of-two table; CIU's LRU cache with sdp's query-cache implementation and OOD LRU notebook; CIU's Fourier transform idea with cpa's DFT; sdp's OOD hash map with CIU's implement-a-hash-table; CIU two's complement into cpa's binary representation.
7. **Kept apart although the names are close.** DP as overlapping subproblems (cpa, CIU) vs DP as smart recursion (Erickson): merging them made a cycle with memoization. Hashing with chaining (structure, core) vs expected chain length (notes' analysis). Erickson's string-matching automaton vs cpa's KMP automaton (also a cycle if merged). Erickson's general reduction vs CIU's polynomial-time reductions. CIU's "recognise NP-complete problems" vs Erickson's NP-hard catalog (merging dragged Cook-Levin into core). TCP, UDP and CIU's TCP-vs-UDP comparison. jeffe-notes' definition of unbalanced flows (vertex balances, edge bounds) vs cpa's reduction of edge demands to one max flow: a definition and a result that overlap, kept as two concepts in one section.
8. **Prerequisite edges dropped (11) and added (3).** Each is recorded in the concept's notes. Dropped, mostly where a source's presentation order posed as a dependency: stack → queue and list → deque (ODS defines them through each other), singly linked list → stack/queue (ODS's SLList implements them), potential method → array resizing, chaining → multiplicative hashing, BFS distances → Ford's relaxation, Huffman → compression, and three that broke cycles (max-flow min-cut ↔ Ford-Fulkerson, two's complement ↔ bitwise operators, random-walk lemma ↔ meldable heap). Added: binary tree → tree, Ford's relaxation → edge relaxation, sparse DP → LCS.
9. **Order of chapters 8 to 12: trees and BSTs, heaps, sorting, then balanced trees and tries.** Treaps need heaps, quicksort's analysis needs random BSTs, and core sorting should not wait behind balanced trees. CIU's order (trees intro, BST, heap, balanced, sorting) is kept except that balanced trees move after sorting.
10. **Core number theory stays in chapter 37.** cpa marks GCD, Euclid, LCM, the sieve and trial division core; they open the number-theory chapter (chapter 37) instead of getting an early chapter. Seven core concepts therefore sit among the beyond-the-interview chapters (30 to 45). The alternative is a short "Number theory essentials" chapter after bits.
11. **Placements of a few CIU core rows.** Distributed hash tables (CIU: under Hash table, core) sit with consistent hashing in the databases chapter's partitioning section (chapter 27). The LRU cache stays in chapter 5 as an interview staple. Huffman is taught as greedy (chapter 20), not on Appendix A's compression page. Tries (CIU: Even More Knowledge) are in chapter 12 with the search trees, as METHOD proposes.
12. **Single-concept sections (6) and thin chapters.** The LRU cache, three worked designs (query cache, sales rank, scaling on AWS: each is one sdp solution page), Bloom filters and simhash are one concept each. They are pages because each is a separate thing a reader looks up; joining them would break rule 11's "a section is a page". 9 chapters have exactly three sections, the floor of the 3-to-8 range; none is outside it.
13. **Folds and what stayed apart.** Thin or duplicate cp-algorithms articles were folded into the home of the concept they duplicate (each section lists its folds in toc.json/toc.md): e.g. mst_kruskal_with_dsu into Kruskal, finding-negative-cycle into Floyd-Warshall, dijkstra_sparse into Dijkstra, sequences/k-th into Selection, string/rabin-karp into string hashing, factorial-divisors into factorials mod p, randomized_heap into ODS's meldable heap. cpa's treap article, by contrast, shares the Treaps home with ODS and notes but keeps its own split/merge concepts.

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
- 17. Backtracking → 4, 8
- 18. Dynamic programming → 3, 4, 6, 8, 17
- 19. Dynamic programming on graphs → 4, 13, 14, 15, 18
- 20. Greedy algorithms → 4, 9, 10, 18
- 21. String searching → 5, 6, 10
- 22. Probability and randomized algorithms → 1, 11
- 23. Lower bounds and intractability → 1, 4, 10, 16, 17, 18
- 24. Approaching a system design question → 7
- 25. Availability and consistency → none
- 26. Scaling the web tier → 24, 25, A
- 27. Databases → 5, 11, 25, 26
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
