#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     17/01/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys


def collectStats(ind, stats, tissue):
    files = [   ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],
                ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                [ 'PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']  ]

    for each in files:
        print each[ind]
        end = each[ind].find('_lung')
        pt_name = each[ind][:end]


        fhname = pt_name + stats
        data = open(fhname, 'rU').readlines()
        fhoutName = pt_name + tissue + stats+ '.csv'
        fhout = open(fhoutName, 'w')
        outline = pt_name + ',' + '\n'
        fhout.write(outline)

        for line in data:
            flds = line.split()
            fhout.write(flds[0]+',' + '\n')
        fhout.close()


def assimilate_data():


    files = [   ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],
                ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                [ 'PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']  ]
    tissue = ['lung', 'brain']
    stats = ['all.stats', 'exons.stats']

    all_Patients_all_stats = {}
    fhout = open('all_patients_all_stats.csv', 'w')
    for each in files:
        print each[0]
        end = each[0].find('_lung')
        pt_name = each[0][:end]
        tissue_dict = {}

        for eachTissue in tissue:
            stat_dict = {}
            for eachStat in stats:
                fileName = pt_name  + '_' + eachTissue + '_' + eachStat + '.csv'

                data = open(fileName, 'rU').readlines()

                numbers = []

                for line in data[1:]:
                    flds = line.strip().strip(',')
                    numbers.append(int(flds))
                stat_dict[eachStat] = numbers

                tissue_dict[eachTissue] = stat_dict
                all_Patients_all_stats[pt_name] = tissue_dict


    for eachPT in all_Patients_all_stats.keys():
        tissueDict = all_Patients_all_stats[eachPT]
        for eachTissue in tissueDict.keys():
            statDict = tissueDict[eachTissue]
            for eachStat in statDict.keys():
                print eachPT, ' : ', eachTissue, '  : ', eachStat, " : ", statDict[eachStat]

    return all_Patients_all_stats



def print_all_stats():
    all_stats =assimilate_data()
    tags = ''
    total_reads = ''
    mapped_reads = ''
    percent_read_mapped = ''
    mapped2exons = ''
    percent_exon_mapped = ''
    paired = ''

    tissue = ['lung', 'brain']
    for eachPT in all_stats.keys():
        for eachTissue in tissue:
            header = eachPT + '_' + eachTissue
            tags +=header + ','

            total = all_stats[eachPT][eachTissue]['all.stats'][0]
            total_reads += str(total)+','

            mapped = all_stats[eachPT][eachTissue]['all.stats'][2]
            mapped_reads += str(mapped)  + ','

            percentMapped = round(((100.00*mapped)/total), 2)
            percent_read_mapped += str(percentMapped) + ','

            exonMapped = all_stats[eachPT][eachTissue]['exons.stats'][0]
            mapped2exons += str(exonMapped) + ','

            percentExonMapped = round(((100.00*exonMapped)/total), 2)
            percent_exon_mapped+= str(percentExonMapped) + ','

            paired_reads = all_stats[eachPT][eachTissue]['exons.stats'][5]
            paired+= str(paired_reads) + ','

    fhout = open('all_patients_all_stats.csv', 'w')
    fhout.write(tags + '\n')
    fhout.write(total_reads + '\n')
    fhout.write(mapped_reads + '\n')
    fhout.write(percent_read_mapped + '\n')

    fhout.write(mapped2exons + '\n')
    fhout.write(percent_exon_mapped + '\n')
    fhout.write(paired + '\n')
    fhout.close()





def main():
##    index = sys.argv[1]
##    stats = sys.argv[2]
##    tissue = sys.argv[3]
##
##    ind = int(index)
##    collectStats(ind, stats, tissue)

##    assimilate_data()
    print_all_stats()

if __name__ == '__main__':
    main()
