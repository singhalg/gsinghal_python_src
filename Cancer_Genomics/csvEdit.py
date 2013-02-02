#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     06/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

def csvEdit(fileName):
    fhin = open(fileName, 'rU')
    data = fhin.readlines()
    fhin.close()

    outFileName = fileName[:-4] + '_SF_RS10.csv'
    fhout = open(outFileName, 'w')
    headings = data[0].split(',')
    outline = headings[0] + '#' +headings[1] +',' + ','.join(headings[2:-1]) + ',' + headings[-1].strip() + ',' + 'AVG DEPTH' + '\n'
    fhout.write(outline)
    for line in data[1:]:
        flds = line.split(',')
        chrPos = flds[0] + '#' + flds[1]
        prim_read_support = int(int(flds[2]) * float(flds[5]))
        met_read_support = int(int(flds[3]) * float(flds[6]))
        if (prim_read_support>=10 ) or (met_read_support>=10):
            outline = chrPos + ',' + ','.join(flds[2:-1]) + ',' + flds[-1].strip() + ',' + str( (int(flds[2])+ int(flds[3]))/2 )+ '\n'
            fhout.write(outline)

    fhout.close()



def main():
    csvEdit("PT_13_variants_rm_common_cutoff.csv")

if __name__ == '__main__':
    main()
