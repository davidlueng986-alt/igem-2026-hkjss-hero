# DEPTH — iGEM 2026 HKJSS mercury hero

Cinematic wiki hero: one mercury droplet, observed, measured, released. Scroll is a **depth gauge** from `0.00 m` to `−1.85 m`.

**Repo:** [davidlueng986-alt/igem-2026-hkjss-hero](https://github.com/davidlueng986-alt/igem-2026-hkjss-hero)

## Status (2026-08-30)

| Gate | State |
|---|---|
| MCP Blender 5.2.1 LTS + OPTIX RTX 5060 | live (addon 1.5, protocol 4) |
| MCP GitHub | live |
| 94 blender-skills | installed (`.claude/skills/`) |
| Workflow | 10 agents, BUILD → AUDIT → DIFF → REFINE |
| Geometry (checks 1–3 + tip) | **SHIP** — width 0.4200, widest z 0.3000, tip R 0.0588 |
| Lookdev still | **NO-SHIP** — lower-third luma 0.136 vs < 0.08 |
| Sequences 48/8/72 | blocked until A6 SHIP |

Working `.blend`: `Downloads/igem-hero-tier1/mercury-hero.blend`

## Authority

1. `docs/00-HERO-DESIGN-SPEC.md` — every number is a contract
2. `docs/02-AGENT-BRIEF-TIER1-BLENDER.md` — Tier 1 execution
3. `pipeline/WORKFLOW.md` — multi-agent loop
4. `pipeline/agents/` — A0–A9 briefs (English). User-facing summaries: Traditional Chinese (HK)
5. [arjun988/blender-skills](https://github.com/arjun988/blender-skills) — 94 skills (AgX / roughness defaults **overridden** by the spec)

## Loop

```
BUILD (MCP) → AUDIT (qa-review, 18 checks) → DIFF vs spec → REFINE one variable
```

Cap: 4 lookdev iterations on SEQ-A frame 0. A0 never models. A6 never fixes. A7 never changes two knobs. A8 never starts before A6 ships the still.

## Install skills

```bash
git clone --depth 1 https://github.com/arjun988/blender-skills.git vendor/blender-skills
cp -a vendor/blender-skills/.claude/skills/. .claude/skills/
```

## HDRI

`studio_small_08` from Poly Haven, **CC0**. https://polyhaven.com/a/studio_small_08
