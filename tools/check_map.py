#!/usr/bin/env python3
"""Validate concept-map/concepts.json (and concept-map/toc.json when present).

Checks, for concepts.json:
  - ids are unique book-level kebab slugs with no source prefix;
  - every row has the required fields, a valid kind and tier;
  - prereqs resolve, contain no self-loops, form no cycle, and are Hasse-reduced
    (no prereq is reachable through another prereq of the same concept);
  - every treatment names an inventory row that exists, and its locator and source
    match that row; open_prose agrees with the treatments;
  - every inventory row is used by some treatment or listed under "dropped".
And for toc.json, when present:
  - every concept sits in exactly one section and its part/chapter/section fields agree;
  - book order respects prerequisites (a prereq never comes after its dependant);
  - section tags (candidate_sources, open_prose) agree with the concepts.

Usage: python3 tools/check_map.py [--quiet]     Exit status 1 on any error.
"""
import json, os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = os.path.join(ROOT, 'concept-map')
INV = os.path.join(ROOT, 'inventory')
INVENTORIES = ['ciu', 'cpa-a', 'cpa-b', 'jeffe', 'jeffe-notes', 'ods', 'sdp']
KINDS = {'definition', 'axiom', 'result', 'idea', 'skill'}
TIERS = ['core', 'stretch', 'contest']
OPEN = {'cpa', 'jeffe', 'ods', 'sdp'}
SOURCES = {'ciu', 'cpa', 'jeffe', 'jeffe-notes', 'ods', 'sdp'}
SLUG = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
REQUIRED = {'id': str, 'name': str, 'kind': str, 'statement': str, 'tier': str, 'part': str, 'chapter': str,
            'section': str, 'prereqs': list, 'treatments': list, 'aliases': list, 'open_prose': bool, 'notes': str}

errors, warnings = [], []
def err(msg): errors.append(msg)
def warn(msg): warnings.append(msg)


def load_inventories():
    rows = {}
    for f in INVENTORIES:
        d = json.load(open(os.path.join(INV, f + '.json')))
        for r in d['concepts']:
            rows[r['id']] = (f, d['source'], r)
    return rows


def check_concepts(data, rows):
    concepts = data.get('concepts')
    if not isinstance(concepts, list):
        err('concepts.json: top-level "concepts" must be a list'); return {}
    by_id = {}
    for i, c in enumerate(concepts):
        cid = c.get('id', f'<row {i}>')
        for k, t in REQUIRED.items():
            if k not in c: err(f'{cid}: missing field {k}')
            elif not isinstance(c[k], t): err(f'{cid}: field {k} should be {t.__name__}')
        if cid in by_id: err(f'duplicate id {cid}')
        by_id[cid] = c
        if not SLUG.match(str(cid)): err(f'{cid}: id is not a kebab slug')
        if ':' in str(cid) or any(str(cid).startswith(s + '-') and s in ('ciu', 'cpa', 'ods', 'sdp') for s in SOURCES):
            err(f'{cid}: id carries a source prefix')
        if c.get('kind') not in KINDS: err(f'{cid}: bad kind {c.get("kind")!r}')
        if c.get('tier') not in TIERS: err(f'{cid}: bad tier {c.get("tier")!r}')
        if not str(c.get('statement', '')).strip(): err(f'{cid}: empty statement')

    # prerequisites
    for cid, c in by_id.items():
        ps = c.get('prereqs', [])
        if len(ps) != len(set(ps)): err(f'{cid}: duplicate prereqs')
        for p in ps:
            if p == cid: err(f'{cid}: lists itself as a prereq')
            elif p not in by_id: err(f'{cid}: prereq {p} does not resolve')
    graph = {cid: [p for p in c.get('prereqs', []) if p in by_id and p != cid] for cid, c in by_id.items()}
    color = dict.fromkeys(graph, 0); cyclic = False
    sys.setrecursionlimit(20000)
    def dfs(u, path):
        nonlocal cyclic
        color[u] = 1; path.append(u)
        for v in graph[u]:
            if color[v] == 1:
                err('cycle: ' + ' -> '.join(path[path.index(v):] + [v])); cyclic = True
            elif color[v] == 0:
                dfs(v, path)
        color[u] = 2; path.pop()
    for u in graph:
        if color[u] == 0: dfs(u, [])
    if not cyclic:
        reach = {}
        def r(u):
            if u not in reach:
                s = set()
                for v in graph[u]: s.add(v); s |= r(v)
                reach[u] = s
            return reach[u]
        for cid, ps in graph.items():
            for p in ps:
                via = [q for q in ps if q != p and p in r(q)]
                if via: err(f'{cid}: prereq {p} is not Hasse-reduced (reachable through {via[0]})')

    # treatments
    used = set()
    for cid, c in by_id.items():
        ts = c.get('treatments', [])
        if not ts: err(f'{cid}: no treatments')
        for t in ts:
            row = t.get('row'); loc = t.get('locator')
            if row not in rows:
                err(f'{cid}: treatment row {row} not in any inventory'); continue
            f, src, r = rows[row]
            used.add(row)
            if t.get('inventory') not in (None, f): err(f'{cid}: treatment {row} names inventory {t.get("inventory")}, row is in {f}')
            if t.get('source') != src: err(f'{cid}: treatment {row} source {t.get("source")} != {src}')
            if loc != r['locator']: err(f'{cid}: treatment {row} locator {loc} != inventory locator {r["locator"]}')
        expect = any(t.get('source') in OPEN for t in ts)
        if c.get('open_prose') != expect: err(f'{cid}: open_prose is {c.get("open_prose")}, treatments say {expect}')

    # coverage of inventory rows
    dropped = {d['row']: d for d in data.get('dropped', [])}
    for row, d in dropped.items():
        if row not in rows: err(f'dropped row {row} not in any inventory')
        if row in used: err(f'dropped row {row} is also a treatment')
        if not d.get('reason'): err(f'dropped row {row} has no reason')
    for row in rows:
        if row not in used and row not in dropped:
            err(f'inventory row {row} is neither a treatment nor dropped')
    return by_id


