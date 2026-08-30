# DEPTH — iGEM 2026 HKJSS mercury hero

Cinematic wiki hero: one mercury droplet, observed, measured, released. Scroll is a **depth gauge** from `0.00 m` to `−1.85 m`.

**Repo:** [davidlueng986-alt/igem-2026-hkjss-hero](https://github.com/davidlueng986-alt/igem-2026-hkjss-hero)

## Status (2026-08-30)

| Gate | State |
|---|---|
| MCP Blender 5.2.1 LTS + OPTIX RTX 5060 | live (addon 1.5, protocol 4) |
| MCP GitHub | live |
| 94 blender-skills | installed (`.claude/skills/` from [arjun988/blender-skills](https://github.com/arjun988/blender-skills)) |
| Brief | **v1.1** — check 6 method + §4.2.1 ladder |
| Geometry (checks 1–3 + tip) | **SHIP** — width 0.4200, widest z 0.3000, tip R 0.0588 |
| Lookdev still | **ESCALATE** — check 6 median 0.3888 after rungs 1–3 |
| Sequences 48/8/72 | blocked |

Working `.blend`: `Downloads/igem-hero-tier1/mercury-hero.blend` (KEY-L 300 W / el 38°)

## Check 6 ladder (v1.1)

| Rung | Action | Median | Mean | Band px |
|---|---|---|---|---|
| 1 | restore ground §4.3 | 0.4205 | 0.4845 | 8.08 |
| 2 | KEY-L el 30°→38°, 400 W | 0.4067 | 0.4629 | 4.08 |
| 3 | KEY-L 300 W, el 38° | **0.3888** | 0.4475 | 4.08 |

Threshold: median < 0.08, composite `#0A0B0D`, exclude 4% rim. None passed. Do not dim below 300 W.

## Authority

1. `docs/00-HERO-DESIGN-SPEC.md` — every number is a contract
2. `docs/02-AGENT-BRIEF-TIER1-BLENDER.md` — Tier 1 execution **v1.1**
3. `pipeline/WORKFLOW.md` — multi-agent loop
4. `pipeline/agents/` — A0–A9 briefs (English). User-facing summaries: Traditional Chinese (HK)
5. [arjun988/blender-skills](https://github.com/arjun988/blender-skills) — 94 skills (AgX / roughness defaults **overridden** by the spec)
