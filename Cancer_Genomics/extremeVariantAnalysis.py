#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     28/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys


def extremeVariantAnalysis(extremeVariantFile):

    fh = open(extremeVariantFile, 'rU')
    data = fh.readlines()
    fh.close()

    geneRecur = {}


    for line in data[1:]:

        flds = line.split(',')
        gene = flds[3].strip()
        if gene in geneRecur:
            val = geneRecur[gene]
            val+=1
            geneRecur[gene] = val

        else:
            geneRecur[gene] = 1

    genes = geneRecur.keys()
    geneList = []
    for agene in genes:

        geneList.append([agene, geneRecur[agene]])

    print sorted(geneList, reverse=True, key=myFun)

    return genes

def myFun(field):
    return field[1]


def main():
    extremeVariantAnalysis('extreme_variants.csv')

if __name__ == '__main__':
    main()
