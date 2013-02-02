'''
Created on Jan 27, 2011

@author: Gaurav
'''


import sys
import re


def adapterInstanceSurvey( file):
    readCount = 0
    switch  = False
    one = open(file, 'rU')
    for line in one:
        if line[0:4] == '@HWI':
            switch = True
        else:
            if switch == True:
                #print line
                switch = False
                if len(line) < 76:
                    #print len(line)
                    readCount+= 1
                
                
                    
        
            
                

 
    return '# Adapter trimmed reads : ' + str(readCount)

def unCalledBasesurvey (file1):
    N = 'N'
    Ncount = 0
    readCount = 0
    one = open(file1, 'rU')
    
    for line in one:
        
        if line[0:1] == 'A' or line[0:1] =='T' or line[0:1] == 'C' or  line[0:1] =='G' or line[0:1] == 'N':
            
            readCount+=1
            if re.search(N, line):
                Ncount+= 1
                
            else:
                pass
        else : 
            pass
        
    
    print 'readCount = ' , readCount
    return 'NCount = '  + str(Ncount)

def main():
    openfile1 = sys.argv[1]   

    print  adapterInstanceSurvey(openfile1)   
 
if __name__ == '__main__':
    main()