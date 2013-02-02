#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     13/01/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys, os

"java -jar /export/picard-tools-1.67/MarkDuplicates.jar INPUT=PT_1_lung_sorted.bam OUTPUT=PT_1_lung_sorted_rmdup.bam METRICS_FILE=metrics_rmdup.txt REMOVE_DUPLICATES=true ASSUME_SORTED=true"


def runMarkDuplicates():
    files = [   ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],
                ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                [ 'PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']  ]

    for each in files:
        print each[1]
        end = each[1].find('_brain')
        folder_end = each[1].find('.vcf')
        inputfileName = each[1][:end] + '_brain_sorted.bam'
        outputfileName = inputfileName[:-4] + '_rmdup.bam'
        print inputfileName
        print outputfileName
        wd= "/BlueArc-scratch/gsinghal/MWatson/Alignments_2/MWatson/MWatson/" + each[1][:end] +  "/"+each[1][end+1:folder_end] + "/"
        jobcmd = "java -jar /export/picard-tools-1.67/MarkDuplicates.jar INPUT=" + inputfileName + " OUTPUT=" +outputfileName + " METRICS_FILE=metrics_rmdup.txt REMOVE_DUPLICATES=true ASSUME_SORTED=true "  '\n'

        fhoutName = inputfileName[:-4] + '_MarkDuplicates.sh'
        fhout = open(fhoutName, 'w')

        options1 = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=1,walltime=12:00:00,vmem=42gb \n" + "#PBS -N   "+fhoutName[:-3] + '\n' + "#PBS -d  " + wd + '\n' + '#PBS -m abe '+'\n'  ##---///---///---

        fhout.write(options1)
        fhout.write(jobcmd)
        fhout.write('\n')
        fhout.write('sleep 10')
        fhout.write('\n')
        fhout.close()

def main():
    runMarkDuplicates()

if __name__ == '__main__':
    main()
