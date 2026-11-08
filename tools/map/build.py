#!/usr/bin/env python3
"""Build concept-map/{concepts.json,toc.json,toc.md,chapters.mmd} and tools/map/stats.json from map.spec (report.py writes report.md)."""
import json, re, sys, collections, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
INV = ROOT + '/inventory'
OUT = ROOT + '/concept-map'
SPEC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'map.spec')

FILES = ['ciu', 'cpa-a', 'cpa-b', 'jeffe', 'jeffe-notes', 'ods', 'sdp', 'gap']
GAP = 'gap'          # inventory/gap.json: rows name their real source in the id prefix (registry locator prefix)
# spec prefixes; g: takes the gap row's full id, e.g. g:wikipedia:Prefix_sum
PFX = {'c': 'ciu', 'p': 'cpa', 'j': 'jeffe', 'n': 'jeffe-notes', 'o': 'ods', 's': 'sdp', 'g': None}
# Sources whose prose may be used: METHOD §0 (PD, CC0, CC BY, CC BY-SA), ruling 12 (MIT and Apache 2.0 prose with
# notices) and ruling 15 (OI Wiki in translation, doocs solution write-ups). Licences as in sources/registry.json.
OPEN = {'cpa', 'jeffe', 'ods', 'sdp',
        'wikipedia', 'wikibooks', 'wp-sysdesign',            # CC BY-SA 4.0
        'dsa-dummies',                                        # CC BY 4.0
        'doocs-leetcode', 'oiwiki',                           # CC BY-SA 4.0 (ruling 15)
        'opendsa', 'algo-explanation', 'trekhleb-jsalgo',     # MIT (ruling 12; trekhleb: README Algorithms sections only)
        'icc',                                                # Apache-2.0 (ruling 12; online_judges stays link-only)
        'mcs2018', 'anfp', 'lt-csbu',                         # CC BY-SA 3.0 / CC BY-SA
        'aspnes-202', 'dmoi3', 'appcomb', 'csci30', 'holden-acs',  # CC BY-SA 4.0
        'aosa', 'raft-site'}                                  # CC BY 3.0
TIERS = ['core', 'stretch', 'contest']
ABBR = {'ciu': 'CIU', 'cpa': 'cpa', 'jeffe': 'Erickson', 'jeffe-notes': 'Erickson notes (NC)', 'ods': 'ODS', 'sdp': 'Primer',
        'wikipedia': 'Wikipedia', 'wikibooks': 'Wikibooks', 'wp-sysdesign': 'Wikipedia (system design set)',
        'opendsa': 'OpenDSA', 'doocs-leetcode': 'doocs/leetcode write-ups', 'oiwiki': 'OI Wiki (in translation)',
        'dsa-dummies': 'DSA for absolute dummies', 'algo-explanation': 'TheAlgorithms explanations', 'icc': 'Interactive Coding Challenges',
        'trekhleb-jsalgo': 'javascript-algorithms READMEs', 'mcs2018': 'Mathematics for Computer Science (2018)',
        'aspnes-202': 'Aspnes, discrete math notes', 'anfp': 'Algorithms Notes for Professionals', 'dmoi3': 'Levin, Discrete Mathematics',
        'appcomb': 'Applied Combinatorics', 'csci30': 'CSCI 30 notes', 'lt-csbu': 'Computer Science from the Bottom Up',
        'holden-acs': 'Holden, Applied CS', 'aosa': 'Architecture of Open Source Applications', 'raft-site': 'Raft website'}
SHORT = {'ciu': 'ciu', 'cpa': 'cpa', 'jeffe': 'jeffe', 'jeffe-notes': 'notes', 'ods': 'ods', 'sdp': 'sdp',
         'wikipedia': 'wikipedia', 'wikibooks': 'wikibooks', 'wp-sysdesign': 'wp', 'opendsa': 'opendsa', 'doocs-leetcode': 'doocs',
         'oiwiki': 'oiwiki', 'dsa-dummies': 'dsa-dummies', 'algo-explanation': 'algo-expl', 'icc': 'icc', 'trekhleb-jsalgo': 'trekhleb',
         'mcs2018': 'mcs2018', 'aspnes-202': 'aspnes', 'anfp': 'anfp', 'dmoi3': 'dmoi3', 'appcomb': 'appcomb', 'csci30': 'csci30',
         'lt-csbu': 'lt-csbu', 'holden-acs': 'holden', 'aosa': 'aosa', 'raft-site': 'raft-site'}

