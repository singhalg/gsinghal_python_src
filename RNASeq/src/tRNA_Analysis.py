'''
Created on Mar 18, 2011

@author: Gaurav
'''



import sys, pickle, os


import numpy.numarray as na

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties



'''
This script goes into the respective folders and open the tRNA files and reads the file contents 
and gets the line count of each file.
'''

def tRNA():

# these are the paths where the repective tRNA read files are present. 
    hg19 = '/net/artemis/mnt/work1/projects/gsinghalWork/RepeatMasker/RM19Class/TRNA/'
    ACAT = '/net/artemis/mnt/work1/projects/gsinghalWork/Keith/ACAT/RepeatClass/TRNA/'
    AGTT = '/net/artemis/mnt/work1/projects/gsinghalWork/Keith/AGTT/RepeatClass/TRNA/'
    ATCT = '/net/artemis/mnt/work1/projects/gsinghalWork/Keith/ATCT/RepeatClass/TRNA/'
    CAGT = '/net/artemis/mnt/work1/projects/gsinghalWork/Keith/CAGT/RepeatClass/TRNA/'
    GACT = '/net/artemis/mnt/work1/projects/gsinghalWork/Keith/GACT/RepeatClass/TRNA/'
    TCAT = '/net/artemis/mnt/work1/projects/gsinghalWork/Keith/TCAT/RepeatClass/TRNA/'




    hg19tRNA = []
    ACATtRNA = []
    AGTTtRNA = []
    ATCTtRNA = []
    CAGTtRNA = []
    GACTtRNA = []
    TCATtRNA = []
    
    


    
    hg19Dir = os.listdir(hg19)  # this would list the names of all the individual tRNA files in this folder.
    for each in hg19Dir:
        hg19tRNA.append(each)

    ACATDir = os.listdir(ACAT)
    for each in ACATDir:
        ACATtRNA.append(each)
    
    AGTTDir = os.listdir(AGTT)
    for each in AGTTDir:
        AGTTtRNA.append(each)
        
    ATCTDir = os.listdir(ATCT)
    for each in ATCTDir:
        ATCTtRNA.append(each)
        
    CAGTDir = os.listdir(CAGT)
    for each in CAGTDir:
        CAGTtRNA.append(each)
    
    GACTDir = os.listdir(GACT)
    for each in GACTDir:
        GACTtRNA.append(each)
        
    TCATDir = os.listdir(TCAT)
    for each in TCATDir:
        TCATtRNA.append(each)



    hg19tRNACount = [] 
    ACATtRNACount = [] 
    AGTTtRNACount = []
    ATCTtRNACount = []
    CAGTtRNACount = []
    GACTtRNACount = []
    TCATtRNACount = []
    
#    Sample                                                            Total Reads    Aligned reads
#Jia475.s_1_sequence.ACAT.fastq                  compute-00-02          15511090       1531721
#Jia475.s_1_sequence.AGTT.fastq                  compute-00-03           8893756       3782255
#Jia475.s_1_sequence.ATCT.fastq                   compute-00-04          7646993       3492888
#Jia475.s_1_sequence.CAGT.fastq                   compute-00-05          6929395        777614
#Jia475.s_1_sequence.GACT.fastq                   compute-00-06         28490744        782489
#Jia475.s_1_sequence.TCAT.fastq                   compute-00-07         19030312       6902208


# for each tRNA, we would count the number of lines in its respective file. 
# eg, line count of tRNA-Ala-GCA is 40. It then divides this number by the total number of tRNA entries in this sample / 1000
# which is hg19. So, hg19 has 2001 tRNA entries, so we would divide 40 by 2.001



    for tRNA in hg19tRNA:
        path = hg19 + tRNA
        hg19input = open(path, 'rU')
        alignedReads = hg19input.readlines()
        hg19tRNACount.append(len(alignedReads)/2.001)
        
