#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     30/01/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys





def novoalign():

##    fastqFiles = open('listOfFiles', 'rU').readlines()
    sampleList = open('SJ_renal_dysplasia_bam_files.csv', 'rU').readlines()
    fastq_file_list = open('fastq_files.csv', 'rU').readlines()


    fhoutName = 'NovoAlign_SJ_RENAL_unique.sh'





    fhout = open(fhoutName, 'w')
    options = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=8,walltime=12:00:00,vmem=40gb \n" + "#PBS -N   "+fhoutName[:-3] + '\n' + "#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Validation/ " + '\n' + '#PBS -m abe '+'\n'
    fhout.write(options)
##    fastqFiles = {}


    commandList = []
    for each in fileList:

        bamFile = each.split(',')[0].strip()
        fastqFiles = ' '
        for each in fastq_file_list:
            fq_file = each.strip().strip(',')
            if fq_file.find(bamFile[:-4]) > -1:
                fastqFiles+= fq_file + '   '




##        vcfFile = bamFile[:-4]+'.vcf'




    fhoutName = 'NovoAlign_amplicons.sh'





    fhout = open(fhoutName, 'w')
    options1 = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=8,walltime=12:00:00,vmem=40gb \n" + "#PBS -N   "+fhoutName[:-3] + '\n' + "#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Validation/ " + '\n' + '#PBS -m abe '+'\n'
    fhout.write(options1)

    for eachPair in fastqFiles:
        files = eachPair.strip().split()
        se = files[0].find('_L001')
        sampleName = files[0][:se]

        novoalign_cmd = "/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/validation/all_amplicons.novoindex -f " + files[0] + ' ' + files[1] + "  | /home/gsinghal/bin/samtools view -bS - > " + sampleName +'_amplicon_ref.bam' + '\n'

        print novoalign_cmd

        fhout.write(novoalign_cmd)

        fhout.write('sleep 2')
        fhout.write('\n')
    fhout.close()


def samtools_flagStat():
    fastqFiles = open('listOfFiles', 'rU').readlines()


    fhoutName = 'NovoAlign_amplicons_samtools_flagstat.sh'
    fhout = open(fhoutName, 'w')
    options1 = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=1,walltime=12:00:00,vmem=40gb \n" + "#PBS -N   "+fhoutName[:-3] + '\n' + "#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Validation/ " + '\n' + '#PBS -m abe '+'\n'
    fhout.write(options1)

    for eachPair in fastqFiles:
        files = eachPair.strip().split()
        se = files[0].find('_L001')
        sampleName = files[0][:se]

        samtools_flagstat_cmd = " /home/gsinghal/bin/samtools flagstat "+ sampleName +'_amplicon_ref.bam   >   '+ sampleName+'_amplicon_ref.stats' + '\n'

        print samtools_flagstat_cmd

        fhout.write(samtools_flagstat_cmd)

        fhout.write('sleep 2')
        fhout.write('\n')
    fhout.close()

def stats_comparison():

    fastqFiles = open('listOfFiles', 'rU').readlines()


##    fhoutName = 'NovoAlign_amplicons_samtools_flagstat.sh'
##    fhout = open(fhoutName, 'w')
##    options1 = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=1,walltime=12:00:00,vmem=40gb \n" + "#PBS -N   "+fhoutName[:-3] + '\n' + "#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Validation/ " + '\n' + '#PBS -m abe '+'\n'
##    fhout.write(options1)

    for eachPair in fastqFiles:
        files = eachPair.strip().split()
        se = files[0].find('_L001')
        sampleName = files[0][:se]

        hg19_stats = sampleName+'.stats'

        hg19_stats_data = open(hg19_stats, 'rU').readlines()[2].partition('(')[2][:5]

        amplicon_stats = sampleName+'_amplicon_ref.stats'

        amplicon_stats_data =open(amplicon_stats, 'rU').readlines()[2].partition('(')[2][:5]

        print hg19_stats_data, '  ', amplicon_stats_data


def samtools2VCF():
    fastqFiles = open('listOfFiles', 'rU').readlines()

    fhoutName = 'NovoAlign_samtools_sort_mpileup_vcf.sh'
    fhout = open(fhoutName, 'w')
    options1 = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=8,walltime=12:00:00,vmem=40gb \n" + "#PBS -N   "+fhoutName[:-3] + '\n' + "#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Validation/hg19_Ref/ " + '\n' + '#PBS -m abe '+'\n'
    fhout.write(options1)

    for eachPair in fastqFiles:
        files = eachPair.strip().split()
        se = files[0].find('_L001')
        sampleName = files[0][:se]


        samtools_sort = " /home/gsinghal/bin/samtools sort "+ sampleName +'.bam  '+ sampleName+'_sorted' + '\n'

        fhout.write(samtools_sort)
        fhout.write('sleep 2')
        fhout.write('\n')

        samtools_index =  " /home/gsinghal/bin/samtools index "+ sampleName +'_sorted.bam  '+ '\n'

        fhout.write(samtools_index)
        fhout.write('sleep 2')
        fhout.write('\n')

        mpileup = " /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  "+ sampleName +'_sorted.bam  >  '+ sampleName+'_hg19_ref_mpileup.txt '+ '\n'

        fhout.write(mpileup)
        fhout.write('sleep 2')
        fhout.write('\n')

        VarScanCmd = 'java -jar  ./VarScan.v2.3.2.jar mpileup2snp ' + sampleName +  '_hg19_ref_mpileup.txt ' + '  --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  ' + sampleName + '_hg19_ref.vcf' + '\n'

        fhout.write(VarScanCmd)
        fhout.write('sleep 2')
        fhout.write('\n')


def VarScan_reRun():
    fastqFiles = open('listOfFiles', 'rU').readlines()

    fhoutName = 'VarScan_reRun.sh'
    fhout = open(fhoutName, 'w')
    options1 = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=8,walltime=12:00:00,vmem=40gb \n" + "#PBS -N   "+fhoutName[:-3] + '\n' + "#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Validation/hg19_Ref/ " + '\n' + '#PBS -m abe '+'\n'
    fhout.write(options1)

    for eachPair in fastqFiles:
        files = eachPair.strip().split()
        se = files[0].find('_L001')
        sampleName = files[0][:se]

        VarScanCmd = 'java -jar  ./VarScan.v2.3.2.jar mpileup2snp ' + sampleName +  '_hg19_ref_mpileup.txt ' + '  --min-reads2  2  --min-var-freq  0.01  --p-value  0.05  --output-vcf  >  ' + sampleName + '_hg19_ref_ReRun.vcf' + '\n'

        fhout.write(VarScanCmd)
        fhout.write('sleep 2')
        fhout.write('\n')
    fhout.close()


def main():
##    novoalign()
##    samtools_flagStat()
##    stats_comparison()
##    samtools2VCF()
    VarScan_reRun()
if __name__ == '__main__':
    main()
