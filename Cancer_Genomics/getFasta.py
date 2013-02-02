#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     29/01/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------
import sys, pickle
from sets import Set
from subprocess import Popen, PIPE, STDOUT

'''
Given a csv file having genomic coordinates in the form chr1:123443+123543 , this script will generate fasta file for each respective location (+100 bases upstream and downstream).
So, for chr1:123443+123543, the coordinates of the fasta file will be chr1:123343+123643.
'''


def getCoordinates(coordinates_fileName):


    data = open(coordinates_fileName, 'rU').readlines()
    genes = Set()

    for each in data:
        line = each.split(',')[0]
        chrom = line.split(':')[0]

        start = line.partition(':')[2].split('+')[0]
        end = line.partition(':')[2].split('+')[1].strip()
        gene = each.split(',')[1].strip()
        if gene not in genes:

            genes.add(gene)
        else:
            print gene, '!!!!!!!!!!!!'
        print chrom, '  ',start, '  ',end, '  ',gene, ' length =   ',(int(end) - int(start))

##    print len(genes)

##
##
##        outFaFile = gene + '_frag.fa'
##        faFragCmd =  'faFrag ' + chrom + '.fa  ' + str(int(start)-100) + '  ' +str(int(end)+100) + '  ' + outFaFile
##
##        runfaFrag = Popen(faFragCmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
##        print 'Running the faFrag '
##        print faFragCmd
##
##        runfaFrag.wait()


def main():
    getCoordinates('amplicon_coordinates.csv')

if __name__ == '__main__':
    main()
