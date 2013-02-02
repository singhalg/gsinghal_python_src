'''
Created on Jan 21, 2011

@author: Gaurav

#-------------------------------------------------------------------#
# Copyright (C) 2011 Gaurav Singhal                                 #
# All Rights Reserved.                                              #
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : Jan 21, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

This script writes a job script and runs it on Lava with required params. 
Only edit at lines having ### TBE ### tag. 

'''
import sys


def renameChr(file):
    map = open(file, 'rU')
    
    
    bedFile = file + 's.bed'
    
    bed = open(bedFile, 'w')
    
    
    for line in map:
        bed.write(organize(line))
    map.close()
    bed.close()
        


def organize(string):
    list = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    
    chrNo = int(list[1][3:])
    
    feature = list[2] + '\t' + list[3] + '\t' + str(int(list[3])+readLen) + '\t' +list[4] + '\t' + str(800) + '\t' + list[1] + '\n'
    
    return feature

def main():
    
    mapFile = sys.argv[1]
    
    map2bed(mapFile)
    
    
if __name__=='__main__':
    main()

