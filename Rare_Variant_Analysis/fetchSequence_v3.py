'''
Created on Feb 16, 2011

@author: Gaurav
'''


#-------------------------------------------------------------------#
# Author: Gaurav Singhal                                            #
# Created : Feb 15, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#


import sys
import pickle

'''''
This script was originally written for fetching L1 sequences from hg18, but it has been modified (on March 06)
to fetch LTR sequences.

Script modified on Nov 27, 2012 for fetching sequence from hg19
'''''



def getCustomRefSequence(coordinates_bed):

    '''

use faFrag to generate a fa file


    '''

    data = open(variant_fileName, 'rU').readlines()
##    outFileName = variant_fileName[:-4] + '_blat.csv'
##    output = open(outFileName, 'w')
##    output.write(data[0])

    for line in data:
        flds = line.split('\t')
        chrm = flds[0].strip()
        pos_start = flds[1].strip()
        pos_end = flds[2].strip()

        outFaFile = chrm + '_' + pos + '.fa'
        faFragCmd =  'faFrag ' + 'chr'+chrm + '.fa  ' + str(int(pos)-100) + '  ' +str(int(pos)+100) + '  ' + outFaFile

        runfaFrag = Popen(faFragCmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        print 'Running the faFrag '
        print faFragCmd

        runfaFrag.wait()




"""
This method reads the chr1.fa to chrY.fa (all fasta files of the hg19 genome build and returns a dictionary of the genome

"""


def readGenome():


    hg19 = {}

    chrFa = []
    for i in range (1, 23):
        chrm = 'chr' + str(i)+ '.fa'
        chrFa.append(chrm)

    chrFa.append('chrX.fa')
    chrFa.append('chrY.fa')


    for each in chrFa:
        chrSeq = open(each, 'rU')
        chrSeq.readline()
        sequence = ''
        for line in chrSeq:
            sline = line.strip()
            sequence+=sline
        key = each[:-3]
        hg19[key] = sequence
    return hg19




"""
This method first calls the readGenome method to develop a dictionary of the whole genome. Then it reads a bed file, and fetches a fasta sequence for each bed
region in the bed file. It accumulates all these fasta sequences and writes them only a fasta composite file.
"""
def fetchSeq(bedFile, left_flank, right_flank):

    hg19 = readGenome()

    variantData = open(bedFile, 'rU').readlines()

    outfileName = bedFile[:-4]+'_all_sequences.fa'

    fhout = open(outfileName, 'w')
##    fhout.write(variantData[0])
    for each in variantData:


        flds = each.split('\t')
        key = flds[0]
        start = int(flds[1]) - int(left_flank)
        end = int(flds[2])+ int(right_flank)

        target_region = key + ':' + str(start) + '-' + str(end)
        chrSeq = hg19[key]
        dnaSeq = chrSeq[start:end]

        fastaHeader = '>'+target_region+'\n'
        fastaSeq = fastacize(dnaSeq)

        outline = fastaHeader + fastaSeq + '\n'
        fhout.write(outline)

    fhout.close()









def complement(s):
    """Return the complementary sequence string."""
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N':'N', 'a':'t', 'c':'g', 'g':'c', 't':'a', 'n':'n', '\n':'\n'}
    letters = list(s)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)


def reverse(s):
    revSeq = ''

    base = len(s) -1
    while base>=0:
        revSeq += s[base]
        base-=1

    return revSeq


def reversecomplement(s):
    """Return the reverse complement of the dna string."""
    s = reverse(s)
    s = complement(s)
    return s

def fastacize(string):

    size = len(string)
    s = 0
    e = s+50
    fasta = ''
    while e < size:
        fasta += string[s:e] + '\n'
        s+= 50
        e= s+50
    fasta+= string[s:size]+'\n'
    return fasta

def organize(string):
    list = string.split()
    slist = [each.strip('()') for each in list]
    return slist


def main():
    bedFile = sys.argv[1]
    left = sys.argv[2]
    right = sys.argv[3]

    fetchSeq(bedFile, left, right)


if __name__ == '__main__':
    main()









