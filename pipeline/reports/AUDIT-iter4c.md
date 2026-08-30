# AUDIT — lookdev lighting 4c
**Auditor:** A6 (`qa-review`)
**Date:** 2026-08-30
**Variable:** MAT_Ground_Absorber Specular IOR Level 0.5 → **0.0** (one knob).
**Verdict:** **NO-SHIP** (check 6 still open, but the lever is proven)

## Measured (Cycles 8 spp 200×280)

| | mean | p50 | p90 |
|---|---|---|---|
| lower-third luma **before** (spec 0.5) | 0.468 | 0.399 | 0.825 |
| lower-third luma **after** (spec 0.0) | **0.136** | 0.104 | 0.207 |
| target | **< 0.08** | — | — |

Ground XY scale 8→40 did nothing (0.473 → 0.468). Specular kill dropped luma by 0.33.

Remaining 0.136 is likely KEY/HDRI in the south-pole reflection, not the ground spec. Next one-variable (do not touch spec or scale again): KEY-L power, **or** HDRI strength 1.20 → 1.00. Cap after that.

Geometry still PASS. Occupancy 86.07%. Sequences blocked.

Deviation: spec does not set ground Specular. 0.0 is a lookdev choice, logged.
