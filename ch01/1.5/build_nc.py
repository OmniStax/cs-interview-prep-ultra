"""Write 1.5's exercises-nc.json: the section's NC exercise cards (METHOD §0, book RULES "Licence and attribution").

The cards are CC BY-NC-SA 4.0 and live apart from section.json, in the shape of section.json's own `exercises`
and `exercise_concepts` tables, with `origin` naming the NC source (book RULES, "Exercise kinds"). The app does
not read this file yet (an approved app change, decision 19); it is written now so the card is ready.

The statement and the key are read by script from the solution handout, which prints the problem with its
solution under each part (`pdftotext -layout` of the cached PDF, sources/_cache/mitocw-6-046j-spring2012). The
text font survives the extraction; the displays do not (fractions and stacked limits come out in pieces), so
each display is set here in LaTeX from the page render, keyed by the first and last line of the pieces, and a
few inline runs the layout breaks are put back by a replacement table, each with its reason. Nothing else is
typed.

6.046J Fall 2005 problem 6-1 (Electronic Billboard), which the plan also lists, is not built: its handout sets
every formula in Type 3 fonts whose glyphs are named a0, a1, …, so no formula of its statement or its solution
can be read by script, and transcribing some hundred of them by hand is left to a pass that can check them.

    python3 -I ch01/1.5/build_nc.py
"""
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
SOL = 'sources/_cache/mitocw-6-046j-spring2012/da32e00aa88ebde8730150db3d7577b8_MIT6_046JS12_ps6_sol.txt'

# (first line of the pieces, last line, LaTeX as the page prints it)
DISPLAYS = [
    ('imbalance(x) = |x.left.size − x.right.size|', None,
     r'\mathit{imbalance}(x) = \lvert x.\mathit{left}.\mathit{size} - x.\mathit{right}.\mathit{size}\rvert'),
    ('imbalance(x)   |x.left.size − x.right.size |', 'x.size                  x.size',
     r'\mathit{imb\text{-}ratio}(x) = \frac{\mathit{imbalance}(x)}{x.\mathit{size}} = \frac{\lvert x.\mathit{left}.\mathit{size} - x.\mathit{right}.\mathit{size}\rvert}{x.\mathit{size}}'),
    ('1', 'x.left.size ≤ 34 · x.size − 12',
     r'\begin{aligned} \mathit{imb\text{-}ratio}(x) &\le \tfrac12 \\ \frac{\lvert x.\mathit{left}.\mathit{size} - x.\mathit{right}.\mathit{size}\rvert}{x.\mathit{size}} &\le \tfrac12 \\ '
     r'\lvert x.\mathit{left}.\mathit{size} - x.\mathit{right}.\mathit{size}\rvert &\le \frac{x.\mathit{size}}{2} \\ '
     r'\lvert x.\mathit{left}.\mathit{size} - (x.\mathit{size} - x.\mathit{left}.\mathit{size} - 1)\rvert &\le \tfrac12 \cdot x.\mathit{size} \\ '
     r'\lvert 2 \cdot x.\mathit{left}.\mathit{size} - x.\mathit{size} + 1\rvert &\le \tfrac12 \cdot x.\mathit{size} \\ '
     r'2 \cdot x.\mathit{left}.\mathit{size} - x.\mathit{size} + 1 &\le \tfrac12 \cdot x.\mathit{size} \\ '
     r'2 \cdot x.\mathit{left}.\mathit{size} &\le \tfrac32 \cdot x.\mathit{size} - 1 \\ '
     r'x.\mathit{left}.\mathit{size} &\le \tfrac34 \cdot x.\mathit{size} - \tfrac12 \end{aligned}'),
    ('1 ≤ # of descendants ≤ ( 34 )d · n', 'd ≤ log 4 n',
     r'\begin{aligned} 1 &\le \text{\# of descendants} \le (\tfrac34)^d \cdot n \\ \log_{\frac43} 1 &\le \log_{\frac43}\bigl((\tfrac34)^d \cdot n\bigr) \\ '
     r'0 &\le \log_{\frac43} (\tfrac34)^d + \log_{\frac43} n \\ d &\le \log_{\frac43} n \end{aligned}'),
    ('φ(x) = c · max{0, imbalance(x) − 1}.', None, r'\phi(x) = c \cdot \max\{0, \mathit{imbalance}(x) - 1\}.'),
    ('amortized cost = real cost + ∆Φ', '= (a − c/2) · x.size + c',
     r'\begin{aligned} \text{amortized cost} &= \text{real cost} + \Delta\Phi \\ &= a \cdot x.\mathit{size} - c \cdot x.\mathit{size}/2 + c \\ &= (a - c/2) \cdot x.\mathit{size} + c \end{aligned}'),
]
# (as extracted, as the page prints it, why)
FIXES = [
    ('I NSERT', 'INSERT', 'small caps: the capital is set apart from the rest of the name'),
    ('con- texts', 'contexts', 'a word broken at a line end'),
    ('D ELETE', 'DELETE', 'the same'),
    ('≤ 34 · root.size = ( 34 )d · n.', '≤ (3/4)^d · root.size = (3/4)^d · n.', 'the fraction 3/4 and the exponent d are stacked'),
    ('Φ(D) = x φ(x).', 'Φ(D) = Σ_x φ(x).', 'the summation sign is drawn on the line above'),
    ('$c', '＄c', 'a dollar sign in an exercise string is the fullwidth ＄ (root RULES 19)'),
]


