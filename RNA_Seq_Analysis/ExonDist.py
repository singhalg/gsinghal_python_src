'''
Created on Mar 15, 2011

@author: Gaurav
'''

#-------------------------------------------------------------------#
# Author: Gaurav Singhal                                            #
# Created : March 15, 2011                                          #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#
import numpy as np
from math import sqrt
import matplotlib.mlab as mlab
from sets import Set
import sys
import matplotlib.pyplot as plt 
from pylab import *   #required for legend
from array import array
from matplotlib.font_manager import FontProperties

def exonDist(filename):
    inFile = open(filename, 'rU')
    # initiate a long array
    
    genesFile = inFile.readlines()
    arrayGenes = []
    incompl = 0
    duplicate = 0
    singleExon = 0
    x = 0
    num  = 0
    while x < 600000:
        arrayGenes.append(num)
        x+=1
    
    
    genes = Set([])
    
    
    print ' Genes which have their second Exon more than 600 kb away from TSS :'
    for line in genesFile:
        aGene = geneParser(line)
        
        
        if aGene[13]=='cmpl' and aGene[14]=='cmpl':
            if aGene[12] not in genes:
                genes.add(aGene[12])
                if aGene[3] == '+' :
                    TSS = int(aGene[4])
                    exons = aGene[9].split(',')
                    if len(exons)>2:
                        dist = int(exons[1]) - TSS
                        if dist<600000:
                            arrayGenes[dist] += 1
                        else: print line
                    else: singleExon+=1
            
                elif aGene[3] == '-':
                    TSS = int(aGene[5])
                    exons = aGene[10].split(',')
                    if len(exons)>2:
                        dist = TSS - int(exons[-3])
                        if dist<600000:
                            arrayGenes[dist] += 1
                        else : print line
                    else:singleExon+=1
            else : 
                duplicate+=1
        else:
            incompl+= 1
            
    print 'There are ',str(len(genesFile)),' entries in refGene.txt'
    print 'Incomplete genes are excluded from analysis. # of incomplete genes is : ', str(incompl)

    print 'We are now left with ', str(len(genesFile) - incompl)   ,' genes '
    
    print 'Only one entry per gene is considered in this analysis.# non unique entries  (as per gene name) are in refGene.txt is : ', str(duplicate)
    print 'We are now left with ', str(len(genes)) ,' unique genes (as per gene name).'
 
    print '# of genes with just one exon : ', str(singleExon)
    
    
    print 'We are now left with ', str(len(genesFile)), ' - ', str(incompl) ,' - ' , str(duplicate), ' - ',  str(singleExon), ' = ', str(len(genesFile) - incompl - duplicate - singleExon), ' genes' 
 
 
    print 'We excluded 5 genes who had there first exons > 600 kb away from TSS'
    
    totalGenes = sum(arrayGenes)
    print 'So, the total number of genes analyzes here is '+ str(totalGenes)
    ninetyPer = 0.9*totalGenes
    ninetyFivePer = 0.95*totalGenes   
    ninetyEight = 0.98*totalGenes
    
    print '90% genes = ', str(ninetyPer) , '; 95% genes = ', str(ninetyFivePer), '; 98% genes = ', str(ninetyEight)
    
    genesPerKb = []
    
    ninetySwitch = True
    ninetyFiveSwitch = True
    ninetyEightSwitch = True
    
    n = 0
    while n < 600000:
        ceiling = n+1000
        sumPerKb = sum(arrayGenes[n:ceiling])
        genesPerKb.append(sumPerKb)
        
        n+=1000
     
    
    length = len(genesPerKb)
     
    for bucket in range(length):
        
        if sum(genesPerKb[0:bucket]) > ninetyPer and ninetySwitch == True:
            print '90% of genes have their second exon within ', str(bucket), 'kb from TSS.' 
            ninetySwitch = False
        if sum(genesPerKb[0:bucket]) > ninetyFivePer and ninetyFiveSwitch == True:
            print '95% of genes have their second exon within ', str(bucket), 'kb from TSS.' 
            ninetyFiveSwitch = False 
        if sum(genesPerKb[0:bucket]) > ninetyEight and ninetyEightSwitch == True:
            print '98% of genes have their second exon within ', str(bucket), 'kb from TSS.' 
            ninetyEightSwitch = False

#    histogram(genesPerKb)   
    manyplots2(genesPerKb)
#    manyplots2(arrayGenes)



