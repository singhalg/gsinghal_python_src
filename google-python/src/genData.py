'''
Created on May 17, 2010

@author: Gaurav
'''
#import re
import sys
"""  
data returns a list of lists. Each item (genData1, genedata2, ....genDataY) of this list is a list of tuples, each tuple contains a CpG island.
The elements of tuples are the start and end position of the CpG island.

"""

def CpGdata(openfile):
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
        list = Find(line)
        if list[1]=='chr1':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData1.append(tuple)
        if list[1]=='chr2':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData2.append(tuple)
        if list[1]=='chr3':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData3.append(tuple)
        if list[1]=='chr4':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData4.append(tuple)
        if list[1]=='chr5':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData5.append(tuple)
        if list[1]=='chr6':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData6.append(tuple)
        if list[1]=='chr7':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData7.append(tuple)
        if list[1]=='chr8':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData8.append(tuple)
        if list[1]=='chr9':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData9.append(tuple)
        if list[1]=='chr10':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData10.append(tuple)
        if list[1]=='chr11':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData11.append(tuple)
        if list[1]=='chr12':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData12.append(tuple)    
        if list[1]=='chr13':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData13.append(tuple) 
        if list[1]=='chr14':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData14.append(tuple)
        if list[1]=='chr15':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData15.append(tuple)
        if list[1]=='chr16':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData16.append(tuple)
        if list[1]=='chr17':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData17.append(tuple)
        if list[1]=='chr18':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData18.append(tuple)
        if list[1]=='chr19':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData19.append(tuple)
        if list[1]=='chr20':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData20.append(tuple)
        if list[1]=='chr21':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData21.append(tuple)
        if list[1]=='chr22':
            tuple = (int(list[2]), int(list[3]), list[0])
            genData22.append(tuple)      
        if list[1]=='chrX':
            tuple = (int(list[2]), int(list[3]), list[0])
            genDataX.append(tuple)
        if list[1]=='chrY':
            tuple = (int(list[2]), int(list[3]), list[0])
            genDataY.append(tuple) 
    genData = [genData1, genData2, genData3, genData4, genData5, genData6, genData7, genData8, genData9, genData10,
               genData11, genData12, genData13, genData14, genData15, genData16, genData17, genData18, genData19, genData20, genData21,
               genData22, genDataX, genDataY]
    fileData.close()
    sum = 0
    for CpG in genData1:
        
        #print CpG
        length = CpG[1] - CpG[0]
        #print length
        sum = sum+length
    print 'the average length of CpG islands in chr1 is ' , sum/len(genData1)    
    return genData # this is actually the whole CpG island file in one big list 
   
   
def Find(str):
    plist = str.split()
    list = [plist[0], plist[1], plist[2], plist[3]]
    return list







 



def main():
 openfile = sys.argv[1]
 CpGdata(openfile)   
 



if __name__ == '__main__':
    main()

