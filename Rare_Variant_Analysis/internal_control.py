#-------------------------------------------------------------------------------
# Name:        internal_control
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     12/04/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------





from sets import Set
import pickle
import sys

def readEVSvcf(fileName):
    fh = open(fileName, 'rU')
    data = fh.readlines()
    fh.close()
    variantsVCF = {}
##    varSet = Set([])

    for line in data:
        if line[0] != '#':
            processVCF(line, variantsVCF)

        else:
            pass


##    print '# of all variants in EVS file = ', len(variantPos)
##    print '# of common variants in EVS file = ', len(varSet)
    variantLocations = Set(variantsVCF.keys())
    return variantLocations

def processVCF(line, variantDict):
    flds = line.split('\t')
    key = flds[0].strip() + '#' + flds[1].strip()
    value = {}
    value['REF'] = flds[3].strip()
    value['ALT'] = flds[4].strip()
##    for each in flds[7].strip().split(';'):
##        info = each.partition('=')
##        infoVal = info[2].split(',')
##        value[info[0]] = infoVal
    variantDict[key] = value



def combineVariantCalls():
    fileList = ['ATGACAG', 'CGGTGGC', 'TACATGG', 'GTACGGC']
    all_variants = Set([])
    for each in fileList:
        vcfFile = each + '_snpEff_SnpSift_GWAS.vcf'
        all_variants= all_variants | readEVSvcf(vcfFile)


    fhout = open('Dysplasia_control_samples.pkl', 'w')
    pickle.dump(all_variants, fhout)
    fhout.close()





def main():
    combineVariantCalls()

if __name__ == '__main__':
    main()

