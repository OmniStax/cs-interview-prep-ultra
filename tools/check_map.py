#!/usr/bin/env python3
"""Validate concept-map/concepts.json (and concept-map/toc.json when present).

Checks, for concepts.json:
  - ids are unique book-level kebab slugs with no source prefix;
  - every row has the required fields, a valid kind and tier;
  - prereqs resolve, contain no self-loops, form no cycle, and are Hasse-reduced
    (no prereq is reachable through another prereq of the same concept);
  - every treatment names an inventory row that exists, and its locator and source
    match that row; open_prose agrees with the treatments;
  - every inventory row is used by some treatment or listed under "dropped";
  - inventory/gap.json rows (source "gap") carry their real source in the id prefix: the prefix must be a
    registry locator prefix, the id must be the locator with spaces as underscores, and the locator must
    resolve in sources/_cache/<source id>/ (file, and heading or section where the locator names one).
And for toc.json, when present:
  - the shape is one book: flat "chapters" numbered 1..N (sections N.1, N.2, ...) plus "appendices"
    (letters A, B, ...; pages A.1, A.2, ...); there are no parts;
  - every concept sits in exactly one chapter section or appendix page, and its chapter/section
    (and, for appendix pages, appendix and group) fields agree;
  - book order respects prerequisites (a prereq never comes after its dependant) among chapter
    concepts and within each appendix; chapter concepts may rest on appendix concepts (the reader
    is pointed to the appendix page);
  - section tags (candidate_sources, open_prose) agree with the concepts.

Usage: python3 tools/check_map.py [--quiet]     Exit status 1 on any error.
"""
import json, os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = os.path.join(ROOT, 'concept-map')
INV = os.path.join(ROOT, 'inventory')
INVENTORIES = ['ciu', 'cpa-a', 'cpa-b', 'jeffe', 'jeffe-notes', 'ods', 'sdp', 'gap']
GAP = 'gap'                          # inventory whose rows name their real source in the id prefix
KINDS = {'definition', 'axiom', 'result', 'idea', 'skill'}
TIERS = ['core', 'stretch', 'contest']
# Sources whose prose may be used (METHOD §0, rulings 12 and 15). Keep in step with tools/map/build.py.
OPEN = {'cpa', 'jeffe', 'ods', 'sdp',
        'wikipedia', 'wikibooks', 'wp-sysdesign', 'dsa-dummies', 'doocs-leetcode', 'oiwiki', 'opendsa',
        'algo-explanation', 'icc', 'trekhleb-jsalgo', 'mcs2018', 'aspnes-202', 'anfp', 'dmoi3', 'appcomb',
        'csci30', 'lt-csbu', 'holden-acs', 'aosa', 'raft-site'}
SOURCES = {'ciu', 'cpa', 'jeffe', 'jeffe-notes', 'ods', 'sdp'}
CACHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sources', '_cache')
REGISTRY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sources', 'registry.json')
SLUG = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
REQUIRED = {'id': str, 'name': str, 'kind': str, 'statement': str, 'tier': str, 'chapter': str,
            'section': str, 'prereqs': list, 'treatments': list, 'aliases': list, 'open_prose': bool, 'notes': str}

errors, warnings = [], []
def err(msg): errors.append(msg)
def warn(msg): warnings.append(msg)


def registry_prefixes():
    """Locator prefix (text before the first ':' of a registry row's locator scheme) -> source id."""
    reg = json.load(open(REGISTRY))
    return {s['locator'].split(':', 1)[0]: s['id'] for s in reg['sources'] if s.get('locator')}


def load_inventories():
    rows = {}
    pfx = registry_prefixes()
    for f in INVENTORIES:
        d = json.load(open(os.path.join(INV, f + '.json')))
        for r in d['concepts']:
            src = d['source']
            if f == GAP:
                p = r['id'].split(':', 1)[0]
                if p not in pfx:
                    err(f'gap row {r["id"]}: prefix {p} is not a registry locator prefix'); continue
                src = pfx[p]
            if r['id'] in rows: err(f'duplicate inventory row id {r["id"]}')
            rows[r['id']] = (f, src, r)
    return rows


