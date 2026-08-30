# A1 Modeler — blender-modeler + procedural-modeling

Read before acting:
- `.claude/skills/blender-modeler/SKILL.md`
- `.claude/skills/procedural-modeling/SKILL.md`
- `docs/02-AGENT-BRIEF-TIER1-BLENDER.md` §2
- `pipeline/blender/01_build_profile.py`

## Build

Bézier profile `CRV_MercProfile` → Screw 32 → (later) Subsurf 3 → Shade Smooth →
`SM_MercuryDroplet`. Method B (metaballs) is fallback only.

Contracts (height = 1.000 BU):

| Feature | Value | Tol |
|---|---|---|
| Total height | 1.000 | — |
| Max width | 0.420 | ±0.005 |
| Widest from base | 0.300 | ±0.005 |
| Apex tip radius | 0.060 | ±0.010 |
| Bulb radius | 0.300 | ±0.005 |
| Profile | C², no inflection apex→bulb | hard |
| Base | rounded, min R 0.28 at pole | hard |

No UV-sphere + proportional edit.

## MCP split (mandatory)

1. Write / update Bézier points only.
2. Screw modifier only.
3. Convert evaluated mesh onto `SM_MercuryDroplet` (copy materials, shade smooth).
4. Measure bbox + r(z) samples. Never combine 3+4 with Subsurf.

Subsurf 3 is its own call, and only after silhouette SHIP.

## Handoff

`geo-profile-check.png` (ortho side, measurements). A6 runs checks 1–3.
One profile handle per A7 refine if A6 fails geometry.
