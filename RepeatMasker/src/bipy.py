'''
Created on May 29, 2010

@author: Gaurav
'''
from Bio.Seq import Seq
import matplotlib.pyplot as plot
import numpy as numpy


mySeq = Seq("ATCTGCTATGCATTGCA")


print 'mySeq = '
print mySeq

print mySeq.complement()
print mySeq.reverse_complement()
from Bio import SeqIO 
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"): 
 print seq_record.id 
 print repr(seq_record.seq) 
 print len(seq_record)
 print 'seq_record.seq', seq_record.seq




