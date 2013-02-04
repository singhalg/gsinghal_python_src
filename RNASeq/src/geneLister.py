'''
Created on Apr 13, 2011

@author: Gaurav

#-------------------------------------------------------------------#
# @copyright:  2011 Gaurav Singhal                                  #
# All Rights Reserved.                                              #
# Author: Gaurav Singhal                                            #
# Created : April 12, 2011                                          #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#



'''
import sys
from sets import Set
from decimal import Decimal

def geneLister(sorted_coverage):
    
    inFile = open(sorted_coverage)
    exons = inFile.readlines()

    genes = Set([])
    genes_sorted  = []

    for line in exons:
        
        aGene = organise(line)
        
        if aGene not in genes:
            genes.add(aGene)
            genes_sorted.append(aGene)
        
    
    print '# of exons entries  = ', len(exons)
    print '# of gene represented by exons = ', len(genes)


    genesList = open('genesList', 'w')
    for eachGene in genes_sorted:
        genesList.write(eachGene + '\n')
        

    genesList.close()


def cancerGeneListCompare(file1, file2, cancerGeneList):
    genes = open(cancerGeneList, 'rU')
    cancerGenes = Set([])
    genesList = genes.readlines()
    for each in genesList:
        cancerGenes.add(each.strip())
        
    
    
    print ' line count of cancer gene file = ', len(genesList)
    print '# of genes in cancer gene file = ', len(cancerGenes)
    
    intersectGenesOver10per, intersectGenesOver30per, intersectGenesOver40per, intersectGenesOver50per = geneListCompare(file1, file2)
    
    cancerAndGenes50 = intersectGenesOver50per & cancerGenes
    cancerAndGenes40 = intersectGenesOver40per & cancerGenes
    cancerAndGenes30 = intersectGenesOver30per & cancerGenes
    cancerAndGenes10 = intersectGenesOver10per & cancerGenes
    
    print '# of genes with score >= 0.1 common among the cancer list and genes lists is :', len(cancerAndGenes10)
    print '# of genes with score >= 0.3 common among the cancer list and genes lists is :', len(cancerAndGenes30)
    print '# of genes with score >= 0.4 common among the cancer list and genes lists is :', len(cancerAndGenes40)
    print '# of genes with score >= 0.5 common among the cancer list and genes lists is :', len(cancerAndGenes50)

def cancerGeneListCompareBRC(file1, file2, cancerGeneList):
    genes = open(cancerGeneList, 'rU')
    cancerGenes = Set([])
    genesList = genes.readlines()
    
    cancerGenes.add(genesList[8].strip())
    cancerGenes.add(genesList[24].strip())
    cancerGenes.add(genesList[40].strip())
    cancerGenes.add(genesList[41].strip())
    cancerGenes.add(genesList[44].strip())
    cancerGenes.add(genesList[61].strip())
    cancerGenes.add(genesList[69].strip())
    cancerGenes.add(genesList[80].strip())
    cancerGenes.add(genesList[119].strip())
    cancerGenes.add(genesList[121].strip())
    cancerGenes.add(genesList[130].strip())
    cancerGenes.add(genesList[167].strip())
    cancerGenes.add(genesList[242].strip())
    cancerGenes.add(genesList[303].strip())
    cancerGenes.add(genesList[312].strip())
    cancerGenes.add(genesList[317].strip())
    cancerGenes.add(genesList[328].strip())
    cancerGenes.add(genesList[358].strip())
    cancerGenes.add(genesList[424].strip())

    
    print ' line count of cancer gene file = ', len(genesList)
    print '# of genes in cancer gene file = ', len(cancerGenes)
    
    intersectGenesOver10per, intersectGenesOver30per, intersectGenesOver40per, intersectGenesOver50per = geneListCompare(file1, file2)
    
    cancerAndGenes50 = intersectGenesOver50per & cancerGenes
    cancerAndGenes40 = intersectGenesOver40per & cancerGenes
    cancerAndGenes30 = intersectGenesOver30per & cancerGenes
    cancerAndGenes10 = intersectGenesOver10per & cancerGenes
    
    

    
    
    print '# of genes with score >= 0.1 common among the cancer list and genes lists is :', len(cancerAndGenes10)
    print '# of genes with score >= 0.3 common among the cancer list and genes lists is :', len(cancerAndGenes30)
    print '# of genes with score >= 0.4 common among the cancer list and genes lists is :', len(cancerAndGenes40)
    print '# of genes with score >= 0.5 common among the cancer list and genes lists is :', len(cancerAndGenes50)

    for eachGene in cancerGenes:
        
        print eachGene


