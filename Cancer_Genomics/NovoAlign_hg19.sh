#!/bin/bash
#PBS -l nodes=1:ppn=8,walltime=12:00:00,vmem=40gb 
#PBS -N   NovoAlign_hg19
#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Validation/ 
#PBS -m abe 
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1123226_S58_L001_R1_001.fastq 1123226_S58_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1123226_S58.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1123226_S64_L001_R1_001.fastq 1123226_S64_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1123226_S64.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1123227_S59_L001_R1_001.fastq 1123227_S59_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1123227_S59.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1123227_S65_L001_R1_001.fastq 1123227_S65_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1123227_S65.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1123231_S57_L001_R1_001.fastq 1123231_S57_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1123231_S57.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1123231_S63_L001_R1_001.fastq 1123231_S63_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1123231_S63.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1123233_S56_L001_R1_001.fastq 1123233_S56_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1123233_S56.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1123233_S62_L001_R1_001.fastq 1123233_S62_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1123233_S62.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1200370_S60_L001_R1_001.fastq 1200370_S60_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1200370_S60.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1200370_S66_L001_R1_001.fastq 1200370_S66_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1200370_S66.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1230318_S3_L001_R1_001.fastq 1230318_S3_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1230318_S3.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1230318_S67_L001_R1_001.fastq 1230318_S67_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1230318_S67.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1230319_S72_L001_R1_001.fastq 1230319_S72_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1230319_S72.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1230319_S8_L001_R1_001.fastq 1230319_S8_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1230319_S8.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1230386_S71_L001_R1_001.fastq 1230386_S71_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1230386_S71.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1230386_S7_L001_R1_001.fastq 1230386_S7_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1230386_S7.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1230389_S73_L001_R1_001.fastq 1230389_S73_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1230389_S73.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1230389_S9_L001_R1_001.fastq 1230389_S9_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1230389_S9.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1230390_S10_L001_R1_001.fastq 1230390_S10_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1230390_S10.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1230390_S74_L001_R1_001.fastq 1230390_S74_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1230390_S74.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1230391_S11_L001_R1_001.fastq 1230391_S11_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1230391_S11.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1230391_S75_L001_R1_001.fastq 1230391_S75_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1230391_S75.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233400_S12_L001_R1_001.fastq 1233400_S12_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233400_S12.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233400_S76_L001_R1_001.fastq 1233400_S76_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233400_S76.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233401_S4_L001_R1_001.fastq 1233401_S4_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233401_S4.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233401_S68_L001_R1_001.fastq 1233401_S68_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233401_S68.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233402_S13_L001_R1_001.fastq 1233402_S13_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233402_S13.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233402_S77_L001_R1_001.fastq 1233402_S77_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233402_S77.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233403_S14_L001_R1_001.fastq 1233403_S14_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233403_S14.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233403_S78_L001_R1_001.fastq 1233403_S78_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233403_S78.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233404_S15_L001_R1_001.fastq 1233404_S15_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233404_S15.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233404_S79_L001_R1_001.fastq 1233404_S79_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233404_S79.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233405_S16_L001_R1_001.fastq 1233405_S16_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233405_S16.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233405_S80_L001_R1_001.fastq 1233405_S80_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233405_S80.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233406_S17_L001_R1_001.fastq 1233406_S17_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233406_S17.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233406_S81_L001_R1_001.fastq 1233406_S81_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233406_S81.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233418_S18_L001_R1_001.fastq 1233418_S18_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233418_S18.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233418_S82_L001_R1_001.fastq 1233418_S82_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233418_S82.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233419_S19_L001_R1_001.fastq 1233419_S19_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233419_S19.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233419_S83_L001_R1_001.fastq 1233419_S83_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233419_S83.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233420_S20_L001_R1_001.fastq 1233420_S20_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233420_S20.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233420_S84_L001_R1_001.fastq 1233420_S84_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233420_S84.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233421_S21_L001_R1_001.fastq 1233421_S21_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233421_S21.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233421_S85_L001_R1_001.fastq 1233421_S85_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233421_S85.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233422_S22_L001_R1_001.fastq 1233422_S22_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233422_S22.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233422_S86_L001_R1_001.fastq 1233422_S86_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233422_S86.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233423_S23_L001_R1_001.fastq 1233423_S23_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233423_S23.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233423_S87_L001_R1_001.fastq 1233423_S87_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233423_S87.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233424_S24_L001_R1_001.fastq 1233424_S24_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233424_S24.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233424_S88_L001_R1_001.fastq 1233424_S88_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233424_S88.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233425_S25_L001_R1_001.fastq 1233425_S25_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233425_S25.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233425_S89_L001_R1_001.fastq 1233425_S89_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233425_S89.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233426_S26_L001_R1_001.fastq 1233426_S26_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233426_S26.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233426_S90_L001_R1_001.fastq 1233426_S90_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233426_S90.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233427_S27_L001_R1_001.fastq 1233427_S27_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233427_S27.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233427_S91_L001_R1_001.fastq 1233427_S91_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233427_S91.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233428_S28_L001_R1_001.fastq 1233428_S28_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233428_S28.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233428_S92_L001_R1_001.fastq 1233428_S92_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233428_S92.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233429_S29_L001_R1_001.fastq 1233429_S29_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233429_S29.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233429_S93_L001_R1_001.fastq 1233429_S93_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233429_S93.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233430_S30_L001_R1_001.fastq 1233430_S30_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233430_S30.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233430_S94_L001_R1_001.fastq 1233430_S94_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233430_S94.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233431_S31_L001_R1_001.fastq 1233431_S31_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233431_S31.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233431_S95_L001_R1_001.fastq 1233431_S95_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233431_S95.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233432_S32_L001_R1_001.fastq 1233432_S32_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233432_S32.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233432_S96_L001_R1_001.fastq 1233432_S96_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233432_S96.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233433_S33_L001_R1_001.fastq 1233433_S33_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233433_S33.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233433_S97_L001_R1_001.fastq 1233433_S97_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233433_S97.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233434_S34_L001_R1_001.fastq 1233434_S34_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233434_S34.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233434_S98_L001_R1_001.fastq 1233434_S98_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233434_S98.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233435_S35_L001_R1_001.fastq 1233435_S35_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233435_S35.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233436_S36_L001_R1_001.fastq 1233436_S36_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233436_S36.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233437_S37_L001_R1_001.fastq 1233437_S37_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233437_S37.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233438_S38_L001_R1_001.fastq 1233438_S38_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233438_S38.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233439_S39_L001_R1_001.fastq 1233439_S39_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233439_S39.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233440_S40_L001_R1_001.fastq 1233440_S40_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233440_S40.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233441_S5_L001_R1_001.fastq 1233441_S5_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233441_S5.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233441_S69_L001_R1_001.fastq 1233441_S69_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233441_S69.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233442_S41_L001_R1_001.fastq 1233442_S41_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233442_S41.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233443_S42_L001_R1_001.fastq 1233443_S42_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233443_S42.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233444_S43_L001_R1_001.fastq 1233444_S43_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233444_S43.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233445_S44_L001_R1_001.fastq 1233445_S44_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233445_S44.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233446_S6_L001_R1_001.fastq 1233446_S6_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233446_S6.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233446_S70_L001_R1_001.fastq 1233446_S70_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233446_S70.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233447_S45_L001_R1_001.fastq 1233447_S45_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233447_S45.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233448_S46_L001_R1_001.fastq 1233448_S46_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233448_S46.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233449_S47_L001_R1_001.fastq 1233449_S47_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233449_S47.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233450_S48_L001_R1_001.fastq 1233450_S48_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233450_S48.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233451_S49_L001_R1_001.fastq 1233451_S49_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233451_S49.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233452_S50_L001_R1_001.fastq 1233452_S50_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233452_S50.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233453_S51_L001_R1_001.fastq 1233453_S51_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233453_S51.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233454_S52_L001_R1_001.fastq 1233454_S52_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233454_S52.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233455_S53_L001_R1_001.fastq 1233455_S53_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233455_S53.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233456_S54_L001_R1_001.fastq 1233456_S54_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233456_S54.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233458-2_S61_L001_R1_001.fastq 1233458-2_S61_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233458-2_S61.bam
sleep 5
/export/novocraftV2.08.03/novoalign -o SAM -r None -l 30 -e 100 -i PE 95-300  -a TGTAGAACCATGTCGTCAGTGTGTGCTCATGTATCTCGTATGCCGTCTTCG  AGACCAAGTCTCTGCTACCGTGTAGATCTCGGTGGTCGCCGTATCATT -H -c 8 -d  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.novoindex -f 1233458_S55_L001_R1_001.fastq 1233458_S55_L001_R2_001.fastq  | /home/gsinghal/bin/samtools view -bS - > 1233458_S55.bam
sleep 5
