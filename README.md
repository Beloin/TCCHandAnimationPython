# Animation

We can follow [this](https://rdmilligan.wordpress.com/2015/11/30/blender-animation-in-opengl-mark-ii/) tutorial to create a list of models with the frames of animation. A little bad to be honest, and too inefficient.

To make animation we saved each frame of the animation as a different model and placed in folders.

# Load model:

We can manually load a model using the following python code to export as plain text:

```python
import bpy

obj = bpy.context.object
mesh = obj.data


file1 = open("/home/beloin/Documents/aulas/hand-animation-py/animations/test_vertices.txt", 'a')
for vert in mesh.vertices:
   xyz = vert.co.xyz
   print(f"{xyz[0]}, {xyz[1]}, {xyz[2]}")
   file1.write(f"({xyz[0]}, {xyz[1]}, {xyz[2]}),\n")



for face in mesh.polygons:
   print(f"{face.vertices[0]}, {face.vertices[1]}, {face.vertices[2]}")
  file2 = open("/home/beloin/Documents/aulas/hand-animation-py/animations/faces.txt", 'a')
  file2.write(f"({face.vertices[0]}, {face.vertices[1]}, {face.vertices[2]}),\n")
```

Or we can use the `./loader.py` or use `loader.py` to load direct using `*.obj` and `*.mtl`.
