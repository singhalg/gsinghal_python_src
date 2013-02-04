'''
Created on Jun 2, 2010

@author: Gaurav
'''

import sys



'''
@param - for every line of reads, it searches for the line of RepeatMasker data which contains the matching start and end coordinates. 
'''

'''
Recursive solution for Binary search
 BinarySearch(A[0..N-1], value, low, high) {
       if (high < low)
           return -1 // not found
       mid = low + ((high - low) / 2) 
       if (A[mid] > value)
           return BinarySearch(A, value, low, mid-1)
       else if (A[mid] < value)
           return BinarySearch(A, value, mid+1, high)
       else
           return mid // found
   }
'''

'''
@param repeat: the list of all repeats (really big list)
@param read: one read, one line of file of read data
@param min: min = 0
@param max: max = len(repeat) - 1  
@return: returns -2 if the matching repeat for a read is not found; else returns the repeat occurance which matches the read

'''
def binaryS(repeat, read, min, max):
    if (max<min):
        return -2 # not found
    mid = (max + min)/2
    if repeat[mid][5] - read[2] > 0:      
        return binaryS(repeat, read, min, mid-1)
    elif repeat[mid][6] - read[1] < 0 :
        return binaryS(repeat, read, mid+1, max)
    else:
        return mid  #found 




'''
All the if and elif cases in this method are true all the time, as this method is called only when there is an overlap. Whether an overlap occurs between read and repeat 
is decided by the binaryS method. Overlap method determines the extent of overlap and then it calls scorer method to 
update the consensus scores accordingly.
@param - readS, readE, TPS, TPE, start, end would be taken from data lines specified by the binaryS method 
@param consensus: 
@param start: the start of occurance of repeat element on the consensus
@param end: the end of occurance of repeat element on the consensus
@param readS: start coordinate of read
@param readE: end coordinate of read
@param TPS: start coordinate of repeat element
@param TPE: end coordinate of repeat element  
'''

def overlap(consensus, start, end, readS, readE, TPS, TPE):
    
    if readS>TPS and readS<TPE:
        shiftS = readS-TPS
        if readE<TPE:
            shiftE = (TPE-readE)*-1
        else: 
            shiftE = 0
        scorer(consensus, start, end, shiftS, shiftE)
        
    
    elif readE>TPS and readE<TPE:
        shiftS = 0
        shiftE = (TPE-readE)*-1
        scorer(consensus, start, end, shiftS, shiftE)
        
    
    elif readS<=TPS and readE>=TPE:
        shiftS = 0
        shiftE = 0
        scorer(consensus, start, end, shiftS, shiftE)
        


'''
This method updates the scores of consensus

@param start - start coordinate of TE on the TE consensus
@param end - end coordinate of TE on the TE consensus
@param consensus - list of numbers representing per base score for consensus
@shiftS - shift from start
@shiftE - shift from end 
'''

def scorer(consensus, start, end, shiftS, shiftE):
    for i in range(start + shiftS, end + shiftE):
        consensus[i] += 1
    

    
    