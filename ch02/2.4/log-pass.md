## Pass: section 2.4 Prefix sums and difference arrays (2026-11-09)

Planned and built in one run (`briefs/section-build.md`; `ch02/2.4/plan.md`, its nine questions decided there), on 1.5's
pipeline. Model: claude-opus-5-5, high effort.

**How the text was made.** No Chinese was typed. OI Wiki's `basic/prefix-sum.md` (pin c794414) is cut by
`tools/build_translation.py` into four blocks; the English is `translation.md`, element for element, parity clean. The page
writes MkDocs boxes (`???+ tip "规定"`), tabbed code and an image, which 1.5's page did not, so a new shared module,
`tools/oiwiki_boxes.py`, installs their reading into build_translation without changing it: a box is a `div.note` with its
title as eyebrow and is compared element for element; a box of code only is a code element (a `[[slot]]` in the
translation); an image is a slot, lifted after its box with any slot inside it; a block may leave out boxes by title
(`drop_boxes`); a link whose text is inline code is a link. `build_translation.py` itself is untouched; 1.5 built through
the module in a scratch copy gives byte-identical `text.html`, `source.md`, `footnotes.json` and `captions.json`. Run it as
`python3 -I tools/oiwiki_boxes.py ch02/2.4`.

**Code.** TheAlgorithms `PrefixSum` (`__init__`, `get_sum`; docstrings and `contains_sum` left out, the spec says why) is
read from the cache into a code set where OI Wiki's 参考实现 box stood; Java, C++ and JavaScript are AI translations,
compiled and run against the Python's doctest cases (all 7 match). doocs 0304 and 0370 Solution 1 in all four languages
(doocs prints them) are written into `figures.js` by `inline_code.py` (LeetCode's harness comment after 0304's classes
dropped). The doocs Python and TheAlgorithms' doctests (13/13) were run isolated (decision 17); 0304 on OI Wiki's matrix
gives the figure's S table exactly.

**What was built.** Four translated blocks with `data-ai`; the Convention, Example and Properties boxes as notes; erratum 20
as correction `err-2d-example`; links to Sections 40.4 (inclusion–exclusion) and 30.2 (Fenwick tree), both unbuilt.
Concepts `prefix-sums` (typed `key`), `prefix-sums-2d`, `difference-array`, `difference-array-2d`, nine forms, five edges
(`prefix-sums → array` added once 2.1 had staged `array`). Two debugger Sims: `sim-prefix-2d` (OI Wiki's figure behind the
original toggle, rendered to `media/ch02/oiwiki-prefix-sum-2d.png`; blue and red as facts; 12 cells then a query stepped
into its four terms; three queries, the whole matrix the padding case) and `sim-range-add` (canonical Java so the prefix
pass steps cell by cell; two inputs, one where the guard skips the write past the end). Referents l, r, c, i. Terms pass:
48 mentions marked, 1 left in ink ("an implementation"), two "difference array" mentions in the 2D block marked
`difference-array-2d`. No exercises (config: none for any concept).

**Checks.** `ost check --section 2.4`: ok. `npm run check:content` (content dir `/home/user/OmniStax/omnistax-content`):
no errors; the two warnings are 1.1's and 1.4's. `npm run check:code`: no errors (2.4 has no code card). Playwright on
port 4504 (own Vite cache), light and dark at 2×: both figures stepped (every stop kind: pad, cells with and without
padding, query terms, updates with and without the guard, the pass into each cell, the end), the original toggle; no
console errors. Shots in the session scratchpad, `sec24/`.

**Deviations from the plan.** None of substance: the 2D figure's legend line and the range figure's rule line are canvas
text, as 1.5's readout; block labels avoid `+=`/`−=` (the note sets them as maths).

**For the chapter pass.** Fold `tools/oiwiki_boxes.py` into `build_translation.py` (2.3 may need the same boxes). Add the
two forced scenarios to `translation-notes.md` and `ch02/config.md` (zh.cppreference → en.cppreference; OI Wiki's own
links → this book's sections) and the new glossary rows (plan.md, Terms) to `glossary.en.json`. Add 30.2 and 40.4 to
RULES' "Links to sections not yet built". `book.json` `authors` does not yet name doocs or TheAlgorithms (their `sources`
rows exist).
