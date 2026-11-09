#!/usr/bin/env python3
"""Render ODS's Figures 3.2 and 3.3 (latex/figs/dllist2.ipe, dllist-addbefore.ipe) for the original toggles of
sim-dllist-ring and sim-dllist.

Ipe's own renderer draws each figure from its .ipe file unchanged, at 300 dpi on a transparent ground. The
figures' LaTeX preamble loads kpfonts and ODS's ods-colors.sty, so TEXINPUTS points at ODS's latex directory;
IPELATEXDIR is a private scratch directory, so that two builds rendering at once do not share Ipe's LaTeX run.
Needs iperender (Ipe 7) and texlive-fonts-extra (kpfonts).

    python3 -I ch02/2.6/render_originals.py
"""
import os
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
ODS = os.path.join(BOOK, 'sources/_cache/ods/latex')
OUT = os.path.join(BOOK, 'media/ch02')
FIGS = {'dllist2': 'ods-dllist.png', 'dllist-addbefore': 'ods-dllist-addbefore.png'}


def main():
    os.makedirs(OUT, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, IPELATEXDIR=tmp, TEXINPUTS=ODS + ':')
        for src, dst in FIGS.items():
            subprocess.run(['iperender', '-png', '-resolution', '300', os.path.join(ODS, 'figs', src + '.ipe'),
                            os.path.join(OUT, dst)], check=True, env=env, capture_output=True)
            print(os.path.join(OUT, dst))


if __name__ == '__main__':
    main()
