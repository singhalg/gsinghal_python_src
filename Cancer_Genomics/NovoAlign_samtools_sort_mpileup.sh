#!/bin/bash
#PBS -l nodes=1:ppn=1,walltime=12:00:00,vmem=40gb 
#PBS -N   NovoAlign_samtools_sort_mpileup
#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Validation/hg19_Ref/ 
#PBS -m abe 
 /home/gsinghal/bin/samtools sort 1123226_S58.bam   >   1123226_S58_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1123226_S58_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1123226_S58_sorted.bam  >  1123226_S58_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1123226_S58_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1123226_S58_hg19_ref.vcf
sleep 2
