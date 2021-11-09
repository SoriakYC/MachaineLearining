# -*- coding: utf-8 -*-
import numpy as np
from vispy import plot as vp

t = np.linspace(0,2,201)
x = np.cos(2 * np.pi * t)
y = (t-1)**2

fig = vp.Fig(size=(600, 800), show=False)
fig[0,0].plot(np.array((t,x)).T, marker_size=0)
fig[1,0].plot(np.array((t,y)).T, marker_size=0)
fig.show(run=True)
