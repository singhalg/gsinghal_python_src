#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     21/08/2012
# Copyright:   (c) Gaurav Singhal 2012
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------
##from sklearn.cluster import KMeans
from sklearn import cluster, datasets
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def kmeans(kclusters, iters, v):

#    originalData = nearestNeighbor(filename, False)

    originalData = joblib.load('imputed_data.pkl')


    kmeansModel = KMeans(k=kclusters, init='k-means++', n_init=iters, max_iter=500, tol=0.002)

    dataArr = np.array(originalData)

    dataArrTp = dataArr.transpose()



    model = kmeansModel.fit(dataArrTp)

    clustDist = model.transform(dataArrTp)



#    array = model.cluster_centers_
#    labels = model.labels_
    inertia = model.inertia_
#    #
#    print len(array), len(array[0])
#    print labels
    print 'inertia', inertia

#    scores = kmeansModel.score(dataArrTp[0])


#
#    print clustDist
#
    print 'sample clustDist='
    print len(clustDist), len(clustDist[0])
#    print clustDist[0]
#    for each in clustDist:
#        print pass

    result = np.argmin(clustDist, 0)
    sortedRes =  sorted(result)
#    print sortedRes

    pickleFile = 'kmeans_Genes_'+str(kclusters) +'_'+str(iters)+'x_'+ v + '.pkl'

    joblib.dump(sortedRes, pickleFile)




def try_kmeans():

    iris = datasets.load_iris()
    X_iris = iris.data
    y_iris = iris.target

    for i in range(0,10):
        print i
        print X_iris[i]

    k_means = cluster.KMeans(k=3)
    k_means.fit(X_iris)
##    KMeans(copy_x=True, init='k-means++', ...
    print k_means.labels_
    ##[1 1 1 1 1 0 0 0 0 0 2 2 2 2 2]
    print y_iris
    ##[0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]


def Kmean_clustering(csvFile):
    fhin = open(csvFile, 'rU')
    data = fhin.readlines()
    fhin.close()
    X_vaf = []
    prim = []
    met = []
    clrs = []
    depth = []

    for line in data[10:]:
        flds =  line.split(',')

        if (float(flds[5]) > 1) or (float(flds[6])>1):
            pass
        else:

            try:
                dp =(int(flds[2]) + int(flds[3]))/2.00
                if dp >= 20:


                    depth.append((int(flds[2]) + int(flds[3]))/2.00)
                    prim.append(float(flds[5]))
                    met.append(float(flds[6]))
                    vaf = [float(flds[5]), float(flds[6])]
                    X_vaf.append(vaf)
            except:
                print line
                continue


    X_arr = np.array(X_vaf)
    print X_arr[:9]
    k_means = cluster.KMeans(k=4)
    k_means.fit(X_arr)
##    KMeans(copy_x=True, init='k-means++', ...
    print k_means.labels_[:1000]
    lbls =  k_means.labels_
    for each in lbls:
        if each == 2:
            clrs.append('c')
        elif each == 3:
            clrs.append('b')
        elif each == 1:
            clrs.append('g')
        elif each == 0:
            clrs.append('w')
    return prim, met, depth, clrs

def plot3dData():

    prim, met, depth, clrs = Kmean_clustering('PT_6_variant_diff.csv')
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')


##import numpy as np
##from mpl_toolkits.mplot3d import Axes3D
##import matplotlib.pyplot as plt
##
##def randrange(n, vmin, vmax):
##    return (vmax-vmin)*np.random.rand(n) + vmin
##
##fig = plt.figure()
##ax = fig.add_subplot(111, projection='3d')
##n = 100
##for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
##    xs = randrange(n, 23, 32)
##    ys = randrange(n, 0, 100)
##    zs = randrange(n, zl, zh)
##    ax.scatter(xs, ys, zs, c=c, marker=m)
##
##ax.set_xlabel('X Label')
##ax.set_ylabel('Y Label')
##ax.set_zlabel('Z Label')
##
##plt.show()
###    n = 100

##
##    Z = [1,0,0,1,0,0,1,0,0,0,0,0,1] # home owner
##
###    Y = [1,1,1,1,1,1,1,1,1,1,1,1,1]
###    Z = [1]*13 # home owner
###    Y = [0,2,0,2,0.5,2,0.5,0,2,0,0,2,0]  # marital status
###    Y = [0]*13  # marital status
###    X = [12.5,10,7,12,9.5,6,22,8.5,7.5,9,9.8,13,8]  #annual income
##    X = [12.5,20,7,24,11.4,12,26.4,8.5,15,9,9.8,26,8]  #annual income
##
##    clr = ['g','g','g','g','r','g','g','r','g','r','m','m','m']
###    clr = ['o','o','o','o','d','o','o','d','o','d','x','x','x']
##
##    A = [-6, -1, 1, 2, 3, 6, 11, 15, 19,]
##
##    Aclr = ['g', 'g', 'r', 'r', 'r', 'g', 'g', 'r', 'r']
###    B =    [1, 1, 0, 0, 0, 1, 1, 0, 0]
##    B = [1,1,1,1,1,1,1,1,1]
    ax.scatter(prim, met, depth, s=5, c=clrs )


    ax.set_ybound(lower=0.05, upper=1.0)
    ax.set_xbound(lower=0.05, upper=1.0)
    ax.set_zbound(lower=100, upper=700.0)

    ax.set_xlabel('Primary VAF')
    ax.set_ylabel('Metastasis VAF')
    ax.set_zlabel('Depth')



    plt.show()


##    kmeansModel = KMeans(k=kclusters, init='k-means++', n_init=iters, max_iter=500, tol=0.002)

def main():
##    try_kmeans()
##    Kmean_clustering('PT_2_variant_diff_cutoff_strict_dp100.csv')
    plot3dData()

if __name__ == '__main__':
    main()
