#!/bin/bash
#PBS -l nodes=1:ppn=48,walltime=12:00:00,mem=18gb
#PBS -N gsinghal_Marjolein_unpaired_bowtie2
#PBS -d /scratch/gsinghal/Marjolein/fastq/Unpaired/
#PBS -m abe 
#PBS -q dque_smp 
bowtie2 -p 48  --sensitive -x hg19 -U SRR060267.sra.fastq,SRR060269.sra.fastq,SRR060271.sra.fastq,SRR060273.sra.fastq,SRR060275.sra.fastq,SRR060277.sra.fastq,SRR060282.sra.fastq,SRR060284.sra.fastq,SRR060286.sra.fastq,SRR060288.sra.fastq,SRR060299.sra.fastq,SRR060301.sra.fastq,SRR060303.sra.fastq,SRR060305.sra.fastq,SRR060307.sra.fastq,SRR060309.sra.fastq,SRR060327.sra.fastq,SRR060329.sra.fastq,SRR060331.sra.fastq,SRR060333.sra.fastq,SRR060335.sra.fastq,SRR060337.sra.fastq,SRR060339.sra.fastq,SRR060341.sra.fastq,SRR060343.sra.fastq,SRR060345.sra.fastq,SRR060348.sra.fastq,SRR060450.sra.fastq,SRR060452.sra.fastq,SRR060454.sra.fastq,SRR060457.sra.fastq,SRR060459.sra.fastq,SRR060461.sra.fastq,SRR060463.sra.fastq,SRR060465.sra.fastq,SRR060467.sra.fastq -S Marjolein_unpaired.sam &> Marjolein_unpaired_bowtie2.txt
sleep 10