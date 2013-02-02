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


import math, pickle, sys

def pValueDensity(fileName):
    fh = open(fileName, 'rU')
    data = fh.readlines()
    fh.close()
    logPvalues = []
    for line in data:
        if line[0] != '#':
            flds = line.split('\t')
            rawPval = flds[9].strip().split(':')[7]

            try:
                pval = (math.log10(float(rawPval))) *-1
                logPvalues.append(pval)
            except:
                print rawPval
    fhoutName = fileName[:-4] + '_pval.csv'
    fhout = open(fhoutName, 'w')
    for eachVal in logPvalues:
        outline = str(eachVal) + '\n'
        fhout.write(outline)
    fhout.close()





def main():
    fileName = sys.argv[1]

    pValueDensity(fileName)

if __name__ == '__main__':
    main()
