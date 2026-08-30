# TIER 1 RENDER REPORT
Date: 2026-08-30 | Blender 5.2.1 LTS | Device: OPTIX · RTX 5060 Laptop (CPU fallback after OOM) | Lookdev only
Brief: **v1.1** (`docs/02-AGENT-BRIEF-TIER1-BLENDER.md`)

## 0. MCP + skills
- Blender MCP: live (addon 1.5, protocol 4). GPU OOM once during 400×560; recovered.
- GitHub MCP: https://github.com/davidlueng986-alt/igem-2026-hkjss-hero
- blender-skills: 94 at `.claude/skills/` from https://github.com/arjun988/blender-skills
- Workflow: `pipeline/WORKFLOW.md` · agents A0–A9
- Check 6 helper: `pipeline/blender/measure_check6.py`

## 1. Audit results

| # | Check | Result | Measured |
|---|---|---|---|
| 1 | width/height | **PASS** | 0.4200 |
| 2 | widest from base | **PASS** | 0.3000 |
| 3 | no neck inflection | **PASS** | monotonic r(z) after 0.30 |
| G | apex tip radius | **PASS** | 0.0588 |
| 4 | greyscale mercury | **HOLD** | hard strips present; 8 spp noisy |
| 5 | softbox rectangle | **HOLD** | two strips; recheck at 512 spp |
| 6 | lower third median < 0.08 | **FAIL** | Last: **median 0.3888**, mean 0.4475, band 4.08 px, composite `#0A0B0D` |
| 7 | grazing rim | **HOLD** | left-lower rim; excluded from check 6 |
| 8 | keys not mirrored | **PASS** | L high / R warm low |
| 9–10 | hue / bump | **HOLD** | 8 spp not diagnostic |
| 16 | 86% framing | **PASS** | occupancy 0.8607 |
| 11–15, 17 | sequences / match | **N/A** | blocked |
| 18 | composite over #0A0B0D | **FAIL** | metal read, foot still mid-grey |

**Verdict: ESCALATE.** Geometry SHIP. Ladder §4.2.1 exhausted. Sequences blocked.

## 2. Iteration log

Which rung resolved check 6? **None.**

| Iter | Variable | From → To | Effect | Kept? |
|---|---|---|---|---|
| 0–4 | Bézier handles | — | geo SHIP 0.420 / 0.300 / 0.0588 | yes |
| 4c | ground Specular IOR | 0.5 → 0.0 | unauthorised. Void under v1.1 | **no** |
| 5 | HDRI Z | 0° → 7° | no luma gain | **no** |
| **Rung 1** | restore ground §4.3 | rough 1.0→0.65, spec 0→0.5, 40×40, cam off, glossy on | median **0.4205** mean 0.4845 band **8.08 px** | yes (specified) |
| **Rung 2** | KEY-L elevation | 30° → 38°, 400 W | median **0.4067** mean 0.4629 band **4.08 px** | yes |
| **Rung 3** | KEY-L power | 400 → **300 W**, el 38° | median **0.3888** mean 0.4475 band **4.08 px** | yes (floor) |

All check 6 numbers: median sRGB luma, composited over `#0A0B0D`, outer 4% silhouette width excluded each side.

KEY-L 400→300 moved median only −0.018. Remaining ~0.39 is not KEY-L.

## 3. Deviations from brief
- Screw 32, **no Subsurf 3** — MCP timed out once on convert.
- HDRI `studio_small_08` **2k** not 4k — lookdev.
- Stills 8–16 spp 200×280 / 400×560 for measurement. Beauty 512 spp 16-bit after SHIP.
- Camera vertical sensor 16.47 mm to hit 86% at 85 mm / 6.0 BU.
- Rung 2/3 stills on CPU after GPU OOM.

## 4. Conflicts found
- Pre-v1.1 mean-on-straight-alpha (0.136) contradicted check 7's rim. v1.1 method is now used.
- Even at KEY-L 300 W / 38°, median is 5× the threshold. Further dimming is forbidden.
- Ground roughness 0.65 + Specular IOR 0.5 does not fully occlude a bright studio cyc.

## 5. Match-cut contract — measured
Not built. Blocked on lookdev SHIP.

## 6. Asset inventory
| Path | Notes |
|---|---|
| `Downloads/igem-hero-tier1/mercury-hero.blend` | KEY-L 300 W / el 38° |
| `lookdev-rung1.png` | 400×560 16 spp |
| `lookdev-rung2.png` / `rung3.png` | 200×280 8 spp |
| sequences | 0 / 48+8+72 |

## 7. HDRI & licence
`studio_small_08` 2k, Poly Haven, **CC0**. https://polyhaven.com/a/studio_small_08

## 8. Known issues
1. Check 6 median 0.3888 vs < 0.08 after full ladder.
2. Do not start 48/72-frame sequences.
3. Do not drop KEY-L below 300 W.
