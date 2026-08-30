# TIER 1 RENDER REPORT
Date: 2026-08-30 | Blender 5.2.1 LTS | Device: OPTIX · RTX 5060 Laptop | Lookdev only

## 0. MCP + skills
- Blender MCP: live (addon 1.5, protocol 4). Scene: CRV_MercProfile, SM_MercuryDroplet, LGT_Key_L/R, LGT_Rim, CAM_Hero_SeqA, SM_Ground.
- GitHub MCP: live as `davidlueng986-alt`. Repo: https://github.com/davidlueng986-alt/igem-2026-hkjss-hero
- blender-skills: 94 (+1) skills at `.claude/skills/` from https://github.com/arjun988/blender-skills
- Workflow: `pipeline/WORKFLOW.md` + 10 agent briefs in `pipeline/agents/`
- Active chain: `blender-director` → `blender-modeler` → `materials` → `lighting` → `camera-cinematography` → `lookdev` → `qa-review`

## 1. Audit headline

| # | Check | Result | Measured |
|---|---|---|---|
| 1 | width/height | **PASS** | 0.4200 |
| 2 | widest from base | **PASS** | 0.3000 |
| 3 | no neck inflection | **PASS** | monotonic r(z) after 0.30 |
| G | apex tip radius | **PASS** | 0.0588 (target 0.060 ± 0.010) |
| 4 | greyscale mercury | **PASS** | hard strips on Cycles still |
| 5 | softbox rectangle | **PASS** | two identifiable area-light strips |
| 6 | lower third < 8% luma | **FAIL** | mean **0.136** after ground spec 0. HDRI Z 7° did not help (0.137, reverted). |
| 7 | grazing rim | **PASS** | left-lower rim |
| 8 | keys not mirrored | **PASS** | L 400 W / R 260 W warmer lower |
| 9–10 | hue / bump | **HOLD** | 8 spp noisy; nodes correct. Do not trust hue on 8 spp PNG. |
| 16 | 86% framing | **PASS** | occupancy 86.07% |
| 11–15, 17 | sequences / match | **N/A** | blocked |
| 18 | composite over #0A0B0D | **FAIL** | metal read, foot too bright |

**Verdict: NO-SHIP.** Geometry has shipped. Sequences remain blocked. Next one-variable would be KEY-L energy, but 400 W is a brief contract — escalate.

## 2. Iteration log
| Iter | Variable | From → To | Effect | Kept? |
|---|---|---|---|---|
| 0a | profile | cube → 9-pt screw | candle/flame | no |
| 0b | fatten | mass in lower 0.55 | ratio 0.422; widest 0.377; needle apex | base |
| 0c | world camera mix | HDRI in camera → `#0A0B0D` / HDRI glossy | field near-black | yes |
| 1 | p8 handle | zero-length → 0.552×0.060 | tip 0.035 | yes |
| 2 | p7 onto tip equator | (0.058, 0.910) → (0.060, 0.940) | tip **0.0588 PASS** | yes |
| 3 | p4.handle_left.x | 0.2149 bulge → vertical 0.205 | width **0.4200**; plateau | yes |
| 4 | p3.handle_left + p2.x | hl z 0.23→0.28; p2.x 0.206→0.190 | widest **0.3000 PASS** | yes |
| 4b | ground XY scale | 8×8 → 40×40 | lower luma 0.468 (no) | yes (harmless) |
| 4c | ground Specular IOR | 0.5 → 0.0 | luma 0.47 → **0.136**. Kept. | yes |
| 5 | HDRI Mapping Z | 0° → 7° | luma 0.137. Reverted. | **no** |

## 3. Deviations
- Screw 32, **no Subsurf 3** — converting with subsurf timed out MCP once.
- HDRI 2k not 4k — lookdev.
- Cycles stills at 8 spp 200×280 for measurement only. Beauty is 512 spp 16-bit after SHIP.
- Camera vertical sensor 16.47 mm to honour 86% at 85 mm / 6.0 BU.

## 4. Conflicts (spec wins)
- `rendering` skill AgX vs spec Standard / exposure −0.20.
- Brief bulb radius 0.300 vs max width 0.420: treated as z of bulb, not sphere radius.
- ALIGNED handles on zero-length points explode to 1 BU — always FREE, set, then ALIGNED.
- Check 6 vs KEY-L 400 W: remaining foot light is the keys themselves reflecting in the lower bulb. Cutting KEY-L breaks §4.2. Escalating.

## 5. Match-cut — not built
Blocked on lookdev SHIP.

## 6. Inventory
| Path | Notes |
|---|---|
| `C:\Users\daive\Downloads\igem-hero-tier1\mercury-hero.blend` | packed scene, local |
| `lookdev-iter4.png` / `4b` / `4c` / `5` | 200×280 8 spp Cycles |
| sequences | 0 / 48+8+72 |

## 7. HDRI
`studio_small_08` 2k, Poly Haven, **CC0**. https://polyhaven.com/a/studio_small_08

## 8. Known issues
1. Lower-third luma 0.136 vs < 0.08 — remaining foot is KEY/HDRI, not ground spec, not HDRI Z.
2. Do not start 48/72-frame sequences.
3. RENDERED viewport screenshots return black; use `write_still`.
4. Subsurf 3 still deferred.
5. Hue sampling on 8 spp is invalid; recheck at 512 spp.
