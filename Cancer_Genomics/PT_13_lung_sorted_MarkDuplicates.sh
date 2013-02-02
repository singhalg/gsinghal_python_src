#!/bin/bash
#PBS -l nodes=1:ppn=1,walltime=12:00:00,vmem=42gb 
#PBS -N   PT_13_lung_sorted_MarkDuplicates
#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Alignments_2/MWatson/MWatson/PT_13/lung_1202946/
#PBS -m abe 
java -jar /export/picard-tools-1.67/MarkDuplicates.jar INPUT=PT_13_lung_sorted.bam OUTPUT=PT_13_lung_sorted_rmdup.bam METRICS_FILE=metrics_rmdup.txt REMOVE_DUPLICATES=true ASSUME_SORTED=true 

sleep 10
