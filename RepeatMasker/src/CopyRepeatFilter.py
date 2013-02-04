

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


"""
@param file: The file that needs to be parsed. Usually, this is an output of repeat masker. 
@param : repFamily : string, which is the name of the repeat family
@param : boolean : write : true / false or 0/1 , if true, this method creates a new file and write the output to that file.
return : returns a list of all the lines in the input file that contain repFamily in col[9]
"""

def Filter(file):
    dict = {}
        
    input = open (file, 'rU')
    input.readlines()    # removing the first 3 lines of the file; these 3 lines do not contain the target info
#    input.readline()
#    input.readline()
#    for line in input:
#        Repeat = organize(line)
#        if Repeat in dict:
#            value = dict[Repeat] + line
#            dict[Repeat] = value
#        else:
#            dict[Repeat] = line
#    
#    input.close()
#    
#    print 'no of repeat elements is :', len(dict)
#    
##    for key in dict.keys():
##        print dict[key]
#    
#    for key in dict:
#        out = open(key, 'w')
#        out.write(dict[key])
#        out.close()
#        print key
#            

    
"""
@param string:takes in one line of a string and splits the words using whitespace as a delimiter
@return : returns a list of words
"""
def organize(string):    
    list = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    repeat = list[9].replace('/','_')    
    return repeat
   

def main():
    openfile = sys.argv[1]   
    Filter(openfile)   
 
if __name__ == '__main__':
    main()