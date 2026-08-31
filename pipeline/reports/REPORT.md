# TIER 1 RENDER REPORT
Date: 2026-08-31 | Blender 5.2.1 LTS | Brief **v1.2**

## Production verdict

**Lookdev / wiki preview: YES.** Check 6 SHIP. Sequences exist and loop.

**Brief PNG16 masters / award plates: NO.** Frames are 8-bit 128 spp at 100% res, not 512 spp / 16-bit / 200% then downscale.

## 1. Audit
Check 6 median **0.0359**. Check 15 max α Δ = **0**. Frame-match 7.13% / 50.0 / 41.20. spec-only-a.png written.

## 8. Why beauty is not done
512 spp × 200% × 129 frames on this GPU previously OOM'd and MCP-timed out. Lookdev 128 spp was the authorised GREEN path to get sequences on disk first.
