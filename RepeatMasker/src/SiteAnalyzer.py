'''
Created on Jun 3, 2010

@author: Gaurav
'''
import sys
from Parser1 import *
from siteParser import * 
from Overlap import *
from Analyzer1 import graph, printScore





"""
This method takes in two files
@param RepeatMaskerData: file containing RepeatMasker data for a particular repeat family
@param - ReadData : file containing sequencing reads 


"""
def siteAnalyzer(RepeatMaskerData, siteData, suffix):
# ============ Picking the Repeat Element name from the RepeatMaskerData file ==========    
    data = open(RepeatMaskerData, 'rU')
    string = data.readline()
    list = string.split()
    print 'Analyzing reads for the following repeat element :', list[9]
    repFamily = list[9]
    data.close()

#==============Constructing Lists of RepeatMasker data and Read data =====================    

    repeats = ParserS(RepeatMaskerData, repFamily, False) #False is to specify that we are not saving the parser output to any file. 
    #only the per base scores will be saved. 
    sites = siteParser(siteData)

#================= getting consensus length of the repeat element =====================
    
# one line of repeats looks like this :
# 318  23.0  3.8  0.0  chr1        15265   15355 (249235266) C  MIR3           SINE/MIR             (119)  143     49      5    
    if repeats[0][0][8] == '+':
        length = repeats[0][0][12] + repeats[0][0][13]
    else:
        length = repeats[0][0][11]+ repeats[0][0][12]
        
    consensus = [0]*(length*2)  # consensus length is kept twice of the original length as some repeat elements extend beyond the range of consensus
    x = 0
#========================================================================================    

    
#=========== now doing binary search=====================================================

# this  calls binaryS() method, which is a recursive implementation of binary search. The method is present in Overlap.py
    
    i = 0
    while i < 24:
        for read in sites[i]:
            max = len(repeats[i]) - 1
            min = 0
            mid = binaryS(repeats[i], read, min, max)
            if mid == -2:
                x +=1
            else:
                readS = read[1]
                readE = read[2]
                TPS = repeats[i][mid][5]
                TPE = repeats[i][mid][6]
                if repeats[i][mid][8] == '+':
                    start = repeats[i][mid][11] - 1
                    end = repeats[i][mid][12]
                else:
                    start = repeats[i][mid][13] - 1
                    end = repeats[i][mid][12] 
                overlap(consensus, start, end, readS, readE, TPS, TPE)
        #========= end of for loop =============            
        i = i+1    
        
    Newlength = length + (length/20) # clipping back consensus to its original length

    Newconsensus = consensus[:Newlength] 
    
    print 'number of unmatched sites is :', x
    printScore(Newconsensus, repFamily, suffix) #this method prints the consensus to an output file
    graph(Newconsensus, repFamily, True) #this plots the data and saves the figure






def main():
    RepeatMaskerData = sys.argv[1]
    siteData = sys.argv[2]
    suffix = sys.argv[3]
    siteAnalyzer(RepeatMaskerData, siteData, suffix)
    
    
    
    
if __name__=='__main__':
    main()
    
    
