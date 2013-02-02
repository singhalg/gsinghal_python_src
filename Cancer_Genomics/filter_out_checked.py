#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     18/10/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import pickle, sys
from sets import Set

def filter_out_checked():
    pre_checked = open('pre_checked.csv', 'rU').readlines()
    bsift_all = open('mutation_status_prim_metastasis_all_patients_bsift.csv', 'rU').readlines()
    bsift_coverage_checked = open('mutation_status_prim_metastasis_all_patients_coverage_filt_bsift.csv', 'rU').readlines()
    fhout_bsift_all = open('mutation_status_prim_metastasis_all_patients_bsift_TBC.csv', 'w')
    fhout_bsift_coverage_pass = open('mutation_status_prim_metastasis_all_patients_coverage_filt_bsift_TBC.csv', 'w')
    fhout_bsift_all.write(bsift_all[0])
    fhout_bsift_coverage_pass.write(bsift_all[0])


    positions = Set([])
    for line in pre_checked:
        flds = line.strip().split(',')
        if line[0] != ",":
            location = flds[0] + '#' + flds[1]
            positions.add(location)
        else:
            pass
    for line in bsift_all[1:]:
        flds=  line.split(',')
        pos = flds[0] + '#' + flds[1]
        if pos not in positions:
            fhout_bsift_all.write(line)
        else:
            pass
    fhout_bsift_all.close()


    for line in bsift_coverage_checked[1:]:
        flds=  line.split(',')
        pos = flds[0] + '#' + flds[1]
        if pos not in positions:
            fhout_bsift_coverage_pass.write(line)
        else:
            pass
    fhout_bsift_coverage_pass.close()







def main():
    filter_out_checked()

if __name__ == '__main__':
    main()
