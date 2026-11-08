#!/usr/bin/env python3
"""Write concept-map/report.md from concepts.json, toc.json and stats.json."""
import json, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = '/home/user/cs-interview-prep-ultra/concept-map'
D = json.load(open(f'{OUT}/concepts.json')); C = D['concepts']; cby = {c['id']: c for c in C}
T = json.load(open(f'{OUT}/toc.json')); S = json.load(open(f'{HERE}/stats.json'))
TIERS = ['core', 'stretch', 'contest']
SHORT = {'ciu': 'ciu', 'cpa': 'cpa', 'jeffe': 'jeffe', 'jeffe-notes': 'notes', 'ods': 'ods', 'sdp': 'sdp'}
CH = T['chapters']; APPS = T['appendices']; APP_A = next(a for a in APPS if a['letter'] == 'A')
chap = {ch['id']: ch for ch in CH}
secs = {(ch['id'], s['id']): s for ch in CH for s in ch['sections']}
pages = {(s['group'], s['id']): s for a in APPS for s in a['pages']}
n_secs = sum(len(ch['sections']) for ch in CH)
def where(c):
    """Number of a concept's chapter, or 'Appendix A'."""
    return f'Appendix {c["appendix"]}' if 'appendix' in c else str(chap[c['chapter']]['number'])
# chapter ranges used for the summary table (book order; the ranges only group rows of the table)
RANGES = [(1, 7), (8, 12), (13, 16), (17, 23), (24, 29), (30, len(CH))]
L = []; A = L.append

A('# Concept map report'); A('')
A(f'Built from the seven inventories in `inventory/` ({D["counts"]["inventory_rows"]} rows). '
  f'Output: one book of **{len(CH)} numbered chapters** and **{n_secs} sections**, plus two appendices that are not built as text: '
  f'**Appendix A · {APP_A["title"]}** ({len(APP_A["pages"])} curated-links pages, {sum(len(s["concepts"]) for s in APP_A["pages"])} concepts) '
  'and **Appendix B · Getting the job** (one reading page, no concepts). '
  f'**{len(C)} concepts** in all. '
  f'`python3 tools/check_map.py` passes (0 errors, {len(S["inversions"])} warnings' +
  ('; the warnings are the tier inversions listed under judgement call 3).' if S['inversions'] else '; no tier inversions remain).')); A('')

# ---- counts
A('## 1. Counts'); A('')
A('### Concepts per chapter range and appendix'); A('')
A('Per-chapter counts are in `toc.md` (each chapter heading) and `toc.json` (`tier_counts`).'); A('')
A('| Chapters | Sections | core | stretch | contest | total |'); A('|---|---:|---:|---:|---:|---:|')
tot = collections.Counter()
for lo, hi in RANGES:
    chs = [ch for ch in CH if lo <= ch['number'] <= hi]
    cnt = collections.Counter(cby[i]['tier'] for ch in chs for s in ch['sections'] for i in s['concepts'])
    tot += cnt
    A(f'| {lo}–{hi} ({chs[0]["title"]} … {chs[-1]["title"]}) | {sum(len(ch["sections"]) for ch in chs)} | '
      f'{cnt["core"]} | {cnt["stretch"]} | {cnt["contest"]} | {sum(cnt.values())} |')
A(f'| **Chapters 1–{len(CH)}** | {n_secs} | **{tot["core"]}** | **{tot["stretch"]}** | **{tot["contest"]}** | **{sum(tot.values())}** |')
for a in APPS:
    if not a['pages']: continue
    cnt = collections.Counter(cby[i]['tier'] for s in a['pages'] for i in s['concepts'])
    tot += cnt
    A(f'| Appendix {a["letter"]} · {a["title"]} (links, not built) | {len(a["pages"])} pages | {cnt["core"]} | {cnt["stretch"]} | {cnt["contest"]} | {sum(cnt.values())} |')
