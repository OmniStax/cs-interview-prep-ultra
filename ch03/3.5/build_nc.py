"""Write 3.5's exercises-nc.json: pythonds' keyed Self Check items on postfix expressions (CC BY-NC-SA 4.0), read
from the cached RST by script, in the shape of ch01/1.6/exercises-nc.json. Each statement is the fill-in's question
as printed; each key is the answer the fill-in accepts as correct.

    python3 -I ch03/3.5/build_nc.py
"""
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
RST = os.path.join(BOOK, 'sources/_cache/pythonds/_sources/BasicDS/InfixPrefixandPostfixExpressions.rst')


def fill_ins():
    """Each fillintheblank: its id, its question (``code`` as <code>) and the pattern it marks Correct."""
    src = open(RST, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'\.\. fillintheblank:: (\w+)\n\n(.*?)\n\n\s*\|blank\|\n\n\s*-\s+:(.*?): Correct\.', src, re.S):
        q = ' '.join(m.group(2).split())
        q = re.sub(r'``(.*?)``', lambda k: '<code>' + html.escape(k.group(1), quote=False) + '</code>', q)
        out[m.group(1)] = {'prompt': q, 'key': m.group(3)}
    return out


def main():
    f = fill_ins()
    # the patterns as the answers they accept: \s+ / \s* a space, \* a star
    key1 = re.sub(r'\\(.)', r'\1', re.sub(r'\\s[+*]', ' ', f['postfix1']['key']))
    key1 = ' '.join(key1.split())
    assert key1 == '10 3 5 * 16 4 - / +', key1
    assert f['postfix2']['key'] == '9'
    loc = 'pythonds:BasicDS/InfixPrefixandPostfixExpressions'
    card = lambda i, n, bloom, prompt, answer: {  # noqa: E731
        'id': i, 'source_id': f'{loc}#{n}', 'source_number': f'Self Check, {n}', 'origin': 'pythonds', 'kind': 'check',
        'bloom': bloom, 'place': {'at': 'end'}, 'cite': 'rpn', 'prompt': prompt, 'answer': answer}
    exercises = [
        card('nc-postfix1', 'postfix1', 'Apply', f['postfix1']['prompt'],
             {'type': 'open', 'generated_by': 'source', 'solution': f'<code>{key1}</code>'}),
        card('nc-postfix2', 'postfix2', 'Apply', f['postfix2']['prompt'],
             {'type': 'number', 'value': 9, 'generated_by': 'source'}),
    ]
    concepts = [{'exercise': 'nc-postfix1', 'concept': 'expression-parsing'}, {'exercise': 'nc-postfix1', 'concept': 'rpn-evaluation'},
                {'exercise': 'nc-postfix2', 'concept': 'rpn-evaluation'}]
    out = {'section': '3.5', 'license': 'CC BY-NC-SA 4.0', 'license_url': 'https://creativecommons.org/licenses/by-nc-sa/4.0/',
           'exercises': exercises, 'exercise_concepts': concepts}
    path = os.path.join(HERE, 'exercises-nc.json')
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    print(f'{path}: {len(exercises)} cards')


if __name__ == '__main__':
    main()
