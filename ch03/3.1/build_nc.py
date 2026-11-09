#!/usr/bin/env python3
"""Write 3.1's exercises-nc.json: the pythonds self-checks of its stack pages (CC BY-NC-SA 4.0, NC cards only;
RULES.md, Licence and attribution), read by script from the cached reStructuredText, nothing typed.

- `stack_1`, `stack_2`: `.. mchoice::` items, their options and `:correct:` key as pythonds prints them, the code block of
  the question as a <pre>.
- `stack_stringrev`: the `.. actex::` item after them, its statement the paragraph before it, its tests its three
  `testEqual` lines (the source's); the references are the AI's (pythonds prints none), marked.

    python3 -I ch03/3.1/build_nc.py
"""
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
RST = os.path.join(BOOK, 'sources/_cache/pythonds/_sources/BasicDS/ImplementingaStackinPython.rst')
LICENSE = 'CC BY-NC-SA 4.0'
LICENSE_URL = 'https://creativecommons.org/licenses/by-nc-sa/4.0/'

REV_PY = '''def rev_string(my_str):
    stack = []
    for ch in my_str:
        stack.append(ch)
    out = []
    while stack:
        out.append(stack.pop())
    return ''.join(out)
'''
REV_JS = '''function revString(myStr) {
    const stack = [];
    for (const ch of myStr) stack.push(ch);
    let out = '';
    while (stack.length > 0) out += stack.pop();
    return out;
}
'''


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'``([^`]+)``', r'<code>\1</code>', s)
    return re.sub(r'`([^`]+)`', r'<code>\1</code>', s)


def directive(lines, start):
    """The indented body of the directive at `start`: (options, body lines without the common indent)."""
    ind = len(lines[start]) - len(lines[start].lstrip())
    body, i = [], start + 1
    while i < len(lines) and (not lines[i].strip() or len(lines[i]) - len(lines[i].lstrip()) > ind):
        body.append(lines[i])
        i += 1
    while body and not body[-1].strip():
        body.pop()
    opts, rest = {}, []
    for l in body:
        m = re.match(r'^\s*:(\w+):\s*(.*)$', l)
        if m and not rest:
            opts[m.group(1)] = m.group(2).strip()
        else:
            rest.append(l)
    cut = min((len(l) - len(l.lstrip()) for l in rest if l.strip()), default=0)
    return opts, [l[cut:] for l in rest], i


def text_of(body):
    """Paragraphs and `.. code-block::` blocks as the prompt's HTML."""
    out, i = [], 0
    while i < len(body):
        l = body[i]
        if not l.strip():
            i += 1
            continue
        if l.startswith('.. code-block::'):
            j, code = i + 1, []
            while j < len(body) and (not body[j].strip() or body[j].startswith(' ')):
                code.append(body[j])
                j += 1
            while code and not code[-1].strip():
                code.pop()
            while code and not code[0].strip():
                code.pop(0)
            cut = min(len(c) - len(c.lstrip()) for c in code if c.strip())
            out.append('<pre>' + html.escape('\n'.join(c[cut:] for c in code), quote=False) + '</pre>')
            i = j
            continue
        acc = []
        while i < len(body) and body[i].strip() and not body[i].startswith('.. '):
            acc.append(body[i].strip())
            i += 1
        out.append(inline(' '.join(acc)))
    return '\n\n'.join(out)


def main():
    lines = open(RST, encoding='utf-8').read().split('\n')
    cards, concepts = [], []
    for i, l in enumerate(lines):
        m = re.match(r'^\s*\.\. mchoice:: (\w+)', l)
        if not m:
            continue
        opts, body, _ = directive(lines, i)
        keys = sorted(k for k in opts if k.startswith('answer_'))
        # an option pythonds prints in quotes is a string value: kept with its quotes
        options = [inline(opts[k]) for k in keys]
        correct = keys.index('answer_' + opts['correct'])
        cid = 'nc-' + m.group(1).replace('_', '-')
        cards.append({
            'id': cid, 'source_id': f'pythonds:BasicDS/ImplementingaStackinPython#{m.group(1)}', 'source_number': f'Self Check {m.group(1)}',
            'origin': 'pythonds', 'kind': 'check', 'bloom': 'Apply', 'place': {'at': 'end'}, 'cite': 'stack',
            'prompt': text_of(body),
            'answer': {'type': 'choice', 'options': options, 'correct': correct, 'generated_by': 'source'},
        })
        concepts.append({'exercise': cid, 'concept': 'stack'})
    # the actex: its statement is the paragraph before it, its tests the testEqual lines
    a = next(i for i, l in enumerate(lines) if re.match(r'^\s*\.\. actex:: stack_stringrev', l))
    j = a - 1
    while not lines[j].strip():
        j -= 1
    para = []
    while lines[j].strip():
        para.insert(0, lines[j].strip())
        j -= 1
    _, body, _ = directive(lines, a)
    tests = []
    for t in body:
        m = re.match(r'\s*testEqual\(rev_string\((".*?")\), (".*?")\)', t)
        if m:
            tests.append({'args': [json.loads(m.group(1))], 'expect': json.loads(m.group(2)), 'generated_by': 'source'})
    assert len(tests) == 3, tests
    for k, t in enumerate(tests):
        t['visible'] = k == 0
    cards.append({
        'id': 'nc-stack-stringrev', 'source_id': 'pythonds:BasicDS/ImplementingaStackinPython#stack_stringrev',
        'source_number': 'Self Check stack_stringrev', 'origin': 'pythonds', 'kind': 'code', 'bloom': 'Apply',
        'place': {'at': 'end'}, 'cite': 'stack',
        'changes': ('pythonds imports its own Stack class (pythonds3.basic), which the runner does not have; a list used '
                    'only through append and pop is a stack. The tests are pythonds’ three; the references are the AI’s.'),
        'prompt': inline(' '.join(para)),
        'answer': {'type': 'code',
                   'python': {'entry': 'rev_string', 'starter': 'def rev_string(my_str):\n    # your code here\n    pass\n',
                              'reference': REV_PY, 'generated_by': 'ai'},
                   'javascript': {'entry': 'revString', 'starter': 'function revString(myStr) {\n    // your code here\n}\n',
                                  'reference': REV_JS, 'generated_by': 'ai'},
                   'tests': tests, 'generated_by': 'source'},
    })
    concepts.append({'exercise': 'nc-stack-stringrev', 'concept': 'stack'})
    out = {'section': '3.1', 'license': LICENSE, 'license_url': LICENSE_URL, 'exercises': cards, 'exercise_concepts': concepts}
    path = os.path.join(HERE, 'exercises-nc.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print(f'{path}: {len(cards)} cards')


if __name__ == '__main__':
    main()
