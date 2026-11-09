# Table of contents

Derived from the concept map (`concepts.json`). One book of numbered chapters; each numbered section is one page, the home of the concepts listed under it. Section tier badges give the most common tier of the section's concepts; a concept whose tier differs from its section's carries its own badge. Sources lists the inventories that teach the section's concepts: **ciu** = CIU, **cpa** = cpa, **jeffe** = Erickson, **notes** = Erickson notes (NC), **ods** = ODS, **sdp** = Primer, **wikipedia** = Wikipedia, **wikibooks** = Wikibooks, **wp** = Wikipedia (system design set), **opendsa** = OpenDSA, **doocs** = doocs/leetcode write-ups, **oiwiki** = OI Wiki (in translation), **algo-expl** = TheAlgorithms explanations, **icc** = Interactive Coding Challenges, **trekhleb** = javascript-algorithms READMEs, **mcs2018** = Mathematics for Computer Science (2018), **aspnes-202** = Aspnes, discrete math notes, **anfp** = Algorithms Notes for Professionals, **dmoi3** = Levin, Discrete Mathematics, **appcomb** = Applied Combinatorics, **csci30** = CSCI 30 notes, **lt-csbu** = Computer Science from the Bottom Up, **holden** = Holden, Applied CS, **aosa** = Architecture of Open Source Applications, **raft-site** = Raft website, **brisk** = A Cool Brisk Walk Through Discrete Mathematics, **aspnes-469** = Aspnes, randomized algorithms notes, **aspnes-223** = Aspnes, data structures and programming notes, **openintro** = OpenIntro Statistics. "Open prose: none" marks a section whose concepts are taught only by CIU links or by Erickson's NC notes, so its text has no open source yet.

Chapters 1 to 3 (marked **first pass**) are the first build pass. The appendices are not built as text.

## 1. Algorithms and their cost · **first pass**

*Concepts: 21 core · 6 stretch*

- **1.1 What an algorithm is** [core] · jeffe, ods
  Algorithm; Underspecified algorithm; Describing an algorithm; The need for efficiency; Interface and implementation; Lattice multiplication [stretch]; Peasant multiplication; Huntington–Hill apportionment [stretch]
- **1.2 Logarithms, factorials and harmonic numbers** [core] · ods
  Logarithms; Factorials and Stirling’s approximation; Harmonic numbers [stretch]
- **1.3 Asymptotic notation** [core] · ciu, ods, wikipedia, opendsa
  Big-O notation; Big-Omega and Big-Theta; Analysis with multiple parameters [stretch]
- **1.4 Analysing running time and space** [core] · ciu, jeffe, ods
  The w-bit word-RAM model; Analysing running time and space; Worst-case, amortized and expected running times
- **1.5 Amortized analysis** [core] · ciu, notes, ods, wikipedia, opendsa, oiwiki
  Amortized analysis; Aggregate analysis and the accounting method; Potential method [stretch]
  *Notes:* Reference link (References item, link only): jeffe-notes:09-amortize.3, Erickson's lecture notes on incrementing and decrementing counters (CC BY-NC-SA 4.0). The concept counter-increment-decrement was removed from the map by ruling 19 (METHOD §4.4): it had no open prose and contest tier; its inventory row is listed under dropped in concepts.json.
- **1.6 Counting and expected value** [core] · ciu, notes, ods, wikipedia, wikibooks, oiwiki, mcs2018, aspnes-202, dmoi3, appcomb, brisk, aspnes-469, openintro
  Factorials, permutations and combinations; Basic probability; Conditional probability and independence; Random variable; Expected value and linearity of expectation; Indicator random variables [stretch]; Expected tosses until the first head

## 2. Arrays and linked lists · **first pass**

*Concepts: 23 core · 3 stretch*

- **2.1 Arrays and the list interface** [core] · ciu, ods, wikipedia, wikibooks, oiwiki, holden, aspnes-223
  Array; Indexing by pointer arithmetic; List interface (linear sequence)
- **2.2 Dynamic arrays** [core] · ciu, ods
  Dynamic array (vector); Growing and shrinking the backing array; Cost of dynamic-array operations; Block copying with memcpy/arraycopy [stretch]; Implement a vector (no open prose)
- **2.3 Two pointers and sliding windows** [core] · wikipedia, doocs, oiwiki, icc
  Two pointers; 3SUM in quadratic time; Merging two sorted lists; Fixed-size sliding window; Variable-size sliding window
  *Folds:* OI Wiki misc/two-pointer is split over this home: its sorted-sequence section treats two-pointers, its window section the variable window, its linked-list section Floyd's cycle detection (2.7).
- **2.4 Prefix sums and difference arrays** [core] · wikipedia, doocs, oiwiki
  Prefix sums; Two-dimensional prefix sums (summed-area table) [stretch]; Difference arrays; Two-dimensional difference arrays [stretch]
  *Folds:* OI Wiki basic/prefix-sum is split over this home: one row per section (1D, 2D, 1D difference, 2D difference); its tree prefix sums and differences are not taken.
- **2.5 Singly linked lists** [core] · ciu, ods, wikipedia, opendsa, oiwiki, aspnes-223
  Singly linked list; Pointer to pointer; Implement a linked list; Linked lists versus arrays
- **2.6 Doubly linked lists** [core] · ciu, ods
  Dummy (sentinel) node; Doubly linked list
- **2.7 Cycles in linked lists: tortoise and hare** [core] · cpa, wikipedia, oiwiki, algo-expl
  Floyd's cycle detection (tortoise and hare); Finding where the cycle starts; Why the reset finds the cycle start

## 3. Stacks, queues and deques · **first pass**

*Concepts: 15 core · 8 stretch · 1 contest*

- **3.1 Stacks and bracket matching** [core] · ciu, cpa, ods, wikipedia
  Stack; Balanced bracket sequence; Checking bracket balance
- **3.2 Queues and circular buffers** [core] · ciu, ods, wikibooks
  Queue; Circular buffer; Queue on a linked list with a tail pointer; ArrayQueue (array-backed FIFO queue)
- **3.3 Deques** [core] · ods
  Deque interface; ArrayDeque; DualArrayDeque: a deque from two stacks [stretch]
- **3.4 Min-stacks and monotonic queues** [core] · cpa, wikipedia, doocs, oiwiki
  Minimum stack; Queue from two stacks (with minimum); Minimum queue via a monotonic deque; Sliding window minimum; Nearest smaller element to the left/right with a stack; Largest zero submatrix in O(nm) [stretch]
  *Folds:* cpa data_structures/stack_queue_modification is the home article; cpa dynamic_programming/zero_matrix contributes its stack step.
- **3.5 Stack applications: expression evaluation** [stretch] · cpa
  Reverse Polish notation evaluation [core]; Infix expression parsing with two stacks; Unary and right-associative operators in parsing
- **3.6 Space-efficient lists** [stretch] · ods
  RootishArrayStack; Block index by the quadratic formula [contest]; Omega(sqrt n) wasted space is unavoidable; SEList (space-efficient list); SEList spreading and gathering

## 4. Recursion and induction

*Concepts: 12 core · 1 stretch*

- **4.1 Recursion and reduction** [core] · ciu, jeffe, wikipedia
  Reduction; Recursion: simplify and delegate (the Recursion Fairy); Tail recursion; Tower of Hanoi
- **4.2 Exponentiation by squaring** [core] · cpa, jeffe
  Binary exponentiation; Iterative binary exponentiation; Modular exponentiation; Binary exponentiation for any associative operation [stretch]
- **4.3 Induction and correctness proofs** [core] · jeffe, notes, csci30
  Proof by smallest counterexample (no open prose); The axiom of induction and strong induction; Induction on numbers, summations and tilings (no open prose); Induction on recursive functions and trees (no open prose); Proving an algorithm correct

## 5. Hash tables

*Concepts: 16 core · 2 stretch · 2 contest*

- **5.1 Sets, maps and the dictionary problem** [core] · ciu, notes, ods, wikipedia, opendsa
  USet interface (unordered set); Dictionary/map as a USet of pairs; Hash table
