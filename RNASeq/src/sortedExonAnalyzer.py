'''
Created on Apr 12, 2011

@author: Gaurav



#-------------------------------------------------------------------#
# Author: Gaurav Singhal                                            #
# Created : April 12, 2011                                          #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

'''

import sys


def sortedExonAnalyzer(file):
    
    infile = open(file, 'rU')
    readExonCov = infile.readlines()
    infile.close()
    
    



def main():
    
    splitReads_Exons_coverage_sorted  = sys.argv[1]
    sortedExonAnalyzer(splitReads_Exons_coverage_sorted)
    
    
if __name__ == '__main__':
    main()