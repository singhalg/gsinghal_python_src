#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     12/12/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------
import sys, pickle
from sets import Set


def tumor_normal_comparison(tumor_sample, normal_sample):

    tumor = pickle.load(open(tumor_sample, 'rU'))
    normal = pickle.load(open(normal_sample, 'rU'))

    tumor_pos = Set(tumor.keys())

    normal_pos = Set(normal.keys())

    somatic = tumor_pos - normal_pos
    common = tumor_pos & normal_pos

    outFile_somatic = tumor_sample[:-4] +'_'+ normal_sample[:-4] + '_somatic.csv'
    outFile_common =tumor_sample[:-4] + '_' + normal_sample[:-4] + '_common.csv'

    output_somatic = open(outFile_somatic, 'w')
    output_common = open(outFile_common, 'w')

    header_somatic = 'Chrom,Pos,REF,ALT,AF,DP,PVAL' + '\n'
    output_somatic.write(header_somatic)

    header_common = 'Chrom,Pos,REF,ALT,AF_tumor,AF_normal,DP_tumor,DP_normal,PVAL_tumor,PVAL_normal' + '\n'
    output_common.write(header_common)

    for each in somatic:
        pos = each.split('#')

        outline = pos[0] + ',' + pos[1] + ',' + tumor[each]['REF'] + ',' + tumor[each]['ALT'][0] + ',' + tumor[each]['AF'][0] + ',' + tumor[each]['DP'][0] + ',' + tumor[each]['PVAL'][0]+ '\n'
        output_somatic.write(outline)

    for each in common:
        pos = each.split('#')

        outline = pos[0] + ',' + pos[1] + ',' + tumor[each]['REF'] + ',' + tumor[each]['ALT'][0] + ',' + tumor[each]['AF'][0] + ',' + normal[each]['AF'][0]+ ',' + tumor[each]['DP'][0] + ',' + normal[each]['DP'][0]+ ',' + tumor[each]['PVAL'][0]+ ',' + normal[each]['PVAL'][0]+ '\n'
        output_common.write(outline)


    output_somatic.close()
    output_common.close()






def main():
    tumor_sample = sys.argv[1]

    normal_sample = sys.argv[2]

    tumor_normal_comparison(tumor_sample, normal_sample)
if __name__ == '__main__':
    main()
