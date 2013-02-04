

'''
Created on Mar 31, 2011

@author: Gaurav

#-------------------------------------------------------------------#
# Copyright (C) 2011 Gaurav Singhal                                 #
# All Rights Reserved.                                              #
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : March 31, 2011                                          #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

'''


'''
This script can extract the complement of a read alignment file given two overlapping read files.
So, if there are two reads alignment files, and there are some reads common among the two alignment files,
then this script can find the reads that do not overlap. 
@param fileB: Any reads that are also present in file B would be discarded. 
@param fileA: This script finds the complement of file A



Also, given two fastq files, where one set of reads is a subset of the second set, the method rep_repEx can 
make a fastq file having reads of fileA - reads of fileB
'''

import sys
from sets import Set

'''
@param fileA: fastq file containing the mates of those reads that mapped to repeats
@param fileB : fastq file (reads of fileB should be a subset of fileA)
'''

def rep_repEx(fileA, fileB):


    filea = open(fileA, 'rU') # this file contains those reads that map to genome (unique + repeat)
    fileb = open(fileB, 'rU') # overlap file (this file contains those reads that map within repeats)
    
    mate2 = filea.readlines()
    mate2ToRepeats = fileb.readlines()
    
    filea.close()
    fileb.close()
    output = open(fileA[:-6] + '_non_repeats.fastq', 'w')
    setA = Set([])
    setB = Set([])
    
    totalReads = len(mate2)
    mate2RepReads = len(mate2ToRepeats)
    
    
    
    x = 0
    while x < totalReads:
        
        setA.add(processFastqReads(mate2[x].strip()))
    
        x+=4
    
    
    y = 0
    
    while y < mate2RepReads:
       
        setB.add(processFastqReads(mate2ToRepeats[y].strip()))
        y+=4
        
    
    
    
    
    print '1) # of reads in mate_2 (to Repeats) is : ', totalReads
    print 'size of set of reads tags in mate_2 is : ', len(setA)
    
    if (totalReads/4) == len(setA):
        
        print 'There are no reads in file 1 with duplicate tags'    
    
    
    
    if (mate2RepReads/4) == len(setB):
        print 'There are no reads in file 2 with duplicate tags'    
        
    aMinusb = setA - setB
    
    z = 0
    
    while z< totalReads:
        readTag = processFastqReads(mate2[z].strip())
        if readTag in aMinusb:
            output.writelines(mate2[z:z+4])
        z+=4
        
    
    print 'done!'

def complement_readEx(fileA, fileB):
    
    filea = open(fileA, 'rU') # this file contains those reads that map to genome (unique + repeat)
    fileb = open(fileB, 'rU') # overlap file (this file contains those reads that map within repeats)
    
    alignedReads = filea.readlines()
    overlapRmsk = fileb.readlines()
    
    filea.close()
    fileb.close()
    output = open(fileA[:4] + 'uniqueGenome.bed', 'w')
    setA = Set([])
    setB = Set([])
    
     
    
    print '# of reads in alignment file is : ', len(alignedReads)
    
    for readA in alignedReads:
        setA.add(processRead(readA))
    
    print 'size of set of reads tags is : ', len(setA)    
    
    
    
    for readB in overlapRmsk:
        setB.add(processOverlapRead(readB))
        
    aMinusb = setA - setB
    
    for line in alignedReads:
        if processRead(line) in aMinusb:
            output.writelines(line)
    
    print 'done!'
    
'''
@param string: a string, which is the first line (header) of a fastq read 
@returns: a string representation of read tag

'''
def processFastqReads(header):
    
   tags  = header.split()
   return tags[0][1:]+'#'+tags[1]
   
   
   
'''
processes each line of aligned reads
'''
def processRead(line):
    
    sline = line.strip().split('\t')
    return sline[3].strip()
    
    
'''
processes each line of reads that overlap with repeats
'''    
def processOverlapRead(line):
    sline = line.strip().split('\t')
    return sline[9].strip()

def main():
    fileA = sys.argv[1] # all the aligned reads
    fileB = sys.argv[2] # reads which mapped to repeats
    
#    complement_readEx(fileA, fileB)
    rep_repEx(fileA, fileB)
    
if __name__ == '__main__':
    main()
    