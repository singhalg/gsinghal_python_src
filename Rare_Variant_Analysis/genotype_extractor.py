#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     02/05/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

from sets import Set
import pickle, pandas
import copy


"""
This script converts a composite vcf file into individual vcf files.

first get a dict of sample id and column index


make a dict, with sample_id as the key and vcf line as the data.
if a variant has ./., then ignore the variant

"""


def genotype_extractor():
    samples = open('control_samples.csv', 'rU').readlines()

    sample_ids = Set([])

    for each in samples[1:]:
        sample_ids.add(each.strip().split(',')[0])

    print sample_ids



    composite_vcf = open('niehs.95samples.polymorphic.filtered.snps.vcf', 'rU').readlines()

##    sample_variant_dict = {}

    sample_location_dict = {}



    for eachLine in composite_vcf[:100]:
        if eachLine[:6] =='#CHROM':
            flds = eachLine.strip().split('\t')
            for eachSample in sample_ids:
                sample_location_dict[eachSample] = flds.index(eachSample)



    print sample_location_dict

    sample_variant_dict = copy.deepcopy(sample_location_dict)

    for each in sample_variant_dict.keys():
        sample_variant_dict[each] = []

    header = []

    for eachLine in composite_vcf:
        if eachLine[0] != '#':
            vcfLine_flds = eachLine.strip().split('\t')
            for each in sample_variant_dict.keys():

                if vcfLine_flds[sample_location_dict[each]] == "./.":
                    pass
                else:
                    vcf_flds = vcfLine_flds[:9] + [vcfLine_flds[sample_location_dict[each]]]
                    vcf_lines = sample_variant_dict[each]
                    vcf_lines.append(list2string(vcf_flds))
                    sample_variant_dict[each] = vcf_lines
        else:
            header.append(eachLine)


    for eachSample in sample_variant_dict.keys():
        fhout_file = eachSample+'_source.vcf'
        fhout = open(fhout_file, 'w')
        fhout.writelines(header[:-1])
        headerLine = '#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT' + '\t' + eachSample + '\n'
        fhout.write(headerLine)
        vcf_lines = sample_variant_dict[eachSample]
        for eachLine in vcf_lines:
            fhout.write(eachLine)
        fhout.close()




##    for each in sample_variant_dict.keys():
##        sample_variant_dict[each] = []






def vcf_line_splitter(sample_location_dict, vcfLine_flds, sample_variant_dict):

    for each in sample_variant_dict.keys():

        if vcfLine_flds[sample_location_dict[each]] == "./.":
            pass
        else:
            vcf_flds = vcfLine_flds[:8] + [vcfLine_flds[sample_location_dict[each]]]
            vcf_lines = sample_variant_dict[each]
            vcf_lines.append(list2string(vcf_flds))
            sample_variant_dict[each] = vcf_lines


def list2string(list_fields):
    astring = ''
    for each in list_fields:
        astring+=each+'\t'

    astring+='\n'

    return astring


def main():
    genotype_extractor()

if __name__ == '__main__':
    main()
