'''
Created on Jan 28, 2011

@author: Gaurav
'''

import sys
import matplotlib.pyplot as plt
from pylab import *
from reportlab.lib.colors import transparent


def plotGraph2(file):
    data1 = open(file, 'rU')
    axis_names =  data1.readline().split()
    
    xax = axis_names[0]
    yax = axis_names[1]
    
    consensus = []
    for line in data1:
        list = line.split()
        consensus.append(int(list[1]))
    
    
    
    print 'total reads = ', sum(consensus)
    print 'total full length reads = ', consensus[-1]
    print 'total truncated reads = ', sum(consensus[:-1])
    print 'fraction of reads truncated = ' , (sum(consensus[:-1]) / sum(consensus))*1.0
    graph2(consensus, xax, yax)
    
    


def graph2(data,xax, yax):
    length = len(data)
    ys = data
    start = 18
    xs = []
    for base in range(start, start +length):
        base += 1
        xs.append(base)
        
    print 'xs = ', xs
    print 'ys = ', ys
    

    print len(xs)
    print len(ys)
    filen = 's_4_1'
    plt.plot(xs, ys) #makes the plot
    

    plt.title('Read Length distribtion after adapter trimming' )
    plt.xlabel(xax)
    plt.ylabel(yax)
    
   
    #plot.show() #shows the plot
    
    if save:
        plt.savefig(transparent = True, filename = filen)


def main():
    file1 = sys.argv[1]
    
    plotGraph2(file1)
    
    
    
    
if __name__=='__main__':
    main()