# ---- locator resolution against the source caches (gap rows)
def _norm(t):
    t = re.sub(r"<[^>]+>|'''|''|\[\[|\]\]|\{\{[^}]*\}\}", '', t)
    return re.sub(r'[\s_]+', ' ', t).strip().lower()

def _wiki_headings(path):
    return {_norm(m.group(1)) for m in re.finditer(r'^=+\s*(.*?)\s*=+\s*$', open(path, encoding='utf-8').read(), re.M)}

def _md_headings(path):
    return {_norm(m.group(1)) for m in re.finditer(r'^#{1,6}\s+(.*?)\s*$', open(path, encoding='utf-8').read(), re.M)}

def _rst_headings(path):
    L = open(path, encoding='utf-8').read().split('\n')
    return {_norm(L[i]) for i in range(len(L) - 1) if L[i].strip() and re.match(r'^([=\-~^"\'`#*+])\1{2,}\s*$', L[i + 1])}

def _wiki_file(cache_dir, title):
    meta = json.load(open(os.path.join(cache_dir, '_meta.json')))
    t = title.replace('_', ' ')
    for k, v in meta.items():
        if k == t or v.get('requested') == t:
            return os.path.join(cache_dir, v.get('file') or (k.replace(' ', '_') + '.wiki'))
    return None

def resolve_locator(src, loc):
    """Return None if the locator resolves in the source cache, else a reason."""
    d = os.path.join(CACHE, src)
    if not os.path.isdir(d): return f'no cache directory sources/_cache/{src}'
    body = loc.split(':', 1)[1]
    path, _, anchor = body.partition('#')
    if src in ('wikipedia', 'wp-sysdesign', 'wikibooks'):
        if src == 'wikibooks':
            f = os.path.join(d, path.replace('/', '_') + '.wiki')
        else:
            f = _wiki_file(d, path)
        if not f or not os.path.exists(f): return f'article {path} not cached'
        if anchor and _norm(anchor) not in _wiki_headings(f): return f'heading {anchor} not in {os.path.basename(f)}'
        return None
    if src == 'doocs-leetcode':
        hits = [os.path.join(r, 'README_EN.md') for r, _, fs in os.walk(os.path.join(d, 'solution'))
                if os.path.basename(r).startswith(path + '.') and 'README_EN.md' in fs]
        if not hits: return f'problem {path} not cached'
        if anchor and _norm(anchor) not in _md_headings(hits[0]): return f'heading {anchor} not in {path}'
        return None
    if src == 'oiwiki':
        f = os.path.join(d, 'docs', path + '.md')
        if not os.path.exists(f): return f'page {path} not cached'
        if anchor and _norm(anchor) not in _md_headings(f): return f'heading {anchor} not in {path}'
        return None
    if src == 'opendsa':
        f = os.path.join(d, 'RST', 'en', path + '.rst')
        if not os.path.exists(f): return f'module {path} not cached'
        if anchor and _norm(anchor) not in _rst_headings(f): return f'heading {anchor} not in {path}'
        return None
    if src == 'trekhleb-jsalgo':
        f = os.path.join(d, path)
        if not os.path.exists(f): return f'file {path} not cached'
        if anchor and _norm(anchor) not in _md_headings(f): return f'heading {anchor} not in {path}'
        return None
    if src in ('dsa-dummies',):
        return None if os.path.exists(os.path.join(d, path)) else f'file {path} not cached'
    if src == 'algo-explanation':
        return None if os.path.exists(os.path.join(d, 'en', path + '.md')) else f'topic {path} not cached'
    if src == 'icc':
        return None if os.path.isdir(os.path.join(d, path)) else f'challenge {path} not cached'
    if src in ('dmoi3', 'appcomb'):
        f = os.path.join(d, 'ptx' if src == 'dmoi3' else 'source', path + '.ptx')
        if not os.path.exists(f): return f'section {path} not cached'
        titles = {_norm(t) for t in re.findall(r'<title>(.*?)</title>', open(f, encoding='utf-8').read())}
        if anchor and _norm(anchor) not in titles: return f'title {anchor} not in {path}'
        return None
    if src == 'csci30':
        f = os.path.join(d, path + '.tex')
        if not os.path.exists(f): return f'chapter {path} not cached'
        secs = {_norm(t) for t in re.findall(r'\\(?:sub)*section\*?\{(.*?)\}', open(f, encoding='utf-8').read())}
        if anchor and _norm(anchor) not in secs: return f'section {anchor} not in {path}'
        return None
    if src in ('mcs2018', 'aspnes-202', 'anfp', 'lt-csbu'):
        txt = ''.join(open(os.path.join(d, x), encoding='utf-8', errors='replace').read()
                      for x in sorted(os.listdir(d)) if x.endswith('.txt') and x != 'FETCHED.txt')
        num = re.escape(path)
        pat = {'anfp': r'^Section ' + num + r':', 'lt-csbu': r'_' + path.replace('.', '_0') + r'_'}.get(src, r'^\s*' + num + r'\s+\S')
        if src == 'lt-csbu':
            ok = any(re.search(pat, x) for x in os.listdir(d))
        else:
            ok = re.search(pat, txt, re.M)
        return None if ok else f'section {path} not found in the cached text'
    if src == 'aosa':
        return None if os.path.exists(os.path.join(d, 'docs', 'en', path + '.html')) else f'chapter {path} not cached'
    if src == 'raft-site':
        return None if os.path.exists(os.path.join(d, path)) else f'file {path} not cached'
    return f'no resolver for source {src}'


