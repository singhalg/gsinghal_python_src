'''
Created on Feb 16, 2011

@author: Gaurav
'''


#-------------------------------------------------------------------#
# Author: Gaurav Singhal                                            #
# Created : Feb 15, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#


import sys
import pickle

'''
This script was originally written for fetching L1 sequences from hg18, but it has been modified (on March 06) 
to fetch LTR sequences.
'''


def fetchSeqBench():
    
    pass


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
    

    
    
    
    
    
    L1files = ['L1saa', 'L1sab','L1sac','L1sad','L1sae','L1saf','L1sag','L1sah','L1sai','L1saj']
    
    for L1split in L1files:
        
    
        L1 = open(L1split, 'rU')
        fetchedTag = 'L1fetched' + L1split[-2:] + '.fa'
        fetchedSeqs = open(fetchedTag, 'w')
    
        for entry in L1:
                 
            repEntry = organize(entry)
            
            repId = ''
            for col in repEntry[:-1]:
                repId+= col + '#'
            repId+=repEntry[-1]
            
            fetchedSeqs.write('\n'+ '>' + repId + '\n')
            repStart = int(repEntry[5])
            repEnd = int(repEntry[6])
            
            chrName = repEntry[4]
            chrSeq = hg18[chrName]
            repSeq = chrSeq[repStart:repEnd]
            
            if repEntry[8] == '+':
                finalSeq = repSeq
            else:
                finalSeq = reversecomplement(repSeq)
            
            fetchedSeqs.write(fastacize(finalSeq))
    
        fetchedSeqs.close()
        L1.close()
                    



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

def organize(string):
    list = string.split()
    slist = [each.strip('()') for each in list]
    return slist
        

def main():

    fetchSeq()
    
    
if __name__ == '__main__':
    main()
    
    
        
        
        
    
    
    
    
    