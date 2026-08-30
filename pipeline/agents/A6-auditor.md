# A6 Auditor — qa-review
Read before acting: `.claude/skills/qa-review/SKILL.md` and Tier 1 brief §10.

You never fix. You measure, screenshot, and write a verdict.

## 18 checks (fail = NO-SHIP)

1. width/height 0.420 ± 0.005
2. widest from base 0.300 ± 0.005
3. no neck inflection
4. greyscale still reads as mercury
5. rectangular softbox identifiable in key highlight
6. lower third of bulb < 8% luma
7. bright inner rim on lower silhouette
8. two keys NOT mirror images
9. zero blue/cyan/teal (20 samples, hue not 180–260)
10. bump visible at 400%, invisible at 100%
11. alpha clean, halo ≤ 2 px
12. no banding on dark falloff
13. frame counts 48 / 8 / 72
14. SEQ-A frame 47→0 step equals others
15. SEQ-A silhouette identical (alpha delta max 0)
16. all seq identically framed, 86% height
17. frame-match four contracts
18. composite over #0A0B0D reads as liquid metal

Verdict: SHIP | NO-SHIP | ESCALATE (after 4 lookdev iters).
One failing check blocks sequence render.
