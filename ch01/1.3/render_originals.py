#!/usr/bin/env python3
"""Render ODS's two plots of 15n against 2n log n (Figure 1.5 of its chapter 1) from ODS's own gnuplot
scripts, for sim-crossover's original toggle.

ODS draws the figure with latex/images/bigoh-1.gp and bigoh-2.gp (gnuplot's tikz terminal) and sets each
plot through \\input in intro.tex. This runs the two scripts unchanged in a scratch directory, typesets
each plot alone with ODS's colour file at the width intro.tex gives it (.98 of the line), and crops the
page to the plot. Needs gnuplot (with its lua/tikz terminal), pdflatex with TikZ, pdftoppm and Pillow.

    python3 -I ch01/1.3/render_originals.py
"""
import os
import shutil
import subprocess
import tempfile

from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
ODS = os.path.join(BOOK, 'sources/_cache/ods/latex')
OUT = os.path.join(BOOK, 'media/ch01')

TEX = r'''\documentclass{article}
\usepackage{tikz}
\usepackage{gnuplot-lua-tikz}
\input{ods-colors.sty}
\pagestyle{empty}
\begin{document}
\noindent\resizebox{.98\linewidth}{!}{\input{%s.tex}}
\end{document}
'''


def main():
    os.makedirs(OUT, exist_ok=True)
    with tempfile.TemporaryDirectory() as w:
        shutil.copy(os.path.join(ODS, 'ods-colors.sty'), w)
        for name in ('bigoh-1', 'bigoh-2'):
            shutil.copy(os.path.join(ODS, 'images', name + '.gp'), w)
            subprocess.run(['gnuplot', name + '.gp'], cwd=w, check=True)
            open(os.path.join(w, f'{name}-page.tex'), 'w').write(TEX % name)
            subprocess.run(['pdflatex', '-interaction=nonstopmode', f'{name}-page.tex'], cwd=w, check=True,
                           stdout=subprocess.DEVNULL)
            subprocess.run(['pdftoppm', '-r', '160', '-png', '-singlefile', f'{name}-page.pdf', name], cwd=w, check=True)
            im = Image.open(os.path.join(w, name + '.png')).convert('RGB')
            x0, y0, x1, y1 = ImageOps.invert(im).getbbox()
            pad = 16
            im = im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad)))
            path = os.path.join(OUT, f'ods-{name}.png')
            im.save(path, optimize=True)
            print(path, im.size)


if __name__ == '__main__':
    main()
