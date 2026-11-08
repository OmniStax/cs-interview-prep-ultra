# CS Interview Prep Ultra: the book's rules

Status: **draft for review**, 2026-11-08. Nothing here is built. This is the file root `RULES.md` item 18 asks for: what is true of this book and of no other. The agreed method behind it is `METHOD.md` (licences §0, tools §1, figures §2, colour §3, organisation §4 with decisions 1–18 in §4.4, one explanation per concept §5, finder and judge §6); where this file and METHOD differ, METHOD's numbered decisions win until this file is agreed. The colour plan is `COLOR.md` beside this file (root item 22). A chapter's decisions are in its `config.md`, its findings in its `exploration.md`. The `book.json` rows to create after review are drafted in `book-json-proposal.md`; `book.json`, `chapter.json` and `section.json` are written through `omnistax-content/tools/ost.py` only after that review.

This book bends three root rules, each for a reason given below: item 3's "the book's prose verbatim" becomes "each block's source prose verbatim, with provenance" (Source); item 11's "never fold sections" becomes "never fold concept homes" (Structure); item 21's "nothing is invented where the book prints no introduction" yields to METHOD decision 13 for the book's own introduction page (Structure).

## Source

**A multi-source book.** There is no one source text. The book is compiled from open sources, each registered in `sources/registry.json` with its id, title, authors, URL, pinned version, licence, the quoted licence evidence and its locator scheme. `tools/fetch_sources.sh` fetches every registered source into `sources/_cache/<id>/` at its pin (the cache is gitignored, 1.3 GB). A source with an `excluded` field in the registry is never used, linked or judged.

**The spine sources.** Coding Interview University (`ciu`, CC BY-SA 4.0) gives the interview order, the tiers and the link lists, and little prose of its own. cp-algorithms (`cpa`, CC BY-SA 4.0) is the main source for chapters 30–45 and many technique articles. *Open Data Structures* (`ods`, CC BY 2.5 Canada) and Erickson's *Algorithms* (`jeffe`, CC BY 4.0) are the textbook core. The System Design Primer (`sdp`, CC BY 4.0) is the system design spine (METHOD decision 1). Everything else came in through the resource finder (METHOD §6.1) and is in the registry: Wikipedia and Wikibooks, OpenDSA, OI Wiki, MCS 2018, Aspnes, *A Cool Brisk Walk* (`brisk`), Applied Combinatorics, Levin 3rd ed., and the system design documentation sets.

**Locators.** Every source has one locator scheme, written in its registry row, and every locator in this repository uses it: `cpa:graph/dijkstra#implementation`, `ods:arrays#sec:arraystack`, `jeffe:0.6`, `wikipedia:Linked_list#Singly linked list`, `oiwiki:basic/prefix-sum#一维前缀和`, `exercism:circular-buffer`. A locator names a heading or a labelled environment, never a line number. Where a block starts or stops inside a heading, the locator says so in words ("from 'A useful trick' to the end of the subsection"), as the winner tables in `judgements/` do. The Erickson cache (`jeffe/*.txt`) has lost every digit, minus sign and small-caps name to the PDF font; Erickson is quoted and transcribed from the PDF, never from the `.txt`.

**One explanation per concept, one source, its words kept whole** (METHOD §5, decision 11). The judge (METHOD §6.2) picks the source for each concept; the winner tables are `judgements/<chapters>-reconciled.md`. The winner's passage is used whole, its sentences, code and figures as the source prints them. There is no second treatment, no "another angle" block, no stitching of two sources inside one concept's explanation. A section may hold concepts from different sources, since a section is a page of several concepts. CIU's video and article links are never explanations; at most three per section go to the shell's References item, each with one sentence on what it is good for.

**Provenance per block.** Every `<section>` block of `text.html` carries `data-source` (the registry id) and `data-locator` (the locator of the passage it holds):

```html
<section id="arraystack" data-source="ods" data-locator="ods:arrays#sec:arraystack">
```

A block holds one source's passage. Where one concept's passage is long it may span several blocks, each with its own locator; a block never holds two sources. The section's attribution footer is built from these attributes (see Licence and attribution). This needs app support that does not exist yet (Figures, "What needs the app").

**What OmniStax writes, and how it is marked.** OmniStax writes the lead (root item 21.5), figure captions and labels, sim headlines and readouts, block headers where the source's own heading does not fit the page, and the book's introduction page. It writes no explanation of a concept. Three kinds of OmniStax text need care:

