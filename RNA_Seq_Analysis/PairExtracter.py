'''
Created on Feb 4, 2011

@author: Gaurav

#-------------------------------------------------------------------#
# Copyright (C) 2011 Gaurav Singhal                                 #
# All Rights Reserved.                                              #
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : Feb 04, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

'''
import sys
from sets import Set

'''
This script takes a set of aligned reads (mate 1 of the pair), and another set of unaligned reads(mate 2 of the pair).
The tags of aligned reads must be a subset of the tags unaligned reads.
@param aligned: Fastq file having aligned reads
@param unaligned: Fastq file having unaligned reads 


USAGE  :  python PairExtracter.py aligned.fastq unaligned.fastq

'''
def pairExtracter(aligned, unaligned):
    readCount = 0
    mapped = Set([])
    
    x = 0
    one = open(aligned, 'rU')
    for line in one:
        
        if x == 3:
            x = 0   # if x==3, we are on the last line of the read, so we reset the x and move on to the next line.
        elif x > 0: # if x > 1, we know that we are not on the first line of the read, so we just increment x by 1 and move on. 
            x+= 1
        else:  # when x == 0, we are on the first line of a read. we add the read tag to out set and increment x by 1
            tag = line.strip()[:-4]
            
            if tag not in mapped:
                
                mapped.add(line.strip()[:-4])
            else :
                print 'STOP !!!! duplicate tag found ', tag
            x+= 1
            
    
    one.close()
    y = 0
    out = open(unaligned[:-6]+'_filtered.fastq', 'w')
    two = open(unaligned, 'rU')
    switch = False
    
    for line in two:
        
            
        if y == 3:
            if switch == True :
                out.write(line)
            y = 0
            switch = False
        elif y > 0:
            if switch == True :
                out.write(line)
            y+= 1
        else:
            readTag = line.strip()[:-4]
            if readTag in mapped:
                switch = True    # when switch is True, we know we have to write the current read to the output.
                out.write(line)
            y+= 1
    
    
    two.close()
    out.close()


def main():
    aligned = sys.argv[1]  
    unaligned = sys.argv[2] 
    pairExtracter(aligned, unaligned)   
 
if __name__ == '__main__':
    main()
        
        
                
                
                    
