# blender-sge
Script that simplifies the process of rendering blender projects with the Sun Grid Engine

# what it already can do
Render a Blender Animation each frame as a single Sun-Grid Job in parallel. Simply enter the command with the following syntax into the console 
   
   python gridrender.py video [file] [from] [to]
  
or for example:
   
   python gridrender.py video test.blend 0 100
   
This would render your test.blend file from frame 0 to 100
