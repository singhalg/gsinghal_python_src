#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     13/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------
import sys
from sets import Set



def read_genes(filename):
    fhin = open(filename, 'r')
    data = fhin.readlines()
    fhin.close()
    genes = []
    for each in data[1:]:
        genes.append(each.split(',')[3].strip())

##    print genes, '   :   ', len(genes)

    geneSet = Set(genes)

##    print len(geneSet)

    print sorted(genes)

    return genes


def readExpression(genesList, geneProbeFile, expressionMatrix):
    genes = read_genes(genesList)
    geneSet = Set(genes)
    geneProbe = {}

    fhin = open(geneProbeFile, 'r')
    data  = fhin.readlines()
    fhin.close()
    probes = []

    for line in data:
        gn = line.split(',')[1].strip()
        if gn in geneSet:
            if gn not in geneProbe:
                probes.append(line.split(',')[0].strip())
                val  = [line.split(',')[0].strip()]
                geneProbe[gn] = val
            else:
                val = geneProbe[gn]
                val.append(line.split(',')[0].strip())
                probes.append(line.split(',')[0].strip())
                geneProbe[gn] = val

    probeSet = Set(probes)
    print geneProbe
    print len(sorted(probes))
    print len(probeSet)

    expFile = open(expressionMatrix, 'rU')
    expData = expFile.readlines()
    expFile.close()
    probesAvail = Set([])
    probeExp = {}

    for each in expData[1:]:
        probe = each.split(',')[0].strip()
        if probe in probeSet:
            probesAvail.add(probe)
            probeExp[probe] = each

    unAvail = probeSet - probesAvail
##    print 'unavailable = ', unAvail

    geneExpression = {}

    for agene in geneProbe.keys():
        gene_probes = geneProbe[agene]
        expVal = 0
        for aprobe in gene_probes:
            expVal+=countExp(probeExp[aprobe])
        finalVal = ((float(expVal)/len(gene_probes))/75.00)*100
        geneExpression[agene] = finalVal

    print geneExpression

    return geneExpression



def readExpressionAllGenes(geneProbeFile, expressionMatrix):
##    genes = read_genes(genesList)
##    geneSet = Set(genes)
    geneProbe = {}

    fhin = open(geneProbeFile, 'r')
    data  = fhin.readlines()
    fhin.close()
    probes = []

    for line in data:
        gn = line.split(',')[1].strip()

        if gn not in geneProbe:
            probes.append(line.split(',')[0].strip())
            val  = [line.split(',')[0].strip()]
            geneProbe[gn] = val
        else:
            val = geneProbe[gn]
            val.append(line.split(',')[0].strip())
            probes.append(line.split(',')[0].strip())
            geneProbe[gn] = val

    probeSet = Set(probes)
    print '# of genes = ', len(geneProbe.keys())
    print '# of probes = ', len(sorted(probes))
    print '# of unique probes = ', len(probeSet)

    expFile = open(expressionMatrix, 'rU')
    expData = expFile.readlines()
    expFile.close()
    probesAvail = Set([])
    probeExp = {}

    for each in expData[1:]:
        probe = each.split(',')[0].strip() # this is the probe found in exp sheet
        if probe in probeSet:
            probesAvail.add(probe)   # These are the probes for which expression data is available.
            probeExp[probe] = each

    unAvail = probeSet - probesAvail
    print 'unavailable = ', len(unAvail)

    geneExpression = {}

    for agene in geneProbe.keys():
        gene_probes = geneProbe[agene]
        expVal = 0
        for aprobe in gene_probes:
            if aprobe in probesAvail:
                expVal+=countExp(probeExp[aprobe])
        finalVal = ((float(expVal)/len(gene_probes))/75.00)*100
        geneExpression[agene] = finalVal

##    print geneExpression

    return geneExpression



def expScore(expressionMatrix):
    expFile = open(expressionMatrix, 'rU')
    expData = expFile.readlines()
    expFile.close()
    for each in expData[1:7]:
        print countExp(each)




def countExp(aline):
    flds = aline.split(',')
    expScore = 0
    for each in flds[1:]:
        if each =='P':
            expScore+=1
        elif each =='M':
            expScore+=0.5
        else:
            expScore+=0
    return expScore



##    print len(geneNames), ' = total genes ##################################################'
####    print geneNames
##    notFound = geneSet - geneNames
##    print  len(notFound),'=====not found=======' , notFound
##    found = geneNames - geneSet
##    print len(found),'============' ##,  found


##
##    print geneNames
##
##    for agene in geneSet:
##        expVal

