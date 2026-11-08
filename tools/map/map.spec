# Concept map spec. Prefixes: c=ciu p=cpa j=jeffe n=jeffe-notes o=ods s=sdp
# C id | title          S id | title [| fold note]
# APPENDIX letter | title | kind  ...  END APPENDIX: the chapters between are an appendix, not numbered book chapters.
# Chapter order in this file is the book order. The '# Part:' comments are old groupings, kept for reading only.
# concept-id = row row ... [:: key=value ;; key=value]

# Part: Foundations (foundations)

C ch-cost | Algorithms and their cost
S what-is-an-algorithm | What an algorithm is
algorithm = j:algorithm
underspecified-algorithm = j:bad-algorithm-underspecified
describing-algorithms = j:describing-algorithms
need-for-efficiency = o:need-for-efficiency
interface-vs-implementation = o:interface-vs-implementation
lattice-multiplication = j:lattice-multiplication
peasant-multiplication = j:peasant-multiplication
S growth-functions | Logarithms, factorials and harmonic numbers
logarithms = o:logarithms
factorials-stirling = o:factorials-stirling
harmonic-numbers = o:harmonic-numbers
S asymptotic-notation | Asymptotic notation
big-o = c:big-o o:big-oh
big-omega-theta = c:big-omega-theta
multivariate-big-o = o:multivariate-big-oh
S analysing-algorithms | Analysing running time and space
word-ram = o:word-ram
complexity-analysis = c:complexity-analysis j:running-time-analysis
running-time-guarantees = o:running-time-guarantees
S amortized-analysis | Amortized analysis
amortized-analysis = c:amortized-analysis n:amortized-cost
aggregate-accounting = n:aggregate-accounting
potential-method = n:potential-method o:potential-method
counter-increment-decrement = n:inc-dec-counter
S counting-expectation | Counting and expected value
counting = c:counting
probability-basics = c:probability-basics n:probability-space
conditional-probability = c:conditional-probability :: tier=core ;; why=linearity-of-expectation (core) rests on it.
linearity-of-expectation = n:linearity-of-expectation o:linearity-of-expectation c:random-variables-expectation :: tier=core ;; why=geometric-expectation and chaining-analysis (both core) rest on it.
indicator-variables = o:indicator-variables
geometric-expectation = o:coin-toss-expectation

C ch-arrays-lists | Arrays and linked lists
S arrays | Arrays and the list interface
array = c:array
pointer-arithmetic = c:pointer-arithmetic
list-interface = o:list-interface
S dynamic-arrays | Dynamic arrays
dynamic-array = c:dynamic-array o:arraystack
array-resize = o:array-resize
dynamic-array-cost = c:dynamic-array-cost o:arraystack-amortized-resize
block-copy = o:fastarraystack
implement-vector = c:implement-vector
S singly-linked-lists | Singly linked lists
singly-linked-list = c:singly-linked-list o:sllist
pointer-to-pointer = c:pointer-to-pointer
implement-linked-list = c:implement-linked-list
linked-list-vs-array = c:linked-list-vs-array o:linked-vs-array
S doubly-linked-lists | Doubly linked lists
doubly-linked-list = c:doubly-linked-list o:dllist
sentinel-node = o:dummy-node
S tortoise-and-hare | Cycles in linked lists: tortoise and hare
floyd-cycle-detection = p:floyd-cycle-detection
cycle-start = p:cycle-start
cycle-start-proof = p:cycle-start-proof

C ch-stacks-queues | Stacks, queues and deques
S stacks | Stacks and bracket matching
stack = c:stack o:stack-interface
balanced-brackets = p:balanced-bracket-sequence
bracket-validation = p:bracket-validation
S queues | Queues and circular buffers
queue = c:queue o:queue-interface
circular-buffer = c:circular-buffer o:circular-array
queue-linked-list = c:queue-linked-list
array-queue = o:arrayqueue c:queue-fixed-array :: note=CIU's fixed-size array queue and ODS's resizing ArrayQueue are one concept (a circular array holding a FIFO queue); ODS adds resizing.
S deques | Deques
deque = o:deque-interface
array-deque = o:arraydeque
dual-array-deque = o:dualarraydeque
S monotonic | Min-stacks and monotonic queues | cpa data_structures/stack_queue_modification is the home article; cpa dynamic_programming/zero_matrix contributes its stack step.
min-stack = p:min-stack
queue-from-two-stacks = p:queue-two-stacks
monotonic-queue-minimum = p:min-queue-monotonic
sliding-window-minimum = p:sliding-window-minimum
nearest-smaller-element = p:nearest-smaller-stack
largest-zero-submatrix = p:largest-zero-submatrix
S expressions | Stack applications: expression evaluation
rpn-evaluation = p:rpn-evaluation
expression-parsing = p:expression-parsing-two-stacks
unary-right-assoc = p:unary-right-assoc
S space-efficient-lists | Space-efficient lists
rootish-array-stack = o:rootisharraystack
rootish-index-math = o:rootish-index-math
sqrt-space-lower-bound = o:sqrt-wasted-space-lower-bound
space-efficient-list = o:selist
selist-spread-gather = o:selist-spread-gather

C ch-recursion | Recursion and induction
S recursion | Recursion and reduction
reduction = j:reduction
recursion = j:recursion c:recursion
tail-recursion = c:tail-recursion
tower-of-hanoi = j:tower-of-hanoi
S exponentiation | Exponentiation by squaring
binary-exponentiation = p:binary-exponentiation j:fast-exponentiation
binary-exp-iterative = p:binary-exp-iterative
modular-exponentiation = p:modular-exponentiation
associative-power = p:associative-power
S induction | Induction and correctness proofs
smallest-counterexample = n:smallest-counterexample
induction = n:induction-axiom
induction-practice = n:induction-practice
structural-induction = n:structural-induction
correctness-proof = j:correctness-proof

C ch-hashing | Hash tables
S sets-and-maps | Sets, maps and the dictionary problem
uset-interface = o:uset-interface
map-interface = o:map-from-uset
hash-table = c:hash-table n:hash-table
S chaining | Hashing with chaining
hashing-with-chaining = c:hashing-with-chaining o:hashing-with-chaining :: note=Split from jeffe-notes 05-hashing.4, whose row is the expected-chain-length analysis (concept chaining-analysis).
table-doubling = c:table-doubling
S open-addressing | Open addressing
open-addressing = c:open-addressing o:open-addressing-linear-probing n:open-addressing
tombstones = o:tombstones
implement-hash-table = c:implement-hash-table s:ood-hash-map :: note=sdp's OOD hash-map notebook is the same exercise as CIU's implementation task.
S hash-families | Hash function families
multiplicative-hashing = o:multiplicative-hashing n:multiplicative-hashing
universal-hashing = n:universal-hashing c:universal-perfect-hashing :: note=CIU's one row covers universal and perfect hashing; split into two concepts, CIU's row treats both.
tabulation-hashing = o:tabulation-hashing
perfect-hashing = n:perfect-hashing c:universal-perfect-hashing
S hash-codes | Hash codes
hash-code-properties = o:hash-code-properties
hash-primitives = o:hash-primitives
hash-compound = o:hash-compound
S hashing-analysis | Analysing hash tables
chaining-analysis = n:chaining :: name=Expected chain length under universal hashing
balls-and-bins = n:balls-and-bins
linear-probing-analysis = o:linear-probing-runs
cuckoo-hashing = n:cuckoo-hashing
S lru-cache | Combining structures: the LRU cache
lru-cache = s:lru-cache c:lru-cache s:ood-lru-cache :: note=sdp's query-cache implementation and its OOD LRU notebook are the same structure CIU asks for under Caches.

C ch-binary-search | Binary search
S binary-search | Binary search in a sorted array
binary-search = c:binary-search p:binary-search
binary-search-invariant = p:binary-search-invariant
lower-upper-bound = p:lower-upper-bound
implement-binary-search = c:implement-binary-search
S binary-search-predicate | Binary search on a predicate and on the answer
binary-search-predicate = p:binary-search-predicate c:binary-search-template
binary-search-on-answer = p:binary-search-on-answer
binary-search-powers-of-two = p:binary-search-powers-of-2
parallel-binary-search = p:parallel-binary-search
S continuous-search | Bisection and ternary search
bisection-method = p:bisection-method
unimodal-function = p:unimodal-function
ternary-search = p:ternary-search
ternary-search-integer = p:ternary-search-integer
golden-section-search = p:golden-section-search

