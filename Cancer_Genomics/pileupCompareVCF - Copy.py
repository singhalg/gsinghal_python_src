#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     20/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys
from sets import Set
import pickle

def pileupCompare(file1, file2, outfileName, targetCapturePlatform):

    targetCaptureFlds = Set(['AgilentV3', 'AgilentV4', 'Illumina'])
    if targetCapturePlatform not in targetCaptureFlds:
        print 'TargetCapturePlatform is invalid !!'
        sys.exit()

    fh1 = open(file1, 'rU')
    fh2 = open(file2, 'rU')

    prim = fh1.readlines()
    met = fh2.readlines()
    fh1.close()
    fh2.close()
    primary = {}
    metastasis = {}
    primarySet = Set([])
    metastasisSet = Set([])
    onlyInPrimSet = Set([])
    onlyInMetSet = Set([])
    depthDict = {} # dict of dict. {'1#1000111':{'primary':'25', 'metastasis':'27'},
    effectDict = {} # dict. {'1#1000111':['NON_SYNONYMOUS_CODING', 'MODERATE', 'MISSENSE']}

##
##"
#ref != N
#first those variants whose freq changes
#then those variants wich are absent from one but present in another group
#
##"

    for line in prim[8:]:
        flds = line.split('\t')
        depth = flds[7].strip().split(';')[0][3:]
        key = flds[0].strip() + '#' +flds[1].strip()  # the position of the variant is always 1-based coordinate

        depthVal = {}
        depthVal['primary'] = depth
        depthDict[key] = depthVal
        effects = ''

        if len(flds[7].strip().split(';')) > 2:

            effects = flds[7].strip().split(';')[2].split(',')
##        except:
##            print line
##            print flds[7]
##            sys.exit()
            impacts = []

            for eachEffect in effects:
                impact = eachEffect.partition('(')[2].split('|')[0]
                if impact == 'MODIFIER':
                    impacts.append(['MODIFIER', 0])
                elif impact == 'MODERATE':
                    impacts.append(['MODERATE', 2])
                elif impact == 'LOW':
                    impacts.append(['LOW', 1])
                elif impact =='HIGH':
                    impacts.append(['HIGH', 3])
            impactVal = sorted(impacts, reverse=True, key=myFun)[0]
            effectDict[key] = impactVal
##        if len(impacts)>1:
##            print sorted(impacts, reverse=True, key=myFun)
        value = {}

        alt = flds[4].strip().split(',')
##        info = flds[3].strip().split(';')
##        alt = info[1][4:].split(',')

#        alt = flds[3].strip().split(',')
#        st = flds[4].strip().index('AF=')

        af = flds[7].strip().split(';')[1][3:].split(',')
##        af = info[3].strip()[3:].split(',')
#        af = flds[4][st+3:].strip().split(',')
        if len(alt) != len(af):
            print 'Error !! # ALT ALLELE and AF mismatch'
            print line
            continue
##            sys.exit()
        for i in range(len(alt)):
            value[alt[i]] = float(af[i])
        primary[key] = value


    for line in met[8:]:
        flds = line.split('\t')
        depth = flds[7].strip().split(';')[0][3:]
        key = flds[0].strip() + '#' +flds[1].strip()  # the position of the variant is always 1-based coordinate

##        depth = flds[3].strip().split(';')[2][3:]
##        key = flds[0].strip() + '#' +flds[2].strip()
        if (key not in effectDict) and(len(flds[7].strip().split(';')) > 2):
            effects = flds[7].strip().split(';')[2].split(',')
            impacts = []

            for eachEffect in effects:
                impact = eachEffect.partition('(')[2].split('|')[0]
                if impact == 'MODIFIER':
                    impacts.append(['MODIFIER', 0])
                elif impact == 'MODERATE':
                    impacts.append(['MODERATE', 2])
                elif impact == 'LOW':
                    impacts.append(['LOW', 1])
                elif impact =='HIGH':
                    impacts.append(['HIGH', 3])
            impactVal = sorted(impacts, reverse=True, key=myFun)[0]
            effectDict[key] = impactVal

        if key in depthDict:
            depthVal = depthDict[key]
            depthVal['metastasis'] = depth
            depthDict[key] = depthVal
        else:
            depthVal = {}
            depthVal['metastasis'] = depth
            depthDict[key] = depthVal

        value = {}
        alt = flds[4].strip().split(',')
        af = flds[7].strip().split(';')[1][3:].split(',')

##        info = flds[3].strip().split(';')
##        alt = info[1][4:].split(',')
##
###        alt = flds[3].strip().split(',')
###        st = flds[4].strip().index('AF=')
##
##        af = info[3].strip()[3:].split(',')
###        af = flds[4][st+3:].strip().split(',')
        if len(alt) != len(af):
            print 'Error !! # ALT ALLELE and AF mismatch'
            print line
##            sys.exit()
            continue
        for i in range(len(alt)):
            value[alt[i]] = float(af[i])
        metastasis[key] = value

##    print primary
##    print metastasis

    primarySet = Set(primary.keys())
    metastasisSet = Set(metastasis.keys())
    onlyInPrimSet = primarySet - metastasisSet
    onlyInMetSet = metastasisSet - primarySet
    commonLoc = primarySet & metastasisSet
    allLoci = primarySet | metastasisSet

    if targetCapturePlatform == 'AgilentV3':
        fhinternal = open('agilent_V3_common.pkl', 'rU')
    elif targetCapturePlatform == 'AgilentV4':
        fhinternal = open('Illumina_Agilent_common.pkl', 'rU')
    else:
        fhinternal = open('Illumina_common.pkl', 'rU')
    internal = pickle.load(fhinternal)
    fhinternal.close()
    fhexternal = open('commonEVS_asrd10.pkl', 'rU')
    external = pickle.load(fhexternal)
    fhexternal.close()

    fhdbSNP = open('dbSNPcommon_nonClinical.pkl', 'rU')
    dbSNP = pickle.load(fhdbSNP)
    fhdbSNP.close()


    allControls = internal | external | dbSNP


