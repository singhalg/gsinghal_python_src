'''
Created on Jun 3, 2010

@author: Gaurav
'''

import sys
from Parser1 import *
from ReadParser import * 
from Overlap import *
import matplotlib.pyplot as plt
from pylab import *



"""
This method takes in two files
@param RepeatMaskerData: file containing RepeatMasker data for a particular repeat family
@param - ReadData : file containing sequencing reads 
@suffix - a string, which will be added to the end of the name of the file containing score

"""
def readAnalyzer(RepeatMaskerData, ReadData):
# ============ Picking the Repeat Element name from the RepeatMaskerData file ==========    
    data = open(RepeatMaskerData, 'rU')
    string = data.readline()
    list = string.split()
    print 'Analyzing reads for the following repeat element :', list[9]
    repFamily = list[9]
    data.close()

#==============Constructing Lists of RepeatMasker data and Read data =====================    
            # Parser1.py has ParserS() method
    repeats = ParserS(RepeatMaskerData, repFamily, False) #False is to specify that we are not saving the parser output to any file. 
    #only the per base scores will be saved. 
    reads = ReadParser(ReadData)

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
    
    print 'number of unmatched reads is :', x
    printScore1(Newconsensus, repFamily) #present in Analyzer1.py. This method prints the consensus to an output file
    #graph(Newconsensus, repFamily, True) #this plots the data and saves the figure



def printScore1(consensus, repFamily):

    name = repFamily + '_read_score'
   
    
    output = open(name, 'w')
    output.write(name)
    output.write('\n')
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

#def main():
#    RepeatMaskerData = sys.argv[1]
#    ReadData = sys.argv[2]
# 
#    readAnalyzer(RepeatMaskerData, ReadData)

def plotGraph1(file1, repFamily, save):
    data1 = open(file1, 'rU')
    data1.readline()
    consensus1 = []
    
    for line in data1:
        list = line.split()
        consensus1.append(int(list[2]))
    
    
    graph(consensus1, repFamily, save)

  
def main():
    file1 = sys.argv[1]
    repFamily = sys.argv[2]
    save = sys.argv[3]
    
    plotGraph1(file1, repFamily, save)
    
    
if __name__=='__main__':
    main()
    
    
