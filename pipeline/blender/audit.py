# audit.py — 18 checks on beauty a-000 + sequence integrity + frame-match
# blender -b mercury-hero.blend --python audit.py
import bpy
import math
import os
import json
import numpy as np

BASE = r"C:\Users\daive\Downloads\igem-hero-tier1\tier1-delivery-beauty"
SC = bpy.context.scene


def load_px(path):
    img = bpy.data.images.load(path, check_existing=False)
    img.colorspace_settings.name = 'Non-Color'
    w, h = img.size
    buf = [0.0] * (w * h * 4)
    img.pixels.foreach_get(buf)
    px = np.array(buf, dtype=np.float32).reshape(h, w, 4)
    bpy.data.images.remove(img)
    return px


R = {}


def chk(n, name, val, target, tol=None, pass_=None):
    if pass_ is None:
        if tol is None:
            pass_ = val == target
        else:
            pass_ = abs(val - target) <= tol
    R[n] = dict(name=name, val=str(val), target=str(target), tol=tol, pass_=pass_)
    print('CHECK', n, name, val, 'TARGET', target, 'TOL', tol, 'PASS', pass_, flush=True)


ob = bpy.data.objects['SM_MercuryDroplet']
me = ob.data
verts = np.empty(len(me.vertices) * 3, dtype=np.float32)
me.vertices.foreach_get('co', verts)
co = verts.reshape(-1, 3)
r = np.sqrt(co[:, 0] ** 2 + co[:, 1] ** 2)
z = co[:, 2]
height = float(z.max() - z.min())
width = float(2 * r.max())
k = int(r.argmax())
widest_z = float(z[k])
ztop = float(z.max())
tm = (z > ztop - 0.08) & (z < ztop - 0.02)
tip_r = float(r[tm].max())
chk(1, 'geometry height', round(height, 4), 1.0, 0.005)
chk(2, 'geometry max width', round(width, 4), 0.42, 0.005)
chk(3, 'widest from base', round(widest_z, 4), 0.30, 0.005)
chk(4, 'apex tip radius', round(tip_r, 4), 0.06, 0.01)

mer = bpy.data.materials['MAT_Mercury_Liquid']
bsdf = [n for n in mer.node_tree.nodes if n.type == 'BSDF_PRINCIPLED'][0]
met = bsdf.inputs['Metallic'].default_value
rgh = bsdf.inputs['Roughness'].default_value
ems = bsdf.inputs['Emission Strength'].default_value
emc = bsdf.inputs['Emission Color'].default_value[:3]
has_bump = any(n.type == 'BUMP' for n in mer.node_tree.nodes)
has_noise = any(n.type == 'TEX_NOISE' for n in mer.node_tree.nodes)
chk(10, 'metallic 1.0', round(met, 3), 1.0, 0.0)
chk(11, 'roughness 0.030', round(rgh, 4), 0.03, 0.001)
chk(12, 'no emission', round(float(ems) * max(map(float, emc)), 5), 0.0, 0.0)
chk(13, 'micro-bump', float(has_bump and has_noise), 1.0, 0.0)
lights = {o.name: (o.data.type, round(o.data.energy, 1)) for o in bpy.data.objects if o.type == 'LIGHT'}
chk(14, 'KEY-L 400W', lights['LGT_Key_L'][1], 400.0, 0.0)

a0 = load_px(os.path.join(BASE, 'seq-a-idle', 'a-000.png'))
h, w, c = a0.shape
BG = (10 / 255.0, 11 / 255.0, 13 / 255.0)
al = a0[:, :, 3]
sil = al > 0.5
ys, xs = np.nonzero(sil)
xmin, xmax, ymin, ymax = xs.min(), xs.max(), ys.min(), ys.max()
silw = int(xmax - xmin + 1)
silh = int(ymax - ymin + 1)
occ = silh / h
r_, g_, b_ = a0[:, :, 0], a0[:, :, 1], a0[:, :, 2]
cr = r_ * al + BG[0] * (1 - al)
cg = g_ * al + BG[1] * (1 - al)
cb2 = b_ * al + BG[2] * (1 - al)
Y = 0.2126 * cr + 0.7152 * cg + 0.0722 * cb2
band = 0.04 * silw
xg = np.arange(w)
yg = np.arange(h)
inband = (xg[None, :] >= xmin + band) & (xg[None, :] <= xmax - band)
lower3 = sil & inband & (yg[:, None] <= ymin + silh / 3.0)
reg = np.sort(Y[lower3])
n = len(reg)
med = float(reg[n // 2])
chk(6, 'check6 lower-third median (<0.08)', round(med, 4), 0.08, tol=None, pass_=med < 0.08)
chk(16, 'occupancy 86%', round(occ * 100, 2), 86.0, 1.0)
mid = float(((al > 0.02) & (al < 0.98)).mean())
chk(15, 'alpha clean mid-alpha <= 0.5%', round(mid, 5), 0.005, tol=None, pass_=mid <= 0.005)
ysh, xsh = np.nonzero(sil)
pts = np.random.RandomState(1).choice(len(ysh), 20, replace=False)
blue_ct = 0
for p in pts:
    yy, xx = int(ysh[p]), int(xsh[p])
    if b_[yy, xx] > r_[yy, xx] * 1.15 and g_[yy, xx] < b_[yy, xx]:
        blue_ct += 1
chk(9, 'no blue (20-pt sample)', blue_ct, 0, 1.0)
chk(5, 'view transform Standard', SC.view_settings.view_transform, 'Standard', None)
chk(7, 'film transparent', float(SC.render.film_transparent), 1.0, None)

maxmask = 0
ad = al
for i in range(48):
    p = os.path.join(BASE, 'seq-a-idle', 'a-%03d.png' % i)
    if not os.path.isfile(p):
        break
    px = load_px(p)
    d = np.logical_xor(px[:, :, 3] > 0.5, ad > 0.5).sum()
    if d > maxmask:
        maxmask = d
chk(17, 'SEQ-A alpha mask delta', int(maxmask), 0, 0)
na = len([f for f in os.listdir(os.path.join(BASE, 'seq-a-idle')) if f.startswith('a-')])
nb = len([f for f in os.listdir(os.path.join(BASE, 'seq-b-scan')) if f.startswith('b-')])
nst = os.path.isfile(os.path.join(BASE, 'seq-b-scan', 'still-scan.png'))
nc = len([f for f in os.listdir(os.path.join(BASE, 'seq-c-fall')) if f.startswith('c-')])
chk(18, 'frame counts A/Bstill+8/C', '%d/%d+%d/%d' % (na, nb, int(nst), nc), '48/8+1/72', None, pass_=(na == 48 and nst and nb == 8 and nc == 72))

with open(os.path.join(BASE, 'AUDIT-BEAUTY.json'), 'w') as f:
    json.dump({k: {kk: vv for kk, vv in v.items()} for k, v in R.items()}, f, indent=1, default=str)
print('AUDIT DONE')
