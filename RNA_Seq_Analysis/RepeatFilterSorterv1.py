

#-------------------------------------------------------------------#
# Author: Gaurav Singhal                                            #
# Created : Feb 15, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#


#!/usr/bin/python

import sys
import pickle
from decimal import *


"""
@param file: hg19.fa.out : This is repeat masker output
@return : Makes a file for each repeat element (such as AluY, L2, MIR) in hg18.fa.out. 
Each of such file contains all the lines from hg19.fa.out that belong to that repeat element.
"""

def Filter(file):
    dict = {} # new dictionary
    input = open (file, 'rU')
#    input.readline()    # In case the first few lines of the file have column tags or are blank, then uncomment 
##                          these lines so that they get removed.
#    input.readline()
#    input.readline()
    for line in input:
        Repeat = organize(line)
        if Repeat in dict:   # if Repeat is already one of the keys in the dictionary
            value = dict[Repeat]   # the line is added to the value of that key
            value.append(tuplize(line))
            dict[Repeat] = value
        else:
            tup = [tuplize(line)]
            dict[Repeat] = tup  # new key value pair is created.
    input.close()
    print 'no of repeat elements is :', len(dict)
    
    commonOut = open('L1_sortedbysize', 'w')
    
    sortedDict = {}
    
    for key in dict:
          # for every key in dictionary, create a new file using the key as the filename
        list = dict[key]
        commonOut.write(key + '\n')
        sortedList = sorted(list, key=sortFun, reverse = True)
        
        sortedDict[key] = sortedList[:50]
        
        
        for each in sortedList[:50]:
            
            commonOut.write(str(each)+ '\n')  # put the value of that key inside the file
         
        print key + '\t' + findLength(list[0])  + '\n'        # print all the keys, 1337 in total for hg18.fa.out
        
    pickled = open('L1_sorted_pickle', 'w')
    
    pickle.dump(sortedDict, pickled)
    
    commonOut.close()
        
        
"""
@param string:takes in one line of a string and splits the words using whitespace as a delimiter
@return : returns a list of words
"""
def organize(string):    
    list = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
#    repeat = list[9]  # in case the repeat element has '/' in it, it is replaced by '_'. This is done
    # because the repeat element name is used to make a file name, and file name cannot contain a '/'.
      
    return list[9]

def tuplize(string):
    list = string.split()
    if list[8] == '+':
        aLine = (int(list[0]), list[1],list[2],list[3], list[4], list[5], list[6], list[7],
             list[8], list[9], list[10], int(list[11]), int(list[12]), list[13], list[14])
    else:
        aLine = (int(list[0]), list[1],list[2],list[3], list[4], list[5], list[6], list[7],
             list[8], list[9], list[10], list[11], int(list[12]), int(list[13]), list[14])
    return aLine

def sortFun(list):
    
    return helpSortFun(list[:])

def helpSortFun(list):
    
    if list[8] == '+':
        length = list[12] - list[11]
    else :
        length = list[12] - list[13]
    return length
    


def findLength(list):
    
    if list[8] == '+':
        length = list[12] + int(list[13].strip('()'))
    else: # if repeats[0][0][8] == 'C':
        length = int(list[11].strip('()'))+ list[12]    
        
    return str(length)


def main():
    openfile = sys.argv[1]   
    Filter(openfile)   
 
if __name__ == '__main__':
    main()