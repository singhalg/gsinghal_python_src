'''
Created on May 27, 2010

@author: Gaurav
'''
#!/usr/bin/env python
import numpy as np

from Analyzer1 import *

import sys
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def plot():
    mu, sigma = 100, 15
    #x = mu + sigma*np.random.randn(10000)
    file = sys.argv[1]
    x = Analyze(file, 'AluY', False, True)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 500, normed=1, facecolor='green', alpha=0.75)

    # add a 'best fit' line
    y = mlab.normpdf( bins, mu, sigma)
    l = plt.plot(bins, y, 'r--', linewidth=1)

    plt.xlabel('Consensus')
    plt.ylabel('Per Base Score')
    plt.title(r'$\mathrm{Per Base Plot\ of\ Repeat Consensus :}\ \mu=100,\ \sigma=15$')
    plt.axis([0, 350, 0, 100])
    plt.grid(True)

    plt.show()



def main():
    plot()

if __name__ == '__main__':
    main()