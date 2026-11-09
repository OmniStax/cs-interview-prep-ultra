"""Write a section's exercises-nc.json from cards whose statements were set from the handout's page render and
whose keys are MIT's worked solutions, linked (the shape of ch01/1.6/exercises-nc.json; docs/content-format.md,
"exercises-nc.json"). Used by ch01/1.2 and ch01/1.3's build_nc.py."""
import json
import os

BOOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LICENSE = 'CC BY-NC-SA 4.0'
LICENSE_URL = 'https://creativecommons.org/licenses/by-nc-sa/4.0/'


def url_of(origin, name):
    for line in open(os.path.join(BOOK, 'sources/_cache', origin, 'index.tsv'), encoding='utf-8'):
        f, nm, url = line.rstrip('\n').split('\t')[:3]
        if nm == name or f.endswith(name):
            return url
    raise SystemExit(f'{origin}: no handout {name!r} in index.tsv')


def write(section, cards):
    exercises, concepts = [], []
    for c in cards:
        sol = url_of(c['origin'], c['handout'])
        exercises.append({
            'id': c['id'], 'source_id': c['source_id'], 'source_number': f"{c['set_']}, Problem {c['n']}",
            'origin': c['origin'], 'kind': 'exercise', 'bloom': c['bloom'], 'place': {'at': 'end'}, 'cite': c['cite'],
            'changes': 'The worked solution is MIT’s, linked rather than copied.',
            'prompt': c['prompt'],
            'answer': {'type': 'open', 'generated_by': 'source',
                       'solution': f'MIT’s worked solution: <a href="{sol}">Solutions to {c["set_"]}</a>, Problem {c["n"]}.'},
        })
        concepts += [{'exercise': c['id'], 'concept': k} for k in c['concepts']]
    out = {'section': section, 'license': LICENSE, 'license_url': LICENSE_URL, 'exercises': exercises, 'exercise_concepts': concepts}
    path = os.path.join(BOOK, 'ch' + section.split('.')[0].zfill(2), section, 'exercises-nc.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print(f'{path}: {len(exercises)} cards')
