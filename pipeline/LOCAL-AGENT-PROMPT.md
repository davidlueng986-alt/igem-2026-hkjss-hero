# LOCAL AGENT TASK — finish iGEM 2026 HKJSS Tier 1 beauty masters

You have **GitHub MCP** and **local Blender MCP**. 3D generalist. Do not redesign. Do not ask. Finish PNG16 masters.
Human-facing: Traditional Chinese (HK). REPORT/code: English.

## 0. Current state (2026-08-31)

Lookdev SHIP in `C:\\Users\\daive\\Downloads\\igem-hero-tier1\\tier1-delivery\\` (8-bit 128 spp). Do **not** overwrite it.

Blend: `C:\\Users\\daive\\Downloads\\igem-hero-tier1\\mercury-hero.blend`
Beauty dest: `C:\\Users\\daive\\Downloads\\igem-hero-tier1\\tier1-delivery-beauty\\`
A Blender **timer is already rendering SEQ-A PNG16** (2000×2800 512 spp → 1000×1400). Check `FARM-LOG.txt` and **skip existing** files >10 KB. Do not start a second timer.

SHIP locked: width 0.420 / widest 0.300 / tip 0.0588 / Screw 128 / Diffuse ground `#050506` / KEY-L **400 W 30°** / check 6 median 0.0359 / check 15 α Δ=0.

Repo: https://github.com/davidlueng986-alt/igem-2026-hkjss-hero
Brief v1.2: `docs/02-AGENT-BRIEF-TIER1-BLENDER.md`
Farm script in repo: `pipeline/blender/beauty_farm.py`

## 1. Job

1. Ping Blender. If SEQ-A timer alive, wait until `seq-a-idle` has 48 PNG16 files.
2. Then SEQ-B still+8 (2400×3360 → 1200×1680), SEQ-C 72 (1600×2240 → 800×1120), same 512 spp 16-bit 200%.
3. Recreate missing actions: SEQ-A sine 0/7/0.29 frames 0/24/47; SEQ-B sine 3.0/4.0/3.25 frames 0/4/7; SEQ-C HDRI linear 0→22 + droplet Z 0→9 frames 0–71. Blender 5 F-curves: `action.layers[0].strips[0].channelbags[0].fcurves`.
4. GPU OOM → keep 512 spp, drop to 100% res, log. Never drop KEY-L or bit depth.
5. Frame-match from beauty c-071: 1920×1080 `#050506`, height 7.2%±0.1, apex 50.0/41.2±0.2. Do not move camera.
6. Beauty spec-only-a Glossy Direct 1000×1400 PNG16. Restore Combined after.
7. REF-000, matte-a, silhouette.svg, contact-sheet, geo-profile-check.png from **beauty**.
8. Re-run all 18 checks on beauty a-000. Check 6: composite `#0A0B0D`, median, exclude 4% rim, lower third, ≥128 spp.
9. Pack blend + HDRI CC0 licence into beauty/source/. Update REPORT.md. Push GitHub. Do not upload PNG16 binaries.

## 2. MCP hard rules
Tiny execute. `numpy`+`foreach_get` never `list(pixels)`. One render per timer tick. MCP timeout ≠ failed render. No `Scene.node_tree`, no `Action.fcurves`, no `CompositorNodeComposite` (use NodeGroupOutput). No `render(animation=True)` via MCP.

## 3. RED
Silhouette, mercury material, KEY-L <300 W, 85 mm, 86% frame, frame counts, PNG16, match-cut, no blue, no emission.

Start: poll FARM-LOG, continue from first missing frame.
