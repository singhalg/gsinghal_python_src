#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     04/09/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------


from sets import Set
import pickle
import sys

def readEVSvcf(fileName):
    fh = open(fileName, 'rU')
    data = fh.readlines()
    fh.close()
    variantsVCF = {}
    varSet = Set([])

    for line in data:
        if line[0] != '#':
            processVCF(line, variantsVCF)

        else:
            pass

    variantPos = sorted(variantsVCF.keys())
    for apos in variantPos:
        info = variantsVCF[apos]
        maf = float(info['MAF'][2])
        dp = int(info['DP'][0])
        if dp >= 100:
            if maf >= 5.0:

                varSet.add(apos)
    pickleOut = open('EVS_all_variants_dict.pkl', 'w')
    pickle.dump(variantsVCF, pickleOut)
##    print '# of all variants in EVS file = ', len(variantPos)
##    print '# of common variants in EVS file = ', len(varSet)
    return varSet, variantPos



def processVCF(line, variantDict):
    flds = line.split('\t')
    key = flds[0].strip() + '#' + flds[1].strip()
    value = {}
    value['REF'] = flds[3].strip()
    value['ALT'] = flds[4].strip()
    for each in flds[7].strip().split(';'):
        info = each.partition('=')
        infoVal = info[2].split(',')
        value[info[0]] = infoVal
    variantDict[key] = value


def compareInternalExternal(internal, external):
    commonExternal, allExternal = readEVSvcf(external)

    print '# of variants in external control (EVS) = ', len(allExternal)
    print '# of COMMON variants in external control (EVS) = ', len(commonExternal)

    fhin = open('snpInExon_AGILENT_count', 'rU')
    internalVariants = fhin.readlines()
    fhin.close()

    internalVariantSet = Set([])


    for line in internalVariants:
        flds = line.split('\t')
        key = flds[0].strip()[3:] + '#' +flds[2].strip()
        internalVariantSet.add(key)
    print '# of variants in internalVariantSet = ', len(internalVariantSet)
##    print list(internalVariantSet)[:100]

    print '# of variants common between internal control set and external (common) control set =', len(internalVariantSet & commonExternal)

    print '# of variants common between internal control set and all external control set =', len(internalVariantSet & Set(allExternal))

def main():
    compareInternalExternal('snpInExon_AGILENT_count', 'ESP6500.all_chr.snps.vcf')

if __name__ == '__main__':
    main()