# bracketed prerequisite names -> merged concept id (None = assumed knowledge, no concept)
BRACKET = {
 '[3SAT]': 'three-sat', '[B-tree]': 'b-tree', '[BFS]': 'graph-bfs', '[Bellman-Ford]': 'bellman-ford',
 '[Boolean formula in CNF]': None, "[Cramer's rule]": None, '[DAG DP]': 'dag-dp', '[DCEL]': None, '[DFA]': None,
 "[Kruskal's algorithm]": 'kruskal', '[MD5 hash]': 'crypto-hash', '[MapReduce]': None, '[NP-hardness]': 'np-hard',
 "[Wilson's theorem]": None, '[adjacency matrix]': 'adjacency-matrix', '[amortised analysis]': 'amortized-analysis',
 '[arrays]': 'array', '[backtracking]': 'backtracking', '[balanced BST]': 'balanced-bst-idea',
 '[balanced binary search tree]': 'balanced-bst-idea', '[big-O notation]': 'big-o', '[binary heap]': 'binary-heap',
 '[binary numbers]': 'binary-representation', '[binary representation]': 'binary-representation',
 '[binary search tree]': 'bst', '[binary tree]': 'binary-tree', '[bipartite graph]': 'bipartite-check',
 '[birthday paradox]': None, '[bit shifts]': 'shift-operators', '[bitmask DP]': None, '[bitmask]': 'bitwise-operators',
 '[breadth-first search]': 'graph-bfs', '[circles]': None, '[complex numbers]': None, '[coordinate geometry]': None,
 '[counting sort]': 'counting-sort', '[definite integrals]': None, '[deque]': 'deque', '[derivatives]': None,
 '[determinant]': None, '[difference array]': 'difference-array', '[directed graph]': 'graph', '[disjoint-set (union-find)]': 'union-find',
 '[divide and conquer]': 'divide-and-conquer', '[divisibility]': None, '[doubly linked list]': 'doubly-linked-list',
 '[dynamic programming]': 'overlapping-subproblems', '[edit distance]': 'edit-distance', '[equivalence relations]': None,
 '[exchange argument]': 'exchange-argument', '[expected value]': 'linearity-of-expectation',
 '[finite automaton]': None, '[floating-point numbers]': 'floating-point',
 '[graph representation: adjacency list]': 'adjacency-list', '[graphs]': 'graph', '[greedy algorithms]': 'exchange-argument',
 '[harmonic series]': 'harmonic-numbers', '[hash table]': 'hash-table', '[heap]': 'binary-heap',
 '[intermediate value theorem]': None, '[interval DP]': 'obst-dp', '[labelled tree]': 'tree', '[linear independence]': None,
 '[linear programming]': 'linear-programming', '[linked list]': 'singly-linked-list', '[mathematical induction]': 'induction',
 '[matrices]': None, '[matrix multiplication]': None, '[maximum flow]': 'ford-fulkerson', '[memory and pointers]': None,
 '[merge sort]': 'mergesort', '[minimum spanning trees]': 'mst', '[modular arithmetic]': None, '[multinomial theorem]': None,
 '[object-oriented programming]': None, '[optimal binary search trees]': 'obst-dp', '[permutation inversions]': None,
 '[permutations]': 'counting', '[persistent data structures]': 'persistent-segment-tree', '[pigeonhole principle]': None,
 '[planar graphs]': None, '[polynomials]': 'polynomial-representations', '[prefix products]': None, '[prefix sums]': 'prefix-sums',
 '[prime factorization]': 'factorization-trial-division', '[prime numbers]': None, '[priority queue]': 'priority-queue',
 '[quad-edge data structure]': None, '[queue]': 'queue', '[quicksort partition]': 'partition', '[quicksort]': 'quicksort',
 '[randomized algorithms]': 'las-vegas-monte-carlo', '[recursion]': 'recursion', '[rooted tree]': 'tree', '[rooted trees]': 'tree',
 '[segment tree]': 'segment-tree', '[sets]': None, '[sorting]': 'comparison-sorting', '[sparse table]': 'sparse-table',
 '[sqrt decomposition]': 'sqrt-decomposition', '[stack]': 'stack', '[subset sum DP]': 'subset-sum-dp',
 '[systems of linear equations]': None, '[tree rotations]': 'tree-rotations', '[tree]': 'tree', '[triangulation]': None,
 '[vertex degree]': 'graph', '[weighted graph]': 'graph',
 # added for inventory/gap.json
 '[topological order]': 'topological-order', '[combinations]': 'counting', '[tabulation]': 'bottom-up-dp',
}

