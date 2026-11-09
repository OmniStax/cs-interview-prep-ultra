# Plan: 3.5 Stack applications: expression evaluation

Status: **plan, built from in the same run** (brief `briefs/section-build.md`: chapters 2 and 3 have no separate plan review; questions decided below), 2026-11-09. Read for this plan: root `RULES.md`; the book's `RULES.md`, `COLOR.md`, `METHOD.md` (§1–§3, §5, decisions 1–21); `LOG.md` (passes 1–8); `ch03/config.md` and `exploration.md`; `judgements/ch01-03-reconciled.md` (winners, bridges, errata, indexing, rulings of 2026-11-08), `judgements/ch03.md` §3.5 and its builder notes, `judgements/ch01-03-references.md` (the forth, calculator and TheAlgorithms rows); the three `concepts.json` rows; `ch01/plans-summary.md`, `ch01/1.5/plan.md`, the built 1.1 and 1.5, and the built 2.7 (the first cpa section, whose `tools/build_markdown.py` this section reuses unchanged); and the winning passage, `sources/_cache/cpa/src/string/expression_parsing.md` at the pinned commit d55d3f5, whole.

One source, cp-algorithms (`cpa`, CC BY-SA 4.0), in English. 4 blocks, 3 concepts, 1 Sim (a debugger), no derivation, 3 code exercises, 2 NC cards.

**What the pinned page prints.** Prose, two display formulas, two full C++ listings (`expression_parsing_simple`, `expression_parsing_unary`) and two one-line C++ fragments (the `while` condition before and after the right-associativity change). C++ only: no Java, no Python, no image. So every Python, Java and JavaScript variant is an AI translation and carries `data-ai` (decision 20); the C++ is the source's and carries none.

## Lead (AI-marked, 53 words)

> An Advanced section on evaluating expressions with stacks: reverse Polish notation with one stack, which is Essential, then ordinary infix expressions with two stacks, then unary and right-associative operators. Expressions are read character by character, and the only index is i, the position of the character the code is reading, counted from 0.

