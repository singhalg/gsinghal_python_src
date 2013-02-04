'''
Created on Jan 19, 2011

@author: Keith Decker's script
'''
#!/usr/bin/python
import sys,os,CHIPSEQ_DICT
if (len(sys.argv)!=2):
       print "1.  EXPERIMENT NAME (LNCAP_AR_TREATED)"
       sys.exit()
EXP_NAME = sys.argv[1]

DICT = CHIPSEQ_DICT.GET_DICT()
ROOTBAR = DICT[EXP_NAME]
print ROOTBAR
DIR             =       "/net/artemis/mnt/work2/projects/keith_test/CHIPSEQ/"
FASTQ_PATH      =       DIR+"FASTQ/"+ROOTBAR
FASTQ_FILE         =       FASTQ_PATH+".fastq"
if "sequence" in ROOTBAR:
       print "SINGLE FASTQ"
else:
       print "MULTIPLE FASTQ"
       TEST = ROOTBAR.lstrip('Jia')
       SPLIT = TEST.rsplit('.',1)
       BAR = SPLIT[1]
       ROOT = SPLIT[0]
       #print TEST
       EXP = []
       LANE = []
       FASTQ = []
       while ROOT != 0:
               NEXT = ROOT.split('s',1)
               EXP.append(NEXT[0])
               AND = NEXT[1].split('_',2)
               LANE.append(AND[1])
               if len(AND)==3:
                       ROOT = AND[2]
               else:
                       ROOT = 0
       DIR = "/net/artemis/mnt/work2/projects/keith_test/CHIPSEQ/FASTQ/"
       CAT_COMMAND = "cat "
       for i in range(0,len(EXP)):
               THIS_FASTQ =  DIR+"Jia"+EXP[i]+"s_"+LANE[i]+"_sequence."+BAR+".fastq "
               a = os.popen('wc -l '+THIS_FASTQ)
               b = a.read()
               read = b.split()
               lines = int(read[0])
               if lines<1000000:
                       print "LESS THAN ONE MILLION READS, ABORTING "+str(lines)
                       sys.exit()
               else:
                       print str(lines)+" lines "+THIS_FASTQ
               CAT_COMMAND = CAT_COMMAND + THIS_FASTQ
       CAT_COMMAND = CAT_COMMAND + " > "+FASTQ_FILE
       os.system(CAT_COMMAND)
INDEX           =       '/data/scratch/keith_bowtieDB/hg18_SEPT_16_2010'

NP              =       "16"
DIR             =       "/net/artemis/mnt/work2/projects/keith_test/CHIPSEQ/"

TAG = EXP_NAME+"."+ROOTBAR
FULLPATH        =       DIR+TAG

sub_script      =       DIR+"SUBMIT/submit_"+TAG
stdout          =       sub_script+".stdout"
stdin           =       sub_script+".stdin"
print "COMPLETE FILE..."
if (os.path.isfile(FASTQ_FILE)):
       os.system("wc -l "+FASTQ_FILE)
OUT_FILE        =       FULLPATH+".map"
print "OUT_FILE..."+OUT_FILE
print "stdout..."+stdout
print "stdin..."+stdin
# bsub requires $1 DIR $2 SAMPLE $3 INDEX
#command = "bsub -q normal -n "+NP+" -J "+ROOT+" -o "+stdout+" -e "+stdin+" < "+sub_script+" "+DIR+" "+ROOT+" "+INDEX

f = open(sub_script, 'w')
f.write('#!/bin/bash\n')
f.write('cp '+FASTQ_FILE+' /data/scratch/bowtie.'+TAG+'.fastq\n')

PARAMS = EXP_NAME.split('_TAG_')
if len(PARAMS)==2:
       if PARAMS[1]=='best':
               REPORTING = " --best "
       if PARAMS[1]=='M1':
               REPORTING = " -M 1 --best "
       if PARAMS[1]=='m1':
               REPORTING = " -m 1 "
else:
       REPORTING = " -m 1 "

#REPORTING = "-k 10"
print "REPORTING FLAG SET TO "+REPORTING
f.write('/net/artemis/mnt/work2/seqApps/bowtie-0.12.1/bowtie  --solexa1.3-quals '+INDEX+' -p 16 '+REPORTING+' -t  /data/scratch/bowtie.'+TAG+'.fastq 1>  /data/scratch/bowtie.'+TAG+'.stdout  2> /data/scratch/bowtie.'+TAG+'.stderr\n')
f.write('mv /data/scratch/bowtie.'+TAG+'.stdout '+DIR+'/STD/bowtie.'+TAG+'.stdout\n')
f.write('mv /data/scratch/bowtie.'+TAG+'.stderr '+DIR+'/STD/bowtie.'+TAG+'.stderr\n')

f.close()
os.system('chmod 777 '+sub_script)

command = "bsub -q normal -n "+NP+" -J "+TAG+" -o "+stdout+" -e "+stdin+" < "+sub_script
print command
os.system(command)