- **5.2 Hashing with chaining** [core] · ciu, ods, wikipedia
  Hashing with chaining; Table doubling
- **5.3 Open addressing** [core] · ciu, notes, ods, sdp
  Open addressing and linear probing; Deleted markers (tombstones) in open addressing; Implement a hash table with linear probing
- **5.4 Hash function families** [core] · ciu, notes, ods, wikipedia
  Universal hash families; Multiplicative hashing; Tabulation hashing [stretch]; Perfect hashing (two-level) (no open prose)
- **5.5 Hash codes** [core] · ods
  Hash code requirements; Hash codes for primitive types; Hash codes for compound objects
- **5.6 Analysing hash tables** [contest] · notes, ods, wikipedia
  Expected chain length under universal hashing [core] (no open prose); Balls and bins: maximum chain length (no open prose); Analysis of linear probing via runs [stretch]; Cuckoo hashing
- **5.7 Combining structures: the LRU cache** [core] · ciu, sdp
  LRU cache: hash map plus doubly linked list

## 6. Binary search

*Concepts: 6 core · 5 stretch · 2 contest*

- **6.1 Binary search in a sorted array** [core] · ciu, cpa
  Binary search; Half-open interval invariant for binary search; Lower bound and upper bound; Implement binary search, iteratively and recursively (no open prose)
- **6.2 Binary search on a predicate and on the answer** [core] · ciu, cpa
  Binary search on a monotone predicate; Binary search on the answer; Binary search by descending powers of two [stretch]; Parallel binary search [contest]
- **6.3 Bisection and ternary search** [stretch] · cpa
  Bisection on real numbers; Unimodal function; Ternary search; Ternary search over integers; Golden-section search [contest]

## 7. Bits and data representation

*Concepts: 12 core · 6 stretch · 1 contest*

- **7.1 Binary numbers and machine words** [core] · ciu, cpa, sdp
  Powers of two and machine words; Binary representation and two's complement
- **7.2 Bitwise operators** [core] · ciu, cpa
  Bitwise operators; Shift operators; Setting, clearing, flipping and testing a bit; Power-of-two and divisibility-by-2^k tests
- **7.3 Bit tricks and counting bits** [core] · ciu, cpa
  Lowest-set-bit tricks; Branch-free bit tricks (no open prose); Counting set bits; Counting set bits over 0..n [stretch]
- **7.4 Submasks and Gray codes** [stretch] · cpa, notes
  Enumerating submasks; All masks with all submasks is O(3^n); Gray code; G(n) = n xor (n >> 1); Inverse Gray code; Applications of Gray codes [contest]
- **7.5 Representing numbers and text** [core] · ciu, lt-csbu
  Floating-point representation; Endianness (no open prose); Unicode and character encodings (no open prose)

## 8. Trees and binary search trees

*Concepts: 19 core · 2 stretch*

- **8.1 Trees and binary trees** [core] · ciu, ods, wikipedia, opendsa
  Tree; Binary tree terminology; Recursive binary-tree algorithms
- **8.2 Tree traversals: depth-first and level-order** [core] · ciu, ods
  Depth-first tree traversals: preorder, inorder, postorder; Non-recursive traversal with parent pointers [stretch]; Level-order (breadth-first) tree traversal
- **8.3 Sorted sets and the BST property** [core] · ciu, ods
  SSet interface and successor search; Prefer USet unless order is needed; Binary search tree
- **8.4 Search and insertion** [core] · ciu, ods, wikipedia
  BST search and successor search; BST insertion; BST minimum, maximum and height (no open prose); Inorder successor in a BST
- **8.5 Deletion, validation and cost** [core] · ciu, ods
  BST deletion; Checking whether a binary tree is a BST (no open prose); Implement a BST (no open prose); Cost of an unbalanced BST
- **8.6 Keeping a BST balanced** [core] · ciu, ods, wikipedia, opendsa
  Balanced search trees (the general idea); Tree rotations; Build a perfectly balanced BST from a sorted array; Random binary search trees [stretch]

## 9. Heaps and priority queues

*Concepts: 8 core · 2 stretch*

- **9.1 Priority queues** [core] · ciu, ods
  Priority queue
- **9.2 Binary heaps** [core] · ciu, ods, wikipedia
  Eytzinger layout (implicit binary tree in an array); Heap property; Binary heap; Sift up and sift down
- **9.3 Heapify and heapsort** [core] · ciu, ods
  Linear-time heapify; Heapsort; Implement a max-heap (no open prose)
- **9.4 Meldable heaps** [stretch] · cpa, ods
  Random walks in binary trees; MeldableHeap (randomized meldable heap)
  *Folds:* cpa data_structures/randomized_heap duplicates ODS's MeldableHeap and is folded here.

## 10. Divide and conquer and sorting

*Concepts: 18 core · 7 stretch · 2 contest*

- **10.1 Elementary sorts** [core] · ciu, ods, wikipedia, opendsa
  Comparison-based sorting; Stability in sorting; Selection sort; Insertion sort; Bubble sort
- **10.2 Divide and conquer and recurrences** [core] · ciu, jeffe, notes
  The divide-and-conquer pattern; Solving recurrences by guess and confirm (no open prose); Recursion trees and the master theorem; The Akra-Bazzi method [contest] (no open prose); Linear recurrences by annihilators [contest] (no open prose); Karatsuba multiplication [stretch]
- **10.3 Merge sort** [core] · ciu, jeffe, ods
  Mergesort; Sorting linked lists versus arrays (no open prose)
- **10.4 Quicksort and partitioning** [core] · ciu, jeffe, notes, ods, wikipedia
  In-place partition around a pivot; In-place three-way partitioning; Quicksort; The nuts and bolts problem [stretch] (no open prose); Expected comparisons of randomized quicksort [stretch]; Implement merge sort and quicksort (no open prose)
- **10.5 Selection** [core] · ciu, cpa, jeffe
  Quickselect; Linear-time selection (median of medians) [stretch]
  *Folds:* cpa sequences/k-th (195 words) duplicates quickselect and is folded here.
- **10.6 Lower bounds for sorting** [core] · ciu, notes, ods
  Decision-tree lower bounds (no open prose); Information-theoretic lower bound (no open prose); Lower bound for comparison sorting; Reductions to and from sorting [stretch] (no open prose)
- **10.7 Counting sort and radix sort** [stretch] · ciu, ods
  Counting sort; Radix sort

## 11. Balanced search trees

*Concepts: 1 core · 30 stretch · 3 contest*

- **11.1 AVL, 2-3 and 2-4 trees** [stretch] · ciu, ods, wikipedia, opendsa
  AVL tree; 2-3 search tree; 2-3-4 tree; Adding and removing leaves in a 2-4 tree
- **11.2 Red-black trees** [stretch] · ciu, ods
  Red-black tree properties [core]; Red-black trees simulate 2-4 trees; Left-leaning red-black trees; Red-black insertion fixup; Red-black deletion fixup; Red-black tree performance
- **11.3 Treaps** [stretch] · ciu, cpa, notes, ods
  Treap; Treap insertion and deletion by rotation; Random priorities give expected logarithmic depth (no open prose); Treap split and merge [contest]; Building a treap in O(N) offline [contest]; Implicit treap [contest]
  *Folds:* cpa data_structures/treap shares this home with ODS and jeffe-notes; its split/merge and implicit-key material is contest-tier.
- **11.4 Scapegoat and splay trees** [stretch] · ciu, notes, ods, opendsa
  Partial rebuilding; Lazy deletion and global rebuilding (no open prose); ScapegoatTree; Amortized analysis of scapegoat rebuilding; Rotations, double rotations and splaying (no open prose); Splay tree
- **11.5 Skip lists** [stretch] · ciu, notes, ods
  Skiplist structure; Expected skiplist search path length; Skip list; SkiplistList (indexed skiplist); Skiplist size and height
- **11.6 B-trees** [stretch] · ciu, ods, wikipedia
  External memory model; K-ary tree; B-tree structure; B-tree search; B-tree insertion with splits; B-tree deletion with borrow and merge; B-tree

