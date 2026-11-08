#!/usr/bin/env python3
"""Write this book's book.json and its first chapters' chapter.json, once.

METHOD §4.4 decision 19: `ost` creates no book and refuses writes to `exercise_kinds`, and it is not
changed, so the first book.json comes from this one-time script. Its input is the decided rows of
`book-json-proposal.md` (identity, authors, sources, licence, highlights, types, exercise_kinds,
exercise_sources) and the sections of `concept-map/toc.json`. Every later write goes through
`omnistax-content/tools/ost.py`.

It writes only fields `docs/content-format.md` lists (the schema is strict) and no concept rows:
concepts are written section by section during the build (root rule 6). It writes no section
content: a chapter.json lists its sections by id and title, and no section folder is made.

    python3 -I tools/scaffold_book.py [--chapters ch01,ch02,ch03] [--dry-run] [--force]

It refuses to overwrite an existing book.json or chapter.json unless --force is given.
"""
import argparse, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROPOSAL = os.path.join(ROOT, 'book-json-proposal.md')
TOC = os.path.join(ROOT, 'concept-map', 'toc.json')

# The fields docs/content-format.md lists for each record (omnistax-web/src/lib/content/schema.ts).
BOOK_FIELDS = {'id', 'title', 'publisher', 'authors', 'source_url', 'sources', 'copyright', 'license', 'license_url',
               'openstax', 'language', 'translation_of', 'translation', 'highlights', 'chapters', 'intro', 'summary',
               'types', 'symbols', 'exercise_kinds', 'exercise_sources', 'concepts', 'concept_prereqs', 'sheets', 'colours'}
REQUIRED_BOOK = {'id', 'title', 'publisher', 'license', 'chapters'}
SOURCE_FIELDS = {'title', 'url'}
HIGHLIGHT_FIELDS = {'facts', 'refs', 'concepts', 'words', 'symbols', 'underlines'}
TYPE_FIELDS = {'id', 'label', 'dimension'}
KIND_FIELDS = {'id', 'label'}
EXSOURCE_FIELDS = {'id', 'title', 'short', 'author', 'url', 'license', 'license_url'}
CHAPTER_FIELDS = {'id', 'dir', 'title', 'intro', 'summary', 'sections', 'variables'}
SECTION_REF_FIELDS = {'id', 'module', 'title', 'slug'}
URL = re.compile(r'^https?://\S+$')
LANG = re.compile(r'^[a-z]{2,3}(-[A-Za-z]{4})?(-[A-Z]{2})?$')


def fail(msg):
    sys.exit(f'scaffold_book: {msg}')


# ------------------------------------------------------------------ reading the proposal

def sections_of(md):
    """Heading text -> the lines under it, for every heading of any level."""
    out, cur = {}, None
    for line in md.splitlines():
        m = re.match(r'^#{2,4} (.*)$', line)
        if m:
            cur = m.group(1).strip(); out[cur] = []
        elif cur is not None:
            out[cur].append(line)
    return out


def table(lines):
    """The first markdown table in the lines, as a list of dicts keyed by its header cells."""
    rows = [l for l in lines if l.startswith('|')]
    if len(rows) < 2:
        return []
    split = lambda l: [c.strip() for c in l.strip().strip('|').split('|')]
    head = [h.strip('`') for h in split(rows[0])]
    return [dict(zip(head, split(r))) for r in rows[2:]]


def under(secs, prefix):
    keys = [k for k in secs if k.startswith(prefix)]
    if len(keys) != 1:
        fail(f'expected one heading starting {prefix!r} in book-json-proposal.md, found {keys}')
    return table(secs[keys[0]])


def ticked(cell):
    """The backticked values of a cell, or None where the cell is 'absent' or names no value."""
    vals = re.findall(r'`([^`]*)`', cell)
    return vals or None


def plain(cell):
    """A cell written as it stands: backticks stripped; 'absent' or empty is no value."""
    v = cell.strip().strip('`').strip()
    return None if v == '' or v.startswith('absent') else v


def read_proposal():
    secs = sections_of(open(PROPOSAL, encoding='utf-8').read())
    book = {}
    for row in under(secs, 'Identity'):
        field = row['field'].strip('`')
        vals = ticked(row['value'])
        if vals is None or row['value'].strip().startswith('absent'):
            continue
        if field == 'chapters':
            book['chapters'] = vals
        else:
            if len(vals) != 1:
                fail(f'identity field {field} has {len(vals)} values')
            book[field] = vals[0]
    book['authors'] = [r['entry'] for r in under(secs, '`authors`')]
    book['sources'] = [{'title': r['title'], 'url': r['url']} for r in under(secs, '`sources`')]
    hl = {}
    for r in under(secs, '`highlights`'):
        v = plain(r['value'])
        if v not in ('true', 'false'):
            fail(f'highlight {r["key"]} is {v!r}')
        hl[r['key'].strip('`')] = v == 'true'
    book['highlights'] = hl
    types = []
    for r in under(secs, '`types`'):
        t = {'id': r['id'].strip('`'), 'label': r['label']}
        if plain(r.get('dimension', '')):
            t['dimension'] = plain(r['dimension'])
        types.append(t)
    book['types'] = types
    book['exercise_kinds'] = [{'id': r['id'].strip('`'), 'label': r['label']} for r in under(secs, '`exercise_kinds`')]
    exs = []
    for prefix in ('Open', 'NC'):
        for r in under(secs, prefix):
            row = {}
            for k in ('id', 'title', 'short', 'author', 'url', 'license', 'license_url'):
                v = plain(r.get(k, ''))
                if v is not None:
                    row[k] = v
            exs.append(row)
    book['exercise_sources'] = exs
    return book


