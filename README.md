# DEPTH — iGEM 2026 HKJSS mercury hero

Cinematic wiki hero: one mercury droplet, observed, measured, released. Scroll is a **depth gauge** from `0.00 m` to `−1.85 m`.

**Repo:** [davidlueng986-alt/igem-2026-hkjss-hero](https://github.com/davidlueng986-alt/igem-2026-hkjss-hero)

## Status (2026-08-30)

| Gate | State |
|---|---|
| MCP Blender 5.2.1 LTS + OPTIX | live |
| MCP GitHub | live |
| 94 blender-skills installed | live |
| Lookdev iter 0 | **NO-SHIP** (apex needle, widest 0.377 vs 0.300) |
| Sequences 48/8/72 | blocked until SHIP |

Working `.blend` on the artist's machine: `Downloads/igem-hero-tier1/mercury-hero.blend`

## Authority

1. `docs/00-HERO-DESIGN-SPEC.md` — every number is a contract
2. `docs/02-AGENT-BRIEF-TIER1-BLENDER.md` — Tier 1 execution
3. `pipeline/WORKFLOW.md` — multi-agent loop
4. [arjun988/blender-skills](https://github.com/arjun988/blender-skills) — 94 specialist skills (AgX / roughness defaults **overridden** by the spec)

## Agents

See `pipeline/agents/README.md`. English in the loop. Traditional Chinese (HK) for the human.

```
BUILD (MCP) → AUDIT (qa-review, 18 checks) → DIFF vs spec → REFINE one variable
```

Cap: 4 lookdev iterations on SEQ-A frame 0. Do not render 128 frames of a wrong look.

## Install skills

```bash
git clone --depth 1 https://github.com/arjun988/blender-skills.git vendor/blender-skills
cp -a vendor/blender-skills/.claude/skills/. .claude/skills/
```

## HDRI

`studio_small_08` from Poly Haven, **CC0**. https://polyhaven.com/a/studio_small_08
