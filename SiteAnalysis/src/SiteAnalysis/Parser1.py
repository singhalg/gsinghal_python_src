'''
Created on May 25, 2010

@author: Gaurav


'''
import sys
import decimal

# README
# this file is a modified form of Parser.py and has been customized to read from files containing RepeatMasker output data for a single family, such as AluY
# such files (containing data of one particular repeat family) have been generated using Parser.py

'''
@param : repFamily : string, which is the name of the repeat family
@param : boolean : write : true / false or 0/1 , if true, this method creates a new file and write the output to that file.
@return : returns a list of all the lines in the input file that contain repFamily in col[9]

'''

def ParserS(file, repFamily, write):
    if write:
        output = open(repFamily, 'w')
    
    chr1 = []
    chr2 = []
    chr3 = []
    chr4 = []
    chr5 = []
    chr6 = []
    chr7 = []
    chr8 = []
    chr9 = []
    chr10 = []
    chr11 = []
    chr12 = []
    chr13 = []
    chr14 = []
    chr15 = []
    chr16 = []
    chr17 = []
    chr18 = []
    chr19 = []
    chr20 = []
    chr21 = []
    chr22 = []
    chrX = []
    chrY = []
    
        
    input = open (file, 'rU')
    for line in input:
        list = organize(line)
        
        if list[4] == 'chr1':
            chr1.append(list)
        elif list[4] == 'chr2':
            chr2.append(list)
        elif list[4] == 'chr3':
            chr3.append(list)
        elif list[4] == 'chr4':
            chr4.append(list)
        elif list[4] == 'chr5':
            chr5.append(list)
        elif list[4] == 'chr6':
            chr6.append(list)
        elif list[4] == 'chr7':
            chr7.append(list)
        elif list[4] == 'chr8':
            chr8.append(list)
        elif list[4] == 'chr9':
            chr9.append(list)
        elif list[4] == 'chr10':
            chr10.append(list)
        elif list[4] == 'chr11':
            chr11.append(list)
        elif list[4] == 'chr12':
            chr12.append(list)
        elif list[4] == 'chr13':
            chr13.append(list)
        elif list[4] == 'chr14':
            chr14.append(list)
        elif list[4] == 'chr15':
            chr15.append(list)
        elif list[4] == 'chr16':
            chr16.append(list)
        elif list[4] == 'chr17':
            chr17.append(list)
        elif list[4] == 'chr18':
            chr18.append(list)
        elif list[4] == 'chr19':
            chr19.append(list)
        elif list[4] == 'chr20':
            chr20.append(list)
        elif list[4] == 'chr21':
            chr21.append(list)
        elif list[4] == 'chr22':
            chr22.append(list)
        elif list[4] == 'chrX':
            chrX.append(list)
        elif list[4] == 'chrY':
            chrY.append(list)
        if write:
            output.write(line)
            
        #else # do nothing, just move on to the next list 
    if write:
        print 'Repeat data for ', repFamily, ' has been extracted and written to file : ', repFamily
        print 'The contents of the file ' ,repFamily,' created by Parser1.py look like this :' 
    input.close()
    if write:
        output.close()
    Repeats = [chr1, chr2, chr3, chr4, chr5, chr6, chr7, chr8, chr9, chr10, chr11, chr12, chr13, chr14, chr15, chr16, chr17, chr18, chr19, chr20, chr21, chr22, chrX, chrY]
    return Repeats




'''
@param string:takes in one line of a string and splits the words using whitespace as a delimiter
@return : returns a list of words
'''
def organize(string):
    string = string.strip()
    oldlist = string.split()
    list = []
    for word in oldlist:
        list.append(word.strip('()'))
    plist = [int(list[0]), list[1], list[2], list[3], list[4], int(list[5]), int(list[6]), int(list[7]), list[8], list[9], list[10], int(list[11]), int(list[12]), int(list[13]), int(list[14])]
    #plist = processed list, all the string that can be converted into int are being converted here.
    return plist
    

'''
@param : takes in a string
@return : returns an empty list with the name as the param
'''
def listcons(string):
    string = []
    return string
    

def main():
    openfile = sys.argv[1]
    repFamily = sys.argv[2]
    write = sys.argv[3]
    ParserS(openfile, repFamily, write)   
 



if __name__ == '__main__':
    main()
