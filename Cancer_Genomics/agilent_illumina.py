#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     05/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

from sets import Set
import pickle

def compareAgilentIllumina():
    fhin = open('snpInExon_AGILENT_count', 'rU')
    internalVariants = fhin.readlines()
    fhin.close()

    allAgilentVariants = Set([])
    commonAgilentVariants = Set([])


    for line in internalVariants:
        flds = line.split('\t')
        key = flds[0].strip()[3:] + '#' +flds[2].strip()
        allAgilentVariants.add(key)
        if int(flds[4].strip())>=5:
            commonAgilentVariants.add(key)
    print 'total # of variants in agilent = ', len(allAgilentVariants)
    print '# of common variants in agilent = ', len(commonAgilentVariants)
    fhAgilent = open('agilent_V3_common.pkl', 'w')
    pickle.dump(commonAgilentVariants, fhAgilent)
    fhAgilent.close()

    fhin = open('Illumina_filter_count', 'rU')
    illuminaVariants = fhin.readlines()
    fhin.close()

    allIlluminaVariants = Set([])
    commonIlluminaVariants = Set([])


    for line in illuminaVariants:
        flds = line.split('\t')
        key = flds[0].strip()[3:] + '#' +flds[2].strip()
        allIlluminaVariants.add(key)
        if int(flds[3].strip())>=5:
            commonIlluminaVariants.add(key)
    print 'total # of variants in Illumina = ', len(allIlluminaVariants)
    print '# of common variants in Illumina = ', len(commonIlluminaVariants)
    fhIllumina = open('Illumina_common.pkl', 'w')
    pickle.dump(commonIlluminaVariants, fhIllumina)
    fhIllumina.close()

    commonAgilentIllumina = commonAgilentVariants & commonIlluminaVariants
    fhIlluminaAgilent = open('Illumina_Agilent_common.pkl', 'w')
    pickle.dump(commonAgilentIllumina, fhIlluminaAgilent)
    fhIlluminaAgilent.close()

    print 'Overlap between all variants of agilent and Illumina = ', len(allAgilentVariants & allIlluminaVariants)
    print 'Overlap between common variants of agilent and Illumina = ', len(commonAgilentVariants & commonIlluminaVariants)

def main():
    compareAgilentIllumina()

if __name__ == '__main__':
    main()
