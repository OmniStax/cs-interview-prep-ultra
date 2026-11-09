## Pass: section 2.1 Arrays and the list interface (2026-11-09)

Planned and built in one run (`briefs/section-build.md`), from `ch02/2.1/plan.md`, with chapter 1's pipeline. Model: claude-opus-5-5, high effort.

**How the text was made.** No source passage was typed. No shared tool read wikitext, so the section brings `readers.py`:
a wikitext reader for its two Wikipedia passages (headings, paragraphs joined over single newlines as MediaWiki renders them,
`;` and `*` lists, `:` lines, wikitables, `<syntaxhighlight>`, image lines, links kept as text, `nowrap`, `mono`, `ISBN`,
and `<ref>` citations set from their templates' fields as book footnotes), and the ODS block through `tools/read_latex.py`
with one step first (`eqnarray*` read as an aligned display). Wikipedia's citation numbers were computed over each whole
article and checked against the rendered revisions (Array 1–5 and 8; Pointer 12 and 13); a named citation used twice is a
second note with the same number, so every note has one marker. `tools/build_text.py` gained one backward-compatible branch:
a block whose `reader` is a function is read by it. 1.1 rebuilt from a frozen copy of the tools, before and after: `source.md`,
`text.html`, `footnotes.json`, `captions.json` byte-identical. `build_spec.py` holds placement, marks, three correction notes,
one display (the k-dimensional formula, which the article sets on an indented line) and an empty replacement table.

**What was fetched.** Wikimedia Commons refuses scripts the original files (429), so the three diagrams came from its
thumbnail service at 960 px: `media/ch02/wp-1d-array-diagram.png`, `wp-2d-array-diagram.png` (CC BY 4.0, Tropwine, credited
in the Sims' original captions) and `wp-array-of-array-storage.png` (public domain, credited in the photograph's caption).
ODS's `figs/list.ipe`, converted as the pseudocode edition's `figs-python/snarf-fig.py` converts it, rendered with
`iperender` to `media/ch02/ods-1-4-list.png`. Wikipedia's "C29 (C standard revision)" (revision 1382563440) for the C29
check; open-std.org and the Wayback Machine are refused by the proxy. Nothing appended to `sources/registry.json`.

**What was built.** Six blocks (Wikipedia Array: lead, addressing formulas with its two subsections, Efficiency, the
Iliffe paragraph; Wikipedia Pointer: C arrays; ODS: The List Interface), each with `data-source`/`data-locator`; ten
Wikipedia citations as book notes; errata 15 and 16 as correction notes and a new one in ODS Exercise 2.5's prompt
("{0, …, a.length}"). Three concepts (`array`, `pointer-arithmetic`, `list-interface`), two edges
(`pointer-arithmetic → array`; `list-interface → interface-vs-implementation`, new) and four forms (address = B + c·i in one,
two and k dimensions; a[i] ≡ *(a + i)) through `ost`. Three Sims, no code panel (properties): `sim-address` (still: i, c,
first index 0 | 1 | 31, B moving off the array; erratum 15 visible), `sim-row-major` (still: int a[2][3] | A[3][4], the grid
and its row-major memory), `sim-list` (moving: the eight List and Deque operations on ODS Figure 1.4's values, one
displaced value per beat, values moved against n − i). One photograph (the Iliffe vector). The terms pass: 104 mentions,
94 marked, 10 left in ink (another sense: "lists and strings", "the term "array"", "array data type", associative and
abstract arrays, a language's implementation, a library's, bit array, combinations). Exercises: three Busbee true/false
cards, three code cards (ODS 2.5 rotate, AI tests that keon's three rotates and TheAlgorithms' pass when run isolated;
Exercism matrix, canonical tests; ODS 1.6's List part, AI tests from a seeded sequence answered by a Python list), each
starter holding the function its tests call; one NC card (MIT 6.006 S20 ps1 1-2) in `exercises-nc.json`.

**Checks.** `ost check --section 2.1`: ok. `npm run check:content` (this book): no errors, the two by-design warnings
(1.1, 1.4). `npm run check:code` (this book): 2.1's three Python references pass; the one error is 1.6's c2 reference
running past its time limit (not this section's; the machine was loaded by parallel builds). The JavaScript references
pass all their tests under node. Playwright on port 4501 (own Vite cache), light and dark at 2×: every figure at its
opening state, its choices and slider extremes, `sim-list` mid-move and at rest for each kind of operation, its original
toggle; no console errors, no failed images, no KaTeX errors. Screenshots in the session scratchpad, `sec02.1/`.

**Deviations from the plan.** None of substance: `sim-row-major`'s link from the grid is drawn under the grid; the C
listings are lone `<pre>` (plan question 2).

**For the chapter pass.** The wikitext reader belongs in `tools/` once 2.3 and 2.5 show what their passages need; whether
Wikipedia's citations are book notes should be one decision for the chapter. ODS camel case: the edition writes add_first,
`read_latex.py` keeps addFirst (plan question 4). The `list-interface → interface-vs-implementation` edge goes into
`tools/map/map.spec`. 1.1's notes say ODS Exercise 6 is held for chapters 3, 5 and 8; its List part is now in 2.1. ODS
Exercise 2.5 comes from ODS's arrays chapter, which is 2.2's. The C29 sentence stands; a person should still read WG14
N3517. App: the article's `<table>` has no style (the byte table and 1.6's table render without rules or padding).
