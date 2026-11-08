# Dossier: exercise sources sweep, Parts I–V

Finder run 2026-11-08. Scope: where code exercises, keyed problem sets and
unkeyed book exercises come from, for Parts I–IV (DSA basics through
cp-algorithms topics) and Part V (system design). This dossier lists and
licenses; it does not rank (the judge does). Rules applied (METHOD.md §0,
§6.3): statements must come from a source; tests and reference solutions
may be AI-written (`tests_by: "ai"`); CC BY-NC / BY-NC-SA material is only
allowed as NC exercise cards (`exercises-nc.json`, `nc: true`); anything
all-rights-reserved, ND, GPL or unlicensed is link-only.

New sources registered in `sources/registry.json` by this run (28 rows):
`kattis`, `icpc-kattis-export`, `icpc-mzuenni`, `icpc-dapc`, `icpc-rmc`,
`icpc-ecna`, `mitocw-6-006-spring2020`, `mitocw-6-006-fall2011`,
`mitocw-6-006-spring2008`, `mitocw-6-046j-spring2015`,
`mitocw-6-046j-spring2012`, `mitocw-6-046j-fall2005`,
`mitocw-6-851-spring2012`, `mitocw-6-854j-fall2008`,
`mitocw-6-854j-fall2005`, `mitocw-6-856j-fall2002`,
`mitocw-6-042j-fall2005`, `mitocw-6-042j-fall2010`,
`mitocw-6-890-fall2014`, `mitocw-6-824-spring2006`,
`mitocw-6-830-fall2010`, `projecteuler`, `thealgorithms-python`,
`thealgorithms-javascript` (link-only), `icc`, `opendsa-exercises`,
`trekhleb-jsalgo`, `keon-algorithms`. Everything is cached under
`sources/_cache/<id>/` with a `FETCHED.txt`.

Two corrections to METHOD.md §6.3 found on the way:

- **TheAlgorithms/JavaScript is GPL-3.0, not MIT.** Its `LICENSE` reads
  "GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007". GPL code cannot be
  relicensed into CC BY-SA 4.0, so it is link-only. MIT-licensed JS tests
  exist in `trekhleb-jsalgo` instead.
- **Kattis licences are CC BY 3.0 / CC BY-SA 3.0** (plus CC0 and Public
  Domain Mark), stated per problem. BY-SA 3.0 lets adaptations use a later
  version, so BY-SA 4.0 output is fine. Kattis problems without a badge say
  "For educational use only" and are link-only.

---

## 1. Master table: topic → exercise sources

Columns: **open code exercises** (licence passes; "tests" says what test
data the source ships), **NC keyed problem sets** (NC cards; statement and
solution from the source), **book exercises, unkeyed** (statement from the
source; a reference and tests would be AI-written), **link-only practice**.
Locators use the source ids above. The "topic" column follows the book's
Parts as the task scoped them, not yet the concept map ids (the map is not
written yet).

