#-------------------------------------------------------------------------------
# Name:        composite_analysis
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     30/01/2013
# Copyright:   (c) Gaurav Singhal 2013

# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------



import sys, pickle
from sets import Set



def composite_analysis():
    variants = Set()
    sampleNames = Set()

    variantStatus = {}
    variants_data = open('finally_validated_variants_coordinates.csv', 'rU').readlines()
    for line in variants_data[1:]:
        flds = line.strip().split(',')
        variants.add(flds[0]+'#'+flds[1])



    fastqFiles = open('listOfFiles', 'rU').readlines()

    sampleVariantDict = {}

    for eachPair in fastqFiles:
        files = eachPair.strip().split()
        se = files[0].find('_L001')
        sampleName = files[0][:se]
        sampleNames.add(sampleName)
        vcfFileName = sampleName +  '_hg19_ref_clean.vcf'
        sample_variant_data = open(vcfFileName,'rU').readlines()
        variantVCFdict = {}



        for line in sample_variant_data:

            if line[0] != '#':
##                flds = line.split('\t')
##                if len(flds[7].split(';'))>2:

                processVCFline(line, variantVCFdict)

        sampleVariantDict[sampleName] = variantVCFdict

    for eachVariant in variants:
        statusDict = {}
        for eachSample in sampleNames:
            sampleVariantData = sampleVariantDict[eachSample]
            if eachVariant in sampleVariantData.keys():
                statusDict[eachSample] = sampleVariantData[eachVariant]

        variantStatus[eachVariant] = statusDict

    variantSampleCoverageDict = {}

    for eachVariant in variants:
        sampleCoverageDict = {} # one variant, all samples and their respective coverages
        for eachSample in sampleNames:
            pileupFile = eachSample+ '_hg19_ref_mpileup.txt'
            pileupData = open(pileupFile, 'rU').readlines()
            for eachline in pileupData:
                flds = eachline.split('\t')
                location = flds[0][3:] + '#' + flds[1]
                if eachVariant == location:
                    sampleCoverageDict[eachSample] = flds[3]
                    break
        variantSampleCoverageDict[eachVariant] = sampleCoverageDict


    return variantStatus, variantSampleCoverageDict,sampleNames


def variantStatus2CSV():
    variantStatus ,variantSampleCoverageDict, sampleNames= composite_analysis()
    sampleNamesList = list(sampleNames)
    fhout = open('composite_variant_status.csv', 'w')
    outline = 'VARIANT_CHRM, VARIANT_POSITION,'
    for each in sampleNamesList:
        outline+= each+'_AF,' + each+'_DP,' + each+'_PVAL,' + each+ '_COVERAGE,'
    outline+='\n'
    fhout.write(outline)
    variants = variantStatus.keys()

    for eachVariant in variants:
        flds = eachVariant.split('#')
        outline=flds[0] + ','+ flds[1]+','
        statusDict = variantStatus[eachVariant]
        coverageDict = variantSampleCoverageDict[eachVariant]
        for eachSample in sampleNamesList:
            if eachSample in statusDict:
                sampleVariantData = statusDict[eachSample]
                AF = sampleVariantData['AF'][0]
                DP = sampleVariantData['DP'][0]
                PVAL = sampleVariantData['PVAL'][0]
                outline+=AF+','+DP+','+PVAL+','
            else:
                outline+='0,0,NA,'
            if eachSample in coverageDict:
                coverage = coverageDict[eachSample]
                outline+=coverage+','
            else:
                print eachVariant, '  ', eachSample, '  ',  'No coverage data!!'
                outline+='NA,'
        outline+='\n'
        fhout.write(outline)
    fhout.close()






def processVCFline(line, variantDict):
    flds = line.split('\t')
    key = flds[0].strip() + '#' + flds[1].strip()
    value = {}
    value['REF'] = flds[3].strip()
    value['ALT'] =   flds[4].strip().split(',') # ALT is a list
    for each in flds[7].strip().split(';'):
        info = each.partition('=')
        infoVal = info[2].split(',')
        value[info[0]] = infoVal  # DP, AF, PVAL, EFF are all lists
    variantDict[key] = value


def main():
    variantStatus2CSV()

if __name__ == '__main__':
    main()