##    for each in genes

def writeExpValsAllGenes():


    expressionData = readExpressionAllGenes('AffyU133Plus2_probe_geneName.csv','LungExpChip.csv')

##    outfileName = filename[:-4] + '_expScore.csv'
    fhout = open('All_genes_LungCancer_expScore.csv', 'w')
##    fhout = open(outfileName, 'w')

##    fhin = open(filename, 'r')
##    data = fhin.readlines()
##    fhin.close()
##    genesData = []

    outline = 'Gene_Name,Expression_Score' + '\n'
    fhout.write(outline)

    for geneName in expressionData.keys():

##    for
##    for each in data[1:]:
##        geneName = each.split(',')[3].strip()
##
##        if geneName in expressionData:
        expVal = expressionData[geneName]
        outline = geneName + ',' + str(expVal) + '\n'
##        else:
##            outline = each.strip() + ',' + '??' + '\n'
        fhout.write(outline)

    fhout.close()


def writeExpVals(filename):

    expressionData = readExpression('Extreme_variants_genes.csv', 'AffyU133Plus2_probe_geneName.csv','LungExpChip.csv')


    outfileName = filename[:-4] + '_expScore.csv'
    fhout = open('All_genes_LungCancer_expScore.csv', 'w')

    fhin = open(filename, 'r')
    data = fhin.readlines()
    fhin.close()
    genesData = []

    outline = 'Gene,Expression Score' + '\n'
    fhout.write(outline)

    for each in data[1:]:
        geneName = each.split(',')[3].strip()

        if geneName in expressionData:
            expVal = expressionData[geneName]
            outline = each.strip() + ',' + str(expVal) + '\n'
        else:
            outline = each.strip() + ',' + '??' + '\n'
        fhout.write(outline)

    fhout.close()


def writeCOSMICrecurrence(filename, Cosmic_primSite, Cosmic_origin ):

    fhin = open(filename, 'rU')
    data = fhin.readlines()
    fhin.close()
    genesData = []

    fhinCosmic = open(Cosmic_primSite, 'rU')
    cosmic_primSite = fhinCosmic.readlines()
    fhinCosmic.close()
    cosmic_psite = {}

    for line in cosmic_primSite[1:]:
        flds = line.split(',')
        gene = flds[0].strip()
        geneScore = 0
        for eachScore in flds[1:]:
            geneScore+= int(eachScore.strip())
        lungScore =int(flds[18].strip())
        val = [lungScore, (geneScore-lungScore)]
        cosmic_psite[gene] = val


    fhinCosmicOrigin = open(Cosmic_origin, 'rU')
    cosmic_origin_data = fhinCosmicOrigin.readlines()
    fhinCosmicOrigin.close()
    cosmic_originSite = {}

    for line in cosmic_origin_data[1:]:
        flds = line.split(',')
        gene = flds[0].strip()
        metScore = int(flds[4].strip())
        primScore =int(flds[5].strip())
        val = [primScore, metScore]
        cosmic_originSite[gene] = val



    outfileName = filename[:-4] + '_COSMIC.csv'
    fhout = open(outfileName, 'w')

    outline = data[0].strip() + ',Lung,All_Other_Site,Primary,Metastasis' + '\n'
    fhout.write(outline)

    for each in data[1:]:
        geneName = each.split(',')[3].strip()

        if geneName in cosmic_psite:
            Val = cosmic_psite[geneName]
            outline = each.strip() + ',' + str(Val[0]) + ',' + str(Val[1]) +','
        else:
            outline = each.strip() + ',' + '??' +',' + '??' + ','

        if geneName in cosmic_originSite:
            Val = cosmic_originSite[geneName]
            outline +=  str(Val[0]) + ',' + str(Val[1]) + '\n'
        else:
            outline += '??' +',' + '??' + '\n'



        fhout.write(outline)

    fhout.close()

def main():
##    read_genes('missense_genes.csv')
##    readExpression('Extreme_variants_genes.csv', 'AffyU133Plus2_probe_geneName.csv','LungExpChip.csv')
##    writeExpVals('Extreme_variants_genes.csv')

##    writeCOSMICrecurrence('Extreme_variants_genes_expScore.csv', 'geneByPrimSite_v60.csv', 'geneByOriginSite_v60.csv' )

##    expScore('LungExpChip.csv')
    writeExpValsAllGenes() # this method writes a csv file containing expression values of all genes. Expression values are derived from LungExpChip.csv (Affy U133Plus 2 platform, 75 primary tumors)

if __name__ == '__main__':
    main()
