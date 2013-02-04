'''
Created on May 27, 2010

@author: Gaurav
'''


import matplotlib.pyplot as plot

def tryplot():
    xs = [2, 3, 5, 7, 11]
    ys = [4, 9, 5, 9, 1]
    plot.plot(xs, ys)
    plot.savefig("squaremod10.png")
    
    
def main():
    tryplot()
    
if __name__ == '__main__':
    main()