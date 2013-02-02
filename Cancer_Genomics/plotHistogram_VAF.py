#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     26/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import sys
import numpy as np

def plotHistogram(fileName):

    fhin = open(fileName, 'rU')
    data = fhin.readlines()
    fhin.close()

    pvafs = []
    allData = []

    for line in data:
        flds = allData.append(line.strip().split(','))


##        value = float(line.strip())
##
##        if value<=100:
##
##            pvafs.append(value)
    for each in allData[1:]:
        if (float(each[7])>=15) and (float(each[7])<=70):
            pvafs.append(float(each[7]))

    print len(pvafs)
    print pvafs[:10]

    plt.hist(pvafs, bins=200)
    plt.xlabel('VAF')
    plt.ylabel('# of variants')
##    plt.legend(fileName[:-4], loc=9)

    plt.show()

##    imageName = fileName[:-4] + '.png'
##    plt.savefig(imageName)

def main():
##    fileName = sys.argv[1]
    plotHistogram('newVarScan_noCommon/PT_10_VarScan_no_commonV2.csv')

if __name__ == '__main__':
    main()
