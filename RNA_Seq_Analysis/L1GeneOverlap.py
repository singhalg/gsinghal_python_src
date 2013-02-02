'''
Created on Mar 2, 2011

@author: Gaurav
'''


#-------------------------------------------------------------------#
# Author: Gaurav Singhal                                            #
# Created : Feb 15, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#




import sys, re, os


def L1GeneIntersectBed():
    
    plusGenes = ['refGeneOnly.bed','refGenePlus1kb.bed', 'refGenePlus2kb.bed', 'refGenePlus5kb.bed', 'refGenePlus10kb.bed']
    minusGenes = ['refGeneOnly.bed','refGeneMinus1kb.bed','refGeneMinus2kb.bed','refGeneMinus5kb.bed','refGeneMinus10kb.bed']
    
    spasp = ['SP', 'ASP']
    orient = ['53', '35']
    pm = ['p', 'm']
    
#    L1s = []
#    for sp in spasp:
#        for dir in orient:
#            for strand in pm:
#                file = 'L1'+ sp + dir + strand + '.bed'
#                L1s.append(file)
                
    
#    print L1s
    plusL1s = ['L1SP53p.bed', 'L1SP35m.bed', 'L1ASP53m.bed', 'L1ASP35p.bed']
    minusL1s = ['L1SP53m.bed', 'L1SP35p.bed', 'L1ASP53p.bed', 'L1ASP35m.bed']
    
    commands = []
    
    output = []
    
    for L1 in plusL1s:
        for geneList in plusGenes:
            cmd = 'nohup intersectBed -a ' + L1 + '  -b ' + geneList + '  -wa -wb > ' + 'Overlap'+L1[:-4]+geneList[11:] + ' &'
            overlapOut = 'Overlap'+L1[:-4]+geneList[11:] 
            output.append(overlapOut)
            commands.append(cmd)
    
    for L1 in minusL1s:
        for geneList in minusGenes:
            cmd = 'nohup intersectBed -a ' + L1 + '  -b ' + geneList + '  -wa -wb > ' + 'Overlap'+L1[:-4]+geneList[12:] + '  &'
            overlapOut = 'Overlap'+L1[:-4]+geneList[12:] 
            output.append(overlapOut)
            commands.append(cmd)
            
    for cmd in commands:
        os.system(cmd)
        print cmd
    
    for eachFile in output:
        print eachFile

    
    
    
    
    
    
    genesOnlyLines = []
    genes1kbLines = []
    genes2kbLines = []
    genes5kbLines = []
    genes10kbLines = []
    
    for overlapFile in output:
        if re.search('kb', overlapFile):
            if re.search('1kb', overlapFile):
                 print 'found 1 kb file : ' , overlapFile
                 overlap = open(overlapFile, 'r')
                 data = overlap.readlines()
                 overlap.close()
                 del overlap
                 genes1kbLines+= data
                 del data
            elif re.search('2kb', overlapFile):
                 print 'found 2 kb file : ' , overlapFile
                 overlap = open(overlapFile, 'r')
                 data = overlap.readlines()
                 overlap.close()
                 del overlap
                 genes2kbLines+= data
                 del data
            elif re.search('5kb', overlapFile):
                 print 'found 5 kb file : ' , overlapFile
                 overlap = open(overlapFile, 'r')
                 data = overlap.readlines()
                 overlap.close()
                 del overlap
                 genes5kbLines+= data
                 del data
            elif re.search('10kb', overlapFile):
                 print 'found 10 kb file : ' , overlapFile
                 overlap = open(overlapFile, 'r')
                 data = overlap.readlines()
                 overlap.close()
                 del overlap
                 genes10kbLines+=data
                 del data
            else : print 'file does not match description : ', overlapFile
        else :
            print 'found genes only : ', overlapFile
            overlap = open(overlapFile, 'r')
            data = overlap.readlines()
            overlap.close()
            del overlap
            genesOnlyLines +=data
            del data
    
    genesOnly =  open('genesOnly.bed', 'w')
    genes1kb = open('genes1kb.bed', 'w')
    genes2kb = open('genes2kb.bed', 'w')
    genes5kb = open('genes5kb.bed', 'w')
    genes10kb = open('genes10kb.bed','w' )
    
    
    print 'now printing genesOnlyLines' 
    
    for each in genes5kbLines:
        print each
    
    genesOnly.writelines(genesOnlyLines)    
    genesOnly.close()
    genes1kb.writelines(genes1kbLines)
    genes1kb.close()
    genes2kb.writelines(genes2kbLines)
    genes2kb.close()
    genes5kb.writelines(genes5kbLines)
    genes5kb.close()
    genes10kb.writelines(genes10kbLines)
    genes10kb.close()
            
    