# ---------------------------------------------------------------- inventories
REG_PFX = {s['locator'].split(':', 1)[0]: s['id'] for s in json.load(open(ROOT + '/sources/registry.json'))['sources'] if s.get('locator')}
rows = {}
for f in FILES:
    d = json.load(open(f'{INV}/{f}.json'))
    for c in d['concepts']:
        c = dict(c); c['_file'] = f; c['_source'] = d['source']
        if f == GAP:                     # the real source is named by the id prefix
            c['_source'] = REG_PFX[c['id'].split(':', 1)[0]]
            assert c['_source'] in ABBR, c['_source']
        assert c['id'] not in rows, c['id']
        rows[c['id']] = c

# ---------------------------------------------------------------- spec
chapters, appendices, drops, noedge, addedge = [], [], {}, [], []
noedge_reason, addedge_reason = {}, {}
cur_a = cur_c = cur_s = None
concepts = collections.OrderedDict()

def exp(r):
    p, rest = r.split(':', 1)
    return rest if p == 'g' else PFX[p] + ':' + rest

for ln, line in enumerate(open(SPEC), 1):
    line = line.rstrip('\n')
    if not line.strip() or line.startswith('#'):
        continue
    if line.startswith('APPENDIX '):
        letter, title, kind = [x.strip() for x in line[9:].split('|')]
        cur_a = {'letter': letter, 'title': title, 'kind': kind, 'chapters': []}; appendices.append(cur_a)
    elif line.strip() == 'END APPENDIX':
        cur_a = None
    elif line.startswith('C '):
        cid, title = [x.strip() for x in line[2:].split('|', 1)]
        cur_c = {'id': cid, 'title': title, 'sections': [], 'appendix': cur_a['letter'] if cur_a else None}
        chapters.append(cur_c)
        if cur_a: cur_a['chapters'].append(cur_c)
    elif line.startswith('S '):
        bits = [x.strip() for x in line[2:].split('|')]
        cur_s = {'id': bits[0], 'title': bits[1], 'folds': bits[2] if len(bits) > 2 else '', 'concepts': []}
        cur_c['sections'].append(cur_s)
    elif line.startswith('DROP '):
        r, reason = [x.strip() for x in line[5:].split('|', 1)]
        drops[exp(r)] = reason
    elif line.startswith('NOEDGE '):
        e, reason = [x.strip() for x in line[7:].split('|', 1)]
        a, b = [x.strip() for x in e.split('->')]
        noedge.append((a, b)); noedge_reason[(a, b)] = reason
    elif line.startswith('EDGE '):
        e, reason = [x.strip() for x in line[5:].split('|', 1)]
        a, b = [x.strip() for x in e.split('->')]
        addedge.append((a, b)); addedge_reason[(a, b)] = reason
    else:
        m = re.match(r'^([a-z0-9-]+) = (.*)$', line)
        if not m:
            sys.exit(f'spec line {ln}: cannot parse: {line}')
        cid, rest = m.group(1), m.group(2)
        opts = {}
        if '::' in rest:
            rest, o = rest.split('::', 1)
            for kv in o.split(';;'):
                k, v = kv.split('=', 1); opts[k.strip()] = v.strip()
        members = [exp(r) for r in rest.split()]
        if cid in concepts:
            sys.exit(f'duplicate concept id {cid}')
        concepts[cid] = {'id': cid, 'members': members, 'opts': opts,
                         'appendix': cur_c['appendix'], 'chapter': cur_c['id'], 'section': cur_s['id']}
        cur_s['concepts'].append(cid)

errors = []
row2c = collections.defaultdict(list)
for cid, c in concepts.items():
    for r in c['members']:
        if r not in rows:
            errors.append(f'{cid}: unknown row {r}')
        else:
            row2c[r].append(cid)
for r in drops:
    if r not in rows: errors.append(f'drop of unknown row {r}')
    if r in row2c: errors.append(f'dropped row {r} is also used')
unused = [r for r in rows if r not in row2c and r not in drops]
for r in unused:
    errors.append(f'unplaced row {r} ({rows[r]["name"]})')
if errors:
    print('\n'.join(errors)); sys.exit(1)

