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




def SnpSift(index):
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
        fileName = eachPatient[index][:-4] + '_snpEff.vcf'
        outFileName = fileName[:-4] + '_SnpSift.vcf'
        cmd = 'java -jar SnpSift.jar dbnsfp -v dbNSFP2.0b3.txt ../' + fileName    + ' > '     + outFileName
        job = Popen(cmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        print cmd


def main():

    SnpSift(1)


if __name__ == '__main__':
    main()
