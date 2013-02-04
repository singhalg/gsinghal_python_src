'''
Created on Jul 24, 2010

@author: Gaurav
'''
'''
This script takes in two files having consensus scores for a Repeat Element
@param Consensus: File containing per base scores for a repeat element from hg18 
@param CpGsite: File containing per base scores for CpG Sites (eg CCGG)  
@param save: Boolean, save the file or not.
@output : plot, which contains hg18/hg19 consensus data on one Y axis and CpG site density data on another Y axis. 
'''

import matplotlib.pyplot as plt 
import sys
from pylab import *   #required for legend
from matplotlib.font_manager import FontProperties


def multiGraph1(Consensus, save ):
   
    # making a list of scores from Consensus

#    axislen = len(siteCon1)  # using the no of bases in siteCon to cut down excess of readData
    len = open(Consensus, 'rU')
    len.readline()
    i = 0
    for line in len:
        i+=1
    len.close()
    
    
    axislen = (i/2) + (i/20)
    readData = open(Consensus, 'rU')
    repFam = readData.readline().rstrip()
    ind = repFam.find('_')
    repFamily = repFam[:ind]
    print 'multiGraph4 repFamily =  ', repFamily
    readCon = []
    
    
    # in case read data file is longer than other files,     
    
    for line in readData:
        list = line.split()
        readCon.append(int(list[2]))
            
    readCon = readCon[:axislen]     
    #once the names of repeat element and CpG site is read and list of per base scores are made, manyplots2() is called. This method plots 2 curves.
    manyplots1(repFamily, readCon, save)
    
    
'''
This method takes in 2 consensus scores, one for consensus score for a particular repeat element for a hg reference, such as hg18, and one for CpG site density.
@param repFamily : This string froms the first part of file name and legend for readCon data
@param repeatCon : This is the per base consensus score for repeat element.
@param siteCon1 : This is the per base consensus score for CpG site. In other words, this represents the per base density of CpG sites on a repeat element.
@param site1name : this String will make the legend for CpG curve.
'''  
    
def manyplots1(repFamily, repeatCon, save):
    font0 = FontProperties()
    rcParams['legend.loc'] = 'upper right'  # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11  # manually setting the plot size (width X height)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(repeatCon)
    ys = repeatCon
    
    
        
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    filename = repFamily+'.png' # plot will be saved with this name
    conlbl = repFamily + ' Genome Coverage' #legend for hg18/hg19 consensus data
    line1, = ax1.plot(xs, ys, linewidth = 1.5, color = 'b', label = conlbl)
    ax1.set_xlabel('base position in Repeat Element consensus')
    ax1.set_ylabel('per base score from hg18', color='k')
    for tl in ax1.get_yticklabels():
        tl.set_color('k')
    
   
    #building legend
    legend()
   
    
    plt.title(repFamily)
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    plt.show()
  
def main():
    Consensus = sys.argv[1]
    save = sys.argv[2]
    multiGraph1(Consensus, save)
    
if __name__=='__main__':
    main()
