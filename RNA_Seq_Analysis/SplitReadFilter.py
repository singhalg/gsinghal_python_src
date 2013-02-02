'''
Created on Apr 7, 2011

@author: Gaurav
'''


'''
This script takes a sam alignment of rna seq reads and filters out those read that align to splice sites
and keeps only those reads that map entirely within exons. 
'''


import sys, re


def splitReadFilter(sam_file):
    
    sam = open(sam_file, 'rU')
    
    output = open(sam_file[:-4]+'_noSplit.sam', 'w')
    
    for line in sam:
        
        if organize(line):
            output.write(line)
        

def organize(sam_alignment_line):
    fields = sam_alignment_line.split('\t')
    cigar = fields[5].strip()
    if re.match('N', cigar):
        return False
    else:
        return True
    
    


def main():
    sam_file = sys.argv[1]
    splitReadFilter(sam_file)
    
    
if __name__ == '__main__':
    main()