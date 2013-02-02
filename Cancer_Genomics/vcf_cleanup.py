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

import sys, os


'''
This method cleans up the vcf files. It takes in a vcf file and writes another vcf file with all the variants with non-legal ALT alleles removed. So, in the new vcf file,
the ALT alleles other than ATCGNatcgn will be removed.

'''
def clean_up(fileName):
    outFileName = fileName[:-4] + '_legal.vcf'
    fhin = open(fileName, 'rU')
    data = fhin.readlines()
    fhin.close()
    fhout = open(outFileName, 'w')
    for line in data[:5]:
        fhout.write(line)

    legal_alleles = Set(['A', 'T', 'C', 'G'])

    for line in data[5:]:
        valid_alleles = ''
        valid_alleles_vaf = ''
        flds = line.split('\t')
        alt = flds[4].strip().split(',')
        alt_vaf = flds[7].strip().split(';')[1][3:].split(',')
        for i in range(len(alt)):
            if alt[i] in legal_alleles:
                valid_alleles += alt[i]+','
                valid_alleles_vaf += alt_vaf[i] + ','

        if len(valid_alleles) > 0:
            outline  = flds[0] + '\t' + flds[1] + '\t' + flds[2] + '\t' + flds[3] + '\t' + valid_alleles[:-1] + '\t' + flds[5] + '\t' + flds[6] + '\t' +  flds[7].strip().split(';')[0]+';AF=' + valid_alleles_vaf[:-1] + '\n'
            fhout.write(outline)
    fhout.close()


def addAF(fileName):
    outFileName = fileName[:-4] + '_legal.vcf'
    fhin = open(fileName, 'rU')
    data = fhin.readlines()
    fhin.close()
    fhout = open(outFileName, 'w')
    for line in data[:5]:
        fhout.write(line)

    legal_alleles = Set(['A', 'T', 'C', 'G'])

    for line in data[5:]:
        valid_alleles = ''
        valid_alleles_vaf = ''
        flds = line.split('\t')
        alt = flds[4].strip().split(',')
        alt_vaf = flds[7].strip().split(';')[1][3:].split(',')
        for i in range(len(alt)):
            if alt[i] in legal_alleles:
                valid_alleles += alt[i]+','
                valid_alleles_vaf += alt_vaf[i] + ','

        if len(valid_alleles) > 0:
            outline  = flds[0] + '\t' + flds[1] + '\t' + flds[2] + '\t' + flds[3] + '\t' + valid_alleles[:-1] + '\t' + flds[5] + '\t' + flds[6] + '\t' +  flds[7].strip().split(';')[0]+';AF=' + valid_alleles_vaf[:-1] + '\n'
            fhout.write(outline)
    fhout.close()



'''
PT_10_brain_1200360_snpEff.vcf  PT_11_brain_1200385.vcf  PT_12_lung_1200381.vcf   PT_1_brain_1123232.vcf  PT_3_lung_1123221.vcf   PT_9_brain_1200383.vcf
PT_10_brain_1200360.vcf         PT_11_lung_1200363.vcf   PT_13_brain_1200370.vcf  PT_1_lung_1123233.vcf   PT_6_brain_1123226.vcf  PT_9_lung_1200382.vcf
PT_10_lung_1200384.vcf          PT_12_brain_1200368.vcf  PT_13_lung_1202946.vcf   PT_3_brain_1123220.vcf  PT_6_lung_1123227.vcf   snpInExon_snpEff.vcf



'''

def vcfCleanUpAll():

    files = [ 'PT_10_brain_1200360.vcf','PT_11_brain_1200385.vcf',  'PT_12_lung_1200381.vcf',   'PT_1_brain_1123232.vcf',  'PT_3_lung_1123221.vcf',   'PT_9_brain_1200383.vcf',
            'PT_11_lung_1200363.vcf',   'PT_13_brain_1200370.vcf',  'PT_1_lung_1123233.vcf',   'PT_6_brain_1123226.vcf',  'PT_9_lung_1200382.vcf',
            'PT_10_lung_1200384.vcf',          'PT_12_brain_1200368.vcf',  'PT_13_lung_1202946.vcf',   'PT_3_brain_1123220.vcf',  'PT_6_lung_1123227.vcf',
            'PT_2_brain_1123230.vcf', 'PT_2_lung_1123231.vcf']
    for eachFile in files:

        clean_up(eachFile)
        command = 'java -jar snpEff.jar -s ' + eachFile[:-4] + '.html  hg19  ' + eachFile[:-4] + '_legal.vcf >  ' + eachFile[:-4]+'_snpEff.vcf  '
        print command
        os.system(command)

def main():
    vcfCleanUpAll()

if __name__ == '__main__':
    main()
