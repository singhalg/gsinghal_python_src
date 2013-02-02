#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     17/12/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys, os
from subprocess import Popen, PIPE, STDOUT

def BLAT(variant_fileName):

    '''

use faFrag to generate a fa file

use blat to run alignment

read alignment file, report top hits



    '''

    data = open(variant_fileName, 'rU').readlines()
    outFileName = variant_fileName[:-4] + '_blat.csv'
    output = open(outFileName, 'w')
    output.write(data[0])

    for line in data[1:]:
        flds = line.split(',')
        chrm = flds[0].strip()
        pos = flds[1].strip()
        outFaFile = chrm + '_' + pos + '.fa'
        faFragCmd =  'faFrag ' + 'chr'+chrm + '.fa  ' + str(int(pos)-100) + '  ' +str(int(pos)+100) + '  ' + outFaFile

        runfaFrag = Popen(faFragCmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        print 'Running the faFrag '
        print faFragCmd

        runfaFrag.wait()

        outBlatFile = outFaFile[:-3] + '_blat.psl'
        blatCmd = 'blat  hg19.fa  ' + outFaFile + '  ' + outBlatFile
        runBlat = Popen(blatCmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        print 'Running BLAT'
        print blatCmd
        runBlat.wait()

        blatResults = open(outBlatFile, 'rU').readlines()
        scores = ''
        scoreList  = []

        for eachLine in blatResults[5:]:
            scoreList.append(int(eachLine.split('\t')[0].strip()))


##            scores+= eachLine.split('\t')[0].strip() + '#'

        sortedScores = sorted(scoreList, reverse=True)

        outline = line.strip() + ',' + analyzeScores(sortedScores) + '\n'
        output.write(outline)

    output.close()


def analyzeScores(scoreList):
    scores = ''
    topScore = scoreList[0]

    for each in scoreList:
        scores += str(each)+ '(' +str(int((each*100.0)/topScore)) + ')#'
    return scores




def main():
    inputFile = sys.argv[1]
    BLAT(inputFile)

if __name__ == '__main__':
    main()
