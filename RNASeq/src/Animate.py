'''
Created on Mar 17, 2011

@author: Gaurav
'''
#import time
#import numpy as np
#import matplotlib
#matplotlib.use('GTKAgg') # do this before importing pylab
#
#import matplotlib.pyplot as plt
#
#fig = plt.figure()
#
#ax = fig.add_subplot(111)
#
#def animate():
#    tstart = time.time()                 # for profiling
#    x = np.arange(0, 2*np.pi, 0.01)        # x-array
#    line, = ax.plot(x, np.sin(x))
#
#    for i in np.arange(1,200):
#        line.set_ydata(np.sin(x+i/10.0))  # update the data
#        fig.canvas.draw()                         # redraw the canvas
#    print 'FPS:' , 200/(time.time()-tstart)
#    raise SystemExit
#
#import gobject
#print 'adding idle'
#gobject.idle_add(animate)
#print 'showing'
#plt.show()



##!/usr/bin/env python
#import numpy as np
#import pylab as P
#
##
## The hist() function now has a lot more options
##
#
##
## first create a single histogram
##
#
#
#
#
##
## histogram has the ability to plot multiple data in parallel ...
## Note the new color kwarg, used to override the default, which
## uses the line color cycle.
##
##!/usr/bin/env python
#import numpy as np
#import pylab as P
#
##
## The hist() function now has a lot more options
##
#
##
## first create a single histogram
##mu, sigma = 200, 25
#
#
#
#
##
## finally: make a multiple-histogram of data-sets with different length
##
#x0 = mu + sigma*P.randn(10000)
#x1 = mu + sigma*P.randn(7000)
#x2 = mu + sigma*P.randn(3000)
#
## and exercise the weights option by arbitrarily giving the first half
## of each series only half the weight of the others:
#
#w0 = np.ones_like(x0)
#w0[:len(x0)/2] = 0.5
#w1 = np.ones_like(x1)
#w1[:len(x1)/2] = 0.5
#w2 = np.ones_like(x2)
#w0[:len(x2)/2] = 0.5
#
#
#
#P.figure()
#
#n, bins, patches = P.hist( [x0,x1,x2], 10, weights=[w0, w1, w2], histtype='bar')
#
#P.show()



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#mu, sigma = 4, 1
#x = [3,50,4,3,2,4,2,1,1,1,1,3,4,65,7,4,6,3,53,4,54,4,3,22,32]
#
#fig = plt.figure()
#ax = fig.add_subplot(111)
#
## the histogram of the data
#n, bins, patches = ax.hist(x, 100, normed=1, facecolor='green', alpha=0.75)
#
## hist uses np.histogram under the hood to create 'n' and 'bins'.
## np.histogram returns the bin edges, so there will be 50 probability
## density values in n, 51 bin edges in bins and 50 patches.  To get
## everything lined up, we'll compute the bin centers
#bincenters = 0.5*(bins[1:]+bins[:-1])
## add a 'best fit' line for the normal PDF
#y = mlab.normpdf( bincenters, mu, sigma)
#l = ax.plot(bincenters, y, 'r--', linewidth=1)
#
#ax.set_xlabel('Smarts')
#ax.set_ylabel('Probability')
##ax.set_title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
#ax.set_xlim(0, 100)
#ax.set_ylim(0, 0.5)
#ax.grid(True)
#
#plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt


def energySurface():

    step = 0.04
    maxval = 1.0
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')



# create supporting points in polar coordinates
    r = np.linspace(0,1.25,50)
    p = np.linspace(0,2*np.pi,50)
    R,P = np.meshgrid(r,p)
# transform them to cartesian system
    X,Y = R*np.cos(P),R*np.sin(P)

    Z = ((R**2 - 1)**2)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet)
    ax.set_zlim3d(0, 1)
    ax.set_xlabel(r'$\phi_\mathrm{real}$')
    ax.set_ylabel(r'$\phi_\mathrm{im}$')
    ax.set_zlabel(r'$V(\phi)$')
    ax.set_xticks([])
    plt.show()



def main ():

    energySurface()
    
if __name__ == '__main__':
    main()