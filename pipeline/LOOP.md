# Loop log — lookdev still (SEQ-A frame 0)

Cap: 4 lighting/lookdev iterations on the still. Geometry S2 is a separate loop.
A6 never fixes. A8 blocked until SHIP.

| Iter | Stage | Agent | Variable | Result | Verdict |
|---|---|---|---|---|---|
| 0 | S1–S6 | A1–A5 | bootstrap + profile + MAT + keys + CAM | width 0.4224 PASS; widest 0.377 FAIL; needle apex | **NO-SHIP** |
| 1 | S2 | A7 | p8 handle = 0.552×0.060 | tip R 0.035 | **NO-SHIP** |
| 2 | S2 | A7 | p7 onto tip equator (0.060, 0.940) | tip R **0.0588 PASS** | **NO-SHIP** |
| 3 | S2 | A7 | p4.handle_left.x vertical FREE | width **0.4200** | **NO-SHIP** |
| 4 | S2 | A7 | p3.handle_left; p2.x → 0.190 | widest **0.3000**; checks 1–3 **PASS** | geo SHIP |
| 4b | S6 | A7 | ground XY scale 8→40 | luma 0.468 (no change) | **NO-SHIP** |
| 4c | S6 | A7 | ground Specular IOR 0.5→0.0 | luma **0.136** (was 0.47; target < 0.08) | **NO-SHIP** |

Sequences, passes, packed beauty: blocked.

## Geometry (SHIP)

bbox 0.4200 × 1.0000. widest_z 0.3000. tip R 0.0588. inflection 0. Screw 32. Subsurf 3 deferred.

## Lookdev still (NO-SHIP)

Hard strip highlights: yes. Occupancy 86.07%. Lower-third luma 0.136 vs < 0.08.
Ground spec was the lever (scale was not). Next one-variable: KEY-L power **or** HDRI strength. Do not start SEQ-A.
