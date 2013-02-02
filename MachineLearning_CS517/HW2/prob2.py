'''
Created on Mar 27, 2012

@author: gsinghal
'''
import sys
from pylab import *
import matplotlib.pyplot as plt

def BOC():
    
#    X = [0]*30
#    htt   hthhtth                  ththhthhht                       hhtththhth
#    seq = [1,0,0,1,0,1,1,0,0,1,   0,1,0,1,1,0,1,1,1,0,      1,1,0,0,1,0,1,1,0,1] # 1 = H, 0 = T
    
    seq = genSeq()
    
    ph =[0.3, 0.7]   
    
    pD_h = [[0.5, 0.4], 
            [0.5, 0.6]]
    
#    
#    pH_h1 = 0.5
#    pT_h1 = 0.5
#    pH_h0 = 0.6
#    pT_h0 = 0.4
    
    H = []      # len(H) = len(seq)                     # vector H;  H1 = Posterior probs of h1 and h0 at flip 1, H2  = posterior prob at flip 2  
    
    LH = [1,1]
    posteriors = [0,0]
    
    for aflip in seq:
        
        for i in range(2):
            
            LH[i] = LH[i]* pD_h[aflip][i]
            
            posterior = ph[i] * LH[i]
            posteriors[i] = posterior
            
        print posteriors
        deno = sum(posteriors)
        print deno
        pp = [n/deno for n in posteriors]
        print pp
        H.append(pp)
        
    for each in H:
        print each
    
    plot_posteriors(H)
    
def plot_posteriors(H):    
    X = []
    for i in range(1,101):
        X.append(i)
        
    Y1 = []
    Y2 = []
    for posterior in H:
        Y1.append(posterior[0])
        Y2.append(posterior[1])
    
    fig = plt.figure()
    
    ax1 = fig.add_subplot(111)
    ax1.plot(X, Y1, color ='b', label = 'H1 : Dice is fair')
    
    ax2 = fig.add_subplot(111)
    ax1.plot(X, Y2, color ='g', label = 'H2 : Dice is loaded ')
    legend(loc = 'upper left')
    title('Posteriors')
    ax1.set_xlabel('Coin flip instance')
    ax1.set_ylabel('Posterior Probability of Hypothesis')
    plt.show()
    


def genSeq():
    seq = 'THTHHTHTTTHHTHHHTTHTTTHHHTTHTHHTHHTHHTHHTHHTHTHHTHHTHTTHTHHHTHHHHHHTHTHHTHHHTHTHTHTTTTTHHTTHTHHHTHTT'
    
    retSeq = []
    for letter in seq:
        if letter =='H':
            retSeq.append(1)
        elif letter =='T':
            retSeq.append(0)
        else:
            print 'error'
    
    print seq
    print retSeq
    print len(retSeq)
    print len(seq)
    return retSeq
def main():
    BOC()
    genSeq()
#    fileName = sys.argv[1]
#    bayes(fileName)

if __name__=='__main__':
    main()