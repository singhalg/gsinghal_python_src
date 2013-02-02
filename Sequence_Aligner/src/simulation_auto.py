#-------------------------------------------------------------------------------
# Name:        simulation_auto
# Purpose:
#
# Author:      gsinghal
#
# Created:     07/06/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, os
from subprocess import Popen, PIPE, STDOUT
import psutil as PS

def pirsSimuAuto():
    scripts = []

    for i in range (15,31):
        depth = 4*i
        ssname = 'pirs_simulation_' + str(depth) +'x.sh'
        scripts.append(ssname)
        fh = open(ssname, 'w')
        options = "#!/bin/bash"  + '\n'+ "#PBS -l nodes=1:ppn=8,walltime=12:00:00,mem=5gb "  + '\n'+ "#PBS -N "+ ssname[:-3]  + '\n' + "#PBS -d /scratch/gsinghal/sens/" +'\n'
        fh.write(options)

##        simulate_reads = '/home/gsinghal/pIRS2/pirs simulate -i chr20_mutPIRS.snp.indel.invertion.fa -a 0  -x ' + str(depth) +' -c 0 -o chr20_pirs'+str(depth)+'x  2> ' +str(depth)+'x_pirs_simulate.e  '+ '\n'
##
##        fh.write(simulate_reads)
        readfile1 = 'chr20_pirs'+str(depth)+'x_100_500_1.fq'
        readfile2 = 'chr20_pirs'+str(depth)+'x_100_500_2.fq'

        unzip1 = 'gunzip ' + readfile1+'.gz'
        fh.write(unzip1)
        fh.write('\n')

        unzip2 = 'gunzip '+ readfile2 + '.gz'
        fh.write(unzip2)
        fh.write('\n')

        sai1 = 'simuReads' + str(depth)+'x_1.sai'
        sai2 = 'simuReads' + str(depth)+'x_2.sai'

        align1 = 'bwa aln -t 6 chr20.fa '+readfile1 + ' > ' + sai1
        align2 = 'bwa aln -t 6 chr20.fa '+readfile2 + ' > ' + sai2

        fh.write(align1)
        fh.write('\n')
        fh.write('sleep 10')
        fh.write('\n')
        fh.write(align2)
        fh.write('\n')
        fh.write('sleep 10')
        fh.write('\n')
        alignment = 'bwa sampe -a 750  chr20.fa ' + sai1 + ' ' + sai2 + ' ' + readfile1+ ' ' + readfile2 + '  >  pirs_simu_aln'+str(depth)+'x.sam  2>  pirs_simu_aln'+str(depth) + 'x.e '

        fh.write(alignment)
        fh.write('\n')
        fh.write('sleep 10')
        fh.write('\n')

        samtools = 'samtools view -bS  pirs_simu_aln'+str(depth)+'x.sam  > pirs_simu_aln' + str(depth)+'x.bam  ' + '\n'
        fh.write(samtools)

        removeSam = 'rm pirs_simu_aln' + str(depth)+'x.sam  '
        fh.write(removeSam)
        fh.write('\n')

        samtools_sort = 'samtools sort pirs_simu_aln' + str(depth)+'x.bam  pirs_simu_alnS'+str(depth)+'x  ' + '\n'
        fh.write(samtools_sort)

        removeBam = 'rm pirs_simu_aln' + str(depth)+'x.bam  '
        fh.write(removeBam)
        fh.write('\n')
        fh.write('sleep 10')
        fh.write('\n')

        compression = 'gzip '+ readfile1
        fh.write(compression)
        fh.write('\n')

        compression = 'gzip '+ readfile2
        fh.write(compression)
        fh.write('\n')


        fh.write('sleep 10')
        fh.write('\n')

##        folder = str(depth)+'x'
##        mkdir = 'mkdir ' + folder + '  \n'
##        move = 'mv *' + folder + '?*  ./' + folder + "/ \n"
##
##        fh.write(mkdir)
##        fh.write(move)

    for each in scripts:
        cmd = 'qsub ' + each
        job = Popen(cmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)



def variantCalling(num):

    depth = int(num)
    fn = 'variantCalling' + num + 'x.sh'
    fh = open(fn, 'w')
    options = "#!/bin/bash "  + '\n'+ "#PBS -l nodes=1:ppn=4,walltime=12:00:00,mem=4gb "  + '\n'+ "#PBS -N "+ fn[:-3]  + '\n' + "#PBS -d /scratch/gsinghal/sens/bams" +'\n'
    fh.write(options)


    cmd1 = 'samtools mpileup -ugf chr20.fa  pirs_simu_alnS' +str(depth)+'x.bam   | bcftools view -bvcg - >  var.raw' + str(depth) + '.bcf'
    print cmd1

    fh.write(cmd1)
    fh.write('\n')
##    job = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
##    job.wait()

    cmd2 = 'bcftools view var.raw' + str(depth) + '.bcf | vcfutils.pl varFilter -D ' + str(depth*2) + ' > var.flt' +str(depth)+'.vcf'
    print cmd2

    fh.write(cmd2)
    fh.write('\n')

##    job = Popen(cmd2, shell=True,  stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    fh.write('sleep 10')
    fh.close()

    comm = 'qsub ' + fn
##    os.system(comm)

'''
samtools mpileup -ugf ref.fa aln.bam | bcftools view -bvcg - > var.raw.bcf
bcftools view var.raw.bcf | vcfutils.pl varFilter -D 100 > var.flt.vcf '''





def main():
##    pirsSimuAuto()
    num = sys.argv[1]
    variantCalling(num)
if __name__ == '__main__':
    main()
