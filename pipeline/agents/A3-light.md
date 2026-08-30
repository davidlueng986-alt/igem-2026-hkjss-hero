# A3 Lookdev light — lighting + lookdev

Read before acting:
- `.claude/skills/lighting/SKILL.md`
- `.claude/skills/lookdev/SKILL.md`
- Brief §4

## World

PolyHaven `studio_small_08` (CC0). Strength **1.20**. Mapping node, Z-rot animatable.
Camera rays see `#0A0B0D`; glossy rays see the HDRI (Light Path mix).
Film Transparent ON.

## Keys (do not symmetrise)

| Light | Type | Size | Pose | Power | Colour |
|---|---|---|---|---|---|
| LGT_Key_L | Area Rect | 0.15 × 2.20 | az −55°, el 30°, d 3.0 | 400 W | `#FFFFFF` |
| LGT_Key_R | Area Rect | 0.15 × 2.20 | az +62°, el 18°, d 3.2 | 260 W | `#FFF6EC` |
| LGT_Rim | Area Disc | 0.80 | az 168°, el 12°, d 2.4 | 150 W | `#FFFFFF` |

MIS ON. Shadow caustics OFF. Rim is behind-low so the grazing rim sits on the lower silhouette.

## Ground

`SM_Ground` at z = −0.002. Principled `#0A0B0D`, Roughness 0.65, Metallic 0.
Camera ray OFF, glossy ON. This is what makes the lower bulb go near-black.
Lookdev 4c: Specular IOR Level 0.0 (logged deviation) — dropped lower-third luma 0.47 → 0.136.

## Gate

A6 checks 5–8. One light knob per A7 refine.
