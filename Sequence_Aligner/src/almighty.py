'''
Created on Apr 6, 2012

@author: gsinghal
'''


import sys, re, os
import psutil as PS
from subprocess import Popen, PIPE, STDOUT
import pickle
import time

'''


'''



def download_expand():
    cmd1 = "wget -b -q ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/data/NA18486/sequence_read/SRR011037_1.filt.fastq.gz"

    job1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    PID1 = job1.pid
    proc1 = PS.Process(PID1)
    proc1.wait()

    cmd2 = "gunzip SRR011037_1.filt.fastq.gz"

    job2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    PID2 = job2.pid
    proc2 = PS.Process(PID2)
    proc2.wait()



def almighty():


#    fn.append('data/NA18486/sequence_read/SRR011037.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011037_1.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011037_2.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011038.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011038_1.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011038_2.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011039.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011039_1.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011039_2.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011040.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011040_1.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011040_2.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011041.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011041_1.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011041_2.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011042.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011042_1.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011042_2.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011043.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR011043_1.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR011043_2.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR020480.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR020480_1.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR020480_2.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR020481.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR020481_1.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR020481_2.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR022607.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR022607_1.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR022607_2.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR027525.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR027525_1.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR027525_2.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR027526.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR027526_1.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR027526_2.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR027527.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR027527_1.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR027527_2.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR027528.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR027528_1.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR027528_2.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR029844.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR029844_1.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR029844_2.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR029845.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR029845_1.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR029845_2.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR032211.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR032211_1.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR032211_2.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR032212.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR032212_1.filt.fastq.gz')
#fn.append('data/NA18486/sequence_read/SRR032212_2.filt.fastq.gz')

    file_loc_prefix = "ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/"

    fh = open('YRI_lowCoverage.csv', 'rU')

    file_PID_dict = {}

#    processes = []

    seq_data = fh.readlines()
    fh.close()
    for line in seq_data:
        flds = line.split(',')
        if (flds[9].strip() == 'NA18486') and (flds[20].strip()== '0')  and (flds[12].strip()=='ILLUMINA'):
            file_loc = file_loc_prefix + flds[0].strip()
            cmd = " wget -b "+ file_loc
