'''
Created on May 20, 2010

@author: Gaurav

Sample on how to define a class in python
'''

import sys

"""
just invokes the class point
"""
def get():
    p = point(5,4)         # making an object
                           # in Java, this used to happen in this way
                           # point p = new point(5,4)
    
    print p.X
    print p.Y



"""
Constructor for class Point. 
As the first argument, the object is passed to itself.
"""
class point:

    
    def __init__(self, x, y):
        self.data = []
        self.X = x      
        self.Y = y      
        
        
get()

# no need for main method
#def main():
#    get()
#if __name__ == '__main__':
#        main()
