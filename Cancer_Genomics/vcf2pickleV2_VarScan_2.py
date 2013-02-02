#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     14/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import pickle, sys
import numpy as np
from sets import Set
'''
vcf2pickle.py was written to convert files from vcf format like 'PT_10_brain_1200360.vcf' into 2 pickles, one containing all variants and other containing only
deleterious variants. This vcf file is the output of snpEff

Here I am modifying this script. This new script (vcf2PickleV2.py) takes in a vcf file which is the output of snpEff and SnpSift (has predictions from both)
and saves 2 pickles, one containing all variants and the other containing only rare deleterious (MISSENSE and NONSENSE) variants. Thus, the second pickle
does not have any variant that appears in internal controls or external set of common variants (dbSNP, 1000 Genomes, EVS etc)

Additional tags:

'SIFT', 'GERP', 'PolyPhen2', 'score', 'logOdds'

'''

def VCFtoPickle():
##    files = [ 'PT_10_brain_1200360.vcf','PT_11_brain_1200385.vcf',  'PT_12_lung_1200381.vcf',   'PT_1_brain_1123232.vcf',  'PT_3_lung_1123221.vcf',   'PT_9_brain_1200383.vcf',
##            'PT_11_lung_1200363.vcf',   'PT_13_brain_1200370.vcf',  'PT_1_lung_1123233.vcf',   'PT_6_brain_1123226.vcf',  'PT_9_lung_1200382.vcf',
##            'PT_10_lung_1200384.vcf',          'PT_12_brain_1200368.vcf',  'PT_13_lung_1202946.vcf',   'PT_3_brain_1123220.vcf',  'PT_6_lung_1123227.vcf',
##            'PT_2_brain_1123230.vcf', 'PT_2_lung_1123231.vcf']


    commonEVS = pickle.load(open('commonEVS.pkl', 'rU'))
    agilentCommon = pickle.load(open('agilent_V3_common.pkl', 'rU'))
    IlluminaCommon = pickle.load(open('Illumina_common.pkl', 'rU'))
    Illumina_agilent = pickle.load(open('Illumina_Agilent_common.pkl', 'rU'))
    dbSNP           = pickle.load(open('dbSNPcommon_nonClinical.pkl', 'rU'))

    dbSNPcommon = Set(dbSNP.keys())
    del dbSNP

    allCommon = commonEVS | agilentCommon | IlluminaCommon | Illumina_agilent | dbSNPcommon

    del commonEVS, agilentCommon,IlluminaCommon,Illumina_agilent,dbSNPcommon

    files = ['2221', '2359', '2556', '3466']
    samples = ['Tumor', 'Normal']


    jobFiles = []

    for eachPatient in files:

        for eachSample in samples:

            fileName = eachPatient + '_' + eachSample + '_VarScan_clean_snpEff_SnpSift.vcf'


##    files = [ 'PT_10_brain_1200360.vcf','']




##    for eachPatient in files:
##        eachFile = eachPatient[1]  #-----====-----====----
##        end = eachFile.find('_brain')   ####----------------==============----------===========-------------=============
##        fileName = eachFile[:end] + '_brain_VarScan_clean_snpEff_SnpSift.vcf'  #-----========---------========--------


            variantVCF, deleteriousVCF = readVCF(fileName, allCommon)
            allVCFPickleName = fileName[:-4]+'.pkl'
            fhAllVCF = open(allVCFPickleName, 'w')
            pickle.dump(variantVCF, fhAllVCF)
            fhAllVCF.close()
            deleteriousVCFpickleName = fileName[:-4]+'_rare_del.pkl'
            fhDelVCF = open(deleteriousVCFpickleName, 'w')
            pickle.dump(deleteriousVCF, fhDelVCF)
            fhDelVCF.close()
            print fileName, ' processed !'
            del variantVCF, deleteriousVCF   # finally purging the objects from memory


def readVCF(fileName, commonSnpSet):
    fh = open(fileName, 'rU')
    data = fh.readlines()
    variantsVCF = {}
    deleteriousVariantsVCF = {}
##    varSet = Set([])

    for line in data:
        if line[0] != '#':
            flds = line.split('\t')
            if len(flds[7].split(';'))>2:

                processVCFline(line, variantsVCF)



    variantPos = sorted(variantsVCF.keys())
    for apos in variantPos:
        if apos not in commonSnpSet:  # filtering out all those variants which are present in allCommon (not rare)

            info = variantsVCF[apos]
            if 'Functional_Class' in info:
                func_class = info['Functional_Class']

                if ('MISSENSE' in func_class) or ('NONSENSE' in func_class):

                    deleteriousVariantsVCF[apos] = info

##    print '# of all variants in EVS file = ', len(variantPos)
##    print '# of common variants = ', len(varSet)
##    fhPickleCommonEVS = open('commonEVS.pkl', 'w')
##    pickle.dump(varSet, fhPickleCommonEVS)
##    fhPickleCommonEVS.close()
##    print variantsVCF
##    print '==============================='
##    print deleteriousVariantsVCF
    return variantsVCF, deleteriousVariantsVCF


'''
This method has been especially edited to parse the snpEff output vcf.

'''
def processVCFline(line, variantDict):
    flds = line.split('\t')
    key = flds[0].strip() + '#' + flds[1].strip()
    value = {}
    value['REF'] = flds[3].strip()
    value['ALT'] =   flds[4].strip().split(',') # ALT is a list
    for each in flds[7].strip().split(';'):
        info = each.partition('=')
        infoVal = info[2].split(',')
        value[info[0]] = infoVal  # DP, AF, PVAL, EFF are all lists

