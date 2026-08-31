# factories.py — shared scene prep for beauty farm/passes/audit
# Blender 5.2 slotted actions: world node animation lives on the NODE TREE id
# (World.keyframe_insert with node paths is NOT resolvable in 5.2 — keyframe the
# node tree instead, slot id_type NODETREE).
# Also arms Cycles RTX explicitly (background mode won't pick GPU by default).
import bpy
import math

SC = None


def grab():
    global SC
    SC = bpy.context.scene
    return SC


def build_actions(SC):
    W = bpy.data.worlds["World"]
    NT = W.node_tree
    D = bpy.data.objects["SM_MercuryDroplet"]

    def act_world(name, keys, interp="SINE"):
        old = bpy.data.actions.get(name)
        if old:
            return old
        a = bpy.data.actions.new(name)
        NT.animation_data_create()
        NT.animation_data.action = a
        nd = NT.nodes["Mapping"]
        for f, deg in keys:
            nd.inputs[2].default_value = (0.0, 0.0, math.radians(deg))
            NT.keyframe_insert(data_path='nodes["Mapping"].inputs[2].default_value',
                               index=2, frame=f)
        cb = a.layers[0].strips[0].channelbags[0]
        for fc in cb.fcurves:
            for kp in fc.keyframe_points:
                kp.interpolation = interp
            fc.update()
        return a

    def act_object(name, keys, interp="LINEAR"):
        old = bpy.data.actions.get(name)
        if old:
            return old
        a = bpy.data.actions.new(name)
        D.animation_data_create()
        D.animation_data.action = a
        for f, deg in keys:
            D.rotation_euler[2] = math.radians(deg)
            D.keyframe_insert("rotation_euler", index=2, frame=f)
        cb = a.layers[0].strips[0].channelbags[0]
        for fc in cb.fcurves:
            for kp in fc.keyframe_points:
                kp.interpolation = interp
            fc.update()
        return a

    aA = act_world("ACT_SEQ_A_HDRI", [(0, 0.0), (24, 7.0), (47, 0.29)])
    aB = act_world("ACT_SEQ_B_HDRI", [(0, 3.0), (4, 4.0), (7, 3.25)])
    aC = bpy.data.actions.get("ACT_SEQ_C_HDRI")
    if aC is None:
        aC = act_world("ACT_SEQ_C_HDRI", [(0, 0.0), (71, 22.0)], interp="LINEAR")
    aD = act_object("ACT_SEQ_C_DROPLET", [(0, 0.0), (71, 9.0)])
    return aA, aB, aC, aD


def arm_render(SC):
    try:
        prefs = bpy.context.preferences.addons['cycles'].preferences
        try:
            prefs.compute_device_type = 'OPTIX'
        except Exception:
            prefs.compute_device_type = 'CUDA'
        prefs.get_devices()
        for d in prefs.devices:
            d.use = d.type != 'CPU'
        print('DEVICES', [(d.name, d.type, d.use) for d in prefs.devices], flush=True)
    except Exception as e:
        print('GPU-PREF-ERR', repr(e)[:120], flush=True)
    SC.render.engine = "CYCLES"
    SC.cycles.device = "GPU"
    SC.cycles.samples = 512
    SC.cycles.use_denoising = True
    SC.render.image_settings.file_format = "PNG"
    SC.render.image_settings.color_mode = "RGBA"
    SC.render.image_settings.color_depth = "16"
    SC.render.image_settings.compression = 15
    SC.render.film_transparent = True
