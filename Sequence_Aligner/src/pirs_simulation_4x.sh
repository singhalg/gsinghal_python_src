#!/bin/bash
/home/gsinghal/pIRS2/pirs simulate -i chr20_mutPIRS.snp.indel.invertion.fa -a 0  -x 4 -c 0 -o chr20_pirs4x  
bwa aln -t 4 chr20.fa chr20_pirs4x_100_500_1.fq > simuReads4x_1.sai
sleep 10
bwa aln -t 4 chr20.fa chr20_pirs4x_100_500_2.fq > simuReads4x_2.sai
sleep 10
bwa sampe -a 750  chr20.fa simuReads4x_1.sai simuReads4x_2.sai chr20_pirs4x_100_500_1.fq chr20_pirs4x_100_500_2.fq  >  pirs_simu_aln4x.sam  2>  pirs_simu_aln4x.e 
sleep 10
samtools view -bS  pirs_simu_aln4x.sam  > pirs_simu_aln4x.bam  
sleep 10samtools sort pirs_simu_aln4x.bam  pirs_simu_alnS4x  
