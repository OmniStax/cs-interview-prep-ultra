#!/usr/bin/env python3
"""ODS's code listings, read from the source cache the way ODS's own extractors print them.

ODS's LaTeX names a listing by class and members, `\\codeimport{ods/DLList.getNode(i)}`; each edition's
extractor (`latex/snarf-java.pl`, `snarf-cpp.pl`, `snarf-python.py`) finds those members in the class's source
and prints them. This reads the same members from `java/ods/<Class>.java`, `cpp/<Class>.h` and
`python/ods/<class>.py` and applies the extractors' visible rules, so no line of code is typed by hand:

- Java (snarf-java.pl): a member is a method whose name and parameter names match (`getNode(i)`), or a field
  by its name (`n`, `dummy`); the modifiers static, public, protected, private and final are dropped, and so are
  the lines that throw IndexOutOfBoundsException and annotation lines.
- C++ (snarf-cpp.pl): an out-of-class definition `DLList<T>::getNode(int i)` or a field of the class body, with
  typename, const, inline, virtual and static dropped, template lines dropped and blank lines skipped.
- Python (snarf-python.py): a method whose name, its underscores stripped, and arguments without self match the
  member in snake case (`get_node(i)`); a plain field name in the list adds `initialize()`, so
  `DLList.n.dummy.DLList()` prints `_initialize`. Blank lines inside a method are skipped, as the extractor
  skips them.

Tabs are four spaces, a member's indentation inside its class is taken off, and members are joined by a blank
line. Used by ch02/2.6's build_spec.py; any ODS section may use it. With printed=True each function also applies
what its extractor hides (Java's `f.` and `Math.`, C++'s class prefix, Python's raising lines), as ch02/2.2 asks.

    python3 -I tools/ods_listing.py DLList getNode(i)      # prints the three languages
"""
import os
import re
import sys

BOOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ODS = os.path.join(BOOK, 'sources/_cache/ods')
JAVA_MODS = r'(?:static|public|protected|private|final)\s+'
CPP_DROP = r'(?:typename|const|inline|virtual|static)\s'


def _members(spec):
    """'getNode(i)' and 'n' from 'getNode(i).n': split on the dots outside parentheses."""
    out, depth, cur = [], 0, ''
    for ch in spec:
        if ch == '.' and depth == 0:
            out.append(cur)
            cur = ''
            continue
        depth += {'(': 1, ')': -1}.get(ch, 0)
        cur += ch
    out.append(cur)
    return [m for m in out if m]


def _dedent(lines):
    lines = [l.replace('\t', '    ').rstrip() for l in lines]
    pad = min((len(l) - len(l.lstrip()) for l in lines if l.strip()), default=0)
    return '\n'.join(l[pad:] for l in lines)


def _sig(name, params):
    """name(p1,p2): the parameter names only, types and defaults dropped."""
    names = []
    for p in params.split(','):
        p = p.split('=')[0].strip()
        if p:
            names.append(re.split(r'[\s*&]+', p)[-1])
    return f'{name}({",".join(names)})'


# What the extractors hide beyond the modifiers (snarf-java.pl: `f.` the factory, `Math.max`, `Math.min`;
# snarf-cpp.pl: the class prefix of an out-of-class definition; snarf-python.py: a line that raises, which its
# translate_code empties). Applied where a caller asks for the listing as the edition prints it (printed=True);
# the default leaves the output as it was.
def _printed_java(text):
    text = re.sub(r'([^A-Za-z0-9])f\.', r'\1', text)
    return re.sub(r'\bMath\.(max|min)\b', r'\1', text)


def _printed_cpp(text, cls):
    return re.sub(r'\b' + cls + r'(<[^>]+>)?::', '', text)


def _printed_python(text):
    return '\n'.join(l for l in text.split('\n') if not re.search(r'\braise\b', l))


