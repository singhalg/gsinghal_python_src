'''
Created on Mar 29, 2012

@author: gsinghal
'''
import sys


def YRI():
    
    fh = open('YRI_high_coverage.csv', 'rU')
    fields = fh.readline()
    
    breakdown = [[0,0], 
               [0,0], 
               [0,0]]
    
    samples = ['NA19238']
    
    data = fh.readlines()
    for line in data:
        elements = line.split('\t')
        if elements[9].strip()=='NA19238':
#            if 
            pass
        pass

def main():
    YRI()
    

if __name__=='__main__':
    main()