def check_toc(toc, by_id):
    seen = collections.Counter(); order = []
    for p in toc.get('parts', []):
        for ch in p.get('chapters', []):
            for s in ch.get('sections', []):
                ids = s.get('concepts', [])
                if not ids: err(f'section {s.get("id")} has no concepts')
                srcs = set()
                for cid in ids:
                    seen[cid] += 1; order.append(cid)
                    c = by_id.get(cid)
                    if c is None:
                        err(f'toc section {s.get("id")}: unknown concept {cid}'); continue
                    for k, v in (('part', p['id']), ('chapter', ch['id']), ('section', s['id'])):
                        if c[k] != v: err(f'{cid}: {k} is {c[k]}, toc puts it in {v}')
                    srcs |= {t['source'] for t in c['treatments']}
                if set(s.get('candidate_sources', [])) != srcs:
                    err(f'section {s.get("id")}: candidate_sources {s.get("candidate_sources")} != {sorted(srcs)}')
                op = any(by_id[i]['open_prose'] for i in ids if i in by_id)
                if s.get('open_prose') != op: err(f'section {s.get("id")}: open_prose tag {s.get("open_prose")} != {op}')
                if s.get('tier') not in TIERS: err(f'section {s.get("id")}: bad tier')
    for cid in by_id:
        if seen[cid] == 0: err(f'{cid}: in no toc section')
        elif seen[cid] > 1: err(f'{cid}: in {seen[cid]} toc sections')
    pos = {cid: i for i, cid in enumerate(order)}
    for cid, c in by_id.items():
        for p in c['prereqs']:
            if p in pos and cid in pos and pos[p] > pos[cid]:
                err(f'order: {cid} ({c["section"]}) comes before its prereq {p} ({by_id[p]["section"]})')
    # tier inversions are allowed but reported
    for cid, c in by_id.items():
        for p in c['prereqs']:
            if p in by_id and TIERS.index(by_id[p]['tier']) > TIERS.index(c['tier']):
                warn(f'tier inversion: {cid} ({c["tier"]}) rests on {p} ({by_id[p]["tier"]})')


def main():
    quiet = '--quiet' in sys.argv
    rows = load_inventories()
    data = json.load(open(os.path.join(MAP, 'concepts.json')))
    by_id = check_concepts(data, rows)
    tp = os.path.join(MAP, 'toc.json')
    if os.path.exists(tp):
        check_toc(json.load(open(tp)), by_id)
    if not quiet:
        for w in warnings: print('warning:', w)
    for e in errors: print('error:', e)
    n_edges = sum(len(c['prereqs']) for c in by_id.values())
    print(f'{len(by_id)} concepts, {n_edges} prerequisite edges, {len(rows)} inventory rows: '
          f'{len(errors)} errors, {len(warnings)} warnings')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