## 12. Tries and other search structures

*Concepts: 3 core · 4 stretch · 2 contest*

- **12.1 Tries** [core] · ciu, cpa, wikipedia
  Trie (R-way); Trie prefix operations and performance; Ternary search trie (no open prose)
- **12.2 Integer search structures** [stretch] · ciu, ods
  BinaryTrie; XFastTrie [contest]; YFastTrie [contest]; van Emde Boas trees (no open prose)
- **12.3 Augmented and spatial trees** [stretch] · ciu · open prose: none
  Augmenting data structures (no open prose); k-d tree (no open prose)

## 13. Graphs and graph search

*Concepts: 18 core · 1 stretch*

- **13.1 Graphs and modelling** [core] · ciu, jeffe, ods
  Graph (directed, undirected, weighted); Modeling problems as graphs; Graph operations
- **13.2 Adjacency matrices and lists** [core] · ciu, jeffe, ods, wikipedia, opendsa
  Adjacency matrices; Adjacency lists; Graph representations
- **13.3 Whatever-first search** [core] · jeffe
  Whatever-first search; Stack, queue and priority-queue traversals
- **13.4 Breadth-first search** [core] · ciu, cpa, jeffe, ods, sdp
  Breadth-first search on graphs; BFS shortest paths in unweighted graphs; Restoring BFS shortest paths; Applications of BFS
- **13.5 Depth-first search** [core] · ciu, cpa, jeffe, ods
  Depth-first search on graphs; Iterative DFS with an explicit stack; Implement BFS and DFS on both representations (no open prose)
- **13.6 Components, flood fill and bipartiteness** [core] · ciu, cpa, jeffe, ods
  Traversal cost restricted to the reachable part [stretch]; Counting connected components; Flood fill as a graph reduction; Checking whether a graph is bipartite
  *Folds:* cpa graph/search-for-connected-components (327 words, mostly BFS/DFS applications) and graph/bipartite-check (264 words) are thin and folded into this home.

## 14. Depth-first structure

*Concepts: 8 core · 9 stretch*

- **14.1 DFS clocks and edge classification** [core] · cpa, jeffe
  DFS entry/exit times and ancestor test; Classification of edges by DFS
- **14.2 Cycles and topological order** [core] · ciu, cpa, jeffe, wikipedia, opendsa, doocs, oiwiki, icc, mcs2018, aspnes-202
  Cycle detection; Topological order; Topological sort; Kahn's algorithm
  *Folds:* cpa graph/finding-cycle (292 words) is folded into this home.
- **14.3 Bridges and articulation points** [stretch] · cpa
  Low-link values; Bridge (cut edge); Finding bridges in O(N + M); Articulation point (cut vertex); Articulation points in O(N + M)
  *Folds:* cpa graph/cutpoints shares the low-link method of graph/bridge-searching; both live here.
- **14.4 Strongly connected components** [core] · ciu, cpa, jeffe
  Strongly connected component and condensation; Strongly connected components (Kosaraju); Tarjan's SCC algorithm [stretch]; Building the condensation graph [stretch]
- **14.5 Eulerian paths** [stretch] · cpa
  Existence of Eulerian path/cycle; Finding an Eulerian path in O(M)

## 15. Shortest paths

*Concepts: 7 core · 3 stretch · 3 contest*

- **15.1 Shortest-path problems and relaxation** [core] · cpa, jeffe
  Single-source shortest paths problem; Edge relaxation and predecessor array; Ford's generic algorithm: relax tense edges; Negative edges and negative cycles
- **15.2 Dijkstra's algorithm and A*** [core] · ciu, cpa, jeffe
  Dijkstra's algorithm; Dijkstra with a priority queue or set; A* search [stretch] (no open prose)
  *Folds:* cpa graph/dijkstra_sparse (the heap/set implementation) is folded into the Dijkstra home.
- **15.3 Bellman-Ford and negative cycles** [core] · ciu, cpa, jeffe
  Bellman-Ford algorithm; Negative cycle detection with Bellman-Ford [stretch]; Shortest Path Faster Algorithm (SPFA) [contest]
- **15.4 Shortest paths with small weights** [contest] · cpa
  0-1 BFS [stretch]; Dial's algorithm; D'Esopo-Pape algorithm

## 16. Disjoint sets and minimum spanning trees

*Concepts: 6 core · 7 stretch*

- **16.1 Disjoint sets** [stretch] · ciu, cpa, notes
  Disjoint sets (union-find) [core]; Shallow threaded trees (no open prose); DSU for incremental connectivity
- **16.2 Union by rank and path compression** [stretch] · ciu, cpa, notes
  Union by size / rank; Path compression; DSU amortised complexity is O(alpha(n))
- **16.3 Minimum spanning trees and safe edges** [core] · cpa, jeffe
  Minimum spanning tree; Minimum spanning trees with distinct weights; Properties of minimum spanning trees [stretch]; The only MST algorithm: safe and useless edges
- **16.4 Prim, Kruskal and Boruvka** [core] · ciu, cpa, jeffe
  Minimum spanning tree: Prim's algorithm; Minimum spanning tree: Kruskal's algorithm; Boruvka's algorithm [stretch]
  *Folds:* cpa graph/mst_kruskal_with_dsu (215 words) duplicates mst_kruskal's improved implementation and is folded into Kruskal.

## 17. Backtracking

*Concepts: 10 core · 3 stretch*

- **17.1 The backtracking pattern** [core] · ciu, jeffe
  The backtracking pattern; n Queens by backtracking; Game trees and minimax [stretch]
- **17.2 Generating permutations, subsets and combinations** [core] · wikipedia, doocs, icc, trekhleb
  Generating all permutations by backtracking; Next permutation in lexicographic order; Heap's algorithm [stretch]; Generating all subsets; Generating k-combinations by backtracking
  *Folds:* cpa combinatorics/generating_combinations stays with stars and bars (40.5), where its next-combination row lives; Wikipedia's k-combination enumeration joins it there.
- **17.3 Subset sum and text segmentation** [core] · jeffe
  Subset sum by backtracking; Text segmentation (word break) by backtracking; Index formulation of a recurrence
- **17.4 Recursive formulations of optimisation problems** [core] · jeffe
  Longest increasing subsequence by backtracking; Optimal binary search tree recurrence [stretch]

## 18. Dynamic programming

*Concepts: 26 core · 6 stretch · 3 contest*

- **18.1 Memoization and tabulation** [core] · ciu, cpa, jeffe
  Dynamic programming: overlapping subproblems; Memoization; Bottom-up (tabulated) DP; Dynamic programming is smart recursion; Recognising a DP problem (no open prose); Classic DP problems [stretch]
- **18.2 Fibonacci numbers: from recursion to logarithmic time** [core] · cpa, jeffe
  Fibonacci numbers; Fibonacci in linear time; Fibonacci via matrix exponentiation [stretch]
- **18.3 Coin change and grid paths** [core] · wikipedia, doocs, algo-expl, icc, trekhleb, anfp, dmoi3
  Coin change: fewest coins by DP; Coin change: counting the ways; Counting grid paths; Counting grid paths around obstacles; Minimum path sum in a grid
- **18.4 Text segmentation and longest increasing subsequence** [core] · cpa, jeffe
  Text segmentation by dynamic programming; Longest increasing subsequence by DP; Restoring a DP solution with parent pointers; LIS in O(n log n) with binary search; LIS variants: non-decreasing, counting, covering [stretch]
- **18.5 Maximum subarray** [core] · cpa
  Maximum subarray sum problem; Maximum subarray via prefix sums and running minimum; Kadane's algorithm; Maximum-sum submatrix [stretch]; Maximum-average subarray with a length bound [contest]
- **18.6 Subset sum and knapsack** [core] · cpa, jeffe
  Subset sum by DP (pseudo-polynomial); 0-1 knapsack; One-dimensional knapsack and iteration order; Complete (unbounded) knapsack; Bounded knapsack by binary grouping [contest]; Bounded knapsack by monotone queue [contest]
