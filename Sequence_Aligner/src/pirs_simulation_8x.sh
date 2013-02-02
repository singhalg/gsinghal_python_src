#!/bin/bash
/home/gsinghal/pIRS2/pirs simulate -i chr20_mutPIRS.snp.indel.invertion.fa -a 0  -x 8 -c 0 -o chr20_pirs8x  
bwa aln -t 4 chr20.fa chr20_pirs8x_100_500_1.fq > simuReads8x_1.sai
sleep 10
bwa aln -t 4 chr20.fa chr20_pirs8x_100_500_2.fq > simuReads8x_2.sai
sleep 10
bwa sampe -a 750  chr20.fa simuReads8x_1.sai simuReads8x_2.sai chr20_pirs8x_100_500_1.fq chr20_pirs8x_100_500_2.fq  >  pirs_simu_aln8x.sam  2>  pirs_simu_aln8x.e 
sleep 10
samtools view -bS  pirs_simu_aln8x.sam  > pirs_simu_aln8x.bam  
sleep 10samtools sort pirs_simu_aln8x.bam  pirs_simu_alnS8x  