def geneListCompare(file1, file2):
    
    file1GenesOver10per, file1GenesOver30per, file1GenesOver40per, file1GenesOver50per = coveredExons(file1)
    
    file2GenesOver10per, file2GenesOver30per, file2GenesOver40per, file2GenesOver50per = coveredExons(file2)
    
    intersectGenesOver10per = file1GenesOver10per & file2GenesOver10per
    intersectGenesOver30per = file1GenesOver30per & file2GenesOver30per
    intersectGenesOver40per = file1GenesOver40per & file2GenesOver40per
    intersectGenesOver50per = file1GenesOver50per & file2GenesOver50per
    
    totalGenesOver10per = file1GenesOver10per | file2GenesOver10per
    totalGenesOver30per = file1GenesOver30per | file2GenesOver30per
    totalGenesOver40per = file1GenesOver40per | file2GenesOver40per
    totalGenesOver50per = file1GenesOver50per | file2GenesOver50per
    
    uncommonGenesOver10per = (file1GenesOver10per - file2GenesOver10per) | (file2GenesOver10per - file1GenesOver10per) 
    uncommonGenesOver30per = (file1GenesOver30per - file2GenesOver30per) | (file2GenesOver30per - file1GenesOver30per) 
    uncommonGenesOver40per = (file1GenesOver40per - file2GenesOver40per) | (file2GenesOver40per - file1GenesOver40per) 
    uncommonGenesOver50per = (file1GenesOver50per - file2GenesOver50per) | (file2GenesOver50per - file1GenesOver50per) 
    
    
    print '# of genes with score >= 0.1 common among the two sets are :', len(intersectGenesOver10per)
    print '# of genes with score >= 0.3 common among the two sets are :', len(intersectGenesOver30per)
    print '# of genes with score >= 0.4 common among the two sets are :', len(intersectGenesOver40per)
    print '# of genes with score >= 0.5 common among the two sets are :', len(intersectGenesOver50per)
    
    
    
    print '# of genes with score >= 0.1 UNcommon among the two sets are :', len(uncommonGenesOver10per)
    print '# of genes with score >= 0.3 UNcommon among the two sets are :', len(uncommonGenesOver30per)
    print '# of genes with score >= 0.4 UNcommon among the two sets are :', len(uncommonGenesOver40per)
    print '# of genes with score >= 0.5 UNcommon among the two sets are :', len(uncommonGenesOver50per)
    
    
    print 'Total # of genes with score >= 0.1 in both of the sets are :', len(totalGenesOver10per)
    print 'Total # of genes with score >= 0.3 in both of the sets are :', len(totalGenesOver30per)
    print 'Total # of genes with score >= 0.4 in both of the sets are :', len(totalGenesOver40per)
    print 'Total # of genes with score >= 0.5 in both of the  sets are :', len(totalGenesOver50per)
    
    
    return intersectGenesOver10per, intersectGenesOver30per, intersectGenesOver40per, intersectGenesOver50per
#    return totalGenesOver10per,     totalGenesOver30per,     totalGenesOver40per,     totalGenesOver50per
    
    

def coveredExons(sorted_coverage):
    inFile = open(sorted_coverage)
    exons = inFile.readlines()
    
    
    above10per = []
    above30per = []
    above40per = []
    above50per = []
    
    over10per = sorted_coverage[:-4]+'_over10per.bed'
    over30per = sorted_coverage[:-4]+'_over30per.bed'
    over40per = sorted_coverage[:-4]+'_over40per.bed'
    over50per = sorted_coverage[:-4]+'_over50per.bed'
    
    genesOver10per = Set([])
    genesOver30per = Set([])
    genesOver40per = Set([])
    genesOver50per = Set([])
   
    
    for line in exons :
        score = returnCoverageScore(line)
        gene = returnGeneName(line)
    
        if score >= 0.5:
            above50per.append(line)
            genesOver50per.add(gene)
        
        if score >= 0.4:
            above40per.append(line)
            genesOver40per.add(gene)
            
        if score >= 0.3:
            above30per.append(line)
            genesOver30per.add(gene)
            
        if score >= 0.1:
            above10per.append(line)
            genesOver10per.add(gene)
    
            
#    outfile1 = open(over10per, 'w')
#    outfile1.writelines(above10per)
#    outfile1.close()
#    
#    outfile2 = open(over30per, 'w')
#    outfile2.writelines(above30per)
#    outfile2.close()
#    
#    
#    outfile3 = open(over50per, 'w')
#    outfile3.writelines(above50per)
#    outfile3.close()
    
    return genesOver10per, genesOver30per, genesOver40per, genesOver50per
            

def returnCoverageScore(line):
    cols = line.split('\t')
    return float(cols[-1].strip())


def returnGeneName(line):
    cols = line.split('\t')
    return cols[3].strip()

   
def organise(string):
    cols = string.split('\t')
    return cols[3].strip()
    

def main ():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    cancerGeneList = sys.argv[3]
#    geneLister(file)
#    coveredExons(file)
    cancerGeneListCompareBRC(file1, file2, cancerGeneList)
    
if __name__ == '__main__':
    main()