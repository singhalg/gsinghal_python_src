#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     11/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------
from sets import Set
import pickle, gc
import numpy as np




'''
This method reads all deleterious mutations (primary) and generates a super object.
'''
def readAllMutations():

    files = [   ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],
                ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                [ 'PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']  ]
##
##    files = [   ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
##                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
##                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],
##                ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
##                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
##                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf']]
##    files = [ ['PT_10_lung_1200384.vcf','']]  #/////----///---////----
    # considering mutations only in primary tumors.
    allDeleterious = {}  # here we are considering only deleterious mutations and only in primary tumors.

##    commonEVS = pickle.load(open('commonEVS.pkl', 'rU'))
##    agilentCommon = pickle.load(open('agilent_V3_common.pkl', 'rU'))
##    IlluminaCommon = pickle.load(open('Illumina_common.pkl', 'rU'))
##    Illumina_agilent = pickle.load(open('Illumina_Agilent_common.pkl', 'rU'))
##    dbSNP           = pickle.load(open('dbSNPcommon_nonClinical.pkl', 'rU'))
##
##    dbSNPcommon = Set(dbSNP.keys())
##    del dbSNP
##
##    allCommon = commonEVS | agilentCommon | IlluminaCommon | Illumina_agilent | dbSNPcommon
##
##    del commonEVS, agilentCommon,IlluminaCommon,Illumina_agilent,dbSNPcommon
    allCommon = Set([]) # we have already filtered out the common variants, the pickles ending in rare_del.pkl have rare varaints. So, we are keeping this set empty.
    mutation_info_dict = {}

    for eachTumor in files:
        prim = eachTumor[0]
        end = prim.find('_lung')   ####----------------==============----------===========-------------=============
        delMutPickleName = prim[:end] + '_lung_snpEff_SnpSift_rare_del.pkl'  #-----========---------========--------
##        delMutPickleName = prim[:-4] + '_snpEff_SnpSift_rare_del.pkl'
        fh = open(delMutPickleName, 'rU')
        delMutationsPrimary = pickle.load(fh)
        fh.close()

        end = delMutPickleName.find('_lung')   ####----------------==============----------===========-------------=============
        patientName = delMutPickleName[:end]

        delMutLocations = delMutationsPrimary.keys()
        for eachLoc in delMutLocations:  #/////----///---////----
            AF =  delMutationsPrimary[eachLoc]['AF']
            DP = delMutationsPrimary[eachLoc]['DP']
            ALT =  delMutationsPrimary[eachLoc]['ALT']

            if eachLoc not in allCommon:  # considering only those locations which are non-common variants


                for i in range(len(AF)):
                    read_support  = (float(AF[i])*int(DP[0]))

                    if ((read_support>=2) and ((float(AF[i]) >= 0.05))): # this will also shorten the list of variants by quite a lot

                        if eachLoc not in allDeleterious:
                            patientDict = {}
                            patientDict[patientName] = [[ALT[i], float(AF[i]), DP[0]]]
        ##                            newVal = [[patientName, ALT[i], float(AF[i]), DP[0]]]
                            allDeleterious[eachLoc] = patientDict

                        else:
                            patientDict = allDeleterious[eachLoc] # this patientDict should be of the form {PT_name:[ [ALT1, AF1], [ALT2, AF2]]}
                            if patientName in patientDict:
                                patientVal = patientDict[patientName]  # here we update the patientDict
                                patientVal.append([ALT[i], float(AF[i]), DP[0]])
                                patientDict[patientName] = patientVal
                            else:
                                newPatientVal = [[ALT[i], float(AF[i]), DP[0]]]
                                patientDict[patientName] = newPatientVal
                            allDeleterious[eachLoc] = patientDict
                if (eachLoc in allDeleterious) and (eachLoc not in mutation_info_dict):       # adding only those variants to mut_info which have been added to allDeleterious
                    info = delMutationsPrimary[eachLoc]
                    mut_info = []
                    mut_info.append(info['REF'])  #0
                    mut_info.append(info['DP'])   #1
                    mut_info.append(info['Functional_Class']) #2
                    mut_info.append(info['Gene_Name'])  #3
                    mut_info.append(info['Effect']) #4
                    mut_info.append(info['Effect_Impact']) #5

