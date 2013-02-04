'''
Created on Jun 27, 2010

@author: Gaurav
'''
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def twoScales():
    
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    t = np.arange(0.01, 10.0, 0.01)
    s1 = np.exp(t)
    ax1.plot(t, s1, 'b-')
    ax1.set_xlabel('time (s)')
    # Make the y-axis label and tick labels match the line color.
    ax1.set_ylabel('exp', color='b')
    for tl in ax1.get_yticklabels():
        tl.set_color('b')


    ax2 = ax1.twinx()
    s2 = np.sin(2*np.pi*t)
    ax2.plot(t, s2, 'r.')
    ax2.set_ylabel('sin', color='r')
    for tl in ax2.get_yticklabels():
        tl.set_color('r')
    plt.show()
    


def try2axis():
    
    
#    rcParams['legend.loc'] = 'best'
    
    
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ys1 = [1,2,5,7,2,100,40,60,300,500,10]
    ys2 = [5,4,3,20,1,2,3,1,5,25,22]
    ys3 = [3,2,5,7,20,4,5,1,7,5, 6]
    xs = [1,2,3,4,5,6,7,8,9,10,11]
    
    
    line1, = ax1.plot(xs, ys1, color = 'r')
    ax1.set_xlabel('time (s)')
  
    # Make the y-axis label and tick labels match the line color.
    ax1.set_ylabel('exp', color='r')
    for tl in ax1.get_yticklabels():
        tl.set_color('r')
    

       
    ax2 = ax1.twinx()
    
    line2, = ax2.plot(xs, ys2, color ='g')
    line3, = ax2.plot(xs, ys3, color ='g')
    ax2.set_ylabel('sin', color='g')
    for tl in ax2.get_yticklabels():
        tl.set_color('g')
        
    
    legend((line1, line2, line3),('x','y','z'))
#    [line1, line2, line3]['x','y','z']
    #legend((ax1, ax2),('label1', 'label2'))
    
    plt.title('Repeat Element')
    plt.grid(True)
    plt.show()
    
    
def main():
    try2axis()
    
    
    
if __name__ == '__main__':
    main()    