A(f'| **All** | | **{tot["core"]}** | **{tot["stretch"]}** | **{tot["contest"]}** | **{sum(tot.values())}** |')
A('')
fp = [ch for ch in CH if ch['first_pass']]
A('First build pass: chapters ' + ', '.join(f'{ch["number"]}. {ch["title"]}' for ch in fp) + '.'); A('')
st = collections.Counter(s['tier'] for ch in CH for s in ch['sections'])
sa = collections.Counter(s['tier'] for s in APP_A['pages'])
A(f'Chapter sections by tag: {st["core"]} core, {st["stretch"]} stretch, {st["contest"]} contest; '
  f'Appendix A pages: {sa["core"]} core, {sa["stretch"]} stretch. '
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
  f'({sum(1 for s in secs.values() if not s["open_prose"])} chapter sections; '
  f'{sum(1 for s in pages.values() if not s["open_prose"])} of Appendix A\'s {len(pages)} pages, which is expected for a links appendix).'); A('')
byc = collections.OrderedDict()
for c in C:
    if not c['open_prose']:
        byc.setdefault(c['chapter'], []).append(c)
for chid, cs in sorted(byc.items(), key=lambda kv: (1, 0) if 'appendix' in kv[1][0] else (0, chap[kv[0]]['number'])):
    c0 = cs[0]
    label = (f'Appendix A, {next(g["title"] for g in APP_A["groups"] if g["id"] == chid)}' if 'appendix' in c0
             else f'{chap[chid]["number"]}. {chap[chid]["title"]}')
    srcs = collections.Counter('notes' if any(t['source'] == 'jeffe-notes' for t in c['treatments']) else 'ciu' for c in cs)
    A(f'- **{label}** ({len(cs)}; ' + ', '.join(f'{k} only {v}' for k, v in srcs.items()) + '): ' +
      '; '.join(c['name'] + (' [core]' if c['tier'] == 'core' else '') for c in cs))
A('')
A('Most of the CIU-only concepts are in Appendix A (operating systems, networking basics, testing, design patterns, security), '
  'which is now a curated links appendix: its pages need good links, not open prose. '
  'Among the numbered chapters the heaviest gaps are the probability, adversary and approximation chapters, whose only treatment is Erickson\'s NC notes. '
  'METHOD §0 already expects Wikipedia (CC BY-SA) for small systems gaps such as endianness and Unicode.'); A('')