def lines_of_problem():
    raw = open(os.path.join(BOOK, SOL), encoding='utf-8').read().split('\n')
    a = next(i for i, l in enumerate(raw) if l.startswith('Problem 6-1.'))
    z = next(i for i, l in enumerate(raw) if l.startswith('Problem 6-2.'))
    out = []
    for l in raw[a + 1:z]:
        s = l.strip().strip('\x01')        # pdftotext marks one stacked exponent with a control character
        if re.match(r'^(\d+\s+)?Handout 17: Problem Set 6 Solutions(\s+\d+)?$', s):
            continue
        if s in ('d', 'P', '3'):                  # pieces of a stacked exponent, a summation sign, a log base
            out.append('\x00' + s)
            continue
        out.append(l.rstrip())
    return out


def set_displays(lines):
    """Each display's pieces become one line `$$…$$`."""
    out, i = [], 0
    while i < len(lines):
        s = lines[i].strip()
        hit = None
        for first, last, tex in DISPLAYS:
            if s == first or (first == '1' and s == '1' and i + 1 < len(lines) and 'imb-ratio(x) ≤' in lines[i + 1]):
                hit = (first, last, tex)
                break
        if hit is None:
            if not s.startswith('\x00'):
                out.append(lines[i])
            i += 1
            continue
        first, last, tex = hit
        j = i
        if last:
            while j < len(lines) and lines[j].strip() != last:
                j += 1
            if j >= len(lines):
                raise SystemExit(f'display {first!r}: no line {last!r}')
            # a log base or an exponent may stand on the line after the last piece
            while j + 1 < len(lines) and lines[j + 1].startswith('\x00'):
                j += 1
        out.append('$$' + tex + '$$')
        i = j + 1
    return out


def paragraphs(lines):
    """Lines to paragraphs: a blank line, a part label, Solution:, Hint: or a display starts a new one."""
    paras, cur = [], []

    def close():
        if cur:
            paras.append(re.sub(r'\s+', ' ', ' '.join(x.strip() for x in cur)))
            cur.clear()
    for l in lines:
        s = l.strip()
        if not s:
            # a page break inside a sentence: the paragraph carries on when the next line starts in lower case
            if cur and not re.search(r'[.:?!)]$', cur[-1].strip()):
                continue
            close()
            continue
        if s.startswith('$$'):
            close()
            paras.append(s)
            continue
        if re.match(r'^\([a-e]\)\s', s) or s.startswith('Solution:') or s.startswith('Hint:'):
            close()
        # a paragraph of the solution that starts on a new line flush with the solution's text
        if cur and re.match(r'^(Now consider|Any insertion|What about|To trigger|So if we set|Note that unlike|We know that at)', s):
            close()
        cur.append(s)
    close()
    return paras


def fix(s, used):
    for i, (a, b, _) in enumerate(FIXES):
        if a in s:
            s = s.replace(a, b)
            used.add(i)
    return s


def to_html(p):
    if p.startswith('$$'):
        return p
    h = html.escape(p, quote=False)
    h = re.sub(r'^(\([a-e]\))\s', r'<strong>\1</strong> ', h)
    h = re.sub(r'^(Solution:|Hint:)', r'<strong>\1</strong>', h)
    return f'<p>{h}</p>'


def build():
    used = set()
    paras = [fix(p, used) for p in paragraphs(set_displays(lines_of_problem()))]
    unused = [FIXES[i][0] for i in range(len(FIXES)) if i not in used]
    if unused:
        raise SystemExit(f'fixes never applied: {unused}')
    prompt, solution, part = [], [], None
    in_sol = False
    for p in paras:
        m = re.match(r'^\(([a-e])\)\s', p)
        if m:
            part, in_sol = m.group(1), False
            prompt.append(p)
            continue
        if p.startswith('Solution:'):
            in_sol = True
            solution.append(re.sub(r'^Solution:\s*', f'({part}) ', p))
            continue
        if in_sol and not re.match(r'^(Clearly we need|Suppose that you modify)', p):
            solution.append(p)
            continue
        in_sol = False
        prompt.append(p)
    card = {
        'id': 'nc1', 'source_id': 'mitocw-6-046j-spring2012:ps6#6-1', 'source_number': 'Problem Set 6, Problem 6-1',
        'origin': 'mitocw-6-046j-spring2012', 'kind': 'exercise', 'bloom': 'Analyze', 'place': {'at': 'end'},
        'cite': 'accounting',
        'prompt': '<p><strong>Amortization in Balanced Binary Trees</strong></p>\n' + '\n'.join(to_html(p) for p in prompt),
        'answer': {'type': 'open', 'solution': '\n'.join(to_html(p) for p in solution), 'generated_by': 'source'},
    }
    rec = {
        'exercises': [card],
        'exercise_concepts': [
            {'exercise': 'nc1', 'concept': 'amortized-analysis'},
            {'exercise': 'nc1', 'concept': 'aggregate-accounting'},
            {'exercise': 'nc1', 'concept': 'potential-method'},
        ],
    }
    with open(os.path.join(HERE, 'exercises-nc.json'), 'w', encoding='utf-8') as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print(f'exercises-nc.json: {len(rec["exercises"])} card, {len(prompt)} prompt paragraphs, {len(solution)} solution paragraphs')


if __name__ == '__main__':
    build()
