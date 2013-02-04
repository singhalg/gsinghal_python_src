'''
Created on May 26, 2010
Last Modified July 19 2010
@author: Gaurav
'''
import sys
from Parser import *



def main():
    file = sys.argv[1]
    Parser(file, 'Looper', True)
    Parser(file, 'MER75', True)
    Parser(file, 'MER85', True)
    Parser(file, 'Charlie9', True)
    Parser(file, 'MER33', True)
    Parser(file, 'Zaphod', True)
    Parser(file, 'Charlie5', True)
    Parser(file, 'MADE1', True)
    Parser(file, 'MARNA', True)
    Parser(file, 'Ricksha_c', True)
    Parser(file, 'L4', True)
   
    
    
#    Parser(file, 'AluYb9', True)
#    Parser(file, 'AluYc', True)
#    Parser(file, 'AluYc3', True)
#    Parser(file, 'AluYc5', True)
#    Parser(file, 'AluYd8', True)
#    Parser(file, 'AluYg6', True)
#    Parser(file, 'AluYh9', True)
#    Parser(file, 'MIR', True)
#    Parser(file, 'MIR3', True)
#    Parser(file, 'L2', True)
#    Parser(file, 'L3', True)
#    Parser(file, 'L2a', True)
#    Parser(file, 'L2b', True)
#    Parser(file, 'L2c', True)
#    Parser(file, 'L5', True)
#    Parser(file, 'U6', True)
#    
#    Parser(file, 'Arthur1', True)
#    Parser(file, 'MADE2', True)
#    Parser(file, 'MER53', True)
#    Parser(file, 'MER45A', True)
#    Parser(file, 'MER58A', True)
#    Parser(file, 'Tigger5', True)
#    Parser(file, 'Tigger1', True)
#    Parser(file, 'MER8', True)
#    Parser(file, 'Charlie9', True)
#    Parser(file, 'Ricksha', True)
#    Parser(file, 'MER5A', True)
#    Parser(file, 'MER5B', True)
#            
#    Parser(file, 'AT_rich', True)
#    Parser(file, 'MLT1H2', True)
#    Parser(file, 'MER4E', True)
#    Parser(file, 'LTR33', True)
#    Parser(file, 'MSTA', True)
    
    
    
    
if __name__ == '__main__':
    main()

