'''
Created on Jan 20, 2011

@author: Gaurav (Adapted from Keith Decker's script)
'''

'''
#-------------------------------------------------------------------#
# @copyright:  2011 Gaurav Singhal                                 #
# All Rights Reserved.                                              #
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : Jan 20, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

This script writes a job script and runs it on Lava with required params. 
Only edit at lines having ### TBE ### tag. 

'''


#!/usr/bin/python
import sys,os



tag = 'Bowtie_mcf7_1'   ### TBE ####
sub_script      =       tag      
stdout          =       sub_script+".stdout"
stdin           =       sub_script+".stdin"


print "stdout..."+stdout
print "stdin..."+stdin
# bsub requires $1 DIR $2 SAMPLE $3 index
#command = "bsub -q normal -n "+NP+" -J "+ROOT+" -o "+stdout+" -e "+stdin+" < "+sub_script+" "+DIR+" "+ROOT+" "+index

WORK = '/net/artemis/mnt/work1/projects/gsinghalWork/SRA/mcf7/'
SCRATCH = '/data/scratch/gsinghal/'
                              
readFile = "SRR097789_1.fastq  "     ### TBE ###
fastqFile = WORK + readFile 
indexes = WORK +"hg19Inv/*  "               ### TBE ###
f = open(sub_script, 'w')
f.write('#!/bin/bash\n')
f.write('mkdir /data/scratch/gsinghal' + '\n')
f.write('mkdir '+SCRATCH+'bowtie' + '\n')
f.write('mkdir '+SCRATCH+'bowtie/indexes' + '\n')
f.write('mkdir '+SCRATCH+'bowtie/output' + '\n')  
f.write('cp ' +indexes + SCRATCH +'bowtie/indexes/'+ '\n')   

f.write('cp '+fastqFile+ SCRATCH +'bowtie/' + '\n')

# bowtie [options]* <ebwt> {-1 <m1> -2 <m2> | --12 <r> | <s>} [<hit>]

BOWTIE = "/net/artemis/mnt/work2/seqApps/bowtie-0.12.7/bowtie "   # Bowtie location



INPUT = " --trim3 6 "         ### TBE ####
ALIGNMENT = " -n 3 -e 120 -l 20 -y "    ### TBE ####
REPORTING = " -k 1 "  # put the alignment reporting parameters here; k 1 means only one alignment per read
OUTPUT = " --al " +SCRATCH+"bowtie/output/aligned_s_4_2_noAdap.fq "    ### TBE ####
COLORSPACE = ""                         ### TBE ####
SAM = ""                                ### TBE ####
PERFORMANCE = " -p 16 "                 ### TBE ####

OPTIONS = INPUT + ALIGNMENT + REPORTING + OUTPUT + COLORSPACE + SAM + PERFORMANCE


## index LOCATION ##
index           =     SCRATCH+   'bowtie/indexes/hg19_inv  '    ### TBE ####



## READ Location ##
IN_READS      =  SCRATCH+'bowtie/'+ readFile
HIT = SCRATCH+ 'bowtie/output/s_4_2_bowtie_noAdap.map ' ### TBE ####
print "OPTIONS are :" + OPTIONS

BOWTIE_USAGE = BOWTIE+ OPTIONS +index+ IN_READS + HIT + '\n'
print BOWTIE_USAGE

f.write(BOWTIE_USAGE)
f.write('mkdir '+WORK+ tag+ '_results' + '\n')
f.write('rm -r '+SCRATCH+'bowtie/indexes' +'\n')
f.write('mv ' + SCRATCH + 'bowtie/*  ' +  WORK+tag+'_results' +'/' +'\n')
f.write('rm -r '+SCRATCH+ '\n')
f.close()
os.system('chmod 777 '+sub_script)
NP              =       "16"
command = "bsub -q normal -n " +NP + " -o "+stdout+" -e "+stdin+" < " +sub_script
print command
#os.system(command)