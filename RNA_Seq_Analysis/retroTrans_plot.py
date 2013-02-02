'''
Created on Jan 24, 2011

@author: Gaurav

#-------------------------------------------------------------------#
# Copyright (C) 2011 Gaurav Singhal                                 #
# All Rights Reserved.                                              #
#                                                                   #
# Author: Gaurav Singhal                                            #
# Created : Jan 24, 2011                                            #
# Send all comments and queries to gsinghal@wustl.edu               #
#                                                                   #
# DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS"                     #
#             WITHOUT WARRANTY OF ANY KIND.                         #
#-------------------------------------------------------------------#


'''


"""
Make a pie chart - see
http://matplotlib.sf.net/matplotlib.pylab.html#-pie for the docstring.

This example shows a basic pie chart with labels optional features,
like autolabeling the percentage, offsetting a slice with "explode"
and adding a shadow.

Requires matplotlib0-0.70 or later

"""
from pylab import *
import matplotlib.pyplot as plt
import sys
import re



def retroTrans_plot():
    pass
    print 'hello'
#    inFile = open(fileName, 'rU')
#    inFile.readline()
#    
#    repeat = {}
#    
#    
#    repeat ['DNA'] = 0
#    repeat ['LINE'] = 1
#    repeat ['Low_Complexity'] = 2
#    LTR = 'LTR'
#    Other = 'Other'
#    RC = 'RC'
#    RNA = 'RNA'
#    rRNA = 'rRNA'
#    Satellite = 'Satellite'
#    scRNA  = 'scRNA'
#    SimpleRepeat = 'Simple_Repeat'
#    SINE = 'SINE'
#    snRNA = 'snRNA'
#    srpRNA = 'srpRNA'
#    tRNA = 'tRNA'
#    Unknown = 'Unknown'
#    
#    
#
#    
#    #repeats = [DNA, LINE, LowComplexity, LTR, Other, RC, RNA, rRNA, 
#     #          Satellite, scRNA, SimpleRepeat, SINE, snRNA, srpRNA,
#      #         tRNA, Unknown ]
#
#    
#    for line in inFile:
#        info = line.split()
#        repFam = info[0]
#        
#   
#    
#    
#    
#    pass
#
#    
#    plot()





def plot():

# make a square figure and axes
    labels = 'DNA', 'LINE', 'Low_complexity', 'LTR','Other','RC','RNA','rRNA','Satellite','scRNA','Simple_Repeat','SINE','snRNA','srpRNA','tRNA', 'Unknown'
    fracs = [3.19, 18.96,1.99, 11.57, 0.458, 0.01, 0.16, 37.46, 0.3958, 0.074, 2.14,22.97, 
             0.102, 0.396, 0.046, 0.04]  
    
    plt.figure(1, figsize=(12,14))
    #ax = plt.axes([0.1, 0.1, 0.8, 0.8,0.1, 0.1, 0.8, 0.8,0.1, 0.1, 0.8, 0.8,0.1, 0.1, 0.8, 0.8 ])
    
    # define labels and fracs
    
    explode=(0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0)
    plt.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
    plt.title('Retrotransposition', bbox={'facecolor':'0.8', 'pad':5})

    plt.show()
    plt.savefig('retro.png')




def main():
       
    plot()   
 
if __name__ == '__main__':
    main()