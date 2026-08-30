"""A6 check 6 v1.1 — median sRGB luma, composite over #0A0B0D, exclude 4% rim.

Run inside Blender after write_still. Do not measure straight-alpha RGBA.
"""
from __future__ import annotations

import json

BG = (10 / 255.0, 11 / 255.0, 13 / 255.0)  # #0A0B0D sRGB


def measure(path: str) -> dict:
    import bpy

    img = bpy.data.images.load(path)
    img.colorspace_settings.name = "Non-Color"
    w, h = img.size
    px = list(img.pixels)
    sil = []
    for y in range(h):
        row = y * w * 4
        for x in range(w):
            i = row + x * 4
            r, g, b, a = px[i], px[i + 1], px[i + 2], px[i + 3]
            if a > 0.5:
                cr = r * a + BG[0] * (1 - a)
                cg = g * a + BG[1] * (1 - a)
                cb = b * a + BG[2] * (1 - a)
                Y = 0.2126 * cr + 0.7152 * cg + 0.0722 * cb
                sil.append((x, y, Y))
    bpy.data.images.remove(img)
    xs = [p[0] for p in sil]
    ys = [p[1] for p in sil]
    xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)
    width = xmax - xmin + 1
    height = ymax - ymin + 1
    band = 0.04 * width
    xlo, xhi = xmin + band, xmax - band
    ycut = ymin + height / 3.0
    region = sorted(p[2] for p in sil if xlo <= p[0] <= xhi and p[1] <= ycut)
    n = len(region)
    med = region[n // 2]
    mean = sum(region) / n
    return {
        "wh": [w, h],
        "bbox": [xmin, ymin, xmax, ymax],
        "sil_w": width,
        "sil_h": height,
        "occupancy": round(height / h, 4),
        "band_px": round(band, 2),
        "n": n,
        "median": round(med, 4),
        "mean": round(mean, 4),
        "p90": round(region[int(n * 0.9)], 4),
        "composite_over": "#0A0B0D",
        "pass": med < 0.08,
    }


if __name__ == "__main__":
    import sys

    print(json.dumps(measure(sys.argv[1])))
