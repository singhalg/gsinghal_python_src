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

def VarScan(ind, tissue, current_dir):

    index = int(ind)

    files = [   ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],
                ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                [ 'PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']  ]


    jobFiles = []

    for eachPatient in files:

        end = eachPatient[index].find(tissue)   ####----------------==============----------===========-------------=============
        pt_name = eachPatient[index][:end]
        outfileName = eachPatient[index][:end] + tissue + '_VarScan.vcf'

        mpileupFile = pt_name + tissue+  '_mpileup.txt'
        VarScanCmd = 'java -jar  ./VarScan.v2.3.2.jar mpileup2snp ' + mpileupFile + '  --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  ' + outfileName

        jobFiles.append(writeJobFile(pt_name, VarScanCmd, current_dir, tissue))
        print VarScanCmd
##        job1 = Popen(VarScanCmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

##        job1.wait()

    for each in jobFiles:
        shellJob = 'qsub ' + each
        print shellJob
        job = Popen(shellJob,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

def writeJobFile(PT_name, jobcmd, current_dir, tissue):



    fhoutName = PT_name + tissue+ '_varScan.sh'
    fhout = open(fhoutName, 'w')

    options1 = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=1,walltime=12:00:00,vmem=20gb \n" + "#PBS -N   "+fhoutName[:-3] + '\n' + "#PBS -d  "+current_dir+ '  \n' + '#PBS -m abe '+'\n'

    fhout.write(options1)
    fhout.write(jobcmd)
    fhout.write('\n')
    fhout.write('sleep 10')
    fhout.write('\n')
    fhout.close()

    return fhoutName
def main():

    ind = sys.argv[1]
    tissue = sys.argv[2]
    current_dir = sys.argv[3]
    VarScan(ind, tissue, current_dir)

if __name__ == '__main__':
    main()
