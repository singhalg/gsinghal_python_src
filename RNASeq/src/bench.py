'''
Created on Feb 17, 2011

@author: Gaurav
'''
import sys
import os

import subprocess


def splitfa(file):
    fasta = open(file, 'rU')
    completeFasta = fasta.read()
    
    fastaLists = completeFasta.split('>')
    for each in fastaLists:
        print each

def getLineNumber(file, linenumberStart, linenumberEnd):
    fasta = open(file, 'rU')
    completeFasta = fasta.readlines()
    fasta.close()
    for each  in completeFasta[int(linenumberStart): int(linenumberEnd)]:
        print each
    
def errorLearning():
    try:
        infile = open('hashset', 'r')

    except:
        print 
def fastacize(string):
    
    size = len(string)
    s = 0
    e = s+50
    fasta = ''
    while e < size:
        fasta += string[s:e] + '\n'
        s+= 50
        e= s+50
    fasta+= string[s:size]+'\n'
    return fasta


def jAlignerDriverbench():
#    cmd = ['java ' ,' Align ' , ' L1ASP35.txt',' L1MB3.txt']
##    sout, sin = os.popen2(cmd)
##    output = sout.read()
#    cmd1 = 'java Align L1ASP35.txt L1MB3.txt'
#    subprocess.Popen(cmd1, shell=True)

    
#    proc = subprocess.Popen(cmd1, stdout=subprocess.PIPE, )
#    stdout_value = proc.communicate()[0]
#    print repr(stdout_value)
    
    cmd = 'java Align L1ASP35.txt L1MB3.txt '
    p = subprocess.Popen(cmd ,shell=True,stdout=subprocess.PIPE)
    output, errors = p.communicate()
    score = float(output.strip())
    if score > 250:
        print "score is greater than 250"
        print "score is : ", score
    
#    output = subprocess.check_call(cmd1)
#    print output
    
#    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
#    output = p.stdout.read()
#    print output
    




def subprocs():
    cmd = 'ls /etc/fstab /etc/non-existent-file'
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read()
    print output

def printUsage():
    pass

def main():
#    print fastacize('ATATCCCGTGTGGGGGGGGGGGGGGGGGAAAAAAAAAATTTTTTTTTTGGGGGGGGGGCCCCCCCCCCCNNNNNNTTTTTTTTTTTTTTTTTTTTTTTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATGGGGGGGGGGGCCCCCCCCCC')
#    file = sys.argv[1]
#    subprocs()
#    splitfa(file)
#    subprocs()



    file = sys.argv[1]
    fromlinenumber = sys.argv[2]
    tolinenumber = sys.argv[3]
    getLineNumber(file, fromlinenumber, tolinenumber)
#    jAlignerDriverbench()
   
if __name__ == '__main__':
    main() 
    