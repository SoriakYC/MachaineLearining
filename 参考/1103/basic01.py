# coding=utf-8
# vispy==0.4.0dev
"""
基础例子
"""
import sys
from vispy import scene, app
import numpy as np

# 数据生成
N = 100
theta = np.linspace(0, 2* np.pi, N)
r = 1.0
x = r* np.sin(theta)
z = r* np.cos(theta)
y = np.zeros(N)

pos = np.array([x,y,z]).T


# Vispy 程序骨架
canvas = scene.SceneCanvas(title='basic01', keys='interactive', show=True)

viewbox = canvas.central_widget.add_view()
viewbox.camera = 'turntable'

axis = scene.visuals.XYZAxis(parent=viewbox.scene)

scatter = scene.visuals.Markers() #散点
viewbox.add(scatter)
scatter.set_data(pos)

line1 = scene.visuals.Line() # 线
viewbox.add(line1)
line1.set_data(pos)

if __name__ == '__main__' and sys.flags.interactive == 0:
    app.run()
