
'''
Created on March 29, 2011

@author: Gaurav

#-------------------------------------------------------------------#
# Copyright (C) 2011 Gaurav Singhal                                 #
# All Rights Reserved.                                              #
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : March 29, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

'''
import sys


'''
This method takes an adapter trimmed fastq-read file or any variable read-length fastq file and extracts all the 
reads of a particular length provided as parameter. 
@param file: File to be trimmed
@param lenRead: reads with length == lenRead would be extracted and saved to another file.
'''

def fullLengthReadEx(file, lenRead):
    x = 0
    one = open(file, 'rU')
    
    allReads = one.readlines()
    
    one.close()
    
    outname = file+'_FL.fq'
    
    output = open(outname, 'w')
    
    lenAllReads = len(allReads)
    
    readLen = int(lenRead)
    
    while x < lenAllReads:
        
        if len(allReads[x+1].strip()) == readLen:
            output.writelines(allReads[x : (x+4)])
    
        x+=4
    output.close()
    
    
def fullLengthReadExSam(file, lenRead):
    one = open(file, 'rU')
    one.readline()
    one.readline()
    
    allReads = one.readlines()
    
    one.close()
    
    outname = file+'_FL.fq'
    
    output = open(outname, 'w')
    

    
    for line in allReads:
        sline = line.strip().split('\t')
        read = sline[9].strip()
        readlen = len(read)
    
        if readlen == 76 :
            output.writelines(line)
   
    output.close()

def fullLengthReadCounter(file, lenRead):
    x = 0
    fullLengthReadCount = 0
    one = open(file, 'rU')
    
    allReads = one.readlines()
    
    one.close()
    
    
    
    lenAllReads = len(allReads)
    
    readLen = int(lenRead)
    
    while x < lenAllReads:
        
        if len(allReads[x+1].strip()) >= readLen:
            fullLengthReadCount+=1
    
        x+=4
    print '# reads >= ' + lenRead+' : ', fullLengthReadCount



def main():
    filename = sys.argv[1]
    lengthOfRead = sys.argv[2]
#    fullLengthReadExSam(filename, lengthOfRead)
    fullLengthReadCounter(filename, lengthOfRead)


if __name__ == '__main__':
    main()