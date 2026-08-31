# beauty_farm.py — iGEM 2026 HKJSS Tier-1 beauty PNG16 masters (CLI background run)
# Run: blender -b mercury-hero.blend --python beauty_farm.py
# Creates sequence actions (Blender 5 slotted: world nodes on NODE TREE id),
# renders 512 spp 16-bit at 200% then downsamples 2x to the master size,
# skips existing >10 KB pairs, logs HI/LO rows to FARM-LOG.txt.
# Env: FORCE=1 re-renders everything; SKIP_REPAIR=1 skips LO repair.
import bpy
import math
import os
import sys
import time
import traceback

BASE = r"C:\Users\daive\Downloads\igem-hero-tier1\tier1-delivery-beauty"
LOG = os.path.join(BASE, "FARM-LOG.txt")
SHIP_BLEND = r"C:\Users\daive\Downloads\igem-hero-tier1\mercury-hero.blend"

MIN_OK = 10240

SC = bpy.context.scene
W = bpy.data.worlds["World"]
NT = W.node_tree
DROPLET = bpy.data.objects["SM_MercuryDroplet"]

FAC = r"C:\Users\daive\AppData\Local\Temp\opencode\factories.py"
import importlib.util
_spec = importlib.util.spec_from_file_location("factories", FAC)
_fac = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_fac)


def log(msg):
    line = msg
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line, flush=True)


def ok(p):
    return os.path.isfile(p) and os.path.getsize(p) > MIN_OK


def set_spp_res(spp, res):
    SC.render.resolution_x = res[0]
    SC.render.resolution_y = res[1]
    SC.render.resolution_percentage = 100


def arm_render():
    _fac.arm_render(SC)


def render_frame(path):
    SC.render.filepath = path
    try:
        bpy.ops.render.render(write_still=True)
        return True
    except Exception as e:
        log("RENDER-ERR %s: %s" % (os.path.basename(path), repr(e)[:120]))
        return False


def downscale_logo(hi_path, lo_path, lo_size):
    import numpy as np
    img = bpy.data.images.load(hi_path, check_existing=False)
    img.colorspace_settings.name = "sRGB"
    w, h = img.size
    buf = [0.0] * (w * h * 4)
    img.pixels.foreach_get(buf)
    px = np.array(buf, dtype=np.float32).reshape(h, w, 4)
    px = (px[0::2, 0::2] + px[0::2, 1::2] + px[1::2, 0::2] + px[1::2, 1::2]) / 4.0
    lw, lh = lo_size
    out = bpy.data.images.new("LO_tmp", width=lw, height=lh, alpha=True, float_buffer=True)
    for cs in ("Linear Rec.709", "Scene Linear"):
        try:
            out.colorspace_settings.name = cs
            break
        except Exception:
            pass
    out.pixels.foreach_set(np.ascontiguousarray(px).ravel())
    try:
        out.save_render(lo_path, scene=SC)
    except Exception:
        out.save()
    bpy.data.images.remove(img)
    bpy.data.images.remove(out)


def build_actions():
    return _fac.build_actions(SC)


def apply(aA, aB, aC, aD, act_names, static_deg=None):
    if static_deg is not None:
        NT.animation_data.action = None
        DROPLET.animation_data.action = None
        NT.nodes["Mapping"].inputs[2].default_value = (0.0, 0.0, math.radians(static_deg))
        return
    by = {"ACT_SEQ_A_HDRI": aA, "ACT_SEQ_B_HDRI": aB,
          "ACT_SEQ_C_HDRI": aC, "ACT_SEQ_C_DROPLET": aD}
    NT.animation_data.action = by.get(act_names[0], aC)
    DROPLET.animation_data.action = by.get(
        act_names[1] if len(act_names) > 1 else "", None)


