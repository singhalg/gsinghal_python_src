'''

#-------------------------------------------------------------------#
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : July 28, 2010                                           #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

'''
#!/usr/bin/python
import sys


"""
@param file: Repeat Masker output hg18.fa.out 
@return : Prints the total number of lines in the file. Also prints the number of unique repeat elements in the file.
"""

def RepeatCounter(file):
    Repeats = []  
    input = open (file, 'rU')
#    input.readline()    # removing the first 3 lines of the file; these 3 lines do not contain the target info
#    input.readline()
#    input.readline()
    for line in input:
        Repeats.append(organize(line))    
    elements = set(Repeats)   # unique members in Repeats are now in elements
    print Repeats[:50]
    print 'length of Repeats = ',len(Repeats)
    print 'length of elements = ', len (elements)



"""
@param string:takes in one line of a string and splits the words using whitespace as a delimiter
@return : returns a list of words
"""
def organize(string):   
    list = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    return list[9]
    

def main():
    openfile = sys.argv[1]
    RepeatCounter(openfile)   
 
if __name__ == '__main__':
    main()