# ---------------------------------------------------------------- prereqs
assumed = collections.defaultdict(set)   # bracket name -> concepts that assume it
pre = {}
for cid, c in concepts.items():
    ps = set()
    for r in c['members']:
        for p in rows[r]['prereqs']:
            if p.startswith('['):
                t = BRACKET[p]
                if t is None:
                    assumed[p].add(cid)
                else:
                    ps.add(t)
            else:
                ps.update(row2c[p])
    ps.discard(cid)
    pre[cid] = ps
used_noedge = []                         # spec order, so notes and stats are deterministic
for a, b in noedge:
    if b in pre[a]:
        pre[a].discard(b); used_noedge.append((a, b))
    else:
        print(f'WARNING: NOEDGE {a} -> {b} not present')
for a, b in addedge:
    assert a in concepts and b in concepts, (a, b)
    pre[a].add(b)
for cid, ps in pre.items():
    for p in ps:
        if p not in concepts:
            sys.exit(f'{cid}: prereq {p} unresolved')

# cycles
def find_cycle():
    color = {c: 0 for c in concepts}; stack = []
    def dfs(u):
        color[u] = 1; stack.append(u)
        for v in sorted(pre[u]):
            if color[v] == 1:
                return stack[stack.index(v):] + [v]
            if color[v] == 0:
                r = dfs(v)
                if r: return r
        color[u] = 2; stack.pop(); return None
    for c in concepts:
        if color[c] == 0:
            r = dfs(c)
            if r: return r
    return None
sys.setrecursionlimit(10000)
cyc = find_cycle()
if cyc:
    print('CYCLE:', ' -> '.join(cyc)); sys.exit(1)

# Hasse reduction
memo = {}
def reach(u):
    if u in memo: return memo[u]
    s = set()
    for v in pre[u]:
        s.add(v); s |= reach(v)
    memo[u] = s; return s
hasse_removed = 0
red = {}
for cid in concepts:
    ps = pre[cid]
    keep = {p for p in ps if not any(p in reach(q) for q in ps if q != p)}
    hasse_removed += len(ps) - len(keep)
    red[cid] = keep

# ---------------------------------------------------------------- order within sections, global positions
for ch in chapters:
        for s in ch['sections']:
            ids = s['concepts']; inset = set(ids); out = []; placed = set()
            while len(out) < len(ids):
                for i in ids:
                    if i not in placed and all(q in placed or q not in inset for q in reach(i)):
                        out.append(i); placed.add(i); break
                else:
                    sys.exit('section topo failed ' + s['id'])
            s['concepts'] = out
# Book chapters are numbered 1..N in spec order; appendix chapters are not numbered, and their
# sections are the appendix's pages, numbered A.1, A.2, ... across the appendix's chapters.
pos = {}; k = 0
chap_num, sec_num = {}, {}
cn = 0; app_page = collections.Counter()
for ch in chapters:
    if ch['appendix']:
        ch['number'] = None; chap_num[ch['id']] = ch['appendix']
    else:
        cn += 1; chap_num[ch['id']] = cn; ch['number'] = cn
    for si, s in enumerate(ch['sections'], 1):
        if ch['appendix']:
            app_page[ch['appendix']] += 1; s['number'] = f'{ch["appendix"]}.{app_page[ch["appendix"]]}'
        else:
            s['number'] = f'{cn}.{si}'
        sec_num[s['id'] + '@' + ch['id']] = s['number']
        for cid in s['concepts']:
            pos[cid] = k; k += 1
viol = []
for cid in concepts:
    for p in red[cid]:
        if pos[p] > pos[cid]:
            viol.append((cid, p))
if viol:
    for a, b in viol:
        ca, cb = concepts[a], concepts[b]
        print(f'ORDER: {a} ({ca["chapter"]}/{ca["section"]}) needs {b} ({cb["chapter"]}/{cb["section"]})')
    sys.exit(1)

# ---------------------------------------------------------------- concept rows
def most_common(ts):
    cnt = collections.Counter(ts)
    best = max(cnt.values())
    return min((t for t in cnt if cnt[t] == best), key=TIERS.index)

