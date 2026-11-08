# book.json: the rows to create after review

Status: **draft for review**, 2026-11-08. Nothing here is written to `book.json`. After review, the rows are created through `omnistax-content/tools/ost.py` (root item 19), never by hand. Two gaps in the tool: `ost` has no command that creates a new book's `book.json` (its identity fields, `highlights`, `chapters`), and it refuses writes to `exercise_kinds`. The first write therefore needs either a small `ost` addition (a `new` or `init` command) or a one-time scaffold script like `scaffold_translation.py`. Which one is a question for the user.

Field names and shapes follow `docs/content-format.md`. A field this book wants that the schema does not have is listed at the end, not invented in a row.

## Identity

| field | proposed value | why |
|---|---|---|
| `id` | `cs-interview-prep-ultra` | the repository's name (OmniStax/cs-interview-prep-ultra) |
| `title` | **to decide**. Candidates: "Data Structures, Algorithms and System Design"; "CS Interview Prep Ultra" | the title also names the folder (`omnistax-content/<Book Title>/`). It must not take a source's title ("Coding Interview University") |
| `publisher` | `OmniStax` | no source publishes this compilation |
| `authors` | see below | "compiled from" the sources, as asked |
| `source_url` | `https://github.com/OmniStax/cs-interview-prep-ultra` | the book's own page |
| `sources` | see below | the schema's field for a book that joins several published works; the attribution credits each |
| `copyright` | absent | no single holder; each source's holder is named in its attribution line (see the end) |
| `license` | `CC BY-SA 4.0` | METHOD §0, decision 6 |
| `license_url` | `https://creativecommons.org/licenses/by-sa/4.0/` | |
| `language` | `en` | OI Wiki passages are translated into English |
| `openstax` | absent | not an OpenStax book |
| `translation_of` | absent | |
| `chapters` | `ch01` … `ch45`, then `appA`, `appB` | `concept-map/toc.json`; only built chapters are listed at first (`ch01`, `ch02`, `ch03`) |
| `intro` | `{}` | the book's introduction page (METHOD decision 13: the tiers and which chapters are which); OmniStax-written, so no `module` or `slug` |
| `summary` | absent | no source prints one |
| `colours` | absent until `npm run colours:default -- cs-interview-prep-ultra` writes it | root item 7.4 |

### `authors`, as "compiled from"

The schema's `authors` is a list of names. To read as "compiled from", each entry names the author with the work in brackets. Order: by how many concept explanations each source supplies in chapters 1–3 (`judgements/ch01-03-reconciled.md`: ODS 31, cpa 13, Wikipedia 11, OI Wiki 9, Erickson 6, brisk 3, OpenDSA 2, MCS 1 under decision 18), then the two spine sources not yet used for an explanation. The list grows as chapters are built.

| # | entry |
|---|---|
| 1 | Pat Morin (Open Data Structures) |
| 2 | cp-algorithms contributors (Algorithms for Competitive Programming) |
| 3 | Wikipedia contributors |
| 4 | OI Wiki Team (OI Wiki, translated from the Chinese) |
| 5 | Jeff Erickson (Algorithms) |
| 6 | Stephen Davies (A Cool Brisk Walk Through Discrete Mathematics) |
| 7 | Cliff Shaffer and the OpenDSA Project |
| 8 | Eric Lehman, F. Thomson Leighton, Albert R. Meyer (Mathematics for Computer Science) |
| 9 | John Washam (Coding Interview University) |
| 10 | Donne Martin (The System Design Primer) |

Whether the app should show these under a "Compiled from" heading rather than "by" is an open question; the schema has no field that says so.

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
| `facts` | true | on for every book (root item 7); few facts here (heatmaps of load) |
| `refs` | true | the code variables are referents: `lo`, `mid`, `hi` wear one colour in code, prose and drawing (`COLOR.md` §3) |
| `concepts` | true | the types: `index` against `key`, `stateless` against `stateful` |
| `words` | true | the vocabulary is what is learnt: "invariant", "amortised", "sentinel", "monotonic", "sharding", "quorum" are words the reader must recognise and use (METHOD §3) |
| `symbols` | true | n, i, T(n), Φ carry the analysis |
| `underlines` | true | on for every book |

