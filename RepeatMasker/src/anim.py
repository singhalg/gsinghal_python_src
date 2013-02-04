'''
Created on Jun 8, 2010

@author: Gaurav
'''
# For detailed comments on animation and the techniqes used here, see
# the wiki entry http://www.scipy.org/Cookbook/Matplotlib/Animations

import matplotlib
matplotlib.use('TkAgg')
from pylab import *

import sys
import pylab as p
import numpy as npy
import time
import matplotlib.pyplot as plt

print matplotlib.__version__


def sine():
    ax = p.subplot(111)
    canvas = ax.figure.canvas
    
    
    # create the initial line
    x = npy.arange(0,2*npy.pi,0.01)
    line, = p.plot(x, npy.sin(x), animated=True, lw=2)
    
    def run(*args):
        background = canvas.copy_from_bbox(ax.bbox)
        # for profiling
        tstart = time.time()
    
        while 1:
            # restore the clean slate background
            canvas.restore_region(background)
            # update the data
            line.set_ydata(npy.sin(x+run.cnt/10.0))
            # just draw the animated artist
            ax.draw_artist(line)
            # just redraw the axes rectangle
            canvas.blit(ax.bbox)
    
            if run.cnt==1000:
                # print the timing info and quit
                print 'FPS:' , 1000/(time.time()-tstart)
                sys.exit()
    
            run.cnt += 1
    run.cnt = 0
    
    
    p.subplots_adjust(left=0.3, bottom=0.3) # check for flipy bugs
    p.grid() # to ensure proper background restore
    manager = p.get_current_fig_manager()
    manager.window.after(100, run)
    
    p.show()
    
    
def more(): 
    import time, sys
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    def data_gen():
        t = data_gen.t
        data_gen.t += 0.05
        return np.sin(2*np.pi*t) * np.exp(-t/10.)
    data_gen.t = 0
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line, = ax.plot([], [], animated=True, lw=2)
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 5)
    ax.grid()
    xdata, ydata = [], []
    def run(*args):
        background = fig.canvas.copy_from_bbox(ax.bbox)
        # for profiling
        tstart = time.time()
    
        while 1:
            # restore the clean slate background
            fig.canvas.restore_region(background)
            # update the data
            t = data_gen.t
            y = data_gen()
            xdata.append(t)
            ydata.append(y)
            xmin, xmax = ax.get_xlim()
            if t>=xmax:
                ax.set_xlim(xmin, 2*xmax)
                fig.canvas.draw()
                background = fig.canvas.copy_from_bbox(ax.bbox)
    
            line.set_data(xdata, ydata)
    
            # just draw the animated artist
            ax.draw_artist(line)
            # just redraw the axes rectangle
            fig.canvas.blit(ax.bbox)
    
            if run.cnt==1000:
                # print the timing info and quit
                print 'FPS:' , 1000/(time.time()-tstart)
                sys.exit()
    
            run.cnt += 1
    run.cnt = 0
    
    
    
    manager = plt.get_current_fig_manager()
    manager.window.after(100, run)
    
    plt.show()   
    

def simple():
    
    x = randn(10000)
    hist(x, 100)

def dots():   
    import pylab as P
    from matplotlib.transforms import offset_copy
    
    X = P.arange(7)
    Y = X**2
    
    fig = P.figure(figsize=(5,10))
    ax = P.subplot(2,1,1)
    
    # If we want the same offset for each text instance,
    # we only need to make one transform.  To get the
    # transform argument to offset_copy, we need to make the axes
    # first; the subplot command above is one way to do this.
    
    transOffset = offset_copy(ax.transData, fig=fig,
                                x = 0.05, y=0.10, units='inches')
    
    for x, y in zip(X, Y):
        P.plot((x,),(y,), 'ro')
        P.text(x, y, '%d, %d' % (int(x),int(y)), transform=transOffset)
    
    
    # offset_copy works for polar plots also.
    
    ax = P.subplot(2,1,2, polar=True)
    
    transOffset = offset_copy(ax.transData, fig=fig, y = 6, units='dots')
    
    for x, y in zip(X, Y):
        P.polar((x,),(y,), 'ro')
        P.text(x, y, '%d, %d' % (int(x),int(y)),
                    transform=transOffset,
                    horizontalalignment='center',
                    verticalalignment='bottom')
    
    
    P.show()

def somedots():
    
    
    def millions(x):
        return '$%1.1fM' % (x*1e-6)
    
    x =     rand(20)
    y =     1e7*rand(20)
    
    ax = subplot(111)
    ax.fmt_ydata = millions
    plot(x, y, 'line')
    
    show()




def oneline():
    plt.plot([1,2,3,4,8,9,10, 15, 16,17,20,21,22,23,24,25],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3], '_')
    plt.plot([1,2,3,4,8,9,10, 15, 16,17,20,21,22,23,24,25],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4], '_')
    plt.ylabel('one line')
    plt.axis([0,100, 0,1000])
    plt.show()
    plt.savefig('filename')
    


def trynumpy():
    t= npy.arange(0.0, 10.0, 0.1)
    t2 = t*2
    t3 = t*3
    
    #plt.plot(t, t, linewidth = 2.0, 'r--')
    plt.show()



def main():
    dots()

if __name__=='__main__':
    main()