- **18.7 Edit distance and longest common subsequence** [core] · ciu, cpa, jeffe
  Edit distance; Longest common subsequence; RNA secondary structure (no open prose)
- **18.8 DP on trees and optimal binary search trees** [stretch] · jeffe
  Dynamic programming on trees; Optimal binary search trees by DP

## 19. Dynamic programming on graphs

*Concepts: 3 core · 7 stretch · 3 contest*

- **19.1 DP in directed acyclic graphs** [stretch] · jeffe
  Memoization and dynamic programming in dags; Shortest paths in dags
- **19.2 All-pairs shortest paths from single-source runs** [contest] · jeffe
  All-pairs shortest paths [core]; APSP by repeated single-source [stretch]; Reweighting with vertex potentials; Johnson's algorithm
- **19.3 Floyd-Warshall** [core] · ciu, cpa, jeffe
  Floyd-Warshall algorithm; Restoring Floyd-Warshall paths; Floyd-Warshall with negative cycles [stretch]; Finding any negative cycle [stretch]
  *Folds:* cpa graph/finding-negative-cycle-in-graph largely duplicates the negative-cycle parts of bellman_ford and all-pair-shortest-path-floyd-warshall and is folded here.
- **19.4 Path-length DP and matrix products** [stretch] · ciu, cpa, jeffe
  APSP by dynamic programming on path length; Counting paths of fixed length by matrix power; Funny (min-plus) matrix multiplication [contest]

## 20. Greedy algorithms

*Concepts: 5 core · 5 stretch · 6 contest*

- **20.1 Greedy choices and exchange arguments** [core] · jeffe, wikipedia, doocs, anfp
  Warning: greed is stupid; Greedy correctness by exchange argument; Storing files on tape [stretch]; Class (interval) scheduling: earliest finish first; Stable matching (Gale-Shapley) [stretch]
- **20.2 Merging intervals and meeting rooms** [core] · doocs
  Merging overlapping intervals; Interval partitioning: minimum rooms as maximum overlap
- **20.3 Huffman codes** [stretch] · ciu, jeffe
  Prefix-free codes as binary trees; Huffman codes
- **20.4 Greedy scheduling and matroids** [contest] · cpa, notes
  Maximum number of jobs meeting deadlines [stretch]; Matroids and the greedy algorithm (no open prose); Scheduling unit jobs with deadlines (no open prose); Single-machine scheduling with linear penalties; Exponential and identical penalty cases; Livshits-Kladov theorem; Johnson's rule for two-machine flow shop
  *Folds:* cpa schedules/schedule_one_machine and schedule_two_machines are contest-tier and share this home with jeffe-notes E-matroids.

## 21. String searching

*Concepts: 10 core · 7 stretch · 5 contest*

- **21.1 Substring search: brute force and Boyer-Moore** [core] · ciu, notes · open prose: none
  Brute-force substring search (no open prose); Boyer-Moore (and Horspool) (no open prose)
- **21.2 String hashing and Rabin-Karp** [core] · ciu, cpa, notes, ods
  Polynomial rolling hash of a string; Substring hash from prefix hashes; Grouping duplicate strings by hash [stretch]; Collision probability and double hashing [stretch]; Counting distinct substrings by hashing [contest]; Rabin-Karp
  *Folds:* cpa string/rabin-karp (176 words) is a thin application of string/string-hashing and is folded here.
- **21.3 Prefix function and Knuth-Morris-Pratt** [core] · ciu, cpa, notes
  String matching with a finite-state machine (no open prose); Prefix function; Computing the prefix function in O(n); Knuth-Morris-Pratt; Shortest period / string compression [stretch]; Counting occurrences of each prefix [contest]; KMP automaton [contest]; Counting distinct substrings incrementally [contest]
- **21.4 The Z-function** [stretch] · cpa
  Z-function; Computing the Z-function in O(n); Pattern search with the Z-function
- **21.5 Suffix arrays** [core] · ciu, cpa
  Suffix array; Suffix array by prefix doubling in O(n log n) [stretch]; Substring search and comparison with a suffix array [contest]

## 22. Probability and randomized algorithms

*Concepts: 2 core · 9 stretch · 1 contest*

- **22.1 Distributions at work** [stretch] · notes · open prose: none
  Common distributions: uniform, Bernoulli, binomial, geometric (no open prose); Removing bias from coin flips (no open prose); Coupon collecting (Pokemon collecting) (no open prose)
- **22.2 Las Vegas and Monte Carlo algorithms** [core] · notes · open prose: none
  Deterministic vs. randomized algorithms; expected running time [stretch] (no open prose); Generating random permutations (shuffling) (no open prose)
- **22.3 Tail bounds** [stretch] · ciu, notes · open prose: none
  Markov's inequality (no open prose); Chebyshev's inequality (no open prose); Chernoff bounds (no open prose); Treap depth with high probability [contest] (no open prose)
- **22.4 Markov chains and random walks** [stretch] · ciu · open prose: none
  Markov chains [core] (no open prose); Random walks (no open prose); Markov text generation (no open prose)

## 23. Lower bounds and intractability

*Concepts: 6 core · 18 stretch · 7 contest*

- **23.1 Adversary arguments** [stretch] · notes · open prose: none
  Finding the maximum needs n-1 comparisons (no open prose); Adversary arguments (no open prose); Finding the minimum and maximum: ceil(3n/2) - 2 (no open prose); Evasive graph properties [contest] (no open prose)
- **23.2 P, NP and NP-hardness** [core] · ciu, jeffe
  Circuit satisfiability [stretch]; P, NP and NP-completeness; NP-hard, NP-easy and NP-complete; Cook-Levin: SAT is NP-hard [stretch]; Beyond NP: PSPACE, EXP and decidability [contest]
- **23.3 NP-hardness by reduction** [stretch] · ciu, jeffe
  Polynomial-time reductions [core] (no open prose); The NP-hardness proof pattern; 3SAT is NP-hard; Maximum independent set is NP-hard; Clique and vertex cover are NP-hard; Graph 3-colouring is NP-hard; Hamiltonian cycle (and TSP) is NP-hard; Subset sum is NP-hard
- **23.4 Recognising NP-hard problems** [stretch] · ciu, jeffe
  Recognising NP-complete problems in disguise [core] (no open prose); A catalog of NP-hard problems; Choosing the right problem to reduce from; A frivolous example: international draughts [contest]
- **23.5 Approximation algorithms** [stretch] · ciu, notes · open prose: none
  Approximation algorithms and ratios [core] (no open prose); Greedy load balancing (no open prose); Vertex cover approximation (no open prose); Greedy set cover and hitting set (no open prose); Traveling salesman: hardness and metric approximation (no open prose); k-center clustering [contest] (no open prose); An FPTAS for subset sum [contest] (no open prose)
- **23.6 Exact exponential and parameterised algorithms** [contest] · ciu, notes · open prose: none
  Fixed-parameter algorithms [core] (no open prose); Faster exponential algorithms for 3SAT (no open prose); Faster exponential algorithms for maximum independent set (no open prose)

## 24. Approaching a system design question

*Concepts: 9 core*

- **24.1 The four-step approach** [core] · ciu, sdp
  Four-step system design interview approach; Scoping use cases, constraints and assumptions; Designing core components per use case; Iterative scaling loop
- **24.2 Back-of-the-envelope estimation** [core] · ciu, sdp
  Latency numbers every programmer should know; Requests-per-month conversion; Back-of-the-envelope estimation
- **24.3 Performance versus scalability, latency versus throughput** [core] · sdp
  Performance vs scalability; Latency vs throughput

## 25. Availability and consistency

*Concepts: 9 core · 2 stretch*

- **25.1 Distributed systems and the CAP theorem** [core] · ciu, sdp, wp
  Fallacies of distributed computing [stretch]; CAP theorem
- **25.2 Consistency patterns** [core] · ciu, sdp, wp, raft-site
  Weak consistency; Eventual consistency; Strong consistency; CP vs AP systems; Consensus: Paxos and Raft [stretch]