def main():
    arm_render()
    log("=== beauty farm resume %s ===" % time.strftime("%Y-%m-%d %H:%M:%S"))
    if bpy.data.actions.get("ACT_SEQ_A_HDRI") is None or bpy.data.actions.get("ACT_SEQ_B_HDRI") is None:
        build_actions()
    else:
        log("ACTIONS present, reuse")
    aA = bpy.data.actions.get("ACT_SEQ_A_HDRI")
    aB = bpy.data.actions.get("ACT_SEQ_B_HDRI")
    aC = bpy.data.actions.get("ACT_SEQ_C_HDRI")
    aD = bpy.data.actions.get("ACT_SEQ_C_DROPLET")

    # ---- LO repair for frames already HI-complete (fix byte-identical bug) ----
    sd_repair = os.environ.get("SKIP_REPAIR") == "1" or os.environ.get("FORCE") == "1"
    seqdirs = ["seq-a-idle", "seq-b-scan", "seq-c-fall"]
    if not sd_repair:
        for sd in seqdirs:
            hid = os.path.join(BASE, "_hi", sd)
            lod = os.path.join(BASE, sd)
            if not os.path.isdir(hid):
                continue
            for f in os.listdir(hid):
                if not f.endswith(".png"):
                    continue
                hp = os.path.join(hid, f)
                lp = os.path.join(lod, f)
                if ok(hp) and os.path.isfile(lp):
                    try:
                        img = bpy.data.images.load(hp, check_existing=False)
                        lo_res = (img.size[0] // 2, img.size[1] // 2)
                        downscale_logo(hp, lp, lo_res)
                        log("REGEN-LO %s/%s -> %s" % (sd, f, os.path.getsize(lp)))
                    except Exception as e:
                        log("REGEN-ERR %s: %s" % (f, repr(e)[:100]))

    # ---- PLAN: A remaining, B still+8, C 72 ----
    plan = [
        dict(act=["ACT_SEQ_A_HDRI"], hi=(2000, 2800), lo=(1000, 1400),
             frames=list(range(0, 48)), fmt="a-{:03d}.png", sub="seq-a-idle"),
        dict(act=["static"], static=3.5, hi=(2400, 3360), lo=(1200, 1680),
             frames=[None], fmt="still-scan.png", sub="seq-b-scan"),
        dict(act=["ACT_SEQ_B_HDRI"], hi=(2400, 3360), lo=(1200, 1680),
             frames=list(range(0, 8)), fmt="b-{:03d}.png", sub="seq-b-scan"),
        dict(act=["ACT_SEQ_C_HDRI", "ACT_SEQ_C_DROPLET"], hi=(1600, 2240), lo=(800, 1120),
             frames=list(range(0, 72)), fmt="c-{:03d}.png", sub="seq-c-fall"),
    ]
    done_all = True
    force = os.environ.get("FORCE") == "1"
    for seg in plan:
        hid = os.path.join(BASE, "_hi", seg["sub"])
        lod = os.path.join(BASE, seg["sub"])
        os.makedirs(hid, exist_ok=True)
        os.makedirs(lod, exist_ok=True)
        for f in seg["frames"]:
            name = seg["fmt"].format(f) if f is not None else seg["fmt"]
            hp = os.path.join(hid, name)
            lp = os.path.join(lod, name)
            if (not force) and ok(hp) and ok(lp):
                continue
            done_all = False
            apply(aA, aB, aC, aD, seg["act"],
                  static_deg=seg.get("static"))
            if f is not None:
                SC.frame_set(int(f))
            set_spp_res(512, seg["hi"])
            okr = render_frame(hp)
            if not okr:
                log("OOM-RETRY-RES100 %s" % name)
                set_spp_res(512, seg["lo"])
                okr = render_frame(hp)
                if not okr:
                    log("FRAME-FAIL %s" % name)
                    continue
            try:
                downscale_logo(hp, lp, seg["lo"])
            except Exception as e:
                log("LO-ERR %s: %s" % (name, repr(e)[:120]))
            log("HI %s %s" % (name, os.path.getsize(hp)))
            log("LO %s %s" % (name, os.path.getsize(lp)))
    SC.frame_set(0)
    log("FARM-COMPLETE" if done_all else "FARM-DONE-WITH-MISSING")
    with open(os.path.join(BASE, "SEQ-DONE.txt"), "w") as f:
        f.write("FARM-COMPLETE" if done_all else "FARM-DONE-WITH-MISSING")


if __name__ == "__main__":
    if os.environ.get("SMOKE") == "1":
        build_actions()
        print("SMOKE-OK actions:", [a.name for a in bpy.data.actions])
    else:
        main()
