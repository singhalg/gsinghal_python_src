#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     06/06/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys, os, pickle
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



def variantCompareIndel(original, detected, third, fourth, platform):
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

        if each[0]!= '#':



##        if (flds[0].strip().find('chr')!= -1) and (flds[0].strip().find('chrU')== -1):
            flds = each.strip().split('\t')

            val = [flds[3], flds[4], flds[5]]
            key = flds[0] + '#' +flds[1]
            originalVariants[key] = val
            originalVarSet.add(key)

    for each in varList2 :
         if each[0]!= '#':



##        if (flds[0].strip().find('chr')!= -1) and (flds[0].strip().find('chrU')== -1):
            flds = each.strip().split('\t')

            val = [flds[3], flds[4], flds[5]]
            key = flds[0] + '#' +flds[1]
            detectedVariants[key] = val
            detectedVarSet.add(key)

    fh3 = open(third, 'rU')
    varList3 = fh3.readlines()
    fh3.close()

    thirdVariants = {}
    thirdVarSet = Set([])

    for each in varList3 :
        if each[0]!= '#':



##        if (flds[0].strip().find('chr')!= -1) and (flds[0].strip().find('chrU')== -1):
            flds = each.strip().split('\t')
            val = [flds[3], flds[4], flds[5]]
            key = flds[0] + '#' +flds[1]
            thirdVariants[key] = val
            thirdVarSet.add(key)

    fh4 = open(fourth, 'rU')
    varList4 = fh4.readlines()
    fh4.close()

    fourthVariants = {}
    fourthVarSet = Set([])

    for each in varList4 :
       if each[0]!= '#':



##        if (flds[0].strip().find('chr')!= -1) and (flds[0].strip().find('chrU')== -1):
            flds = each.strip().split('\t')
            val = [flds[3], flds[4], flds[5]]
            key = flds[0] + '#' +flds[1]
            fourthVariants[key] = val
            fourthVarSet.add(key)

    list1 = sorted(list(originalVarSet))

    list2 = sorted(list(detectedVarSet))

    common = thirdVarSet & originalVarSet & detectedVarSet

    oneAndTwo = originalVarSet & detectedVarSet

    print 'size of set one : ', len(originalVarSet)
    print 'size of set two : ', len(detectedVarSet)
    print 'size of set third : ', len(thirdVarSet)
    print 'size of set fourth : ', len(fourthVarSet)
    print '# of variants common between one and two : ', len(oneAndTwo)

    twoAndThree = detectedVarSet & thirdVarSet

    print '# of variants common between two and three : ', len(twoAndThree)

    oneAndThree = originalVarSet & thirdVarSet

    print '# of variants common between one and three : ', len(oneAndThree)

    oneAndFour = originalVarSet & fourthVarSet

    print '# of variants common between one and four : ', len(oneAndFour)

    twoAndFour = detectedVarSet & fourthVarSet

    print '# of variants common between two and four : ', len(twoAndFour)

    threeAndFour = thirdVarSet & fourthVarSet

    print '# of variants common between three and four : ', len(threeAndFour)

    print '# of variants common between one, two and three : ', len(common)

    print '# of variants common between two, three and four : ', len(  detectedVarSet & thirdVarSet & fourthVarSet  )

    print '# of variants common between one, three and four : ', len(  originalVarSet & thirdVarSet & fourthVarSet  )

    print '# of variants common between one, two and four : ', len(  originalVarSet& detectedVarSet &  fourthVarSet  )

    print '# of variants common between one, two, three and four : ', len(  originalVarSet & detectedVarSet & thirdVarSet & fourthVarSet  )

    commonInAll =  originalVarSet & detectedVarSet & thirdVarSet & fourthVarSet
    pickleName = platform+'_exp_common.pkl'
    fhPickle = open(pickleName, 'w')
    pickle.dump(commonInAll, fhPickle)
    fhPickle.close()
    common_all_together = open('common_all_together.txt', 'w')
    commonFhOut1 = open('common_from_one.txt', 'w')
    commonFhOut2 = open('common_from_two.txt', 'w')
    commonFhOut3 = open('common_from_three.txt', 'w')
    commonFhOut4 = open('common_from_four.txt', 'w')
    keys = list(commonInAll)
    keys = sorted(keys)
    print keys[:50]
    for key in keys:
        val = originalVariants[key]
        chrm, pos = key.split('#')
        outline = chrm +'\t' +pos + '\t' + (val[0]) + '\t' + (val[1]) + '\t' + (val[2]) +  '\n'

        common_all_together.write(outline)



        val = detectedVariants[key]
        chrm, pos = key.split('#')
        outline = chrm +'\t' +pos + '\t' + (val[0]) + '\t' + (val[1]) + '\t' + (val[2]) +  '\n'

        common_all_together.write(outline)


        val = thirdVariants[key]
        chrm, pos = key.split('#')
        outline = chrm +'\t' +pos + '\t' + (val[0]) + '\t' + (val[1]) + '\t' + (val[2]) + '\n'

        common_all_together.write(outline)

        val = fourthVariants[key]
        chrm, pos = key.split('#')
        outline = chrm +'\t' +pos + '\t' + (val[0]) + '\t' + (val[1]) + '\t' + (val[2]) +  '\n'

        common_all_together.write(outline)
    common_all_together.close()
