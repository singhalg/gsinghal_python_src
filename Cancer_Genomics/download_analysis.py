#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     17/10/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------


import os



def download_analysis():





    loc1 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/AGACTGA/'
    loc2 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/ATCGAGC/'
    loc3 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/ATGACAG/'
    loc4 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/CACCTCC/'
    loc5 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/CTTGGAA/'
    loc6 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/GCTTAGA/'
    loc7  ='http://cgs.wustl.edu/solexa/Watson_0658_67/TACTCTA/'
    loc8 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/TGAGGTT/'

    locations = [loc1, loc2, loc3, loc4, loc5, loc6, loc7, loc8]


    file1 = 'all.stats'
    file2 = 'all_sorted_rmdup_sorted.bam'
    file3 = 'exons.stats'
    file4 = 'rawSNP.txt'
    file5 = 'snpInExon.txt'
    file6 = 'snpInExon.vcf'
    file7 = 'snps_indels.xls'


    files = [ file1, file2, file3, file4,file5,file6,file7]

    for aloc in locations:
        path = aloc[-8:-1]+"/"
        os.chdir(path)
        for afile in files:
            job = 'nohup wget '+ aloc+afile + ' &>  wget_analysis.txt & '
            os.system(job)
        os.chdir('/scratch/gsinghal/MWatson/GTAC_Analysis/')




def main():
    download_analysis()
#    download_data2()


if __name__=='__main__':
    main()

