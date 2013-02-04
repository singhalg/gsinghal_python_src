'''
Created on Mar 18, 2011

@author: Gaurav
'''
import numpy as np
import matplotlib.pyplot as plt


def histogram():
    
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(100)
    
    print np.random.randn(2)
    
    for each in x:
        print each
# the histogram of the data
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([0, 180, 0, 0.05])
    plt.grid(True)
    plt.show()

 
def main():
    histogram() 
 
if __name__=='__main__':
    main()    