# Agents

All agent prompts are English. User-facing summaries are Traditional Chinese (HK).

Skills they must open before acting live in `/workspace/.claude/skills/`
(94 from [arjun988/blender-skills](https://github.com/arjun988/blender-skills),
also vendored at `vendor/blender-skills` and symlinked as `pipeline/blender-skills`).

| ID | File | Skills | May write pixels? | May commit? |
|---|---|---|---|---|
| A0 | [A0-director.md](A0-director.md) | `blender-director` | no | no |
| A1 | [A1-modeler.md](A1-modeler.md) | `blender-modeler`, `procedural-modeling` | yes (geo) | no |
| A2 | [A2-shade.md](A2-shade.md) | `materials`, `realistic-style`, `lookdev` | yes (shader) | no |
| A3 | [A3-light.md](A3-light.md) | `lighting`, `lookdev` | yes (lights/world) | no |
| A4 | [A4-camera.md](A4-camera.md) | `camera-cinematography` | yes (cam) | no |
| A5 | [A5-renderer.md](A5-renderer.md) | `rendering`, `compositing` | yes (frames) | no |
| A6 | [A6-auditor.md](A6-auditor.md) | `qa-review` | **never** | no |
| A7 | [A7-refiner.md](A7-refiner.md) | skill of the failing check | yes, **one variable** | no |
| A8 | [A8-sequence.md](A8-sequence.md) | `animation`, `rendering` | yes after SHIP | no |
| A9 | [A9-release.md](A9-release.md) | `export-pipeline`, `qa-review` | no | **yes** |

Loop: A1–A5 BUILD → A6 AUDIT → A7 REFINE (max 4 on the still) → A6 again.
A8 is gated on A6 SHIP. A9 commits only SHIP artifacts plus reports of NO-SHIP.

Hard MCP rule: never combine Subsurf-convert + measure + render in one
`execute_blender_code` call. It timed out once and reset the scene.

Log: `../LOOP.md`.
