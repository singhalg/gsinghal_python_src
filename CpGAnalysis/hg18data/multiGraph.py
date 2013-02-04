'''
Created on Jun 14, 2010

@author: Gaurav
'''
import matplotlib.pyplot as plt
import sys
from pylab import *
from matplotlib.font_manager import FontProperties

"""
This script takes in four files having consensus scores for a Repeat Element
@param readFile: File containing scores from reads
@param siteFile1: File containing scores from one kind of Restriction Site (eg CCGG); similarly siteFile2 and siteFile3  
@param save: Boolean, save the file or not.
"""

def multiGraph4(readFile, siteFile1, siteFile2, siteFile3, save ):
    
    # making a list of scores from readFile
    readData = open(readFile, 'rU')
    repFam = readData.readline().strip()
    repFamily = repFam.strip('_read_score')
    
    readCon = []
    for line in readData:
        list = line.split()
        readCon.append(int(list[2]))
    
    # making a list of scores from file containing scores for a particular RS
    siteData1 = open(siteFile1, 'rU')
    site1 = siteData1.readline().strip()
    site1name = site1.strip('_sites.bed_score')
    siteCon1 = []
    for line in siteData1:
        list = line.split()
        siteCon1.append(int(list[2]))
        
    
    siteData2 = open(siteFile2, 'rU')
    site2 = siteData2.readline().strip()
    site2name = site2.strip('_sites.bed_score')
    siteCon2 = []
    for line in siteData2:
        list = line.split()
        siteCon2.append(int(list[2]))
    
    
    siteData3 = open(siteFile3, 'rU')
    site3 = siteData3.readline().strip()
    site3name = site3.strip('_sites.bed_score')
    siteCon3 = []
    for line in siteData3:
        list = line.split()
        siteCon3.append(int(list[2]))
    
    
    manyplots4(repFamily, readCon, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save)
       

def multiGraph2(Consensus, CpGsite, save ):
   
    # making a list of scores from Consensus
    readData = open(Consensus, 'rU')
    
    repFam = readData.readline().strip()
    repFamily = repFam.strip('_score')
    readCon = []
    
    CpGdata = open(CpGsite, 'rU')
    site1name = CpGdata.readline().rstrip()
    siteCon1 = []
    for line in CpGdata:
        list = line.split()
        siteCon1.append(int(list[2]))
    
    axislen = len(siteCon1)
    
    
    
    
    i=0
    for line in readData:
        if i < axislen:
            list = line.split()
            readCon.append(int(list[2]))
            i+=1
           
    
    # making a list of scores from file containing scores for a particular RS
    
        
    
    manyplots2(repFamily, readCon, site1name, siteCon1, save)
       

'''
This method takes in 4 consensus scores, one for reads, and one each for three restriction sites.
@param repFamily : This string froms the first part of file name and legend for readCon data
@param readCon : This is the per base consensus score for reads.
@param siteCon1 : This is the per base consensus score for restriction site. similarly siteCon2, siteCon3
@param site1name : String, representing the name of the string, and will make the legend. similarly site2name, site3name
'''     
def manyplots4(repFamily, readCon, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save):
    rcParams['legend.loc'] = 'best'
    rcParams['figure.figsize'] = 16, 11
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(readCon)
    ys = readCon
    ys1 = siteCon1
    ys2 = siteCon2
    ys3 = siteCon3
    
    
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    filename = repFamily+'_read_RS.png'
    conlbl = repFamily + ' reads'
    line1, = ax1.plot(xs, ys, linewidth = 2.0, color = 'k')
    ax1.set_xlabel('base position in consensus')
    ax1.set_ylabel('per base score from read data', color='k')
    for tl in ax1.get_yticklabels():
        tl.set_color('k')
    
    
    
    ax2 = ax1.twinx()
    
    line2, = ax2.plot(xs, ys1) 
    line3, = ax2.plot(xs, ys2)
    line4, = ax2.plot(xs, ys3)
    
    ax2.set_ylabel('per base score for Restriction site', color='g')
    for tl in ax2.get_yticklabels():
        tl.set_color('g')
    
    legend((line1, line2, line3, line4),(conlbl, site1name, site2name, site3name))
   
    
    plt.title(repFamily.strip('_read_score'))
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    plt.show()
    
    
def manyplots2(repFamily, repeatCon, site1name, siteCon1, save):
    rcParams['legend.loc'] = 'best'
    rcParams['figure.figsize'] = 16, 11
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(repeatCon)
    ys = repeatCon
    
    ys1 = siteCon1
        
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    filename = repFamily+'_CpG.png'
    conlbl = repFamily + ' Consensus'
    line1, = ax1.plot(xs, ys, linewidth = 2.0, color = 'b')
    ax1.set_xlabel('base position in consensus')
    ax1.set_ylabel('per base score from consensus (hg18) ', color='b')
    for tl in ax1.get_yticklabels():
        tl.set_color('b')
    
    
    
    ax2 = ax1.twinx()
    
    line2, = ax2.plot(xs, ys1, color = 'g') 

    
    ax2.set_ylabel('per base score for CpG site', color='g')
    for tl in ax2.get_yticklabels():
        tl.set_color('g')
    
    legend((line1, line2),(conlbl, site1name))
   
    
    plt.title(repFamily.strip('_read_score'))
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    plt.show()
    
def main():
    
    
    
    readFile = sys.argv[1]
    siteFile1 = sys.argv[2]
#    siteFile2 = sys.argv[3]
#    siteFile3 = sys.argv[4]
    
    save = sys.argv[3]
    multiGraph2(readFile, siteFile1, save )
    #, siteFile2, siteFile3,
if __name__=='__main__':
    main()
    
    
    
    