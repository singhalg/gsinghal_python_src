#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     18/05/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def exomeReadCounter(sampleName):
    fh = open('YRIexome.csv', 'rU')
    data = fh.readlines()
    fh.close()
    readCount = 0
    seqCenter = ''
    for line in data[1:]:
        flds = line.split(',')
        if (flds[9].strip() == sampleName) and (flds[20].strip()== '0'):
            seqCenter = flds[5].strip()
            if flds[18].strip()=='PAIRED':
                readCount += (int(flds[23].strip()))
            else:
                readCount += int(flds[23].strip())

    print sampleName, 'has ',  readCount, '  reads. It came from ', seqCenter, '. ', '\n'




def main():
    exomeReadCounter('NA18519')
    exomeReadCounter('NA18519')
    exomeReadCounter('NA18868')
    exomeReadCounter('NA18917')
    exomeReadCounter('NA18923')
    exomeReadCounter('NA19239')
    exomeReadCounter('NA19175')


if __name__ == '__main__':
    main()
