#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     02/04/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import datetime
import sys
from sets import Set

import re, os
##import psutil as PS
from subprocess import Popen, PIPE, STDOUT


def runMpileup(bamFiles_csv, start, end):
    hg19 = '/BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa'
    targetBed = 'S0347602_BED_20110607_expanded.bed'
    fileList = open(bamFiles_csv, 'rU').readlines()
    commandList = []
    for i in range (int(start), int(end)):
        line = fileList[i]
        bamFile = line.split(',')[0].strip()



        mpileupFile = bamFile[:-4]+'_mpileup.txt'
    ##    vcfFile = bamFile[:-4]+'.vcf'

        samtools = 'samtools mpileup -f ' + hg19 + '  -l '+ targetBed + '  ' + bamFile + ' > ' + mpileupFile + '\n'

        commandList.append(samtools)

        runMpileup = Popen(samtools, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        print 'Running the mpileup for file ', bamFile
        print samtools
    ##    procID = runMpileup.pid
    ##    mpileup = PS.Process(int(procID))
    ##    mpileup.wait()
##        runMpileup.wait()
##
##    return commandList
##def writeJobScript(bamFile_csv):
##    commandList = runMpileup(bamFile_csv)
##
##    fhout = open('mpileupJob', 'w')
##
##    options1 = "#!/bin/bash" + '\n'+ '#PBS -l nodes=1:ppn=32,walltime=12:00:00,mem=10gb ' + '\n' + "#PBS -N runMpileup "+ '\n' + "#PBS -d /BlueArc-scratch/gsinghal/MWatson/SJ_renal" +'\n' + '#PBS -m abe '+'\n' +'#PBS -q dque_smp ' +'\n'
##    fhout.write(options1)
##    fhout.writelines(commandList)



def main():
    bamFile_csv = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]
    runMpileup(bamFile_csv, start, end)

if __name__ == '__main__':
    main()
