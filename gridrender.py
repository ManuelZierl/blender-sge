import os
import sys
from subprocess import call

# syntax python gridrender.py video [file] [from] [to]
import time

if sys.argv[1] == "video":
    file = sys.argv[2]
    name = file[0:len(file) - 6]
    print(name)

    start = int(sys.argv[3])
    end = int(sys.argv[4])

    # erstelle Jobs
    i = start
    filelist = []
    imageList = []
    while i <= end:
        n = "00000000000000" + str(i)
        n = n[len(n) - 5:len(n)]
        print(n)
        with open("r" + n + ".sh", "w") as text_file:
            text_file.write("blender -b " + file + " -x 1 -o //render/" + name + "/ -f " + str(i))

        filelist.append("r" + n + ".sh")

        i += 1

    try:
        os.makedirs("render/" + name)
    except:
        pass

    for f in filelist:
        call(["qsub", "-V", "-b", "n", "-cwd", f])

    # ...
    time.sleep(1)

    # Loesche Jobs
    for f in filelist:
        os.remove(f)

    with open("render/" + name + "/finalize.py", "w") as text_file:
        string = 'from subprocess import call' + '\n' + 'call(["ffmpeg", "-r", "25", "-i", "%04d.png", "-vb", "20M", "-vcodec", "mpeg4", "-y", "movie.mp4"])'
        text_file.write(string)

# syntax python gridrender.py image [file] [frame] [horizontal_splits] [vertical_splits]
if sys.argv[1] == "image":

    file = sys.argv[2]
    frame = int(sys.argv[3])

    horizontal_step, vertical_step = 1.0/int(sys.argv[4]), 1.0/int(sys.argv[5])
    i = 0
    j = 0
    filelist = []
    while horizontal_step <= 1:
        vertical_step = 1.0 / int(sys.argv[5])
        while vertical_step <= 1:

            with open("r_" + str(i) + "_" + str(j) + ".sh", "w") as text_file:
                text_file.write("blender -b untitled.blend --python render_box.py -- "   + str((horizontal_step - 1.0/int(sys.argv[4]))) + " "
                                                                                   + str(horizontal_step) + " "
                                                                                   + str((vertical_step - 1.0 / int(sys.argv[5]))) + " "
                                                                                   + str(vertical_step) + " "
                                                                                   + str(frame) + " "
                                                                                   + file[0:len(file) - 6])

            filelist.append("r_" + str(i) + "_" + str(j) + ".sh")
            j += 1
            vertical_step += 1.0 / int(sys.argv[5])
        i += 1
        horizontal_step += 1.0 / int(sys.argv[4])


    for f in filelist:
        os.system("qsub -V -b n -cwd " + f)
        call(["qsub", "-V", "-b", "n", "-cwd", f])

    # ...
    time.sleep(1)

    # Loesche Jobs
    for f in filelist:
        os.remove(f)