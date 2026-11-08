# Chapter 1 config: Algorithms and their cost

Status: **agreed** (2026-11-08, METHOD §4.4 decision 19: every recommendation accepted). One setting per line (root item 10). The per-section loop may begin; the exercise choice is at the end.

1. Chapter: 1 Algorithms and their cost, folder `ch01`, sections 1.1–1.6, 27 concepts (`exploration.md`).
2. Start point: 1.1, then in order to 1.6 (the book's first template is 2.3 or 2.2, `RULES.md`).
3. Loop: one section per page, with a stop after each section for review (root item 2); the plan of each section is reviewed before it is built (root item 5).
4. Sources per concept: the winners in `judgements/ch01-03-reconciled.md` (final table, chapter 1) plus `random-variable` from `mcs2018:19.1` (decision 18); one source per concept, its words kept whole; per-block `data-source` and `data-locator` as listed in `exploration.md`.
5. Worked example and Huntington–Hill: `jeffe:0.3` (ApportionCongress) carried whole in 1.1 (decision 18), the home of `apportionment` (decision 19).
6. Erickson's 0.2 "Compass and Straightedge": carried whole with the 0.2 blocks, no concept row (decision 19).
7. Erickson text: transcribed from the PDF, never from the cached `.txt`.
8. Translation: the three 1.5 blocks from OI Wiki (≈1,420 words) under `docs/prompts/translate.md`, AI-marked as translations; no OI Wiki code copied.
9. Bridges: B2 and B3 in the leads, B5 as links; B1 is settled by item 6; no bridge in the text. A bridge that does not fit the lead goes back to the user.
10. Errata: notes 1–12 and 14 of `exploration.md` as correction footnotes, AI-marked; the source text unchanged.
11. Leads: one or two sentences, AI-marked, naming the section's tier (all six sections Essential) and the concepts of another tier (1.1 lattice and Huntington–Hill Advanced; 1.2 harmonic Advanced; 1.3 multivariate Big-O Advanced; 1.5 potential Advanced; 1.6 indicators Advanced), the indexing convention, and the section's bridges, within 80 words. 1.6's lead carries one sentence on the three probability notations (decision 19).
12. Objectives and summaries: none (no source prints them).
13. Chapter introduction and summary pages: none.
14. Figures: the ten Sims of `exploration.md` as seeds; each plan argues its own lines. Source figures (ODS bigoh and harmonic plots, Erickson's traces) are originals behind the toggle; Erickson's two historical scans kept as photographs with their credits where the text points at them.
15. Figure label: Sim or photograph only, no figure numbers (decision 19).
16. Code beside the visual: in sim-peasant, sim-lattice, sim-apportion and sim-loop-count; none in the property and growth figures (sim-halving, sim-harmonic, sim-big-o-witness, sim-growth-race) and none in sim-coin-tosses.
17. Code shown: the source's own (Erickson pseudocode, ODS Java); runnable Python/JS counterparts only where an exercise needs them.
18. Depth: 2D throughout; no 3D scene.
19. Extra simulations (root item 15): none proposed beyond the seeds until the plans.
20. Colour: types `cost`, `size`, `key`, `index`; referents per figure (`exploration.md`), named code variables as referents and the `index` colour for unnamed positions (decision 19); probabilities untyped.
21. Derivations: the candidates in `exploration.md`, each scored in its plan.
22. References item: at most three links per section, each with one sentence; all CIU videos are link-only (their licences could not be read). 1.5's References item carries jeffe-notes 9.3 (incrementing and decrementing counters, CC BY-NC-SA, link only) for the concept that left the map (decision 19).
23. Exercise placement: end exercises to the Exercises system; no inline Try Its (no source prints one); a figure's predict pause is a figure control only, never an exercise card (decision 19). An item that tests concepts of two sections goes with the later one, tagged with both.
24. Exercises held elsewhere: Erickson ch. 1 Factorial item and Aspnes 202 B.1.1 → 4; ODS ch. 1 ex. 1, 5, 6, 7 → 3, 5, 8; MIT 6.006 S20 ps0 0-6 (NC) → 2.3; MIT 6.006 F11 ps1 1-3 to 1-6 (NC) → 6; OpenDSA AnalProblemTF10–12 → 10; MIT 6.856J → 22.
25. Bloom levels and concept tags: AI-judged.
26. `ai`: the building agent's model id and effort per part; `built` the ISO date.

## Exercise count report (root item 13)

Counted from `dossiers/ch01.md` (Exercises tables) and `judgements/ch01.md` (ranked exercises), with excluded sources removed. "Items" are the sources' own items; a source row that gives no number is counted as one row and said so. Proposed new: none, under METHOD decision 4 (no AI-written exercises).

- **Check** (keyed multiple choice, true/false, fill-in; OpenDSA): 88 printed (1.1: 30, 1.2: 6, 1.3: 23, 1.4: 28, 1.6: 1), plus 10 OpenDSA summary sets that redraw the same items; 87 keyed and usable (the judge drops AlgAnlsMCQalgdfn, whose key contradicts Erickson). Available as `choice` or `number` once a converter reads OpenDSA's Khan-format HTML; 6 of the 1.2 items are parameterised generators and become one fixed instance each.
- **Trace** (keyed interactive ordering; OpenDSA CompareGrowth, GrowthRatesPRO, 1.3): 2 printed, 2 keyed; available with the `sequence` answer type (shared library, not yet built).
- **Exercise** (written):
  - keyed in the source: 130 (1.2: Aspnes 2; 1.3: Aspnes 2; 1.6: brisk 25, Wikibooks 87, Aspnes 14), available now;
  - partly keyed: 80 (1.6: Levin 46, of which the first file keys 10 of 16 and the rest are not yet counted; Applied Combinatorics 34, of which 28 have a hint or answer);
  - unkeyed: 209 in the chapter (1.1: Erickson ch. 0, 5; 1.2: MCS 14.12–14.17, 6; 1.3: MCS 14.18–14.42, 25, and Applied Combinatorics, 6; 1.6: MCS ch. 15–19, about 115, Applied Combinatorics 7, OpenIntro 45), available only with AI solutions. By what writing them takes, counted by source and not yet item by item: about 5 explain or design (Erickson), about 31 prove (MCS 14.x), about 173 compute (MCS 15–19, Applied Combinatorics, OpenIntro), some of MCS 15–19 being proofs. Erickson's ex. 5 (Huntington–Hill by divisor) leans on 0.3, now in 1.1.
- **Code** (implement against tests):
  - with source tests: 4 (difference-of-squares 9 tests, grains 11, baffling-birthdays 17, pascals-triangle 8); references run: the Exercism examples for difference-of-squares and grains pass, the judge's own references for the other two pass. Available once the `code` answer type and runners exist (app);
  - samples only (Kattis, statement plus 1–3 samples, no reference on file): 13 (1.2: 5; 1.6: 8), available only with AI tests and an AI reference (marked `generated_by: "ai"`). The judge rates 6 a good fit (howmanydigits, stirlingsapproximation, inversefactorial, dicecup, anagramcounting, fruitbaskets) and flags 7 (loworderzeros and factorialpower are number theory; subcommittees is factorisation; catalan never defines Cₓ; diceyfrequencies misstates its sum; estimatingtheareaofacircle is arithmetic; expectedearnings tests one expectation, not linearity);
  - test cases with no statement: peasant multiplication (TheAlgorithms 13 doctests; trekhleb 2 jest suites, run and passing): test sources only, no exercise (decision 19).
- **NC cards** (`exercises-nc.json`): 34 keyed (1.2: 1; 1.3: 4; 1.4: 5, one a code exercise with tests; 1.5: 3; 1.6: 21), 30 unkeyed (Erickson's notes: 14 on amortized analysis, 16 on probability), 4 statement-only (Project Euler 15, 20, 34, 53, answers unpublished).
- **Concepts with no open exercise**: underspecified-algorithm, multivariate-big-o, amortized-analysis, aggregate-accounting and potential-method (1.5 has NC cards only), peasant-multiplication (tests, no statement), lattice-multiplication (its only exercise is held for chapter 4), apportionment (Erickson's ex. 5 is unkeyed); running-time-guarantees has no exercise that separates amortized from expected time; word-ram has none on w ≥ log n; random-variable has none ranked (the judge ran before decision 18).

## The exercise choice (decision 19)

Per kind: **check** items, the judge's top three ranked entries per concept (an entry is one ranked line of `judgements/ch01.md`, which may be a set of related OpenDSA files); **trace** items wait for the `sequence` answer type; **written** items keyed only, at most about five per concept, in the judge's order (unkeyed and partly keyed items left out and named in `exercise_notes`); **code** items with source tests or Exercism track tests now, Kattis with AI tests only where the judge rated the fit good, at most two code items per concept; **NC cards** keyed only. New exercises: none (decision 4). An item ranked for concepts in two sections goes with the later section and is listed there.

| § | concept | check | written (keyed) | code | NC cards (keyed) |
|---|---|---|---|---|---|
| 1.1 | algorithm | opendsa ProblemAlgorithmProgramTF1–TF11 + AnalPrelimSumm; opendsa AlgAnlsMCQrelalgprb (AlgAnlsMCQalgdfn not used: its key contradicts the winner) | none (jeffe 0 ex. 1 unkeyed) | none | none |
| 1.1 | underspecified-algorithm | none | none | none | none |
| 1.1 | describing-algorithms | the ProblemAlgorithmProgramTF set above, tagged with both | none (jeffe 0 ex. 5 unkeyed) | none | none |
| 1.1 | need-for-efficiency | opendsa IntroMCQeff, IntroMCQeff2 (AnlsIntroMCQszip and FasterCorASumm go with 1.4) | none (ODS ex. 7 unkeyed, held) | exercism difference-of-squares (9 canonical tests; the Exercism example passes) | none |
| 1.1 | interface-vs-implementation | opendsa ADTMCQadt, ADTMCQinter, ADTMCQds + IntroADTSumm | none (ODS ex. 1, 5, 6 unkeyed, held) | none | none |
| 1.1 | lattice-multiplication | none | none (held for 4) | none | none |
| 1.1 | peasant-multiplication | none | none | none (test cases, no statement) | none |
| 1.1 | apportionment | none | none (jeffe 0 ex. 5 unkeyed) | none | none |
| 1.2 | logarithms | opendsa logarithms_1, logarithms_1.5, logarithms_2 + MathLogSumm, MthBgFIBlgbs1/2 (one fixed instance per generator); opendsa AlgAnlsFIBsmlintgr2 (`number`) | none | exercism grains (11 tests; the Exercism example passes); kattis howmanydigits (CC BY-SA 3.0, AI tests; tagged with factorials-stirling too) | none |
| 1.2 | factorials-stirling | none | aspnes-202 A.5.2 (B.1.1 held for 4) | kattis howmanydigits (above); kattis stirlingsapproximation (AI tests); inversefactorial is over the cap | none (Project Euler 20, 34 statement-only) |
| 1.2 | harmonic-numbers | none | none (MCS 14.12–14.17 unkeyed) | none | 6.042J F05 ps6 #7 |
| 1.3 | big-o | opendsa AnalPairMCQ1–AnalPairMCQ11 + UpperBoundsSumm | aspnes-202 A.6.2, A.6.3 | none | 6.006 S20 ps1 1-1; 6.046J F05 ps1 1-1; 6.006 F11 ps1 1-1; 6.042J F05 ps6 #8 (tagged with big-omega-theta where they ask for Ω or Θ) |
| 1.3 | big-omega-theta | opendsa ThetaUpperMCQ, AlgAnlsTFbgthta + LowerThetaSumm (MisunderstandingsTF goes with 1.4) | aspnes-202 A.6.2 (above, tagged with both) | none | as big-o |
| 1.3 | multivariate-big-o | none | none | none | none |
| 1.4 | word-ram | opendsa AnlsIntroMCQszip + FasterCorASumm (tagged with need-for-efficiency); opendsa MthBgMCQrmacc, MthBgMCQdskacc (the judge calls rmacc a weak fit; kept as ranked) | none (jeffe 0 ex. 3 unkeyed) | none | none |
| 1.4 | complexity-analysis | opendsa AnalProgramMCQtheta1–9 + AnalProgramSumm; opendsa AnalProblemTF1, TF2, TF4–TF7 + AnalProblemSumm | none (jeffe 0 ex. 2, 4 and appcomb unkeyed) | none | none here (6.006 S20 ps0 0-6 → 2.3; 6.006 F11 ps1 1-3 to 1-6 → 6) |
| 1.4 | running-time-guarantees | opendsa AlgAnlsMCQsqlsrch, AlgAnlsTFsqlsrch1, AlgAnlsTFsqlsrch2; opendsa MisunderstandingsTF1–6 + MisSumm (tagged with big-o and big-omega-theta) | none | none | none |
| 1.5 | amortized-analysis | none | none | none | 6.046J S15 ps4 4-1 "Extreme FIFO Queues" (tagged with potential-method); 6.046J F05 ps6 (electronic billboard); 6.046J S12 ps6 6-1 |
| 1.5 | aggregate-accounting | none | none | none | none (jeffe-notes 09 ex. 1 unkeyed) |
| 1.5 | potential-method | none | none | none | 6.046J S15 ps4 4-1 (above) |
| 1.6 | counting | none | brisk countingEx items 1–5 (item 2's "skip one or more" admits the empty costume, a note for the card) | exercism pascals-triangle (8 tests); kattis anagramcounting (AI tests) | 6.042J F05 ps7 #1–#5 (Project Euler 15, 53 statement-only) |
| 1.6 | probability-basics | none | brisk probabilityEx items 1, 4, 6, 7, 8 | exercism baffling-birthdays (17 tests; the estimate cases need a tolerance); kattis dicecup (AI tests) | 6.042J F05 ps9 #1–#7 (tagged with conditional-probability) |
| 1.6 | conditional-probability | none | brisk probabilityEx items 16, 17, 18 (with item 9's set-up on the card); wikibooks Probability/Conditional_Probability, its first two keyed exercises | none | 6.042J F05 ps9 (above) |
| 1.6 | random-variable | none | none ranked | none | none |
| 1.6 | linearity-of-expectation | none | aspnes-202 C.9.3, F.5.3, F.5.4; wikibooks Probability/Random_Variables, its first two keyed exercises (tagged with random-variable) | none (kattis expectedearnings: weak fit) | 6.042J F05 ps10 #1–#8 (#1 tagged with geometric-expectation, #8 with indicator-variables); 6.006 S20 ps0 0-2 |
| 1.6 | indicator-variables | none | none (MCS 19.x unkeyed) | kattis fruitbaskets (AI tests) | 6.042J F05 ps10 #8 (above) |
| 1.6 | geometric-expectation | none | none (MCS 19.x unkeyed) | none | 6.042J F05 ps10 #1 (above) |

Trace items deferred: OpenDSA CompareGrowth and GrowthRatesPRO (1.3). Every Kattis card here is CC BY-SA 3.0 (`kattis-by-sa`); its tests and reference are AI-written and marked. Left out and named in `exercise_notes`: every unkeyed written item above, the partly keyed Levin and Applied Combinatorics sets, the unkeyed NC cards (jeffe-notes 01 and 09) and the statement-only Project Euler cards.
