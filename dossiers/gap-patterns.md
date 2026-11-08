# Dossier: gap patterns (two pointers, sliding window, Kahn, prefix sums, intervals, generation, coin change, grid paths)

Finder run of 2026-11-08, targeted at the eight interview topics that
`concept-map/report.md` lists as having no source in the six inventories.
It builds on `dossiers/sweep-dsa.md` and `dossiers/sweep-exercises.md` and does
not repeat their rows unless a row needs an exact locator. No quality ranking:
the `treatment` column only says what a passage does with the technique.

- **E** (explains): states the idea, says why it works or what it costs, and shows it.
- **A** (applies): a worked solution to one problem that uses the technique, with its own reasoning.
- **M** (mentions): names it or uses it in passing.

None of the eight topics has a concept id in `concepts.json` yet. The
`concepts covered` column therefore uses topic names. Where an existing id
sits next to a topic it is named (`sliding-window-minimum`,
`topological-sort`, `interval-scheduling`, `max-subarray-prefix-min`,
`backtracking`, `counting`, `lattice-paths-obstacles`, `next-combination`).
`assumes` lists prerequisites the passage relies on. The map's position for
these topics is still undecided.

Lengths are approximate word counts of the section, markup and references stripped.

## Verdict per topic

| topic | verdict | open prose that explains (E) | open exercises with tests |
|---|---|---|---|
| Two pointers | **open prose found**, mostly attached to specific problems | wikipedia 3SUM#Quadratic algorithm, Merge algorithm#Merging two lists, Dutch national flag problem#The array case, Cycle detection#Floyd's tortoise and hare; cpa tortoise_and_hare; dsa-dummies Two Pointers (short general note, CC BY); doocs-leetcode 0167/0011/0015 | yes (keon three_sum/n_sum, TheAlgorithms two_pointer, tryalgo merge, kattis closestsums, exercism sublist) |
| Sliding window, fixed size | **open prose found** | wikipedia Double-ended queue#Monotonic queue, Moving average#Simple moving average, Rolling hash; cpa stack_queue_modification#Finding the minimum for all subarrays of fixed length; doocs 0239/0643/1456/0567 | yes (exercism series, largest-series-product; keon max_sliding_window; TheAlgorithms max_sum_sliding_window, sliding_window_maximum) |
| Sliding window, variable size | **open prose at problem level only.** No open general account of the expand/shrink invariant: the general write-ups are NC (cphb, USACO Guide), licence-unclear (OI Wiki, Tech Interview Handbook) or unlicensed copies (labuladong, Grokking mirrors) | doocs 0003, 0076, 0209 (Solution 2); icc longest_substr_k_distinct #Algorithm; dsa-dummies Sliding Window (fixed-window code, names the variable cases) | yes (icc longest_substr_k_distinct; keon longest_non_repeat; TheAlgorithms min_window_substring; tryalgo windows_k_distinct; icpc-rmc slidecount) |
| Kahn's algorithm | **open prose found** | wikipedia Topological sorting#Kahn's algorithm; opendsa Graph/GraphTopsort#Queue-based Solution (MIT); mcs2018 10.5.1 (CC BY-SA 3.0); aspnes-202 9.5.5.1 (CC BY-SA 4.0); icc graph_build_order #Algorithm; doocs 0207 | yes (icc graph_build_order; keon topological_sort_bfs; TheAlgorithms kahns_algorithm_topo; tryalgo topological_order; kattis pickupsticks, builddeps, brexit, succession, managingpackaging, easyascab; icpc gcpc2018/coolestskiroute) |
| Prefix sums, 1D | **open prose found** | wikipedia Prefix sum (lead, Scan); dsa-dummies Prefix Sum; doocs 0303, 0560, 0209 (Solution 1); cpa maximum_average_segment (applies) | yes (TheAlgorithms prefix_sum, range_sum_query; kattis subseqhard, frosting; icpc-mzuenni documentdimensions) |
| Prefix sums, 2D | **open prose found** | wikipedia Summed-area table#The algorithm; doocs 0304 | **none found** (Kattis prozor and cudoviste are "educational use only") |
| Difference arrays (1D/2D) | **open prose at problem level only** (doocs, CC BY-SA). Wikipedia only says that finite differences invert prefix sums. OI Wiki explains 1D/2D/tree differences but its licence needs a ruling | doocs 0370 (Solution 1), 1094, 1109, 0253 (Solution 1); cpa fenwick#2. Range Update and Point Query (applies the idea) | **none found** with tests |
| Interval scheduling | **open prose found** | jeffe 4.2; wikipedia Interval scheduling#Unweighted, Activity selection problem; anfp 17.2, 18.3; doocs 0435 | yes (kattis intervalscheduling, intervalcover, airconditioned; TheAlgorithms activity_selection, weighted_interval_scheduling) |
| Merging intervals | **open prose at problem level** | doocs 0056, 0057, 0986 | yes (keon merge_intervals + tests; TheAlgorithms merge_intervals; tryalgo intervals_union) |
| Meeting rooms / interval partitioning | **open prose at problem level**, plus one textbook exercise and mentions | doocs 0252, 0253; jeffe ch. 4 exercise "proper coloring of intervals"; wikipedia Interval graph#Applications and Interval scheduling#Variations (one sentence each) | yes (tryalgo max_interval_intersec = maximum overlap; kattis classrooms, bookingaroom; icpc gcpc2021/joinedsessions) |
| Sweep line over intervals | **open prose found** | cpa geometry/length-of-segments-union; doocs 0253; wikipedia Sweep line algorithm (M), Bentley–Ottmann#Overall strategy (segments) | yes (tryalgo max_interval_intersec, intervals_union) |
| Generating permutations, subsets, combinations | **open prose found** | wikipedia Permutation#Generation in lexicographic order, Heap's algorithm, Steinhaus–Johnson–Trotter, Combination#Enumerating k-combinations, Power set#Representing subsets as functions, Gray code; cpa generating_combinations, all-submasks; trekhleb power-set README; doocs 0046/0047/0077/0078/0090/0031/0039 | yes (icc permutations, power_set; keon permute, subsets, combination_sum; TheAlgorithms all_permutations, all_combinations, subset_generation; trekhleb jest tests; tryalgo next_permutation; exercism killer-sudoku-helper) |
| Coin change, minimum coins | **open prose found** | wikipedia Change-making problem (DP, Python code, greedy); anfp 17.3; doocs 0322; icc coin_change_min | yes (exercism change; icc coin_change_min; kattis exactchange2, canonical, exactchange; icpc gcpc2015/souvenirs) |
| Coin change, counting ways | **open prose found** | algo-explanation Dynamic Programming/Coin Change (MIT); icc coin_change_ways #Algorithm; doocs 0518 | yes (icc coin_change, coin_change_ways; keon coin_change; TheAlgorithms dp_count; kattis orders) |
| Grid paths (lattice paths, obstacles, min path sum) | **open prose found** | wikipedia Lattice path; dmoi3 sec_counting-binom#Lattice Paths; appcomb s_strings_bin-coeff; trekhleb unique-paths README #Algorithms; doocs 0062, 0063, 0064; icc grid_path #Algorithm | yes (kattis robotsonagrid; icc grid_path; keon count_paths, count_paths_dp; TheAlgorithms count_paths, minimum_path_sum, minimum_cost_path; trekhleb unique-paths jest; exercism pascals-triangle) |

The sweep's "no open prose" for two pointers and sliding window was too
strong. It missed:

- Wikipedia sections that teach concrete instances (3SUM, merge, Dutch flag, monotonic queue, moving average).
- dsa-dummies, which is already registered (CC BY 4.0).
- doocs/leetcode, whose solution write-ups are CC BY-SA 4.0.

What remains true is narrower. No open source gives a general, textbook-style
account of the variable-size window or of the two-pointer pattern as a
pattern. The only general treatments are NC, unclear or unlicensed (see
link-only).

## New sources registered (sources/registry.json, appended)

| id | licence | what was cached | why it matters here |
|---|---|---|---|
| `mcs2018` | CC BY-SA 3.0 (verified: page ii of the PDF) | `sources/_cache/mcs2018/` (PDF + text) | The 2018 MCS edition is BY-SA, not NC. The sweep could not check it because courses.csail.mit.edu was blocked. Covers topological sort by minimal elements (10.5.1), counting subsets and permutations (15.2–15.6), and making change by generating functions (Problem 16.7) and by induction (5.2.4) |
| `aspnes-202` | CC BY-SA 4.0 | `sources/_cache/aspnes-202/` | topological sort by repeated choice of a minimal element (9.5.5.1); counting |
| `aspnes-223` | CC BY-SA 4.0 | `sources/_cache/aspnes-223/` | Not on these topics. Registered because the sweep listed Yale as blocked and the CIU links to these notes (sorting, DP, tries) are now open |
| `doocs-leetcode` | CC BY-SA 4.0 for the solution prose; the problem descriptions are LeetCode's text and link-only | `sources/_cache/doocs-leetcode/` (38 README_EN.md) | the only open, problem-level prose for variable windows, difference arrays, merge intervals and meeting rooms |
| `tryalgo` | MIT (code and tests); the book is commercial | `sources/_cache/tryalgo/` | tests and reference code for windows_k_distinct, Kahn (`topological_order`), interval union, sweep-line maximum overlap, next permutation |
| `oiwiki` | **unclear**: CC BY-SA 4.0 *and* the SATA licence, conjunctive. Link-only until ruled | `sources/_cache/oiwiki/` (15 pages, Chinese) | the most complete open-looking prose on two pointers, 1D/2D/tree difference arrays, monotonic queue and Kahn. Needs a licence ruling and a translation |