C ch-bits | Bits and data representation
S binary-numbers | Binary numbers and machine words
powers-of-two = c:powers-of-two-words s:powers-of-two :: note=sdp's powers-of-two table (for estimation) and CIU's powers of two are one fact table; it lives here and system design points back to it.
binary-representation = p:binary-representation c:twos-complement
S bitwise-operators | Bitwise operators
bitwise-operators = c:bitwise-operators p:bitwise-operators
shift-operators = p:shift-operators
set-clear-flip-bit = p:set-clear-flip-bit
power-of-two-check = p:power-of-two-check
S bit-tricks | Bit tricks and counting bits
lowest-set-bit-tricks = p:lowest-set-bit-tricks
branch-free-tricks = c:bit-tricks
popcount = c:count-set-bits p:kernighan-popcount
count-bits-up-to-n = p:count-bits-up-to-n
S submasks-gray-codes | Submasks and Gray codes
submask-enumeration = p:submask-enumeration
submasks-three-to-n = p:submasks-3-to-n
gray-code = p:gray-code n:gray-codes
gray-code-formula = p:gray-code-formula
inverse-gray-code = p:inverse-gray-code
gray-code-applications = p:gray-code-applications
S data-representation | Representing numbers and text
floating-point = c:floating-point
endianness = c:endianness
character-encodings = c:character-encodings

# Part: Trees and sorting (trees-sorting)

C ch-bst | Trees and binary search trees
S trees | Trees and binary trees
tree = c:tree
binary-tree = o:binary-tree-terms
binary-tree-recursion = o:binarytree-recursive
S tree-traversals | Tree traversals: depth-first and level-order
tree-dfs-orders = c:tree-dfs-orders o:traversal-orders
nonrecursive-traversal = o:nonrecursive-traversal
tree-bfs = c:tree-bfs o:breadth-first-traversal

S sorted-sets | Sorted sets and the BST property
sset-interface = o:sset-interface
uset-vs-sset = o:uset-vs-sset-choice
bst = c:bst o:bst-property
S bst-search-insert | Search and insertion
bst-search = o:bst-search c:bst-search-insert :: note=CIU joins search and insertion in one row; ODS separates them. Split to ODS's grain, CIU's row treats both.
bst-insert = o:bst-add c:bst-search-insert
bst-min-max-height = c:bst-min-max-height
bst-successor = c:bst-successor
S bst-delete | Deletion, validation and cost
bst-delete = c:bst-delete o:bst-remove
validate-bst = c:validate-bst
implement-bst = c:implement-bst
unbalanced-bst-cost = o:unbalanced-bst-cost
S balance-idea | Keeping a BST balanced
balanced-bst-idea = c:balanced-bst-idea
tree-rotations = o:tree-rotations
build-balanced-from-sorted = o:build-balanced-from-sorted
random-bst = o:random-bst

C ch-heaps | Heaps and priority queues
S priority-queues | Priority queues
priority-queue = c:priority-queue o:priority-queue-interface
apportionment = j:huntington-hill-apportionment
S binary-heaps | Binary heaps
implicit-tree-layout = o:eytzinger
heap-property = o:heap-property
binary-heap = c:binary-heap o:binary-heap
heap-sift = c:heap-sift
S heapify-heapsort | Heapify and heapsort
build-heap = c:build-heap o:bottom-up-heapify
heapsort = c:heapsort o:heap-sort
implement-heap = c:implement-heap
S meldable-heaps | Meldable heaps | cpa data_structures/randomized_heap duplicates ODS's MeldableHeap and is folded here.
random-walk-binary-tree = o:random-walk-binary-tree p:randomized-heap-bound
meldable-heap = o:meldable-heap p:randomized-heap

C ch-sorting | Divide and conquer and sorting
S elementary-sorts | Elementary sorts
comparison-sorting = o:comparison-sorting
sort-stability = c:sort-stability
selection-sort = c:selection-sort
insertion-sort = c:insertion-sort
bubble-sort = c:bubble-sort
S divide-and-conquer | Divide and conquer and recurrences
divide-and-conquer = j:divide-and-conquer
guess-and-confirm = n:guess-and-confirm
recursion-trees = j:recursion-trees n:recursion-tree-method c:recurrences-master-theorem :: name=Recursion trees and the master theorem ;; note=CIU's master-theorem row joins Erickson's recursion-tree method: the master theorem's three cases are read off the recursion tree.
akra-bazzi = n:akra-bazzi
annihilators = n:annihilators
karatsuba = j:karatsuba c:karatsuba
S mergesort | Merge sort
mergesort = j:mergesort c:mergesort o:merge-sort
sorting-linked-lists = c:sorting-linked-lists
S quicksort | Quicksort and partitioning
partition = j:partition
three-way-partition = o:three-way-partition
quicksort = j:quicksort c:quicksort o:quicksort
nuts-and-bolts = n:nuts-and-bolts
quicksort-expected-comparisons = n:quicksort-expected-comparisons o:quicksort-analysis
implement-sorts = c:implement-sorts
S selection | Selection | cpa sequences/k-th (195 words) duplicates quickselect and is folded here.
quickselect = j:quickselect c:quickselect p:quickselect
median-of-medians = j:median-of-medians p:median-of-medians
S sorting-lower-bound | Lower bounds for sorting
decision-tree-model = n:decision-tree-model
information-theoretic-bound = n:information-theoretic-bound
comparison-sort-lower-bound = c:comparison-sort-lower-bound o:sorting-lower-bound n:sorting-lower-bound
sorting-reductions = n:sorting-reductions
S linear-sorts | Counting sort and radix sort
counting-sort = o:counting-sort c:linear-time-sorts :: note=CIU's one row covers counting and radix sort; split, CIU's row treats both.
radix-sort = o:radix-sort c:linear-time-sorts

C ch-balanced | Balanced search trees
S multiway-trees | AVL, 2-3 and 2-4 trees
avl-tree = c:avl-tree
two-three-tree = c:2-3-tree :: tier=core ;; why=two-four-tree (core) rests on it.
two-four-tree = c:2-3-4-tree o:two-four-tree :: tier=core ;; why=two-four-updates, b-tree-structure (core) rest on it.
two-four-updates = o:two-four-updates
S red-black | Red-black trees
red-black-properties = o:red-black-properties
red-black-as-2-4 = o:red-black-as-2-4
left-leaning-red-black = o:left-leaning-red-black
red-black-insert = o:red-black-add
red-black-delete = o:red-black-remove
red-black-tree = c:red-black-tree o:red-black-performance :: name=Red-black tree performance
S treaps | Treaps | cpa data_structures/treap shares this home with ODS and jeffe-notes; its split/merge and implicit-key material is contest-tier.
treap = o:treap c:treap p:treap n:treap
treap-rotations = o:treap-updates n:treap-operations
treap-depth = n:treap-depth
treap-split-merge = p:treap-split-merge
treap-linear-build = p:treap-linear-build
implicit-treap = p:implicit-treap
S amortized-trees | Scapegoat and splay trees
partial-rebuilding = o:partial-rebuilding
global-rebuilding = n:global-rebuilding
scapegoat-tree = o:scapegoat-tree n:scapegoat-tree
scapegoat-amortized = o:scapegoat-amortized
splaying = n:splaying
splay-tree = c:splay-tree n:splay-tree
S skip-lists | Skip lists
skiplist-structure = o:skiplist-structure
skiplist-search-path = o:skiplist-search-path-length
skip-list = c:skip-list n:skip-list o:skiplist-sset
skiplist-list = o:skiplist-list
skiplist-analysis = o:skiplist-analysis
S b-trees | B-trees
external-memory-model = o:external-memory-model
k-ary-tree = c:k-ary-tree :: tier=core ;; why=b-tree (core) rests on it.
b-tree-structure = o:b-tree-structure
b-tree-search = o:b-tree-search
b-tree-insert = o:b-tree-add
b-tree-delete = o:b-tree-remove
b-tree = c:b-tree o:b-tree-performance :: tier=core ;; why=database-indexes (core) rests on it.

C ch-tries | Tries and other search structures
S tries | Tries
trie = c:trie p:trie
trie-operations = c:trie-operations
ternary-search-trie = c:ternary-search-trie
S integer-search | Integer search structures
binary-trie = o:binary-trie
x-fast-trie = o:xfast-trie
y-fast-trie = o:yfast-trie
van-emde-boas = c:van-emde-boas
S augmented-spatial | Augmented and spatial trees
augmented-trees = c:augmented-ds
kd-tree = c:kd-tree

# Part: Graphs (graphs)

C ch-graph-search | Graphs and graph search
S graphs | Graphs and modelling
graph = c:graph j:graph-basics o:graph-definitions
graph-modeling = j:graph-modeling
graph-operations = o:graph-interface
S representations | Adjacency matrices and lists
adjacency-matrix = j:adjacency-matrix o:adjacency-matrix
adjacency-list = j:adjacency-list o:adjacency-lists
graph-representations = c:graph-representations
S whatever-first | Whatever-first search
whatever-first-search = j:whatever-first-search
traversal-variants = j:traversal-variants
S bfs | Breadth-first search
graph-bfs = c:graph-bfs p:bfs o:bfs
bfs-shortest-paths = o:bfs-shortest-paths j:bfs-shortest-paths s:bfs-shortest-path
bfs-path-restore = p:bfs-path-restore
bfs-applications = p:bfs-applications
S dfs | Depth-first search
graph-dfs = c:graph-dfs p:dfs o:dfs j:dfs
iterative-dfs = p:iterative-dfs o:dfs-iterative
implement-bfs-dfs = c:implement-bfs-dfs
S components | Components, flood fill and bipartiteness | cpa graph/search-for-connected-components (327 words, mostly BFS/DFS applications) and graph/bipartite-check (264 words) are thin and folded into this home.
traversal-cost = o:traversal-cost-reachable
connected-components = c:connected-components p:connected-components j:counting-components
flood-fill = j:flood-fill
bipartite-check = c:bipartite-check p:bipartite-check

