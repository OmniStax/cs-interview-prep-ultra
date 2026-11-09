# Brief: plan and build one section (chapters 2 and 3)

The user asked for chapters 2 and 3 to be built and published. There is no
separate plan review for these chapters: write the plan, then build from it
in the same run. Chapter 1 is built and is the model. Copy its pipeline and
conventions exactly.

## Read first

- **Root rules:** /home/user/OmniStax/RULES.md, all of it.
- **This book:** RULES.md, COLOR.md, METHOD.md (§1–§3, §5, and decisions
  1–21 in §4.4), glossary.en.json, LOG.md (chapter 1's passes, including
  pass 8, the chapter pass, and its "copy / avoid" notes).
- **Your chapter:** <chapter>/exploration.md and <chapter>/config.md (the
  exercises chosen per concept, already agreed).
- **Judgements:** judgements/ch01-03-reconciled.md (winners, bridges, errata,
  indexing, translations; "Rulings applied 2026-11-08"),
  judgements/ch0N.md for your chapter, and judgements/ch01-03-references.md
  (which exercise references were run and what failed).
- **Concepts:** concept-map/toc.md and concepts.json rows for your section.
- **Chapter 1 as the model:** ch01/plans-summary.md, one chapter 1
  plan.md, and the built ch01/1.1 and ch01/1.5 (build_spec.py, text.html,
  figures.js, section.json, exercises-nc.json).
- **Tools:** tools/ (extract_jeffe.py, build_text.py, read_latex.py,
  extract_mcs.py, extract_opendsa.py, build_translation.py, build_blocks.py,
  build_section.py, apply_terms.py, nc_cards.py).
- **App docs:** /home/user/OmniStax/docs/content-format.md,
  docs/prompts/interactive-figures.md (the debugger API, F.code in four
  languages, F.ds), manim-style.md, derivations.md, translate.md (for OI Wiki
  passages), docs/design-code-and-debugger.md;
  /home/user/OmniStax/omnistax-content/tools/README.md (ost).

## 1. Plan

Write <chapter>/<section>/plan.md in chapter 1's plan format:
- **the lead** (≤ 80 words: tier as Essential, Advanced or Beyond; the
  indexing convention; any concept of another tier);
- **the blocks in order,** each with its locator, data-source, and whether
  it needs translation;
- **bridges,** with their wording, AI-marked;
- **concepts,** with each one's introducing span;
- **errata;**
- **derivation candidates,** with the item-29 score;
- **one plan line per figure,** with the debugger fields (code, blocks,
  inputs) where code sits beside the visual, plus keep/drop for every
  source figure;
- **exercises** with their answer shapes;
- **referents;**
- **attribution.**

Don't stop for review. Decide what chapter 1's answered questions already
settle the same way. Put any genuinely new question in a "Questions" list at
the end of the plan, choose its recommended answer yourself, and go on.

## 2. Build

### Production rules
- **Never reproduce long source passages in your own output.** Source text
  goes through scripts, plus a per-section build_spec.py holding anchors,
  marks and a replacement table with a reason for each entry. Erickson comes
  from glyph extraction, never from pdftotext digits.
- **OI Wiki passages are translated** under translate.md, block by block,
  with tools/build_translation.py's parity check. They are AI-marked as
  translations, using the book's glossary. OI Wiki's code is not licensed and
  is never used.
- **Code listings are four-language code sets** (decision 20): Python first.
  A language the source doesn't print is an AI translation and carries
  data-ai. The source's own code stays as printed where it is the source's
  words.
- **Debugger figures** use F.code, F.trace, F.debug and F.ds. Step by named
  block. Shade the invariant. Show a cost counter in the readout. Input
  presets include the bad case. Never give a figure hundreds of stops. Debugger
  canvas text is 26–40 logical units. Fit every scene to its canvas.
- **Captions are about the subject,** never about the figure or its controls
  (root rule 17). An unnumbered Sim's eyebrow is "Sim" (rule 14).
- **Concepts go through ost.** section.json is written once with
  build_section.py, then edited with `ost set` or `ost field`. The terms pass
  is tools/apply_terms.py with a terms.jsonl.
- **Exercises are those config.md chose,** with these rules:
  - Code exercises use the `code` answer type, with tests and a reference
    solution. AI-written tests and references carry generated_by "ai".
  - Run the references isolated (decision 17: copy into a fresh scratch dir,
    `python3 -I`).
  - NC cards go in exercises-nc.json, in 1.6's shape.
  - Items waiting for the OpenDSA converter or the `sequence` answer type
    are left out and named in exercise_notes.
- **Every block carries data-source and data-locator.** Translated blocks
  carry data-ai. The footer credits come from these.

### Checks until clean
- `ost check` for the book.
- In /home/user/OmniStax/omnistax-web, `npm run check:content` and
  `npm run check:code`, each with
  `OMNISTAX_CONTENT_DIR=/home/user/OmniStax/omnistax-content`. The book is
  symlinked there.

### Browser pass
- Run `npm run dev -- --port <your port> --force` with
  `OMNISTAX_CACHE_DIR=/tmp/claude-0/-home-user/249e18c8-3562-5258-9ce2-fd057404a6b0/scratchpad/vite-<section>`.
  The private cache is required: shared caches break MathJax.
- Use Playwright with `NODE_PATH=/opt/node22/lib/node_modules`. Reuse the
  scratchpad scripts (shoot.cjs, pageshot.cjs, and those under sec11–sec16).
  The page scrolls inside div.pane.
- Shoot every figure in light and dark at deviceScaleFactor 2, into
  /tmp/claude-0/-home-user/249e18c8-3562-5258-9ce2-fd057404a6b0/scratchpad/sec<chapter><section>/.
- Step every debugger figure and derivation through. Look at every shot and
  fix what's wrong.

## Concurrency

Other agents are building the other sections of this chapter at the same
time.
- Touch only your own section folder and any media you add.
- Change shared tools only backward-compatibly. Re-run 1.1's build from a
  frozen copy to confirm its output is unchanged, and say so.
- Re-read sources/registry.json before appending to it.
- Don't commit in the book repo; the orchestrator commits.
- Write your LOG entry to <section>/log-pass.md.

App bugs:
- Note them precisely.
- Fix a small, clear one in a fresh clone,
  `git clone /home/user/OmniStax /tmp/claude-0/-home-user/249e18c8-3562-5258-9ce2-fd057404a6b0/scratchpad/app-<section>`,
  on a branch `claude/app-fixes-<section>`, with a test, and commit it.
  Don't push; say the clone path and commit.
- Never edit or switch branches in /home/user/OmniStax. Every agent's dev
  server runs from it.

## Report back

- what was built;
- check results;
- deviations from the plan, and the questions you decided;
- screenshot paths;
- what the chapter pass should reconcile.
