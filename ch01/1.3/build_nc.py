#!/usr/bin/env python3
"""Write 1.3's NC exercise cards, exercises-nc.json (METHOD §0: CC BY-NC-SA cards live in their own file).

The four MIT OpenCourseWare problems the chapter config assigns to big-o and big-omega-theta. Each statement is
set from the page render of its cached handout (sources/_cache/mitocw-*/), whose pdftotext output loses the
mathematics; each key is MIT's worked solution, linked as 1.6's cards link theirs (tools/nc_cards.py). A problem's
own preamble about write-ups is left out; nothing of the problem is.

    python3 -I ch01/1.3/build_nc.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'tools'))
import nc_cards  # noqa: E402

S20 = ('<p><strong>Asymptotic behavior of functions</strong></p>\n'
       '<p>For each of the following sets of five functions, order them so that if $f_a$ appears before $f_b$ in your sequence, '
       'then $f_a = O(f_b)$. If $f_a = O(f_b)$ and $f_b = O(f_a)$ (meaning $f_a$ and $f_b$ could appear in either order), indicate '
       'this by enclosing $f_a$ and $f_b$ in a set with curly braces. For example, if the functions are:</p>\n'
       '$$f_1 = n, \\qquad f_2 = \\sqrt{n}, \\qquad f_3 = n + \\sqrt{n},$$\n'
       '<p>the correct answers are $(f_2, \\{f_1, f_3\\})$ or $(f_2, \\{f_3, f_1\\})$.</p>\n'
       '<p><strong>Note:</strong> Recall that $a^{b^c}$ means $a^{(b^c)}$, not $(a^b)^c$, and that $\\log$ means $\\log_2$ unless a '
       'different base is specified explicitly. Stirling’s approximation may help for comparing factorials.</p>\n'
       '<p><strong>a)</strong> $f_1 = \\log(n^n)$, $f_2 = (\\log n)^n$, $f_3 = \\log(n^{6006})$, $f_4 = (\\log n)^{6006}$, '
       '$f_5 = \\log\\log(6006n)$</p>\n'
       '<p><strong>b)</strong> $f_1 = 2^n$, $f_2 = 6006^n$, $f_3 = 2^{6006^n}$, $f_4 = 6006^{2^n}$, $f_5 = 6006^{n^2}$</p>\n'
       '<p><strong>c)</strong> $f_1 = n^n$, $f_2 = \\binom{n}{n-6}$, $f_3 = (6n)!$, $f_4 = \\binom{n}{n/6}$, $f_5 = n^6$</p>\n'
       '<p><strong>d)</strong> $f_1 = n^{n+4} + n!$, $f_2 = n^{7\\sqrt{n}}$, $f_3 = 4^{3n \\log n}$, $f_4 = 7^{n^2}$, '
       '$f_5 = n^{12 + 1/n}$</p>')

F05 = ('<p><strong>Asymptotic Notation</strong></p>\n'
       '<p>For each of the following statements, decide whether it is <strong>always true</strong>, <strong>never true</strong>, '
       'or <strong>sometimes true</strong> for asymptotically nonnegative functions $f$ and $g$. If it is <strong>always true</strong> '
       'or <strong>never true</strong>, explain why. If it is <strong>sometimes true</strong>, give one example for which it is true, '
       'and one for which it is false.</p>\n'
       '<p><strong>(a)</strong> $f(n) = O(f(n)^2)$</p>\n'
       '<p><strong>(b)</strong> $f(n) + g(n) = \\Theta(\\max(f(n), g(n)))$</p>\n'
       '<p><strong>(c)</strong> $f(n) + O(f(n)) = \\Theta(f(n))$</p>\n'
       '<p><strong>(d)</strong> $f(n) = \\Omega(g(n))$ and $f(n) = o(g(n))$ (note the little-$o$)</p>\n'
       '<p><strong>(e)</strong> $f(n) \\neq O(g(n))$ and $g(n) \\neq O(f(n))$</p>')

F11 = ('<p><strong>Asymptotic Practice</strong></p>\n'
       '<p>For each group of functions, sort the functions in increasing order of asymptotic (big-O) complexity:</p>\n'
       '<p><strong>(a)</strong> Group 1: $f_1(n) = n^{0.999999}\\log n$, $f_2(n) = 10000000n$, $f_3(n) = 1.000001^n$, $f_4(n) = n^2$</p>\n'
       '<p><strong>(b)</strong> Group 2: $f_1(n) = 2^{2^{1000000}}$, $f_2(n) = 2^{100000n}$, $f_3(n) = \\binom{n}{2}$, '
       '$f_4(n) = n\\sqrt{n}$</p>\n'
       '<p><strong>(c)</strong> Group 3: $f_1(n) = n^{\\sqrt{n}}$, $f_2(n) = 2^n$, $f_3(n) = n^{10} \\cdot 2^{n/2}$, '
       '$f_4(n) = \\sum_{i=1}^{n} (i + 1)$</p>')

M042 = ('<p><strong>(a)</strong> Given that $f(x) = O(g(x))$, prove that $f(x)^2 = O(g(x)^2)$.</p>\n'
        '<p><strong>(b)</strong> Let $f(x) ::= 2x$ and $g(x) ::= x$, so $f(x) = O(g(x))$. Prove that $2^{g(x)} = o(2^{f(x)})$, so '
        '$2^{f(x)} \\neq O(2^{g(x)})$.</p>')

CARDS = [
    dict(id='nc-6006s20-ps1-1', origin='mitocw-6-006-spring2020', handout='Problem Set 1 Solutions', set_='Problem Set 1', n='1-1',
         source_id='mitocw-6-006-spring2020:ps1#1-1', bloom='Analyze', cite='big-o', concepts=['big-o', 'big-omega-theta', 'logarithms'], prompt=S20),
    dict(id='nc-6046f05-ps1-1', origin='mitocw-6-046j-fall2005', handout='Problem Set 1 Solutions', set_='Problem Set 1', n='1-1',
         source_id='mitocw-6-046j-fall2005:ps1#1-1', bloom='Evaluate', cite='omega-theta', concepts=['big-o', 'big-omega-theta'], prompt=F05),
    dict(id='nc-6006f11-ps1-1', origin='mitocw-6-006-fall2011', handout='Problem Set 1 Solutions', set_='Problem Set 1', n='1-1',
         source_id='mitocw-6-006-fall2011:ps1#1-1', bloom='Analyze', cite='big-o', concepts=['big-o'], prompt=F11),
    dict(id='nc-6042f05-ps6-8', origin='mitocw-6-042j-fall2005', handout='ps6sol.pdf', set_='Problem Set 6', n='8',
         source_id='mitocw-6-042j-fall2005:ps6#8', bloom='Apply', cite='big-o', concepts=['big-o'], prompt=M042),
]

if __name__ == '__main__':
    nc_cards.write('1.3', CARDS)
