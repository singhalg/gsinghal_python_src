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

'''

#!/usr/bin/env python -tt

import sys


'''
This script converts the Illumina read output in txt format into Sanger-FASTQ format and saves the output
in a new file with .fastq extension

This script is ultra-light, with minimal memory consumption as it reads 
just one line at a time. This line is purged from memory as soon as it is 
parsed and written to the output(disk).

python txt2SangerFq.py <txtfile>

'''
def txt2SangerFq(txtFile):
    input = open(txtFile, 'r')
    

    filename = txtFile + '.fastq'
    output = open(filename, 'w')
    
    
    
   
    for line in input:
        list = line.split(':')
        
#--- Comment the line below and Uncomment the later commented code if you want to keep mapping information in the sequence id.         
        header = '@' + list[0] + ':'+ list[1]+ ':' + list[2] + ':' + list[3] + ':' + list[4] + '\n'



# UnComment this if you want to keep the mapping information in sequence id           
#        if re.search('chr', list[10]):
#            header = '@' + list[0] + '_000' + list[1]+ ':' + list[2] + ':' + list[3] + ':'
#            + list[4] + ':' + list[5] + '#'+ list[6] + '/' + list[7]+ ':' + list[10] + ':' + list[11]
#            if list[12]=='F':
#                header += '+' + list[13] +'\n'
#            else: header += '-' + '\n'  
        
        seq = list[5]+'\n'
        
        headerPlus = '+' + '\n'   
        
        SangerQual = ''
        quality = list[6].strip()
        for letter in quality:
            SangerQual = SangerQual+ chr(ord(letter)- 64 + 33)   # to convert from Illumina to Sanger score

        read = header + seq + headerPlus + SangerQual + '\n'
        
        output.write(read)    
        
        #del read, header, headerPlus, seq, quality, list # purging from memory
            
    input.close()
    output.close()    
            
        
def main():
    
    txtFile = sys.argv[1]
    
    txt2SangerFq(txtFile)
    
    
if __name__=='__main__':
    main()