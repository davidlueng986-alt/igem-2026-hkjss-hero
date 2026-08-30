# A8 Sequence TD — animation + rendering

Read before acting:
- `.claude/skills/animation/SKILL.md`
- `.claude/skills/rendering/SKILL.md`
- Brief §6

**Hard gate:** A6 SHIP on the lookdev still. If the still is NO-SHIP you do not exist.

## SEQ-A — idle 48f

1000×1400 (render 200% → 2000×2800, downscale). HDRI Z ping-pong 0° → 7° → 0°.
Sine in-out. Frame 0 = 0°, 24 = 7°, 47 = 0.29°. Droplet and camera locked.
Silhouette byte-identical across 48 frames (alpha delta max 0).

## SEQ-B — scan

Still 1200×1680 at HDRI 3.5°. Micro-loop 8f ping-pong 3.0° → 4.0° → 3.0°, sine.

## SEQ-C — descent 72f

800×1120 (render 200%). HDRI Z 0° → 22° linear. Droplet Z 0° → 9°.
No squash. Constant scale in frame.

## FRAME-MATCH

1920×1080, opaque `#050506`, Film Transparent OFF.
Droplet height 7.2% ±0.1. Apex 50.0% / 41.2% ±0.2. Tilt 0. Specular 11 o'clock.

## Passes

matte-a, spec-only-a, silhouette.svg, contact-sheet, REF-000.
