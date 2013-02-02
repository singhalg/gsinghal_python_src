#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     13/06/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, os
from subprocess import Popen, PIPE, STDOUT


def GATKCaller():

    fns = ['GATK_caller1.sh', 'GATK_caller2.sh', 'GATK_caller3.sh', 'GATK_caller4.sh','GATK_caller5.sh','GATK_caller6.sh' ]
    fhs = []
    for afn in fns:
        fh = open(afn, 'w')
        fh.write('#!/bin/bash')
        fh.write('\n')
        fhs.append(fh)

##    depths = [4,8]
    depths1 = [12,16,20,24,28]
    depths2 = [32,36,40,44,48]
    depths3 = [52,60,64,68,76]
    depths4 = [92,96,100]
    depths5 = [104,108,112]
    depths6 = [116,120]
    for i in depths1:
        Picard = "java -jar /export/picard-tools-1.67/AddOrReplaceReadGroups.jar INPUT=pirs_simu_alnS" + str(i) + "x.bam OUTPUT=pirs_simu_alnS_RG" + str(i) + "x.bam RGID=1 RGLB=lb1 RGPL=Illumina RGPU=747 RGSM=pirs_simu_hg19_chr20_" + str(i) +"x RGCN=NL "
        samtools = "samtools index pirs_simu_alnS_RG" + str(i) + "x.bam "
        UniGeno = "java -jar /home/gsinghal/myBin/GenomeAnalysisTK-1.6-11-g3b2fab9/GenomeAnalysisTK.jar -R /scratch/gsinghal/sens/chr20.fa -T UnifiedGenotyper -I pirs_simu_alnS_RG" + str(i) + "x.bam -o GATK_"+str(i)+"x_pre.vcf "
        fhs[0].write(Picard)
        fhs[0].write('\n')
        fhs[0].write(samtools)
        fhs[0].write('\n')
        fhs[0].write(UniGeno)
        fhs[0].write('\n')
        fhs[0].write('sleep 10')
        fhs[0].write('\n')
    fhs[0].close()


    for i in depths2:
        Picard = "java -jar /export/picard-tools-1.67/AddOrReplaceReadGroups.jar INPUT=pirs_simu_alnS" + str(i) + "x.bam OUTPUT=pirs_simu_alnS_RG" + str(i) + "x.bam RGID=1 RGLB=lb1 RGPL=Illumina RGPU=747 RGSM=pirs_simu_hg19_chr20_" + str(i) +"x RGCN=NL "
        samtools = "samtools index pirs_simu_alnS_RG" + str(i) + "x.bam "
        UniGeno = "java -jar /home/gsinghal/myBin/GenomeAnalysisTK-1.6-11-g3b2fab9/GenomeAnalysisTK.jar -R /scratch/gsinghal/sens/chr20.fa -T UnifiedGenotyper -I pirs_simu_alnS_RG" + str(i) + "x.bam -o GATK_"+str(i)+"x_pre.vcf "
        fhs[1].write(Picard)
        fhs[1].write('\n')
        fhs[1].write(samtools)
        fhs[1].write('\n')
        fhs[1].write(UniGeno)
        fhs[1].write('\n')
        fhs[1].write('sleep 10')
        fhs[1].write('\n')

    fhs[1].close()

    for i in depths3:
        Picard = "java -jar /export/picard-tools-1.67/AddOrReplaceReadGroups.jar INPUT=pirs_simu_alnS" + str(i) + "x.bam OUTPUT=pirs_simu_alnS_RG" + str(i) + "x.bam RGID=1 RGLB=lb1 RGPL=Illumina RGPU=747 RGSM=pirs_simu_hg19_chr20_" + str(i) +"x RGCN=NL "
        samtools = "samtools index pirs_simu_alnS_RG" + str(i) + "x.bam "
        UniGeno = "java -jar /home/gsinghal/myBin/GenomeAnalysisTK-1.6-11-g3b2fab9/GenomeAnalysisTK.jar -R /scratch/gsinghal/sens/chr20.fa -T UnifiedGenotyper -I pirs_simu_alnS_RG" + str(i) + "x.bam -o GATK_"+str(i)+"x_pre.vcf "
        fhs[2].write(Picard)
        fhs[2].write('\n')
        fhs[2].write(samtools)
        fhs[2].write('\n')
        fhs[2].write(UniGeno)
        fhs[2].write('\n')
        fhs[2].write('sleep 10')
        fhs[2].write('\n')
    fhs[2].close()

    for i in depths4:
        Picard = "java -jar /export/picard-tools-1.67/AddOrReplaceReadGroups.jar INPUT=pirs_simu_alnS" + str(i) + "x.bam OUTPUT=pirs_simu_alnS_RG" + str(i) + "x.bam RGID=1 RGLB=lb1 RGPL=Illumina RGPU=747 RGSM=pirs_simu_hg19_chr20_" + str(i) +"x RGCN=NL "
        samtools = "samtools index pirs_simu_alnS_RG" + str(i) + "x.bam "
        UniGeno = "java -jar /home/gsinghal/myBin/GenomeAnalysisTK-1.6-11-g3b2fab9/GenomeAnalysisTK.jar -R /scratch/gsinghal/sens/chr20.fa -T UnifiedGenotyper -I pirs_simu_alnS_RG" + str(i) + "x.bam -o GATK_"+str(i)+"x_pre.vcf "
        fhs[3].write(Picard)
        fhs[3].write('\n')
        fhs[3].write(samtools)
        fhs[3].write('\n')
        fhs[3].write(UniGeno)
        fhs[3].write('\n')
        fhs[3].write('sleep 10')
        fhs[3].write('\n')
    fhs[3].close()

    for i in depths5:
        Picard = "java -jar /export/picard-tools-1.67/AddOrReplaceReadGroups.jar INPUT=pirs_simu_alnS" + str(i) + "x.bam OUTPUT=pirs_simu_alnS_RG" + str(i) + "x.bam RGID=1 RGLB=lb1 RGPL=Illumina RGPU=747 RGSM=pirs_simu_hg19_chr20_" + str(i) +"x RGCN=NL "
        samtools = "samtools index pirs_simu_alnS_RG" + str(i) + "x.bam "
        UniGeno = "java -jar /home/gsinghal/myBin/GenomeAnalysisTK-1.6-11-g3b2fab9/GenomeAnalysisTK.jar -R /scratch/gsinghal/sens/chr20.fa -T UnifiedGenotyper -I pirs_simu_alnS_RG" + str(i) + "x.bam -o GATK_"+str(i)+"x_pre.vcf "
        fhs[4].write(Picard)
        fhs[4].write('\n')
        fhs[4].write(samtools)
        fhs[4].write('\n')
        fhs[4].write(UniGeno)
        fhs[4].write('\n')
        fhs[4].write('sleep 10')
        fhs[4].write('\n')

    fhs[4].close()

    for i in depths6:
        Picard = "java -jar /export/picard-tools-1.67/AddOrReplaceReadGroups.jar INPUT=pirs_simu_alnS" + str(i) + "x.bam OUTPUT=pirs_simu_alnS_RG" + str(i) + "x.bam RGID=1 RGLB=lb1 RGPL=Illumina RGPU=747 RGSM=pirs_simu_hg19_chr20_" + str(i) +"x RGCN=NL "
        samtools = "samtools index pirs_simu_alnS_RG" + str(i) + "x.bam "
        UniGeno = "java -jar /home/gsinghal/myBin/GenomeAnalysisTK-1.6-11-g3b2fab9/GenomeAnalysisTK.jar -R /scratch/gsinghal/sens/chr20.fa -T UnifiedGenotyper -I pirs_simu_alnS_RG" + str(i) + "x.bam -o GATK_"+str(i)+"x_pre.vcf "
        fhs[5].write(Picard)
        fhs[5].write('\n')
        fhs[5].write(samtools)
        fhs[5].write('\n')
        fhs[5].write(UniGeno)
        fhs[5].write('\n')
        fhs[5].write('sleep 10')
        fhs[5].write('\n')
    fhs[5].close()

##
    for each in fns:
        cmd = 'bash ' + each
        job = Popen(cmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

def main():
    GATKCaller()

if __name__ == '__main__':
    main()


