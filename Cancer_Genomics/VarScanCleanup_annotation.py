#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     22/01/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys

from subprocess import Popen, PIPE, STDOUT
import pickle

def VarScan_cleanup_snpSift_annotation():

    files = [   ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],
                ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                [ 'PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']  ]
    switch = True

    for eachPatient in files:
        for eachFile in eachPatient:

            if switch:
                tissue = '_lung'
                switch = False
            else:
                tissue = '_brain'
                switch = True


            end = eachFile.find(tissue)   ####----------------==============----------===========-------------=============
            pt_name = eachFile[:end]
            fileName = pt_name + tissue + '_VarScan.vcf'
            newFile = varScan_vcf_cleanup(fileName)
            snpEffSnpSift2(newFile)



def varScan_vcf_cleanup(fileName):
    fh = open(fileName, 'rU')
    data = fh.readlines()
    fh.close()

    fhoutName = fileName[:-4] + '_clean.vcf'
    fhout = open(fhoutName, 'w')

    fhout.write(data[0])
    fhout.write(data[1])

    fhout.write('''##INFO=<ID=DP,Number=1,Type=Integer,Description="Quality Read Depth of bases with Phred score >= 15">  \n''')
    fhout.write('''##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency (Depth of variant-supporting bases (Phred score >=15) / Total depth (Phred score >=15))"> \n''')
    fhout.write('''##INFO=<ID=PVAL,Number=1,Type=String,Description="P-value from Fisher's Exact Test">  \n''')
    outline = '#CHROM' + '\t'+ 'POS' +  '\t' +  'ID' + '\t' + 'REF' + '\t' + 'ALT' +  '\t' +  'QUAL'+  '\t' +  'FILTER'+  '\t' +  'INFO' + '\n'
    fhout.write(outline)



    for line in data[24:]:
        flds = line.split('\t')
        chrom = flds[0][3:]
        infotags = flds[9].split(':')
        info = 'DP=' + infotags[3] + ';AF=' + infotags[6][:-1] + ';PVAL=' + infotags[7]
        outline = chrom + '\t' + flds[1] + '\t' + flds[2] + '\t' + flds[3] + '\t' + flds[4] + '\t' + flds[5] + '\t' + flds[6] + '\t' + info + '\n'
        fhout.write(outline)
    fhout.close()



    del data
    return fhoutName



def snpEffSnpSift2(fileName):


##        fileName = eachPatient[index][:-4] + '_snpEff.vcf'
    outFileName = fileName[:-4] + '_snpEff.vcf'
    summaryFile = outFileName[:-4] + '_summary.html'

    snpEffCmd = 'java -jar ./snpEff.jar -s ' + summaryFile + '  hg19  ' + fileName + ' > ' + outFileName
##        cmd = 'java -jar SnpSift.jar dbnsfp -v dbNSFP2.0b3.txt ../' + fileName    + ' > '     + outFileName
    print snpEffCmd
    job1 = Popen(snpEffCmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
####        print snpEffCmd
    job1.wait()


##        print snpEffCmd

    snpSiftOutput = outFileName[:-4] + '_SnpSift.vcf'

    SIFTcmd = 'java -jar ./SnpSift.jar dbnsfp -v ./dbNSFP2.0b3.txt  ' + outFileName    + '  >  '     + snpSiftOutput
    print SIFTcmd
    job2 = Popen(SIFTcmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    job2.wait()


def main():
    VarScan_cleanup_snpSift_annotation()

if __name__ == '__main__':
    main()
