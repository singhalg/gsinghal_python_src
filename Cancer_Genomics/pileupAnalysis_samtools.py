#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gsinghal
#
# Created:     17/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import datetime
import sys
from sets import Set

import re, os
##import psutil as PS
from subprocess import Popen, PIPE, STDOUT

'''
This is the main method which does variant detection and calculation of variant allele frequency. It reports the results in vcf format.

'''
def pileupSummary(pileup, outfile):
    now = datetime.datetime.now()
    fhout = open(outfile, 'w')
    fhout.write("##fileformat=VCFv4.1 \n")
    outline = "##File Generated at : " + str(now) + "__ \n"
    fhout.write(outline)

    fhout.write('''##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth"> \n''')
    fhout.write('''##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency"> \n''')
    outline = '#CHROM' + '\t'+ 'POS' +  '\t' +  'ID' + '\t' + 'REF' + '\t' + 'ALT' +  '\t' +  'QUAL'+  '\t' +  'FILTER'+  '\t' +  'INFO' + '\n'
    fhout.write(outline)

    fhin = open(pileup, 'r')
    #data = fhin.readlines(1000000000) ## CANT do this, need to read the pileup file line by line.

    for line in fhin:
        flds = line.split('\t')
        chrom = flds[0].strip()[3:]
        pos = flds[1].strip()
        ref = flds[2].strip()
        depth = flds[3].strip()
        pile = flds[4].strip()
        alt_all = {}
        ins = False
        deletion = False
        skipCheck = False
        getCount = 0

        if (int(depth) >= 10) :
            for n in range(len(pile)):
                abase = pile[n]


                if validityCheck(abase):

##                if (abase !='.') or (abase != ',') or (abase != '^') or (abase !='$') :
                    if getCount>0:
                        getCount-=1
                        pass
                    else:
                        if abase == '+':
##                            ins = True
##                            skipCheck = True
                            if 'In' in alt_all:
                                baseCount = alt_all['In']
                                baseCount+=1
                                alt_all['In'] = baseCount
                            else:
                                alt_all['In'] = 1
##                            print pile[n+1]
                            try:
                                getCount = int(pile[n+1])+1
                            except:
                                pass
##                                print pile[n]
##                                print line
                        elif abase == '-':
##                            deletion = True
##                            skipCheck = True
                            if 'Del' in alt_all:
                                baseCount = alt_all['Del']
                                baseCount+=1
                                alt_all['Del'] = baseCount
                            else:
                                alt_all['Del'] = 1
##                            print pile[n+1]
                            try:
                                getCount = int(pile[n+1])+1
                            except:
                                pass
##                                print pile[n], ' ', pile[n+1]
##                                print line
                        elif abase == '^':

                            getCount = 1


                        else:
                            base = abase.upper()

                            if base in alt_all:
                                baseCount = alt_all[base]
                                baseCount+=1
                                alt_all[base] = baseCount
                            else:
                                alt_all[base] = 1
                else:
                    pass



            alt = ''
            VAF = ''
            bases = Set(['A', 'T', 'C', 'G']) ## earlier, the bases was = Set(['A','T','G','C','N'])
            alt_all_set = Set(alt_all.keys())
            if len(alt_all_set & bases ) > 0:
                for each in alt_all.keys():
                    alt_al_depth = alt_all[each]
                    if alt_al_depth > 1:

                        alt+=each + ','
                        af = float(alt_all[each])/float(depth)
                        VAF+= str(af) + ','

                if len(alt)>0:
                    outline = chrom + '\t' + pos + '\t' + '.'+ '\t' +ref + '\t'  + alt[:-1] + '\t' + '100'+ '\t' + 'PASS' +'\t' + 'DP='+ depth + ';AF=' + VAF[:-1] + '\n'
                    fhout.write(outline)
                else:
                    pass
##                    print line
        else:
            pass






def pileupSummaryFast(pileup, outfile):
    now = datetime.datetime.now()
    fhout = open(outfile, 'w')
    fhout.write("##fileformat=VCFv4.1 \n")
    outline = "##File Generated at : " + str(now) + "__ \n"
    fhout.write(outline)

    fhout.write('''##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth"> \n''')
    fhout.write('''##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency"> \n''')
    outline = '#CHROM' + '\t'+ 'POS' +  '\t' +  'ID' + '\t' + 'REF' + '\t' + 'ALT' +  '\t' +  'QUAL'+  '\t' +  'FILTER'+  '\t' +  'INFO' + '\n'
    fhout.write(outline)
    output = []

    fhin = open(pileup, 'rU')
    #data = fhin.readlines(1000000000) ## CANT do this, need to read the pileup file line by line.
    data = fhin.readlines()
    fhin.close()
    for line in data:
        flds = line.split('\t')
        chrom = flds[0].strip()[3:]
        pos = flds[1].strip()
        ref = flds[2].strip()
        depth = flds[3].strip()
        pile = flds[4].strip()
        alt_all = {}
        ins = False
        deletion = False
        skipCheck = False
        getCount = 0

        if (int(depth) >= 10) :
            for n in range(len(pile)):
                abase = pile[n]


                if validityCheck(abase):

