'''
Created on Jul 25, 2010

@author: Gaurav
'''


'''
This script converts a Bowtie output(*.map) into bed format(*.bed). Extensions are not binding.

BOWTIE OUTPUT
bowtie outputs one alignment per line. Each line is a collection of 8 fields separated by tabs; from left to right, the fields are:
1.Name of read that aligned
2. Reference strand aligned to, + for forward strand, - for reverse
3. Name of reference sequence where alignment occurs, or numeric ID if no name was provided
4. 0-based offset into the forward reference strand where leftmost character of the alignment occurs
5. Read sequence (reverse-complemented if orientation is -).If the read was in colorspace, then the sequence shown in this column is the sequence of decoded nucleotides, not the original colors. See the Colorspace alignment section for details about decoding. To display colors instead, use the --col-cseq option.
6. ASCII-encoded read qualities (reversed if orientation is -). The encoded quality values are on the Phred scale and the encoding is ASCII-offset by 33 (ASCII char !).If the read was in colorspace, then the qualities shown in this column are the decoded qualities, not the original qualities. See the Colorspace alignment section for details about decoding. To display colors instead, use the --col-cqual option.
7. If -M was specified and the prescribed ceiling was exceeded for this read, this column contains the value of the ceiling, indicating that at least that many valid alignments were found in addition to the one reported.Otherwise, this column contains the number of other instances where the same sequence aligned against the same reference characters as were aligned against in the reported alignment. This is not the number of other places the read aligns with the same number of mismatches. The number in this column is generally not a good proxy for that number (e.g., the number in this column may be '0' while the number of other alignments with the same number of mismatches might be large).
8. Comma-separated list of mismatch descriptors. If there are no mismatches in the alignment, this field is empty. A single descriptor has the format offset:reference-base>read-base. The offset is expressed as a 0-based offset from the high-quality (5') end of the read. 


BED FORMAT
The first three required BED fields are:
1.chrom - The name of the chromosome (e.g. chr3, chrY, chr2_random) or scaffold (e.g. scaffold10671). 
2. chromStart - The starting position of the feature in the chromosome or scaffold. The first base in a chromosome is numbered 0. 
3. chromEnd - The ending position of the feature in the chromosome or scaffold. The chromEnd base is not included in the display of the feature. For example, the first 100 bases of a chromosome are defined as chromStart=0, chromEnd=100, and span the bases numbered 0-99. 

The 9 additional optional BED fields are:
4. name - Defines the name of the BED line. This label is displayed to the left of the BED line in the Genome Browser window when the track is open to full display mode or directly to the left of the item in pack mode. 
5. score - A score between 0 and 1000. If the track line useScore attribute is set to 1 for this annotation data set, the score value will determine the level of gray in which this feature is displayed (higher numbers = darker gray). This table shows the Genome Browser's translation of BED score values into shades of gray:
6. strand - Defines the strand - either '+' or '-'.
'''
import sys


def map2bed(file):
    map = open(file, 'rU')
    
    
    if file[-4:] == '.map':
        bedFile = file[:-4]+'.bed'
    else:
        bedFile = file + '.bed'
    
    bed = open(bedFile, 'w')
    
    
    for line in map:
        bed.write(organize(line))
    map.close()
    bed.close()
        


def organize(string):
    list = string.split('\t') # this splits the list on the basis of whitespace and returns individual words of the string as a list 
    read = list[4].strip()
    readLen = len(read)
    feature = list[2] + '\t' + list[3] + '\t' + str(int(list[3])+readLen) + '\t' +list[0] + '\t' + str(800) + '\t' + list[1] + '\n'
    
    return feature

def main():
    
    mapFile = sys.argv[1]
    
    map2bed(mapFile)
    
    
if __name__=='__main__':
    main()

