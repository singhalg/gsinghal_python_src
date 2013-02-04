'''
Created on Apr 12, 2011

@author: Gaurav


#-------------------------------------------------------------------#
# @copyright:  2011 Gaurav Singhal                                  #
# All Rights Reserved.                                              #
# Author: Gaurav Singhal                                            #
# Created : April 12, 2011                                          #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

'''

import sys
from decimal import Decimal

def exonCoverageSorter(file):
    
    infile = open(file, 'rU')
    readExonCov = infile.readlines()
    infile.close()
    exons = []
        
    for each in readExonCov:
        exons.append(organize(each))
        
    sortedExons = sorted(exons, key=helpSort, reverse =True)
    
    outfile = open(file+'_sortByReadNum.bed', 'w')
    
    for each in sortedExons:
        outfile.write(list2String(each))
        
    outfile.close()
        
    
def helpSort(list):

    return list[-4]

def organize(line):
    cols = line.split('\t')[:-1]
    
    readNum = int(cols[-4].strip())
    
    coveredBases = int(cols[-3].strip())
    
    exonsSize = int(cols[-2].strip())
    
    score = Decimal(cols[-1].strip())
        
    allButScore = ''
    for each in cols[:-4]:
        allButScore+=each + '\t'
        
    processed = [allButScore, readNum, coveredBases, exonsSize, score]
    return processed


def list2String(list):
    
    string = ''
    for each in list[1:]:
        string += str(each) + '\t'
        
    return list[0] + '\t' + string + '\n'





def organizeWrite(list):
    
    if list[-1] == 0:
        return list[0] + '\t' + '0.0000000' + '\n'
    else:
        return list[0] + '\t' + str(list[1]) + '\n'
    

def main():
    
    splitReads_Exons_coverage  = sys.argv[1]
    exonCoverageSorter(splitReads_Exons_coverage)
    
    
if __name__ == '__main__':
    main()