"""Apply a section's judged concept mentions (`<section>/terms.jsonl`) to the text.html the build just wrote.

The terms pass (root RULES item 7; omnistax-content/tools/terms_pass.py) lists every mention of a concept's
glossary words that no span marks, a person or agent decides for each whether it names its concept, and the
decisions are kept beside the section as `terms.jsonl` (one candidates row per mention, `concept` set or null).
The build writes the page without them, so this runs after it: the rows carry the hash of the page as listed,
which a rebuild from an unchanged spec reproduces. Where the spec changed the page, the rows no longer fit and
the build says so: list the candidates again (`terms_pass.py candidates <book> --chapter N`) and re-judge.

A row's `idx` numbers its mention among the mentions of every built concept's terms, so a concept added to the
book later (chapter 3's `stack` in chapter 2's prose) shifts the numbers of an earlier section's rows. Before
applying, each row is found again in the page as it is now by its term, its sentence and its place among the
mentions with that term and sentence (`term`, `context`, `nth`), and given that mention's number (chapter 2–3
pass). Rows left in ink (`concept` null) are kept as the record of the judgement and not passed on. A row that is no
longer a mention (a longer term of a later concept now holds it) is named and left out; the mentions the later
concepts' terms add are left in ink until the section's candidates are listed and judged again.
"""
import json
import os
import sys
import types
from collections import defaultdict

TERMS_PASS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'OmniStax', 'omnistax-content', 'tools', 'terms_pass.py')


def _tool():
    return os.environ.get('OMNISTAX_TERMS_PASS', os.path.normpath(TERMS_PASS))


def _import_terms_pass(tool):
    sys.path.insert(0, os.path.dirname(tool))
    import importlib
    return importlib.import_module('terms_pass')


def apply(sec_dir):
    """Wrap each chosen mention of the page the build just wrote in its concept span, in place (in this folder, so a
    scratch copy of the book builds without touching the book: the glossary is this copy's book.json)."""
    path = os.path.join(sec_dir, 'terms.jsonl')
    if not os.path.exists(path):
        return
    tool = _tool()
    if not os.path.exists(tool):
        print(f'{sec_dir}: terms.jsonl not applied: no terms_pass.py at {tool} (set OMNISTAX_TERMS_PASS)', file=sys.stderr)
        return
    with open(path, encoding='utf-8') as f:
        rows = [json.loads(line) for line in f if line.strip()]
    rows = [r for r in rows if r.get('concept') is not None]
    if not rows:
        return
    tp = _import_terms_pass(tool)
    g = tp.glossary_of(types.SimpleNamespace(book_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(sec_dir))), 'book.json')))
    page = os.path.join(sec_dir, 'text.html')
    text = open(page, encoding='utf-8').read()
    ts = tp.tokens(text)
    now = defaultdict(list)
    for m in tp.mentions(ts, g.pattern):
        now[(' '.join(m.text.split()).lower(), tp.sentence(ts, m))].append(m)
    chosen, lost, taken = {}, [], []
    for r in rows:
        if r['concept'] not in g.ids:
            raise SystemExit(f'{sec_dir}: terms row {r["term"]!r}: {r["concept"]!r} is no concept of the book')
        found = now.get((r['term'].lower(), r['context']), [])
        if r['nth'] >= len(found):
            lost.append(r)
        elif found[r['nth']].inside:
            taken.append(r)
        else:
            chosen[found[r['nth']]] = r['concept']
    for r in lost:
        print(f'{sec_dir}: terms row {r["term"]!r} → {r["concept"]} is no mention now; left out ({r["context"][:80]})', file=sys.stderr)
    for r in taken:
        print(f'{sec_dir}: terms row {r["term"]!r} → {r["concept"]} already sits in a span the spec marks; left as it is', file=sys.stderr)
    with open(page, 'w', encoding='utf-8') as f:
        f.write(tp.wrapped(ts, chosen))
    print(f'{sec_dir}: {len(chosen)} mentions marked')