out_concepts = []
split_rows = {r: cs for r, cs in row2c.items() if len(cs) > 1}
for cid, c in concepts.items():
    mem = [rows[r] for r in c['members']]
    first = mem[0]
    o = c['opts']
    srcs = [m['_source'] for m in mem]
    ciu_t = [m['tier'] for m in mem if m['_source'] == 'ciu']
    other_t = [m['tier'] for m in mem if m['_source'] != 'ciu']
    notes = []
    if ciu_t:
        tier = 'core' if 'core' in ciu_t else 'stretch'
        if other_t and any(t != tier for t in other_t):
            notes.append('Tier from CIU (' + ('required list' if tier == 'core' else 'optional list') + '); other sources say ' +
                         ', '.join(f'{m["_source"]} {m["tier"]}' for m in mem if m['_source'] != 'ciu') + '.')
    else:
        tier = most_common(other_t)
        if len(set(other_t)) > 1:
            notes.append('Source tiers differ (' + ', '.join(f'{m["_source"]} {m["tier"]}' for m in mem) + f'); reconciled to the most common, {tier}.')
    if 'tier' in o:
        # explicit tier in the spec overrides the reconciled one; the reconciling notes above give way to one note
        if o['tier'] != tier:
            notes = ['Tier set to ' + o['tier'] + ' in the spec (sources say ' + ', '.join(f'{m["_source"]} {m["tier"]}' for m in mem) + ')' +
                     (': ' + o['why'] if 'why' in o else '.')]
        elif 'why' in o:
            notes = ['Tier ' + tier + ': ' + o['why']]
        tier = o['tier']
    name = o.get('name', first['name'])
    stmt = o.get('stmt', first['statement'])
    kind = o.get('kind', first['kind'])
    aliases = []
    seen = {name.lower()}
    for m in mem:
        for a in [m['name']] + m['aliases']:
            if a.lower() not in seen:
                seen.add(a.lower()); aliases.append(a)
    if 'aliases' in o:
        aliases = [a.strip() for a in o['aliases'].split(',') if a.strip()]
    if len(mem) > 1:
        notes.insert(0, f'Merged {len(mem)} rows (' + ', '.join(m['id'] for m in mem) + ').')
    for m in mem:
        if m['id'] in split_rows:
            others = [x for x in split_rows[m['id']] if x != cid]
            notes.append(f'{m["id"]} also treats {", ".join(others)} (row split by granularity).')
    if 'note' in o:
        notes.append(o['note'])
    for (a, b) in used_noedge:
        if a == cid:
            notes.append(f'Edge to {b} dropped: {noedge_reason[(a, b)]}')
    for (a, b) in addedge:
        if a == cid:
            notes.append(f'Edge to {b} added: {addedge_reason[(a, b)]}')
    ass = sorted(k for k, v in assumed.items() if cid in v)
    if ass:
        notes.append('Assumes, untaught in the map: ' + ', '.join(x.strip('[]') for x in ass) + '.')
    treatments = [{'source': m['_source'], 'row': m['id'], 'locator': m['locator'], 'inventory': m['_file']} for m in mem]
    row = {'id': cid, 'name': name, 'kind': kind, 'statement': stmt, 'tier': tier}
    if c['appendix']:
        row['appendix'] = c['appendix']
    row.update({'chapter': c['chapter'], 'section': c['section'],
        'prereqs': sorted(red[cid], key=lambda x: pos[x]),
        'treatments': treatments, 'aliases': aliases,
        'open_prose': any(s in OPEN for s in srcs),
        'notes': ' '.join(notes),
    })
    out_concepts.append(row)
out_concepts.sort(key=lambda c: pos[c['id']])
cbyid = {c['id']: c for c in out_concepts}

# Tier propagation: a concept with no CIU row (and no explicit tier) is at most as advanced as the
# most basic concept resting on it. CIU-row concepts keep CIU's verdict; remaining inversions are reported.
has_ciu = {cid for cid, c in concepts.items() if any(rows[r]['_source'] == 'ciu' for r in c['members']) or 'tier' in c['opts']}
promoted = {}
changed = True
while changed:
    changed = False
    for c in out_concepts:
        for p in c['prereqs']:
            q = cbyid[p]
            if p in has_ciu:
                continue
            if TIERS.index(c['tier']) < TIERS.index(q['tier']):
                promoted[p] = (promoted[p][0] if p in promoted else q['tier'], c['id'])
                q['tier'] = c['tier']; changed = True
for p, (old, by) in promoted.items():
    q = cbyid[p]
    q['notes'] = (q['notes'] + ' ' if q['notes'] else '') + \
        f'Tier raised from {old} to {q["tier"]}: it is a prerequisite of {by} ({q["tier"]}).'

