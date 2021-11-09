'''
11.03作业
需要安装 imageio 库，得到的图片在 animation.gif 里面，本文参考
https://vispy.org/gallery/scene/save_animation.html#sphx-glr-gallery-scene-save-animation-py
能力所限，不会写经纬线斑斓的变化的部分。
'''
import imageio
from numpy import cos,sin,deg2rad
from vispy import scene
from vispy.visuals.transforms import MatrixTransform

output_filename='animation.gif'
n_steps=36
step_angle=180/n_steps
rotate_angle=30
polar_angle=20

canvas=scene.SceneCanvas(keys='interactive',bgcolor='white',size=(800,600),show=True)
view=canvas.central_widget.add_view()
view.camera='arcball'
sphere2=scene.visuals.Sphere(radius=1,cols=24,rows=12,method='latitude',parent=view.scene,color=(.1,.2,.5,.4),edge_color=(0.5,0,0,1))

tr=MatrixTransform()
tr.rotate(rotate_angle,(cos(deg2rad(polar_angle)),sin(deg2rad(polar_angle)),0))
sphere2.transform=tr
view.camera.set_range(x=[-3,3])
writer=imageio.get_writer(output_filename)
for i in range(n_steps):
    im=canvas.render()
    view.camera.transform.rotate(step_angle,[sin(deg2rad(rotate_angle))*sin(deg2rad(polar_angle)),-sin(deg2rad(rotate_angle))*cos(deg2rad(polar_angle)),cos(deg2rad(rotate_angle))])
    writer.append_data(im)
writer.close()