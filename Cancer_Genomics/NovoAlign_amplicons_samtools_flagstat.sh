#!/bin/bash
#PBS -l nodes=1:ppn=1,walltime=12:00:00,vmem=40gb 
#PBS -N   NovoAlign_amplicons_samtools_flagstat
#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Validation/ 
#PBS -m abe 
 /home/gsinghal/bin/samtools flagstat 1123226_S58_amplicon_ref.bam   >   1123226_S58_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1123226_S64_amplicon_ref.bam   >   1123226_S64_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1123227_S59_amplicon_ref.bam   >   1123227_S59_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1123227_S65_amplicon_ref.bam   >   1123227_S65_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1123231_S57_amplicon_ref.bam   >   1123231_S57_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1123231_S63_amplicon_ref.bam   >   1123231_S63_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1123233_S56_amplicon_ref.bam   >   1123233_S56_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1123233_S62_amplicon_ref.bam   >   1123233_S62_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1200370_S60_amplicon_ref.bam   >   1200370_S60_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1200370_S66_amplicon_ref.bam   >   1200370_S66_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1230318_S3_amplicon_ref.bam   >   1230318_S3_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1230318_S67_amplicon_ref.bam   >   1230318_S67_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1230319_S72_amplicon_ref.bam   >   1230319_S72_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1230319_S8_amplicon_ref.bam   >   1230319_S8_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1230386_S71_amplicon_ref.bam   >   1230386_S71_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1230386_S7_amplicon_ref.bam   >   1230386_S7_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1230389_S73_amplicon_ref.bam   >   1230389_S73_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1230389_S9_amplicon_ref.bam   >   1230389_S9_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1230390_S10_amplicon_ref.bam   >   1230390_S10_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1230390_S74_amplicon_ref.bam   >   1230390_S74_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1230391_S11_amplicon_ref.bam   >   1230391_S11_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1230391_S75_amplicon_ref.bam   >   1230391_S75_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233400_S12_amplicon_ref.bam   >   1233400_S12_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233400_S76_amplicon_ref.bam   >   1233400_S76_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233401_S4_amplicon_ref.bam   >   1233401_S4_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233401_S68_amplicon_ref.bam   >   1233401_S68_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233402_S13_amplicon_ref.bam   >   1233402_S13_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233402_S77_amplicon_ref.bam   >   1233402_S77_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233403_S14_amplicon_ref.bam   >   1233403_S14_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233403_S78_amplicon_ref.bam   >   1233403_S78_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233404_S15_amplicon_ref.bam   >   1233404_S15_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233404_S79_amplicon_ref.bam   >   1233404_S79_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233405_S16_amplicon_ref.bam   >   1233405_S16_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233405_S80_amplicon_ref.bam   >   1233405_S80_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233406_S17_amplicon_ref.bam   >   1233406_S17_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233406_S81_amplicon_ref.bam   >   1233406_S81_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233418_S18_amplicon_ref.bam   >   1233418_S18_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233418_S82_amplicon_ref.bam   >   1233418_S82_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233419_S19_amplicon_ref.bam   >   1233419_S19_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233419_S83_amplicon_ref.bam   >   1233419_S83_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233420_S20_amplicon_ref.bam   >   1233420_S20_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233420_S84_amplicon_ref.bam   >   1233420_S84_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233421_S21_amplicon_ref.bam   >   1233421_S21_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233421_S85_amplicon_ref.bam   >   1233421_S85_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233422_S22_amplicon_ref.bam   >   1233422_S22_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233422_S86_amplicon_ref.bam   >   1233422_S86_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233423_S23_amplicon_ref.bam   >   1233423_S23_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233423_S87_amplicon_ref.bam   >   1233423_S87_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233424_S24_amplicon_ref.bam   >   1233424_S24_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233424_S88_amplicon_ref.bam   >   1233424_S88_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233425_S25_amplicon_ref.bam   >   1233425_S25_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233425_S89_amplicon_ref.bam   >   1233425_S89_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233426_S26_amplicon_ref.bam   >   1233426_S26_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233426_S90_amplicon_ref.bam   >   1233426_S90_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233427_S27_amplicon_ref.bam   >   1233427_S27_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233427_S91_amplicon_ref.bam   >   1233427_S91_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233428_S28_amplicon_ref.bam   >   1233428_S28_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233428_S92_amplicon_ref.bam   >   1233428_S92_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233429_S29_amplicon_ref.bam   >   1233429_S29_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233429_S93_amplicon_ref.bam   >   1233429_S93_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233430_S30_amplicon_ref.bam   >   1233430_S30_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233430_S94_amplicon_ref.bam   >   1233430_S94_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233431_S31_amplicon_ref.bam   >   1233431_S31_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233431_S95_amplicon_ref.bam   >   1233431_S95_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233432_S32_amplicon_ref.bam   >   1233432_S32_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233432_S96_amplicon_ref.bam   >   1233432_S96_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233433_S33_amplicon_ref.bam   >   1233433_S33_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233433_S97_amplicon_ref.bam   >   1233433_S97_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233434_S34_amplicon_ref.bam   >   1233434_S34_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233434_S98_amplicon_ref.bam   >   1233434_S98_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233435_S35_amplicon_ref.bam   >   1233435_S35_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233436_S36_amplicon_ref.bam   >   1233436_S36_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233437_S37_amplicon_ref.bam   >   1233437_S37_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233438_S38_amplicon_ref.bam   >   1233438_S38_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233439_S39_amplicon_ref.bam   >   1233439_S39_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233440_S40_amplicon_ref.bam   >   1233440_S40_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233441_S5_amplicon_ref.bam   >   1233441_S5_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233441_S69_amplicon_ref.bam   >   1233441_S69_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233442_S41_amplicon_ref.bam   >   1233442_S41_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233443_S42_amplicon_ref.bam   >   1233443_S42_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233444_S43_amplicon_ref.bam   >   1233444_S43_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233445_S44_amplicon_ref.bam   >   1233445_S44_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233446_S6_amplicon_ref.bam   >   1233446_S6_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233446_S70_amplicon_ref.bam   >   1233446_S70_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233447_S45_amplicon_ref.bam   >   1233447_S45_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233448_S46_amplicon_ref.bam   >   1233448_S46_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233449_S47_amplicon_ref.bam   >   1233449_S47_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233450_S48_amplicon_ref.bam   >   1233450_S48_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233451_S49_amplicon_ref.bam   >   1233451_S49_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233452_S50_amplicon_ref.bam   >   1233452_S50_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233453_S51_amplicon_ref.bam   >   1233453_S51_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233454_S52_amplicon_ref.bam   >   1233454_S52_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233455_S53_amplicon_ref.bam   >   1233455_S53_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233456_S54_amplicon_ref.bam   >   1233456_S54_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233458-2_S61_amplicon_ref.bam   >   1233458-2_S61_amplicon_ref.stats
sleep 2
 /home/gsinghal/bin/samtools flagstat 1233458_S55_amplicon_ref.bam   >   1233458_S55_amplicon_ref.stats
sleep 2
