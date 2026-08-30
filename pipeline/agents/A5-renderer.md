# A5 Renderer — rendering + compositing

Read before acting:
- `.claude/skills/rendering/SKILL.md`
- `.claude/skills/compositing/SKILL.md`
- Brief §7

## Cycles (spec wins over skill AgX)

| Setting | Value |
|---|---|
| Engine | Cycles OPTIX GPU |
| Samples | lookdev 16–64; beauty 512 |
| Denoise | OIDN, Albedo + Normal if the build exposes them |
| Bounces | Total 16, Glossy 8, Transmission 4 |
| Clamp Indirect | 0 |
| Film Transparent | ON (OFF only for frame-match) |
| Filter Width | 1.20 px |
| View Transform | **Standard** (not AgX, not Filmic) |
| Look | None |
| Exposure | −0.20 |
| Output | PNG RGBA 16-bit, compression 15% |

## MCP

Keep `execute_blender_code` tiny. `write_still` to disk; do **not** rely on
RENDERED viewport screenshots (they return black on this addon/GPU path).
MATERIAL camera view is allowed for lookdev only.

Lookdev still = SEQ-A frame 0 only. Do not render 128 frames of a wrong look.

## Composite

Over `#0A0B0D`. Greyscale test before calling A6.
