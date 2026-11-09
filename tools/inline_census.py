#!/usr/bin/env python3
"""Write the 2020 census rows into a figures.js between its DATA census-2020 markers, so the figure's
numbers come from the registered file and are never typed.

Each row is [state, resident population, representatives in the 2020 apportionment].

    python3 -I tools/inline_census.py ch01/1.1/figures.js
"""
import csv
import json
import os
import re
import sys

BOOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BOOK, 'sources', '_cache', 'census-2020', 'res2020.csv')

rows = [[r[0], int(r[1]), int(r[2])] for r in csv.reader(open(CSV, encoding='utf-8'))]
assert len(rows) == 50 and sum(r[2] for r in rows) == 435, 'expected the 50 states and 435 seats'
path = sys.argv[1]
src = open(path, encoding='utf-8').read()
body = 'const CENSUS = [\n' + ''.join(f'    {json.dumps(r, ensure_ascii=False)},\n' for r in rows) + '  ];'
new, n = re.subn(r'(/\* DATA census-2020 BEGIN[^\n]*\*/\n)\s*const CENSUS = \[.*?\];(\n\s*/\* DATA census-2020 END \*/)',
                 lambda m: m.group(1) + '  ' + body + m.group(2), src, flags=re.S)
assert n == 1, 'markers not found'
open(path, 'w', encoding='utf-8').write(new)
print(f'{path}: {len(rows)} states written', file=sys.stderr)
