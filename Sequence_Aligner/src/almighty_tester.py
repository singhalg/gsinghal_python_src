#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     07/05/2012
# Copyright:   (c) gsinghal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import sys, re, os
import psutil as PS
from subprocess import Popen, PIPE, STDOUT
import pickle
import time
import datetime



def fastqDownload(sampleName):

    st = time.time()
    ExitSwitch = False

    fn = 'gsinghal'+sampleName+'.log'
    log = open(fn, 'w')

##    file_loc_NCBI = "ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/"
##    file_loc_EBI = "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/"

    fh = open('YRI_lowcoverage.csv', 'rU')

    file_PID_dict = {}

    gunzipProcs = []
    switch = True
    seq_data = fh.readlines()
    fh.close()
    psList = {}
    fileNameMD5 = {}
    corruptFiles = []
    for line in seq_data:
        flds = line.split(',')
        if (flds[9].strip() == sampleName) and (flds[20].strip()== '0')  and (flds[12].strip()=='ILLUMINA'):

            if switch:

                file_loc = 'ascp -i /home/gsinghal/.aspera/connect/etc/asperaweb_id_dsa.putty -Q -l 500M -q anonftp@ftp-trace.ncbi.nlm.nih.gov:/1000genomes/ftp/'
            else:
                file_loc = 'ascp -i /home/gsinghal/.aspera/connect/etc/asperaweb_id_dsa.putty -Q -l 500M -q fasp-g1k@fasp.1000genomes.ebi.ac.uk:vol1/ftp/'

            if switch:
                switch=False
            else:
                switch=True

