# Production Brief: Mercury Droplet (Tier 1 Hero)

**Type:** Hero cinematic prop (liquid-metal droplet)
**Target:** Cinematic stills + frame sequences for iGEM wiki canvas playback
**Style:** Photoreal / material-accurate mercury. Skill: `realistic-style`
**Authority:** docs/00-HERO-DESIGN-SPEC.md is normative. Spec wins on conflict.
**Pivot:** Base pole at world origin; optical centre at z = 0.50 BU
**Animation:** HDRI Z-rotation only (SEQ-A/B). No squash (CSS). No camera move.

## Active skills (ordered)

1. blender-director
2. blender-modeler + procedural-modeling
3. materials + realistic-style
4. lighting + lookdev
5. camera-cinematography
6. rendering + compositing (Standard, NOT AgX)
7. animation (after SHIP)
8. qa-review (18 checks)

**Explicitly NOT used:** hard-surface, horror-style, sci-fi-punk-worlds, AgX, emission, WebGL.

## Conflict log (spec vs blender-skills)

| Topic | blender-skills default | Spec contract | Resolution |
|---|---|---|---|
| View transform | AgX | Standard | Spec wins |
| Cycles max bounces | 12 | 16 total, glossy 8 | Spec wins |
| Metal roughness | 0.1–0.3 | 0.030 | Spec wins |
| Colour | unrestricted | Zero blue. Zero --toxic | Spec wins |
