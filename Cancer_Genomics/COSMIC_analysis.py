#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     21/04/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

from sets import Set
from sklearn.externals import joblib
import pickle
import numpy as np
import matplotlib.pyplot as plt
import time

def geneBySite(file_name1, file_name2):
    fhin = open(file_name1, 'rU')
    data = fhin.readlines()
    fhin.close()
    pSite = {}

    for line in data[1:]:
        flds = line.split(',')
        if flds[7] not in pSite: # in case the psite does not exist
            geneDict  = {} # this will become a new value in pSite
            mutationList =[]
            mutationList.append(flds[15])
            geneDict[flds[0]] = mutationList
            pSite[flds[7]] = geneDict # new entry for the primary site has been created.
        else:
            genDict = pSite[flds[7]]
            if flds[0] in genDict: # if gene entry is present in that cancer
                mutList = genDict[flds[0]]
                mutList.append(flds[15])
                genDict[flds[0]] = mutList
                pSite[flds[7]] = genDict

            else:
                # create new entry with gene name as the key and list of mutation types as value
                mutList = []
                mutList.append(flds[15])
                genDict[flds[0]] = mutList


                pSite[flds[7]] = genDict



    fhin = open(file_name2, 'rU')
    data2 = fhin.readlines()
    fhin.close()



    for line in data2[1:]:
        flds = line.split(',')
        if flds[4] not in pSite:
            geneDict  = {} # this will become a new value in pSite
            mutationList =[]
            mutationList.append(flds[12])
            geneDict[flds[0]] = mutationList
            pSite[flds[4]] = geneDict # new entry for the primary site has been created.
        else:
            genDict = pSite[flds[4]]
            if flds[0] in genDict: # if gene entry is present in that cancer
                mutList = genDict[flds[0]]
                mutList.append(flds[12])
                genDict[flds[0]] = mutList
                pSite[flds[4]] = genDict

            else:
                # create new entry with gene name as the key and list of mutation types as value
                mutList = []
                mutList.append(flds[12])
                genDict[flds[0]] = mutList

                pSite[flds[4]] = genDict


##    keys = pSite.keys()
##    for each in keys[:10]:
##        print each
##        genDict = pSite[each]
##        genes = genDict.keys()
##        for aGene in genes[:10]:
##            print aGene, genDict[aGene]

    return pSite



def geneBySiteCSV(file_name1, file_name2, pickleDump):

    geneSet = Set([])

    fhin = open(file_name1, 'rU')
    data = fhin.readlines()
    fhin.close()

    for line in data[1:]:
        flds = line.split(',')
        geneSet.add(flds[0])

    fhin = open(file_name2, 'rU')
    data2 = fhin.readlines()
    fhin.close()
    for line in data2[1:]:
        flds = line.split(',')
        geneSet.add(flds[0])

    print '# of genes = ', len(geneSet)
    genes = sorted(list(geneSet))


    pSite = geneBySite(file_name1, file_name2)
    primarySites = sorted(pSite.keys())

    fhout = open('geneByPrimSite.csv', 'w')
    firstline = 'Genes,' + ','.join(primarySites) + '\n'
    fhout.write(firstline)

    geneSite = []

    for aGene in genes:
        geneScore = []
        for aSite in primarySites:
            geneDict = pSite[aSite]
            if aGene in geneDict:
                geneScore.append(processGene(geneDict[aGene]))
            else:
                geneScore.append(0)
        geneSite.append(geneScore)

    geneSiteArr = np.array(geneSite)

    if pickleDump:
        fhPickle = open('gene_primarySites.pkl', 'w')
        pickle.dump(geneSite, fhPickle)
        fhPickle.close()
        joblib.dump(geneSiteArr, 'gene_primarySiteArr.pkl')

    for i in range(len(genes)):
        geneSiteStr = [str(n) for n in geneSite[i]]
        outline = genes[i]+ ','+ ','.join(geneSiteStr) + '\n'
        fhout.write(outline)

    fhout.close()
    print 'DONE'

    return primarySites, genes, geneSite, geneSiteArr