# here we are dividing line count in particular tRNA file in ACAT by normalized total tRNA read count (/1000)
# so this would mean tRNA reads of a particular codon per thousand normalized total tRNA reads.
        try:
            ACATinput = open(ACAT+tRNA, 'rU')
            ACATar = ACATinput.readlines()
            ACATtRNACount.append(len(ACATar)/0.989)
        except:
            ACATtRNACount.append(0)
        
        try:
            AGTTinput = open(AGTT+tRNA, 'rU')
            AGTTar = AGTTinput.readlines()
            AGTTtRNACount.append(len(AGTTar)/8.853)
        except:
            AGTTtRNACount.append(0)
        
        try:
            ATCTinput = open(ATCT+tRNA, 'rU')
            ATCTar = ATCTinput.readlines()
            ATCTtRNACount.append(len(ATCTar)/12.04)
        except:
            ATCTtRNACount.append(0)
        
        try:
            CAGTinput = open(CAGT+tRNA, 'rU')
            CAGTar = CAGTinput.readlines()
            CAGTtRNACount.append(len(CAGTar)/1.02)
        except:
            CAGTtRNACount.append(0)
        
        try:
            GACTinput = open(GACT+tRNA, 'rU')
            GACTar = GACTinput.readlines()
            GACTtRNACount.append(len(GACTar)/ 1.1)
        except:
            GACTtRNACount.append(0)
        try:
            TCATinput = open(TCAT+tRNA, 'rU')
            TCATar = TCATinput.readlines()
            TCATtRNACount.append(len(TCATar)/ 9.67)
        except:
            TCATtRNACount.append(0)
            
            
    
    # finally, everything is saved into a pickle object. This pickle object is then copied locally to the computer
    # and then imported into eclipse, then unpickled.  
    
    
    data =  [hg19tRNACount, ACATtRNACount, AGTTtRNACount, ATCTtRNACount, CAGTtRNACount, GACTtRNACount, TCATtRNACount ]
    
    dataSum = [sum(hg19tRNACount), sum(ACATtRNACount), sum(AGTTtRNACount), sum(ATCTtRNACount), sum(CAGTtRNACount),
            sum(GACTtRNACount), sum(TCATtRNACount) ]
    
    
    legends = ['hg19', 'ACAT', 'AGTT', 'ATCT', 'CAGT', 'GACT', 'TCAT']
    barData = [data, dataSum, legends, hg19tRNA]
    
    pickled = open('tRNA_barData', 'w')
    
    pickle.dump(barData, pickled)
    
    
        
        
    

'''

This method was used to create the plot of normalized tRNA reads in each sample. 
Normalized tRNA reads  = [ # reads that map to tRNA / total # reads that map to repeats ] 
This method is run locally on the laptop, since it generates all the plots and uses matplotlib (matplotlib is not available on server).
'''
def barchart():


#    pickled = open('pickleName', 'rU')
#    
#    barData = pickle.load(pickled)
#    
#    data = barData[0]
#    labels = barData[1]

    labels = ["hg19", "ACAT", "AGTT", "ATCT", "CAGT", "GACT", "TCAT"]
    data =   [2001,      989,   8853,  12040,  1028,    1101,  9672]   # total number of reads that align to tRNA / million reads that map to repeats
    
#    Sample                                                            Total Reads    Aligned reads
#Jia475.s_1_sequence.ACAT.fastq                  compute-00-02          15511090       1531721
#Jia475.s_1_sequence.AGTT.fastq                  compute-00-03           8893756       3782255
#Jia475.s_1_sequence.ATCT.fastq                   compute-00-04          7646993       3492888
#Jia475.s_1_sequence.CAGT.fastq                   compute-00-05          6929395        777614
#Jia475.s_1_sequence.GACT.fastq                   compute-00-06         28490744        782489
#Jia475.s_1_sequence.TCAT.fastq                   compute-00-07         19030312       6902208

    xlocations = na.array(range(len(data)))+0.5
    width = 0.6
    bar(xlocations, data, width=width)
#    yticks(range(0, 5000))
    xticks(xlocations+ width/2, labels)
    xlim(0, xlocations[-1]+width*2)
    title("Reads that align to tRNA (pseudo)genes (per million reads mapped to repeats)")
    gca().get_xaxis().tick_bottom()
    gca().get_yaxis().tick_left()

    show()
    savefig('tRNA_reads.png')
   


