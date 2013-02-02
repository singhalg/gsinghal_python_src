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

python AlignmentFilter.py Overlaphg19WithmappedRepeats

'''


import sys


"""
@param file: hg19.fa.out : This is repeat masker output
@return : Makes a file for each repeat family (such as Alu, LINE etc) present in the overlap output. 
Each of such file contains all the lines from the overlap output that belong to that repeat element.
"""

def Filter(file):
    dict = {} # new dictionary
    input = open (file, 'rU')
    #input.readline()    # In case the first few lines of the file have column tags or are blank, then uncomment 
    #                      these lines so that they get removed.
    #input.readline()
    #input.readline()
    for line in input:
        Repeat = organize(line)
        if Repeat in dict:   # if Repeat is already one of the keys in the dictionary
            value = dict[Repeat] + line   # the line is added to the value of that key
            dict[Repeat] = value
        else:
            dict[Repeat] = line  # new key value pair is created.
    input.close()
    
    
    
    print ' # of repeat families identified is :', len(dict)
    for key in dict:
        out = open(key, 'w')  # for every key in dictionary, create a new file using the key as the filename
        out.write(dict[key])  # put the value of that key inside the file
        out.close()
        print key           # print all the keys, 1337 in total for hg18.fa.out
        
      
      
    result = open('filtered', 'w')
    result.write(' # Repeat Families = ' + str(len(dict)) + '\n')  
    for key in dict:
        count = countLines(key)
        result.write(key + '\t' + count + '\n')
    result.close()
    
        
"""
@param string:takes in one line of a string and splits the words using whitespace as a delimiter
@return : returns a list of words
"""
def organize(string):    
    list = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    
    repeat = list[9]
    
    repeatFam = repeat.split('#')
    
    repeatType = repeatFam[1].replace('/','_')  # in case the repeat element has '/' in it, it is replaced by '_'. This is done
    # because the repeat element name is used to make a file name, and file name cannot contain a '/'.
      
    return repeatType
   

def countLines(filename):
    file = open(filename, 'rU')
    return str(len(file.readlines()))



def main():
    openfile = sys.argv[1]   
    Filter(openfile)   
 
if __name__ == '__main__':
    main()