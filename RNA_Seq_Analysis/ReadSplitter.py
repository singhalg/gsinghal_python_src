'''
Created on Apr 7, 2011

@author: Gaurav


#-------------------------------------------------------------------#
# Copyright (C) 2011 Gaurav Singhal                                 #
# All Rights Reserved.                                              #
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : April 07, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

'''
import sys




'''
This file takes a read file and for every read, it generates 30 bp reads with an offset of 3 bp. 
So, a 50 bp read would give rise to 1 + (20/3)

'''
def readSplitter(readsFile, windowSize):
    pass

    filea = open(readsFile, 'rU') # this file contains fastq reads
    
    
    reads = filea.readlines()
   
    
    filea.close()
    
    output = open(readsFile[:-6] + '_split.fastq', 'w')

    
    totalReads = len(reads)
  
    
    
    
    x = 0
    while x < totalReads:
        
        output.writelines(generateReads(reads[x:x+4], int(windowSize)))
        x+=4


'''
@param list: a list of 4 strings, these are 4 lines that make a fastq read
@param size: int number representing size of the smaller read 
This method returns a list of split reads to be written to the output file.  
'''
def generateReads(list, size):
    
    header = list[0].strip() # eg @SRR097789.1658 HWI-EAS217:4:1:37:1927 length=50
    read = list[1].strip() #      AGAACATCCTGGCCTGTCCATTGGTGATGTTGCGAAGAAACTGGGAGAGA
    footer = list[2].strip() #    +SRR097789.1658 HWI-EAS217:4:1:37:1927 length=50
    quality = list[3].strip() #   ABBACBCBBBBBBBBBACB@BCCB@C@BBABBBB>AB>9A=CBA><B+B>
    
    
    
    
    readSet = []
    
    
    rng = (len(read) - size ) +1
    
    for x in range(rng):
        
        tags  = header.split()
        newHeader =  tags[0]+' '+tags[1] +'#' + str(x+1) + ' length=30'
        
        splitRead = read[x:x+30]
        splitQuality = quality[x:x+30]
        readSet.append(newHeader +'\n')
        readSet.append(splitRead +'\n')
        readSet.append('+'+newHeader[1:] +'\n')
        readSet.append(splitQuality  +'\n')
        
    return readSet

    
    
    

def main():
#    aligned = sys.argv[1]  
#    unaligned = sys.argv[2] 
#    pairExtracter(aligned, unaligned)   

    reads = sys.argv[1]
    windowSize = sys.argv[2]
    readSplitter(reads, windowSize)
if __name__ == '__main__':
    main()