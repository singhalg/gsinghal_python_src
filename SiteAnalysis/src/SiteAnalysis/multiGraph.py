'''
Created on Jun 14, 2010

@author: Gaurav
'''
import matplotlib.pyplot as plt
import sys
from pylab import *

"""
This script takes in four files having consensus scores for a Repeat Element
@param readFile: File containing scores from reads
@param siteFile1: File containing scores from one kind of Restriction Site (eg CCGG); similarly siteFile2 and siteFile3  
@param save: Boolean, save the file or not.
"""

def multiGraph(readFile, siteFile1, siteFile2, siteFile3, save ):
    
    # making a list of scores from readFile
    readData = open(readFile, 'rU')
    repFamily = readData.readline().rstrip()
    readCon = []
    for line in readData:
        list = line.split()
        readCon.append(int(list[2]))
    
    # making a list of scores from file containing scores for a particular RS
    siteData1 = open(siteFile1, 'rU')
    site1name = siteData1.readline().rstrip()
    siteCon1 = []
    for line in siteData1:
        list = line.split()
        siteCon1.append(int(list[2]))
        
    
    siteData2 = open(siteFile2, 'rU')
    site2name = siteData2.readline().rstrip()
    siteCon2 = []
    for line in siteData2:
        list = line.split()
        siteCon2.append(int(list[2]))
    
    
    siteData3 = open(siteFile3, 'rU')
    site3name = siteData3.readline().rstrip()
    siteCon3 = []
    for line in siteData3:
        list = line.split()
        siteCon3.append(int(list[2]))
    
    
    manyplots(repFamily, readCon, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save)
       

'''
This method takes in 4 consensus scores, one for reads, and one each for three restriction sites.
@param repFamily : This string froms the first part of file name and legend for readCon data
@param readCon : This is the per base consensus score for reads.
@param siteCon1 : This is the per base consensus score for restriction site. similarly siteCon2, siteCon3
@param site1name : String, representing the name of the string, and will make the legend. similarly site2name, site3name
'''     
def manyplots(repFamily, readCon, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save):
    rcParams['legend.loc'] = 'best'
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
    filename = repFamily+'_RS.png'
    plt.plot(xs, ys, linewidth = 2.0, label = repFamily)
    plt.plot(xs, ys1, label = site1name) 
    plt.plot(xs, ys2, label = site2name)
    plt.plot(xs, ys3, label = site3name)
    legend()
    plt.xlabel('base position in consensus')
    plt.ylabel('per base score')
    plt.title('Per base representation for Repeat Element' + repFamily)
   
    if save:
        plt.savefig(filename)
    plt.show()
    
    
    
def main():
    
    readFile = sys.argv[1]
    siteFile1 = sys.argv[2]
    siteFile2 = sys.argv[3]
    siteFile3 = sys.argv[4]
    save = sys.argv[5]
    multiGraph(readFile, siteFile1, siteFile2, siteFile3, save )
    
if __name__=='__main__':
    main()
    
    
    
    