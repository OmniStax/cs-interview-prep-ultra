#!/usr/bin/env python3
"""Write ODS’s ArrayQueue listings (add, remove, resize) into figures.js between its generated markers, so
the code panel of sim-arrayqueue shows ODS's own code and no line of it is typed by hand. Python, Java and C++
are read by tools/ods_listing.py as ODS's editions print them (printed=True); the JavaScript in figures.js is
the AI's and is not touched.

    python3 -I ch03/3.2/inline_code.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
import ods_listing  # noqa: E402

MEMBERS = ["add(x)", "remove()", "resize()"]
BEGIN, END = '/* BEGIN ODS LISTINGS (ch03/3.2/inline_code.py) */', '/* END ODS LISTINGS */'


def listing(lang):
    f = getattr(ods_listing, lang)
    return '\n\n'.join(f("ArrayQueue", m, printed=True) for m in MEMBERS)


def main():
    path = os.path.join(HERE, 'figures.js')
    js = open(path, encoding='utf-8').read()
    a, b = js.index(BEGIN), js.index(END)
    body = ''.join(f'  const {name} = {json.dumps(listing(lang))};\n'
                   for name, lang in (('PY', 'python'), ('JAVA', 'java'), ('CPP', 'cpp')))
    js = js[:a + len(BEGIN)] + '\n' + body + '  ' + js[b:]
    open(path, 'w', encoding='utf-8').write(js)
    print(f'{path}: {len(MEMBERS)} members in three languages', file=sys.stderr)


if __name__ == '__main__':
    main()
