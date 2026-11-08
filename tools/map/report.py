#!/usr/bin/env python3
"""Write concept-map/report.md from concepts.json, toc.json and stats.json."""
import json, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = '/home/user/cs-interview-prep-ultra/concept-map'
D = json.load(open(f'{OUT}/concepts.json')); C = D['concepts']; cby = {c['id']: c for c in C}
T = json.load(open(f'{OUT}/toc.json')); S = json.load(open(f'{HERE}/stats.json'))
TIERS = ['core', 'stretch', 'contest']
SHORT = {'ciu': 'ciu', 'cpa': 'cpa', 'jeffe': 'jeffe', 'jeffe-notes': 'notes', 'ods': 'ods', 'sdp': 'sdp'}
chap = {ch['id']: ch for p in T['parts'] for ch in p['chapters']}
secs = {(ch['id'], s['id']): s for p in T['parts'] for ch in p['chapters'] for s in ch['sections']}
L = []; A = L.append

A('# Concept map report'); A('')
A(f'Built from the seven inventories in `inventory/` ({D["counts"]["inventory_rows"]} rows). '
  f'Output: **{len(C)} concepts** in **{sum(len(p["chapters"]) for p in T["parts"])} chapters** and '
  f'**{sum(len(ch["sections"]) for p in T["parts"] for ch in p["chapters"])} sections** across {len(T["parts"])} parts, plus an unbuilt appendix page. '
  '`python3 tools/check_map.py` passes (0 errors; its 6 warnings are the tier inversions listed under judgement call 5).'); A('')

# ---- counts
A('## 1. Counts'); A('')
A('### Concepts per part and tier'); A('')
A('| Part | Chapters | Sections | core | stretch | contest | total |'); A('|---|---:|---:|---:|---:|---:|---:|')
tot = collections.Counter()
for p in T['parts']:
    cnt = collections.Counter(cby[i]['tier'] for ch in p['chapters'] for s in ch['sections'] for i in s['concepts'])
    tot += cnt
    A(f'| {p["number"]} · {p["title"]} | {len(p["chapters"])} | {sum(len(ch["sections"]) for ch in p["chapters"])} | '
      f'{cnt["core"]} | {cnt["stretch"]} | {cnt["contest"]} | {sum(cnt.values())} |')
A(f'| **All** | {sum(len(p["chapters"]) for p in T["parts"])} | {sum(len(ch["sections"]) for p in T["parts"] for ch in p["chapters"])} | '
  f'**{tot["core"]}** | **{tot["stretch"]}** | **{tot["contest"]}** | **{sum(tot.values())}** |')
A('')
st = collections.Counter(s['tier'] for p in T['parts'] for ch in p['chapters'] for s in ch['sections'])
A(f'Sections by tag: {st["core"]} core, {st["stretch"]} stretch, {st["contest"]} contest. '
  f'Section sizes (concepts: sections): ' + ', '.join(f'{k}: {v}' for k, v in S['secsizes'].items()) + '.'); A('')
kinds = collections.Counter(c['kind'] for c in C)
A('Kinds: ' + ', '.join(f'{k} {v}' for k, v in kinds.most_common()) + '.'); A('')

A('### Merging'); A('')
multi = [c for c in C if len(c['treatments']) > 1]
cross = [c for c in multi if len({t['source'] for t in c['treatments']}) > 1]
A(f'- {D["counts"]["inventory_rows"]} rows in, {D["counts"]["dropped_rows"]} dropped, {len(S["split_rows"])} rows split over two concepts each, '
  f'so {sum(len(c["treatments"]) for c in C)} treatments in {len(C)} concepts.')
A(f'- **{len(multi)} merged clusters** (concepts with more than one treatment); {len(cross)} of them join different sources, '
  f'the other {len(multi)-len(cross)} join two rows of one source. Cluster sizes: ' +
  ', '.join(f'{v} with {k} rows' for k, v in S['size_hist'].items() if k != '1') + f'; {S["size_hist"]["1"]} concepts have one treatment.')
