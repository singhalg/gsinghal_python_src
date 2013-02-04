'''
Created on Jun 14, 2010

@author: Gaurav
'''
import matplotlib.pyplot as plt 
import sys
from pylab import *   #required for legend


'''
This script generates plots from files containing per base scores for repeat elements using matplotlib.

'''


'''
This script takes in four files having consensus scores for a Repeat Element
@param readFile: File containing per base scores from reads (sequencing data)
@param siteFile1: File containing per base scores from one kind of Restriction Site (eg CCGG); similarly siteFile2 and siteFile3  
@param save: Boolean, save the file or not.
@output : plot, which contains read data on one Y axis and Restriction site data on another Y axis. 
'''

def multiGraph4(readFile, siteFile1, siteFile2, siteFile3, save ):
    
    # making a list of scores from readFile
    
    readData = open(readFile, 'rU')
    
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score
       
    repFam = readData.readline().rstrip()
    ind = repFam.find('_') 
    repFamily = repFam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'multiGraph4 repFamily =  ', repFamily
    
    readCon = []
    for line in readData:
        list = line.split()
        readCon.append(int(list[2]))    # list[2] contains the scores.
    
    # making a list of scores from file containing scores for a particular RS
    siteData1 = open(siteFile1, 'rU')
    site1 = siteData1.readline().strip()
    site1name = site1.strip('_sites.bed_score')  # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon1 = []
    for line in siteData1:
        list = line.split()
        siteCon1.append(int(list[2]))
        
    
    siteData2 = open(siteFile2, 'rU')
    site2 = siteData2.readline().strip()
    site2name = site2.strip('_sites.bed_score')
    # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon2 = []
    for line in siteData2:
        list = line.split()
        siteCon2.append(int(list[2]))
    
    
    siteData3 = open(siteFile3, 'rU')
    site3 = siteData3.readline().strip()
    site3name = site3.strip('_sites.bed_score')
    # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon3 = []
    for line in siteData3:
        list = line.split()
        siteCon3.append(int(list[2]))
    
    #once the names of repeat element and RS sites is read and  list of per base scores are made, manyplots4() is called. This method plots 4 curves.
    manyplots4(repFamily, readCon, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save)
       



'''
This script takes in two files having consensus scores for a Repeat Element
@param Consensus: File containing per base scores for a repeat element from hg18 
@param CpGsite: File containing per base scores for CpG Sites (eg CCGG)  
@param save: Boolean, save the file or not.
@output : plot, which contains hg18/hg19 consensus data on one Y axis and CpG site density data on another Y axis. 
'''

def multiGraph2(Consensus, CpGsite, save ):
   
    # making a list of scores from Consensus

    
    CpGdata = open(CpGsite, 'rU')
    site1name = CpGdata.readline().rstrip()
    siteCon1 = []
    for line in CpGdata:
        list = line.split()
        siteCon1.append(int(list[2]))
    
    axislen = len(siteCon1)  # using the no of bases in siteCon to cut down excess of readData
    
    readData = open(Consensus, 'rU')
    repFam = readData.readline().rstrip()
    ind = repFam.find('_')
    repFamily = repFam[:ind]
    print 'multiGraph4 repFamily =  ', repFamily
    readCon = []
    
    
    # in case read data file is longer than other files,     
    i=0
    for line in readData:
        if i < axislen:
            list = line.split()
            readCon.append(int(list[2]))
            i+=1
    
        
    #once the names of repeat element and CpG site is read and list of per base scores are made, manyplots2() is called. This method plots 2 curves.
    manyplots2(repFamily, readCon, site1name, siteCon1, save)
       

'''
This method takes in 4 consensus scores, one for reads, and one each for three restriction sites.
@param repFamily : This string froms the first part of file name and legend for readCon data
@param readCon : This is the per base consensus score for reads.
@param siteCon1 : This is the per base consensus score for restriction site. similarly siteCon2, siteCon3
@param site1name : String, representing the name of the string, and will make the legend. similarly site2name, site3name
'''     
def manyplots4(repFamily, readCon, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save):
    rcParams['legend.loc'] = 'best'    # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11 # manually setting the plot size (width X height)
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
    
    
    filename = repFamily+'_read_RS.png' # plot will be saved with this name
    conlbl = repFamily + ' reads'   #legend for reads data
    line1, = ax1.plot(xs, ys, linewidth = 2.0, color = 'k')
    ax1.set_xlabel('base position in consensus')
    ax1.set_ylabel('per base score from read data', color='k')
    #yticklabels are also kept with the same color as the line so that they can be visually related to each other. 
    for tl in ax1.get_yticklabels():
        tl.set_color('k')
    
    
    #making a twin y - axis, on the right hand side of the plot. This axis is used for plotting Restriction site data. 
    ax2 = ax1.twinx()
    
    
    #plotting the data for restriction site
    line2, = ax2.plot(xs, ys1) 
    line3, = ax2.plot(xs, ys2)
    line4, = ax2.plot(xs, ys3)
    
    ax2.set_ylabel('per base score for Restriction site', color='g')
    for tl in ax2.get_yticklabels():
        tl.set_color('g')
    
    #building legend
    legend((line1, line2, line3, line4),(conlbl, site1name, site2name, site3name))
   
    
    plt.title(repFamily)
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    plt.show()
    
    
'''
This method takes in 2 consensus scores, one for consensus score for a particular repeat element for a hg reference, such as hg18, and one for CpG site density.
@param repFamily : This string froms the first part of file name and legend for readCon data
@param repeatCon : This is the per base consensus score for repeat element.
@param siteCon1 : This is the per base consensus score for CpG site. In other words, this represents the per base density of CpG sites on a repeat element.
@param site1name : this String will make the legend for CpG curve.
'''  
    
def manyplots2(repFamily, repeatCon, site1name, siteCon1, save):
    rcParams['legend.loc'] = 'best'  # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11  # manually setting the plot size (width X height)
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
    
    filename = repFamily+'_CpG.png' # plot will be saved with this name
    conlbl = repFamily + ' Consensus' #legend for hg18/hg19 consensus data
    line1, = ax1.plot(xs, ys, linewidth = 2.0, color = 'b')
    ax1.set_xlabel('base position in consensus')
    ax1.set_ylabel('per base score from consensus (hg18) ', color='b')
    for tl in ax1.get_yticklabels():
        tl.set_color('b')
    
    
    #making a twin y - axis, on the right hand side of the plot. This axis is used for plotting CpG site data. 
    ax2 = ax1.twinx()
    #plotting the data for restriction site
    line2, = ax2.plot(xs, ys1, color = 'g') 

    
    ax2.set_ylabel('per base score for CpG site', color='g')
    for tl in ax2.get_yticklabels():
        tl.set_color('g')
    
    #building legend
    legend((line1, line2),(conlbl, site1name))
   
    
    plt.title(repFamily)
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    plt.show()
    
def main():
    # use either of the two method calls. 
    readFile = sys.argv[1]
    siteFile1 = sys.argv[2]
    siteFile2 = sys.argv[3]
    siteFile3 = sys.argv[4]
    save = sys.argv[5]
    multiGraph4(readFile, siteFile1, siteFile2, siteFile3, save )
    

#    readFile = sys.argv[1]
#    siteFile1 = sys.argv[2]
#    save = sys.argv[3]
#    multiGraph2(readFile, siteFile1, save )
    
    
    
    
if __name__=='__main__':
    main()    