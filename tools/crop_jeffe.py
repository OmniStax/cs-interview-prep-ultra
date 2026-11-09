#!/usr/bin/env python3
"""Cut a figure of Erickson's out of a page render, for a photograph or a Sim's original.

A band of the page is given in PDF points from the bottom edge (as tools/extract_jeffe.py reports
baselines), the page is rendered with pdftoppm and the band trimmed to its ink.

    python3 -I tools/crop_jeffe.py sources/_cache/jeffe/00-intro.pdf 5 575 462 media/ch01/x.png [--dpi 200] [--x 0 481]
"""
import argparse
import os
import subprocess
import tempfile

from PIL import Image, ImageChops


def crop(pdf, page, top, bottom, out, dpi=200, x0=0, x1=None, pad=8):
    with tempfile.TemporaryDirectory() as d:
        base = os.path.join(d, 'p')
        subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page), '-r', str(dpi), '-png', pdf, base], check=True)
        png = [f for f in os.listdir(d) if f.endswith('.png')][0]
        im = Image.open(os.path.join(d, png)).convert('RGB')
    s = dpi / 72.0
    H = im.height / s
    box = (int(x0 * s), int((H - top) * s), int((x1 * s) if x1 else im.width), int((H - bottom) * s))
    band = im.crop(box)
    bg = Image.new('RGB', band.size, (255, 255, 255))
    diff = ImageChops.difference(band, bg).convert('L').point(lambda v: 255 if v > 24 else 0)
    bb = diff.getbbox()
    if bb:
        band = band.crop((max(0, bb[0] - pad), max(0, bb[1] - pad), min(band.width, bb[2] + pad), min(band.height, bb[3] + pad)))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    band.save(out, optimize=True)
    return band.size


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf'); ap.add_argument('page', type=int); ap.add_argument('top', type=float); ap.add_argument('bottom', type=float); ap.add_argument('out')
    ap.add_argument('--dpi', type=int, default=200); ap.add_argument('--x', type=float, nargs=2, default=None)
    a = ap.parse_args()
    x0, x1 = a.x if a.x else (0, None)
    print(a.out, crop(a.pdf, a.page, a.top, a.bottom, a.out, a.dpi, x0, x1))
