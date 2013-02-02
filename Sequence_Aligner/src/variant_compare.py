#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     06/06/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, os
from sets import Set


def variantCompare(original, detected):
    fh1 = open(original, 'rU')
    varList1 = fh1.readlines()
    fh1.close()

    originalVariants = {}
    originalVarSet = Set([])

    fh2 = open(detected, 'rU')
    varList2 = fh2.readlines()
    fh2.close()

    detectedVariants = {}
    detectedVarSet = Set([])

    for each in varList1:
        flds = each.strip().split('\t')
        originalVarSet.add(int(flds[1]))
        val = [flds[2], flds[3]]
        originalVariants[int(flds[1])] = val

    for each in varList2:
        flds = each.strip().split('\t')
        if flds[0].strip()=='chr20':
            detectedVarSet.add(int(flds[1]))
            val = [flds[3], flds[4]]
            detectedVariants[int(flds[1])] = val

    list1 = sorted(list(originalVarSet))

    list2 = sorted(list(detectedVarSet))

##    print 'Printing original variants ...'
##    for each in list1[:10]:
##        print each
##        print originalVariants[each]
##    print '\n'
##    print 'Now printing detected variants ...'
##    for each in list2[:10]:
##        print each
##        print detectedVariants[each]

    print '# of original variants = ', len(originalVarSet)

    tp = originalVarSet.intersection(detectedVarSet)  # set of true positives

    truePositives = {}      # dictionary of true positives
    for each in tp:
        if originalVariants[each] == detectedVariants[each]:
            val = originalVariants[each]
            truePositives[each] = val


    print '# of variants detected = ', len(tp)
    tpKeys = truePositives.keys()
    print '# of variants accurately detected (true positives) = ', len(tpKeys)
    print len(tpKeys)
    print float(len(originalVarSet))
    recall = (float(len(tpKeys))/float(len(originalVarSet)))*100.0
    print float(len(detectedVarSet))
    precision = (float(len(tpKeys))/ float(len(detectedVarSet)))*100.0

    print 'recall rate = ', recall
    print 'precision rate = ', precision
    return precision, recall

def coverageCompare():

    fhoutAll = open('simResults_allSNP.csv', 'w')
    fhoutExon = open('simResults_exonSNP.csv', 'w')
    fhoutTxn  = open('simResults_txnSNP.csv', 'w')
    fhoutOutTxn = open('simResults_outsideTxnSNP.csv', 'w')



##    var.flt100.vcf  var.flt112.vcf  var.flt12.vcf  var.flt24.vcf  var.flt36.vcf  var.flt48.vcf  var.flt60.vcf  var.flt76.vcf  var.flt96.vcf
##    var.flt104.vcf  var.flt116.vcf  var.flt16.vcf  var.flt28.vcf  var.flt40.vcf  var.flt4.vcf   var.flt64.vcf  var.flt8.vcf
##    var.flt108.vcf  var.flt120.vcf  var.flt20.vcf  var.flt32.vcf  var.flt44.vcf  var.flt52.vcf  var.flt68.vcf  var.flt92.vcf
    original = 'chr20_mutPIRS_snp.lst'

    detected = 'var.flt4.vcf'

##    st = detected.find('t') +1
##    end = detected.find('.vc')
##    cov = detected[st:end]
##    precision, recall = variantCompare(original, detected)
##    outline = cov + ',' + precision + ',' + recall+'\n'

    fhoutAll.write(executer(original, detected))

    detected = 'var.flt8.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt12.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt16.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt20.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt24.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt28.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt32.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt36.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt40.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt44.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt48.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt52.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt60.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt64.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt68.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt76.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt92.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt96.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt100.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt104.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt108.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt112.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt116.vcf'
    fhoutAll.write(executer(original, detected))

    detected = 'var.flt120.vcf'
    fhoutAll.write(executer(original, detected))
##    detected = 'var.flt8.vcf'
##    st = detected.find('t') +1
##    end = detected.find('.vc')
##    cov = detected[st:end]
##    precision, recall = variantCompare(original, detected)
##    outline = cov + ',' + precision + ',' + recall+'\n'
##    fhoutAll.write()
    fhoutAll.close()
