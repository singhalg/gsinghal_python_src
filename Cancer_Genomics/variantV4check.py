#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     02/10/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys, pickle

def readV4():
    fh  = open('SureSelect_V4_All_Exon_51mb_with_annotation.hg19.bed', 'rU')
    data = fh.readlines()
    fh.close()
    targets = []
    for line in data:
        flds = line.strip().split('\t')
        entry = [flds[0][3:], int(flds[1]), int(flds[2])]
        targets.append(entry)

    fhout = open('V4_all_targets.pkl', 'w')
    pickle.dump(targets, fhout)
    fhout.close()


def checkVariant(variant):
    fhin = open('V4_all_targets.pkl', 'rU')
    targets = pickle.load(fhin)
    fhin.close()

    chrom = variant.split('_')[0]
    pos = int(variant.split('_')[1])
    for each in targets:
        if chrom == each[0]:
            if (pos >= each[1]) and (pos<= each[2]):
                print 'Variant present in V4 Target'
                print 'Target is : ', each
                print ' Variant is: ',variant
                sys.exit()
    print 'Variant not present in V4 Target'




def main():
##    readV4()
    checkVariant('10_51363294')




if __name__ == '__main__':
    main()