#    command = 'intersectBed -a L1Promoter_RMOUT.bed -b refGene10kb.bed -wa -wb > OverlapL1Promoter_refGene10kb.bed &'
#    
#    os.system(intersect)
    

def L1GeneOverlap(L1Promoters):
    
    L1inGenes = []
    L1Genes1k = []
    L1Genes2k = []
    L1Genes5k = []
    L1Genes10k = []
    
    L1Filtered = open(L1Promoters, 'rU')
    
    L1s = []
    for line in L1Filtered:
        L1instance = repeatParser(line)
        L1s.append(L1instance)

    
    
    genefile = open('refGene.txt', 'rU')
    Genes = []
    for each in geneFile:
        Genes.append(geneParser(each))
    
    
    plusGenes = []
    minusGenes = []
    for each in Genes:
        if each[13] == 'cmpl':
            if each[14] == 'cmpl':
                if each[3] == '+':
                    plusGenes.append(each)
                else:
                    minusGenes.append(each)
    
            
    
    for L1 in L1s:
        if L1[0] == 'L1SP53':
            for gene in plusGenes:
                dist = gene[4] - int(L1[8])
                if dist <= 1000 and dist > 0:
                    L1GenePair = []
                    
                    for entryofL1 in L1:
                        L1GenePair.append(entryofL1)
                    for entryofGene in gene[1:6]:
                        L1GenePair.append(entryofGene)
                    L1GenePair.append(gene[12])    
                    
                    L1Genes1k.append(L1GenePair)
                    L1Genes2k.append(L1GenePair)
                    L1Genes5k.append(L1GenePair)
                    L1Genes10k.append(L1GenePair)
                
                elif dist <= 2000 and dist > 0:
                    L1GenePair = []
                    
                    for entryofL1 in L1:
                        L1GenePair.append(entryofL1)
                    for entryofGene in gene[1:6]:
                        L1GenePair.append(entryofGene)
                    L1GenePair.append(gene[12])
                    
                    L1Genes2k.append(L1GenePair)
                    L1Genes5k.append(L1GenePair)
                    L1Genes10k.append(L1GenePair)
                elif dist <= 5000 and dist > 0:
                    L1GenePair = []
                    
                    for entryofL1 in L1:
                        L1GenePair.append(entryofL1)
                    for entryofGene in gene[1:6]:
                        L1GenePair.append(entryofGene)
                    L1GenePair.append(gene[12])
                    
                    
                    L1Genes5k.append(L1GenePair)
                    L1Genes10k.append(L1GenePair)
                
                elif dist <= 10000 and dist > 0:
                    L1GenePair = []
                    
                    for entryofL1 in L1:
                        L1GenePair.append(entryofL1)
                    for entryofGene in gene[1:6]:
                        L1GenePair.append(entryofGene)
                    L1GenePair.append(gene[12])
                    
                    L1Genes10k.append(L1GenePair)
                
                elif dist < 0:
                    if (gene[5] - int(L1[8])) > 0 and (gene[5] - int(L1[7])) > 0:
                        L1GenePair = []
                    
                        for entryofL1 in L1:
                            L1GenePair.append(entryofL1)
                        for entryofGene in gene[1:6]:
                            L1GenePair.append(entryofGene)
                        L1GenePair.append(gene[12])
                        L1inGenes.append(L1GenePair)
         
         
         #==================#               
        if L1[0] == 'L1SP35':
            for gene in minusGenes:
                dist = int(L1[7]) - gene[5] # promoter start - gene end
                if dist <= 1000 and dist > 0:
                    L1GenePair = []
                    
                    for entryofL1 in L1:
                        L1GenePair.append(entryofL1)
                    for entryofGene in gene[1:6]:
                        L1GenePair.append(entryofGene)
                    L1GenePair.append(gene[12])    
                    
                    L1Genes1k.append(L1GenePair)
                    L1Genes2k.append(L1GenePair)
                    L1Genes5k.append(L1GenePair)
                    L1Genes10k.append(L1GenePair)
                
                elif dist <= 2000 and dist > 0:
                    L1GenePair = []
                    
                    for entryofL1 in L1:
                        L1GenePair.append(entryofL1)
                    for entryofGene in gene[1:6]:
                        L1GenePair.append(entryofGene)
                    L1GenePair.append(gene[12])
                    
                    L1Genes2k.append(L1GenePair)
                    L1Genes5k.append(L1GenePair)
                    L1Genes10k.append(L1GenePair)
                elif dist <= 5000 and dist > 0:
                    L1GenePair = []
                    
                    for entryofL1 in L1:
                        L1GenePair.append(entryofL1)
                    for entryofGene in gene[1:6]:
                        L1GenePair.append(entryofGene)
                    L1GenePair.append(gene[12])
                    
                    
                    L1Genes5k.append(L1GenePair)
                    L1Genes10k.append(L1GenePair)
                
                elif dist <= 10000 and dist > 0:
                    L1GenePair = []
                    
                    for entryofL1 in L1:
                        L1GenePair.append(entryofL1)
                    for entryofGene in gene[1:6]:
                        L1GenePair.append(entryofGene)
                    L1GenePair.append(gene[12])
                    
                    L1Genes10k.append(L1GenePair)
                
                elif dist < 0:
                    if (gene[5] - int(L1[8])) > 0 and (gene[5] - int(L1[7])) > 0:
                        L1GenePair = []
                    
                        for entryofL1 in L1:
                            L1GenePair.append(entryofL1)
                        for entryofGene in gene[1:6]:
                            L1GenePair.append(entryofGene)
                        L1GenePair.append(gene[12])
                        L1inGenes.append(L1GenePair)
   
    