def filterOutDup(overlapFile):
    overLapFile = open(overlapFile, 'rU')
    
    firstline = overLapFile.readline()
    
    entry = organizeRepeat(firstline)
    firstGene = organizeGene(firstline)
    
    
    repeats = Set([entry])
    genes = Set([firstGene])
    outname = overlapFile[:-4]+'_unique_rep_v2.bed'

    uniqueOut = open(outname, 'w')
    
    uniqueOut.write(firstline)


        
    for line in overLapFile:
        repnum = organizeRepeat(line)
        gene = organizeGene(line)
        if repnum not in repeats:
            genes.add(gene)
            uniqueOut.write(line)
            repeats.add(repnum)
        elif gene not in genes:
            print 'found a repeat overlapping 2 genes'
            print line
            genes.add(gene)
            uniqueOut.write(line)
        
    uniqueOut.close()
                     
            
def histogram(arrayGenes):
    
    arrayG = np.array(arrayGenes)
    mean = arrayG.mean()
    std = arrayG.std()
    print 'mean = ', mean
    print 'std = ', std
#    mu, sigma = 100, 15
#    x = mu + sigma * np.random.randn(100)
#    
#    print np.random.randn(2)
#    
#    for each in x:
#        print each
# the histogram of the data
    n, bins, patches = plt.hist(arrayG, 60, normed=1, facecolor='g', alpha=0.75)


    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([0, 1000, 0, 1000])
    plt.grid(True)
    plt.show()
            
def manyplots2(arrayGenes):
    rcParams['legend.loc'] = 'best'  # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11  # manually setting the plot size (width X height)
    fig = plt.figure()
    
    
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(0,200), ylim=(0,1500))
    length = len(arrayGenes)
    ys = arrayGenes
    
    
        
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    filename = 'TSStoExon2.png' # plot will be saved with this name
    conlbl = 'distance from TSS to second Exon' #legend for hg18/hg19 consensus data


    line1, = ax.plot(xs, ys, linewidth = 1.2, color = 'b')
    
    

#    ax.annotate('axes center', xy=(.5, .5),  xycoords='axes fraction',
#                horizontalalignment='center', verticalalignment='center')
#
#    ax.annotate('pixels', xy=(20, 20),  xycoords='figure pixels')
#
#    ax.annotate('points', xy=(100, 300),  xycoords='figure points')

    ax.annotate('90% genes (37 kb)', xy=(37, 150),  xycoords='data',
                xytext=(0, 40), textcoords='offset points',
                arrowprops=dict(facecolor='black', shrink=0.05, frac=0.3),
                horizontalalignment='center', verticalalignment='bottom',
                )


    ax.annotate('95% genes (61 kb)', xy=(61, 50),  xycoords='data',
                xytext=(0, 30), textcoords='offset points',
                arrowprops=dict(facecolor='black', shrink=0.05, frac = 0.3),
                horizontalalignment='center', verticalalignment='bottom',
                )
    
    ax.annotate('98% genes (110kb)' , xy=(110, 30),  xycoords='data',
                xytext=(0, 30), textcoords='offset points',
                arrowprops=dict(facecolor='black', shrink=0.05, frac=0.3),
                horizontalalignment='center', verticalalignment='bottom',
                )

    plt.xlabel('Distance from TSS to second Exon (in kilobases)')
    plt.ylabel('Number of genes ')

#    plt.axis([])
    
    

    
    
    
    
    
    
    plt.title('TSS to Second Exon')
    plt.grid(True)
   
    plt.savefig(filename)
    plt.show()
         



##mu, sigma = 100, 15
##x = mu + sigma * np.random.randn(10000)
#    print arrayGenes
#    fig = plt.figure()
#    ax = fig.add_subplot(111)
#
## the histogram of the data
#    n, bins, patches = ax.hist(arrayGenes, 60, normed=True, facecolor='green', alpha=0.75)
#
## hist uses np.histogram under the hood to create 'n' and 'bins'.
## np.histogram returns the bin edges, so there will be 50 probability
## density values in n, 51 bin edges in bins and 50 patches.  To get
## everything lined up, we'll compute the bin centers
#    bincenters = 0.5*(bins[1:]+bins[:-1])
### add a 'best fit' line for the normal PDF
#    mu, sigma = meanstdv(arrayGenes)
#    y = mlab.normpdf( bincenters, mu, sigma)
#    l = ax.plot(bincenters, y, 'r--', linewidth=1)
#
#    ax.set_xlabel('Smarts')
#    ax.set_ylabel('Probability')
##ax.set_title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
#    ax.set_xlim(0, 70)
#    ax.set_ylim(0, 5)
#    ax.grid(True)
#
#    plt.show()
            
    
    

def geneParser(line):
    splitline = line.split()
    
    
    listOfEntries = [word.strip() for word in splitline]
    return listOfEntries


def meanstdv(x):
    
    n, mean, std = len(x), 0, 0
    for a in x:
        mean = mean + a
        mean = mean / float(n)
    for a in x:
        std = std + (a - mean)**2
        std = sqrt(std / float(n-1))
    return mean, std

def main():
    
    file = sys.argv[1]
    
    exonDist(file)
   
if __name__ == '__main__':
    main() 