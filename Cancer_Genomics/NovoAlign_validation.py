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
import sys, re, pickle
from sets import Set


def getSampleNames():
    sample_names = Set()
    outfile = open('listOfFiles', 'w')

    switch = False
    data = open('validation_fastq_files.csv', 'rU').readlines()
    for line in data:
        sample_names.add(line.strip()[:7])

        if switch:


            outline+= line.strip() + '\n'
            outfile.write(outline)
            switch = False

        else:
            outline = line.strip() + '  '
            switch = True


    print len(sample_names)
    print sample_names
    outfile.close()

def verify_listOfFiles():
    data = open('listOfFiles', 'rU').readlines()
    for line in data:
        flds = line.strip().split()
        ff = flds[0].find('_R1')
        rf = flds[1].find('_R2')
        if  (flds[0][:ff] == flds[1][:rf]) and (ff>0) and (rf>0):
            print 'ok'
        else:
            print line

def main():
##    getSampleNames()
    verify_listOfFiles()

if __name__ == '__main__':
    main()
