# Loop log — lookdev still (SEQ-A frame 0)

Cap: 4 lighting/lookdev iterations on the still, plus brief v1.1 §4.2.1 ladder (pre-authorised).
A6 never fixes. A8 blocked until SHIP.

| Iter | Stage | Agent | Variable | Result | Verdict |
|---|---|---|---|---|---|
| 0–4 | S2 | A7 | profile handles | width 0.4200, widest 0.3000, tip 0.0588 | geo **SHIP** |
| 4c | S6 | A7 | ground Specular IOR 0 *(void — not in spec)* | mean 0.136 on straight-alpha | discarded |
| 5 | S6 | A7 | HDRI Mapping Z 0→7° | luma 0.137 | reverted |
| **R1** | S6 | A7 | restore ground §4.3 (rough 0.65, spec 0.5) | median **0.4205** band 8.08 px | **FAIL** |
| **R2** | S6 | A7 | KEY-L el 30°→38°, 400 W | median **0.4067** band 4.08 px | **FAIL** |
| **R3** | S6 | A7 | KEY-L 400→300 W, el 38° | median **0.3888** band 4.08 px | **FAIL · ESCALATE** |

## Geometry (SHIP)

bbox 0.4200 × 1.0000. widest_z 0.3000. tip R 0.0588. inflection 0. Screw 32. Subsurf 3 deferred.

## Lookdev still (ESCALATE)

Check 6 v1.1: median sRGB luma, composite `#0A0B0D`, exclude 4% rim. Threshold < 0.08.
Ladder exhausted. KEY-L 300 W only moved median −0.018. Remaining ~0.39 is not KEY-L.
Do not dim below 300 W. Do not start SEQ-A/B/C.
