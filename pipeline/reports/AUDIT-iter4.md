# AUDIT — geometry iteration 4 (+ S2 extra p2.x)
**Auditor:** A6 (`qa-review`)
**Date:** 2026-08-30
**Variables (sequential, one per call):**
- iter 4: shorten p3.handle_left (z 0.23 → 0.28)
- S2 extra: translate p2.x 0.206 → 0.190 (handles with co)
**Verdict:** geometry **PASS** (checks 1–3 + tip). Lookdev still **NO-SHIP** until Cycles PNG.

## Measured

| # | Check | Result | Measured / note |
|---|---|---|---|
| 1 | width/height | **PASS** | 0.4200 exact |
| 2 | widest from base | **PASS** | 0.3000. Plateau r=0.2100 on z∈[0.287, 0.300]; global max not above 0.210. |
| 3 | no neck inflection | **PASS** | r(z) decreases 0.300 → 1.000 |
| G | apex tip radius | **PASS** | median 0.0588 (target 0.060 ± 0.010) |
| 4–10 | lookdev | **HOLD** | MATERIAL camera. Cycles `write_still` next. |
| 11–18 | sequences / match | **N/A** | blocked on lookdev still |

## Silhouette

Fat lower bulb, short 0.06 cap, no needle, no S-curve neck. Screw 32, no Subsurf 3 yet.

## Next

A5: Cycles 16 spp `write_still` (do not use RENDERED viewport). Then A6 checks 4–10 on pixels.
A8 remains blocked.
