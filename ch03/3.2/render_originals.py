#!/usr/bin/env python3
"""Render ODS's FIFO queue figure (latex/figs/queue.ipe, in the intro chapter) and its ArrayQueue figure
(latex/figs/arrayqueue.ipe) for the original toggles of sim-fifo-queue and sim-arrayqueue.

Ipe's own renderer draws each figure from its .ipe file unchanged, at 300 dpi on a transparent ground; the
preamble loads kpfonts and ODS's ods-colors.sty, so TEXINPUTS points at ODS's latex directory, and IPELATEXDIR
is a private scratch directory (as ch02/2.6/render_originals.py does). Needs iperender (Ipe 7) and
texlive-fonts-extra (kpfonts).

    python3 -I ch03/3.2/render_originals.py
"""
import os
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.dirname(os.path.dirname(HERE))
ODS = os.path.join(BOOK, 'sources/_cache/ods/latex')
OUT = os.path.join(BOOK, 'media/ch03')
FIGS = {'queue': 'ods-queue.png', 'arrayqueue': 'ods-arrayqueue.png'}


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
