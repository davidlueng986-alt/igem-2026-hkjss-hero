# AUDIT — brief v1.1 check 6 · Rung 1

**Date:** 2026-08-30
**Still:** `lookdev-rung1.png` 400×560, 16 spp, film transparent
**Composite:** over `#0A0B0D` (not straight-alpha)
**Excluded band:** 8.08 px = 4% of silhouette width 202 px, each side

## Rung 1 actions (KEY-L untouched: 400 W / el 30°)

Restored `SM_Ground` to §4.3:
- z = −0.002
- Base `#0A0B0D` linear, Metallic 0, Roughness **0.65** (was 1.0)
- Specular IOR Level **0.5** (was 0.0 — that was an unauthorised 4c hack)
- camera vis OFF, glossy vis ON
- size 40 × 40 BU (≥ 12 × 12)

## Check 6 v1.1

| Stat | Value |
|---|---|
| occupancy | 0.8643 |
| n pixels in region | 27573 |
| **median** sRGB luma | **0.4205** |
| mean | 0.4845 |
| p90 | 0.8269 |
| threshold | median < 0.08 |
| result | **FAIL** |

Old 0.136 figure is void: it was mean-on-straight-alpha with Specular IOR 0 and the rim band included.

**Kept?** Yes — rung 1 is the specified plane. Do not re-disable spec.

**Next:** rung 2 (KEY-L el 30° → 38°, power 400 W).
