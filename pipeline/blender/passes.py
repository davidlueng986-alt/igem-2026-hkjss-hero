# passes.py — beauty passes + frame-match composite (run AFTER beauty_farm.py)
# blender -b mercury-hero.blend --python passes.py
# Produces: spec-only-a.png (Glossy Direct, compositing_node_group rewire via
# NodeGroupOutput), matte-a.png, silhouette.svg, REF-000, contact-sheet,
# geo-profile-check.png, match/frame-match.png (c-071 at 0.0808x on 1920x1080
# opaque #050506 plate) and the check-6 measurement.
import bpy
import math
import os
import time
import numpy as np

BASE = r"C:\Users\daive\Downloads\igem-hero-tier1\tier1-delivery-beauty"
LOG = os.path.join(BASE, "PASSES-LOG.txt")
BLEND = r"C:\Users\daive\Downloads\igem-hero-tier1\mercury-hero.blend"
SC = bpy.context.scene
W = bpy.data.worlds['World']
NT = W.node_tree
DROPLET = bpy.data.objects['SM_MercuryDroplet']


def log(m):
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(m + '\n')
    print(m, flush=True)


def ensure_actions():
    import importlib.util
    spec = importlib.util.spec_from_file_location('factories', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'factories.py'))
    fac = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fac)
    fac.grab()
    fac.arm_render(SC)
    fac.build_actions(SC)
    log('ACTIONS ensured')


