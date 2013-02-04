'''
Created on May 26, 2010

@author: Gaurav
'''


import sys
from Analyzer1 import *



def main():
    
    file26 = sys.argv[1]
    file27 = sys.argv[2]
    file28 = sys.argv[3]
    file29 = sys.argv[4]
    file30 = sys.argv[5]
    file31 = sys.argv[6]
    file32 = sys.argv[7]
    file33 = sys.argv[8]
    file34 = sys.argv[9]
    file35 = sys.argv[10]
    
    
    
    Analyze(file26, 'L4', True, False)
    Analyze(file27, 'Ricksha_c', True, False)
    Analyze(file28, 'MARNA', True, False)
    Analyze(file29, 'Looper', True, False)
    Analyze(file30, 'Charlie5', True, False)
    Analyze(file31, 'Zaphod', True, False)
    Analyze(file32, 'MER33', True, False)
    Analyze(file33, 'Charlie9', True, False)
    Analyze(file34, 'MER85', True, False)
    Analyze(file35, 'MER75', True, False)

    
   
if __name__ == '__main__':
    main()