'''

This method was used to create the plot of comparison of total reads, reads aligned to repeats and reads aligned to tRNA in each sample. 
This method is run locally on the laptop, since it generates all the plots and uses matplotlib (matplotlib is not available on server).
'''
def multiBarChart():
    rcParams['legend.fontsize'] = 10
    labels = ["hg19", "ACAT", "AGTT", "ATCT", "CAGT", "GACT", "TCAT"]
    ReadsAlignedtotRNA =   (2001, 1513, 33466, 42021, 792, 859, 66740)
    AlignedReads = (2001,1531, 3782, 3492, 777, 782, 6902) # X 1000  [reads which got aligned to repeats]
    TotalReads = (2001, 15511, 8893, 7646, 6929, 28490, 19030) # X 1000
    
#    N = 5
#    menMeans = (20, 35, 30, 35, 27)
#    menStd =   (2, 3, 4, 1, 2)

    N = 7
    ind = np.arange(N)  # the x locations for the groups
    print ind
    width = 0.2       # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)

#    rects1 = ax.bar(ind, menMeans, width, color='r')
    rects1 = ax.bar(ind, TotalReads, width, color='g')

#    womenMeans = (25, 32, 34, 20, 25)

#    womenStd =   (3, 5, 2, 3, 3)
#    rects2 = ax.bar(ind+width, womenMeans, width, color='b')
    rects2 = ax.bar(ind+width, AlignedReads, width, color='b')
    
    rects3 = ax.bar(ind+width+width, ReadsAlignedtotRNA, width, color='r')

# add some
    ax.set_ylabel('# reads')
    ax.set_title('Alignment of reads to Repeats')
    ax.set_xticks(ind+width)
#    ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5') )
    ax.set_xticklabels( ("hg19", "ACAT", "AGTT", "ATCT", "CAGT", "GACT", "TCAT") )
#    ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )

    ax.legend( (rects1[0], rects2[0], rects3[0]), ('Total_Reads (X1000)', 'Reads Aligned to Repeats (X1000)', 'Reads aligned to tRNA genes') , loc=2)

    plt.grid(True)
    plt.show()






'''
This method is run locally on the laptop, since it generates all the plots and uses matplotlib (matplotlib is not available on server).
This method loads the pickle, and then calls the barchartTRNA() method that generates a simple Bar Graph for a particular sample. It plots the 
number of reads that got aligned to a particular tRNA-codon (per thousand normalized reads that aligned to all tRNAs)  in that sample. 
'''  
def tRNA_plot(pickleFile):
    
    
    
    pickled = open(pickleFile, 'rU')
    
    barData = pickle.load(pickled)
    data = barData[0][6]   # TBC  barData[0][1]; barData[0][2]   etc
    labels = barData[3]  # tRNA-Ser-ATG, tRNA-Thr-CAG etc
    clipLabels = []
    for each in labels:
        clipLabels.append(each[5:])
        
    legend = barData[2][6] # hg19, ACAT etc
    
    barchartTRNA(data, clipLabels, legend)
    
    
    
'''
This method generates a simple Bar Graph for a particular sample. It plots the 
number of reads that got aligned to a particular tRNA-codon (per thousand normalized reads that aligned to all tRNAs)  
in that sample. 
'''
def barchartTRNA(data, labels, legend):
    rcParams['figure.figsize'] = 30, 8
    rcParams['xtick.labelsize'] = 'x-small'
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xlocations = na.array(range(len(data)))+0.5
    width = 0.6
    plt.bar(xlocations, data, width=width)
#    yticks(range(0, 5000))
    plt.xticks(xlocations+ width/2, labels, rotation='vertical')
    plt.xlim(0, xlocations[-1]+width*2)
    plt.title(legend)
    plt.gca().get_xaxis().tick_bottom()
    
    plt.gca().get_yaxis().tick_left()

    plt.show()
    plt.savefig('tRNA_reads'+ legend + '.png')



def main():
#    tRNA()
#    file = sys.argv[1]
#    
#    tRNA(file, expanse, strand)
#    barchart()
#    multiBarChart()
    pickleFile = sys.argv[1]
    tRNA_plot(pickleFile)

   
if __name__ == '__main__':
    main()