Tier: Advanced (the section's), rpn-evaluation Essential (config item 10). Indexing: none, tokens (`exploration.md`, reconciled table); the lead names the one index the code uses. Bridges: none (B1–B18 assign none to 3.5). cpa leans only on "stack" (3.1) and on O(n) (1.3).

## Blocks (`<h2>`), in cpa's own order

| # | block id | `<h2>` | `data-source` | `data-locator` | translate | what it holds |
|---|---|---|---|---|---|---|
| 1 | `rpn` | Expression parsing (source, the article's title); "Reverse Polish notation" `<h3>` | cpa | `cpa:string/expression_parsing` lead + #reverse-polish-notation | no | the problem in O(n); the bold "reverse Polish notation"; the example and its RPN as two displays; Hamblin and Łukasiewicz; the one-stack evaluation; "Obviously this simple evaluation runs in O(n) time." |
| 2 | `parsing` | Parsing of simple expressions (source) | cpa | `cpa:string/expression_parsing#parsing-of-simple-expressions` | no | binary, left-associative; the two stacks and their invariant; the four cases; listing `expression_parsing_simple` as a four-language code set (C++ the source's); "implicitly used the reverse Polish notation" |
| 3 | `unary` | Unary operators (source) | cpa | `cpa:string/expression_parsing#unary-operators` | no | the unary test; priority above every binary operator (erratum 30's marker); unary plus and minus right-associative |
| 4 | `right-assoc` | Right-associativity (source) | cpa | `cpa:string/expression_parsing#right-associativity` | no | right-associativity; the two `while` fragments as code sets; listing `expression_parsing_unary` as a code set; then `sim-two-stack-parser` |

*Build note:* `exploration.md` had one block `unary-right` for both headings. cpa prints them as sibling `##` headings, so one block would hold two `<h2>`s; they are two blocks, each opened by its own heading, and the concept spans both (introduced in `unary`, reinforced in `right-assoc`).

Not carried: the front matter (`tags`, `e_maxx_link`). The page has no Problems list. Source text goes through `tools/build_markdown.py` (2.7's, imported unchanged; no shared tool changes), with a section `build_spec.py` holding placement, marks, the code sets and the figure's HTML.

## Concepts

| id | kind | tier | statement (reworded to cpa) | introducing span |
|---|---|---|---|---|
| `rpn-evaluation` | skill | Essential | In reverse Polish notation the operators come after their operands. To evaluate it, read it left to right with a stack: push each number; for an operator, take the top two elements off the stack, perform the operation and put the result back. At the end the one element left is the value, in O(n). | `rpn`, "The convenience of the reverse Polish notation is, that expressions in this form are very easy to evaluate in linear time." |
| `expression-parsing` | result | Advanced | With binary, left-associative operators and parentheses, an expression is evaluated in O(n) with a stack of numbers and a stack of operators kept in strictly descending priority within each pair of parentheses: push a number or an opening parenthesis; at a closing parenthesis, execute operators back to the opening one; before pushing an operator, execute every operator on top of the same or higher priority; at the end, execute what is left. This evaluates the reverse Polish notation implicitly. | `parsing`, "We will set up two stacks: one for numbers, and one for operators and parentheses." |
| `unary-right-assoc` | skill | Advanced | An operator is unary when it comes first, after another operator or after an opening parenthesis; it is executed on one value and given a priority above every binary operator. A right-associative operator (unary minus and plus, exponentiation) is postponed when the priorities are equal: the operators on the stack are executed only while their priority is strictly higher. | `unary`, "You can notice, that before an unary operator, there always is another operator or an opening parenthesis, or nothing at all" |

Edges as `concepts.json` has them, Hasse-reduced: `rpn-evaluation → stack` (3.1's), `expression-parsing → rpn-evaluation`, `unary-right-assoc → expression-parsing`. Terms: "reverse Polish notation", "RPN" (rpn-evaluation); "two stacks" in the parsing block (expression-parsing); "unary", "right-associative" (unary-right-assoc). The map's statements are kept in substance and reworded to cpa's words (chapter 1 question 27).

## Errata

- **30** (config item 9): after "And we need to chose the priority of a unary operator higher than all of the binary operators." A correction note: with exponentiation among the binary operators, as the next subsection has it, that rule reads −2^2 as (−2)^2 = 4, where the usual convention is −(2^2) = −4. The figure's `−2^2` input shows it.
- **31** (char negation): not noted in the first pass (config item 9).
- Typos that change no meaning stay as printed without notes: "the we execute", "than each block", "to chose", "an right-associative".

## Derivation candidates (root item 29)

None. The page prints no chain of equations; "Obviously this simple evaluation runs in O(n) time" is one move (each element is read once and the stack does O(1) work), score 1 + 0 + 0 < 4. Not built.

## Figures

The page prints no image, so nothing is kept or dropped. `exploration.md` named Wikipedia's Shunting yard.svg as an original; it is not the winning source's figure (one explanation per concept, METHOD §5), so the Sim has no original toggle (question 4).

```
sim-two-stack-parser · Sim (replaces nothing) · expression-parsing, unary-right-assoc, rpn-evaluation · flow by animation; invariant made visible; variation by input · arrows: kinematic (the reading position i moves along the string; numbers and operators move onto and off the two stacks; an applied operator and its operands collapse into the result) · moving: one block per step, entries easing onto and off the stacks · choice input: cp-algorithms-style (2*5-1*2)/(11-9) = 4 (default) | unary minus -(3-5)*-2 = -4 | right-associative 2^3^2 = 512 | 8-3-2 = 3 (left-associative, for contrast) | −2^2: cpa's priority rule gives 4 (erratum 30, the bad case: result in PAL.bad) · headline per stop, saying what the block did with the live tokens ("* on top has priority 2 ≥ 1, so it is applied first: 2 * 5 = 10") · graph none · 2D · code: cpa `expression_parsing_unary`'s `evaluate`, with its `while` condition in the general form cpa prints under Right-associativity (`left_assoc`), C++ canonical; Python, Java and JavaScript translated line for line; all four AI-marked, since the C++ is cpa's function with cpa's own replacement made (question 2); helpers (priority, left_assoc, process_op) not shown, the priorities drawn as a legend: + − 1, * / 2, ^ 3 (right-associative), unary 4 (right-associative); lines 1–47 · blocks: open "push the opening bracket" 9–11 touches op; close "execute back to the opening bracket" 12–18 ⟶ cl-apply "execute the top operator" 14–15 touches st, op; operator "an operator" 19–31 ⟶ read-op "read it: unary after an operator, a bracket or nothing" 20–22 touches cur_op; outrank "execute every operator on top that outranks it" 23–29 ⟶ op-apply "execute the top operator" 27–28 touches st, op; push-op "push it" 30–31 touches op, cur_op; number "read a number and push it" 32–39 touches st, i; finish "execute what is left" 42–45 ⟶ fin-apply 43–44 touches st, op; result "the one number left is the value" 46 touches st · opens at level 1 (read, execute, push), each token's blocks one stop each · invariant: within the innermost bracket, op's priorities strictly rise from bottom to top (a right-associative pair may repeat), the run above the last "(" shaded in the index tint · readout: the watch (i, cur_op, may_be_unary), and under the strip the reverse Polish notation emitted so far (each number as it is pushed, each operator as it is executed), which st evaluates as 3.5's first block says · cost: "characters read 9 of n = 16 · operators executed 3 of 5 pushed", each character read once and each operator pushed and executed once, O(n) · labels: the characters of s in strip cells with their indices; st and op named under their columns in their referent colours; i at its pointer; priorities beside operator entries
```

Extra Sim considered and not built (config item 15): a one-stack RPN evaluator on cpa's `a b c * d * + …`. The debugger's RPN row already shows st evaluating the notation it emits.

## Exercises (config.md, decision 19)

| concept | kind | item | answer shape | status |
|---|---|---|---|---|
| rpn-evaluation | code | Exercism `forth` (MIT): description.md as the statement; the 54 canonical cases the Python track runs (the track sets `evaluateBoth` off) as source tests; the track's `example.py` as the Python reference (source); an AI JavaScript reference | `code`, entry `evaluate(instructions)`, `expect` a list or `raises` StackUnderflowError / ZeroDivisionError / ValueError as the track maps the canonical errors (`changes` says so); no bound (user-defined words expand) | ships |
| expression-parsing, unary-right-assoc | code | Kattis `calculator` (CC BY-SA 3.0, Per Austrin): the statement; its sample (10 lines) visible; AI tests (precedence, left-associativity, nested brackets, unary minus before a bracket and after an operator, spaces, the ±500 range, long products) checked with exact fractions and kept off rounding ties and −0.00 | `code`, a stdin program; `compare: tokens`; AI references in Python and JavaScript; bound n on a long expression | ships |
| expression-parsing | code | Kattis `bracketsequence` (CC BY-SA 3.0, Timon Knigge): the statement; its six sample files (the first visible); AI tests (deep nesting to n = 3·10⁵, zeros, the modulus, alternating depth) | `code`, a stdin program; `compare: tokens`; AI references; bound n | ships |
| rpn-evaluation, expression-parsing | NC check | *pythonds* Self Check `postfix1` (convert `10 + 3 * 5 / (16 - 4)`) | `open`, the key "10 3 5 * 16 4 - / +" as its solution, `generated_by: source` | ships in `exercises-nc.json` |
| rpn-evaluation | NC check | *pythonds* Self Check `postfix2` (evaluate `17 10 + 3 * 9 / ==`) | `number`, 9 | ships in `exercises-nc.json` |

No exercise combines unary minus with `^` (erratum 30): calculator has no `^`. `exercise_notes`: kattis circuitmath (samples only, not rated good), TheAlgorithms `postfix_evaluation.py`, `dijkstras_two_stack_algorithm.py`, `infix_to_postfix_conversion.py` and tryalgo `arithm_expr_eval` (test sources with no printed statement), the Wikibooks traces and OpenDSA's postfix proficiency exercises (waiting for `sequence`), pythonds `postfix3` (it asks the reader to modify a function the book only links, and its key writes the exponent as `**` where its question writes `^`), pythonds end-of-chapter exercises 2–5 and 10–13 (unkeyed), Kattis polish (chapter 4), Exercism wordy (not a stack exercise).

## Referents

| id | what | figures | blocks that mark it |
|---|---|---|---|
| `st` | the stack of numbers | sim-two-stack-parser | `parsing` ("one for numbers") and the caption |
| `op` | the stack of operators and parentheses | sim-two-stack-parser | `parsing` ("one for operators and parentheses", "the second stack", "the top of the stack") and the caption |
| `i` | the position of the character being read | sim-two-stack-parser | the lead |
| `cur_op` | the operator just read | sim-two-stack-parser | `unary` ("the current operator") |

One group of four. Types drawn: `index` (the strip's index labels, the invariant tint), `cost` (the counter). Maths in the text stays in ink (no variables rows, as chapters 1 and 2).

## References item (at most three; no `section.json` field carries them yet)

- Wikipedia, "Shunting yard algorithm": the same two-stack idea written as a conversion to postfix, with a worked table.
- None from CIU for this section.

## Attribution

- cp-algorithms contributors, *Algorithms for Competitive Programming*, string/expression_parsing, https://github.com/cp-algorithms/cp-algorithms (d55d3f5), CC BY-SA 4.0, adapted.
- Exercism (MIT) for forth; Per Austrin (calculator) and Timon Knigge (bracketsequence), Kattis, CC BY-SA 3.0; Miller and Ranum, *pythonds*, CC BY-NC-SA 4.0, in `exercises-nc.json` only.
- `notes`: none needed (nothing of the page is left out but its front matter). `ai`: text and figures, this model; `built`: the build date.

## Questions (decided here; the brief asks for no stop)

1. **The source's code languages.** The pinned page prints C++ only. *Decided:* C++ is the source's variant in every code set; Python, Java and JavaScript are AI translations with the mark, Python first.
2. **The debugger's code.** cpa's unary listing handles + − * / and unary ± only; its `while` is specialised to "unary is right-associative". The exploration's inputs (right-associative `^`, −2^2) need the general `while` cpa prints under Right-associativity and a `^`. *Decided:* the panel shows only `evaluate`, cpa's unary listing's function with its `while` replaced by cpa's own general fragment (`left_assoc`), every other line cpa's; the helpers are not shown, and the figure draws the priorities it uses as a legend (+ − 1, * / 2, ^ 3, unary 4, as cpa says: unary above every binary operator). Since the C++ is changed, all four languages carry the AI mark.
3. **The listing the figure shows, shown again?** Chapter 1's question 17 shows a listing once, as the panel where it stood. Here the panel is not cpa's listing (a part of it, changed), so cpa's listing stays in the text as its own code set, the source's words, and the Sim stands after it.
4. **An original for the Sim.** *Decided:* none; Shunting yard.svg is Wikipedia's, not the winner's, and the cpa page prints no figure. The Sim is plain, eyebrow "Sim".
5. **Priority of `^` against unary minus.** *Decided:* cpa's rule as written (unary above every binary operator), so the figure reproduces erratum 30 on its −2^2 input, flagged in `PAL.bad`, with the usual −4 named in the headline.
6. **pythonds self-checks.** `config.md` counts six for 3.5; the cached page prints three (postfix1–3). *Decided:* postfix1 and postfix2 ship; postfix3 is left out (above).
7. **forth's user-defined words.** The judge offered "a stretch part, or cut them"; the code answer type has no parts. *Decided:* one card with every applicable case, the statement kept whole.
8. **Which Kattis items.** The orchestrator named calculator and circuitmath "where rated good"; `config.md` rates calculator and bracketsequence good and circuitmath not. *Decided:* `config.md`'s two.
9. **The two one-line fragments.** *Decided:* code sets like the listings (decision 20: every listing in four languages), each fragment translated as one condition.
10. **Predict pause ("pop or push?").** The library has no predict pause yet (1.1's pass). *Decided:* not built; the outrank block's stop and headline say which it is.
