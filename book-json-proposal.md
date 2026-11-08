# book.json: the decided rows

Status: **decided**, 2026-11-08 (METHOD §4.4 decision 19: every recommendation of the full-book pass accepted). `tools/scaffold_book.py` reads the tables of this file once and writes `book.json` from them, with `ch01`–`ch03/chapter.json` from `concept-map/toc.json` (decision 19: a one-time scaffold script in this book's `tools/`; `ost` has no command that creates a book and refuses writes to `exercise_kinds`, and it is not changed). Every later write goes through `omnistax-content/tools/ost.py` (root item 19). Concept rows are not written here: they are written section by section during the build (root item 6).

Field names and shapes follow `docs/content-format.md`. A field this book wants that the schema does not have is listed at the end, not invented in a row. In the tables the script reads, a value in backticks is written as it stands; a row whose value is "absent" is not written.

## Identity

| field | value | why |
|---|---|---|
| `id` | `cs-interview-prep-ultra` | the repository's name (OmniStax/cs-interview-prep-ultra); decision 19 |
| `title` | `Data Structures, Algorithms and System Design` | decision 19. It also names the folder (`omnistax-content/Data Structures, Algorithms and System Design/`) and takes no source's title |
| `publisher` | `OmniStax` | no source publishes this compilation |
| `authors` | see below | "Author (Work)", decision 19 |
| `source_url` | `https://github.com/OmniStax/cs-interview-prep-ultra` | the book's own page |
| `sources` | see below | the schema's field for a book that joins several published works; the attribution credits each |
| `copyright` | absent | no single holder; each source's holder is named in its attribution line (see the end) |
| `license` | `CC BY-SA 4.0` | METHOD §0, decision 6 |
| `license_url` | `https://creativecommons.org/licenses/by-sa/4.0/` | |
| `language` | `en` | OI Wiki passages are translated into English |
| `openstax` | absent | not an OpenStax book |
| `translation_of` | absent | |
| `chapters` | `ch01`, `ch02`, `ch03` | the built chapters of `concept-map/toc.json`, in its order; `ch04` … `ch45`, `appA`, `appB` are added as each is built |
| `intro` | absent for now | the book's introduction page (METHOD decision 13: the tiers and which chapters are which) is OmniStax-written; `{}` is set when its `intro/` page is built, since the app builds the page the record names |
| `summary` | absent | no source prints one |
| `colours` | absent until `npm run colours:default -- cs-interview-prep-ultra` writes it | root item 7.4 |

### `authors`, as "Author (Work)"

Each entry names the author with the work in brackets, so the list reads as "compiled from" without a field the schema lacks (decision 19). Order: by how many concept explanations each source supplies in chapters 1–3 (`judgements/ch01-03-reconciled.md`: ODS 31, cpa 13, Wikipedia 11, OI Wiki 9, Erickson 6, brisk 3, OpenDSA 2, MCS 1 under decision 18), then the two spine sources not yet used for an explanation. The list grows as chapters are built.

| # | entry |
|---|---|
| 1 | Pat Morin (Open Data Structures) |
| 2 | cp-algorithms contributors (Algorithms for Competitive Programming) |
| 3 | Wikipedia contributors (Wikipedia) |
| 4 | OI Wiki Team (OI Wiki, translated from the Chinese) |
| 5 | Jeff Erickson (Algorithms) |
| 6 | Stephen Davies (A Cool Brisk Walk Through Discrete Mathematics) |
| 7 | Cliff Shaffer and the OpenDSA Project (OpenDSA eTextbook) |
| 8 | Eric Lehman, F. Thomson Leighton, Albert R. Meyer (Mathematics for Computer Science) |
| 9 | John Washam (Coding Interview University) |
| 10 | Donne Martin (The System Design Primer) |

### `sources`

`{title, url}` rows, in the order above. Chapters 1–3 use the first nine; the Primer is the system design spine.

| title | url |
|---|---|
| Open Data Structures | https://github.com/patmorin/ods |
| Algorithms for Competitive Programming (cp-algorithms) | https://github.com/cp-algorithms/cp-algorithms |
| Wikipedia | https://en.wikipedia.org/ |
| OI Wiki | https://github.com/OI-wiki/OI-wiki |
| Algorithms (Jeff Erickson, 1st edition, June 2019) | https://jeffe.cs.illinois.edu/teaching/algorithms/ |
| A Cool Brisk Walk Through Discrete Mathematics | https://github.com/divilian/cool-brisk-walk |
| OpenDSA eTextbook | https://github.com/OpenDSA/OpenDSA |
| Mathematics for Computer Science (2018) | https://courses.csail.mit.edu/6.042/spring18/mcs.pdf |
| Coding Interview University | https://github.com/jwasham/coding-interview-university |
| The System Design Primer | https://github.com/donnemartin/system-design-primer |

## `highlights`

All six on.

| key | value | reason |
|---|---|---|
| `facts` | `true` | on for every book (root item 7); few facts here (heatmaps of load) |
| `refs` | `true` | the code variables are referents: `lo`, `mid`, `hi` wear one colour in code, prose and drawing (`COLOR.md` §3, decision 19) |
| `concepts` | `true` | the types: `index` against `key`, `stateless` against `stateful` |
| `words` | `true` | the vocabulary is what is learnt: "invariant", "amortised", "sentinel", "monotonic", "sharding", "quorum" are words the reader must recognise and use (METHOD §3) |
| `symbols` | `true` | n, i, T(n), Φ carry the analysis |
| `underlines` | `true` | on for every book |

There is no `syntax` flag (decision 19): code panels colour only the variables the figure draws (`COLOR.md`).

## `types`, in order

All eleven, declared now (decision 19). `label` is what the legend and the colour menu print. `dimension` only where the type is a quantity with a unit the sources write. `size` is fourth so that the first pass's four types take the first four hues (METHOD §3 had `weight` there; the swap is accepted).

| # | id | label | dimension |
|---|---|---|---|
| 1 | `index` | index | |
| 2 | `key` | key | |
| 3 | `cost` | cost | |
| 4 | `size` | size | |
| 5 | `weight` | weight | |
| 6 | `stateless` | stateless component | |
| 7 | `stateful` | stateful component | |
| 8 | `async` | asynchronous channel | |
| 9 | `traffic` | traffic | requests/s |
| 10 | `latency` | latency | ms |
| 11 | `bytes` | data size | bytes |

## `exercise_kinds`

All six, declared now: `ost` refuses writes to this table, so a kind added later would need another script. `estimate` and `design` are first used in chapter 24. What each kind is and which answer types it uses: `RULES.md`, Exercise kinds.

| id | label |
|---|---|
| `check` | Check |
| `trace` | Trace |
| `exercise` | Exercise |
| `code` | Code |
| `estimate` | Estimate |
| `design` | Design |

## `exercise_sources`

Every exercise of this book has an origin, since the book itself sets none. One row per source whose exercise statements chapters 1–3 use or rank, plus the NC sources whose cards are available there. `short` is what the card's eyebrow prints before the number. Rows whose exercises the chapter 1–3 choice (decision 19, each chapter's `config.md`) does not ship yet stay, since their chapters or a later choice will use them; a row is added through `ost add … exercise_sources` when a new source is first used.

