#!/bin/bash
#PBS -l nodes=1:ppn=1,walltime=12:00:00,vmem=40gb 
#PBS -N   NovoAlign_hg19_samtools_flagstat
#PBS -d  /BlueArc-scratch/gsinghal/MWatson/Validation/ 
#PBS -m abe 
 /home/gsinghal/bin/samtools flagstat 1123226_S58.bam   >   1123226_S58.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1123226_S64.bam   >   1123226_S64.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1123227_S59.bam   >   1123227_S59.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1123227_S65.bam   >   1123227_S65.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1123231_S57.bam   >   1123231_S57.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1123231_S63.bam   >   1123231_S63.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1123233_S56.bam   >   1123233_S56.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1123233_S62.bam   >   1123233_S62.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1200370_S60.bam   >   1200370_S60.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1200370_S66.bam   >   1200370_S66.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1230318_S3.bam   >   1230318_S3.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1230318_S67.bam   >   1230318_S67.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1230319_S72.bam   >   1230319_S72.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1230319_S8.bam   >   1230319_S8.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1230386_S71.bam   >   1230386_S71.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1230386_S7.bam   >   1230386_S7.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1230389_S73.bam   >   1230389_S73.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1230389_S9.bam   >   1230389_S9.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1230390_S10.bam   >   1230390_S10.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1230390_S74.bam   >   1230390_S74.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1230391_S11.bam   >   1230391_S11.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1230391_S75.bam   >   1230391_S75.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233400_S12.bam   >   1233400_S12.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233400_S76.bam   >   1233400_S76.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233401_S4.bam   >   1233401_S4.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233401_S68.bam   >   1233401_S68.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233402_S13.bam   >   1233402_S13.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233402_S77.bam   >   1233402_S77.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233403_S14.bam   >   1233403_S14.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233403_S78.bam   >   1233403_S78.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233404_S15.bam   >   1233404_S15.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233404_S79.bam   >   1233404_S79.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233405_S16.bam   >   1233405_S16.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233405_S80.bam   >   1233405_S80.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233406_S17.bam   >   1233406_S17.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233406_S81.bam   >   1233406_S81.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233418_S18.bam   >   1233418_S18.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233418_S82.bam   >   1233418_S82.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233419_S19.bam   >   1233419_S19.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233419_S83.bam   >   1233419_S83.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233420_S20.bam   >   1233420_S20.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233420_S84.bam   >   1233420_S84.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233421_S21.bam   >   1233421_S21.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233421_S85.bam   >   1233421_S85.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233422_S22.bam   >   1233422_S22.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233422_S86.bam   >   1233422_S86.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233423_S23.bam   >   1233423_S23.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233423_S87.bam   >   1233423_S87.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233424_S24.bam   >   1233424_S24.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233424_S88.bam   >   1233424_S88.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233425_S25.bam   >   1233425_S25.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233425_S89.bam   >   1233425_S89.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233426_S26.bam   >   1233426_S26.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233426_S90.bam   >   1233426_S90.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233427_S27.bam   >   1233427_S27.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233427_S91.bam   >   1233427_S91.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233428_S28.bam   >   1233428_S28.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233428_S92.bam   >   1233428_S92.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233429_S29.bam   >   1233429_S29.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233429_S93.bam   >   1233429_S93.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233430_S30.bam   >   1233430_S30.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233430_S94.bam   >   1233430_S94.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233431_S31.bam   >   1233431_S31.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233431_S95.bam   >   1233431_S95.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233432_S32.bam   >   1233432_S32.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233432_S96.bam   >   1233432_S96.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233433_S33.bam   >   1233433_S33.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233433_S97.bam   >   1233433_S97.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233434_S34.bam   >   1233434_S34.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233434_S98.bam   >   1233434_S98.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233435_S35.bam   >   1233435_S35.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233436_S36.bam   >   1233436_S36.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233437_S37.bam   >   1233437_S37.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233438_S38.bam   >   1233438_S38.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233439_S39.bam   >   1233439_S39.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233440_S40.bam   >   1233440_S40.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233441_S5.bam   >   1233441_S5.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233441_S69.bam   >   1233441_S69.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233442_S41.bam   >   1233442_S41.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233443_S42.bam   >   1233443_S42.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233444_S43.bam   >   1233444_S43.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233445_S44.bam   >   1233445_S44.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233446_S6.bam   >   1233446_S6.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233446_S70.bam   >   1233446_S70.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233447_S45.bam   >   1233447_S45.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233448_S46.bam   >   1233448_S46.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233449_S47.bam   >   1233449_S47.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233450_S48.bam   >   1233450_S48.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233451_S49.bam   >   1233451_S49.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233452_S50.bam   >   1233452_S50.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233453_S51.bam   >   1233453_S51.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233454_S52.bam   >   1233454_S52.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233455_S53.bam   >   1233455_S53.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233456_S54.bam   >   1233456_S54.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233458-2_S61.bam   >   1233458-2_S61.stats
sleep 5
 /home/gsinghal/bin/samtools flagstat 1233458_S55.bam   >   1233458_S55.stats
sleep 5