- **25.3 Availability patterns** [core] · sdp
  Active-passive fail-over; Active-active fail-over; Availability in nines; Availability in sequence vs in parallel

## 26. Scaling the web tier

*Concepts: 19 core · 3 stretch*

- **26.1 DNS and content delivery networks** [core] · sdp
  Domain name system; DNS record types [stretch]; DNS traffic routing [stretch]; Content delivery network; Push vs pull CDNs
- **26.2 Load balancers and reverse proxies** [core] · sdp
  Load balancer; Load balancer routing methods; Layer 4 vs layer 7 load balancing; Reverse proxy (web server); Load balancer vs reverse proxy
- **26.3 Horizontal scaling and stateless servers** [core] · ciu, sdp, aosa
  Horizontal vs vertical scaling; Stateless web and application servers; Scaling a web service: clones, databases, caches, asynchrony; Autoscaling
- **26.4 The application layer and microservices** [core] · sdp
  Separating web and application layers; Microservices; Service discovery [stretch]
- **26.5 Object storage, monitoring and security** [core] · sdp
  Object store for blobs; Offloading static content to an object store and CDN; Monitoring and automated operations; Security basics; Locking down hosts and network

## 27. Databases

*Concepts: 17 core · 5 stretch*

- **27.1 Relational databases** [core] · ciu, sdp
  ACID transactions; Database normalisation [stretch] (no open prose); Database indices; Tightening the schema [stretch]
- **27.2 Replication** [core] · sdp
  Master-slave replication; Master-master replication; Replication drawbacks and lag; Read replicas with read/write splitting
- **27.3 Federation, sharding and denormalisation** [core] · ciu, sdp, wp
  Federation (functional partitioning); Sharding; Denormalization; SQL tuning [stretch]; Consistent hashing [stretch]; Distributed hash tables; Keeping hot data in the database, the rest in a warehouse
- **27.4 NoSQL stores** [core] · ciu, sdp, aosa
  NoSQL and BASE; Key-value store; Document store; Wide column store; Graph database; NoSQL patterns [stretch]; SQL or NoSQL

## 28. Caching and asynchrony

*Concepts: 14 core · 3 stretch*

- **28.1 Caches and where to put them** [core] · ciu, sdp, wp
  Caching; Where to cache; In-memory application cache; What to cache: query level vs object level; Redis as an in-memory data store [stretch]; Spreading a cache over many machines
- **28.2 Cache update strategies** [core] · sdp
  Cache-aside (lazy loading); Write-through cache; Write-behind (write-back) cache; Refresh-ahead cache [stretch]; Cache invalidation and TTL
- **28.3 Message queues and back pressure** [core] · ciu, sdp
  Asynchronous workflows; Message queues; Task queues [stretch]; Back pressure
- **28.4 Batch processing with MapReduce** [core] · sdp
  MapReduce aggregation over logs; Distributed sort as a second MapReduce step

## 29. Worked designs

*Concepts: 18 core · 6 stretch*

- **29.1 Pastebin and Bit.ly** [core] · sdp
  Base62 encoding; Short link generation by hashing; Design Pastebin / Bit.ly
- **29.2 Twitter timeline and search** [core] · sdp
  Fan-out on write to home timelines; Skipping fan-out for highly followed users; Bounding the timeline cache; Reverse (inverted) index; Search query processing and scatter-gather; Design the Twitter timeline and search
- **29.3 A web crawler** [core] · sdp
  Crawl loop over a prioritised link store; Duplicate URL and content detection; Recrawl freshness policy; Crawler throughput optimisations; Design a web crawler
- **29.4 Mint.com** [stretch] · sdp
  Categorising transactions by seller; Budget templates with stored overrides; Design Mint.com
- **29.5 A social graph** [stretch] · ciu, sdp
  BFS over a sharded graph with a lookup service [core]; Speeding up distributed BFS; Distributed graph algorithms (no open prose); Design the data structures for a social network
- **29.6 A query cache** [core] · sdp
  Design a key-value cache for search query results
- **29.7 Sales rank by category** [core] · sdp
  Design Amazon's sales rank by category
- **29.8 Scaling to millions of users on AWS** [core] · sdp
  Design a system that scales to millions of users on AWS

## 30. Range queries

*Concepts: 16 stretch · 18 contest*

- **30.1 Range minimum and sparse tables** [stretch] · cpa
  Range minimum query problem; Sparse table; Sparse table range query by power-of-two decomposition; O(1) range minimum with a sparse table; Structures for O(1) associative range queries [contest]
  *Folds:* cpa sequences/rmq (361 words) is an index of RMQ approaches and is folded here; its rmq-approaches row sits in the sqrt section, after the structures it compares.
- **30.2 Fenwick trees** [stretch] · cpa
  Fenwick tree; Fenwick tree for point update, range sum; Linear-time Fenwick construction [contest]; Fenwick tree for prefix minimum [contest]; Fenwick range update with point / range query
- **30.3 Segment trees** [stretch] · cpa
  Segment tree; Segment tree range query and point update; Segment tree with custom node values; Searching by descending the segment tree [contest]
- **30.4 Segment tree extensions** [contest] · cpa
  Lazy propagation [stretch]; Merge sort tree; 2D segment tree; Persistent segment tree; Dynamic (implicit) segment tree; LIS with a prefix-maximum structure [stretch]
- **30.5 Sqrt decomposition** [contest] · cpa
  Sqrt decomposition for range queries [stretch]; Mo's algorithm; Sqrt tree; Sqrt tree updates; Choosing an RMQ structure [stretch]
  *Folds:* cpa data_structures/sqrt-tree builds on sqrt_decomposition and shares this home.
- **30.6 DSU tricks and offline processing** [contest] · cpa
  Painting subarrays offline with DSU; DSU with distance/parity to the representative; Arpa's trick: offline RMQ with DSU; Small-to-large merging; Undoing operations with a change stack (rollback DSU); Offline deletion via segment tree over time
  *Folds:* cpa data_structures/deleting_in_log_n (236 words) is folded here with the DSU applications.
- **30.7 MEX queries** [stretch] · cpa
  MEX of a sequence; Computing MEX in O(N); MEX under point updates [contest]

## 31. Tree algorithms

*Concepts: 3 stretch · 14 contest*

- **31.1 Lowest common ancestor** [stretch] · cpa
  Lowest common ancestor; LCA via Euler tour and range minimum; Binary lifting for LCA; Binary lifting with depths (supports adding leaves) [contest]; LCA with O(n) space jump pointers [contest]
- **31.2 Linear-time LCA and RMQ** [contest] · cpa
  Farach-Colton and Bender LCA; Static RMQ in O(N)/O(1) via Cartesian tree; Tarjan's offline LCA
  *Folds:* cpa graph/rmq_linear and graph/lca_tarjan are short companions of lca_farachcoltonbender and share this home.
- **31.3 Heavy-light and centroid decomposition** [contest] · cpa
  Heavy-light decomposition; Path queries with HLD and segment trees; Centroid of a tree; Centroid decomposition; Counting painted edges on tree paths with Euler tour
- **31.4 Prufer codes and counting trees** [contest] · cpa
  Prufer code; Prufer code and tree restoration in linear time; Cayley's formula; Ways to make a graph connected

## 32. Network flow and matching

*Concepts: 12 stretch · 23 contest*

- **32.1 Flows, cuts and the max-flow min-cut theorem** [stretch] · cpa, jeffe
  Flow networks and (s,t)-flows; (s,t)-cuts and capacity; Residual graphs and augmenting paths; Maxflow-mincut theorem; Combining and decomposing flows [contest]
- **32.2 Augmenting paths: Ford-Fulkerson and Edmonds-Karp** [stretch] · ciu, cpa, jeffe
  Ford-Fulkerson augmenting paths; Integral flow theorem; Edmonds-Karp augmenting-path rules
