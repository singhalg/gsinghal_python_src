'''
Created on Jun 2, 2010

@author: Gaurav
'''

import sys

def ReadParser(file):
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
        list = organize(line)
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
    del chr1, chr2, chr3, chr4, chr5, chr6, chr7, chr8, chr9, chr10, chr11, chr12, chr13, chr14, chr15, chr16, chr17, chr18, chr19, chr20, chr21, chr22, chrX, chrY
    if reads[0]:
        print 'a read from chromosome 1 : ', reads[0][1]
    if reads[1]:
        print 'a read from chromosome 2 : ', reads[1][1]
    if reads[2]:  
        print 'a read from chromosome 3 : ', reads[2][1]
    if reads[3]:    
        print 'a read from chromosome 4 : ', reads[3][1]
    if reads[4]:    
        print 'a read from chromosome 5 : ', reads[4][1]
    if reads[5]:    
        print 'a read from chromosome 6 : ', reads[5][1]
    if reads[6]:    
        print 'a read from chromosome 7 : ', reads[6][1]
    if reads[7]:    
        print 'a read from chromosome 8 : ', reads[7][1]
    if reads[8]:    
        print 'a read from chromosome 9 : ', reads[8][1]
    if reads[9]:    
        print 'a read from chromosome 10 : ', reads[9][1]
    if reads[10]:    
        print 'a read from chromosome 11 : ', reads[10][1]
    if reads[11]:    
        print 'a read from chromosome 12 : ', reads[11][1]
    if reads[12]:    
        print 'a read from chromosome 13 : ', reads[12][1]
    if reads[13]:    
        print 'a read from chromosome 14 : ', reads[13][1]
    if reads[14]:    
        print 'a read from chromosome 15 : ', reads[14][1]
    if reads[15]:    
        print 'a read from chromosome 16 : ', reads[15][1]
    if reads[16]:    
        print 'a read from chromosome 17 : ', reads[16][1]
    if reads[17]:    
        print 'a read from chromosome 18 : ', reads[17][1]
    if reads[18]:    
        print 'a read from chromosome 19 : ', reads[18][1]
    if reads[19]:    
        print 'a read from chromosome 20 : ', reads[19][1]
    if reads[20]:    
        print 'a read from chromosome 21 : ', reads[20][1]
    if reads[21]:    
        print 'a read from chromosome 22 : ', reads[21][1]
    if reads[22]:    
        print 'a read from chromosome X : ', reads[22][1]
    if reads[23]:    
        print 'a read from chromosome Y : ', reads[23][1]
    data.close()
    return reads

    
"""
@param string:takes in one line of a string and splits the words using whitespace as a delimiter
@return : returns a list of words
"""
def organize(string):
    string = string.strip() # stripping the string of the leading and trailing whitespaces
    list = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    #long can hold longer numbers
    plist = [list[0], int(list[1]), int(list[2]), list[5]]
    del list
    #plist = processed list, all the string that can be converted into long are being converted here.
    return plist
    
def main():
    file = sys.argv[1]
    ReadParser(file)
    
if __name__=='__main__':
    main()