Kattis has one row per licence (decision 19), because a row carries one `license` and Kattis licenses problem by problem; every Kattis problem chosen for chapters 1–3 is CC BY-SA 3.0. A Kattis problem's own author has no field on the exercise row (see the end); the row names no author. The ICPC packages' `problem.yaml` says `license: cc by-sa` with no version, so their rows say "CC BY-SA" with no licence URL; the version is checked per package before a card ships (decision 19), and a package whose version differs gets a row of its own, as Kattis does. No ICPC item ships in chapters 1–3.

Test-case sources (TheAlgorithms/Python, keon/algorithms, trekhleb/javascript-algorithms, tryalgo, all MIT) are not origins of statements and get no row; their notices go in the attribution (see the end).

### Open (CC BY-SA 4.0 edition)

| id | title | short | author | url | license | license_url |
|---|---|---|---|---|---|---|
| `ods` | Open Data Structures | ODS | Pat Morin | https://github.com/patmorin/ods | CC BY 2.5 Canada | https://creativecommons.org/licenses/by/2.5/ca/ |
| `cpa` | Algorithms for Competitive Programming | cp-algorithms | cp-algorithms contributors | https://github.com/cp-algorithms/cp-algorithms | CC BY-SA 4.0 | https://creativecommons.org/licenses/by-sa/4.0/ |
| `jeffe` | Algorithms (1st edition, June 2019) | Erickson | Jeff Erickson | https://jeffe.cs.illinois.edu/teaching/algorithms/ | CC BY 4.0 | https://creativecommons.org/licenses/by/4.0/ |
| `mcs2018` | Mathematics for Computer Science (2018) | MCS | Eric Lehman, F. Thomson Leighton, Albert R. Meyer | https://courses.csail.mit.edu/6.042/spring18/mcs.pdf | CC BY-SA 3.0 | https://creativecommons.org/licenses/by-sa/3.0/ |
| `aspnes-202` | Notes on Discrete Mathematics (CPSC 202) | Aspnes | James Aspnes | https://www.cs.yale.edu/homes/aspnes/classes/202/notes.pdf | CC BY-SA 4.0 | https://creativecommons.org/licenses/by-sa/4.0/ |
| `brisk` | A Cool Brisk Walk Through Discrete Mathematics | Brisk Walk | Stephen Davies | https://github.com/divilian/cool-brisk-walk | CC BY-SA 4.0 | https://creativecommons.org/licenses/by-sa/4.0/ |
| `appcomb` | Applied Combinatorics | Applied Combinatorics | Mitchel T. Keller, William T. Trotter | https://github.com/mitchkeller/applied-combinatorics | CC BY-SA 4.0 | https://creativecommons.org/licenses/by-sa/4.0/ |
| `dmoi3` | Discrete Mathematics: An Open Introduction, 3rd edition | Levin | Oscar Levin | https://github.com/oscarlevin/discrete-book/tree/3rd-ed | CC BY-SA 4.0 | https://creativecommons.org/licenses/by-sa/4.0/ |
| `openintro-stats` | OpenIntro Statistics, 4th edition | OpenIntro | David M. Diez, Mine Çetinkaya-Rundel, Christopher D. Barr | https://github.com/OpenIntroStat/openintro-statistics | CC BY-SA 3.0 | https://creativecommons.org/licenses/by-sa/3.0/ |
| `wikibooks` | Wikibooks (Probability; A-level Computing) | Wikibooks | Wikibooks contributors | https://en.wikibooks.org/ | CC BY-SA 4.0 | https://creativecommons.org/licenses/by-sa/4.0/ |
| `opendsa-exercises` | OpenDSA exercises | OpenDSA | OpenDSA Project (Cliff Shaffer, Ville Karavirta and contributors) | https://github.com/OpenDSA/OpenDSA | MIT | https://opensource.org/license/mit |
| `lt-busbee` | Programming Fundamentals (LibreTexts) | Programming Fundamentals | Kenneth Leroy Busbee, Dave Braunschweig | https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/Programming_Fundamentals_(Busbee_and_Braunschweig) | CC BY-SA 4.0 | https://creativecommons.org/licenses/by-sa/4.0/ |
| `lt-njoroge` | Data Structure and Algorithms (African Virtual University) | AVU | Harrison Njoroge | https://eng.libretexts.org/Bookshelves/Computer_Science/Databases_and_Data_Structures/Data_Structure_and_Algorithms_(Njoroge) | CC BY-SA (version not stated) | https://creativecommons.org/licenses/by-sa/4.0/ |
| `sicp` | Structure and Interpretation of Computer Programs, 2nd ed. | SICP | Harold Abelson, Gerald Jay Sussman, Julie Sussman | https://github.com/sarabander/sicp | CC BY-SA 4.0 | https://creativecommons.org/licenses/by-sa/4.0/ |
| `ciu` | Coding Interview University | CIU | John Washam | https://github.com/jwasham/coding-interview-university | CC BY-SA 4.0 | https://creativecommons.org/licenses/by-sa/4.0/ |
| `exercism` | Exercism problem specifications | Exercism | Exercism contributors | https://github.com/exercism/problem-specifications | MIT | https://opensource.org/license/mit |
| `icc` | Interactive Coding Challenges | Coding Challenges | Donne Martin | https://github.com/donnemartin/interactive-coding-challenges | Apache-2.0 | https://www.apache.org/licenses/LICENSE-2.0 |
| `kattis-by-sa` | Open Kattis (problems under CC BY-SA 3.0) | Kattis | absent | https://open.kattis.com/problems | CC BY-SA 3.0 | https://creativecommons.org/licenses/by-sa/3.0/ |
| `kattis-by` | Open Kattis (problems under CC BY 3.0) | Kattis | absent | https://open.kattis.com/problems | CC BY 3.0 | https://creativecommons.org/licenses/by/3.0/ |
| `kattis-pd` | Open Kattis (public domain problems) | Kattis | absent | https://open.kattis.com/problems | Public Domain Mark 1.0 | https://creativecommons.org/publicdomain/mark/1.0/ |
| `kattis-cc0` | Open Kattis (CC0 problems) | Kattis | absent | https://open.kattis.com/problems | CC0 1.0 | https://creativecommons.org/publicdomain/zero/1.0/ |
| `icpc-kattis-export` | GCPC and NWERC problem packages | GCPC/NWERC | the GCPC and NWERC juries | https://github.com/mzuenni/kattis-export | CC BY-SA | absent |
| `icpc-mzuenni` | ICPC-style problem packages (NWERC, GCPC, Winter Contest) | ICPC | Michael Zündorf and co-authors | https://github.com/mzuenni/icpc-problems | CC BY-SA | absent |
| `icpc-rmc` | ICPC Rocky Mountain Regional problem sets | RMRC | Rocky Mountain Regional judges | https://github.com/icpc/na-rocky-mountain-2020-public | CC BY-SA | absent |