def geneByOrigin(file_name1):
    fhin = open(file_name1, 'rU')
    data = fhin.readlines()
    fhin.close()
    pSite = {}

    for line in data[1:]:
        flds = line.split(',')
        if flds[24] not in pSite: # in case the site of origin does not exist (site of origin can be primary, metastasis, NS etc
            geneDict  = {} # this will become a new value in pSite
            mutationList =[]
            mutationList.append(flds[15])
            geneDict[flds[0]] = mutationList
            pSite[flds[24]] = geneDict # new entry for the site of origin has been created.
        else:
            genDict = pSite[flds[24]]
            if flds[0] in genDict: # if gene entry is present in that cancer
                mutList = genDict[flds[0]]
                mutList.append(flds[15])
                genDict[flds[0]] = mutList
                pSite[flds[24]] = genDict

            else:
                # create new entry with gene name as the key and list of mutation types as value
                mutList = []
                mutList.append(flds[15])
                genDict[flds[0]] = mutList


                pSite[flds[24]] = genDict






##    keys = pSite.keys()
##    for each in keys[:10]:
##        print each
##        genDict = pSite[each]
##        genes = genDict.keys()
##        for aGene in genes[:10]:
##            print aGene, genDict[aGene]

    return pSite



def geneByOriginCSV(file_name1, pickleDump):

    geneSet = Set([])

    fhin = open(file_name1, 'rU')
    data = fhin.readlines()
    fhin.close()

    for line in data[1:]:
        flds = line.split(',')
        geneSet.add(flds[0])



    print '# of genes = ', len(geneSet)
    genes = sorted(list(geneSet))


    pSite = geneByOrigin(file_name1)
    primarySites = sorted(pSite.keys())

    fhout = open('geneByOriginSite_v60.csv', 'w')
    firstline = 'Genes,' + ','.join(primarySites) + '\n'
    fhout.write(firstline)

    geneSite = []

    for aGene in genes:
        geneScore = []
        for aSite in primarySites:
            geneDict = pSite[aSite]
            if aGene in geneDict:
                geneScore.append(processGene(geneDict[aGene]))
            else:
                geneScore.append(0)
        geneSite.append(geneScore)

    geneSiteArr = np.array(geneSite)

    if pickleDump:
        fhPickle = open('gene_originSites.pkl', 'w')
        pickle.dump(geneSite, fhPickle)
        fhPickle.close()
        joblib.dump(geneSiteArr, 'gene_originSiteArr.pkl')

    for i in range(len(genes)):
        geneSiteStr = [str(n) for n in geneSite[i]]
        outline = genes[i]+ ','+ ','.join(geneSiteStr) + '\n'
        fhout.write(outline)

    fhout.close()
    print 'DONE'

    return primarySites, genes, geneSite, geneSiteArr

def processGene(flds):
    score = 0
    adict = {'Complex - compound substitution':1,
    'Complex - deletion inframe':1,
    'Complex - frameshift':4,
    'Complex - insertion inframe':1,
    'Deletion - Frameshift':4,
    'Deletion - In frame':1,
    'Insertion - Frameshift':4,
    'Insertion - In frame':1,
    'Mutations':0,
    'No detectable mRNA/protein':4,
    'Nonstop extension':4,
    'Substitution - Missense':1,
    'Substitution - Nonsense':4,
    'Substitution - coding silent':0,
    'Unknown':0,
    'Whole gene deletion':4,
    'Complex':1
    }



    for each in flds:
##        if each in adict:
        score+= adict[each]
##        else:
##            print each
    return score



def geneByHistology(file_name1, file_name2):
    # reading from point mutation data
    fhin = open(file_name1, 'rU')
    data = fhin.readlines()
    fhin.close()
    pSite = {}

    for line in data[1:]:
        flds = line.split(',')
        if flds[8] not in pSite:
            geneDict  = {} # this will become a new value in pSite
            mutationList =[]
            mutationList.append(flds[14])
            geneDict[flds[0]] = mutationList
            pSite[flds[8]] = geneDict # new entry for the primary site has been created.
        else:
            genDict = pSite[flds[8]]
            if flds[0] in genDict: # if gene entry is present in that cancer
                mutList = genDict[flds[0]]
                mutList.append(flds[14])
                genDict[flds[0]] = mutList
                pSite[flds[8]] = genDict

            else:
                # create new entry with gene name as the key and list of mutation types as value
                mutList = []
                mutList.append(flds[14])
                genDict[flds[0]] = mutList

                pSite[flds[8]] = genDict


    # now reading from insertion data :
    fhin = open(file_name2, 'rU')
    data2 = fhin.readlines()
    fhin.close()



    for line in data2[1:]:
        flds = line.split(',')
        if flds[6] not in pSite:
            geneDict  = {} # this will become a new value in pSite
            mutationList =[]
            mutationList.append(flds[12])
            geneDict[flds[0]] = mutationList
            pSite[flds[6]] = geneDict # new entry for the primary site has been created.
        else:
            genDict = pSite[flds[6]]
            if flds[0] in genDict: # if gene entry is present in that cancer
                mutList = genDict[flds[0]]
                mutList.append(flds[12])
                genDict[flds[0]] = mutList
                pSite[flds[6]] = genDict

            else:
                # create new entry with gene name as the key and list of mutation types as value
                mutList = []
                mutList.append(flds[12])
                genDict[flds[0]] = mutList

                pSite[flds[6]] = genDict


