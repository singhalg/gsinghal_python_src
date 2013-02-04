'''
Created on May 17, 2010

@author: Gaurav

This script parses CpG data in file cpgIslandExt.txt
One line of text looks like this 

586    chr1    135124    135563    CpG: 30    439    30    295    13.7    67.2    0.64

'''
import sys
import re

"""
@param - takes in one line of string as a parameter
@ returns [chr#, CpG_Start Coordinates, CpG_End Coordinates]

"""

def Find(str):
    list = []
    chr = re.search('chr\d+\s', str)   #returns the first instance of match, otherwise returns null
    if chr:                             # true, if chr is not null
       # print chr.group()
        list.append(chr.group())        # chr.group() returns the string match
    wsloci = re.findall('\s\d\d\d\d\d+\s', str)  # finds all instances of match, and returns a list containing all those instances
    loci = []
    for locus in wsloci:  # wsloci = loci with whitespace
        loci.append(locus.strip())  # strip all the elements of wsloci and add them to loci
        
    if loci:
        list.extend(loci)    # add loci to list
    print list
    return list


def main():
    Find(sys.argv[1])


if __name__ == '__main__':
    main()

