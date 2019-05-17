# blender-sge
Script that simplifies the process of rendering blender projects with the Sun Grid Engine, or Slurm

# what it already can do
Render a Blender Animation each frame as a single Sun-Grid/Slurm Job in parallel. Simply enter the command with the following syntax into the console
   
   python gridrender.py video [file] [from] [to]

or

   python slurmrender.py video [file] [from] [to]

or for example:
   
   python gridrender.py video test.blend 0 100
   
This would render your test.blend file from frame 0 to 100
______________________________________________________________________________________________________________

Render a single frame split up in multiple Sun-Grid Jobs. The Image is seperated in a Raster. The syntax of the command:

   python gridrender.py image [file] [frame] [horizontal_splits] [vertical_splits]

or

   python slurmrender.py image [file] [frame] [horizontal_splits] [vertical_splits]
   
or for example:
   
   python gridrender.py image test.blend 0 4 4

This would render the frame 0 of the test.blend file split up to 16 jobs
