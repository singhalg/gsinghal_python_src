#!/bin/bash
#PBS -l nodes=1:ppn=1,walltime=12:00:00,vmem=42gb 
#PBS -N   PT_2_lung_sorted_MarkDuplicates
#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Alignments_2/MWatson/MWatson/PT_2/lung_1123231/
#PBS -m abe 
java -jar /export/picard-tools-1.67/MarkDuplicates.jar INPUT=PT_2_lung_sorted.bam OUTPUT=PT_2_lung_sorted_rmdup.bam METRICS_FILE=metrics_rmdup.txt REMOVE_DUPLICATES=true ASSUME_SORTED=true 

sleep 10