pairs = collections.Counter()
for c in cross:
    ss = sorted({SHORT[t['source']] for t in c['treatments']})
    pairs[' + '.join(ss)] += 1
A('- Source combinations in cross-source clusters: ' + ', '.join(f'{k} ({v})' for k, v in pairs.most_common()) + '.')
src = collections.Counter(); srcc = collections.Counter()
for c in C:
    for s in {t['source'] for t in c['treatments']}: srcc[s] += 1
A('- Concepts each source treats: ' + ', '.join(f'{SHORT[k]} {v}' for k, v in sorted(srcc.items(), key=lambda x: -x[1])) + '.')
A(f'- Hasse reduction removed {S["hasse_removed"]} redundant prerequisite edges; {sum(len(c["prereqs"]) for c in C)} edges remain.')
A('')
A('Rows split over two concepts (a source row whose grain was coarser than "an exercise could test it alone"):'); A('')
for r, cs in S['split_rows'].items():
    A(f'- `{r}` → {", ".join(cby[x]["name"] for x in cs)}')
A('')

A('### Dropped rows'); A('')
A('| Row | Name | Reason |'); A('|---|---|---|')
for d in D['dropped']:
    A(f'| `{d["row"]}` | {d["name"]} | {d["reason"]} |')
A('')
A('No other row was dropped. ODS\'s implementation-variant classes (DualArrayDeque, RootishArrayStack, SEList, SkiplistList, XFastTrie, YFastTrie, scapegoat trees) stay as stretch or contest concepts, since each teaches an idea (amortised rebuilding, sqrt-space blocks, indexing by skiplist widths).'); A('')

# ---- gaps
A('## 2. Gaps'); A('')
A('### Interview topics no inventory teaches'); A('')
A('None of these is in the map, because no inventory row teaches it (the rule: never invent a concept). Each is a job for the resource finder (METHOD §6).'); A('')
gaps = [
 ('Two pointers', 'core', 'No inventory names it. Closest rows: cpa\'s tortoise and hare (2.5) and Kadane (18.4).'),
 ('Sliding window (variable-size)', 'core', 'cpa teaches only the fixed-window minimum with a monotonic deque (3.4, `sliding-window-minimum`). The general expand/shrink window has no row.'),
 ("Kahn's algorithm (topological sort by in-degrees)", 'core', 'cpa graph/topological-sort says outright "Kahn\'s algorithm is not covered"; Erickson and CIU teach only the DFS method.'),
 ('Prefix sums and difference arrays', 'core', 'Assumed by cpa (Fenwick trees, sqrt decomposition, maximum subarray, range updates) but taught nowhere.'),
 ('Modular arithmetic basics', 'core', 'Assumed by 8 cpa rows (modular exponentiation, inverses, congruences, string hashing); taught nowhere.'),
 ('Interval problems (merge intervals, meeting rooms)', 'core', 'Only interval scheduling (Erickson 4.2) and the contest-tier union of segments (cpa).'),
 ('Generating permutations and subsets by backtracking', 'core', 'CIU links only; Erickson\'s backtracking examples are n queens, subset sum and segmentation; cpa covers k-combinations and bracket sequences.'),
 ('Classic DP problems: coin change, grid paths, longest palindromic subsequence', 'core', 'Grid paths is an alias in cpa\'s classic-DP table; the others have no row.'),
 ('Object-oriented programming basics', 'core', 'Assumed by CIU\'s design patterns and SOLID rows and by sdp\'s OOD notebooks.'),
 ('Memory and pointers', 'core', 'Assumed by CIU arrays and linked lists.'),
 ('Rate limiting', 'stretch', 'METHOD §0 already names it; the primer has no section.'),
 ('Unique ID generation', 'stretch', 'Only a prompt in CIU\'s dropped practice list (`ciu:sd-exercises`).'),
 ('MapReduce as a concept', 'stretch', 'sdp\'s worked designs use it (`mapreduce-aggregation` assumes it) but nothing defines it.'),
 ('Queueing (Little\'s law, utilisation and latency)', 'stretch', 'sdp\'s back pressure links it as further reading only; METHOD §2.4 wants a sim for it.'),
]
A('| Topic | Tier it would get | Evidence |'); A('|---|---|---|')
for g in gaps: A(f'| {g[0]} | {g[1]} | {g[2]} |')
A('')
A('One bridge concept **was** added because an inventory names it: **Longest common subsequence** (18.6), split out of cpa\'s classic-DP table (`cpa:classic-dp-problems`, alias "LCS"). Its only treatment is that table row, so it counts as open prose but has no article behind it: treat it as a prose gap too.'); A('')
A('Other assumed knowledge that no row teaches (bracketed prerequisites in the inventories, contest-tier mostly): ' +
  ', '.join(sorted(k.strip('[]') for k in S['assumed'] if k not in ('[prefix sums]', '[modular arithmetic]', '[object-oriented programming]', '[memory and pointers]', '[MapReduce]', '[difference array]'))) + '. '
  'Each affected concept says so in its notes ("Assumes, untaught in the map").'); A('')