| topic | open code exercises (tests?) | NC keyed problem sets | book exercises (unkeyed) | link-only practice |
|---|---|---|---|---|
| **I. Asymptotics, recurrences** | — (none open as code) | mitocw-6-006-fall2011 ps1 (1-1, 1-2); mitocw-6-006-spring2020 ps1 1-1, ps2 2-1; mitocw-6-046j-fall2005 ps1 1-1, 1-2; mitocw-6-042j-fall2005 (asymptotics, recurrences sets) | jeffe ch. 1 exercises; jeffe-notes 99-recurrences; ods intro.tex (7) | — |
| **I. Arrays, sequences, 2D arrays** | exercism: sublist (18), spiral-matrix (6), matrix (8), transpose (12), saddle-points (9), series (11), largest-series-product (18) (all with canonical tests); icc arrays_strings/* (10, unittest); kattis twosum, nsum, cd, greedilyincreasing (samples only) | mitocw-6-006-spring2020 ps0 0-6 (count_long_subarray, tests.py), ps1 1-2/1-3 | ods arrays.tex (13; ~10 "implement"); jeffe ch. 3 "Sequences/Arrays" block | cpa practice links; LeetCode "Array" |
| **I. Strings (basic)** | exercism: anagram (22), isogram (14), run-length-encoding (13), hamming (15), reverse-string (9), word-count (15), rotational/atbash/affine ciphers; icc arrays_strings (compress, permutation, rotation, unique_chars, reverse_string, str_diff) | mitocw-6-006-spring2020 ps3 3-5 (count_anagram_substrings, tests.py) | — | LeetCode "String" |
| **I. Linked lists** | exercism: linked-list (19, doubly), simple-linked-list (27, singly + reverse); icc linked_lists/* (8: add_reverse, delete_mid, find_loop_start, kth_to_last_elem, palindrome, partition, remove_duplicates, linked_list); thealgorithms-python data_structures/linked_list (23 files, all with doctests); trekhleb-jsalgo data-structures/linked-list, doubly-linked-list (jest) | mitocw-6-006-spring2020 ps1 1-4 (Doubly_Linked_List_Seq.py, tests.py) | ods linkedlists.tex (19; ~15 "implement") | LeetCode "Linked List" |
| **I. Stacks, queues, deques, ring buffers** | exercism: matching-brackets (20), circular-buffer (14), forth (55, stack machine); icc stacks_queues/* (7: n_stacks, queue_from_stacks, set_of_stacks, sort_stack, stack_min, …); opendsa-exercises AV/**/infixToPostfix, postfixEvaluation (proficiency) | mitocw-6-046j-spring2015 ps4 4-1 (Extreme FIFO Queues) | ods arrays.tex (ArrayDeque, RootishArrayStack variants, "Design and implement a Treque") | — |
| **I. Hash tables, sets, maps** | exercism: custom-set (40), etl (4), word-count, isogram, pangram (11); kattis babelfish, compoundwords, securedoors, deduplicatingfiles, enlarginghashtables, oddmanout (samples); icc arrays_strings/hash_map; opendsa-exercises Exercises/Hashing (47 keyed) + AV hashing/openHashing/rehashing/HashingDel PRO; thealgorithms-python data_structures/hashing (6 with doctests) | mitocw-6-006-spring2020 ps3 (3-1 … 3-5); mitocw-6-006-fall2011 ps4 (4-1 hash functions, 4-2 dictionaries, 4-3 DNA rolling hash, code + code solutions); mitocw-6-856j-fall2002 (universal hashing sets) | ods hashing.tex (11, mostly written); jeffe-notes 05-hashing | LeetCode "Hash Table" |
| **I. Recursion** | exercism: flatten-array (15), say (19), sgf-parsing (24); icc recursion_dynamic/{hanoi, permutations, power_set, n_pairs_parentheses, magic_index, steps}; opendsa-exercises Exercises/RecurTutor (40 keyed) | mitocw-6-006-spring2020 ps0 0-4, 0-5 (induction) | jeffe ch. 1 (recursion) exercises | — |
| **I. Sorting** | kattis sortofsorting, sidewayssorting, sorttwonumbers (samples); icc sorting_searching/{insertion_sort, merge_sort, quick_sort, radix_sort, selection_sort, merge_into, anagrams}; opendsa-exercises Exercises/Sorting (147 keyed) + AV Sorting PRO (insertionSort, selectionSort, shellsort, mergesort, quicksort, heapsort, radixExchangeSort); thealgorithms-python sorts (57 of 60 with doctests); trekhleb-jsalgo algorithms/sorting (11 test dirs, 73 tests); keon-algorithms tests/test_sorting.py | mitocw-6-006-spring2020 ps2 2-2 "Sorting Sorts", 2-5 (satisfying_booking, tests.py); mitocw-6-046j-fall2005 ps2 (almost-sorted, weighted median); mitocw-6-046j-spring2015 ps4 4-2 (quicksort analysis) | ods sorting.tex (15; ~2 implement); jeffe ch. 1 (mergesort/quicksort exercises) | LeetCode "Sorting" |
| **I. Searching, binary search** | exercism: binary-search (11; requires the algorithm), square-root (6); kattis guess (interactive), prettygoodcuberoot; icc sorting_searching/{rotated_array_search, search_sorted_matrix}; opendsa-exercises AV binarySearch / interpolationSearch PRO; thealgorithms-python searches (16 of 18 with doctests, 320 doctest lines) | mitocw-6-006-fall2011 ps1 1-3…1-6 (peak finding); mitocw-6-046j-fall2005 ps1 1-3 (unimodal search) | — | cpa num_methods/binary_search practice links |
| **I. Bit manipulation** | exercism: eliuds-eggs (4; forbids the library popcount), secret-handshake (11), allergies (50), variable-length-quantity (31), grains (11), intergalactic-transmission (26); icc bit_manipulation/* (8); thealgorithms-python bit_manipulation (31 of 32 with doctests); kattis bitbybit, logicfunctions | — | ods integers.tex (4) | — |
| **II. Binary trees, BSTs, traversals** | exercism: binary-search-tree (10), satellite (9, rebuild from pre-/in-order), pov (15), zipper (14), tree-building (16); icc graphs_trees/{bst, bst_min, bst_second_largest, bst_successor, bst_validate, check_balance, invert_tree, tree_bfs, tree_dfs, tree_height, tree_lca, tree_level_lists}; opendsa-exercises Exercises/Binary (32) + AV BSTinsert/BSTsearch/BSTremove/btTrav PRO; thealgorithms-python data_structures/binary_tree (35 of 36 doctests); trekhleb-jsalgo data-structures/tree/* | mitocw-6-006-spring2020 ps4 4-1 (binary tree practice), 4-6 (AVL, tastiest_slice, tests.py) | ods binarytrees.tex (19; ~6 implement) | LeetCode "Tree" |
| **II. Balanced trees, skip lists, B-trees, treaps** | opendsa-exercises AV AVLinsert, redBlackTree, bPlusTreeInsert, bMinusTreeInsert PRO; thealgorithms-python data_structures/binary_tree (avl, red_black, treap) doctests; kattis — | mitocw-6-006-fall2011 ps3 3-1 (range queries, code + code solutions); mitocw-6-046j-spring2015 ps2 2-2 (combining B-trees), ps5 5-1 (skip lists); mitocw-6-046j-fall2005 ps4 (treaps, balanced), ps5 5-1 (skip lists, B-trees), ps6 6-2 (red-black restructuring); mitocw-6-046j-spring2012 ps6 6-1 | ods rbs.tex (14; ~8 implement), redblack.tex (14), scapegoat.tex (11), skiplists.tex (15), btree.tex (8); jeffe-notes 03-treaps, 10-scapegoat-splay | — |
| **II. Heaps, priority queues** | kattis heap (Binary Heap, CC BY-SA), splitmedian; icc graphs_trees/min_heap, arrays_strings/priority_queue; opendsa-exercises AV heapbuild/heapinsert/heapremove/heapsort PRO; thealgorithms-python data_structures/heap (7 of 8 doctests); trekhleb-jsalgo data-structures/heap | mitocw-6-006-spring2020 ps4 4-2 (heap practice); mitocw-6-006-fall2011 ps2 (circuit simulation, PQ, code solutions) | ods heaps.tex (11) | — |
| **II. Tries** | icc graphs_trees/trie; opendsa-exercises AV commonTrie/radixTrie/digitalSearchTree PRO; thealgorithms-python data_structures/trie (2 of 3 doctests); trekhleb-jsalgo data-structures/trie | — | ods (binarytrie in integers chapter) | — |
| **II. Union-find** | kattis unionfind (CC BY), virtualfriends, almostunionfind (CC BY); opendsa-exercises AV UnionFind PRO; thealgorithms-python data_structures/disjoint_set | mitocw-6-046j-spring2012 ps8 8-1 (improving union-by-rank); mitocw-6-046j-spring2015 recitation "Amortization: Union-find" | jeffe-notes 11-unionfind (7 exercises, mostly proofs) | — |
| **II. Graph representations, BFS, DFS, connectivity** | exercism: two-bucket (11, state-space BFS), relative-distance (7), connect (12), go-counting (11), word-search (24), flower-field (13); kattis 10kindsofpeople, reachableroads, erdosnumbers, weakvertices, countingstars, grid, hidingplaces, torn2pieces, martensdfs, kastenlauf; icc graphs_trees/{graph, graph_bfs, graph_dfs, graph_path_exists, graph_build_order}; opendsa-exercises Exercises/Graph (30 keyed); thealgorithms-python graphs (55 of 73 doctests); trekhleb-jsalgo algorithms/graph (15 test dirs) | mitocw-6-006-spring2020 ps5 (5-1 … 5-6, solve_tilt.py BFS, tests.py); mitocw-6-006-fall2011 ps6 6-1…6-3 (BFS, Rubik's cube 2x2, code + code solutions) | jeffe ch. 5 (graphs), ch. 6 (DFS: ~32 exercises, ~20 algorithmic); ods graphs.tex (10) | LeetCode "Graph" |
| **II. Topological sort, DAGs, SCC** | exercism: react (14, dependency propagation); kattis longestpathinadag, familydag, promotions; icc graphs_trees/graph_build_order; thealgorithms-python graphs (kahns_algorithm_*, scc_kosaraju, tarjans_scc) | mitocw-6-006-spring2020 ps5 | jeffe ch. 6 | — |
| **II. Shortest paths** | kattis shortestpath1/2/3 (CC BY), shortestpath4, allpairspath (CC BY), getshorty (CC BY), transportationplanning; icc graphs_trees/{graph_shortest_path, graph_shortest_path_unweighted}; thealgorithms-python graphs (dijkstra*, bellman_ford, graphs_floyd_warshall, johnson) | mitocw-6-006-spring2020 ps6 (6-1 … 6-6, johnson.py, tests.py); mitocw-6-006-fall2011 ps6 6-4 (Dijkstra, code solutions); mitocw-6-046j-spring2015 ps6 6-1 (APSP); mitocw-6-046j-spring2012 ps2 2-2; mitocw-6-046j-fall2005 ps8 8-1 | jeffe ch. 8 (SSSP), ch. 9 (APSP) | cpa graph practice links |
| **II. Minimum spanning trees** | kattis minspantree (CC BY), islandhopping, lostmap (CC0); thealgorithms-python graphs (kruskal, prims, boruvka) | mitocw-6-046j-spring2015 ps6 6-2; mitocw-6-046j-spring2012 ps2 2-1, 2-2 | jeffe ch. 7 (MST) | — |
| **II. Dynamic programming** | exercism: change (13, fewest coins), knapsack (7, 0/1), book-store (18), pascals-triangle (8); kattis knapsack (CC BY), longincsubseq (CC BY), increasingsubsequence, exactchange2, canonical, ninepacks, walrusweights (CC BY), orders, narrowartgallery (CC BY), dnasimilarity, stringfactoring; icc recursion_dynamic/{coin_change*, knapsack_01, knapsack_unbounded, longest_common_subsequence, longest_inc_subseq, grid_path, matrix_mult, max_profit_k, fibonacci}; thealgorithms-python dynamic_programming (51 of 53 doctests, 401 lines); keon-algorithms tests/test_dynamic_programming.py | mitocw-6-006-spring2020 ps7 (7-1 … 7-5, short_company.py, tests.py), ps8 (8-1 … 8-4); mitocw-6-006-fall2011 ps7 (seam carving, code solutions); mitocw-6-046j-fall2005 ps7 7-1 (edit distance); mitocw-6-046j-spring2015 ps9 9-1 (knapsack) | jeffe ch. 3 (~52 exercise items, ~44 algorithmic with concrete input/output; sampled below) | LeetCode "Dynamic Programming"; CSES DP section |
| **II. Greedy** | kattis intervalcover (CC BY), intervalscheduling, fibonaccisum, canonical; exercism roman-numerals (27) | mitocw-6-046j-spring2012 ps9 9-2 (Huffman); mitocw-6-046j-fall2005 ps7 7-2 | jeffe ch. 4 (greedy) | — |
| **II. Backtracking, exhaustive search** | exercism: alphametics (10), zebra-puzzle (2), killer-sudoku-helper (13), dominoes (13), queen-attack (13); kattis holeynqueensbatman, maxclique (PD), pebblesolitaire, flowfree; thealgorithms-python backtracking (22 of 23 doctests) | mitocw-6-890-fall2014 (hardness, not search) | jeffe ch. 2 (backtracking) | — |
| **II. Divide and conquer** | kattis closestpair1/2 (CC BY), polymul2 (CC BY); thealgorithms-python divide_and_conquer (13 of 16 doctests) | mitocw-6-046j-spring2015 ps1 (1-1, 1-2); mitocw-6-046j-spring2012 ps1 (median select) | jeffe ch. 1 | — |
| **III/IV. Amortised analysis** | — | mitocw-6-046j-spring2015 ps4 4-1; mitocw-6-046j-spring2012 ps6 6-1; mitocw-6-046j-fall2005 ps6; mitocw-6-854j-fall2005/2008 (amortisation, Fibonacci heaps, splay) | jeffe-notes 09-amortize, 10-scapegoat-splay | — |
| **III/IV. Randomised algorithms** | exercism baffling-birthdays (17, probability) | mitocw-6-856j-fall2002 (13 homeworks + answers); mitocw-6-046j-spring2012 ps5; mitocw-6-046j-spring2015 ps5 5-2 | jeffe-notes 01-random, 02-nutsbolts, 04-chernoff, 06-bloom | — |
| **IV. Number theory (primes, gcd, modular, CRT)** | exercism: sieve (5), nth-prime (5), prime-factors (12), perfect-numbers (14), rational-numbers (43), affine-cipher (16), diffie-hellman (6, deprecated), all-your-base (21); kattis primesieve, primality, primecount (PD), modulararithmetic, chineseremainder, generalchineseremainder, gcd (PD), gcdandlcm, divisorcounts (PD), positivedivisors (PD), inversetotient (PD), factorialpower (PD), pseudoprime (CC BY), crackingrsa, goldbach2, primereduction; thealgorithms-python maths (211 of 220 doctests) + ciphers (rsa, affine); icpc-* tagged number-theory (≈14 packages, unverified tags) | mitocw-6-042j-fall2005 (number theory, RSA sets + solutions); mitocw-6-006-fall2011 ps5 5-2 (RSA, code solutions) | jeffe-notes B-fastexpo | projecteuler (NC, below); cpa algebra practice links; CSES Mathematics |
| **IV. Combinatorics, counting** | kattis catalan, anagramcounting, subcommittees; exercism pascals-triangle | mitocw-6-042j-fall2005, mitocw-6-042j-fall2010 (counting, recitation problems; finals with solutions) | — | projecteuler 15, 24, 53, 76–78, 114–117 (NC) |
| **IV. Strings (KMP, Z, hashing, suffix structures, Aho-Corasick)** | kattis stringmatching (CC BY), stringmultimatching (CC BY), suffixsorting (CC BY), hashing (string hashing), burrowswheeler, substrings, palindromesubstring; thealgorithms-python strings (66 of 67 doctests: knuth_morris_pratt, z_function, rabin_karp, aho_corasick, suffix_array…) | mitocw-6-046j-spring2015 ps2 2-1 (pattern matching); mitocw-6-046j-spring2012 ps4 4-1 (word search via FFT); mitocw-6-006-fall2011 ps4 4-3 (rolling hash DNA, code) | jeffe-notes 07-strings | cpa string practice links |
| **IV. Range queries (Fenwick, segment tree, sparse table)** | kattis fenwick (CC BY), supercomputer (CC BY), moviecollection; thealgorithms-python data_structures/binary_tree (fenwick_tree, segment_tree*); keon-algorithms test_iterative_segment_tree.py; icpc-kattis-export tagged segment/fenwick: gcpc2023/japaneselottery, gcpc2024/darkalley, nwerc2025/groupphoto | mitocw-6-851-spring2012 (dynamic DS) | — | cpa data_structures practice links |
| **IV. Network flow, matching, min cut** | kattis maxflow, mincut, mincostmaxflow (all CC BY); thealgorithms-python networking_flow (4 of 5), graphs (dinic, edmonds_karp, hopcroft_karp); icpc-kattis-export tagged flow: gcpc2023/balloondarts, freestylemasonry, highwaycombinatorics, gcpc2025/labourlaws, nwerc2025/hastyhaul | mitocw-6-046j-spring2015 ps7 (7-1 … 7-3); mitocw-6-046j-spring2012 ps9 9-1; mitocw-6-854j-fall2005/2008 (flows, min-cost flow) | jeffe ch. 10, 11 (max flow, applications) | — |
| **IV. Computational geometry** | kattis convexhull, polygonarea, convexpolygonarea, pointinpolygon, segmentintersection, segmentdistance, maxcolinear, closestpair1/2, triarea (CC BY / BY-SA); thealgorithms-python geometry (9 of 14) | mitocw-6-046j-fall2005 ps5 5-2 (points in the plane), ps8 8-1 | — | cpa geometry practice links |
| **IV. FFT, polynomials, linear algebra, matrix exponentiation** | kattis polymul1/2 (CC BY), linearrecurrence (CC BY), equationsolver, equationsolverplus; thealgorithms-python maths (fft), matrix (24 of 27 doctests), linear_algebra | mitocw-6-046j-spring2012 ps3 (electric potential, FFT); mitocw-6-046j-spring2015 ps8 8-1 (simplex) | jeffe-notes A-fft, H-lp, I-simplex | — |
| **IV. NP-hardness, reductions, approximation** | — (written by nature) | mitocw-6-890-fall2014 (4 sets + solutions); mitocw-6-046j-spring2015 ps8 8-2, ps9 9-2; mitocw-6-046j-spring2012 ps8 8-2 | jeffe ch. 12 (NP-hardness); jeffe-notes J-approx | — |
| **IV. Game theory** | kattis bitgame; icpc-kattis-export gcpc2023/adolescentarchitecture2 (tag unverified) | — | — | cpa game_theory practice links |
| **IV. Advanced data structures (persistence, vEB, succinct, dynamic graphs)** | — | mitocw-6-851-spring2012 (10 sets + solutions); mitocw-6-046j-spring2015 ps3 (vEB); mitocw-6-046j-spring2012 ps7 (vEB) | — | — |
| **Contest-style mixed practice (Part IV capstones)** | icpc-kattis-export (233 packages, 221 CC BY-SA, full test data + accepted submissions); icpc-mzuenni (38, overlaps NWERC 2022–24); icpc-dapc (25); icpc-rmc (≈108 across 2018–2026); icpc-ecna (91, CC0); kattis (325 open) | — | — | Codeforces, AtCoder, CSES, LeetCode, HackerRank (all rights reserved) |
| **V. Distributed systems: clocks, ordering, broadcast, replication, consensus** | exercism bank-account (concurrency-safe state, 17), parallel-letter-frequency (13) | mitocw-6-824-spring2006 (2 quizzes 2005 with answers, paper-based: Frangipani, Ivy, Porcupine, Paxos-style questions); mitocw-6-046j-spring2015 ps10 (leader election, async BFS) | **kleppmann-ds** (another finder's fetch, CC BY-SA 4.0): 23 `\supervision{question}{solution}` pairs in `dist-sys.tex` — keyed and open (RPC framing, failure detectors, clocks, happens-before, Lamport/vector clocks, broadcast, quorum replication, linearizability, consensus/Raft, CRDTs) | — |
| **V. Databases: indexing, transactions, recovery, storage** | — | mitocw-6-830-fall2010 (2 quizzes + solutions: OCC, schema design, external aggregation, cost estimation, ARIES, snapshot isolation, C-Store, BigTable, distributed queries) | — | — |
| **V. Whole-system design questions (pastebin, timeline, crawler, cache, KV store…)** | sdp solutions/system_design/* (8 exercises with worked solutions, CC BY 4.0, incl. "Calculate usage" back-of-envelope sections); sdp resources/flash_cards: "System Design Exercises.apkg" (8 notes), "System Design.apkg" (42 notes), "OO Design.apkg" (6 notes) | — | — | ByteByteGo system-design-101 (CC BY-NC-ND), karanpratapsingh/system-design (CC BY-NC-ND), algodeck (CC BY-NC-ND): ND, so link-only |
| **V. APIs, REST, unique IDs, I/O metering** | exercism rest-api (9), robot-name (no canonical data; unique random names without collision), paasio (no canonical data) | — | — | — |
| **V. Object-oriented design** | sdp solutions/object_oriented_design/* (6: call_center, deck_of_cards, hash_table, lru_cache, online_chat, parking_lot; notebooks with code) | — | — | weeeBox/mobile-system-design (all rights reserved) |
| **V. Rate limiting, consistent hashing, CDN/DNS, sharding, back-of-envelope as standalone drills** | **none found** | none | none (sdp prose covers sharding/CDN/DNS but poses no exercise on them except inside the 8 worked designs) | — |

## 1a. Candidates by source (resource-finder row format)

Item-level locators are in the tables of §2–§9. `assumes` is left to the
chapter dossiers, since it depends on concept-map ids that don't exist yet.

| locator | source id | licence | nc | kind | concepts covered | length | assumes | what it is |
|---|---|---|---|---|---|---|---|---|
| `exercism:<slug>` | exercism | MIT | false | code-exercise | Part I–II basics, number theory, a few concurrency/API items | 92 exercises, 1402 canonical cases | — | description + language-neutral test cases; track repos have example solutions |
| `kattis:<slug>` | kattis | CC BY 3.0 / CC BY-SA 3.0 / CC0 / PD (per problem) | false | code-exercise | all Parts I–IV; 144 tagged in §3 | 325 open problems | — | statement + sample data; no hidden tests |
| `icpc-kattis-export:<contest>/<problem>` | icpc-kattis-export | CC BY-SA | false | code-exercise | contest mix (Part IV) | 221 packages | — | full package: statement, secret tests, accepted solutions, 125 solution slides |
| `icpc-mzuenni:<problem>` | icpc-mzuenni | CC BY-SA | false | code-exercise | contest mix | 38 | — | same format; overlaps NWERC above |
| `icpc-dapc:<dir>/<problem>` | icpc-dapc | CC BY-SA | false | code-exercise | contest mix (easier, preliminaries) | 25 | — | same format with slides |
| `icpc-rmc:<year>/<problem>` | icpc-rmc | CC BY-SA (problem.yaml); MIT repo files | false | code-exercise | contest mix | ≈108 | — | same format, per-year slides |
| `icpc-ecna:<season>/<problem>` | icpc-ecna | CC0 | false | code-exercise | contest mix | 91 | — | zipped full packages |
| `mitocw-<course>:<file>#<n-m>` | mitocw-* (15 ids) | CC BY-NC-SA 4.0 | true | exercise (keyed); 6.006 S2020 and F2011 also code-exercise with tests | Parts I–IV, plus distributed systems and databases | see §5 | — | problem sets/quizzes/exams with official solutions |
| `projecteuler:<n>` | projecteuler | CC BY-NC-SA 4.0 | true | code-exercise (statement only) | number theory, DP, combinatorics, graphs | 200 cached | — | statements; no answers published |
| `icc:<topic>/<challenge>` | icc | Apache-2.0 | false | code-exercise | Part I–II interview basics | ~91 | — | challenge + solution notebooks + unittest |
| `opendsa-exercises:<path>` | opendsa-exercises | MIT | false | exercise (keyed), proficiency (trace) | Part I–II | ~1650 + ~50 | — | Khan-style keyed items; step-by-step algorithm simulations |
| `thealgorithms-python:<path>` | thealgorithms-python | MIT | false | dataset (test cases) | all DSA areas | ~1000 files with doctests | — | doctests, for testing statements taken elsewhere |
| `trekhleb-jsalgo:<path>` | trekhleb-jsalgo | MIT | false | dataset (test cases, JS) | DS, sorting, graphs, math, strings | ~110 test dirs | — | jest tests |
| `keon-algorithms:<path>` | keon-algorithms | MIT | false | dataset (test cases, Python) | DSA areas | ~590 test methods | — | unittest suites |
| `ods:<tex>#exc` + `ods` python tests | ods | CC BY | false | exercise (unkeyed) + test harness | Part I–II data structures | 171 exercises, ~57 "implement" | — | book exercises; python/ods/tests harnesses |
| `jeffe:<ch>.ex<n>` | jeffe | CC BY 4.0 | false | exercise (unkeyed) | recursion → NP-hardness | sampled ch. 3, 6 (§6) | — | algorithm-design exercises |
| `sdp:solutions/system_design/<name>`, sdp flash cards | sdp | CC BY 4.0 | false | exercise (keyed) | Part V | 8 + 6 worked, 56 cards | — | system / OO design exercises with solutions |
| `kleppmann-ds:dist-sys#supervision-<n>` | kleppmann-ds (other finder) | CC BY-SA 4.0 | false | exercise (keyed) | Part V distributed systems | 23 | — | question + solution pairs |

---

## 2. Exercism problem-specifications (`exercism`, MIT, pin 7b49ec41)

152 exercise dirs; 92 bear on Parts I–V and are listed. "Canonical test
cases" counts leaf cases in `canonical-data.json`, minus those superseded
by a later case's `reimplements` field (1402 cases across the 92). The
last column quotes the description when it states a requirement on the
*method*; "no" means only input/output behaviour is specified, so a
complexity bound (§1.2 `bound`) may not be added by our tests.

Statements are Exercism's own words (MIT). Some cite outside inspiration
in `metadata.toml`: Project Euler (difference-of-squares, largest-series-
product, nth-prime, palindrome-products, pythagorean-triplet), Uncle Bob
katas (bowling, prime-factors), Cyber-Dojo (book-store); the text is
still Exercism's and MIT. Reference solutions exist in the track repos,
e.g. `exercism/python` `exercises/practice/<slug>/.meta/example.py` (MIT,
"MIT License Copyright (c) 2021 Exercism"; not fetched), so `tests_by`
can be `"source"` and `reference` can come from the source too.

| slug | topic | canonical test cases | algorithmic requirement stated in description |
|---|---|---|---|
| `exercism:transpose` | 2D arrays / strings | 12 | no |
| `exercism:matrix` | 2D arrays: parsing rows/columns | 8 | no |
| `exercism:saddle-points` | 2D arrays: row/column extrema | 9 | no |
| `exercism:spiral-matrix` | 2D arrays: traversal order | 6 | no |
| `exercism:queen-attack` | 2D geometry on a board | 13 | no |
| `exercism:book-store` | DP / greedy grouping | 18 | no |
| `exercism:knapsack` | DP: 0/1 knapsack | 7 | no |
| `exercism:change` | DP: fewest coins (coin change) | 13 | no |
| `exercism:complex-numbers` | arithmetic ADT | 40 | no |
| `exercism:piecing-it-together` | arithmetic constraint solving | 7 | no |
| `exercism:sublist` | arrays: subarray matching | 18 | no |
| `exercism:zebra-puzzle` | backtracking / constraint search | 2 | no |
| `exercism:alphametics` | backtracking / search | 10 | no |
| `exercism:variable-length-quantity` | bit manipulation: VLQ encode/decode | 31 | no |
| `exercism:secret-handshake` | bit manipulation: bitmask decode | 11 | no |
| `exercism:allergies` | bit manipulation: bitmask flags | 50 | no |
| `exercism:intergalactic-transmission` | bit manipulation: parity bits | 26 | no |
| `exercism:eliuds-eggs` | bit manipulation: popcount | 4 | yes: "Keep your hands off that bit-count functionality provided by your standard library" |
| `exercism:isbn-verifier` | checksums | 21 | no |
| `exercism:luhn` | checksums | 22 | no |
| `exercism:difference-of-squares` | closed-form sums (Project Euler 6) | 9 | no |
| `exercism:killer-sudoku-helper` | combinations / backtracking | 13 | no |
| `exercism:pascals-triangle` | combinatorics / DP rows | 8 | no |
| `exercism:parallel-letter-frequency` | concurrency: parallel map-reduce | 13 | yes: "Employ parallelism" |
| `exercism:armstrong-numbers` | digits | 11 | no |
| `exercism:relative-distance` | graphs: BFS distance in a family tree | 7 | no |
| `exercism:two-bucket` | graphs: BFS over states | 11 | no |
| `exercism:dominoes` | graphs: Eulerian cycle / backtracking | 13 | no |
| `exercism:connect` | graphs: connectivity on a hex grid (DFS/BFS) | 12 | no |
| `exercism:dot-dsl` | graphs: data model / builder DSL | 19 | no |
| `exercism:react` | graphs: dependency propagation (reactive cells, callbacks) | 14 | no |
| `exercism:go-counting` | graphs: flood fill on a grid | 11 | no |
| `exercism:roman-numerals` | greedy conversion | 27 | no |
| `exercism:rectangles` | grids: counting rectangles | 14 | no |
| `exercism:flower-field` | grids: neighbour counting | 13 | no |
| `exercism:word-search` | grids: search in 8 directions | 24 | no |
| `exercism:game-of-life` | grids: simulation | 8 | no |
| `exercism:word-count` | hash maps: counting | 14 | no |
| `exercism:etl` | hash maps: inverting a map | 4 | no |
| `exercism:isogram` | hashing / sets | 14 | no |
| `exercism:anagram` | hashing: letter multisets | 18 | no |
| `exercism:sum-of-multiples` | inclusion / sets of multiples | 16 | no |
| `exercism:collatz-conjecture` | iteration | 6 | no |
| `exercism:linked-list` | linked lists: doubly linked list (push/pop/shift/unshift/delete) | 19 | no |
| `exercism:simple-linked-list` | linked lists: singly linked list + reverse | 27 | no |
| `exercism:strain` | lists: filter (keep/discard) | 14 | track-dependent: no builtin filter |
| `exercism:list-ops` | lists: map/filter/fold from scratch | 23 | yes: "without using existing functions" |
| `exercism:rotational-cipher` | modular arithmetic on letters | 10 | no |
| `exercism:all-your-base` | number bases: conversion | 21 | no |
| `exercism:sieve` | number theory: Sieve of Eratosthenes | 5 | yes: "implements the Sieve of Eratosthenes" (but "tests don't check that you've implemented the algorithm") |
| `exercism:perfect-numbers` | number theory: divisor sums | 14 | no |
| `exercism:rational-numbers` | number theory: gcd, reduced fractions | 43 | no |
| `exercism:diffie-hellman` (deprecated) | number theory: modular exponentiation (deprecated) | 6 | no |
| `exercism:affine-cipher` | number theory: modular inverse, coprimality | 16 | no |
| `exercism:nth-prime` | number theory: primes | 5 | yes: "pretend [standard-library prime methods] don't exist" |
| `exercism:prime-factors` | number theory: trial division | 12 | no |
| `exercism:ocr-numbers` | parsing grids | 17 | no |
| `exercism:wordy` | parsing: left-to-right evaluation | 27 | no |
| `exercism:grains` | powers of two / big integers | 11 | no |
| `exercism:baffling-birthdays` | probability: birthday paradox, simulation | 17 | no |
| `exercism:circular-buffer` | queues: ring buffer (read/write/overwrite/clear) | 14 | no |
| `exercism:flatten-array` | recursion on nested lists | 11 | no |
| `exercism:say` | recursion on number groups | 19 | no |
| `exercism:pythagorean-triplet` | search / number theory (Project Euler 9) | 7 | no |
| `exercism:palindrome-products` | search with pruning (Project Euler 4) | 13 | no |
| `exercism:binary-search` | searching: binary search | 11 | yes: "implement a binary search algorithm"; describes halving steps |
| `exercism:square-root` | searching: binary search / Newton on integers | 6 | soft: "Try to avoid using the pre-existing math libraries" |
| `exercism:pangram` | sets | 10 | no |
| `exercism:custom-set` | sets: implement a set ADT | 40 | "How it works internally doesn't matter" |
| `exercism:largest-series-product` | sliding window (Project Euler 8 variant) | 15 | no |
| `exercism:tournament` | sorting + aggregation | 12 | no |
| `exercism:grade-school` | sorting + maps | 20 | no |
| `exercism:high-scores` | sorting / top-k | 12 | no |
| `exercism:matching-brackets` | stacks: bracket matching | 20 | no |
| `exercism:forth` | stacks: stack-machine interpreter | 55 | no |
| `exercism:split-second-stopwatch` | state machine | 29 | no |
| `exercism:reverse-string` | strings | 9 | no |
| `exercism:run-length-encoding` | strings: encoding | 13 | no |
| `exercism:hamming` | strings: pairwise compare | 9 | no |
| `exercism:grep` | strings: search over files | 25 | no |
| `exercism:series` | strings: sliding window of length n | 11 | no |
| `exercism:atbash-cipher` | substitution | 14 | no |
| `exercism:paasio` | system design: I/O metering wrapper (no canonical data) | none (no canonical-data.json) | no |
| `exercism:rest-api` | system design: REST endpoints (IOU ledger) | 9 | no |
| `exercism:bank-account` | system design: concurrency-safe state | 17 | yes: "must allow accounts to be safely accessed from multiple threads/processes" |
| `exercism:robot-name` | system design: unique random IDs without collision (no canonical data) | none (no canonical-data.json) | no |
| `exercism:binary-search-tree` | trees: BST insert + in-order traversal | 10 | no |
| `exercism:tree-building` | trees: build from parent records | 16 | refactoring exercise; no bound stated |
| `exercism:pov` | trees: re-rooting, path between nodes | 15 | no |
| `exercism:satellite` | trees: rebuild from pre-order + in-order | 9 | no |
| `exercism:sgf-parsing` | trees: recursive-descent parse | 23 | no |
| `exercism:zipper` | trees: zipper navigation (functional) | 14 | no |

Not listed (no DSA or system-design content): song/lyrics, date/time,
string-formatting and game-scoring exercises (e.g. beer-song, gigasecond,
bob, bowling, yacht, poker, darts, leap, space-age).

## 3. Kattis (`kattis`)

**How licences are stated.** Every problem page has a "Source & License"
card with a `rel="license"` link and badge. Patterns seen across 336
pages checked (347 slugs tried, 11 returned 404):

| badge / text | count | status |
|---|---|---|
| `Creative Commons License (cc by-sa)` → creativecommons.org/licenses/by-sa/3.0/ | 282 | open |
| `Creative Commons License (cc by)` → creativecommons.org/licenses/by/3.0/ | 31 | open |
| `Public Domain` → creativecommons.org/about/pdm | 10 | open |
| `Creative Commons License (cc0)` → creativecommons.org/about/cc0 | 2 | open |
| "For educational use only" (COCI, SWERC 2011, Waterloo, GNY regionals, Alberta) | 9 | link-only |
| no badge, source name only (COCI 2013/14 #6 `hash`, COCI 2015/16 #3 `pot`) | 2 | link-only |

Evidence, verbatim from the HTML:
- `kattis:10kindsofpeople` (Baylor Competitive Learning course, David
  Sturgill): `<a rel="license" href="https://creativecommons.org/licenses/by-sa/3.0/"> … alt="Creative Commons License (cc by-sa)"`
- `kattis:shortestpath1` (KTH CSC Popup 2005, Per Austrin): `href="https://creativecommons.org/licenses/by/3.0/" … alt="Creative Commons License (cc by)"`
- `kattis:hello`: `href="https://creativecommons.org/about/pdm" … alt="Public Domain"`
- `kattis:ballotboxes` (SWERC 2011): licence span reads "For educational use only".

General pattern: problems written for Kattis itself, the KTH popup
courses, Baylor's course, *Principles of Algorithmic Problem Solving*
(Sannemo), and the NWERC, GCPC and NA-regional problems sampled (bookingaroom, moviecollection, kastenlauf, canonical, torn2pieces …) carry CC BY-SA (NCPC and BAPC pages were not sampled);
Per Austrin's KTH algorithm "implement X" problems carry CC BY; imported
COCI, Waterloo, SWERC 2011 and older Greater New York sets are
educational-use-only. Only statements and sample data are public; hidden
tests are not, so tests past the samples are AI-written.

Cached: 325 open-licensed statement pages, 314 sample zips,
`index.json` with every checked slug's licence. The 144 below map to a
textbook topic (topic assigned from the problem's title and statement by
this finder, not by Kattis, which publishes no topic tags). The other
~180 open problems are contest-style and untagged.

| topic | problem | licence (badge) | source | difficulty |
|---|---|---|---|---|
| DP: 0/1 knapsack | [`kattis:knapsack`](https://open.kattis.com/problems/knapsack) Knapsack | cc by | KTH CSC Popup 2006 | 2.4 |
| DP: LIS | [`kattis:increasingsubsequence`](https://open.kattis.com/problems/increasingsubsequence) Increasing Subsequence | cc by-sa | Baylor Competitive Learning course | 2.0 |
| DP: LIS (n log n) | [`kattis:longincsubseq`](https://open.kattis.com/problems/longincsubseq) Longest Increasing Subsequence | cc by | KTH CSC Popup 2006 | 3.3 |
| DP: coin change | [`kattis:exactchange2`](https://open.kattis.com/problems/exactchange2) Exact Change | cc by-sa | Waterloo Programming Contest 2008-10-04 | 3.7 |
| DP: edit distance/LCS | [`kattis:dnasimilarity`](https://open.kattis.com/problems/dnasimilarity) DNA Similarity | cc by-sa | Baylor Competitive Learning course | 2.4 |
| DP: subset sum | [`kattis:walrusweights`](https://open.kattis.com/problems/walrusweights) Walrus Weights | cc by | Popup 2015 Session 1 | 2.3 |
| DP: subset sums | [`kattis:ninepacks`](https://open.kattis.com/problems/ninepacks) Nine Packs | cc by-sa | 2016 ICPC North American Qualifier Contest | 2.9 |
| DP: unbounded knapsack with reconstruction | [`kattis:orders`](https://open.kattis.com/problems/orders) Restaurant Orders | cc by-sa | KTH Challenge 2012 | 3.1 |
| DP / bitmask search | [`kattis:pebblesolitaire`](https://open.kattis.com/problems/pebblesolitaire) Pebble Solitaire | cc by-sa | Swedish Championships 2000 | 1.7 |
| DP / greedy: canonical coin systems | [`kattis:canonical`](https://open.kattis.com/problems/canonical) Canonical Coin Systems | cc by-sa | 2017 ICPC North American Qualifier Contest | 3.9 |
| DP on grid | [`kattis:narrowartgallery`](https://open.kattis.com/problems/narrowartgallery) Narrow Art Gallery | cc by | 2014 ICPC North America Qualifier | 2.0 |
| DP on strings | [`kattis:stringfactoring`](https://open.kattis.com/problems/stringfactoring) String Factoring | cc by-sa | Swedish Championships 2000 | 4.1 |
| Fenwick / segment tree | [`kattis:supercomputer`](https://open.kattis.com/problems/supercomputer) Supercomputer | cc by | Reykjav%C3%ADk University %C3%81FLV 2016 | 2.8 |
| Fenwick tree | [`kattis:fenwick`](https://open.kattis.com/problems/fenwick) Fenwick Tree | cc by | KTH CSC Popup spring 2013 | 3.5 |
| Fenwick tree | [`kattis:moviecollection`](https://open.kattis.com/problems/moviecollection) Movie Collection | cc by-sa | Northwestern Europe Regional Contest %28NWERC%29 2011 | 3.0 |
| arrays: sums | [`kattis:nsum`](https://open.kattis.com/problems/nsum) N-sum | cc by-sa | Principles of Algorithmic Problem Solving | 1.3 |
| arrays: two-sum | [`kattis:twosum`](https://open.kattis.com/problems/twosum) Two-sum | cc by-sa | Principles of Algorithmic Problem Solving | 1.2 |
| backtracking: N-queens | [`kattis:holeynqueensbatman`](https://open.kattis.com/problems/holeynqueensbatman) Holey N-Queens (Batman) | cc by-sa | Baylor Competitive Learning course | 2.4 |
| backtracking / bitmask: max clique | [`kattis:maxclique`](https://open.kattis.com/problems/maxclique) Maximum Clique | Public Domain | Principles of Algorithmic Problem Solving | 1.8 - 5.2 |
| backtracking on grid | [`kattis:flowfree`](https://open.kattis.com/problems/flowfree) Flow Free | cc by-sa | Rocky Mountain Regional Contest %28RMRC%29 2017 | 3.6 |
| binary heap | [`kattis:heap`](https://open.kattis.com/problems/heap) Binary Heap | cc by-sa | Introduction to Algorithms, Danderyds Gymnasium | 2.4 |
| binary search (interactive) | [`kattis:guess`](https://open.kattis.com/problems/guess) Guess the Number | cc by-sa | Kattis | 2.1 |
| binary search / Newton on big ints | [`kattis:prettygoodcuberoot`](https://open.kattis.com/problems/prettygoodcuberoot) Pretty Good Cube Root | cc by-sa | Baylor Competitive Learning course | 3.5 |
| bit manipulation | [`kattis:bitbybit`](https://open.kattis.com/problems/bitbybit) Bit by Bit | cc by-sa | Baylor Competitive Learning course | 2.1 |
| bit manipulation / boolean logic | [`kattis:logicfunctions`](https://open.kattis.com/problems/logicfunctions) Logic Functions | cc by-sa | Principles of Algorithmic Problem Solving | 1.7 |
| combinatorics | [`kattis:subcommittees`](https://open.kattis.com/problems/subcommittees) Subcommittees | cc by-sa | Principles of Algorithmic Problem Solving | 3.5 |
| combinatorics: Catalan numbers (big ints) | [`kattis:catalan`](https://open.kattis.com/problems/catalan) Catalan Numbers | cc by-sa | KTH CSC Popup 2005 | 2.8 |
| combinatorics: multinomials (big ints) | [`kattis:anagramcounting`](https://open.kattis.com/problems/anagramcounting) Anagram Counting | cc by-sa | Baylor Competitive Learning course | 3.0 |
| game / bits | [`kattis:bitgame`](https://open.kattis.com/problems/bitgame) Bit Game | cc by-sa | Principles of Algorithmic Problem Solving | 8.4 |
| geometry: closest pair | [`kattis:closestpair1`](https://open.kattis.com/problems/closestpair1) Closest Pair (Uniform) | cc by | KTH CSC Popup 2005 | 3.3 |
| geometry: closest pair (divide & conquer) | [`kattis:closestpair2`](https://open.kattis.com/problems/closestpair2) Closest Pair | cc by | KTH CSC Popup 2005 | 5.3 |
| geometry: convex hull | [`kattis:convexhull`](https://open.kattis.com/problems/convexhull) Convex Hull | cc by-sa | KTH CSC Popup 2005 | 2.4 |
| geometry: point in polygon | [`kattis:pointinpolygon`](https://open.kattis.com/problems/pointinpolygon) Point in Polygon | cc by-sa | KTH CSC Popup 2005 | 3.6 |
| geometry: polygon area | [`kattis:convexpolygonarea`](https://open.kattis.com/problems/convexpolygonarea) Convex Polygon Area | cc by-sa | Baylor Competitive Learning course | 1.8 |
| geometry: segment distance | [`kattis:segmentdistance`](https://open.kattis.com/problems/segmentdistance) Line Segment Distance | cc by-sa | KTH CSC Popup 2005 | 2.9 |
| geometry: segment intersection | [`kattis:segmentintersection`](https://open.kattis.com/problems/segmentintersection) Line Segment Intersection | cc by-sa | KTH CSC Popup 2005 | 4.6 |
| geometry: segment intersection counting | [`kattis:countingtriangles`](https://open.kattis.com/problems/countingtriangles) Counting Triangles | cc by-sa | Baylor Competitive Learning course | 1.8 |
| geometry: shoelace | [`kattis:polygonarea`](https://open.kattis.com/problems/polygonarea) Polygon Area | cc by-sa | KTH CSC Popup 2005 | 1.8 |
| geometry / hashing: collinear points | [`kattis:maxcolinear`](https://open.kattis.com/problems/maxcolinear) Maximum Number of Colinear Points | cc by-sa | KTH CSC Popup 2005 | 2.6 |
| geometry basics | [`kattis:triarea`](https://open.kattis.com/problems/triarea) Triangle Area | cc by-sa | Principles of Algorithmic Problem Solving | 1.2 |
| graphs | [`kattis:sneakattack`](https://open.kattis.com/problems/sneakattack) Sneak Attack | cc by-sa | Baylor Competitive Learning course | 7.8 |
| graphs: BFS | [`kattis:erdosnumbers`](https://open.kattis.com/problems/erdosnumbers) Erdős Numbers | cc by-sa | Baylor Competitive Learning course | 4.1 |
| graphs: BFS (knight moves) | [`kattis:hidingplaces`](https://open.kattis.com/problems/hidingplaces) Hiding Places | cc by-sa | Baylor Competitive Learning course | 1.6 |
| graphs: BFS / flood fill | [`kattis:10kindsofpeople`](https://open.kattis.com/problems/10kindsofpeople) 10 Kinds of People | cc by-sa | Baylor Competitive Learning course | 3.0 |
| graphs: BFS on grid | [`kattis:grid`](https://open.kattis.com/problems/grid) Grid | cc by-sa | 2015 Southeast USA Regionals Division 1 | 2.3 |
| graphs: BFS reachability | [`kattis:kastenlauf`](https://open.kattis.com/problems/kastenlauf) Kastenlauf | cc by-sa | German Collegiate Programming Contest %28GCPC%29 2013 | 2.7 |
| graphs: BFS/DFS path | [`kattis:torn2pieces`](https://open.kattis.com/problems/torn2pieces) Torn To Pieces | cc by-sa | 2015 ICPC North American Qualifier Contest | 2.6 |
| graphs: Bellman-Ford, negative cycles | [`kattis:shortestpath3`](https://open.kattis.com/problems/shortestpath3) Single source shortest path, negative weights | cc by | KTH CSC Popup 2005 | 2.0 |
| graphs: DAG / cycle detection | [`kattis:familydag`](https://open.kattis.com/problems/familydag) Family DAG | cc by-sa | Baylor Competitive Learning course | 6.0 |
| graphs: DAG longest path / topo order | [`kattis:longestpathinadag`](https://open.kattis.com/problems/longestpathinadag) Longest path in a DAG | cc by-sa | Principles of Algorithmic Problem Solving | 4.0 |
| graphs: DAG reachability counting | [`kattis:promotions`](https://open.kattis.com/problems/promotions) Promotions | cc by-sa | Southwestern Europe Regional Contest %28SWERC%29 2015 | 4.7 |
| graphs: DFS | [`kattis:martensdfs`](https://open.kattis.com/problems/martensdfs) Mårten's DFS | cc by-sa | Principles of Algorithmic Problem Solving | 2.1 - 2.3 |
| graphs: Dijkstra | [`kattis:shortestpath1`](https://open.kattis.com/problems/shortestpath1) Single source shortest path, non-negative weights | cc by | KTH CSC Popup 2005 | 1.9 |
| graphs: Dijkstra (time-tabled edges) | [`kattis:shortestpath2`](https://open.kattis.com/problems/shortestpath2) Single source shortest path, time table | cc by | KTH CSC Popup 2005 | 2.2 |
| graphs: Eulerian | [`kattis:eulerian`](https://open.kattis.com/problems/eulerian) Eulerian Graphs | cc by-sa | Principles of Algorithmic Problem Solving | 2.3 |
| graphs: Eulerian | [`kattis:eulerian2`](https://open.kattis.com/problems/eulerian2) Eulerian Graphs 2 | cc by-sa | Principles of Algorithmic Problem Solving | 2.5 |
| graphs: Eulerian path | [`kattis:eulerianpath`](https://open.kattis.com/problems/eulerianpath) Eulerian Path | cc by | KTH CSC Popup 2005 | 3.8 |
| graphs: Floyd-Warshall | [`kattis:allpairspath`](https://open.kattis.com/problems/allpairspath) All Pairs Shortest Path | cc by | KTH CSC Popup 2005 | 2.6 |
| graphs: MST | [`kattis:islandhopping`](https://open.kattis.com/problems/islandhopping) Island Hopping | cc by-sa | Baylor Competitive Learning course | 2.0 |
| graphs: MST | [`kattis:lostmap`](https://open.kattis.com/problems/lostmap) Lost Map | cc0 | 2017 ACM ICPC North Central North America Regional Contest | 1.5 |
| graphs: MST | [`kattis:minspantree`](https://open.kattis.com/problems/minspantree) Minimum Spanning Tree | cc by | KTH CSC Popup 2005 | 2.4 |
| graphs: adjacency matrix | [`kattis:weakvertices`](https://open.kattis.com/problems/weakvertices) Weak Vertices | cc by-sa | Baylor Competitive Learning course | 1.3 |
| graphs: all-pairs shortest path | [`kattis:transportationplanning`](https://open.kattis.com/problems/transportationplanning) Transportation Planning | cc by-sa | Baylor Competitive Learning course | 3.9 |
| graphs: connected components | [`kattis:reachableroads`](https://open.kattis.com/problems/reachableroads) Reachable Roads | cc by-sa | Baylor Competitive Learning course | 1.7 |
| graphs: flood fill | [`kattis:countingstars`](https://open.kattis.com/problems/countingstars) Counting Stars | cc by-sa | International Collegiate Programming Contest %28ACM-ICPC%29 Dress Rehearsal 2012 | 2.2 |
| graphs: max flow | [`kattis:maxflow`](https://open.kattis.com/problems/maxflow) Maximum Flow | cc by | KTH CSC Popup 2005 | 3.1 |
| graphs: min cut | [`kattis:mincut`](https://open.kattis.com/problems/mincut) Minimum Cut | cc by | KTH CSC Popup 2006 | 2.4 |
| graphs: min-cost max-flow | [`kattis:mincostmaxflow`](https://open.kattis.com/problems/mincostmaxflow) Minimum Cost Maximum Flow | cc by | KTH CSC Popup 2005 | 3.8 |
| graphs: shortest path (multiplicative weights) | [`kattis:getshorty`](https://open.kattis.com/problems/getshorty) Get Shorty | cc by |  | 2.2 |
| graphs: shortest path with constraints | [`kattis:shortestpath4`](https://open.kattis.com/problems/shortestpath4) Single source shortest path, safe path | cc by-sa | NUS Competitive Programming | 3.5 |
| greedy: Zeckendorf | [`kattis:fibonaccisum`](https://open.kattis.com/problems/fibonaccisum) Minimal Fibonacci Sums | cc by-sa | Principles of Algorithmic Problem Solving | 4.0 |
| greedy: interval cover | [`kattis:intervalcover`](https://open.kattis.com/problems/intervalcover) Interval Cover | cc by | KTH CSC Popup 2006 | 4.3 |
| greedy: interval scheduling | [`kattis:intervalscheduling`](https://open.kattis.com/problems/intervalscheduling) Interval Scheduling | cc by-sa | Algorithm Design, ITU 2019 | 1.8 |
| greedy / arrays | [`kattis:greedilyincreasing`](https://open.kattis.com/problems/greedilyincreasing) Greedily Increasing Subsequence | cc by-sa | HiQ Challenge 2017 | 1.5 |
| hash maps | [`kattis:babelfish`](https://open.kattis.com/problems/babelfish) Babelfish | cc by-sa | Waterloo Programming Contest 2001-09-22 | 2.0 |
| hash maps | [`kattis:securedoors`](https://open.kattis.com/problems/securedoors) Secure Doors | cc by-sa | Baylor Competitive Learning course | 1.6 |
| hash maps / parsing | [`kattis:addingwords`](https://open.kattis.com/problems/addingwords) Adding Words | cc by-sa | Baylor Competitive Learning course | 2.1 |
| hash sets | [`kattis:compoundwords`](https://open.kattis.com/problems/compoundwords) Compound Words | cc by-sa | Baylor Competitive Learning course | 1.6 |
| hashing | [`kattis:deduplicatingfiles`](https://open.kattis.com/problems/deduplicatingfiles) Deduplicating Files | cc by-sa | Baylor Competitive Learning course | 3.0 |
| hashing: primes for table sizes | [`kattis:enlarginghashtables`](https://open.kattis.com/problems/enlarginghashtables) Enlarging Hash Tables | cc by-sa | Baylor Competitive Learning course | 2.3 |
| hashing / XOR | [`kattis:oddmanout`](https://open.kattis.com/problems/oddmanout) Odd Man Out | cc by | Google Code Jam 2010 Online Competition Africa | 1.5 |
| heaps / order statistics | [`kattis:splitmedian`](https://open.kattis.com/problems/splitmedian) Split Median | cc by-sa | T-301-REIR Algorithms | 2.0 - 9.0 |
| heuristics: TSP | [`kattis:tsp`](https://open.kattis.com/problems/tsp) Travelling Salesperson 2D | cc by-sa | KTH CSC Avancerade Algoritmer 2006 | 1.5 - 9.8 |
| interpreter / parsing | [`kattis:basicinterpreter`](https://open.kattis.com/problems/basicinterpreter) BASIC Interpreter | cc by-sa | Baylor Competitive Learning course | 4.6 |
| interval reasoning | [`kattis:thinkingofanumber`](https://open.kattis.com/problems/thinkingofanumber) I'm Thinking of a Number | cc by-sa | Baylor Competitive Learning course | 3.5 |
| linear algebra: Gaussian elimination | [`kattis:equationsolver`](https://open.kattis.com/problems/equationsolver) Linear Equation Solver | cc by-sa | KTH CSC Popup 2005 | 4.3 |
| linear algebra: Gaussian elimination (partial) | [`kattis:equationsolverplus`](https://open.kattis.com/problems/equationsolverplus) Partial Linear Equation Solver | cc by-sa | KTH CSC Popup 2005 | 6.4 |
| long division / cycle detection | [`kattis:repeatingdecimal`](https://open.kattis.com/problems/repeatingdecimal) Repeating Decimal | cc by-sa | Baylor Competitive Learning course | 4.2 |
| math: approximations | [`kattis:stirlingsapproximation`](https://open.kattis.com/problems/stirlingsapproximation) Stirling's Approximation | cc by-sa | Baylor Competitive Learning course | 3.8 |
| math: digits of factorials | [`kattis:inversefactorial`](https://open.kattis.com/problems/inversefactorial) Inverse Factorial | cc by-sa | 2016 ICPC North American Qualifier Contest | 4.9 |
| math: digits of factorials (logs) | [`kattis:howmanydigits`](https://open.kattis.com/problems/howmanydigits) How Many Digits? | cc by-sa | Baylor Competitive Learning course | 3.1 |
| matrix exponentiation | [`kattis:linearrecurrence`](https://open.kattis.com/problems/linearrecurrence) Linear Recurrences | cc by | KTH CSC Popup spring 2013 | 4.2 |
| number bases | [`kattis:mixedbasearithmetic`](https://open.kattis.com/problems/mixedbasearithmetic) Mixed-Base Arithmetic | cc by-sa | Baylor Competitive Learning course | 5.4 |
| number bases | [`kattis:parsinghex`](https://open.kattis.com/problems/parsinghex) Parsing Hex | cc by-sa | Baylor Competitive Learning course | 2.3 |
| number theory: CRT | [`kattis:chineseremainder`](https://open.kattis.com/problems/chineseremainder) Chinese Remainder | cc by-sa | KTH CSC Popup 2005 | 2.6 |
| number theory: Euler totient | [`kattis:inversetotient`](https://open.kattis.com/problems/inversetotient) Inverse Totient | Public Domain | Principles of Algorithmic Problem Solving | 7.3 |
| number theory: Fermat test, modexp | [`kattis:pseudoprime`](https://open.kattis.com/problems/pseudoprime) Pseudoprime numbers | cc by | Waterloo Programming Contest 2007-09-23 | 2.9 |
| number theory: Legendre formula | [`kattis:factorialpower`](https://open.kattis.com/problems/factorialpower) Factorial Power | Public Domain | Principles of Algorithmic Problem Solving | 3.5 |
| number theory: RSA, modular inverse | [`kattis:crackingrsa`](https://open.kattis.com/problems/crackingrsa) Cracking RSA | cc by-sa | 2016 Virginia Tech High School Programming Contest | 1.8 |
| number theory: divisor counting | [`kattis:divisorcounts`](https://open.kattis.com/problems/divisorcounts) Divisor Counts | Public Domain | Principles of Algorithmic Problem Solving | 2.5 |
| number theory: divisor function | [`kattis:productdivisors`](https://open.kattis.com/problems/productdivisors) Product Divisors | Public Domain | Principles of Algorithmic Problem Solving | 5.2 |
| number theory: divisors | [`kattis:positivedivisors`](https://open.kattis.com/problems/positivedivisors) Positive Divisors | Public Domain | Principles of Algorithmic Problem Solving | 2.5 |
| number theory: factorisation | [`kattis:primalrepresentation`](https://open.kattis.com/problems/primalrepresentation) Primal Representation | cc by-sa | Baylor Competitive Learning course | 2.8 |
| number theory: factorisation | [`kattis:primereduction`](https://open.kattis.com/problems/primereduction) Prime Reduction | cc by-sa | Baylor Competitive Learning course | 2.5 |
| number theory: gcd | [`kattis:gcd`](https://open.kattis.com/problems/gcd) GCD | Public Domain | Principles of Algorithmic Problem Solving | 1.4 |
| number theory: gcd sums | [`kattis:gcdsum`](https://open.kattis.com/problems/gcdsum) GCD Sum | cc by-sa | Principles of Algorithmic Problem Solving | 6.1 |
| number theory: gcd sums | [`kattis:gcdsum2`](https://open.kattis.com/problems/gcdsum2) GCD Sum 2 | Public Domain | Principles of Algorithmic Problem Solving | 5.4 |
| number theory: gcd/lcm | [`kattis:gcdandlcm`](https://open.kattis.com/problems/gcdandlcm) GCD and LCM | cc by-sa | Principles of Algorithmic Problem Solving | 3.6 |
| number theory: general CRT | [`kattis:generalchineseremainder`](https://open.kattis.com/problems/generalchineseremainder) Chinese Remainder Theorem (non-relatively prime moduli) | cc by-sa | KTH CSC Popup 2005 | 2.5 |
| number theory: lcm | [`kattis:smallestmultiple`](https://open.kattis.com/problems/smallestmultiple) Smallest Multiple | cc by-sa | Baylor Competitive Learning course | 2.8 |
| number theory: modular inverse | [`kattis:modulararithmetic`](https://open.kattis.com/problems/modulararithmetic) Modular Arithmetic | cc by-sa | KTH CSC Popup 2005 | 2.3 |
| number theory: multiplicative functions | [`kattis:arithmeticfunctions`](https://open.kattis.com/problems/arithmeticfunctions) Arithmetic Functions | cc by-sa | Principles of Algorithmic Problem Solving | 2.0 |
| number theory: primality (Miller-Rabin) | [`kattis:primality`](https://open.kattis.com/problems/primality) Primality | cc by-sa | Principles of Algorithmic Problem Solving | 2.0 - 4.4 |
| number theory: prime counting | [`kattis:primecount`](https://open.kattis.com/problems/primecount) Prime Count | Public Domain | Principles of Algorithmic Problem Solving | 2.7 - 7.8 |
| number theory: primes | [`kattis:goldbach2`](https://open.kattis.com/problems/goldbach2) Goldbach's Conjecture | cc by-sa | 2013 ACM-ICPC North American Qualifier | 1.8 |
| number theory: primes | [`kattis:primes2`](https://open.kattis.com/problems/primes2) Blackboard Numbers | cc by-sa | IDI Open 2015 | 3.1 |
| number theory: primes + prefix sums | [`kattis:longestprimesum`](https://open.kattis.com/problems/longestprimesum) Longest Prime Sum | cc by-sa | Principles of Algorithmic Problem Solving | 2.0 |
| number theory: sieve | [`kattis:primesieve`](https://open.kattis.com/problems/primesieve) Prime Sieve | cc by-sa | KTH CSC Popup 2005 | 5.0 |
| number theory: trailing digits of n! | [`kattis:loworderzeros`](https://open.kattis.com/problems/loworderzeros) Low Order Zeros | cc by-sa | Baylor Competitive Learning course | 3.6 |
| parsing: expression evaluation | [`kattis:calculator`](https://open.kattis.com/problems/calculator) Calculator | cc by-sa | KTH CSC Popup 2005 | 2.9 |
| polynomials: FFT multiplication | [`kattis:polymul2`](https://open.kattis.com/problems/polymul2) Polynomial Multiplication 2 | cc by | KTH CSC Avalg 2006 | 4.5 |
| polynomials: naive multiplication | [`kattis:polymul1`](https://open.kattis.com/problems/polymul1) Polynomial Multiplication 1 | cc by | KTH CSC Avalg 2006 | 1.7 |
| rationals / gcd | [`kattis:rationalarithmetic`](https://open.kattis.com/problems/rationalarithmetic) Rational Arithmetic | cc by-sa | KTH CSC Popup 2005 | 2.6 |
| sorting: custom comparator | [`kattis:sidewayssorting`](https://open.kattis.com/problems/sidewayssorting) Sideways Sorting | cc by-sa | Baylor Competitive Learning course | 1.7 |
| sorting: stable sort | [`kattis:sortofsorting`](https://open.kattis.com/problems/sortofsorting) Sort of Sorting | cc by-sa | Baylor Competitive Learning course | 1.6 |
| sorting / sets | [`kattis:bookingaroom`](https://open.kattis.com/problems/bookingaroom) Booking a Room | cc by-sa | Northwestern Europe Regional Contest %28NWERC%29 2014 Practice Session | 1.6 |
| sorting basics | [`kattis:sorttwonumbers`](https://open.kattis.com/problems/sorttwonumbers) Sort Two Numbers | cc by-sa | Kattis | 1.2 |
| string hashing (polynomial) | [`kattis:hashing`](https://open.kattis.com/problems/hashing) String Hashing | cc by-sa | KTH CSC Popup 2016 | 4.7 |
| strings | [`kattis:selfsimilarstrings`](https://open.kattis.com/problems/selfsimilarstrings) Self-Similar Strings | cc by-sa | Baylor Competitive Learning course | 2.7 |
| strings: Aho-Corasick | [`kattis:stringmultimatching`](https://open.kattis.com/problems/stringmultimatching) String Multimatching | cc by | KTH CSC Popup 2005 | 4.0 |
| strings: BWT / suffix sorting | [`kattis:burrowswheeler`](https://open.kattis.com/problems/burrowswheeler) Burrows-Wheeler | cc by-sa | Baylor Competitive Learning course | 4.9 |
| strings: KMP / Z | [`kattis:stringmatching`](https://open.kattis.com/problems/stringmatching) String Matching | cc by | KTH CSC Popup 2005 | 2.9 |
| strings: palindromic substrings | [`kattis:palindromesubstring`](https://open.kattis.com/problems/palindromesubstring) Palindrome Substring | cc by-sa | Baylor Competitive Learning course | 3.0 |
| strings: repeated substrings (suffix structures) | [`kattis:substrings`](https://open.kattis.com/problems/substrings) Repeated Substrings | cc by-sa | Rocky Mountain Regional Contest %28RMRC%29 2014 | 5.2 |
| strings: suffix array | [`kattis:suffixsorting`](https://open.kattis.com/problems/suffixsorting) Suffix Sorting | cc by | KTH CSC Popup 2005 | 4.3 |
| strings / search | [`kattis:dictionaryattack`](https://open.kattis.com/problems/dictionaryattack) Dictionary Attack | cc by-sa | Baylor Competitive Learning course | 6.0 |
| two pointers / sets on sorted lists | [`kattis:cd`](https://open.kattis.com/problems/cd) CD | cc by | Waterloo Programming Contest 2010-09-26 | 2.1 |
| union-find | [`kattis:unionfind`](https://open.kattis.com/problems/unionfind) Union-Find | cc by | KTH CSC Popup spring 2013 | 2.4 |
| union-find | [`kattis:virtualfriends`](https://open.kattis.com/problems/virtualfriends) Virtual Friends | cc by-sa | Waterloo Programming Contest 2008-09-27 | 2.7 |
| union-find (with moves) | [`kattis:almostunionfind`](https://open.kattis.com/problems/almostunionfind) Almost Union-Find | cc by | Rujia Liu's Present 3%3A A datastructure contest celebrating the 100th anniversary of Tsinghua University | 3.3 |
| warm-up: big integers | [`kattis:different`](https://open.kattis.com/problems/different) A Different Problem | cc by-sa | Kattis | 2.0 |
| warm-up I/O | [`kattis:addtwonumbers`](https://open.kattis.com/problems/addtwonumbers) Add Two Numbers | cc by-sa | Kattis | 1.2 |
| warm-up I/O | [`kattis:hello`](https://open.kattis.com/problems/hello) Hello World! | Public Domain | Kattis | 1.2 |
| warm-up strings | [`kattis:echoechoecho`](https://open.kattis.com/problems/echoechoecho) Echo Echo Echo | cc by-sa | Kattis | 1.2 |

## 4. ICPC and regional problem packages with open licences

All in Kattis/BAPCtools package format: `problem.yaml` (licence line),
`problem_statement/*.tex`, `data/sample`, `data/secret` (full test data),
`submissions/accepted` (reference solutions), often `solution.en.tex`
(jury solution slide). Caches are sparse clones without `data/secret`
(re-enable with `git sparse-checkout disable`); `icpc-ecna` is complete.

| source id | repo @ pin | contests | packages | licence evidence | solution slides |
|---|---|---|---|---|---|
| `icpc-kattis-export` | mzuenni/kattis-export @ bd404d38 | GCPC 2011–2026 (excl. 2020), NWERC 2023, 2024, 2025 (+ practice) | 233 (`problem.yaml` found in 221 dirs, all `license: cc by-sa`) | `nwerc2023/arrangingadapters/problem.yaml`: "license: cc by-sa / rights_owner: author" | 125 `solution.en.tex` |
| `icpc-mzuenni` | mzuenni/icpc-problems @ 351157ef | NWERC 2022–2024, GCPC 2021–2022, Winter Contest 2022–2025 (overlaps the row above) | 38 | 38× "license: cc by-sa" | 28 |
| `icpc-dapc` | To5BG/dapc-problems @ 7e7028b8 | BAPC preliminaries 2022, 2023 | 25 | 25× "license: cc by-sa" | 25 |
| `icpc-rmc` | icpc/na-rocky-mountain-<year>-public (8 repos, pins in FETCHED.txt) | Rocky Mountain Regional 2018–2025/26 | ≈108 (97 with `problem.yaml`, all `license: cc by-sa`; 2023–24 uses another layout) | `2020/problems/antimatterrain/problem.yaml`: "license: cc by-sa"; repos 2018, 2020, 2022–23, 2023–24 also have an MIT `LICENSE` | slides.pdf per year |
| `icpc-ecna` | icpc/na-ecna-archive @ a6e190a1 | ECNA 2019–2026 | 91 zipped packages | `LICENSE`: "CC0 1.0 Universal"; `problem.yaml`: "license: cc0" | none |

Keyword tags pulled from the solution slides (`_tags.json` in each cache;
regex over the slide text, unverified, a judge-side aid only):
kattis-export: sorting 16, dp 14, simulation 10, bitmask 8, strings 7,
geometry 7, number theory 7, probability 7, flow/matching 5, BFS 5,
greedy 5, shortest paths 4, binary search 4, segment/Fenwick 3,
union-find 2, topo sort 1, FFT 1. Examples per tag are in the master
table.

Found but not cached (same licence pattern, CC BY-SA in `problem.yaml`,
with test data): Swedish Olympiad packages `Kodsport/swedish-olympiad-2013`
… `-2019`, `-2026` and Baltic Olympiad 2018
(`nordicolympiad/baltic-olympiad-2018`); `csecutsc/utscode2`. Olympiad
level; Part IV capstones if wanted.

Not reachable: nwerc.eu, bapc.eu, icpc.global host the official NWERC /
BAPC / World Finals packages (403, see blocked hosts). The GitHub copies
above cover NWERC 2022–2025 and BAPC preliminaries 2022–2023 only.

## 5. MIT OCW algorithm and systems courses (CC BY-NC-SA 4.0 → NC cards)

Licence evidence for each course: the course page's metadata,
`"license": "https://creativecommons.org/licenses/by-nc-sa/4.0/"`, at
`https://ocw.mit.edu/courses/<slug>/`. OCW's terms note that third-party
content inside a handout can be excluded from the CC licence; check each
card's PDF for such a notice. Each cache dir has `index.tsv` (file → OCW
title → URL) and `.txt` per PDF.

| source id | keyed? | what is there | topics, problem by problem |
|---|---|---|---|
| `mitocw-6-006-spring2020` | **yes**, all | ps0–ps8 questions + solutions + **code templates with `tests.py`** (ps0–ps7); problem sessions 1–9 + solutions; quizzes 1–3, reviews, final + solutions | ps0 sets, probability, induction, count_long_subarray (code) · ps1 asymptotics, sequence interfaces, Binder Bookmarks, doubly linked list (code) · ps2 recurrences, Sorting Sorts, Friend Finder, Beaver Bookings (code) · ps3 hashing ×4, Anagram Archaeology (code) · ps4 binary trees, heaps, Gardening Contest, Solar Supply, Robot Wrangling, AVL augmentation (code) · ps5 graph practice, Power Plants, Short-Circuitry, Ancient Avenue, Statum Quest, 6.006 Tilt (BFS, code) · ps6 Dijkstra, negative cycles, Johnson's algorithm (code) · ps7–ps8 DP (Effective Campaigning, Caged Cats, Odd Paths, Pizza Partitioning, Shorting Stocks (code), Oil Well, Splits Bowling, Quarter Partition, Corrupt Chronicles) |
| `mitocw-6-006-fall2011` | **yes** | ps1–ps7 + written solutions + **code (ZIP) + code solutions (ZIP)**; quizzes 1–2, final + solutions | ps1 asymptotics, recurrences, peak finding · ps2 fractal rendering, circuit simulation (PQ) · ps3 range queries (BST/AVL), circuit layout (sweep) · ps4 hash functions, Python dicts, DNA matching (rolling hash) · ps5 Knight's Shield, RSA, image decryption (big-number arithmetic) · ps6 graph search, Rubik's cube BFS, Dijkstra · ps7 seam carving (DP), HG Fargo |
| `mitocw-6-006-spring2008` | partly | ps1–ps6 + LaTeX + templates (no pset solutions); quiz/final practice problems with solutions; lecture code (BFS, DFS, AVL, heap, rolling hash, Dijkstra…) | DSA basics; only the practice problems are keyed |
| `mitocw-6-046j-spring2015` | **yes** | ps1–ps10, quizzes 1–2, final, all with solutions; recitations | D&C (restaurant location, radio frequency) · pattern matching, B-trees · vEB · amortised FIFO queues, quicksort analysis · skip lists, randomised prizes · APSP, MST · max flow (dynamic network, disjoint roads, orders) · simplex, NP-completeness · knapsack approximation, FPT · distributed: leader election in a ring, BFS in an asynchronous network |
| `mitocw-6-046j-spring2012` | **yes** | ps1–ps9 + solutions; quizzes, practice quizzes, two practice finals, final + solutions | median select, 1D land sale · unique MST, SP vs MST · electric potential (FFT) · word search via FFT · randomised select bounds · amortised balanced trees · vEB · union-by-rank, NP-hard or P · plumbing (flow), Huffman |
| `mitocw-6-046j-fall2005` | **yes** | ps1–ps9 with solutions, quizzes + practice + finals with solutions; edit-distance code | asymptotics, recurrences, unimodal search · almost-sorted, weighted median · treaps, balance · skip lists, B-trees, planar points · electronic billboard (amortised), red-black restructuring · edit distance, GreedSox · no-left-turns shortest path, video game design · parallel merge sort |
| `mitocw-6-851-spring2012` | **yes** | ps1–ps10 + solutions | persistent/retroactive DS, geometric DS, dynamic optimality, memory hierarchy, hashing, integer DS, succinct DS, string DS, dynamic graphs |
| `mitocw-6-854j-fall2008` | yes (1–6) | ps1–ps6 + solutions; 2001 sets (unkeyed) | advanced algorithms: amortisation, heaps, flows, LP, approximation, online, hashing |
| `mitocw-6-854j-fall2005` | yes (11 of 12) | ps1–ps12, sol1–sol11, handouts (splay, Fibonacci heaps, persistence, min-cost flow, duality) | same areas as above |
| `mitocw-6-856j-fall2002` | **yes** | hw1–hw13 + ans1–ans13 | randomised algorithms: expectation, Chernoff, hashing, random walks, Markov chains |
| `mitocw-6-042j-fall2005` | **yes** | ps1–ps10, quizzes, final, with solutions | proofs, induction, number theory and RSA, graphs, counting, probability, recurrences, asymptotics |
| `mitocw-6-042j-fall2010` | partly | 10 problem sets (no solutions), recitation problems, midterm + finals 2004/2006/2008 with solutions | same; finals and midterm are keyed |
| `mitocw-6-890-fall2014` | **yes** | ps1–ps4 + solutions | NP-hardness reductions, 3-Partition, hardness of games |
| `mitocw-6-824-spring2006` | **yes** | quiz 1 and 2 (2005) with answers | distributed systems, but each question is about an assigned paper (Frangipani, Ivy, Porcupine, OKWS, XOM, Paxos-style protocols) |
| `mitocw-6-830-fall2010` | **yes** | quiz 1 and 2 + solutions | DB internals: OCC, schema design, external aggregation, cost estimation, ARIES/CLRs, snapshot isolation, C-Store, BigTable, distributed query execution |

Checked and without keyed exercises for this scope: 6.033 Spring 2018
(design project and critiques with rubrics, no keys), 6.828 Fall 2012
(OS labs; out of scope). Not on OCW: 6.006 Fall 2009, 6.1210, 6.1220J,
6.824 Spring 2020, 18.410J Spring 2015, 6.033 Spring 2005/2009 (404).

## 6. Erickson and ODS: which exercises suit a code exercise

The inventory agents count these; here one chapter of each was sampled
to say what share fits a `code` exercise (statement has concrete input
and output, so AI tests plus an AI reference can check it) versus a
written answer (proofs, reductions, "give an example").

| sample | exercise items | fit for code exercise | written | notes |
|---|---|---|---|---|
| `jeffe` ch. 3 Dynamic Programming (CC BY 4.0) | ~52 items (heuristic split on item starts) | ~44: "Describe and analyze an algorithm that finds/computes …" over arrays or strings with worked examples (e.g. max subarray sum and product with examples [−6, 12, −7, 0, 14, −7, 5] → 19 and 504; text segmentation counts; LCS / shortest common supersequence / bitonic / oscillating subsequences; Dream-Dollar change) | ~8 (prove greedy fails, counterexamples) | pdftotext drops digits and small caps in this PDF (e.g. "$ , $ , $"), so statements must be re-extracted before use |
| `jeffe` ch. 6 Depth-first search | ~32 | ~20 | ~12 | graph-algorithm design items fit; proofs don't |
| `jeffe-notes` 11-unionfind (CC BY-NC-SA → NC cards) | 7 | 1 | 6 | mostly analysis proofs |
| `ods` arrays.tex (CC BY) | 13 | ~10 ("Design and implement a RandomQueue/Treque/…", "Implement rotate(a, r)") | ~3 ("Where is the extra non-null value?", "Explain why …") | ods ships `python/ods/tests/` (listtest.py, settest.py, sorttest.py, heaptest.py, graphtest.py, test_<structure>.py): CC BY test harnesses that fit "implement X" exercises directly |

Across all ODS chapters (171 exercises), ~57 begin "Design and
implement / Implement / Write"; linkedlists (15 of 19), arrays (10 of
13), rbs (8 of 14) are the most code-shaped; hashing (0 of 11) and
intro (0 of 7) are written.

## 7. TheAlgorithms and other MIT test-case sources

`thealgorithms-python` (MIT, pin 574d100b). Directories, files, files
with doctests, doctest lines:

| dir | files | with doctests | `>>>` lines |
|---|---|---|---|
| data_structures (arrays 20/21, binary_tree 35/36, linked_list 23/23, stacks 17/18, queues 8/10, heap 7/8, hashing 6/11, disjoint_set 2/3, trie 2/3, kd_tree 0/9, suffix_tree 0/7) | 150 | 120 | 2696 |
| maths | 220 | 211 | 2131 |
| graphs | 73 | 55 | 806 |
| sorts | 60 | 57 | 730 |
| strings | 67 | 66 | 500 |
| dynamic_programming | 53 | 51 | 401 |
| ciphers | 54 | 49 | 396 |
| searches | 18 | 16 | 320 |
| bit_manipulation | 32 | 31 | 314 |
| backtracking | 23 | 22 | 267 |
| matrix | 27 | 24 | 263 |
| geometry | 14 | 9 | 171 |
| scheduling | 11 | 10 | 152 |
| divide_and_conquer | 16 | 13 | 142 |
| linear_algebra | 17 | 14 | 140 |
| hashes | 15 | 14 | 88 |
| greedy_methods | 13 | 12 | 78 |
| networking_flow | 5 | 4 | 41 |
| knapsack | 7 | 3 | 10 |
| project_euler (MIT code; the PE statements are NC) | 322 | 181 | 941 |

Topics with few or no doctests: kd trees, suffix trees, knapsack/,
web_programming. Doctests pin the implementation's own function
signature and sometimes its quirks; a test lifted from here must not add
a requirement the exercise statement doesn't make (§6.3).

`thealgorithms-javascript`: **GPL-3.0**, link-only (346 `*.test.js`
files; do not port).

MIT JS and Python alternatives fetched:
- `trekhleb-jsalgo` (MIT): jest tests, data-structures 19 test dirs /
  259 tests; algorithms: sorting 11/73, math 18/85, graph 15/43, sets
  11/27, string 8/12, search 4/8, cryptography 3/19, uncategorized 8/31.
- `keon-algorithms` (MIT): `tests/` with ~590 unittest methods across
  arrays, backtracking, bit manipulation, DP, graph, greedy, heap, linked
  list, map, math, matrix, queue, searching, set, sorting, stack,
  string, tree, segment tree, vEB tree.
- `icc` (Apache-2.0): each challenge has a challenge notebook (statement),
  a solution notebook and `test_<name>.py`, so it supplies statement,
  reference and tests together. ~91 challenges outside `online_judges/`.
  Many are restatements of classic interview problems (several follow
  *Cracking the Coding Interview*'s problem list); the wording is the
  author's, so the licence holds, but the judge may want to know.
  `online_judges/` (20) restates LeetCode/HackerRank problems with links
  to them and is link-only.

## 8. Project Euler (`projecteuler`, CC BY-NC-SA 4.0 → NC cards)

Evidence, https://projecteuler.net/copyright: "All of the main problem
content that appears in the Archives and the Recent problems sections is
licensed under a Creative Commons (CC) Licence: Attribution-NonCommercial-
ShareAlike 4.0 International (CC BY-NC-SA 4.0)". The page also asks for
"The following problem is taken from Project Euler" or "inspired by
problem {id}". No answers are published, so reference and tests are
AI-written. Cached: statements 1–200.

| topic | problems (by number) |
|---|---|
| primes, sieves, factorisation | 3, 7, 10, 27, 35, 37, 41, 46, 47, 49, 50, 51, 58, 60, 87, 111, 123, 187 |
| divisors, gcd, totient, fractions | 5, 12, 21, 23, 33, 69, 70, 71, 72, 73, 95, 108, 110, 179, 193 |
| modular arithmetic, fast exponentiation, RSA | 48, 97, 120, 122 (addition chains), 129–133 (repunits), 182, 188 |
| big integers, digit manipulation | 13, 16, 20, 25, 30, 34, 36, 40, 55, 56, 63, 92, 104, 112, 113 |
| DP and counting paths | 14 (memoised Collatz), 15, 18, 67 (max path in triangle), 31 (coin sums), 76, 77, 78 (partitions), 81, 82, 114–117 (tilings), 164, 172, 178, 191 |
| graphs | 79 (passcode: topological order), 83 (min path, four directions: Dijkstra), 107 (minimal network: MST), 186 (union-find over a stream) |
| combinatorics, permutations | 15, 24 (lexicographic permutations), 43, 53, 62 (cubic permutations: hashing), 68, 90, 106, 158 |
| sequences, number shapes, Pell, continued fractions | 2, 28, 42, 44, 45, 57, 61, 64, 65, 66, 94, 100, 137, 138, 140 |
| geometry | 39, 75, 91, 102 (triangle containment), 144, 165 (segment intersections), 184 |
| search, backtracking, puzzles | 4, 9, 32, 38, 43, 68, 93, 96 (Su Doku), 185 |
| probability, Markov chains | 84 (Monopoly odds), 121, 151 |
| strings and files | 17, 22, 42, 54 (poker), 59 (XOR decryption), 89 (Roman numerals), 98 |
| subarray / sliding window | 8, 11, 149 (maximum-sum subsequence in a grid), 150 |

Topic assignment by this finder from titles and statements (PE has no
tags).

## 9. Other open exercise sources checked

| source | licence (evidence) | what | status |
|---|---|---|---|
| `opendsa-exercises` (registered) | MIT: `MIT-license.txt` "OpenDSA Project Distributed under the MIT License" | ~1650 Khan-style exercise HTML (keyed MC / fill-in): Sorting 147, List 72, AlgAnal 75, Hashing 47, RecurTutor 40, Binary trees 32, Graph 30, Background 25, NP 6, Searching 3; ~50 DSA proficiency exercises (simulate the algorithm: insertionSort, mergesort, quicksort, heapsort, shellsort, radixExchangeSort, binarySearch, BSTinsert/remove/search, AVLinsert, redBlackTree, bPlusTreeInsert, heapbuild/insert/remove, hashing, openHashing, rehashing, UnionFind, infixToPostfix, postfixEvaluation, tries) | open, keyed; fits `sequence` and `choice`. Prose is in `opendsa` (another finder) |
| sdp flash cards and solutions (registered as `sdp`) | CC BY 4.0 | System Design.apkg 42 notes, System Design Exercises.apkg 8, OO Design.apkg 6; 8 system design + 6 OO design worked exercises | open, keyed; the only open system design exercise set found besides Kleppmann |
| `kleppmann-ds` (cached by another finder, not yet in registry) | CC BY-SA 4.0: README "The material is published under a Creative Commons BY-SA license" | 23 `\supervision{question}{solution}` exercises in `dist-sys.tex` (`solutions.tex` builds the key) | open, keyed, Part V |
| AllenDowney/ThinkDataStructures | repo MIT ("The MIT License (MIT) Copyright (c) 2016 Allen Downey"); book text CC BY-NC-SA at greenteapress.com (blocked, not verified) | Java exercises with JUnit tests (code MIT), statements in the NC book | NC card candidate once the book licence is verified; not fetched |
| RunestoneInteractive/pythonds | CC BY-NC-SA 4.0 (`LICENSE.txt`: "This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License") | *Problem Solving with Algorithms and Data Structures*: end-of-chapter exercises, unkeyed | NC unkeyed; not fetched |
| pllk/cphb (*Competitive Programmer's Handbook*) | CC BY-NC-SA 4.0 (README "The license of the book is Creative Commons BY-NC-SA 4.0.") | no exercises of its own; points to CSES | prose NC → link-only |
| `mcs` (*Mathematics for Computer Science* 2015, cached by another finder) | CC BY-NC-SA 3.0 per that finder's NOTE.txt | ~780 "Problem n.m" items, unkeyed | NC exercise cards possible (counting, number theory, graphs, probability); the other finder marked it link-only as prose |
| Wikibooks *Algorithms*, *Data Structures* | CC BY-SA | sampled DP, greedy, D&C, backtracking, trees: no exercise sections (Hash Tables has one heading) | nothing to take |
| LibreTexts Engineering | per page | DSA texts fetched by other finders (`lt-njoroge`, `lt-justo`, `lt-csbu`) | exercises to be counted by inventory |
| Open Textbook Library (open.umn.edu) | — | TLS failure through the proxy | not checked |
| jepsen-io/maelstrom (Gossip Glomers workloads) | EPL-1.0 | distributed-systems challenges with a checker | EPL is copyleft and not BY-SA-compatible: link-only |
| ByteByteGoHq/system-design-101 | CC BY-NC-ND 4.0 (`LICENSE.md`) | visual explainers | ND: link-only |
| karanpratapsingh/system-design | CC BY-NC-ND 4.0 (`LICENSE`) | course text | ND: link-only |
| teivah/algodeck | CC BY-NC-ND 4.0 (`LICENSE.md`) | algorithm flash cards | ND: link-only |
| weeeBox/mobile-system-design | "All rights reserved" (`LICENSE.md`) | mobile design framework | link-only |
| Addi-11/system-design-excercises | MIT by a third party, but described as "System design exercises by Arpit Bhayani" | restated exercises | licence unclear (repackaged third-party content): link-only |
| checkcheckzz/system-design-interview, arpitbbhayani/system-design-questions, shashank88/system_design | no licence | link lists / question lists | link-only |

## 10. Link-only items, with reasons

- LeetCode, Codeforces, AtCoder, HackerRank, SPOJ, UVa / onlinejudge.org,
  CSES: statements are all rights reserved (and the hosts are blocked
  here). cp-algorithms' practice links point to these. Link-only.
- Kattis problems labelled "For educational use only" or with no badge:
  ballotboxes, bits, bst, ferryloading, hash, islands, modulo, pot,
  relatives, reseto, sumkindofproblem. Link-only.
- TheAlgorithms/JavaScript: GPL-3.0. Link-only.
- icc `online_judges/`: restates LeetCode/HackerRank. Link-only.
- MIT OCW prose (lecture notes, recitations) and jeffe-notes prose: NC,
  link-only; exercises only as NC cards.
- ND-licensed system design repos (system-design-101,
  karanpratapsingh/system-design, algodeck), all-rights-reserved
  mobile-system-design, unlicensed question lists, EPL Maelstrom.

## 11. blocked_hosts

| host | result | wanted |
|---|---|---|
| www.nwerc.eu | CONNECT 403 | official NWERC problem packages and solution slides (older years) |
| bapc.eu, 2023.bapc.eu | CONNECT 403 | official BAPC packages |
| icpc.global | CONNECT 403 | World Finals problem archive and licence statements |
| open.umn.edu | TLS failure via proxy ("unable to get local issuer certificate") | Open Textbook Library DSA books with exercise keys |
| greenteapress.com | CONNECT 403 | *Think Data Structures* licence page and exercise text |
| runestone.academy | CONNECT 403 | pythonds interactive exercises |
| usaco.guide | CONNECT 403 | USACO Guide licence (problem modules) |
| cses.fi | CONNECT 403 | CSES licence check (expected link-only) |
| codeforces.com, atcoder.jp, www.hackerrank.com, spoj.com, onlinejudge.org | CONNECT 403 | licence confirmation only; link-only anyway |
| www.codewars.com | CONNECT 403 | kata licence terms |
| rosettacode.org | CONNECT 403 | task licence (GFDL expected; link-only either way) |

## 12. Gaps: topics with no open exercise found

- **System design drills for rate limiting, consistent hashing, CDN and
  DNS, sharding, unique ID generation at scale, standalone back-of-envelope
  estimation.** Nothing open poses these as exercises. Closest: sdp's 8
  worked designs (their "Calculate usage" sections), Exercism robot-name
  (unique random names, single process), Kleppmann's replication and
  consensus exercises. Under the no-AI-exercises rule these stay
  without exercises unless a source turns up.
- **Asymptotics and recurrences as code exercises.** Only NC keyed sets
  (6.006, 6.046J, 6.042J) and unkeyed Erickson/ODS items; by nature
  written.
- **Amortised analysis, NP-hardness, advanced DS (persistence, vEB,
  succinct).** Only NC keyed MIT sets plus unkeyed Erickson notes; no open
  code exercises with tests.
- **Sparse tables, LCA, centroid/HLD, suffix automata, game theory
  (Sprague-Grundy).** No open textbook-style code exercise found; only
  contest packages whose tags are unverified, and Kattis problems that
  are not obviously on these topics. cp-algorithms' practice links for
  them are link-only.
- **Probability.** Only Exercism baffling-birthdays, Project Euler 84/121/151
  (NC), 6.856J and 6.042J (NC).
