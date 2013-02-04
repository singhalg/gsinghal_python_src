'''
Created on Feb 16, 2011

@author: Gaurav
'''



import sys
import pickle

'''
This script was originally written for fetching L1 sequences from hg18, but it has been modified (on March 06) 
to fetch LTR sequences.
'''




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
    

    
    
    
    
    
    
    fetchedTag = 'chr.fa'
    fetchedSeqs = open(fetchedTag, 'w')
    
            
    fetchedSeqs.write('\n'+ '>' + fetchedTag + '\n')
    repStart = int(repEntry[5])
    repEnd = int(repEntry[6])
            
    chrName = repEntry[4]
    chrSeq = hg18[chrName]
    repSeq = chrSeq[repStart:repEnd]
            
            
    if repEntry[8] == '+':
        print repEntry[8]
        print 'its on + strand'
        finalSeq = repSeq
    else:
        finalSeq = reversecomplement(repSeq)
            
            
    fetchedSeqs.write(fastacize(finalSeq))
    
    fetchedSeqs.close()
        
                    



def complement(s): 
    """Return the complementary sequence string.""" 
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N':'N','X':'X', 'a':'t', 'c':'g', 'g':'c', 't':'a', 'n':'n', '\n':'\n', 'x':'x'} 
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

def organize(string):
    list = string.split()
    slist = [each.strip('()') for each in list]
    return slist
        

def main():

    fetchSeq()
    
    
if __name__ == '__main__':
    main()
    
    
        
        
        
    
    
    
    
    