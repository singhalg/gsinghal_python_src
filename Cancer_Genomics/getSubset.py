#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     18/12/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys
from sets import Set

def getSubSet():

    unchecked = open('mutation_status_prim_metastasis_all_patients_V2_VarScan_prim_refbase_count_coverage_filt_man_recurrent_LS_blat.csv', 'rU').readlines()
    checked = open('previously_selected_variants_blat.csv', 'rU').readlines()

    previously_checked = Set()
    previously_checked_blat = {}

    outFileName = 'mutation_status_prim_metastasis_all_patients_V2_VarScan_prim_refbase_count_coverage_filt_man_recurrent_LS_blat_TBC.csv'

    outFile = open(outFileName, 'w')
    outFile.write(unchecked[0])



    for line in checked[1:]:
        flds = line.split(',')
        pos = flds[0] + '#' + flds[1]
        previously_checked.add(pos)
        previously_checked_blat[pos] = line

    for line in unchecked[1:]:
        flds = line.split(',')
        pos = flds[0] + '#' + flds[1]
        if pos in previously_checked:
            print previously_checked_blat[pos]
        else:
            outFile.write(line)

    outFile.close()



def main():
    getSubSet()

if __name__ == '__main__':
    main()
