#!/usr/bin/python -tt


'''
Adapted from sam2bed.py written by Aaron Quinlan, 2009-08-27.
@author - Gaurav Singhal, 2010-07-08.
'''
###################################################################################################
#  This script parses a sam file (line by line) and produces a corresponding bed format file.     #
#  It creates a new file with the same name, and changes extension to .bed or adds .bed at the end#
#  and writes the output to this file.                                                            #
#  python sam2bedcon.py <samfile>                                                                 #
###################################################################################################


import sys
import re


def processSAM(file):
    """
        Load a SAM file and convert each line to BED format.
    """        
    
    if file[-4:] == '.sam':
        filename = file[:-4]+'.bed'
    else: 
        filename = file + '.bed'
    output = open(filename, 'w')
    
    f = open(file,'r')
    for line in f:
        samLine = splitLine(line.strip())
        bedline = makeBED(samLine)
        output.write(bedline)
    f.close()    
    output.close()


'''
@return: One line in BED format
'''                   
def makeBED(samFields):
    
    samFlag = int(samFields[1])
    
    # Only create a BED entry if the read was aligned
    if (not (samFlag & 0x0004)):
        
        chrom = 'chr'+ samFields[2]
        start = str(int(samFields[3])-1)
        end = str(int(samFields[3]) + len(samFields[9]) - 1)
        name = samFields[9]    
        strand = getStrand(samFlag)

        # Let's use the edit distance as the BED score.
        # Clearly alternatives exist.
        editPattern = re.compile('NM\:i\:(\d+)')
        editDistance = editPattern.findall(samFields[12])

        # Write out the BED entry
        aLine =  chrom + "\t" + start + "\t" + end + "\t" + name + "\t" + editDistance[0] + "\t" + strand + '\n'
        del chrom, start, end, name, strand, editDistance, editPattern
        return aLine
        
        
        
def splitLine(line, delim="\t"):
    splitline = line.split(delim)
    return splitline 
       


def getStrand(samFlag):
    strand = "+"
    if (samFlag & (0x10)):    # minus strand if true.
        strand = "-"        
    return strand
    
        
def main():
    samFile = sys.argv[1]  

    # make a BED file of the SAM file.
    processSAM(samFile)

if __name__ == "__main__":
    main()