##    keys = pSite.keys()
##    for each in keys[:10]:
##        print each
##        genDict = pSite[each]
##        genes = genDict.keys()
##        for aGene in genes[:10]:
##            print aGene, genDict[aGene]

    return pSite




def geneByHistologyCSV(file_name1, file_name2, pickleDump):
    geneSet = Set([])

    fhin = open(file_name1, 'rU')
    data = fhin.readlines()
    fhin.close()

    for line in data[1:]:
        flds = line.split(',')
        geneSet.add(flds[0])

    fhin = open(file_name2, 'rU')
    data2 = fhin.readlines()
    fhin.close()
    for line in data2[1:]:
        flds = line.split(',')
        geneSet.add(flds[0])

    print '# of genes = ', len(geneSet)
    genes = sorted(list(geneSet))


    pSite = geneByHistology(file_name1, file_name2)
    primarySites = sorted(pSite.keys())

    fhout = open('geneByPrimHist.csv', 'w')
    firstline = 'Genes,' + ','.join(primarySites) + '\n'
    fhout.write(firstline)

    geneSite = []

    for aGene in genes:
        geneScore = []
        for aSite in primarySites:
            geneDict = pSite[aSite]
            if aGene in geneDict:
                geneScore.append(processGene(geneDict[aGene]))
            else:
                geneScore.append(0)
        geneSite.append(geneScore)

    geneSiteArr = np.array(geneSite)

    if pickleDump:
        fhPickle = open('gene_primaryHist.pkl', 'w')
        pickle.dump(geneSite, fhPickle)
        fhPickle.close()
        joblib.dump(geneSiteArr, 'gene_primaryHistArr.pkl')

    for i in range(len(genes)):
        geneSiteStr = [str(n) for n in geneSite[i]]
        outline = genes[i]+ ','+ ','.join(geneSiteStr) + '\n'
        fhout.write(outline)

    fhout.close()
    print 'DONE'

    return primarySites, genes, geneSite, geneSiteArr


def geneByIndividuals(file_name1, file_name2):
    # now opening CosmicMutantExport_v58_150312.csv
    fhin = open(file_name1, 'rU')
    data = fhin.readlines()
    fhin.close()
    Individual = {}

    relevant = relevance()

    relevantIds = Set([])
    for eachId in relevant:
        relevantIds.add(eachId[0])

    del relevant

    for line in data[1:]:
        flds = line.split(',')
        if flds[4] in relevantIds:
            if flds[4] not in Individual: # in case the entry for this sample_ID does not exist
                geneDict  = {} # this will become a new value in pSite
                mutationList =[]
                mutationList.append(flds[14])
                geneDict[flds[0]] = mutationList
                Individual[flds[4]] = geneDict # new entry for the primary site has been created.
            else:
                genDict = Individual[flds[4]]
                if flds[0] in genDict: # if gene entry is present in that cancer
                    mutList = genDict[flds[0]]
                    mutList.append(flds[14])
                    genDict[flds[0]] = mutList
                    Individual[flds[4]] = genDict

                else:
                    # create new entry with gene name as the key and list of mutation types as value
                    mutList = []
                    mutList.append(flds[14])
                    genDict[flds[0]] = mutList


                    Individual[flds[4]] = genDict




    sampleNameID = sampleMap() # getting sample name and id mappings from CosmicMutantExport_v58_150312.csv

    # now opening 'CosmicInsMutExport_v58_150312.csv'
    fhin = open(file_name2, 'rU')
    data2 = fhin.readlines()
    fhin.close()



    for line in data2[1:]:
        flds = line.split(',')

        sampleID = getSampleId(flds[3], sampleNameID)
        if sampleID in relevantIds:

            if sampleID not in Individual:
                geneDict  = {} # this will become a new value in Individuals
                mutationList =[]
                mutationList.append(flds[12])
                geneDict[flds[0]] = mutationList
                Individual[sampleID] = geneDict # new entry for the primary site has been created.
            else:
                genDict = Individual[sampleID]
                if flds[0] in genDict: # if gene entry is present in that cancer
                    mutList = genDict[flds[0]]
                    mutList.append(flds[12])
                    genDict[flds[0]] = mutList
                    Individual[sampleID] = genDict

                else:
                    # create new entry with gene name as the key and list of mutation types as value
                    mutList = []
                    mutList.append(flds[12])
                    genDict[flds[0]] = mutList

                    Individual[sampleID] = genDict