def check6(path):
    img = bpy.data.images.load(path, check_existing=False)
    img.colorspace_settings.name = 'Non-Color'
    w, h = img.size
    buf = [0.0] * (w * h * 4)
    img.pixels.foreach_get(buf)
    px = np.array(buf, dtype=np.float32).reshape(h, w, 4)
    bpy.data.images.remove(img)
    BG = (10.0 / 255.0, 11.0 / 255.0, 13.0 / 255.0)
    a = px[:, :, 3]
    sil = a > 0.5
    ys, xs = np.nonzero(sil)
    if len(xs) == 0:
        return None
    r, g, b = px[:, :, 0], px[:, :, 1], px[:, :, 2]
    cr = r * a + BG[0] * (1 - a)
    cg = g * a + BG[1] * (1 - a)
    cb = b * a + BG[2] * (1 - a)
    Y = 0.2126 * cr + 0.7152 * cg + 0.0722 * cb
    xmin, xmax, ymin, ymax = xs.min(), xs.max(), ys.min(), ys.max()
    width = xmax - xmin + 1
    height = ymax - ymin + 1
    band = 0.04 * width
    xlo, xhi = xmin + band, xmax - band
    ycut = ymin + height / 3.0
    mask = sil & (np.arange(w)[None, :] >= xlo) & (np.arange(w)[None, :] <= xhi)
    reg = Y[mask & (np.arange(h)[:, None] <= ycut)]
    reg = np.sort(reg)
    n = len(reg)
    med = float(reg[n // 2]) if n else None
    mean = float(reg.mean()) if n else None
    p90 = float(reg[int(n * 0.9)]) if n else None
    return dict(wh=[w, h], bbox=[int(xmin), int(ymin), int(xmax), int(ymax)],
                sil_w=int(width), sil_h=int(height),
                occupancy=round(height / h, 4), band_px=round(float(band), 2),
                n=int(n), median=round(med, 4), mean=round(mean, 4), p90=round(p90, 4),
                pass_=True if (med is not None and med < 0.08) else False)


def main():
    ensure_actions()
    os.makedirs(os.path.join(BASE, 'passes'), exist_ok=True)
    os.makedirs(os.path.join(BASE, 'review'), exist_ok=True)
    os.makedirs(os.path.join(BASE, 'match'), exist_ok=True)
    log('=== passes %s ===' % time.strftime('%Y-%m-%d %H:%M:%S'))

    lo_a0 = os.path.join(BASE, 'seq-a-idle', 'a-000.png')
    spec_path = os.path.join(BASE, 'passes', 'spec-only-a.png')
    if os.path.isfile(spec_path) and os.path.getsize(spec_path) > 10240:
        log('spec-only-a exists, skip')
    else:
        vl = SC.view_layers[0]
        vl.use_pass_glossy_direct = True
        cg = SC.compositing_node_group
        nodes = cg.nodes
        links = cg.links
        rl = [n for n in nodes if n.type == 'R_LAYERS'][0]
        out = [n for n in nodes if n.type == 'GROUP_OUTPUT'][0]
        sock = None
        for o in rl.outputs:
            if 'glossy' in o.name.lower():
                sock = o
                if 'direct' in o.name.lower():
                    break
        if sock is None:
            log('FATAL no glossy socket')
            return
        for l in list(links):
            if l.to_node == out:
                links.remove(l)
        links.new(sock, out.inputs[0])
        SC.render.resolution_x = 2000
        SC.render.resolution_y = 2800
        SC.render.resolution_percentage = 100
        SC.cycles.samples = 512
        SC.render.image_settings.color_depth = '16'
        SC.render.film_transparent = True
        NT.animation_data.action = bpy.data.actions.get('ACT_SEQ_A_HDRI')
        DROPLET.animation_data.action = None
        SC.frame_set(0)
        SC.render.filepath = spec_path
        bpy.ops.render.render(write_still=True)
        log('spec HI %s %s' % (os.path.basename(spec_path), os.path.getsize(spec_path)))
        img = bpy.data.images.load(spec_path, check_existing=False)
        img.colorspace_settings.name = 'sRGB'
        w, h = img.size
        buf = [0.0] * (w * h * 4)
        img.pixels.foreach_get(buf)
        px = np.array(buf, dtype=np.float32).reshape(h, w, 4)
        bpy.data.images.remove(img)
        px2 = (px[0::2, 0::2] + px[0::2, 1::2] + px[1::2, 0::2] + px[1::2, 1::2]) / 4.0
        img2 = bpy.data.images.new('spec_lo', width=1000, height=1400, alpha=True, float_buffer=True)
        try:
            img2.colorspace_settings.name = 'Linear Rec.709'
        except Exception:
            pass
        img2.pixels.foreach_set(np.ascontiguousarray(px2).ravel())
        img2.save_render(spec_path, scene=SC)
        bpy.data.images.remove(img2)
        log('spec LO %s %s' % (os.path.basename(spec_path), os.path.getsize(spec_path)))

    # REF-000 + matte-a + silhouette.svg + contact-sheet + frame-match + geo
    import shutil
    ref_path = os.path.join(BASE, 'review', 'REF-000.png')
    shutil.copyfile(lo_a0, ref_path)
    log('REF-000 copied')
    img = bpy.data.images.load(lo_a0, check_existing=False)
    img.colorspace_settings.name = 'Non-Color'
    w, h = img.size
    buf = [0.0] * (w * h * 4)
    img.pixels.foreach_get(buf)
    px = np.array(buf, dtype=np.float32).reshape(h, w, 4)
    bpy.data.images.remove(img)
    matte = np.zeros_like(px)
    matte[:, :, :3] = 1.0 * (px[:, :, 3:4] > 0.5)
    matte[:, :, 3] = 1.0
    matte_path = os.path.join(BASE, 'passes', 'matte-a.png')
    mimg = bpy.data.images.new('matte', width=w, height=h, alpha=True)
    mimg.colorspace_settings.name = 'Non-Color'
    mimg.pixels.foreach_set(np.ascontiguousarray(matte).ravel())
    mimg.filepath_raw = matte_path
    mimg.file_format = 'PNG'
    mimg.save()
    bpy.data.images.remove(mimg)
    log('matte-a written')
    a = px[:, :, 3]
    mask = a > 0.5
    ys, xs = np.nonzero(mask)
    xmin, xmax, ymin, ymax = xs.min(), xs.max(), ys.min(), ys.max()
    bxp, byp = int(xmax - xmin), int(ymax - ymin)
    top = []
    bot = []
    for x in range(int(xmin), int(xmax) + 1, 4):
        col = np.nonzero(mask[:, x])[0]
        if len(col):
            top.append((x, int(col.max())))
            bot.append((x, int(col.min())))
    pts = top[::-1] + bot
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">' % (bxp, byp, bxp, byp)]
    d = 'M ' + ' L '.join('%d %d' % (x - xmin, byp - (y - ymin)) for x, y in pts)
    svg.append('<path d="%s" fill="#BFBEAE" stroke="black" stroke-width="8"/>' % d)
    svg.append('</svg>')
    with open(os.path.join(BASE, 'passes', 'silhouette.svg'), 'w') as f:
        f.write('\n'.join(svg))
    log('silhouette.svg written %d pts' % len(pts))

    n = 48
    cols = 6
    rows = 8
    tw, th = 125, 175
    sheet = np.zeros((rows * th, cols * tw, 4), dtype=np.float32)
    for i in range(n):
        p = os.path.join(BASE, 'seq-a-idle', 'a-%03d.png' % i)
        if not os.path.isfile(p):
            continue
        im = bpy.data.images.load(p, check_existing=False)
        im.colorspace_settings.name = 'Non-Color'
        ww, hh = im.size
        bf = [0.0] * (ww * hh * 4)
        im.pixels.foreach_get(bf)
        pp = np.array(bf, dtype=np.float32).reshape(hh, ww, 4)
        bpy.data.images.remove(im)
        ys2 = (np.arange(th) * hh // th).astype(int)
        xs2 = (np.arange(tw) * ww // tw).astype(int)
        sm = pp[ys2][:, xs2]
        r, c = i // cols, i % cols
        sheet[r * th:(r + 1) * th, c * tw:(c + 1) * tw, :] = sm
    simg = bpy.data.images.new('sheet', width=cols * tw, height=rows * th, alpha=True)
    simg.colorspace_settings.name = 'Non-Color'
    simg.pixels.foreach_set(np.ascontiguousarray(sheet).ravel())
    sheet_path = os.path.join(BASE, 'review', 'contact-sheet.png')
    simg.filepath_raw = sheet_path
    simg.file_format = 'PNG'
    simg.save()
    bpy.data.images.remove(simg)
    log('contact-sheet written')

    c71 = os.path.join(BASE, 'seq-c-fall', 'c-071.png')
    if os.path.isfile(c71):
        im = bpy.data.images.load(c71, check_existing=False)
        im.colorspace_settings.name = 'Non-Color'
        ww, hh = im.size
        bf = [0.0] * (ww * hh * 4)
        im.pixels.foreach_get(bf)
        pp = np.array(bf, dtype=np.float32).reshape(hh, ww, 4)
        bpy.data.images.remove(im)
        canvas = np.zeros((1080, 1920, 4), dtype=np.float32)
        canvas[:, :, 0] = 5 / 255.0
        canvas[:, :, 1] = 5 / 255.0
        canvas[:, :, 2] = 6 / 255.0
        canvas[:, :, 3] = 1.0
        q = 0.0808
        dst_w, dst_h = int(round(ww * q)), int(round(hh * q))
        ys2 = np.round((np.arange(dst_h) + 0.5) / q - 0.5).astype(int).clip(0, hh - 1)
        xs2 = np.round((np.arange(dst_w) + 0.5) / q - 0.5).astype(int).clip(0, ww - 1)
        small = pp[ys2][:, xs2]
        x0 = (1920 - dst_w) // 2
        y0 = int(round(558 - 94 * q))
        al = small[:, :, 3:4]
        reg = canvas[y0:y0 + dst_h, x0:x0 + dst_w, :]
        reg[:, :, :3] = small[:, :, :3] * al + reg[:, :, :3] * (1 - al)
        reg[:, :, 3] = 1.0
        canvas[y0:y0 + dst_h, x0:x0 + dst_w, :] = reg
        fim = bpy.data.images.new('fm', width=1920, height=1080, alpha=True)
        fim.colorspace_settings.name = 'Non-Color'
        fim.pixels.foreach_set(np.ascontiguousarray(canvas).ravel())
        fm_path = os.path.join(BASE, 'match', 'frame-match.png')
        fim.filepath_raw = fm_path
        fim.file_format = 'PNG'
        fim.save()
        bpy.data.images.remove(fim)
        log('frame-match composite written')
    r6 = check6(lo_a0)
    print('CHECK6', r6)
    log('PASSES COMPLETE')


main()