##    variantDict[key] = value
    snpEff = value['EFF']
##    snpEff = flds[7].strip().split(';')[2][4:].split(',')
##    print snpEff

##    valueBack = variantDict[key]
####    if 'EFF' in valueBack:
##    snpEff = valueBack['EFF']
##    else:
##        print line
##        sys.exit()
##        except:
##            print line
##            print flds[7]
##            sys.exit()
##    impacts = []
    '''
'Effect ( Effect_Impact | Functional_Class | Codon_Change | Amino_Acid_change|
Amino_Acid_length | Gene_Name | Gene_BioType | Coding | Transcript |
Exon [ | ERRORS | WARNINGS ] )'

    '''

    for eachEffect in snpEff:
        flds = eachEffect.partition('(')[2].split('|')
        effect = eachEffect.partition('(')[0]

        addValuetoDict('Effect', effect, value) # value is the dictionary here, this dictionary will be added as a value to variantDict later
        addValuetoDict('Effect_Impact', flds[0], value)
        addValuetoDict('Functional_Class', flds[1],value)
##        addValuetoDict('Codon_Change',flds[2],value)
##        addValuetoDict('Amino_Acid_Change',flds[3],value)
        addValuetoDict('Amino_Acid_Length',flds[4],value)
        addValuetoDict('Gene_Name',flds[5],value)
##        addValuetoDict('Gene_BioType',flds[6],value)
        addValuetoDict('Coding',flds[7],value)
        addValuetoDict('Transcript',flds[8],value)
        addValuetoDict('Exon',flds[9].partition(')')[0] ,value)

#calculating the SIFT score
    scores = []

    if 'dbnsfpSIFT_score' in value:
##        try:
        siftScores = list2FloatNParray(value['dbnsfpSIFT_score'])
##        for eachSift in value['dbnsfpSIFT_score']:
##            try:
##                fSift = float(eachSift)
##                siftScores.append(fSift)
##            except:
##                pass

        if len(siftScores)>0:

            SiftNew = 1 - (np.array(siftScores)).min()
            if SiftNew >=0.95:
                value['SIFT'] = SiftNew
                scores.append(SiftNew)

            else:
                value['SIFT'] = SiftNew/2
                newSc = SiftNew/2
                scores.append(newSc) #-------

##        except:
##            print value['dbnsfpSIFT_score']
##        SiftNew = 1 - siftScores.min()
##
##
##        if SiftNew >=0.95:
##            value['SIFT'] = SiftNew
##            scores.append(SiftNew)
##
##        else:
##            value['SIFT'] = SiftNew/2
##            newSc = SiftNew/2
##            scores.append(newSc) #-------

#calculating the GERP score

    if ('dbnsfpGERP++_RS' in value) and ('dbnsfpGERP++_NR' in value):
        gerp_rs = list2FloatNParray(value['dbnsfpGERP++_RS'])
##        try:
##            gerp_rs = np.array([float(n) for n  in value['dbnsfpGERP++_RS']])
##            gerp_rs_max = gerp_rs.max()
##        except :
##            print line

        gerp_nr = list2FloatNParray(value['dbnsfpGERP++_NR'])
        if (len(gerp_rs)>0) and (len(gerp_nr)>0):
            gerp_nr_max = gerp_nr.max()
            gerp_rs_max = gerp_rs.max()
            if gerp_rs_max>0:
                gerpScore = gerp_rs_max/gerp_nr_max
            else:
                gerpScore = 0
            if gerpScore >=1:
                value['GERP'] = 1
                scores.append(1)
            else:
                value['GERP'] = gerpScore
                scores.append(gerpScore)

#calculating polyPhen2 score

    if 'dbnsfpPolyphen2_HVAR_pred' in value:
        polyphen2 = value['dbnsfpPolyphen2_HVAR_pred']
        polyPhenScores = []
        for eachPred in polyphen2:
            if eachPred =='D':
                polyPhenScores.append(0.9)
            elif eachPred =='P':
                polyPhenScores.append(0.5)
            elif eachPred =='B':
                polyPhenScores.append(0)
        if len(polyPhenScores)>0:
            ppScore = np.array(polyPhenScores).max()
            value['PolyPhen2'] = ppScore
            scores.append(ppScore)

#calculating logOdds
    if 'dbnsfp29way_logOdds' in value:
        logOdds = list2FloatNParray(value['dbnsfp29way_logOdds'])
##        logOdds = np.array([float(n) for n in value['dbnsfp29way_logOdds']]).max()
        if len(logOdds)>0:

            LOScore  = (logOdds.max())/14
            if LOScore>=1:

                value['logOdds'] = 1
                scores.append(1)

            else:
                value['logOdds'] = LOScore
                scores.append(LOScore)
    if len(scores)>0:

##        print scores

        combinedScore = (np.array(scores)).sum() / float(len(scores))
        value['score'] = combinedScore






    variantDict[key] = value

def addValuetoDict(akey, newValue, dictionary):
    if akey in dictionary:
        value = dictionary[akey]
        if len(newValue) > 0:
            value.add(newValue)
            dictionary[akey] = value
    else:
        value = Set([])
        if len(newValue) > 0:
            value.add(newValue)
            dictionary[akey] = value

'''
Converts a list of numbers into floats, and returns them as an numpy array. Also takes care if some elements are strings,
it removes the elements which are strings and just returns the float numbers.
'''

def list2FloatNParray(alist):
    floatArray = []
    for each in alist:
        try:

            fScore = float(each)
            floatArray.append(fScore)
        except:
            pass

    return np.array(floatArray)

def main():
    VCFtoPickle()




if __name__ == '__main__':
    main()
