#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     01/09/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# Read the EVS vcf file, consider variants having read depth > 100 (?) and allele freq > 0.05
# throw out the variants which match the EVS variants from the patient data.

from sets import Set
import pickle
import sys

def simpleSurvey(fileName):
    fh = open(fileName, 'rU')
    data = fh.readlines()
    variantsVCF = {}
    varSet = Set([])

    for line in data:
        if line[0] != '#':

            processVCF(line, variantsVCF)

        else:
            pass

    count = 0
    '''
If a variant is present in 5 people out of 100 in heterozygous, and each person has read depth of 5, then you will have
25 reads supporting the alt allele and 975 alleles supporting the ref allele. Thus the MAF =25*100 / 1000, which equals to
2.5%. If the alt allele is present in more than 5 people out of 100, then the maf >= 3%  (30*100/1000)
However, if the read depth is highly biased, such such the alt allele has 100 reads in each of 5 samples (heterozygous)
and ref allele has depth of 10 each, then you have 250 reads supporting alt allele and 1200 reads (95*10 + 5*50) supporting ref allele.
So, maf will be 250*100/1450  = 17.24%. We will assume that such biases do not exist in the data.

So, we will set our threshold for
MAF>= 3
Average sample read depth = 10
# of samples >=100

Code this !

    '''
    variantPos = sorted(variantsVCF.keys())
    for apos in variantPos:
        info = variantsVCF[apos]
        maf = float(info['MAF'][2])
        dp = int(info['DP'][0])
        if dp >= 10: #---==------====----
            if maf >= 5.0:  # EVS describes maf as percentage

                varSet.add(apos)


    print '# of all variants in EVS file = ', len(variantPos)
    print '# of common variants = ', len(varSet)
    fhPickleCommonEVS = open('commonEVS_asrd10.pkl', 'w') #-=====-------------==========-----------
    pickle.dump(varSet, fhPickleCommonEVS)
    fhPickleCommonEVS.close()
    return varSet, variantPos


'''
This method takes a variant file in csv format and throws out those variants which are also present in EVS vcf file.
fileName = file of csv variant file
'''
def filterOutEVS(fileName):

    varSet, AllVariants = simpleSurvey('ESP6500.all_chr.snps.vcf')
    print '# of entries in EVS file = ', len(varSet)
    fhin = open(fileName, 'rU')
    data = fhin.readlines()
    fhin.close()
    patient_variants = Set([])
    outFile = fileName[:-4]+'EVS.csv'
    fhout = open(outFile, 'w')
    match = 0
    for line in data:
        flds = line.split(',')
        if len(flds[0]) < 7:
            key = flds[0][3:] + '#' + flds[1].strip()
            patient_variants.add(key)
            if key in varSet:
                match+=1
            else:
                fhout.write(line)
    print '# total entries in ', fileName , ' = ', len(data)
    print '# of entries which are also found in EVS file = ', match
    fhout.close()
    patient_variant_loc = list(patient_variants)
    print patient_variant_loc[:100]

##    for each in variantPos:
##        print each
##        print variantsVCF[each]
####    print variantsVCF
##    print '==========================================='
##    print varSet


def processVCF(line, variantDict):
    flds = line.split('\t')
    key = flds[0].strip() + '#' + flds[1].strip()
    value = {}
    value['REF'] = flds[3].strip()
    value['ALT'] = flds[4].strip()
    for each in flds[7].strip().split(';'):
        info = each.partition('=')
        infoVal = info[2].split(',')
        value[info[0]] = infoVal
    variantDict[key] = value

def main():
##    vcfFile = sys.argv[1]
##    simpleSurvey(vcfFile)
##
##    variantFile = sys.argv[1]
##    filterOutEVS(variantFile)
    simpleSurvey('ESP6500.all_chr.snps.vcf')

if __name__ == '__main__':
    main()
