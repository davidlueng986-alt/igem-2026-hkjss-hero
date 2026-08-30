# AUDIT iter 5 — lookdev still (HDRI Z-rot)

**Agent:** A7 one-variable → A6 measure  
**Variable:** World Mapping Rotation Z `0° → 7°` (brief SEQ-A range). Strength, keys, ground untouched.  
**Still:** `lookdev-iter5.png` 200×280, 8 spp, film transparent.

| Check | Target | Measured | Result |
|---|---|---|---|
| 1 width/height | 0.420 ± 0.005 | 0.4200 | PASS (unchanged) |
| 2 widest from base | 0.300 ± 0.005 | 0.3000 | PASS |
| 6 lower-third luma | < 0.08 | **mean 0.1373** (p50 0.105, p90 0.204) | **FAIL** |
| 16 occupancy | 86% | 86.07% | PASS |

Delta vs iter 4c luma 0.136: **+0.001, no improvement.**

**Kept?** No. Reverted Mapping Z to `0.0`. Scene saved.

**Hue sample on 8 spp PNG is not diagnostic** (97% of weakly-chromatic pixels fell 180–260 because denoiser noise on a near-black field). Recheck at 512 spp / 16-bit.

Verdict: **NO-SHIP**. Lookdev lighting cap remaining: 1 (this was lighting iter 3 of 4 if 4b/4c count). Next allowed variable: KEY-L energy, *or* escalate because KEY-L 400 W is a brief contract.
