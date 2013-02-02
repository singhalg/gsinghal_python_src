#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     12/11/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys

def filterUsingAF(fileName):
    data = open(fileName, 'rU').readlines()
    outFileName  = fileName[:-4] + '_AF_filt.csv'
    fhout = open(outFileName,'w')

    fhout.write(data[0])

    for line in data[1:]:
        if countAF(line.split(',')):
            fhout.write(line)

    fhout.close()





def countAF(flds):
    index = [22,27,32,37] #---///---///---///----///---
    totalAF = 0
    pt_count=0
    for each in index:
##        print flds[each] #
        if len(flds[each])>0:
            totalAF+=float(flds[each])
            pt_count+=1.0
    if pt_count>0 and ((totalAF/pt_count) <=0.5):
        return True


def main():
    fileName = sys.argv[1]
    filterUsingAF(fileName)

if __name__ == '__main__':
    main()
