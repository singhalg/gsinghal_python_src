

'''

#-------------------------------------------------------------------#
# Copyright (C) 2010 Center for Genome Sciences and Systems Biology #
# All Rights Reserved.                                              #
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : July 22, 2010                                           #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

'''

#!/usr/bin/env python -tt

import sys
import re

'''
This script takes the sequence alignment output in Export format 
and counts the number of lines with at least one ambiguous base.
The output is written to StdOut and also stored in a file with the name
<inputfile>_NCount 

This script is ultra-light, with minimal memory consumption as it reads 
just one line at a time. This line is purged from memory as soon as it is 
parsed.

python Export2Fastq.pl <exportfile>

'''
def ExportAmbCounter(ExportFile):
    input = open(ExportFile, 'r')
    Ncounter = 0
    
    
    for line in input:
        
        list = line.split()
        
        if re.search('N', list[8]):
            Ncounter +=1
        
        del list
    input.close()
    count = str(Ncounter)
    out = ExportFile + '_NCount'
    output = open(out, 'w')
    output.write(count)  
    print Ncounter
    
    output.close()
    
def main():
    
    ExportFile = sys.argv[1]
    
    ExportAmbCounter(ExportFile)
    
    
if __name__=='__main__':
    main()