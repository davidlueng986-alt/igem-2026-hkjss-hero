# A2 Lookdev shade — materials + realistic-style + lookdev

Read before acting:
- `.claude/skills/materials/SKILL.md`
- `.claude/skills/realistic-style/SKILL.md`
- `.claude/skills/lookdev/SKILL.md`
- Brief §3

## MAT_Mercury_Liquid (Principled, one group)

| Input | Value |
|---|---|
| Base Color | `#E4E6E8` linear `0.7913, 0.8069, 0.8227` |
| Metallic | 1.000 |
| Roughness | **0.030** (not 0, not skill-default 0.1–0.3) |
| Coat / Aniso / Emission / SSS / Transmission / Sheen | 0 |

Micro-bump (required):

```
Noise Scale 14 / Detail 4 / Roughness 0.5
  → Bump Strength 0.020 Distance 0.010
    → Principled Normal
```

Strength ceiling 0.020. Above 0.04 reads as hammered metal.

## Forbidden

Blue / cyan / teal anywhere. Any texture map other than the Noise bump.

## Gate

Do not change lighting. If clay silhouette is wrong, bounce to A1. A6 checks 9–10.
