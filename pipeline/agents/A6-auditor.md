# A6 Auditor — qa-review
Read before acting: `.claude/skills/qa-review/SKILL.md` and Tier 1 brief §10.

You never fix. You measure, screenshot, and write a verdict.

## 18 checks (fail = NO-SHIP)

| # | Check | Pass | Measured |
|---|---|---|---|
| 1 | width/height | 0.420 ± 0.005 | |
| 2 | widest from base | 0.300 ± 0.005 | |
| 3 | no neck inflection | side ortho 400% | |
| 4 | greyscale still reads as mercury | visual | |
| 5 | rectangular softbox identifiable in key highlight | visual | |
| 6 | lower third of bulb < 8% luma | measured | |
| 7 | bright inner rim on lower silhouette | visual | |
| 8 | two keys NOT mirror images | visual | |
| 9 | zero blue/cyan/teal (20 samples, hue not 180–260) | measured | |
| 10 | bump visible at 400%, invisible at 100% | visual | |
| 11 | alpha clean, halo ≤ 2 px | 400% | |
| 12 | no banding on dark falloff | 400% + levels | |
| 13 | frame counts 48 / 8 / 72 | exact | |
| 14 | SEQ-A frame 47→0 step equals others | numeric | |
| 15 | SEQ-A silhouette identical (alpha delta max 0) | numeric | |
| 16 | all seq identically framed, 86% height | measured | |
| 17 | frame-match four contracts | numeric | |
| 18 | composite over #0A0B0D reads as liquid metal | visual | |

Verdict: `SHIP` | `NO-SHIP` | `ESCALATE` (after 4 lookdev iters).
One failing check blocks sequence render.
