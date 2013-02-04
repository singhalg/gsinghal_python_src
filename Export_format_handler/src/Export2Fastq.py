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
and converts the information into FASTQ format and saves the output
in a new file.

This script is ultra-light, with minimal memory consumption as it reads 
just one line at a time. This line is purged from memory as soon as it is 
parsed and written to the output(disk).

python Export2Fastq.pl <exportfile>

'''
def export2fastq(ExportFile):
    input = open(ExportFile, 'r')
    
# Ripping the filename off the 'export' tag    
    if ExportFile[-11:] == '.export.txt':
        filename = ExportFile[:-11]+'.fq'
    elif ExportFile[-11:] == '_export.txt':
        filename = ExportFile[:-11]+'.fq'
    elif ExportFile[-7:] == '.export':
        filename = ExportFile[:-7]+'.fq'
    elif ExportFile[-7:] == '_export':
        filename = ExportFile[:-7]+'.fq'
    elif ExportFile[-4:] == '.txt':
        filename = ExportFile[:-4]+'.fq'
    else: 
        filename = ExportFile + '.fq'
    output = open(filename, 'w')
    
    
    
   
    for line in input:
        list = line.split()
        
#--- Comment the line below and Uncomment the later commented code if you want to keep mapping information in the sequence id.         
        header = '@' + list[0] + '_000' + list[1]+ ':' + list[2] + ':' + list[3] + ':' + list[4] + ':' + list[5] + '#'+ list[6] + '/' + list[7] + '\n'



# UnComment this if you want to keep the mapping information in sequence id           
#        if re.search('chr', list[10]):
#            header = '@' + list[0] + '_000' + list[1]+ ':' + list[2] + ':' + list[3] + ':'
#            + list[4] + ':' + list[5] + '#'+ list[6] + '/' + list[7]+ ':' + list[10] + ':' + list[11]
#            if list[12]=='F':
#                header += '+' + list[13] +'\n'
#            else: header += '-' + '\n'  
        
        seq = list[8]+'\n'
        
        headerPlus = '+' + header        
        
        quality = list[9]+'\n'

        read = header + seq + headerPlus + quality
        
        output.write(read)    
        
        del read, header, headerPlus, seq, quality, list # purging from memory
            
    input.close()
    output.close()    
            
        
def main():
    
    ExportFile = sys.argv[1]
    
    export2fastq(ExportFile)
    
    
if __name__=='__main__':
    main()