##                    predictions = {}

                    if'dbnsfpSIFT_score' in info: #6
                        siftScore = list2FloatArray(info['dbnsfpSIFT_score'])
                        if len(siftScore)>0:
                            mut_info.append(str(siftScore.min()))
                    else:
                        mut_info.append('NA')

                    if'dbnsfpGERP++_RS' in info: #7
                        GERP_RS = list2FloatArray(info['dbnsfpGERP++_RS'])
                        if len(GERP_RS)>0:
                            mut_info.append(GERP_RS.max())
                    else:
                        mut_info.append('NA')

                    if'dbnsfpGERP++_NR' in info: #8
                        GERP_NR = list2FloatArray(info['dbnsfpGERP++_NR'])
                        if len(GERP_NR)>0:
                            mut_info.append(GERP_NR.max())
                    else:
                        mut_info.append('NA')

                    if'dbnsfpPolyphen2_HVAR_pred' in info: #9
                        polyP = info['dbnsfpPolyphen2_HVAR_pred']
                        if len(polyP)>0:
                            mut_info.append(polyP[0])
                    else:
                        mut_info.append('NA')

                    if'dbnsfp29way_logOdds' in info:   #10
                        logOdd = list2FloatArray(info['dbnsfp29way_logOdds'])
                        if len(logOdd)>0:
                            mut_info.append(logOdd.max())
                    else:
                        mut_info.append('NA')

                    if'score' in info:  #11
                        score = info['score']

                        mut_info.append(score)
                    else:
                        mut_info.append('NA')



                    mut_info.append(info['EFF']) #12

                    if'dbnsfpESP5400_EA_AF' in info: #13
                        mut_info.append(alt_allele_af(ALT,info['dbnsfpESP5400_EA_AF']))
                    else:
                        mut_info.append('NA')

                    if'dbnsfpESP5400_AA_AF' in info:  #14
                        mut_info.append(alt_allele_af(ALT,info['dbnsfpESP5400_AA_AF']))
                    else:
                        mut_info.append('NA')

                    if'dbnsfp1000Gp1_AFR_AF' in info: #15
                        mut_info.append(alt_allele_af(ALT,info['dbnsfp1000Gp1_AFR_AF']))
                    else:
                        mut_info.append('NA')


                    if'dbnsfp1000Gp1_EUR_AF' in info:  #16
                        mut_info.append(alt_allele_af(ALT,info['dbnsfp1000Gp1_EUR_AF']))
                    else:
                        mut_info.append('NA')

                    if'dbnsfp1000Gp1_AMR_AF' in info: #17
                        mut_info.append(alt_allele_af(ALT,info['dbnsfp1000Gp1_AMR_AF']))
                    else:
                        mut_info.append('NA')

                    if'dbnsfp1000Gp1_AF' in info:  #18
                        mut_info.append(alt_allele_af(ALT,info['dbnsfp1000Gp1_AF']))
                    else:
                        mut_info.append('NA')


                    mutation_info_dict[eachLoc] = mut_info

        gc.collect()
        del delMutationsPrimary, delMutLocations, mut_info


    allDeleteriousPickle = open('All_deleterious_primary_rare.pkl', 'w')  #/////----///---////----
    pickle.dump(allDeleterious, allDeleteriousPickle)
    allDeleteriousPickle.close()

    mut_info_pickle = open('prim_mutation_info_dict_new.pkl', 'w')  ##---===----====---
    pickle.dump(mutation_info_dict, mut_info_pickle)
    mut_info_pickle.close()

    del mutation_info_dict, allDeleterious
    print 'Finished reading primary mutations'

def mutationRecurrence():
##    commonEVS = pickle.load(open('commonEVS.pkl', 'rU'))
##    agilentCommon = pickle.load(open('agilent_V3_common.pkl', 'rU'))
##    IlluminaCommon = pickle.load(open('Illumina_common.pkl', 'rU'))
##    Illumina_agilent = pickle.load(open('Illumina_Agilent_common.pkl', 'rU'))
##    dbSNP           = pickle.load(open('dbSNPcommon_nonClinical.pkl', 'rU'))
##
##    dbSNPcommon = dnSNP.keys()
##    del dbSNP
##
##    allCommon = commonEVS | agilentCommon | IlluminaCommon | Illumina_agilent | dbSNPcommon




    fhAllDeleterious = open('All_deleterious_primary_rare.pkl', 'rU') #/////----///---////----
    allDeleterious = pickle.load(fhAllDeleterious)
    fhAllDeleterious.close()

    allDelList = []
    locations = allDeleterious.keys()
    for eachLoc in locations:
##        if eachLoc not in allCommon: # here, we are taking only those locations which are not present in any of the internal or external common snps
        patientDict = allDeleterious[eachLoc]
        allDelList.append([eachLoc, len(patientDict.keys())])
        del patientDict


    allDelListSorted = sorted(allDelList, reverse=True, key = myFun) # these are mutations which are not common SNPS and sorted by their recurrence.

    fhRecurrentMutList = open('prim_recurrent_mutation_list.pkl', 'w')  #/////----///---////----
    pickle.dump(allDelListSorted, fhRecurrentMutList)
    fhRecurrentMutList.close()

##    count = 0
##    for eachMostRecurrent in allDelListSorted[:100]:
##        if (int(eachMostRecurrent[1][0][3])>100) :
##        print eachMostRecurrent, '   # of patients having this mutation = ', eachMostRecurrent[1]

    print 'Finished calculating recurrence in primary'
    del allDeleterious, allDelListSorted, allDelList

def myFun(alist):
    return alist[1]




def recurrentMut2CSV():
    recurrentMutList = pickle.load(open('prim_recurrent_mutation_list.pkl', 'rU')) #/////----///---////----
    allDeleterious = pickle.load(open('All_deleterious_primary_rare.pkl', 'rU')) #/////----///---////----
    mutation_info_dict = pickle.load(open('prim_mutation_info_dict_new.pkl', 'rU'))   #/////----///---////----
    cosmic = pickle.load(open('cosmic_V60_coding_Point_mutations_locations.pkl', 'rU'))
    dbSNPClinical = pickle.load(open('dbSNP_clinical.pkl', 'rU')) #////----/////------/////

    fhout = open('mutation_recurrence_results_primary_GTAC.csv', 'w')
    outline = 'CHRM,POS,REF,GENE,EFFECT_IMPACT,COSMIC,dbSNP_Clinical,ESP_EA,ESP_AFR_A,1000Gp1_AFR,1000Gp1_EUR,1000Gp1_AMR,1000Gp1,SIFT,GERP_RS,GERP_NR,logOdds,PolyPhen2,Composite_Score,Gene#AA,Num_Patients,PT_NAME,ALT,AF,DEPTH,READ_SUPPORT' + '\n'
    fhout.write(outline)
    # add num patients to each mutation
    # add depth to each mutation
    # add if present in dbSNP clinical
    # which of these mutations are present in metastasis as well
    # which of these mutations have increased freq in metastasis
    for eachLoc in recurrentMutList:
        patientDict = allDeleterious[eachLoc[0]]
        mut_info = mutation_info_dict[eachLoc[0]]
        REF = mut_info[0]
        chrm = eachLoc[0].split('#')[0]
        position = eachLoc[0].split('#')[1]
        dp = mut_info[1][0]
        gene = '#'.join(list(mut_info[3]))
        effect_impact = '#'.join(list(mut_info[5]))


        sift = str(mut_info[6])
        gerp_rs = str(mut_info[7])
        gerp_nr = str(mut_info[8])

        polyPhen2 = str(mut_info[9])
        logOdds = str(mut_info[10])
        comp_score = str(mut_info[11])
        gene_aa_mut = effProcesser(mut_info[12])

        '''Effect ( Effect_Impact | Functional_Class | Codon_Change | Amino_Acid_change|
Amino_Acid_length | Gene_Name | Gene_BioType | Coding | Transcript |
Exon [ | ERRORS | WARNINGS ] )'''



        if eachLoc[0] in cosmic:
            cosmic_check = 'Yes'
        else:
            cosmic_check = 'No'

        if eachLoc[0] in dbSNPClinical:
            dbSNP_check = 'Yes'
        else:
            dbSNP_check = 'No'


                                                                                                                    #ESP_EA,ESP_AFR_A,1000Gp1_AFR,1000Gp1_EUR,1000Gp1_AMR,1000Gp1,
        outline = chrm +','+ position +','+REF +','+ gene+','+ effect_impact +',' +cosmic_check + ','+ dbSNP_check+ ',' +mut_info[13] + ','+mut_info[14] +',' +mut_info[15]+','+mut_info[16] + ',' + mut_info[17] +',' +mut_info[18]+',' + sift+ ',' +gerp_rs+ ',' +gerp_nr+ ',' +logOdds+ ',' +polyPhen2+ ',' +comp_score + ','+gene_aa_mut +',' + str(eachLoc[1])+'\n'
        fhout.write(outline)
        patients = patientDict.keys()
        for eachPatient in patients:
            patientVal = patientDict[eachPatient]
            for eachVal in patientVal:
                readSupport = str(int(eachVal[1]*int(eachVal[2])))
                outline=',,,,,,,,,,,,,,,,,,,,,'+eachPatient+',' +eachVal[0]+','+str(eachVal[1]) + ',' + eachVal[2]+',' + readSupport+'\n'
                fhout.write(outline)
    fhout.close()