- **Bridging sentences.** Where a kept-whole winner leans on a name, a notation or a passage that another source introduced (ODS's DLList says "when implementing an SLList, we saw…" after a Wikipedia 2.5), OmniStax supplies the missing name or pointer in a bridging sentence. A bridge supplies a name, a notation or a forward pointer; it never explains a concept. Bridges go in the section lead, which is AI-marked already (root item 17), so no new in-text mark is needed. A bridge that cannot fit the lead's 80 words is a question for the user, not a sentence in the text. The bridges for chapters 1–3 are listed in `judgements/ch01-03-reconciled.md` (B1–B18) and assigned in each chapter's `config.md`.
- **Translations of OI Wiki.** OI Wiki (`oiwiki`, CC BY-SA 4.0 + SATA, METHOD decision 15) is Chinese. A winning OI Wiki passage is translated into English under `docs/prompts/translate.md`: the field's standard English terms, looked up and never coined; OI Wiki's sentences, order and content kept, nothing added or removed. The translated block is AI-marked as a translation and its footer line says "translated from the Chinese". OI Wiki's code blocks are outside its licence (its README excludes 代码部分) and are never copied; where a translated passage points at its code, the code shown comes from an MIT or CC BY-SA source (TheAlgorithms, doocs code under decision 18) and is credited to that source. A credit trace or table that OI Wiki puts in a code fence is redrawn as a figure from the numbers in the prose. OI Wiki's 例题 boxes that restate LeetCode problems become links.
- **Errata.** A source's words are never corrected in place. A wrong claim, a typo that changes meaning, or a code/prose mismatch keeps the source's text as printed and gets a numbered correction note (root item 13, the `footnotes` table, kind `correction`), AI-marked. A figure caption is corrected through the row's `figure` field. The errata found so far for chapters 1–3 are listed in `judgements/ch01-03-reconciled.md` (31 items) and assigned in each chapter's `config.md`.

**Versions.** The current version of a page, unless the page is marked AI-assisted (front matter, an edit summary, a `Co-Authored-By` model line); then its last version before the mark (METHOD §6.1). Decided per page: OI Wiki `basic/complexity.md` is used at `5a3c3d0d`; Wikipedia articles at the revision in `sources/_cache/wikipedia/_meta.json`. A source that is likely AI-written though unmarked is excluded on the user's ruling (so far `eh-dsa`, `algowiki`, `dsa-dummies`, and doocs' "Thinking" blocks).

**Code the source prints stays in the source's language** (METHOD §1.5): cpa's C++, ODS's Java/C++/pseudocode, Erickson's pseudocode, Wikipedia's pseudocode. It is not translated. Runnable code beside a figure and code exercises run in Python or JavaScript (decision 3); where the winner's code is C++ or Java, the runnable counterpart comes from an MIT or CC BY-SA source (the judge lists them per concept) or is an AI-written port marked as such. The ODS Python edition does not run on current Python as cached (`numpy.object`, Python 2 `print`, a float index); the mechanical port in `judgements/ch01-03-references.md` is AI-made and is marked where it is used.

