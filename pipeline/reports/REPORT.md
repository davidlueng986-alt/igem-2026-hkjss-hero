# TIER 1 RENDER REPORT
Date: 2026-08-30 | Blender 5.2.1 LTS | Device: OPTIX RTX 5060 Laptop | lookdev only

## Verdict: NO-SHIP

Loop continues at refine 1 (apex radius + widest-z). Do not start sequences.

| # | Check | Result | Measured |
|---|-------|--------|----------|
| 1 | width/height | PASS | 0.4224 |
| 2 | widest from base | FAIL | 0.377 vs 0.300 |
| 3 | no neck inflection | PASS | monotonic r(z) |
| 5 | softbox rectangle | PASS | two hard strips |
| 8 | keys not mirrored | PASS | L 400 W / R 260 W |
| 13-17 | sequences / match | N/A | blocked |

HDRI: studio_small_08 2k, Poly Haven, CC0. https://polyhaven.com/a/studio_small_08
View transform: Standard (spec), not AgX.
Working blend: Downloads/igem-hero-tier1/mercury-hero.blend