A('### Concepts with no open prose'); A('')
np = [c for c in C if not c['open_prose']]
npt = collections.Counter(c['tier'] for c in np)
A(f'**{len(np)} concepts** are taught only by CIU links or by Erickson\'s NC notes ({npt["core"]} core, {npt["stretch"]} stretch, {npt["contest"]} contest). '
  'Their prose needs the finder. Whole sections with no open source at all are marked "open prose: none" in toc.md '
  f'({sum(1 for s in secs.values() if not s["open_prose"])} sections).'); A('')
byc = collections.OrderedDict()
for c in C:
    if not c['open_prose']:
        byc.setdefault(c['chapter'], []).append(c)
for chid, cs in byc.items():
    ch = chap[chid]
    srcs = collections.Counter('notes' if any(t['source'] == 'jeffe-notes' for t in c['treatments']) else 'ciu' for c in cs)
    A(f'- **{ch["number"]}. {ch["title"]}** ({len(cs)}; ' + ', '.join(f'{k} only {v}' for k, v in srcs.items()) + '): ' +
      '; '.join(c['name'] + (' [core]' if c['tier'] == 'core' else '') for c in cs))
A('')
A('The heaviest gaps are Part V (operating systems, networking basics, testing, design patterns, security: CIU links only, all core in CIU\'s required list) '
  'and the probability, adversary and approximation chapters, whose only treatment is Erickson\'s NC notes. '
  'METHOD §0 already expects Wikipedia (CC BY-SA) for small systems gaps such as endianness and Unicode.'); A('')

