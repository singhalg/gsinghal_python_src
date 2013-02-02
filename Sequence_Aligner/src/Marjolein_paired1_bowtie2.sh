#!/bin/bash
#PBS -l nodes=1:ppn=48,walltime=12:00:00,mem=18gb
#PBS -N gsinghal_Marjolein_unpaired_bowtie2
#PBS -d /scratch/gsinghal/Marjolein/fastq/Unpaired/
#PBS -m abe 
#PBS -q dque_smp 
tie2 -p 48  --sensitive -x hg19 -1 SRR060469.sra_1.fastq,SRR060471.sra_1.fastq,SRR060473.sra_1.fastq,SRR060475.sra_1.fastq,SRR060477.sra_1.fastq,SRR060479.sra_1.fastq,SRR060481.sra_1.fastq,SRR060483.sra_1.fastq,SRR060485.sra_1.fastq,SRR060487.sra_1.fastq,SRR060489.sra_1.fastq,SRR060491.sra_1.fastq,SRR060493.sra_1.fastq,SRR060495.sra_1.fastq,SRR060497.sra_1.fastq,SRR060499.sra_1.fastq,SRR060501.sra_1.fastq,SRR060503.sra_1.fastq,SRR060505.sra_1.fastq,SRR060507.sra_1.fastq,SRR060509.sra_1.fastq,SRR060511.sra_1.fastq,SRR060513.sra_1.fastq,SRR060515.sra_1.fastq,SRR060517.sra_1.fastq,SRR064452.sra_1.fastq,SRR064453.sra_1.fastq,SRR064454.sra_1.fastq,SRR064455.sra_1.fastq,SRR064456.sra_1.fastq,SRR064457.sra_1.fastq,SRR064458.sra_1.fastq,SRR064459.sra_1.fastq -2 SRR060469.sra_2.fastq,SRR060471.sra_2.fastq,SRR060473.sra_2.fastq,SRR060475.sra_2.fastq,SRR060477.sra_2.fastq,SRR060479.sra_2.fastq,SRR060481.sra_2.fastq,SRR060483.sra_2.fastq,SRR060485.sra_2.fastq,SRR060487.sra_2.fastq,SRR060489.sra_2.fastq,SRR060491.sra_2.fastq,SRR060493.sra_2.fastq,SRR060495.sra_2.fastq,SRR060497.sra_2.fastq,SRR060499.sra_2.fastq,SRR060501.sra_2.fastq,SRR060503.sra_2.fastq,SRR060505.sra_2.fastq,SRR060507.sra_2.fastq,SRR060509.sra_2.fastq,SRR060511.sra_2.fastq,SRR060513.sra_2.fastq,SRR060515.sra_2.fastq,SRR060517.sra_2.fastq,SRR064452.sra_2.fastq,SRR064453.sra_2.fastq,SRR064454.sra_2.fastq,SRR064455.sra_2.fastq,SRR064456.sra_2.fastq,SRR064457.sra_2.fastq,SRR064458.sra_2.fastq,SRR064459.sra_2.fastq -S Marjolein_paired1.sam &> Marjolein_paired1_bowtie2.txt
sleep 10