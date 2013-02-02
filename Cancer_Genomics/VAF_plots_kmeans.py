#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gaurav Singhal
#
# Created:     28/01/2013
# Copyright:   (c) Gaurav Singhal 2013
# Licence:     This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Unported License.
#              To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/.
#-------------------------------------------------------------------------------

import sys, pickle
from sets import Set
import numpy as np
from sklearn.cluster import KMeans

def csv_parser(fileName):
    data = open(fileName, 'rU').readlines()
    outfile = fileName[:-4] + '_kmeans.csv'
    fhout = open(outfile, 'w')
    outfile = data[0].strip() + ',Label' + '\n'
    fhout.write(outfile)


    vaf = []

    for line in data[1:]:
        flds = line.split(',')
        vaf.append([float(flds[7]), float(flds[8])])

    print vaf[:5]

    vaf_np = np.array(vaf)
    print len(vaf_np)
    print vaf_np[:5]

    kmeansModel = KMeans(k=6, init='k-means++', n_init=100, max_iter=3000)

    labels = kmeansModel.fit_predict(vaf_np)

##    clustDist = model.transform(vaf_np)
    print labels[:30]

    for j in range(1, len(data)):
        outline = data[j].strip() + ',' + str(labels[j-1]) + '\n'
        fhout.write(outline)
    fhout.close()

##
##
###    array = model.cluster_centers_
###    labels = model.labels_
##    inertia = model.inertia_
###    #
###    print len(array), len(array[0])
###    print labels
##    print 'inertia', inertia
##
##
##    #
##    print 'sample clustDist='
##    print len(clustDist), len(clustDist[0])
###    print clustDist[0]
###    for each in clustDist:
###        print pass
##
##    result = np.argmin(clustDist, 0)
##    sortedRes =  sorted(result)


def main():

    csv_parser('PT_2_VarScan_rare.csv')

if __name__ == '__main__':
    main()
