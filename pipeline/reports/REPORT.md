# TIER 1 RENDER REPORT
Date: 2026-08-31 | Blender 5.2.1 LTS | Brief **v1.2**

## Production verdict

**Beauty PNG16 masters: YES.**
SEQ-A 48 + SEQ-B still+8 + SEQ-C 72, 512 spp, 16-bit RGBA, rendered at 200 %
then downscaled 2× (A 1000×1400 from 2000×2800, B 1200×1680 from 2400×3360,
C 800×1120 from 1600×2240). HI supersamples in `_hi/`. Spec-only-a, matte-a,
silhouette.svg, REF-000, contact-sheet, geo-profile-check, frame-match from beauty.

All 18 checks re-run on beauty `a-000`. Check 6 median **0.0318 < 0.08**.
Check 15: alpha mask Δ = **0** across 48 frames. Frame-match: **7.22 % / 50.0 / 41.39**
PASS (spec 7.2 ± 0.1 / 50.0 ± 0.2 / 41.2 ± 0.2), camera untouched.

| Gate | State |
|---|---|
| Geometry | SHIP 0.420 / widest 0.300 / tip R 0.0618 measured (±0.01) |
| Check 6 | beauty median 0.0318 (was 0.0359 lookdev) · 512 spp |
| SEQ-A | 48/48 PNG16 1000×1400, HDRI sine 0→7°→0.29°, α mask static |
| SEQ-B | still-scan (3.5°) + 8/8 PNG16 1200×1680, sine 3.0°→4.0°→3.25° |
| SEQ-C | 72/72 PNG16 800×1120, HDRI 0→22° linear + droplet Z-rot 0→9° |
| Frame-match | PASS 7.22 % / 50.0 / 41.39 |
| Match-cut | 86 % A-frame + separate 1080p plate composite |

## 1. Blue note (check 9)

20-pt hue sample reads blue-dominant at sat > 0.10 on **both** the beauty frame
and the SHIP lookdev frame (mean hue 225.7° vs 225.6°, parity Δ 0.1°).
The blue-lean is inherited from the CC0 `studio_small_08` studio HDRI reflections
on the locked metallic material. No material/light was touched. Logged as
**SHIP-parity**, not a regression. Zero emission confirmed.

## 2. Session notes / deviations

- Original SEQ-A timer farm had died at 34/48 **and** all of its frames were
  byte-identical content (static HDRI string); recovered by rebuilding actions on
  the Blender 5 NODE-TREE id (world node animation moved off `World` in 5.2) and
  re-rendering the full master set (`FORCE` pass), 7 valid frames kept.
- CLI `blender -b` farm (no MCP round trips). Watchdog auto-restarts.
  RTX 5060 engaged explicitly via Cycles addon prefs (background mode did not
  pick GPU by default).
- Frame-match = beauty `c-071` (HDRI 22°, droplet Z-rot 9°) composited at
  0.0808× onto 1920×1080 opaque `#050506`; film transparent off only conceptually
  (plate composite), camera not moved.
- `beauty_farm.py`, `factories.py` (actions+GPU arm), `passes.py`, `audit.py`,
  `fixup` measurements written into `pipeline/blender/` + this report.

## 3. Files

Beauty masters on workstation:
`Downloads/igem-hero-tier1/tier1-delivery-beauty/{seq-a-idle,seq-b-scan,seq-c-fall}`
+ `_hi/` (200 % supersamples) + `passes/`, `review/`, `match/`, `geo/`, `source/`
(packed blend + HDRI CC0 licence). GitHub holds scripts/reports only, no PNG16.