- **32.3 Faster maximum flow** [contest] · cpa, jeffe
  Dinic's algorithm [stretch]; Dinic on unit networks; MPM maximum flow; Preflow, excess and valid labeling; Push-relabel maximum flow; Highest-label push-relabel; Faster maximum-flow algorithms (survey)
  *Folds:* cpa graph/push-relabel-faster (168 words) is folded into push-relabel.
- **32.4 Bipartite matching** [stretch] · cpa, jeffe
  Matching, maximal and maximum matching, augmenting path; Berge's lemma; Kuhn's algorithm for maximum bipartite matching; Bipartite matching via maximum flow
- **32.5 Reductions to flow** [contest] · jeffe
  Edge-disjoint paths; Vertex capacities and vertex-disjoint paths; Tuple selection (exam scheduling); Disjoint-path covers of dags; Baseball elimination; Project selection by minimum cut
- **32.6 Demands and minimum-cost flow** [contest] · cpa, notes
  Unbalanced flows: supplies and demands (no open prose); Pseudoflows and augmenting between imbalances (no open prose); Flows with lower bounds (demands); Minimal flow with demands by binary search; Minimum-cost circulations and cycle canceling (no open prose); Minimum-cost flow by successive shortest paths; Node potentials and reduced costs (no open prose)
- **32.7 The assignment problem** [contest] · cpa
  Assignment problem; Hungarian algorithm; Assignment problem via min-cost flow
  *Folds:* cpa graph/Assignment-problem-min-flow (425 words) overlaps hungarian-algorithm and is folded here.

## 33. More graph algorithms

*Concepts: 2 stretch · 11 contest*

- **33.1 2-SAT** [contest] · cpa
  2-CNF and the implication graph; 2-SAT
- **33.2 Online bridges and strong orientation** [contest] · cpa
  Online bridge finding with 2-edge-connected components; Strong orientation
- **33.3 Edge and vertex connectivity** [contest] · cpa
  Edge and vertex connectivity; Whitney inequalities; Computing connectivity with max flow
- **33.4 Global minimum cut** [stretch] · cpa, notes
  Global minimum cut and edge contraction; Stoer-Wagner global minimum cut [contest]; Karger's contraction algorithm (no open prose); Karger-Stein recursive contraction [contest] (no open prose)
- **33.5 Second-best spanning trees** [contest] · cpa
  Second-best MST is one edge swap from the MST; Second-best minimum spanning tree

## 34. Advanced string algorithms

*Concepts: 3 stretch · 16 contest*

- **34.1 LCP arrays and substring counting** [contest] · cpa
  LCP array (Kasai); Distinct substrings from suffix array and LCP
- **34.2 Aho-Corasick** [contest] · cpa
  Aho-Corasick automaton; Multi-pattern search with Aho-Corasick; Search and DP over the Aho-Corasick automaton
- **34.3 Suffix trees and suffix automata** [contest] · cpa
  Suffix tree (Ukkonen's algorithm); Suffix automaton; endpos classes and suffix links; Online linear-time suffix automaton construction; Suffix automaton size bounds; Suffix automaton applications
  *Folds:* cpa string/suffix-tree-ukkonen (213 words) is a code-only article and is folded here.
- **34.4 Palindromes: Manacher's algorithm** [stretch] · cpa
  Palindrome radii d_odd and d_even; Manacher's algorithm; Manacher with interleaved separators
- **34.5 Repetitions and Lyndon words** [contest] · cpa
  Repetitions (squares) in a string; Main-Lorentz algorithm; Lyndon word and Lyndon factorization; Duval's algorithm; Smallest cyclic shift

## 35. Advanced dynamic programming

*Concepts: 13 contest*

- **35.1 Divide-and-conquer and Knuth optimisations** [contest] · cpa, notes
  Monotone optimal split point; Divide and conquer DP optimization; Quadrangle inequality; Knuth's optimization; Total monotonicity and the SMAWK algorithm (no open prose)
- **35.2 Saving space and time** [contest] · notes · open prose: none
  Saving space by divide and conquer (Hirschberg) (no open prose); Saving time with sparseness (no open prose); The Four Russians speedup (no open prose)
- **35.3 Profile and bitmask DP** [contest] · cpa
  DP on broken profile; Non-attacking bishops by diagonal DP
- **35.4 DP over automata and grammars** [contest] · notes · open prose: none
  DFA minimization by dynamic programming (no open prose); NFA acceptance and regular-expression matching (no open prose); Context-free parsing (CYK) (no open prose)

## 36. Sketches and probabilistic data structures

*Concepts: 5 stretch*

- **36.1 Bloom filters** [stretch] · ciu, notes, wp
  Bloom filters
- **36.2 Streaming sketches** [stretch] · ciu, notes, wp
  The streaming model (no open prose); Count-min sketch; HyperLogLog
- **36.3 Locality-sensitive hashing** [stretch] · ciu, wp
  Locality-sensitive hashing (simhash)

## 37. Number theory: divisibility and primes

*Concepts: 7 core · 23 stretch · 9 contest*

- **37.1 Greatest common divisors** [core] · cpa
  Greatest common divisor; Euclidean algorithm; Lame's theorem: Euclid runs in O(log min(a,b)) [stretch]; Least common multiple via GCD; Binary GCD (Stein's algorithm) [contest]
- **37.2 Extended Euclid and Diophantine equations** [stretch] · cpa
  Bezout's identity; Extended Euclidean algorithm; Iterative extended Euclid; Linear Diophantine equation in two variables; Solvability and one solution of ax+by=c; General solution of a linear Diophantine equation; Counting Diophantine solutions in a box [contest]; Diophantine solution minimising x+y [contest]
- **37.3 The sieve of Eratosthenes** [core] · cpa
  Sieve of Eratosthenes; Sieve runs in O(n log log n) [stretch]; Sieving only by primes up to sqrt(n); Odd-only sieve [stretch]; Bit-packed sieve and memory trade-offs [contest]
- **37.4 Segmented and linear sieves** [stretch] · cpa
  Segmented sieve; Primes in a range [L, R]; Linear sieve; Each composite is marked exactly once [contest]; Least prime factor table for fast factorisation
  *Folds:* cpa algebra/prime-sieve-linear overlaps sieve-of-eratosthenes#linear-time-modification and shares this home.
- **37.5 Primality and factorisation by trial division** [core] · cpa
  Primality by trial division; Prime factorisation by trial division; Wheel factorisation [contest]; Trial division by precomputed primes [stretch]; Fermat's factorisation method [contest]
- **37.6 Divisor functions** [stretch] · cpa
  Multiplicative functions; Number of divisors formula; Sum of divisors formula
- **37.7 Euler's totient function** [stretch] · cpa
  Euler's totient function; Totient product formula; Computing phi(n) by factorisation; Totients of 1..n by sieve; Gauss's divisor-sum identity [contest]
- **37.8 Euler's and Fermat's theorems** [stretch] · cpa
  Euler's theorem; Fermat's little theorem; Exponent reduction for non-coprime bases [contest]

## 38. Number theory: modular arithmetic

*Concepts: 12 stretch · 23 contest*

- **38.1 Modular inverses** [stretch] · cpa
  Modular multiplicative inverse; Inverse via extended Euclid; Inverse via Fermat/Euler; Linear-time inverses of 1..m-1 mod prime [contest]; Batch inversion with prefix products [contest]
- **38.2 Linear congruences** [stretch] · cpa
  Linear congruence a*x = b (mod n); Solving a linear congruence; Linear congruence as a Diophantine equation
- **38.3 Probabilistic primality and Pollard's methods** [contest] · cpa
  Fermat primality test; Miller-Rabin primality test; Pollard's p-1 method; Pollard's rho algorithm; Brent's cycle-finding in Pollard rho
- **38.4 The Chinese remainder theorem** [stretch] · ciu, cpa
  Chinese Remainder Theorem; CRT for two moduli; Inductive CRT for many moduli; Direct CRT construction [contest]; CRT with non-coprime moduli [contest]
