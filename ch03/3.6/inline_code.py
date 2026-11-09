#!/usr/bin/env python3
"""Write ODS's listings into figures.js between its generated markers, so that each code panel shows ODS's own code
and no line of it is typed by hand: RootishArrayStack's i2b, get, set, add, grow, remove and shrink (sim-rootish),
FastSqrt's sqrt(x) in Java and C++ (sim-fastsqrt), SEList's add(i, x) and spread(u) (sim-selist-add) and remove(i)
and gather(u) (sim-selist-remove). The listings come from build_spec.listing(), as the text's code sets do: Python,
Java and C++ as ODS's editions print them (tools/ods_listing.py, printed=True), RootishArrayStack's Python with the
`//` port. The JavaScript, and FastSqrt's Python, in figures.js are the AI's and are not touched.

    python3 -I ch03/3.6/inline_code.py
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('build_spec', os.path.join(HERE, 'build_spec.py'))
spec = importlib.util.module_from_spec(sp)
sp.loader.exec_module(spec)

PANELS = {
    'rootish': ('RootishArrayStack', ['i2b(i)', 'get(i).set(i,x)', 'add(i,x)', 'grow()', 'remove(i)', 'shrink()'], ('python', 'java', 'cpp')),
    'fastsqrt': ('FastSqrt', ['sqrt(x)'], ('java', 'cpp')),
    'seladd': ('SEList', ['add(i,x)', 'spread(u)'], ('python', 'java', 'cpp')),
    'selrem': ('SEList', ['remove(i)', 'gather(u)'], ('python', 'java', 'cpp')),
}
NAMES = {'python': 'PY', 'java': 'JAVA', 'cpp': 'CPP'}


def main():
    path = os.path.join(HERE, 'figures.js')
    js = open(path, encoding='utf-8').read()
    for panel, (cls, members, langs) in PANELS.items():
        begin = f'/* BEGIN ODS LISTINGS {panel} (ch03/3.6/inline_code.py) */'
        end = f'/* END ODS LISTINGS {panel} */'
        a, b = js.index(begin), js.index(end)
        body = ''
        for lang in langs:
            text = '\n\n'.join(spec.listing(f'ods/{cls}.{m}')[lang] for m in members)
            body += f'  const {NAMES[lang]} = {json.dumps(text)};\n'
        js = js[:a + len(begin)] + '\n' + body + '  ' + js[b:]
    open(path, 'w', encoding='utf-8').write(js)
    print(f'{path}: {len(PANELS)} panels', file=sys.stderr)


if __name__ == '__main__':
    main()
