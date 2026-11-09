"""Apply a section's judged concept mentions (`<section>/terms.jsonl`) to the text.html the build just wrote.

The terms pass (root RULES item 7; omnistax-content/tools/terms_pass.py) lists every mention of a concept's
glossary words that no span marks, a person or agent decides for each whether it names its concept, and the
decisions are kept beside the section as `terms.jsonl` (one candidates row per mention, `concept` set or null).
The build writes the page without them, so this runs after it: the rows carry the hash of the page as listed,
which a rebuild from an unchanged spec reproduces. Where the spec changed the page, the rows no longer fit and
the build says so: list the candidates again (`terms_pass.py candidates <book> --chapter N`) and re-judge.
"""
import os
import subprocess
import sys

TERMS_PASS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'OmniStax', 'omnistax-content', 'tools', 'terms_pass.py')


def apply(sec_dir):
    rows = os.path.join(sec_dir, 'terms.jsonl')
    if not os.path.exists(rows):
        return
    tool = os.environ.get('OMNISTAX_TERMS_PASS', os.path.normpath(TERMS_PASS))
    if not os.path.exists(tool):
        print(f'{sec_dir}: terms.jsonl not applied: no terms_pass.py at {tool} (set OMNISTAX_TERMS_PASS)', file=sys.stderr)
        return
    r = subprocess.run([sys.executable, tool, 'apply', rows], capture_output=True, text=True)
    if r.returncode != 0:
        print(f'{sec_dir}: terms.jsonl not applied: {r.stderr.strip()}', file=sys.stderr)
    else:
        print(f'{sec_dir}: {r.stdout.strip()}')
