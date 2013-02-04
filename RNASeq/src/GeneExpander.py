'''
Created on Mar 8, 2011

@author: Gaurav
'''

#-------------------------------------------------------------------#
# Author: Gaurav Singhal                                            #
# Created : March 08, 2011                                          #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#


'''
This script converts the refSeq gene list into bed format and expands the txn start and txn end
boundary by 1kb, 2kb or 5 kb etc. The method geneExpanded(file, expanse) takes 2 arguments, file is the refGene.txt file and 
expanse is the number of bases by which you want the genes txn start and end sites to get expanded. 
It converts only those genes for which the cdsStartStat, cdsEndStat are "cmpl".  
'''


import sys




def geneExpanded(file, expanse, strand):
    
    expansion = int(expanse)
    
    if expansion == 0 and strand == 'plus':
        outTag = 'refGeneOnlyPlus.bed'
    elif expansion == 0 and strand == 'minus':
        outTag = 'refGeneOnlyMinus.bed'
    
    elif strand == 'plus':
        if  (expansion == 1000):
            outTag = 'refGenePlus1kb.bed'
        elif (expansion == 2000):
            outTag = 'refGenePlus2kb.bed'
        elif expansion == 5000:
            outTag = 'refGenePlus5kb.bed'
        elif expansion == 10000:
            outTag = 'refGenePlus10kb.bed'
        else :outTag= 'refGenePlus' + str(expanse)+ 'Bases.bed'
            
    elif strand == 'minus':
        if  expansion == 1000:
            outTag = 'refGeneMinus1kb.bed'
        elif expansion == 2000:
            outTag = 'refGeneMinus2kb.bed'
        elif expansion == 5000:
            outTag = 'refGeneMinus5kb.bed'
        elif expansion == 10000:
            outTag = 'refGeneMinus10kb.bed'
        else:
            outTag = 'refGeneMinus' + str(expanse)+ 'Bases.bed'     
    
    
    output = open(outTag, 'w')
    
    
    
    Genes = refGeneParser(file)
    cmplGenes = []
    plusGenes = []
    minusGenes = []

    for each in Genes:
        if each[13] == 'cmpl':
            if each[14] == 'cmpl':
                cmplGenes.append(each)
                if each[3] == '+':
                    plusGenes.append(each)
                if each[3] == '-':
                    minusGenes.append(each)
                    
    
    if expansion == 0 and strand == 'plus':
        for gene in plusGenes:
            output.write(makeBed(gene))
    elif expansion == 0 and strand == 'minus':
        for gene in minusGenes:
            output.write(makeBed(gene))
    elif expansion > 0:
        if strand == 'plus':    
            for gene in plusGenes:
                output.write(makeBedPlus(gene, expansion))
        if strand == 'minus':
            for gene in minusGenes:
                output.write(makeBedMinus(gene, expansion)) 




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

def makeBed(gene):
    
    bedForm = gene[2] + '\t' + gene[4] + '\t' + gene[5] + '\t' + gene[12] + '\t' + gene[8] + '\t' + gene[3] + '\n'
    
    return bedForm


def makeBedPlus(gene, expansion ):
    
    txnStart =  int(gene[4])-expansion
    if txnStart <0:
        txnStart = 0
    
    bedForm = gene[2] + '\t' + str(txnStart) + '\t' + gene[4] + '\t' + gene[12] + '\t' + gene[8] + '\t' + gene[3] + '\n'

    return bedForm

def makeBedMinus(gene, expansion):
    
    
    bedForm = gene[2] + '\t' + gene[5] + '\t' + str(int(gene[5])+expansion) + '\t' + gene[12] + '\t' + gene[8] + '\t' + gene[3] + '\n'

    return bedForm
    



def refGeneParser(refGene):
    genefile = open(refGene, 'rU')
    Genes = []
    for each in genefile:
        Genes.append(geneParser(each))
    
    genefile.close()
    return Genes
    

    


def main():
    
    file = sys.argv[1]
    expanse = sys.argv[2]
    strand = sys.argv[3]
    
    geneExpanded(file, expanse, strand)
   
if __name__ == '__main__':
    main() 

