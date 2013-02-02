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
import pickle

'''
This method takes in the csv file containing coding point mutations in COSMIC and saves a pickle which contains all the locations of point mutations.
Once we have these locations, we will see if any of the recurrent mutations in our data set is also present in the COSMIC
'''
def readCosmic(cosmicFile):
    fh = open(cosmicFile, 'rU')
    data = fh.readlines()
    fh.close()
    mut_loc = Set([])
    for line in data[1:100]:
        flds = line.split(',')
        chrom = flds[19].partition(':')[0]
        pos = flds[19].partition('-')[2]
        loc = chrom + '#' + pos
        mut_loc.add(loc)

##    print mut_loc

    fhPickle = open('cosmic_V60_coding_Point_mutations_locations.pkl', 'w')
    pickle.dump(mut_loc, fhPickle)


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


    # considering mutations only in primary tumors.
    allDeleterious = {}  # here we are considering only deleterious mutations and only in primary tumors.

    mutation_info_dict = {}

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

            if eachLoc in delMutLocations:
                if eachLoc not in mutation_info_dict:
                    info = delMutationsPrimary[eachLoc]
                    mut_info = []
                    mut_info.append(info['REF'])
                    mut_info.append(info['DP'])
                    mut_info.append(info['Functional_Class'])
                    mut_info.append(info['Gene_Name'])
                    mut_info.append(info['Effect'])
                    mut_info.append(info['Effect_Impact'])
                    mutation_info_dict[eachLoc] = mut_info

            for i in range(len(AF)):
                if (float(AF[i]) >= 0.1) and (int(DP[0])>=20):

                    if eachLoc not in allDeleterious:
                        patientDict = {}
                        patientDict[patientName] = [[ALT[i], float(AF[i])]]
##                            newVal = [[patientName, ALT[i], float(AF[i]), DP[0]]]
                        allDeleterious[eachLoc] = patientDict

                    else:
                        patientDict = allDeleterious[eachLoc] # this patientDict should be of the form {PT_name:[ [ALT1, AF1], [ALT2, AF2]]}
                        if patientName in patientDict:
                            patientVal = patientDict[patientName]  # here we update the patientDict
                            patientVal.append([ALT[i], float(AF[i])])
                            patientDict[patientName] = patientVal
                        else:
                            newPatientVal = [[ALT[i], float(AF[i])]]
                            patientDict[patientName] = newPatientVal
                        allDeleterious[eachLoc] = patientDict


        del delMutationsPrimary, delMutLocations


    allDeleteriousPickle = open('All_deleterious.pkl', 'w')
    pickle.dump(allDeleterious, allDeleteriousPickle)
    allDeleteriousPickle.close()

    mut_info_pickle = open('prim_mutation_info_dict.pkl', 'w')
    pickle.dump(mutation_info_dict, mut_info_pickle)
    mut_info_pickle.close()




def mutationRecurrence():
    commonEVS = pickle.load(open('commonEVS.pkl', 'rU'))
    agilentCommon = pickle.load(open('agilent_V3_common.pkl', 'rU'))
    IlluminaCommon = pickle.load(open('Illumina_common.pkl', 'rU'))
    Illumina_agilent = pickle.load(open('Illumina_Agilent_common.pkl', 'rU'))
    dbSNP           = pickle.load(open('dbSNPcommon_nonClinical.pkl', 'rU'))

    dbSNPcommon = Set(dbSNP.keys())
    del dbSNP

    allCommon = commonEVS | agilentCommon | IlluminaCommon | Illumina_agilent | dbSNPcommon




    fhAllDeleterious = open('All_deleterious.pkl', 'rU')
    allDeleterious = pickle.load(fhAllDeleterious)
    fhAllDeleterious.close()

    allDelList = []
    locations = allDeleterious.keys()
    for eachLoc in locations:
        if eachLoc not in allCommon: # here, we are taking only those locations which are not present in any of the internal or external common snps
            patientDict = allDeleterious[eachLoc]
            allDelList.append([eachLoc, len(patientDict.keys())])
            del patientDict


    allDelListSorted = sorted(allDelList, reverse=True, key = myFun) # these are mutations which are not common SNPS and sorted by their recurrence.

    fhRecurrentMutList = open('recurrent_mutation_list.pkl', 'w')
    pickle.dump(allDelListSorted, fhRecurrentMutList)
    fhRecurrentMutList.close()

    count = 0
    for eachMostRecurrent in allDelListSorted[:100]:
##        if (int(eachMostRecurrent[1][0][3])>100) :
        print eachMostRecurrent, '   # of patients having this mutation = ', eachMostRecurrent[1]



def myFun(alist):
    return alist[1]




def recurrentMut2CSV():
    recurrentMutList = pickle.load(open('recurrent_mutation_list.pkl', 'rU'))
    allDeleterious = pickle.load(open('All_deleterious.pkl', 'rU'))
    mutation_info_dict = pickle.load(open('prim_mutation_info_dict.pkl', 'rU'))
    cosmic = pickle.load(open('cosmic_V60_coding_point_mutations_locations.pkl', 'rU'))
    dbSNPClinical = pickle.load(open('dbSNP_clinical.pkl', 'rU'))

    fhout = open('mutation_recurrence_results.csv', 'w')
    outline = 'CHRM,POS,REF,DEPTH,GENE,EFFECT_IMPACT,COSMIC,PT_NAME,ALT,AF' + '\n'
    fhout.write(outline)

    for eachLoc in recurrentMutList:
        patientDict = allDeleterious[eachLoc]
        mut_info = mutation_info_dict[eachLoc]
        REF = mut_info[0]
        chrm = eachLoc.split('#')[0]
        position = eachLoc.split('#')[1]
        dp = mut_info[1][0]
        gene = '#'.join(list(mut_info[3]))
        effect_impact = '#'.join(list(mut_info[5]))

        if eachLoc in cosmic:
            cosmic_check = 'Yes'
        else:
            cosmic_check = 'No'


        outline=chrm +','+ position +','+REF +','+dp+','+ gene+','+ effect_impact +',' +cosmic_check + '\n'
        fhout.write(outline)
        patients = patientDict.keys()
        for eachPatient in patients:
            patientVal = patientDict[eachPatient]
            for eachVal in patientVal:
                outline=',,,,,,,'+eachPatient+',' +eachVal[0]+','+str(eachVal[1])+'\n'
                fhout.write(outline)
    fhout.close()

##
##                    mut_info.append(info['REF'])
##                    mut_info.append(info['DP'])
##                    mut_info.append(info['Functional_Class'])
##                    mut_info.append(info['Gene_Name'])
##                    mut_info.append(info['Effect'])
##                    mut_info.append(info['Effect_Impact'])


def recurrentMut2CSVPre():
    recurrentMutList = pickle.load(open('common_del_list.pkl', 'rU'))
##    allDeleterious = pickle.load(open('All_deleterious.pkl', 'rU'))
##    mutation_info_dict = pickle.load(open('prim_mutation_info_dict.pkl', 'rU'))
    cosmic = pickle.load(open('cosmic_V60_coding_point_mutations_locations.pkl', 'rU'))
    dbSNP = pickle.load(open('dbSNPcommon_nonClinical.pkl', 'rU'))
    dbSNPLoc = dbSNP.keys()

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




def main():
##    readCosmic('CosmicMutantExport_v60_190712.csv')

##    readAllMutations()
##    mutationRecurrence()
    recurrentMut2CSVPre()

if __name__ == '__main__':
    main()
