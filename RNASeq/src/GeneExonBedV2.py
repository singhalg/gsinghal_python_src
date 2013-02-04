

#-------------------------------------------------------------------#
# Author: Gaurav Singhal                                            #
# Created : March 08, 2011                                          #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#


'''
This script converts the refSeq gene list into bed format and create one bed entry for every exon. 

It converts only those genes for which the cdsStartStat, cdsEndStat are "cmpl".  
'''


import sys
from sets import Set

'''
This method pulls out genes out of refGene.txt so that there is only one gene entry per name (no non-unique
genes as per gene name).
'''
def ExonBed(geneFileName):
    
    
    inFile = open(geneFileName,'rU' )
    
    geneBed = open('refGeneExonExt.bed', 'w')
    
    
    genesIn = inFile.readlines()
    
    genes = Set([])
    uniqueGenes = []
    
    for line in genesIn:
        aGene = geneParser(line)
        
        if aGene[13]=='cmpl' and aGene[14]=='cmpl':
            if aGene[12] not in genes:
                genes.add(aGene[12])
                uniqueGenes.append(aGene)
                
    print '# unique genes is : ', len(uniqueGenes)
    
    for eachGene in uniqueGenes:
        
        geneBed.writelines(writeExons(eachGene))
        
        
'''
This script pulls out genes and makes sure that for all gene entries having the same gene name,
all the exons have been pulled out. So, if there are 5 isoforms of a gene, all having the same gene name
and each having 6 exons, out of which one exon is unique only to that isoform, this script will make 9 exons
entries.


'''
def AllExonBed(geneFileName):
    
    
    inFile = open(geneFileName,'rU' )
    
    geneBed = open('refGeneAllExon.bed', 'w')
    geneBedExt = open('refGeneAllExonExt.bed', 'w')
    
    
    genesIn = inFile.readlines()
    inFile.close()
    
    # here we are making 2 dictionaries. 
    
    # In dict, key is  gene name and value is a Set of exon-start and exon-end coordinates.   
    
    dict = {}    
    
     # In uniqueGenes, key is  gene name and value is the line (among several lines of multi-isoform genes)
     # of refGene that has represents the gene.
    uniqueGenes = {}
    
    for line in genesIn:
        aGene = geneParser(line)
        
        if aGene[13]=='cmpl' and aGene[14]=='cmpl':
            if aGene[12] not in uniqueGenes:
                uniqueGenes[aGene[12]] = aGene
                
            if aGene[12]  in dict:
                exons = dict[aGene[12]]
                
                # for each exon, make a tuple and then add it to the set.
                exonTuples = tupulizeExons(aGene)
                for tup in exonTuples:
                    exons.add(tup)
                dict[aGene[12]] = exons
                
                
            else :
               #  exonTuple = createExonTuples from aGene (write a method that creates tuples of all exons in a gene
               # then add tuple  one by one
               
               
               
                
                exons = Set([])
                
                exonTuples = tupulizeExons(aGene)
                for tup in exonTuples:
                    exons.add(tup)
                dict[aGene[12]] = exons
                
                
                
    print '# kay-value pairs in uniqueGenes is : ', len(uniqueGenes)
    print '# kay-value pairs in dict is : ', len(dict)
    
    
    for eachGene in uniqueGenes:
        
        geneBedExt.writelines(writeExons(eachGene, uniqueGenes, dict))
        geneBed.writelines(writeExonsBrief(eachGene, uniqueGenes, dict))
        
    geneBed.close()
    geneBedExt.close()
        
    
'''
It returns a list of tuples. Each tuple is an 'ExonStart:ExonEnd' string.
'''
def tupulizeExons(gene):
    
    
    exonCount = int(gene[8].strip())
    exonSt =  gene[9].split(',')
    exonE = gene[10].split(',')
    
    
    # exonTuples is a list of tuples of exons. Once tuple consists of ('exonStart:exonEnd')
    exonTuples = []
    
    for x in range(exonCount):
        tup = (exonSt[x]+':'+exonE[x] ,)
        exonTuples.append(tup)
        
    return exonTuples