C ch-dfs-structure | Depth-first structure
S dfs-clocks | DFS clocks and edge classification
dfs-clocks = p:dfs-entry-exit-times j:pre-postorder
edge-classification = p:dfs-edge-classification j:edge-classification
S topological-order | Cycles and topological order | cpa graph/finding-cycle (292 words) is folded into this home.
cycle-detection = c:cycle-detection j:cycle-detection p:cycle-detection-dfs
topological-order = p:topological-order
topological-sort = c:topological-sort p:topological-sort j:topological-sort
S bridges | Bridges and articulation points | cpa graph/cutpoints shares the low-link method of graph/bridge-searching; both live here.
low-link = p:low-link
bridge = p:bridge
bridge-finding = p:bridge-finding
articulation-point = p:articulation-point-def
articulation-point-finding = p:articulation-point
S scc | Strongly connected components
scc = p:scc j:strong-components
kosaraju = c:strongly-connected-components p:kosaraju j:kosaraju-sharir
tarjan-scc = p:tarjan-scc j:tarjan-scc
condensation = p:condensation-build
S euler-paths | Eulerian paths
euler-path-existence = p:euler-path-existence
hierholzer = p:hierholzer

C ch-shortest-paths | Shortest paths
S sssp | Shortest-path problems and relaxation
sssp = p:sssp j:shortest-path-tree
edge-relaxation = p:edge-relaxation
ford-relaxation = j:ford-relaxation
negative-edges = j:negative-edges
S dijkstra | Dijkstra's algorithm and A* | cpa graph/dijkstra_sparse (the heap/set implementation) is folded into the Dijkstra home.
dijkstra = c:dijkstra p:dijkstra j:dijkstra
dijkstra-heap = p:dijkstra-heap
a-star = c:a-star
S bellman-ford | Bellman-Ford and negative cycles
bellman-ford = c:bellman-ford p:bellman-ford j:bellman-ford
bellman-ford-negative-cycle = p:bellman-ford-negative-cycle
spfa = p:spfa j:moore-queue :: note=Moore's queue-based Bellman-Ford (jeffe) is the algorithm cp-algorithms calls SPFA.
S small-weights | Shortest paths with small weights
zero-one-bfs = p:zero-one-bfs
dial-algorithm = p:dial-algorithm
desopo-pape = p:desopo-pape

C ch-mst | Disjoint sets and minimum spanning trees
S union-find | Disjoint sets
union-find = c:union-find p:dsu n:disjoint-set-adt :: tier=core ;; why=kruskal (core) rests on it; ruling of 2026-11-08.
shallow-threaded-trees = n:shallow-threaded-trees
dsu-connectivity = p:dsu-connectivity
S dsu-heuristics | Union by rank and path compression
union-by-rank = p:dsu-union-by-rank c:union-find-optimisations :: note=CIU's one row covers both heuristics; split, CIU's row treats both.
path-compression = p:dsu-path-compression n:path-compression c:union-find-optimisations
inverse-ackermann = p:dsu-inverse-ackermann n:inverse-ackermann
S mst | Minimum spanning trees and safe edges
mst = p:mst
mst-unique = j:mst-unique
mst-properties = p:mst-properties
generic-mst = j:generic-mst
S mst-algorithms | Prim, Kruskal and Boruvka | cpa graph/mst_kruskal_with_dsu (215 words) duplicates mst_kruskal's improved implementation and is folded into Kruskal.
prim = c:mst-prim p:prim j:prim
kruskal = c:mst-kruskal p:kruskal p:kruskal-dsu j:kruskal
boruvka = j:boruvka

# Part: Paradigms (paradigms)

C ch-backtracking | Backtracking
S backtracking-pattern | The backtracking pattern
backtracking = j:backtracking-pattern c:backtracking
n-queens = j:n-queens
game-trees = j:game-trees
S subset-sum-segmentation | Subset sum and text segmentation
subset-sum-backtracking = j:subset-sum-backtracking
text-segmentation = j:text-segmentation
index-formulation = j:index-formulation
S recursive-formulations | Recursive formulations of optimisation problems
lis-backtracking = j:lis-backtracking
obst-recurrence = j:obst-recurrence

C ch-dp | Dynamic programming
S dp-idea | Memoization and tabulation
overlapping-subproblems = p:dp-overlapping-subproblems c:dynamic-programming :: name=Dynamic programming: overlapping subproblems
memoization = j:memoization p:memoization
bottom-up-dp = p:bottom-up-dp j:dp-fill-deliberately
dp-smart-recursion = j:dp-pattern
dp-recognition = c:dp-recognition
classic-dp-problems = p:classic-dp-problems c:dp-classics
S fibonacci | Fibonacci numbers: from recursion to logarithmic time
fibonacci-numbers = p:fibonacci-definition
fibonacci-linear = p:fibonacci-iterative
fibonacci-matrix = p:fibonacci-matrix j:fast-fibonacci
S dp-sequences | Text segmentation and longest increasing subsequence
text-segmentation-dp = j:text-segmentation-dp
lis-dp = j:lis-dp p:lis-quadratic
dp-reconstruction = p:dp-reconstruction
lis-nlogn = p:lis-nlogn
lis-variants = p:lis-variants
S max-subarray | Maximum subarray
max-subarray-problem = p:max-subarray-problem
max-subarray-prefix-min = p:max-subarray-prefix-min
kadane = p:kadane
max-submatrix = p:max-submatrix
max-average-subarray = p:max-average-subarray
S knapsack | Subset sum and knapsack
subset-sum-dp = j:subset-sum-dp
knapsack-01 = p:knapsack-01
knapsack-1d-order = p:knapsack-1d-order
knapsack-unbounded = p:knapsack-complete
knapsack-bounded-binary = p:knapsack-multiple-binary
knapsack-monotone-queue = p:knapsack-monotone-queue
S string-dp | Edit distance and longest common subsequence
edit-distance = j:edit-distance c:edit-distance
longest-common-subsequence = p:classic-dp-problems :: name=Longest common subsequence ;; kind=result ;; stmt=The longest common subsequence of strings a and b satisfies L[i][j] = L[i-1][j-1] + 1 when a_i = b_j and max(L[i-1][j], L[i][j-1]) otherwise, so a table over prefix pairs gives it in O(nm) time. ;; tier=core ;; aliases=LCS ;; note=Bridge concept split out of cpa's classic-DP table, which names LCS (alias) but has no article; the statement is the map's own. Prose gap: no open source teaches LCS as a section (jeffe-notes D-faster-dynprog mentions it, NC).
rna-secondary-structure = c:rna-secondary-structure
S dp-trees | DP on trees and optimal binary search trees
dp-on-trees = j:dp-on-trees
obst-dp = j:obst-dp

