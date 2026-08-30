# AUDIT — brief v1.1 check 6 · Rung 2

**Date:** 2026-08-30
**Still:** `lookdev-rung2.png` 200×280, 8 spp CPU (GPU OOM on 400×560)
**Composite:** over `#0A0B0D`
**Excluded band:** 4.08 px = 4% of silhouette width 102 px, each side

## Rung 2 actions

KEY-L elevation **30° → 38°**. Power **400 W**. Az −55°, dist 3.0, size 0.15×2.20 unchanged.
Location: `(-1.9365, -1.356, 2.347)`. Track −Z to droplet centre.

Ground remains rung-1 spec (rough 0.65, spec IOR 0.5, 40×40).

## Check 6 v1.1

| Stat | Value |
|---|---|
| occupancy | 0.8607 |
| n pixels | 6948 |
| **median** sRGB luma | **0.4067** |
| mean | 0.4629 |
| p90 | 0.781 |
| delta vs rung 1 median | −0.014 |
| threshold | median < 0.08 |
| result | **FAIL** |

Elevation moved the key strip up a little. Not enough. Lower hemisphere is still the studio cyc via the 0.65-rough ground.

**Kept?** Yes (ladder forbids reverting a rung that did not pass in order to skip).

**Next:** rung 3 — KEY-L power 400 → 300 W, elevation stays 38°.
