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




def snpEffSnpSift(index):
##    index = int(index)

    files = [   ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
                ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],

                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                ['PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']]

    for eachPatient in files:

        end = eachPatient[index].find('_brain')   ####----------------==============----------===========-------------=============
        fileName = eachPatient[index][:end] + '_brain_VarScan_clean.vcf'

##        fileName = eachPatient[index][:-4] + '_snpEff.vcf'
        outFileName = fileName[:-4] + '_snpEff.vcf'
        summaryFile = outFileName[:-4] + '_summary.html'

        snpEffCmd = 'java -jar ./snpEff.jar -s ' + summaryFile + '  hg19  ' + fileName + ' > ' + outFileName
##        cmd = 'java -jar SnpSift.jar dbnsfp -v dbNSFP2.0b3.txt ../' + fileName    + ' > '     + outFileName
        print snpEffCmd
        job1 = Popen(snpEffCmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
##        print snpEffCmd
        job1.wait()


##        print snpEffCmd

        snpSiftOutput = outFileName[:-4] + '_SnpSift.vcf'

        SIFTcmd = 'java -jar ./SnpSift_latest.jar dbnsfp -v ./dbNSFP2.0b3.txt  ' + outFileName    + '  >  '     + snpSiftOutput
        print SIFTcmd
        job2 = Popen(SIFTcmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)


def snpEffSnpSiftdbSNP(index):
##    index = int(index)

    files = [   ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
                ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],

                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                ['PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']]

    for eachPatient in files:

        end = eachPatient[index].find('_brain')   ####----------------==============----------===========-------------=============
        fileName = eachPatient[index][:end] + '_brain_snpInExon.vcf'

##        fileName = eachPatient[index][:-4] + '_snpEff.vcf'
        outFileName = fileName[:-4] + '_dbSNP.vcf'
##        summaryFile = outFileName[:-4] + '_summary.html'

        dbSNPCmd = 'java -jar ./SnpSift_latest.jar annotate  common_all.vcf  ' + fileName + '  >  ' + outFileName
##        cmd = 'java -jar SnpSift.jar dbnsfp -v dbNSFP2.0b3.txt ../' + fileName    + ' > '     + outFileName

        print dbSNPCmd
        job1 = Popen(dbSNPCmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        job1.wait()

        fileName = outFileName
        outFileName = outFileName[:-4] + '_snpEff.vcf'

        summaryFile = outFileName[:-4] + '_summary.html'
##
        snpEffCmd = 'java -jar ./snpEff.jar -s ' + summaryFile + '  hg19  ' + fileName + ' > ' + outFileName
####        cmd = 'java -jar SnpSift.jar dbnsfp -v dbNSFP2.0b3.txt ../' + fileName    + ' > '     + outFileName
##
        print snpEffCmd
        job2 = Popen(snpEffCmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        job2.wait()
##


        snpSiftOutput = outFileName[:-4] + '_SnpSift.vcf'

        SIFTcmd = 'java -jar ./SnpSift_latest.jar dbnsfp -v ./dbNSFP2.0b3.txt  ' + outFileName    + '  >  '     + snpSiftOutput
        print SIFTcmd
        job3 = Popen(SIFTcmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)


def snpEffSnpSift2(index):
##    index = int(index)

    files = [   ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
                ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],

                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                ['PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']]

    for eachPatient in files:

        end = eachPatient[index].find('_brain')   ####----------------==============----------===========-------------=============
        fileName = eachPatient[index][:end] + '_brain_VarScan_clean.vcf'

##        fileName = eachPatient[index][:-4] + '_snpEff.vcf'
        outFileName = fileName[:-4] + '_snpEff.vcf'
        summaryFile = outFileName[:-4] + '_summary.html'

        snpEffCmd = 'java -jar ./snpEff.jar -s ' + summaryFile + '  hg19  ' + fileName + ' > ' + outFileName
##        cmd = 'java -jar SnpSift.jar dbnsfp -v dbNSFP2.0b3.txt ../' + fileName    + ' > '     + outFileName
##        print snpEffCmd
##        job1 = Popen(snpEffCmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
####        print snpEffCmd
##        job1.wait()


##        print snpEffCmd

        snpSiftOutput = outFileName[:-4] + '_SnpSift.vcf'

        SIFTcmd = 'java -jar ./SnpSift_latest.jar dbnsfp -v ./dbNSFP2.0b3.txt  ' + outFileName    + '  >  '     + snpSiftOutput
        print SIFTcmd
        job2 = Popen(SIFTcmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)


def main():

    snpEffSnpSift2(1)


if __name__ == '__main__':
    main()
