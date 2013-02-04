'''
Created on Apr 18, 2011

@author: Gaurav

#-------------------------------------------------------------------#
# @copyright:  2011 Gaurav Singhal                                  #
# All Rights Reserved.                                              #
# Author: Gaurav Singhal                                            #
# Created : April 12, 2011                                          #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

'''
import matplotlib.pyplot as plt 

from pylab import *
import sys
from sets import Set
import random, math




def factorial():
    
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    
    genes = []
    
    for x in range(26):
        for y in range(26):
            for z in range(26):
                genes.append(alpha[x] + alpha[y] + alpha[z])
                
    print '# of genes = ', len(genes)
    
    geneSet = Set(genes)
    
    print ' size of set of genes is : ', len(geneSet)
    
    
    extra = []
    
    for each in genes[:1428]:
        extra.append(each+'a')
        
    
    for letter in extra:
        genes.append(letter)
        
    print 'now the # of genes = ', len(genes)
    
    mcf7Genes = genes[:12500]
    
    geneSet = Set(genes)
    
    print ' now the size of set of genes is : ', len(geneSet)
    
    return genes, mcf7Genes


def permutations(N , M , R, Iterations):
    
    n = int(N) # overlap b/t the two sets
    m = int(M) # size of genes set
    r = int(R) # total genes
    iterations = int(Iterations)
    genes, mcf7Genes = factorial()
    
#    print genes[:100]
       
    Ho = 0
    Ha = 0
    
    distribution = []
    for x in range(m):
        distribution.append(0) 
        
        
    totalIter = 0
    while totalIter < iterations:
        
        cancerPicks = Set([])
        genePicks = Set([])
        cancerSet = Set([])
        geneSet = Set([])
        for iterCancer in range(458):
#            y = random.uniform(0,1)
#            if y >=0.5:
#                x = math.ceil(random.uniform(0, 17576))
#            else:
            
            x = math.floor(random.uniform(0, r))
#            print x
            
            while x in cancerPicks:
                x = math.floor(random.uniform(0, r))
                
            
            cancerPicks.add(x)
            cancerSet.add(genes[int(x)])
            iterCancer+=1
    
    
        
        for iterGene in range(m):
#            y = random.uniform(0,1)
#            if y >=0.5:
#                x = math.ceil(random.uniform(0, 17576))
#            else:
            x = math.floor(random.uniform(0, r))
#            print x
    
            while x in genePicks:
                x = math.floor(random.uniform(0, r))
            
            genePicks.add(x)
            geneSet.add(genes[int(x)])
            iterGene+=1
        
        totalIter+=1
        
        overlap = cancerSet & geneSet
        
#        print 'leng of cancer set  = ', len(cancerSet)
#        print 'leng of gene set  = ', len(geneSet)
        
        lenOfOverlap = len(overlap)
        
        if lenOfOverlap < n :
            Ha += 1
        else :
            Ho += 1
        
#        print 'len of overlap = ',lenOfOverlap
        distribution[lenOfOverlap] +=1
    
    
    newdist = distribution[:180]
    
          
    print 'Ho = ' ,Ho
    print 'Ha = ', Ha

        
    manyplots1(newdist, N,M, R, Iterations)
        
        
            
            
            
def manyplots1(repeatCon, N, M, R, Iter):
    
    
#    font0 = FontProperties()
#    rcParams['legend.loc'] = 'upper right'  # puts the legend at the best possible location, where it minimally overlaps the curves
#    rcParams['figure.figsize'] = 16, 11  # manually setting the plot size (width X height)
    
    
    
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
    
    filename = N + '_' + M + '_' + R + '_' + Iter + '.png' # plot will be saved with this name
    
    conlbl = 'n = ' + N + '; m = ' + M + '; r = ' + R + '; iterations =' + Iter  
    line1, = ax1.plot(xs, ys, linewidth = 1.5, color = 'b', label = conlbl)
    ax1.set_xlabel('# common genes')
    ax1.set_ylabel('occurance ')
    for tl in ax1.get_yticklabels():
        tl.set_color('k')
   
   
   
   
   
    ax1.annotate(N+' (cut-off)', xy=(int(N), 1),  xycoords='data',
                xytext=(0, 40), textcoords='offset points',
                arrowprops=dict(facecolor='black', shrink=0.05, frac=0.3),
                horizontalalignment='center', verticalalignment='bottom',
                )   
    legend()
#    plt.title(conlbl)
    plt.grid(True)
   
    plt.savefig(filename)
    plt.show() 

def main():
    
    # r = 18810 (total size of gene pool) , 
    # m = # of genes pulled out at every instance. 
    # n = # of genes overlapping between the two gene sets
    
    n = sys.argv[1]
    m = sys.argv[2]
    r = sys.argv[3]
    iterations = sys.argv[4]
    permutations(n, m, r, iterations)

if __name__ == '__main__':
    main()