##    keys = pSite.keys()
##    for each in keys[:10]:
##        print each
##        genDict = pSite[each]
##        genes = genDict.keys()
##        for aGene in genes[:10]:
##            print aGene, genDict[aGene]
    del sampleNameID
    return Individual

def geneByIndividualsCSV(file_name1,file_name2, pickleDump):
    wallStart = time.time()
    cpuStart = time.clock()
    geneSet = Set([])

    fhin = open(file_name1, 'rU') # getting genes from file1
    data = fhin.readlines()
    fhin.close()
    for line in data[1:]:
        flds = line.split(',')
        geneSet.add(flds[0])

    fhin = open(file_name2, 'rU') # getting genes from file2
    data2 = fhin.readlines()
    fhin.close()
    for line in data2[1:]:
        flds = line.split(',')
        geneSet.add(flds[0])

    print '# of genes = ', len(geneSet)
    genes = sorted(list(geneSet))
    del geneSet

##    Individual = geneByIndividuals(file_name1, file_name2)
    Individual = geneByIndividuals(file_name1, file_name2)
    Individuals = sorted(Individual.keys())
    print '# of Individuals = ', len(Individuals)

    fhout = open('geneByIndividuals.csv', 'w')
    firstline = 'Genes,' + ','.join(Individuals) + '\n'
    fhout.write(firstline)

    geneInd = []

    for aGene in genes:
        geneScore = []
        for anInd in Individuals:
            geneDict = Individual[anInd]
            if aGene in geneDict:
                geneScore.append(processGene(geneDict[aGene]))
            else:
                geneScore.append(0)
        geneInd.append(geneScore)

    geneIndArr = np.array(geneInd)

    if pickleDump:
        fhPickle = open('gene_Individuals', 'w')
        pickle.dump(geneInd, fhPickle)
        fhPickle.close()
        joblib.dump(geneIndArr, 'gene_IndividualsArr.pkl')

    for i in range(len(genes)):
        geneSiteStr = [str(n) for n in geneInd[i]]
        outline = genes[i]+ ','+ ','.join(geneSiteStr) + '\n'
        fhout.write(outline)

    fhout.close()
    CPUend = (time.clock() - cpuStart)
    print 'Total elapsed CPU time = ', CPUend

    wallEnd = (time.time() - wallStart)
    print 'Total elapsed wall time = ', wallEnd
    print 'DONE'

##    return Individuals, genes, geneInd, geneIndArr


def sampleMap():

## 'CosmicInsMutExport_v58_150312.csv'
    fhin1 = open('CosmicMutantExport_v58_150312.csv', 'rU')
    fhin1.readline()
    data1 = fhin1.readlines()
    fhin1.close()

    sampleNameID = {}
    for line in data1:
        flds = line.split(',')
        if flds[3] in sampleNameID:
            idList = sampleNameID[flds[3]]
            idList.add(flds[4])
            sampleNameID[flds[3]] = idList

        else:
            idList =Set([])
            idList.add(flds[4])
            sampleNameID[flds[3]] = idList


    return sampleNameID
##    names = sampleNameID.keys()
##    count = 0
##    for each in names:
##        ids = sampleNameID[each]
##        if len(ids)>1:
####            print each, ' has multiple IDS, viz ', ids
##            count+=1
##    print len(names)
##    print count


##    fhin2 = open('CosmicInsMutExport_v58_150312.csv', 'rU')
##    fhin2.readline()
##    data2 = fhin2.readlines()
##    fhin2.close()
##
##    conflicting  =0
##    found = Set([])
##    notFound = Set([])
##    for line in data2:
##        flds = line.split(',')
##        if flds[3] in sampleNameID:
##            found.add(flds[3])
##            ids = sampleNameID[flds[3]]
##            if len(ids)>1:
##                conflicting+=1
##        else:
##            notFound.add(flds[3])
##
##    print '# found',len(found)
##    print '# not found ', len(notFound)
##    print '# conflicting', conflicting



