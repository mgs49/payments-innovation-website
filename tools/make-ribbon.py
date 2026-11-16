#!/usr/bin/env python3
"""Draws the ribbon used by the alternative look: engraved banknote lines (a guilloche)
that turn into discrete tokens half-way across. Run from the repository root:
    python3 tools/make-ribbon.py
It writes src/_includes/ribbon.svg (home page, with the moving dot) and
src/assets/img/ribbon-strip.svg (the strip under every page title)."""
import math

GOLD = "#ffc000"

def build(W, H, amp, grid, sq, pulse, css_colours):
    mid = H / 2
    fams = [  # (number of lines, wavelength, share of the amplitude, phase shift)
        (14, W / 4.0, 1.00, 0.0),
        (9, W / 10.5, 0.46, 0.7),
    ]
    def env(x):
        return amp * (0.74 + 0.26 * math.cos(2 * math.pi * x / (W / 1.8) + 0.6))
    def y(x, fam, i):
        n, lam, share, ph = fam
        return mid + env(x) * share * math.sin(2 * math.pi * x / lam + 2 * math.pi * i / n + ph)

    line_end = 0.60 * W          # engraved lines stop here
    tok_start = 0.45 * W         # tokens begin here
    ramp_end = 0.58 * W          # ... and are at full strength here
    gold = "currentColor" if css_colours else GOLD
    out = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false">']
    out.append('<defs>'
               f'<linearGradient id="rb-fade" gradientUnits="userSpaceOnUse" x1="0" x2="{W}" y1="0" y2="0">'
               '<stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.04" stop-color="#fff"/>'
               '<stop offset="0.46" stop-color="#fff"/><stop offset="0.6" stop-color="#fff" stop-opacity="0"/></linearGradient>'
               f'<mask id="rb-mask" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="url(#rb-fade)"/></mask>'
               '</defs>')
    # engraved lines
    out.append(f'<g mask="url(#rb-mask)" fill="none" stroke="{gold}" stroke-width="{0.9 if pulse else 0.7}" stroke-opacity="0.78">')
    step = 8 if pulse else 14
    for fam in fams:
        for i in range(fam[0]):
            pts = []
            x = 0
            while x <= line_end:
                pts.append(f"{x:g},{y(x, fam, i):.1f}")
                x += step
            out.append('<polyline points="' + " ".join(pts) + '"/>')
    out.append('</g>')
    # tokens: the same curves, snapped to a grid
    cells = {}
    x = math.ceil(tok_start / grid) * grid
    while x <= W:
        for fam in fams:
            for i in range(fam[0]):
                gy = round(y(x, fam, i) / grid) * grid
                cells.setdefault(x, set()).add(gy)
        x += grid
    h = sq / 2
    def rect(cx, cy):
        return f"M{cx - h:g} {cy - h:g}h{sq:g}v{sq:g}h-{sq:g}z"
    def bright(cx, cy):
        return (int(cx / grid) * 7 + int(cy / grid) * 13) % 6 == 0
    dim_full, bright_full = [], []
    for cx in sorted(cells):
        t = min(1.0, max(0.0, (cx - tok_start) / (ramp_end - tok_start)))
        if cx > 0.97 * W:
            t = max(0.0, (W - cx) / (0.03 * W))
        d = "".join(rect(cx, cy) for cy in sorted(cells[cx]) if not bright(cx, cy))
        b = "".join(rect(cx, cy) for cy in sorted(cells[cx]) if bright(cx, cy))
        if t >= 1.0:
            dim_full.append(d); bright_full.append(b)
        else:
            if d: out.append(f'<path d="{d}" fill="{gold}" fill-opacity="{0.42 * t:.2f}"/>')
            if b: out.append(f'<path d="{b}" fill="{gold}" fill-opacity="{t:.2f}"/>')
    out.append(f'<path d="{"".join(dim_full)}" fill="{gold}" fill-opacity="0.42"/>')
    out.append(f'<path d="{"".join(bright_full)}" fill="{gold}"/>')
    if pulse:
        # one payment travelling along the middle line
        fam = fams[0]
        pts = []
        x = 0
        while x <= W:
            pts.append(f"{x:g} {y(x, fam, 0):.1f}")
            x += 16
        path = "M" + " L".join(pts)
        out.append(f'<g class="rb-pulse"><circle r="11" fill="#fff" fill-opacity="0.16"/><circle r="4.5" fill="#fff"/>'
                   f'<animateMotion dur="11s" repeatCount="indefinite" path="{path}"/></g>')
    out.append('</svg>')
    return "\n".join(out)

open("src/_includes/ribbon.svg", "w").write(build(1600, 240, 92, 12, 7, True, True))
open("src/assets/img/ribbon-strip.svg", "w").write(build(2400, 80, 30, 8, 4.6, False, False))
print("written")
