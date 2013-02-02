#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     24/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys


def surveyPileup(fileName):

    fh = open(fileName, 'rU')
    symbols = {}

    for line in fh:
        flds = line.split('\t')
        pile = flds[4].strip()
        l = len(pile)
        for i in range(l):
            if pile[i] =='^':
                newChar = pile[i+1]
                if newChar in symbols:
                    count = symbols[newChar]
                    count+=1
                    symbols[newChar] = count
                else:
                    symbols[newChar] = 1

            else:
                pass
    fh.close()
    newChars = symbols.keys()
    symbolsList = []
    for each in newChars:
        symbolsList.append([each, symbols[each]])

    symbolsListSorted = sorted(symbolsList, key=myFun, reverse=True)

    print symbolsListSorted[:50]


def myFun(alist):
    return alist[1]


def main():
    fileName = sys.argv[1]
    surveyPileup(fileName)

if __name__ == '__main__':
    main()