def getSampleId(sampleName, nameIdMap):

    return sorted(nameIdMap[sampleName])[0]

def relevance():
    fhin1 = open('CosmicMutantExport_v58_150312.csv', 'rU')
    fhin1.readline()
    data1 = fhin1.readlines()
    fhin1.close()
    sampleNameID = {}

    for line in data1:
        flds = line.split(',')
        if flds[4] in sampleNameID:
            idList = sampleNameID[flds[4]]
            idList+=1
            sampleNameID[flds[4]] = idList

        else:
            idList = 1
            sampleNameID[flds[4]] = idList

    sampleNameMap = sampleMap() # getting sample name and id mappings from CosmicMutantExport_v58_150312.csv

    fhin2 = open('CosmicInsMutExport_v58_150312.csv', 'rU')
    fhin2.readline()
    data2 = fhin2.readlines()
    fhin2.close()


    for line in data2:
        flds = line.split(',')
        sampleID = getSampleId(flds[3], sampleNameMap)
##        print sampleID
        if sampleID in sampleNameID:
            idList = sampleNameID[sampleID]
            idList+=1
            sampleNameID[sampleID] = idList

        else:
            idList = 1
            sampleNameID[sampleID] = idList



    keys = sampleNameID.keys()

    sampleNames = []

    for each in keys:
        sampleNames.append([each, sampleNameID[each]])

    sortedNames = sorted(sampleNames, key=myFun, reverse=True)

    print 'Total # of sample_Ids = ', len(sortedNames)
    print 'we are using one top 600'
    print sortedNames[:600]
    return sortedNames[:600]
##
##    sortedWeights = sorted(sampleWeights, reverse=True)
##    count = 0
##    for each in sortedNames:
##        if each[1]>20:
####            print each
##            count+= 1
##    print count
##    print len(keys)



def primaryMetLookup():
    fhin = open('CosmicMutantExport_v60_190712.csv', 'rU')
    fhin.readline()
    data1 = fhin.readlines()
    fhin.close()
    sampleOrigin = {}
    for line in data1[1:]:
        flds=  line.split(',')
        if flds[4] not in sampleOrigin: # in case the psite does not exist

            sampleOrigin[flds[4]] = Set([flds[23]])
        else:
            originSet = sampleOrigin[flds[4]]
            originSet.add(flds[23])
            sampleOrigin[flds[4]] = originSet


    keys = sampleOrigin.keys()
    samples = 0
    amb = 0
    for k in keys:
        origin = sampleOrigin[k]
        if len(origin) > 1:
            amb+=1
        else:
            samples+=1
    print 'ambiguous samples = ', amb
    print 'fine samples = ', samples
    print 'total number of ', str(samples+amb)
    joblib.dump(sampleOrigin, 'samples_origin.pkl')


##    fhin = open('CosmicInsMutExport_v58_150312.csv', 'rU')



def myFun(list ):
    return list[:][1]


def timeCalc():
    wallStart = time.time()
    cpuStart = time.clock()
    time.sleep(10)
    CPUend = (time.clock() - cpuStart)
    print 'Total elapsed CPU time = ', CPUend
    wallEnd = (time.time() - wallStart)
    print 'Total elapsed wall time = ', wallEnd

def main():
#CosmicMutantExport_v60_190712.csv
##    geneBySite('CosmicMutantExport_v58_150312.csv')
##    geneBySiteCSV('CosmicMutantExport_v60_190712.csv','CosmicInsMutExport_v60_190712.csv' , True)
    geneByOriginCSV('CosmicMutantExport_v60_190712.csv', False)
##    geneByHistologyCSV('CosmicMutantExport_v58_150312.csv', 'CosmicInsMutExport_v58_150312.csv' , True)

##    geneByIndividualsCSV('CosmicMutantExport_v58_150312.csv', 'CosmicInsMutExport_v58_150312.csv' ,False)
##    geneByIndividualsCSV('mut_small.csv', False)
##    sampleMap()
##    #printme('hello !!')
##    relevance()
##    timeCalc()
##    primaryMetLookup()
if __name__ == '__main__':
    main()