

#-------------------------------------------------------------------#
# Author: Gaurav Singhal                                            #
# Created : July 28, 2010                                           #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#


#!/usr/bin/python

import sys


def gff2(file):
    
    
    if file[-4:] == '.gff':
        bedFile = file[:-4]+'.bed'
    else:
        bedFile = file + '.bed'
    gff = open(file, 'rU')
    bed = open(bedFile, 'w')

    for line in gff:       
        bed.write(organize(line))
        
    
    gff.close()
    bed.close()
        


def organize(string):
    list = string.split()
    chr = list[0]
    start = list[3]
    end = str(int(list[4])+1)
    name = list[1] + '#' + list[2] 
    score = str(int(float(list[5])))
    
    if list[6] == '+':
        strand = '+'
        nameS = name
    elif list[6] == '-':
        strand = '-'
        nameS = name
    else: 
        strand = '+'
        nameS = name + '#Strand_unknown'
    
    if list[7] == '0':
        nameF = nameS + '#frame_0'
    elif list[7] == '1':
        nameF = nameS + '#frame_1'
    elif list[7] == '2':
        nameF = nameS + '#frame_1'
    else :
        nameF = nameS
    
    feature = chr + '\t' + start + '\t' + end + '\t' + nameF + '\t' +score + '\t' + strand + '\n'
    
    return feature

def main():
    
    File = sys.argv[1]
    
    gff2(File)
    
    
if __name__=='__main__':
    main()