##
##                    mut_info.append(info['REF'])
##                    mut_info.append(info['DP'])
##                    mut_info.append(info['Functional_Class'])
##                    mut_info.append(info['Gene_Name'])
##                    mut_info.append(info['Effect'])
##                    mut_info.append(info['Effect_Impact'])
    print 'Finished printing to csv'
    del recurrentMutList, allDeleterious, mutation_info_dict, cosmic, dbSNPClinical

def recurrentMut2CSVPre():
    recurrentMutList = pickle.load(open('common_del_list.pkl', 'rU'))
##    allDeleterious = pickle.load(open('All_deleterious.pkl', 'rU'))
##    mutation_info_dict = pickle.load(open('prim_mutation_info_dict.pkl', 'rU'))
    cosmic = pickle.load(open('cosmic_V60_coding_point_mutations_locations.pkl', 'rU'))
    dbSNP = pickle.load(open('dbSNPcommon_nonClinical.pkl', 'rU'))
    dbSNPLoc = dbSNP.keys()
    del dbSNP

    fhout = open('mutation_recurrence_PREresults.csv', 'w')
    outline = 'CHRM,POS,COSMIC,PT_NAME,ALT,AF,DP' + '\n'
    fhout.write(outline)

    for eachLoc in recurrentMutList:
        if eachLoc not in dbSNPLoc:

            chrm = eachLoc.split('#')[0]
            position = eachLoc.split('#')[1]

            if eachLoc in cosmic:
                cosmic_check = 'Yes'
            else:
                cosmic_check = 'No'
            outline=chrm +','+ position +',' +cosmic_check + '\n'
            fhout.write(outline)

            patientInfo = recurrentMutList[eachLoc]
            for eachPT_info in patientInfo:
                outline=',,,'+ eachPT_info[0] +','+ eachPT_info[1] + ',' + str(eachPT_info[2]) + ',' + str(eachPT_info[3]) +'\n'
                fhout.write(outline)

##
##        patientDict = allDeleterious[eachLoc]
##        mut_info = mutation_info_dict[eachLoc]
##        REF = mut_info[0]
##
##        dp = mut_info[1][0]
##        gene = '#'.join(list(mut_info[3]))
##        effect_impact = '#'.join(list(mut_info[5]))
##
##
##
##        outline=chrm +','+ position +','+REF +','+dp+','+ gene+','+ effect_impact +',' +cosmic_check + '\n'
##        fhout.write(outline)
##        patients = patientDict.keys()
##        for eachPatient in patients:
##            patientVal = patientDict[eachPatient]
##            for eachVal in patientVal:
##                outline=',,,,,,,'+eachPatient+',' +eachVal[0]+','+str(eachVal[1])+'\n'
##                fhout.write(outline)
##    fhout.close()

##
##                    mut_info.append(info['REF'])
##                    mut_info.append(info['DP'])
##                    mut_info.append(info['Functional_Class'])
##                    mut_info.append(info['Gene_Name'])
##                    mut_info.append(info['Effect'])
##                    mut_info.append(info['Effect_Impact'])

        '''Effect ( Effect_Impact | Functional_Class | Codon_Change | Amino_Acid_change|
Amino_Acid_length | Gene_Name | Gene_BioType | Coding | Transcript |
Exon [ | ERRORS | WARNINGS ] )'''
def effProcesser(effList):
    gene_aa_mut = ''

    for each in effList:
        flds = each.split('|')
        gene_aa_mut+= flds[5] + '#' +flds[3] + '|'

    return gene_aa_mut[:-1]

def list2FloatArray(alist):
    floatArray = []
    for each in alist:
        try:

            fScore = float(each)
            floatArray.append(fScore)
        except:
            pass



    return np.array(floatArray)

'''
takes in 2 lists, ALT and AF (in a population) and returns a string of the format
'ALT1=AF1|ALT2=AF2'
'''
def alt_allele_af(alt, af):
    ALT_AF = ''
    for i in range(len(alt)):
        ALT_AF += alt[i] + '='+af[i] +'|'
    return ALT_AF[:-1]




def main():
##    readCosmic('CosmicMutantExport_v60_190712.csv')
##
    readAllMutations()
    mutationRecurrence()
    recurrentMut2CSV()

if __name__ == '__main__':
    main()
