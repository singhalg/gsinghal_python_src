'''
Created on Jun 14, 2010

@author: Gaurav
'''

import matplotlib.pyplot as plt
#import matplotlib.legend as lgd
import numpy as npy
from pylab import *
#rcParams['legend.loc'] = 'best'
def many():
    xs1 = [1,2,3,4,5,6,7,8,9]
    ys1 = [5,4,3,2,1,2,3,4,5]
    
    ys2 = [1,2,3,4,5,4,3,2,1]
    
    line1 =  plt.plot(xs1, ys1, label = 'line1')
    line2 =  plt.plot(xs1, ys2, label = 'line2')
    legend()
    plt.xlabel('something')
    plt.ylabel('somethingsomething')
    plt.title('title')
    
    plt.savefig('2lines')
   
    
    
    plt.show()
    
def main():
    many()

if __name__ == '__main__':
    main()
    