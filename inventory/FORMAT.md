# Concept inventory format

One file per source, `inventory/<source id>.json`: an object
`{"source": "<id>", "concepts": [...]}`. Rows describe what **that source**
teaches. No merging across sources happens here.

```json
{
  "id": "cpa:dijkstra",
  "name": "Dijkstra's algorithm",
  "kind": "result",
  "statement": "On a graph with non-negative edge weights, repeatedly settling the unsettled vertex of least tentative distance and relaxing its out-edges yields all shortest-path distances from the source.",
  "locator": "cpa:graph/dijkstra#algorithm",
  "prereqs": ["cpa:sssp-problem", "cpa:edge-relaxation"],
  "aliases": ["Dijkstra"],
  "tier": "core",
  "has_code": true,
  "exercises": 0,
  "notes": ""
}
```

- `kind` is one of root RULES.md item 6's five: definition | axiom | result |
  idea | skill. An algorithm is usually a result (its correctness and
  cost are claims). An implementation technique is a skill.
- **Granularity:** a concept is something an exercise could test on its
  own. Most articles or sections give 2 to 8. Don't make one row per
  paragraph, and don't make one row per article.
- `prereqs` point to ids in the same file, or to plain names in brackets
  (`"[binary heap]"`) for things this source assumes without teaching.
  Hasse-reduce them: list only the direct prerequisites.
- `tier`: `core` = asked in typical software interviews (CIU's required
  list); `stretch` = asked at harder interviews or common in contests
  (DSU, segment tree, KMP, topological sort); `contest` = competitive
  programming only.
- `exercises`: how many exercises the source prints at that locator.
  `0` where it only links to external judges (cp-algorithms' practice
  lists count as 0, with the count of links in `notes`).
- **The gap inventory** `inventory/gap.json` is the one exception to "one file per
  source": its `source` is `"gap"`, and each row's id and locator start with the
  real source's locator prefix from `sources/registry.json` (`wikipedia:`,
  `doocs-leetcode:`, `oiwiki:`, ...). The id is the locator with spaces as
  underscores. `tools/map/build.py` takes each row's source from that prefix, and
  `tools/check_map.py` checks that the locator resolves in `sources/_cache/<id>/`.
