'''
Created on Jul 24, 2010

@author: Gaurav
'''

import matplotlib.pyplot as plt 
import sys
from pylab import *   #required for legend
from matplotlib.font_manager import FontProperties



def multiGraph3(readFile1, siteFile1, siteFile2, siteFile3, save ):
    
    # making a list of scores from readFile1
    
    read1Data = open(readFile1, 'rU') # normal
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score  
    rep1Fam = read1Data.readline().rstrip()
#    rC1 = read1Data.readline().split()   # this line contains 'total read count' + '/t' + '# of unmatched reads'
#    read1Count = float(rC1[0])
    ind = rep1Fam.find('_') 
    rep1Family = rep1Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element :  ', rep1Family
    read1Con = []
    for line in read1Data:
        list = line.split()
        read1Con.append(int(list[2]))    # list[2] contains the scores.
    
    
    
    # making a list of scores from file containing scores for a particular RS
    siteData1 = open(siteFile1, 'rU')
    site1 = siteData1.readline().strip()
    site1name = site1.strip('_sites.bed_score')  # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon1 = []
    for line in siteData1:
        list = line.split()
        siteCon1.append(int(list[2]))
    
    axislen = len(siteCon1)  
    
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
    
    
    read1Con = read1Con[:axislen]
    #once the names of repeat element and RS sites is read and  list of per base scores are made, manyplots4() is called. This method plots 4 curves.
    manyplots3(rep1Family, read1Con, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save)
       

def manyplots3(rep1Family, read1Con, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save):
    rcParams['legend.loc'] = 'upper right'    # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11 # manually setting the plot size (width X height)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(read1Con)
    ys = read1Con #genome consensus
   
    ys1 = siteCon1
    ys2 = siteCon2
    ys3 = siteCon3
    
#    print 'normal :'
#    print ys
#    print '\n'
    
   
    
    
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    print rep1Family
    print 'xs = ', len(xs)
    print 'ys = ', len(ys)
    
    print 'ys1 = ', len(ys1)
    print 'ys2 = ', len(ys2)
    print 'ys3 = ', len(ys3)
        
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    
    filename = rep1Family+'Cons_RS.png' # plot will be saved with this name
    conlbl = rep1Family + ' Genome Coverage'   #legend for reads data
   # con2Label = rep2Family + ' reads (Cancer)'
    line1, = ax1.plot(xs, ys, linewidth = 1.5, color = 'b')
    line2, = ax1.plot(xs, ys1, color = 'k') 
    line3, = ax1.plot(xs, ys2, color = 'm')
    line4, = ax1.plot(xs, ys3, color = 'c')
    #line5, = ax1.plot(xs, ys4, linewidth = 2.0, color = 'r')
    ax1.set_xlabel('base position in Repeat Element Consensus')
    ax1.set_ylabel('per base score from hg18', color='k')
    #yticklabels are also kept with the same color as the line so that they can be visually related to each other. 
    for tl in ax1.get_yticklabels():
        tl.set_color('k')
    
    
    
    
    #building legend
    legend((line1, line2, line3, line4),(conlbl, site1name, site2name, site3name))
   
    
    plt.title(rep1Family )
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    
    plt.show()
    
    
def main():
    readFile1N = sys.argv[1]
   
    siteFile1 = sys.argv[2]
    siteFile2 = sys.argv[3]
    siteFile3 = sys.argv[4]
    save = sys.argv[5]
    multiGraph3(readFile1N, siteFile1, siteFile2, siteFile3, save )
    
    
if __name__=='__main__':
    main()   