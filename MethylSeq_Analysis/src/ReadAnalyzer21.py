'''
Created on Jun 3, 2010
Last Edited July 18, 2010
@author: Gaurav Singhal
'''

import sys
from Parser1 import *
from ReadParser import * 
from Overlap import *
import matplotlib.pyplot as plt
from pylab import *



'''
This method takes in two files
@param RepeatMaskerData: file containing RepeatMasker data for a particular repeat family
@param - ReadData : file containing sequencing reads 
@suffix - a string, which will be added to the end of the name of the file containing score


This method takes in RepeatMasker output parsed for a specific repeat element. It also takes a big list containing all the reads.

'''
def readAnalyzer(RepeatMaskerData, reads):
# ============ Picking the Repeat Element name from the RepeatMaskerData file ==========    
    data = open(RepeatMaskerData, 'rU')
    string = data.readline() # just reading the first line to get info abt the repeat element.
    list = string.split()
    print 'Analyzing reads for the following repeat element :', list[9]
    repFamily = list[9]
    data.close()

#==============Constructing Lists of RepeatMasker data and Read data =====================    
            # Parser1.py has ParserS() method
    repeats = ParserS(RepeatMaskerData, repFamily, False) #False is to specify that we are not saving the parser output to any file. 
    #only the per base scores will be saved. 
    

#============= Getting total readCount ==================================
    readCount = 0
    for chr in reads:
        readCount+= len(chr)


#================= getting consensus length of the repeat element =====================
    
# one line of repeats looks like this :
# 318  23.0  3.8  0.0  chr1        15265   15355 (249235266) C  MIR3           SINE/MIR             (119)  143     49      5    
    if repeats[0][0][8] == '+':
        length = repeats[0][0][12] + repeats[0][0][13]
    else: # if repeats[0][0][8] == 'C':
        length = repeats[0][0][11]+ repeats[0][0][12]
        
    consensus = [0]*(length*2)  # consensus length is kept twice of the original length as some repeat elements extend beyond the range of consensus
    x = 0 #counter for unmatched reads
#========================================================================================    

    
#=========== now doing binary search=====================================================

# this  calls binaryS() method, which is a recursive implementation of binary search. The method is present in Overlap.py
    
    i = 0
    while i < 24:
        for read in reads[i]:
            
            max = len(repeats[i]) - 1
            min = 0
            mid = binaryS(repeats[i], read, min, max) # here, mid = score returned by the binaryS method
            if mid == -2:
                x +=1 #read not found, increment the counter
            else:
                readS = read[1]
                readE = read[2]
                TPS = repeats[i][mid][5]
                TPE = repeats[i][mid][6]
                if repeats[i][mid][8] == '+':
                    start = repeats[i][mid][11] - 1
                    end = repeats[i][mid][12]
                else: # if repeats[i][mid][8] == 'C':
                    start = repeats[i][mid][13] - 1
                    end = repeats[i][mid][12] 
                overlap(consensus, start, end, readS, readE, TPS, TPE) #overlap() is present in Overlap.py
        #========= end of for loop =============            
        i = i+1    
        
    Newlength = length + (length/20) # clipping back consensus to its original length

    Newconsensus = consensus[:Newlength] 
    del repeats
    print 'number of unmatched reads is :', x
    printScore1(Newconsensus, readCount, x, repFamily) #present in Analyzer1.py. This method prints the consensus to an output file
    #graph(Newconsensus, repFamily, True) #this plots the data and saves the figure
    
    
def SuperReadAnalyzer(ReadData, Repeat1, Repeat2, Repeat3, Repeat4,
                      Repeat5, Repeat6, Repeat7, Repeat8, Repeat9, 
                      Repeat10, Repeat11, Repeat12, Repeat13, Repeat14,
                       Repeat15, Repeat16, Repeat17, Repeat18, Repeat19, Repeat20, Repeat21):
    reads = ReadParser(ReadData)
    readAnalyzer(Repeat1, reads)
    readAnalyzer(Repeat2, reads)
    readAnalyzer(Repeat3, reads)
    readAnalyzer(Repeat4, reads)
    readAnalyzer(Repeat5, reads)
    readAnalyzer(Repeat6, reads)
    readAnalyzer(Repeat7, reads)
    readAnalyzer(Repeat8, reads)
    readAnalyzer(Repeat9, reads)
    readAnalyzer(Repeat10, reads)
    readAnalyzer(Repeat11, reads)
    readAnalyzer(Repeat12, reads)
    readAnalyzer(Repeat13, reads)
    readAnalyzer(Repeat14, reads)
    readAnalyzer(Repeat15, reads)
    readAnalyzer(Repeat16, reads)
    readAnalyzer(Repeat17, reads)
    readAnalyzer(Repeat18, reads)
    readAnalyzer(Repeat19, reads)
    readAnalyzer(Repeat20, reads)
    readAnalyzer(Repeat21, reads)



 

def printScore1(consensus, readCount, x, repFamily):

    name = repFamily + '_read_score'
   
    
    output = open(name, 'w')
    output.write(name)
    output.write('\n')
    rc = str(readCount) + '\t' + str(x) + '\n'
    output.write(rc)
    index = 1
    for base in consensus:
        string = str(index) + ' = ' + str(base) + '\n'
        output.write(string)
        index +=1
    output.close()
    print ' The scores for this repeat family have been written to file :' , name



'''
@param : Data
@param : repFamily : Repeat Family
@param : save : Save ? True or False
@return - returns a image of the output graph
'''
def graph(data, repFamily, save):
    rcParams['legend.loc'] = 'best'
    length = len(data)
    ys = data
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
    filename = repFamily+'_read.png'
    plt.plot(xs, ys, label = repFamily) #makes the plot
    plt.title(r'Per Base Score for Repeat Element' )
    plt.xlabel('Consensus')
    plt.ylabel('Per Base Score')
    
    legend()
    if save:
        plt.savefig(filename)
    plt.show() #shows the plot

def main():
    ReadData = sys.argv[1]
    Repeat1 = sys.argv[2]
    Repeat2 = sys.argv[3]
    Repeat3 = sys.argv[4]
    Repeat4 = sys.argv[5]
    Repeat5 = sys.argv[6]
    Repeat6 = sys.argv[7]
    Repeat7 = sys.argv[8]
    Repeat8 = sys.argv[9]
    Repeat9 = sys.argv[10]
    Repeat10 = sys.argv[11]
    Repeat11 = sys.argv[12]
    Repeat12 = sys.argv[13]
    Repeat13 = sys.argv[14]
    Repeat14 = sys.argv[15]
    Repeat15 = sys.argv[16]
    Repeat16 = sys.argv[17]
    Repeat17 = sys.argv[18]
    Repeat18 = sys.argv[19]
    Repeat19 = sys.argv[20]
    Repeat20 = sys.argv[21]
    Repeat21 = sys.argv[22]
    
  
    
 
    SuperReadAnalyzer(ReadData, Repeat1, Repeat2, Repeat3, Repeat4,
                      Repeat5, Repeat6, Repeat7, Repeat8, Repeat9, 
                      Repeat10, Repeat11, Repeat12, Repeat13, Repeat14,
                       Repeat15, Repeat16, Repeat17, Repeat18, Repeat19, Repeat20, Repeat21)
    
    
    
    
if __name__=='__main__':
    main()
    
    
