'''
Created on Jan 20, 2011

@author: Gaurav (Adapted from Keith Decker's script)
'''

'''
#-------------------------------------------------------------------#
# Copyright (C) 2011 Gaurav Singhal                                 #
# All Rights Reserved.                                              #
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : Jan 18, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#

This script writes a job script and runs it on Java. 

'''


#!/usr/bin/python
import sys,os



### TBE ####
sub_script      =       "gsJob_s_4_1_old"      
stdout          =       sub_script+".stdout"
stdin           =       sub_script+".stdin"


print "stdout..."+stdout
print "stdin..."+stdin
# bsub requires $1 DIR $2 SAMPLE $3 INDEX
#command = "bsub -q normal -n "+NP+" -J "+ROOT+" -o "+stdout+" -e "+stdin+" < "+sub_script+" "+DIR+" "+ROOT+" "+INDEX

### TBE ####
FASTQ_FILE = "/net/artemis/mnt/work1/projects/gsinghalWork/s_4_1_sequence.txt.fastq "
INDEXES = "/net/artemis/mnt/work1/projects/gsinghalWork/hg19Inv/* "
f = open(sub_script, 'w')
f.write('#!/bin/bash\n')
f.write('mkdir /data/scratch/gsinghal' + '\n')
f.write('mkdir /data/scratch/gsinghal/bowtie' + '\n')
f.write('mkdir /data/scratch/gsinghal/bowtie/indexes' + '\n')
f.write('cp ' +INDEXES + ' /data/scratch/gsinghal/bowtie/indexes/'+ '\n')

f.write('cp '+FASTQ_FILE+' /data/scratch/gsinghal/bowtie/' + '\n')

# bowtie [options]* <ebwt> {-1 <m1> -2 <m2> | --12 <r> | <s>} [<hit>]

BOWTIE = "/net/artemis/mnt/work2/seqApps/bowtie-0.12.7/bowtie "   # Bowtie location

### TBE ####
####### OPTIONS ########
INPUT = " --trim5 1 --trim3 5 "
ALIGNMENT = " -n 3 -e 120 -l 20 -y "
REPORTING = " -k 1 "  # put the alignment reporting parameters here; k 1 means only one alignment per read
OUTPUT = " --al /data/scratch/gsinghal/bowtie/aligned.fq "
COLORSPACE = ""
SAM = ""
PERFORMANCE = " -p 16 "

OPTIONS = INPUT + ALIGNMENT + REPORTING + OUTPUT + COLORSPACE + SAM + PERFORMANCE

### TBE ####
## INDEX LOCATION ##
INDEX           =       ' /data/scratch/gsinghal/bowtie/indexes/hg19_inv '

### TBE ####
## READ Location ##
IN_READS      =  ' /data/scratch/gsinghal/bowtie/s_4_1_sequence.txt.fastq '
HIT = '/data/scratch/gsinghal/bowtie/s_4_1_bowtie.map '
print "OPTIONS are :" + OPTIONS

BOWTIE_USAGE = BOWTIE+ OPTIONS +INDEX+ IN_READS + HIT + '\n'
print BOWTIE_USAGE

f.write(BOWTIE_USAGE)
f.write('mv ' + HIT +  '/net/artemis/mnt/work1/projects/gsinghalWork/ ' +'\n')
f.write('mv /data/scratch/gsinghal/bowtie/aligned.fq /net/artemis/mnt/work1/projects/gsinghalWork/ ' + '\n')
f.write('rm -r /data/scratch/gsinghal/bowtie'+ '\n')
f.close()
os.system('chmod 777 '+sub_script)
NP              =       "16"
command = "bsub -q normal -n " +NP + " -o "+stdout+" -e "+stdin+" < " +sub_script
print command
#os.system(command)