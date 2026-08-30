# A4 Camera — camera-cinematography

Read before acting: `.claude/skills/camera-cinematography/SKILL.md` and brief §5.

## CAM_Hero_SeqA

| Property | Value |
|---|---|
| Type | Perspective |
| Focal length | 85 mm |
| Distance | 6.0 BU from droplet centre |
| Height | camera z = 0.50, target z = 0.50 |
| Roll | 0 |
| DOF | OFF |
| Shift | Y only if needed; never move the camera |

Framing: droplet occupies **86%** of frame height, centred, equal margins.

Conflict: 85 mm + 6.0 BU + 36 × 24 mm sensor cannot hit 86%.
Keep 85 mm and 6.0 BU. Set `sensor_fit = VERTICAL` and `sensor_height` so occupancy is 86%.
Document the millimetre value in REPORT.md. Measured occupancy 86.07%.

Locked-off product still. No cinematic move. Track To `EMPTY_CamTarget_Hero` at (0, 0, 0.50).