C ch-graph-dp | Dynamic programming on graphs
S dag-dp | DP in directed acyclic graphs
dag-dp = j:dag-dp
dag-shortest-paths = j:dag-shortest-paths
S apsp-sssp | All-pairs shortest paths from single-source runs
apsp-problem = j:apsp-problem
apsp-repeated-sssp = j:apsp-repeated-sssp
reweighting = j:reweighting
johnson = j:johnson
S floyd-warshall | Floyd-Warshall | cpa graph/finding-negative-cycle-in-graph largely duplicates the negative-cycle parts of bellman_ford and all-pair-shortest-path-floyd-warshall and is folded here.
floyd-warshall = p:floyd-warshall j:floyd-warshall c:apsp-dp :: note=CIU's APSP-by-DP row names Floyd-Warshall and matrix-style DPs; it treats both floyd-warshall and apsp-dp. ;; tier=core ;; why=floyd-warshall-path (core) rests on it.
floyd-warshall-path = p:floyd-warshall-path
floyd-warshall-negative = p:floyd-warshall-negative
negative-cycle-finding = p:negative-cycle-any
S path-length-dp | Path-length DP and matrix products
apsp-dp = j:apsp-dp c:apsp-dp
min-plus-product = j:min-plus-product p:min-plus-matrix-power
paths-fixed-length-count = p:paths-fixed-length-count p:paths-length-k-matrix :: note=cpa teaches this twice (graph/fixed_length_paths and algebra/binary-exp#counting paths); joined.

C ch-greedy | Greedy algorithms
S greedy-idea | Greedy choices and exchange arguments
greed-is-stupid = j:greed-is-stupid
exchange-argument = j:exchange-argument
tape-storage = j:tape-storage
interval-scheduling = j:interval-scheduling
stable-matching = j:stable-matching
S huffman | Huffman codes
prefix-free-code = j:prefix-free-code
huffman = j:huffman c:huffman
S scheduling | Greedy scheduling and matroids | cpa schedules/schedule_one_machine and schedule_two_machines are contest-tier and share this home with jeffe-notes E-matroids.
deadline-scheduling-greedy = p:deadline-scheduling-greedy
matroid = n:matroid
scheduling-deadlines = n:scheduling-deadlines
exchange-argument-scheduling = p:exchange-argument-scheduling
exponential-penalty-scheduling = p:exponential-penalty-scheduling
livshits-kladov = p:livshits-kladov
johnson-rule = p:johnson-rule

C ch-strings | String searching
S substring-search | Substring search: brute force and Boyer-Moore
substring-search-brute-force = c:substring-search-brute-force n:brute-force-matching
boyer-moore = c:boyer-moore
S string-hashing | String hashing and Rabin-Karp | cpa string/rabin-karp (176 words) is a thin application of string/string-hashing and is folded here.
polynomial-hash = p:polynomial-hash o:polynomial-hash c:rolling-hash :: note=ODS's polynomial hash, cpa's polynomial rolling hash and CIU's rolling hash are one concept. ;; tier=core ;; why=prefix-hash-substring and rabin-karp (core) rest on it.
prefix-hash-substring = p:prefix-hash-substring
hash-group-duplicates = p:hash-group-duplicates
hash-collisions = p:hash-collisions
hash-distinct-substrings = p:hash-distinct-substrings
rabin-karp = c:rabin-karp p:rabin-karp n:karp-rabin
S kmp | Prefix function and Knuth-Morris-Pratt
string-matching-automaton = n:string-matching-automaton
prefix-function = p:prefix-function
prefix-function-linear = p:prefix-function-linear n:failure-function
kmp = c:kmp p:kmp
string-period = p:string-period
prefix-occurrence-counts = p:prefix-occurrence-counts
kmp-automaton = p:prefix-automaton
distinct-substrings-incremental = p:distinct-substrings-incremental
S z-function | The Z-function
z-function = p:z-function
z-function-linear = p:z-function-linear
z-pattern-search = p:z-pattern-search
S suffix-arrays | Suffix arrays
suffix-array = c:suffix-array p:suffix-array
suffix-array-doubling = p:suffix-array-doubling
suffix-array-search = p:suffix-array-search

C ch-randomized | Probability and randomized algorithms
S distributions | Distributions at work
common-distributions = n:common-distributions
unbiasing-coins = n:unbiasing-coins
coupon-collector = n:coupon-collector
S randomized-algorithms | Las Vegas and Monte Carlo algorithms
las-vegas-monte-carlo = n:las-vegas-monte-carlo
random-permutation = n:random-permutation
S tail-bounds | Tail bounds
markov-inequality = n:markov-inequality
chebyshev-inequality = n:chebyshev-inequality
chernoff-bound = n:chernoff-bound c:large-deviations
treap-depth-whp = n:treap-depth-whp
S markov-chains | Markov chains and random walks
markov-chains = c:markov-chains
random-walks = c:random-walks
markov-text-generation = c:markov-text-generation

C ch-intractability | Lower bounds and intractability
S adversary | Adversary arguments
max-lower-bound = n:max-lower-bound
adversary-argument = n:adversary-argument
min-max-lower-bound = n:min-max-lower-bound
evasive-properties = n:evasive-properties
S p-np | P, NP and NP-hardness
circuit-sat = j:circuit-sat
p-np = c:p-np j:p-np
np-hard = j:np-hard
cook-levin = j:cook-levin
beyond-np = j:beyond-np
S np-reductions | NP-hardness by reduction
poly-time-reductions = c:reductions
np-hardness-proof-pattern = j:np-hardness-proof-pattern
three-sat = j:three-sat
max-independent-set-np = j:max-independent-set-np
clique-vertex-cover = j:clique-vertex-cover
graph-coloring-np = j:graph-coloring-np
hamiltonian-cycle-np = j:hamiltonian-cycle-np
subset-sum-np = j:subset-sum-np
S recognising-np-hard | Recognising NP-hard problems
recognise-np-hard = c:recognise-npc :: note=Kept apart from Erickson's catalog (np-hard-catalog): recognising a famous problem in disguise needs P and NP, not the reduction machinery the catalog rests on.
np-hard-catalog = j:np-hard-catalog
choosing-reduction-source = j:choosing-reduction-source
draughts-np = j:draughts-np
S approximation | Approximation algorithms
approximation-algorithms = n:approximation-ratio c:approximation-algorithms
load-balancing = n:load-balancing
vertex-cover-approx = n:vertex-cover-approx
set-cover-greedy = n:set-cover-greedy
tsp-approx = n:tsp-approx
k-center = n:k-center
subset-sum-fptas = n:subset-sum-fptas
S exponential-algorithms | Exact exponential and parameterised algorithms
fixed-parameter-algorithms = c:fixed-parameter-algorithms
faster-3sat = n:faster-3sat
faster-mis = n:faster-mis

# Part: Computer systems (systems)
APPENDIX A | Computer systems | links

C ch-os | Computers and operating systems
S cpu-memory | CPU, memory and caches
cpu-components = c:cpu-components
instruction-cycle = c:instruction-cycle
memory-hierarchy = c:memory-hierarchy
computer-from-gates = c:computer-from-gates
S compilers-runtimes | Compilers and runtimes
compilers = c:compilers
compiler-optimization = c:compiler-optimization
garbage-collection = c:garbage-collection
S processes-threads | Processes, threads and context switches
process-vs-thread = c:process-vs-thread
context-switching = c:context-switching
S virtual-memory | Virtual memory
virtual-memory = c:virtual-memory
fork-cow = c:fork-cow
S concurrency | Concurrency and synchronisation
sync-primitives = c:sync-primitives
deadlock-livelock = c:deadlock-livelock
python-concurrency = c:python-concurrency
parallel-programming = c:parallel-programming

C ch-networking | Networking
S network-layers | Network layers and addressing
network-layers = c:network-layers
cidr = c:cidr
S transport | TCP and UDP
tcp = s:tcp
udp = s:udp
tcp-vs-udp = c:tcp-vs-udp
connection-pooling = s:connection-pooling
sockets = c:sockets
S http | HTTP and TLS
http = s:http c:http
http-verbs = s:http-verbs
tls-https = c:tls-https
S rpc-rest | RPC, REST and serialisation
serialization = c:serialization :: tier=core ;; why=rpc (core) rests on it.
rpc = s:rpc c:rpc :: tier=core ;; why=rpc-vs-rest (core) rests on it.
rest = s:rest
rpc-vs-rest = s:rpc-vs-rest
hateoas = s:hateoas

C ch-engineering | Software engineering practice
S testing | Testing
unit-testing = c:unit-testing
mock-objects = c:mock-objects
integration-testing = c:integration-testing
dependency-injection = c:dependency-injection
tdd = c:tdd
S design-patterns | Design patterns and UML
uml = c:uml
creational-patterns = c:creational-patterns
structural-patterns = c:structural-patterns
behavioral-patterns = c:behavioral-patterns
S solid | SOLID principles
solid-srp = c:solid-srp
solid-ocp = c:solid-ocp
solid-lsp = c:solid-lsp
solid-isp = c:solid-isp
solid-dip = c:solid-dip
S ood | Object-oriented design exercises
ood-parking-lot = s:ood-parking-lot
ood-call-center = s:ood-call-center
ood-deck-of-cards = s:ood-deck-of-cards
ood-online-chat = s:ood-online-chat
S developer-tools | Developer tools
vim-emacs = c:vim-emacs
unix-cli = c:unix-cli

C ch-information-security | Information, coding and security
S information | Information and entropy
information-theory = c:information-theory :: tier=core ;; why=crypto-hash (core) rests on it.
entropy = c:entropy
S error-detection | Parity and Hamming codes
parity = c:parity
hamming-code = c:hamming-code
S compression | Compression
compression = c:compression
lz77 = c:lz77
S cryptography | Cryptography
crypto-hash = c:crypto-hash :: tier=core ;; why=shortlink-generation (core) rests on it.
encryption = c:encryption
S security | Computer security
threat-models = c:threat-models
control-hijacking = c:control-hijacking
web-security = c:web-security
network-security = c:network-security

END APPENDIX

# Part: System design (system-design)

C ch-sd-method | Approaching a system design question
S approach | The four-step approach
interview-approach = s:interview-approach c:sd-process :: tier=core ;; why=requirements-scoping, core-component-design and iterative-scaling (core) rest on it.
requirements-scoping = s:requirements-scoping
core-component-design = s:core-component-design
iterative-scaling = s:iterative-scaling
S estimation | Back-of-the-envelope estimation
latency-numbers = s:latency-numbers
rate-conversion = s:rate-conversion
back-of-envelope = s:back-of-envelope c:back-of-envelope :: tier=core ;; why=the core worked designs rest on it.
S trade-offs | Performance versus scalability, latency versus throughput
performance-vs-scalability = s:performance-vs-scalability
latency-vs-throughput = s:latency-vs-throughput

C ch-sd-availability | Availability and consistency
S cap | Distributed systems and the CAP theorem
distributed-fallacies = c:distributed-fallacies
cap-theorem = s:cap-theorem c:cap-theorem :: tier=core ;; why=weak, eventual and strong consistency (core) rest on it.
S consistency | Consistency patterns
weak-consistency = s:weak-consistency
eventual-consistency = s:eventual-consistency
strong-consistency = s:strong-consistency
cp-vs-ap = s:cp-vs-ap
consensus = c:consensus
S availability | Availability patterns
active-passive-failover = s:active-passive-failover
active-active-failover = s:active-active-failover
availability-nines = s:availability-nines
availability-composition = s:availability-composition

C ch-sd-web | Scaling the web tier
S dns-cdn | DNS and content delivery networks
dns = s:dns
dns-records = s:dns-records
dns-traffic-routing = s:dns-traffic-routing
cdn = s:cdn
push-vs-pull-cdn = s:push-vs-pull-cdn
S load-balancing | Load balancers and reverse proxies
load-balancer = s:load-balancer
lb-routing-methods = s:lb-routing-methods
l4-vs-l7-lb = s:l4-vs-l7-lb
reverse-proxy = s:reverse-proxy
lb-vs-reverse-proxy = s:lb-vs-reverse-proxy
S horizontal-scaling | Horizontal scaling and stateless servers
horizontal-scaling = s:horizontal-scaling
stateless-servers = s:stateless-servers
scaling-basics = c:scaling-basics :: tier=core ;; why=sharding (core) rests on it.
autoscaling = s:autoscaling
S application-layer | The application layer and microservices
application-layer = s:application-layer
microservices = s:microservices
service-discovery = s:service-discovery
S operations | Object storage, monitoring and security
object-store = s:object-store
static-content-offload = s:static-content-offload
monitoring = s:monitoring
security-basics = s:security-basics
network-hardening = s:network-hardening

C ch-sd-data | Databases
S rdbms | Relational databases
acid = s:acid
db-normalization = c:db-normalization
database-indexes = s:database-indexes
schema-tightening = s:schema-tightening
S replication | Replication
master-slave-replication = s:master-slave-replication
master-master-replication = s:master-master-replication
replication-drawbacks = s:replication-drawbacks
read-write-split = s:read-write-split
S partitioning | Federation, sharding and denormalisation
federation = s:federation
sharding = s:sharding c:sharding :: tier=core ;; why=denormalization, cache-cluster-partitioning and several worked designs (core) rest on it.
denormalization = s:denormalization
sql-tuning = s:sql-tuning
consistent-hashing = c:consistent-hashing
distributed-hash-table = c:distributed-hash-table
data-tiering = s:data-tiering
S nosql | NoSQL stores
nosql-base = s:nosql-base
key-value-store = s:key-value-store
document-store = s:document-store
wide-column-store = s:wide-column-store
graph-database = s:graph-database
nosql-patterns = c:nosql-patterns
sql-vs-nosql = s:sql-vs-nosql

C ch-sd-cache-async | Caching and asynchrony
S caching | Caches and where to put them
caching = s:caching
cache-locations = s:cache-locations
application-cache = s:application-cache
cache-granularity = s:cache-granularity
redis = c:redis
cache-cluster-partitioning = s:cache-cluster-partitioning
S cache-strategies | Cache update strategies
cache-aside = s:cache-aside
write-through = s:write-through
write-behind = s:write-behind
refresh-ahead = s:refresh-ahead
cache-invalidation = s:cache-invalidation
S queues-back-pressure | Message queues and back pressure
asynchronism = s:asynchronism
message-queue = s:message-queue c:message-queues :: tier=core ;; why=back-pressure, fanout-on-write and several worked designs (core) rest on it.
task-queue = s:task-queue
back-pressure = s:back-pressure
S mapreduce | Batch processing with MapReduce
mapreduce-aggregation = s:mapreduce-aggregation
distributed-sort = s:distributed-sort

C ch-sd-cases | Worked designs
S pastebin | Pastebin and Bit.ly
base62 = s:base62
shortlink-generation = s:shortlink-generation
design-pastebin = s:design-pastebin
S twitter | Twitter timeline and search
fanout-on-write = s:fanout-on-write
celebrity-fanout = s:celebrity-fanout
timeline-cache-trimming = s:timeline-cache-trimming
reverse-index = s:reverse-index
search-query-processing = s:search-query-processing
design-twitter = s:design-twitter
S web-crawler | A web crawler
crawl-frontier = s:crawl-frontier
duplicate-detection = s:duplicate-detection
recrawl-policy = s:recrawl-policy
crawler-throughput = s:crawler-throughput
design-web-crawler = s:design-web-crawler
S mint | Mint.com
transaction-categorization = s:transaction-categorization
budget-template = s:budget-template
design-mint = s:design-mint
S social-graph | A social graph
sharded-graph-lookup = s:sharded-graph-lookup
distributed-bfs-optimizations = s:distributed-bfs-optimizations
distributed-graph-algorithms = c:distributed-graph-algorithms
design-social-graph = s:design-social-graph
S query-cache | A query cache
design-query-cache = s:design-query-cache
S sales-rank | Sales rank by category
design-sales-rank = s:design-sales-rank
S scaling-aws | Scaling to millions of users on AWS
design-scaling-aws = s:design-scaling-aws

# Part: Beyond the interview (beyond)

C ch-range-queries | Range queries
S sparse-tables | Range minimum and sparse tables | cpa sequences/rmq (361 words) is an index of RMQ approaches and is folded here; its rmq-approaches row sits in the sqrt section, after the structures it compares.
rmq-problem = p:rmq-problem
sparse-table = p:sparse-table
sparse-table-range-sum = p:sparse-table-range-sum
sparse-table-rmq = p:sparse-table-rmq
disjoint-sparse-table = p:disjoint-sparse-table-mention
S fenwick | Fenwick trees
fenwick = p:fenwick
fenwick-sum = p:fenwick-sum
fenwick-linear-build = p:fenwick-linear-build
fenwick-prefix-min = p:fenwick-prefix-min
fenwick-range-update = p:fenwick-range-update
S segment-trees | Segment trees
segment-tree = p:segment-tree
segment-tree-query-update = p:segment-tree-query-update
segment-tree-custom-merge = p:segment-tree-custom-merge
segment-tree-descent = p:segment-tree-descent
S segment-tree-extensions | Segment tree extensions
lazy-propagation = p:lazy-propagation
merge-sort-tree = p:merge-sort-tree
segment-tree-2d = p:segment-tree-2d
persistent-segment-tree = p:persistent-segment-tree
dynamic-segment-tree = p:dynamic-segment-tree
lis-data-structure = p:lis-data-structure
S sqrt-decomposition | Sqrt decomposition | cpa data_structures/sqrt-tree builds on sqrt_decomposition and shares this home.
sqrt-decomposition = p:sqrt-decomposition
mo-algorithm = p:mo-algorithm
sqrt-tree = p:sqrt-tree
sqrt-tree-updates = p:sqrt-tree-updates
rmq-approaches = p:rmq-approaches
S dsu-offline | DSU tricks and offline processing | cpa data_structures/deleting_in_log_n (236 words) is folded here with the DSU applications.
dsu-painting-offline = p:dsu-painting-offline
dsu-parity = p:dsu-parity
arpa-trick = p:arpa-trick
small-to-large = p:small-to-large
rollback-dsu = p:rollback-dsu
offline-deletion = p:offline-deletion
S mex | MEX queries
mex = p:mex
mex-linear = p:mex-linear
mex-with-updates = p:mex-with-updates

C ch-tree-algorithms | Tree algorithms
S lca | Lowest common ancestor
lca = p:lca
lca-euler-tour-rmq = p:lca-euler-tour-rmq
binary-lifting-lca = p:binary-lifting-lca
binary-lifting-dynamic = p:binary-lifting-dynamic
lca-linear-jump-pointers = p:lca-linear-jump-pointers
S linear-lca | Linear-time LCA and RMQ | cpa graph/rmq_linear and graph/lca_tarjan are short companions of lca_farachcoltonbender and share this home.
farach-colton-bender = p:farach-colton-bender
cartesian-tree-rmq = p:cartesian-tree-rmq
tarjan-offline-lca = p:tarjan-offline-lca
S tree-decompositions | Heavy-light and centroid decomposition
heavy-light-decomposition = p:heavy-light-decomposition
hld-path-queries = p:hld-path-queries
centroid = p:centroid
centroid-decomposition = p:centroid-decomposition
tree-edge-painting = p:tree-edge-painting
S pruefer | Prufer codes and counting trees
pruefer-code = p:pruefer-code
pruefer-linear = p:pruefer-linear
cayley-formula = p:cayley-formula
ways-to-connect-graph = p:ways-to-connect-graph

C ch-flows | Network flow and matching
S flow-basics | Flows, cuts and the max-flow min-cut theorem
flow-network = j:flow p:flow-network
st-cut = j:cut
residual-graph = j:residual-graph
max-flow-min-cut = j:maxflow-mincut p:max-flow-min-cut
flow-decomposition = j:flow-decomposition
S augmenting-paths | Augmenting paths: Ford-Fulkerson and Edmonds-Karp
ford-fulkerson = j:ford-fulkerson p:ford-fulkerson c:max-flow
integral-flow = p:integral-flow
edmonds-karp = j:edmonds-karp p:edmonds-karp
S faster-maxflow | Faster maximum flow | cpa graph/push-relabel-faster (168 words) is folded into push-relabel.
dinic = p:dinic
dinic-unit-networks = p:dinic-unit-networks
mpm = p:mpm
preflow-labeling = p:preflow-labeling
push-relabel = p:push-relabel
push-relabel-highest = p:push-relabel-highest
maxflow-survey = j:maxflow-further :: name=Faster maximum-flow algorithms (survey)
S bipartite-matching | Bipartite matching
matching-definitions = p:matching-definitions
berge-lemma = p:berge-lemma
kuhn-matching = p:kuhn-matching
bipartite-matching-flow = j:bipartite-matching
S flow-applications | Reductions to flow
edge-disjoint-paths = j:edge-disjoint-paths
vertex-splitting = j:vertex-splitting
tuple-selection = j:tuple-selection
disjoint-path-cover = j:disjoint-path-cover
baseball-elimination = j:baseball-elimination
project-selection = j:project-selection
S min-cost-flow | Demands and minimum-cost flow
unbalanced-flow = n:unbalanced-flow
pseudoflow = n:pseudoflow
flow-with-demands = p:flow-with-demands
minimal-flow-demands = p:minimal-flow-demands
min-cost-circulation = n:min-cost-circulation
min-cost-flow = p:min-cost-flow n:successive-shortest-paths
reduced-costs = n:reduced-costs
S assignment | The assignment problem | cpa graph/Assignment-problem-min-flow (425 words) overlaps hungarian-algorithm and is folded here.
assignment-problem = p:assignment-problem
hungarian-algorithm = p:hungarian-algorithm
assignment-via-mcf = p:assignment-via-mcf

C ch-advanced-graphs | More graph algorithms
S two-sat | 2-SAT
implication-graph = p:implication-graph
two-sat = p:two-sat
S online-bridges | Online bridges and strong orientation
bridges-online = p:bridges-online
strong-orientation = p:strong-orientation
S connectivity | Edge and vertex connectivity
edge-vertex-connectivity = p:edge-vertex-connectivity
whitney-inequalities = p:whitney-inequalities
connectivity-via-flow = p:connectivity-via-flow
S global-min-cut | Global minimum cut
global-min-cut = n:global-min-cut p:global-min-cut
stoer-wagner = p:stoer-wagner
karger = n:karger
karger-stein = n:karger-stein
S mst-variants | Second-best spanning trees
mst-one-swap = p:mst-one-swap
second-best-mst = p:second-best-mst

C ch-advanced-strings | Advanced string algorithms
S lcp | LCP arrays and substring counting
lcp-array-kasai = p:lcp-array-kasai
sa-distinct-substrings = p:sa-distinct-substrings
S aho-corasick | Aho-Corasick
aho-corasick-automaton = p:aho-corasick-automaton
aho-corasick-matching = p:aho-corasick-matching
aho-corasick-dp = p:aho-corasick-dp
S suffix-automata | Suffix trees and suffix automata | cpa string/suffix-tree-ukkonen (213 words) is a code-only article and is folded here.
suffix-tree-ukkonen = p:suffix-tree-ukkonen
suffix-automaton = p:suffix-automaton
endpos-suffix-links = p:endpos-suffix-links
suffix-automaton-construction = p:suffix-automaton-construction
suffix-automaton-size = p:suffix-automaton-size
suffix-automaton-applications = p:suffix-automaton-applications
S palindromes | Palindromes: Manacher's algorithm
palindrome-radius = p:palindrome-radius
manacher = p:manacher
manacher-parity = p:manacher-parity
S repetitions-lyndon | Repetitions and Lyndon words
repetition = p:repetition
main-lorentz = p:main-lorentz
lyndon-word = p:lyndon-word
duval-algorithm = p:duval-algorithm
smallest-cyclic-shift = p:smallest-cyclic-shift

C ch-advanced-dp | Advanced dynamic programming
S dp-optimizations | Divide-and-conquer and Knuth optimisations
monotone-opt = p:monotone-opt
dc-dp-optimization = p:dc-dp-optimization
quadrangle-inequality = p:quadrangle-inequality
knuth-optimization = p:knuth-optimization n:knuth-monotonicity
smawk = n:smawk
S dp-speedups | Saving space and time
hirschberg = n:hirschberg
sparse-dp = n:sparse-dp
four-russians = n:four-russians
S profile-dp | Profile and bitmask DP
broken-profile-dp = p:broken-profile-dp
bishops-placement-dp = p:bishops-placement-dp
S automata-dp | DP over automata and grammars
dfa-minimization = n:dfa-minimization
nfa-acceptance = n:nfa-acceptance
cyk-parsing = n:cyk-parsing

C ch-sketches | Sketches and probabilistic data structures
S bloom-filters | Bloom filters
bloom-filter = n:bloom-filter c:bloom-filter
S streaming | Streaming sketches
streaming-model = n:streaming-model
count-min-sketch = n:count-min-sketch
hyperloglog = c:hyperloglog
S similarity-hashing | Locality-sensitive hashing
simhash = c:simhash

C ch-number-theory-1 | Number theory: divisibility and primes
S gcd | Greatest common divisors
gcd-definition = p:gcd-definition
euclidean-algorithm = p:euclidean-algorithm
lame-theorem = p:lame-theorem
lcm-via-gcd = p:lcm-via-gcd
binary-gcd = p:binary-gcd
S extended-euclid | Extended Euclid and Diophantine equations
bezout-identity = p:bezout-identity
extended-euclidean = p:extended-euclidean
extended-euclidean-iterative = p:extended-euclidean-iterative
linear-diophantine = p:linear-diophantine
diophantine-solvability = p:diophantine-solvability
diophantine-all-solutions = p:diophantine-all-solutions
diophantine-count-in-range = p:diophantine-count-in-range
diophantine-min-sum = p:diophantine-min-sum
S sieve | The sieve of Eratosthenes
sieve-of-eratosthenes = p:sieve-of-eratosthenes
sieve-complexity = p:sieve-complexity
sieve-till-root = p:sieve-till-root
sieve-odd-only = p:sieve-odd-only
sieve-bit-packing = p:sieve-bit-packing
S segmented-linear-sieve | Segmented and linear sieves | cpa algebra/prime-sieve-linear overlaps sieve-of-eratosthenes#linear-time-modification and shares this home.
segmented-sieve = p:segmented-sieve
primes-in-range = p:primes-in-range
linear-sieve = p:linear-sieve
linear-sieve-proof = p:linear-sieve-proof
least-prime-factor-table = p:least-prime-factor-table
S trial-division | Primality and factorisation by trial division
primality-trial-division = p:primality-trial-division
factorization-trial-division = p:factorization-trial-division
wheel-factorization = p:wheel-factorization
factor-by-precomputed-primes = p:factor-by-precomputed-primes
fermat-factorization = p:fermat-factorization
S divisors | Divisor functions
multiplicative-function = p:multiplicative-function
number-of-divisors = p:number-of-divisors
sum-of-divisors = p:sum-of-divisors
S totient | Euler's totient function
euler-totient = p:euler-totient
totient-formula = p:totient-formula
totient-by-factorization = p:totient-by-factorization
totient-sieve = p:totient-sieve
totient-divisor-sum = p:totient-divisor-sum
S euler-fermat | Euler's and Fermat's theorems
euler-theorem = p:euler-theorem
fermat-little-theorem = p:fermat-little-theorem
generalized-euler-theorem = p:generalized-euler-theorem

C ch-number-theory-2 | Number theory: modular arithmetic
S modular-inverse | Modular inverses
modular-inverse = p:modular-inverse
inverse-by-extended-euclid = p:inverse-by-extended-euclid
inverse-by-fermat = p:inverse-by-fermat
inverse-recurrence-prime = p:inverse-recurrence-prime
batch-inverse = p:batch-inverse
S linear-congruences | Linear congruences
linear-congruence = p:linear-congruence
linear-congruence-solution = p:linear-congruence-solution
linear-congruence-via-diophantine = p:linear-congruence-via-diophantine
S primality-tests | Probabilistic primality and Pollard's methods
fermat-primality-test = p:fermat-primality-test
miller-rabin = p:miller-rabin
pollard-p-minus-1 = p:pollard-p-minus-1
pollard-rho = p:pollard-rho
brent-cycle-finding = p:brent-cycle-finding
S crt | The Chinese remainder theorem
crt = p:crt-statement c:crt
crt-two-moduli = p:crt-two-moduli
crt-inductive = p:crt-inductive
crt-direct-construction = p:crt-direct-construction
crt-non-coprime = p:crt-non-coprime
S garner | Garner's algorithm and residue number systems | cpa algebra/garners-algorithm is summarised by chinese-remainder-theorem#garners-algorithm and big-integer; one home.
mixed-radix = p:mixed-radix
garner-algorithm = p:garner-algorithm
residue-number-system = p:residue-number-system
S factorial-mod-p | Factorials modulo p | cpa algebra/factorial-divisors (256 words) duplicates factorial-modulo#multiplicity-of-p and is folded here.
legendre-formula = p:legendre-formula p:legendre-prime-k :: note=cpa states Legendre's formula twice (factorial-modulo and factorial-divisors); joined.
factorial-power-composite-k = p:factorial-power-composite-k
factorial-mod-p-modified = p:factorial-mod-p-modified
factorial-mod-p-recursion = p:factorial-mod-p-recursion
S discrete-log | Discrete logarithms
discrete-log-problem = p:discrete-log-problem
meet-in-the-middle = p:meet-in-the-middle-idea
baby-step-giant-step = p:baby-step-giant-step
bsgs-hash = p:bsgs-hash
discrete-log-non-coprime = p:discrete-log-non-coprime
S primitive-roots | Primitive roots and discrete roots
primitive-root = p:primitive-root
primitive-root-existence = p:primitive-root-existence
find-primitive-root = p:find-primitive-root
discrete-root = p:discrete-root
discrete-root-all-solutions = p:discrete-root-all-solutions

C ch-number-theory-3 | Number theory: representations and fast arithmetic
S modular-multiplication | Fast modular multiplication
binary-multiplication-mod = p:binary-multiplication-mod
montgomery-space = p:montgomery-space
montgomery-reduction = p:montgomery-reduction
newton-inverse-mod-2k = p:newton-inverse-mod-2k
montgomery-fast-transform = p:montgomery-fast-transform
S exponent-tricks | Powers of permutations, matrices and 2^d | cpa algebra/factoring-exp shares this home with the binary-exp applications.
permutation-power = p:permutation-power
transformation-matrix-power = p:transformation-matrix-power
exp-by-factoring = p:exp-by-factoring
pohlig-hellman-power-of-2 = p:pohlig-hellman-power-of-2
S big-integers | Arbitrary-precision arithmetic
bignum-representation = p:bignum-representation
bignum-add-subtract = p:bignum-add-subtract
bignum-multiply = p:bignum-multiply
bignum-divide-short = p:bignum-divide-short
exact-fractions = p:exact-fractions
factorized-representation = p:factorized-representation
bignum-residues = p:bignum-residues
separate-exponent-float = p:separate-exponent-float
S balanced-ternary | Balanced ternary
balanced-ternary = p:balanced-ternary
balanced-ternary-conversion = p:balanced-ternary-conversion
S fibonacci-identities | Fibonacci identities
fibonacci-identities = p:fibonacci-identities
zeckendorf-fibonacci-coding = p:zeckendorf-fibonacci-coding
binet-formula = p:binet-formula
fibonacci-fast-doubling = p:fibonacci-fast-doubling
pisano-period = p:pisano-period
S continued-fractions | Continued fractions
continued-fraction = p:continued-fraction
continued-fraction-euclid = p:continued-fraction-euclid
convergents = p:convergents
best-rational-approximation = p:best-rational-approximation
calkin-wilf-tree = p:calkin-wilf-tree
linear-fractional-transformation = p:linear-fractional-transformation
S stern-brocot | The Stern-Brocot tree and Farey sequences | cpa algebra/continued-fractions#stern-brocot-tree overlaps others/stern_brocot_tree_farey_sequences; one home.
stern-brocot-tree = p:stern-brocot-tree
stern-brocot-properties = p:stern-brocot-properties
stern-brocot-number-system = p:stern-brocot-number-system
stern-brocot-log-search = p:stern-brocot-log-search
continued-fractions-stern-brocot = p:continued-fractions-stern-brocot
farey-sequence = p:farey-sequence
farey-length = p:farey-length

C ch-combinatorics | Combinatorics
S binomial | Binomial coefficients
binomial-coefficient = p:binomial-coefficient
binomial-formula = p:binomial-formula
binomial-identities = p:binomial-identities
binomial-multiplicative = p:binomial-multiplicative
pascals-triangle = p:pascals-triangle
binomial-mod-prime = p:binomial-mod-prime
binomial-mod-prime-power = p:binomial-mod-prime-power
lucas-theorem = p:lucas-theorem
S catalan | Catalan numbers | cpa combinatorics/bracket_sequences#counting duplicates catalan-numbers' bracket interpretation; the two articles share this home and the next.
catalan-numbers = p:catalan-numbers
catalan-interpretations = p:catalan-interpretations
catalan-recurrence = p:catalan-recurrence
catalan-closed-form = p:catalan-closed-form
bracket-count = p:bracket-count
S bracket-sequences | Generating bracket sequences
next-bracket-sequence = p:next-bracket-sequence
generate-bracket-sequences = p:generate-bracket-sequences
bracket-sequence-rank = p:bracket-sequence-rank
S inclusion-exclusion | Inclusion-exclusion
inclusion-exclusion = p:inclusion-exclusion
inclusion-exclusion-proof = p:inclusion-exclusion-proof
inclusion-exclusion-exactly-r = p:inclusion-exclusion-exactly-r
complement-counting = p:complement-counting
coprime-count-interval = p:coprime-count-interval
lattice-paths-obstacles = p:lattice-paths-obstacles
mobius-style-ie = p:mobius-style-ie
derangements = p:derangements
S stars-bars | Stars and bars and k-combinations
stars-and-bars = p:stars-and-bars
positive-integer-sums = p:positive-integer-sums
lower-bounded-sums = p:lower-bounded-sums
upper-bounded-sums = p:upper-bounded-sums
next-combination = p:next-combination
combinations-gray-order = p:combinations-gray-order
S burnside | Burnside's lemma and Polya enumeration
orbits-under-symmetry = p:orbits-under-symmetry
burnside-lemma = p:burnside-lemma
polya-enumeration = p:polya-enumeration
necklace-counting = p:necklace-counting
burnside-by-generation = p:burnside-by-generation
S counting-structures | Counting graphs and puzzle states
labeled-graph-count = p:labeled-graph-count
connected-labeled-graphs = p:connected-labeled-graphs
labeled-graphs-k-components = p:labeled-graphs-k-components
fifteen-puzzle-parity = p:fifteen-puzzle-parity
S josephus | The Josephus problem
josephus-problem = p:josephus-problem
josephus-recurrence = p:josephus-recurrence
josephus-k-log-n = p:josephus-k-log-n
josephus-k2 = p:josephus-k2

C ch-games | Game theory
S games-on-graphs | Games on graphs
retrograde-analysis = p:retrograde-analysis
policeman-thief = p:policeman-thief
S nim | Nim
impartial-game = p:impartial-game
nim-xor = p:nim-xor
misere-nim = p:misere-nim
nim-with-increases = p:nim-with-increases
S sprague-grundy | The Sprague-Grundy theorem
sprague-grundy = p:sprague-grundy
grundy-sum-of-games = p:grundy-sum-of-games
grundy-patterns = p:grundy-patterns

C ch-algebra | Linear algebra, polynomials and the FFT
S gauss | Gaussian elimination
gauss-jordan = p:gauss-jordan
partial-pivoting = p:partial-pivoting
gauss-solution-count = p:gauss-solution-count
gauss-complexity = p:gauss-complexity
gauss-mod-2-bitset = p:gauss-mod-2-bitset
iterative-refinement = p:iterative-refinement
S determinant-rank | Determinants and rank | cpa linear_algebra/determinant-gauss (200 words), determinant-kraut (245) and rank-matrix (228) are thin and share this home; graph/kirchhoff-theorem joins as the application.
determinant-gauss = p:determinant-gauss
lu-decomposition-crout = p:lu-decomposition-crout
matrix-rank = p:matrix-rank
rank-by-elimination = p:rank-by-elimination
kirchhoff-matrix-tree = p:kirchhoff-matrix-tree
S dft | Polynomials and the discrete Fourier transform
polynomial-representations = n:polynomial-representations
vandermonde = n:vandermonde
dft = p:dft c:fourier-transform :: note=CIU's Fourier-transform idea (signals as sums of sinusoids) is taught here through cpa's discrete transform; joined.
S fft | The fast Fourier transform
fft = p:fft c:fft n:fft
inverse-fft = p:inverse-fft n:inverse-fft
fast-polynomial-multiplication = n:fft-multiplication p:convolution-via-dft
fft-iterative = p:fft-iterative
S fft-variants | FFT variants and applications
ntt = p:ntt
fft-arbitrary-modulus = p:fft-arbitrary-modulus
fft-applications = p:fft-applications
S power-series | Operations on power series
formal-power-series = p:formal-power-series
power-series-inverse = p:power-series-inverse
polynomial-division = p:polynomial-division
newton-for-series = p:newton-for-series
series-log-exp = p:series-log-exp
multipoint-evaluation = p:multipoint-evaluation
chirp-z = p:chirp-z
resultant = p:resultant

C ch-numerical | Numerical methods and optimisation
S newton | Newton's method
newton-method = p:newton-method
newton-sqrt = p:newton-sqrt
S simpson | Numerical integration
simpson-rule = p:simpson-rule
simpson-error = p:simpson-error
S annealing | Simulated annealing
energy-minimisation = p:energy-minimisation
neighbouring-state = p:neighbouring-state
simulated-annealing = p:simulated-annealing
annealing-parameters = p:annealing-parameters
S linear-programming | Linear programming and duality
linear-programming = n:linear-programming c:linear-programming
lp-geometry = n:lp-geometry
lp-formulations = n:lp-formulations
lp-duality = n:lp-duality
complementary-slackness = n:complementary-slackness
S simplex | The simplex method and LP rounding
simplex = n:simplex
network-simplex = n:network-simplex
seidel-lp = n:seidel-lp
lp-rounding = n:lp-rounding

C ch-geometry-primitives | Computational geometry: primitives
S vectors | Points, vectors, dot and cross products
points-as-vectors = p:points-as-vectors
dot-product = p:dot-product
dot-product-uses = p:dot-product-uses
cross-product = p:cross-product
orientation-test = p:orientation-test
S lines | Lines and their intersections | cpa geometry/lines-intersection (306 words) and segment-to-line share this home.
line-through-two-points = p:line-through-two-points
line-normalisation = p:line-normalisation
parametric-line = p:parametric-line
line-intersection-parametric = p:line-intersection-parametric
line-intersection-cramer = p:line-intersection-cramer
planes-intersection = p:planes-intersection
S segments | Segments | cpa geometry/check-segments-intersection (167 words) and length-of-segments-union (158 words) are thin and share this home with segments-intersection.
segments-intersect-test = p:segments-intersect-test
segment-intersection-points = p:segment-intersection-points
union-of-segments-length = p:union-of-segments-length
S circles | Circles and enclosing circles
circle-line-intersection = p:circle-line-intersection
circle-circle-intersection = p:circle-circle-intersection
common-tangent-count = p:common-tangent-count
common-tangents = p:common-tangents
min-enclosing-circle = p:min-enclosing-circle
mec-point-tests = p:mec-point-tests
welzl-algorithm = p:welzl-algorithm
S areas | Areas and Pick's theorem | cpa geometry/oriented-triangle-area (236 words) and area-of-simple-polygon (168 words) are thin and share this home.
oriented-triangle-area = p:oriented-triangle-area
shoelace-formula = p:shoelace-formula
picks-theorem = p:picks-theorem
picks-theorem-proof = p:picks-theorem-proof
reeve-tetrahedron = p:reeve-tetrahedron
S lattice-points | Lattice points
floor-sum-lattice = p:floor-sum-lattice
lattice-points-non-lattice-polygon = p:lattice-points-non-lattice-polygon
continued-fraction-geometry = p:continued-fraction-geometry
S manhattan | Manhattan distance
manhattan-distance = p:manhattan-distance
manhattan-farthest-pair = p:manhattan-farthest-pair
manhattan-to-chebyshev = p:manhattan-to-chebyshev
manhattan-mst = p:manhattan-mst

C ch-geometry-algorithms | Computational geometry: algorithms
S convex-hull | Convex hulls
convex-hull = p:convex-hull c:convex-hull :: note=CIU's row names the hull and its algorithms (Graham, Jarvis, divide and conquer); it treats both convex-hull and graham-scan.
graham-scan = p:graham-scan c:convex-hull
monotone-chain = p:monotone-chain
S convex-polygons | Convex polygons and Minkowski sums
point-in-convex-polygon = p:point-in-convex-polygon
minkowski-sum = p:minkowski-sum
minkowski-sum-convex = p:minkowski-sum-convex
polygon-distance-minkowski = p:polygon-distance-minkowski
S convex-hull-trick | The convex hull trick and Li Chao trees
line-min-query-dp = p:line-min-query-dp
convex-hull-trick = p:convex-hull-trick
li-chao-tree = p:li-chao-tree
S sweep-line | Sweep lines and point location
sweep-line-segment-intersection = p:sweep-line-segment-intersection
offline-point-location = p:offline-point-location
online-point-location-persistent = p:online-point-location-persistent
vertical-decomposition = p:vertical-decomposition
union-of-triangles-area = p:union-of-triangles-area
convex-polygon-intersection-stripes = p:convex-polygon-intersection-stripes
S planar-graphs | Faces of planar graphs
euler-formula-planar = p:euler-formula-planar
planar-faces-traversal = p:planar-faces-traversal
planar-graph-from-segments = p:planar-graph-from-segments
S closest-pair | The closest pair of points
closest-pair-divide-conquer = p:closest-pair-divide-conquer
closest-pair-strip-bound = p:closest-pair-strip-bound
closest-pair-grid = p:closest-pair-grid
min-perimeter-triangle = p:min-perimeter-triangle
S delaunay | Delaunay triangulations and Voronoi diagrams
voronoi-delaunay = p:voronoi-delaunay
delaunay-properties = p:delaunay-properties
guibas-stolfi = p:guibas-stolfi
S half-planes | Half-plane intersection
half-plane = p:half-plane
halfplane-incremental = p:halfplane-incremental
sort-and-incremental = p:sort-and-incremental
halfplane-applications = p:halfplane-applications

# ---- rows not merged into any concept
DROP c:os-courses | Pointer row for course-length OS lectures; CIU's own note says it is not a single concept. Its links stay available to the side panel of the processes and virtual-memory sections.
DROP c:real-world-architectures | Reading list (27 links, "pick a few"), not a concept; candidate references for the worked-designs chapter.
DROP c:discrete-math | Course-length links only; the discrete-math content it points at is covered by counting, induction and probability concepts.
DROP c:devops | One reading-list link and a one-line definition; nothing an exercise could test.
DROP c:sd-exercises | List of practice prompts (unique IDs, key-value store, picture sharing, recommender, URL shortener, cache); the URL shortener and cache are sdp worked designs, the rest are gaps.

# ---- prerequisite edges dropped (concept -> prereq) with reasons
NOEDGE potential-method -> dynamic-array-cost | ODS states the potential method inside its DualArrayDeque lemma; the method itself rests on amortized analysis, not on array resizing. Keeps amortized analysis in chapter 1 as CIU orders it.
NOEDGE list-interface -> deque | ODS introduces List as a generalisation of Deque; a list does not need the deque interface. Otherwise lists would wait for stacks and queues.
NOEDGE singly-linked-list -> queue | ODS's SLList implements Stack and Queue operations, but a linked list rests on neither; those operations are the concepts queue-linked-list and stack.
NOEDGE singly-linked-list -> stack | as above
NOEDGE binary-representation -> bitwise-operators | CIU teaches two's complement through bitwise NOT; the representation does not need the operators (cpa makes the operators depend on the representation). Breaks a cycle.
NOEDGE hashing-with-chaining -> multiplicative-hashing | ODS's ChainedHashTable happens to use multiplicative hashing; chaining works with any hash function.
NOEDGE bfs-shortest-paths -> ford-relaxation | Erickson frames BFS as an instance of Ford's relaxation; unweighted BFS distances need no relaxation framework, and cpa and ODS teach them from BFS alone.
NOEDGE max-flow-min-cut -> ford-fulkerson | cpa proves the theorem through Ford-Fulkerson; Erickson states it first and derives the algorithm from it. Breaks a cycle.
NOEDGE huffman -> compression | CIU files Huffman under Compression; the greedy construction needs prefix codes and a priority queue, not the compression chapter.
NOEDGE stack -> queue | ODS defines a stack as a LIFO queue; CIU and most readers meet stacks first, and nothing in the stack needs FIFO queues.

# ---- prerequisite edges added between sources (concept -> prereq) with reasons
EDGE binary-tree -> tree | ODS's binary-tree terminology and CIU's tree are taught by different sources; a binary tree is a tree.
EDGE ford-relaxation -> edge-relaxation | Erickson's generic algorithm repeats the relaxation step that cpa names separately.
EDGE sparse-dp -> longest-common-subsequence | Hunt-Szymanski's sparse DP is stated on LCS.
NOEDGE random-walk-binary-tree -> meldable-heap | cpa proves the random root-to-leaf path bound inside its randomized-heap article; ODS states it as a lemma about any binary tree, and the heap rests on it, not the reverse. Breaks a cycle.
