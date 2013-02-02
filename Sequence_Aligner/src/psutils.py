'''
Created on Apr 6, 2012

@author: gsinghal
'''


import sys, re, os, psutils


'''


'''
def createBS(nodes, ppn, wt, jobname, bsName):
    
    fhout = open(bsName, 'w')
    
    options = "#!/bin/bash"+ '\n'+"#PBS -l nodes="+nodes+":ppn="+ppn+",walltime="+wt+ ',mem=5gb \n' + "#PBS -N "+jobname + '\n'
    
    fhout.write(options)
    
    command = 'nohup bowtie2 -p 8 --sensitive -x YRIref_index -U SRR006273.filt.fastq -S NA18498_YRI_unpaired.sam &'
    fhout.write(command)
    fhout.close()
    

def runBS(bsName):
    cmd = "qsub " + bsName 
    
    os.system(cmd)

def psutils_try():
    
    
    
    pass

    a = 4    
    return 0
    
def main():
    createBS('1', '8', '8:00:00','gsinghal_3' , 'gsinghal_3')
    runBS('gsinghal_3')
    
if __name__=='__main__':
    main()