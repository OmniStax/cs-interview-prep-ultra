# CIU topic order

Coding Interview University (registry id `ciu`, CC BY-SA 4.0), snapshot in `sources/_cache/ciu/README.md`. This is CIU's order of study topics, taken from its body and checked against its table of contents. Locators are GitHub heading slugs. Counts are rows in `inventory/ciu.json` and entries in `inventory/ciu-links.json`.

Not listed: CIU's front matter ("The Study Plan": why and how to use it, language choice, book lists, flashcards, daily plan, coding-practice advice and practice sites). It is advice, not topics, and its links are not in `ciu-links.json`.

## Required (tier `core`)

1. Algorithmic complexity / Big-O / Asymptotic analysis (`ciu:#algorithmic-complexity--big-o--asymptotic-analysis`; 5 concepts, 10 links)
2. Data Structures (`ciu:#data-structures`)
    - Arrays (`ciu:#arrays`; 5 concepts, 5 links)
    - Linked Lists (`ciu:#linked-lists`; 5 concepts, 11 links)
    - Stack (`ciu:#stack`; 1 concept, 2 links)
    - Queue (`ciu:#queue`; 4 concepts, 3 links)
    - Hash table (`ciu:#hash-table`; 7 concepts, 13 links)
3. More Knowledge (`ciu:#more-knowledge`)
    - Binary search (`ciu:#binary-search`; 3 concepts, 5 links)
    - Bitwise operations (`ciu:#bitwise-operations`; 5 concepts, 19 links)
4. Trees (`ciu:#trees`)
    - Trees - Intro (`ciu:#trees---intro`; 3 concepts, 6 links). Covers the ToC's "traversals: preorder, inorder, postorder, BFS, DFS".
    - Binary search trees: BSTs (`ciu:#binary-search-trees-bsts`; 7 concepts, 16 links)
    - Heap / Priority Queue / Binary Heap (`ciu:#heap--priority-queue--binary-heap`; 6 concepts, 14 links)
    - balanced search trees (general concept, not details). ToC entry only: no body section here. The one row for it (`ciu:balanced-bst-idea`, core) is located at the optional `ciu:#balanced-search-trees`.
5. Sorting (`ciu:#sorting`; 11 concepts, 54 links)
    - selection, insertion, heapsort, quicksort, mergesort (ToC sub-items; they are not headings in the body)
    - radix and counting sort: inside this section but marked by CIU "Not required, but I recommended them", so inventoried as stretch
6. Graphs (`ciu:#graphs`; 14 concepts, 22 links)
    - directed, undirected, adjacency matrix, adjacency list, traversals BFS and DFS (ToC sub-items; not headings in the body)
    - the body also asks for Dijkstra, MST, cycle check, topological sort, connected components, SCC and bipartite check
7. Even More Knowledge (`ciu:#even-more-knowledge`)
    - Recursion (`ciu:#recursion`; 3 concepts, 9 links)
    - Dynamic Programming (`ciu:#dynamic-programming`; 4 concepts, 17 links)
    - Design Patterns (`ciu:#design-patterns`; 4 concepts, 4 links)
    - Combinatorics (n choose k) & Probability (`ciu:#combinatorics-n-choose-k--probability`; 3 concepts, 5 links)
    - NP, NP-Complete and Approximation Algorithms (`ciu:#np-np-complete-and-approximation-algorithms`; 5 concepts, 13 links)
    - How computers process a program (`ciu:#how-computers-process-a-program`; 2 concepts, 5 links)
    - Caches (`ciu:#caches`; 2 concepts, 5 links)
    - Processes and Threads (`ciu:#processes-and-threads`; 8 concepts, 14 links)
    - Testing (`ciu:#testing`; 5 concepts, 7 links)
    - String searching & manipulations (`ciu:#string-searching--manipulations`; 5 concepts, 8 links)
    - Tries (`ciu:#tries`; 3 concepts, 12 links)
    - Floating Point Numbers (`ciu:#floating-point-numbers`; 1 concept, 1 link)
    - Unicode (`ciu:#unicode`; 1 concept, 2 links)
    - Endianness (`ciu:#endianness`; 1 concept, 3 links)
    - Networking (`ciu:#networking`; 6 concepts, 12 links)
8. Final Review (`ciu:#final-review`; 5 links). Short review videos only; no concept rows.

**---- CIU: "Everything below this point is optional. It is NOT needed for an entry-level interview." ----**

In both CIU's body and its ToC this line comes after the Getting the Job sections.

## Optional (tier `stretch`)

