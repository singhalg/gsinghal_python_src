'''
Created on Feb 16, 2011

@author: Gaurav
'''



import sys
import pickle





def fetchSeq():
    
    
    hg18 = {}
    
    chrFa = []
    for i in range (1, 23):
        chr = 'chr' + str(i)+ '.fa'
        chrFa.append(chr)
    
    chrFa.append('chrX.fa')
    chrFa.append('chrY.fa')
    
          
    for each in chrFa:
        chrSeq = open(each, 'rU')
        chrSeq.readline()
        sequence = ''
        for line in chrSeq:
            sline = line.strip()
            sequence+=sline
        key = each[:-3]
        hg18[key] = sequence
    

    pickled = open('L1_sorted_pickle', 'rU')
    
    sortedDict = pickle.load(pickled)
    
    fetchedSeqs = open('L1_fetchedSeqs_id', 'w')
    
    
    for repFamily in sortedDict:
        list = sortedDict[repFamily]
        
        for entry in list[:2]:
            
            
            repEntry = str(entry)
            
            
            fetchedSeqs.write('\n'+ '>' + repEntry + '\n')
            repStart = int(entry[5])
            repEnd = int(entry[6])
            
            chrName = entry[4]
            chrSeq = hg18[chrName]
            repSeq = chrSeq[repStart:repEnd]
            
            if entry[8] == '+':
                
                finalSeq = repSeq
                
                
            else:
                finalSeq = reversecomplement(repSeq)
            fetchedSeqs.write(fastacize(finalSeq))
    
    fetchedSeqs.close()
                    
   
   
   
   
        
    
        
    


def complement(s): 
    """Return the complementary sequence string.""" 
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N':'N', 'a':'t', 'c':'g', 'g':'c', 't':'a', 'n':'n', '\n':'\n'} 
    letters = list(s) 
    letters = [basecomplement[base] for base in letters] 
    return ''.join(letters) 


def reverse(s):
    revSeq = ''
    
    base = len(s) -1
    while base>=0:
        revSeq += s[base]
        base-=1
    
    return revSeq
        

def reversecomplement(s):
    """Return the reverse complement of the dna string.""" 
    s = reverse(s) 
    s = complement(s) 
    return s 

def fastacize(string):
    
    size = len(string)
    s = 0
    e = s+50
    fasta = ''
    while e < size:
        fasta += string[s:e] + '\n'
        s+= 50
        e= s+50
    fasta+= string[s:size]+'\n'
    return fasta

    

def main():

    fetchSeq()
    
    
if __name__ == '__main__':
    main()
    
    
        
        
        
    
    
    
    
    