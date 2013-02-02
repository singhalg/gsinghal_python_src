#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     26/10/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys, pickle
from sets import Set

def count_refBases(inFile):
    data = open(inFile, 'rU').readlines()
    outFile = inFile[:-4] + '_prim_refbase_count.csv'

    fhout = open(outFile, 'w')
    outline  = data[0].strip() + 'PT_1,PT_2,PT_3,PT_6,PT_9,PT_10,PT_11,PT_12,PT_13' +'\n'
    fhout.write(outline)

    variant_locations = Set([])

    mpileup = {}

    pt_list = ['PT_1', 'PT_2', 'PT_3', 'PT_6', 'PT_9', 'PT_10', 'PT_11', 'PT_12', 'PT_13']


    for line in data[1:]:
        flds  = line.split(',')
        chrm = flds[0]
        position = flds[1]
        refAllele = flds[6]
        key = chrm + '#' + position
        variant_locations.add(key)


    for each_mpileup in pt_list:
        fileName = each_mpileup +'_lung_mpileup.txt'  #---//---/--//--/ change this to _lung_mpileup.txt
        fh_mpileup = open(fileName, 'rU')
        for line in fh_mpileup:
            flds = line.split('\t')
            key = flds[0][3:] + '#' + flds[1]
            if key in variant_locations:
                if key in mpileup:
                    all_patients_mpileup = mpileup[key]
                    all_patients_mpileup[each_mpileup] = line
                    mpileup[key] = all_patients_mpileup


                else:
                    all_patients_mpileup = {}
                    all_patients_mpileup[each_mpileup] = line
                    mpileup[key] = all_patients_mpileup

    for line in data[1:]:

        flds  = line.split(',')
        location = flds[0]  +'#' + flds[1]

        mpileup_info = mpileup[location]
        refAllele_percentage = ''

        for eachPT in pt_list:
            if eachPT in mpileup_info:
                mpileupLine = mpileup_info[eachPT]
                flds = mpileupLine.split('\t')

                refAllele_percentage += count_refalleles(flds[3], flds[4]) + ','
            else:
                refAllele_percentage+=','

        outline = line.strip() + refAllele_percentage[:-1] + '\n'
        fhout.write(outline)

    fhout.close()







def count_refalleles(dep, pileup):
    depth = int(dep)
    ct = pileup.count('.')
    ct+= pileup.count(',')
    return  str(ct/float(depth))








def main():
    inFile = sys.argv[1]
    count_refBases(inFile)

if __name__ == '__main__':
    main()
