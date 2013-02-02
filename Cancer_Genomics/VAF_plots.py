#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav
#
# Created:     26/01/2013
# Copyright:   (c) Gaurav 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pickle, sys, math
from sets import Set



def pickleCompare(prim, met, PT_name):

    prim_pickle = prim[:-4] + '_SnpSift_rare.pkl'
    prim_data = pickle.load(open(prim_pickle, 'rU'))

    met_pickle = met[:-4] + '_SnpSift_rare.pkl'
    met_data = pickle.load(open(met_pickle, 'rU'))

    allVariants  = Set(prim_data.keys()).union(Set(met_data.keys()))

    fhoutFileName = PT_name + '_rare.csv'
    fhout = open(fhoutFileName, 'w')
    outline = 'chr' + ',' + 'position' + ',' + 'DP_PRIM' +',' + 'PVAL_PRIM' + ',' +'DP_MET'+','+ 'PVAL_MET' +',' + 'ALT_ALLELE' + ','  + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',EFFECT_IMPACT' '\n'  ##+ 'ALT_ALLELE_2' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_3' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_4' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_5' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + 'ALT_ALLELE_6' + ',' + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',' + '\n'
    fhout.write(outline)


    for eachVariant in allVariants:
        chrom = eachVariant.split('#')[0]
        position = eachVariant.split('#')[1]
        if eachVariant in prim_data:
            vaf_prim = prim_data[eachVariant]['AF'][0]
            try:
                p_val_prim = str((math.log10(float(prim_data[eachVariant]['PVAL'][0]))) *-1)
            except:
                p_val_prim = '0'
            dp_prim = prim_data[eachVariant]['DP'][0]
            ALT_AL = prim_data[eachVariant]['ALT'][0]
            impact =list(prim_data[eachVariant]['Effect_Impact'])[0]
        else:
            vaf_prim = '0'
            p_val_prim = '0'
            dp_prim = '0'

        if eachVariant in met_data:
            vaf_met = met_data[eachVariant]['AF'][0]
            try:
                p_val_met = str((math.log10(float(met_data[eachVariant]['PVAL'][0]))) *-1)
            except:
                p_val_met = '0'
            dp_met= met_data[eachVariant]['DP'][0]
            ALT_AL = met_data[eachVariant]['ALT'][0]
            impact =list(met_data[eachVariant]['Effect_Impact'])[0]
        else:
            vaf_met= '0'
            p_val_met = '0'
            dp_met = '0'


        if impact == 'MODIFIER':
            effect_impact = '0'
        elif impact == 'MODERATE':
            effect_impact = '2'
        elif impact == 'LOW':
            effect_impact = '1'
        elif impact =='HIGH':
            effect_impact = '3'
#outline = 'chr' + ',' + 'position' + ',' + 'DP_PRIM' +',' + 'PVAL_PRIM' + ',' +'DP_MET'+','+ 'PVAL_MET' +',' + 'ALT_ALLELE' + ','  + 'VAR_FREQ_PRIM' + ',' + 'VAR_FREQ_MET' + ',EFFECT_IMPACT' '\n'
        outline = chrom + ',' + position + ',' + dp_prim + ',' +p_val_prim + ',' + dp_met + ',' +p_val_met + ',' +ALT_AL + ',' + vaf_prim + ',' + vaf_met + ',' +effect_impact + '\n'
        fhout.write(outline)
    fhout.close()

def VAFplots():


    pickleCompare('PT_1_lung_VarScan_clean_snpEff.vcf', 'PT_1_brain_VarScan_clean_snpEff.vcf', 'PT_1_VarScan')
    pickleCompare('PT_2_lung_VarScan_clean_snpEff.vcf', 'PT_2_brain_VarScan_clean_snpEff.vcf', 'PT_2_VarScan')
    pickleCompare('PT_3_lung_VarScan_clean_snpEff.vcf', 'PT_3_brain_VarScan_clean_snpEff.vcf', 'PT_3_VarScan')
    pickleCompare('PT_6_lung_VarScan_clean_snpEff.vcf', 'PT_6_brain_VarScan_clean_snpEff.vcf', 'PT_6_VarScan')
    pickleCompare('PT_9_lung_VarScan_clean_snpEff.vcf', 'PT_9_brain_VarScan_clean_snpEff.vcf', 'PT_9_VarScan')
    pickleCompare('PT_10_lung_VarScan_clean_snpEff.vcf', 'PT_10_brain_VarScan_clean_snpEff.vcf', 'PT_10_VarScan')
    pickleCompare('PT_11_lung_VarScan_clean_snpEff.vcf', 'PT_11_brain_VarScan_clean_snpEff.vcf', 'PT_11_VarScan')
    pickleCompare('PT_12_lung_VarScan_clean_snpEff.vcf', 'PT_12_brain_VarScan_clean_snpEff.vcf', 'PT_12_VarScan')
    pickleCompare('PT_13_lung_VarScan_clean_snpEff.vcf', 'PT_13_brain_VarScan_clean_snpEff.vcf', 'PT_13_VarScan')

def main():
    VAFplots()

if __name__ == '__main__':
    main()
