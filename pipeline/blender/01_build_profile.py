"""A1 Modeler — Bezier mercury profile. Run via Blender MCP in SMALL chunks."""
import bpy
import math

CTRL = [
    (0.000, 0.000, -0.010, 0.000, 0.155, 0.000),
    (0.165, 0.065, -0.055, -0.028, 0.040, 0.040),
    (0.206, 0.175, -0.012, -0.055, 0.004, 0.055),
    (0.210, 0.300, 0.000, -0.070, 0.000, 0.075),
    (0.205, 0.450, 0.004, -0.070, -0.010, 0.070),
    (0.185, 0.600, 0.016, -0.065, -0.028, 0.070),
    (0.130, 0.760, 0.032, -0.055, -0.030, 0.050),
    (0.058, 0.910, 0.028, -0.035, -0.022, 0.028),
    (0.000, 1.000, 0.033, 0.000, 0.000, 0.000),
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
        p.handle_left_type = "ALIGNED"
        p.handle_right_type = "ALIGNED"
        p.handle_left = (x + hlx, 0.0, z + hlz)
        p.handle_right = (x + hrx, 0.0, z + hrz)
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
