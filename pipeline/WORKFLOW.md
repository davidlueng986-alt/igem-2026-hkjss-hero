# Multi-agent multi-stage workflow
# iGEM 2026 HKJSS · Mercury Hero · Tier 1
# Language: English (agents). User-facing summaries: Traditional Chinese (HK).

Authority: `docs/00-HERO-DESIGN-SPEC.md` > this file > blender-skills.
Skills root: `.claude/skills/` (94 skills from https://github.com/arjun988/blender-skills).
MCP: Blender MCP (`execute_blender_code`, `get_viewport_screenshot`, `get_scene_info`, PolyHaven).
Git: `davidlueng986-alt/igem-2026-hkjss-hero`.

---

## Loop (non-negotiable)

```
        ┌──────────────────────────────────────────────┐
        │                                              │
   ┌────▼─────┐   ┌────────┐   ┌────────┐   ┌──────────┐
   │  BUILD   │──▶│ AUDIT  │──▶│  DIFF  │──▶│  REFINE    │
   │  (MCP)   │   │ qa-rev │   │vs spec │   │ ONE THING  │
   └──────────┘   └────────┬───┘   └────────┘   └──────────┘
                       │ all PASS
                       ▼
                   ┌────────┐
                   │ COMMIT │  git + GitHub MCP
                   └────────┘
```

Rules
1. Screenshot after every BUILD that changes pixels.
2. AUDIT writes measured values, not impressions. Fail = no commit of beauty frames.
3. REFINE changes **one variable**. If two change, the loop is invalid.
4. Lookdev cap: **4 iterations** on SEQ-A frame 0. Escalate with REPORT.md; do not grind.
5. Sequences render only after the single frame passes all 18 checks.
6. Spec numbers are contracts. If Blender disagrees, Blender is wrong.

---

## Agents

| ID | Agent | Skills it MUST read before acting | Writes | MCP |
|---|---|---|---|---|
| A0 | **Director** | `blender-director`, `references/asset-pipeline.md` | PRODUCTION-BRIEF, stage gate | scene info |
| A1 | **Modeler** | `blender-modeler`, `procedural-modeling` | SM_MercuryDroplet, geo-profile-check | execute + screenshot |
| A2 | **Lookdev shade** | `materials`, `realistic-style`, `lookdev` | MAT_Mercury_Liquid | execute |
| A3 | **Lookdev light** | `lighting`, `lookdev` | LGT_*, World HDRI | execute + PolyHaven |
| A4 | **Camera** | `camera-cinematography` | CAM_Hero_SeqA, EMPTY_CamTarget_Hero | execute |
| A5 | **Renderer** | `rendering`, `compositing` | PNG16 frames, AOVs | execute (keep calls tiny) |
| A6 | **Auditor** | `qa-review` + brief §10 (18 checks) | AUDIT.md, verdict ship/no-ship | screenshot + measure |
| A7 | **Refiner** | same skill as the failing check | one-variable patch + iteration log | execute |
| A8 | **Sequence TD** | `animation`, `rendering` | SEQ-A 48 / SEQ-B 8 / SEQ-C 72 / match | execute |
| A9 | **Release** | `export-pipeline`, `qa-review` | REPORT.md, GitHub commit | GitHub MCP |

A0 never models. A6 never fixes. A7 never changes two knobs. A8 never starts before A6 ships the still.

---

## Stages

### S0 — Connect & install
- Ping Blender MCP + GitHub MCP.
- Install blender-skills into `.claude/skills/`.
- Create GitHub repo if missing.
- Gate: addon up-to-date, GPU visible.

### S1 — Scene bootstrap (A0)
- OPTIX GPU, collections `COL_*`, PolyHaven on.
- Download `studio_small_08` HDRI (CC0). Strength 1.20. Mapping node for Z-rot.
- Film Transparent ON. View Transform **Standard**. Exposure **−0.20**.
- Gate: world has Environment Texture; cycles.device = GPU.

### S2 — Geometry (A1 → A6)
Build Bézier profile (height 1.000, width 0.420, widest at 0.300 from base, tip r 0.060, C², no neck inflection). Screw 32, Subsurf 3, Shade Smooth.
Audit checks 1–3. Screenshot: ortho side + matcap.
Refine: move **one** profile handle.

### S3 — Material (A2 → A6)
Principled: Base `#E4E6E8` linear, Metallic 1, Roughness 0.030, Coat 0, Aniso 0.
Noise 14 / 4 / 0.5 → Bump 0.020 / 0.010.
Audit checks 9–10 (hue, micro-bump). **Do not light yet** if clay silhouette is wrong — bounce to S2.

### S4 — Lighting + ground (A3 → A6)
Ground plane z = −0.002, `#0A0B0D`, Roughness 0.65, camera-invisible, glossy-visible.
KEY-L / KEY-R / RIM per brief §4.2. Do not symmetrise.
Audit checks 5–8 (softbox shape, lower-third <8% luma, rim, asymmetry).

### S5 — Camera (A4)
85 mm, 6.0 BU, dead level, DOF off, droplet 86% frame height, centred.
Shot is locked-off product, not cinematic move.

### S6 — Lookdev still (A5 → A6 → A7)  **the expensive gate**
Render SEQ-A frame 0 only.
Samples: preview 64, then 512 when lighting is close.
Auditor runs all 18 checks. Refiner: one variable, max 4 loops.
Composite over `#0A0B0D`. Greyscale test.

### S7 — Sequences (A8)  only after S6 ship
- SEQ-A 48f idle HDRI ping-pong 0→7→0, sine in-out, 1000×1400 (render 200%)
- SEQ-B still + 8f micro-loop 1200×1680
- SEQ-C 72f HDRI 0→22 linear + droplet Z 0→9, 800×1120
- FRAME-MATCH 1920×1080 opaque `#050506`, 7.2% height, apex 50.0 / 41.2

### S8 — Passes + report (A8, A9)
matte-a, spec-only-a, silhouette.svg, contact-sheet, REF-000, packed .blend, REPORT.md.

### S9 — Git (A9)
Commit stills, scripts, reports, workflow. Push `main`.
Do not commit 4.8 MB of AVIF until compression script has run.

---

## MCP execution rules (from blender-director)

1. Check MCP before Phase 1.
2. Query scene after every phase.
3. Never describe UI clicks when MCP can execute.
4. **Keep `execute_blender_code` small.** Subsurf-convert + measure in the same call timed out once. Split: create → modifier → convert → measure.
5. Viewport screenshot after any pixel change.
6. Naming: `SM_`, `MAT_`, `LGT_`, `CAM_`, `EMPTY_`, `COL_`.

---

## Quality bar (ship)

A6 must mark **SHIP** on:
- Geometry contracts within tolerance
- Greyscale mercury read
- Identifiable rectangular softbox in the key highlight
- Lower third of bulb < 8% luminance
- Bright inner rim
- Asymmetric keys
- Zero blue (20-point hue sample)
- Alpha clean
- Match-cut four values (when S7 done)

Anything else is NO-SHIP. Motion cannot rescue a bad still (spec §10 S2).
