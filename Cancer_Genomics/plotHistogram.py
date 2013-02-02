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

def plotHistogram(fileName):

    fhin = open(fileName, 'rU')
    data = fhin.readlines()
    fhin.close()

    pvals = []

    for line in data:
        value = float(line.strip())
        if value<=100:

            pvals.append(value)

    plt.hist(pvals, bins=100)
    plt.xlabel('-log10(p)')
    plt.ylabel('# of variants')
##    plt.legend(fileName[:-4], loc=9)

    plt.show()

##    imageName = fileName[:-4] + '.png'
##    plt.savefig(imageName)

def main():
##    fileName = sys.argv[1]
    plotHistogram('PT_13_brain_VarScanpval.csv')

if __name__ == '__main__':
    main()
