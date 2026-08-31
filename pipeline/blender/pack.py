# pack.py — pack HDRI + save SHIP blend into beauty/source, copy CC0 licence
# blender -b mercury-hero.blend --python pack.py
import bpy
import os
import shutil

BASE = r"C:\Users\daive\Downloads\igem-hero-tier1\tier1-delivery-beauty"
SRC = os.path.join(BASE, 'source')
os.makedirs(SRC, exist_ok=True)

w = bpy.data.worlds['World']
nt = w.node_tree
env = [n for n in nt.nodes if n.type == 'TEX_ENVIRONMENT'][0]
img = env.image
print('HDRI', img.name, img.filepath, 'packed', img.packed_file is not None)
if img:
    try:
        img.pack()
        print('PACKED', img.packed_file is not None)
    except Exception as e:
        print('PACK ERR', repr(e)[:100])
bpy.ops.file.pack_all()
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(SRC, 'mercury-hero.blend'), compress=True)
print('SAVED blend to', os.path.join(SRC, 'mercury-hero.blend'))
lic = r"C:\Users\daive\Downloads\igem-hero-tier1\tier1-delivery\source\HDRI-LICENCE.txt"
if os.path.isfile(lic):
    shutil.copyfile(lic, os.path.join(SRC, 'HDRI-LICENCE.txt'))
    print('LICENCE copied')
print('PACK COMPLETE')
