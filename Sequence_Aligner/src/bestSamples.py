#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     25/05/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from sets import Set
import sys, os

def getTopSamples():
    fh = open('YRI_lowCoverage.csv', 'rU')
    data = fh.readlines()
    fh.close()
    topSamples = Set([])

    for line in data[1:]:
        flds = line.split(',')

        if (flds[20].strip()== '0'):
            sampleName = flds[9].strip()
            topSamples.add(sampleName)
    topYRI = list(topSamples)
    fh = open('allTopSamples.csv', 'rU')
    data = fh.readlines()
    fh.close()
    allTopSamples = {}
    for line in data[1:]:
        flds = line.split(',')

        allTopSamples[flds[0]] = float(flds[2].strip())
    toplist = []

    for each in topYRI:
        if each in allTopSamples:
            toplist.append([each, allTopSamples[each]])
        else:
            toplist.append(['null', 'null'])
    sortedTopList = sorted(toplist, key = myFun, reverse=True)

    print sortedTopList

def myFun(ls):
    return ls[1]



def main():
    getTopSamples()

if __name__ == '__main__':
    main()