# remember to sort the tuples by start pos while writing them onto exons.bed

    
'''
This file takes a list of string entries (list of entries of refGene.txt)
and returns a list of lines, one for each exon of a gene. 

The fields resemble bed fields, the corresponding bed field is written in parenthesis.
1). chrom
2). exon Start (chromStart)
3). exon End (chrom End)
4). gene name (name)
5). Exon number (score)
6). strand
7).  Txn Start (thickStart)
8). Txn End (thickEnd)
9). itemRgb  (0,0,0)
10). exon Count (blockCount)
11). exonSizes (blockSizes) A comma-separated list of exon sizes.
12). exon Starts (blockStarts) : A comma-separated list of exon start positions.



'''
def writeExons(geneName, uniqueGenes, dict):
    
    gene = uniqueGenes[geneName]
     
    chrom = gene[2]
    
    # chromStart  = ExonSt
    # chromEnd = ExonEnd
    
    name = gene[12]
    
    #score = gene[8] # we will not use this field, instead of score, we will put exonCount 
    
    strand = gene[3]
    
    txnStart = gene[4]
    
    txnEnd = gene[5]
    
    rgb = '0,0,0'
    
    exons = dict[geneName]
    
    sortedExons = sorted(exons, key=sortFun)
    
    
    
    
    
    exonCount = str(len(sortedExons))
    
    exonSizes = ''
    
    ExonStart = '' # this will become the last (12th) bed entry
    exonSt = []
    exonE = []
    
    for eachExon in sortedExons:
        
        ExonStart+= exonStart(eachExon)+','
        
        exonSt.append(exonStart(eachExon))
        exonE.append(exonEnd(eachExon))
    
    

    for x in range(int(exonCount)):
        exonSize = int(exonE[x]) - int(exonSt[x])
        exonSizes+= str(exonSize) + ','
        
            
    
    Exons = []
    for x in range(int(exonCount)):
        
        if strand == '+':
        
            exonBedEntry  = chrom + '\t' +  exonSt[x] + '\t' + exonE[x] + '\t' + name + '\t'+ str(x+1) + '\t' + strand + '\t' + txnStart + '\t' + txnEnd + '\t' +rgb + '\t' +exonCount + '\t' + exonSizes + '\t' + ExonStart + '\n' 
        else :
            exonBedEntry  = chrom + '\t' +  exonSt[x] + '\t' + exonE[x] + '\t' + name + '\t'+ str(int(exonCount) -x) + '\t' + strand + '\t' + txnStart + '\t' + txnEnd + '\t' +rgb + '\t' +exonCount + '\t' + exonSizes + '\t' + ExonStart + '\n'     
        Exons.append(exonBedEntry)                 
        
    
    return Exons



