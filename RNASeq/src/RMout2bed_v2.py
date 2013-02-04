'''
Created on Jul 26, 2010

@author: Gaurav
'''

'''

This script converts a RepeatMasker output(*.out) into bed format(*.bed). Extensions are not binding.

'''
import sys

'''
@param file:L1Promoter_RM.out
@param orientation: L1SP53 / L1SP35 / L1ASP53 / L1ASP35
@param strand : p / m 
'''
def RMout2bed(file, orientation, strand):
    
    

    bedFile = orientation + strand +'.bed'
    RMout = open(file, 'rU')
    bed = open(bedFile, 'w')

    if strand == 'p':
        strand = '+'
    else : strand = 'C'
    for line in RMout:
        L1bed = organizeSp(line, orientation, strand)
        if L1bed:
            bed.write(L1bed) # organizeSp is a special method to convert the L1PromoterOutput into bed format. 
        # the above mrthod call needs to be replaced with organize() in case the conventional RMout file is used. 
        
    
    RMout.close()
    bed.close()
        
        


'''

This is a special method written to convert the  L1PromoterOutput into bed format. 

'''

def organizeSp(string, orientation, dnaStrand):
    
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
    
    if orientation == list[0]:
        if dnaStrand == list[10]:
               
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
    orientation = sys.argv[2]
    strand = sys.argv[3]
    
    RMout2bed(File, orientation, strand)
    
    
if __name__=='__main__':
    main()