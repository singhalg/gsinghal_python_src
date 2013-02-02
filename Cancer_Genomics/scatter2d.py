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
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
from matplotlib.collections import EllipseCollection

def scatter2d(x,y, clrArray, markerArray, title):


##    # the random data
##    x = np.random.randn(100)
##    y = np.random.randn(100)

    nullfmt   = NullFormatter()         # no labels

    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left+width+0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    # start with a rectangular Figure
    plt.figure(1, figsize=(14,14))

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)

    # no labels
    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)

    # the scatter plot:
    axScatter.scatter(x, y, c=clrArray, marker = '*')
    axScatter.set_xlabel('Primary')
    axScatter.set_ylabel('Metastasis')
    axScatter.set_title(title, position=(1.05,1), size='x-large' )

    # now determine nice limits by hand:
    binwidth = 0.01
    xymax = np.max( [np.max(np.fabs(x)), np.max(np.fabs(y))] )
    lim = ( int(xymax/binwidth) + 1) * binwidth

    axScatter.set_xlim( (0, 1) )
    axScatter.set_ylim( (0, 1) )

    bins = np.arange(-lim, lim + binwidth, binwidth)
    axHistx.hist(x, bins=bins)
    axHisty.hist(y, bins=bins, orientation='horizontal')

    axHistx.set_xlim( axScatter.get_xlim() )
    axHisty.set_ylim( axScatter.get_ylim() )
##    plt.colorbar()
    plt.show()


def scatterPlot(csvFile, depth, title):
    fhin = open(csvFile, 'rU')
    data = fhin.readlines()
    fhin.close()
    prim_vaf = []
    met_vaf = []
    markerArray = []
    clrArray = []

    markers = {'0':'o', '1':'D', '2':'s', '3':'*'}

    for line in data[1:]:
        flds =  line.split(',')
##        if len(flds[0])>5:
##            print flds[0]

        try:
            if ((float(flds[5]) < 0.05) or (float(flds[6])<0.05)):
                pass
            else:
                variantDepth  = (float(flds[2]) + float(flds[3]) )/2
                if (len(flds[0])<7  )  and ( variantDepth>=depth):
##                    if (float(flds[5]))
                    colr = variantDepth*0.001
                    if colr > 1:
                        colr = 1  # if depth > 1000, then colr = 1, otherwise colr = 0.001 * variant depth

##                    prim_met_fc.append(foldChange(flds))
##                    print markers[flds[7].strip()]
                    markerArray.append(markers[flds[7].strip()])
                    clrArray.append(colr)
##                    prim_met_annotation.append([markers[flds[7].strip()], colr])

                    prim_vaf.append(float(flds[5]))
                    met_vaf.append(float(flds[6]))

                else:
                    pass
        except:
            print "Iter failed"
##    orderedByFC = sorted(prim_met_fc, reverse = True, key = myFun)
##    print orderedByFC[:20]
##
##    primary_vafs = []
##    metastasis_vafs = []
##    for each in orderedByFC[:10000]:
##        primary_vafs.append(each[0])
##        metastasis_vafs.append(each[1])
##

    prim_arr = np.array(prim_vaf)
    met_arr = np.array(met_vaf)
##    prim_arr = np.array(primary_vafs)
##    met_arr = np.array(metastasis_vafs)

    print len(prim_vaf), len(met_vaf)
    scatter2d(prim_arr, met_arr, clrArray, markerArray, title)


def myFun(alist):
    return alist[2]


def foldChange(flds):

    prim = float(flds[5])

    met = float(flds[6])
    if (prim == 0):
        prim+=0.0001
    if (met == 0):
        met+=0.0001


    if prim >= met:
        greater = prim
        smaller = met
    else:
        greater = met
        smaller = prim
    change = greater/smaller
    return [prim, met, change]
##    if change >=1.1:
##        significant+=1
##        prim_vaf.append(prim)
##        met_vaf.append(met)
##        fhout.write(line)
##    else:
##        insignificant+=0
##        insignf.append([prim, met])
##    X_arr = np.array(X_vaf)
##    print X_arr[:9]
##    k_means = cluster.KMeans(k=30)
##    k_means.fit(X_arr)
####    KMeans(copy_x=True, init='k-means++', ...
##    print k_means.labels_[:100]
####    kmeansModel = KMeans(k=kclusters, init='k-means++', n_init=iters, max_iter=500, tol=0.002)

def main():
##    fileName = sys.argv[1]
    scatterPlot("PT_13_variants_rm_common_cutoff.csv", 100, 'PT_13')

if __name__ == '__main__':
    main()
