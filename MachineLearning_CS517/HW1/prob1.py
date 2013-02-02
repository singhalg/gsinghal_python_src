'''
Created on Feb 18, 2012

@author: gsinghal
'''


import sys
from sklearn.neighbors import KNeighborsClassifier as KN
from sklearn.neighbors import NearestNeighbors as NN
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import parse 

def randrange(n, vmin, vmax):
    return (vmax-vmin)*np.random.rand(n) + vmin

def plot3dFig():

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    n = 100
    
    
    
    
    
    for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
        xs = randrange(n, 23, 32)
        ys = randrange(n, 0, 100)
        zs = randrange(n, zl, zh)
        ax.scatter(xs, ys, zs, c=c, marker=m)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()



#def trysklearn():
#    
#    iris = datasets.load_iris()
#    digits = datasets.load_digits()
#    print digits.data
#    print iris
    
def plot3dData():


    fig = plt.figure()
    ax = fig.add_subplot(111)
#    n = 100
    
    
    Z = [1,0,0,1,0,0,1,0,0,0,0,0,1] # home owner
    
#    Y = [1,1,1,1,1,1,1,1,1,1,1,1,1]
#    Z = [1]*13 # home owner
#    Y = [0,2,0,2,0.5,2,0.5,0,2,0,0,2,0]  # marital status
#    Y = [0]*13  # marital status
#    X = [12.5,10,7,12,9.5,6,22,8.5,7.5,9,9.8,13,8]  #annual income
    X = [12.5,20,7,24,11.4,12,26.4,8.5,15,9,9.8,26,8]  #annual income

    clr = ['g','g','g','g','r','g','g','r','g','r','m','m','m']
#    clr = ['o','o','o','o','d','o','o','d','o','d','x','x','x']

    A = [-6, -1, 1, 2, 3, 6, 11, 15, 19,]
    
    Aclr = ['g', 'g', 'r', 'r', 'r', 'g', 'g', 'r', 'r']
#    B =    [1, 1, 0, 0, 0, 1, 1, 0, 0]
    B = [1,1,1,1,1,1,1,1,1]
    ax.scatter(A, B, s=50, c=Aclr )
    
 
    ax.set_ybound(lower=-1, upper=5)
    ax.set_xlabel('Annual Income * Marital Status')
    ax.set_ylabel('Home Owner, Y=1; N=0')


    plt.show()

    
    
    


def knn():
    
    X = [[125,1], [200,0], [70,0], [240,1], [114,0], [120,0], [264,1], [85,0], [150,0], [90,0]]
    y = [ 0, 0, 0, 0, 1, 0, 0, 1, 0,1 ]
    model = KN(n_neighbors=3, weights='distance')
    model.fit(X,y)
    print '80k, Single, HO=Y', model.predict([80,1])
    print '98k, Single, HO=N', model.predict([98,0])
    print '130k, Married, HO=N', model.predict([260, 0])


def nearestN():
    X = [[125,1], [200,0], [70,0], [240,1], [114,0], [120,0], [264,1], [85,0], [150,0], [90,0]]
#    y = [ 0, 0, 0, 0, 1, 0, 0, 1, 0,1 ]
    model = NN(n_neighbors=1, radius=1)
    model.fit(X)
    y = [98.,0.]
    print model.kneighbors(y)
#    print '80k, Single, HO=Y', model.predict([80,1])
#    print '98k, Single, HO=N', model.predict([98,0])
#    print '130k, Married, HO=N', model.predict([260, 0])

def main():
#    trysklearn()
    plot3dData()
#    knn()
#    nearestN()
if __name__=='__main__':
    main()