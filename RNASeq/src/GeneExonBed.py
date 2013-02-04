

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
This file takes a list of string entries (list of entries of refGene.txt)
and returns a list of lines, one for each exon of a gene. 
'''
def writeExons(gene):
    
    
     
    chrom = gene[2]
    
    name = gene[12]
    
    score = gene[8]
    
    strand = gene[3]
    
    txnStart = gene[4]
    
    txnEnd = gene[5]
    
    rgb = '0,0,0'
    
    exonCount = gene[8]
    
    exonSizes = ''
    
    exonStart = gene[9]
    
    exonSt =  gene[9].split(',')
    exonE = gene[10].split(',')
    for x in range(int(exonCount)):
        exonSize = int(exonE[x]) - int(exonSt[x])
        exonSizes+= str(exonSize) + ','
        
            
    
    Exons = []
    for x in range(int(exonCount)):
        
        exonBedEntry  = chrom + '\t' +  exonSt[x] + '\t' + exonE[x] + '\t' + name + '\t'+ score + '\t' + strand + '\t' + txnStart + '\t' + txnEnd + '\t' +rgb + '\t' +exonCount + '\t' + exonSizes + '\t' + exonStart + '\n' 
        Exons.append(exonBedEntry)                 
        
    
    return Exons

def writeExonsBrief(gene):
    
    
     
    chrom = gene[2]
    
    name = gene[12]
    
    score = gene[8]
    
    strand = gene[3]
    
    txnStart = gene[4]
    
    txnEnd = gene[5]
    
    rgb = '0,0,0'
    
    exonCount = gene[8]
    
    exonSizes = ''
    
    exonStart = gene[9]
    
    exonSt =  gene[9].split(',')
    exonE = gene[10].split(',')
    for x in range(int(exonCount)):
        exonSize = int(exonE[x]) - int(exonSt[x])
        exonSizes+= str(exonSize) + ','
        
            
    
    Exons = ''
    for x in range(int(exonCount)):
        
        exonBedEntry  = chrom + '\t' +  exonSt[x] + '\t' + exonE[x] + '\t' + name + '\t'+ score + '\t' + strand +  '\n' 
        Exons+=exonBedEntry                 
        
    
    return Exons


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

    
    ExonBed(file)
   
if __name__ == '__main__':
    main() 