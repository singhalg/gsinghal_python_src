#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     20/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/
#-------------------------------------------------------------------------------
import datetime, pickle, sys
from sets import Set


def addAlleleFreq(vcfFile, pileup, outfile):

##def pileupSummaryFast(pileup, outfile):
    now = datetime.datetime.now()
    fhout = open(outfile, 'w')
    fhout.write("##fileformat=VCFv4.1 \n")
    outline = "##File Generated at : " + str(now) + "__ \n"
    fhout.write(outline)

##    vcfData = {}
    pileupData = {}

    fhout.write('''##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth"> \n''')
    fhout.write('''##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency"> \n''')
    fhout.write('''##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype"> \n''')
    fhout.write('''##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality"> \n''')
    fhout.write('''##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth"> \n''')
    outline = '#CHROM' + '\t'+ 'POS' +  '\t' +  'ID' + '\t' + 'REF' + '\t' + 'ALT' +  '\t' +  'QUAL'+  '\t' +  'FILTER'+  '\t' +  'INFO' + '\t' +'FORMAT' + '\t' + 'data' +'\n'
    fhout.write(outline)
    output = []

    fhin = open(pileup, 'rU')
    #data = fhin.readlines(1000000000) ## CANT do this, need to read the pileup file line by line.
    data = fhin.readlines()
    fhin.close()
    for line in data:
        flds = line.split('\t')
        chrom = flds[0].strip()[3:]
        pos = flds[2].strip()
        key = chrom + '#' + pos
        pileupData[key] = flds[9]
    del data


    vcfFhin = open(vcfFile, 'rU')
    vcfData = vcfFhin.readlines()
    vcfFhin.close()




    for line in vcfData[7:]:
        flds = line.split('\t')
        chrom = flds[0].strip()[3:]
        pos = flds[1].strip()
        key = chrom + '#' + pos

        pile = pileupData[key]

##            print line
        ref = flds[3].strip()
        ALT = flds[4].strip()
        depth = flds[7].strip().split(';')[0][3:]
        qual = flds[5]
        format_flds = flds[8]
        format_data = flds[9].strip()


        alt_all = {}
        ins = False
        deletion = False
        skipCheck = False
        getCount = 0

##        if (int(depth) >= 10) :
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


##
##            alt = ''
##            VAF = ''
##            bases = Set(['A', 'T', 'C', 'G']) ## earlier, the bases was = Set(['A','T','G','C','N'])
##            alt_all_set = Set(alt_all.keys())
##            if len(alt_all_set & bases ) > 0:
##                for each in alt_all.keys():
##                    alt_al_depth = alt_all[each]
##                    if alt_al_depth > 1:
##
##                        alt+=each + ','
##                        af = float(alt_all[each])/float(depth)
##                        VAF+= str(af) + ','
##
##                if len(alt)>0:
        alt = ''
        allele_freq =''
        bases = Set(['A', 'T', 'C', 'G']) ## earlier, the bases was = Set(['A','T','G','C','N'])
        alt_all_set = Set(alt_all.keys())
        if len(alt_all_set & bases ) > 0:
            for each in ALT.split(','):
                if each in alt_all_set:
                    alt+=each+','
                    allele_freq += str(float(alt_all[each])/int(depth)) +','
            if len(alt)>0:
                outline = chrom + '\t' + pos + '\t' + '.'+ '\t' +ref + '\t'  + alt[:-1] + '\t' + qual + '\t' + 'PASS' +'\t' + 'DP='+ depth + ';AF=' + allele_freq[:-1] + '\t'  + format_flds  + '\t'+ format_data+  '\n'
                output.append(outline)

##                    fhout.write(outline)
##                else:
##                    pass
##                    print line
##        else:
##            pass

    fhout.writelines(output)



    fhout.close()






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


def addAlleleFreqToAllFiles(index):


    files = [
##      ['PT_3_lung_1123221.vcf','PT_3_brain_1123220.vcf'],
##                ['PT_10_lung_1200384.vcf','PT_10_brain_1200360.vcf'],
##                ['PT_11_lung_1200363.vcf', 'PT_11_brain_1200385.vcf'],
##                ['PT_12_lung_1200381.vcf', 'PT_12_brain_1200368.vcf'],

                ['PT_1_lung_1123233.vcf', 'PT_1_brain_1123232.vcf'],
                ['PT_6_lung_1123227.vcf', 'PT_6_brain_1123226.vcf'],
                ['PT_9_lung_1200382.vcf',  'PT_9_brain_1200383.vcf'],
                ['PT_13_lung_1202946.vcf', 'PT_13_brain_1200370.vcf'],
                ['PT_2_lung_1123231.vcf', 'PT_2_brain_1123230.vcf']]

    for eachPatient in files:

        end = eachPatient[index].find('_lung')   ####----------------==============----------===========-------------=============
        fileName = eachPatient[index][:end] + '_lung_snpInExon.vcf'
        outFileName = eachPatient[index][:end] + '_lung.vcf'
        pileupFile = eachPatient[index][:end] +'_lung_pileup.txt'
        addAlleleFreq(fileName, pileupFile, outFileName)
        print fileName, 'processed !!'



def main():
##    vcf = sys.argv[1]
##    pileup = sys.argv[2]
##    outfile = sys.argv[3]
##    addAlleleFreq(vcf, pileup, outfile)
    addAlleleFreqToAllFiles(0)
if __name__ == '__main__':
    main()
