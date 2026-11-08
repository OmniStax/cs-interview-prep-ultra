# Plan: 1.5 Amortized analysis

Status: **plan for review** (root item 5), 2026-11-08. Nothing is built. Read for this plan: as 1.1, plus `oiwiki/docs/basic/amortized-analysis.md` at the cached pin (c794414), whole, and `judgements/ch01-03-reconciled.md` item 2 and the translation list.

One source, OI Wiki (CC BY-SA 4.0 + SATA), **all of it translated** from the Chinese under `docs/prompts/translate.md`, each block AI-marked as a translation. 5 blocks, 3 concepts, 1 Sim, 2 derivations.

## Lead (draft, AI-marked, 68 words with B-new-a)

> Essential; the potential method is Advanced. One dynamic array, doubled when full, analysed three ways, then a stack analysed the same three ways. n is the number of elements and m the array's capacity, except in the aggregate analysis, where m is the size of the full array being copied. *[B-new-a:]* The stack's push, pop and multi-pop are defined in its own table; stacks are the subject of 3.1.

Tier: Essential. Of another tier: `potential-method` (Advanced). Indexing: none; the n/m notation as above (erratum 14 is the matching note). Bridges: none from the reconciled list; **B-new-a** (the stack forward pointer) is new and goes to the user (Questions). B6, the notation bridge between this section and ODS, is 2.2's.

## Sub-concept blocks (`<h2>`), in OI Wiki's own order

`exploration.md` grouped the page into three blocks, one per concept, which would move the stack example's aggregate and accounting parts ahead of the potential method and so reorder OI Wiki's page. This plan keeps OI Wiki's order and lets two concepts span two blocks each (book `RULES.md`, Source: a long passage may span several blocks). See Questions.

| # | block id | `<h2>` (translated or OmniStax) | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `amortized` | Amortized analysis (OmniStax: the source's 引入 "Introduction" does not name it); the source's 聚合分析 as `<h3>` "Aggregate analysis" | oiwiki | `oiwiki:basic/amortized-analysis#引入` + `#内容` + `#聚合分析` | **yes** (≈400 words) | what amortized analysis is and is not ("involves no probability…"), the three methods named, the growing `vector` from capacity m = 1, the aggregate count Σ 2ⁱ = 2^⌈log₂ n⌉ − 1 < 2n. The 内容 ("Content") heading is an empty label: dropped, its paragraphs kept |
| 2 | `accounting` | The accounting method (记账分析) | oiwiki | `#记账分析` | **yes** | charge 3 per insert, 1 now and 2 banked; the newer half's n/2 elements prepaid n units; "Here is a concrete example:" followed by `sim-pay-for-doubling` in place of the code-fenced credit trace (OI Wiki's code is outside its licence; the figure is redrawn from the prose's numbers) |
| 3 | `potential` | The potential method (势能分析), with 原理 "Principle" and 示例：动态数组的扩容分析 "Example: growing a dynamic array" as `<h3>` | oiwiki | `#势能分析` (原理, 示例) | **yes** | the state S, Φ(S) ≥ Φ(S₀), ĉ = c + Φ(S′) − Φ(S), the telescoping sum (→ `drv-potential-sum`), Φ(h) = 2n − m with Φ(h₀) = −1, the two insert cases (→ `drv-doubling-potential`); OI Wiki's four reference footnotes (Clemson, UC Irvine, Stanford, Cornell) as book footnotes |
| 4 | `stack-example` | Extended example: stack operations (扩展示例：堆栈操作), with 聚合分析法 and 记账分析法 as `<h3>` | oiwiki | `#扩展示例：堆栈操作` (intro and table) + `#聚合分析法` + `#记账分析法` | **yes** | second block of `aggregate-accounting`: the push / pop / multi-pop table, the aggregate count, the 2-per-push accounting |
| 5 | `stack-potential` | Potential analysis of the stack (势能分析法) | oiwiki | `#扩展示例：堆栈操作` › `#势能分析法` | **yes** | second block of `potential-method`: Φ(h) = \|S\|, amortized costs 2, 0, 0 |

