# AUDIT — brief v1.1 check 6 · Rung 3 (ladder floor)

**Date:** 2026-08-30
**Still:** `lookdev-rung3.png` 200×280, 8 spp CPU
**Composite:** over `#0A0B0D`
**Excluded band:** 4.08 px (4% of 102 px silhouette width)

## Rung 3 actions

KEY-L power **400 W → 300 W** (floor). Elevation **held at 38°**. Az, size, colour, dist unchanged. Ground remains §4.3.

## Check 6 v1.1

| Stat | Value |
|---|---|
| occupancy | 0.8607 |
| n pixels | 6948 |
| **median** sRGB luma | **0.3888** |
| mean | 0.4475 |
| p90 | 0.7535 |
| delta vs rung 2 | −0.018 |
| threshold | median < 0.08 |
| result | **FAIL** |

400 W → 300 W only moved the median 0.018. The remaining ~0.39 is **not** KEY-L. Brief §4.2.1: *If 300 W at 38° with the plane restored still fails, escalate — the problem is elsewhere and further dimming will not find it.*

**Kept?** Yes (last authorised rung). Do not drop below 300 W.

**Verdict: ESCALATE.** Sequences stay blocked.
