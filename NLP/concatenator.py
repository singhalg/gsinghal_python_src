'''
Created on Jan 15, 2012

@author: gsinghal
'''





import os, sys


def concatenator(outputFileName):

    cwd = os.getcwd()
    print cwd
    items = os.listdir(cwd)
    print items
##    fh = open('filelist.txt', 'rU')
    data = fh.readlines()
    filenames = []
    for each in items:
        if (each[-4:] == '.txt') and (each[:3] =='Doc'):
            filenames.append(each)




##    for each in data:
####        print each
##        files = each.split()
####        print files
####        print 'finished processing one line'
##        for afile in files:
##            filenames.append(afile)
    print 'Appending the text in ', len(filenames) , ' files to ', outputFileName

    fhout = open(outputFileName, 'w')
    perfect = 0
    imperfect = 0
    fail = 0
    for eachFile in filenames:
        fhout.write('\n')
        fline = '#########################' + eachFile + '#########################'
        fhout.write(fline)
        fhout.write('\n')

        fhout.write('\n')

        fhin = open(eachFile, 'rU')
        notes = fhin.readlines()
        fhin.close()

        fhout.writelines(notes)


    fhout.close()






def main():
    concatenator(outputFileName)

if __name__ == '__main__':
    main()