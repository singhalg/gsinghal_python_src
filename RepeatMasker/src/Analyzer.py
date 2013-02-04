'''
Created on May 26, 2010

@author: Gaurav
'''
import sys
from Parser import *


def Analyze2(file, repFamily, write, ret):
    list = Parser(file, repFamily, False)
    
# one line of list looks like this
# [2266, '10.4', '0.0', '0.0', 'chr1', 229525, 229825, 249020796, '+', 'AluY', 'SINE/Alu', 2, 311, 0, 267]
    
    if list[0][8] == '+':  # list[0][8] contains + or C, which represents positive strand or negative strand
        length = list[0][12] + list[0][13]
    else:
        length = list[0][11] + list[0][12]
    consensus = [0]*(length*2)
    for line in list:
        if line[8] == '+':
            a = line[11]-1
            b = line[12]
            c = line[13]-1
            for i in range (a, b):   
                consensus[i] += 1    
        elif line[8] == 'C':
            for i in range (c,b):  
                consensus[i] += 1
    index = 1
    for base in consensus: # base is each base of the repeat consensus
        print  index, '=', base
        index+=1
    
    # if the third argument(write) is true, it prints the output to a line
    if write:
        name = repFamily + '_score'
        output = open(name, 'w')
        output.write(name)
        index = 1
        for base in consensus:
            string = str(index) + ' = ' + str(base) + '\n'
            output.write(string)
            index +=1
        output.close()
    if ret:    
        return consensus
        
    

def main():
    openfile = sys.argv[1]
    repFamily = sys.argv[2]
    write = sys.argv[3]
    ret = sys.argv[4]
    
    Analyze2(openfile, repFamily, write, ret)   
 



if __name__ == '__main__':
    main()