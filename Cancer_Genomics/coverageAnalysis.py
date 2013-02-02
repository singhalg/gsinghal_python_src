#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     15/10/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import pickle, sys, math
from sets import Set

def coverage():

    pt_list = ['PT_1', 'PT_2', 'PT_3', 'PT_6', 'PT_9', 'PT_10', 'PT_11', 'PT_12', 'PT_13']

    allPatientLocations = pickle.load(open('allPatientsLocations.pkl', 'rU'))
    allPatientCoverage = {}
    for each in allPatientLocations:

        allPatientCoverage[each] = []

    for each in pt_list:
        locationsInPatient = Set([])
        fileName = each + '_lung_mpileup.txt'
        fh = open(fileName, 'rU')
        for line in fh:
            flds = line.split('\t')
            key = flds[0][3:].strip() + '#' + flds[1].strip()
            locationsInPatient.add(key)


            pt_coverage = allPatientCoverage[key]

            pt_coverage.append(int(flds[3].strip()))

            allPatientCoverage[key] = pt_coverage

##            else:
##                pt_coverage = [int(flds[3].strip())]
##                allPatientCoverage[key] = pt_coverage

        fh.close()

        notFoundInPatient = allPatientLocations-locationsInPatient
        for each in notFoundInPatient:
            pt_coverage = allPatientCoverage[each]
            pt_coverage.append(0)
            allPatientCoverage[each] = pt_coverage
        del notFoundInPatient, locationsInPatient



##    allPatientCoverageList = []
##    locations = allPatientCoverage.keys()
##    for eachLoc in locations:
##
##        patientDict = allPatientCoverage[eachLoc]
##        allPatientCoverageList.append([eachLoc, len(patientDict.keys())])
##        del patientDict
##
##
##    allPatientCoverageListSorted = sorted(allPatientCoverageList, reverse=True, key = myFun)
##
##    fhCoverageList = open('allPatientsCoverageList.pkl', 'w')  #/////----///---////----
##    pickle.dump(allPatientCoverageListSorted, fhCoverageList)
##    fhCoverageList.close()

    fhAllCoverage = open('allPatientsCoverage.pkl', 'w')
    pickle.dump(allPatientCoverage, fhAllCoverage)
    fhAllCoverage.close()

'''
This method generates a set of all the locations where there is coverage in the different mpileup files. The mpileup files also limited to the
coordinates of the Illumina Truseq, Agilent V3 and V4 platforms. So, for example, there is a location in the exome which is officially outside
the coverage region (coordinates) for Illumina TruSeq ad Agilent V3, but within the coverage coordinates for V4. So, for such a location, the coverage
in Illumina patient (PT_1) and Agilent V3 patients (PT_9,10,11,12) will be zero, even if some reads did align to those locations.
Also, if a variant happens to exist at this location, then it will be called only in V4 because variant calls were generated from filtered mpileups and
not the raw alignment files (bam files). So, in the recurrence lists, the variant will show up as absent from V3 and Illumina, but will show up
as a variant when the bam files for the other patients are viewed in IGV.

'''
def surveyLocations():

    pt_list = ['PT_1', 'PT_2', 'PT_3', 'PT_6', 'PT_9', 'PT_10', 'PT_11', 'PT_12', 'PT_13']

    allPatientsLocations = Set([])

    for each in pt_list:
        fileName = each + '_lung_mpileup.txt'
        fh = open(fileName, 'rU')
        for line in fh:
            flds = line.split('\t')
            key = flds[0][3:].strip() + '#' + flds[1].strip()

            allPatientsLocations.add(key)
            del flds, key
        fh.close()
    fhLocations = open('allPatientsLocations.pkl', 'w')
    pickle.dump(allPatientsLocations,fhLocations)
    fhLocations.close()



def myFun(alist):
    return alist[1]

def main():
    coverage()
##    surveyLocations()

if __name__ == '__main__':
    main()
