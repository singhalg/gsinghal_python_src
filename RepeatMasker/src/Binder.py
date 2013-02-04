'''
Created on Jun 21, 2010

@author: Gaurav
'''


'''This script binds the repeat masker output data from multiple chromosomes'''


import sys

def reader(hg18, file):
    data = open(file, 'rU')
    data.readline()
    data.readline()
    data.readline()
    for line in data:
        hg18.append(line)
    
    
    data.close()
    return hg18


def binder(file1, file2, file3, file4, 
           file5, file6, file7, file8, 
           file9, file10, file11, file12, 
           file13, file14, file15, file16, 
           file17, file18, file19, file20, 
           file21, file22, fileX, fileY):
    
    
    list = []
    
    hg18 = reader(list, file1)
    
    hg18 = reader(hg18, file2)
    
    hg18 = reader(hg18, file3)
    
    hg18 = reader(hg18, file4)
    
    hg18 = reader(hg18, file5)
    
    hg18 = reader(hg18, file6)
    
    hg18 = reader(hg18, file7)
    
    hg18 = reader(hg18, file8)
    
    hg18 = reader(hg18, file9)
    
    hg18 = reader(hg18, file10)
    
    hg18 = reader(hg18, file11)
    
    hg18 = reader(hg18, file12)
    
    hg18 = reader(hg18, file13)
    
    hg18 = reader(hg18, file14)
    
    hg18 = reader(hg18, file15)
    
    hg18 = reader(hg18, file16)
    
    hg18 = reader(hg18, file17)
    
    hg18 = reader(hg18, file18)
    
    hg18 = reader(hg18, file19)
    
    hg18 = reader(hg18, file20)
    
    hg18 = reader(hg18, file21)
    
    hg18 = reader(hg18, file22)
    
    hg18 = reader(hg18, fileX)
    
    hg18 = reader(hg18, fileY)
    
    output = open('hg18.fa.out', 'w')
    
    
    for line in hg18:
        output.write(line)
        
    output.close()
    
def main():
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    file3 = sys.argv[3]
    file4 = sys.argv[4]
    file5 = sys.argv[5]
    file6 = sys.argv[6]
    file7 = sys.argv[7]
    file8 = sys.argv[8]
    file9 = sys.argv[9]
    file10 = sys.argv[10]
    file11 = sys.argv[11]
    file12 = sys.argv[12]
    file13 = sys.argv[13]
    file14 = sys.argv[14]
    file15 = sys.argv[15]
    file16 = sys.argv[16]
    file17 = sys.argv[17]
    file18 = sys.argv[18]
    file19 = sys.argv[19]
    file20 = sys.argv[20]
    file21 = sys.argv[21]
    file22 = sys.argv[22]
    fileX = sys.argv[23]
    fileY = sys.argv[24]
    binder(file1, file2, file3, file4, 
           file5, file6, file7, file8, 
           file9, file10, file11, file12, 
           file13, file14, file15, file16, 
           file17, file18, file19, file20, 
           file21, file22, fileX, fileY)
    
if __name__=='__main__':
    main()
    
    