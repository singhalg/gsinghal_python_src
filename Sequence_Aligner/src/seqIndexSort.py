'''
Created on Feb 17, 2012

@author: gsinghal
'''


import sys, re
from sets import Set



def indexAnalyzer(fn):

    fh = open(fn, 'rU')
    fh.readline()
    fh.readline()
    fh.readline()
    data = fh.readlines()
    fh.close()
    adict = {}  # dictionary in which key is population symbol ,eg, JPT, YRI,CEU etc. value = list of Sample names,eg, ['NA19010', 'NA10032',...]

    pset = Set([]) # set of population symbols

#    AGset = Set([])
#    CHBdata = open('CHBSamples.txt', 'w')

    for eachLine in data:
        terms = eachLine.split('\t')
        if len(terms) > 11 : # and not terms[25] == '':

#            if terms[10] =='CHB':
#                CHBdata.write(eachLine)

            if terms[10] not in pset:
                pop = terms[10]
                pset.add(pop)

                sampleList = [(terms[9], terms[25])]
                adict[pop] = sampleList
            else:
                sampleList = adict[terms[10]]
                sampleList.append((terms[9], terms[25]))
                adict[terms[10]] = sampleList
#                AGset.add(terms[25])

    print pset
    print 'Population', '\t', 'lowCoverage', '\t','[Illumina]', '\t','high coverage','\t', 'exome','\t\t', 'exon targeted','\t\t', 'Total', '\t', 'Unique individuals'
    for popSet in pset:
        popSamples = adict[popSet]
        uniqueSamples = set(popSamples)
        individuals = Set([])
        low = 0
        high = 0
        exome = 0
        exon = 0
        noAnno = 0
        Illumina = 0
        for aSample in uniqueSamples:
            individuals.add(aSample[0])
            if re.search('low', aSample[1]):
                low+=1
#                if re.search('ILLUMINA', aSample[2]):
#                    Illumina+=1
            elif re.search('high', aSample[1]):
                high+=1
            elif re.search('exome', aSample[1]):
                exome+=1
            elif re.search ('exon', aSample[1]):
                exon+=1
            else :
                noAnno+=1



        print popSet, '\t','\t', low, '\t','\t', Illumina, '\t','\t', high, '\t','\t', exome, '\t' ,'\t', exon,'[', noAnno,']', '\t','\t', len(uniqueSamples), '\t\t', len(individuals)


    CHSsamples = adict['CHS']
    uniqueCHSsamples = set(CHSsamples)
    for aCHS in uniqueCHSsamples:
        if re.search('low', aCHS[1]):
            print aCHS[0]

    fh2 = open('1000G_data.txt', 'rU')
    samples = fh2.readlines()
    fh2.close()
    sampleSet =  Set([])
    for eachline in samples:
        aSample = eachline[:7]
        sampleSet.add(aSample)
    print len(sampleSet)
    print '''Total = # datasets available per population (low coverage + high coverage + exome + exon targeted) \n
    In all, 1985 datasets available for download.\n

    Stats calculated from 20120130.sequence.index, released on Jan 30, 2012. File available at

    <ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/sequence_indices/20120130.sequence.index> '''

#    for popSet in pset:
#        print popSet, '\t', len(set(adict[popSet]))
##        print adict[popSet]
##        print set(adict[popSet])
#
#        for eachSample in set(adict[popSet]):
#            if eachSample not in sampleSet:
#                print eachSample, ' not available for download'
#
#        print '\n'
#
#
#    print AGset



def spaceToComa(fn):


    fh = open(fn, 'rU')
    data = fh.readlines()
    fh.close()
    out = open('seq_index.csv', 'w')

    for eachLine in data:
        csv = eachLine.replace('\t', ',')
        out.write(csv)

    out.close()

'''
population : YRI, CHB, JPT etc
sequenceType : low coverage, exome etc

Using the input as sequence.index file, it creates a csv file that contains only the entries corresponding to the specificed population and
sequence type. Creates and saves a csv file. Does not return anything.

'''
def sortByPopulation(population, sequenceType ):

    fh  = open('20120522.sequence.index', 'rU')
    if sequenceType.find('low') >0:
        outfile = population+'_LC.csv'
    fhout = open(outfile, 'w')
    header = fh.readline()
    outHeader = header.replace('\t', ',')
    fhout.write(outHeader)
    data = fh.readlines()
    fh.close()

    for line in data:
        flds = line.split('\t')
        if (flds[10].strip()==population) and (flds[25].strip()==sequenceType):
            outline = line.replace('\t', ',')
            fhout.write(outline)
    fhout.close()


def main():
    population = sys.argv[1]
    sequenceType = sys.argv[2]
    sortByPopulation(population, sequenceType)
##    indexAnalyzer('sequence.index')
#    spaceToComa('sequence.index')

if __name__=='__main__':
    main()

