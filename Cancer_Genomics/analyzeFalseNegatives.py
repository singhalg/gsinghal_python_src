#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     31/12/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import pickle, sys
import numpy as np
from sets import Set


def analyzeFalseNegatives():

    commonEVS = pickle.load(open('commonEVS.pkl', 'rU'))
    agilentCommon = pickle.load(open('agilent_V3_common.pkl', 'rU'))
    IlluminaCommon = pickle.load(open('Illumina_common.pkl', 'rU'))
    Illumina_agilent = pickle.load(open('Illumina_Agilent_common.pkl', 'rU'))
    dbSNP           = pickle.load(open('dbSNPcommon_nonClinical.pkl', 'rU'))

    dbSNPcommon = Set(dbSNP.keys())
    del dbSNP

    allCommon = commonEVS | agilentCommon | IlluminaCommon | Illumina_agilent | dbSNPcommon

    del commonEVS, agilentCommon,IlluminaCommon,Illumina_agilent,dbSNPcommon

    files = ['2221_false_negatives.pkl', '2359_false_negatives.pkl', '2556_false_negatives.pkl', '3466_false_negatives.pkl']

    for each in files:
        data = pickle.load(open(each, 'rU'))
        pos = Set(data.keys())
        commonPos = pos & allCommon
        print "# variants in ", each, ' = ', len(pos)
        print "#  common polymorphisms in ", each, ' = ', len(commonPos)
        del data, pos, commonPos




def main():
    analyzeFalsePositives()

if __name__ == '__main__':
    main()
