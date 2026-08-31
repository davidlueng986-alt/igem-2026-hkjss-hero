# TIER 1 RENDER REPORT
Date: 2026-08-30 | Blender 5.2.1 LTS | Brief **v1.2**

## 1. Audit headline

| # | Check | Result | Measured |
|---|---|---|---|
| 1–3 + tip | geometry | **PASS** | 0.420 / 0.300 / 0.0588 |
| 6 | lower third median | **PASS** | **0.0359** mean 0.037 band 10.08 px / 128 spp / `#0A0B0D` |
| 16 | 86% frame | **PASS** | 0.8629 |
| 13 | SEQ-A count | **PASS** | 48 |
| 17 | frame-match | N/A | SEQ-C pending |

**Lookdev: SHIP.** SEQ-A 48/48 on disk. SEQ-B/C next after MCP recovery.

## 2. What fixed check 6

Diffuse BSDF ground (§4.3 v1.2 / ADR-015). Median 0.39 → **0.036**. KEY-L restored to 400 W / 30° (AMBER); still SHIP.

## 3. Deviations
SEQ-A at 1000×1400 128 spp 8-bit, not 2000×2800 512 spp 16-bit. Screw 128 not Subsurf 3.

## 7. HDRI
studio_small_08 4k, Poly Haven, CC0. https://polyhaven.com/a/studio_small_08
