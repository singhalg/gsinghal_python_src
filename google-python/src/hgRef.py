'''
Created on May 18, 2010

@author: Gaurav
'''
import sys
"""  
data returns a list of lists. Each item (genData1, genedata2, ....genDataY) of this list is a list of tuples, each tuple contains a CpG island.
The elements of tuples are the start and end position of the CpG island.

"""

def genedata(openfile):
    genData1 = []
    genData2 = []
    genData3 = []
    genData4 = []
    genData5 = []
    genData6 = []
    genData7 = []
    genData8 = []
    genData9 = []
    genData10 = []
    genData11 = []
    genData12 = []
    genData13 = []
    genData14 = []
    genData15 = []
    genData16 = []
    genData17 = []
    genData18 = []
    genData19 = []
    genData20 = []
    genData21 = []
    genData22 = []
    genDataX = []
    genDataY = []
    
    fileData =  open(openfile, 'rU')
    for line in fileData:
        list = Find(line)  # Find parses the line and makes the data structured
        if list[2]=='chr1':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData1.append(tuple)
        if list[2]=='chr2':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData2.append(tuple)
        if list[2]=='chr3':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData3.append(tuple)
        if list[2]=='chr4':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData4.append(tuple)
        if list[2]=='chr5':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData5.append(tuple)
        if list[2]=='chr6':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData6.append(tuple)
        if list[2]=='chr7':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData7.append(tuple)
        if list[2]=='chr8':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData8.append(tuple)
        if list[2]=='chr9':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData9.append(tuple)
        if list[2]=='chr10':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData10.append(tuple)
        if list[2]=='chr11':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData11.append(tuple)
        if list[2]=='chr12':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData12.append(tuple)    
        if list[2]=='chr13':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData13.append(tuple) 
        if list[2]=='chr14':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData14.append(tuple)
        if list[2]=='chr15':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData15.append(tuple)
        if list[2]=='chr16':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData16.append(tuple)
        if list[2]=='chr17':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData17.append(tuple)
        if list[2]=='chr18':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData18.append(tuple)
        if list[2]=='chr19':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData19.append(tuple)
        if list[2]=='chr20':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData20.append(tuple)
        if list[2]=='chr21':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData21.append(tuple)
        if list[2]=='chr22':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genData22.append(tuple)      
        if list[2]=='chrX':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genDataX.append(tuple)
        if list[2]=='chrY':
            tuple = (int(list[4]), int(list[5]), list[0], list[1])
            genDataY.append(tuple) 
    refFlat = [genData1, genData2, genData3, genData4, genData5, genData6, genData7, genData8, genData9, genData10,
               genData11, genData12, genData13, genData14, genData15, genData16, genData17, genData18, genData19, genData20, genData21,
               genData22, genDataX, genDataY]
    sum = 0
    for gene in genData1:
        #print gene
        length = gene[1] - gene[0]
        sum = sum + length
    
    print 'for chr1, the average gene length is ', sum/len(genData1)
    return refFlat # this is actually the whole CpG island file in one big list 
   
   
   
"""

splits the line using whitespace as a delimiter, and puts the first 6 words in a list. Returns that list.
@param - str - one line of string
@return - a list of (string)data    
   
"""
     
def Find(str):
    plist = str.split()
    list = plist[0:6]
    return list




def main():
 openfile = sys.argv[1]
 genedata(openfile)   
 



if __name__ == '__main__':
    main()