Additions to existing caches (no new registry row):

- **`wikipedia`:** 36 articles added to `sources/_cache/wikipedia/` and `_meta.json`, with revids from `action=info`.
- **`kattis`:** 17 open problems added (`robotsonagrid`, `pickupsticks`, `builddeps`, `brexit`, `classrooms`, `dancerecital`, `subseqhard`, `closestsums`, `succession`, `frosting`, `kayaking`, `airconditioned`, `4thought`, `bestrelayteam`, `hothike`, `easyascab`, `exactchange`). Each has its page, `samples.zip` and an `index.json` entry.

Suggested evidence upgrade, not applied because this run only appends:

- **`anfp`:** the official GoalKicker PDF (https://goalkicker.com/AlgorithmsBook/AlgorithmsNotesForProfessionals.pdf) is byte-identical to the cached mirror (same SHA-256). Its page says "Text content is released under Creative Commons BY-SA". It is a better evidence URL than the third-party mirror.

---

## 1. Two pointers

| locator | source id | licence | nc | kind | concepts covered | length | assumes | treatment | what it is |
|---|---|---|---|---|---|---|---|---|---|
| wikipedia:3SUM#Quadratic algorithm | wikipedia | CC BY-SA 4.0 | no | prose | two pointers (opposite ends of a sorted array), 3SUM | ~411w | sorting, hash table | E | sort, fix a, move start/end inward by the sign of a+b+c; colour-coded trace on a small array; correctness argument |
| wikipedia:Merge_algorithm#Merging two lists | wikipedia | CC BY-SA 4.0 | no | prose | two pointers (one per sorted list), merge | ~284w | arrays, sorting | E | merging two sorted lists by advancing the pointer at the smaller head; pseudocode, linear cost |
| wikipedia:Dutch_national_flag_problem#The array case | wikipedia | CC BY-SA 4.0 | no | prose | three-pointer partition | ~401w | quicksort partition | E | Dijkstra's three-way partition with i/j/k pointers and pseudocode |
| wikipedia:Cycle_detection#Floyd's tortoise and hare | wikipedia | CC BY-SA 4.0 | no | prose | fast/slow pointers | ~745w | functions on finite sets | E | already in sweep-dsa; exact section locator |
| wikipedia:Algorithmic_technique#Two Pointers | wikipedia | CC BY-SA 4.0 | no | prose | two pointers (definition) | ~45w | — | M | two-sentence, unsourced definition in a list of techniques |
| wikipedia:Subset_sum_problem#Horowitz and Sahni | wikipedia | CC BY-SA 4.0 | no | prose | meet in the middle + merge-like scan | ~266w | subset sum, sorting | M | uses a two-list scan of sorted sums |
| dsa-dummies:Algorithms/Two Pointers/Python/Two Pointers.py | dsa-dummies | CC BY 4.0 | no | prose + code | two pointers (pair with target sum on a sorted array) | ~870w incl. code | sorting | E (short) | docstring essay: what it is, O(n)/O(1), when to use; commented pair-sum code; LeetCode links at the end (links only) |
| cpa:others/tortoise_and_hare | cpa | CC BY-SA 4.0 | no | prose | fast/slow pointers | 905w | linked lists | E | already in sweep-dsa |
| cpa:geometry/minkowski#Algorithm; cpa:data_structures/segment_tree (merge sort tree) | cpa | CC BY-SA 4.0 | no | prose | two pointers inside other algorithms | one paragraph each | convex polygons; segment trees | M | "create two pointers i and j …" as a step |
| algo-explanation:Search Algorithms/Floyd Cycle Detection Algorithm to Find Duplicate Number | algo-explanation | MIT | no | prose | fast/slow pointers on an array-as-function | ~510w | — | E | duplicate number via tortoise and hare |
| doocs-leetcode:0167#Solution 2: Two Pointers | doocs-leetcode | CC BY-SA 4.0 | no | prose | two pointers on a sorted array | part of 264w | binary search | A | pair sum in a sorted array; why moving one end is safe; complexity |
| doocs-leetcode:0011#Solution 1: Two Pointers | doocs-leetcode | CC BY-SA 4.0 | no | prose | two pointers (container with most water) | 278w | — | A | move the shorter side inward; reasoning and complexity |
| doocs-leetcode:0015#Solution 1: Sort + Two Pointers | doocs-leetcode | CC BY-SA 4.0 | no | prose | 3SUM with two pointers, skipping duplicates | 451w | sorting | A | fix i, two pointers on the rest, duplicate skipping |
| doocs-leetcode:0986#Solution 1 | doocs-leetcode | CC BY-SA 4.0 | no | prose | two pointers over two interval lists | 50w | intervals | A | terse |
| ods:linkedlists | ods | CC BY 2.5 CA | no | prose | — | — | — | M | the "two pointer" hit is pointer manipulation in linked lists, not the technique |
| oiwiki:misc/two-pointer | oiwiki | unclear (CC BY-SA 4.0 + SATA) | — | link-only (pending ruling) | two pointers: maintaining window info, subsequence matching, sorted order, cycle in a list | ~8.5k chars (Chinese) | sorting, linked lists | E | the only general chapter on the pattern found outside NC sources |

Exercises with tests:

| locator | source id | licence | nc | kind | concepts covered | tests | what it is |
|---|---|---|---|---|---|---|---|
| keon-algorithms:algorithms/array/three_sum.py::three_sum | keon-algorithms | MIT | no | code-exercise (tests) | 3SUM with two pointers | tests/test_array.py | implementation + unittest |
| keon-algorithms:algorithms/array/n_sum.py | keon-algorithms | MIT | no | code-exercise (tests) | k-sum by recursion down to two pointers | tests/test_array.py (4 calls) | |
| keon-algorithms:algorithms/array/two_sum.py, algorithms/searching/two_sum.py | keon-algorithms | MIT | no | code-exercise (tests) | pair sum (hash and sorted two-pointer variants) | tests/test_array.py, test_searching.py | |
| thealgorithms-python:maths/two_pointer.py::two_pointer | thealgorithms-python | MIT | no | test cases | pair sum on a sorted array | 8 doctests | |
| thealgorithms-python:maths/three_sum.py | thealgorithms-python | MIT | no | test cases | 3SUM | 2 doctests | |
| tryalgo:merge_ordered_lists::merge; tryalgo:closest_values::closest_values | tryalgo | MIT | no | test cases | merge with two indices; closest pair after sorting | tests/test_tryalgo.py | |
| icc:arrays_strings/two_sum | icc | Apache-2.0 | no | code-exercise | pair sum (solution uses a hash map) | test_two_sum.py | the two-pointer variant needs a sorted-input restatement |
| exercism:sublist | exercism | MIT | no | code-exercise | list containment (pointer scan) | 18 canonical cases | from sweep-exercises |
| exercism:pythagorean-triplet | exercism | MIT | no | code-exercise | triplets with a+b+c=N (two-pointer-able) | 7 | technique not required by the statement |
| kattis:closestsums | kattis | CC BY 3.0 | no | code-exercise | closest pair sum to each query (sorted pair sums / two pointers) | samples only | Waterloo 2001-10-20, Piotr Rudnicki (new in cache) |
| kattis:kayaking | kattis | CC BY-SA 3.0 | no | code-exercise | binary search on the answer + greedy pairing from both ends | samples only | NCPC 2017, difficulty 5.3 (new) |
| kattis:cd | kattis | CC BY 3.0 | no | code-exercise | intersection of two sorted lists | samples only | from sweep-exercises |
| kattis:pivot | kattis | CC BY-SA 3.0 | no | code-exercise | prefix max / suffix min scan | samples only | not two pointers strictly; prefix/suffix pass |

## 2. Sliding window (fixed size and variable size)

| locator | source id | licence | nc | kind | concepts covered | length | assumes | treatment | what it is |
|---|---|---|---|---|---|---|---|---|---|
| wikipedia:Double-ended_queue#Monotonic queue | wikipedia | CC BY-SA 4.0 | no | prose + pseudocode | fixed window min/max with a monotonic deque; min-queue | ~595w | deque | E | sliding-window minimum in O(n); compares naive O(nk) and O(n log n); pseudocode; the min-queue variant |
| cpa:data_structures/stack_queue_modification#Finding the minimum for all subarrays of fixed length | cpa | CC BY-SA 4.0 | no | prose | `sliding-window-minimum` | ~160w (+ queue methods ~800w above) | min-stack / min-queue methods | E | already cited in sweep-dsa; exact section |
| cpa:dynamic_programming/knapsack#Monotone Queue Optimization | cpa | CC BY-SA 4.0 | no | prose | window minimum inside a DP | ~150w | bounded knapsack | A | |
| wikipedia:Moving_average#Simple moving average | wikipedia | CC BY-SA 4.0 | no | prose | fixed window, O(1) update by adding the new item and dropping the old | ~570w | summation | E | derives SMA_next = SMA_prev + (p_new − p_old)/k; FIFO buffer |
| wikipedia:Rolling_hash#Polynomial rolling hash; wikipedia:Rabin–Karp_algorithm#Hash function used | wikipedia | CC BY-SA 4.0 | no | prose | fixed window with a rolling hash | ~184w; ~532w | modular arithmetic, hashing | E | window hash update in O(1) |
| wikipedia:Algorithmic_technique#Sliding Window | wikipedia | CC BY-SA 4.0 | no | prose | sliding window (definition) | ~21w | — | M | one sentence |
| wikipedia:Streaming_algorithm | wikipedia | CC BY-SA 4.0 | no | prose | "sliding window" streaming model | — | — | M | different sense of the term |
| dsa-dummies:Algorithms/Sliding Window/Python/Sliding Window.py | dsa-dummies | CC BY 4.0 | no | prose + code | fixed window (definition, cost, when to use) | ~640w incl. code | — | E (short, fixed only) | the code only lists windows by slicing; names longest-substring and max-sum-of-size-k as uses |
| doocs-leetcode:0003#Solution 1: Sliding Window | doocs-leetcode | CC BY-SA 4.0 | no | prose | variable window with a hash set, shrink on repeat | 314w | hash set | A | longest substring without repeats |
| doocs-leetcode:0076#Solution 1: Counting + Two Pointers | doocs-leetcode | CC BY-SA 4.0 | no | prose | variable window, minimum covering window | 453w | hash map counting | A | minimum window substring |
| doocs-leetcode:0209#Solution 2: Two Pointers | doocs-leetcode | CC BY-SA 4.0 | no | prose | variable window, positive numbers, shortest sum ≥ target | part of 495w | — | A | |
| doocs-leetcode:0239#Solution 1, #Solution 2: Monotonic Queue | doocs-leetcode | CC BY-SA 4.0 | no | prose | fixed window max: heap vs monotonic deque | 427w | heap, deque | A | two models |
| doocs-leetcode:0567, 0438 | doocs-leetcode | CC BY-SA 4.0 | no | prose | fixed window of counts (anagram windows) | 295w; 142w | counting | A | |
| doocs-leetcode:0643, 1456 | doocs-leetcode | CC BY-SA 4.0 | no | prose | fixed window running sum / count | 109w; 145w | — | A | |
| icc:recursion_dynamic/longest_substr_k_distinct (solution notebook, ## Algorithm) | icc | Apache-2.0 | no | prose + code-exercise | variable window with a char→index map | 133w | hash map | A | the recursion_dynamic copy; the online_judges copy is link-only per the registry ruling |
| oiwiki:ds/monotonic-queue; oiwiki:misc/two-pointer#维护区间信息 | oiwiki | unclear | — | link-only (pending ruling) | monotonic queue; variable window info | Chinese | deque | E | |

Exercises with tests:

| locator | source id | licence | nc | kind | concepts covered | tests | what it is |
|---|---|---|---|---|---|---|---|
| exercism:series | exercism | MIT | no | code-exercise | fixed window of substrings | 11 canonical | from sweep-exercises |
| exercism:largest-series-product | exercism | MIT | no | code-exercise | fixed window product | 18 canonical (15 current) | |
| icc:recursion_dynamic/longest_substr_k_distinct | icc | Apache-2.0 | no | code-exercise | variable window | test_longest_substr.py | |
| keon-algorithms:algorithms/queue/max_sliding_window.py | keon-algorithms | MIT | no | code-exercise (tests) | fixed window max, monotonic deque | tests/test_queue.py (5 asserts) | |
| keon-algorithms:algorithms/heap/sliding_window_max.py | keon-algorithms | MIT | no | code-exercise (tests) | same | tests/test_heap.py | |
| keon-algorithms:algorithms/array/longest_non_repeat.py | keon-algorithms | MIT | no | code-exercise (tests) | variable window, longest substring without repeats | tests/test_array.py (v1, v2) | docstring cites LeetCode (link only) |
| thealgorithms-python:maths/max_sum_sliding_window.py | thealgorithms-python | MIT | no | test cases | fixed window max sum | 8 doctests | |
| thealgorithms-python:other/sliding_window_maximum.py | thealgorithms-python | MIT | no | test cases | fixed window max | 5 doctests | |
| thealgorithms-python:greedy_methods/sliding_window.py | thealgorithms-python | MIT | no | test cases | window | 7 doctests | |
| thealgorithms-python:strings/min_window_substring.py | thealgorithms-python | MIT | no | test cases | variable window, minimum cover | 2 doctests | |
| tryalgo:windows_k_distinct::windows_k_distinct | tryalgo | MIT | no | test cases | all maximal windows with exactly k distinct values | tests/test_tryalgo.py | |
| icpc-rmc:2021/problems/slidecount | icpc-rmc | CC BY-SA | no | code-exercise (full data) | variable window with start/end indices and capacity C, named "sliding window algorithm" in the statement | data/ + submissions/ | RMC 2021 |
| kattis:hothike | kattis | CC BY-SA 3.0 | no | code-exercise | fixed window of days (min over windows of max of two days) | samples only | NCPC 2019 (new) |

## 3. Kahn's algorithm (BFS topological sort)

| locator | source id | licence | nc | kind | concepts covered | length | assumes | treatment | what it is |
|---|---|---|---|---|---|---|---|---|---|
| wikipedia:Topological_sorting#Kahn's algorithm | wikipedia | CC BY-SA 4.0 | no | prose + pseudocode | Kahn: set of sources, remove edges, cycle detection by leftover edges | ~244w | queues/sets, adjacency lists | E | the classic statement with pseudocode and O(V+E) |
| opendsa:Graph/GraphTopsort#Queue-based Solution | opendsa | MIT | no | prose + slideshow | in-degree counts, queue of zero-count vertices, cycle detection when the queue empties early | ~316w (+ topSortQCON JSAV slideshow) | graph traversal (OpenDSA `:requires: graph traversal`) | E | also #Depth-first solution in the same module |
| mcs2018:10.5.1 | mcs2018 | CC BY-SA 3.0 | no | prose + figure | topological sort by repeatedly picking a minimal element (getting-dressed DAG) | ~600w | DAGs, reachability | E (mathematical, no data structures) | proves every finite DAG has a topological sort; 10.5.2 parallel scheduling follows |
| aspnes-202:9.5.5.1 | aspnes-202 | CC BY-SA 4.0 | no | prose + figure | topological sort as selection of a minimal element; existence proof | ~500w | partial orders | E (mathematical, efficiency explicitly skipped) | |
| icc:graphs_trees/graph_build_order (solution notebook, ## Algorithm) | icc | Apache-2.0 | no | prose | process nodes with no incoming edges; detect a circular dependency | 96w | graphs | A | build order for projects and dependencies |
| doocs-leetcode:0207#Solution 1: Topological Sorting; 0210; 0269 | doocs-leetcode | CC BY-SA 4.0 | no | prose | Kahn with an in-degree array and a queue; alien dictionary (graph from words) | 188w; 60w; 74w | BFS | A | |
| tryalgo:topological_order::topological_order | tryalgo | MIT | no | code (docstring) | "Topological sorting by maintaining indegree" | 25 lines | | M | reference code |
| keon-algorithms:algorithms/graph/kahns_algorithm.py; topological_sort_bfs.py | keon-algorithms | MIT | no | code (docstring) | Kahn | 60; 65 lines | | M | |
| thealgorithms-python:graphs/kahns_algorithm_topo.py | thealgorithms-python | MIT | no | code (docstring) | Kahn | 71 lines | | M | |
| anfp:9.4 | anfp | CC BY-SA | no | prose | topological sort (DFS finishing times only) | ~667w | DFS | M (not Kahn) | |
| cpa:graph/topological-sort; jeffe:6.3; holden-acs:Directed Acyclic Graphs | cpa; jeffe; holden-acs | CC BY-SA 4.0; CC BY 4.0; CC BY-SA 4.0 | no | prose | DFS method only | 894w; ~810w; — | DFS | M (not Kahn) | listed so the judge knows they were checked |
| oiwiki:graph/topo#Kahn 算法 | oiwiki | unclear | — | link-only (pending ruling) | Kahn, complexity, lexicographically smallest order | Chinese | | E | |

Exercises with tests:

| locator | source id | licence | nc | kind | concepts covered | tests | what it is |
|---|---|---|---|---|---|---|---|
| icc:graphs_trees/graph_build_order | icc | Apache-2.0 | no | code-exercise | Kahn / cycle detection | test_build_order.py | |
| keon-algorithms:tests/test_graph.py::TestTopologicalSort | keon-algorithms | MIT | no | test cases | topological sort incl. cycle → ValueError | 6 asserts | |
| thealgorithms-python:graphs/kahns_algorithm_topo.py | thealgorithms-python | MIT | no | test cases | Kahn, returns None on a cycle | 8 doctests | |
| tryalgo:topological_order | tryalgo | MIT | no | test cases | Kahn and DFS orders | tests/test_tryalgo.py | |
| kattis:pickupsticks | kattis | CC BY-SA 3.0 | no | code-exercise | topological order or "IMPOSSIBLE" | samples only | Waterloo 2009 (new) |
| kattis:builddeps | kattis | CC BY-SA 3.0 | no | code-exercise | recompile order after a change (reachable subgraph + topological order) | samples only | NWERC 2015 practice (new) |
| kattis:brexit | kattis | CC BY-SA 3.0 | no | code-exercise | queue-driven peeling by a threshold (Kahn-like) | samples only | BAPC 2016 (new) |
| kattis:succession | kattis | CC BY-SA 3.0 | no | code-exercise | DP over a family DAG in topological order | samples only | NCPC 2010 (new) |
| kattis:managingpackaging | kattis | CC BY-SA 3.0 | no | code-exercise | lexicographically smallest topological order, cycle → "cannot be ordered" | samples only | in cache already |
| kattis:easyascab | kattis | CC BY-SA 3.0 | no | code-exercise | derive alphabet order from sorted words (alien dictionary) | samples only | difficulty 7.1 (new) |
| kattis:longestpathinadag | kattis | CC BY-SA 3.0 | no | code-exercise | DP in topological order | samples only | from sweep-exercises |
| icpc-kattis-export:gcpc2018/coolestskiroute | icpc-kattis-export | CC BY-SA | no | code-exercise (full data) | topological order + longest path DP (named in the solution slides) | data/, submissions/ | |

## 4. Prefix sums and difference arrays (1D and 2D)

| locator | source id | licence | nc | kind | concepts covered | length | assumes | treatment | what it is |
|---|---|---|---|---|---|---|---|---|---|
| wikipedia:Prefix_sum (lead) and #Scan higher order function | wikipedia | CC BY-SA 4.0 | no | prose | prefix sum definition, inclusive/exclusive scan; finite differences named as the inverse | ~261w + ~510w | — | E (definition) | already cited in sweep-dsa; the range-sum-query use is not spelled out |
| wikipedia:Prefix_sum#Data structures | wikipedia | CC BY-SA 4.0 | no | prose | Fenwick tree; summed-area table for 2D | ~112w | | M | |
| wikipedia:Summed-area_table (lead) and #The algorithm | wikipedia | CC BY-SA 4.0 | no | prose + figure | 2D prefix sums, one-pass build, four-corner rectangle sum | ~144w + ~190w | 2D arrays | E | figure `File:Summed area table.png` licence not yet checked |
| wikipedia:Fenwick_tree#Motivation | wikipedia | CC BY-SA 4.0 | no | prose | static prefix sums vs updates | ~115w | | M | |
| wikipedia:Finite_difference | wikipedia | CC BY-SA 4.0 | no | prose | difference operator (mathematics) | — | calculus | M | not the difference-array technique |
| dsa-dummies:Algorithms/Prefix Sum/Python/Prefix Sum.py | dsa-dummies | CC BY 4.0 | no | prose + code | 1D prefix sums for O(1) range queries | ~400w incl. code | | E (short) | |
| doocs-leetcode:0303#Solution 1: Prefix Sum | doocs-leetcode | CC BY-SA 4.0 | no | prose | 1D prefix array with a leading 0; range sum = s[r+1]−s[l] | 145w | | A/E | |
| doocs-leetcode:0304#Solution 1: Two-dimensional Prefix Sum | doocs-leetcode | CC BY-SA 4.0 | no | prose | 2D prefix build and inclusion–exclusion query | 235w | 2D arrays | A/E | |
| doocs-leetcode:0560#Solution 1: Hash Table + Prefix Sum | doocs-leetcode | CC BY-SA 4.0 | no | prose | count subarrays with sum k via prefix sums in a hash map | 163w | hash map | A | |
| doocs-leetcode:0209#Solution 1: Prefix Sum + Binary Search | doocs-leetcode | CC BY-SA 4.0 | no | prose | prefix sums of positives are monotone | part of 495w | binary search | A | |
| doocs-leetcode:0370#Solution 1: Difference Array | doocs-leetcode | CC BY-SA 4.0 | no | prose | 1D difference array: d[l]+=v, d[r+1]−=v, prefix-sum back | part of 250w | prefix sums | A/E | Solution 2 adds a Fenwick tree |
| doocs-leetcode:1094#Solution 1: Difference Array; 1109#Solution 1 | doocs-leetcode | CC BY-SA 4.0 | no | prose | difference arrays for range updates (car pooling, flight bookings) | 158w; 438w | | A | |
| doocs-leetcode:0253#Solution 1: Difference Array | doocs-leetcode | CC BY-SA 4.0 | no | prose | difference array over time = meeting-rooms sweep | 337w | | A | also listed under intervals |
| cpa:others/maximum_average_segment#Algorithm 2 | cpa | CC BY-SA 4.0 | no | prose | max subarray via prefix sums and running minimum (`max-subarray-prefix-min`) | ~450w | | A | |
| cpa:data_structures/fenwick#2. Range Update and Point Query | cpa | CC BY-SA 4.0 | no | prose | difference idea: add at l, subtract at r+1, point value = prefix sum | ~240w | Fenwick tree | A (difference arrays under a BIT) | |
| cpa:data_structures/segment_tree (intro), cpa:num_methods/binary_search | cpa | CC BY-SA 4.0 | no | prose | "precomputed prefix sums can compute sum queries in O(1)" | one sentence | | M | |
| algo-explanation:Sorting Algorithms/Counting Sort | algo-explanation | MIT | no | prose | prefix sums of counts → positions | — | | A | |
| icpc-mzuenni:documentdimensions (solution slides) | icpc-mzuenni | CC BY-SA | no | prose (slides) + exercise | prefix sum over word lengths | slide bullets | | M | |
| oiwiki:basic/prefix-sum | oiwiki | unclear | — | link-only (pending ruling) | 1D, 2D (inclusion–exclusion and per-dimension), subset-sum DP, tree prefix sums; 1D/2D/tree difference arrays; worked examples with .in/.ans files | ~17k chars (Chinese), 7 code + 7 example pairs | | E | the only complete treatment of difference arrays found |

Exercises with tests:

| locator | source id | licence | nc | kind | concepts covered | tests | what it is |
|---|---|---|---|---|---|---|---|
| thealgorithms-python:data_structures/arrays/prefix_sum.py::PrefixSum | thealgorithms-python | MIT | no | test cases | 1D prefix sums, range sum, contains-sum | 13 doctests | |
| thealgorithms-python:dynamic_programming/range_sum_query.py | thealgorithms-python | MIT | no | test cases | range sum queries | 2 doctests | |
| kattis:subseqhard | kattis | CC BY-SA 3.0 | no | code-exercise | count subarrays with sum 47 (prefix sums + map) | samples only | IPSC 2006 (new) |
| kattis:frosting | kattis | CC BY-SA 3.0 | no | code-exercise | sums grouped by index mod 3 (row/column aggregates) | samples only | SWERC 2017 (new) |
| kattis:longestprimesum | kattis | CC BY-SA 3.0 | no | code-exercise | primes + prefix sums | samples only | from sweep-exercises |
| kattis:fenwick, kattis:supercomputer | kattis | CC BY 3.0 | no | code-exercise | dynamic prefix sums | samples only | in cache already |
| icpc-mzuenni:documentdimensions | icpc-mzuenni | CC BY-SA | no | code-exercise (full data) | prefix sums inside a search | data/ | |
| 2D prefix sums, difference arrays | — | — | — | gap | — | — | no open exercise with tests found. Checked Exercism, icc, keon, TheAlgorithms, trekhleb, tryalgo, Kattis (prozor, cudoviste, srednji, dvoniz, akcija are "For educational use only") and the ICPC caches |

## 5. Interval problems

| locator | source id | licence | nc | kind | concepts covered | length | assumes | treatment | what it is |
|---|---|---|---|---|---|---|---|---|---|
| jeffe:4.2 | jeffe | CC BY 4.0 | no | prose + figures | `interval-scheduling` (earliest finish first), `exchange-argument` | ~1300w | greedy | E | already the map's source; exact locator |
| jeffe:4.ex "Let X be a set of n intervals … proper coloring" (≈ exercise 4; exercise numbers lost in the PDF text) | jeffe | CC BY 4.0 | no | exercise (unkeyed) | interval partitioning = minimum number of colours (rooms) | ~80w | greedy proof | — | the meeting-rooms-II problem in textbook form, with a figure |
| jeffe:4.ex "set of intervals stabbed by four points" (the exercise just before the colouring one) | jeffe | CC BY 4.0 | no | exercise (unkeyed) | interval stabbing | — | | — | |
| wikipedia:Interval_scheduling (lead), #Unweighted, #Weighted | wikipedia | CC BY-SA 4.0 | no | prose | interval scheduling greedy and failing greedies; weighted DP | ~505w, ~234w, ~409w | sorting, DP | E | |
| wikipedia:Interval_scheduling#Variations | wikipedia | CC BY-SA 4.0 | no | prose | "resource allocation … k is minimized" (interval partitioning) | one sentence | | M | |
| wikipedia:Activity_selection_problem#Algorithm, #Explanation, #Proof of optimality | wikipedia | CC BY-SA 4.0 | no | prose | earliest finish greedy with pseudocode and proof; weighted variant | ~297w + ~250w + ~216w | sorting | E | |
| wikipedia:Interval_graph#Applications; wikipedia:Graph_coloring#Greedy coloring | wikipedia | CC BY-SA 4.0 | no | prose | greedy colouring by left endpoint = minimum resources | one sentence each | graph colouring | M | |
| wikipedia:Sweep_line_algorithm | wikipedia | CC BY-SA 4.0 | no | prose | sweep line (general) | ~260w | | M | stub-like |
| wikipedia:Bentley–Ottmann_algorithm#Overall strategy | wikipedia | CC BY-SA 4.0 | no | prose | event queue + status structure sweep (segments) | ~342w | BSTs, priority queues | E (for segments, not intervals) | |
| wikipedia:Interval_tree#Naïve approach | wikipedia | CC BY-SA 4.0 | no | prose | overlap queries | short | | M | |
| anfp:17.2 Activity Selection Problem | anfp | CC BY-SA | no | prose + code | earliest finish greedy with a class timetable example | ~700w | sorting | E | carry the chapter's contributor credits |
| anfp:18.3 Interval Scheduling | anfp | CC BY-SA | no | prose | four candidate greedies with counterexamples; earliest finish optimal | ~700w | | E | images link-only |
| anfp:14.2 Weighted Job Scheduling Algorithm | anfp | CC BY-SA | no | prose + code | weighted interval scheduling DP | — | DP | E | |
| wikibooks:Algorithms/Greedy_Algorithms#Event Scheduling Problem | wikibooks | CC BY-SA 4.0 | no | prose | backtracking solution, shortest-first and fewest-conflicts counterexamples; stops before the correct greedy | ~500w | recursion | M (incomplete) | |
| openstax-introcs:3.4 | openstax-introcs | CC BY 4.0 | no | prose + figure | defines interval scheduling; shows shortest-first failing (Figure 3.18) | ~150w | | M | |
| cpa:geometry/length-of-segments-union | cpa | CC BY-SA 4.0 | no | prose + code | sweep over sorted endpoints with an open-segment counter (Klee) | 240w | sorting | E | the same sweep counts the maximum overlap |
| cpa:geometry/intersecting_segments | cpa | CC BY-SA 4.0 | no | prose | sweep line for segment intersection (`sweep-line-segment-intersection`) | 1447w | BSTs | E (contest tier) | |
| doocs-leetcode:0056 (Solutions 1–3) | doocs-leetcode | CC BY-SA 4.0 | no | prose | merge intervals: sort by start, extend or append | 405w | sorting | A/E | |
| doocs-leetcode:0057 | doocs-leetcode | CC BY-SA 4.0 | no | prose | insert interval (one pass) | 396w | | A | |
| doocs-leetcode:0252#Solution 1: Sorting | doocs-leetcode | CC BY-SA 4.0 | no | prose | can attend all meetings: sort, check neighbours | 128w | | A | |
| doocs-leetcode:0253 (Solutions 1–2) | doocs-leetcode | CC BY-SA 4.0 | no | prose | minimum rooms by a difference array / event sweep | 337w | prefix sums | A | |
| doocs-leetcode:0435#Solution 1: Sorting + Greedy | doocs-leetcode | CC BY-SA 4.0 | no | prose | remove fewest intervals = keep earliest-ending | 243w | | A | |
| appcomb:s_graphs_color (interval graphs); appcomb:s_posets_dilworth-intord | appcomb | CC BY-SA 4.0 | no | prose | interval graphs are perfect; interval orders | — | graph colouring, posets | M | |
| keon-algorithms:algorithms/array/merge_intervals.py; algorithms/sorting/meeting_rooms.py (docstrings) | keon-algorithms | MIT | no | code | merge; can-attend | 123; 35 lines | | M | meeting_rooms docstring restates LeetCode's statement (link only) |
| oiwiki:geometry/scanning | oiwiki | unclear | — | link-only (pending ruling) | sweep line: rectangle union area, 2D counting | Chinese | segment tree | E | |

Exercises with tests:

| locator | source id | licence | nc | kind | concepts covered | tests | what it is |
|---|---|---|---|---|---|---|---|
| kattis:intervalscheduling | kattis | CC BY-SA 3.0 | no | code-exercise | earliest finish greedy | samples only | from sweep-exercises |
| kattis:intervalcover | kattis | CC BY 3.0 | no | code-exercise | minimum interval cover | samples only | from sweep-exercises |
| kattis:classrooms | kattis | CC BY-SA 3.0 | no | code-exercise | maximum activities in k rooms (greedy with an ordered multiset) | samples only | Hong Kong 2016 (new) |
| kattis:airconditioned | kattis | CC BY-SA 3.0 | no | code-exercise | minimum rooms where each minion's temperature interval fits (stabbing) | samples only | Singapore 2015 (new) |
| kattis:bookingaroom; kattis:busyschedule | kattis | CC BY-SA 3.0 | no | code-exercise | free slot among bookings; sort times | samples only | from sweep-exercises |
| icpc-kattis-export:gcpc2021/joinedsessions | icpc-kattis-export | CC BY-SA | no | code-exercise (full data) | choose meetings that overlap all others | data/, submissions/ | |
| icpc-kattis-export:nwerc2023/datepicker | icpc-kattis-export | CC BY-SA | no | code-exercise (full data) | availability windows, greedy | data/, submissions/ | |
| keon-algorithms:algorithms/array/merge_intervals.py | keon-algorithms | MIT | no | code-exercise (tests) | merge intervals | tests/test_array.py | |
| thealgorithms-python:data_structures/arrays/merge_intervals.py | thealgorithms-python | MIT | no | test cases | merge intervals | 5 doctests | |
| thealgorithms-python:greedy_methods/activity_selection.py; other/activity_selection.py | thealgorithms-python | MIT | no | test cases | activity selection | 5 doctests | |
| thealgorithms-python:scheduling/weighted_interval_scheduling.py | thealgorithms-python | MIT | no | test cases | weighted interval scheduling DP | 27 doctests | |
| tryalgo:intervals_union::intervals_union | tryalgo | MIT | no | test cases | merge intervals (union) | tests/test_tryalgo.py (7 refs) | |
| tryalgo:max_interval_intersec::max_interval_intersec | tryalgo | MIT | no | test cases | sweep line: point covered by most intervals (= minimum meeting rooms) | tests/test_tryalgo.py (8 refs) | |
| tryalgo:interval_cover | tryalgo | MIT | no | test cases | interval cover | tests/test_interval_cover.py | |

## 6. Generating permutations, subsets and combinations

| locator | source id | licence | nc | kind | concepts covered | length | assumes | treatment | what it is |
|---|---|---|---|---|---|---|---|---|---|
| wikipedia:Permutation#Generation in lexicographic order | wikipedia | CC BY-SA 4.0 | no | prose + steps | next permutation (find k, find l, swap, reverse), handles repeats | ~408w | lexicographic order | E | |
| wikipedia:Permutation#Generation with minimal changes; #Generation of permutations in nested swap steps | wikipedia | CC BY-SA 4.0 | no | prose | SJT/Heap summaries; nested swaps | ~357w; ~531w | | E | |
| wikipedia:Heap's_algorithm#Details of the algorithm | wikipedia | CC BY-SA 4.0 | no | prose + pseudocode | Heap's algorithm, recursive and iterative | ~484w (+ proof, mis-implementations) | recursion | E | |
| wikipedia:Steinhaus–Johnson–Trotter_algorithm#Recursive structure; #Even's speedup | wikipedia | CC BY-SA 4.0 | no | prose | adjacent-transposition order | ~517w; ~335w | | E | |
| wikipedia:Combination#Enumerating k-combinations | wikipedia | CC BY-SA 4.0 | no | prose | lexicographic k-combinations by index increment; bit-twiddling | ~253w | | E | |
| wikipedia:Combinatorial_number_system#Ordering combinations | wikipedia | CC BY-SA 4.0 | no | prose | ranking/unranking combinations | ~357w | binomial coefficients | E | stretch tier |
| wikipedia:Power_set#Representing subsets as functions | wikipedia | CC BY-SA 4.0 | no | prose | subsets ↔ bit strings (enumeration by counting) | ~412w | binary numbers | E | |
| wikipedia:Gray_code#Constructing an n-bit Gray code | wikipedia | CC BY-SA 4.0 | no | prose | reflected Gray code: subsets with one change per step | ~727w | binary | E | |
| wikipedia:Backtracking; wikipedia:Lexicographic_order | wikipedia | CC BY-SA 4.0 | no | prose | backtracking pattern; order definition | — | | M | |
| cpa:combinatorics/generating_combinations | cpa | CC BY-SA 4.0 | no | prose + code | `next-combination`, `combinations-gray-order` | 960w | | E | |
| cpa:algebra/all-submasks | cpa | CC BY-SA 4.0 | no | prose + code | submask enumeration, O(3^n) | 597w | bit operations | E | |
| trekhleb-jsalgo:src/algorithms/sets/power-set/README.md#Algorithms | trekhleb-jsalgo | MIT | no | prose + table | power set: bitwise, backtracking, cascading | ~545w | | E | the registry row says the READMEs are not used. MIT prose is now allowed; this section reads as the author's own |
| doocs-leetcode:0046#Solution 1: DFS (Backtracking); 0047#Solution 1 | doocs-leetcode | CC BY-SA 4.0 | no | prose | permutations by backtracking with a used-array; duplicates by sorting and skipping | 175w; 350w | recursion | A/E | |
| doocs-leetcode:0078 (DFS; Binary Enumeration); 0090 | doocs-leetcode | CC BY-SA 4.0 | no | prose | subsets by include/exclude recursion and by bitmask; duplicates | 382w; 505w | | A/E | two models |
| doocs-leetcode:0077 (Backtracking, two ways) | doocs-leetcode | CC BY-SA 4.0 | no | prose | k-combinations, pick/skip vs loop-from-i | 418w | | A/E | |
| doocs-leetcode:0039 (two forms) | doocs-leetcode | CC BY-SA 4.0 | no | prose | combination sum with reuse, pruning | 592w | sorting | A | |
| doocs-leetcode:0031#Solution 1: Two traversals | doocs-leetcode | CC BY-SA 4.0 | no | prose | next permutation | 221w | | A | |
| icc:recursion_dynamic/permutations; icc:recursion_dynamic/power_set (solution notebooks, ## Algorithm) | icc | Apache-2.0 | no | prose | permutations of a string with duplicates; all subsets | short | recursion | A | |
| jeffe:2.3 Subset Sum; jeffe:2.4 The General Pattern | jeffe | CC BY 4.0 | no | prose | include/exclude recursion (the subset tree), backtracking pattern | ~1190w (2.3) | recursion | A (decision, not generation) | `subset-sum-backtracking`, `backtracking` |
| dmoi3:sec_counting-binom#Subsets, #Bit Strings; dmoi3:sec_counting-combperm | dmoi3 | CC BY-SA 4.0 | no | prose | counting subsets, bit strings, permutations, combinations | ~3.5k words (whole section) | | E (counting, not generation) | `counting` |
| appcomb:s_strings_permutations; appcomb:s_strings_combinations | appcomb | CC BY-SA 4.0 | no | prose | counting permutations/combinations | 1262w; 690w | | E (counting) | |
| mcs2018:15.2.2, 15.3.3, 15.5 | mcs2018 | CC BY-SA 3.0 | no | prose | subsets of an n-set, permutations, subset rule, bit sequences | — | | E (counting) | |
| oiwiki:search/backtracking; math/permutation; math/combinatorics/combination; math/numeral-sys/gray-code; basic/enumerate | oiwiki | unclear | — | link-only (pending ruling) | | Chinese | | E | |

Exercises with tests:

| locator | source id | licence | nc | kind | concepts covered | tests | what it is |
|---|---|---|---|---|---|---|---|
| icc:recursion_dynamic/permutations | icc | Apache-2.0 | no | code-exercise | permutations with duplicates | test_permutations.py | from sweep-exercises |
| icc:recursion_dynamic/power_set | icc | Apache-2.0 | no | code-exercise | all subsets | test_power_set.py | |
| keon-algorithms:algorithms/backtracking/permute.py, permute_unique.py, subsets.py, subsets_unique.py, combination_sum.py | keon-algorithms | MIT | no | code-exercise (tests) | permutations, subsets, combination sum | tests/test_backtracking.py | |
| keon-algorithms:algorithms/bit_manipulation/subsets.py | keon-algorithms | MIT | no | code-exercise (tests) | subsets by bitmask | tests/test_bit_manipulation.py | |
| thealgorithms-python:backtracking/all_permutations.py; all_combinations.py | thealgorithms-python | MIT | no | test cases | | 14; 24 doctests | |
| thealgorithms-python:dynamic_programming/subset_generation.py | thealgorithms-python | MIT | no | test cases | k-subsets | 12 doctests | |
| thealgorithms-python:bit_manipulation/gray_code_sequence.py; maths/kth_lexicographic_permutation.py | thealgorithms-python | MIT | no | test cases | Gray code; k-th permutation | 9; 2 doctests | |
| trekhleb-jsalgo:src/algorithms/sets/permutations/__test__, combinations/__test__, power-set/__test__ | trekhleb-jsalgo | MIT | no | test cases (jest) | with/without repetition; three power-set methods | 7 test files | |
| tryalgo:next_permutation | tryalgo | MIT | no | test cases | next permutation | tests/test_next_permutation.py | |
| exercism:killer-sudoku-helper | exercism | MIT | no | code-exercise | all k-combinations of 1..9 with a given sum, with exclusions | 13 canonical | |
| exercism:alphametics | exercism | MIT | no | code-exercise | search over digit permutations | 10 canonical | |
| kattis:dancerecital | kattis | CC BY-SA 3.0 | no | code-exercise | try all permutations of routines | samples only | Mid-Central 2015 (new) |
| kattis:bestrelayteam | kattis | CC BY-SA 3.0 | no | code-exercise | choose first-leg runner + best three (enumeration) | samples only | NCPC 2017 (new) |
| kattis:4thought | kattis | CC BY-SA 3.0 | no | code-exercise | enumerate 4^3 operator triples | samples only | NAQ 2013 (new) |
| kattis:namethatpermutation | kattis | (in cache, open badge) | no | code-exercise | k-th permutation | samples only | already cached |

## 7. Coin change (minimum coins and counting ways)

| locator | source id | licence | nc | kind | concepts covered | length | assumes | treatment | what it is |
|---|---|---|---|---|---|---|---|---|---|
| wikipedia:Change-making_problem (lead), #Simple dynamic programming, #Implementation, #Greedy method | wikipedia | CC BY-SA 4.0 | no | prose + Python code | minimum coins: DP table, greedy for canonical systems, when greedy fails | ~338w + ~271w + ~169w | DP | E (minimum only) | the Python code is CC BY-SA text |
| anfp:17.3 Change-making problem | anfp | CC BY-SA | no | prose + OCaml | greedy on canonical systems; exhaustive recursion with a memoisation note | ~480w | recursion | E | |
| anfp:18.2 Ticket automat | anfp | CC BY-SA | no | prose + C++ | greedy change machine | — | | A | |
| algo-explanation:Dynamic Programming/Coin Change | algo-explanation | MIT | no | prose + code | counting ways: dp[0]=1, coin-outer loop | 562w | DP | E (counting) | |
| icc:recursion_dynamic/coin_change_ways (solution notebook, ## Algorithm) | icc | Apache-2.0 | no | prose | counting ways, why the coin-outer loop avoids double counting | 147w | DP | E | |
| icc:recursion_dynamic/coin_change; coin_change_min (## Algorithm) | icc | Apache-2.0 | no | prose | counting ways (memo); minimum coins | short | | A | |
| doocs-leetcode:0322 (Complete Knapsack; Optimized) | doocs-leetcode | CC BY-SA 4.0 | no | prose | minimum coins as complete knapsack, 2D → 1D | 354w | knapsack | E/A | |
| doocs-leetcode:0518 (Complete Knapsack; Optimized) | doocs-leetcode | CC BY-SA 4.0 | no | prose | counting combinations; the role of loop order | 365w | knapsack | E/A | |
| cpa:dynamic_programming/knapsack#Complete Knapsack | cpa | CC BY-SA 4.0 | no | prose | unbounded knapsack recurrence (coin change is the special case) | ~430w | 0-1 knapsack | A (related) | |
| mcs2018:5.2.4 Making Change | mcs2018 | CC BY-SA 3.0 | no | prose | strong induction: 3- and 5-coins make every amount ≥ 8 | ~400w | induction | M (math) | |
| mcs2018:problem.16.7 | mcs2018 | CC BY-SA 3.0 | no | exercise (unkeyed) | counting ways to change n cents with generating functions | ~150w | generating functions | — | |
| appcomb:s_genfunction_distributions (exercise genfunction_distributions_rq-coins) | appcomb | CC BY-SA 4.0 | no | exercise | generating function for change in "Combinatoria" | short | generating functions | — | |
| jeffe:3.ex "Dream-Dollars" (first exercise of ch. 3) | jeffe | CC BY 4.0 | no | exercise (unkeyed) | greedy counterexample; recursive and DP minimum bills | ~250w | DP | — | |
| jeffe:4.ex "El Generalissimo" shopkeeper (≈ exercise 13 of ch. 4) | jeffe | CC BY 4.0 | no | exercise (unkeyed) | greedy fails; optimal for powers of b; DP | ~200w | greedy, DP | — | |
| wikipedia:Greedy_algorithm; wikipedia:Knapsack_problem | wikipedia | CC BY-SA 4.0 | no | prose | coin example; unbounded knapsack | — | | M | cached already |

Exercises with tests:

| locator | source id | licence | nc | kind | concepts covered | tests | what it is |
|---|---|---|---|---|---|---|---|
| exercism:change | exercism | MIT | no | code-exercise | fewest coins, return the coins; impossible and negative cases | 13 canonical | |
| icc:recursion_dynamic/coin_change, coin_change_min, coin_change_ways | icc | Apache-2.0 | no | code-exercise | counting ways; minimum | 3 unittest files | |
| keon-algorithms:algorithms/dynamic_programming/coin_change.py::count | keon-algorithms | MIT | no | code-exercise (tests) | counting ways | tests/test_dynamic_programming.py::TestCoinChange | docstring cites LeetCode (link only) |
| thealgorithms-python:dynamic_programming/minimum_coin_change.py::dp_count | thealgorithms-python | MIT | no | test cases | counting ways (despite the file name) | 6 doctests | the docstring paraphrases HackerRank; use the doctests only |
| thealgorithms-python:greedy_methods/minimum_coin_change.py | thealgorithms-python | MIT | no | test cases | greedy change | 5 doctests | |
| kattis:exactchange2 | kattis | CC BY-SA 3.0 | no | code-exercise | paying at least the price with fewest coins (subset-sum DP) | samples only | from sweep-exercises |
| kattis:canonical | kattis | CC BY-SA 3.0 | no | code-exercise | is greedy optimal for this coin system? | samples only | from sweep-exercises |
| kattis:orders | kattis | CC BY-SA 3.0 | no | code-exercise | unbounded knapsack: impossible / ambiguous / unique order | samples only | from sweep-exercises |
| kattis:exactchange | kattis | CC BY-SA 3.0 | no | code-exercise | greedy change in Umbertoland (1, 5, 15, 30, 150) | samples only | Mines HS 2024 (new) |
| icpc-kattis-export:gcpc2015/souvenirs | icpc-kattis-export | CC BY-SA | no | code-exercise (full data) | two-coin system change | data/, submissions/ | |

## 8. Grid paths (lattice paths, obstacles, minimum path sum)

| locator | source id | licence | nc | kind | concepts covered | length | assumes | treatment | what it is |
|---|---|---|---|---|---|---|---|---|---|
| wikipedia:Lattice_path#North-East lattice paths, #Counting lattice paths, #Combinations and NE lattice paths | wikipedia | CC BY-SA 4.0 | no | prose + figure | NE paths counted by C(n+k, n); link to Pascal's triangle | ~228w + ~198w + ~428w | binomial coefficients | E | figure `File:Walking on Pascal's Triangle SVG.svg` (licence not checked) |
| wikipedia:Delannoy_number; wikipedia:Catalan_number#Applications in combinatorics; wikipedia:Pascal's_triangle#Combinations | wikipedia | CC BY-SA 4.0 | no | prose | paths with diagonal steps; Dyck paths; Pascal | — | | M | |
| dmoi3:sec_counting-binom#Lattice Paths | dmoi3 | CC BY-SA 4.0 | no | prose + figures | lattice paths ↔ bit strings ↔ subsets; C(m+n, n) | ~600w (section) | | E | |
| appcomb:s_strings_bin-coeff (lattice path paragraphs, fig_latticepath) | appcomb | CC BY-SA 4.0 | no | prose + figure | lattice paths counted by binomial coefficients | part of 1643w | | E | |
| appcomb:s_strings_lattice-paths-binomial-thm_activity | appcomb | CC BY-SA 4.0 | no | exercise (activity) | lattice paths and the binomial theorem | 952w | | — | |
| cpa:dynamic_programming/intro-to-dp#Classic Dynamic Programming Problems | cpa | CC BY-SA 4.0 | no | prose (table row) | "Counting Paths in a 2D Array" | one row | | M | the alias the concept map found |
| cpa:combinatorics/catalan-numbers | cpa | CC BY-SA 4.0 | no | prose | monotone paths not crossing the diagonal | 873w | | M | |
| trekhleb-jsalgo:src/algorithms/uncategorized/unique-paths/README.md#Algorithms | trekhleb-jsalgo | MIT | no | prose | decision-tree backtracking, DP table, Pascal's triangle shortcut | ~350w (Algorithms part) | DP | E | the opening problem statement and robot_maze.png are LeetCode's: link-only |
| doocs-leetcode:0062 (three DP solutions) | doocs-leetcode | CC BY-SA 4.0 | no | prose | unique paths, prefilled borders, rolling array | 451w | DP | E/A | |
| doocs-leetcode:0063 (Memoization; DP) | doocs-leetcode | CC BY-SA 4.0 | no | prose | unique paths with obstacles (`lattice-paths-obstacles`) | 444w | DP | E/A | |
| doocs-leetcode:0064#Solution 1 | doocs-leetcode | CC BY-SA 4.0 | no | prose | minimum path sum DP | 227w | DP | E/A | |
| icc:recursion_dynamic/grid_path (solution notebook, ## Algorithm) | icc | Apache-2.0 | no | prose | robot from top-left to bottom-right avoiding off-limits cells; memoised recursion | 217w | recursion, memoisation | A | |
| thealgorithms-python:matrix/count_paths.py (module docstring) | thealgorithms-python | MIT | no | code (docstring) | count paths with blocked cells by DFS backtracking | ~150w | | M | |
| jeffe:3.ex "Vankin's Mile" | jeffe | CC BY 4.0 | no | exercise (unkeyed) | right/down moves on a grid, maximum score DP | ~200w | DP | — | the min-path-sum shape |

Exercises with tests:

| locator | source id | licence | nc | kind | concepts covered | tests | what it is |
|---|---|---|---|---|---|---|---|
| kattis:robotsonagrid | kattis | CC BY-SA 3.0 | no | code-exercise | count right/down paths around obstacles mod 2^31−1; fall back to BFS if none | samples only | NCPC 2011 (new) |
| icc:recursion_dynamic/grid_path | icc | Apache-2.0 | no | code-exercise | path with off-limits cells | test_grid_path.py | from sweep-exercises |
| keon-algorithms:algorithms/dynamic_programming/count_paths_dp.py; algorithms/matrix/count_paths.py | keon-algorithms | MIT | no | code-exercise (tests) | unique paths (recursive, memo, bottom-up) | tests/test_community_algorithms.py | |
| thealgorithms-python:matrix/count_paths.py | thealgorithms-python | MIT | no | test cases | paths with blocked cells | 4 doctests | |
| thealgorithms-python:graphs/minimum_path_sum.py; dynamic_programming/minimum_cost_path.py | thealgorithms-python | MIT | no | test cases | minimum path sum right/down | 5; 2 doctests | |
| trekhleb-jsalgo:src/algorithms/uncategorized/unique-paths/__test__ | trekhleb-jsalgo | MIT | no | test cases (jest) | backtracking, DP, Pascal versions | 3 test files | |
| exercism:pascals-triangle | exercism | MIT | no | code-exercise | rows of Pascal's triangle | 8 canonical | |

---

## link-only (with reasons)

| item | licence / status | reason | what it would give |
|---|---|---|---|
| OI Wiki (github.com/OI-wiki/OI-wiki), cached as `oiwiki` | CC BY-SA 4.0 **plus** SATA 2.0 ("及附加的 The Star And Thank Author License") | Conjunctive extra licence: an MIT-style notice condition plus "you should star/+1/like the project(s) … and then thank the author(s)". Needs a ruling. Also Chinese, so it needs translation | the fullest prose on two pointers, 1D/2D/tree difference arrays, monotonic queue, Kahn, sweep line |
| Competitive Programmer's Handbook (pllk/cphb) | CC BY-NC-SA 4.0 | NC prose | ch. 8 two pointers and sliding window minimum; ch. 9 prefix sums, 2D prefix sums |
| USACO Guide (cpinitiative/usaco-guide) | CC BY-NC-SA 4.0 (LICENSE checked this run) | NC prose | two pointers, sliding window, prefix sums 1D/2D, difference arrays, topological sort modules |
| CSES problem set (cses.fi/problemset) | no licence stated on the pages | all rights reserved by default | Sliding Window Sum, Static Range Sum Queries, Forest Queries (2D), Course Schedule (Kahn), Coin Combinations I/II, Minimizing Coins, Grid Paths, Movie Festival, Restaurant Customers, Room Allocation, Creating Strings, Sum of Two Values, Playlist, Subarray Sums |
| Problem Solving with Algorithms and Data Structures (RunestoneInteractive/pythonds) | CC BY-NC-SA 4.0 (LICENSE.txt) | NC prose; runestone.academy itself returned 403 | DP making change (min coins), topological sort |
| Tech Interview Handbook (yangshun/tech-interview-handbook, apps/website/contents/algorithms/) | MIT LICENSE, but README: "I am providing code in the repository to you under an open source license" | unclear whether the licence covers the prose (ruling kept from sweep-dsa) | array.md#Sliding window and #Two pointers (short, mostly LeetCode links), interval.md (tips), graph.md#Topological sorting |
| greyireland/algorithm-pattern (en/advanced_algorithm/slide_window.md) | MIT | the sliding-window template and comments match labuladong's framework (fucking-algorithm, no licence), so the MIT grant on that text is doubtful | sliding-window template + 4 LeetCode solutions |
| labuladong/fucking-algorithm | no LICENSE file | all rights reserved | the sliding-window and two-pointer "frameworks" |
| youngyangyang04/leetcode-master | no LICENSE file | all rights reserved | Chinese pattern guides |
| azl397985856/leetcode (thinkings/slide-window.en.md, prefix.en.md, backtrack.en.md) | CC BY-NC-ND 4.0 | ND and NC | sliding window, prefix sums, backtracking |
| ByteByteGoHq/coding-interview-patterns | CC BY-NC-ND 4.0 | ND and NC; code only | |
| seanprashad/leetcode-patterns | CC BY-NC 4.0 | NC; a list of LeetCode links | |
| dipjul/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions | MIT on a repo that reproduces Educative's "Grokking the Coding Interview" lessons (same pattern and problem titles) | the uploader cannot license Educative's text: suspected unauthorised copy | sliding window, two pointers, merge intervals, subsets lessons |
| Chanda-Abdul/Several-Coding-Patterns-… | no LICENSE; same Grokking material | all rights reserved / suspected copy | |
| liuyubobobo/Play-Leetcode | no LICENSE | all rights reserved | |
| kdn251/interviews | MIT | lists links only; no prose on these topics | |
| doocs-leetcode problem descriptions (`<!-- description:start -->` blocks) | LeetCode terms | LeetCode's copyrighted statements | only the solution blocks are usable |
| trekhleb-jsalgo sets/permutations/README.md, sets/combinations/README.md | MIT on the repo | text and formula images are copied from Math Is Fun ("My fruit salad is a combination of apples, grapes and bananas"), cited in References | |
| trekhleb-jsalgo unique-paths and combination-sum README problem statements | MIT on the repo | statement text and robot_maze.png are LeetCode's | the Algorithms sections are listed above as usable |
| trekhleb-jsalgo graph/topological-sorting/README.md | MIT on the repo | opening text is Wikipedia's (CC BY-SA), so use Wikipedia directly | |
| icc online_judges/merge_ranges, busiest_period, move_zeroes, assign_cookies, mult_other_numbers, longest_substr_k_distinct | Apache-2.0 on the repo | registry ruling: online_judges restates LeetCode/HackerRank/Interview Cake problems (assign_cookies quotes LeetCode verbatim) | merge intervals, sweep over enter/exit events, two pointers, prefix products, variable window |
| Kattis perket, geppetto, veci, srednji, prozor, sumsets, cudoviste, nikola, conservation, bus, dvoniz, akcija, ljutnja, mravi, zbrka, prsteni, tajna, kemija, kornislav, lektira, natrij | "For educational use only" badge | not an open licence | subsets (perket, geppetto), next permutation (veci), prefix counts (srednji), 2D windows (prozor, cudoviste), prefix sums (dvoniz) |
| Kattis windows (Window Manager) | no licence badge | | |
| Laaksonen, Guide to Competitive Programming; Sannemo, Principles of Algorithmic Problem Solving; tryalgo book; Grokking (Educative); Alex Xu / ByteByteGo "Coding Interview Patterns" (CIU's main recommendation) | commercial / all rights reserved | | |
| CIU links for these topics: Aduni "Graph Algorithms I – Topological Sorting …" (youtube i_AQT_XfvD8); "Math Skills: … Permutation, and Combination" (youtube 8RRo6Ti9d0U); LeetCode backtracking blueprint posts (Java, Python) | YouTube licence flag not readable (redirected to a bot check); LeetCode terms | link-only side-panel candidates. Lengths could not be read (YouTube served the bot check) | Aduni lecture: topological sort walk-through in a full graph-algorithms lecture; Math Skills: short counting refresher; LeetCode posts: one template for subsets/permutations/combination sum |
| MIT OCW 6.006 / 6.046 problem sets, Project Euler (8, 15, 24, 31, 79, 81) | CC BY-NC-SA 4.0 | allowed only as NC exercise cards (already in sweep-exercises) | fixed windows (PE 8), lattice paths (PE 15), lexicographic permutations (PE 24), coin sums (PE 31), topological passcode (PE 79), min path sum (PE 81) |

## blocked_hosts

| host | what happened | what was wanted |
|---|---|---|
| stackoverflow.com | CONNECT tunnel refused (403) | Stack Overflow Documentation archive (the source of ANFP; there is no separate two-pointer topic there) |
| archive.org | CONNECT tunnel refused | archived pages of dead CIU links |
| runestone.academy | HTTP 403 from the site (bot check). Not worked around | pythonds DP making-change and topological sort pages. The GitHub source (RunestoneInteractive/pythonds) was checked instead: CC BY-NC-SA 4.0, so link-only anyway |
| www.youtube.com | redirected to google.com/sorry (bot check). Not worked around | the Creative Commons flag and length of the CIU-linked videos |
| www.cs.cornell.edu | TLS verification failure at the proxy ("unable to get local issuer certificate") | Cornell CS 2110/3110 notes (nothing specific identified) |
| en.wikipedia.org `/w/api.php`, `/w/rest.php` | "You are making too many requests to the API" (Wikimedia rate limit on the shared egress) | full-text search for "two pointers", "sliding window", "difference array", "interval partitioning". Raw wikitext (`index.php?action=raw`) and revids (`action=info`) still worked; the 36 articles above came from known titles |
| en.wikibooks.org `/w/api.php` | same rate limit after two searches | Wikibooks search. The two searches that ran found nothing relevant for "sliding window" or "two pointers" |
| eng.libretexts.org search | the search page is JS-rendered; `@api/deki/site/query` needs a developer token (403) | site-wide LibreTexts search. Only the cached books (lt-justo, lt-njoroge, openstax-introcs) were grepped: no hits |
| api.github.com (gh api) | "GitHub access to this repository is not enabled for this session" | repository trees. Public `git clone --filter=blob:none` worked instead |
| www.geeksforgeeks.org, codeberg.org, open.umn.edu | CONNECT tunnel refused (403) | GfG is all rights reserved anyway; Open Textbook Library search |

Reachable now and used: courses.csail.mit.edu (MCS 2018), www.cs.yale.edu
(Aspnes 202/223), goalkicker.com (ANFP licence confirmed against the
mirror), openstax.org, cses.fi (licence check only), usaco.guide (licence
via GitHub), open.kattis.com.

## What was tried, by topic, beyond sweep-dsa.md

- **Registered corpus, grepped:** cpa, jeffe, jeffe-notes, ods, opendsa, opendsa-exercises, algo-explanation, wikibooks, wikipedia, holden-acs, csci30, appcomb, brisk, dmoi3, addiscoder, openstax-introcs, itsy-bitsy, dsa-dummies, lt-njoroge, lt-justo, anfp, icc, keon, TheAlgorithms, trekhleb, exercism, kattis, and the ICPC caches. ANFP has no two-pointer or sliding-window chapter (checked its full table of contents). Those chapters are not in the 2018 Algorithms Notes.
- **cp-algorithms upstream main** (0b3d4d72): no articles beyond the pinned cache.
- **OpenDSA full tree** (blobless clone): no modules beyond GraphTopsort on these topics.
- **Wikipedia:** 36 articles by known title, listed in `_meta.json`.
- **GitHub:** licences checked for 16 pattern repos (table above), plus doocs, tryalgo, OI Wiki.
- **Kattis:** 60 candidate slugs checked for licence badges; 17 new open problems cached.
- **ICPC packages:** statements and solution slides grepped for technique keywords.