def java(cls, spec, printed=False):
    if printed:
        return _printed_java(java(cls, spec))
    want = _members(spec)
    src = open(os.path.join(ODS, 'java/ods', cls + '.java'), encoding='utf-8').read().split('\n')
    out, cur, depth, printing = [], [], 0, False
    for line in src:
        if 'IndexOutOfBoundsException' in line or re.match(r'\s*@', line):
            continue
        if depth == 1 and not printing:
            m = re.match(r'\s*(?:' + JAVA_MODS + r')*(?:<[^>]*>\s*)?[\w<>\[\]]+\s+(\w+)\s*\(([^)]*)\)', line) or \
                re.match(r'\s*(?:' + JAVA_MODS + r')*(\w+)\s*\(([^)]*)\)\s*\{', line)
            f = re.match(r'\s*(?:' + JAVA_MODS + r')*[\w<>\[\]]+\s+(\w+)\s*;', line)
            if m and _sig(m.group(1), m.group(2)) in want:
                printing = True
            elif f and f.group(1) in want:
                out.append(_dedent([re.sub(JAVA_MODS, '', line)]))
        if printing:
            cur.append(re.sub(JAVA_MODS, '', line))
        depth += line.count('{') - line.count('}')
        if printing and depth == 1:
            out.append(_dedent(cur))
            cur, printing = [], False
    return _join(out)


def _join(parts):
    """Fields stand together; each method stands apart, after a blank line. A field is a one-line part, so a
    run of fields (ArrayQueue's a, j and n) stays one paragraph however long it is (ch03/3.2)."""
    text, prev = '', None
    for p in parts:
        if text:
            text += '\n' if '\n' not in p and prev is not None and '\n' not in prev else '\n\n'
        text += p
        prev = p
    return text


def cpp(cls, spec, printed=False):
    if printed:
        return _printed_cpp(cpp(cls, spec), cls)
    want = _members(spec)
    src = open(os.path.join(ODS, 'cpp', cls + '.h'), encoding='utf-8').read().split('\n')
    out, cur, depth, printing, inclass, body = [], [], 0, False, False, 1
    for raw in src:
        line = re.sub(CPP_DROP, '', raw)
        line = re.sub(r'template\s*<[^\]]+>', '', line)
        if not printing:
            m = re.match(r'\s*(?:[\w<>:*&]+\s*[*&]*\s+)?' + cls + r'(?:<[^>]*>)?::(\w+)\s*\(([^)]*)\)', line)
            if depth == 1 and m and _sig(m.group(1), m.group(2)) in want:
                printing = True
            # a method defined inside the class body (SLList.h), as snarf-cpp.pl also prints one (ch03/3.2)
            mi = re.match(r'\s*[\w<>:]+\s*[*&]*\s+[*&]*(\w+)\s*\(([^)]*)\)[^;]*$', line)
            if inclass and depth == 2 and mi and _sig(mi.group(1), mi.group(2)) in want:
                printing, body = True, 2
            if depth == 1 and re.match(r'\s*class\s+' + cls + r'\b', line):
                inclass = True
            # a field, its type perhaps a template of pointers (RootishArrayStack's ArrayStack<T*> blocks, ch03/3.6)
            f = re.match(r'\s*[\w<>]+\s*\*?\s+\*?(\w+)\s*;', line) or re.match(r'\s*\w+<[\w*\s,]+>\s+(\w+)\s*;', line)
            if inclass and depth == 2 and f and f.group(1) in want:
                out.append(_dedent([line]))
        if printing and line.strip():
            cur.append(line)
        depth += line.count('{') - line.count('}')
        if inclass and depth == 1:
            inclass = False
        if printing and depth == body and any('{' in l for l in cur):
            out.append(_dedent(cur))
            cur, printing, body = [], False, 1
    return _join(out)


def python(cls, spec, printed=False):
    if printed:
        return _printed_python(python(cls, spec))
    want = [re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower() for s in _members(spec)]
    if any(re.match(r'^\w+$', s) for s in want):
        want.append('initialize()')
    src = open(os.path.join(ODS, 'python/ods', cls.lower() + '.py'), encoding='utf-8').read().split('\n')
    out, cur, indent = [], None, None
    for line in src:
        if cur is not None:
            if line == '' or line.startswith(indent):
                if line.strip():
                    cur.append(line)
                continue
            out.append(_dedent(cur))
            cur = None
        m = re.match(r'(\s{4})?def\s+(\w+)(\(.*\))\s*:', line)
        if m:
            name = re.sub(r'^_*|_*$', '', m.group(2))
            args = re.sub(r'\s*', '', re.sub(r'^\(self\s*,?\s*', '(', m.group(3)))
            if name + args in want:
                indent = re.match(r'\s*', line).group(0) + '    '
                cur = [line]
    if cur is not None:
        out.append(_dedent(cur))
    return '\n\n'.join(out)


if __name__ == '__main__':
    cls, spec = sys.argv[1], sys.argv[2]
    for f in (python, java, cpp):
        print(f'--- {f.__name__}\n{f(cls, spec)}')
