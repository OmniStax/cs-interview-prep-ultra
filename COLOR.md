# CS Interview Prep Ultra: colour plan

Status: **agreed**, 2026-11-08 (METHOD §4.4 decision 19). The rule is root `RULES.md` item 7: colour reaches a page in four ways, and where two apply the earlier wins (fact, then convention, then referent, then category). This file records what is particular to this book, from METHOD §3. A chapter's or section's `COLOR.md` may refine it, never inventing a hue.

## The book-wide rule: hue for identity, decoration for status

In a DSA figure the reader's question is which of two things a mark is: `i` or `j`, this pointer or that, the primary or replica 2. Hue answers that. Status (unvisited, in the frontier, settled; unsorted, sorted; live, dead) is a variant of one kind, and root item 7.4 already makes a variant a decoration: hollow, dashed ring, filled, faded to ink. Most visualisers do the opposite (frontier yellow, visited green); with six statuses in six hues no hue is left for identity, and the reader carries a legend in their head. Here a status never takes a hue of its own.

| Status | Decoration |
|---|---|
| not yet reached, unseen | hollow, thin outline |
| in progress, in the frontier, in the window | dashed ring |
| done, settled, sorted, kept | filled |
| discarded, out of the window, popped | faded to ink |
| an invariant region (the sorted prefix, `[lo, hi]`, Lomuto's bands, the settled set, a sliding window) | a light tint of the type whose positions it spans (almost always `index`), named in the readout |
| broken: an invariant shown failing, a wrong answer on screen (Dijkstra with a negative edge) | the app's `PAL.bad`, the one status with a colour, since it says the picture is wrong |

## 1. Facts

Few. A false-colour map of one scalar over a structure (key load per bucket, cache hotness per key, request rate per shard) is drawn on one sequential scale with its legend, listed in the figure row's `facts` as `"spectrum"`. Nothing in chapters 1–3 is drawn as a fact.

## 2. Conventions

- **Red-black trees** (chapter 11): red nodes are red and black nodes are black, because the field names them so. The red is a fixed colour kept away from every type hue; the black is ink. The figure row lists both in `facts` as `#rrggbb`, since `conventions` takes only `F.el` keys and there is no element key for them (whether figlib should gain a convention key for them is a question for later).
- No other convention. Bits are not coloured 0/1; a heap is not coloured by level.

## 3. Referents

**In an algorithm figure the referents are the variables of its code**: `lo`, `mid`, `hi`; `l`, `r`; `slow`, `fast`; `head`, `tail`, `top`; `u`, `v`; `front`, `back`. Each is a referent of the section (`referents`), dealt its colour by root item 7.3's smart assignment, and it wears that one colour everywhere it appears in the scope: its token in the code panel, its pointer and label on the drawing, its value in the watch panel, and every mention in the prose (`<span data-ref="lo">`, pronouns included). A phrase naming two ("the two pointers") lists both and is banded.

**A variable is the referent itself, not a quantity of one.** Root item 7.3 splits a symbol for a referent's quantity (F₁: the F in the category's colour, the 1 in the referent's). `lo` is not a quantity of something; it is the thing, so its whole name wears the referent's colour, and so does the pointer drawn for it. The type colour then goes to what is not named: the index labels under a strip, an unnamed position ("position 3"), the general word ("an index"). In `a[lo]`, `lo` wears its referent colour and the cell's value wears `key`. This settles a conflict in METHOD §3, which asks both for "`i` in index colour" and for "a variable's letter is its referent colour": named code variables are referents, and the `index` colour is for unnamed positions (decision 19).

**Named elements.** An element of the input is unnamed (`F.cat`) unless the text points at it: "the pivot, 5", "the node where the cycle starts", "the first repeated character". Then it is a referent.

**System design.** A component the text keeps pointing at ("the primary", "replica 2", "shard B", "the cache in front of the database") is a referent; its box wears its category's colour by kind, and its name label wears the referent's colour (the rule for a referent whose body another rule colours).

**Scope and reuse.** A referent's scope is the figures that draw it, the blocks they sit in, and every block that marks it, as root item 7.3 says. Two sections' `i` are different referents; they may wear the same colour, since their groups never meet.

## 4. Categories

The types, in scheme order, are in `RULES.md` (Types): `index`, `key`, `cost`, `size`, `weight`, `stateless`, `stateful`, `async`, `traffic`, `latency`, `bytes`. What each colours:

| Type | Symbols | Words and phrases (`data-concept` where they name a concept) | In figures |
|---|---|---|---|
| `index` | i, j, k as positions, p for a pointer, an address B + c·i | "index", "position", "pointer", "the head", "a node reference" | index labels under a strip, unnamed positions, invariant tints |
| `key` | x, a_i, the cell's value, S_i (a prefix sum), a window's sum | "key", "element", "value", "the pivot" | cell contents, bar heights of values |
| `cost` | T(n), O(·), Ω(·), Θ(·), Φ, ĉ (amortised cost), credits | "running time", "comparisons", "amortised cost", "potential" | the cost counter, a growth curve, a credit stack |
| `size` | n, m, a.length, w, n₀, b (block size) | "size", "capacity", "word size", "length of the window" | the extent of a strip, a capacity bracket |
| `weight` | w(u, v), d[v] | "weight", "distance" | edge labels, distance labels |
| `stateless` | | "web server", "worker", "application tier" | component boxes |
| `stateful` | | "database", "cache", "object store", "replica" | component boxes |
| `async` | | "queue", "stream", "topic" | channels |
| `traffic` | λ, QPS | "requests", "read traffic" | packets on edges |
| `latency` | p99, the service time | "latency", "response time" | meters, readouts |
| `bytes` | | "storage", "bandwidth" | readouts |

**Variants** share the hue and differ by decoration: an initial or average cost, a bound against a count (the bound dashed, the count solid), capacity against size (capacity hollow, size filled), the old array against the new during a resize (old faded).

**Untyped, in ink**: as listed in `RULES.md` (probabilities, events, plain counts, logarithms and factorials as functions, the constant c, digits as symbols, random variables that are not running times).

**`stack` and `queue` the structures are not types.** They are concepts, defined in chapter 3; their words are underlined as concept mentions but in ink, since no type covers "a data structure" (a type for it would colour nearly every noun of the book). The `async` type is the system-design channel, and "queue" is marked `async` only in chapters 24–29, where it names a message queue.

## Code panels: no syntax highlighting

Keyword colouring is extraneous colour a programmer has stopped seeing. In this book's code panels and code listings, keywords are ink at medium weight, comments muted, strings and literals ink. **Only the variables the figure draws are coloured**, each as its referent, so colour in code means what it means in the drawing. A token of a variable the figure does not draw stays ink. There is no `syntax` highlights flag and no editor theme for code panels (decision 19).

## Highlights

All six on (`book.json`, from `book-json-proposal.md`): facts, referents, concepts, words, symbols and underlines. Words are on because the vocabulary is what the reader is here to learn: "invariant", "amortised", "sentinel", "monotonic", "sharding", "quorum" are the terms an interviewer listens for. Symbols are on: n, i and T(n) carry most of the analysis.

## Chapters 1–3

Types in use: `index` (2.1 addresses and indices, 2.3 the two pointers' unnamed positions, 2.5–2.7 node references, 3.x top, front, back), `key` (2.3–2.4 values and sums, 3.4 the minimum), `cost` (1.3–1.5 throughout, every cost counter), `size` (n, capacity, w, block size b). No `weight` and no system design type. Referents: the code variables of each figure (listed per chapter in `exploration.md`). No facts, no conventions.
