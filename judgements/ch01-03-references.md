# Reference runs: chapters 1 to 3

Run of 2026-11-08 under METHOD.md decision 17. It covers every code exercise with tests
that `judgements/ch01.md`, `ch02.md` or `ch03.md` ranks first or second for a concept
(the reconciliation pass moved no exercise), plus the two chapter 3 rejections. Each
source's own reference was run against the source's own tests.

**How it was run.**
- Isolation. Each file needed was copied from `sources/_cache/` into a fresh directory
  `R/<exercise-id>/`, where
  `R = /tmp/claude-0/-home-user/249e18c8-3562-5258-9ce2-fd057404a6b0/scratchpad/refrun`.
  Every run starts from `R/_work` (empty), uses `python3 -I` (Python 3.13.18) or
  `node` (v22.23.4), and has a `timeout`. Nothing was executed inside `sources/_cache`.
  No packages were installed. numpy 2.5.3 was already present.
- Harnesses. These are my own code, in `R/_harness/`:
  - `doctest_mod.py`: imports a module from the copy and runs `doctest.testmod`.
  - `unit_names.py`: runs named unittest tests.
  - `unit_file.py`: runs a unittest file by path.
  - `icc_build.py`: concatenates the icc solution notebook's code cells with the
    cached test file.
  - `ods_run.py`: runtime shims only, listed under ODS below.
  - `exer_canon.py`: Exercism canonical-data adapter.
  - `minijest.mjs` + `jest_hooks.mjs`: a describe/it/expect stand-in for jest, because
    jest is not installed. A self-check confirms it reports a failing expect.
  - `run_*.sh`: copy-then-run wrappers.
- Exercism. The cache holds problem-specifications only, so there is no reference on
  file. Each Python-track `example.py` (MIT) was fetched from `exercism/python` at
  `main` = `479f11b44b02337b0413e805b948491c2179615a`, along with the track's own test
  file and `tests.toml`, into `R/_dl/exercism-python/`.
  - Each example was run against the cached `canonical-data.json` (cache commit
    `7b49ec4`). Superseded cases (`reimplements`) were dropped. Cases the Python track
    marks `include = false`, and mutually exclusive groups the track does not use,
    were counted as not applicable.
  - Each example was also run against the track's own test file.
  - Error-message wording is compared separately. A case counts as a logic pass when
    the right condition raises.
- Counts. Doctest counts are examples attempted. unittest counts are tests run, with
  the number of assert calls in parentheses where it helps.

Wrapper commands are shown short. `run_ta.sh X P` means "copy P into `R/X/`, then
`python3 -I R/_harness/doctest_mod.py R/X <module>`" (see the script).

## Chapter 1

| concept | rank | exercise | reference used | command | result | notes |
|---|---|---|---|---|---|---|
| need-for-efficiency | 1 | `exercism:difference-of-squares` | Exercism Python `example.py` (fetched) | `run_exer.sh difference-of-squares` | **pass** 9/9 canonical; track tests 9/9 | Returns floats (`/ 2`, `/ 6`). They compare equal to the integer expectations, but a JS/strict runner would need `//`. |
| logarithms | 2 | `exercism:grains` | Exercism Python `example.py` (fetched) | `run_exer.sh grains` | **pass** 11/11 canonical (3 error cases, wording identical); track 11/11 | |
| factorials-stirling | 1 | `kattis:howmanydigits` | **no reference on file** | none | not run | 1 sample file cached. The judge's own solution had passed it (ch01.md). |
| factorials-stirling | 2 | `kattis:stirlingsapproximation` | **no reference on file** | none | not run | 1 sample file. |
| counting | 2 | `kattis:anagramcounting` | **no reference on file** | none | not run | 1 sample file. |
| probability-basics | 2 | `kattis:dicecup` | **no reference on file** | none | not run | 3 samples. |
| linearity-of-expectation | 2 | `kattis:expectedearnings` | **no reference on file** | none | not run | 3 samples. |
| indicator-variables | 2 | `kattis:fruitbaskets` | **no reference on file** | none | not run | 1 sample. |
| peasant-multiplication (ranked "none shippable"; run because ch01 says trekhleb was not run) | n/a | trekhleb `algorithms/math/bits` `multiplyUnsigned.test.js` + `multiply.test.js` | trekhleb `multiplyUnsigned.js`, `multiply.js` (+ `multiplyByTwo`, `divideByTwo`, `isEven`, `isPositive`) | `node --import R/_harness/jest_register.mjs R/_harness/minijest.mjs R/trekhleb-multiply/.../multiplyUnsigned.test.js .../multiply.test.js` | **pass** 2/2 tests (21 expects) | Copy has `{"type":"module"}` added. Extensionless imports are resolved by the hook, as babel-jest would. |

