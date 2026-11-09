# Translation notes

The places where a translated block of this book could not follow its source word for word, and the terms that were hard to decide (`docs/prompts/translate.md` §4 and §2). The terms themselves are in `glossary.en.json`; each chapter's `config.md` repeats its forced scenarios as a table.

## Forced scenarios

| file | where | what was done | why |
|---|---|---|---|
| `ch01/1.5/translation.md`, `text.html` | the first sentence of 引入, 聚合分析, 记账分析 and 势能分析 (blocks `amortized`, `accounting`, `potential`) | OI Wiki's English glosses in parentheses after its Chinese terms (均摊分析（Amortized Analysis）…) are not repeated after the English term | translate.md §4.3: a parenthesis that gives the English word reads as a repetition in English |

## Terms decided in a chapter pass

- 预存 (1.5): first rendered "prestore", which is not an English word; now "save" ("saved *n* units", "the saved credit"), after Wikipedia's Amortized analysis ("accumulates a saved 'credit'"). Chapter 1 pass, 2026-11-09.
- 原理 / 示例 / 扩展示例 (1.5 headings): "Principle", "Example", "Extended example", the plain register of an English textbook. Chapter 1 pass.
- 均摊分析 and 均摊成本: "amortized analysis" and "amortized cost", confirmed against Wikipedia (NIST's DADS unreachable from the session). Chapter 1 pass.

## Outstanding

The owner's humanizer review of the translated blocks (translate.md §10).
