#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     25/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

from subprocess import Popen, PIPE, STDOUT
import sys, pickle

def VarScan(index):

##    files = [   ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
##                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
##                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],
##                ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
##                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
##                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
##                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
##                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
##                [ 'PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']  ]
    files = ['2221', '2359', '2556', '3466']
    samples = ['Tumor', 'Normal']


    jobFiles = []

    for eachPatient in files:

        for eachSample in samples:

            outfileName = eachPatient + '_' + eachSample + '_VarScan.vcf'

##        end = eachPatient[index].find('_brain')   ####----------------==============----------===========-------------=============
##        pt_name = eachPatient[index][:end]
##        outfileName = eachPatient[index][:end] + '_brain_VarScan.vcf'
            eachFile = eachPatient + '_' + eachSample

            mpileupFile = eachPatient + '_' + eachSample + '_mpileup.txt'
            VarScanCmd = 'java -jar  ./VarScan.v2.3.2.jar mpileup2snp ' + mpileupFile + '  --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  ' + outfileName

            jobFiles.append(writeJobFile(eachFile, VarScanCmd))
            print VarScanCmd
##        job1 = Popen(VarScanCmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

##        job1.wait()

    for each in jobFiles:
        shellJob = 'qsub ' + each
        print shellJob
        job = Popen(shellJob,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

def writeJobFile(PT_name, jobcmd):



    fhoutName = PT_name + '_VarScan.sh'
    fhout = open(fhoutName, 'w')

    options1 = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=1,walltime=12:00:00,vmem=20gb \n" + "#PBS -N   "+fhoutName[:-3] + '\n' + "#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Tumor_Normal/  \n" + '#PBS -m abe '+'\n'  ##---///---///---

    fhout.write(options1)
    fhout.write(jobcmd)
    fhout.write('\n')
    fhout.write('sleep 10')
    fhout.write('\n')
    fhout.close()

    return fhoutName
def main():
    VarScan(1)

if __name__ == '__main__':
    main()
