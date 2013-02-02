'''
Created on Jan 22, 2011

@author: Gaurav
'''
from pylab import *
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

delta = 15.0 # degrees

angles = arange(0, 360+delta, delta)
ells = [Ellipse((1, 1), 4, 1, a) for a in angles]

a = plt.subplot(111, aspect='equal')

for e in ells:
    e.set_clip_box(a.bbox)
    e.set_alpha(0.1)
    a.add_artist(e)

plt.xlim(-2, 4)
plt.ylim(-1, 3)

plt.show()
plt.savefig('some')