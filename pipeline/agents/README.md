# Agents

All agent prompts are English. User-facing summaries are Traditional Chinese (HK).

Skills they must open before acting live in `.claude/skills/` (94 from https://github.com/arjun988/blender-skills).

| ID | Role | Skills | May write pixels? | May commit? |
|---|---|---|---|---|
| A0 | Director | blender-director | no | no |
| A1 | Modeler | blender-modeler, procedural-modeling | yes (geo) | no |
| A2 | Shade | materials, realistic-style | yes (shader) | no |
| A3 | Light | lighting | yes (lights/world) | no |
| A4 | Camera | camera-cinematography | yes (cam) | no |
| A5 | Renderer | rendering, compositing | yes (frames) | no |
| A6 | Auditor | qa-review | **never** | no |
| A7 | Refiner | skill of the failing check | yes, **one variable** | no |
| A8 | Sequence TD | animation, rendering | yes after SHIP | no |
| A9 | Release | export-pipeline | no | **yes** |

Loop: A1–A5 BUILD → A6 AUDIT → A7 REFINE (max 4 on the still) → A6 again. A8 is gated on A6 SHIP.

Hard MCP rule: never combine Subsurf-convert + measure + render in one execute_blender_code call.
