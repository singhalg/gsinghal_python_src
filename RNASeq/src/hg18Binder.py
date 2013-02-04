'''
Created on Feb 9, 2011

@author: Gaurav
'''

import sys

def rmoutBinder():
    
    outFile = 'hg18.fa.out'
    
    hg18 = open(outFile, 'w')
    
    
    chrs = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 
           'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY']
    
    for chr in chrs:
        infile = chr+'.fa.out'
        rmout = open(infile, 'rU')
        rmout.readline()
        rmout.readline()
        rmout.readline()
        hg18.write(rmout.readlines())
        rmout.close()
    
    
    hg18.close()
    
    
    
    

def main():
    rmoutBinder()

if __name__ == '__main__':
    main()
    