# ---- judgement calls
A('## 3. Judgement calls to check'); A('')
promoted = [c for c in C if 'Tier raised' in c['notes']]
J = [
 ('Seven parts instead of METHOD §4.2\'s five.',
  'I added **Part V · Computer systems** (CIU\'s required OS, networking, testing and design-pattern topics had no home in the draft), '
  'split the draft\'s Part II into **II · Trees and sorting** and **III · Graphs** (Kruskal needs sorting, and CIU orders trees, then sorting, then graphs), '
  'and moved **Beyond the interview** to the end (Part VII) so every core part comes first. System design is Part VI.'),
 ('Recursion and induction moved into Part I (chapter 4).',
  'METHOD puts recursion in Part III, but recursive binary search, tree traversals and DFS rest on it in the inventories, so the DAG pulls it forward. '
  'Correctness proofs and induction (Erickson, notes) come with it. Backtracking, DP and greedy stay in Part IV.'),
 ('All-pairs shortest paths and DAG shortest paths live in "Dynamic programming on graphs" (chapter 19), not in Shortest paths.',
  'Erickson\'s Floyd-Warshall, APSP-by-path-length and DAG shortest paths rest on his DP pattern; merged with cpa\'s rows they inherit that edge. '
  'Dijkstra and Bellman-Ford stay in Part III. Floyd-Warshall is **stretch**, because CIU\'s only row for it sits in the optional Additional Detail (cpa says core).'),
 (f'System design capped at stretch ({len(S["capped"])} concepts).',
  'CIU lists system design as optional ("if you have 4+ years experience"), so I read "CIU\'s required list decides core" as capping every sdp concept in Part VI at stretch. '
  'sdp\'s own core/stretch is kept in each note ("sdp marks it core; capped"). If you want sdp\'s internal split as the tier, it is a one-line change in the build. '
  'sdp concepts outside Part VI (TCP, UDP, HTTP, REST, OOD notebooks) keep sdp\'s tier, since CIU requires networking and design patterns.'),
 ('Tier propagation, and six inversions left on purpose.',
  f'A concept with no CIU row takes the most basic tier of the concepts that rest on it ({len(promoted)} raised, each noted: e.g. MST definition and SCC definition to core because Prim and Kosaraju are core; '
  'decision-tree lower bounds to core under the sorting lower bound). Concepts with a CIU row keep CIU\'s verdict, which leaves six inversions: '
  + '; '.join(f'{cby[a]["name"]} ({ta}) rests on {cby[b]["name"]} ({tb})' for a, b, ta, tb in S['inversions']) +
  '. The Kruskal one is CIU\'s own inconsistency (union-find is optional, Kruskal is required). Promote those prerequisites to core if you prefer.'),
 ('Probability split between chapter 1 and chapter 22.',
  'Counting, basic probability, conditional probability, expectation and indicator variables are in 1.6 because hashing, heapify\'s analysis and skip lists need them; '
  'distributions, tail bounds, Markov chains and randomized algorithms are chapter 22. "Random variables and linearity of expectation" is **stretch** because the CIU row merged into it is in CIU\'s optional list.'),
 ('Rows split by granularity (7).',
  'CIU rows that cover two testable concepts were split, and the CIU row treats both: BST search/insertion, universal/perfect hashing, counting/radix sort, '
  'union by rank/path compression, Floyd-Warshall/APSP DP, convex hull/Graham scan; cpa\'s classic-DP table also treats the new LCS concept.'),
 ('Joins across sources that might look loose.',
  'ODS\'s resizing ArrayQueue with CIU\'s fixed-size array queue; SPFA (cpa) with Moore\'s queue-based Bellman-Ford (Erickson); the master theorem (CIU) with recursion trees (Erickson, notes); '
  'ODS polynomial hashing, cpa polynomial rolling hash and CIU rolling hash; CIU powers of two with sdp\'s powers-of-two table; CIU\'s LRU cache with sdp\'s query-cache implementation and OOD LRU notebook; '
  'CIU\'s Fourier transform idea with cpa\'s DFT; sdp\'s OOD hash map with CIU\'s implement-a-hash-table; CIU two\'s complement into cpa\'s binary representation.'),
 ('Kept apart although the names are close.',
  'DP as overlapping subproblems (cpa, CIU) vs DP as smart recursion (Erickson): merging them made a cycle with memoization. Hashing with chaining (structure, core) vs expected chain length (notes\' analysis). '
  'Erickson\'s string-matching automaton vs cpa\'s KMP automaton (also a cycle if merged). Erickson\'s general reduction vs CIU\'s polynomial-time reductions. '
  'CIU\'s "recognise NP-complete problems" vs Erickson\'s NP-hard catalog (merging dragged Cook-Levin into core). TCP, UDP and CIU\'s TCP-vs-UDP comparison. jeffe-notes\' definition of unbalanced flows (vertex balances, edge bounds) vs cpa\'s reduction of edge demands to one max flow: a definition and a result that overlap, kept as two concepts in one section.'),
 (f'Prerequisite edges dropped ({len(S["used_noedge"])}) and added (3).',
  'Each is recorded in the concept\'s notes. Dropped, mostly where a source\'s presentation order posed as a dependency: stack → queue and list → deque (ODS defines them through each other), '
  'singly linked list → stack/queue (ODS\'s SLList implements them), potential method → array resizing, chaining → multiplicative hashing, BFS distances → Ford\'s relaxation, '
  'Huffman → compression, and three that broke cycles (max-flow min-cut ↔ Ford-Fulkerson, two\'s complement ↔ bitwise operators, random-walk lemma ↔ meldable heap). '
  'Added: binary tree → tree, Ford\'s relaxation → edge relaxation, sparse DP → LCS.'),
 ('Order inside Part II: trees and BSTs, heaps, sorting, then balanced trees and tries.',
  'Treaps need heaps, quicksort\'s analysis needs random BSTs, and core sorting should not wait behind stretch balanced trees. CIU\'s order (trees intro, BST, heap, balanced, sorting) is kept except that balanced trees move after sorting.'),
 ('Core number theory stays in Part VII.',
  f'cpa marks GCD, Euclid, LCM, the sieve and trial division core; they open the number-theory chapter (chapter {chap["ch-number-theory-1"]["number"]}) instead of getting a Part I chapter. '
  'Seven core concepts therefore sit in Part VII. The alternative is a short "Number theory essentials" chapter after bits.'),
 ('Placements of a few CIU core rows.',
  'Distributed hash tables (CIU: under Hash table, core) sit with consistent hashing in Part VI\'s partitioning section. The LRU cache stays in chapter 5 as an interview staple. '
  'Huffman is taught as greedy (chapter 20), not in Part V\'s compression section. Tries (CIU: Even More Knowledge) are in Part II with the search trees, as METHOD proposes.'),
 ('Single-concept sections (6) and thin chapters.',
  'The LRU cache, three worked designs (query cache, sales rank, scaling on AWS: each is one sdp solution page), Bloom filters and simhash are one concept each. '
  'They are pages because each is a separate thing a reader looks up; joining them would break rule 11\'s "a section is a page". Nine chapters have exactly three sections, the floor of the 3-to-8 range; none is outside it.'),
 ('Folds and what stayed apart.',
  'Thin or duplicate cp-algorithms articles were folded into the home of the concept they duplicate (each section lists its folds in toc.json/toc.md): e.g. mst_kruskal_with_dsu into Kruskal, '
  'finding-negative-cycle into Floyd-Warshall, dijkstra_sparse into Dijkstra, sequences/k-th into Selection, string/rabin-karp into string hashing, factorial-divisors into factorials mod p, '
  'randomized_heap into ODS\'s meldable heap. cpa\'s treap article, by contrast, shares the Treaps home with ODS and notes but keeps its own split/merge concepts.'),
]
for i, (h, b) in enumerate(J, 1):
    A(f'{i}. **{h}** {b}')
A('')

# ---- chapter deps
A('## 4. Chapter dependencies'); A('')
A('Chapter → the chapters whose concepts it uses directly (any prerequisite edge that crosses chapters). The Mermaid graph in `chapters.mmd` shows the Hasse-reduced version.'); A('')
for p in T['parts']:
    A(f'**Part {p["number"]} · {p["title"]}**'); A('')
    for ch in p['chapters']:
        deps = sorted(S['cdep'].get(ch['id'], []), key=lambda x: chap[x]['number'])
        d = ', '.join(f'{chap[x]["number"]}' for x in deps) or 'none'
        A(f'- {ch["number"]}. {ch["title"]} → {d}')
    A('')
open(f'{OUT}/report.md', 'w').write('\n'.join(L))
print('report lines', len(L))
