#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     21/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------


from scipy.stats.kde import gaussian_kde
from scipy.stats import norm
from numpy import linspace,hstack
from pylab import plot,show,hist

def kernelDensity():
    # creating data with two peaks
    sampD1 = norm.rvs(loc=-1.0,scale=1,size=300)
    sampD2 = norm.rvs(loc=2.0,scale=0.5,size=300)
    samp = hstack([sampD1,sampD2])

    # obtaining the pdf (my_pdf is a function!)
    my_pdf = gaussian_kde(samp)

    # plotting the result
    x = linspace(-5,5,100)
    plot(x,my_pdf(x),'r') # distribution function
    hist(samp,normed=1,alpha=.3) # histogram
    show()



def main():
    kernelDensity()

if __name__ == '__main__':
    main()