The other first and second ranks in chapter 1 are written, MCQ or NC items with no code
to run: opendsa sets, jeffe, aspnes-202, brisk, wikibooks and mcs2018 problems.

## Chapter 2

| concept | rank | exercise | reference used | command | result | notes |
|---|---|---|---|---|---|---|
| array | 1 | TheAlgorithms `data_structures/arrays/index_2d_array_in_1d.py` | the file itself | `run_ta.sh ta-index_2d_array_in_1d …` | **pass** 17/17 doctests | |
| array | 2 | ODS Exercise 2.5 rotate. Cross-checks: keon TestRotateArray and TheAlgorithms `rotate_array.py` | keon `algorithms/array/rotate.py`; TA file | `run_keon.sh keon-rotate test_array.py tests.test_array.TestRotateArray`; `run_ta.sh ta-rotate_array …` | **pass**: keon 3/3 tests (12 asserts); TA 4/4 doctests | The ODS statement has no tests of its own (AI tests planned). |
| list-interface | 1 | ODS Exercise 1.6 + `tests/listtest.py` | ODS ArrayStack, FastArrayStack, SLList, DLList, ArrayDeque, DualArrayDeque, ArrayQueue | `python3 -I R/_harness/ods_run.py R/ods-python <classes> -- test_arraystack …` | **pass**: every list structure that imports passes `exercise_list` | See ODS notes. |
| list-interface | 2 | `exercism:list-ops` | Exercism Python `example.py` (fetched) | `run_exer.sh list-ops` | **pass** 23/23 canonical (6 superseded dropped); track 25/25 | The judge had not run this. |
| dynamic-array | 2 | TheAlgorithms `data_structures/arrays/dynamic_array.py` | the file | `run_ta.sh ta-dynamic_array …` | **pass** 36/36 doctests | Rank 1 is the CIU checklist, which has no tests. |
| block-copy | 1 | ODS `test_fastarraystack.py` | ODS FastArrayStack | `ods_run.py` as above | **pass** | |
| two-pointers | 1 | TheAlgorithms `maths/two_pointer.py` | the file | `run_ta.sh ta-two_pointer …` | **pass** 8/8 | |
| two-pointers | 2 | keon `searching/two_sum.py` | keon | `run_keon.sh keon-two_sum test_searching.py tests.test_searching.TestSuite.test_two_sum` | **pass** 1/1 (6 asserts) | |
| three-sum | 1 | keon `three_sum.py` | keon | `run_keon.sh keon-three_sum test_array.py tests.test_array.TestThreeSum` | **pass** 1/1 (2 asserts) | Thin. |
| three-sum | 2 | TheAlgorithms `find_triplets_with_0_sum.py` | the file | `run_ta.sh ta-find_triplets_with_0_sum …` | **pass** 11/11 | |
| merge-sorted-sequences | 1 | TheAlgorithms `data_structures/arrays/merge_sorted.py` | the file | `run_ta.sh ta-merge_sorted …` | **pass** 9/9 | |
| merge-sorted-sequences | 2 | tryalgo `merge_ordered_lists` | tryalgo package copy | `python3 -I unit_names.py R/tryalgo-merge_ordered_lists tests.test_tryalgo.TestBellmanFordNegCycles.test_merge_ordered_lists` | **pass** 1/1 (1 assert) | Most of tryalgo's tests are defined under the class `TestBellmanFordNegCycles`, not `TestTryalgo`. |
| sliding-window-fixed | 1 | TheAlgorithms `maths/max_sum_sliding_window.py` | the file | `run_ta.sh ta-max_sum_sliding_window …` | **pass** 8/8 | |
| sliding-window-fixed | 2 | `exercism:series` | Exercism Python `example.py` (fetched); the judge had used an AI reference | `run_exer.sh series` | **pass** 11/11 canonical (wording identical); track 11/11 | |
| sliding-window-variable | 1 | TheAlgorithms `greedy_methods/sliding_window.py` | the file | `run_ta.sh ta-sliding_window …` | **pass** 7/7 | |
| sliding-window-variable | 2 | keon `longest_non_repeat.py` | keon | `run_keon.sh keon-longest_non_repeat test_array.py tests.test_array.TestLongestNonRepeat` | **pass** 4/4 (20 asserts) | |
| prefix-sums | 1 | TheAlgorithms `data_structures/arrays/prefix_sum.py` | the file | `run_ta.sh ta-prefix_sum …` | **pass** 13/13 | |
| prefix-sums | 2 | TheAlgorithms `equilibrium_index_in_array.py` | the file | `run_ta.sh ta-equilibrium_index …` | **pass** 9/9 | |
| prefix-sums-2d | 1 | keon `matrix/sum_sub_squares.py` | keon | `run_keon.sh keon-sum_sub_squares test_matrix.py tests.test_matrix.TestSumSubSquares`; `doctest_mod.py … algorithms.matrix.sum_sub_squares` | **pass** 1/1 (1 assert) + 1/1 doctest | Its O(n²k²) reference is not a prefix-sum solution (ch02.md). |
| difference-array | 1 | `kattis:freefood` | **no reference on file** | none | not run | 3 samples. |
| singly-linked-list, implement-linked-list | 1 | icc `linked_lists/linked_list` | icc solution notebook + `linked_list.py` | `run_icc.sh icc-linked_list linked_lists/linked_list -` | **pass** 5/5 tests (16 asserts) | |
| singly-linked-list, implement-linked-list | 2 | `exercism:simple-linked-list` | Exercism Python `example.py` (fetched) | `run_exer.sh simple-linked-list` | **pass** 24/24 canonical (2 superseded dropped; the 3 "toList FIFO" cases do not apply, since the track is LIFO); track 20/20 | The judge had not run this. Wording: "The list is empty." vs canonical "list is empty". The Python API differs (`head().value()`, `reversed()` returns a new list). |
| doubly-linked-list | 1 | `exercism:linked-list` | Exercism Python `example.py` (fetched); the judge had used an AI reference | `run_exer.sh linked-list` | **pass** 18/18 applicable; track 24/24 | 1 canonical case is excluded by the track: "delete does not modify the list if the element is not found". The example raises `ValueError` there, where canonical expects a silent no-op. A statement must pick one. |
| doubly-linked-list | 2 | ODS `test_dllist.py` | ODS DLList | `ods_run.py` | **pass** | |
| floyd-cycle-detection | 1 | keon `linked_list/is_cyclic.py` | keon | `run_keon.sh keon-is_cyclic test_linked_list.py tests.test_linked_list.TestSuite.test_is_cyclic`; doctests | **pass** 1/1 (2 asserts) + 4/4 doctests | |
| floyd-cycle-detection | 2 | TheAlgorithms `has_loop.py`, `floyds_cycle_detection.py` | the files | `run_ta.sh ta-has_loop …`; `run_ta.sh ta-floyds_cycle_detection …` | **pass** 7/7 and 18/18 | |
| cycle-start | 1 | icc `linked_lists/find_loop_start` | icc solution notebook (+ `../linked_list/linked_list.py`) | `run_icc.sh icc-find_loop_start linked_lists/find_loop_start linked_lists/linked_list` | **pass** 1/1 (5 asserts) | |
| cycle-start | 2 | keon `first_cyclic_node.py` | keon | `doctest_mod.py R/keon-is_cyclic algorithms.linked_list.first_cyclic_node` | **pass** 3/3 doctests | |