'''
 BED FIELDS
1). chrom - The name of the chromosome (e.g. chr3, chrY, chr2_random) or scaffold (e.g. scaffold10671). 
2). chromStart - The starting position of the feature in the chromosome or scaffold. The first base in a chromosome is numbered 0. 
3). chromEnd - The ending position of the feature in the chromosome or scaffold. The chromEnd base is not included in the display of the feature. For example, the first 100 bases of a chromosome are defined as chromStart=0, chromEnd=100, and span the bases numbered 0-99. 
4). name - Defines the name of the BED line. This label is displayed to the left of the BED line in the Genome Browser window when the track is open to full display mode or directly to the left of the item in pack mode. 
5). score - A score between 0 and 1000. If the track line useScore attribute is set to 1 for this annotation data set, the score value will determine the level of gray in which this feature is displayed (higher numbers = darker gray). This table shows the Genome Browser's translation of BED score values into shades of gray
6). strand - Defines the strand - either '+' or '-'. 
7). thickStart - The starting position at which the feature is drawn thickly (for example, the start codon in gene displays). 
8). thickEnd - The ending position at which the feature is drawn thickly (for example, the stop codon in gene displays). 
9). itemRgb - An RGB value of the form R,G,B (e.g. 255,0,0). If the track line itemRgb attribute is set to "On", this RBG value will determine the display color of the data contained in this BED line. NOTE: It is recommended that a simple color scheme (eight colors or less) be used with this attribute to avoid overwhelming the color resources of the Genome Browser and your Internet browser. 
10). blockCount - The number of blocks (exons) in the BED line. 
11). blockSizes - A comma-separated list of the block sizes. The number of items in this list should correspond to blockCount. 
12). blockStarts - A comma-separated list of block starts. All of the blockStart positions should be calculated relative to chromStart. The number of items in this list should correspond to blockCount.
'''
def writeExonsBrief(geneName, uniqueGenes, dict):
    
    gene = uniqueGenes[geneName]
    chrom = gene[2]
    # chromStart  = ExonSt
    # chromEnd = ExonEnd
    name = gene[12]
    
    #score = gene[8] # we will put exon count in this field
    
    strand = gene[3]
    
    txnStart = gene[4]
    
    txnEnd = gene[5]
    
    rgb = '0,0,0'
    
   
    exons = dict[geneName]
    
    sortedExons = sorted(exons, key=sortFun)

    exonCount = str(len(sortedExons))
    
    exonSizes = ''
    
    exonStarts = '' # this will become the last (12th) bed entry
    exonSt = []
    exonE = []
    
    for eachExon in sortedExons:
        
        exonStarts+= exonStart(eachExon)+','
        
        exonSt.append(exonStart(eachExon))
        exonE.append(exonEnd(eachExon))
    

    for x in range(int(exonCount)):
        exonSize = int(exonE[x]) - int(exonSt[x])
        exonSizes+= str(exonSize) + ','
        
    Exons = ''
    for x in range(int(exonCount)):
        if strand == '+':
            
            exonBedEntry  = chrom + '\t' +  exonSt[x] + '\t' + exonE[x] + '\t' + name + '\t'+ str(x+1) + '\t' + strand +  '\n' 
            
        else:
             
            exonBedEntry  = chrom + '\t' +  exonSt[x] + '\t' + exonE[x] + '\t' + name + '\t'+ str(int(exonCount) - x) + '\t' + strand +  '\n' 
             
        
        Exons+=exonBedEntry                 
        
    
    return Exons


def sortFun(tuple):
    return int(tuple[0].split(':')[0])

def exonStart(string):
    return string[0].split(':')[0]

def exonEnd(string):
    return string[0].split(':')[1]


def refGeneParser(refGene):
    genefile = open(refGene, 'rU')
    Genes = []
    for each in genefile:
        Genes.append(geneParser(each))
    
    genefile.close()
    return Genes


def geneParser(line):
    splitline = line.split()
    
    
    listOfEntries = [word.strip() for word in splitline]
    
#    gene = []
#    
#    bin = listOfEntries[0]
#    gene.append(bin)
#    
#    nameGtf = listOfEntries[1]
#    gene.append(nameGtf)
#    
#    chr = listOfEntries[2]
#    gene.append(chr)
#    
#    strand= listOfEntries[3]
#    gene.append(strand)
#    
#    txStart = listOfEntries[4]
#    gene.append(txStart)
#    
#    txEnd = listOfEntries[5]
#    gene.append(txEnd)
#    
#    cdStart = listOfEntries[6]
#    gene.append(cdStart)
#    
#    cdEnd = listOfEntries[7]
#    gene.append(cdEnd)
#    
#    exonCount = listOfEntries[8]
#    gene.append(exonCount)
#    
#    exonStrt = listOfEntries[9]
#    gene.append(exonStrt)
#    
#    exonEnd = listOfEntries[10]
#    gene.append(exonEnd)
#    
#    id = listOfEntries[11]
#    gene.append(id)
#    
#    name = listOfEntries[12]
#    gene.append(name)
#    
#    cdsStat = listOfEntries[13]
#    gene.append(cdsStat)
#    
#    cdsEndStat = listOfEntries[14]
#    gene.append(cdsEndStat)
#    
#    exonFrames = listOfEntries[15]
#    gene.append(exonFrames)
#    
    return listOfEntries

def main():

    file = sys.argv[1]

    
    AllExonBed(file)
   
if __name__ == '__main__':
    main() 