##        val = originalVariants[key]
##        chrm, pos = key.split('#')
##        outline = chrm +'\t' +pos + '\t' + (val[0]) + '\t' + (val[1]) + '\t' + (val[2]) + '\t' + (val[3])+ '\n'
##        commonFhOut1.write(outline)
##        common_all_together.write(outline)
##    commonFhOut1.close()
##
##    for key in keys:
##        val = detectedVariants[key]
##        chrm, pos = key.split('#')
##        outline = chrm +'\t' +pos + '\t' + (val[0]) + '\t' + (val[1]) + '\t' + (val[2]) + '\t' + (val[3])+ '\n'
##        commonFhOut2.write(outline)
##
##    commonFhOut2.close()
##
##    for key in keys:
##        val = thirdVariants[key]
##        chrm, pos = key.split('#')
##        outline = chrm +'\t' +pos + '\t' + (val[0]) + '\t' + (val[1]) + '\t' + (val[2]) + '\t' + (val[3])+ '\n'
##        commonFhOut3.write(outline)
##
##    commonFhOut3.close()
##
##    for key in keys:
##        val = fourthVariants[key]
##        chrm, pos = key.split('#')
##        outline = chrm +'\t' +pos + '\t' + (val[0]) + '\t' + (val[1]) + '\t' + (val[2]) + '\t' + (val[3])+ '\n'
##        commonFhOut4.write(outline)
##    commonFhOut4.close()
##
##






##    print 'Printing original variants ...'
##    for each in list1[:10]:
##        print each
##        print originalVariants[each]
##    print '\n'
##    print 'Now printing detected variants ...'
##    for each in list2[:10]:
##        print each
##        print detectedVariants[each]

##    print '# of variants in primary = ', len(originalVarSet)
##    print '# of variants in metastasis = ', len(detectedVarSet)
##    fhoutND = open('discrepancy.txt', 'w')
##
##    undetected = []
##    tp = originalVarSet.intersection(detectedVarSet)  # set of variants common between primary and metastasis
##
##    only_in_primary = originalVarSet - detectedVarSet
##    only_in_metastasis = detectedVarSet - originalVarSet
##
####    print '# possible true positives  =',len(tp)
##    truePositives = {}      # dictionary of true positives
##
##    leftOut = originalVarSet-tp
##
##    for each in tp:
##        called = False
##
##        ref = originalVariants[each][0]
##        refChange = originalVariants[each][1]
##        altref = detectedVariants[each][0]
##        altDet = detectedVariants[each][1]
##        alts = altDet
##        if len(altDet)>1:
##            alts = Set(altDet.split(','))
##        if len(refChange)>1:
##            refChange = Set(refChange.split(','))
##        if refChange == alts:
##            called = True
##        if called:
##            val = originalVariants[each]
##            truePositives[each] = val
##
##        else:
##            chrm, pos = each.split('#')
##            outline1 = chrm +'\t' +pos + '\t' + str(originalVariants[each][0]) + '\t' + str(originalVariants[each][1]) + '\t' + str(originalVariants[each][2]) + '\t' + str(originalVariants[each][3])   + '\n'
##            fhoutND.write(outline1)
##            outline2 = chrm +'\t' +pos + '\t' + str(detectedVariants[each][0]) + '\t' + str(detectedVariants[each][1]) + '\t' + str(originalVariants[each][2]) + '\t' + str(originalVariants[each][3])  + '\n'
##            fhoutND.write(outline2)
##
##            undetected.append(outline1)
####    for eachone in leftOut:
####        chr, pos = eachone.split('_')
####        chrPos = chr+pos
####        outline = chr +'\t' +pos + '\t'  + str(originalVariants[chrPos][0]) + '\t' + str(originalVariants[chrPos][1]) + '\n'
####        fhoutND.write(outline)
##    fhoutND.close()
####    for each in undetected[:100]:
####        print each
##
####    print '# of variants detected = ', len(tp)
##    tpKeys = truePositives.keys()
##    print '# of variants common between primary and metastasis = ', len(tpKeys)
##
##
##    rec =  (len(tpKeys)/float(len(originalVarSet)))*100.0
##    prec = (len(tpKeys)/float(len(detectedVarSet)))*100.0
##    print '% of primary tumor variants retained in metastatic tissue = ', rec
####    print 'precision rate = ', prec
##
##    prim_only = open('only_in_primary.txt', 'w')
##    met_only = open('only_in_metastasis.txt', 'w')
##
##    print '# of variants unique to primary : ', len(only_in_primary)
##    for key in only_in_primary:
##        val = originalVariants[key]
##        chrm, pos = each.split('#')
##        outline = chrm +'\t' +pos + '\t' + (val[0]) + '\t' + (val[1]) + '\t' + (val[2]) + '\t' + (val[3])+ '\n'
##        prim_only.write(outline)
##    prim_only.close()
##
##    print '# of variants unique to metastasis : ', len(only_in_metastasis)
##    for key in only_in_metastasis:
##
##        val = detectedVariants[key]
##        chrm, pos = each.split('#')
##        outline = chrm +'\t' +pos + '\t' + (val[0]) + '\t' + (val[1]) + '\t' + (val[2]) + '\t' + (val[3])+ '\n'
##        met_only.write(outline)
##    met_only.close()
##
##
##    return prec, rec
##



def main():
    original = sys.argv[1]
    detected = sys.argv[2]
    third = sys.argv[3]
    fourth = sys.argv[4]
    platform = sys.argv[5]
    variantCompareIndel(original, detected, third, fourth, platform)

##    coverageCompare()
if __name__ == '__main__':
    main()