The other first and second ranks in chapter 2 have no runnable reference:
- CIU checklist (dynamic-array 1);
- ODS written exercises 2.1, 2.2, 2.7 and 3.1;
- OpenDSA (dynamic-array-cost 2, linked-list-vs-array 1).

## Chapter 3

| concept | rank | exercise | reference used | command | result | notes |
|---|---|---|---|---|---|---|
| stack | 1 | `exercism:simple-linked-list` | as in 2.5 | as in 2.5 | **pass** 24/24 applicable; track 20/20 | |
| balanced-brackets | 2 | `kattis:brackets` | **no reference on file** | none | not run | 3 samples. Rank 1 (ODS exc-2) is written. |
| bracket-validation | 1 | `exercism:matching-brackets` | Exercism Python `example.py` (fetched) | `run_exer.sh matching-brackets` | **pass** 20/20 canonical; track 20/20 | |
| bracket-validation | 2 | `kattis:bracketmatching` | **no reference on file** | none | not run | 3 samples. |
| circular-buffer | 1 | `exercism:circular-buffer` | Exercism Python `example.py` (fetched) | `run_exer.sh circular-buffer` | **pass** 14/14 canonical (items passed as strings, as the track does); track 14/14 | The example marks empty slots with byte 0, so it cannot store the value 0 or `"\x00"`, and `all(self.buffer)` is O(capacity) per write. It is not a model reference for the book. |
| circular-buffer | 2 | TheAlgorithms `data_structures/queues/circular_queue.py` | the file | copy at `R/ta-circular_queue/data_structures/queues/` (with the repo's empty `__init__.py` files); `doctest_mod.py R/ta-circular_queue data_structures.queues.circular_queue` | **pass** 25/25 | Imported as a top-level module, 4 doctests fail only because their expected reprs name `data_structures.queues.circular_queue`. With the repo's package path, all pass. |
| queue-linked-list | 1 | icc `stacks_queues/queue_list` | icc notebook + `queue_list.py` | `run_icc.sh icc-queue_list stacks_queues/queue_list -` | **pass** 1/1 (5 asserts) | Thin, as ch03.md says. |
| queue-linked-list | 2 | TheAlgorithms `linked_queue.py` | the file | `run_ta.sh ta-linked_queue …` | **pass** 43/43 | |
| array-queue | 1 | ODS `test_arrayqueue.py` | ODS ArrayQueue | `ods_run.py` | **pass** | It runs with the shims, so a port is not needed for this file (ch03.md expected one). |
| array-queue | 2 | keon `test_queue.py::TestQueue.test_array_queue` | keon | `run_keon.sh keon-array_queue test_queue.py tests.test_queue.TestQueue.test_array_queue` | **pass** 1/1 (11 asserts) | |
| queue (ADT) | 2 | `kattis:ferryloading4` | **no reference on file** | none | not run | 1 sample. Rank 1 is OpenDSA MCQ. |
| deque | 1 | `exercism:linked-list` | as in 2.6 | as in 2.6 | **pass** 18/18 applicable; track 24/24 | As in 2.6, the "delete not found" behaviour is a divergence. |
| deque | 2 | trekhleb `data-structures/deque/__test__/Deque.test.js` | trekhleb `Deque.js` + `DoublyLinkedList`, `Comparator` | `node --import R/_harness/jest_register.mjs R/_harness/minijest.mjs R/trekhleb-deque/src/data-structures/deque/__test__/Deque.test.js` | **pass** 14/14 tests (59 expects) | Uses the jest stand-in. |
| array-deque | 1 | ODS `test_arraydeque.py` | ODS ArrayDeque | `ods_run.py` | **pass** | |
| dual-array-deque | 1 | ODS `test_dualarraydeque.py` | ODS DualArrayDeque | `ods_run.py` | **pass** | The code (`front.size()-i`) passes. The prose erratum `front.size()-i-1` stands as a note. |
| min-stack | 1 | TheAlgorithms `stack_tracking_min_max.py` | the file | `run_ta.sh ta-stack_tracking_min_max …`; extra `R/_harness/extra_rank1_checks.py` | **pass** 37/37 doctests; extra duplicate check 500/500 random sequences agree with min/max of contents | The extra check is AI-written (values 0..4, so duplicates are frequent). |
| min-stack | 2 | icc `stacks_queues/stack_min` | icc notebook + `../stack/stack.py` | `run_icc.sh icc-stack_min stacks_queues/stack_min stacks_queues/stack R/_harness/extra_stack_min_dup.py` | own test **pass** 1/1 (17 asserts); AI duplicate tests **fail** 2/2 | **Rejection confirmed.** Push 5, 1, 1 then pop: `minimum()` returns 5 while a 1 is still on the stack. The cause is `push` recording a new minimum only on `data < minimum()`, while `pop` removes it on `==`. 172 of 200 random sequences diverge. |
| queue-from-two-stacks | 1 | TheAlgorithms `queues/queue_by_two_stacks.py` | the file | `run_ta.sh ta-queue_by_two_stacks …`; extra timing | **pass** 32/32 (Python 3.13 handles `class QueueByTwoStacks[T]`); alternating put/get flat at 0.11 µs/op for n = 2,000 to 32,000 | Amortised O(1), as expected. |
| queue-from-two-stacks | 2 | tryalgo `our_queue` | tryalgo copy | `unit_names.py R/tryalgo-our_queue …TestBellmanFordNegCycles.test_OurQueue …test_our_queue` | **pass** 2/2 (randomised against `deque`); alternating ops flat at 0.05 µs/op | |
| queue-from-two-stacks (rejected item) | 4 | icc `stacks_queues/queue_from_stacks` | icc notebook + `../stack/stack.py` | `run_icc.sh icc-queue_from_stacks stacks_queues/queue_from_stacks stacks_queues/stack R/_harness/extra_qfs_complexity.py` | own test **pass** 1/1 (5 asserts); complexity check **fail** | **Rejection confirmed.** With n items held, n alternating enqueue/dequeue pairs cost n pushes per op. Counts: 500,500 / 2,001,000 / 8,002,000 / 32,004,000 pushes for n = 500 / 1,000 / 2,000 / 4,000, and 0.13 s / 0.47 s / 1.78 s / 6.96 s. That is Θ(n) per op, Θ(n²) total. The cause is that `enqueue` shifts everything back to the left stack. |
| monotonic-queue-minimum | 2 | TheAlgorithms `queues/monotonic_queue.py` | the file | `run_ta.sh ta-monotonic_queue …` | **pass** 1/1 | Maximum variant, a single doctest. Rank 1 (ODS exc-15/16) is written. |
| sliding-window-minimum | 1 | keon `test_queue.py::TestSuite.test_max_sliding_window` + TheAlgorithms `other/sliding_window_maximum.py` | keon `queue/max_sliding_window.py`; TA file | `run_keon.sh keon-max_sliding_window test_queue.py tests.test_queue.TestSuite.test_max_sliding_window`; `run_ta.sh ta-sliding_window_maximum …` | **pass** keon 1/1 (6 asserts); TA 5/5 | Both are maximum variants. |
| sliding-window-minimum | 2 | keon `heap/sliding_window_max` | keon | `run_keon.sh keon-heap_sliding_window_max test_heap.py tests.test_heap.TestSuite.test_max_sliding_window` | **pass** 1/1 (1 assert) | Heap-based, so it is deferred to chapter 9. |
| nearest-smaller-element | 1 | TheAlgorithms `stacks/stock_span_problem.py` | the file | `run_ta.sh ta-stock_span_problem …` | **pass** 6/6 | The module prints at import (`1 1 2 4 5 1`). |
| nearest-smaller-element | 2 | TheAlgorithms `next_greater_element.py`, `kth_next_greater_element.py` | the files | `run_ta.sh ta-next_greater_element …`; `run_ta.sh ta-kth_next_greater_element …` | **pass** 3/3 and 5/5 | |
| largest-zero-submatrix | 1 | tryalgo `rectangles_from_grid` (+ `rectangles_from_histogram`) | tryalgo copy | `unit_names.py R/tryalgo-rectangles_from_grid …test_rectangles_from_grid …test_rectangles_from_histogram` | **pass** 2/2 (grid: 2 asserts; histogram: randomised against brute force) | |
| rpn-evaluation | 1 | `exercism:forth` | Exercism Python `example.py` (fetched) | `run_exer.sh forth` | **pass** 54/54 applicable; track 54/54 | Not applicable: 1 case excluded by the track ("only defines locally", `evaluateBoth`). Wording: 14 stack errors read "Insufficient number of items in stack" against canonical "empty stack" or "only one value on the stack". |
| rpn-evaluation | 2 | `kattis:circuitmath` | **no reference on file** | none | not run | 1 sample. |
| expression-parsing, unary-right-assoc | 1 | `kattis:calculator` | **no reference on file** | none | not run | 1 sample file (10 lines). |
| expression-parsing | 2 | TheAlgorithms `stacks/dijkstras_two_stack_algorithm.py` | the file + sibling `stack.py` | copied as package `R/ta-dijkstras_two_stack/pkg/` (an empty `__init__.py` is mine), for the relative import; `doctest_mod.py … pkg.dijkstras_two_stack_algorithm` | **pass** 3/3 | |
| unary-right-assoc | 2 | TheAlgorithms `stacks/infix_to_postfix_conversion.py` | the file + `stack.py`, `balanced_parentheses.py` | package copy `R/ta-infix_to_postfix/pkg/` | **pass** 8/8 | |
| rpn-evaluation | 3 (cpa's runnable companion in the ch03 builder notes) | TheAlgorithms `stacks/postfix_evaluation.py` | the file | `run_ta.sh ta-postfix_evaluation …` | **pass** 13/13 | Out of rank, but run because the builder notes name it. Its quirk doctests (unary minus, `[]` → 0) pass as written. |
| rootish-array-stack | 1 | ODS `test_rootisharraystack.py` | ODS RootishArrayStack | `ods_run.py` | **fail as cached**: `IndexError` (float index, `rootisharraystack.py:52`, `j = i - b*(b+1)/2`) | A mechanical port in a scratch copy (`R/ods-python-port/`) changes `/` to `//` on lines 38, 45, 51, 59 and 72, and with it the test **passes**. The port is AI-made and is not in the cache. |
| space-efficient-list | 1 | ODS `test_selist.py` | ODS SEList | `ods_run.py` | **fail as cached**: `selist.py` does not parse (`print ell`, line 149) | The same scratch port changes only the two `print ell` lines in `__main__` to `print(ell)`. With it, `exercise_list` **passes** for block sizes 5, 10 and 42. |

The other first and second ranks in chapter 3 are written, MC, wikibooks or OpenDSA
items with no code to run. These are stack 2, balanced-brackets 1, queue 1, array-deque
2, dual-array-deque 2, monotonic-queue-minimum 1 and the rootish/selist exercises.

**ODS notes.**
- ODS has no FETCHED commit on file.
- `ods_run.py` uses runtime shims only. The copied files are not edited.
  - `numpy.object = object` (removed in NumPy 1.24; this is numpy 2.5.3).
  - `BaseList.__eq__` is replaced by the same loop with `next(it)` for Python 2's
    `it.next()`.
  - A two-function `nose.tools` stand-in, because nose is not installed.
  - A fake `ods` module holding only the named classes. `ods/__init__.py` imports
    every structure, `selist.py` included, so the real one cannot load.
- The ODS harness is randomised (`random.seed(5)`, 5 rounds of 100 adds and 500 mixed
  operations, each checked against `ControlList`).

## Summary

**Rejections.**
- **icc `stack_min`: confirmed.** Its own 17 asserts pass, because they never push a
  repeated minimum. On 5, 1, 1 then pop, `minimum()` returns 5. 172 of 200 random
  sequences with repeated values diverge.
- **icc `queue_from_stacks`: confirmed.** Its own 5 asserts pass. Alternating
  operations cost n pushes each, Θ(n²) in total: 32,004,000 pushes and 6.96 s for
  n = 4,000. The rank 1 and rank 2 replacements (TheAlgorithms `QueueByTwoStacks`,
  tryalgo `OurQueue`) stay flat per operation from n = 2,000 to 32,000.
- **No other reference failed its own tests.** The only exceptions are the two ODS
  files that do not run as cached.

**Fails as cached, port needed.**
- ODS `rootisharraystack.py` (float index) and `selist.py` (Python 2 `print`).
- Both pass the ODS harness after a mechanical port: `//` on 5 lines, and `print(…)`
  on 2.
- The other ODS list structures pass with runtime shims alone, ArrayQueue included.
  So the "port needed" note in ch03.md covers only these two files and the
  `numpy.object` / `it.next()` / `__init__` shims.

**Missing references.**
- Kattis has no accepted solutions on file for any of the ranked problems, and the
  ICPC caches hold none of them. Each has samples only (1 to 3 files):
  - howmanydigits, stirlingsapproximation (ch. 1 factorials, ranks 1 and 2);
  - anagramcounting, dicecup, expectedearnings, fruitbaskets (ch. 1, rank 2);
  - freefood (2.4, rank 1);
  - brackets, bracketmatching, ferryloading4, circuitmath (ch. 3, rank 2);
  - calculator (3.5, rank 1 for two concepts).
- Exercism ships no reference in the cache. All nine ranked slugs were covered with the
  MIT Python-track `example.py`, and all pass canonical data on the applicable cases
  and their own track tests: difference-of-squares, grains, list-ops, series,
  simple-linked-list, linked-list, matching-brackets, circular-buffer and forth.
  Three track divergences matter for statements:
  - linked-list `delete` raises on "not found";
  - simple-linked-list uses LIFO `toList`;
  - error wording in forth and simple-linked-list.

  The circular-buffer example cannot store 0 and is not a model reference.
- Not runnable here: none. jest is absent, so the two trekhleb suites ran under a
  minimal stand-in, and both passed.
