# coding=utf-8
# vispy==0.4.0dev
"""
例子1: 螺旋线
"""
import sys
from vispy import scene, app
import numpy as np

# 数据生成
N = 100
theta = np.linspace(0, 6* np.pi, N)
r = 0.5
x = r* np.sin(theta)
z = r* np.cos(theta)
y = np.linspace(0,2,N)

pos = np.array([x,y,z]).T


# Vispy 程序骨架
canvas = scene.SceneCanvas(title='basic01', keys='interactive', show=True)

viewbox = canvas.central_widget.add_view()
viewbox.camera = 'turntable'

axis = scene.visuals.XYZAxis(parent=viewbox.scene)

scatter = scene.visuals.Markers() #散点
viewbox.add(scatter)
scatter_pos = np.array([pos[0]])
scatter.set_data(scatter_pos)

line1 = scene.visuals.Line() # 线
viewbox.add(line1)
line1.set_data(pos)


i  = 0
def on_timer(ev):
    global i, N
    scatter_pos = np.array([pos[i]])
    scatter.set_data(scatter_pos)
    i += 1
    if i >= N:
        i = 0

Running = True
@canvas.events.key_press.connect
def key_press(event):
    global Running
    if event.key == 'Space':
        Running = not Running
        if Running:
            timer.start()
        else:
            timer.stop()

timer = app.Timer()
timer.connect(on_timer)
timer.start()

if __name__ == '__main__' and sys.flags.interactive == 0:
    app.run()
