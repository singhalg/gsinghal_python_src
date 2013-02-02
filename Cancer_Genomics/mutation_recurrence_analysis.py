#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     12/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import pickle, sys
from sets import Set

'''
This method takes the output (csv file) of mutationRecurrence2.py and split the csv file into a bunch of files.

    fhoutLOF1 = open('mutation_recurrence_LOF.csv', 'w')   Here, the ALT allele set has multiple ALT alleles
    fhoutLOF2 = open('mutation_recurrence_LOF_STOP_FS.csv', 'w')  Here, the ALT leads to a stop codon or Frameshift
    fhoutCOSMIC = open('mutation_recurrence_COSMIC.csv', 'w')   Here, the varants which are present in COSMIC are listed in top order.
    fhoutCOSMIC_noDBSNP = open('mutation_recurrence_COSMIC_noDBSNP.csv', 'w')  Here variants which are not present in dbSNP, but present in COSMIC are listed.

'''
def mutationRecurrenceDataSplit():
    fh = open('mutation_recurrence_results_metastasis.csv', 'rU')
    data = fh.readlines()
    fh.close()
    header = data[0]


    fhoutLOF1 = open('mutation_recurrence_met_LOF.csv', 'w')
    fhoutLOF2 = open('mutation_recurrence_met_LOF_STOP_FS.csv', 'w')
    fhoutCOSMIC = open('mutation_recurrence_met_COSMIC.csv', 'w')
    fhoutCOSMIC_noDBSNP = open('mutation_recurrence_met_COSMIC_noDBSNP.csv', 'w')
    fhoutLOF1.write(header)
    fhoutLOF2.write(header)
    fhoutCOSMIC.write(header)
    fhoutCOSMIC_noDBSNP.write(header)
    Mutations = []

    '''
    for eachline in data:
        fill aMutation for 1 complete mutation, make lists

    for eachMutation in mutations:




    '''
# LOSS of FUNCTION mutations ref != N, ALT allele set len > 1
# LOSS of func : ref != N, effect impact has high
# TOP COSMIC
# COSMIC yes, dnSNP yes
# COSMIC yes, dbSNP no

    mutationDetails = []

    for line in data[1:]:
        flds = line.split(',')

        if len(flds[0])>0:
            Mutations.append(mutationDetails)
            mutationDetails = []
            mutationDetails.append(line)
        else:
            mutationDetails.append(line)

##    print Mutations


    for eachMutation in Mutations[1:]:
        flds = eachMutation[0].split(',')
        impact = Set(flds[4].split('#'))
        ref = flds[2]
        ALT = Set([])
        for eachALT in eachMutation[1:]:
            alt_flds = eachALT.split(',')
            ALT.add(alt_flds[9])

        if ref != 'N':
            if len(ALT) >1:
                writeOut(eachMutation, fhoutLOF1)
            if 'HIGH' in impact:
                writeOut(eachMutation, fhoutLOF2)
            if flds[5] == 'Yes' and flds[6] =='Yes':
                writeOut(eachMutation, fhoutCOSMIC)
            if flds[5] == 'Yes' and flds[6] =='No':
                writeOut(eachMutation, fhoutCOSMIC_noDBSNP)


    fhoutLOF1.close()
    fhoutLOF2.close()
    fhoutCOSMIC.close()
    fhoutCOSMIC_noDBSNP.close()



def mutationSearch(fileName):

    fh = open(fileName, 'rU')
    data = fh.readlines()
    fh.close()
    outFileName = fileName[:-4] + '_fixed_in_met.csv'
    fhout = open(outFileName, 'w')

    header = data[0]
    fhout.write(header)
    Mutations = []
    mutationDetails = []

    for line in data[1:]:
        flds = line.split(',')

        if len(flds[0])>0:
            Mutations.append(mutationDetails)
            mutationDetails = []
            mutationDetails.append(line)
        else:
            mutationDetails.append(line)

    for eachMutation in Mutations[1:]:
        af = 0
        for each in eachMutation[1:]:
            af+= float(each.split(',')[23])
        av_af = float(af)/(len(eachMutation)-1)
        if av_af>=0.4:
            fhout.write(eachMutation[0])
##            print eachMutation[0]
    fhout.close()


def writeOut(lineList, fhout):
    for each in lineList:
        fhout.write(each)



def main():

    mutationSearch('mutation_recurrence_results_metastasis_VarScan.csv')

if __name__ == '__main__':
    main()