def check_gap_rows(rows):
    for rid, (f, src, r) in rows.items():
        if f != GAP: continue
        if rid != r['locator'].replace(' ', '_'): err(f'gap row {rid}: id is not its locator with spaces as underscores ({r["locator"]})')
        if r['locator'].split(':', 1)[0] != rid.split(':', 1)[0]: err(f'gap row {rid}: locator prefix differs from the id prefix')
        if src not in OPEN: err(f'gap row {rid}: source {src} is not open prose')
        why = resolve_locator(src, r['locator'])
        if why: err(f'gap row {rid}: locator does not resolve: {why}')


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
        if 'part' in c: err(f'{cid}: has a part field (the book has no parts)')
        if 'appendix' in c and not (isinstance(c['appendix'], str) and re.match(r'^[A-Z]$', c['appendix'])):
            err(f'{cid}: appendix should be a capital letter, got {c["appendix"]!r}')

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


def check_section(s, ids, by_id):
    if not ids: err(f'section {s.get("id")} has no concepts')
    srcs = set()
    for cid in ids:
        if cid in by_id: srcs |= {t['source'] for t in by_id[cid]['treatments']}
    if set(s.get('candidate_sources', [])) != srcs:
        err(f'section {s.get("id")}: candidate_sources {s.get("candidate_sources")} != {sorted(srcs)}')
    op = any(by_id[i]['open_prose'] for i in ids if i in by_id)
    if s.get('open_prose') != op: err(f'section {s.get("id")}: open_prose tag {s.get("open_prose")} != {op}')
    if s.get('tier') not in TIERS: err(f'section {s.get("id")}: bad tier')


