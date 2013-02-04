'''
Created on Jan 14, 2011

@author: Gaurav
'''
'''
#-------------------------------------------------------------------#
# Copyright (C) 2011 Gaurav Singhal                                 #
# All Rights Reserved.                                              #
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : Jan 14, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#


This script takes the human genone reference file as input and masks 
the unique regions on the given fasta file. So, any upper case letter
(which includes both unique sequences and undertermined sequences) 
is converted to 'X' and any lower case letter is converted to upper case.  


'''



import sys
import re

def invertGenome(hgRef):
    input = open(hgRef, 'r')
    if hgRef[-3:] == '.fa':
        filename = hgRef[:-3]+'_invert.fa'
    else:
        filename = hgRef + '_invert'
    output = open(filename, 'w')
    for line in input:
        if line[0:1]== '>':
            output.write(line)
        else :    
            x = 0
            y = 1
            line = line.strip()
            length  = len(line)
            
            invertLine = ''
            while x<length:
                base = line[x:y]
                if base.isupper():
                    invertLine= invertLine +'X'
                else:
                    invertLine= invertLine + base.upper()
                    
                x = x+1
                y = y+1
            output.write(invertLine)
            output.write('\n')
            
       
        
        
def main():
    
    fastaFile = sys.argv[1]
    
    invertGenome(fastaFile)
    
    
if __name__=='__main__':
    main()
                
                
        
        
        