os.makedirs(OUT, exist_ok=True)
json.dump({
    'about': 'Merged concept map for cs-interview-prep-ultra: one row per concept, merged across the inventories in inventory/. '
             'Rows are in spec order (toc.json chapters, with appendix A\'s concepts where its chapters stood). '
             'A concept with an "appendix" field lives on that appendix\'s pages (curated links, not built as text); its chapter and section ids still name its group and page. '
             'treatments list every inventory row that teaches the concept; the judge picks a home later. '
             'dropped lists inventory rows that became no concept.',
    'counts': {'concepts': len(out_concepts), 'inventory_rows': len(rows), 'dropped_rows': len(drops)},
    'concepts': out_concepts,
    'dropped': [{'row': r, 'name': rows[r]['name'], 'locator': rows[r]['locator'], 'reason': drops[r]} for r in drops],
}, open(f'{OUT}/concepts.json', 'w'), indent=1, ensure_ascii=False)

# ---------------------------------------------------------------- toc
def sec_tier(ids):
    return most_common([cbyid[i]['tier'] for i in ids])

def toc_section(s, extra=None):
    ids = s['concepts']
    srcs = sorted({t['source'] for i in ids for t in cbyid[i]['treatments']}, key=list(ABBR).index)
    d = {'id': s['id'], 'number': s['number'], 'title': s['title']}
    d.update(extra or {})
    d.update({'concepts': ids, 'tier': sec_tier(ids), 'candidate_sources': srcs,
              'open_prose': any(cbyid[i]['open_prose'] for i in ids),
              'no_open_prose': [i for i in ids if not cbyid[i]['open_prose']],
              'folds': s['folds']})
    return d

def tier_counts(ids):
    tcnt = collections.Counter(cbyid[i]['tier'] for i in ids)
    return {t: tcnt[t] for t in TIERS if tcnt[t]}

book_chapters = [ch for ch in chapters if not ch['appendix']]
toc_chapters = []
for ch in book_chapters:
    tc = {'id': ch['id'], 'number': ch['number'], 'title': ch['title'], 'first_pass': ch['number'] <= 3,
          'sections': [toc_section(s) for s in ch['sections']]}
    tc['tier_counts'] = tier_counts([i for s in ch['sections'] for i in s['concepts']])
    toc_chapters.append(tc)

APP_ID = {'A': 'appendix-computer-systems', 'B': 'appendix-getting-the-job'}
toc_appendices = []
for a in appendices:
    pages = [toc_section(s, {'group': ch['id']}) for ch in a['chapters'] for s in ch['sections']]
    toc_appendices.append({
        'id': APP_ID.get(a['letter'], 'appendix-' + a['letter'].lower()), 'letter': a['letter'], 'title': a['title'],
        'kind': a['kind'], 'built': False,
        'note': 'Curated links appendix: each page lists the reader-facing links for its concepts, no text is written for it. '
                'The concepts stay in the concept map so prerequisite edges into them resolve; a book concept that rests on one '
                'points the reader to its page. Pages are grouped by the former chapters (group ids), which are not numbered book chapters.',
        'groups': [{'id': ch['id'], 'title': ch['title']} for ch in a['chapters']],
        'tier_counts': tier_counts([i for p in pages for i in p['concepts']]),
        'pages': pages,
    })
toc_appendices.append({
    'id': 'appendix-getting-the-job', 'letter': 'B', 'title': 'Getting the job', 'kind': 'reading', 'built': False,
    'note': "CIU's career sections, kept as one reading page with CIU's own lists and links (in inventory/ciu-links.json). No concepts, no exercises. Not part of the first build pass.",
    'locators': ['ciu:#update-your-resume', 'ciu:#interview-process--general-interview-prep',
                 'ciu:#be-thinking-of-for-when-the-interview-comes', 'ciu:#have-questions-for-the-interviewer',
                 'ciu:#once-youve-got-the-job'],
    'pages': [],
})
toc = {'about': 'Table of contents derived from concept-map/concepts.json. One book: chapters numbered 1..N, each made of sections; '
                'each section is one concept home (one page). Appendices follow: A is a curated links appendix whose pages (A.1, A.2, ...) '
                'hold concepts but are not built as text; B is a reading page with no concepts. '
                'Chapters with first_pass true are the first build pass. Section tier is the most common tier of its concepts (ties go to the more basic tier).',
       'chapters': toc_chapters, 'appendices': toc_appendices}
json.dump(toc, open(f'{OUT}/toc.json', 'w'), indent=1, ensure_ascii=False)

