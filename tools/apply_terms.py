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
import subprocess
import sys
import tempfile
from collections import defaultdict

TERMS_PASS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'OmniStax', 'omnistax-content', 'tools', 'terms_pass.py')


def _tool():
    return os.environ.get('OMNISTAX_TERMS_PASS', os.path.normpath(TERMS_PASS))


def _import_terms_pass(tool):
    sys.path.insert(0, os.path.dirname(tool))
    import importlib
    return importlib.import_module('terms_pass')


def renumber(sec_dir, rows, tool):
    """The rows with `idx` and `hash` of the mention they name in the page as it is now; and the rows not found."""
    tp = _import_terms_pass(tool)
    book = tp.ost.book_of(rows[0]['book'])
    g = tp.glossary_of(book)
    text = tp.ost.read_text(os.path.join(sec_dir, 'text.html'))
    ts, h = tp.tokens(text), tp.digest(text)
    now = defaultdict(list)
    for idx, m in enumerate(tp.mentions(ts, g.pattern)):
        now[(' '.join(m.text.split()).lower(), tp.sentence(ts, m))].append(idx)
    out, lost = [], []
    for r in rows:
        if r.get('concept') is None:
            continue
        found = now.get((r['term'].lower(), r['context']), [])
        if r['nth'] < len(found):
            out.append({**r, 'idx': found[r['nth']], 'hash': h})
        else:
            lost.append(r)
    return out, lost


def apply(sec_dir):
    path = os.path.join(sec_dir, 'terms.jsonl')
    if not os.path.exists(path):
        return
    tool = _tool()
    if not os.path.exists(tool):
        print(f'{sec_dir}: terms.jsonl not applied: no terms_pass.py at {tool} (set OMNISTAX_TERMS_PASS)', file=sys.stderr)
        return
    with open(path, encoding='utf-8') as f:
        rows = [json.loads(line) for line in f if line.strip()]
    if not any(r.get('concept') for r in rows):
        return
    rows, lost = renumber(sec_dir, rows, tool)
    for r in lost:
        print(f'{sec_dir}: terms row #{r["idx"]} ({r["term"]!r} → {r["concept"]}) is no mention now; left out', file=sys.stderr)
    with tempfile.NamedTemporaryFile('w', suffix='.jsonl', delete=False, encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
        tmp = f.name
    try:
        r = subprocess.run([sys.executable, tool, 'apply', tmp], capture_output=True, text=True)
    finally:
        os.unlink(tmp)
    if r.returncode != 0:
        print(f'{sec_dir}: terms.jsonl not applied: {r.stderr.strip()}', file=sys.stderr)
    else:
        print(f'{sec_dir}: {r.stdout.strip()}')
