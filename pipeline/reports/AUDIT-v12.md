# AUDIT — brief v1.2 lookdev still (128 spp)

**Still:** `lookdev-v12-key400.png` 500×700 / 128 spp
**Composite:** `#0A0B0D` · rim band 10.08 px

## Ground (one variable, ADR-015)

Principled → Diffuse BSDF `#050506` roughness 1.0, 40×40, camera OFF, glossy ON.

| Lighting | Median | Mean | p90 | Occupancy | Verdict |
|---|---|---|---|---|---|
| KEY-L 300 W / 38° | 0.0319 | 0.0337 | 0.0476 | 0.8629 | SHIP |
| KEY-L 400 W / 30° (restored) | **0.0359** | 0.0370 | 0.0518 | 0.8629 | **SHIP** |

Lookdev still **SHIP**. SEQ-A 48/48 rendered.