# ------------------------------------------------------------------ checking the shape

def check_book(b):
    errs = []
    errs += [f'book.json: unknown field {k}' for k in b if k not in BOOK_FIELDS]
    errs += [f'book.json: missing {k}' for k in REQUIRED_BOOK if k not in b]
    for k in ('source_url', 'license_url'):
        if k in b and not URL.match(b[k]): errs.append(f'book.json {k} is not a URL')
    if 'language' in b and not LANG.match(b['language']): errs.append('book.json language is not a BCP 47 tag')
    if not isinstance(b.get('authors', []), list) or not all(isinstance(a, str) for a in b['authors']):
        errs.append('book.json authors is not a list of strings')
    for s in b.get('sources', []):
        if set(s) != SOURCE_FIELDS or not URL.match(s['url']): errs.append(f'book.json sources row {s}')
    if set(b.get('highlights', {})) != HIGHLIGHT_FIELDS or not all(isinstance(v, bool) for v in b['highlights'].values()):
        errs.append('book.json highlights must declare all six as booleans')
    def rows(name, allowed, required):
        seen = set()
        for r in b.get(name, []):
            errs.extend(f'book.json {name}[{r.get("id")}]: unknown field {k}' for k in r if k not in allowed)
            errs.extend(f'book.json {name}[{r.get("id")}]: missing {k}' for k in required if k not in r)
            errs.extend(f'book.json {name}[{r.get("id")}]: {k} is not a string' for k, v in r.items() if not isinstance(v, str))
            if r.get('id') in seen: errs.append(f'book.json {name}: {r["id"]} twice')
            seen.add(r.get('id'))
    rows('types', TYPE_FIELDS, {'id', 'label'})
    rows('exercise_kinds', KIND_FIELDS, {'id', 'label'})
    rows('exercise_sources', EXSOURCE_FIELDS, {'id', 'title'})
    return errs


def check_chapter(c):
    errs = [f'{c["dir"]}/chapter.json: unknown field {k}' for k in c if k not in CHAPTER_FIELDS]
    for s in c['sections']:
        errs += [f'{c["dir"]}/chapter.json sections[{s.get("id")}]: unknown field {k}' for k in s if k not in SECTION_REF_FIELDS]
    return errs


# ------------------------------------------------------------------ the chapters

def chapters_from_toc(dirs):
    toc = json.load(open(TOC, encoding='utf-8'))
    by_dir = {f'ch{c["number"]:02d}': c for c in toc['chapters']}
    out = []
    for d in dirs:
        if d not in by_dir:
            fail(f'{d} is not a chapter of concept-map/toc.json')
        c = by_dir[d]
        out.append({'id': str(c['number']), 'dir': d, 'title': c['title'],
                    'sections': [{'id': s['number'], 'title': s['title']} for s in c['sections']],
                    'variables': []})
    return out


def write(path, record, dry, force):
    text = json.dumps(record, indent=1, ensure_ascii=False) + '\n'
    if dry:
        same = os.path.exists(path) and open(path, encoding='utf-8').read() == text
        state = 'exists, identical' if same else 'exists, differs' if os.path.exists(path) else 'new'
        print(f'--- {os.path.relpath(path, ROOT)} ({len(text)} bytes; {state})')
        return
    if os.path.exists(path) and not force:
        fail(f'{os.path.relpath(path, ROOT)} exists; this script runs once (use --force to overwrite)')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        f.write(text)
    json.load(open(tmp, encoding='utf-8'))
    os.replace(tmp, path)
    print(f'wrote {os.path.relpath(path, ROOT)}')


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--chapters', help='chapter directories to scaffold (default: book.json chapters)')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()
    book = read_proposal()
    dirs = a.chapters.split(',') if a.chapters else book['chapters']
    if dirs != book['chapters']:
        fail(f'--chapters {dirs} differs from the proposal\'s chapters {book["chapters"]}')
    chapters = chapters_from_toc(dirs)
    # Key order as content-format.md lists the fields; empty tables are written so ost finds them.
    order = ['id', 'title', 'publisher', 'authors', 'source_url', 'sources', 'license', 'license_url', 'language',
             'highlights', 'chapters', 'types', 'symbols', 'exercise_kinds', 'exercise_sources', 'concepts',
             'concept_prereqs', 'sheets']
    book.update({'symbols': [], 'concepts': [], 'concept_prereqs': [], 'sheets': []})
    book = {k: book[k] for k in order if k in book} | {k: v for k, v in book.items() if k not in order}
    errs = check_book(book) + [e for c in chapters for e in check_chapter(c)]
    if errs:
        fail('\n  ' + '\n  '.join(errs))
    write(os.path.join(ROOT, 'book.json'), book, a.dry_run, a.force)
    for c in chapters:
        write(os.path.join(ROOT, c['dir'], 'chapter.json'), c, a.dry_run, a.force)
    print(f'{len(book["types"])} types, {len(book["exercise_kinds"])} exercise kinds, '
          f'{len(book["exercise_sources"])} exercise sources, {len(book["authors"])} authors, '
          f'{len(chapters)} chapters, {sum(len(c["sections"]) for c in chapters)} sections')


if __name__ == '__main__':
    main()
