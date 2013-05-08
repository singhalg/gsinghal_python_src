#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     13/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------


from subprocess import Popen, PIPE, STDOUT
import sys, pickle
##from mutationRecurrence_control import *
##
##from vcf2pickleV2_VarScan_alignment_2_control import *


def snpEffSnpSift():
##    index = int(index)
    fileList = open('control_samples.csv', 'rU').readlines()
    commandList = []
    for each in fileList[1:]:

        bamFile = each.split(',')[0].strip()



        vcfFile = bamFile+'_source_filtered_clean.vcf'
        legal_vcf = vcfFile


        outFileName = bamFile + '_snpEff.vcf'
        summaryFile = bamFile + '_summary.html'

        snpEffCmd = 'java -Xmx4g -jar ./snpEff.jar eff  -s ' + summaryFile + '  GRCh37.69 ' + legal_vcf + ' > ' + outFileName
##        cmd = 'java -jar SnpSift.jar dbnsfp -v dbNSFP2.0b3.txt ../' + fileName    + ' > '     + outFileName
        print snpEffCmd
        job1 = Popen(snpEffCmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
##        print snpEffCmd
        job1.wait()


##        print snpEffCmd

        snpSiftOutput = outFileName[:-4] + '_SnpSift.vcf'

        SIFTcmd = 'java -jar ./SnpSift.jar dbnsfp -v ./dbNSFP2.0b3.txt  ' + outFileName    + '  >  '     + snpSiftOutput
        print SIFTcmd
        job2 = Popen(SIFTcmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        job2.wait()


        gwasOutput = snpSiftOutput[:-4] + '_GWAS.vcf'

        GWAScmd = 'java -jar ./SnpSift.jar gwasCat ./gwascatalog.txt ' + snpSiftOutput    + '  >  '     + gwasOutput
        print GWAScmd
        job3 = Popen(GWAScmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        job3.wait()


def make_legal_vcf(illegal_vcf):
    data = open(illegal_vcf, 'rU').readlines()
    fhout_name = illegal_vcf[:-4] + '_legal.vcf'
    fhout = open(fhout_name, 'w')
    for line in data:
        if line[0] == '#':
            fhout.write(line)
        else:
            outline = 'chr' + line
            fhout.write(outline)

    fhout.close()
    return fhout_name


def main():

    snpEffSnpSift()
##    mutationRecurrence(2)
##    VCFtoPickle('dbSNP_allCommon.pkl')


if __name__ == '__main__':
    main()
