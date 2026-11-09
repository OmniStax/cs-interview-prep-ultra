#!/usr/bin/env python3
"""Write ODS's listings for the two debugger panels into figures.js between its generated markers, so the panels
show ODS's own code and no line of it is typed by hand: ArrayDeque's add(i,x), remove(i) and resize() for
sim-arraydeque, DualArrayDeque's add(i,x), remove(i) and balance() for sim-dualarraydeque. Python, Java and C++ are
read by tools/ods_listing.py as ODS's editions print them (printed=True, as ch02/2.2); the JavaScript in figures.js
is the AI's and is not touched.

    python3 -I ch03/3.3/inline_code.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
import ods_listing  # noqa: E402

PANELS = {
    'ARRAYDEQUE': ('ArrayDeque', ['add(i,x)', 'remove(i)', 'resize()']),
    'DUAL': ('DualArrayDeque', ['add(i,x)', 'remove(i)', 'balance()']),
}


def listing(cls, members, lang):
    f = getattr(ods_listing, lang)
    return '\n\n'.join(f(cls, m, printed=True) for m in members)


def main():
    path = os.path.join(HERE, 'figures.js')
    js = open(path, encoding='utf-8').read()
    for key, (cls, members) in PANELS.items():
        begin, end = f'/* BEGIN ODS LISTINGS {key} (ch03/3.3/inline_code.py) */', f'/* END ODS LISTINGS {key} */'
        a, b = js.index(begin), js.index(end)
        body = ''.join(f'  const {name} = {json.dumps(listing(cls, members, lang))};\n'
                       for name, lang in (('PY', 'python'), ('JAVA', 'java'), ('CPP', 'cpp')))
        js = js[:a + len(begin)] + '\n' + body + '  ' + js[b:]
    open(path, 'w', encoding='utf-8').write(js)
    print(f'{path}: {len(PANELS)} panels in three languages', file=sys.stderr)


if __name__ == '__main__':
    main()