`cpa` is new against the draft: 3.4's largest-zero-submatrix card takes cp-algorithms' own problem sentence as its statement (`ch03/config.md`).

### NC (`exercises-nc.json` only, CC BY-NC-SA 4.0)

| id | title | short | author | url | license | license_url |
|---|---|---|---|---|---|---|
| `jeffe-notes` | Algorithms: extra lecture notes | Erickson notes | Jeff Erickson | https://jeffe.cs.illinois.edu/teaching/algorithms/ | CC BY-NC-SA 4.0 | https://creativecommons.org/licenses/by-nc-sa/4.0/ |
| `mitocw-6-006-spring2020` | 6.006 Introduction to Algorithms, Spring 2020 | MIT 6.006 | Erik Demaine, Jason Ku, Justin Solomon | https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/ | CC BY-NC-SA 4.0 | https://creativecommons.org/licenses/by-nc-sa/4.0/ |
| `mitocw-6-006-fall2011` | 6.006 Introduction to Algorithms, Fall 2011 | MIT 6.006 | Erik Demaine, Srini Devadas | https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/ | CC BY-NC-SA 4.0 | https://creativecommons.org/licenses/by-nc-sa/4.0/ |
| `mitocw-6-046j-spring2015` | 6.046J Design and Analysis of Algorithms, Spring 2015 | MIT 6.046J | Erik Demaine, Srini Devadas, Nancy Lynch | https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/ | CC BY-NC-SA 4.0 | https://creativecommons.org/licenses/by-nc-sa/4.0/ |
| `mitocw-6-046j-spring2012` | 6.046J Design and Analysis of Algorithms, Spring 2012 | MIT 6.046J | Dana Moshkovitz, Bruce Tidor | https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/ | CC BY-NC-SA 4.0 | https://creativecommons.org/licenses/by-nc-sa/4.0/ |
| `mitocw-6-046j-fall2005` | 6.046J Introduction to Algorithms, Fall 2005 | MIT 6.046J | Charles Leiserson, Erik Demaine | https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/ | CC BY-NC-SA 4.0 | https://creativecommons.org/licenses/by-nc-sa/4.0/ |
| `mitocw-6-042j-fall2005` | 6.042J Mathematics for Computer Science, Fall 2005 | MIT 6.042J | Albert Meyer, Adam Chlipala | https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2005/ | CC BY-NC-SA 4.0 | https://creativecommons.org/licenses/by-nc-sa/4.0/ |
| `projecteuler` | Project Euler | Project Euler | Colin Hughes and contributors | https://projecteuler.net/archives | CC BY-NC-SA 4.0 | https://creativecommons.org/licenses/by-nc-sa/4.0/ |
| `pythonds` | Problem Solving with Algorithms and Data Structures using Python | pythonds | Bradley N. Miller, David L. Ranum | https://github.com/RunestoneInteractive/pythonds | CC BY-NC-SA 4.0 | https://creativecommons.org/licenses/by-nc-sa/4.0/ |

