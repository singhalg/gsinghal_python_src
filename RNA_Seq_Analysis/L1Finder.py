'''
Created on Feb 14, 2011

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

'''

import sys
import re

def L1finder(filename):
    repeatLib = open (filename, 'rU')
    int = 0
    filtered = open('L1', 'w')
    switch = False
    for line in repeatLib:
        if line[0] == '>':
            if re.search('L1', line):
                int+= 1
                switch = True
                filtered.write(line)
                
            else:
                switch = False
        else :
            if switch :
                filtered.write(line)
        

    
    repeatLib.close()
    filtered.close()
    print int

def main():
    file = sys.argv[1]
    L1finder(file)
    
    
if __name__ == '__main__':
    main()
    




