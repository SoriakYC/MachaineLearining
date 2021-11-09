# -*-coding: utf-8 -*-
# vispy: gallery 30
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
"""
Simple use of SceneCanvas to display a cube with an arcball camera.
"""
import sys

from vispy import scene
from vispy.color import Color

import numpy as np


canvas = scene.SceneCanvas(keys='interactive', size=(800, 600), show=True)

# Set up a viewbox to display the cube with interactive arcball
view = canvas.central_widget.add_view()
#view.bgcolor = '#efefef'
#view.bgcolor = '#ffffff'
view.camera = 'turntable' # 摄像机
view.padding = 10

#color = Color("#3f51b5")
color = Color("#20af20")

nv = 24
vcolor = np.ones((nv, 4), dtype=np.float32)
rng = np.random.RandomState(1)
vcolor[:, 0] = np.linspace(1, 0, nv)
vcolor[:, 1] = rng.randn(nv)
vcolor[:, 2] = np.linspace(0, 1, nv)
vcolor[:, 3] = 0.8

cube = scene.visuals.Cube(size=1, vertex_colors=vcolor, edge_color="black", parent=view.scene) # 立方体
#cube = scene.visuals.Cube(size=1, color=color, edge_color="black", parent=view.scene)
cube.mesh.set_gl_state('additive', blend=True, depth_test=False)


pos = np.array([[1,-1,1],[-1,1,1],
                [1,1,-1],[1,-1,1] ], 
        dtype=np.float32) 
line = scene.visuals.Line(pos=pos, color='brown', parent=view.scene, width=2.0) # 线1

pos2 = np.array([[1,-1,-1],[-1,-1,1],
                [-1,1,-1],[1,-1,-1] ], 
        dtype=np.float32) 
line2 = scene.visuals.Line(pos=pos2, color='pink', parent=view.scene, width=2.0) # 线2

def get_one_third(a,b):
    return a+(b-a)/3.

pos3 = np.array([get_one_third(pos[0], pos[1]),
                 get_one_third(pos[1], pos[2]),
                 get_one_third(pos[2], pos[3]), ], 
        dtype=np.float32) 

pos4 = np.array([get_one_third(pos2[1], pos2[0]),
                 get_one_third(pos2[2], pos2[1]),
                 get_one_third(pos2[3], pos2[2]), ], 
        dtype=np.float32) 
face2 = scene.visuals.Mesh(vertices=pos4, color='pink', parent=view.scene) # 面2

#face1 = scene.visuals.Mesh(vertices=pos3, color='brown', parent=view.scene)
face1 = scene.visuals.Mesh(vertices=pos3, color='#40A0F080', parent=view.scene) # 面1
face1.set_gl_state('additive', blend=True, depth_test=False)

pos_middle = np.array([[1,-1,0],[0,-1,1],
                [-1,0,1],[-1,1,0],
                [0,1,-1], [1,0,-1],
                [1,-1,0] ], 
        dtype=np.float32) 
line_middle = scene.visuals.Line(pos=pos_middle, color='blue', parent=view.scene)

pos_between1 = np.array([pos3[0], pos4[0]])
l1 = scene.visuals.Tube(pos_between1, color=['red', 'green', 'yellow'], shading='smooth', tube_points=8, radius=0.02, parent=view.scene)

pos_between2 = np.array([pos3[1], pos4[1]])
l2 = scene.visuals.Tube(pos_between2, color=['red', 'green', 'yellow'], shading='smooth', tube_points=8, radius=0.02, parent=view.scene)

pos_between3 = np.array([pos3[2], pos4[2]])
l3 = scene.visuals.Tube(pos_between3, color=['red', 'green', 'yellow'], shading='smooth', tube_points=8, radius=0.02, parent=view.scene) # 管

#torus_center = np.zeros((20,2))
nums = 200
tc = np.zeros((nums,3))
theta = np.linspace(0, 1*np.pi, nums)
tc[:, 2] = 0
tc[:, 0] = np.cos(2*np.pi*theta)
tc[:, 1] = np.sin(2*np.pi*theta)
#print(pos_between3)
colors = np.random.random((nums,4))
colors[:,3] = 0.5
colors[:,0] = 0.
#l_torus = scene.visuals.Tube(tc, color=['red', 'green', 'yellow'], shading='smooth', tube_points=8, radius=0.2, parent=view.scene)
#l_torus = scene.visuals.Tube(tc, color=colors, shading='smooth', tube_points=8, radius=0.2, parent=view.scene)

axis = scene.visuals.XYZAxis(width=2.0, parent=view.scene)
axis.set_data(pos=axis.pos*3)

if __name__ == '__main__' and sys.flags.interactive == 0:
    canvas.app.run()
