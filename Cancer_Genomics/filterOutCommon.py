#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     31/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------
import random
from sets import Set

def filterOutCommonSNP():

    fhin =  open('PT_11_variant_diff_cutoff_strict.csv', 'rU')
    allVariants = fhin.readlines()
    fhin.close()

    fhin = open('snpInExon_AGILENT_count', 'rU')
    commonVariants = fhin.readlines()
    fhin.close()

    fhout = open('PT_11_variant_diff_cutoff_strict_FOcommon.csv', 'w')


    allVariantSet = Set([])
    commonVariantSet = Set([])


    for line in commonVariants:
        flds = line.split('\t')
        key = flds[0].strip() + '#' +flds[2].strip()
        commonVariantSet.add(key)
    print '# of variants in commonVariantSet = ', len(commonVariantSet)


    print 'Length of all variant set = ', len(allVariants)

    for line in allVariants:
        flds = line.split(',')
        key = flds[0].strip() + '#' +flds[1].strip()
        if key in commonVariantSet:
            pass
        else:
            fhout.write(line)

    fhout.close()
    print '# of variants in allVariantSet = ', len(allVariantSet)
##
##    print 'Length of common variants = ', len(commonVariants)
##
##    commonFilterOut = allVariantSet & commonVariantSe

##
##    print '# of common variants that can be filtered out are  = ', len(commonFilterOut)


def sampleRandomly(percent):
    fhin = open('PT_11_variant_diff_cutoff_strict_FOcommon.csv', 'rU')
    data = fhin.readlines()
    fhin.close()

    percent = int(percent)
    fhout = open('PT_11_variant_diff_cutoff_strict_FOcommon_random10p.csv', 'w')

    Range = len(data)/percent

    for i in range(Range):
        st = i*percent
        end = (i+1)*percent
        randLoc = random.randint(st, end)
        if randLoc >= len(data):
            print randLoc
        else:
            fhout.write(data[randLoc])

    fhout.close()



def main():
    filterOutCommonSNP()
    sampleRandomly(10)

if __name__ == '__main__':
    main()
