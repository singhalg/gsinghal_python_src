'''
Created on Jun 10, 2010

@author: Gaurav
'''
import sys

def siteParser(file):
    data = open(file, 'rU')
    
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
    
    
    for line in data:
        list = organizeRead(line)
        if list[0] == 'chr1':
            chr1.append(list)
        elif list[0] == 'chr2':
            chr2.append(list)
        elif list[0] == 'chr3':
            chr3.append(list)
        elif list[0] == 'chr4':
            chr4.append(list)
        elif list[0] == 'chr5':
            chr5.append(list)
        elif list[0] == 'chr6':
            chr6.append(list)
        elif list[0] == 'chr7':
            chr7.append(list)
        elif list[0] == 'chr8':
            chr8.append(list)
        elif list[0] == 'chr9':
            chr9.append(list)
        elif list[0] == 'chr10':
            chr10.append(list)
        elif list[0] == 'chr11':
            chr11.append(list)
        elif list[0] == 'chr12':
            chr12.append(list)
        elif list[0] == 'chr13':
            chr13.append(list)
        elif list[0] == 'chr14':
            chr14.append(list)
        elif list[0] == 'chr15':
            chr15.append(list)
        elif list[0] == 'chr16':
            chr16.append(list)
        elif list[0] == 'chr17':
            chr17.append(list)
        elif list[0] == 'chr18':
            chr18.append(list)
        elif list[0] == 'chr19':
            chr19.append(list)
        elif list[0] == 'chr20':
            chr20.append(list)
        elif list[0] == 'chr21':
            chr21.append(list)
        elif list[0] == 'chr22':
            chr22.append(list)
        elif list[0] == 'chrX':
            chrX.append(list)
        elif list[0] == 'chrY':
            chrY.append(list)
    reads = [chr1, chr2, chr3, chr4, chr5, chr6, chr7, chr8, chr9, chr10, chr11, chr12, chr13, chr14, chr15, chr16, chr17, chr18, chr19, chr20, chr21, chr22, chrX, chrY]
    return reads
    
"""
@param string:takes in one line of a string and splits the words using whitespace as a delimiter
@return : returns a list of words
"""
def organizeRead(string):
    string = string.strip() # stripping the string of the leading and trailing whitespaces
    list = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    #long can hold longer numbers
    plist = [list[0], long(list[1]), long(list[2])]
    #plist = processed list, all the string that can be converted into long are being converted here.
    return plist
    
def main():
    file = sys.argv[1]
    siteParser(file)
    
if __name__=='__main__':
    main()