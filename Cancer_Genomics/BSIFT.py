#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     16/10/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys, pickle

def getSIFTinput():
    fhall = open('mutation_status_prim_metastasis_all_patients.csv', 'rU')
    allVariants = fhall.readlines()
    fhoutAlt = open('mutation_status_all_patients_SIFT_input_alt_allele.txt', 'w')
    fhoutRef = open('mutation_status_all_patients_SIFT_input_ref_allele.txt', 'w')
##    fhoutAlt.write(allVariants[0])
##    fhoutRef.write(allVariants[0])
    index = [21,26,31,36,41,46,51,56,61]
    for line in allVariants[1:]:
        flds = line.strip().split(',')
        alt_allele = getAltAllele(flds)
        outline = flds[0] + ',' + flds[1] + ',1,' + flds[2] + "/" + alt_allele + '\n'
        fhoutAlt.write(outline)
        outlineRef = flds[0] + ',' + flds[1] + ',1,' + flds[2] + "/" + flds[2] + '\n'
        fhoutRef.write(outlineRef)
    fhoutAlt.close()
    fhoutRef.close()


'''
This method reads SIFT scores and writes them back to the csv files containing recurrent status of primary tumor mutations.
This method also saves the SIFT scores in a pickle.

'''

def readSiftScores():
    siftScores = {} # the dict which holds all the SIFT scores. keys are locations (genomic coordinates), and values are dicts. The value dict contains sift scores for ref and alt allele and other SIFT parameters.

    SIFT_ref = open('mutation_status_all_patients_SIFT_output_refAllele.txt', 'rU').readlines()

    SIFT_alt = open('mutation_status_all_patients_SIFT_output_alt_allele.txt','rU').readlines()

    for line in SIFT_ref[1:]:
        flds = line.split('\t')
        loc = flds[0].split(',')
        key = loc[0][3:] + '#' + loc[1]
        refScore = flds[9].strip()
##        msi = flds[10].strip()  # Median sequence information (would MSI be same for a particular location, be it REF allele or ALT allele) ?

        scores = {}

        scores['REF'] = refScore
##        scores['MSI'] = msi  # reading MSI and LowCoverage status from the reference alleles only, assuming that these statuses remain the same
                            # between alt allele and ref allele.
##        scores['SAP'] = flds[11].strip()
##        if flds[8].find('Low')>-1:
##
##            scores['LC'] = True
##        else:
##            scores['LC'] = False

        siftScores[key] = scores

    for line in SIFT_alt[1:]:
        flds = line.split('\t')
        loc = flds[0].split(',')
        key = loc[0][3:] + '#' + loc[1]
        altScore = flds[9].strip()
##        scores['MSI'] = flds[10].strip()  # reading MSI and LowCoverage status from the reference alleles only, assuming that these statuses remain the same
##                            # between alt allele and ref allele.
##        scores['SAP'] = flds[11].strip()

        if key in siftScores:

            scores = siftScores[key]
            scores['ALT']  = altScore
            if len(flds)>10:
                scores['MSI'] = flds[10].strip()  # reading MSI and LowCoverage status from the alternate alleles only, for a lot of alleles, these values are NA in ref allele output file

            #    scores['']
                scores['SAP'] = flds[11].strip()
            else:
                scores['MSI'] = ''
                scores['SAP'] = ''


            if flds[8].find('Low') > -1:

                scores['LC'] = True
            else:
                scores['LC'] = False


            siftScores[key] = scores
        else:
            print 'Error !!!'
            print line



    all_patients_mutation_info = open('mutation_status_prim_metastasis_all_patients.csv', 'rU').readlines()
    filtered_mutation_info = open('mutation_status_prim_metastasis_all_patients_coverage_filt.csv', 'rU').readlines()

    fhout_allVariants = open('mutation_status_prim_metastasis_all_patients_bsift.csv', 'w')
    fhout_filteredVariants = open('mutation_status_prim_metastasis_all_patients_coverage_filt_bsift.csv', 'w')

    outline = all_patients_mutation_info[0].strip() + 'SIFT_ALT,SIFT_REF,Median_Seq_Info,Low_Coverage,BSIFT,Seq_At_Position' + '\n'
    fhout_allVariants.write(outline)
    fhout_filteredVariants.write(outline)

    for line in all_patients_mutation_info[1:]:

        flds = line.strip().split(',')
        location = flds[0] + '#' + flds[1]
        if location in siftScores:

            scores = siftScores[location]
            ref = scores['REF']
            alt = scores['ALT']
            msi = scores['MSI']
            seq_at_pos = scores['SAP']
            if scores['LC']:

                lowCoverage = 'Low Coverage'
            else:
                lowCoverage = ''

            try:

                refScore = float(ref)
                altScore = float(alt)
                bsift = str(altScore - refScore)
            except:
                bsift = 'NA'

            outline = line.strip()  + alt + ',' + ref + ',' + msi + ',' + lowCoverage + ',' + bsift +','+seq_at_pos +'\n'
            fhout_allVariants.write(outline)
        else:
            fhout_allVariants.write(line)
    fhout_allVariants.close()


    for line in filtered_mutation_info[1:]:

        flds = line.strip().split(',')
        location = flds[0] + '#' + flds[1]
        if location in siftScores:
            scores = siftScores[location]
            ref = scores['REF']
            alt = scores['ALT']
            msi = scores['MSI']
            seq_at_pos = scores['SAP']
            if scores['LC']:

                lowCoverage = 'Low Coverage'
            else:
                lowCoverage = ''

            try:

                refScore = float(ref)
                altScore = float(alt)
                bsift = str(altScore - refScore)
            except:
                bsift = 'NA'

            outline = line.strip()  + alt + ',' + ref + ',' + msi + ',' + lowCoverage + ',' + bsift +','+seq_at_pos +'\n'
            fhout_filteredVariants.write(outline)
        else:
            fhout_filteredVariants.write(line)
    fhout_filteredVariants.close()

    fhPickle = open('sift_scores_all_patients_prim_mutations.pkl', 'w')
    pickle.dump(siftScores, fhPickle)
    fhPickle.close()

def getAltAllele(alist):

    index = [21,26,31,36,41,46,51,56,61]
    for each in index:
        if len(alist[each])>0:
            return alist[each]
    return ''

def main():
##    getSIFTinput()
    readSiftScores()

if __name__ == '__main__':
    main()
