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





def fetchSeq(left_flank, right_flank):


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



    variantData = open('unselected_variants.csv', 'rU').readlines()

    outfileName ='unselected_variants_' + left_flank + '_' + right_flank + '.csv'

    fhout = open(outfileName, 'w')
    fhout.write(variantData[0])
    for each in variantData[1:]:


        flds = each.split(',')
        key = 'chr'+ flds[0]
        start = int(flds[1]) - int(left_flank)
        end = int(flds[1])+ int(right_flank)

        target_region = key + ':' + str(start) + '-' + str(end)
        chrSeq = hg19[key]
        dnaSeq = chrSeq[start:end]
        outline = each.strip() +',' + target_region + ',' + dnaSeq + '\n'
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
    left = sys.argv[1]
    right = sys.argv[2]

    fetchSeq(left, right)


if __name__ == '__main__':
    main()