- **38.5 Garner's algorithm and residue number systems** [contest] · cpa
  Mixed radix representation; Garner's algorithm; Residue number system for big integers
  *Folds:* cpa algebra/garners-algorithm is summarised by chinese-remainder-theorem#garners-algorithm and big-integer; one home.
- **38.6 Factorials modulo p** [stretch] · cpa
  Legendre's formula; Largest power of a composite k dividing n!; Factorial with p-factors removed, mod p [contest]; Computing n! mod p without p-factors [contest]
  *Folds:* cpa algebra/factorial-divisors (256 words) duplicates factorial-modulo#multiplicity-of-p and is folded here.
- **38.7 Discrete logarithms** [contest] · cpa
  Discrete logarithm problem; Meet in the middle (as used in BSGS) [stretch]; Baby-step giant-step; BSGS with incremental powers and hashing; Discrete log for non-coprime a and m
- **38.8 Primitive roots and discrete roots** [contest] · cpa
  Primitive root modulo n; Existence of primitive roots; Finding a primitive root; Discrete root via primitive root and discrete log; All discrete roots from one

## 39. Number theory: representations and fast arithmetic

*Concepts: 7 stretch · 30 contest*

- **39.1 Fast modular multiplication** [contest] · cpa
  Binary multiplication modulo m; Montgomery representation; Montgomery reduction (REDC); Inverse modulo 2^k by Newton iteration; Fast conversion into Montgomery form
- **39.2 Powers of permutations, matrices and 2^d** [contest] · cpa
  Applying a permutation k times [stretch]; Geometric transformations as matrix powers; Exponentiation mod 2^d by factoring; Logarithm table via Pohlig-Hellman for 2^d
  *Folds:* cpa algebra/factoring-exp shares this home with the binary-exp applications.
- **39.3 Arbitrary-precision arithmetic** [stretch] · cpa
  Big integers as digit arrays; Schoolbook big-integer addition and subtraction; Big-integer multiplication; Big integer divided by a short integer; Exact fraction arithmetic; Numbers stored as prime factorisations [contest]; Big integers as residues modulo primes [contest]; Floating point with a separate exponent [contest]
- **39.4 Balanced ternary** [contest] · cpa
  Balanced ternary; Converting to balanced ternary
- **39.5 Fibonacci identities** [contest] · cpa
  Fibonacci identities; Zeckendorf representation and Fibonacci coding; Binet's formula [stretch]; Fast doubling for Fibonacci; Periodicity of Fibonacci modulo p
- **39.6 Continued fractions** [contest] · cpa
  Continued fraction representation; Computing a continued fraction by Euclid; Convergents and their recurrence; Best rational approximation; Calkin-Wilf tree; Linear fractional transformations
- **39.7 The Stern-Brocot tree and Farey sequences** [contest] · cpa
  Stern-Brocot tree; Ordering, irreducibility and completeness; Stern-Brocot path as a number system; Logarithmic Stern-Brocot search; Stern-Brocot path from a continued fraction; Farey sequences; Length of a Farey sequence
  *Folds:* cpa algebra/continued-fractions#stern-brocot-tree overlaps others/stern_brocot_tree_farey_sequences; one home.

## 40. Combinatorics

*Concepts: 25 stretch · 18 contest*

- **40.1 Binomial coefficients** [stretch] · cpa
  Binomial coefficient and binomial theorem; Factorial formula and Pascal recurrence; Binomial identities; Overflow-safe multiplicative computation; Pascal's triangle table; Binomial coefficients modulo a large prime; Binomial coefficients modulo a prime power or arbitrary m [contest]; Lucas's theorem [contest]
- **40.2 Catalan numbers** [stretch] · cpa
  Catalan numbers; Objects counted by Catalan numbers; Catalan recurrence; Catalan closed form by reflection; Number of balanced bracket sequences
  *Folds:* cpa combinatorics/bracket_sequences#counting duplicates catalan-numbers' bracket interpretation; the two articles share this home and the next.
- **40.3 Generating bracket sequences** [stretch] · cpa
  Next balanced sequence in lexicographic order; Generating all balanced sequences; Index and k-th balanced sequence [contest]
- **40.4 Inclusion-exclusion** [stretch] · cpa
  Inclusion-exclusion principle; Proof of inclusion-exclusion; Counting elements in exactly r sets [contest]; Counting via the complement of bad events; Integers in [1, r] coprime to n; Lattice paths avoiding obstacles [contest]; Inclusion-exclusion over square-free divisors [contest]; Derangements
- **40.5 Stars and bars and k-combinations** [stretch] · cpa, wikipedia
  Stars and bars; Compositions into positive parts; Sums with lower bounds; Sums with upper bounds [contest]; Next k-combination in lexicographic order; k-combinations with minimal change via Gray codes [contest]
- **40.6 Burnside's lemma and Polya enumeration** [contest] · cpa
  Counting objects up to symmetry; Burnside's lemma; Polya enumeration theorem; Counting necklaces; Burnside by generating the group programmatically
- **40.7 Counting graphs and puzzle states** [contest] · cpa
  Number of labelled graphs; Number of connected labelled graphs; Labelled graphs with k components; Solvability of the 15 puzzle
- **40.8 The Josephus problem** [stretch] · cpa
  Josephus problem; Josephus recurrence in O(n); Josephus in O(k log n) for small k [contest]; Closed form for k = 2

## 41. Game theory

*Concepts: 2 stretch · 7 contest*

- **41.1 Games on graphs** [contest] · cpa
  Win/lose/draw on arbitrary game graphs; Policeman and thief game
- **41.2 Nim** [stretch] · cpa
  Impartial games; Nim: winning iff the xor of pile sizes is non-zero; Misere Nim [contest]; Nim with increases [contest]
- **41.3 The Sprague-Grundy theorem** [contest] · cpa
  Sprague-Grundy theorem; Grundy values of sums of games; Finding patterns in Grundy tables

## 42. Linear algebra, polynomials and the FFT

*Concepts: 4 stretch · 25 contest*

- **42.1 Gaussian elimination** [contest] · cpa
  Gauss-Jordan elimination; Pivot selection (partial pivoting); Detecting no, one or infinitely many solutions; Complexity of Gaussian elimination; Gaussian elimination mod 2 with bitsets; Refining the solution numerically
- **42.2 Determinants and rank** [contest] · cpa
  Determinant by Gaussian elimination; Determinant via LU (Crout/Kraut) decomposition; Rank of a matrix; Rank by Gaussian elimination; Kirchhoff's matrix tree theorem
  *Folds:* cpa linear_algebra/determinant-gauss (200 words), determinant-kraut (245) and rank-matrix (228) are thin and share this home; graph/kirchhoff-theorem joins as the application.
- **42.3 Polynomials and the discrete Fourier transform** [stretch] · ciu, cpa, notes
  Polynomial representations (no open prose); Converting by Vandermonde matrices (no open prose); Discrete Fourier transform
- **42.4 The fast Fourier transform** [contest] · ciu, cpa, notes
  Fast Fourier transform [stretch]; Inverse FFT; Fast polynomial multiplication; In-place iterative FFT with bit reversal
- **42.5 FFT variants and applications** [contest] · cpa
  Number theoretic transform; Polynomial multiplication for an arbitrary modulus; Problems reduced to convolution
- **42.6 Operations on power series** [contest] · cpa
  Formal power series; Power-series inverse by Newton/Hensel lifting; Polynomial Euclidean division; Newton's method on power series; Logarithm, exponent and powers of a series; Multipoint evaluation and interpolation; Chirp-z transform; Polynomial GCD and resultant

## 43. Numerical methods and optimisation

*Concepts: 3 stretch · 14 contest*

- **43.1 Newton's method** [stretch] · cpa
  Newton's method for root finding; Square roots by Newton's method
- **43.2 Numerical integration** [contest] · cpa
  Composite Simpson's rule; Error of Simpson's rule
- **43.3 Simulated annealing** [contest] · cpa
  State-space optimisation with an energy function; Neighbouring states; Simulated annealing; Tuning temperature and decay
