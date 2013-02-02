#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     14/01/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

"/home/gsinghal/myBin/BEDTools-Version-2.16.2/bin/intersectBed -abam  "

"/BlueArc-scratch/gsinghal/MWatson/Targets/TruSeq_exome_targeted_regions.bed"

"/BlueArc-scratch/gsinghal/MWatson/Targets/SureSelect_All_Exon_50mb_merged.hg19.bed"

"/BlueArc-scratch/gsinghal/MWatson/Targets/SureSelect_V4_All_Exon_51mb_with_annotation.hg19.bed"

import sys


# tissue = '_lung' or '_brain'

def runExomeStats(ind, tissue):
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
        end = each[ind].find(tissue)
        folder_end = each[ind].find('.vcf')
        inputfileName = each[ind][:end] +tissue +'_sorted_rmdup.bam'

        print inputfileName

        if each[ind][:end] == "PT_1":
            target_bed = "/BlueArc-scratch/gsinghal/MWatson/Targets/TruSeq_exome_targeted_regions.bed"
        elif (each[ind][:end] =="PT_2") or (each[ind][:end] =="PT_3") or (each[ind][:end] =="PT_6") or (each[ind][:end] =="PT_13") :

            target_bed = "/BlueArc-scratch/gsinghal/MWatson/Targets/SureSelect_V4_All_Exon_51mb_with_annotation.hg19.bed"

        elif (each[ind][:end] =="PT_9") or (each[ind][:end] =="PT_10") or (each[ind][:end] =="PT_11") or (each[ind][:end] =="PT_12") :
            target_bed = "/BlueArc-scratch/gsinghal/MWatson/Targets/SureSelect_All_Exon_50mb_merged.hg19.bed"

        wd= "/BlueArc-scratch/gsinghal/MWatson/Alignments_2/MWatson/MWatson/" + each[ind][:end] +  "/"+each[ind][end+1:folder_end] + "/"

        targetExome = each[ind][:end]+'_exome.bam'

        jobcmd1 = "/home/gsinghal/myBin/BEDTools-Version-2.16.2/bin/intersectBed -abam " + inputfileName + " -b " + target_bed + "  >  " + targetExome + '\n'

        jobcmd2 = "/home/gsinghal/bin/samtools flagstat " + inputfileName + " > " + each[ind][:end] + "_all.stats" + '\n'

        jobcmd3 = "/home/gsinghal/bin/samtools flagstat " + targetExome + " > " + each[ind][:end] + "_exons.stats" + '\n'

        fhoutName = inputfileName[:-4] + '_runExomeStats.sh'
        fhout = open(fhoutName, 'w')

        options1 = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=1,walltime=12:00:00,vmem=42gb \n" + "#PBS -N   "+fhoutName[:-3] + '\n' + "#PBS -d  " + wd + '\n' + '#PBS -m abe '+'\n'  ##---///---///---

        fhout.write(options1)
        fhout.write(jobcmd1)
        fhout.write(jobcmd2)
        fhout.write(jobcmd3)
        fhout.write('\n')
        fhout.write('sleep 10')
        fhout.write('\n')
        fhout.close()




def main():
    runExomeStats(1, '_brain')

if __name__ == '__main__':
    main()
