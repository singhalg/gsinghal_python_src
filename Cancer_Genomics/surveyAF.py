#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     22/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys
import math


def surveyAF(csvFile):
    fhin = open(csvFile, 'rU')
    data = fhin.readlines()
    fhin.close()
    prim_vaf = []
    met_vaf = []
    significant = 0
    insignificant = 0
    insignf = []

    fhout = open('PT_2_variant_diff_cutoff_strict_dp100_fc1.1.csv', 'w')


    for line in data[1:]:
        flds =  line.split(',')
        prim = float(flds[5])

        met = float(flds[6])
        if (prim == 0) or (met == 0):
            pass
        else:
            if prim >= met:
                greater = prim
                smaller = met
            else:
                greater = met
                smaller = prim
            change = greater/smaller
            if change >=1.1:
                significant+=1
                prim_vaf.append(prim)
                met_vaf.append(met)
                fhout.write(line)
            else:
                insignificant+=0
                insignf.append([prim, met])

    fhout.close()

    print '# of significant variants = ', significant
    print insignf[:100]





def main():
    surveyAF('PT_2_variant_diff_cutoff_strict_dp100.csv')

if __name__ == '__main__':
    main()