(`mitocw-6-856j-fall2002` is held for chapter 22.) Under decision 19 NC cards ship keyed only, so `jeffe-notes` (unkeyed exercises) and `projecteuler` (statements only, answers unpublished) have no card in chapters 1–3; jeffe-notes 9.3 is a References link of 1.5.

## Not in the schema

Decision 19 approved the app changes for per-block attribution, the NC card files (reading them, the check that refuses NC origins elsewhere, the BY-SA export) and the AI mark on translated blocks. Until the schema gains them, the scaffold writes none of these fields. Settled without a field: "Compiled from" is carried by the "Author (Work)" entries; there is no `syntax` flag; AI-written tests use the answer's existing `generated_by`.

| what | why this book needs it | status |
|---|---|---|
| per-source licence, licence URL, copyright line and notice on each `sources` row (or a table the per-block footer reads) | the per-block attribution footer must print each source's licence; MIT and Apache sources require their copyright line and licence text | app change approved (per-block attribution); schema field not yet designed |
| a block-level provenance and translation mark the schema knows of (`data-source`, `data-locator`, a translated block's AI mark) | per-block attribution and the AI mark on translated blocks are read from `text.html` attributes the checker does not yet know | app change approved |
| reading `exercises-nc.json` (a section-level NC exercise table) | the NC separation (METHOD §0) | app change approved |
| a per-exercise credit (the author of one Kattis problem, the rights owner of one ICPC package) | a Kattis or ICPC row carries one licence and no single author; `changes` is for alterations, not credit | not yet ruled; no Kattis or ICPC card needs it before chapter 1–3 cards are built |
| `exercise_sources` for test-case sources, or a `tests_from` on an answer | to credit TheAlgorithms, keon, trekhleb and tryalgo where their test cases are used | not yet ruled; until then their notices go in the attribution |
| the `code`, `sequence`, `pick`, `parsons`, `estimate`, `rubric` answer types | METHOD §1.2, §1.3; `code` is covered by decision 16, the others by "shared library, as little format change as possible" | `code` approved (decision 16); the others in the shared library |
