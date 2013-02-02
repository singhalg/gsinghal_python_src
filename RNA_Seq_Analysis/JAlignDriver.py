'''
Created on Feb 24, 2011

@author: Gaurav
'''


import sys, os

import subprocess

'''
In this python script, I need to create a fasta file for each of the repeat instances, then do the java alignment,
if the alignment score is greater than cutoff, then save the fasta sequence and score in a big comprehensive fasta file. 

Do this for each of the four promoter sequences. 


use the subprocess module instead of popen2

'''

def jAlignDriver(promoter, repSequence):
    
    fastaIn = open(repSequence, 'rU')
    completeFasta = fastaIn.read()
    fastaList = completeFasta.split('>')
    
    outfile =  promoter[:-4]+ repSequence [-5:-3] +'_Out.fa'
    
    fastaOut = open( outfile, 'w')
    
    
    if promoter[:-6] == 'L1ASP':
        cutoff = 950
    elif promoter[:-6] == 'L1SP':
        cutoff = 650
    
    
    for each in fastaList[1:]:
        
        repinstanceTag =  promoter[:-4] + repSequence[-5:-3] 
        aRepInstance = open(repinstanceTag, 'w')
        aRepInstance.write('>' + each.rstrip())
        aRepInstance.close()
        
        
        
        javaCommand = "java Align "
        strCommand= javaCommand+ promoter+" "+repinstanceTag
#        cmd1 = 'java Align  ' + promoter + '  ' +repinstanceTag

        
        
        p = subprocess.Popen(strCommand, shell=True, stdout=subprocess.PIPE)
        output, errors = p.communicate()
        
        soutput = output.strip()
#        print "the output is " , soutput
        
        score = float(soutput)
        
        
        
        if score >= cutoff:
            
            fastaOut.write('>' + soutput + '#'+ each )
#        else:
#            'score < cutoff, so skipping'
            
        cmd2 = 'rm ' + repinstanceTag
        os.system(cmd2)
#        print 'deleted the file'
        
        
    fastaOut.close()
    fastaIn.close()
    


def jAlignerDriverbench():
#    cmd = ['java ' ,' Align ' , ' L1ASP35.txt',' L1MB3.txt']
##    sout, sin = os.popen2(cmd)
##    output = sout.read()
#    cmd1 = 'java Align L1ASP35.txt L1MB3.txt'
#    subprocess.Popen(cmd1, shell=True)

    
#    proc = subprocess.Popen(cmd1, stdout=subprocess.PIPE, )
#    stdout_value = proc.communicate()[0]
#    print repr(stdout_value)
    
    promoter = 'L1ASP35.txt'
    repSequence = 'L1MB3.txt'
    
    cmd = 'java Align '
    strcmd = cmd +  promoter+ ' ' + repSequence
    print strcmd
    p = subprocess.Popen(strcmd ,shell=True,stdout=subprocess.PIPE)
    output, errors = p.communicate()
    score = float(output.strip())
    if score > 250:
        print "score is greater than 250"
        print "score is : ", score  



def splitFastaTester(repSequence):
    fastaIn = open(repSequence, 'rU')
    completeFasta = fastaIn.read()
    fastaList = completeFasta.split('>')
    num = 0
   
    for each in fastaList[:5]:
        num+=1
        print 'fasta sequence #', num, '  is : '
        print each.rstrip()
    


def main():
    
#    jAlignerDriverbench()
    promoterfile = sys.argv[1]
    filerepSequence = sys.argv[2]
    jAlignDriver(promoterfile, filerepSequence)
#    repSeq = sys.argv[1]
#    splitFastaTester(repSeq)

    
    
    

    
    
if __name__ == '__main__':
    main()