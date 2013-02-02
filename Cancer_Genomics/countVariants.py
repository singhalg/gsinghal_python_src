#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     04/01/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import pickle, sys
import numpy as np
from sets import Set


def count_variants():


    files = [   ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],
                ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                [ 'PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']  ]

    for eachFile in files:


        end = eachFile[0].find('_lung')   ####----------------==============----------===========-------------=============
        fileName2 = eachFile[0][:end] + '_brain_VarScan_clean_snpEff_SnpSift.pkl'
        fileName = eachFile[0][:end] + '_brain_VarScan_clean_snpEff_SnpSift_rare_del.pkl'  #-----========---------========--------
        data = pickle.load(open(fileName, 'rU'))
        data2 =pickle.load(open(fileName2, 'rU'))
        print fileName
        print len(data.keys())
        print fileName2
        print len(data2.keys())

def main():
    count_variants()

if __name__ == '__main__':
    main()
