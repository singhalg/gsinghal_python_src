'''
Created on Jun 4, 2010

@author: Gaurav
'''
import sys
from ReadAnalyzer import *


"""
@param file: a file containing per base score for the consensus. The score file has been produced by running Analyzer1.py on RepeatMasker output data, for a particular repeat family. 
@param repFamily: The repeat element specific to the file
@param save : Boolean, save file or not? 

It reads the score file, and produces a list of consensus score, which is exactly the list returned by Analyze.py method in Analyzer1.py

It finally invokes graph method from Analyzer1.py . The name space for Analyzer1.py is imported by ReadAnalyzer.py, whose name space is imported in this script. 
"""

def plotGraph2(file1, file2, repFamily, save):
    data1 = open(file1, 'rU')
    data1.readline()
    data2 = open(file2, 'rU')
    data2.readline()
    consensus1 = []
    consensus2 = []
    for line in data1:
        list = line.split()
        consensus1.append(int(list[2]))
    for line in data2:
        list = line.split()
        consensus2.append(int(list[2]))
    
    
    graph2(consensus1, consensus2, repFamily, save)
    
    
def plotGraph1(file1, repFamily, save):
    data1 = open(file1, 'rU')
    data1.readline()
    consensus1 = []
    
    for line in data1:
        list = line.split()
        consensus1.append(int(list[2]))
    
    
    graph1(consensus1, repFamily, save)


def graph2(data1,data2, repFamily, save):
    length = len(data1)
    ys = data1
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    #print 'xs = ', xs
    #print 'ys = ', ys
    

    print len(xs)
    print len(ys)
    filename = repFamily+'read_site.png'
    plot.plot(xs, ys) #makes the plot
    if save:
        plot.savefig(filename)
##    plot.title(r'Per Base Score for Repeat Element ' )
##    plot.xlabel('Consensus')
##    plot.ylabel('Per Base Score')
##    #plot.show() #shows the plot
    
    
    otherlength = len(data1)
    ys2 = data2
    base = 0
    xs2 = []
    for base in range(otherlength):
        base += 1
        xs2.append(base)
        
    #print 'xs = ', xs
    #print 'ys = ', ys
    

    print len(xs2)
    print len(ys2)
    filename = repFamily+'_site.png'
    plot.plot(xs2, ys2) #makes the plot
#    if save:
#        plot.savefig(filename)
    plot.title(r'Per Base Score for Repeat Element ' )
    plot.xlabel('Consensus')
    plot.ylabel('Per Base Score')
    plot.show() #shows the plot
    
    
def graph1(data1, repFamily, save):

    
    
    length = len(data1)
    ys = data1
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
    filename = repFamily+'_read.png'
    plt.plot(xs, ys, label = 'repFamily') #makes the plot
    plt.title(r'Per Base Score for Repeat Element ' )
    plt.xlabel('Consensus')
    plt.ylabel('Per Base Score')
    legend()
    if save:
        plt.savefig(filename)
    plt.show() #shows the plot
    

def main():
    file1 = sys.argv[1]
    #file2 = sys.argv[2]
    repFamily = sys.argv[2]
    save = sys.argv[3]
    plotGraph1(file1, repFamily, save)
    
    
    
    
if __name__=='__main__':
    main()