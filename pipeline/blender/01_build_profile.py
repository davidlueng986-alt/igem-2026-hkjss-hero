"""A1 Modeler — Bézier mercury profile. Run via Blender MCP in SMALL chunks.
Contracts (spec §8.2 / brief §2): height 1.000, width 0.420, widest from base 0.300,
tip radius 0.060, bulb radius 0.300, C2, no neck inflection, base R >= 0.28.

Live CTRL after A7 iters 1–4 + S2 extra (2026-08-30). Measured:
  bbox 0.4200 × 1.0000, widest_z 0.3000, tip R median 0.0588.
"""
import bpy
import math

# x, z, hlx, hlz, hrx, hrz   (offsets from co)
CTRL = [
    (0.00000, 0.00000, -1.00000, 0.00000, 0.15500, 0.00000),  # p0 pole
    (0.16500, 0.06500, -0.04364, -0.04364, 0.04000, 0.04000),  # p1
    (0.19000, 0.17500, -0.00408, -0.05615, 0.00400, 0.05500),  # p2
    (0.21000, 0.30000, 0.00000, -0.02000, 0.00000, 0.07500),  # p3 widest
    (0.20500, 0.45000, 0.00000, -0.06941, 0.00000, 0.07000),  # p4
    (0.18500, 0.60000, 0.02486, -0.06215, -0.02800, 0.07000),  # p5
    (0.13000, 0.76000, 0.03274, -0.05456, -0.03000, 0.05000),  # p6
    (0.06000, 0.94000, 0.00000, -0.04000, 0.00000, 0.03000),  # p7 tip equator
    (0.00000, 1.00000, 0.03314, 0.00000, -0.03314, 0.00000),  # p8 apex R=0.060
]


def ensure_col(name):
    c = bpy.data.collections.get(name)
    if c is None:
        c = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(c)
    return c


def link_only(obj, col_name):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    ensure_col(col_name).objects.link(obj)


def build_profile():
    old = bpy.data.objects.get("CRV_MercProfile")
    if old:
        bpy.data.objects.remove(old, do_unlink=True)
    cd = bpy.data.curves.new("CRV_MercProfile", "CURVE")
    cd.dimensions = "3D"
    cd.resolution_u = 32
    spl = cd.splines.new("BEZIER")
    spl.bezier_points.add(len(CTRL) - 1)
    for i, (x, z, hlx, hlz, hrx, hrz) in enumerate(CTRL):
        p = spl.bezier_points[i]
        p.co = (x, 0.0, z)
        p.handle_left_type = "FREE"
        p.handle_right_type = "FREE"
        p.handle_left = (x + hlx, 0.0, z + hlz)
        p.handle_right = (x + hrx, 0.0, z + hrz)
        if i not in (3, 4):
            p.handle_left_type = "ALIGNED"
            p.handle_right_type = "ALIGNED"
    obj = bpy.data.objects.new("CRV_MercProfile", cd)
    link_only(obj, "COL_Mercury")
    return obj


def add_screw(obj, steps=32):
    for m in list(obj.modifiers):
        obj.modifiers.remove(m)
    sc = obj.modifiers.new("Screw", "SCREW")
    sc.axis = "Z"
    sc.angle = math.tau
    sc.steps = steps
    sc.render_steps = steps
    sc.use_smooth_shade = True
    sc.use_merge_vertices = True
    sc.merge_threshold = 0.0001
    return sc


if __name__ == "__main__":
    o = build_profile()
    add_screw(o, steps=32)
    print("profile", o.name, "pts", len(CTRL))
