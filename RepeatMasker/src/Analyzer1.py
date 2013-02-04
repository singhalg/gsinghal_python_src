'''
Created on May 26, 2010

@author: Gaurav
'''
import sys
from Parser import *
import matplotlib.pyplot as plt
from pylab import *

"""
@param - file : the file that needs to be parsed. Usually, this is a Repeat Masker output file. 
@param repFamily: The repeat family for which the file is being parsed and analysed.
@param - write - Boolean, determines whether the output (per base scores)  has to be written to a file or not.
@param - ret - Boolean, determines whether the output has to be returned or not. 
"""
def Analyze(file, repFamily, write, ret):
 
#output of parser not to be written to a file
    list = Parser(file, repFamily, False)
    
# one line of list looks like this
# [2266, '10.4', '0.0', '0.0', 'chr1', 229525, 229825, 249020796, '+', 'AluY', 'SINE/Alu', 2, 311, 0, 267]
    
    
    #determining the length of consensus
    if list[0][8] == '+':  # list[0][8] contains + or C, which represents positive strand or negative strand
        length = list[0][12] + list[0][13]
    else:
        length = list[0][11] + list[0][12]
    #this makes a list of 0's, such as [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0....]
    consensus = [0]*(length*2)   # there seems to be a discrepancy between consensus length and the actual spread of TE's with respect to consensus
                                 # so we initially set the consensus to be twice its supposed length
    for line in list:
        if line[8] == '+':
            for i in range(line[11] - 1, line[12]):
                consensus[i] += 1
        elif line[8] == 'C':
            for i in range(line[13] - 1, line[12]):
                consensus[i] += 1
    
    Newlength = length + (length/20)

    Newconsensus = consensus[:Newlength] #trimming the consensus back to near its supposed length 
    # if the third argument(write) is true, it prints the output to a line
    if write:
        name = repFamily + '_score'
        output = open(name, 'w')
        output.write(name)
        output.write('\n')
        index = 1
        for base in Newconsensus:
            string = str(index) + ' = ' + str(base) + '\n'
            output.write(string)
            index +=1
        output.close()
    print ' The scores for this repeat family have been written to file :' , name
    print ' The actual length of consensus is ', length
    print 'the contents of the output file ( ', name , ' )look like this :' 
    for base in Newconsensus[:10]:
        print base

    del consensus, Newconsensus, list
    # if the fourth argument (ret) is true, it returns the consensus file
    if ret:    
        return consensus
    
    

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
    filename = repFamily+'.png'
    plt.plot(xs, ys, label = repFamily) #makes the plot
    plt.title(r'Per Base Score for Repeat Element' )
    plt.xlabel('Consensus')
    plt.ylabel('Per Base Score')
   
    legend()
    if save:
        plt.savefig(filename)
    plt.show() #shows the plot
    
        
def printScore(consensus, repFamily):

    name = repFamily + '_score'
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

def main():
    openfile = sys.argv[1]
    repFamily = sys.argv[2]
    write = sys.argv[3]
    ret = sys.argv[4]  # has to be True for the graph method to work
    savefig = sys.argv[5]
    graph(Analyze(openfile, repFamily, write, ret), repFamily, savefig)   
    #graph(data,                                  repFamily, savefig) 



if __name__ == '__main__':
    main()
