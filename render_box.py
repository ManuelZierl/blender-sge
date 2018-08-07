import bpy
import sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]

# For this script: Thanks to stack-exchange user Leander
# https://blender.stackexchange.com/questions/107343/how-do-i-render-only-part-of-an-image-via-the-command-line

# Syntax render_box
print(sys.argv)
print("######'>", sys.argv[0])

scn = bpy.data.scenes["Scene"]
frame = int(argv[4])
scn.frame_set(frame)

scn.render.filepath = "//render/" + str(argv[5]) + "/" +  str(frame).zfill(6)
for i in range(0, 4):
    scn.render.filepath += "_" + argv[i]


# setup the render border
scn.render.use_border = True
scn.render.border_min_x = float(argv[0])
scn.render.border_max_x = float(argv[1])
scn.render.border_min_y = float(argv[2])
scn.render.border_max_y = float(argv[3])

# render a still frame
bpy.ops.render.render(write_still=True)
print("Success.")

