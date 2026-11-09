#!/usr/bin/env python3
"""Render Brisk Walk's two figures that 1.6's Sims replace (the Venn diagram of All-time Idol, Figure 4.1,
and the first six rows of Pascal's triangle, Figure 6.1), for the Sims' original toggle.

Davies draws both in TikZ inside the chapter files. This reads each figure environment out of the cached
.tex by its label (tools/read_latex.py), drops its caption and label (the caption is the row's
original_caption), and typesets the drawing alone with the TikZ libraries brisk.tex loads, then crops the
page to the drawing. Nothing in the drawing is retyped. Needs pdflatex with TikZ, pdftoppm and Pillow.

    python3 -I ch01/1.6/render_originals.py
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(BOOK, 'tools'))
import read_latex  # noqa: E402

BRISK = os.path.join(BOOK, 'sources/_cache/brisk')
OUT = os.path.join(BOOK, 'media/ch01')
FIGS = [('probability.tex', 'venn', 'brisk-4-1-venn.png'), ('counting.tex', 'pascal', 'brisk-6-1-pascal.png')]

TEX = r'''\documentclass{article}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,shapes.symbols,graphs,quotes,math,positioning,fit}
\pagestyle{empty}
\begin{document}
\begin{center}
%s
\end{center}
\end{document}
'''


def body(path, label):
    s = read_latex.strip_comments(open(path, encoding='utf-8').read())
    for m in re.finditer(r'\\begin\{figure\}(\[[^\]]*\])?', s):
        a, _ = read_latex.env_end(s, 'figure', m.end())
        b = s[m.end():a]
        if '\\label{' + label + '}' in b:
            b = read_latex.drop_command(b, 'caption')
            b = read_latex.drop_command(b, 'label')
            return b.replace('\\centering', '')
    raise SystemExit(f'no figure {label} in {path}')


def main():
    os.makedirs(OUT, exist_ok=True)
    for f, label, png in FIGS:
        d = tempfile.mkdtemp()
        try:
            open(os.path.join(d, 'fig.tex'), 'w').write(TEX % body(os.path.join(BRISK, f), label))
            r = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'fig.tex'], cwd=d, capture_output=True, text=True)
            if not os.path.exists(os.path.join(d, 'fig.pdf')):
                print(r.stdout[-2000:])
                raise SystemExit(f'{label}: no PDF')
            subprocess.run(['pdftoppm', '-r', '220', '-png', '-singlefile', 'fig.pdf', 'fig'], cwd=d, check=True)
            im = Image.open(os.path.join(d, 'fig.png')).convert('RGB')
            box = ImageOps.invert(im).getbbox()
            im = im.crop((box[0] - 24, box[1] - 24, box[2] + 24, box[3] + 24))
            im.save(os.path.join(OUT, png))
            print(png, im.size)
        finally:
            shutil.rmtree(d)


if __name__ == '__main__':
    main()