##    for eachLoc in allLoci:
##        if eachLoc not in allControls:
##            if eachLoc in primarySet:
##                allele_dict = primary[eachLoc]
##                for anAllele in allele_dict:



    different = {}
##    print 'reached point 1'
    for each in commonLoc:
        primVar = primary[each]
        metVar = metastasis[each]
        primAlleles = primVar.keys()
        metAlleles = metVar.keys()

        commonAltAlleles = Set(metAlleles) & Set(primAlleles)                                        # alt_alleles (C,G etc) at a particular location which are present in both prim and metastasis
        for alt_al in commonAltAlleles:

##            if primVar[alt_al] != metVar[alt_al]:

            if each in different:
                val = different[each]
                val[alt_al] = [primVar[alt_al], metVar[alt_al]]
            else:
                val = {}
                val[alt_al] = [primVar[alt_al], metVar[alt_al]]
            different[each] = val   # different is a dict of dict of the form {'1#1001232':{'A':['0.1210249','0.002321'], 'C':['0.002322','0.0232']}, '2#1034465':{'T':['0.4456459','0.445651'], 'G':['0.0544','0.0432']},.. }
##            else:
##                pass

##            else:
##                if each in different:
##                    val = different[each]
##                    val[alt_al] = [primVar[alt_al], 0]
##                else:
##                    val = {}
##                    val[alt_al] = [primVar[alt_al], 0]
##                    different[each] = val


        MetAlleleNotInPrim = Set(metAlleles) - Set(primAlleles)
        PrimAlleleNotInMet =  Set(primAlleles) - Set(metAlleles)

        for alt_all in PrimAlleleNotInMet:
            if each in different:
                val = different[each]
                val[alt_all] = [primVar[alt_all], 0]
            else:
                val = {}
                val[alt_all] = [primVar[alt_all], 0]
            different[each] = val
        for alt_all in MetAlleleNotInPrim:
            if each in different:
                val = different[each]
                val[alt_all] = [0, metVar[alt_all]]
            else:
                val = {}
                val[alt_all] = [0, metVar[alt_all]]
            different[each] = val

##    print 'reached point 2'
    for each in onlyInMetSet:
        val = {}
        variants = metastasis[each]
        for abase in variants.keys():
            val[abase] = [0, variants[abase]]
        different[each]  = val
    for each in onlyInPrimSet:
        val = {}
        variants = primary[each]
        for abase in variants.keys():
            val[abase] = [variants[abase], 0]
        different[each]  = val
##    print 'reached point 3'

    outfile1 = outfileName + '_variants_rm_common.csv'
    outfile2 = outfileName + '_variants_rm_common_cutoff.csv'
    fhout = open(outfile1, 'w')

    fhout2 = open(outfile2, 'w')


    outline = 'chr' + ',' + 'position' + ',' + 'DP_PRIM' +',' +'DP_MET' +',' + 'ALT_ALLELE' + ','  + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',EFFECT_IMPACT' '\n'  ##+ 'ALT_ALLELE_2' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_3' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_4' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_5' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_6' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + '\n'
    fhout.write(outline)
    fhout2.write(outline)

##    print 'All variants detected = ', len(different.keys())

    rareVariants = Set(different.keys()) - allControls

    variantLoc = sorted(list(rareVariants))
##    print 'Rare variants detected  =', len(variantLoc)

##    variantLoc = sorted(different.keys())
    for eachLoc in variantLoc:

        chrm, pos = eachLoc.split('#')
        outline = chrm + ',' + pos + ','

        depths = depthDict[eachLoc]
        if 'primary' in depths:

            prim_depth = depths['primary']
        else:
            prim_depth = '0'

        if 'metastasis' in depths:
            met_depth = depths['metastasis']
        else:
            met_depth = '0'

        outline += prim_depth + ',' + met_depth + ','



        variants = different[eachLoc]
        for eachVar in variants.keys():

            VAF = variants[eachVar]
            if eachLoc in effectDict:  # not all loci are present as keys in effectDict, some variants have ATL allele == REF allele and have no entry for mutation effect, so we are excluding such loci from our csv file
                outline1 = outline + eachVar + ','+ str(VAF[0]) + ',' + str(VAF[1]) + ',' + str(effectDict[eachLoc][1]) + '\n'

                fhout.write(outline1)

            if ((VAF[0] >= 0.05) or (VAF[1] >= 0.05)) and ((VAF[0] <= 0.95) or (VAF[1] <= 0.95)):
                if eachLoc in effectDict:
                    outline2 = outline  + eachVar + ',' + str(VAF[0]) + ',' + str(VAF[1]) + ',' + str(effectDict[eachLoc][1]) +  '\n'
                    fhout2.write(outline2)



##    print 'reached point 4'
    fhout.close()
    fhout2.close()





def myFun(alist):
    return alist[1]





def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    outfile = sys.argv[3]
    target_capture_platform = sys.argv[4]
    # needs input in vcf format, these vcf files have those variants which fall in target capture boundaries.
    # target_capture_platform is a string having one of the following values : 'AgilentV3', 'AgilentV4', Illumina'

    pileupCompare(file1, file2, outfile, target_capture_platform)


if __name__ == '__main__':
    main()
