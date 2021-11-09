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
theta = np.linspace(0, 6* np.pi, N)
r = 0.5
x = r* np.sin(theta)
z = r* np.cos(theta)
#y = np.zeros(N)
y = np.linspace(0, 1, N)

pos = np.array([x,y,z]).T


# Vispy 程序骨架
canvas = scene.SceneCanvas(title='basic01', keys='interactive', show=True)

viewbox = canvas.central_widget.add_view()
viewbox.camera = 'fly'

axis = scene.visuals.XYZAxis(parent=viewbox.scene)

scatter = scene.visuals.Markers() #散点
viewbox.add(scatter)
pos1 = np.array([pos[0]])
scatter.set_data(pos1)

#line1 = scene.visuals.Line() # 线
# viewbox.add(line1)
#line1.set_data(pos)


line1 = scene.visuals.Line(pos=pos, parent=viewbox.scene) # 线

count = 0
def on_timer(event):
    global count
    count += 1
    count = count % N 
    scatter.set_data(np.array([pos[count]]))
    


timer = app.Timer(connect=on_timer, start=True)
#timer.connect(on_timer)
#timer.start()

Running = True
@canvas.events.key_press.connect
def on_key(event):
    global Running
    if event.key == 'Space':
        if Running:
            timer.stop()
        else:
            timer.start()
        Running= not Running



if __name__ == '__main__' and sys.flags.interactive == 0:
    app.run()
