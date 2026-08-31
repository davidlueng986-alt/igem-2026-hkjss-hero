# Loop log — lookdev still + SEQ-A

## Lookdev (SHIP)

| Iter | Variable | Result | Verdict |
|---|---|---|---|
| R1–R3 | v1.1 ladder (Principled ground) | median 0.39 | void — wrong shader |
| **v1.2** | ground → **Diffuse BSDF** `#050506` R=1, 40×40, glossy ON | median **0.0319** @ 128 spp | **SHIP** |
| AMBER | restore KEY-L 400 W / el 30° | median **0.0359** @ 128 spp | **SHIP** (kept) |

GREEN: HDRI `studio_small_08` **4k**. Screw **128** + shade smooth (no Subsurf). 32642 verts. Width 0.420 height 1.000. Occupancy 86.29%.

## SEQ-A

48 frames `a-000`…`a-047` at 1000×1400 128 spp GPU. HDRI Z sine ping-pong 0° → 7° → 0.29°.
Wrap 47→0 = 0.29°. Interior steps vary (sine). Beauty 200%/512 spp still pending.

SEQ-B / SEQ-C / match-cut: next.