- **43.4 Linear programming and duality** [contest] · ciu, notes · open prose: none
  Linear programming [stretch] (no open prose); The geometry of linear programs (no open prose); Formulating problems as linear programs (no open prose); Linear programming duality (no open prose); Complementary slackness (no open prose)
- **43.5 The simplex method and LP rounding** [contest] · notes · open prose: none
  The simplex algorithm (no open prose); Network simplex (no open prose); Linear expected time in fixed dimension (no open prose); LP rounding for weighted vertex cover (no open prose)

## 44. Computational geometry: primitives

*Concepts: 14 stretch · 19 contest*

- **44.1 Points, vectors, dot and cross products** [stretch] · cpa
  Points as vectors; Dot product; Geometry with the dot product; Cross product and triple product; Orientation and collinearity via cross product
- **44.2 Lines and their intersections** [contest] · cpa
  Line equation through two points [stretch]; Normalising integer and real line equations; Parametric line in 3D and higher; Intersecting parametric lines; Intersection of two lines by Cramer's rule; Intersecting three planes
  *Folds:* cpa geometry/lines-intersection (306 words) and segment-to-line share this home.
- **44.3 Segments** [stretch] · cpa
  Do two segments intersect?; Computing the intersection of two segments [contest]; Length of a union of segments (Klee)
  *Folds:* cpa geometry/check-segments-intersection (167 words) and length-of-segments-union (158 words) are thin and share this home with segments-intersection.
- **44.4 Circles and enclosing circles** [contest] · cpa
  Circle-line intersection; Circle-circle intersection; Number of common tangents of two circles; Finding common tangents; Minimum enclosing circle; In-circle tests for 2- and 3-point circles; Welzl's randomized algorithm
- **44.5 Areas and Pick's theorem** [stretch] · cpa
  Signed area of a triangle; Area of a simple polygon (shoelace); Pick's theorem; Proof of Pick's theorem [contest]; No Pick formula in 3D (Reeve tetrahedron) [contest]
  *Folds:* cpa geometry/oriented-triangle-area (236 words) and area-of-simple-polygon (168 words) are thin and share this home.
- **44.6 Lattice points** [contest] · cpa
  Lattice points under a line (floor sum); Lattice points in a polygon with arbitrary vertices; Geometric interpretation: convex hull of lattice points
- **44.7 Manhattan distance** [stretch] · cpa
  Manhattan distance; Farthest pair in Manhattan distance; Rotating Manhattan into Chebyshev distance; Manhattan minimum spanning tree [contest]

## 45. Computational geometry: algorithms

*Concepts: 5 stretch · 25 contest*

- **45.1 Convex hulls** [stretch] · ciu, cpa
  Convex hull; Graham's scan; Andrew's monotone chain
- **45.2 Convex polygons and Minkowski sums** [contest] · cpa
  Point in convex polygon in O(log n); Minkowski sum; Minkowski sum of convex polygons in linear time; Distance between convex polygons via Minkowski sum
- **45.3 The convex hull trick and Li Chao trees** [contest] · cpa
  Minimum over lines in DP transitions; Convex hull trick; Li Chao tree
- **45.4 Sweep lines and point location** [contest] · cpa
  Detecting an intersecting pair by sweep line; Offline point location in O(log n); Online point location with persistent trees; Vertical decomposition; Area of a union of triangles; Intersecting convex polygons by stripes
- **45.5 Faces of planar graphs** [contest] · cpa
  Euler's formula for planar graphs; Finding faces by next-edge traversal; Building a planar graph from segments
- **45.6 The closest pair of points** [stretch] · cpa
  Closest pair of points by divide and conquer; Constant candidates in the strip; Randomized expected-linear closest pair [contest]; Minimum-perimeter triangle [contest]
- **45.7 Delaunay triangulations and Voronoi diagrams** [contest] · cpa
  Voronoi diagram and Delaunay triangulation; Delaunay properties and duality; Guibas-Stolfi divide and conquer Delaunay
- **45.8 Half-plane intersection** [contest] · cpa
  Half-planes as point-plus-direction; Incremental O(n^2) half-plane intersection; Sort-and-incremental half-plane intersection; Applications of half-plane intersection

## Appendix A · Computer systems (curated links, not built)

*Concepts: 36 core · 26 stretch. Each page is a curated list of links for its concepts; book chapters that rest on them point here.*

### Computers and operating systems

- **A.1 CPU, memory and caches** [core] · ciu · open prose: none
  CPU components: ALU, registers and RAM (no open prose); How a CPU executes a program (no open prose); Memory hierarchy and CPU caches (no open prose); Building a computer from logic gates [stretch] (no open prose)
- **A.2 Compilers and runtimes** [stretch] · ciu · open prose: none
  How a compiler works (no open prose); Compiler optimisation (no open prose); Garbage collection (no open prose)
- **A.3 Processes, threads and context switches** [core] · ciu · open prose: none
  Processes versus threads (no open prose); Interrupts and context switching (no open prose)
- **A.4 Virtual memory** [core] · ciu · open prose: none
  Paging, segmentation and virtual memory (no open prose); Fork and copy-on-write (no open prose)
- **A.5 Concurrency and synchronisation** [core] · ciu · open prose: none
  Locks, mutexes, semaphores and monitors (no open prose); Deadlock and livelock (no open prose); Concurrency in Python and the GIL (no open prose); Parallel programming [stretch] (no open prose)

### Networking

- **A.6 Network layers and addressing** [core] · ciu · open prose: none
  OSI and TCP/IP models (no open prose); Subnetting and CIDR notation (no open prose)
- **A.7 TCP and UDP** [core] · ciu, sdp
  TCP; UDP; TCP versus UDP (no open prose); Connection pooling; Socket programming (no open prose)
- **A.8 HTTP and TLS** [core] · ciu, sdp
  HTTP; HTTP verbs: idempotent, safe, cacheable; TLS and HTTPS (no open prose)
- **A.9 RPC, REST and serialisation** [core] · ciu, sdp
  Serialisation formats (no open prose); Remote procedure call (RPC); REST; RPC vs REST; HATEOAS [stretch]

### Software engineering practice

- **A.10 Testing** [core] · ciu · open prose: none
  Unit testing (no open prose); Mock objects (no open prose); Integration testing (no open prose); Dependency injection (no open prose); Test-driven development (no open prose)
- **A.11 Design patterns and UML** [core] · ciu · open prose: none
  UML class diagrams (no open prose); Creational design patterns (no open prose); Structural design patterns (no open prose); Behavioural design patterns (no open prose)
- **A.12 SOLID principles** [stretch] · ciu · open prose: none
  Single responsibility principle (no open prose); Open/closed principle (no open prose); Liskov substitution principle (no open prose); Interface segregation principle (no open prose); Dependency inversion principle (no open prose)
- **A.13 Object-oriented design exercises** [stretch] · sdp
  OOD: design a parking lot [core]; OOD: design a call center; OOD: design a deck of cards; OOD: design an online chat
- **A.14 Developer tools** [stretch] · ciu · open prose: none
  Using vi(m) and Emacs (no open prose); Unix command-line tools (no open prose)

### Information, coding and security

- **A.15 Information and entropy** [core] · ciu · open prose: none
  Information theory (no open prose); Entropy [stretch] (no open prose)
- **A.16 Parity and Hamming codes** [stretch] · ciu · open prose: none
  Parity bits (no open prose); Hamming code (no open prose)
- **A.17 Compression** [stretch] · ciu · open prose: none
  Lossless compression (no open prose); LZ77 (no open prose)
- **A.18 Cryptography** [core] · ciu · open prose: none
  Cryptographic hash functions (no open prose); Encryption [stretch] (no open prose)
- **A.19 Computer security** [stretch] · ciu · open prose: none
  Threat models and privilege separation (no open prose); Control hijacking and buffer overflows (no open prose); Web security model (no open prose); Network security and side channels (no open prose)

## Appendix B · Getting the job (reading page, not built)

CIU's career sections as one reading page: update your resume; interview process and general interview prep; be thinking of for when the interview comes; have questions for the interviewer; once you've got the job. No concepts.
