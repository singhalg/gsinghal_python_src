#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     19/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------
import sys

def csvToBed(fileName):
    fhin = open(fileName, 'rU')
    data = fhin.readlines()
    fhin.close()

    outfilename = fileName[:-4] + '.bed'
    fhout = open(outfilename, 'w')
    for line in data[1:]:
        flds = line.split(',')
        if len(flds[0])>0:
            fhout.write(processBed(line))
    fhout.close()

def processBed(aline):
    outline =  ''
    flds = aline.split(',')
    outline = 'chr' + flds[0] + '\t' + str(int(flds[1])-1) + '\t' + flds[1] + '\t' + flds[19] + '##PTS_' + flds[20] + '\n'
    return outline


def main():
    csvToBed('mutation_recurrence_results_primary_GTAC.csv')

# fixed_in_met
if __name__ == '__main__':
    main()
