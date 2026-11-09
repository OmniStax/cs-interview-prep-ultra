# Translation notes

The places where a translated block of this book could not follow its source word for word, and the terms that were hard to decide (`docs/prompts/translate.md` §4 and §2). The terms themselves are in `glossary.en.json`; each chapter's `config.md` repeats its forced scenarios as a table.

## Forced scenarios

| file | where | what was done | why |
|---|---|---|---|
| `ch01/1.5/translation.md`, `text.html` | the first sentence of 引入, 聚合分析, 记账分析 and 势能分析 (blocks `amortized`, `accounting`, `potential`) | OI Wiki's English glosses in parentheses after its Chinese terms (均摊分析（Amortized Analysis）…) are not repeated after the English term | translate.md §4.3: a parenthesis that gives the English word reads as a repetition in English |
| `ch02/2.3/translation.md`, `text.html` | 例题 4 (block `sorted-pair`) and 例题 1 (block `variable-window`) | the box's heading prints "Example", without OI Wiki's number | the page carries only two of the source's four 例题, so its numbers 4 and 1 would count examples the reader never sees |
| `ch02/2.3/translation.md`, `text.html` | the same two boxes | each box, which restates a LeetCode problem, becomes a link to the English LeetCode page of the same problem (leetcode.com, not leetcode-cn.com), with LeetCode's English title | LeetCode's statements are link-only (RULES.md, Source), and the reader of the English book is sent to the English site |
| `ch02/2.4/translation.md`, `text.html` | `std::partial_sum`, `std::inclusive_scan`, `std::adjacent_difference` (blocks `prefix-sums`, `difference-array`) | OI Wiki's links to zh.cppreference.com point at the same pages of en.cppreference.com; the anchor text is unchanged | an English reader's reference; the Chinese pages are the same reference in translation |
| `ch02/2.4/translation.md`, `text.html` | 容斥原理 (block `prefix-sums-2d`) and 树状数组 (block `difference-array`) | OI Wiki's links to its own pages become links to the sections of this book that will carry those topics, Sections 40.4 and 30.2 (RULES.md, Links to sections not yet built) | RULES.md, Cross-references: a source's reference to a passage the book carries links the book's section |

## Terms decided in a chapter pass

- 预存 (1.5): first rendered "prestore", which is not an English word; now "save" ("saved *n* units", "the saved credit"), after Wikipedia's Amortized analysis ("accumulates a saved 'credit'"). Chapter 1 pass, 2026-11-09.
- 原理 / 示例 / 扩展示例 (1.5 headings): "Principle", "Example", "Extended example", the plain register of an English textbook. Chapter 1 pass.
- 均摊分析 and 均摊成本: "amortized analysis" and "amortized cost", confirmed against Wikipedia (NIST's DADS unreachable from the session). Chapter 1 pass.
- 区间 (2.3, 2.4): "range" in both sections. 2.3 first wrote "interval" (its window [l, r], "intervals with right
  endpoint r", the heading 维护区间信息) and 2.4 "range" (range sums, range updates, "over the range [l, r]"); range
  queries and updates are named so in English (Wikipedia, Fenwick tree: "range sum"; cp-algorithms: "Range Update and
  Point Query"), and an index range of an array is the same thing, so 2.3's three places now read "range". Chapter 2–3
  pass, 2026-11-09.
- 2.3's fourteen and 2.4's sixteen pending rows confirmed as their sections set them (`glossary.en.json`, every row
  decided). Chapter 2–3 pass.

## Outstanding

The owner's humanizer review of the translated blocks (translate.md §10).
