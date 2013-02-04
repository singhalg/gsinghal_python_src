'''

#-------------------------------------------------------------------#
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : August 19, 2010                                         #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

'''

#!/usr/bin/env python -tt



import sys


def OverlapAnalysis(file):
    
    Overlap = []
    input = open (file, 'rU')
    firstLine = input.readline()
    prev = organize(firstLine)
    count = 1
    
    for line in input:
        
        curr = organize(line)
        
        if curr != prev :
            set = [count, prev]  # encountered new repeat, so saving the prev repeat into Overlap 
            
            Overlap.append(set)
            
            count = 1   # resetting count to 1
            prev = curr
        else:
            count+= 1  
            prev = curr
            
    
    print Overlap[1:50]
    sortedOver = sorted(Overlap)
    print sortedOver[-50:-1]
    
def organize(string):   
    list = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    repeat = list[9] +'#'+  list[10] +'#'+  list[11]
    return repeat


def main():
    file = sys.argv[1]
    OverlapAnalysis(file)
    
    
if __name__=='__main__':
    main()