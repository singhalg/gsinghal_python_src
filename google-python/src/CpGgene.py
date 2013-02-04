'''
Created on May 18, 2010

@author: Gaurav

This is a recursive implementation of Binary search. It finds the appropriate CpG island for a gene, given a list of CpG islands and Genes with their coordinates. 

'''

from genData import CpGdata
from hgRef import genedata
import sys




def CpGMap(file1, file2):
    CpG = CpGdata(file1) # CpG = a list of lists. Each item of this list represents one chromosome and is a list of tuples, each tuple contains a CpG island.
                         # The elements of tuples are the start and end coordinates of the CpG island, and CpG island number
    gene = genedata(file2)
    print 'length of gene is ', len(gene)
    print 'length of CpG is ', len(CpG)
                        #gene = a list of lists. Each item of this list represents one chromosome, and is a list of tuples, each tuple contains 4 elements, each tuple contains info about a particular gene.
                         # The elements of tuples are the txn start and txn end coordinates of the gene, and gene names
   # chrCpG = 1
    print 'an element of CpG list looks like', CpG[1][1]
    print 'an element of gene list looks like', gene[1][1]
    print 'no of genes in chr1 is  ', len(gene[0])
    print 'no of CpG islands in chr1 is ', len(CpG[0])
    print 'no of genes in chr2 is  ', len(gene[1])
    print 'no of CpG islands in chr2 is ', len(CpG[1])
    print 'no of genes in chrY is  ', len(gene[23])
    print 'no of CpG islands in chrY is ', len(CpG[23])
    print gene[1][1][0]
    print CpG[1][1][0]
    print 'distance between gene and CpG' , gene[1][1][0] - CpG[1][1][0]
    chr1 = []
    chr2 = []
    chr3 = []
    chr4 = []
    chr5 = []
    chr6 = []
    chr7 = []
    chr8 = []
    chr9 = []
    chr10 = []
    chr11 = []
    chr12 = []
    chr13 = []
    chr14 = []
    chr15 = []
    chr16 = []
    chr17 = []
    chr18 = []
    chr19 = []
    chr20 = []
    chr21 = []
    chr22 = []
    chrX = []
    chrY = []
    
    
    #for j in range(len(gene)): # for each chr in the whole gene list
        
    j = 0
    i = 0
    genrange = len(gene[0])   # no of genes in chr 1
    
    
    while i < genrange:
        #mid = (min+max)/2
        min = 0
        max = len(CpG[0])-1
    # for each gene throughout the length of chr
        while min <= max :
            mid = (min + max)/2
            if (gene[j][i][0] - CpG[j][mid][0])<2500 and (gene[j][i][0] - CpG[j][mid][0])>0:
                print 'found match', gene[j][i][2], gene[j][i][3], gene[j][i][0], gene[j][i][1], CpG[j][mid][0], CpG[j][mid][1], CpG[j][mid][2]
                list = [gene[j][i][2], gene[j][i][3], gene[j][i][0], gene[j][i][1], CpG[j][mid][0], CpG[j][mid][1], CpG[j][mid][2]]
                
                #if j == 0:
                chr1.extend(list)
                i = i+1
                print 'moving on to the next gene'
                #print chr1
#                elif j == 1:
#                    chr2.append(list)
#                elif j == 2:
#                    chr3.append(list)
#                elif j == 3:
#                    chr4.append(list)
#                elif j == 4:
#                    chr5.append(list)
#                elif j == 5:
#                    chr6.append(list)
#                elif j == 6:
#                    chr7.append(list)
#                elif j == 7:
#                    chr8.append(list)
#                elif j == 8:
#                    chr9.append(list)
#                elif j == 9:
#                    chr10.append(list)
#                elif j == 10:
#                    chr11.append(list)
#                elif j == 11:
#                    chr12.append(list)
#                elif j == 12:
#                    chr13.append(list)
#                elif j == 13:
#                    chr14.append(list)
#                elif j == 14:
#                    chr15.append(list)
#                elif j == 15:
#                    chr16.append(list)
#                elif j == 16:
#                    chr17.append(list)
#                elif j == 17:
#                    chr18.append(list)
#                elif j == 18:
#                    chr19.append(list)
#                elif j == 19:
#                    chr20.append(list)
#                elif j == 20:
#                    chr21.append(list)
#                elif j == 21:
#                    chr22.append(list)
#                elif j == 22:
#                    chrX.append(list)
#                elif j == 23:
#                    chrY.append(list)
#                        
                        
                            
            elif (gene[j][i][0] - CpG[j][mid][0])< 0:
                max = mid-1
                #print  gene[j][i][0], ' - ', CpG[j][mid][0],'< 0 '
                #print 'not found'
            else: # if (gene[j][i][0] - CpG[j][mid][0])>2500 0:
                min = mid+1
                #print 'still not found'
                #print gene[j][i][0], ' - ', CpG[j][mid][0],'> 2500 '
        
        
    
    CpGmap = [chr1, chr2, chr3, chr4, chr5, chr6, chr7, chr8, chr9, chr10, chr11, chr12, chr13, chr14, chr15, chr16, chr17, chr18, chr19, chr20,chr21, chr22, chrX, chrY]
    
#    for match in chr1:
#        print match
    
    #return CpGmap
    return chr1
    
    #for chr in genelist:
    #for gene in chr:
            #do binary search for gene on CpG[chrCpG]
        # ...end of for
        #chrCpG = chrCpG + 1 #chromosome on CpG
        
#def bnSrch(gene, CpG):
#    min = CpG[0][0][0]
#while min<=max
#if (genestrt - CpGstrt[mid])<2500 and (genestrt - CpGstrt[mid])>0
# make a new list item in chr# [gene name, gene coordinates, cpg name, cpg coordinates, chr#]
#
#elif (genestrt - CpGstrt[mid]) <0
# min = mid+1
#else 
# max = mid-1
 
 


def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    CpGMap(file1, file2)   
 



if __name__ == '__main__':
    main()








