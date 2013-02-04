'''
Created on Jul 24, 2010

@author: Gaurav
'''

import matplotlib.pyplot as plt 
import sys
from pylab import *   #required for legend
from matplotlib.font_manager import FontProperties


def multiGraph5SuExSp(readFile1, readFile2, readFile3, readFile4, save ):
    
    read1Data = open(readFile1, 'rU') # normal
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score  
    rep1Fam = read1Data.readline().rstrip()
    rC1 = read1Data.readline().split()   # this line contains 'total read count' + '/t' + '# of unmatched reads'
    read1Count = float(rC1[0])
    ind = rep1Fam.find('_') 
    rep1Family = rep1Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element :  ', rep1Family
    read1Con = []
    for line in read1Data:
        list = line.split()
        read1Con.append(int(list[2]))    # list[2] contains the scores.
        
        
    read2Data = open(readFile2, 'rU')  #cancer
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score
    rep2Fam = read2Data.readline().rstrip()
    rC2 = read2Data.readline().split()
    read2Count = float(rC2[0])
    ind = rep2Fam.find('_') 
    rep2Family = rep2Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element =  ', rep2Family
    read2Con = []
    for line in read2Data:
        list = line.split()
        read2Con.append(int(list[2]))    # list[2] contains the scores.
    print 'readCount1 = ', read1Count
    print 'readCount2 = ', read2Count
    print 'readCount1/readCount2 = ', read1Count/read2Count
    
    normRead1Con = []
    normRead2Con = []
    
    if read1Count>read2Count:
        normRead2Con = read2Con
        for base in read1Con:
            normRead1Con.append(int(float(base)*(read2Count/read1Count)))
    else:
        normRead1Con = read1Con
        for base in read2Con:
            normRead2Con.append(int(float(base)*(read1Count/read2Count)))

    read3Data = open(readFile3, 'rU') # normal
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score  
    rep3Fam = read3Data.readline().rstrip()
    rC3 = read3Data.readline().split()   # this line contains 'total read count' + '/t' + '# of unmatched reads'
    read3Count = float(rC3[0])
    ind = rep3Fam.find('_') 
    rep3Family = rep3Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element :  ', rep3Family
    read3Con = []
    for line in read3Data:
        list = line.split()
        read3Con.append(int(list[2]))    # list[2] contains the scores.
        
        
    read4Data = open(readFile4, 'rU')  #cancer
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score
    rep4Fam = read4Data.readline().rstrip()
    rC4 = read4Data.readline().split()
    read4Count = float(rC4[0])
    ind = rep4Fam.find('_') 
    rep4Family = rep4Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element =  ', rep4Family
    read4Con = []
    for line in read4Data:
        list = line.split()
        read4Con.append(int(list[2]))    # list[2] contains the scores.
    print 'readCount3 = ', read3Count
    print 'readCount4 = ', read4Count
    print 'readCount3/readCount4 = ', read3Count/read4Count
    
    normRead3Con = []
    normRead4Con = []
    
    if read3Count>read4Count:
        normRead4Con = read4Con
        for base in read3Con:
            normRead3Con.append(int(float(base)*(read4Count/read3Count)))
    else:
        normRead3Con = read3Con
        for base in read4Con:
            normRead4Con.append(int(float(base)*(read3Count/read4Count)))
    
    
    
   
    
    #once the names of repeat element and RS sites is read and  list of per base scores are made, manyplots4() is called. This method plots 4 curves.
    manyplots5SuExSp( rep1Family, normRead1Con, rep2Family, normRead2Con,rep3Family, normRead3Con, rep4Family, normRead4Con,save)

    
def manyplots5SuExSp(rep1Family, normRead1Con, rep2Family, normRead2Con,rep3Family, normRead3Con, rep4Family, normRead4Con, save):
    rcParams['legend.loc'] = 'upper right'    # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11 # manually setting the plot size (width X height)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(normRead1Con)

    
   
    ys1 = normRead1Con # mre normal
    ys2 = normRead2Con #mre Cancer
    
    ys3 = normRead3Con #meDip normal
    ys4 = normRead4Con #medip cancer
    
    
    
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    print rep1Family
    print 'xs = ', len(xs)
    
    
    print 'ys1 = ', len(ys1)
    print 'ys2 = ', len(ys2)
    print 'ys3 = ', len(ys3)
    print 'ys4 = ', len(ys4)    
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    
    filename = rep1Family+'_MeDip_MRE.png' # plot will be saved with this name
    
    con1Label = rep1Family + ' MRE reads (Normal)'   #legend for reads data
    con2Label = rep2Family + ' MRE reads (Cancer)'
    con3Label = rep3Family + ' MeDIP reads (Normal)'   #legend for reads data
    con4Label = rep4Family + ' MeDIP reads (Cancer)'
    line1, = ax1.plot(xs, ys1, linewidth = 1.5, color = 'g')
    
    line2, = ax1.plot(xs, ys2, linewidth = 1.5, color = 'r')
    
    
   
   
    ax1.set_xlabel('base position in Repeat Element consensus')
    ax1.set_ylabel('per base score from MRE reads', color='k')
    #yticklabels are also kept with the same color as the line so that they can be visually related to each other. 
    for tl in ax1.get_yticklabels():
        tl.set_color('k')
    
    
    #making a twin y - axis, on the right hand side of the plot. This axis is used for plotting Restriction site data. 
    ax2 = ax1.twinx()
    
    #plotting the data for medip
   
    line3, = ax2.plot(xs, ys3, linewidth = 1.5, color = 'm') #normal medip
    line4, = ax2.plot(xs, ys4, linewidth = 1.5, color = 'k') #cancer medip

   
    ax2.set_ylabel('per base score from MeDIP reads', color='k')
    for tl in ax2.get_yticklabels():
        tl.set_color('k')
    
    #building legend
    legend((line1, line2, line3, line4,),(con1Label, con2Label,con3Label, con4Label))
   
    
    plt.title(rep1Family )
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    
    plt.show()      


def main():
    readFile1N = sys.argv[1]
    readFile1C = sys.argv[2]
    readFile2N = sys.argv[3]
    readFile2C = sys.argv[4]
    
    multiGraph5SuExSp(readFile1N, readFile1C, readFile2N, readFile2C, save )


if __name__=='__main__':
    main() 