def check_toc(toc, by_id):
    if 'parts' in toc: err('toc.json has "parts"; the book is flat chapters plus appendices')
    chapters = toc.get('chapters')
    appendices = toc.get('appendices')
    if not isinstance(chapters, list): err('toc.json: "chapters" must be a list'); chapters = []
    if not isinstance(appendices, list): err('toc.json: "appendices" must be a list'); appendices = []
    seen = collections.Counter()
    book_order = []                       # concepts of numbered chapters, in book order
    app_order = collections.defaultdict(list)
    for n, ch in enumerate(chapters, 1):
        if ch.get('number') != n: err(f'chapter {ch.get("id")}: number {ch.get("number")}, expected {n}')
        if ch.get('first_pass') != (n <= 3): err(f'chapter {ch.get("id")}: first_pass should be {n <= 3}')
        if 'parts' in ch or 'part' in ch: err(f'chapter {ch.get("id")}: carries a part')
        for k, s in enumerate(ch.get('sections', []), 1):
            if s.get('number') != f'{n}.{k}': err(f'section {s.get("id")}: number {s.get("number")}, expected {n}.{k}')
            ids = s.get('concepts', [])
            for cid in ids:
                seen[cid] += 1; book_order.append(cid)
                c = by_id.get(cid)
                if c is None:
                    err(f'toc section {s.get("id")}: unknown concept {cid}'); continue
                if 'appendix' in c: err(f'{cid}: has appendix {c["appendix"]} but sits in chapter {n}')
                for k2, v in (('chapter', ch['id']), ('section', s['id'])):
                    if c[k2] != v: err(f'{cid}: {k2} is {c[k2]}, toc puts it in {v}')
            check_section(s, ids, by_id)
    letters = []
    for a in appendices:
        L = a.get('letter'); letters.append(L)
        if not (isinstance(L, str) and re.match(r'^[A-Z]$', L)): err(f'appendix {a.get("id")}: bad letter {L!r}'); continue
        if a.get('built') is not False: err(f'appendix {L}: built should be false')
        if a.get('kind') not in ('links', 'reading'): err(f'appendix {L}: bad kind {a.get("kind")!r}')
        groups = {g['id'] for g in a.get('groups', [])}
        pages = a.get('pages', [])
        if a.get('kind') == 'links' and not pages: err(f'appendix {L}: a links appendix needs pages')
        for k, s in enumerate(pages, 1):
            if s.get('number') != f'{L}.{k}': err(f'appendix page {s.get("id")}: number {s.get("number")}, expected {L}.{k}')
            if groups and s.get('group') not in groups: err(f'appendix page {s.get("id")}: group {s.get("group")} not in the appendix groups')
            ids = s.get('concepts', [])
            for cid in ids:
                seen[cid] += 1; app_order[L].append(cid)
                c = by_id.get(cid)
                if c is None:
                    err(f'appendix page {s.get("id")}: unknown concept {cid}'); continue
                if c.get('appendix') != L: err(f'{cid}: appendix is {c.get("appendix")}, toc puts it in appendix {L}')
                for k2, v in (('chapter', s.get('group')), ('section', s['id'])):
                    if c[k2] != v: err(f'{cid}: {k2} is {c[k2]}, toc puts it in {v}')
            check_section(s, ids, by_id)
    if letters != [chr(ord('A') + i) for i in range(len(letters))]: err(f'appendix letters {letters} are not A, B, ... in order')
    for cid in by_id:
        if seen[cid] == 0: err(f'{cid}: in no toc section or appendix page')
        elif seen[cid] > 1: err(f'{cid}: in {seen[cid]} toc sections or appendix pages')
    for order in [book_order] + list(app_order.values()):
        pos = {cid: i for i, cid in enumerate(order)}
        for cid in order:
            c = by_id.get(cid)
            if c is None: continue
            for p in c['prereqs']:
                if p in pos and pos[p] > pos[cid]:
                    err(f'order: {cid} ({c["section"]}) comes before its prereq {p} ({by_id[p]["section"]})')
    # tier inversions are allowed but reported
    for cid, c in by_id.items():
        for p in c['prereqs']:
            if p in by_id and TIERS.index(by_id[p]['tier']) > TIERS.index(c['tier']):
                warn(f'tier inversion: {cid} ({c["tier"]}) rests on {p} ({by_id[p]["tier"]})')


def main():
    quiet = '--quiet' in sys.argv
    rows = load_inventories()
    check_gap_rows(rows)
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