##                if (abase !='.') or (abase != ',') or (abase != '^') or (abase !='$') :
                    if getCount>0:
                        getCount-=1
                        pass
                    else:
                        if abase == '+':
##                            ins = True
##                            skipCheck = True
                            if 'In' in alt_all:
                                baseCount = alt_all['In']
                                baseCount+=1
                                alt_all['In'] = baseCount
                            else:
                                alt_all['In'] = 1
##                            print pile[n+1]
                            try:
                                getCount = int(pile[n+1])+1
                            except:
                                pass
##                                print pile[n]
##                                print line
                        elif abase == '-':
##                            deletion = True
##                            skipCheck = True
                            if 'Del' in alt_all:
                                baseCount = alt_all['Del']
                                baseCount+=1
                                alt_all['Del'] = baseCount
                            else:
                                alt_all['Del'] = 1
##                            print pile[n+1]
                            try:
                                getCount = int(pile[n+1])+1
                            except:
                                pass
##                                print pile[n], ' ', pile[n+1]
##                                print line
                        elif abase == '^':

                            getCount = 1


                        else:
                            base = abase.upper()

                            if base in alt_all:
                                baseCount = alt_all[base]
                                baseCount+=1
                                alt_all[base] = baseCount
                            else:
                                alt_all[base] = 1
                else:
                    pass



            alt = ''
            VAF = ''
            bases = Set(['A', 'T', 'C', 'G']) ## earlier, the bases was = Set(['A','T','G','C','N'])
            alt_all_set = Set(alt_all.keys())
            if len(alt_all_set & bases ) > 0:
                for each in alt_all.keys():
                    alt_al_depth = alt_all[each]
                    if alt_al_depth > 1:

                        alt+=each + ','
                        af = float(alt_all[each])/float(depth)
                        VAF+= str(af) + ','

                if len(alt)>0:
                    outline = chrom + '\t' + pos + '\t' + '.'+ '\t' +ref + '\t'  + alt[:-1] + '\t' + '100'+ '\t' + 'PASS' +'\t' + 'DP='+ depth + ';AF=' + VAF[:-1] + '\n'
                    output.append(outline)
##                    fhout.write(outline)
                else:
                    pass
##                    print line
        else:
            pass

    fhout.writelines(output)






'''
depth >=5
if alt allele has >=2 reads


'''

def validityCheck(letter):
    if letter == '$':
        return False
    elif letter == '.':
        return False
    elif letter == ',':
        return False
    elif letter == '"':
        return False
    elif letter == '#':
        return False
    elif letter == '&':
        return False
    elif letter == '!':
        return False
    elif letter == ';':
        return False
    elif letter == '[':
        return False
    elif letter == ']':
        return False

    else:
        return True


def bamToVCF(hg19, geneBed, bamFile):
    sortedBam = bamFile[:-4] + '_sorted.bam'
    samtoolsSort = 'samtools sort ' + bamFile + ' ' +sortedBam[:-4]

    runSamtoolsSort = Popen(samtoolsSort, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

    print 'Running the samtools sort '
    print samtoolsSort
##    ssprocID = runSamtoolsSort.pid
##    ssort = PS.Process(int(ssprocID))
##    ssort.wait()
    runSamtoolsSort.wait()


    samtoolsIndex = 'samtools index ' + sortedBam

    runSamtoolsIndex = Popen(samtoolsIndex, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    print 'Running the samtools index '
    print samtoolsIndex

##    siprocID = runSamtoolsIndex.pid
##    sindex = PS.Process(int(siprocID))
##    sindex.wait()
    runSamtoolsIndex.wait()


    mpileupFile = bamFile[:-4]+'_mpileup.txt'
    vcfFile = bamFile[:-4]+'.vcf'

    samtools = 'samtools mpileup -f ' + hg19 + '  -l '+ geneBed + '  ' + sortedBam + ' > ' + mpileupFile


    runMpileup = Popen(samtools, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    print 'Running the mpileup '
    print samtools
##    procID = runMpileup.pid
##    mpileup = PS.Process(int(procID))
##    mpileup.wait()
    runMpileup.wait()
    print 'Now generating the vcf file '
    pileupSummaryFast(mpileupFile, vcfFile)


def main():
##    pileup_file = sys.argv[1]
##    output_filename = sys.argv[2]
##    pileupSummary(pileup_file, output_filename)

    hg19 = sys.argv[1]
    geneBed = sys.argv[2]
    bamFile = sys.argv[3]
    bamToVCF(hg19, geneBed, bamFile)

if __name__ == '__main__':
    main()
