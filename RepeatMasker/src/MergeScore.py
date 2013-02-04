'''
Created on Jun 7, 2010

@author: Gaurav
'''

import sys

def mergeScore(repFamily, file1, file2):
    score1 = open(file1, 'rU')
    score2 = open(file2, 'rU')
    data1 = []
    data2 = []
    merged = []
    
    throw1 = score1.readline()
    keep1 = score1.readline().split()
    unmap1 = keep1[1]
    print throw1
    for line in score1:
        list = line.split()
        data1.append(int(list[2]))
        
    throw2 = score2.readline()
    keep2 = score2.readline().split()
    unmap2 = keep2[1]
    print throw2
    for line in score2:
        list = line.split()
        data2.append(int(list[2]))
    
    keep = unmap1 + unmap2
    
    i=0
    while i < len(data1):
        merged.append(data1[i] + data2[i])
        i+=1
    
    score1.close()
    score2.close()
        
    output = file1+file2
    out = open(output, 'w')
    out.write(repFamily)
    out.write('\n')
    out.write(keep)
    out.write('\n')
    index = 1
    for elem in merged:
        string = str(index) + ' = ' + str(elem)+'\n'
        out.write(string)
        index+=1
        
    out.close()
def main():
    repFamily = sys.argv[1]
    file1 = sys.argv[2]
    file2 = sys.argv[3]
    mergeScore(repFamily, file1, file2)
    
if __name__=='__main__':
    main()
