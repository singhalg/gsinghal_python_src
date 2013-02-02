#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     15/05/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import nwalign as nw
from pyfasta import Fasta
from subprocess import Popen, PIPE, STDOUT
import os
import time


def align():
    hg19 = Fasta('hg19.fa')
    print hg19.keys()

    hg19Chr = sorted(hg19.keys(), reverse=True)

    YRI = Fasta('YRIref.fasta')
    print YRI.keys()
    YRIChr = sorted(YRI.keys())
    print hg19[hg19Chr[0]][:20]
    print YRI[YRIChr[0]][:20]

    print hg19[hg19Chr[0]][:20]
    print YRI[YRIChr[0]][:20]

    fhout = open('hg19_YRI_diff.bed', 'w')

    header = 'chrom, chromStart, chromEnd, hg19, YRI \n'
    fhout.write(header)
    for each in hg19Chr:
        seq1 = hg19[each][:10000]
        seq2 = YRI[each][:10000]
        print 'reached 1'
        print 'doing alignment for ', each
        alignment = nw.global_align(seq1, seq2, gap=-2, matrix=None, match=1, mismatch=-1)
        print 'reached 2'
        len1 = len(alignment[0]) #hg19
        len2 = len(alignment[1]) #YRI

        if len2>len1:
            x = len2
        else:
            x = len1

        for i in range(x):
            if alignment[0][i] != alignment[1][i]:
                #write to fhout
                outline = each + ',' + str(i) + ',' + str(i+1) + ',' + alignment[0][i] + ',' + alignment[1][i] + '\n'
                fhout.write(outline)


    fhout.close()

       ## now do stuff with the alignment

def pythonAlign(file1, file2):
    fh1 = open(file1, 'rU')
    data1 = fh1.readlines()
    fh1.close()

    fh2 = open(file2, 'rU')
    data2 = fh2.readlines()
    fh2.close()

    seq1 = ''
    for line in data1[1:]:
        seq1+=line.strip()
    del data1

    seq2 = ''
    for line in data2[2:]:
        seq2+=line.strip()
    del data2
    print len(seq1)
    print len(seq2)
    del seq1, seq2


def runStretcher():
    chroms = []
    for i in range(1, 23):
        chrom = 'chr'+str(i)+'.fa'
        chroms.append(chrom)
    chroms.append('chrX.fa')
    chroms.append('chrY.fa')

    sChroms = sorted(chroms)



    fn = 'stretcher_alignment.log'
    log = open(fn, 'w')






    for each in sChroms:
        file1 = '/scratch/gsinghal/hg19/chrom/'+each
        file2 = '/scratch/gsinghal/alignment/YRI/'+each

        jobname = 'gsinghal_' + each[:-3]+'_stretcher'

        bsName = jobname
        working_dir = "/scratch/gsinghal/stretcher/"

        fhout = open(bsName, 'w')

        options = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=8,walltime=24:00:00,mem=6gb,vmem=15gb \n"+"#PBS -N "+jobname + '\n' + "#PBS -d " + working_dir + '\n' + '#PBS -m be '+'\n'


        fhout.write(options)
        cmd = '/export/emboss-6.4.0/bin/stretcher ' + file1 + '  ' + file2 +'  ' +each[:-3]+'_stretcher_hg19_YRI.fa' + '\n'

        fhout.write(cmd)
        fhout.write('sleep 10')
        fhout.close()
        log.write(cmd)
        log.write('\n')
        runJob = 'qsub '+bsName
        print runJob
        os.system(runJob)
        time.sleep(10)
    log.close()

def tryStretcher():
    chroms = ['10kaa', '20kaa', '40kaa', '80kaa', '160kaa']





    fn = 'try_stretcher_alignment.log'
    log = open(fn, 'w')






    for each in chroms:
        file1 = each
        file2 = each

        jobname = 'gsinghal_' + each[:-2]+'_stretcher'

        bsName = jobname
        working_dir = "/scratch/gsinghal/stretcher/testing/"

        fhout = open(bsName, 'w')

        options = "#!/bin/bash" + '\n'+ "#PBS -l nodes=1:ppn=8,walltime=24:00:00,mem=6gb,vmem=15gb \n"+"#PBS -N "+jobname + '\n' + "#PBS -d " + working_dir + '\n' + '#PBS -m be '+'\n'


        fhout.write(options)
        cmd = '/export/emboss-6.4.0/bin/stretcher ' + file1 + '  ' + file2 +'  ' +each[:-2]+'_stretcher.fa' + '\n'

        fhout.write(cmd)
        fhout.close()
        log.write(cmd)
        log.write('\n')
        runJob = 'qsub '+bsName
        print runJob
        os.system(runJob)
        time.sleep(2)
    log.close()




def main():
##    align()

    pythonAlign('/scratch/gsinghal/hg19/chrom/chr1.fa', '/scratch/gsinghal/alignment/YRI/chr1.fa')
##    runStretcher()
##    tryStretcher()

if __name__ == '__main__':
    main()