A seventh flag, `syntax` (the reader's editor theme in code panels, off by default), is not in the schema: see the end.

## `types`, in order

`label` is what the legend and the colour menu print. `dimension` only where the type is a quantity with a unit the sources write.

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

METHOD §3 orders `weight` before `size`; this proposal puts `size` fourth so that the first pass's four types take the first four hues. Rows 5–11 can wait until their chapters (13, 24–29) if the user prefers to add types as they are first used; the colour script is rerun after each addition either way.

## `exercise_kinds`

| id | label |
|---|---|
| `check` | Check |
| `trace` | Trace |
| `exercise` | Exercise |
| `code` | Code |
| `estimate` | Estimate |
| `design` | Design |

`estimate` and `design` are first used in chapter 24 and can be added then. What each kind is and which answer types it uses: `RULES.md`, Exercise kinds.

## `exercise_sources`

Every exercise of this book has an origin, since the book itself sets none. One row per source whose exercise statements are used in chapters 1–3, plus the NC sources whose cards are available there. `short` is what the card's eyebrow prints before the number.

### Open (CC BY-SA 4.0 edition)

| id | title | short | author | url | license | license_url |
|---|---|---|---|---|---|---|
| `ods` | Open Data Structures | ODS | Pat Morin | https://github.com/patmorin/ods | CC BY 2.5 Canada | https://creativecommons.org/licenses/by/2.5/ca/ |
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
| `kattis-by-sa` | Open Kattis (problems under CC BY-SA 3.0) | Kattis | per problem (named in `changes`, see below) | https://open.kattis.com/problems | CC BY-SA 3.0 | https://creativecommons.org/licenses/by-sa/3.0/ |
| `kattis-by` | Open Kattis (problems under CC BY 3.0) | Kattis | per problem | https://open.kattis.com/problems | CC BY 3.0 | https://creativecommons.org/licenses/by/3.0/ |
| `kattis-pd` | Open Kattis (public domain problems) | Kattis | per problem | https://open.kattis.com/problems | Public Domain Mark 1.0 | https://creativecommons.org/publicdomain/mark/1.0/ |
| `kattis-cc0` | Open Kattis (CC0 problems) | Kattis | per problem | https://open.kattis.com/problems | CC0 1.0 | https://creativecommons.org/publicdomain/zero/1.0/ |
| `icpc-kattis-export` | GCPC and NWERC problem packages | GCPC/NWERC | the jury of each contest | https://github.com/mzuenni/kattis-export | CC BY-SA (per problem.yaml) | https://creativecommons.org/licenses/by-sa/4.0/ |
| `icpc-mzuenni` | ICPC-style problem packages (NWERC, GCPC, Winter Contest) | ICPC | Michael Zündorf and co-authors | https://github.com/mzuenni/icpc-problems | CC BY-SA (per problem.yaml) | https://creativecommons.org/licenses/by-sa/4.0/ |
| `icpc-rmc` | ICPC Rocky Mountain Regional problem sets | RMRC | Rocky Mountain Regional judges | https://github.com/icpc/na-rocky-mountain-2020-public | CC BY-SA (per problem.yaml) | https://creativecommons.org/licenses/by-sa/4.0/ |

Kattis needs one row per licence, because a row carries one `license` and Kattis licenses problem by problem; the problem's own author goes in the card's credit. ICPC packages say "cc by-sa" with no version: the URL above assumes 4.0 and should be checked per package.

Test-case sources (TheAlgorithms/Python, keon/algorithms, trekhleb/javascript-algorithms, tryalgo, all MIT) are not origins of statements and get no row; their notices go in the attribution (see the end).

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

(`mitocw-6-856j-fall2002` is held for chapter 22.)

## Not in the schema (needs an app change and a ruling)

| what | why this book needs it |
|---|---|
| per-source licence, licence URL, copyright line and notice on each `sources` row | the per-block attribution footer must print each source's licence; MIT and Apache sources require their copyright line and licence text |
| a "compiled from" flag or heading | so the footer and the book's card say "compiled from" rather than "by" |
| `highlights.syntax` | the reader's editor theme in code panels (`COLOR.md`) |
| `exercise_sources` for test-case sources, or `tests_from` on an answer | to credit TheAlgorithms, keon, trekhleb and tryalgo where their test cases are used |
| `tests_by: "ai"` and the `code`, `sequence`, `pick`, `parsons`, `estimate`, `rubric` answer types | METHOD §1.2, §1.3; the `code` type is covered by decision 16, the others by "shared library, as little format change as possible" |
| reading `exercises-nc.json` | the NC separation (METHOD §0) |
