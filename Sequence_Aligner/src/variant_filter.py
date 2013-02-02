#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     12/06/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, os
from sets import Set




def variant_filter(exonBed, allSNP, allIndel):


    txnIntervals = [] # list of transcription start and stop sites
    genes = Set([])
    fhExonBed = open(exonBed, 'rU')
    exons = fhExonBed.readlines()
    fhExonBed.close()
    for line in exons:
        flds  = line.split('\t')
        if flds[0].strip()=='chr20':
            gene = flds[3].strip()
            if gene not in genes:
                txnIntervals.append([int(flds[6].strip()), int(flds[7].strip())])
                genes.add(gene)

    print '# genes  = ', len(txnIntervals)

    sortedTxnInt = sorted(txnIntervals)
    print sortedTxnInt[:20]

    # now doing exons

    exonIntervals = []
    for line in exons:
        flds  = line.split('\t')
        if flds[0].strip()=='chr20':
            exonIntervals.append([int(flds[1].strip()), int(flds[2].strip())])


    print '# of exon intervals = ', len(exonIntervals)
    sortedExons = sorted(exonIntervals)
    print sortedExons[:20]

    # now filtering SNPs


    fhAllsnp  = open(allSNP, 'rU')
    allSNP = fhAllsnp.readlines()
    fhAllsnp.close()

    # first filtering SNPs by txn start and txn end
    txnSNP = open('chr20_mutPIRS_snp_txn.lst', 'w')
    OutOfTxnSNP = open('chr20_mutPIRS_SNP_outoftxn.lst', 'w')

    for each in allSNP:
        flds = each.split('\t')
        loc = int(flds[1].strip())
        inTxn = False
        for agene in sortedTxnInt:
            if ((loc>=agene[0]) and (loc<=agene[1])):

                inTxn = True
        if inTxn == True:
            txnSNP.write(each)
        else:
            OutOfTxnSNP.write(each)

    txnSNP.close()
    OutOfTxnSNP.close()

    #now filtering SNPs by exon start and exon stop

    exonSNP = open('chr20_mutPIRS_SNP_Exon.lst', 'w')
##    outOfExon =open('chr20_mutPIRS_SNP_OutofExon.lst', 'w')

    for each in allSNP:
        flds = each.split('\t')
        loc = int(flds[1].strip())
        inExon = False
        for anExon in sortedExons:
            if ((loc>=anExon[0]) and (loc<=anExon[1])):
                inExon = True
        if inExon == True:
            exonSNP.write(each)

    exonSNP.close()







def sortFun(lst):
    lst[0]






def main():
    exonBed = sys.argv[1]
    allSNP = sys.argv[2]
    allIndel = sys.argv[3]
    variant_filter(exonBed,allSNP, allIndel )

if __name__ == '__main__':
    main()
