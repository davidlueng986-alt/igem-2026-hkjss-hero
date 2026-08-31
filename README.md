# DEPTH — iGEM 2026 HKJSS mercury hero

**Repo:** [davidlueng986-alt/igem-2026-hkjss-hero](https://github.com/davidlueng986-alt/igem-2026-hkjss-hero)

## Status (2026-08-30)

| Gate | State |
|---|---|
| Brief | **v1.2** |
| Geometry | **SHIP** 0.420 / 0.300 / tip 0.0588 · Screw 128 |
| Check 6 | **SHIP** median **0.0359** (128 spp, composite `#0A0B0D`, band 10.08 px) |
| Lookdev still | **SHIP** — Diffuse BSDF ground (ADR-015) + KEY-L 400 W / 30° |
| SEQ-A | **48/48** `a-000`…`a-047` 1000×1400 128 spp |
| SEQ-B / C / match | pending MCP restart |

Root cause of the 0.39 median: Principled dielectric Fresnel at grazing on the ground plane. Diffuse BSDF dropped it to 0.036.
