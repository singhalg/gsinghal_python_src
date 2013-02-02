#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     21/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys


def vcfToBed(filename):

    txtFile = open(filename, 'rU')
    txtFile.readline()
    txtFile.readline()
    txtFile.readline()
    txtFile.readline()
    txtFile.readline()



    if filename[-4:] == '.txt':
        bedFile = filename[:-4]+'.bed'
    else:
        bedFile = filename + '.bed'

    bed = open(bedFile, 'w')


    for line in txtFile:
        bed.write(organize(line))
    txtFile.close()
    bed.close()



def organize(string):
    flds = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list

    feature = 'chr' + flds[0].strip() + '\t' + str(int(flds[1].strip())-1) + '\t' + flds[1].strip() + '\t' + 'REF=' + flds[2].strip() + ';ALT=' +flds[3].strip() + ';' + flds[4].strip() + '\n'



    return feature

def main():

    txtFile = sys.argv[1]

    vcfToBed(txtFile)


if __name__=='__main__':
    main()



