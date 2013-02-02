#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     04/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------



def phredScore(astring):
    score = 0
    for each in astring:
        score+= ord(each)
    print float(score)

def main():
    phredScore('9.02784544..08')

if __name__ == '__main__':
    main()
