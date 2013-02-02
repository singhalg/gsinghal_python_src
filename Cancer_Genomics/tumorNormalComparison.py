#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     21/12/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------


import sys, pickle
from sets import Set


'''
Given the set of variant pickles, it calculates true positives, false positives, false negatives.

'''

def SensSpec(patientNum, predicted_del_somatic):

    allTrueSomatic = patientNum + '_somatic.pkl'

    trueSomaticVariants = pickle.load(open(allTrueSomatic, 'rU'))

    somatic_del = {}

    for each in trueSomaticVariants.keys():

        variantElement = trueSomaticVariants[each]
        if 'Functional_Class' in variantElement:

            if ('MISSENSE' in variantElement['Functional_Class']) or ('NONSENSE' in variantElement['Functional_Class']):

                somatic_del[each] = trueSomaticVariants[each]

    outPickleName = patientNum + '_true_somatic_del.pkl'
    outPickle = open(outPickleName, 'w')
    pickle.dump(somatic_del, outPickle)
    outPickle.close()

    likelySomatic = pickle.load(open(predicted_del_somatic, 'rU'))


    FalsePositivePos = Set(likelySomatic.keys()) - Set(somatic_del.keys())

    FalsePositive = {}
    for each in FalsePositivePos:
        FalsePositive[each] = likelySomatic[each]

    fpPickleName = patientNum + '_false_positives.pkl'
    fpPickle = open(fpPickleName, 'w')
    pickle.dump(FalsePositive, fpPickle)
    fpPickle.close()

    TruePositivePos = Set(likelySomatic.keys()) & Set(somatic_del.keys())

    TruePositive = {}
    for each in TruePositivePos:
        TruePositive[each] = likelySomatic[each]

    tpPickleName = patientNum + '_true_positives.pkl'
    tpPickle = open(tpPickleName, 'w')
    pickle.dump(TruePositive, tpPickle)
    tpPickle.close()



    FalseNegativePos =  Set(somatic_del.keys()) -  Set(likelySomatic.keys())

    FalseNegative = {}
    for each in FalseNegativePos:
        FalseNegative[each] = somatic_del[each]

    fnPickleName = patientNum + '_false_negatives.pkl'
    fnPickle = open(fnPickleName, 'w')
    pickle.dump(FalseNegative, fnPickle)
    fnPickle.close()

    print "# of predicted somatic variants = ", len(likelySomatic.keys())

    print "# of true somatic variants = ", len(somatic_del.keys())

    print "# of false positive variants = ", len(FalsePositivePos)

    print "# of true positive variants = ", len(TruePositivePos)


    print "# of false negative variants = ", len(FalseNegativePos)



def writePickles2CSV(patientNum):

    pass

def main():
    patientNum = sys.argv[1]
    likelySomaticPickle = sys.argv[2]

    SensSpec(patientNum, likelySomaticPickle)

if __name__ == '__main__':
    main()
