#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     24/01/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys

def refBase_filter(fileName):
    data  = open(fileName, 'rU').readlines()
    fhoutname = fileName[:-4]+'_refbase_filtered.csv'

    fhout = open(fhoutname, 'w')

    fhout.write(data[0])

    for each in data[1:]:
        flds = each.strip().split(',')
        if check_af(flds[-9:]):
            fhout.write(each)

    fhout.close()


def check_af(af):

    for each in af:
        if (len(each)>0) and (float(each)==1.0):
            return True   # if any of the ref_base (allele freq of reference base) is 1.0, then we return True, and that line included in the output

    return False


def main():
    fileName = sys.argv[1]
    refBase_filter(fileName)

if __name__ == '__main__':
    main()