# ---- decided rulings
A('## 3. Rulings (decided 2026-11-08)'); A('')
set_core = [c for c in C if 'Tier set to core in the spec' in c['notes'] and c['id'] != 'union-find']
raised = [c for c in C if 'Tier raised' in c['notes']]
sd_ids = [ch['id'] for ch in CH if ch['id'].startswith('ch-sd-')]
sd = [c for c in C if c['chapter'] in sd_ids]
sdt = collections.Counter(c['tier'] for c in sd)
cascade = ['b-tree', 'k-ary-tree', 'two-three-tree', 'two-four-tree']
R = [
 ('One book, flat chapters, no parts.',
  f'OmniStax books are book → chapters → sections, so the map has no parts: `toc.json` holds {len(CH)} chapters numbered 1 to {len(CH)} and a list of appendices; '
  'concept rows carry no part field; `toc.md` and `chapters.mmd` have no part headings or subgraphs. The old part lines in `tools/map/map.spec` are `#` comments now; the spec\'s chapter order is the book order.'),
 (f'Appendix A · {APP_A["title"]} is a curated links appendix.',
  'The four computer-systems chapters (' + ', '.join(g['title'] for g in APP_A['groups']) + ') are not numbered book chapters and are not built as text. '
  f'Their {len(APP_A["pages"])} sections are the appendix\'s pages A.1 to A.{len(APP_A["pages"])}, each a list of curated links for its concepts. '
  f'The {sum(len(s["concepts"]) for s in APP_A["pages"])} concepts stay in the map, with `"appendix": "A"` and their old chapter and section ids (the chapter id names the page group), '
  f'so prerequisite edges into them still resolve: {len(S["into_appendix"])} edges run from a chapter concept to an Appendix A concept, '
  'and the chapter page points the reader to the appendix for those. Chapter numbering skips the appendix, so the system design chapters '
  f'({chap[sd_ids[0]]["number"]} to {chap[sd_ids[-1]]["number"]}) follow the paradigm chapters directly. Getting the job is Appendix B (one reading page, no concepts).'),
 ('System design concepts take their own tiers.',
  'The cap that held every system design concept at stretch is gone. They take the tiers the inventories give, reconciled as for any other concept: '
  f'the system design chapters now hold {sdt["core"]} core and {sdt["stretch"]} stretch concepts. '
  'Where an sdp row merged with a CIU row from CIU\'s optional system design list, the CIU-first rule still said stretch; those that core concepts rest on were set to core under ruling 4.'),
 ('Union-find is core, and so is every prerequisite a core concept rests on.',
  'Union-find is set core in the spec (Kruskal, core, rests on it). Every other case where a core concept rested on a stretch one was settled the same way, '
  f'by setting tier=core in the spec ({len(set_core)} concepts, each with a note saying which core concept needs it): '
  + '; '.join(f'{c["name"]} ({where(c)})' for c in set_core) + '. '
  'None looked like a CIU mistake in the other direction, so none was settled by lowering the dependant. '
  'The propagation rule then raised the concepts with no CIU row under them (each noted "Tier raised"). '
  'The widest cascade comes from database indexes (sdp, core) resting on B-trees: B-trees, k-ary trees, 2-3 trees, 2-3-4 trees and, by propagation, ODS\'s B-tree and 2-4 tree operations and the external-memory model are core. '
  'If B-trees should stay stretch, dropping the edge database-indexes → b-tree with a NOEDGE line undoes the whole cascade. '
  + (f'{len(S["inversions"])} tier inversions remain.' if S['inversions'] else 'No tier inversions remain.')),
 ('First pass stays chapters 1 to 3.',
  'The first build pass is ' + ', '.join(f'{ch["number"]}. {ch["title"]}' for ch in CH if ch['first_pass']) + '.'),
]
for i, (h, b) in enumerate(R, 1):
    A(f'{i}. **{h}** {b}')
A('')

