#!/bin/bash
#PBS -l nodes=1:ppn=8,walltime=12:00:00,vmem=40gb 
#PBS -N   NovoAlign_samtools_sort_mpileup_vcf
#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Validation/hg19_Ref/ 
#PBS -m abe 
 /home/gsinghal/bin/samtools sort 1123226_S58.bam  1123226_S58_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1123226_S58_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1123226_S58_sorted.bam  >  1123226_S58_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1123226_S58_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1123226_S58_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1123226_S64.bam  1123226_S64_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1123226_S64_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1123226_S64_sorted.bam  >  1123226_S64_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1123226_S64_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1123226_S64_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1123227_S59.bam  1123227_S59_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1123227_S59_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1123227_S59_sorted.bam  >  1123227_S59_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1123227_S59_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1123227_S59_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1123227_S65.bam  1123227_S65_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1123227_S65_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1123227_S65_sorted.bam  >  1123227_S65_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1123227_S65_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1123227_S65_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1123231_S57.bam  1123231_S57_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1123231_S57_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1123231_S57_sorted.bam  >  1123231_S57_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1123231_S57_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1123231_S57_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1123231_S63.bam  1123231_S63_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1123231_S63_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1123231_S63_sorted.bam  >  1123231_S63_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1123231_S63_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1123231_S63_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1123233_S56.bam  1123233_S56_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1123233_S56_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1123233_S56_sorted.bam  >  1123233_S56_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1123233_S56_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1123233_S56_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1123233_S62.bam  1123233_S62_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1123233_S62_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1123233_S62_sorted.bam  >  1123233_S62_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1123233_S62_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1123233_S62_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1200370_S60.bam  1200370_S60_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1200370_S60_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1200370_S60_sorted.bam  >  1200370_S60_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1200370_S60_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1200370_S60_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1200370_S66.bam  1200370_S66_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1200370_S66_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1200370_S66_sorted.bam  >  1200370_S66_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1200370_S66_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1200370_S66_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1230318_S3.bam  1230318_S3_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1230318_S3_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1230318_S3_sorted.bam  >  1230318_S3_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1230318_S3_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1230318_S3_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1230318_S67.bam  1230318_S67_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1230318_S67_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1230318_S67_sorted.bam  >  1230318_S67_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1230318_S67_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1230318_S67_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1230319_S72.bam  1230319_S72_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1230319_S72_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1230319_S72_sorted.bam  >  1230319_S72_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1230319_S72_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1230319_S72_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1230319_S8.bam  1230319_S8_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1230319_S8_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1230319_S8_sorted.bam  >  1230319_S8_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1230319_S8_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1230319_S8_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1230386_S71.bam  1230386_S71_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1230386_S71_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1230386_S71_sorted.bam  >  1230386_S71_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1230386_S71_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1230386_S71_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1230386_S7.bam  1230386_S7_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1230386_S7_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1230386_S7_sorted.bam  >  1230386_S7_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1230386_S7_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1230386_S7_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1230389_S73.bam  1230389_S73_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1230389_S73_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1230389_S73_sorted.bam  >  1230389_S73_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1230389_S73_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1230389_S73_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1230389_S9.bam  1230389_S9_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1230389_S9_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1230389_S9_sorted.bam  >  1230389_S9_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1230389_S9_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1230389_S9_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1230390_S10.bam  1230390_S10_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1230390_S10_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1230390_S10_sorted.bam  >  1230390_S10_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1230390_S10_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1230390_S10_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1230390_S74.bam  1230390_S74_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1230390_S74_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1230390_S74_sorted.bam  >  1230390_S74_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1230390_S74_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1230390_S74_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1230391_S11.bam  1230391_S11_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1230391_S11_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1230391_S11_sorted.bam  >  1230391_S11_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1230391_S11_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1230391_S11_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1230391_S75.bam  1230391_S75_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1230391_S75_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1230391_S75_sorted.bam  >  1230391_S75_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1230391_S75_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1230391_S75_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233400_S12.bam  1233400_S12_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233400_S12_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233400_S12_sorted.bam  >  1233400_S12_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233400_S12_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233400_S12_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233400_S76.bam  1233400_S76_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233400_S76_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233400_S76_sorted.bam  >  1233400_S76_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233400_S76_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233400_S76_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233401_S4.bam  1233401_S4_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233401_S4_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233401_S4_sorted.bam  >  1233401_S4_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233401_S4_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233401_S4_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233401_S68.bam  1233401_S68_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233401_S68_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233401_S68_sorted.bam  >  1233401_S68_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233401_S68_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233401_S68_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233402_S13.bam  1233402_S13_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233402_S13_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233402_S13_sorted.bam  >  1233402_S13_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233402_S13_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233402_S13_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233402_S77.bam  1233402_S77_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233402_S77_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233402_S77_sorted.bam  >  1233402_S77_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233402_S77_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233402_S77_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233403_S14.bam  1233403_S14_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233403_S14_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233403_S14_sorted.bam  >  1233403_S14_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233403_S14_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233403_S14_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233403_S78.bam  1233403_S78_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233403_S78_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233403_S78_sorted.bam  >  1233403_S78_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233403_S78_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233403_S78_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233404_S15.bam  1233404_S15_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233404_S15_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233404_S15_sorted.bam  >  1233404_S15_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233404_S15_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233404_S15_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233404_S79.bam  1233404_S79_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233404_S79_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233404_S79_sorted.bam  >  1233404_S79_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233404_S79_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233404_S79_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233405_S16.bam  1233405_S16_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233405_S16_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233405_S16_sorted.bam  >  1233405_S16_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233405_S16_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233405_S16_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233405_S80.bam  1233405_S80_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233405_S80_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233405_S80_sorted.bam  >  1233405_S80_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233405_S80_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233405_S80_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233406_S17.bam  1233406_S17_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233406_S17_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233406_S17_sorted.bam  >  1233406_S17_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233406_S17_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233406_S17_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233406_S81.bam  1233406_S81_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233406_S81_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233406_S81_sorted.bam  >  1233406_S81_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233406_S81_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233406_S81_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233418_S18.bam  1233418_S18_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233418_S18_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233418_S18_sorted.bam  >  1233418_S18_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233418_S18_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233418_S18_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233418_S82.bam  1233418_S82_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233418_S82_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233418_S82_sorted.bam  >  1233418_S82_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233418_S82_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233418_S82_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233419_S19.bam  1233419_S19_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233419_S19_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233419_S19_sorted.bam  >  1233419_S19_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233419_S19_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233419_S19_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233419_S83.bam  1233419_S83_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233419_S83_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233419_S83_sorted.bam  >  1233419_S83_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233419_S83_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233419_S83_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233420_S20.bam  1233420_S20_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233420_S20_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233420_S20_sorted.bam  >  1233420_S20_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233420_S20_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233420_S20_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233420_S84.bam  1233420_S84_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233420_S84_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233420_S84_sorted.bam  >  1233420_S84_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233420_S84_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233420_S84_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233421_S21.bam  1233421_S21_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233421_S21_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233421_S21_sorted.bam  >  1233421_S21_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233421_S21_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233421_S21_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233421_S85.bam  1233421_S85_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233421_S85_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233421_S85_sorted.bam  >  1233421_S85_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233421_S85_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233421_S85_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233422_S22.bam  1233422_S22_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233422_S22_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233422_S22_sorted.bam  >  1233422_S22_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233422_S22_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233422_S22_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233422_S86.bam  1233422_S86_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233422_S86_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233422_S86_sorted.bam  >  1233422_S86_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233422_S86_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233422_S86_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233423_S23.bam  1233423_S23_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233423_S23_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233423_S23_sorted.bam  >  1233423_S23_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233423_S23_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233423_S23_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233423_S87.bam  1233423_S87_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233423_S87_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233423_S87_sorted.bam  >  1233423_S87_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233423_S87_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233423_S87_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233424_S24.bam  1233424_S24_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233424_S24_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233424_S24_sorted.bam  >  1233424_S24_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233424_S24_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233424_S24_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233424_S88.bam  1233424_S88_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233424_S88_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233424_S88_sorted.bam  >  1233424_S88_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233424_S88_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233424_S88_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233425_S25.bam  1233425_S25_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233425_S25_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233425_S25_sorted.bam  >  1233425_S25_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233425_S25_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233425_S25_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233425_S89.bam  1233425_S89_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233425_S89_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233425_S89_sorted.bam  >  1233425_S89_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233425_S89_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233425_S89_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233426_S26.bam  1233426_S26_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233426_S26_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233426_S26_sorted.bam  >  1233426_S26_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233426_S26_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233426_S26_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233426_S90.bam  1233426_S90_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233426_S90_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233426_S90_sorted.bam  >  1233426_S90_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233426_S90_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233426_S90_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233427_S27.bam  1233427_S27_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233427_S27_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233427_S27_sorted.bam  >  1233427_S27_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233427_S27_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233427_S27_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233427_S91.bam  1233427_S91_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233427_S91_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233427_S91_sorted.bam  >  1233427_S91_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233427_S91_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233427_S91_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233428_S28.bam  1233428_S28_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233428_S28_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233428_S28_sorted.bam  >  1233428_S28_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233428_S28_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233428_S28_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233428_S92.bam  1233428_S92_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233428_S92_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233428_S92_sorted.bam  >  1233428_S92_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233428_S92_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233428_S92_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233429_S29.bam  1233429_S29_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233429_S29_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233429_S29_sorted.bam  >  1233429_S29_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233429_S29_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233429_S29_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233429_S93.bam  1233429_S93_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233429_S93_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233429_S93_sorted.bam  >  1233429_S93_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233429_S93_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233429_S93_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233430_S30.bam  1233430_S30_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233430_S30_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233430_S30_sorted.bam  >  1233430_S30_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233430_S30_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233430_S30_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233430_S94.bam  1233430_S94_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233430_S94_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233430_S94_sorted.bam  >  1233430_S94_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233430_S94_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233430_S94_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233431_S31.bam  1233431_S31_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233431_S31_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233431_S31_sorted.bam  >  1233431_S31_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233431_S31_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233431_S31_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233431_S95.bam  1233431_S95_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233431_S95_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233431_S95_sorted.bam  >  1233431_S95_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233431_S95_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233431_S95_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233432_S32.bam  1233432_S32_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233432_S32_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233432_S32_sorted.bam  >  1233432_S32_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233432_S32_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233432_S32_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233432_S96.bam  1233432_S96_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233432_S96_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233432_S96_sorted.bam  >  1233432_S96_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233432_S96_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233432_S96_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233433_S33.bam  1233433_S33_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233433_S33_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233433_S33_sorted.bam  >  1233433_S33_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233433_S33_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233433_S33_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233433_S97.bam  1233433_S97_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233433_S97_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233433_S97_sorted.bam  >  1233433_S97_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233433_S97_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233433_S97_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233434_S34.bam  1233434_S34_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233434_S34_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233434_S34_sorted.bam  >  1233434_S34_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233434_S34_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233434_S34_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233434_S98.bam  1233434_S98_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233434_S98_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233434_S98_sorted.bam  >  1233434_S98_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233434_S98_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233434_S98_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233435_S35.bam  1233435_S35_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233435_S35_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233435_S35_sorted.bam  >  1233435_S35_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233435_S35_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233435_S35_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233436_S36.bam  1233436_S36_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233436_S36_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233436_S36_sorted.bam  >  1233436_S36_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233436_S36_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233436_S36_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233437_S37.bam  1233437_S37_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233437_S37_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233437_S37_sorted.bam  >  1233437_S37_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233437_S37_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233437_S37_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233438_S38.bam  1233438_S38_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233438_S38_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233438_S38_sorted.bam  >  1233438_S38_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233438_S38_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233438_S38_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233439_S39.bam  1233439_S39_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233439_S39_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233439_S39_sorted.bam  >  1233439_S39_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233439_S39_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233439_S39_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233440_S40.bam  1233440_S40_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233440_S40_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233440_S40_sorted.bam  >  1233440_S40_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233440_S40_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233440_S40_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233441_S5.bam  1233441_S5_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233441_S5_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233441_S5_sorted.bam  >  1233441_S5_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233441_S5_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233441_S5_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233441_S69.bam  1233441_S69_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233441_S69_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233441_S69_sorted.bam  >  1233441_S69_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233441_S69_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233441_S69_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233442_S41.bam  1233442_S41_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233442_S41_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233442_S41_sorted.bam  >  1233442_S41_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233442_S41_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233442_S41_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233443_S42.bam  1233443_S42_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233443_S42_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233443_S42_sorted.bam  >  1233443_S42_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233443_S42_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233443_S42_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233444_S43.bam  1233444_S43_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233444_S43_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233444_S43_sorted.bam  >  1233444_S43_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233444_S43_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233444_S43_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233445_S44.bam  1233445_S44_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233445_S44_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233445_S44_sorted.bam  >  1233445_S44_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233445_S44_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233445_S44_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233446_S6.bam  1233446_S6_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233446_S6_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233446_S6_sorted.bam  >  1233446_S6_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233446_S6_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233446_S6_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233446_S70.bam  1233446_S70_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233446_S70_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233446_S70_sorted.bam  >  1233446_S70_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233446_S70_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233446_S70_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233447_S45.bam  1233447_S45_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233447_S45_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233447_S45_sorted.bam  >  1233447_S45_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233447_S45_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233447_S45_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233448_S46.bam  1233448_S46_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233448_S46_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233448_S46_sorted.bam  >  1233448_S46_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233448_S46_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233448_S46_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233449_S47.bam  1233449_S47_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233449_S47_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233449_S47_sorted.bam  >  1233449_S47_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233449_S47_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233449_S47_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233450_S48.bam  1233450_S48_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233450_S48_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233450_S48_sorted.bam  >  1233450_S48_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233450_S48_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233450_S48_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233451_S49.bam  1233451_S49_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233451_S49_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233451_S49_sorted.bam  >  1233451_S49_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233451_S49_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233451_S49_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233452_S50.bam  1233452_S50_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233452_S50_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233452_S50_sorted.bam  >  1233452_S50_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233452_S50_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233452_S50_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233453_S51.bam  1233453_S51_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233453_S51_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233453_S51_sorted.bam  >  1233453_S51_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233453_S51_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233453_S51_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233454_S52.bam  1233454_S52_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233454_S52_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233454_S52_sorted.bam  >  1233454_S52_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233454_S52_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233454_S52_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233455_S53.bam  1233455_S53_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233455_S53_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233455_S53_sorted.bam  >  1233455_S53_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233455_S53_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233455_S53_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233456_S54.bam  1233456_S54_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233456_S54_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233456_S54_sorted.bam  >  1233456_S54_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233456_S54_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233456_S54_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233458-2_S61.bam  1233458-2_S61_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233458-2_S61_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233458-2_S61_sorted.bam  >  1233458-2_S61_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233458-2_S61_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233458-2_S61_hg19_ref.vcf
sleep 2
 /home/gsinghal/bin/samtools sort 1233458_S55.bam  1233458_S55_sorted
sleep 2
 /home/gsinghal/bin/samtools index 1233458_S55_sorted.bam  
sleep 2
 /home/gsinghal/bin/samtools mpileup  -f  /BlueArc-scratch/gsinghal/MWatson/hg19/hg19.fa  1233458_S55_sorted.bam  >  1233458_S55_hg19_ref_mpileup.txt 
sleep 2
java -jar  ./VarScan.v2.3.2.jar mpileup2snp 1233458_S55_hg19_ref_mpileup.txt   --min-reads2  5  --min-var-freq  0.05  --p-value  0.05  --output-vcf  >  1233458_S55_hg19_ref.vcf
sleep 2
