#!/usr/bin/env python3
"""Write doocs/leetcode's code for 0304 and 0370 (Solution 1, Python3, Java, C++ and JavaScript, all printed by
doocs: ruling 3, decision 18) into figures.js between its generated markers, read from the cache by script.

One thing is left out, for its reason: the comment block after 0304's classes ("Your NumMatrix object will be
instantiated and called as such: …"), which is LeetCode's harness template, not the solution. Nothing else changes.

    python3 -I ch02/2.4/inline_code.py
"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
SOL = os.path.join(BOOK, 'sources/_cache/doocs-leetcode/solution/0300-0399')
FILES = {'0304': '0304.Range Sum Query 2D - Immutable/README_EN.md', '0370': '0370.Range Addition/README_EN.md'}
TABS = {'python': ('Python3', 'python'), 'java': ('Java', 'java'), 'cpp': ('C++', 'cpp'), 'javascript': ('JavaScript', 'js')}
HARNESS = [re.compile(r'\n+# Your NumMatrix object.*$', re.S), re.compile(r'\n+/\*\*\n \* Your NumMatrix object.*?\*/\s*$', re.S)]


def solution1(text):
    a = text.index('### Solution 1')
    z = text.find('<!-- solution:end -->', a)
    return text[a:z]


def code(problem):
    t = solution1(open(os.path.join(SOL, FILES[problem]), encoding='utf-8').read())
    out = {}
    for lang, (tab, fence) in TABS.items():
        m = re.search(rf'#### {re.escape(tab)}\n\n```{fence}\n(.*?)\n```', t, re.S)
        src = m.group(1)
        for h in HARNESS:
            src = h.sub('', src)
        out[lang] = src.rstrip()
    return out


def main():
    path = os.path.join(HERE, 'figures.js')
    js = open(path, encoding='utf-8').read()
    body = '\n'.join(f'const DOOCS_{p} = {json.dumps(code(p), ensure_ascii=False, indent=2)};' for p in FILES)
    js = re.sub(r'(/\* @generated doocs: inline_code\.py \*/\n).*?(/\* @end generated \*/)', lambda m: m.group(1) + body + '\n' + m.group(2), js, flags=re.S)
    open(path, 'w', encoding='utf-8').write(js)


if __name__ == '__main__':
    main()
