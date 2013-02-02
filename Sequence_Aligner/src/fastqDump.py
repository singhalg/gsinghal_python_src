#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     21/06/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, os


def fastqDump():

##sralist = ['SRR060192.sra',  'SRR060206.sra',  'SRR060220.sra',  'SRR060234.sra',  'SRR060248.sra',  'SRR060262.sra' , 'SRR060288.sra' , 'SRR060341.sra' , 'SRR060471.sra' , 'SRR060499.sra' , 'SRR064456.sra',
##
##'SRR060193.sra', 'SRR060207.sra',  'SRR060221.sra',  'SRR060235.sra',  SRR060249.sra  SRR060263.sra  SRR060299.sra  SRR060343.sra  SRR060473.sra  SRR060501.sra  SRR064457.sra
##SRR060194.sra  SRR060208.sra  SRR060222.sra  SRR060236.sra  SRR060250.sra  SRR060264.sra  SRR060301.sra  SRR060345.sra  SRR060475.sra  SRR060503.sra  SRR064458.sra
##SRR060195.sra  SRR060209.sra  SRR060223.sra  SRR060237.sra  SRR060251.sra  SRR060265.sra  SRR060303.sra  SRR060348.sra  SRR060477.sra  SRR060505.sra  SRR064459.sra
##SRR060196.sra  SRR060210.sra  SRR060224.sra  SRR060238.sra  SRR060252.sra  SRR060266.sra  SRR060305.sra  SRR060450.sra  SRR060479.sra  SRR060507.sra
##SRR060197.sra  SRR060211.sra  SRR060225.sra  SRR060239.sra  SRR060253.sra  SRR060267.sra  SRR060307.sra  SRR060452.sra  SRR060481.sra  SRR060509.sra
##SRR060198.sra  SRR060212.sra  SRR060226.sra  SRR060240.sra  SRR060254.sra  SRR060269.sra  SRR060309.sra  SRR060454.sra  SRR060483.sra  SRR060511.sra
##SRR060199.sra  SRR060213.sra  SRR060227.sra  SRR060241.sra  SRR060255.sra  SRR060271.sra  SRR060327.sra  SRR060457.sra  SRR060485.sra  SRR060513.sra
##SRR060200.sra  SRR060214.sra  SRR060228.sra  SRR060242.sra  SRR060256.sra  SRR060273.sra  SRR060329.sra  SRR060459.sra  SRR060487.sra  SRR060515.sra
##SRR060201.sra  SRR060215.sra  SRR060229.sra  SRR060243.sra  SRR060257.sra  SRR060275.sra  SRR060331.sra  SRR060461.sra  SRR060489.sra  SRR060517.sra
##SRR060202.sra  SRR060216.sra  SRR060230.sra  SRR060244.sra  SRR060258.sra  SRR060277.sra  SRR060333.sra  SRR060463.sra  SRR060491.sra  SRR064452.sra
##SRR060203.sra  SRR060217.sra  SRR060231.sra  SRR060245.sra  SRR060259.sra  SRR060282.sra  SRR060335.sra  SRR060465.sra  SRR060493.sra  SRR064453.sra
##SRR060204.sra  SRR060218.sra  SRR060232.sra  SRR060246.sra  SRR060260.sra  SRR060284.sra  SRR060337.sra  SRR060467.sra  SRR060495.sra  SRR064454.sra
##SRR060205.sra  SRR060219.sra  SRR060233.sra  SRR060247.sra  SRR060261.sra  SRR060286.sra  SRR060339.sra  SRR060469.sra  SRR060497.sra  SRR064455.sra

    fh  = open('files.txt', 'rU')
    data = fh.readlines()
    i = 0
    filelist1 = ''
    filelist2 = ''
    for each in data[-33:]:

        elements  = each.split(' ')

        filename1 =  elements[-1].strip() + '_1.fastq'
        filename2 =  elements[-1].strip() + '_2.fastq'

##        job = open(jobScript, 'w')
##        options = "#!/bin/bash "  + '\n'+ "#PBS -l nodes=1:ppn=1,walltime=1:00:00,mem=12gb"  + '\n'+ "#PBS -N "+ jobScript  + '\n' + "#PBS -d /scratch/gsinghal/Marjolein/SRA/" +'\n'
##        job.write(options)
##        cmd = 'fastq-dump -A ' + filename + '\n'
##        job.write(cmd)
##        job.write('sleep 10')
##        job.write('\n')
##        job.close()
##        qsub = 'qsub '+ jobScript
##        os.system(qsub)
        filelist1 += filename1 + ','
        filelist2 += filename2 + ','
##        print filename
##        print i
        i+=1

    print filelist1
    print filelist2

    options1 = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=48,walltime=12:00:00,mem=24gb" + '\n'+ "#PBS -N gsinghal_Marjolein_paired2_bowtie2" + '\n' + "#PBS -d /scratch/gsinghal/Marjolein/fastq/Paired/" + '\n' + '#PBS -m abe '+'\n' +'#PBS -q dque_smp ' +'\n'

    jobScript = 'Marjolein_paired2_bowtie2.sh'
    job = open(jobScript, 'w')
    job.write(options1)
    cmd = 'bowtie2 -p 48  --sensitive -x hg19 -1 ' + filelist1[:-1] + ' -2 '+ filelist2[:-1] + ' -S Marjolein_paired2.sam &> Marjolein_paired2_bowtie2.txt'
    job.write(cmd)
    job.write('\n')
    job.write('sleep 10')
    job.close()




def main():
    fastqDump()

if __name__ == '__main__':
    main()
