# TIER 1 RENDER REPORT
Date: 2026-08-31 | Blender 5.2.1 LTS | Device: OPTIX · RTX 5060 | Brief **v1.2**

## 1. Audit results

| # | Check | Result | Measured |
|---|---|---|---|
| 1 | width/height | **PASS** | 0.4200 |
| 2 | widest from base | **PASS** | 0.3000 |
| 3 | no neck inflection | **PASS** | monotonic after 0.30 |
| G | tip radius | **PASS** | 0.0588 |
| 4 | greyscale mercury | **PASS** | 128 spp still; hard strips |
| 5 | rectangular softbox | **PASS** | KEY-L 400 W / 30° |
| 6 | lower third median < 0.08 | **PASS** | **median 0.0359** mean 0.0370 band 10.08 px · 128 spp · composite `#0A0B0D` |
| 7 | grazing rim | **PASS** | present; excluded from #6 |
| 8 | keys not mirrored | **PASS** | L 400 W 30° / R 260 W 18° |
| 9 | zero blue | **HOLD** | 128 spp chroma ≈ 0 |
| 10 | bump 400% | **HOLD** | Noise 14 / 0.020 in tree |
| 11 | alpha clean | **HOLD** | 3-master pixel-diff stalled MCP once; not re-run |
| 12 | banding | **HOLD** | lookdev 8-bit; beauty 16-bit pending |
| 13 | frame counts | **PASS** | **48 / 8 / 72** |
| 14 | SEQ-A wrap | **PASS / NOTE** | deg0=0 deg24=7 deg47=0.29 wrap=0.29°. Sine interior steps 0.03–0.45 |
| 15 | SEQ-A silhouette identical | **EXPECTED 0** | HDRI-only; pixel-diff skipped |
| 16 | 86% framing | **PASS** | still 0.8629 / c-071 0.8634 |
| 17 | frame-match | **PASS** | h **7.13%** (Δ −0.07) apex x **50.0** y **41.20** tilt 0 |
| 18 | composite #0A0B0D | **PASS** | liquid metal, foot dark |

**Lookdev: SHIP. Sequences: complete at lookdev spp.**

## 2. Iteration log — what fixed check 6

**v1.2 §4.3 Diffuse BSDF ground** (ADR-015). Not the KEY-L ladder.

| Iter | Variable | From → To | Effect | Kept? |
|---|---|---|---|---|
| R1–R3 | v1.1 Principled ground + KEY-L ladder | median 0.39 | **no** |
| v1.2 | ground | Principled → **Diffuse BSDF** `#050506` R=1 40×40 | median **0.0319** @ 128 spp | **yes** |
| AMBER | KEY-L | 300 W/38° → **400 W/30°** | median **0.0359**, highlights restored | **yes** |

GREEN: HDRI `studio_small_08` 4k. Screw 128 + shade smooth (32 642 verts).

## 3. Deviations
- Sequences at **100% / 128 spp / 8-bit**, not 200% / 512 spp / 16-bit. GPU OOM history. Beauty pass remaining.
- Screw 128 instead of Screw 32 + Subsurf 3.
- `spec-only-a.png` (Glossy Direct AOV) not yet rendered.
- Check 14: sine easing makes adjacent steps unequal; wrap is the specified 0.29°.

## 4. Conflicts
- v1.0/v1.1 Principled ground Fresnel at grazing lit the lower bulb. Diffuse BSDF dropped median 0.39 → 0.036.
- Check 14 vs sine interpolation: cannot have both equal adjacent steps and sine in-out.

## 5. Match-cut contract — measured

| Property | Required | Measured | Δ |
|---|---|---|---|
| Droplet height % of frame | 7.2% ±0.1 | **7.13%** | −0.07 |
| Apex x | 50.0% ±0.2 | **50.0%** | 0 |
| Apex y (from top) | 41.2% ±0.2 | **41.20%** | 0.00 |
| Tilt | 0.0° ±0.2 | 0.0° | 0 |

Composited `c-071.png` onto 1920×1080 `#050506` (same lighting/silhouette as SEQ-C, no camera move). `frame-match-crop.png` 800×800.

## 6. Asset inventory (Windows)

`C:\Users\daive\Downloads\igem-hero-tier1\tier1-delivery\`

| Path | Frames | Res | Bytes |
|---|---|---|---|
| seq-a-idle/a-000…047 | 48 | 1000×1400 | 38.2 MB |
| seq-b-scan/still-scan + b-000…007 | 1+8 | 1200×1680 | 10.2 MB |
| seq-c-fall/c-000…071 | 72 | 800×1120 | 37.5 MB |
| match/frame-match(.crop) | 2 | 1920×1080 / 800×800 | 92 KB |
| passes/matte-a.png + silhouette.svg | 2 | 500×700 | 28 KB |
| review/REF-000 + contact-sheet | 2 | 1000×1400 / 1000×1120 | 1.2 MB |
| source/mercury-hero.blend + HDRI-LICENCE.txt | — | — | 0.90 MB |

## 7. HDRI & licence
`studio_small_08` **4k**, Poly Haven, **CC0**. https://polyhaven.com/a/studio_small_08

## 8. Known issues
1. Beauty 512 spp / 16-bit / 200% not rendered.
2. `spec-only-a.png` AOV missing.
3. Check 15 alpha-diff not numeric (MCP stall on 3×1000×1400 load).
4. Check 9/10/11/12 HOLD pending 400% beauty inspection.
