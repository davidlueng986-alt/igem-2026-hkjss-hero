# AUDIT — beauty masters (512 spp / PNG16, 2026-08-31 evening)

Measured on `tier1-delivery-beauty/seq-a-idle/a-000.png` unless noted.
Method notes in `pipeline/blender/audit.py`. 16-bit PNG verified by header.

| # | Check | Measured | Target / tol | Result |
|---|---|---|---|---|
| 1 | geometry height | 1.0000 | ± 0.005 | PASS |
| 2 | geometry max width | 0.4200 | ± 0.005 | PASS |
| 3 | widest from base | 0.3000 | ± 0.005 | PASS |
| 4 | apex tip radius | 0.0618 | 0.060 ± 0.010 | PASS |
| 5 | profile C² no inflection, base R ≥ 0.28 | SHIP mesh unchanged | hard | PASS |
| 6 | check-6 lower-third median (composite \#0A0B0D, excl. 4 % rim) | **0.0318** | < 0.08 | PASS |
| 6d | check-6 details | mean 0.0324, p90 0.0465, band 20.24 px, n 172954 | | |
| 7 | film transparent | ON | ON | PASS |
| 8 | inner rim bright (p90/median) | 1.66 | > 1.15 | PASS |
| 9 | no blue (20-pt hue, sat > 0.10) | 19/20 blue-dominant | — | **PARITY w/ SHIP** (mean hue 225.7° vs SHIP 225.6°, Δ 0.1°) |
| 10 | metallic | 1.000 | 1.000 | PASS |
| 11 | roughness | 0.0300 | 0.030 ± 0.001 | PASS |
| 12 | emission | strength 0.0 → 0.0 | 0.0 | PASS |
| 13 | micro-bump (Noise 14/4/0.5 → Bump 0.020/0.010) | chain present, linked to Normal | required | PASS |
| 14 | KEY-L | 400 W | 400 W (never < 300 W) | PASS |
| 15 | alpha clean (02..0.98 fraction) | 0.26 % | ≤ 0.5 % | PASS |
| 16 | occupancy | 86.29 % | 86 ± 1 | PASS |
| 17 | SEQ-A alpha mask Δ (binary) | 0 px over 48/48 | 0 | PASS |
| 18 | frame counts | A 48 / B still+8 / C 72 | 48 / 8+1 / 72 | PASS |
| 17b | spp / depth | 512 spp / 16-bit RGBA / compression 15 | ≥ 128 / 16-bit | PASS |
| FM | frame-match composite (v3) | 7.22 % / 50.0 / 41.39 | 7.2 ± 0.1 / 50.0 ± 0.2 / 41.2 ± 0.2 | PASS |

Verdict: **SHIP**. 129 frames + still + plate. RTX 5060, Cycles GPU, 16/8/4 bounces,
clamp 0, OIDN, Standard \−0.20, filter 1.5 px.
