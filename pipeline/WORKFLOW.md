# Multi-agent multi-stage workflow
# iGEM 2026 HKJSS · Mercury Hero · Tier 1
# Language: English (agents). User-facing summaries: Traditional Chinese (HK).

Authority: `docs/00-HERO-DESIGN-SPEC.md` > this file > blender-skills.
Skills root: `.claude/skills/` (94 skills from https://github.com/arjun988/blender-skills).
MCP: Blender MCP (`execute_blender_code`, `get_viewport_screenshot`, `get_scene_info`, PolyHaven).
Git: `davidlueng986-alt/igem-2026-hkjss-hero`.

## Loop (non-negotiable)

BUILD (MCP) → AUDIT (qa-review) → DIFF vs spec → REFINE ONE THING → AUDIT
SHIP → COMMIT

Rules
1. Screenshot after every BUILD that changes pixels.
2. AUDIT writes measured values, not impressions. Fail = no commit of beauty frames.
3. REFINE changes **one variable**. If two change, the loop is invalid.
4. Lookdev cap: **4 iterations** on SEQ-A frame 0. Escalate with REPORT.md; do not grind.
5. Sequences render only after the single frame passes all 18 checks.
6. Spec numbers are contracts. If Blender disagrees, Blender is wrong.

## Agents

| ID | Agent | Skills it MUST read before acting | Writes | MCP |
|---|---|---|---|---|
| A0 | **Director** | `blender-director` | PRODUCTION-BRIEF, stage gate | scene info |
| A1 | **Modeler** | `blender-modeler`, `procedural-modeling` | SM_MercuryDroplet | execute + screenshot |
| A2 | **Lookdev shade** | `materials`, `realistic-style`, `lookdev` | MAT_Mercury_Liquid | execute |
| A3 | **Lookdev light** | `lighting`, `lookdev` | LGT_*, World HDRI | execute + PolyHaven |
| A4 | **Camera** | `camera-cinematography` | CAM_Hero_SeqA | execute |
| A5 | **Renderer** | `rendering`, `compositing` | PNG16 frames, AOVs | execute (keep calls tiny) |
| A6 | **Auditor** | `qa-review` + brief §10 (18 checks) | AUDIT.md, verdict | screenshot + measure |
| A7 | **Refiner** | same skill as the failing check | one-variable patch | execute |
| A8 | **Sequence TD** | `animation`, `rendering` | SEQ-A 48 / SEQ-B 8 / SEQ-C 72 / match | execute |
| A9 | **Release** | `export-pipeline`, `qa-review` | REPORT.md, GitHub commit | GitHub MCP |

A0 never models. A6 never fixes. A7 never changes two knobs. A8 never starts before A6 ships the still.

## Stages S0–S9

S0 Connect & install — Ping Blender + GitHub MCP. Install blender-skills.
S1 Scene bootstrap — OPTIX, COL_*, studio_small_08 @ 1.20, Standard / −0.20.
S2 Geometry — height 1.000, width 0.420, widest 0.300, tip r 0.060, C2, no inflection.
S3 Material — Metallic 1, Roughness 0.030, bump 0.020. No blue.
S4 Lighting — KEY-L / KEY-R / RIM, glossy-only ground. Do not symmetrise.
S5 Camera — 85 mm, 6.0 BU, 86% frame height, DOF off.
S6 Lookdev still — ONE frame. Max 4 refine loops.
S7 Sequences — gated on SHIP.
S8 Passes + report.
S9 Git.

## MCP execution rules

Keep `execute_blender_code` small. Subsurf-convert + measure in the same call timed out once.
Naming: SM_, MAT_, LGT_, CAM_, EMPTY_, COL_.
