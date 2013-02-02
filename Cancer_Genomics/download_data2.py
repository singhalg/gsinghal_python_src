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



def download_data1():

    jobs = []

    job1 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/AGACTGA/run_658_s_6_1_withindex_sequence.txt_AGACTGA.fq.gz'
    job2 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/AGACTGA/run_658_s_6_3_withindex_sequence.txt_AGACTGA.fq.gz'
    job3 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/AGACTGA/run_658_s_7_1_withindex_sequence.txt_AGACTGA.fq.gz'
    job4 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/AGACTGA/run_658_s_7_3_withindex_sequence.txt_AGACTGA.fq.gz'

    job5 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/ATCGAGC/run_658_s_6_1_withindex_sequence.txt_ATCGAGC.fq.gz'
    job6 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/ATCGAGC/run_658_s_6_3_withindex_sequence.txt_ATCGAGC.fq.gz'
    job7 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/ATCGAGC/run_658_s_7_1_withindex_sequence.txt_ATCGAGC.fq.gz'
    job8 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/ATCGAGC/run_658_s_7_3_withindex_sequence.txt_ATCGAGC.fq.gz'

    job9 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/ATGACAG/run_658_s_6_1_withindex_sequence.txt_ATGACAG.fq.gz'
    job10 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/ATGACAG/run_658_s_6_3_withindex_sequence.txt_ATGACAG.fq.gz'
    job11 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/ATGACAG/run_658_s_7_1_withindex_sequence.txt_ATGACAG.fq.gz'
    job12 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/ATGACAG/run_658_s_7_3_withindex_sequence.txt_ATGACAG.fq.gz'

    job13 =  'http://cgs.wustl.edu/solexa/Watson_0658_67/CACCTCC/run_658_s_6_1_withindex_sequence.txt_CACCTCC.fq.gz'
    job14 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/CACCTCC/run_658_s_6_3_withindex_sequence.txt_CACCTCC.fq.gz'
    job15 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/CACCTCC/run_658_s_7_1_withindex_sequence.txt_CACCTCC.fq.gz'
    job16 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/CACCTCC/run_658_s_7_3_withindex_sequence.txt_CACCTCC.fq.gz'


    jobs.append(job1)
    jobs.append(job2)
    jobs.append(job3)
    jobs.append(job4)
    jobs.append(job5)
    jobs.append(job6)
    jobs.append(job7)
    jobs.append(job8)
    jobs.append(job9)
    jobs.append(job10)
    jobs.append(job11)
    jobs.append(job12)
    jobs.append(job13)
    jobs.append(job14)
    jobs.append(job15)
    jobs.append(job16)

    for ajob in jobs:
        cmd = 'nohup wget ' + ajob + '  &>  wget'+      ajob[-13:-6] +   '.txt & '
        os.system(cmd)






def download_data2():
    jobs = []

    job17 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/CTTGGAA/run_658_s_6_1_withindex_sequence.txt_CTTGGAA.fq.gz'
    job18 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/CTTGGAA/run_658_s_6_3_withindex_sequence.txt_CTTGGAA.fq.gz'
    job19 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/CTTGGAA/run_658_s_7_1_withindex_sequence.txt_CTTGGAA.fq.gz'
    job20 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/CTTGGAA/run_658_s_7_3_withindex_sequence.txt_CTTGGAA.fq.gz'

    job21 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/GCTTAGA/run_658_s_6_1_withindex_sequence.txt_GCTTAGA.fq.gz'
    job22 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/GCTTAGA/run_658_s_6_3_withindex_sequence.txt_GCTTAGA.fq.gz'
    job23 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/GCTTAGA/run_658_s_7_1_withindex_sequence.txt_GCTTAGA.fq.gz'
    job24 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/GCTTAGA/run_658_s_7_3_withindex_sequence.txt_GCTTAGA.fq.gz'


    job25 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/TACTCTA/run_658_s_6_1_withindex_sequence.txt_TACTCTA.fq.gz'
    job26 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/TACTCTA/run_658_s_6_3_withindex_sequence.txt_TACTCTA.fq.gz'
    job27 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/TACTCTA/run_658_s_7_1_withindex_sequence.txt_TACTCTA.fq.gz'
    job28 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/TACTCTA/run_658_s_7_3_withindex_sequence.txt_TACTCTA.fq.gz'

    job29 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/TGAGGTT/run_658_s_6_1_withindex_sequence.txt_TGAGGTT.fq.gz'
    job30 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/TGAGGTT/run_658_s_6_3_withindex_sequence.txt_TGAGGTT.fq.gz'
    job31 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/TGAGGTT/run_658_s_7_1_withindex_sequence.txt_TGAGGTT.fq.gz'
    job32 = 'http://cgs.wustl.edu/solexa/Watson_0658_67/TGAGGTT/run_658_s_7_3_withindex_sequence.txt_TGAGGTT.fq.gz'




    jobs.append(job17)
    jobs.append(job18)
    jobs.append(job19)
    jobs.append(job20)
    jobs.append(job21)
    jobs.append(job22)
    jobs.append(job23)
    jobs.append(job24)
    jobs.append(job25)
    jobs.append(job26)
    jobs.append(job27)
    jobs.append(job28)
    jobs.append(job29)
    jobs.append(job30)
    jobs.append(job31)
    jobs.append(job32)


    for ajob in jobs:
        cmd = 'nohup wget ' + ajob + '  &>  wget'+      ajob[-13:-6] +   '.txt & '
        os.system(cmd)



def main():
#    download_data1()
    download_data2()


if __name__=='__main__':
    main()