**Tools.** `tools/` holds what the full-book pass has needed so far: `fetch_sources.sh` (the corpus), `map/` (`build.py`, `report.py`, `map.spec`: the concept map from the inventories) and `check_map.py` (the map's checker). Still to write, one converter per source format, each turning one locator into a block of `source.md`: Markdown (cpa, sdp, OI Wiki, doocs, CIU), LaTeX (ODS, MCS 2018, brisk, Aspnes), PreTeXt (appcomb, dmoi3), RST (OpenDSA), wikitext (Wikipedia, Wikibooks) and PDF with manual transcription (Erickson). A section's `source.md` is the concatenation of its blocks in page order, each opened by a marker line with its source id and locator. A converter a second book uses moves to `omnistax-content/tools/`.

## Structure

book → 45 numbered chapters → sections → concepts, plus **Appendix A · Computer systems** and **Appendix B · Getting the job**. One flat book with no parts (METHOD decision 9; `concept-map/report.md` ruling 1). The table of contents is `concept-map/toc.md` (and `toc.json`), derived from the concept map, not from any source's ToC.

| Chapters | What | Main sources |
|---|---|---|
| 1–7 | foundations: cost, arrays and lists, stacks and queues, recursion, hashing, binary search, bits | ODS, Erickson, Wikipedia, OI Wiki, cpa |
| 8–16 | trees, heaps, sorting, balanced trees, tries, graphs, shortest paths, MSTs | ODS, Erickson, cpa |
| 17–23 | backtracking, dynamic programming, greedy, strings, probability, lower bounds | Erickson, cpa |
| 24–29 | system design | the Primer and the registered documentation sets |
| 30–45 | beyond the interview: range queries, advanced graphs and strings, number theory, combinatorics, geometry | cpa |
| A | computer systems: 19 curated-links pages, not built as text | CIU links |
| B | getting the job: one reading page, no concepts | CIU |

Folders: `ch01` … `ch45`, `appA`, `appB`; sections `N.M` inside them. Section numbers are OmniStax's, since no source numbers this book; `chapter.json` writes no `module` or `slug` (there is no publisher page to complete). A section's `module` is absent too.

**A section is a concept home** (METHOD §4.3). Rule 11's "never fold" protects the units of a source, and here the unit is the concept home the map made: a section is a page of the concepts whose home it is. A thin section stays a page (the LRU cache, a single worked design). A source article that duplicates a home is folded into that home and is not a page of its own; each fold is listed in `toc.md` and in the chapter's `exploration.md`. Joining two concept homes is never done.

**Tiers** (METHOD decision 13). The map tags every concept `core`, `stretch` or `contest`; the reader sees **Essential**, **Advanced** and **Beyond**. No app change:

- The **book's introduction** (`intro/`) is an OmniStax-written page, AI-marked: it says what the three words mean and lists the chapters under each, a chapter of mixed tiers under its most common tier with its exceptions named. This is the one place the book has an introduction no source printed; root item 21's "nothing is invented" is set aside here by decision 13.
- **Each section's lead** names the section's tier, and any concept in it whose tier differs ("Essential; the potential method is Advanced").
- Nothing else changes. Practice sessions do not filter by tier.

Chapter introductions and summaries: none. No source prints one for a chapter of this book, so no `chNN/intro/` or `chNN/summary/` page is made (root item 21). A section opens on its lead and its first block.

**Appendices.** Appendix A's 19 pages keep their 62 concepts in the map (so the 11 edges into them resolve) and are built as link lists only, later. Appendix B is CIU's career sections, CIU's words, one page. Neither is in the first pass.

## Apparatus

What each source brings, and where it goes:

- **Prose** stays in the text, in blocks, as the source prints it: headings, paragraphs, lists, tables, display maths, code listings and the source's own figures.
- **Headings.** A block opens with the source's own heading as its `<h2>` where it names the concept; otherwise with an OmniStax header naming the concept. The source's numbering (ODS 2.1, Erickson §0.3) is not printed; it lives in the locator.
- **Learning objectives.** No source prints any for this book's sections; `objectives` is empty.
- **Summaries.** ODS's per-structure "Summary" subsections (a theorem and a paragraph) are part of their concept's passage and stay in the block; they are not a section summary. No source prints a section summary, so `summary_html` is empty.
- **Theorems, lemmas and proofs** (ODS, Erickson, MCS): a theorem or lemma stays in the text as `div.note` with its eyebrow ("Lemma", "Theorem", the source's title if any) and is a `result` concept's form where it is an equation. A printed proof is a derivation (root item 29) and the plan scores it.
- **Worked examples** stay whole (Erickson §0.3, ApportionCongress, is the worked example for `algorithm`, decision 18).
- **Footnotes** the source prints (Erickson's etymology and history notes) are book footnotes, kind `book`, under the source's numbering where it has one.
- **Code listings** stay as `<pre><code>` in the source's language, keywords in ink (`COLOR.md`). Code shown beside a figure is the figure's code panel and follows the Figures rules.
- **Exercises** go to the Exercises system (root item 12); see Exercise kinds. Practice-problem links at the end of cpa articles (LeetCode, Codeforces, SPOJ, CSES) are copyrighted statements and become References links, never cards.
- **References** (the shell's item): at most three links per section, from CIU's lists or the dossiers' link-only rows, each with one sentence on what it gives.

## Licence and attribution

**The book is CC BY-SA 4.0** (`license_url` https://creativecommons.org/licenses/by-sa/4.0/), **except the NC exercise cards** (METHOD §0, decision 6). CC BY-SA requires its adaptations to allow commercial use and CC BY-NC-SA forbids it, so the two never mix in one unit:

- Prose, figures, block labels, bridging sentences, translations, the concept map, and AI-written tests, references and hints for a BY-SA or BY exercise are CC BY-SA 4.0.
- NC material is allowed only as **exercise cards**: MIT OCW problem sets with their solutions, Project Euler, Erickson's extra lecture notes' exercises, *pythonds*' exercises. A card is a self-contained item with its own licence line. AI-written tests and hints for an NC card are adaptations of it and are CC BY-NC-SA 4.0 too. NC prose is link-only.
- NC cards live in their own file per section, `exercises-nc.json`, never in `section.json`. The content check refuses an NC origin anywhere else; the build can drop every `exercises-nc.json` to give a clean BY-SA edition. Each NC source is an `exercise_sources` row with its `license` and `license_url`.

**Sources whose licence allows adaptation into CC BY-SA 4.0**: public domain, CC0, CC BY (any version), CC BY-SA 3.0 and 4.0, MIT, BSD, Apache 2.0. ODS is CC BY 2.5 Canada; MCS 2018, OpenIntro and Kattis's BY-SA problems are 3.0, which allows a 4.0 adaptation. The licence gate is per page, not per site (METHOD §6.1).

**Attribution is per block.** Each section's footer lists, for every source its blocks draw on: the author or authors, the title, the URL, the licence with its link, and "adapted" (or "translated from the Chinese and adapted" for OI Wiki). The footer is generated from `data-source` and `book.json`; the section writes only `notes`, `ai` and `built` (root item 17).

- **MIT and Apache 2.0** sources keep their notices. OpenDSA prose and figures (MIT), TheAlgorithms explanations and test cases (MIT), trekhleb, keon and tryalgo test cases (MIT), Exercism problem specifications and Python-track examples (MIT) and Interactive Coding Challenges (Apache 2.0) each carry their copyright line and licence text, reached from the footer. A Wikipedia figure under MIT (HarmonicNumbers.svg) keeps its notice in its credit.
- **OI Wiki's SATA terms**: the attribution thanks the OI Wiki authors by name of the project and links its contributor list ("Thanks to the OI Wiki Team and its contributors"), and the OI Wiki repository is starred from the owner's account. A person does the starring, not an agent.
- **Figure credits.** A source figure kept or redrawn keeps its own credit and licence where it differs from its page's (Wikipedia files are licensed per file; the licences read so far are in the dossiers' Figures sections). Erickson's historical scans keep the credits printed at the end of his book.

**Excluded, and why:**

| What | Why |
|---|---|
| Alex Xu, *System Design Interview* | commercial, all rights reserved; the PDF the original plan pointed at is an unauthorised copy (METHOD §0) |
| Peterson and Davie, *Computer Networks: A Systems Approach* | excluded outright by the user; not used, not linked (decision 12) |
| OpenStax *Introduction to Computer Science* (prose and exercises) | the licence evidence conflicts (CC BY on LibreTexts, CC BY-NC-SA on openstax.org) and openstax.org forbids use in training or ingestion by generative AI |
| `eh-dsa`, `algowiki`, `dsa-dummies`, doocs "Thinking" blocks | likely AI-written (user rulings, 2026-11-08, decision 18) |
| LeetCode, Codeforces, SPOJ, CSES, HackerRank statements | copyrighted; links only. A doocs write-up's LeetCode statement is never copied |
| TheAlgorithms/JavaScript | GPL-3.0 |
| OI Wiki code blocks | outside OI Wiki's licence |
| NC prose: Erickson's extra notes, MIT OCW notes and transcripts, *pythonds*, hello-algo, the Competitive Programmer's Handbook, USACO Guide, MCS 2015, Levin 4th ed., redis/docs | NC; link-only (their exercises may be NC cards where the source is registered) |
| Kattis problems marked "For educational use only" or with no badge | no open licence |
| GPL, MPL, GFDL-only, ND, no licence | fail the gate |

## Types

In scheme order (METHOD §3). The first four are the ones chapters 1–3 use, so they take the four hues farthest apart:

| Order | Type id | Label | Covers |
|---|---|---|---|
| 1 | `index` | index | positions into a structure: i, j, lo, hi, l, r, a pointer, a node reference, head, tail, top, an address |
| 2 | `key` | key | the values stored and compared: array elements, a pivot, a window's sum, a prefix sum S_i |
| 3 | `cost` | cost | step counts, T(n), O(·), Θ(·), Ω(·), amortised cost, a potential Φ, credits, the counter |
| 4 | `size` | size | n, m, k when it is a length, capacity (`a.length`), the word size w, height, n₀ |
| 5 | `weight` | weight | edge weights, distances, dist[] (from chapter 13) |
| 6 | `stateless` | stateless component | web and app servers, workers: scaled by adding copies |
| 7 | `stateful` | stateful component | databases, caches, object stores: where data lives |
| 8 | `async` | asynchronous channel | queues, streams, pub/sub |
| 9 | `traffic` | traffic | requests, QPS, packets on the wire |
| 10 | `latency` | latency | time per request, p50/p99 |
| 11 | `bytes` | data size | storage, bandwidth |

METHOD lists `weight` before `size`; this draft swaps them so the first pass's four types are the first four. Eleven types and ten hue families: two types share a family a clear lightness step apart, and `npm run colours:default` keeps types that share a page in different families.

**`index` against `key`** is the distinction the colour exists for: in `a[i]` the `i` is an index and the cell's value is a key. **Stateless against stateful** is the system design distinction: every architecture diagram colours its components by these two (and `async`).

**Untyped, in ink:** probabilities, events and outcomes; counts that are neither a size nor a cost (the number of permutations, a bracket balance, a vote); logarithms, factorials and harmonic numbers as functions (H_k is in ink; an expected cost that equals H_k is `cost`); the constant c of a Big-O definition; digits and bits as symbols (a digit of an input number is a `key` where the figure draws it as a stored value); random variables (except where one is a running time, then `cost`); a time step t of a moving average; a loop counter that indexes nothing.

## Formulas list

The chapter's equations table is printed as **Formulas and bounds**: the forms of definitions and results that are equations (log_b k = ln k / ln b, Stirling, H_k bounds, linearity of expectation, address = B + c·i, S_i = S_{i−1} + a_i, the i2b formula) and the cost bounds the sources state as theorems (ArrayStack's amortised O(1), ArrayDeque's O(1 + min{i, n−i})).

## Exercise kinds

No exercise is AI-written (METHOD decision 4). Every statement comes from a source; tests and reference solutions may be AI-written and are marked (`tests_by: "ai"`, the card's AI mark). A keyed answer always comes from the source's key. The kinds, declared in `book.json`:

| id | Label | What | Answer types today | Needs |
|---|---|---|---|---|
| `check` | Check | keyed multiple choice, true/false, fill-in (OpenDSA, LibreTexts review questions, *pythonds* self-checks as NC) | `choice`, `number` | a converter for OpenDSA's Khan-format HTML; OpenDSA's parameterised generators become one fixed instance each unless the app gains generators |
| `trace` | Trace | the state after some steps: a visit order, the stack after five operations, a pointer's value, an order of growth (OpenDSA proficiency exercises, Wikibooks A-level traces) | `open` with the key as its solution, or `choice` where the source gives options | the `sequence` and `pick` answer types (shared library, decision 16); OpenDSA's JSAV proficiency exercises must be rebuilt as figures in the house style |
| `exercise` | Exercise | written: explain, prove, compute (ODS, Erickson, MCS, Aspnes, brisk, Wikibooks, appcomb, Levin, OpenIntro) | `number`, `multi`, `open` | nothing |
| `code` | Code | implement against tests (Exercism, Interactive Coding Challenges, ICPC packages, Kattis, ODS's harness, CIU's "implement" checklists) | none: there is no `code` answer type | the `code` answer type, the Python and JavaScript runners and the complexity check (METHOD §1.2, an app change under decision 16) |
| `estimate` | Estimate | back-of-envelope system design questions (from chapter 24) | `number` with `tol` is a stopgap that cannot express "within a factor of 2" | the `estimate` answer type (shared library) |
| `design` | Design | an open system design question with a checklist (from chapter 24) | `open` | the `rubric` answer type (shared library); no evidence until AI grading |

NC cards use the same kinds, with `origin` naming their NC source, in `exercises-nc.json`.

**Exercise fields.** `source_id` is the locator (`ods:arrays#exc-6`, `exercism:forth`); `source_number` the number as the source prints it ("Exercise 2.6", "Problem 14.22"); `origin` the `exercise_sources` row. An exercise goes with the section that introduces what it tests; one a source places early is held for the later page, and both pages' `exercise_notes` say so (root item 12). Bloom levels and concept tags are AI-judged.

**Tests for code exercises** (METHOD §6.3): source tests first (Exercism canonical data, ICPC secret data, ODS's harness, the source's doctests); where the source has only samples (Kattis) or none, tests are AI-written and cover what the statement implies (empty input, one element, duplicates, the worst case at the stated bound) and never add a requirement. A reference solution passes every test and the complexity check before the exercise ships; downloaded references are run isolated (decision 17). Test cases from implementations (TheAlgorithms, keon, trekhleb, tryalgo) are a source of tests for a printed statement, not exercises of their own.

**Inline Try Its.** No source of chapters 1–3 prints an inline question. The figure's predict pauses (METHOD §2.1.6) are inline `pick`s with no persisted evidence; whether they count as AI-written exercises under decision 4 is an open question for the user.

## Figures

The house style is Manim's (root item 25). What is particular to this book is METHOD §2.

**Code beside the visual, by default** (decision 8). Whenever an algorithm has code, the figure shows the code panel beside the drawing, and one transport drives both. The plan line argues against the pairing, never for it. The pairing is dropped only when the idea is a property and not a procedure (the BST order, a heap's shape, the list interface), in system design diagrams, and in growth plots; the plan line names which case applies. On a narrow pane the code sits above the drawing and shows only the current block.

**Stepping by block, like a debugger.** The unit of a step is a block, a few lines that do one thing, with a name for that thing ("find the smallest remaining", "relax every edge out of u"). The source's code stays verbatim; the blocks are named outside it. One step runs one block: its lines are marked as one band with its label, what it touched lights up on the drawing at the same moment, and its label is the figure's note. Blocks nest, so the transport has *step*, *step into* and *step out*; the default level is the coarsest that still changes the picture every step. The watch panel is the readout, variables in their referent colours; recursion shows a stack of frame cards; a breakpoint is a predict pause; *run to* jumps to the next interesting moment. Over about 25 lines the panel shows the block outline with the current block open. A trace is a pure array of states, so the transport reaches exact states in either direction (manim-style item 6: the trace index is the story's slider).

**Draw the invariant.** Every loop figure shades its invariant regions (the sorted prefix, the `[lo, hi]` window, Lomuto's three bands, the settled set, the window of a sliding window) and the readout states the invariant with live values ("a[0..i) is sorted · i = 4"). This is the book's form of root item 24.7.

**A cost counter is always on** in an algorithm figure, against its bound: "comparisons 3 ≤ ⌊log₂ n⌋ + 1 = 4". **Input is a choice**, and the bad case is one of the choices: `random | sorted | reversed | adversarial`, plus an editable input where it helps. Where it teaches, an `n` slider replays the count on a log–log plot beside the bound.

**The plan line, extended.** Root's plan line (`docs/prompts/interactive-figures.md` §1) gains five fields for an algorithm figure, after the value add:

```
… · code: <locator of the code shown>, <language>, <lines> | none (<which exception>) · blocks: <id> "<label>" lines a–b touches <x, y>; … (nesting by indentation) · invariant: <region shaded> · readout "<invariant with live values>" · cost: <what is counted> against <bound> · inputs: <presets, adversarial first-class> · …
```

Blocks are declared in the plan line and in `figures.js`, not as a new field of the figure row, to keep the content format unchanged (decision 16); whether the row should carry them is an open question.

**Motion.** An algorithm's steps are a story, not a clock: the transport scrubs the trace. A pointer that moves is a kinematic arrow (root item 24.1) and sets the floor at the moving tier; a swap morphs, it does not jump. A figure of a property is still. 3D: nowhere in chapters 1–3. The borderline groups arrive later (k-d trees, 3D convex hull and the external-memory model) and are settled in their chapters.

**System design figures** (METHOD §2.4): one architecture graph per chapter, its steps diffs of that graph, each step headed by the failure that forced it, dragging back shows the failure. The quantitative cores (queueing and utilisation, consistent hashing, token bucket, quorums, replication lag) are real sims. Back-of-envelope estimates are derivations (root item 29), their facts sourced to the Primer's tables.

**Source figures.** A source's sketch figure is replaced by a figure in the house style with the source's numbers as defaults, its image kept as the original (root item 14). Root item 14 gives the reader two labels, "Figure N.M" (the book's number) and "Sim". This book numbers no figures of its own, and a source's number (ODS's Figure 2.1, Erickson's Figure 0.4) is not this book's number, so the draft proposes: **every figure is a Sim or a photograph**; a Sim that replaces a source figure keeps that image behind the original toggle and its caption in `original_caption`, and has no `number`. The alternative is to number figures per section (Figure 2.2.1) as a book of our own would. This needs a ruling.

**What the shared library must gain** (figlib, or a library beside it; decision 16): the DSA primitives `strip`, `pointer`, `region`, `nodes`/`links`, `tree` (tidy layout, stable under insert), `graph` (fixed coordinates, never force-directed at runtime), `grid` (DP table with dependency arrows), `stack`, `queue`, `heap` (tree and array together), `buckets`, `bits`; the system design primitives `component(kind)`, `edge` with packets, `meter`, `ring`; a static `code` panel that sets source code as page text (root item 26.8) with a marked band; the `sequence`, `pick`, `parsons` and `estimate` answer widgets and `rubric`.

**What needs the app** (allowed by decision 16: the code runner and the debugger figures): the trace engine (figures emit `{line, vars, event}`; exercises trace the reader's Python with `sys.settrace`); the block transport (step, step into, step out, run to); the `code` answer type with the Python and JavaScript runners and the step-counting complexity check.

**What needs the app but decision 16 does not cover** (each an open question): per-block attribution from `data-source`; the AI mark on a translated block; `exercises-nc.json` (reading it, the check that refuses NC origins elsewhere, the BY-SA export); `tests_by` on an answer; a `syntax` highlights flag; the pinned scrollytelling diagram for system design chapters.

## Files

The root layout, plus:

```
METHOD.md                     the agreed method (read before this file)
RULES.md, COLOR.md            this book's rules and colour plan
book-json-proposal.md         the book.json rows to create after review (removed once book.json exists)
sources/registry.json         every source: licence, evidence, pin, locator scheme, exclusions
sources/_cache/<id>/          the fetched corpus (gitignored)
inventory/<source>.json       each source's concepts, unmerged (inventory/FORMAT.md); gap.json for the gap rows
concept-map/                  concepts.json, toc.json, toc.md, chapters.mmd, report.md: the merged DAG and the ToC
dossiers/<chapter>.md         the finder's candidates per concept (prose, exercises, figures, link-only, blocked hosts)
dossiers/sweep-*.md, gap-patterns.md   the finder's sweeps across the book
judgements/<chapter>.md       the judge's verdicts per concept, ranked exercises, builder notes
judgements/<chs>-reconciled.md   the cross-chapter pass: final winners, bridges, errata, indexing, translation list
judgements/<chs>-references.md   reference solutions run against their tests
.claude/agents/               resource-finder.md, resource-judge.md
tools/                        fetch_sources.sh, map/, check_map.py (and the converters, to come)
<chapter>/<section>/exercises-nc.json   the section's NC exercise cards
<chapter>/<section>/source.md the section's blocks, each opened by its source id and locator
```

## Template sections

None is built yet. The first template should be **2.3 Two pointers and sliding windows**, because it exercises nearly everything this book adds to the root rules on one page: blocks from two sources (OI Wiki in translation, Wikipedia), per-block provenance, two bridges in the lead (B9, B16), mixed indexing stated in the lead (1-based OI Wiki, 0-based Wikipedia), code-beside-the-visual figures with an invariant region and a cost counter (two pointers closing on a target, a window sliding), runnable code from a third source because OI Wiki's code is unlicensed, and code exercises with source tests (TheAlgorithms, Exercism) and with AI tests (Kattis samples). Its concepts are all Essential.

It depends on the app's trace engine and `code` answer type. If those are not ready when the build starts, the first template should be **2.2 Dynamic arrays** instead: one source (ODS), a figure that needs no code panel to be useful (doubling and its amortised counter), written exercises, two errata notes and the bridge B6, with the code exercise added once the runner exists.

Later templates, named when built: a translation-heavy page (1.5), a maths-prose page with derivations (1.3 or 1.6), a page of figures over linked structures (2.5–2.7), a system design page (chapter 26), and Appendix A's links page.

## What was built

Nothing. The full-book pass so far: the corpus and registry, the inventories, the concept map and ToC (`concept-map/report.md`), the dossiers and judgements for chapters 1–3, and these drafts.
