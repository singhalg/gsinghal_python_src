#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     07/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

from sets import Set
import pickle, sys

def geneRecurrence():

    files = [   ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],
                ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                [ 'PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']  ]


    geneDict = {}



    for eachPatient in files:
        primPick = eachPatient[0][:-4] +'_snpEff_del.pkl'
        metPick = eachPatient[1][:-4] +'_snpEff_del.pkl'


        fhPickleInPrim = open(primPick, 'rU')
        primPatientData = pickle.load(fhPickleInPrim)
        fhPickleInPrim.close()

        fhPickleInMet = open(metPick, 'rU')
        metPatientData = pickle.load(fhPickleInMet)
        fhPickleInMet.close()

        end = primPick.find('_lung')
        patientName = primPick[:end]


        primPositions = primPatientData.keys()
        metPositions = metPatientData.keys()

        ''' pick those genes which have
        DP>=20,
        AF>=0.1
        Present in both prim and met for the same allele

        {Gene_name: [{PT_name:recurrence_score},{func_class:mut_info}, {mut_loc: mut_loc_val_prim}, {mut_loc:, mut_loc_val_met}]}
            '''

def mutationRecurrence():

    files = [   ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],
                ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                [ 'PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']  ]


    # considering mutations only in primary tumors.
    allDeleterious = {}  # here we are considering only deleterious mutations and only in primary tumors.


    for eachTumor in files:
        prim = eachTumor[0]
        delMutPickleName = prim[:-4] + '_snpEff_del.pkl'
        fh = open(delMutPickleName, 'rU')
        delMutationsPrimary = pickle.load(fh)
        fh.close()

        end = delMutPickleName.find('_lung')
        patientName = delMutPickleName[:end]

        delMutLocations = delMutationsPrimary.keys()
        for eachLoc in delMutLocations:
            AF =  delMutationsPrimary[eachLoc]['AF']
            DP = delMutationsPrimary[eachLoc]['DP']
            ALT =  delMutationsPrimary[eachLoc]['ALT']
            for i in range(len(AF)):
                if (float(AF[i]) >= 0.1) and (int(DP[0])>=20):

                    if eachLoc not in allDeleterious:

                            newVal = [[patientName, ALT[i], float(AF[i]), DP[0]]]
                            allDeleterious[eachLoc] = newVal

                    else:
                        val = allDeleterious[eachLoc]

                        val.append([patientName, ALT[i], float(AF[i]), DP[0]])
                        allDeleterious[eachLoc] = val
##                        except:
##                            print delMutationsPrimary[eachLoc]
##                            sys.exit()

        del delMutationsPrimary, delMutLocations

    allDeleteriousPickle = open('All_deleterious.pkl', 'w')
    pickle.dump(allDeleterious, allDeleteriousPickle)
    allDeleteriousPickle.close()


def topRecurrentLocations():

    commonEVS = pickle.load(open('commonEVS.pkl', 'rU'))
    agilentCommon = pickle.load(open('agilent_V3_common.pkl', 'rU'))
    IlluminaCommon = pickle.load(open('Illumina_common.pkl', 'rU'))
    Illumin_agilent = pickle.load(open('Illumina_Agilent_common.pkl', 'rU'))

    allCommon = commonEVS | agilentCommon | IlluminaCommon | Illumin_agilent


    fh = open('All_deleterious.pkl', 'rU')



    allDeleterious = pickle.load(fh)
    fh.close()
    allDelList = []
    locations = allDeleterious.keys()
    for eachLoc in locations:
        if eachLoc not in allCommon:

            allDelList.append([eachLoc, allDeleterious[eachLoc]])

    allDelListSorted = sorted(allDelList, reverse=True, key = myFun)

    fhCommonDelList = open('common_del_list.pkl', 'w')
    pickle.dump(allDelListSorted, fhCommonDelList)

    count = 0
    for eachMostRecurrent in allDelListSorted[:1000]:
        if (int(eachMostRecurrent[1][0][3])>100) :
            print eachMostRecurrent
            print '# of patients having this mutation = ', len(eachMostRecurrent[1])



def myFun(alist):
    return len(alist[1])







def VCFtoPickle():
    files = [ 'PT_10_brain_1200360.vcf','PT_11_brain_1200385.vcf',  'PT_12_lung_1200381.vcf',   'PT_1_brain_1123232.vcf',  'PT_3_lung_1123221.vcf',   'PT_9_brain_1200383.vcf',
            'PT_11_lung_1200363.vcf',   'PT_13_brain_1200370.vcf',  'PT_1_lung_1123233.vcf',   'PT_6_brain_1123226.vcf',  'PT_9_lung_1200382.vcf',
            'PT_10_lung_1200384.vcf',          'PT_12_brain_1200368.vcf',  'PT_13_lung_1202946.vcf',   'PT_3_brain_1123220.vcf',  'PT_6_lung_1123227.vcf',
            'PT_2_brain_1123230.vcf', 'PT_2_lung_1123231.vcf']

##    files = [ 'PT_10_brain_1200360.vcf','']

    for eachFile in files:
        fileName = eachFile[:-4]+'_snpEff.vcf'
        variantVCF, deleteriousVCF = readVCF(fileName)
        allVCFPickleName = fileName[:-4]+'.pkl'
        fhAllVCF = open(allVCFPickleName, 'w')
        pickle.dump(variantVCF, fhAllVCF)
        fhAllVCF.close()
        deleteriousVCFpickleName = fileName[:-4]+'_del.pkl'
        fhDelVCF = open(deleteriousVCFpickleName, 'w')
        pickle.dump(deleteriousVCF, fhDelVCF)
        fhDelVCF.close()


def readVCF(fileName):
    fh = open(fileName, 'rU')
    data = fh.readlines()
    variantsVCF = {}
    deleteriousVariantsVCF = {}
##    varSet = Set([])

    for line in data:
        if line[0] != '#':
            flds = line.split('\t')
            if len(flds[7].split(';'))>2:

                processVCF(line, variantsVCF)



    variantPos = sorted(variantsVCF.keys())
    for apos in variantPos:
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
def processVCF(line, variantDict):
    flds = line.split('\t')
    key = flds[0].strip() + '#' + flds[1].strip()
    value = {}
    value['REF'] = flds[3].strip()
    value['ALT'] = flds[4].strip().split(',')  # ALT is a list
    for each in flds[7].strip().split(';'):
        info = each.partition('=')
        infoVal = info[2].split(',')
        value[info[0]] = infoVal  # DP, AF, EFF are all lists

##    variantDict[key] = value
    snpEff = flds[7].strip().split(';')[2][4:].split(',')
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



def main():
##    VCFtoPickle()
    mutationRecurrence()
    topRecurrentLocations()
if __name__ == '__main__':
    main()
