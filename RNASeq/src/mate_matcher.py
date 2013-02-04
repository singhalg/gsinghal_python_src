'''
Created on Jan 19, 2011

@author: Gaurav
'''
'''
#-------------------------------------------------------------------#
# Copyright (C) 2011 Gaurav Singhal                                 #
# All Rights Reserved.                                              #
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : Jan 19, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

This script goes through 2 Sanger-fastq files and matches the reads and verifies whether all
the reads have their mate pairs. 
It successively compares the header of two fastq files and checks if both the reads of a pair are present
Bofore running this script, you may count the number of lines in both the read files and see if there are 
any discrepancies in line count. wc -l <file.fq>
'''

import sys

def mate_matcher(file1, file2):
    input1 = open(file1, 'r')
    input2 = open(file2, 'r')
    while input1.next() &  input2.next():
        line1 = input1.next()
        line2 = input2.next()
        if line1[:-2] == line2[:-2]:
            x = 1
            while x<4:
                input1.next()
                input2.next()
                x = x+1
             
    else :
        print 'Discrepancy at reads '
        print line1
        print line2



def main():
    
    fastqFile1 = sys.argv[1]
    fastqFile2 = sys.argv[2]
    
    
    mate_matcher(fastqFile1, fastqFile2)
    
    
if __name__=='__main__':
    main()     
        
        
    
             
             
         