9. Additional Books (`ciu:#additional-books`; 13 links). Book list; no concept rows.
10. System Design, Scalability, Data Handling (`ciu:#system-design-scalability-data-handling`; 12 concepts, 63 links) (CIU: "if you have 4+ years experience")
11. Additional Learning (`ciu:#additional-learning`)
    - Compilers (`ciu:#compilers`; 2 concepts, 4 links)
    - Emacs and vi(m) (`ciu:#emacs-and-vim`; 1 concept, 15 links)
    - Unix/Linux command line tools (`ciu:#unixlinux-command-line-tools`; 1 concept, 3 links)
    - DevOps (`ciu:#devops`; 1 concept, 1 link). In the body but missing from CIU's ToC.
    - Information theory (`ciu:#information-theory-videos`; 2 concepts, 4 links)
    - Parity & Hamming Code (`ciu:#parity--hamming-code-videos`; 2 concepts, 5 links)
    - Entropy (`ciu:#entropy`; 1 concept, 1 link)
    - Cryptography (`ciu:#cryptography`; 2 concepts, 3 links)
    - Compression (`ciu:#compression`; 3 concepts, 8 links)
    - Computer Security (`ciu:#computer-security`; 4 concepts, 13 links)
    - Garbage collection (`ciu:#garbage-collection`; 1 concept, 3 links)
    - Parallel Programming (`ciu:#parallel-programming`; 1 concept, 2 links)
    - Messaging, Serialization, and Queueing Systems (`ciu:#messaging-serialization-and-queueing-systems`; 4 concepts, 20 links)
    - A* (`ciu:#a`; 1 concept, 2 links)
    - Fast Fourier Transform (`ciu:#fast-fourier-transform`; 2 concepts, 5 links)
    - Bloom Filter (`ciu:#bloom-filter`; 1 concept, 4 links)
    - HyperLogLog (`ciu:#hyperloglog`; 1 concept, 1 link)
    - Locality-Sensitive Hashing (`ciu:#locality-sensitive-hashing`; 1 concept, 1 link)
    - van Emde Boas Trees (`ciu:#van-emde-boas-trees`; 1 concept, 2 links)
    - Augmented Data Structures (`ciu:#augmented-data-structures`; 1 concept, 1 link)
    - Balanced search trees (`ciu:#balanced-search-trees`; 8 concepts, 27 links). Sub-items (bold, not headings): AVL, splay, red/black, 2-3, 2-3-4, N-ary, B-trees.
    - k-D Trees (`ciu:#k-d-trees`; 1 concept, 1 link)
    - Skip lists (`ciu:#skip-lists`; 1 concept, 2 links)
    - Network Flows (`ciu:#network-flows`; 1 concept, 3 links)
    - Disjoint Sets & Union Find (`ciu:#disjoint-sets--union-find`; 2 concepts, 2 links)
    - Math for Fast Processing (`ciu:#math-for-fast-processing`; 2 concepts, 2 links)
    - Treap (`ciu:#treap`; 1 concept, 3 links)
    - Linear Programming (`ciu:#linear-programming-videos`; 1 concept, 4 links)
    - Geometry, Convex hull (`ciu:#geometry-convex-hull-videos`; 1 concept, 3 links)
    - Discrete math (`ciu:#discrete-math`; 1 concept, 3 links)
12. Additional Detail on Some Subjects (`ciu:#additional-detail-on-some-subjects`; 14 concepts, 56 links)
    - bold sub-items, not headings: SOLID, Union-Find, More Dynamic Programming, Advanced Graph Processing, MIT Probability, Simonson approximation algorithms, String Matching, Sorting, NAND to Tetris
    - new material got its own rows here; links that reinforce an earlier topic are counted in that topic's concept rows (their notes say how many sit here)
13. Video Series (`ciu:#video-series`; 26 links). Full lecture series; no concept rows.
14. Computer Science Courses (`ciu:#computer-science-courses`; 2 links). Course directories; no concept rows.
15. Algorithms implementation (`ciu:#algorithms-implementation`; 1 link). Code; no concept rows. In the body but missing from the ToC.
16. Papers (`ciu:#papers`; 17 links). Classic systems papers; no concept rows.

## Getting the Job (appendix)

These sit above the optional line in CIU, between Final Review and the optional banner. They are career advice, not CS concepts, so they have no rows in `ciu.json`; their links are in `ciu-links.json`.

1. Update Your Resume (`ciu:#update-your-resume`; 2 links)
2. Interview Process & General Interview Prep (`ciu:#interview-process--general-interview-prep`; 18 links) (includes prep courses and mock-interview sites)
3. Be thinking of for when the interview comes (`ciu:#be-thinking-of-for-when-the-interview-comes`; 0 links) (CIU's list of behavioural questions to prepare stories for)
4. Have questions for the interviewer (`ciu:#have-questions-for-the-interviewer`; 0 links) (CIU's list of questions to ask)
5. Once You've Got The Job (`ciu:#once-youve-got-the-job`; 0 links) ("Keep learning.")