# ---------------------------------------------------------------- chapter dependencies
# Nodes are book chapters plus appendix A as one node (keyed by its letter).
def node(chid):
    a = next(ch['appendix'] for ch in chapters if ch['id'] == chid)
    return a or chid
nodes = [ch['id'] for ch in book_chapters] + [a['letter'] for a in appendices]
node_num = {ch['id']: ch['number'] for ch in book_chapters}
node_num.update({a['letter']: len(book_chapters) + 1 + i for i, a in enumerate(appendices)})
cdep = {n: set() for n in nodes}
for c in out_concepts:
    for p in c['prereqs']:
        a, b = node(c['chapter']), node(cbyid[p]['chapter'])
        if a != b: cdep[a].add(b)
cmemo = {}
def creach(u):
    if u in cmemo: return cmemo[u]
    s = set()
    for v in cdep[u]: s.add(v); s |= creach(v)
    cmemo[u] = s; return s
cred = {a: {b for b in bs if not any(b in creach(x) for x in bs if x != b)} for a, bs in cdep.items()}

# ---------------------------------------------------------------- toc.md
def badge(t): return f'[{t}]'
def md_section(s, L):
    srcs = ', '.join(SHORT[x] for x in s['candidate_sources'])
    op = '' if s['open_prose'] else ' · open prose: none'
    L.append(f'- **{s["number"]} {s["title"]}** {badge(s["tier"])} · {srcs}{op}')
    names = []
    for i in s['concepts']:
        c = cbyid[i]
        nm = c['name']
        if c['tier'] != s['tier']: nm += ' ' + badge(c['tier'])
        if not c['open_prose']: nm += ' (no open prose)'
        names.append(nm)
    L.append('  ' + '; '.join(names))
    if s['folds']:
        L.append(f'  *Folds:* {s["folds"]}')

L = ['# Table of contents', '',
     'Derived from the concept map (`concepts.json`). One book of numbered chapters; each numbered section is one page, the home of the concepts listed under it. '
     'Section tier badges give the most common tier of the section\'s concepts; a concept whose tier differs from its section\'s carries its own badge. '
     'Sources lists the inventories that teach the section\'s concepts: '
     + ', '.join(f'**{SHORT[k]}** = {v}' for k, v in ABBR.items()) + '. '
     '"Open prose: none" marks a section whose concepts are taught only by CIU links or by Erickson\'s NC notes, so its text has no open source yet.', '',
     'Chapters 1 to 3 (marked **first pass**) are the first build pass. The appendices are not built as text.', '']
tier_count = collections.Counter(c['tier'] for c in out_concepts)
for tc in toc_chapters:
    fp = ' · **first pass**' if tc['first_pass'] else ''
    mix = ' · '.join(f'{n} {t}' for t, n in tc['tier_counts'].items())
    L.append(f'## {tc["number"]}. {tc["title"]}{fp}'); L.append('')
    L.append(f'*Concepts: {mix}*'); L.append('')
    for s in tc['sections']:
        md_section(s, L)
    L.append('')
for ta in toc_appendices:
    if ta['kind'] == 'links':
        L.append(f'## Appendix {ta["letter"]} · {ta["title"]} (curated links, not built)'); L.append('')
        mix = ' · '.join(f'{n} {t}' for t, n in ta['tier_counts'].items())
        L.append(f'*Concepts: {mix}. Each page is a curated list of links for its concepts; book chapters that rest on them point here.*'); L.append('')
        gtitle = {g['id']: g['title'] for g in ta['groups']}
        cur = None
        for s in ta['pages']:
            if s['group'] != cur:
                cur = s['group']
                if L[-1] != '': L.append('')
                L.append(f'### {gtitle[cur]}'); L.append('')
            md_section(s, L)
        L.append('')
    else:
        L.append(f'## Appendix {ta["letter"]} · {ta["title"]} (reading page, not built)'); L.append('')
        L.append("CIU's career sections as one reading page: update your resume; interview process and general interview prep; "
                 "be thinking of for when the interview comes; have questions for the interviewer; once you've got the job. No concepts.")
        L.append('')
open(f'{OUT}/toc.md', 'w').write('\n'.join(L))

# ---------------------------------------------------------------- mermaid
def mnode(n): return f'C{node_num[n]}' if n in {ch['id'] for ch in book_chapters} else f'App{n}'
M = ['%% Chapter-level dependencies (Hasse-reduced). An arrow A --> B means chapter B uses concepts from chapter A.',
     '%% AppA is Appendix A (curated links, not built); chapters that use its concepts point to it.',
     'graph TD']