Not carried: the 前置知识 (prerequisite) line and the page's one-line opener (outside the locators), and 参考资料与注释 (the further-reading list; its one link, Wikipedia's Amortized analysis, is not a References pick). The translated blocks follow `translate.md`: standard English terms looked up, never coined (amortized analysis, aggregate analysis, accounting method, potential method, potential function Φ, amortized cost ĉ, actual cost, credit, resize, multi-pop), OI Wiki's sentences, order and content kept, nothing added; the footer line reads "translated from the Chinese and adapted".

## Concepts

| id | kind | tier | statement | introducing span |
|---|---|---|---|---|
| `amortized-analysis` | idea | Essential | Amortized analysis bounds the average cost per operation over a worst-case sequence of operations, spreading occasional expensive steps (a resize) over the cheap ones; it involves no probability. | `amortized`, "Amortized analysis" in its first sentence |
| `aggregate-accounting` | skill | Essential | Bound the total cost by summing it over the sequence and dividing (aggregate), or by charging each operation a fixed amount whose surplus is banked to pay for later expensive work (accounting). | `accounting`, "The accounting method" in its first sentence (the aggregate method is named first in `amortized`, but the concept's home and its two methods together begin here; see Questions) |
| `potential-method` | skill | Advanced | Define a potential Φ on states with Φ(S) ≥ Φ(S₀); an operation's amortized cost is its actual cost plus the change in Φ, and the total amortized cost bounds the total actual cost. | `potential`, "The potential method" in its first sentence |

## Errata notes

- **14** (notation; marker in block 1 at "where m is the current size of the array"): in the aggregate analysis m is the size of the full array being copied, while the opening of the section and the potential method write m for the capacity (and n for the number of elements); the accounting method's "O(m), where m is the current size of the array" is the same full size. The counts are right in either reading.

## Derivation candidates

| candidate | how printed | moves | score | decision |
|---|---|---|---|---|
| 原理: p_i = c_i + Φ(S_i) − Φ(S_{i−1}); Σc_i = Σp_i + Φ(S₀) − Φ(S_m); since Φ(S) ≥ Φ(S₀), Σp_i ≥ Σc_i | three displays with words between | 4 (sum over i; telescope; rearrange; apply Φ(S_m) ≥ Φ(S₀)) | printed: qualifies by rule 29.1 | **build** `drv-potential-sum`, *Derivation · the total amortized cost bounds the total actual cost*; replaces the displays; facts: the definition of p_i (block 3), Φ(S) ≥ Φ(S₀) (block 3, a condition); words translated |
| 示例: ΔΦ = 2(n + 1) − m − (2n − m) = 2, amortized 1 + 2 = 3; with resizing ΔΦ = 2(n + 1) − 2n − (2n − n) = 2 − n, amortized n + 1 + (2 − n) = 3 | equations inside a numbered list | 2 + 2, two independent lines to the same result | printed: qualifies | **build** `drv-doubling-potential`, *Derivations · the amortized cost of an insert*, two results (no resize, resize); facts: Φ(h) = 2n − m (block 3), m = n before a resize and 2n after (block 1) |
| 聚合分析: Σ_{i=0}^{⌈log₂ n⌉−1} 2ⁱ = 2^⌈log₂ n⌉ − 1 < 2n | inline in prose | 2 (geometric sum; 2^⌈log₂ n⌉ < 2n) | 2 (the geometric sum; ⌈log₂ n⌉ < log₂ n + 1) + 2 + 0 = 4 | not built: two moves, under the four-move bar |
| stack potential: 1 + 1 = 2, 1 − 1 = 0, t − t = 0 | prose list | 1 each | — | never (substitutions) |

## Figures

```
sim-pay-for-doubling · Sim (no original: it replaces OI Wiki's code-fenced credit trace, which is outside OI Wiki's licence and is not copied or shown) · amortized-analysis, aggregate-accounting, potential-method · flow by animation; variation by choice · arrows: kinematic (elements copied from the old array into the new one at a resize) · moving: one insert per step, a resize morphing the array to twice its length · choice method: aggregate | accounting | potential (default accounting, where the figure stands) · headline "Insert 9 pays 3: 1 for itself and 2 banked; the bank never runs dry." · graph: below, the actual cost of each insert as bars with the running total against the line 3n (aggregate), the banked credits (accounting), or Φ(h) = 2n − m (potential) · 2D · code: none (OI Wiki describes the vector in words; its code blocks are unlicensed) · invariant: credits ≥ 0 (accounting); Φ(h) ≥ Φ(h₀) = −1 (potential), read in the readout · readout (aggregate) "inserts 9 · copies 15 = 2^⌈log₂ 9⌉ − 1 < 2n = 18 · total 24 ≤ 3n = 27"; (accounting) "charged 3·9 = 27 · spent 24 · banked 3 ≥ 0"; (potential) "ĉ = c + ΔΦ = 1 + 2 = 3 · Φ = 2·9 − 16 = 2 ≥ −1" (on a resize "ĉ = (n + 1) + (2 − n) = 3") · cost: total actual cost against 3n · inputs: inserts only, from an empty array of capacity 1 (OI Wiki's start; the exploration's "push and pop at the boundary" is dropped: OI Wiki never shrinks the array) · labels: element values on the cells; each cell's banked credits as coins stacked on it in accounting mode, hover names on the coins
```

The figure stands where OI Wiki's trace stood (block 2, after "Here is a concrete example:"). The trace's own starting state (four full cells holding 2 credits each) is not reachable from capacity 1 under the stated charge, so the figure starts from capacity 1 and runs the charge as stated; no words on the page mention the difference.

**Source figures, keep or drop.** OI Wiki's page has no figure; the credit trace is code, replaced as above. The stack table is a table and stays in block 4.

## Extra simulations

- `sim-multipop`: a stack under a seeded run of push, pop and multi-pop(k), each pushed element carrying its banked unit, multi-pop spending them, with Φ(h) = |S| drawn as the stack's height, so the reader sees one picture for the three analyses of blocks 4 and 5.

## Exercises

No open (non-NC) exercise exists for any 1.5 concept. NC cards only, keyed, in `exercises-nc.json`:

| concept | items | answer shape | note |
|---|---|---|---|
| amortized-analysis, potential-method | mitocw-6-046j-spring2015 ps4 4-1 "Extreme FIFO Queues" | `open`, the key as solution | it uses queues (3.2): config item 24 and `exploration.md` place it here, config item 23 sends an item spanning two sections to the later one (see Questions) |
| amortized-analysis | mitocw-6-046j-fall2005 ps6 (electronic billboard) | `open` | |
| amortized-analysis | mitocw-6-046j-spring2012 ps6 6-1 | `open` | |

`exercise_notes`: Erickson's lecture-note exercises on amortized analysis (14, CC BY-NC-SA, unkeyed) left out.

## Referents

None: no figure draws a named code variable. n (elements) and m (capacity) wear `size`; actual and amortized costs, credits, the 3n line and Φ wear `cost` (book `RULES.md`); the elements' values wear `key`.

## References item

- Erickson, lecture notes on amortized analysis, §9.3 "incrementing and decrementing counters" (CC BY-NC-SA 4.0, link only, config item 22): the one treatment of a counter that both increments and decrements, the concept that left the map.
- "Amortized Analysis" (video, profbillbyrne, CIU): the three methods worked on a lecture board.
- MIT 6.006, "Rolling Hashes, Amortized Analysis" (video, CC BY-NC-SA, CIU): table doubling analysed in an MIT lecture.

## Attribution

- OI Wiki Team and contributors, *OI Wiki*, basic/amortized-analysis, https://github.com/OI-wiki/OI-wiki (c794414), CC BY-SA 4.0 with the SATA terms: "translated from the Chinese and adapted"; "Thanks to the OI Wiki Team and its contributors", linking the contributor list. (A person stars the repository; not an agent.)
- `notes`: "OI Wiki's code examples are not included." `ai`: text (the translation) and figures, this model; `built`.
