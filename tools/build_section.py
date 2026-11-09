#!/usr/bin/env python3
"""Write a section's section.json once, from its build_spec.py and what tools/build_text.py extracted.

The record's scalars, figure rows, referents and coverage are the spec's SECTION; the book footnotes come
from footnotes.json (each in the source's words, as the converter read them) and the corrections from
SECTION['footnotes_extra']; a figure's original caption is the book's own, read from captions.json; the
exercises are built by the section's EXERCISES function where it has one, from files in the source cache.

ROOT RULES item 19: a section.json is written whole once and corrected row by row with `ost set` after,
so this refuses to overwrite one unless given --force (for a section that is being rebuilt from nothing).

    python3 -I tools/build_section.py ch01/1.1 [--force]
"""
import html
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(HERE)


def load_spec(sec_dir):
    sp = importlib.util.spec_from_file_location('build_spec', os.path.join(sec_dir, 'build_spec.py'))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def exercism_code(path, entry_py, entry_js, prop, ref_py, ref_js, ex):
    """An Exercism exercise as a code card: the statement is the exercise's description.md, the tests its
    canonical data for one property (the source's), the references the AI's."""
    desc = open(os.path.join(path, 'description.md'), encoding='utf-8').read()
    desc = re.sub(r'^# Instructions\s*', '', desc).strip()
    paras = [' '.join(p.split()) for p in re.split(r'\n\s*\n', desc)]
    prompt = '\n\n'.join(html.escape(p, quote=False).replace('$', '＄') for p in paras)
    data = json.load(open(os.path.join(path, 'canonical-data.json'), encoding='utf-8'))
    cases = []

    def walk(c):
        for x in c.get('cases', []):
            if 'cases' in x:
                walk(x)
            elif x['property'] == prop:
                cases.append(x)
    walk(data)
    tests = [{'args': list(c['input'].values()), 'expect': c['expected'], 'visible': i == 0, 'generated_by': 'source'}
             for i, c in enumerate(cases)]
    return dict(ex, prompt=prompt, answer={
        'type': 'code',
        'python': {'entry': entry_py, 'starter': f'def {entry_py}(number):\n    pass\n', 'reference': ref_py, 'generated_by': 'ai'},
        'javascript': {'entry': entry_js, 'starter': f'function {entry_js}(number) {{\n}}\n', 'reference': ref_js, 'generated_by': 'ai'},
        'tests': tests, 'generated_by': 'source'})


def build(sec_dir, force=False):
    out = os.path.join(sec_dir, 'section.json')
    if os.path.exists(out) and not force:
        raise SystemExit(f'{out} exists: correct it row by row with ost set (or pass --force to rebuild it whole)')
    spec = load_spec(sec_dir)
    S = dict(spec.SECTION)
    captions = json.load(open(os.path.join(sec_dir, 'captions.json'), encoding='utf-8'))
    notes = json.load(open(os.path.join(sec_dir, 'footnotes.json'), encoding='utf-8'))

    def fill(v):
        if isinstance(v, str):
            return re.sub(r'\{\{caption-text ([\d.]+)\}\}', lambda m: captions[m.group(1)]['text'], v)
        if isinstance(v, list):
            return [fill(x) for x in v]
        if isinstance(v, dict):
            return {k: fill(x) for k, x in v.items()}
        return v
    S = fill(S)
    extra = S.pop('footnotes_extra', [])
    S['footnotes'] = [{k: v for k, v in n.items() if k != 'source'} for n in notes] + extra
    exercises, concepts = [], []
    if hasattr(spec, 'EXERCISES'):
        exercises, concepts = spec.EXERCISES(lambda *a: exercism_code(*a), BOOK)
    S['exercises'] = exercises
    S['exercise_concepts'] = concepts
    S.setdefault('derivations', [])
    order = ['id', 'chapter', 'title', 'short', 'lead', 'objectives', 'summary_html', 'notes', 'ai', 'built', 'exercise_notes',
             'figures', 'coverage', 'exercises', 'exercise_concepts', 'referents', 'footnotes', 'derivations']
    rec = {k: S[k] for k in order if k in S}
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print(f'{out}: {len(rec["figures"])} figures, {len(rec["footnotes"])} notes, {len(rec["exercises"])} exercises', file=sys.stderr)


if __name__ == '__main__':
    build(os.path.abspath(sys.argv[1]), '--force' in sys.argv)