for ch in book_chapters:
    M.append(f'  C{ch["number"]}["{ch["number"]}. {ch["title"]}"]')
for a in appendices:
    M.append(f'  App{a["letter"]}["Appendix {a["letter"]}. {a["title"]}"]')
for a in sorted(cred, key=lambda x: node_num[x]):
    for b in sorted(cred[a], key=lambda x: node_num[x]):
        M.append(f'  {mnode(b)} --> {mnode(a)}')
M.append('  classDef first fill:#e8f0ff,stroke:#3a5bbf,stroke-width:2px;')
M.append('  classDef appendix fill:#f4f4f4,stroke:#888,stroke-dasharray:4 3;')
M.append('  class C1,C2,C3 first;')
if appendices:
    M.append('  class ' + ','.join(f'App{a["letter"]}' for a in appendices) + ' appendix;')
open(f'{OUT}/chapters.mmd', 'w').write('\n'.join(M) + '\n')

# ---------------------------------------------------------------- stats for report (dumped for the report writer)
all_secs = [s for tc in toc_chapters for s in tc['sections']] + [s for ta in toc_appendices for s in ta['pages']]
chapter_tier = {tc['id']: tc['tier_counts'] for tc in toc_chapters}
appendix_tier = {ta['letter']: ta['tier_counts'] for ta in toc_appendices if ta['pages']}
multi = [c for c in out_concepts if len(c['treatments']) > 1]
cross = [c for c in multi if len({t['source'] for t in c['treatments']}) > 1]
size_hist = collections.Counter(len(c['treatments']) for c in out_concepts)
src_count = collections.Counter(t['source'] for c in out_concepts for t in c['treatments'])
noprose = [c for c in out_concepts if not c['open_prose']]
inversions = [(c['id'], p, c['tier'], cbyid[p]['tier']) for c in out_concepts for p in c['prereqs']
              if TIERS.index(cbyid[p]['tier']) > TIERS.index(c['tier'])]
secsizes = collections.Counter(len(s['concepts']) for s in all_secs)
into_appendix = [(c['id'], p) for c in out_concepts if 'appendix' not in c for p in c['prereqs'] if 'appendix' in cbyid[p]]
json.dump({
    'concepts': len(out_concepts), 'rows': len(rows), 'drops': len(drops),
    'tier_count': {t: tier_count[t] for t in TIERS},
    'chapter_tier': chapter_tier, 'appendix_tier': appendix_tier,
    'multi': len(multi), 'cross': len(cross), 'size_hist': dict(sorted(size_hist.items())),
    'src_count': dict(sorted(src_count.items())),
    'noprose': len(noprose), 'inversions': inversions, 'split_rows': {r: v for r, v in split_rows.items()},
    'hasse_removed': hasse_removed, 'secsizes': dict(sorted(secsizes.items())),
    'inventories': FILES, 'gap_rows': sum(1 for r in rows.values() if r['_file'] == GAP),
    'open_sources': sorted(OPEN), 'short': SHORT, 'addedge': [list(x) for x in addedge],
    'used_noedge': [list(x) for x in used_noedge], 'assumed': {k: sorted(v) for k, v in sorted(assumed.items())},
    'promoted': {p: list(v) for p, v in promoted.items()},
    'into_appendix': into_appendix,
    'cred': {a: sorted(b, key=lambda x: node_num[x]) for a, b in cred.items()},
    'cdep': {a: sorted(b, key=lambda x: node_num[x]) for a, b in cdep.items()},
}, open(os.path.join(os.path.dirname(SPEC), 'stats.json'), 'w'), indent=1)
print('concepts', len(out_concepts), 'tiers', {t: tier_count[t] for t in TIERS}, 'hasse removed', hasse_removed,
      'multi', len(multi), 'cross', len(cross), 'noprose', len(noprose), 'inversions', len(inversions))
print('chapters', len(toc_chapters), 'appendices', ', '.join(f'{ta["letter"]} ({len(ta["pages"])} pages)' for ta in toc_appendices))
print('section sizes', dict(sorted(secsizes.items())))
for tc in toc_chapters:
    n = len(tc['sections'])
    if n < 3 or n > 8: print('   CHAPTER SIZE', tc['number'], tc['title'], n)