#            print cmd
            job = Popen(cmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

            output = job.stdout.read()

            s = output.find('pid') + 4
            e = output.find('.')


            PID = output[s:e]

            fq_file_name = ret_FQfile_name(file_loc)

            file_PID_dict[PID] = fq_file_name

#            processes.append(PID)

    PIDs = file_PID_dict.keys()

#    done = False

    gzPIDs = []

    for PID in PIDs:

        process = PS.Process(int(PID))
        process.wait()
        cmd = "gunzip "+ file_PID_dict[PID]
        job = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

        gzPIDs.append(job.pid)

#
#    for gsPID in gzPIDs:
#        process = PS.Process(gzPID)
#        process.wait()

    wgetProcList = open('wgetProcList', 'w')
    pickle.dump(PIDs, wgetProcList)

    gzProcList = open('gzProcList', 'w')
    pickle.dump(gzPIDs, gzProcList)

#    #createBS(nodes, ppn, wt, jobname, bsName, working_dir):
#    createBS('4', '8', '48:00:00', 'NA18486', 'bowtie2_NA18486_lc', '/scratch/gsinghal/YRI_LC/')
#    runBS()




def fastqDownload(sampleName):

    file_loc_NCBI = "ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/"
    file_loc_EBI = "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/"

    fh = open('YRI_lowCoverage.csv', 'rU')

    file_PID_dict = {}

#    processes = []
    switch = True
    seq_data = fh.readlines()
    fh.close()
    psList = {}

    for line in seq_data:
        flds = line.split(',')
        if (flds[9].strip() == sampleName) and (flds[20].strip()== '0')  and (flds[12].strip()=='ILLUMINA'):

            if switch:

                file_loc = file_loc_NCBI + flds[0].strip()
            else:
                file_loc = file_loc_EBI + flds[0].strip()

            if switch:
                switch=False
            else:
                switch=True

            cmd = " wget --retry-connrefused -b "+ file_loc
            print cmd
            job = Popen(cmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

            output = job.stdout.read()

            s = output.find('pid') + 4
            e = output.find('.')
            PID = output[s:e]

            fq_file_name = ret_FQfile_name(file_loc)
            file_PID_dict[PID] = fq_file_name


            proc = PS.Process(int(PID))

            psList[PID] = proc

            time.sleep(10)
    #print file_PID_dict
    processes = file_PID_dict.keys()
    for each in processes:
        p = psList[each]
        p.wait
        fileName = file_PID_dict[each]
        cmd = 'gunzip  ' + fileName
        job = Popen(cmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        print cmd
        time.sleep(10)



#            processes.append(PID)



def ret_FQfile_name(file_loc):
    start = file_loc.find('SRR')
    return file_loc[start:]


def ret_FQfile_name2(file_loc):
    start = file_loc.find('SRR')
    return file_loc[start:-3]

def bash():



    floc = "ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/"

    fn = []

    fn.append('data/NA18486/sequence_read/SRR011037.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011037_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011037_2.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR011038.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011038_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011038_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011039.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011039_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011039_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011040.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011040_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011040_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011041.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011041_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011041_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011042.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011042_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011042_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011043.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011043_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR011043_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR020480.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR020480_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR020480_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR020481.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR020481_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR020481_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR022607.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR022607_1.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR022607_2.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR027525.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR027525_1.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR027525_2.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR027526.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR027526_1.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR027526_2.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR027527.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR027527_1.filt.fastq.gz')
#    fn.append('data/NA18486/sequence_read/SRR027527_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR027528.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR027528_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR027528_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR029844.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR029844_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR029844_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR029845.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR029845_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR029845_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR032211.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR032211_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR032211_2.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR032212.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR032212_1.filt.fastq.gz')
    fn.append('data/NA18486/sequence_read/SRR032212_2.filt.fastq.gz')

    fh1 = open('wget1.sh', 'w')
    for filename in fn:
        file_add = " wget " + floc + filename + "   \n"
        fh1.write(file_add)

    fh1.close()



def run_alignment():
    createBS('1', '48', '12:00:00' , 'gsinghal_NA18489_YRI',  'gsinghal_NA18489_YRI', '/scratch/gsinghal/YRI_LC/' , 'YRIref_index', 'NA18489')
    #runBS('gsinghal_NA18487_YRI')

def creatBS(nodes, ppn, wt, jobname, bsName, working_dir, reference, samplename):

    fhout = open(bsName, 'w')

    options = "#!/bin/bash" + '\n'+ "#PBS -l nodes="+nodes+":ppn="+ppn+",walltime="+wt+ ',mem=10gb \n' + "#PBS -N "+jobname + '\n' + "#PBS -d " + working_dir + '\n' + '#PBS -q dque_smp ' +'\n'

    fhout.write(options)

    single_end = []
    paired = []
    fh = open('YRI_lowCoverage.csv', 'rU')
    seq_data = fh.readlines()
    fh.close()

    unpaired = ''
    mate1 = ''
    mate2 = ''


    for line in seq_data:
        flds = line.split(',')
        if (flds[9].strip() == samplename) and (flds[20].strip()=='0') and (flds[12].strip()=='ILLUMINA'):
            file_loc = flds[0].strip()
            fq_file_name = ret_FQfile_name2(file_loc)
            if flds[18].strip() == 'PAIRED':
                print fq_file_name
                if re.search('_1', fq_file_name):
                    mate1 += fq_file_name + ','
                elif re.search('_2', fq_file_name):
                    mate2 += fq_file_name + ','
                else :
                    unpaired += fq_file_name + ','


    proc = str(int(nodes)*int(ppn))
    outFile = samplename+'_'+reference+'.sam'
    stdoutFile = samplename+'_'+reference+'_bowtie2.txt  '

    command = 'bowtie2 -p ' + proc +'  --sensitive -x  ' + reference+ '  -1 ' + mate1[:-1] + ' -2 ' + mate2[:-1] +  ' -S '+outFile +' &>  '+ stdoutFile

    fhout.write(command)
    fhout.write('\n')
##    fhout.write('wait \n')
##
##    error_handling_bowtie = '''if [ $? != 0 ]; then
##{
##    LOG = "JOB"
##    echo $! >> $LOG
##    echo "failed" >> $LOG
##    echo $LOG
##    bash email_bowtie2_fail
##    exit
##
##} fi\n
##'''
##
##    error_handling_samtools = '''if [ $? != 0 ]; then
##{
##    LOG = "JOB"
##    echo $! >> $LOG
##    echo "failed" >> $LOG
##    echo $LOG
##    bash email_samtools
##    exit
##
##} fi\n
##'''
##
##
##
##
##    fhout.write(error_handling_bowtie)
##
##    fhout.write("bash bowtie2_done  \n")
##
##    sam2bam = 'samtools view -bS  NA18487_YRI.sam > NA18487_YRI.bam \n '
##
##    fhout.write(sam2bam)
##
##    fhout.write('wait \n')
##
##
##    fhout.write(error_handling_samtools)
##
##    fhout.write("bash email_samtoolsOK  \n")
##
##
##    fhout.write('bash email_success')

    fhout.close()


def createBS2(nodes, ppn, wt, jobname, bsName, working_dir):

    fhout = open(bsName, 'w')

    options = "#!/bin/bash" + '\n'+ "#PBS -l nodes="+nodes+":ppn="+ppn+",walltime="+wt+ ',mem=8gb \n' + "#PBS -N "+jobname + '\n' + "#PBS -d " + working_dir + '\n'

    fhout.write(options)

    single_end = []
    paired = []
    fh = open('YRI_lowCoverage.csv', 'rU')
    seq_data = fh.readlines()
    fh.close()

    unpaired = ''
    mate1 = ''
    mate2 = ''


    for line in seq_data:
        flds = line.split(',')
        if (flds[9].strip() == 'NA18486') and (flds[20].strip()=='0') and (flds[12].strip()=='ILLUMINA'):
            file_loc = flds[0].strip()
            fq_file_name = ret_FQfile_name2(file_loc)
            if flds[18].strip() == 'PAIRED':
                print fq_file_name
                if re.search('_1', fq_file_name):
                    mate1 += fq_file_name + ','
                elif re.search('_2', fq_file_name):
                    mate2 += fq_file_name + ','
                else :
                    unpaired += fq_file_name + ','




    command = 'bowtie2 -p 32 --sensitive -x YRIref_index '  + '  -1 ' + mate1[:-1] + ' -2 ' + mate2[:-1] + ' -S NA18486_YRI.sam &> NA18486_bowtie2.txt '

    fhout.write(command)

    fhout.close()




def runBS(bsName):
    cmd = "qsub " + bsName

    os.system(cmd)


def tryIndent():
    error_handling_bowtie = '''if [ $? != 0 ]; then
{
    LOG = "JOB"
    echo $! >> $LOG
    echo "failed" >> $LOG
    echo $LOG
    bash email_bowtie2_fail
    exit

} fi
'''

    error_handling_samtools = '''if [ $? != 0 ]; then
{
    LOG = "JOB"
    echo $! >> $LOG
    echo "failed" >> $LOG
    echo $LOG
    bash email_samtools
    exit

} fi
'''

    print error_handling_bowtie
    print error_handling_samtools
def download_expand(file_loc):



    cmd1 = "wget -b -q ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/data/NA18486/sequence_read/SRR011037_1.filt.fastq.gz"




    job1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)



    PID1 = job1.pid
    proc1 = PS.Process(PID1)
    proc1.wait()




def main():
#    createBS('1', '8', '8:00:00','gsinghal_3' , 'gsinghal_3')
#    runBS('gsinghal_3')
#    download_expand()
#    almighty()
#    bash()
    run_alignment()
##    fastqDownload('NA18489')
#    tryIndent()
if __name__=='__main__':
    main()