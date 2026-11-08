# Dossier: broad sweep, Parts I–III (DSA prose, figures, videos)

Finder run of 2026-11-08. Scope: METHOD.md §4.2 Parts I–III (complexity, arrays
and dynamic arrays, linked lists, stacks and queues, hash tables, binary search,
bit manipulation, trees and traversals, BSTs, heaps, balanced trees, tries, graph
representations, BFS/DFS, topological sort, shortest paths, MST, recursion and
backtracking, divide and conquer and sorting, greedy, DP, two pointers and sliding
window). Exercises and system design are covered by the other finders'
dossiers (`sweep-exercises.md`, `sweep-system-design.md`) and are not repeated
here. Registered corpus (cpa, ciu, jeffe, jeffe-notes, ods) is assumed known and
is not listed again, except where it is the only open prose for a concept.

The finder makes no quality judgements. "What it is" columns describe, they do
not rank.

## New sources registered (rows appended to `sources/registry.json`)

| id | licence | evidence (where read) | what it is |
|---|---|---|---|
| `wikipedia` | CC BY-SA 4.0 (text); figures per file | en.wikipedia.org/wiki/Wikipedia:Copyrights: "Most of Wikipedia's text and many of its images are co-licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA)" | 81 articles, wikitext at pinned revids (`_meta.json`) |
| `wikibooks` | CC BY-SA 4.0 (dual GFDL) | en.wikibooks.org/wiki/Wikibooks:Copyrights: "Permission is granted to copy, distribute and/or modify Wikibooks' text under the terms of the Creative Commons Attribution-ShareAlike 4.0 International License" | *Data Structures* (11 chapters) and *Algorithms* (10 chapters) Wikibooks |
| `opendsa` | **MIT, needs a ruling** | header of every topic `.rst`: "Copyright (c) 2012-2020 by the OpenDSA Project Contributors, and distributed under an MIT open source license." (803 of 861 en files; all files in the 15 topic dirs) | Shaffer et al.'s OpenDSA eTextbook modules (~135 modules over 150 words) plus 31 static figures; the JSAV slideshows are MIT code in `AV/` (not cached) |
| `algo-explanation` | **MIT, needs a ruling** | LICENSE.txt: "The MIT License  Copyright (c) 2020-2024 The Algorithms and contributors" | 47 short English explanations (sorting, searching, DP, lists, trie) |
| `lt-njoroge` | CC BY-SA (version not stated) | each page footer: "is shared under a CC BY-SA license and was authored, remixed, and/or curated by Harrison Njoroge (African Virtual University)"; every content page tagged `license:ccbysa` | AVU module: algorithms, recursion, basic data structures, searching and sorting |
| `lt-justo` | mixed per page | units 2 and 3: "shared under a CC BY-SA 3.0 license"; units 1 and 4: "shared under a not declared license" | AVU module: only units 2 (search, BST, heaps) and 3 (sorting) pass; 1 and 4 are unclear |
| `openstax-introcs` | CC BY 4.0 (figures per caption) | LibreTexts chapter page: "is shared under a CC BY 4.0 license"; captions read "attribution: Copyright Rice University, OpenStax, under CC BY 4.0 license" | OpenStax *Introduction to Computer Science* ch. 3 (Data Structures and Algorithms), ~21k words, 32 figures |
| `lt-csbu` | CC BY-SA 3.0 | "is shared under a CC BY-SA 3.0 license" | Wienand, *Computer Science from the Bottom Up* ch. 2 (binary, bitwise operations, two's complement), ~8.8k words |
| `csci30` | CC BY-SA 4.0 | copyright.tex: "This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License" | Guadalupe (Ateneo de Manila) DSA lecture notes, LaTeX; complete chapters: correctness, efficiency, recursion, sorting |
| `holden-acs` | CC BY-SA 4.0 | README.md: "This is a Creative Commons Attribution Sharealike 4.0 endeavor." plus LICENSE (CC BY-SA 4.0 legal code) | Holden, *Applied Computer Science* lecture notes (LaTeX + Graphviz): MST, Dijkstra, binary, recursion, tries, DAGs, DP, hashing |
| `itsy-bitsy` | CC BY 4.0 | LICENSE: "Creative Commons Attribution 4.0 International" | Kyle, *Itsy Bitsy Data Structures*: one annotated JS file |
| `dsa-dummies` | CC BY 4.0 | LICENCE: "Creative Commons Attribution 4.0 International" | short Big O README plus Python code |
| `addiscoder` | CC BY-SA 4.0 | LICENSE: "Attribution-ShareAlike 4.0 International" | AddisCoder course notes; only §16 Recursion is in scope |
| `appcomb` | CC BY-SA 4.0 | LICENSE.md: "Attribution-ShareAlike 4.0 International" | Keller & Trotter, *Applied Combinatorics* (PreTeXt): graph basics, MST (Kruskal, Prim), Dijkstra |
| `brisk` | CC BY-SA 4.0 | copyright.tex: "Creative Commons Attribution-ShareAlike 4.0 International License" | Davies, *A Cool Brisk Walk Through Discrete Mathematics* (LaTeX): graphs, BFS/DFS, Dijkstra, Prim, trees, BSTs |
| `dmoi3` | CC BY-SA 4.0 (3rd ed. only) | LICENSE at tag `3rd-ed`: "This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License." (4th ed. is CC BY-NC-SA 4.0) | Levin, *Discrete Mathematics: An Open Introduction* 3rd ed.: trees, spanning trees, recurrences |
| `anfp` | CC BY-SA (text only) | PDF p. 1: "Text content is released under Creative Commons BY-SA, see credits at the end of this book ... Images may be copyright of their respective owners unless otherwise specified" | GoalKicker *Algorithms Notes for Professionals* (from Stack Overflow Documentation), 257 pp; third-party GitHub mirror |
| `arxiv-2211.11009` | CC BY 4.0 | arxiv.org/abs/2211.11009 licence link: http://creativecommons.org/licenses/by/4.0/ | Tarjan & Zwick, *Optimal resizable arrays* (stretch tier for dynamic arrays) |

Notes on the two MIT rows: METHOD.md §0 and the finder's gate list PD, CC0,
CC BY and CC BY-SA for prose, and MIT/BSD/Apache for code only. OpenDSA and
TheAlgorithms state MIT for the prose itself. MIT is more permissive than
CC BY, but MIT text inside a BY-SA book has to carry the MIT notice. That is
a policy call, so both rows are registered with "PENDING A RULING" in
`use`. Until someone rules, treat them as link-only for prose. The exercises
finder registered `opendsa-exercises` from the same commit, for the exercises.

Cached but **not** registered: `sources/_cache/mcs/` (MIT OCW 6.042J 2015
*Mathematics for Computer Science* PDF. Page ii says "available under the
terms of the Creative Commons Attribution-NonCommercial-ShareAlike 3.0
license", so it is link-only. A NOTE.txt there says so).

## Licence check per page: what failed inside passing sources

- `lt-justo` 1.1–1.4, 4.1–4.4 (recursion, backtracking, DP, hashing, graphs,
  graph algorithms): the footer says "shared under a not declared license".
  The AVU "Copyright Notice" page in the same book says "published under the
  conditions of the Creative Commons ... Attribution http://creativecommons.org/licenses/by/2.5/".
  The evidence conflicts, so these are `unclear`, link-only.
- `openstax-introcs`: figure licences are per caption. Most say "Copyright Rice
  University, OpenStax, under CC BY 4.0 license". Check each caption before use
  (Fig. 3.1 also cites OpenStreetMap data under ODbL; Fig. 3.15 cites
  GeeksforGeeks as a *data source*).
- `lt-njoroge`, `lt-justo`: inline images in the AVU modules have no
  per-image credit; treat as unclear.
- `csci30`: the raster figures `Chocolate-Fountains.png`, `fountain_fail.png`
  and `insertionsort.jpg` have no stated source: unclear. The TikZ figures are
  part of the BY-SA text.
- `anfp`: images excluded by the book's own notice; prose must carry the
  per-chapter contributor credits printed at the end of the PDF.
- `algo-explanation`: images are hot-linked from GitHub user uploads,
  geeksforgeeks.org, tutorialhorizon.com and upload.wikimedia.org: link-only
  unless traced to a passing file.
- `wikipedia`/`wikibooks` figures: see "Figures" below. Each file was checked
  through the Commons `extmetadata` licence field, not assumed from the article
  licence.

## Candidates (one row per locator)

Lengths: Wikipedia/Wikibooks word counts are approximate (wikitext with templates and refs stripped). OpenDSA counts exclude RST directives. `assumes` lists prerequisites that METHOD.md §4.2 puts later. It is filled in only where the text clearly relies on them (mostly recursion, which is Part III, used by tree code in Part II).

| locator | source id | licence | nc | kind | concepts covered | length | assumes | what it is |
|---|---|---|---|---|---|---|---|---|
| wikipedia:2–3_tree | wikipedia | CC BY-SA 4.0 | no | prose | balanced trees (2-3) | ~1005 words (wikitext, rev 1383622351) |  | Wikipedia article |
| wikipedia:AVL_tree | wikipedia | CC BY-SA 4.0 | no | prose | balanced trees (AVL) | ~4744 words (wikitext, rev 1384121402) |  | Wikipedia article |
| wikipedia:Adjacency_list | wikipedia | CC BY-SA 4.0 | no | prose | graph representations | ~1155 words (wikitext, rev 1366823976) |  | Wikipedia article |
| wikipedia:Adjacency_matrix | wikipedia | CC BY-SA 4.0 | no | prose | graph representations | ~2128 words (wikitext, rev 1376061415) |  | Wikipedia article |
| wikipedia:Amortized_analysis | wikipedia | CC BY-SA 4.0 | no | prose | complexity; dynamic arrays | ~1094 words (wikitext, rev 1380651778) |  | Wikipedia article |
| wikipedia:Analysis_of_algorithms | wikipedia | CC BY-SA 4.0 | no | prose | complexity | ~3186 words (wikitext, rev 1365706079) |  | Wikipedia article |
| wikipedia:Array_(data_structure) | wikipedia | CC BY-SA 4.0 | no | prose | arrays | ~3188 words (wikitext, rev 1375967624) |  | Wikipedia article |
| wikipedia:B-tree | wikipedia | CC BY-SA 4.0 | no | prose | balanced trees (B-tree) | ~6651 words (wikitext, rev 1384320239) |  | Wikipedia article |
| wikipedia:Backtracking | wikipedia | CC BY-SA 4.0 | no | prose | backtracking | ~1843 words (wikitext, rev 1370199668) |  | Wikipedia article |
| wikipedia:Bellman–Ford_algorithm | wikipedia | CC BY-SA 4.0 | no | prose | shortest paths (Bellman-Ford) | ~2369 words (wikitext, rev 1381060493) |  | Wikipedia article |
| wikipedia:Big_O_notation | wikipedia | CC BY-SA 4.0 | no | prose | complexity | ~6749 words (wikitext, rev 1384271173) |  | Wikipedia article |
| wikipedia:Binary_heap | wikipedia | CC BY-SA 4.0 | no | prose | heaps | ~3606 words (wikitext, rev 1371608911) |  | Wikipedia article |
| wikipedia:Binary_search | wikipedia | CC BY-SA 4.0 | no | prose | binary search | ~7650 words (wikitext, rev 1382043435) |  | Wikipedia article |
| wikipedia:Binary_search_tree | wikipedia | CC BY-SA 4.0 | no | prose | BSTs | ~2400 words (wikitext, rev 1380655902) | recursion (Part III) | Wikipedia article |
| wikipedia:Binary_tree | wikipedia | CC BY-SA 4.0 | no | prose | trees | ~4490 words (wikitext, rev 1378025742) |  | Wikipedia article |
| wikipedia:Bit_array | wikipedia | CC BY-SA 4.0 | no | prose | bit manipulation | ~3316 words (wikitext, rev 1367290989) |  | Wikipedia article |
| wikipedia:Bit_manipulation | wikipedia | CC BY-SA 4.0 | no | prose | bit manipulation | ~1284 words (wikitext, rev 1376584902) |  | Wikipedia article |
| wikipedia:Bitwise_operation | wikipedia | CC BY-SA 4.0 | no | prose | bit manipulation | ~4261 words (wikitext, rev 1381437298) |  | Wikipedia article |
| wikipedia:Breadth-first_search | wikipedia | CC BY-SA 4.0 | no | prose | BFS | ~1336 words (wikitext, rev 1384388217) |  | Wikipedia article |
| wikipedia:Bubble_sort | wikipedia | CC BY-SA 4.0 | no | prose | sorting | ~2091 words (wikitext, rev 1378651729) |  | Wikipedia article |
| wikipedia:Circular_buffer | wikipedia | CC BY-SA 4.0 | no | prose | queues (ring buffer) | ~1324 words (wikitext, rev 1373518894) |  | Wikipedia article |
| wikipedia:Counting_sort | wikipedia | CC BY-SA 4.0 | no | prose | sorting (counting) | ~1248 words (wikitext, rev 1366088359) |  | Wikipedia article |
| wikipedia:Cycle_detection | wikipedia | CC BY-SA 4.0 | no | prose | two pointers (fast/slow) | ~3702 words (wikitext, rev 1380990752) |  | Wikipedia article |
| wikipedia:Depth-first_search | wikipedia | CC BY-SA 4.0 | no | prose | DFS | ~1988 words (wikitext, rev 1380662582) | recursion (Part III) | Wikipedia article |
| wikipedia:Dijkstra's_algorithm | wikipedia | CC BY-SA 4.0 | no | prose | shortest paths (Dijkstra) | ~4949 words (wikitext, rev 1383795292) |  | Wikipedia article |
| wikipedia:Divide-and-conquer_algorithm | wikipedia | CC BY-SA 4.0 | no | prose | divide and conquer | ~2426 words (wikitext, rev 1363143428) |  | Wikipedia article |
| wikipedia:Double-ended_queue | wikipedia | CC BY-SA 4.0 | no | prose | queues (deque) | ~4605 words (wikitext, rev 1382165484) |  | Wikipedia article |
| wikipedia:Doubly_linked_list | wikipedia | CC BY-SA 4.0 | no | prose | linked lists | ~1348 words (wikitext, rev 1376710206) |  | Wikipedia article |
| wikipedia:Dynamic_array | wikipedia | CC BY-SA 4.0 | no | prose | dynamic arrays (amortised doubling) | ~1833 words (wikitext, rev 1375968792) |  | Wikipedia article |
| wikipedia:Dynamic_programming | wikipedia | CC BY-SA 4.0 | no | prose | DP | ~7095 words (wikitext, rev 1376326876) |  | Wikipedia article |
| wikipedia:Eight_queens_puzzle | wikipedia | CC BY-SA 4.0 | no | prose | backtracking | ~2747 words (wikitext, rev 1364646763) |  | Wikipedia article |
| wikipedia:Find_first_set | wikipedia | CC BY-SA 4.0 | no | prose | bit manipulation | ~3879 words (wikitext, rev 1377853279) |  | Wikipedia article |
| wikipedia:Floyd–Warshall_algorithm | wikipedia | CC BY-SA 4.0 | no | prose | shortest paths (Floyd-Warshall) | ~2375 words (wikitext, rev 1368880655) |  | Wikipedia article |
| wikipedia:Graph_(abstract_data_type) | wikipedia | CC BY-SA 4.0 | no | prose | graph representations | ~1600 words (wikitext, rev 1357528269) |  | Wikipedia article |
| wikipedia:Graph_traversal | wikipedia | CC BY-SA 4.0 | no | prose | BFS/DFS | ~1291 words (wikitext, rev 1376980928) |  | Wikipedia article |
| wikipedia:Greedy_algorithm | wikipedia | CC BY-SA 4.0 | no | prose | greedy | ~1244 words (wikitext, rev 1380963546) |  | Wikipedia article |
| wikipedia:Hamming_weight | wikipedia | CC BY-SA 4.0 | no | prose | bit manipulation (popcount) | ~2828 words (wikitext, rev 1340429552) |  | Wikipedia article |
| wikipedia:Hash_function | wikipedia | CC BY-SA 4.0 | no | prose | hash tables | ~6204 words (wikitext, rev 1381471264) |  | Wikipedia article |
| wikipedia:Hash_table | wikipedia | CC BY-SA 4.0 | no | prose | hash tables | ~4383 words (wikitext, rev 1384236591) |  | Wikipedia article |
| wikipedia:Heap_(data_structure) | wikipedia | CC BY-SA 4.0 | no | prose | heaps | ~2009 words (wikitext, rev 1377140311) |  | Wikipedia article |
| wikipedia:Heapsort | wikipedia | CC BY-SA 4.0 | no | prose | sorting (heapsort) | ~5418 words (wikitext, rev 1382190663) |  | Wikipedia article |
| wikipedia:Huffman_coding | wikipedia | CC BY-SA 4.0 | no | prose | greedy | ~4289 words (wikitext, rev 1379018579) | priority queues | Wikipedia article |
| wikipedia:Insertion_sort | wikipedia | CC BY-SA 4.0 | no | prose | sorting (insertion) | ~2891 words (wikitext, rev 1376135275) |  | Wikipedia article |
| wikipedia:Interval_scheduling | wikipedia | CC BY-SA 4.0 | no | prose | greedy | ~2235 words (wikitext, rev 1321258022) |  | Wikipedia article |
| wikipedia:Iterative_deepening_depth-first_search | wikipedia | CC BY-SA 4.0 | no | prose | DFS (iterative deepening) | ~2087 words (wikitext, rev 1359452063) |  | Wikipedia article |
| wikipedia:Knapsack_problem | wikipedia | CC BY-SA 4.0 | no | prose | DP | ~5024 words (wikitext, rev 1382620032) | complexity classes (NP) | Wikipedia article |
| wikipedia:Kruskal's_algorithm | wikipedia | CC BY-SA 4.0 | no | prose | MST (Kruskal) | ~1666 words (wikitext, rev 1383615701) |  | Wikipedia article |
| wikipedia:Linear_probing | wikipedia | CC BY-SA 4.0 | no | prose | hash tables (linear probing) | ~2825 words (wikitext, rev 1382496804) |  | Wikipedia article |
| wikipedia:Linked_list | wikipedia | CC BY-SA 4.0 | no | prose | linked lists | ~7740 words (wikitext, rev 1382386163) |  | Wikipedia article |
| wikipedia:Longest_common_subsequence | wikipedia | CC BY-SA 4.0 | no | prose | DP | ~4174 words (wikitext, rev 1375229678) |  | Wikipedia article |
| wikipedia:M-ary_tree | wikipedia | CC BY-SA 4.0 | no | prose | trees | ~2206 words (wikitext, rev 1354344919) |  | Wikipedia article |
| wikipedia:Mask_(computing) | wikipedia | CC BY-SA 4.0 | no | prose | bit manipulation | ~1832 words (wikitext, rev 1324860206) |  | Wikipedia article |
| wikipedia:Master_theorem_(analysis_of_algorithms) | wikipedia | CC BY-SA 4.0 | no | prose | complexity; divide and conquer | ~1955 words (wikitext, rev 1277959662) | recursion, divide and conquer (Part III) | Wikipedia article |
| wikipedia:Maximum_subarray_problem | wikipedia | CC BY-SA 4.0 | no | prose | DP (Kadane); sliding window | ~1773 words (wikitext, rev 1365852288) |  | Wikipedia article |
| wikipedia:Memoization | wikipedia | CC BY-SA 4.0 | no | prose | DP (memoisation) | ~3528 words (wikitext, rev 1371985897) |  | Wikipedia article |
| wikipedia:Merge_sort | wikipedia | CC BY-SA 4.0 | no | prose | sorting (merge sort) | ~5702 words (wikitext, rev 1381904724) | recursion | Wikipedia article |
| wikipedia:Minimum_spanning_tree | wikipedia | CC BY-SA 4.0 | no | prose | MST | ~3829 words (wikitext, rev 1383319305) |  | Wikipedia article |
| wikipedia:Ones'_complement | wikipedia | CC BY-SA 4.0 | no | prose | bit manipulation | ~1659 words (wikitext, rev 1379520662) |  | Wikipedia article |
| wikipedia:Open_addressing | wikipedia | CC BY-SA 4.0 | no | prose | hash tables (open addressing) | ~1000 words (wikitext, rev 1353211902) |  | Wikipedia article |
| wikipedia:Prefix_sum | wikipedia | CC BY-SA 4.0 | no | prose | sliding window / prefix sums | ~4643 words (wikitext, rev 1380268978) |  | Wikipedia article |
| wikipedia:Prim's_algorithm | wikipedia | CC BY-SA 4.0 | no | prose | MST (Prim) | ~1663 words (wikitext, rev 1383615903) |  | Wikipedia article |
| wikipedia:Priority_queue | wikipedia | CC BY-SA 4.0 | no | prose | priority queues | ~3891 words (wikitext, rev 1384203053) |  | Wikipedia article |
| wikipedia:Queue_(abstract_data_type) | wikipedia | CC BY-SA 4.0 | no | prose | queues | ~1608 words (wikitext, rev 1370002097) |  | Wikipedia article |
| wikipedia:Quickselect | wikipedia | CC BY-SA 4.0 | no | prose | divide and conquer (selection) | ~1123 words (wikitext, rev 1360595071) |  | Wikipedia article |
| wikipedia:Quicksort | wikipedia | CC BY-SA 4.0 | no | prose | sorting (quicksort) | ~8050 words (wikitext, rev 1380361759) | recursion | Wikipedia article |
| wikipedia:Radix_sort | wikipedia | CC BY-SA 4.0 | no | prose | sorting (radix) | ~2680 words (wikitext, rev 1368747876) |  | Wikipedia article |
| wikipedia:Recursion_(computer_science) | wikipedia | CC BY-SA 4.0 | no | prose | recursion | ~8135 words (wikitext, rev 1361825212) |  | Wikipedia article |
| wikipedia:Red–black_tree | wikipedia | CC BY-SA 4.0 | no | prose | balanced trees (red-black) | ~8472 words (wikitext, rev 1383669143) |  | Wikipedia article |
| wikipedia:Selection_sort | wikipedia | CC BY-SA 4.0 | no | prose | sorting | ~1675 words (wikitext, rev 1384045827) |  | Wikipedia article |
| wikipedia:Self-balancing_binary_search_tree | wikipedia | CC BY-SA 4.0 | no | prose | balanced trees | ~993 words (wikitext, rev 1371949161) |  | Wikipedia article |
| wikipedia:Shortest_path_problem | wikipedia | CC BY-SA 4.0 | no | prose | shortest paths | ~3846 words (wikitext, rev 1381885415) |  | Wikipedia article |
| wikipedia:Sorting_algorithm | wikipedia | CC BY-SA 4.0 | no | prose | sorting | ~7199 words (wikitext, rev 1381709665) |  | Wikipedia article |
| wikipedia:Stack_(abstract_data_type) | wikipedia | CC BY-SA 4.0 | no | prose | stacks | ~3997 words (wikitext, rev 1376688119) |  | Wikipedia article |
| wikipedia:Tail_call | wikipedia | CC BY-SA 4.0 | no | prose | recursion (tail calls) | ~4663 words (wikitext, rev 1375331405) |  | Wikipedia article |
| wikipedia:Time_complexity | wikipedia | CC BY-SA 4.0 | no | prose | complexity | ~4060 words (wikitext, rev 1383623835) |  | Wikipedia article |
| wikipedia:Topological_sorting | wikipedia | CC BY-SA 4.0 | no | prose | topological sort | ~2760 words (wikitext, rev 1380558942) |  | Wikipedia article |
| wikipedia:Tree_(abstract_data_type) | wikipedia | CC BY-SA 4.0 | no | prose | trees | ~2057 words (wikitext, rev 1317276420) |  | Wikipedia article |
| wikipedia:Tree_traversal | wikipedia | CC BY-SA 4.0 | no | prose | tree traversals | ~3013 words (wikitext, rev 1379688139) | recursion (Part III) | Wikipedia article |
| wikipedia:Trie | wikipedia | CC BY-SA 4.0 | no | prose | tries | ~2411 words (wikitext, rev 1357162034) |  | Wikipedia article |
| wikipedia:Two's_complement | wikipedia | CC BY-SA 4.0 | no | prose | bit manipulation (two's complement) | ~5827 words (wikitext, rev 1382915041) |  | Wikipedia article |
| wikipedia:Word_(computer_architecture) | wikipedia | CC BY-SA 4.0 | no | prose | bit manipulation (words) | ~4272 words (wikitext, rev 1368412660) |  | Wikipedia article |
| wikibooks:Algorithms/Backtracking | wikibooks | CC BY-SA 4.0 | no | prose | backtracking | ~1204 words (rev 4657611) |  | Wikibooks chapter |
| wikibooks:Algorithms/Distance_approximations | wikibooks | CC BY-SA 4.0 | no | prose | (out of scope) | ~585 words (rev 3251364) |  | Wikibooks chapter |
| wikibooks:Algorithms/Divide_and_Conquer | wikibooks | CC BY-SA 4.0 | no | prose | divide and conquer; merge sort; binary search | ~5672 words (rev 4657612) |  | Wikibooks chapter |
| wikibooks:Algorithms/Dynamic_Programming | wikibooks | CC BY-SA 4.0 | no | prose | DP (memoisation and tabulation) | ~2353 words (rev 4657613) |  | Wikibooks chapter |
| wikibooks:Algorithms/Greedy_Algorithms | wikibooks | CC BY-SA 4.0 | no | prose | greedy | ~3816 words (rev 3676146) |  | Wikibooks chapter |
| wikibooks:Algorithms/Hill_Climbing | wikibooks | CC BY-SA 4.0 | no | prose | (out of scope: local search, max flow) | ~2606 words (rev 4657608) |  | Wikibooks chapter |
| wikibooks:Algorithms/Introduction | wikibooks | CC BY-SA 4.0 | no | prose | complexity | ~2661 words (rev 4535199) |  | Wikibooks chapter |
| wikibooks:Algorithms/Mathematical_Background | wikibooks | CC BY-SA 4.0 | no | prose | complexity; recurrences | ~1814 words (rev 4657614) |  | Wikibooks chapter |
| wikibooks:Algorithms/Randomization | wikibooks | CC BY-SA 4.0 | no | prose | quicksort; selection | ~7495 words (rev 4657610) |  | Wikibooks chapter |
| wikibooks:Algorithms/Unweighted_Graph_Algorithms | wikibooks | CC BY-SA 4.0 | no | prose | BFS/DFS (stub) | ~655 words (rev 4328030) |  | Wikibooks chapter |
| wikibooks:Data_Structures/Arrays | wikibooks | CC BY-SA 4.0 | no | prose | arrays; dynamic arrays | ~1219 words (rev 4665701) |  | Wikibooks chapter |
| wikibooks:Data_Structures/Asymptotic_Notation | wikibooks | CC BY-SA 4.0 | no | prose | complexity | ~1848 words (rev 4591912) |  | Wikibooks chapter |
| wikibooks:Data_Structures/Graphs | wikibooks | CC BY-SA 4.0 | no | prose | graph representations; BFS/DFS | ~1631 words (rev 4660018) |  | Wikibooks chapter |
| wikibooks:Data_Structures/Hash_Tables | wikibooks | CC BY-SA 4.0 | no | prose | hash tables | ~9601 words (rev 4665700) |  | Wikibooks chapter |
| wikibooks:Data_Structures/Introduction | wikibooks | CC BY-SA 4.0 | no | prose | complexity; arrays; linked lists (node chains) | ~3140 words (rev 4660024) |  | Wikibooks chapter |
| wikibooks:Data_Structures/List_Structures | wikibooks | CC BY-SA 4.0 | no | prose | linked lists; dynamic arrays (vector) | ~3044 words (rev 4660021) |  | Wikibooks chapter |
| wikibooks:Data_Structures/Min_and_Max_Heaps | wikibooks | CC BY-SA 4.0 | no | prose | heaps; priority queues | ~1166 words (rev 3956746) |  | Wikibooks chapter |
| wikibooks:Data_Structures/Sets | wikibooks | CC BY-SA 4.0 | no | prose | sets (bit vectors) | ~898 words (rev 4660019) |  | Wikibooks chapter |
| wikibooks:Data_Structures/Stacks_and_Queues | wikibooks | CC BY-SA 4.0 | no | prose | stacks; queues | ~8203 words (rev 4660020) |  | Wikibooks chapter |
| wikibooks:Data_Structures/Tradeoffs | wikibooks | CC BY-SA 4.0 | no | prose | complexity (ADT trade-offs) | ~812 words (rev 4082984) |  | Wikibooks chapter |
| wikibooks:Data_Structures/Trees | wikibooks | CC BY-SA 4.0 | no | prose | trees; traversals; BSTs; balanced trees | ~7907 words (rev 4071458) | recursion (Part III) | Wikibooks chapter |
| opendsa:AlgAnal/AnalAsymptotic | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 1791 words |  | Asymptotic Analysis and Upper Bounds (OpenDSA module) |
| opendsa:AlgAnal/AnalCases | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 489 words |  | Best, Worst, and Average Cases (OpenDSA module) |
| opendsa:AlgAnal/AnalChap | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 266 words |  | Chapter Introduction: Algorithm Analysis (OpenDSA module) |
| opendsa:AlgAnal/AnalCompvsAlg | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 1302 words |  | Faster Computer, or Faster Algorithm? (OpenDSA module) |
| opendsa:AlgAnal/AnalIntro | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 2066 words |  | Comparing Algorithms (OpenDSA module) |
| opendsa:AlgAnal/AnalLower | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 1207 words |  | Lower Bounds and Theta Notation (OpenDSA module) |
| opendsa:AlgAnal/AnalMisunderstanding | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 628 words |  | Common Algorithm Analysis Misunderstandings (OpenDSA module) |
| opendsa:AlgAnal/AnalMultiple | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 466 words |  | Algorithm Analysis with Multiple Parameters (OpenDSA module) |
| opendsa:AlgAnal/AnalPrelim | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 1301 words |  | Problems, Algorithms, and Programs (OpenDSA module) |
| opendsa:AlgAnal/AnalProblem | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 924 words |  | Analyzing Problems (OpenDSA module) |
| opendsa:AlgAnal/AnalProgram | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 1395 words |  | Calculating Program Running Time (OpenDSA module) |
| opendsa:AlgAnal/AnalSpace | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 1083 words |  | Algorithm Analysis for Space Bounds (OpenDSA module) |
| opendsa:AlgAnal/AnalTuning | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 1372 words |  | Code Tuning and Empirical Analysis (OpenDSA module) |
| opendsa:Background/Logarithms | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 787 words |  | Logarithms (OpenDSA module) |
| opendsa:Background/RecurrenceIntro | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity; recursion | 307 words |  | An Introduction to Recurrent Relations (OpenDSA module) |
| opendsa:Background/Summations | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 538 words |  | Summations Introduction (OpenDSA module) |
| opendsa:Binary/BST | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | BSTs | 1524 words | recursion (Part III) | Binary Search Trees (OpenDSA module) |
| opendsa:Binary/BSTDict | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | BSTs | 279 words |  | Dictionary Implementation Using a BST (OpenDSA module) |
| opendsa:Binary/BinaryTree | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | trees | 761 words |  | Binary Trees Definitions and Properties (OpenDSA module) |
| opendsa:Binary/BinaryTreeFullThm | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | trees | 779 words |  | The Full Binary Tree Theorem (OpenDSA module) |
| opendsa:Binary/BinaryTreeImpl | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | trees | 797 words |  | Binary Tree Node Implementations (OpenDSA module) |
| opendsa:Binary/BinaryTreeNodeSpace | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | trees | 722 words |  | Binary Tree Space Requirements (OpenDSA module) |
| opendsa:Binary/BinaryTreeTraversal | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | tree traversals | 713 words | recursion (Part III) | Binary Tree Traversals (OpenDSA module) |
| opendsa:Binary/CompleteTree | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | heaps (array layout) | 618 words |  | Array Implementation for Complete Binary Trees (OpenDSA module) |
| opendsa:Binary/Heaps | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | heaps; priority queues | 2316 words |  | Heaps and Priority Queues (OpenDSA module) |
| opendsa:Binary/HuffProof | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | greedy (Huffman proof) | 486 words |  | Proof of Optimality for Huffman Coding (OpenDSA module) |
| opendsa:Binary/Huffman | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | greedy (Huffman) | 2137 words |  | Huffman Coding Trees (OpenDSA module) |
| opendsa:Binary/TreeTrie | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | tries (short) | 188 words |  | Trees versus Tries (OpenDSA module) |
| opendsa:Binary/WritingTraversals | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | tree traversals | 765 words | recursion (Part III) | Implementing Tree Traversals (OpenDSA module) |
| opendsa:Bounds/SortingOptimal | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting (lower bound) | 1017 words |  | Optimal Sorting (OpenDSA module) |
| opendsa:Design/ADT | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | (background) ADTs | 1898 words |  | Abstract Data Types (OpenDSA module) |
| opendsa:Design/Dictionary | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | hash tables; BSTs (dictionary ADT) | 1292 words |  | The Dictionary ADT (OpenDSA module) |
| opendsa:General/GenTreeIntro | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | trees (general) | 998 words |  | General Trees (OpenDSA module) |
| opendsa:General/SequentialRep | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | trees (serialisation) | 1189 words |  | Sequential Tree Representations (OpenDSA module) |
| opendsa:Graph/Floyd | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | shortest paths (Floyd) | 514 words |  | All-Pairs Shortest Paths (OpenDSA module) |
| opendsa:Graph/GraphImpl | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | graph representations | 807 words |  | Graph Implementations (OpenDSA module) |
| opendsa:Graph/GraphIntro | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | graph representations | 1789 words |  | Graphs Chapter Introduction (OpenDSA module) |
| opendsa:Graph/GraphShortest | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | shortest paths (Dijkstra) | 1391 words |  | Shortest-Paths Problems (OpenDSA module) |
| opendsa:Graph/GraphTopsort | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | topological sort | 697 words |  | Topological Sort (OpenDSA module) |
| opendsa:Graph/GraphTraversal | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | BFS/DFS | 931 words |  | Graph Traversals (OpenDSA module) |
| opendsa:Graph/Kruskal | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | MST (Kruskal) | 296 words |  | Kruskal's Minimal Cost Spanning Tree Algorithm (OpenDSA module) |
| opendsa:Graph/MCST | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | MST (Prim) | 989 words |  | Minimal Cost Spanning Trees (OpenDSA module) |
| opendsa:Hashing/BucketHash | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | hash tables | 529 words |  | Bucket Hashing (OpenDSA module) |
| opendsa:Hashing/HashAnal | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | hash tables | 956 words |  | Analysis of Closed Hashing (OpenDSA module) |
| opendsa:Hashing/HashCImproved | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | hash tables | 1789 words |  | Improved Collision Resolution (OpenDSA module) |
| opendsa:Hashing/HashCSimple | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | hash tables | 708 words |  | Simple Collision Resolution (OpenDSA module) |
| opendsa:Hashing/HashDel | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | hash tables | 626 words |  | Hashing Deletion (OpenDSA module) |
| opendsa:Hashing/HashFunc | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | hash tables | 1056 words |  | Hash Function Principles (OpenDSA module) |
| opendsa:Hashing/HashFuncExamp | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | hash tables | 1765 words |  | Sample Hash Functions (OpenDSA module) |
| opendsa:Hashing/HashIntro | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | hash tables | 750 words |  | Introduction to Hashing (OpenDSA module) |
| opendsa:Hashing/OpenHash | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | hash tables | 546 words |  | Open Hashing (OpenDSA module) |
| opendsa:List/Freelist | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | linked lists | 544 words |  | Freelists (OpenDSA module) |
| opendsa:List/ListADT | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | linked lists; arrays | 1183 words |  | A List ADT (OpenDSA module) |
| opendsa:List/ListAnalysis | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | arrays vs linked lists | 1062 words |  | Comparison of List Implementations (OpenDSA module) |
| opendsa:List/ListArray | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | arrays | 202 words |  | Lists and the Array-Based List Implementation (OpenDSA module) |
| opendsa:List/ListDouble | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | linked lists | 766 words |  | Doubly Linked Lists (OpenDSA module) |
| opendsa:List/ListElement | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | linked lists | 368 words |  | List Element Implementations (OpenDSA module) |
| opendsa:List/ListLinked | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | linked lists | 612 words |  | Linked List Implementation (OpenDSA module) |
| opendsa:List/Queue | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | queues (circular array) | 458 words |  | Implementing the Array-Based Queue (OpenDSA module) |
| opendsa:List/StackArray | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | stacks | 280 words |  | Implementing an Array-Based Stack (OpenDSA module) |
| opendsa:List/StackLinked | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | stacks | 270 words |  | Implementing a Linked Stack (OpenDSA module) |
| opendsa:List/StackRecur | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | stacks; recursion | 1046 words |  | Implementing Recursion with a Stack (OpenDSA module) |
| opendsa:RecurTutor/HarderWrite | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | recursion | 319 words |  | Writing More Sophisticated Recursive Functions (OpenDSA module) |
| opendsa:RecurTutor/RecIntro | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | recursion | 662 words |  | Introduction to Recursion (OpenDSA module) |
| opendsa:RecurTutor/Trace | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | recursion | 925 words |  | Tracing Recursive Code (OpenDSA module) |
| opendsa:RecurTutor/Write | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | recursion | 229 words |  | Writing a Recursive Function (OpenDSA module) |
| opendsa:SearchStruct/AVL | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | balanced trees (AVL) | 717 words |  | AVL (OpenDSA module) |
| opendsa:SearchStruct/BalancedTree | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | balanced trees | 455 words |  | BalancedTree (OpenDSA module) |
| opendsa:SearchStruct/SkipList | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | (stretch) skip lists | 1145 words |  | Skip Lists (OpenDSA module) |
| opendsa:SearchStruct/Splay | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | balanced trees (splay) | 1253 words |  | Splay (OpenDSA module) |
| opendsa:Searching/BinarySearch | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | binary search | 673 words | recursion (Part III) | BinarySearch (OpenDSA module) |
| opendsa:Searching/SearchIntro | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | binary search (search intro) | 503 words |  | SearchIntro (OpenDSA module) |
| opendsa:Searching/SortedSearch | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | binary search | 3747 words |  | Search in Sorted Arrays (OpenDSA module) |
| opendsa:Searching/UnsortedSearch | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity (linear search) | 1251 words |  | Analyzing Search in Unsorted Lists (OpenDSA module) |
| opendsa:SeniorAlgAnal/AmortAnal | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity (amortised analysis) | 1411 words |  | Amortized Analysis (OpenDSA module) |
| opendsa:SeniorAlgAnal/DynamicProgramming | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | DP | 3213 words |  | Dynamic Programming (OpenDSA module) |
| opendsa:SeniorAlgAnal/GrowthRate | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity | 917 words |  | Growth Rates Review (OpenDSA module) |
| opendsa:SeniorAlgAnal/Recurrence | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | complexity; divide and conquer (recurrences) | 2525 words |  | Solving Recurrence Relations (OpenDSA module) |
| opendsa:SeniorAlgAnal/TOH | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | recursion (Towers of Hanoi) | 3270 words |  | Introduction to Analyzing a Problem (OpenDSA module) |
| opendsa:Sorting/BinSort | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 716 words |  | Binsort (OpenDSA module) |
| opendsa:Sorting/BubbleSort | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 440 words |  | Bubble Sort (OpenDSA module) |
| opendsa:Sorting/ExchangeSort | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 290 words |  | The Cost of Exchange Sorting (OpenDSA module) |
| opendsa:Sorting/Heapsort | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 630 words |  | Heapsort (OpenDSA module) |
| opendsa:Sorting/InSort | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 623 words |  | Chapter Introduction: Sorting (OpenDSA module) |
| opendsa:Sorting/InsertionSort | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 786 words |  | Insertion Sort (OpenDSA module) |
| opendsa:Sorting/Mergesort | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 357 words |  | Mergesort Concepts (OpenDSA module) |
| opendsa:Sorting/MergesortImpl | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 598 words |  | Implementing Mergesort (OpenDSA module) |
| opendsa:Sorting/Quicksort | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 2215 words |  | Quicksort (OpenDSA module) |
| opendsa:Sorting/QuicksortVid | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 2323 words |  | QuicksortVid (OpenDSA module) |
| opendsa:Sorting/RadixSort | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 1175 words |  | Radix Sort (OpenDSA module) |
| opendsa:Sorting/SelectionSort | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 388 words |  | Selection Sort (OpenDSA module) |
| opendsa:Sorting/Shellsort | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 1280 words |  | Shellsort (OpenDSA module) |
| opendsa:Sorting/SortNotation | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 502 words |  | Sorting Terminology and Notation (OpenDSA module) |
| opendsa:Sorting/SortOpt | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 1917 words |  | Optimizing Sort Algorithms with Code Tuning (OpenDSA module) |
| opendsa:Sorting/SortingEmpirical | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 1382 words |  | An Empirical Comparison of Sorting Algorithms (OpenDSA module) |
| opendsa:Sorting/SortingLowerBound | opendsa | MIT (needs ruling) | no | prose + figure (JSAV slideshows) | sorting | 1032 words |  | Lower Bounds for Sorting (OpenDSA module) |
| lt-njoroge:1.1 | lt-njoroge | CC BY-SA | no | prose | complexity (algorithms intro) | 738 words, 0 images |  | 1.1: Activity 1 - Introduction to Algorithms and Problem Solving |
| lt-njoroge:1.2 | lt-njoroge | CC BY-SA | no | prose | complexity | 483 words, 0 images |  | 1.2: Activity 2 - The characteristics of an algorithm |
| lt-njoroge:1.3 | lt-njoroge | CC BY-SA | no | prose | (background) pseudocode | 1117 words, 1 images |  | 1.3: Activity 3 - Using pseudo-codes and flowcharts to represent algorithms |
| lt-njoroge:2.1 | lt-njoroge | CC BY-SA | no | prose | recursion | 656 words, 0 images |  | 2.1: Activity 1 - Recursive Algorithm |
| lt-njoroge:3.1 | lt-njoroge | CC BY-SA | no | prose | arrays; linked lists; stacks; queues; trees | 1905 words, 5 images |  | 3.1: Activity 1 - Data Structures |
| lt-njoroge:3.2 | lt-njoroge | CC BY-SA | no | prose | (background) ADTs | 583 words, 0 images |  | 3.2: Activity 2 - Abstract Data Type |
| lt-njoroge:4.1 | lt-njoroge | CC BY-SA | no | prose | binary search | 588 words, 1 images |  | 4.1: Activity 1 - Searching Algorithm |
| lt-njoroge:4.2 | lt-njoroge | CC BY-SA | no | prose | sorting | 1425 words, 16 images |  | 4.2: Activity 2 - Sorting Algorithm |
| lt-justo:1.1 | lt-justo | not declared (unclear: link-only) | no | link-only | complexity | 1619 words, 5 images |  | 1.1: Activity 1 - Overview of Algorithm Design and Analysis |
| lt-justo:1.2 | lt-justo | not declared (unclear: link-only) | no | link-only | recursion; backtracking | 2288 words, 12 images |  | 1.2: Activity 2 - Recursion and Recursive Backtracking |
| lt-justo:1.3 | lt-justo | not declared (unclear: link-only) | no | link-only | DP | 2325 words, 2 images |  | 1.3: Activity 3 - Dynamic Programming |
| lt-justo:2.1 | lt-justo | CC BY-SA 3.0 | no | prose | binary search | 1443 words, 2 images |  | 2.1: Activity 1 - Searching Techniques |
| lt-justo:2.2 | lt-justo | CC BY-SA 3.0 | no | prose | BSTs | 1554 words, 8 images |  | 2.2: Activity 2 - Binary Search Tree |
| lt-justo:2.3 | lt-justo | CC BY-SA 3.0 | no | prose | heaps | 1778 words, 10 images |  | 2.3: Activity 3 - Heaps |
| lt-justo:3.1 | lt-justo | CC BY-SA 3.0 | no | prose | sorting (insertion) | 856 words, 1 images |  | 3.1: Activity 1 - Sorting Algorithms by insertion method |
| lt-justo:3.2 | lt-justo | CC BY-SA 3.0 | no | prose | sorting (selection, heapsort) | 925 words, 4 images |  | 3.2: Activity 2 - Sorting Algorithms by selection method |
| lt-justo:3.3 | lt-justo | CC BY-SA 3.0 | no | prose | sorting (merge, quick) | 2237 words, 1 images |  | 3.3: Activity 3 - Sorting Algorithms by Merge and Partition methods |
| lt-justo:4.1 | lt-justo | not declared (unclear: link-only) | no | link-only | hash tables | 2982 words, 5 images |  | 4.1: Activity 1 - Hash Tables |
| lt-justo:4.2 | lt-justo | not declared (unclear: link-only) | no | link-only | graph representations | 2125 words, 12 images |  | 4.2: Activity 2 - Graphs |
| lt-justo:4.3 | lt-justo | not declared (unclear: link-only) | no | link-only | BFS/DFS; shortest paths; MST | 2641 words, 5 images |  | 4.3: Activity 3 - Graph Algorithms |
| openstax-introcs:3.1 | openstax-introcs | CC BY 4.0 | no | prose | arrays; linked lists; stacks; queues; trees; BSTs; heaps; graphs; hash tables (survey) | 4400 words, 7 images |  | 3.1: Introduction to Data Structures and Algorithms |
| openstax-introcs:3.2 | openstax-introcs | CC BY 4.0 | no | prose | complexity | 3705 words, 3 images |  | 3.2: Algorithm Design and Discovery |
| openstax-introcs:3.3 | openstax-introcs | CC BY 4.0 | no | prose | complexity; sorting (correctness, cost) | 3093 words, 2 images |  | 3.3: Formal Properties of Algorithms |
| openstax-introcs:3.4 | openstax-introcs | CC BY 4.0 | no | prose | divide and conquer; greedy; brute force; reductions | 2878 words, 6 images |  | 3.4: Algorithmic Paradigms |
| openstax-introcs:3.5 | openstax-introcs | CC BY 4.0 | no | prose | sorting; searching; hashing; DFS/BFS; MST (Kruskal, Prim); Dijkstra | 3130 words, 9 images |  | 3.5: Sample Algorithms by Problem |
| openstax-introcs:3.6 | openstax-introcs | CC BY 4.0 | no | prose | (background) computability | 2242 words, 1 images |  | 3.6: Computer Science Theory |
| lt-csbu:2.1 | lt-csbu | CC BY-SA 3.0 | no | prose | bit manipulation (binary, bitwise ops, masks) | 3994 words, 1 images |  | 2.1: Binary — the basis of computing |
| lt-csbu:2.2 | lt-csbu | CC BY-SA 3.0 | no | prose | bit manipulation (two's complement, floats) | 4803 words, 1 images |  | 2.2: Types and Number Representation |
| csci30:efficiency | csci30 | CC BY-SA 4.0 | no | prose | complexity (orders of growth, asymptotics) | 3212 words |  | Lecture notes chapter: measuring efficiency, model of computation, asymptotic analysis |
| csci30:correctness | csci30 | CC BY-SA 4.0 | no | prose | (background) loop invariants; binary search correctness | 5344 words |  | Induction and loop invariants |
| csci30:recursion | csci30 | CC BY-SA 4.0 | no | prose | recursion; divide and conquer; recurrences | 2403 words |  | Thinking recursively, D&C, solving recurrences |
| csci30:sorting | csci30 | CC BY-SA 4.0 | no | prose | sorting (quadratic, n log n, lower bound, linear) | 1299 words | heaps (for heapsort) | Sorting chapter |
| holden-acs:Minimum Spanning Trees | holden-acs | CC BY-SA 4.0 | no | prose + figure | MST (Kruskal, union-find, Prim) | 1336 words | union-find (Part IV) | Lecture: MST, Kruskal, Prim, spanning tree protocol |
| holden-acs:Dijkstra's Algorithm | holden-acs | CC BY-SA 4.0 | no | prose + figure | BFS; shortest paths (Dijkstra) | 2566 words |  | Lecture: paths, BFS, Dijkstra |
| holden-acs:Binary | holden-acs | CC BY-SA 4.0 | no | prose | bit manipulation | 3074 words |  | Lecture: binary representation and bit operations |
| holden-acs:Recursion | holden-acs | CC BY-SA 4.0 | no | prose | recursion | 1794 words |  | Lecture: recursion |
| holden-acs:Tries | holden-acs | CC BY-SA 4.0 | no | prose + figure | tries | 1861 words |  | Lecture: tries |
| holden-acs:Queues and Stacks | holden-acs | CC BY-SA 4.0 | no | prose | stacks; queues | 393 words |  | Short lecture |
| holden-acs:Directed Acyclic Graphs | holden-acs | CC BY-SA 4.0 | no | prose + figure | topological sort (DAGs) | 1133 words |  | Lecture: DAGs |
| holden-acs:Dynamic Programming | holden-acs | CC BY-SA 4.0 | no | prose | DP | 1986 words |  | Lecture: DP |
| holden-acs:Hashing | holden-acs | CC BY-SA 4.0 | no | prose | hash tables | 1033 words |  | Lecture: hashing |
| itsy-bitsy:(whole file) | itsy-bitsy | CC BY 4.0 | no | prose (code comments) | arrays; hash tables; stacks; queues; linked lists; trees; BSTs; graphs | 7622 words incl. code |  | Annotated JavaScript implementations of basic data structures |
| dsa-dummies:Big O Notation/README.md | dsa-dummies | CC BY 4.0 | no | prose | complexity | ~1000 words |  | Short Big O explainer |
| addiscoder:16 | addiscoder | CC BY-SA 4.0 | no | prose | recursion | ~400 words |  | Intro recursion section in Python course notes |
| appcomb:s_graphs_intro | appcomb | CC BY-SA 4.0 | no | prose + figure | graph representations (terminology) | 2050 words |  | Graph notation and terminology |
| appcomb:s_graphalgorithms_min-wt-span | appcomb | CC BY-SA 4.0 | no | prose + figure | MST (Kruskal, Prim, exchange principle) | 2300 words |  | Minimum weight spanning trees with proofs |
| appcomb:s_graphalgorithms_shortest-paths | appcomb | CC BY-SA 4.0 | no | prose + figure | shortest paths (Dijkstra) | 1705 words |  | Dijkstra with worked example |
| appcomb:s_graphalgorithms_digraphs | appcomb | CC BY-SA 4.0 | no | prose | graph representations (digraphs) | 296 words |  |  |
| brisk:structures#Graph traversal | brisk | CC BY-SA 4.0 | no | prose + figure | BFS; DFS | (part of structures.tex) | queues, stacks | Discrete-math treatment of BFS/DFS |
| brisk:structures#Finding the shortest path | brisk | CC BY-SA 4.0 | no | prose + figure | shortest paths (Dijkstra) | (part of structures.tex) |  |  |
| brisk:structures#Finding the minimal connecting edge set | brisk | CC BY-SA 4.0 | no | prose + figure | MST (Prim) | (part of structures.tex) |  |  |
| brisk:structures#Binary search trees (BST's) | brisk | CC BY-SA 4.0 | no | prose + figure | BSTs; tree traversals; balancedness | (part of structures.tex) |  |  |
| dmoi3:sec_gt-trees | dmoi3 | CC BY-SA 4.0 | no | prose | trees; spanning trees | (PreTeXt section) |  |  |
| dmoi3:sec_seq-recurrence | dmoi3 | CC BY-SA 4.0 | no | prose | recurrences (complexity background) | (PreTeXt section) |  |  |
| anfp:2-3 | anfp | CC BY-SA (text) | no | prose | complexity | ~6 pp |  | SO Documentation: Big-Theta/Omega, Big-O examples |
| anfp:4-8 | anfp | CC BY-SA (text) | no | prose | trees; BSTs; traversals | ~20 pp |  |  |
| anfp:9-11,20,22 | anfp | CC BY-SA (text) | no | prose | graph representations; BFS/DFS; Dijkstra; Bellman-Ford; Floyd-Warshall | ~40 pp |  |  |
| anfp:14-15,26,45,47,48 | anfp | CC BY-SA (text) | no | prose | DP (knapsack, LCS, LIS, edit distance) | ~30 pp |  |  |
| anfp:16-19 | anfp | CC BY-SA (text) | no | prose | greedy; MST (Kruskal, Prim) | ~25 pp | union-find |  |
| anfp:28-38 | anfp | CC BY-SA (text) | no | prose | sorting | ~30 pp |  |  |
| anfp:41-43 | anfp | CC BY-SA (text) | no | prose | BFS; DFS; hash functions | ~12 pp |  |  |
| arxiv-2211.11009:1-2 | arxiv-2211.11009 | CC BY 4.0 | no | prose | dynamic arrays (stretch: space-optimal resizable arrays) | 15264 words (whole paper) | amortised analysis | Research paper (Tarjan, Zwick) |

## Candidates per concept (open prose beyond the registered corpus)

Counts are rows in the table below that pass the gate. They exclude link-only
rows and the registered corpus. OpenDSA and algo-explanation rows are counted,
but they depend on the MIT ruling.

| concept | rows | sources |
|---|---|---|
| complexity / Big-O | 38 | opendsa 20, wikipedia 5, wikibooks 5, lt-njoroge 2, openstax-introcs 2, csci30, dmoi3, anfp, dsa-dummies |
| arrays | 13 | wikipedia 3, wikibooks 3, opendsa 3, itsy-bitsy, lt-njoroge, openstax-introcs, arxiv |
| dynamic arrays (amortised doubling) | 6 | wikipedia 2 (Dynamic array, Amortized analysis), wikibooks 3, arxiv-2211.11009 (stretch) |
| linked lists | 13 | opendsa 6, wikipedia 2, wikibooks 2, itsy-bitsy, lt-njoroge, openstax-introcs |
| stacks / queues | 9 / 12 | wikipedia, wikibooks, opendsa, holden-acs, itsy-bitsy, lt-njoroge, openstax-introcs |
| hash tables | 20 | opendsa 10, wikipedia 4, openstax-introcs 2, wikibooks, holden-acs, itsy-bitsy, anfp |
| binary search | 8 | opendsa 3, wikipedia, wikibooks, lt-justo 2.1, lt-njoroge 4.1, csci30 |
| bit manipulation | 13 | wikipedia 9, lt-csbu 2, holden-acs, wikibooks (Sets: bit vectors) |
| trees and traversals | 27 | opendsa 11, wikipedia 9, brisk, dmoi3, itsy-bitsy, lt-njoroge, openstax-introcs, wikibooks, anfp |
| BSTs | 10 | opendsa 3, wikipedia, wikibooks, lt-justo 2.2, brisk, itsy-bitsy, openstax-introcs, anfp |
| heaps / priority queues | 10 | wikipedia 4, opendsa 2, lt-justo 2, wikibooks, openstax-introcs |
| balanced trees | 10 | wikipedia 5 (AVL, red-black, 2–3, B-tree, self-balancing), opendsa 3, wikibooks, brisk |
| tries | 3 | wikipedia, holden-acs, opendsa (188 words only) |
| graph representations | 9 | wikipedia 3, appcomb 2, opendsa 2, wikibooks, anfp |
| BFS / DFS | 12 | wikipedia 4, wikibooks 2, anfp 2, brisk, holden-acs, opendsa, openstax-introcs |
| topological sort | 3 | wikipedia, opendsa, holden-acs (DAGs) |
| shortest paths | 11 | wikipedia 4, opendsa 2, appcomb, brisk, holden-acs, openstax-introcs, anfp |
| MST | 10 | wikipedia 3, opendsa 2, appcomb, brisk, holden-acs, openstax-introcs, anfp |
| recursion | 13 | opendsa 7, wikipedia 2, csci30, holden-acs, lt-njoroge, addiscoder |
| backtracking | 3 | wikipedia 2 (Backtracking, Eight queens), wikibooks |
| divide and conquer | 7 | wikipedia 3, wikibooks, csci30, opendsa, openstax-introcs |
| sorting | 35 | opendsa 18, wikipedia 9, lt-justo 3, csci30, lt-njoroge, openstax-introcs 2, anfp |
| greedy | 8 | wikipedia 3, opendsa 2 (Huffman), wikibooks, openstax-introcs, anfp |
| dynamic programming | 9 | wikipedia 5, wikibooks, opendsa, holden-acs, anfp |
| two pointers / sliding window | 3 | wikipedia only, and only around the edges: Cycle detection (fast/slow pointers), Prefix sum, Maximum subarray (Kadane) |

## Gaps: concepts with little or no open prose beyond the corpus

- **Two pointers and sliding window: no dedicated open prose.** Wikipedia
  has no article on either technique. Inside the corpus: `cpa:data_structures/stack_queue_modification`
  (sliding-window minimum via a min-queue) and `cpa:others/tortoise_and_hare`.
  The dedicated treatments all fail the gate: Competitive Programmer's
  Handbook ch. 8 and USACO Guide (both CC BY-NC-SA), Tech Interview Handbook
  `array.md` (licence scope unclear), and LeetCode posts linked by CIU (all
  rights reserved).
- **Backtracking: thin.** Open prose is the Wikipedia articles, the Wikibooks
  chapter (~1.2k words), and Erickson ch. 2 in the corpus. The AVU text
  (lt-justo 1.2) is "not declared".
- **Tries: thin.** Wikipedia *Trie*, holden-acs ch. "Tries" (~1.9k words) and
  OpenDSA's 188-word note. CIU's trie links are all Coursera, Yale (blocked)
  or Toptal.
- **Topological sort: thin.** Wikipedia, OpenDSA *Topological Sort* (~700
  words), holden-acs DAGs; Erickson ch. 6 and cp-algorithms in the corpus.
- **Dynamic arrays (amortised doubling):** Wikipedia *Dynamic array* and
  *Amortized analysis*, Wikibooks *Arrays/List Structures*, ODS in the corpus.
  OpenDSA's *Amortized Analysis* module does not cover array doubling. The
  only other open source is a research paper (arxiv-2211.11009).
- **Greedy beyond Huffman, MST and interval scheduling:** only Wikipedia,
  Wikibooks, the OpenStax §3.4 overview and ANFP ch. 17–18.
- **No CC BY video was verifiable** for any topic: the YouTube licence flag
  is unreadable from this environment (see above).

## blocked_hosts

| host | what it was wanted for | how it failed |
|---|---|---|
| www.youtube.com (watch pages) | licence flag (CC BY) and duration of the 100 CIU-linked videos; captions for any CC BY ones | 302 to www.google.com/sorry (bot check); yt-dlp: "Sign in to confirm you're not a bot". oEmbed works (title and channel only). Not worked around. |
| archive.org | licence metadata of 13 UC Berkeley CS61B webcasts linked by CIU | CONNECT tunnel failed, response 403 |
| www.cs.yale.edu | James Aspnes's CS223 notes (tries, radix sort, DP, sorting code) linked by CIU; licence check | CONNECT refused (403) |
| courses.csail.mit.edu | *Mathematics for Computer Science* 2017/2018 edition, reportedly CC BY-SA 3.0 | CONNECT refused |
| export.arxiv.org | arXiv search API (arxiv.org redirects /api/query there) | not on allowlist; used the arxiv.org/search HTML instead |
| open.umn.edu (Open Textbook Library) | search for DSA and algorithms textbooks and their licences | TLS failure: "SSL certificate problem: unable to get local issuer certificate", even with the proxy CA bundle; not retried with verification off |
| pconrad.github.io | CIU "Practice Operations" bits page | CONNECT refused (403) |
| api.github.com (per-repo endpoints) | repo licence metadata | "GitHub access to this repository is not enabled for this session"; worked via `git clone` and raw.githubusercontent.com, and the search endpoint worked |
| en.wikipedia.org / en.wikibooks.org `w/api.php` | bulk wikitext and file licences | HTTP 429 (rate limit, probably shared egress with the other finders); switched to `index.php?action=raw` plus `api/rest_v1/page/title` for revids; the file licence query was retried with backoff |
| not tried (not on allowlist): www.coursera.org, www.geeksforgeeks.org, brilliant.org, www.topcoder.com, khanacademy.org, stackoverflow.com, goalkicker.com, openstax.org, greenteapress.com, runestone.academy, cs50.harvard.edu, visualgo.net, usaco.guide, graphics.stanford.edu | licence pages of CIU-linked or known resources | recorded from repo mirrors where possible (see link-only table) |

## Figures: Wikipedia and Wikibooks files, licence per file

241 files are referenced from the first 67 Wikipedia articles and the 21 Wikibooks pages. Each licence was read from the Commons/en.wikipedia `imageinfo` extmetadata field `LicenseShortName`. 240 pass (84 'Public domain', 4 'PD', 30 CC0, 62 CC BY-SA 3.0 variants, 50 CC BY-SA 4.0, 2 CC BY-SA 2.5, 5 CC BY 4.0, 3 CC BY 3.0, 1 CC BY 2.0). One is tagged MIT and needs the same ruling as OpenDSA. Files in the 14 articles added late (Cycle detection, Prefix sum, Find first set, Mask, Bit array, Ones' complement, Word, K-ary tree, Selection sort, Quickselect, Graph traversal, Bubble sort, IDDFS, Bellman–Ford) were **not** checked, because the API kept returning 429. Check them before use. Files are not downloaded. Fetch them from upload.wikimedia.org when a figure is chosen, and keep the author line for attribution.

| file (Commons/en.wp) | licence (extmetadata LicenseShortName) | status | author | used in |
|---|---|---|---|---|
| 0...15 AND.svg | CC BY 4.0 | pass | WatchduckYou can name the author as "T.  | wikipedia:Bitwise_operation |
| 0...15 OR.svg | CC BY 4.0 | pass | WatchduckYou can name the author as "T.  | wikipedia:Bitwise_operation |
| 1D array diagram.svg | CC BY 4.0 | pass | Tropwine | wikipedia:Array_(data_structure) |
| 2-3 insertion.svg | CC BY-SA 4.0 | pass | Diaa abdelmoneim | wikipedia:2–3_tree |
| 2-3-4 tree 2-node.svg | Public domain | pass | Chrismiceli | wikipedia:2–3_tree |
| 2-3-4-tree 3-node.svg | Public domain | pass | Chrismiceli | wikipedia:2–3_tree |
| 2D array diagram.svg | CC BY 4.0 | pass | Tropwine | wikipedia:Array_(data_structure) |
| 3D array diagram.svg | CC BY 4.0 | pass | Tropwine | wikipedia:Array_(data_structure) |
| 5 minimal red-black trees nN.svg | CC BY-SA 4.0 | pass | Nomen4Omen | wikipedia:Red–black_tree |
| 6n-graph2.svg | Public domain | pass | - | wikipedia:Adjacency_matrix |
| 8 queens puzzle 3d.svg | CC BY-SA 4.0 | pass | Cmglee | wikipedia:Eight_queens_puzzle |
| 8queensminconflict.gif | CC BY-SA 4.0 | pass | Daniel Moisset | wikipedia:Eight_queens_puzzle |
| AST binary tree arith variables.svg | Public domain | pass | original image by User:Emergie, modifica | wikipedia:Tree_traversal |
| AVL Tree Example.gif | CC BY-SA 4.0 | pass | Bruno Schalch | wikipedia:AVL_tree |
| AVL-double-rl K.svg | CC BY-SA 4.0 | pass | Nomen4Omen | wikipedia:AVL_tree |
| AVL-simple-left K.svg | CC BY-SA 4.0 | pass | Nomen4Omen | wikipedia:AVL_tree |
| AVL-tree-wBalance K.svg | CC BY-SA 4.0 | pass | Nomen4Omen | wikipedia:AVL_tree |
| AVLtreef.svg | Public domain | pass | User:Mikm | wikipedia:Self-balancing_binary_search_tree |
| Algorithms-Asymptotic-ExamplePlot1.png | Public domain | pass | NatasaVuksanovic123 | wikibooks:Algorithms/Mathematical_Background |
| Algorithms-Asymptotic-ExamplePlot2.png | Public domain | pass | NatasaVuksanovic123 | wikibooks:Algorithms/Mathematical_Background |
| Algorithms-Asymptotic-ExamplePlot3.png | Public domain | pass | NatasaVuksanovic123 | wikibooks:Algorithms/Mathematical_Background |
| Algorithms-Asymptotic-ExamplePlot4.png | Public domain | pass | NatasaVuksanovic123 | wikibooks:Algorithms/Mathematical_Background |
| Algorithms-F6CallTree.png | Public domain | pass | NatasaVuksanovic123 | wikibooks:Algorithms/Dynamic_Programming |
| Algorithms-F6CallTreeMemoized.png | Public domain | pass | NatasaVuksanovic123 | wikibooks:Algorithms/Dynamic_Programming |
| Algorithms-NetFlow1.png | Public domain | pass | NatasaVuksanovic123 | wikibooks:Algorithms/Hill_Climbing |
| Algorithms-NetFlow2.png | Public domain | pass | NatasaVuksanovic123 | wikibooks:Algorithms/Hill_Climbing |
| Algorithms-NetFlow3.png | Public domain | pass | NatasaVuksanovic123 | wikibooks:Algorithms/Hill_Climbing |
| AlgorithmsLeastConflicts.png | Public domain | pass | NatasaVuksanovic123 | wikibooks:Algorithms/Greedy_Algorithms |
| AlgorithmsShortestFirst.png | Public domain | pass | NatasaVuksanovic123 | wikibooks:Algorithms/Greedy_Algorithms |
| Approximate-binary-search.svg | CC0 | pass | Esquivalience | wikipedia:Binary_search |
| Array of array storage.svg | Public domain | pass | No machine-readable author provided. Dco | wikipedia:Array_(data_structure); wikibooks:Data_Structures/Arrays |
| ArrayListAmotizedPush.png | CC0 | pass | Mxxxr | wikipedia:Amortized_analysis |
| B tree insertion example.png | Public domain | pass | User:Maxtremus | wikipedia:B-tree |
| B-tree.svg | CC BY-SA 3.0 | pass | CyHawk | wikipedia:B-tree |
| BFS-Algorithm Search Way.gif | CC BY-SA 4.0 | pass | NeptoTech | wikipedia:Breadth-first_search |
| BST node deletion.png | CC0 | pass | WikiLinuz | wikipedia:Binary_search_tree |
| Bellman-Ford worst-case example.svg | CC0 | pass | User:Dcoetzee | wikipedia:Bellman–Ford_algorithm |
| BigOnotationfunctionapprox popular.svg | CC BY-SA 4.0 | pass | User:Colourfulskier | wikipedia:Big_O_notation |
| Binary Tree Rotation (animated).gif | CC BY-SA 3.0 de | pass | Nomen4Omen | wikipedia:Red–black_tree |
| Binary search complexity.svg | CC0 | pass | Esquivalience | wikipedia:Binary_search |
| Binary search example tree.svg | CC0 | pass | Esquivalience | wikipedia:Binary_search |
| Binary search tree search 4.svg | Public domain | pass | Binary_search_tree.svg: Booyabazooka der | wikipedia:Binary_search |
| Binary search tree.svg | Public domain | pass | No machine-readable author provided. Dco | wikipedia:Binary_search_tree |
| Binary search vs Linear search example svg.svg | CC BY-SA 4.0 | pass | Jochen Burghardt | wikipedia:Analysis_of_algorithms |
| Binary tree in array.svg | Public domain | pass | No machine-readable author provided. Dco | wikipedia:Binary_tree; wikipedia:Binary_heap |
| Binary tree v2.svg | CC BY-SA 4.0 | pass | Radke7CB | wikipedia:Binary_tree |
| Binary-heap.png | CC BY-SA 3.0 | pass | Mahanga at English Wikibooks | wikibooks:Data_Structures/Min_and_Max_Heaps |
| Binary-search-work.gif | CC BY-SA 4.0 | pass | Mazen Embaby | wikipedia:Binary_search |
| BinaryTreeRotations.svg | CC BY-SA 3.0 | pass | Josell7 | wikipedia:Binary_tree; wikipedia:Self-balancing_binary_search_tree |
| BlackNode.svg | Public domain | pass | Nomen4Omen | wikipedia:Red–black_tree |
| Bstreedeleteleafexample.jpg | Public domain | pass | - | wikibooks:Data_Structures/Trees |
| Bstreedeletenotrightchildexample.jpg | Public domain | pass | - | wikibooks:Data_Structures/Trees |
| Bstreedeleteonechildexample.jpg | Public domain | pass | - | wikibooks:Data_Structures/Trees |
| Bstreedeleterightchildexample.jpg | Public domain | pass | Linuxdude at English Wikibooks | wikibooks:Data_Structures/Trees |
| Bstreefindsuccessorexample.jpg | Public domain | pass | Linuxdude at English Wikibooks | wikibooks:Data_Structures/Trees |
| Bstreesample.jpg | Public domain | pass | - | wikibooks:Data_Structures/Trees |
| Bstreesearchexample.jpg | Public domain | pass | - | wikibooks:Data_Structures/Trees |
| Bubblesort-edited-color.svg | CC0 | pass | Pmdumuid | wikipedia:Sorting_algorithm |
| BulkDeletionPQ.svg | CC BY-SA 4.0 | pass | Bahodil | wikipedia:Priority_queue |
| CAS insert.png | CC BY-SA 3.0 | pass | Spamduck | wikibooks:Algorithms/Randomization |
| CPT-LinkedLists-addingnode.svg | Public domain | pass | Singly_linked_list_insert_after.png: Der | wikipedia:Linked_list |
| CPT-LinkedLists-deletingnode.svg | Public domain | pass | Pluke | wikipedia:Linked_list |
| Check-green.svg | Public domain | pass | User:ZStoler, User:WarX, gmaxwell | wikipedia:Red–black_tree |
| Chess d45.svg | Public domain | pass | Cburnett | wikipedia:Eight_queens_puzzle |
| Chess l45.svg | Public domain | pass | Cburnett | wikipedia:Eight_queens_puzzle |
| Chess qld45.svg | CC BY-SA 3.0 | pass | Cburnett | wikipedia:Eight_queens_puzzle |
| Chess qll45.svg | CC BY-SA 3.0 | pass | Cburnett | wikipedia:Eight_queens_puzzle |
| Chess qlt45.svg | CC BY-SA 3.0 | pass | Cburnett | wikipedia:Eight_queens_puzzle |
| Chessboard480.svg | CC0 | pass | החבלן | wikipedia:Eight_queens_puzzle |
| Circular Buffer Animation.gif | CC BY-SA 4.0 | pass | MuhannadAjjan | wikipedia:Circular_buffer |
| Circular buffer - 6789345.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Circular_buffer |
| Circular buffer - 6789AB5 with pointers.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Circular_buffer |
| Circular buffer - 6789AB5.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Circular_buffer |
| Circular buffer - X789ABX.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Circular_buffer |
| Circular buffer - XX123XX with pointers.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Circular_buffer |
| Circular buffer - XX123XX.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Circular_buffer |
| Circular buffer - XX1XXXX.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Circular_buffer |
| Circular buffer - XXXX3XX.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Circular_buffer |
| Circular buffer - empty.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Circular_buffer |
| Circular buffer.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Circular_buffer |
| Circularly-linked-list.svg | Public domain | pass | Lasindi | wikipedia:Linked_list |
| Commons-logo.svg | CC-BY-SA-3.0 | pass | - | wikipedia:Analysis_of_algorithms; wikipedia:Array_(data_structure); wikipedia:Linked_list; wikipedia:Stack_(abstract_data_type); wikipedia:H |
| Comparison computational complexity.svg | CC BY-SA 4.0 | pass | Cmglee | wikipedia:Analysis_of_algorithms; wikipedia:Time_complexity |
| Complete binary2.svg | CC BY-SA 4.0 | pass | Tmigler, jmatocha | wikipedia:Binary_tree |
| Concurrent prio queue conflict.svg | CC BY-SA 4.0 | pass | Zratak | wikipedia:Priority_queue |
| DHT en.svg | Public domain | pass | Jnlin | wikipedia:Hash_table |
| Data Queue.svg | CC BY-SA 3.0 | pass | This Image was created by User:Vegpuff.  | wikipedia:Queue_(abstract_data_type) |
| Data stack.svg | Public domain | pass | User:Boivie | wikibooks:Data_Structures/Stacks_and_Queues |
| Deletion of internal binary tree node.svg | CC0 | pass | Chris857 | wikipedia:Binary_tree |
| Depth-First-Search.gif | CC BY-SA 3.0 | pass | Mre | wikipedia:Depth-first_search |
| Depth-first-tree.svg | CC BY-SA 3.0 | pass | Alexander Drichel | wikipedia:Depth-first_search |
| Deque-01.svg | CC BY-SA 4.0 | pass | Xavier-gl71 | wikipedia:Double-ended_queue |
| Deque-railroad.svg | CC BY-SA 4.0 | pass | Xavier-gl71 | wikipedia:Double-ended_queue |
| Dijkstra negative edge counterexample.gif | Public domain | pass | Author: ChatGPT | wikipedia:Dijkstra's_algorithm |
| DijkstraDemo.gif | CC BY-SA 4.0 | pass | Shiyu Ji | wikipedia:Dijkstra's_algorithm |
| Dijkstras progress animation.gif | CC BY 3.0 | pass | Subh83 | wikipedia:Dijkstra's_algorithm |
| Directed acyclic graph 2.svg | Public domain | pass | Johannes Rössel (talk) | wikipedia:Topological_sorting |
| Directed.svg | Public domain | pass | - | wikipedia:Graph_(abstract_data_type); wikibooks:Data_Structures/Graphs |
| Distributed adjacency matrix for parallel prim.png | CC BY-SA 4.0 | pass | Kmmsfg | wikipedia:Prim's_algorithm |
| Doubly-linked-list.svg | Public domain | pass | Lasindi | wikipedia:Linked_list; wikipedia:Doubly_linked_list; wikipedia:Double-ended_queue |
| Dynamic array.svg | CC0 | pass | Dcoetzee | wikipedia:Dynamic_array; wikipedia:Double-ended_queue |
| Edit-clear.svg | Public domain | pass | The people from the Tango! project. And  | wikipedia:AVL_tree; wikipedia:Double-ended_queue |
| Eight-queens-animation.gif | Public domain | pass | Hsilgneymerej | wikipedia:Eight_queens_puzzle |
| Exponential search.svg | CC0 | pass | Esquivalience | wikipedia:Binary_search |
| Fractional cascading.svg | CC0 | pass | Esquivalience | wikipedia:Binary_search |
| Full binary.svg | CC BY-SA 4.0 | pass | Tmigler | wikipedia:Binary_tree |
| GermanyBFS.svg | Public domain | pass | No machine-readable author provided. Reg | wikipedia:Breadth-first_search |
| Global thinking.svg | Public domain | pass | Benjamin D. Esham (bdesham) | wikipedia:Analysis_of_algorithms |
| Graph.traversal.example.svg | CC BY-SA 3.0 | pass | Miles | wikipedia:Depth-first_search; wikipedia:Iterative_deepening_depth-first_search |
| HASHTB12.svg | Public domain | pass | - | wikipedia:Linear_probing; wikipedia:Open_addressing; wikibooks:Data_Structures/Hash_Tables |
| Hamming weight plot.png | CC BY-SA 4.0 | pass | Laurence R. Ugalde URL: https://formulae | wikipedia:Hamming_weight |
| Hardware circular buffer implementation patent us3979733 fig4.png | Public domain | pass | Alexander Gibson Fraser (Bell Telephone  | wikipedia:Circular_buffer |
| Hash table 3 1 1 0 1 0 0 SP.svg | CC BY-SA 3.0 | pass | Jorge Stolfi | wikipedia:Hash_table |
| Hash table 4 1 1 0 0 1 0 LL.svg | Public domain | pass | Jorge Stolfi | wikipedia:Hash_function |
| Hash table 5 0 1 1 1 1 0 LL.svg | CC BY-SA 3.0 | pass | Jorge Stolfi | wikipedia:Hash_table |
| Hash table 5 0 1 1 1 1 0 SP.svg | CC BY-SA 3.0 | pass | Jorge Stolfi | wikipedia:Hash_table |
| Hash table 5 0 1 1 1 1 1 LL.svg | CC BY-SA 3.0 | pass | Jorge Stolfi | wikipedia:Hash_table |
| Heap-as-array.svg | CC BY-SA 4.0 | pass | Maxiantor | wikipedia:Heap_(data_structure) |
| Hewlett-Packard HP-42S, programmable calculator with RPN (combined from two images, cropped).jpg | CC BY 2.0 | pass | File:Programmable RPN calculator Hewlett | wikipedia:Stack_(abstract_data_type) |
| Honeycomb Recursion.jpg | CC0 | pass | NectarLupine | wikipedia:Recursion_(computer_science) |
| IBM 729 Tape Drives.nasa.jpg | Public domain | pass | NASA | wikipedia:Merge_sort |
| If-then-else-control-flow-graph.svg | Public domain | pass | BenRG at English Wikipedia | wikipedia:Depth-first_search |
| Insertion of binary tree node.svg | CC0 | pass | Chris857 | wikipedia:Binary_tree |
| Interpolation search.svg | CC0 | pass | Esquivalience | wikipedia:Binary_search |
| Kruskal Algorithm 1.svg | Public domain | pass | - | wikipedia:Kruskal's_algorithm |
| Kruskal Algorithm 2.svg | Public domain | pass | - | wikipedia:Kruskal's_algorithm |
| Kruskal Algorithm 3.svg | Public domain | pass | - | wikipedia:Kruskal's_algorithm |
| Kruskal Algorithm 4.svg | Public domain | pass | - | wikipedia:Kruskal's_algorithm |
| Kruskal Algorithm 5.svg | Public domain | pass | - | wikipedia:Kruskal's_algorithm |
| Kruskal Algorithm 6.svg | Public domain | pass | - | wikipedia:Kruskal's_algorithm |
| KruskalDemo.gif | CC BY-SA 4.0 | pass | Shiyu Ji | wikipedia:Kruskal's_algorithm |
| Labeled-singly-linked-list.svg | Public domain | pass | JJPMaster | wikibooks:Data_Structures/Introduction |
| Lifo stack.svg | CC0 | pass | Vectorization: Alhadis | wikipedia:Stack_(abstract_data_type) |
| Linear Probing Deletion.png | CC BY-SA 4.0 | pass | Cryptic C62 | wikipedia:Linear_probing |
| Linked-list-based Stack Pop Operation-en.gif | CC BY-SA 4.0 | pass | Michel Bakni | wikipedia:Stack_(abstract_data_type) |
| Linked-list-based Stack Push operation-en.gif | CC BY-SA 4.0 | pass | Michel Bakni | wikipedia:Stack_(abstract_data_type) |
| MAZE 30x20 DFS.ogv | CC BY-SA 3.0 | pass | Purpy Pupple | wikipedia:Depth-first_search |
| MAZE 30x20 Prim.ogv | CC BY-SA 3.0 | pass | Purpy Pupple | wikipedia:Prim's_algorithm |
| Magicsquareexample.svg | Public domain | pass | User:Phidauex | wikipedia:Eight_queens_puzzle |
| MapGermanyGraph.svg | Public domain | pass | No machine-readable author provided. Reg | wikipedia:Breadth-first_search |
| Max-Heap-new.svg | CC BY-SA 4.0 | pass | Kelott | wikipedia:Heap_(data_structure) |
| Merge sort algorithm diagram.svg | Public domain | pass | VineetKumar at English Wikipedia | wikipedia:Divide-and-conquer_algorithm; wikipedia:Merge_sort |
| Merge sort animation.gif | CC BY-SA 2.5 | pass | Nuno Nogueira (Nmnogueira) | wikipedia:Sorting_algorithm |
| Merge sort animation2.gif | CC BY-SA 2.5 | pass | CobaltBlue | wikipedia:Merge_sort |
| Minimum spanning tree.svg | Public domain | pass | No machine-readable author provided. Dco | wikipedia:Minimum_spanning_tree |
| Msp-the-cut-correct.svg | CC BY-SA 3.0 | pass | King rhoton | wikipedia:Minimum_spanning_tree |
| Multiple minimum spanning trees.svg | CC BY-SA 3.0 | pass | Ftiercel | wikipedia:Minimum_spanning_tree |
| N-ary to binary.svg | Public domain | pass | CyHawk | wikipedia:Binary_tree |
| Newton iteration.svg | Public domain | pass | Original: Olegalexandrov Vector: Pbroks1 | wikibooks:Algorithms/Hill_Climbing |
| NilBlue.svg | CC BY-SA 4.0 | pass | Nomen4Omen | wikipedia:Red–black_tree |
| Noisy binary search.svg | CC0 | pass | Esquivalience | wikipedia:Binary_search |
| OOjs UI icon edit-ltr-progressive.svg | PD | pass | https://phabricator.wikimedia.org/diffus | wikipedia:Array_(data_structure); wikipedia:Linked_list; wikipedia:Stack_(abstract_data_type); wikipedia:Hash_table |
| Octicons-terminal.svg | MIT | needs ruling (MIT on an image) | GitHub | wikipedia:Array_(data_structure); wikipedia:Stack_(abstract_data_type); wikipedia:Queue_(abstract_data_type) |
| PD-icon.svg | PD | pass | - | wikipedia:Stack_(abstract_data_type); wikipedia:AVL_tree; wikipedia:Queue_(abstract_data_type) |
| Parallel Topological Sorting.gif | CC BY-SA 4.0 | pass | Morris Kurz | wikipedia:Topological_sorting |
| Parallel multiway mergesort process.svg | CC BY-SA 4.0 | pass | Prof. Dr. Peter Sanders | wikipedia:Merge_sort |
| Pointer implementation of a trie.svg | CC BY-SA 4.0 | pass | Qwertyus | wikipedia:Trie |
| Prim's algorithm proof.svg | CC0 | pass | User:Dcoetzee | wikipedia:Prim's_algorithm |
| Prim's algorithm.svg | CC0 | pass | User:Dcoetzee | wikipedia:Prim's_algorithm |
| PrimAlgDemo.gif | CC BY-SA 4.0 | pass | Shiyu Ji | wikipedia:Prim's_algorithm |
| ProgramCallStack2 en.svg | Public domain | pass | Vectorization: Alhadis | wikipedia:Stack_(abstract_data_type) |
| Question book-new.svg | Cc-by-sa-3.0 | pass | Tkgd2007 | wikipedia:Array_(data_structure); wikipedia:Doubly_linked_list; wikipedia:Tree_traversal; wikipedia:Adjacency_list; wikipedia:Depth-first_se |
| Quicksort-diagram.svg | Public domain | pass | Znupi | wikipedia:Quicksort |
| Quicksort-example.gif | CC BY-SA 3.0 | pass | Matt Chan (jacky's brother) | wikipedia:Quicksort |
| Quicksort1.pdf | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Quicksort2.pdf | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Quicksort3.pdf | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Quicksort4.pdf | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Quicksort5.pdf | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Quicksort6.pdf | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Quicksort7.pdf | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Railroadcars2.png | CC BY-SA 3.0 | pass | PranavAmbhore | wikibooks:Data_Structures/Stacks_and_Queues |
| Recursive problem solving.svg | CC BY-SA 4.0 | pass | Shybovycha | wikipedia:Master_theorem_(analysis_of_algorithms) |
| Recursive1.svg | CC0 | pass | User:Maxtremus | wikipedia:Recursion_(computer_science) |
| Recursive2.svg | CC0 | pass | User:Maxtremus | wikipedia:Recursion_(computer_science) |
| RecursiveTree.JPG | Public domain | pass | Brentsmith101 | wikipedia:Recursion_(computer_science) |
| Red-black tree example with sockets.svg | CC BY-SA 4.0 | pass | Nomen4Omen | wikipedia:Red–black_tree |
| Red-black trees and 2–3–4 trees.svg | CC BY-SA 4.0 | pass | IntGrah | wikipedia:Red–black_tree |
| RedNode.svg | CC BY-SA 4.0 | pass | Nomen4Omen | wikipedia:Red–black_tree |
| RedOrBlackNode.svg | CC BY-SA 4.0 | pass | Nomen4Omen | wikipedia:Red–black_tree |
| Rotate left logically.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Bitwise_operation |
| Rotate left through carry.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Bitwise_operation |
| Rotate left.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Bitwise_operation |
| Rotate right arithmetically.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Bitwise_operation |
| Rotate right logically.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Bitwise_operation |
| Rotate right through carry.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Bitwise_operation |
| Rotate right.svg | CC BY-SA 3.0 | pass | en:User:Cburnett | wikipedia:Bitwise_operation |
| Row and column major order.svg | CC BY-SA 4.0 | pass | Cmglee | wikipedia:Array_(data_structure) |
| SEACComputer 038.jpg | Public domain | pass | National Institute of Standards and Tech | wikipedia:Radix_sort |
| Shell sorting algorithm color bars.svg | CC BY-SA 4.0 | pass | Balu Ertl | wikipedia:Sorting_algorithm |
| Shortest path with direct weights.svg | CC BY-SA 3.0 | pass | Artyom Kalinin | wikipedia:Shortest_path_problem |
| Sierpinski triangle turtle.gif | CC0 | pass | Neuteche | wikipedia:Recursion_(computer_science) |
| Simple cycle graph.svg | Public domain | pass | Booyabazooka at English Wikipedia | wikipedia:Adjacency_list |
| SimpleArray.png | Public domain | pass | - | wikibooks:Data_Structures/Arrays |
| Singly-linked-list.svg | Public domain | pass | Vectorization: Lasindi | wikipedia:Linked_list |
| Snowflake Recursion.jpg | CC0 | pass | NectarLupine | wikipedia:Recursion_(computer_science) |
| Sorted binary tree ALL RGB.svg | Public domain | pass | user:Nomen4Omen | wikipedia:Tree_traversal |
| Sorted binary tree breadth-first traversal.svg | CC0 | pass | Rory O'Kane | wikipedia:Tree_traversal |
| Sorting playing cards using stable sort.svg | CC0 | pass | User:Dcoetzee, User:WDGraham | wikipedia:Sorting_algorithm |
| Sorting stability playing cards.svg | CC0 | pass | Dcoetzee, WDGraham | wikipedia:Sorting_algorithm |
| Stack Pop Operation-en.gif | CC BY-SA 4.0 | pass | Michel Bakni | wikipedia:Stack_(abstract_data_type) |
| Stack Push operation-en.gif | CC BY-SA 4.0 | pass | Michel Bakni | wikipedia:Stack_(abstract_data_type) |
| Stack UML class diagram.svg | CC BY-SA 4.0 | pass | Michel Bakni | wikipedia:Stack_(abstract_data_type) |
| Stack of books.jpg | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Stockspan.svg | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Sudoku solved by bactracking.gif | CC BY-SA 3.0 | pass | Simpsons contributor | wikipedia:Backtracking |
| Symbol category class.svg | PD | pass | PC78, based on work by Julian Herzog, Zs | wikipedia:Analysis_of_algorithms; wikipedia:Array_(data_structure); wikipedia:Sorting_algorithm; wikipedia:Radix_sort |
| Symbol question.svg | Public domain | pass | - | wikipedia:Analysis_of_algorithms |
| Symbol support vote.svg | PD | pass | Zscout370, improved by Ed g2s, simplifie | wikipedia:Linear_probing |
| Symmetric group 4; Cayley graph 1,5,21 (Nauru Petersen); numbers.svg | Public domain | pass | WatchduckYou can name the author as "T.  | wikipedia:Adjacency_matrix |
| Symmetric group 4; Cayley graph 1,5,21 (adjacency matrix).svg | Public domain | pass | WatchduckYou can name the author as "T.  | wikipedia:Adjacency_matrix |
| Symmetric group 4; Cayley graph 4,9 (adjacency matrix).svg | Public domain | pass | WatchduckYou can name the author as "T.  | wikipedia:Adjacency_matrix |
| Symmetric group 4; Cayley graph 4,9; numbers.svg | Public domain | pass | original: Fool (talk) derivative: Watchd | wikipedia:Adjacency_matrix |
| Tallrik - Ystad-2018.jpg | CC BY 3.0 | pass | Foto: Jonn Leffmann | wikipedia:Stack_(abstract_data_type) |
| Text document with red question mark.svg | Public domain | pass | Benjamin D. Esham (bdesham) | wikipedia:Analysis_of_algorithms; wikipedia:Linked_list; wikipedia:Queue_(abstract_data_type) |
| Tic-tac-toe-game-tree.svg | CC BY-SA 3.0 | pass | Traced by User:Stannered, original by en | wikipedia:Breadth-first_search |
| Tower of Hanoi.jpeg | CC BY-SA 3.0 | pass | - | wikipedia:Recursion_(computer_science); wikipedia:Dynamic_programming; wikibooks:Data_Structures/Stacks_and_Queues |
| Towerofhanoi.jpg | CC BY-SA 3.0 | pass | PranavAmbhore | wikibooks:Data_Structures/Stacks_and_Queues |
| Towersofhanoi1.pdf | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Towersofhanoi2.pdf | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Towersofhanoi3.pdf | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Towersofhanoi4.pdf | CC BY-SA 3.0 | pass | Nipunbayas | wikibooks:Data_Structures/Stacks_and_Queues |
| Tree (computer science).svg | CC BY-SA 4.0 | pass | Paddy3118 | wikipedia:Tree_(abstract_data_type) |
| Tree edges.svg | Public domain | pass | Stimpy at English Wikipedia | wikipedia:Depth-first_search |
| TriangleSubtree.svg | Public domain | pass | Nomen4Omen | wikipedia:Red–black_tree |
| TriangleTop.svg | CC BY-SA 4.0 | pass | Nomen4Omen | wikipedia:Red–black_tree |
| Trie example.svg | Public domain | pass | Booyabazooka (based on PNG image by Deco | wikipedia:Trie |
| Trie representation.png | CC BY-SA 4.0 | pass | WikiLinuz | wikipedia:Trie |
| Twos vs ones complement circle.svg | CC BY-SA 4.0 | pass | Cmglee | wikipedia:Two's_complement; wikipedia:Ones'_complement |
| UML deque.svg | CC0 | pass | Frap | wikipedia:Double-ended_queue |
| UML graph ADT.svg | CC0 | pass | Frap | wikipedia:Graph_(abstract_data_type) |
| UML queue class.svg | CC0 | pass | Frap | wikipedia:Queue_(abstract_data_type) |
| Unbalanced binary tree.svg | Public domain | pass | Me (Intgr) | wikipedia:Self-balancing_binary_search_tree |
| Undirected.svg | Public domain | pass | - | wikibooks:Data_Structures/Graphs |
| Uniform binary search.svg | CC0 | pass | Esquivalience | wikipedia:Binary_search |
| Waldburg Ahnentafel.jpg | Public domain | pass | AnonymousUnknown author | wikipedia:Binary_tree |
| Wikibooks-logo.svg | Public domain | pass | Bastique, Ramac et al. | wikipedia:Big_O_notation; wikipedia:Array_(data_structure); wikipedia:Stack_(abstract_data_type); wikipedia:Hash_table; wikipedia:AVL_tree;  |
| Wikisource-logo.svg | CC BY-SA 3.0 | pass | Nicholas Moreau | wikipedia:Linked_list |
| Wikiversity logo 2017.svg | CC BY-SA 3.0 | pass | Julian Herzog | wikipedia:Big_O_notation |
| Wiktionary-logo-en-v2.svg | CC BY-SA 4.0 | pass | Dan Polansky based on work currently att | wikipedia:Array_(data_structure) |
| Z2^4; Cayley table; binary.svg | CC BY 3.0 | pass | WatchduckYou can name the author as "T.  | wikipedia:Bitwise_operation |

## Link-only items found outside CIU (with reason)

| item | licence (where read) | reason | in scope for |
|---|---|---|---|
| Miller & Ranum, *Problem Solving with Algorithms and Data Structures using Python* (github.com/RunestoneInteractive/pythonds) | CC BY-NC-SA 4.0 (LICENSE.txt: "This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License") | NC prose | all of Parts I–III (Python, interactive) |
| Downey, *Think Data Structures* (github.com/AllenDowney/ThinkDataStructures) | book CC BY-NC-SA 3.0 (book/book.tex: "Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License"); repo LICENSE is MIT, which covers the code only | NC prose; the MIT file covers only the code | lists, trees, hashing, maps (Java) |
| Laaksonen, *Competitive Programmer's Handbook* (github.com/pllk/cphb) | CC BY-NC-SA 4.0 (README: "The license of the book is Creative Commons BY-NC-SA 4.0.") | NC prose | **two pointers, sliding window minimum** (ch. 8), bit manipulation (ch. 10), DP, graphs |
| USACO Guide (github.com/cpinitiative/usaco-guide) | CC BY-NC-SA 4.0 (LICENSE) | NC prose | **two pointers, sliding window** modules, prefix sums, BFS/DFS |
| MIT OCW 6.006 Spring 2020 lecture/recitation notes and videos | CC BY-NC-SA 4.0 (ocw.mit.edu course page licence link; OCW terms page) | NC prose and video | every Part I–III topic; the exercises finder registered the problem sets as NC cards |
| MIT OCW 6.042J 2015 *Mathematics for Computer Science* (cached in `sources/_cache/mcs/`) | CC BY-NC-SA 3.0 (page ii of the PDF) | NC. The 2017/2018 edition is reported CC BY-SA 3.0, but courses.csail.mit.edu is blocked, so this is unverified | asymptotics, recurrences, graphs |
| LibreTexts *Mathematics for Computer Science* (Lehman, Leighton, Meyer) | page tag `ccbyncsa`, "shared under a CC BY-NC-SA 4.0" | NC | same |
| Levin, *Discrete Mathematics: An Open Introduction*, 4th ed. | CC BY-NC-SA 4.0 (LICENSE at HEAD) | NC (the 3rd ed. passes and is registered as `dmoi3`) | trees, recurrences |
| Liu Xinyu, *Elementary Algorithms* (github.com/liuxinyu95/AlgoXY) | GNU FDL 1.3 (book includes fdl-1.3.tex); code GPL-3.0 | GFDL is not compatible with CC BY-SA 4.0 | lists, trees, heaps, sorting, search, functional style |
| Di Pierro, *Annotated Algorithms in Python* (github.com/mdipierro/nlib) | book PDF CC BY-NC-ND 3.0 (README); code BSD-3 | NC-ND prose (the code would pass) | sorting, graphs, DP, numerics |
| Sedgewick & Wayne, *Algorithms* 4th ed. | book all rights reserved; algs4 code GPL-3.0 (github.com/kevin-wayne/algs4 LICENSE) | not open; GPL code is outside the code list | everything; Coursera course videos too |
| Berkeley CS61B Fall 2026 textbook (github.com/Berkeley-CS61B/fa26-gitbook) | no licence file or statement | no licence | asymptotics, BSTs, B-trees, LLRB, heaps, graphs, shortest paths, MST, hashing, tries, sorting |
| Tech Interview Handbook, algorithms pages (github.com/yangshun/tech-interview-handbook `apps/website/contents/algorithms/`) | repo LICENSE MIT, but README: "I am providing code in the repository to you under an open source license" | the licence scope for the prose is unclear | **two pointers / sliding window** (array.md), cheat sheets for every topic |
| trekhleb *javascript-algorithms* READMEs | MIT (LICENSE) | provenance unclear: much README text and 125 of the images come from Wikipedia/Wikimedia (BY-SA) and from GeeksforGeeks, mathsisfun.com and tutorialspoint, relicensed as MIT. The exercises finder uses only its tests. | most topics |
| Sean Anderson, *Bit Twiddling Hacks* (graphics.stanford.edu, read on the gibsjose/BitHacks mirror) | "Individually, the code snippets here are in the public domain ... The aggregate collection and descriptions are © 1997-2005 Sean Eron Anderson" | prose is copyrighted (the code snippets are PD and usable as code) | bit manipulation |
| Khan Academy / Dartmouth *Algorithms* (Cormen & Balkcom) | CC BY-NC-SA (not fetched; khanacademy.org not on the allowlist) | NC | binary search, sorting, recursion, graphs |
| GeeksforGeeks, Brilliant, Programiz, VisuAlgo, bigocheatsheet.com, Topcoder tutorials | all rights reserved (not fetched; none of these hosts is on the allowlist) | not open | all |
| CIU `extras/cheat sheets/big-o-cheatsheet.pdf`, `bits-cheat-sheet.pdf` | inside the CC BY-SA repo, but they are browser printouts of third-party pages (bigocheatsheet.com; PDF title "https://devj.talktothemanager.com/bits.php") | provenance unclear | complexity, bits |
| Jasonpolites, Stephan Brumme "Bit Twiddler", eskimo.com C notes, btechsmartclass, toptal, quora | no open licence found / not fetched | not open | bits, linked lists, tries, B-trees |
| Bender, Kuszmaul, Kuszmaul, *Linear Probing Revisited* (arXiv 2107.01250) | arXiv non-exclusive distribution licence 1.0 | not CC | hash tables (stretch) |

## CIU links followed and classified (224 links in the Part I–III sections)

Method: every link in CIU README lines 573–1035 (complexity through DP),
1173–1186 (tries) and 1688–1782 (balanced trees) was extracted (224 links)
and classified. For YouTube links, title and channel came from the official
oEmbed endpoint (www.youtube.com/oembed). The **licence flag could not be
read**: every watch page redirects to `www.google.com/sorry` (a bot check),
and yt-dlp hits the same "Sign in to confirm you're not a bot" wall. Getting
around a bot check is out of bounds. So no YouTube video could be verified
as CC BY. All are link-only, and none had captions pulled.

Counts: link-only 207; pass 12 (all Wikipedia, now fetched); code-only PD 2
(Bit Twiddling Hacks); CC BY-SA in principle but host not allowlisted 2
(Stack Overflow); unclear 1 (CIU's own bits cheat sheet).

By host: YouTube 100 (21 MIT OpenCourseWare → CC BY-NC-SA via OCW terms,
4 CS50, 12 Steven Skiena, 10 mycodeschool, 8 David Taylor, 8 Coderisland,
6 xoaxdotnet, 6 Michael Sambol, 4 Stanford, 19 other channels, 2 unavailable via
oEmbed), Coursera 61 (Coursera terms; not on allowlist), archive.org 13
(UC Berkeley CS61B webcasts; blocked), Wikipedia 12, LeetCode 5, GitHub 5,
Yale/Aspnes 5 (blocked), Topcoder 4, bits.stephan-brumme.com 4, GfG 3, other 12.

Video lengths are not recorded: oEmbed returns no duration, and the watch
pages are behind the bot check. Side-panel notes on length need a browser
pass by a person.

Full per-link table:

| topic | ciu line | title | channel | url | licence | status | note |
|---|---|---|---|---|---|---|---|
| complexity | 579 | Asymptotic Notation | CS50 | https://www.youtube.com/watch?v=iOq5kSKqeR4 | unclear (CS50 states CC BY-NC-SA elsewhere; not verified here) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check |
| complexity | 580 | Big O Notations | Derek Banas | https://www.youtube.com/watch?v=V6mKVRU1evU | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| complexity | 581 | Big Oh Notation (and Omega and Theta) | profbillbyrne | https://www.youtube.com/watch?v=ei-A_wy5Yxw&index=2&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| complexity | 582 | CSE 373 -- Lecture 2, Fall 2020 | Steven Skiena | https://www.youtube.com/watch?v=z1mkCe3kVUA | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| complexity | 583 | UC Berkeley Big O (video) |  | https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98 | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| complexity | 584 | Amortized Analysis - Potential functions | profbillbyrne | https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| complexity | 586 | Computational Complexity: Section 1 |  | https://www.topcoder.com/thrive/articles/Computational%20Complexity%20part%20one | all rights reserved (Topcoder site) | link-only | Topcoder tutorial article; host not allowlisted |
| complexity | 587 | Computational Complexity: Section 2 |  | https://www.topcoder.com/thrive/articles/Computational%20Complexity%20part%20two | all rights reserved (Topcoder site) | link-only | Topcoder tutorial article; host not allowlisted |
| complexity | 588 | Cheat sheet |  | https://bigocheatsheet.com/ | no licence stated / not fetched | link-only | third-party site (bigocheatsheet.com), not on allowlist |
| arrays | 602 | CS50 2020 - Lecture 2 - Arrays | CS50 | https://www.youtube.com/watch?v=tI_tIZFyKBw&t=3009s | unclear (CS50 states CC BY-NC-SA elsewhere; not verified here) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check |
| arrays | 603 | Arrays (video) |  | https://www.coursera.org/lecture/data-structures/arrays-OsBSF | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| arrays | 604 | UC Berkeley CS61B - Linear and Multi-Dim Arrays (video) |  | https://archive.org/details/ucberkeley_webcast_Wp8oiO_CZZE | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| arrays | 605 | Dynamic Arrays (video) |  | https://www.coursera.org/lecture/data-structures/dynamic-arrays-EwbnV | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| arrays | 606 | 07 06  Jagged Arrays | Hemant Maurya | https://www.youtube.com/watch?v=1jtrQqYpt7g | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| linked-lists | 635 | CS50 2020 - Lecture 5 - Data Structures | CS50 | https://www.youtube.com/watch?v=2T-A_GFuoTo&t=650s | unclear (CS50 states CC BY-NC-SA elsewhere; not verified here) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check |
| linked-lists | 636 | Singly Linked Lists (video) |  | https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| linked-lists | 637 | CS 61B - Linked Lists 1 (video) |  | https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0 | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| linked-lists | 638 | CS 61B - Linked Lists 2 (video) |  | https://archive.org/details/ucberkeley_webcast_-c4I3gFYe3w | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| linked-lists | 640 | 5.Linked Data Structures in C Creating a SingleList. | Srikanth Dasari | https://www.youtube.com/watch?v=QN6FPiD0Gzo | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| linked-lists | 643 | Core Linked Lists Vs Arrays (video) |  | https://www.coursera.org/lecture/data-structures-optimizing-performance/core-linked-lists-vs-arrays-rjBs9 | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| linked-lists | 644 | In The Real World Linked Lists Vs Arrays (video) |  | https://www.coursera.org/lecture/data-structures-optimizing-performance/in-the-real-world-lists-vs-arrays-QUaUd | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| linked-lists | 645 | Why you should avoid linked lists (video) |  | https://www.youtube.com/watch?v=YQs6IC-vgmo | unclear | link-only | oEmbed refused (HTTP Error 403: Forbidden); video private/removed or embedding off |
| linked-lists | 649 | Pointers to Pointers |  | https://www.eskimo.com/~scs/cclass/int/sx8.html | no licence stated / not fetched | link-only | third-party site (www.eskimo.com), not on allowlist |
| linked-lists | 666 | Description (video) |  | https://www.coursera.org/lecture/data-structures/doubly-linked-lists-jpGKD | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| stacks | 670 | Stacks (video) |  | https://www.coursera.org/lecture/data-structures/stacks-UdKzQ | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| queues | 675 | Queue (video) |  | https://www.coursera.org/lecture/data-structures/queues-EShpq | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| queues | 676 | Circular buffer/FIFO |  | https://en.wikipedia.org/wiki/Circular_buffer | CC BY-SA 4.0 | pass | fetched into sources/_cache/wikipedia/ where in the topic list |
| hash-tables | 696 | Lecture 8: Hashing with Chaining | MIT OpenCourseWare | https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8 | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| hash-tables | 697 | Lecture 9: Table Doubling, Karp-Rabin | MIT OpenCourseWare | https://www.youtube.com/watch?v=BRO7mVIFt08&index=9&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| hash-tables | 698 | Lecture 10: Open Addressing, Cryptographic Hashing | MIT OpenCourseWare | https://www.youtube.com/watch?v=rvdJDijO2Ro&index=10&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| hash-tables | 699 | PyCon 2010: The Mighty Dictionary | Eugene Yarmash | https://www.youtube.com/watch?v=C4Kc8xzcA68 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| hash-tables | 700 | PyCon 2017: The Dictionary Even Mightier (video) |  | https://www.youtube.com/watch?v=66P5FMkWoVU | unclear | link-only | oEmbed refused (HTTP Error 401: Unauthorized); video private/removed or embedding off |
| hash-tables | 701 | 8. Randomization: Universal & Perfect Hashing | MIT OpenCourseWare | https://www.youtube.com/watch?v=z0lJ2k0sl1g&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=11 | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| hash-tables | 702 | Lecture 07, 09/23: Perfect Hashing | Karger Skoltech | https://www.youtube.com/watch?v=N0COwN14gt0&list=PL2B4EEwhKD-NbwZ4ezj7gyc_3yNrojKM9&index=4 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| hash-tables | 706 | Core Hash Tables (video) |  | https://www.coursera.org/lecture/data-structures-optimizing-performance/core-hash-tables-m7UuP | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| hash-tables | 707 | Data Structures (video) |  | https://www.coursera.org/learn/data-structures/home/week/4 | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| hash-tables | 708 | Phone Book Problem (video) |  | https://www.coursera.org/lecture/data-structures/phone-book-problem-NYZZP | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| hash-tables | 710 | Instant Uploads And Storage Optimization In Dropbox (video) |  | https://www.coursera.org/lecture/data-structures/instant-uploads-and-storage-optimization-in-dropbox-DvaIb | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| hash-tables | 711 | Distributed Hash Tables (video) |  | https://www.coursera.org/lecture/data-structures/distributed-hash-tables-tvH8H | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| binary-search | 725 | Binary Search | CS50 | https://www.youtube.com/watch?v=D5SrAga1pno | unclear (CS50 states CC BY-NC-SA elsewhere; not verified here) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check |
| binary-search | 726 | Binary Search (video) |  | https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search | CC BY-NC-SA (Khan Academy content; not fetched) | link-only | Khan/Dartmouth algorithms tutorial; NC |
| binary-search | 727 | detail |  | https://www.topcoder.com/thrive/articles/Binary%20Search | all rights reserved (Topcoder site) | link-only | Topcoder tutorial article; host not allowlisted |
| binary-search | 728 | blueprint |  | https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems | all rights reserved (LeetCode terms) | link-only | problem/discussion page |
| bits | 735 | Bits cheat sheet |  | https://github.com/jwasham/coding-interview-university/blob/main/extras/cheat%20sheets/bits-cheat-sheet.pdf | CC BY-SA 4.0 (repo) but content is a printout of a third-party page | unclear | bits cheat sheet PDF: title metadata is a third-party URL; provenance unclear |
| bits | 738 | words |  | https://en.wikipedia.org/wiki/Word_(computer_architecture | CC BY-SA 4.0 | pass | fetched into sources/_cache/wikipedia/ where in the topic list |
| bits | 740 | Bit Manipulation | Make School | https://www.youtube.com/watch?v=7jkIUgLC29I | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| bits | 741 | C Programming Tutorial 2-10: Bitwise Operators | rax7 | https://www.youtube.com/watch?v=d0AwjSpNXR0 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| bits | 742 | Bit Manipulation |  | https://en.wikipedia.org/wiki/Bit_manipulation | CC BY-SA 4.0 | pass | fetched into sources/_cache/wikipedia/ where in the topic list |
| bits | 743 | Bitwise Operation |  | https://en.wikipedia.org/wiki/Bitwise_operation | CC BY-SA 4.0 | pass | fetched into sources/_cache/wikipedia/ where in the topic list |
| bits | 744 | Bithacks |  | https://graphics.stanford.edu/~seander/bithacks.html | code PD; descriptions (c) Sean Anderson | link-only (prose); code PD | verified on gibsjose/BitHacks mirror: "Individually, the code snippets here are in the public domain ... The aggregate collection and descriptions are (c) 1997-2005 Sean Eron Anderson" |
| bits | 745 | The Bit Twiddler |  | https://bits.stephan-brumme.com/ | no licence stated / not fetched | link-only | third-party site (bits.stephan-brumme.com), not on allowlist |
| bits | 746 | The Bit Twiddler Interactive |  | https://bits.stephan-brumme.com/interactive.html | no licence stated / not fetched | link-only | third-party site (bits.stephan-brumme.com), not on allowlist |
| bits | 747 | 3. Bit Hacks | MIT OpenCourseWare | https://www.youtube.com/watch?v=ZusiKXcz_ac | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| bits | 748 | Practice Operations |  | https://pconrad.github.io/old_pconrad_cs16/topics/bitOps/ | unclear (host blocked) | link-only | pconrad.github.io refused by proxy (403) |
| bits | 750 | Binary: Plusses & Minuses (Why We Use Two's Complement) - Computerphil | Computerphile | https://www.youtube.com/watch?v=lKTsv6iVxV4 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| bits | 751 | 1s Complement |  | https://en.wikipedia.org/wiki/Ones%27_complement | CC BY-SA 4.0 | pass | fetched into sources/_cache/wikipedia/ where in the topic list |
| bits | 752 | 2s Complement |  | https://en.wikipedia.org/wiki/Two%27s_complement | CC BY-SA 4.0 | pass | fetched into sources/_cache/wikipedia/ where in the topic list |
| bits | 754 | 4 ways to count bits in a byte | Deege  | https://youtu.be/Hzuzo9NJrlc | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| bits | 755 | Count Bits |  | https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan | code PD; descriptions (c) Sean Anderson | link-only (prose); code PD | verified on gibsjose/BitHacks mirror: "Individually, the code snippets here are in the public domain ... The aggregate collection and descriptions are (c) 1997-2005 Sean Eron Anderson" |
| bits | 756 | How To Count The Number Of Set Bits In a 32 Bit Integer |  | http://stackoverflow.com/questions/109023/how-to-count-the-number-of-set-bits-in-a-32-bit-integer | CC BY-SA (version by post date; not fetched) | pass in principle; host not allowlisted | Stack Overflow posts are CC BY-SA; stackoverflow.com not on allowlist |
| bits | 758 | Swap |  | https://bits.stephan-brumme.com/swap.html | no licence stated / not fetched | link-only | third-party site (bits.stephan-brumme.com), not on allowlist |
| bits | 760 | Absolute Integer |  | https://bits.stephan-brumme.com/absInteger.html | no licence stated / not fetched | link-only | third-party site (bits.stephan-brumme.com), not on allowlist |
| trees-bst | 767 | Intro to Trees (video) |  | https://www.coursera.org/lecture/data-structures/trees-95qda | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| trees-bst | 768 | Tree Traversal (video) |  | https://www.coursera.org/lecture/data-structures/tree-traversal-fr51b | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| trees-bst | 769 | BFS and DFS in a Binary Tree | Vivekanand Khyade - Algorithm Every Day | https://www.youtube.com/watch?v=uWL6FJhq5fM | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| trees-bst | 787 | Binary Search Tree Review | David Taylor | https://www.youtube.com/watch?v=x6At0nzX92o&index=1&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| trees-bst | 788 | Introduction (video) |  | https://www.coursera.org/learn/data-structures/lecture/E7cXP/introduction | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| trees-bst | 789 | 6. Binary Trees, Part 1 | MIT OpenCourseWare | https://www.youtube.com/watch?v=76dhtgZt38A&ab_channel=MITOpenCourseWare | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| trees-bst | 791 | Binary search tree - Implementation in C/C++ | mycodeschool | https://www.youtube.com/watch?v=COZK7NATh4k&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=28 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| trees-bst | 792 | BST implementation -  memory allocation in stack and heap | mycodeschool | https://www.youtube.com/watch?v=hWokyBoo0aI&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=29 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| trees-bst | 793 | Find min and max element in a binary search tree | mycodeschool | https://www.youtube.com/watch?v=Ut90klNN264&index=30&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| trees-bst | 794 | Find height of a binary tree | mycodeschool | https://www.youtube.com/watch?v=_pnqMz5nrRs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=31 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| trees-bst | 795 | Binary tree traversal - breadth-first and depth-first strategies | mycodeschool | https://www.youtube.com/watch?v=9RHO6jU--GU&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=32 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| trees-bst | 796 | Binary tree: Level Order Traversal | mycodeschool | https://www.youtube.com/watch?v=86g8jAQug04&index=33&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| trees-bst | 797 | Binary tree traversal: Preorder, Inorder, Postorder | mycodeschool | https://www.youtube.com/watch?v=gm8DUJJhmY4&index=34&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| trees-bst | 798 | Check if a binary tree is binary search tree or not | mycodeschool | https://www.youtube.com/watch?v=yEwSGhSsT0U&index=35&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| trees-bst | 799 | Delete a node from Binary Search Tree | mycodeschool | https://www.youtube.com/watch?v=gcULXE7ViZw&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=36 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| trees-bst | 800 | Inorder Successor in a binary search tree | mycodeschool | https://www.youtube.com/watch?v=5cPbNCrdotA&index=37&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| trees-bst | 802 | insert    // insert value into tree |  | https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/987660183/ | all rights reserved (LeetCode terms) | link-only | problem/discussion page |
| trees-bst | 807 | get_height // returns the height in nodes (single node's height is 1) |  | https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/ | all rights reserved | link-only | GfG article |
| trees-bst | 810 | is_binary_search_tree |  | https://leetcode.com/problems/validate-binary-search-tree/ | all rights reserved (LeetCode terms) | link-only | problem/discussion page |
| heaps | 816 | Heap |  | https://en.wikipedia.org/wiki/Heap_(data_structure | CC BY-SA 4.0 | pass | fetched into sources/_cache/wikipedia/ where in the topic list |
| heaps | 817 | Introduction (video) |  | https://www.coursera.org/lecture/data-structures/introduction-2OpTs | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| heaps | 818 | Binary Trees (video) |  | https://www.coursera.org/learn/data-structures/lecture/GRV2q/binary-trees | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| heaps | 819 | Tree Height Remark (video) |  | https://www.coursera.org/learn/data-structures/supplement/S5xxz/tree-height-remark | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| heaps | 820 | Basic Operations (video) |  | https://www.coursera.org/learn/data-structures/lecture/0g1dl/basic-operations | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| heaps | 821 | Complete Binary Trees (video) |  | https://www.coursera.org/learn/data-structures/lecture/gl5Ni/complete-binary-trees | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| heaps | 822 | Pseudocode (video) |  | https://www.coursera.org/learn/data-structures/lecture/HxQo9/pseudocode | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| heaps | 823 | Algorithms - Sorting - Lecture 2 | Coderisland | https://youtu.be/odNJmw5TOEE?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3291 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| heaps | 824 | Heap Sort (video) |  | https://www.coursera.org/lecture/data-structures/heap-sort-hSzMO | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| heaps | 825 | Building a heap (video) |  | https://www.coursera.org/lecture/data-structures/building-a-heap-dwrOS | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| heaps | 826 | 8. Binary Heaps | MIT OpenCourseWare | https://www.youtube.com/watch?v=Xnpo1atN-Iw&list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY&index=12 | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| heaps | 827 | CS 61B Lecture 24: Priority Queues (video) |  | https://archive.org/details/ucberkeley_webcast_yIUFT6AKBGE | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| heaps | 828 | Linear Time BuildHeap | Algorithms with Attitude | https://www.youtube.com/watch?v=MiyLo8adrWw | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 850 | Sorting Algorithm Stability |  | https://en.wikipedia.org/wiki/Sorting_algorithm#Stability | CC BY-SA 4.0 | pass | fetched into sources/_cache/wikipedia/ where in the topic list |
| sorting | 851 | Stability In Sorting Algorithms |  | http://stackoverflow.com/questions/1517793/stability-in-sorting-algorithms | CC BY-SA (version by post date; not fetched) | pass in principle; host not allowlisted | Stack Overflow posts are CC BY-SA; stackoverflow.com not on allowlist |
| sorting | 852 | Stability In Sorting Algorithms |  | https://www.geeksforgeeks.org/stability-in-sorting-algorithms/ | all rights reserved | link-only | GfG article |
| sorting | 853 | Sorting Algorithms - Stability |  | https://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/stability.pdf | no licence stated / not fetched | link-only | third-party site (homepages.math.uic.edu), not on allowlist |
| sorting | 856 | Merge Sort For Linked List |  | https://www.geeksforgeeks.org/merge-sort-for-linked-list/ | all rights reserved | link-only | GfG article |
| sorting | 860 | Sedgewick - Mergesort (5 videos) |  | https://www.coursera.org/learn/algorithms-part1/home/week/3 | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 861 | 1. Mergesort |  | https://www.coursera.org/lecture/algorithms-part1/mergesort-ARWDq | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 862 | 2. Bottom-up Mergesort |  | https://www.coursera.org/learn/algorithms-part1/lecture/PWNEl/bottom-up-mergesort | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 863 | 3. Sorting Complexity |  | https://www.coursera.org/lecture/algorithms-part1/sorting-complexity-xAltF | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 864 | 4. Comparators |  | https://www.coursera.org/lecture/algorithms-part1/comparators-9FYhS | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 865 | 5. Stability |  | https://www.coursera.org/learn/algorithms-part1/lecture/pvvLZ/stability | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 867 | Sedgewick - Quicksort (4 videos) |  | https://www.coursera.org/learn/algorithms-part1/home/week/3 | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 868 | 1. Quicksort |  | https://www.coursera.org/lecture/algorithms-part1/quicksort-vjvnC | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 869 | 2. Selection |  | https://www.coursera.org/lecture/algorithms-part1/selection-UQxFT | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 870 | 3. Duplicate Keys |  | https://www.coursera.org/lecture/algorithms-part1/duplicate-keys-XvjPd | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 871 | 4. System Sorts |  | https://www.coursera.org/lecture/algorithms-part1/system-sorts-QBNZ7 | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 874 | CS 61B Lecture 29: Sorting I (video) |  | https://archive.org/details/ucberkeley_webcast_EiUvYS2DT6I | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| sorting | 875 | CS 61B Lecture 30: Sorting II (video) |  | https://archive.org/details/ucberkeley_webcast_2hTY3t80Qsk | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| sorting | 876 | CS 61B Lecture 32: Sorting III (video) |  | https://archive.org/details/ucberkeley_webcast_Y6LOLpxg6Dc | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| sorting | 877 | CS 61B Lecture 33: Sorting V (video) |  | https://archive.org/details/ucberkeley_webcast_qNMQ4ly43p4 | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| sorting | 878 | CS 61B 2014-04-21: Radix Sort(video) |  | https://archive.org/details/ucberkeley_webcast_pvbBMd-3NoI | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| sorting | 880 | Algorithms Lesson 1: Bubblesort | xoaxdotnet | https://www.youtube.com/watch?v=P00xJgWzz2c&index=1&list=PL89B61F78B552C1AB | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 881 | Algorithms Lesson 7: Analyzing Bubblesort | xoaxdotnet | https://www.youtube.com/watch?v=ni_zk257Nqo&index=7&list=PL89B61F78B552C1AB | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 882 | Lecture 3: Insertion Sort, Merge Sort | MIT OpenCourseWare | https://www.youtube.com/watch?v=Kg4bqzAqRBM&index=3&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| sorting | 883 | Algorithms Lesson 2: Insertion Sort | xoaxdotnet | https://www.youtube.com/watch?v=c4BRHC7kTaQ&index=2&list=PL89B61F78B552C1AB | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 884 | Algorithms Lesson 3: Merge Sort | xoaxdotnet | https://www.youtube.com/watch?v=GCae1WNvnZM&index=3&list=PL89B61F78B552C1AB | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 885 | Algorithms Lesson 4: Quicksort | xoaxdotnet | https://www.youtube.com/watch?v=y_G9BkAm6B8&index=4&list=PL89B61F78B552C1AB | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 886 | Algorithms Lesson 8: Selection Sort | xoaxdotnet | https://www.youtube.com/watch?v=6nDMgr0-Yyo&index=8&list=PL89B61F78B552C1AB | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 889 | Using output array (C) |  | https://www.cs.yale.edu/homes/aspnes/classes/223/examples/sorting/mergesort.c | unclear (host blocked) | link-only | Aspnes CS223 notes/code; www.cs.yale.edu refused by proxy |
| sorting | 890 | Using output array (Python) |  | https://github.com/jwasham/practice-python/blob/master/merge_sort/merge_sort.py | no licence | link-only | jwasham/practice-* repos have no LICENSE file (checked main/master) |
| sorting | 891 | In-place (C++) |  | https://github.com/jwasham/practice-cpp/blob/master/merge_sort/merge_sort.cc | no licence | link-only | jwasham/practice-* repos have no LICENSE file (checked main/master) |
| sorting | 893 | Implementation (C) |  | https://www.cs.yale.edu/homes/aspnes/classes/223/examples/randomization/quick.c | unclear (host blocked) | link-only | Aspnes CS223 notes/code; www.cs.yale.edu refused by proxy |
| sorting | 894 | Implementation (C) |  | https://github.com/jwasham/practice-c/blob/master/quick_sort/quick_sort.c | no licence | link-only | jwasham/practice-* repos have no LICENSE file (checked main/master) |
| sorting | 895 | Implementation (Python) |  | https://github.com/jwasham/practice-python/blob/master/quick_sort/quick_sort.py | no licence | link-only | jwasham/practice-* repos have no LICENSE file (checked main/master) |
| sorting | 898 | Quick sort in 4 minutes | Michael Sambol | https://youtu.be/Hoixgm4-P4M | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 899 | Heap sort in 4 minutes | Michael Sambol | https://youtu.be/2DmK_H7IdTo | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 900 | Merge sort in 3 minutes | Michael Sambol | https://youtu.be/4VqmGXwpLqc | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 901 | Bubble sort in 2 minutes | Michael Sambol | https://youtu.be/xli_FI7CuzA | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 902 | Selection sort in 3 minutes | Michael Sambol | https://youtu.be/g-PGLbMth_g | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 903 | Insertion sort in 2 minutes | Michael Sambol | https://youtu.be/JU767SDMDvA | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 912 | Sedgewick - Radix Sorts (6 videos) |  | https://www.coursera.org/learn/algorithms-part2/home/week/3 | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 913 | 1. Strings in Java |  | https://www.coursera.org/learn/algorithms-part2/lecture/vGHvb/strings-in-java | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 914 | 2. Key Indexed Counting |  | https://www.coursera.org/lecture/algorithms-part2/key-indexed-counting-2pi1Z | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 915 | 3. Least Significant Digit First String Radix Sort |  | https://www.coursera.org/learn/algorithms-part2/lecture/c1U7L/lsd-radix-sort | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 916 | 4. Most Significant Digit First String Radix Sort |  | https://www.coursera.org/learn/algorithms-part2/lecture/gFxwG/msd-radix-sort | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 917 | 5. 3 Way Radix Quicksort |  | https://www.coursera.org/lecture/algorithms-part2/3-way-radix-quicksort-crkd5 | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 918 | 6. Suffix Arrays |  | https://www.coursera.org/learn/algorithms-part2/lecture/TH18W/suffix-arrays | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| sorting | 919 | Radix Sort |  | https://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#radixSort | unclear (host blocked) | link-only | Aspnes CS223 notes/code; www.cs.yale.edu refused by proxy |
| sorting | 920 | Radix Sort Tutorial | TechRetox | https://www.youtube.com/watch?v=xhr26ia4k38 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| sorting | 921 | Lecture 7: Counting Sort, Radix Sort, Lower Bounds for Sorting | MIT OpenCourseWare | https://www.youtube.com/watch?v=Nz1KZXbghj8&index=7&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| sorting | 922 | 6. Randomization: Matrix Multiply, Quicksort | MIT OpenCourseWare | https://www.youtube.com/watch?v=cNB2lADK3_s&index=8&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| sorting | 923 | 14. Sorting in Linear Time | MIT OpenCourseWare | https://www.youtube.com/watch?v=pOKy3RZbSws&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf&index=14 | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| sorting | 925 | 15 Sorting Algorithms in 6 Minutes | Timo Bingmann | https://www.youtube.com/watch?v=kPRA0W1kECg | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| graphs | 945 | 9. Breadth-First Search | MIT OpenCourseWare | https://www.youtube.com/watch?v=oFVYVzlvk9c&t=14s&ab_channel=MITOpenCourseWare | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| graphs | 946 | 10. Depth-First Search | MIT OpenCourseWare | https://www.youtube.com/watch?v=IBfWDYSffUU&t=32s&ab_channel=MITOpenCourseWare | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| graphs | 949 | CSE 373 -- Lecture 10, Fall 2020 | Steven Skiena | https://www.youtube.com/watch?v=Sjk0xqWWPCc&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=10 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| graphs | 950 | CSE 373 -- Lecture 11, Fall 2020 | Steven Skiena | https://www.youtube.com/watch?v=ZTwjXj81NVY&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=11 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| graphs | 951 | CSE 373 -- Lecture 12, Fall 2020 | Steven Skiena | https://www.youtube.com/watch?v=KyordYB3BOs&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=12 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| graphs | 952 | CSE 373 -- Lecture 13, Fall 2020 | Steven Skiena | https://www.youtube.com/watch?v=oolm2VnJUKw&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=13 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| graphs | 953 | CSE 373 -- Lecture 14, Fall 2020 | Steven Skiena | https://www.youtube.com/watch?v=RktgPx0MarY&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=14 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| graphs | 954 | CSE 373 - Lecture 15, Fall 2020 | Steven Skiena | https://www.youtube.com/watch?v=MUe5DXRhyAo&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=15 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| graphs | 958 | Lecture 15: Single-Source Shortest Paths Problem | MIT OpenCourseWare | https://www.youtube.com/watch?v=Aa2sqUhIn-E&index=15&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| graphs | 959 | 13. Dijkstra | MIT OpenCourseWare | https://www.youtube.com/watch?v=NSHizBK9JD8&t=1731s&ab_channel=MITOpenCourseWare | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| graphs | 960 | 12. Bellman-Ford | MIT OpenCourseWare | https://www.youtube.com/watch?v=f9cVS_URPc0&ab_channel=MITOpenCourseWare | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| graphs | 961 | Lecture 18: Speeding up Dijkstra | MIT OpenCourseWare | https://www.youtube.com/watch?v=CHvQ3q_gJ7E&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=18 | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| graphs | 964 | Graph Algorithms III: Shortest Path - Lecture 8 | Coderisland | https://www.youtube.com/watch?v=DiedsPsMKXc&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=8 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| graphs | 965 | Graph Alg. IV: Intro to geometric algorithms - Lecture 9 | Coderisland | https://www.youtube.com/watch?v=XIAQRlNkJAw&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=9 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| graphs | 966 | CS 61B 2014: Weighted graphs (video) |  | https://archive.org/details/ucberkeley_webcast_zFbq8vOZ_0k | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| graphs | 967 | 12. Greedy Algorithms: Minimum Spanning Tree | MIT OpenCourseWare | https://www.youtube.com/watch?v=tKwnms5iRBU&index=16&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| graphs | 968 | Strongly Connected Components Kosaraju's Algorithm Graph Algorithm | Tushar Roy - Coding Made Simple | https://www.youtube.com/watch?v=RpgcYiky7uw | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| graphs | 973 | Algorithms on Graphs (video) |  | https://www.coursera.org/learn/algorithms-on-graphs/home/welcome | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| recursion | 997 | Lecture 8 / Programming Abstractions (Stanford) | Stanford | https://www.youtube.com/watch?v=gl3emqCuueQ&list=PLFE6E58F856038C69&index=8 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| recursion | 998 | Lecture 9 / Programming Abstractions (Stanford) | Stanford | https://www.youtube.com/watch?v=uFJhEPrbycQ&list=PLFE6E58F856038C69&index=9 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| recursion | 999 | Lecture 10 / Programming Abstractions (Stanford) | Stanford | https://www.youtube.com/watch?v=NdF1QDTRkck&index=10&list=PLFE6E58F856038C69 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| recursion | 1000 | Lecture 11 / Programming Abstractions (Stanford) | Stanford | https://www.youtube.com/watch?v=p-gpaIGRCQI&list=PLFE6E58F856038C69&index=11 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| recursion | 1003 | What Is Tail Recursion Why Is It So Bad? |  | https://www.quora.com/What-is-tail-recursion-Why-is-it-so-bad | no licence stated / not fetched | link-only | third-party site (www.quora.com), not on allowlist |
| recursion | 1004 | Tail Recursion (video) |  | https://www.coursera.org/lecture/programming-languages/tail-recursion-YZic1 | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| recursion | 1005 | 5 Simple Steps for Solving Any Recursive Problem | Reducible | https://youtu.be/ngCos392W4w | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| recursion | 1007 | Java |  | https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning | all rights reserved (LeetCode terms) | link-only | problem/discussion page |
| recursion | 1008 | Python |  | https://leetcode.com/problems/combination-sum/discuss/429538/General-Backtracking-questions-solutions-in-Python-for-reference-%3A | all rights reserved (LeetCode terms) | link-only | problem/discussion page |
| dp | 1015 | CSE 373 -- Lecture 18, Fall 2020 | Steven Skiena | https://www.youtube.com/watch?v=wAA0AMfcJHQ&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=18 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| dp | 1016 | CSE 373 -- Lecture 19, Fall 2020 | Steven Skiena | https://www.youtube.com/watch?v=T3A4jlHlhtA&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=19 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| dp | 1017 | CSE 373 -- Lecture 20, Fall 2020 | Steven Skiena | https://www.youtube.com/watch?v=iPnPVcZmRbE&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=20 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| dp | 1018 | CSE 373 -- Lecture 21, Fall 2020 | Steven Skiena | https://www.youtube.com/watch?v=2xPE4Wq8coQ&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=21 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| dp | 1019 | CSE 373 -- Lecture 22, Fall 2020 | Steven Skiena | https://www.youtube.com/watch?v=Yh3RzqQGsyI&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=22 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| dp | 1020 | Geometric Algorithms: Graham & Jarvis - Lecture 10 | Coderisland | https://youtu.be/J5aJEcOr6Eo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3558 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| dp | 1021 | Dynamic Programming I - Lecture 11 | Coderisland | https://www.youtube.com/watch?v=0EzHjQ_SOeU&index=11&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| dp | 1022 | Dynamic programming II - Lecture 12 | Coderisland | https://www.youtube.com/watch?v=v1qiRwuJU7g&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=12 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| dp | 1024 | Dynamic Programming | Tushar Roy - Coding Made Simple | https://www.youtube.com/playlist?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| dp | 1026 | Dynamic Programming |  | https://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#dynamicProgramming | unclear (host blocked) | link-only | Aspnes CS223 notes/code; www.cs.yale.edu refused by proxy |
| dp | 1028 | The RNA secondary structure problem (video) |  | https://www.coursera.org/learn/algorithmic-thinking-2/lecture/80RrW/the-rna-secondary-structure-problem | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| dp | 1029 | A dynamic programming algorithm (video) |  | https://www.coursera.org/lecture/algorithmic-thinking-2/a-dynamic-programming-algorithm-PSonq | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| dp | 1030 | Illustrating the DP algorithm (video) |  | https://www.coursera.org/lecture/algorithmic-thinking-2/illustrating-the-dp-algorithm-oUEK2 | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| dp | 1031 | Running time of the DP algorithm (video) |  | https://www.coursera.org/learn/algorithmic-thinking-2/lecture/nfK2r/running-time-of-the-dp-algorithm | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| dp | 1032 | DP vs. recursive implementation (video) |  | https://www.coursera.org/learn/algorithmic-thinking-2/lecture/M999a/dp-vs-recursive-implementation | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| dp | 1033 | Global pairwise sequence alignment (video) |  | https://www.coursera.org/lecture/algorithmic-thinking-2/global-pairwise-sequence-alignment-UZ7o6 | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| dp | 1034 | Local pairwise sequence alignment (video) |  | https://www.coursera.org/learn/algorithmic-thinking-2/lecture/WnNau/local-pairwise-sequence-alignment | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| tries | 1177 | Sedgewick - Tries (3 videos) |  | https://www.coursera.org/learn/algorithms-part2/home/week/4 | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| tries | 1178 | 1. R Way Tries |  | https://www.coursera.org/learn/algorithms-part2/lecture/CPVdr/r-way-tries | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| tries | 1179 | 2. Ternary Search Tries |  | https://www.coursera.org/learn/algorithms-part2/lecture/yQM8K/ternary-search-tries | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| tries | 1180 | 3. Character Based Operations |  | https://www.coursera.org/learn/algorithms-part2/lecture/jwNmV/character-based-operations | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| tries | 1181 | Notes on Data Structures and Programming Techniques |  | https://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#Tries | unclear (host blocked) | link-only | Aspnes CS223 notes/code; www.cs.yale.edu refused by proxy |
| tries | 1183 | Introduction To Tries (video) |  | https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/08Xyf/core-introduction-to-tries | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| tries | 1184 | Performance Of Tries (video) |  | https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/PvlZW/core-performance-of-tries | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| tries | 1185 | Implementing A Trie (video) |  | https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/DFvd3/core-implementing-a-trie | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| tries | 1186 | The Trie: A Neglected Data Structure |  | https://www.toptal.com/java/the-trie-a-neglected-data-structure | no licence stated / not fetched | link-only | third-party site (www.toptal.com), not on allowlist |
| balanced-trees | 1700 | Self-balancing binary search tree |  | https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree | CC BY-SA 4.0 | pass | fetched into sources/_cache/wikipedia/ where in the topic list |
| balanced-trees | 1709 | Lecture 6: AVL Trees, AVL Sort | MIT OpenCourseWare | https://www.youtube.com/watch?v=FNeL18KsWPc&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=6 | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| balanced-trees | 1710 | AVL Trees (video) |  | https://www.coursera.org/learn/data-structures/lecture/Qq5E0/avl-trees | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| balanced-trees | 1711 | AVL Tree Implementation (video) |  | https://www.coursera.org/learn/data-structures/lecture/PKEBC/avl-tree-implementation | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| balanced-trees | 1712 | Split And Merge |  | https://www.coursera.org/learn/data-structures/lecture/22BgE/split-and-merge | all rights reserved (Coursera terms; not fetched) | link-only | course video behind Coursera terms; host not on allowlist |
| balanced-trees | 1720 | CS 61B: Splay Trees (video) |  | https://archive.org/details/ucberkeley_webcast_G5QIXywcJlY | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| balanced-trees | 1723 | Lecture 04, 09/13: Splay Trees | Karger Skoltech | https://www.youtube.com/watch?v=QnPl_Y6EqMo | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| balanced-trees | 1735 | Algorithms - Searching & Data Structures - Lecture 4 | Coderisland | https://youtu.be/1W3x0f_RmUo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3871 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| balanced-trees | 1736 | Algorithms - Red-Black Trees - Lecture 5 | Coderisland | https://www.youtube.com/watch?v=hm2GHwyKF1o&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=5 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| balanced-trees | 1737 | Red-Black Tree |  | https://en.wikipedia.org/wiki/Red%E2%80%93black_tree | CC BY-SA 4.0 | pass | fetched into sources/_cache/wikipedia/ where in the topic list |
| balanced-trees | 1738 | An Introduction To Binary Search And Red Black Tree |  | https://www.topcoder.com/thrive/articles/An%20Introduction%20to%20Binary%20Search%20and%20Red-Black%20Trees | all rights reserved (Topcoder site) | link-only | Topcoder tutorial article; host not allowlisted |
| balanced-trees | 1745 | 23-Tree Intuition and Definition | David Taylor | https://www.youtube.com/watch?v=C3SsdUqasD4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=2 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| balanced-trees | 1746 | Binary View of 23-Tree | David Taylor | https://www.youtube.com/watch?v=iYvBtGKsqSg&index=3&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| balanced-trees | 1747 | R2. 2-3 Trees and B-Trees | MIT OpenCourseWare | https://www.youtube.com/watch?v=TOb1tuEZ2X4&index=5&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
| balanced-trees | 1755 | CS 61B Lecture 26: Balanced Search Trees (video) |  | https://archive.org/details/ucberkeley_webcast_zqrqYXkth6Q | unclear (host blocked) | link-only | UC Berkeley webcast on archive.org; archive.org refused by proxy (403) |
| balanced-trees | 1756 | Bottom Up 234-Trees | David Taylor | https://www.youtube.com/watch?v=DQdMYevEyE4&index=4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| balanced-trees | 1757 | Top Down 234-Trees | David Taylor | https://www.youtube.com/watch?v=2679VQ26Fp4&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=5 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| balanced-trees | 1763 | K-Ary Tree |  | https://en.wikipedia.org/wiki/K-ary_tree | CC BY-SA 4.0 | pass | fetched into sources/_cache/wikipedia/ where in the topic list |
| balanced-trees | 1772 | B-Tree |  | https://en.wikipedia.org/wiki/B-tree | CC BY-SA 4.0 | pass | fetched into sources/_cache/wikipedia/ where in the topic list |
| balanced-trees | 1773 | B-Tree Datastructure |  | http://btechsmartclass.com/data_structures/b-trees.html | no licence stated / not fetched | link-only | third-party site (btechsmartclass.com), not on allowlist |
| balanced-trees | 1774 | Introduction to B-Trees | David Taylor | https://www.youtube.com/watch?v=I22wEC1tTGo&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6&index=6 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| balanced-trees | 1775 | B-Tree Definition and Insertion | David Taylor | https://www.youtube.com/watch?v=s3bCdZGrgpA&index=7&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| balanced-trees | 1776 | B-Tree Deletion | David Taylor | https://www.youtube.com/watch?v=svfnVhJOfMc&index=8&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6 | unclear (YouTube flag not readable) | link-only | YouTube licence flag unreadable: watch pages redirect to a Google bot check; treat as Standard YouTube Licence |
| balanced-trees | 1777 | 7. Memory Hierarchy Models | MIT OpenCourseWare | https://www.youtube.com/watch?v=V3omVLzI0WE&index=7&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf | CC BY-NC-SA 4.0 | link-only | MIT OCW video; OCW terms page states CC BY-NC-SA 4.0 (NC: video/transcript link-only) |
