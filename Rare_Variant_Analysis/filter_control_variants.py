#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     03/05/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

"""
1       985826  rs17160775      G       A       4529.22 PASS
HaplotypeScore=0.3199;MQ=54.17;MQ0=0;MQRankSum=94.863;QD=18.04;ReadPosRankSum=4.079;SB=-772.77  GT:AD:DP:GQ:PL  0/0:25,0:25:72.22:0,72,910


chr1    985266  .       C       T       249     PASS    DP=22   GT:GQ:DP        1/1:63:22
"""


from sets import Set
import pickle, pandas
import copy
from subprocess import Popen, PIPE, STDOUT

def filter_vcf():
    samples = open('control_samples.csv', 'rU').readlines()

    sample_ids = Set([])

    for each in samples[1:]:
        sample_ids.add(each.strip().split(',')[0])

    print sample_ids

    for eachSample in sample_ids:
        outFile = eachSample + '_source_filtered.vcf'

        jobcmd = 'bedtools intersect -a ' + eachSample + '_source.vcf -b  SJ_renal_1000Genes_miRNA_sorted_merged_nochr.bed  -wa >  ' + eachSample + '_source_filtered.vcf'
        print jobcmd
        job = Popen(jobcmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        job.wait()
        parse_filter_vcf(outFile)


def parse_filter_vcf(inFile):
    outFileName = inFile[:-4] + '_clean.vcf'

    InData = open(inFile, 'rU').readlines()

    fhout = open(outFileName, 'w')

    fhout.write('##fileformat=VCFv4.1')
    fhout.write('\n')
    fhout.write('##INFO=<ID=DP,Number=1,Type=Integer,Description="Read Depth (only filtered reads used for calling)">')
    fhout.write('\n')
    fhout.write('##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">')
    fhout.write('\n')
    fhout.write('##FORMAT=<ID=GQ,Number=1,Type=Float,Description="Genotype Quality">')
    fhout.write('\n')
    fhout.write('##FORMAT=<ID=AD,Number=.,Type=Integer,Description="Allelic depths for the ref and alt alleles in the order listed">')
    fhout.write('\n')
    fhout.write('#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  1796')
    fhout.write('\n')



    for line in InData:
        flds = line.strip().split('\t')
        format_data = flds[9].split(':')
        if format_data[0] != "0/0":
            outline = flds[0] + '\t' + flds[1] + '\t' +flds[2] + '\t' +flds[3] + '\t' +flds[4] + '\t' +flds[5] + '\t' + flds[6] + '\t' + 'DP='+format_data[2] + '\t' + 'GT:GQ:AD' + '\t' + format_data[0]+':'+format_data[3] + ':' + format_data[1] + '\n'
            fhout.write(outline)

    fhout.close()










def main():
    filter_vcf()

if __name__ == '__main__':
    main()
