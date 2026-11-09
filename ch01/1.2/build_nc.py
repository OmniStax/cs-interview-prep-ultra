#!/usr/bin/env python3
"""Write 1.2's NC exercise card, exercises-nc.json (METHOD §0: CC BY-NC-SA cards live in their own file).

MIT 6.042J (Fall 2005) problem set 6, problem 7, the card the chapter config assigns to harmonic-numbers' integral
bounds. Its statement is set from the page render of the cached handout (sources/_cache/mitocw-6-042j-fall2005/,
ps6.pdf p. 5), whose pdftotext output loses the display; its key is MIT's worked solution, linked as 1.6's cards
link theirs. Shared with 1.3's build_nc.py: tools/nc_cards.py.

    python3 -I ch01/1.2/build_nc.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'tools'))
import nc_cards  # noqa: E402

CARDS = [
    dict(id='nc-6042-ps6-7', origin='mitocw-6-042j-fall2005', handout='ps6sol.pdf', set_='Problem Set 6', n='7',
         source_id='mitocw-6-042j-fall2005:ps6#7', bloom='Apply', cite='harmonic', concepts=['harmonic-numbers'],
         prompt='<p>Use the integral method to find upper and lower bounds for the following summation that differ by at most 0.05.</p>\n'
                '$$\\sum_{i=1}^{\\infty} \\frac{1}{i^3}$$\n'
                '<p><em>Hint:</em> Try adding the first few terms explicitly and then use integrals to bound the sum of the remaining terms.</p>'),
]

if __name__ == '__main__':
    nc_cards.write('1.2', CARDS)
