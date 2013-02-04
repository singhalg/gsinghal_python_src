'''
Created on Jul 14, 2010
Last Edited on Jul 19, 2010 
@author: Gaurav
'''



import matplotlib.pyplot as plt 
import sys
from pylab import *   #required for legend


'''
This script generates plots from files containing per base scores for repeat elements using matplotlib.

'''


'''
This script takes in four files having consensus scores for a Repeat Element
@param - read1, read2 : File containing mapped reads (MRE)
@param - read3, read4 : File containing mapped reads (MeDip)

@param save: Boolean, save the file or not.
@output : plot, which contains read data on one Y axis and Restriction site data on another Y axis. 
'''

def multiGraph4(readFile1, readFile2, readFile3, readFile4, save ):
    
    # making a list of scores from readFile1
    
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
    read2Count = float(rC2[1])
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
    read4Count = float(rC4[1])
    ind = rep4Fam.find('_') 
    rep4Family = rep4Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element =  ', rep4Family
    read4Con = []
    for line in read4Data:
        list = line.split()
        read4Con.append(int(list[2]))    # list[2] contains the scores.
    print 'readCount1 = ', read3Count
    print 'readCount2 = ', read4Count
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
    manyplots4(rep1Family, normRead1Con, rep2Family, normRead2Con, rep3Family, normRead3Con, rep4Family, normRead4Con, save)
       



'''
This method takes in 4 consensus scores, one for reads, and one each for three restriction sites.
@param repFamily : This string froms the first part of file name and legend for readCon data
@param readCon : This is the per base consensus score for reads.
@param siteCon1 : This is the per base consensus score for restriction site. similarly siteCon2, siteCon3
@param site1name : String, representing the name of the string, and will make the legend. similarly site2name, site3name
'''     
def manyplots4(rep1Family, read1Con, rep2Family, read2Con, rep3Family, read3Con, rep4Family, read4Con,  save):
    rcParams['legend.loc'] = 'best'    # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11 # manually setting the plot size (width X height)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(read1Con)
    ys = read1Con #Normal MRE
    ys4 = read2Con #cancer MRE
    ys1 = read3Con # normal MEDip
    ys2 = read4Con # cancer MeDip

    
    print 'normal :'
    print ys
    print '\n'
    
    print 'cancer :'
    print ys4
    print '\n'
    
    
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    print rep1Family
    print 'xs = ', len(xs)
    print 'ys = ', len(ys)
    print 'ys4 = ', len(ys4)
    print 'ys1 = ', len(ys1)
    print 'ys2 = ', len(ys2)
    
        
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    # plotting data for MRE
    filename = rep1Family+'_read_RS.png' # plot will be saved with this name
    con1Label = rep1Family + ' reads (MRE : Normal)'   #legend for reads data
    con2Label = rep2Family + ' reads (MRE : Cancer)'
    line1, = ax1.plot(xs, ys, linewidth = 2.0, color = 'g')
    line5, = ax1.plot(xs, ys4, linewidth = 2.0, color = 'r')
    ax1.set_xlabel('base position in consensus')
    ax1.set_ylabel('per base score from read data', color='k')
    #yticklabels are also kept with the same color as the line so that they can be visually related to each other. 
    for tl in ax1.get_yticklabels():
        tl.set_color('k')
    
    #plotting data for MeDip
    line2, = ax1.plot(xs, ys1, color = 'b') 
    line3, = ax1.plot(xs, ys2, color = 'm')
    con3Label = rep1Family + ' reads (MeDip : Normal)'   #legend for reads data
    con4Label = rep2Family + ' reads (MeDip : Cancer)'
   

    
    #building legend
    legend((line1, line5, line2, line3),(con1Label, con2Label, con3Label, con4Label))
   
    
    plt.title(rep1Family )
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    
    plt.show()
    
    

  
def SuperPlotter(siteFile1, siteFile2, siteFile3, readFile1N, readFile1C, readFile2N, readFile2C, readFile3N, readFile3C ):
    save = True
    multiGraph4(readFile1N, readFile1C, siteFile1, siteFile2, siteFile3, save)
    multiGraph4(readFile2N, readFile2C, siteFile1, siteFile2, siteFile3, save)
    multiGraph4(readFile3N, readFile3C, siteFile1, siteFile2, siteFile3, save)
   


#def main():
#    # use either of the two method calls. 
#    readFile1N = sys.argv[1] #normal
#    readFile1C = sys.argv[2] #cancer
#    readFile2N = sys.argv[3] #normal
#    readFile2C = sys.argv[4] #cancer
#    readFile3N = sys.argv[5]
#    readFile3C = sys.argv[6]
#    siteFile1 = sys.argv[7]
#    siteFile2 = sys.argv[8]
#    siteFile3 = sys.argv[9]
#    
#    
#    SuperPlotter(siteFile1, siteFile2, siteFile3, 
#                 readFile1N, readFile1C, readFile2N, readFile2C, readFile3N, readFile3C )
#    
#
##    readFile = sys.argv[1]
##    siteFile1 = sys.argv[2]
##    save = sys.argv[3]
##    multiGraph2(readFile, siteFile1, save )
    
    
def main():
    readFile1N = sys.argv[1]
    readFile1C = sys.argv[2]
    readFile2N = sys.argv[3]
    readFile2C = sys.argv[4]
    save = sys.argv[6]
    multiGraph4(readFile1N, readFile1C, readFile2N, readFile2C, save )
    
    
if __name__=='__main__':
    main()    