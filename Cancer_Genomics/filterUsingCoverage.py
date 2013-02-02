#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     16/10/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------


import pickle, sys

def filterUsingCoverage(variantFileName):


    recurrentVariantData = (open(variantFileName, 'rU')).readlines()

    coverageData = pickle.load(open('allPatientsCoverage.pkl', 'rU'))  #---///---//------

    outfile = variantFileName[:-4]+'_coverage_filt.csv'
    fhout = open(outfile, 'w')
    fhout.write(recurrentVariantData[0])
    for eachVariant in recurrentVariantData[1:]:
        flds = eachVariant.split(',')
        location = flds[0] + '#' + flds[1]
        coverage = coverageData[location]

        if checkCoverage(coverage):
            fhout.write(eachVariant)

    fhout.close()
'''
This method takes in a list of 9 numbers,
'''
def checkCoverage(aList):
    score=0
    for each in aList:
        if each>=10:
            score+=1
    if score>=6:  #---//------//---    This means that the variant should have coverage of 10 or more in atleast 6 patients (primary/metastasis, depending on analysis).
        return True


def main():
    inFile = sys.argv[1]
    filterUsingCoverage(inFile)

if __name__ == '__main__':
    main()