def repeatParser(line):
    
    splitline = line.split()
    
    
    listOfEntries = [word.strip() for word in splitline]
    
    return listOfEntries
    
    
    
    
def geneParser(line):
    splitline = line.split()
    
    
    listOfEntries = [word.strip() for word in splitline]
    
    gene = []
    
    bin = listOfEntries[0]
    gene.append(bin)
    
    nameGtf = listOfEntries[1]
    gene.append(nameGtf)
    
    chr = listOfEntries[2]
    gene.append(chr)
    
    strand= listOfEntries[3]
    gene.append(strand)
    
    txStart = int(listOfEntries[4])
    gene.append(txStart)
    
    txEnd = int(listOfEntries[5])
    gene.append(txEnd)
    
    cdStart = int(listOfEntries[6])
    gene.append(cdStart)
    
    cdEnd = int(listOfEntries[7])
    gene.append(cdEnd)
    
    exonCount = int(listOfEntries[8])
    gene.append(exonCount)
    
    exonStrt = listOfEntries[9]
    gene.append(exonStrt)
    
    exonEnd = listOfEntries[10]
    gene.append(exonEnd)
    
    id = listOfEntries[11]
    gene.append(id)
    
    name = listOfEntries[12]
    gene.append(name)
    
    cdsStat = listOfEntries[13]
    gene.append(cdsStat)
    
    cdsEndStat = listOfEntries[14]
    gene.append(cdsEndStat)
    
    exonFrames = listOfEntries[15]
    gene.append(exonFrames)
    
    return gene
    
def fastaIdExtractor():
    filetags = ['aa', 'ab','ac','ad','ae', 'af', 'ag', 'ah','ai','aj']
    orientTags = ['53', '35']
    orient = ['SP', 'ASP']
    filenames = []
    for SPASP in orient:
        for numTags in orientTags:
            for tag in filetags:
                aFileName = 'L1'+SPASP+numTags+tag+'_Out.fa'
                filenames.append(aFileName)
    
    
    for eachFile in filenames:
        print eachFile
    
    
    rmOut = open('L1Promoter_RMOUT.out', 'w')
    
    for name in filenames:
        filein = open(name, 'rU')
        
        JalignOut = filein.readlines()
        
        filein.close()
        
        for line in JalignOut:
            if line[0] == '>':
                parsedRMout = name[:-9]+ '\t' +  line[1:].replace('#', '\t')
                rmOut.write(parsedRMout)
        print 'Done ', name
               
#    name = 'L1ASP35aa_Out.fa'
#    filein = open(name, 'rU')
#        
#    JalignOut = filein.readlines()
#        
#    filein.close()
#        
#    for line in JalignOut:
#        if line[0]== '>':
#            parsedRMout = name[:-9]+ '\t' +  line[1:].replace('#', '\t')
#            rmOut.write(parsedRMout)
    rmOut.close()
        


def refGeneParser(file):
    
    refGenes = open(file, 'rU')
    
    for line in refGenes:
        sline = line.split()
        
        
    
    
def main():
#    fastaIdExtractor()
    L1GeneIntersectBed()
    
if __name__ == '__main__':
    main()