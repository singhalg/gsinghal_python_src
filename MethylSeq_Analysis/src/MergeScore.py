'''
Created on Jun 7, 2010

@author: Gaurav
'''

import sys

def mergeScore(file1, file2):
    score1 = open(file1, 'rU')
    score2 = open(file2, 'rU')
    data1 = []
    data2 = []
    merged = []
    
    line1 = score1.readline()
    ind = line1.find('_')
    repFamily = line1[:ind]
    print line1
    keep1 = score1.readline().split()
    unmap1 = int(keep1[1])
    
    for line in score1:
        list = line.split()
        data1.append(int(list[2]))
        
    throw2 = score2.readline()
    keep2 = score2.readline().split()
    unmap2 = int(keep2[1])
    print throw2
    for line in score2:
        list = line.split()
        data2.append(int(list[2]))
    
    keep = unmap1 + unmap2
    unmapped = str(keep)
    i=0
    while i < len(data1):
        merged.append(data1[i] + data2[i])
        i+=1
    
    score1.close()
    score2.close()
        
    output = repFamily + 'MeDIP_score_HS1821'
    out = open(output, 'w')
    out.write(output)
    out.write('\n')
    out.write(unmapped)
    out.write('\n')
    index = 1
    for elem in merged:
        string = str(index) + ' = ' + str(elem)+'\n'
        out.write(string)
        index+=1
    out.close()
    


def SuperMerger(file1, file2, file3, file4, file5,
                file6, file7, file8, file9, file10,
                file11, file12, file13, file14, file15,
                file16, file17, file18, file19, file20):
    mergeScore(file1, file2)
    mergeScore(file3, file4)
    mergeScore(file5, file6)
    mergeScore(file7, file8)
    mergeScore(file9, file10)
    mergeScore(file11, file12)
    mergeScore(file13, file14)
    mergeScore(file15, file16)
    mergeScore(file17, file18)
    mergeScore(file19, file20)
    

   
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

    SuperMerger(file1, file2, file3, file4, file5,
                file6, file7, file8, file9, file10,
                file11, file12, file13, file14, file15,
                file16, file17, file18, file19, file20)
    
if __name__=='__main__':
    main()
    
