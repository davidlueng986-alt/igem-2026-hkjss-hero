# A7 Refiner

Read the skill that owns the failing A6 check. Then change **one variable**.

## One-variable rule

If two knobs move, the loop is invalid and A6 must discard the iteration.

Examples of ONE variable:

- Apex Bézier handle length (tip radius)
- z of the widest profile point
- KEY-L power
- HDRI Z rotation at frame 0
- Bump strength
- Vertical sensor height

Not one variable: "reshape the silhouette", "fix lighting", "make it look more like mercury".

## Cap

4 lookdev iterations on SEQ-A frame 0. Then A0 writes ESCALATE.

## After each patch

1. Screenshot (MATERIAL camera, or Cycles still on disk).
2. Hand back to A6. Do not self-score SHIP.
