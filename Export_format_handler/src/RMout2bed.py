'''
Created on Jul 26, 2010

@author: Gaurav
'''
'''

This script converts a RepeatMasker output(*.out) into bed format(*.bed). Extensions are not binding.
'''
import sys


def RMout2bed(file):
    
    
    if file[-4:] == '.out':
        bedFile = file[:-4]+'.bed'
    else:
        bedFile = file + '.bed'
    RMout = open(file, 'rU')
    bed = open(bedFile, 'w')
    RMout.readline()
    RMout.readline()
    RMout.readline()
    for line in RMout:       
        bed.write(organize(line))
        
    
    RMout.close()
    bed.close()
        


def organize(string):
    list = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    chr = list[4]
    start = list[5]
    end = str(int(list[6])+1)
    name = list[9] + '#' + list[10] + '#' +list[11] +'#' + list[12] +'#' + list[13] +'#' + list[14] + '         '
    score = '800'
    
    if list[8] == '+':
        strand = '+'
    else:
        strand = '-'
    
    
    feature = chr + '\t' + start + '\t' + end + '\t' + name + '\t' +score + '\t' + strand + '\n'
    
    return feature

def main():
    
    File = sys.argv[1]
    
    RMout2bed(File)
    
    
if __name__=='__main__':
    main()