####################################################### now doing Exons
##
##    original = 'chr20_mutPIRS_SNP_Exon.lst'
##
##    detected = 'var.flt4.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt8.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt12.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt16.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt20.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt24.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt28.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt32.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt36.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt40.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt44.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt48.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt52.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt60.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt64.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt68.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt76.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt92.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt96.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt100.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt104.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt108.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt112.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt116.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    detected = 'var.flt120.vcf'
##    fhoutExon.write(executer(original, detected))
##
##    fhoutExon.close()
##
##
##
##
#################################### now doing txn
##
##    original = 'chr20_mutPIRS_snp_txn.lst'
##
##    detected = 'var.flt4.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt8.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt12.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt16.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt20.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt24.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt28.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt32.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt36.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt40.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt44.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt48.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt52.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt60.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt64.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt68.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt76.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt92.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt96.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt100.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt104.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt108.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt112.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt116.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    detected = 'var.flt120.vcf'
##    fhoutTxn.write(executer(original, detected))
##
##    fhoutTxn.close()
##
##
#################################### now doing OUT OF txn
##
##    original = 'chr20_mutPIRS_SNP_outoftxn.lst'
##
##    detected = 'var.flt4.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt8.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt12.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt16.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt20.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt24.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt28.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt32.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt36.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt40.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt44.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt48.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt52.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt60.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt64.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt68.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt76.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt92.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt96.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt100.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt104.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt108.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt112.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt116.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##    detected = 'var.flt120.vcf'
##    fhoutOutTxn.write(executer(original, detected))
##
##
##
##    fhoutOutTxn.close()


def executer(original, detected):
    st = detected.find('t') +1
    end = detected.find('.vc')
    cov = detected[st:end]
    prec, rec = variantCompareIndel(original, detected)
    outline = cov + ',' + str(prec) + ',' + str(rec)+'\n'
    print outline
    return outline



def variantCompareIndel(original, detected):
    fh1 = open(original, 'rU')
    varList1 = fh1.readlines()
    fh1.close()

    originalVariants = {}
    originalVarSet = Set([])

    fh2 = open(detected, 'rU')
    varList2 = fh2.readlines()
    fh2.close()

    detectedVariants = {}
    detectedVarSet = Set([])

    for each in varList1:
        flds = each.strip().split('\t')
        originalVarSet.add(int(flds[1]))
        val = [flds[2], flds[3]]
        originalVariants[int(flds[1])] = val

    for each in varList2:
        flds = each.strip().split('\t')
        if flds[0].strip()=='chr20':
            detectedVarSet.add(int(flds[1]))
            val = [flds[3], flds[4]]
            detectedVariants[int(flds[1])] = val

    list1 = sorted(list(originalVarSet))

    list2 = sorted(list(detectedVarSet))

##    print 'Printing original variants ...'
##    for each in list1[:10]:
##        print each
##        print originalVariants[each]
##    print '\n'
##    print 'Now printing detected variants ...'
##    for each in list2[:10]:
##        print each
##        print detectedVariants[each]

    print '# of original variants = ', len(originalVarSet)
    print '# of detected variants = ', len(detectedVarSet)
    fhoutND = open('notdetected.txt', 'w')
    undetected = []
    tp = originalVarSet.intersection(detectedVarSet)  # set of true positives
##    print '# possible true positives  =',len(tp)
    truePositives = {}      # dictionary of true positives

    leftOut = originalVarSet-tp

    for each in tp:
        called = False
        ref = originalVariants[each][0]
        refChange = originalVariants[each][1]
        altref = detectedVariants[each][0]
        altDet = detectedVariants[each][1]
        alts = altDet
        if len(altDet)>1:
            alts = altDet.split(',')
        for eachAlt in alts:

            if refChange == eachAlt:
                called = True
        if called:
            val = originalVariants[each]
            truePositives[each] = val

        else:
            outline = 'chr20' + '\t' + str(each) + '\t' + str(originalVariants[each][0]) + '\t' + str(originalVariants[each][1]) + '\n'
            fhoutND.write(outline)
            undetected.append(outline)
    for eachone in leftOut:
        outline = 'chr20' + '\t' + str(eachone) + '\t' + str(originalVariants[eachone][0]) + '\t' + str(originalVariants[eachone][1]) + '\n'
        fhoutND.write(outline)
    fhoutND.close()
##    for each in undetected[:100]:
##        print each

##    print '# of variants detected = ', len(tp)
    tpKeys = truePositives.keys()
    print '# of variants accurately detected (true positives) = ', len(tpKeys)


    rec =  (len(tpKeys)/float(len(originalVarSet)))*100.0
    prec = (len(tpKeys)/float(len(detectedVarSet)))*100.0
    print 'recall rate = ', rec
    print 'precision rate = ', prec
    return prec, rec




def main():
    original = sys.argv[1]
    detected = sys.argv[2]
    variantCompareIndel(original, detected)

##    coverageCompare()
if __name__ == '__main__':
    main()
