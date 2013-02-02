#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     07/01/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys

def fastqTransfer():
    data = open('prim_met_fastq_files_all', 'rU').readlines()
    outFile = 'prim_met_fastq_scp.sh'
    fhout = open(outFile, 'w')
    for line in data:
        flds = line.split()
        fastqFile = flds[-1]
        end = fastqFile.find('run')
        if end >0 :
            e = end
        else:
            end = fastqFile.find('s_')
            e = end
        outline = 'scp ' + fastqFile + ' gsinghal@login2.chpc.wustl.edu:/BlueArc-scratch/gsinghal/MWatson/' + fastqFile[:e] + '\n'
        fhout.write(outline)
    fhout.close()




def main():
    fastqTransfer()


if __name__ == '__main__':
    main()
