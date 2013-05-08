#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     10/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------
import sys, pickle
from sets import Set

'''
reads the vcf file having dbSNP variants, saves them to a pickle. Considers only those variants as common which either have GMAF>=0.1 or have a G5A tag.
'''

"""
The read_dbSNP method has been edited to read all_common.vcf. This vcf file contains only common SNPs derived from 1000 genomes, CSHL-Hapmap, ESV project etc.


"""
def read_dbSNP(fileName, outfileName, build, maf):
    fh = open(fileName, 'rU')
    gmaf = float(maf)
    buildID = int(build)
    variantsVCF = {}
    commonVariantsVCF = {}

    for line in fh:
        if line[0] != '#':

            processVCF(line, variantsVCF, buildID, gmaf)

        else:
            pass
    fh.close()

##    variantPos = sorted(variantsVCF.keys())
##    for apos in variantPos:
##        info = variantsVCF[apos]
##        if ('GMAF' in info) and (float(info['GMAF'][0]) >=0.01):
##            commonVariantsVCF[apos] = info
##
##
##        elif 'G5A' in info:
##            commonVariantsVCF[apos] = info

##    print '# of all variants in dbSNP file = ', len(fh)
    print '# of variants saved in the pickle : ', len(variantsVCF.keys())
    fhPickledbSNP = open(outfileName, 'w')
    pickle.dump(variantsVCF, fhPickledbSNP)
    fhPickledbSNP.close()



def processVCF(line, variantDict, build, maf):
    flds = line.split('\t')
    key = flds[0].strip() + '#' + flds[1].strip()
    value = {}
    value['REF'] = flds[3].strip()
    value['ALT'] = flds[4].strip().split(',')
    tags = Set(['G5A', 'G5'])
    for each in flds[7].strip().split(';'):
        info = each.partition('=')
        infoVal = info[2].split(',')
        if info[0] in tags:
            value[info[0]] = 1
        elif info[0] =='GMAF':
            value[info[0]] = infoVal
        elif info[0] == 'dbSNPBuildID':
            value[info[0]] = infoVal
##

    if ('GMAF' in value) and (float(value['GMAF'][0]) >=maf) and ('dbSNPBuildID' in value) and (int(value['dbSNPBuildID'][0]) <= build) :
        variantDict[key] = value
##
##    elif 'G5A' in value:
##    variantDict[key] = value

    del value # making sure that if the value isn't stored inside variantDict, it is removed from memory. The dbSNP file is very big and we want to
        # try to minimize the memory footprint for our objects/variables



def read_clin_sign_snps(fileName):
    fh = open(fileName, 'rU')

    variantsVCF = {}
##    commonVariantsVCF = {}

    for line in fh:
        if line[0] != '#':

            processVCFClin(line, variantsVCF)

        else:
            pass
    fh.close()

##    print '# of variants with global minor allele freq >=0.01 or if they are G5A : ', len(variantsVCF.keys())
    fhPickledbSNP = open('dbSNP_common_clinical.pkl', 'w')
    pickle.dump(variantsVCF, fhPickledbSNP)
    fhPickledbSNP.close()



def processVCFClin(line, variantDict):
    flds = line.split('\t')
    key = flds[0].strip() + '#' + flds[1].strip()
    value = {}
    value['REF'] = flds[3].strip()
    value['ALT'] = flds[4].strip().split(',')
    tags = Set(['G5A', 'G5', 'PM', 'TPA', 'PMC', 'NSF', 'NSM', 'NSN', 'ASS', 'DSS', 'U3', 'U5', 'INT', 'R3', 'R5' ])

    fields = Set(['GMAF', 'CLNSIG', 'CLNDBN', 'GENEINFO'])

    for each in flds[7].strip().split(';'):
        info = each.partition('=')

        if info[0] in tags:
            value[info[0]] = 1
        elif info[0] in fields:
            value[info[0]] = info[2]



    variantDict[key] = value


    del value # making sure that if the value isn't stored inside variantDict, it is removed from memory. The dbSNP file is very big and we want to
        # try to minimize the memory footprint for our objects/variables






def main():

    read_dbSNP('common_all.vcf', 'dbSNP_common_build129_maf5.pkl', 129, 0.05)
##    read_clin_sign_snps('common_and_clinical_20130226.vcf')

if __name__ == '__main__':
    main()
