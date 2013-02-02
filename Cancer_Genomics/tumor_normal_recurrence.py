#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     29/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys, pickle
from sets import Set
import math

'''
This script works after mutationRecurrence_primary_tumor_normal_fp.py and takes the pickles produced by the previous script and prints out all the data
in a csv format

'''

def primary_metastasis_recurrence():

    recurrentMutList = pickle.load(open('falsePositives_recurrent_mutation_list.pkl', 'rU')) #/////----///---////----
    allDeleterious = pickle.load(open('All_deleterious_falsePositives_rare.pkl', 'rU')) #/////----///---////----

    allDeleteriousMet = pickle.load(open('All_deleterious_metastasis_rare.pkl', 'rU'))

    mutation_info_dict = pickle.load(open('prim_mutation_info_dict_new.pkl', 'rU'))   #/////----///---////----
    cosmic = pickle.load(open('cosmic_V60_coding_Point_mutations_locations.pkl', 'rU'))
    dbSNPClinical = pickle.load(open('dbSNP_clinical.pkl', 'rU')) #////----/////------/////

    fhout = open('mutation_recurrence_prim_metastasis_combined.csv', 'w')
    outline = 'CHRM,POS,REF,GENE,EFFECT_IMPACT,COSMIC,dbSNP_Clinical,ESP_EA,ESP_AFR_A,1000Gp1_AFR,1000Gp1_EUR,1000Gp1_AMR,1000Gp1,SIFT,GERP_RS,GERP_NR,logOdds,PolyPhen2,Composite_Score,Gene#AA,'
    outline+= 'Num_Patients_Primary,PT_1_P,ALT_1_P,AF_1_P,DP_1_P,RS_1_P,PV_1_P,'
    outline+= 'PT_2_P,ALT_2_P,AF_2_P,DP_2_P,RS_2_P,PV_2_P,'
    outline+= 'PT_3_P,ALT_3_P,AF_3_P,DP_3_P,RS_3_P,PV_3_P,'
    outline+= 'PT_6_P,ALT_6_P,AF_6_P,DP_3_P,RS_6_P,PV_6_P,'
    outline+= 'PT_9_P,ALT_9_P,AF_9_P,DP_9_P,RS_9_P,PV_9_P,'
    outline+= 'PT_10_P,ALT_10_P,AF_10_P,DP_10_P,RS_10_P,PV_10_P,'
    outline+= 'PT_11_P,ALT_11_P,AF_11_P,DP_11_P,RS_11_P,PV_11_P,'
    outline+= 'PT_12_P,ALT_12_P,AF_12_P,DP_12_P,RS_12_P,PV_12_P,'
    outline+= 'PT_13_P,ALT_13_P,AF_13_P,DP_13_P,RS_13_P,PV_13_P,'

    outline+= 'Num_Patients_Metastasis,PT_1_M,ALT_1_M,AF_1_M,DP_1_M,RS_1_M,PV_1_M,'
    outline+= 'PT_2_M,ALT_2_M,AF_2_M,DP_2_M,RS_2_M,PV_2_M,'
    outline+= 'PT_3_M,ALT_3_M,AF_3_M,DP_3_M,RS_3_M,PV_3_M,'
    outline+= 'PT_6_M,ALT_6_M,AF_6_M,DP_3_M,RS_6_M,PV_6_M,'
    outline+= 'PT_9_M,ALT_9_M,AF_9_M,DP_9_M,RS_9_M,PV_9_M,'
    outline+= 'PT_10_M,ALT_10_M,AF_10_M,DP_10_M,RS_10_M,PV_10_M,'
    outline+= 'PT_11_M,ALT_11_M,AF_11_M,DP_11_M,RS_11_M,PV_11_M,'
    outline+= 'PT_12_M,ALT_12_M,AF_12_M,DP_12_M,RS_12_M,PV_12_M,'
    outline+= 'PT_13_M,ALT_13_M,AF_13_M,DP_13_M,RS_13_M,PV_13_M,'


    #  ALT_Met,AF_Met,DEPTH_Met,READ_SUPPORT_Met,P_VALUE_Met ' + '\n'
    fhout.write(outline)

    for eachLoc in recurrentMutList:  # we can considering only those mutations which are in prim_recurrent_mutation_list.pkl
        patientDict = allDeleterious[eachLoc[0]]
        if eachLoc[0] in allDeleteriousMet:
            met_patientDict = allDeleteriousMet[eachLoc[0]]
        else:
            met_patientDict = {}

        # mutation info is the same for both primary and metastasis and we are just going to use the info from primary_mutation_info_dict.pkl
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
        prim_patients = Set(patientDict.keys())
        met_patients = Set(met_patientDict.keys())
        patients = prim_patients.union(met_patients)
        for eachPatient in patients:


            if eachPatient in prim_patients:

                prim_patientVal = patientDict[eachPatient]
                prim_readSupport = str(int(prim_patientVal[0][1]*int(prim_patientVal[0][2])))
                try:
                    prim_pValue = str((math.log10(float(prim_patientVal[0][3]))) *-1)
                except:
                    prim_pValue = '0'

            else:
                prim_patientVal = [['NA', 'NA', 'NA', 'NA']]
                prim_readSupport ='NA'
                prim_pValue = 'NA'
            if eachPatient in met_patients:

                met_patientVal = met_patientDict[eachPatient]
                met_readSupport = str(int(met_patientVal[0][1]*int(met_patientVal[0][2])))

                try:
                    met_pValue = str((math.log10(float(met_patientVal[0][3]))) *-1)
                except:
                    met_pValue = '0'

            else:
                met_patientVal = [['NA', 'NA', 'NA', 'NA']]
                met_readSupport = 'NA'
                met_pValue = 'NA'
##            patientVal = patientDict[eachPatient]
##            for eachVal in patientVal:


            outline=',,,,,,,,,,,,,,,,,,,,,'+eachPatient+',' +prim_patientVal[0][0]+','+str(prim_patientVal[0][1]) + ',' + prim_patientVal[0][2]+',' + prim_readSupport +',' + prim_pValue+  ',' +met_patientVal[0][0]+','+str(met_patientVal[0][1]) + ',' + met_patientVal[0][2]+',' + met_readSupport + ',' + met_pValue+ '\n'
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

####################################################################################################

def effProcesser(effList):
    gene_aa_mut = ''

    for each in effList:
        flds = each.split('|')
        gene_aa_mut+= flds[5] + '#' +flds[3] + '|'

    return gene_aa_mut[:-1]



def main():
    primary_metastasis_recurrence()

if __name__ == '__main__':
    main()
