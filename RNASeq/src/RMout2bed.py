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
#    RMout.readline()
#    RMout.readline()
#    RMout.readline()
    for line in RMout:       
        bed.write(organizeSp(line)) # organizeSp is a special method to convert the L1PromoterOutput into bed format. 
        # the above mrthod call needs to be replaced with organize() in case the conventional RMout file is used. 
        
    
    RMout.close()
    bed.close()
        
        


'''

This is a special method written to convert the  L1PromoterOutput into bed format. 

'''

def organizeSp(string):
    
    list = string.split() # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    chr = list[6]
    start = list[7]
    end = str(int(list[8])+1)
    name = list[10] + '#' + list[0] +'#'+  list[1] +'#'+ list[11] + '#' + list[12] + '#' +list[13] +'#' + list[14] +'#' + list[15] +'#' + list[16]
    score = '800'
    
    if list[10] == '+':
        strand = '+'
    else:
        strand = '-'
    
    
    feature = chr + '\t' + start + '\t' + end + '\t' + name + '\t' +score + '\t' + strand + '\n'
    
    return feature


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