'''
Created on Jan 18, 2011

@author: Gaurav
'''
'''
#-------------------------------------------------------------------#
# Copyright (C) 2011 Gaurav Singhal                                 #
# All Rights Reserved.                                              #
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : Jan 18, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#
'''


import sys
from Bio import SeqIO


def illumina2sangerFq(inputfile):
    
    print help(SeqIO.convert)
    
    filename = inputfile[:-3]+'.fastq'
    
    SeqIO.convert(inputfile, "fastq-illumina", filename, "fastq")

def main():
    
    inputfile = sys.argv[1]
    
    illumina2sangerFq(inputfile)
    
    
if __name__=='__main__':
    main()
                