##            oldcmd = " wget --retry-connrefused -b -q "+ file_loc

            # in case the ascp does not work, replace the cmd with oldcmd .
            cmd = file_loc + flds[0].strip() + '   ./ '
            cmds = cmd.split()
            print cmd
            log.write(cmd)
            log.write('\n')
            job = Popen(cmds)


            PID = job.pid

            fq_file_name = ret_FQfile_name(flds[0].strip())

            file_PID_dict[PID] = fq_file_name



            psList[PID] = job

            fileNameMD5[fq_file_name] = flds[1].strip()

            time.sleep(2)
    #print file_PID_dict
    processes = file_PID_dict.keys()
    for each in processes:
        p = psList[each]
        p.wait()

        fileName = file_PID_dict[each]

        md5 = ['md5sum', fileName]
        chkSum = Popen(md5, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        procID = chkSum.pid
        md5Proc = PS.Process(int(procID))
        md5Proc.wait()
        filePrint = chkSum.stdout.read().split()[0]
        if filePrint == fileNameMD5[fileName]:
            cmd = 'gunzip  ' + fileName
            job = Popen(cmd,  shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
            print cmd
            log.write(cmd)
            log.write('\n')
            gunzipProcs.append(job)
            time.sleep(1)
        else:
            errmsg = fileName + '  is corrupt !!!   Need to be downloaded again.'
            print fileName, ' Corrupt !!!   Download again'
            corruptFiles.append(fileName)
            log.write(errmsg)
            ExitSwitch = True

    for aproc in gunzipProcs:
        aproc.wait()
    if ExitSwitch:
        print corruptFiles
        print 'These files did not download completely or correctly. Download them again and run alignments. '
        log.write('Some file is corrupt! Exiting without doing alignments  \n')
        sys.exit()
    log.write('File download complete \n')
    log.write('gunzip extraction complete \n')
    os.system(' bash mail_finish_download \n')

    end = (time.time() - st)
    timestamp =  ' It took '+ str(datetime.timedelta(seconds=end)) + ' to complete the downloading and unzipping. \n'
    print timestamp
    log.write(timestamp)

    log.close()

def bashScript(nodes, ppn, wt, working_dir, reference, samplename):

    fn = 'gsinghal'+samplename+'_testing.log'
    log = open(fn, 'a')


    jobname1 = 'gsinghal_' + samplename + '_'+reference+ '_paired_'+ppn
    jobname2 = 'gsinghal_' + samplename + '_'+reference+ '_se+'+ppn
    bsName1 = jobname1
    bsName2 = jobname2

    fhout1 = open(bsName1, 'w')
    fhout2 = open(bsName2, 'w')
    options1 = "#!/bin/bash" + '\n'+ "#PBS -l nodes="+nodes+":ppn="+ppn+",walltime="+wt+ ',mem=10gb \n' + "#PBS -N "+jobname1 + '\n' + "#PBS -d " + working_dir + '\n' + '#PBS -m abe '+'\n' +'#PBS -q dque_smp ' +'\n'

    options2 = "#!/bin/bash" + '\n'+ "#PBS -l nodes="+nodes+":ppn="+ppn+",walltime="+wt+ ',mem=10gb \n' + "#PBS -N "+jobname2 + '\n' + "#PBS -d " + working_dir + '\n' + '#PBS -m abe '+'\n' +'#PBS -q dque_smp ' +'\n'


    fhout1.write(options1)
    fhout2.write(options2)
    single_end = ''
    se_count = 0

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
                #print fq_file_name
                if re.search('_1', fq_file_name):
                    mate1 += fq_file_name + ','
                elif re.search('_2', fq_file_name):
                    mate2 += fq_file_name + ','
                else :
                    unpaired += fq_file_name + ','
            elif  flds[18].strip() == 'SINGLE':
                single_end += fq_file_name + ','
                se_count+=1


    proc = str(int(nodes)*int(ppn))
# writing bowtie command for paired mates
    outFile1 = samplename+'_'+reference+'_'+proc+'_paired.sam'
    stdoutFile = samplename+'_'+reference+'_'+proc+'_paired_bowtie2.txt  '

    command = 'bowtie2 -p ' + proc +'  --sensitive  -X 1000  -x  ' + reference+ '  -1 ' + mate1[:-1] + ' -2 ' + mate2[:-1] +  ' -S '+outFile1 +' &>  '+ stdoutFile

    fhout1.write(command)
    fhout1.write('\n')
    fhout1.write('bash mail_bowtie_paired \n')
    log.write('Writing bowtie commands to the bash script \n')
    log.write(command)
    log.write('\n')

    # deleting sam file
    command = 'rm  ' + outFile1
    fhout1.write(command)
    fhout1.write('\n')
    fhout1.write('bash mail_del_sam \n')

    log.write(command)
    log.write('\n')

# writing bowtie command for single ended reads
    if se_count>0:
        outFile2 = samplename+'_'+reference+'_'+proc+'_se.sam'
        stdoutFile = samplename+'_'+reference+'_se_bowtie2.txt  '

        command = 'bowtie2 -p ' + proc +'  --sensitive -x  ' + reference+ '  -U ' + single_end[:-1] +  ' -S '+outFile2 +' &>  '+ stdoutFile

        fhout2.write(command)
        fhout2.write('\n')

        log.write(command)
        log.write('\n')

        fhout2.write('bash mail_bowtie_se \n')
    else:
        log.write('NO SINGLE END READS IN THIS SAMPLE \n')





    if se_count>0:
        command = 'samtools view -bS  ' + outFile2 + ' > ' + outFile2[:-4] + '.bam'
        fhout2.write(command)
        fhout2.write('\n')
        fhout2.write('bash mail_samtools_se \n')
        log.write(command)
        log.write('\n')


##    #now moving the results to their respective locations
##
##    YRI_reloc_paired = '''
##
##    '''
##
##    if reference == 'YRIref_index':
##
##        fhout1.write(YRI_reloc_paired)
##        fhout2.write(YRI_reloc_single)
    fhout1.write('sleep 2')
    fhout2.write('sleep 2')
    log.close()
    fhout1.close()
    fhout2.close()
    return bsName1, bsName2


def runBS(bsName):
    cmd = "qsub " + bsName

    os.system(cmd)


def ret_FQfile_name(file_loc):
    start = file_loc.find('read')
    s = 0
    if start < 0:
        print 'FILE NAME ERROR ', file_loc
    else:
        s = start+ 5

    return file_loc[s:].strip()


def ret_FQfile_name2(file_loc):
    start = file_loc.find('read')
    s = 0
    if start < 0:
        print 'FILE NAME ERROR ', file_loc
    else:
        s = start+ 5

    return file_loc[s:-3].strip()




def control(sampleName, processes):

##    fastqDownload(sampleName)
    #bashScript(nodes, ppn, wt, working_dir, reference, samplename)
##    bsName1, bsName2 = bashScript('1', processes, '12:00:00' , '/scratch/gsinghal/YRI_LC/' , 'YRIref_index', sampleName)
##    runBS(bsName1)
##    runBS(bsName2)
    bsName1, bsName2 = bashScript('1', processes, '12:00:00' , '/scratch/gsinghal/YRI_LC/' , 'hg19', sampleName)
##    runBS(bsName1)
##    runBS(bsName2)


def almightyTester():
    control('NA18519', '8')
    control('NA18519', '16')
    control('NA18519', '24')
    control('NA18519', '32')
    control('NA18519', '40')
    control('NA18519', '48')
    control('NA18519', '56')
    control('NA18519', '64')



def main():
    almightyTester()


if __name__ == '__main__':
    main()