# ---- judgement calls
A('## 4. Judgement calls to check'); A('')
three = sum(1 for ch in CH if len(ch['sections']) == 3)
outside = sum(1 for ch in CH if not 3 <= len(ch['sections']) <= 8)
single = [s for s in list(secs.values()) + list(pages.values()) if len(s['concepts']) == 1]
J = [
 ('Recursion and induction moved early (chapter 4).',
  'METHOD puts recursion later, but recursive binary search, tree traversals and DFS rest on it in the inventories, so the DAG pulls it forward. '
  'Correctness proofs and induction (Erickson, notes) come with it. Backtracking, DP and greedy stay in chapters 17 to 20.'),
 ('All-pairs shortest paths and DAG shortest paths live in "Dynamic programming on graphs" (chapter 19), not in Shortest paths.',
  'Erickson\'s Floyd-Warshall, APSP-by-path-length and DAG shortest paths rest on his DP pattern; merged with cpa\'s rows they inherit that edge. '
  'Dijkstra and Bellman-Ford stay in Shortest paths (chapter 15). Floyd-Warshall is now **core** (cpa says core; CIU\'s row is in its optional Additional Detail), because path reconstruction, core, rests on it.'),
 ('Tier propagation.',
  f'A concept with no CIU row takes the most basic tier of the concepts that rest on it ({len(raised)} raised, each noted: e.g. MST definition and SCC definition to core because Prim and Kosaraju are core; '
  'decision-tree lower bounds to core under the sorting lower bound). Concepts with a CIU row keep CIU\'s verdict unless the spec sets a tier (ruling 4).'
  + (' Remaining inversions: ' + '; '.join(f'{cby[a]["name"]} ({ta}) rests on {cby[b]["name"]} ({tb})' for a, b, ta, tb in S['inversions']) + '.' if S['inversions'] else '')),
 ('Probability split between chapter 1 and chapter 22.',
  'Counting, basic probability, conditional probability, expectation and indicator variables are in 1.6 because hashing, heapify\'s analysis and skip lists need them; '
  'distributions, tail bounds, Markov chains and randomized algorithms are chapter 22. "Random variables and linearity of expectation" and conditional probability are now **core** (ruling 4: hashing analysis rests on them), although CIU lists them as optional.'),
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
 ('Order of chapters 8 to 12: trees and BSTs, heaps, sorting, then balanced trees and tries.',
  'Treaps need heaps, quicksort\'s analysis needs random BSTs, and core sorting should not wait behind balanced trees. CIU\'s order (trees intro, BST, heap, balanced, sorting) is kept except that balanced trees move after sorting.'),
 (f'Core number theory stays in chapter {chap["ch-number-theory-1"]["number"]}.',
  f'cpa marks GCD, Euclid, LCM, the sieve and trial division core; they open the number-theory chapter (chapter {chap["ch-number-theory-1"]["number"]}) instead of getting an early chapter. '
  f'Seven core concepts therefore sit among the beyond-the-interview chapters ({chap["ch-range-queries"]["number"]} to {len(CH)}). The alternative is a short "Number theory essentials" chapter after bits.'),
 ('Placements of a few CIU core rows.',
  f'Distributed hash tables (CIU: under Hash table, core) sit with consistent hashing in the databases chapter\'s partitioning section (chapter {chap["ch-sd-data"]["number"]}). The LRU cache stays in chapter 5 as an interview staple. '
  'Huffman is taught as greedy (chapter 20), not on Appendix A\'s compression page. Tries (CIU: Even More Knowledge) are in chapter 12 with the search trees, as METHOD proposes.'),
 (f'Single-concept sections ({len(single)}) and thin chapters.',
  'The LRU cache, three worked designs (query cache, sales rank, scaling on AWS: each is one sdp solution page), Bloom filters and simhash are one concept each. '
  f'They are pages because each is a separate thing a reader looks up; joining them would break rule 11\'s "a section is a page". {three} chapters have exactly three sections, the floor of the 3-to-8 range; '
  + ('none is outside it.' if not outside else f'{outside} are outside it.')),
 ('Folds and what stayed apart.',
  'Thin or duplicate cp-algorithms articles were folded into the home of the concept they duplicate (each section lists its folds in toc.json/toc.md): e.g. mst_kruskal_with_dsu into Kruskal, '
  'finding-negative-cycle into Floyd-Warshall, dijkstra_sparse into Dijkstra, sequences/k-th into Selection, string/rabin-karp into string hashing, factorial-divisors into factorials mod p, '
  'randomized_heap into ODS\'s meldable heap. cpa\'s treap article, by contrast, shares the Treaps home with ODS and notes but keeps its own split/merge concepts.'),
]
for i, (h, b) in enumerate(J, 1):
    A(f'{i}. **{h}** {b}')
A('')

# ---- chapter deps
A('## 5. Chapter dependencies'); A('')
A('Chapter → the chapters whose concepts it uses directly (any prerequisite edge that crosses chapters); "A" is Appendix A. '
  'The Mermaid graph in `chapters.mmd` shows the Hasse-reduced version.'); A('')
def num(x): return 'A' if x == 'A' else str(chap[x]['number'])
for ch in CH:
    d = ', '.join(num(x) for x in S['cdep'].get(ch['id'], [])) or 'none'
    A(f'- {ch["number"]}. {ch["title"]} → {d}')
d = ', '.join(num(x) for x in S['cdep'].get('A', [])) or 'none'
A(f'- Appendix A · {APP_A["title"]} → {d}')
A('')
open(f'{OUT}/report.md', 'w').write('\n'.join(L))
print('report lines', len(L))
