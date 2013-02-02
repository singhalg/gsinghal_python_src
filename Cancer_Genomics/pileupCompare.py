#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     20/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys
from sets import Set


def pileupCompare(file1, file2, outfileName):

    fh1 = open(file1, 'rU')
    fh2 = open(file2, 'rU')

    prim = fh1.readlines()
    met = fh2.readlines()
    fh1.close()
    fh2.close()
    primary = {}
    metastasis = {}
    primarySet = Set([])
    metastasisSet = Set([])
    onlyInPrimSet = Set([])
    onlyInMetSet = Set([])
    depthDict = {}

##
##"
#ref != N
#first those variants whose freq changes
#then those variants wich are absent from one but present in another group
#
##"

    for line in prim:
        flds = line.split('\t')
        depth = flds[3].strip().split(';')[2][3:]
        key = flds[0].strip() + '#' +flds[2].strip()  # the position of the variant is always 1-based coordinate

        depthVal = {}
        depthVal['primary'] = depth
        depthDict[key] = depthVal

        value = {}

        info = flds[3].strip().split(';')
        alt = info[1][4:].split(',')

#        alt = flds[3].strip().split(',')
#        st = flds[4].strip().index('AF=')

        af = info[3].strip()[3:].split(',')
#        af = flds[4][st+3:].strip().split(',')
        if len(alt) != len(af):
            print 'Error !! # ALT ALLELE and AF mismatch'
            print line
            continue
##            sys.exit()
        for i in range(len(alt)):
            value[alt[i]] = float(af[i])
        primary[key] = value


    for line in met:
        flds = line.split('\t')

        depth = flds[3].strip().split(';')[2][3:]
        key = flds[0].strip() + '#' +flds[2].strip()


        if key in depthDict:
            depthVal = depthDict[key]
            depthVal['metastasis'] = depth
            depthDict[key] = depthVal
        else:
            depthVal = {}
            depthVal['metastasis'] = depth
            depthDict[key] = depthVal

        value = {}


        info = flds[3].strip().split(';')
        alt = info[1][4:].split(',')

#        alt = flds[3].strip().split(',')
#        st = flds[4].strip().index('AF=')

        af = info[3].strip()[3:].split(',')
#        af = flds[4][st+3:].strip().split(',')
        if len(alt) != len(af):
            print 'Error !! # ALT ALLELE and AF mismatch'
            print line
##            sys.exit()
            continue
        for i in range(len(alt)):
            value[alt[i]] = float(af[i])
        metastasis[key] = value

##    print primary
##    print metastasis

    primarySet = Set(primary.keys())
    metastasisSet = Set(metastasis.keys())
    onlyInPrimSet = primarySet - metastasisSet
    onlyInMetSet = metastasisSet - primarySet
    commonLoc = primarySet & metastasisSet

    different = {}
    print 'reached point 1'
    for each in commonLoc:
        primVar = primary[each]
        metVar = metastasis[each]
        primAlleles = primVar.keys()
        metAlleles = metVar.keys()

        commonAltAlleles = Set(metAlleles) & Set(primAlleles)                                        # alt_alleles (C,G etc) at a particular location which are present in both prim and metastasis
        for alt_al in commonAltAlleles:

            if primVar[alt_al] != metVar[alt_al]:

                if each in different:
                    val = different[each]
                    val[alt_al] = [primVar[alt_al], metVar[alt_al]]
                else:
                    val = {}
                    val[alt_al] = [primVar[alt_al], metVar[alt_al]]
                    different[each] = val
            else:
                pass

##            else:
##                if each in different:
##                    val = different[each]
##                    val[alt_al] = [primVar[alt_al], 0]
##                else:
##                    val = {}
##                    val[alt_al] = [primVar[alt_al], 0]
##                    different[each] = val


        MetAlleleNotInPrim = Set(metAlleles) - Set(primAlleles)
        PrimAlleleNotInMet =  Set(primAlleles) - Set(metAlleles)

        for alt_all in PrimAlleleNotInMet:
            if each in different:
                val = different[each]
                val[alt_all] = [primVar[alt_all], 0]
            else:
                val = {}
                val[alt_all] = [primVar[alt_all], 0]
                different[each] = val
        for alt_all in MetAlleleNotInPrim:
            if each in different:
                val = different[each]
                val[alt_all] = [0, metVar[alt_all]]
            else:
                val = {}
                val[alt_all] = [0, metVar[alt_all]]
                different[each] = val

    print 'reached point 2'
    for each in onlyInMetSet:
        val = {}
        variants = metastasis[each]
        for abase in variants.keys():
            val[abase] = [0, variants[abase]]
        different[each]  = val
    for each in onlyInPrimSet:
        val = {}
        variants = primary[each]
        for abase in variants.keys():
            val[abase] = [variants[abase], 0]
        different[each]  = val
    print 'reached point 3'

    outfile1 = outfileName + '_variant_diff.csv'
    outfile2 = outfileName + '_variant_diff_cutoff_strict.csv'
    fhout = open(outfile1, 'w')

    fhout2 = open(outfile2, 'w')


    outline = 'chr' + ',' + 'position' + ',' + 'DP_PRIM' +',' +'DP_MET' +',' + 'ALT_ALLELE_1' + ','  + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_2' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_3' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_4' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_5' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_6' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + '\n'
    fhout.write(outline)
    fhout2.write(outline)
    variantLoc = sorted(different.keys())
    for eachLoc in variantLoc:

        chrm, pos = eachLoc.split('#')
        outline = chrm + ',' + pos + ','

        depths = depthDict[eachLoc]
        if 'primary' in depths:

            prim_depth = depths['primary']
        else:
            prim_depth = '0'

        if 'metastasis' in depths:
            met_depth = depths['metastasis']
        else:
            met_depth = '0'

        outline += prim_depth + ',' + met_depth + ','

        outline2 = outline

        variants = different[eachLoc]
        for eachVar in variants.keys():
            outline += eachVar + ','
            VAF = variants[eachVar]

            outline += str(VAF[0]) + ',' + str(VAF[1]) + ','


        for eachVar in variants.keys():

            VAF = variants[eachVar]
            if (VAF[0] > 0.1) or (VAF[1] > 0.1):
                outline2 += eachVar + ',' + str(VAF[0]) + ',' + str(VAF[1]) + ','


        fhout.write(outline[:-1] +'\n')
        if len(outline2.split(',')) > 5:

            fhout2.write(outline2[:-1] + '\n')

    print 'reached point 4'
    fhout.close()
    fhout2.close()











def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    outfile = sys.argv[3]
    # needs input in bed format, these bed files have those variants which fall in target capture boundaries.
    pileupCompare(file1, file2, outfile)


if __name__ == '__main__':
    main()
