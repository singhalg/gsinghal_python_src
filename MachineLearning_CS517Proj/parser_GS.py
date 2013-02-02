'''
Created on Apr 9, 2012

@author: gsinghal
'''
import sys, re
from sklearn.neighbors import NearestNeighbors as NN
#import parse
import pickle
import numpy as np
from sklearn.cluster import Ward
import random as rd
import copy
from sklearn.cluster import KMeans
import time as T
from sklearn.ensemble import RandomForestClassifier as RFC
#=======
from sklearn.externals import joblib
import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from sets import Set
from sklearn import cross_validation


from scipy import interp
import pylab as pl

from sklearn.metrics import roc_curve, auc
from sklearn.cross_validation import StratifiedKFold


def tsv2csv():
    fh = open('test.tsv', 'rU')
#    header = fh.readline()
    data = fh.readlines()
    fhout = open('test.csv', 'w')

#    hds = header.replace('\t', ',')
#    fhout.write(hds)

    for line in data:
        fhout.write(line.replace('\t', ','))


    fh.close()
    fhout.close()

def convert_file2dictionary(filename,dictKeyField):
    fTasks=open(filename,"r")
    original_lines=fTasks.readlines()
    fTasks.close()
    original_fields=map(lambda s:s.strip('"'),original_lines[0].strip("\n").strip("\r").split("\t"))
    all_items=dict()
    numrows = 0
    for t in original_lines[1:]:
        numrows += 1
        #print "processing row %s" % numrows
        item_dictionary={}
        for k,v in map(None,original_fields,t.split('\t')):
            item_dictionary[k]=v.strip("\n").strip("\r").strip('"')
        all_items[item_dictionary["TargetID"]]=item_dictionary
    print "processed %s rows" % numrows
    return all_items

def convert_file2dictionary2(filename,dictKeyField):
    fTasks=open(filename,"r")
    original_lines=fTasks.readlines()
    fTasks.close()
    original_fields=map(lambda s:s.strip('"'),original_lines[0].strip("\n").strip("\r").split("\t"))
    all_items=dict()
    for name in original_fields[1:]:
        all_items[name] = dict()
    numrows = 0
    for t in original_lines[1:]:
        numrows += 1
        #print "processing row %s" % numrows
        item_dictionary={}
        for k,v in map(None,original_fields,t.split('\t')):
            item_dictionary[k]=v.strip("\n").strip("\r").strip('"')
        for k,v in all_items.iteritems():
            all_items[k][item_dictionary["TargetID"]] = item_dictionary[k]
    print "processed %s rows" % numrows
    return all_items


def run():
    result = convert_file2dictionary("train.tsv","TargetID") #row major
    result2 = convert_file2dictionary2("train.tsv", "TargetID") #col major

    res1_keys = result.keys()
    res2_keys = result2.keys()

    for each in res1_keys[:1]:
        print each
        all_patients = result[each]
        print all_patients
#        print result[each]

    for each in res2_keys[:1]:
        print each
        allGenes =  result2[each]
        genes = allGenes.keys()
        for agene in genes[:300]:
            print agene
            print allGenes[agene]




def parser():
    pass
#    fh = open('train.csv', 'rU')
#    header = fh.readline()
#    data = fh.readlines()
#    NaNFree = len(data)
#    for line in data:
#        flds = line.split(',')
#
#
#
#        if re.search('NaN', line):
#            NaNFree-=1
#
#    print len(data)
#    print NaNFree


#    patients = parse.convert_file2dictionary("train.tsv","TargetID")
#
#    patient_ids = patients.keys()
#
#    for each in patient_ids[:1]:
#        print each, '\n'
##        patients[each], '\n'
#
#
#    print 'OKAY'
#    genes = parse.convert_file2dictionary2("train.tsv","TargetID")
#
#    gene_ids = genes.keys()



def makeArray(filename):

#    patients = parse.load_data(fnames = [])
#    keys = patients.keys()
#    for each in keys[:5]:
#        print each
#    print patients[keys[1]]

#    fhpatients = open('patients_pickle', 'rU')
#    patientTags = pickle.load(fhpatients)
#    fhpatients.close()
#
#    fhgenes = open('geneTags_pickled', 'rU')
#    geneTags = pickle.load(fhgenes)
#    fhgenes.close()




    fh = open(filename, 'rU')
    data = fh.readlines()
    patientTags = data[0].split(',')[1:]
#    print 'patientTags = ', patientTags
    # eg patientTags =  ['WGAAD-144', 'WGAAD-148', 'WGAAD-15', 'WGAAD-156', 'WGAAD-158', 'WGAAD-165', 'WGAAD-166', 'WGAAD-171', 'WGAAD-175', ..., 'WGAAD-189', 'WGAAD-190\n']



    patients = []
    patientsC = []
    for i in range(len(patientTags)):
        genesA =[]
        genesB = []
        for line in data:
            fld = line.split(',')[i+1].strip()
            genesA.append(fld)
            genesB.append(fld)
        patients.append(genesA)

        patientsC.append(genesB)


    genes = []
    geneTags = []
    for line in data:

        geneTags.append(line.split(',')[0])
        flds = line.split(',')[1:]
        genes.append(flds)

#    print 'geneTags = ', geneTags
    # eg geneTags = ['GI_10047091-S', 'GI_10047093-S', 'GI_10047103-S', 'GI_10047133-A', 'GI_10092596-S',..., 'GI_10092600-S']

    meanGeneVals= []
    for aGene in genes:
        meanGeneVals.append(mean(aGene))
#    print meanGeneVals
    # eg meanGeneVals = [3418.4777777777776, 83.35294117647061, 1179.7222222222224, 98.18750000000001, ... ,208.67222222222222]

    for i in range(len(patientsC)):
        for j in range(len(geneTags)):
            if (patientsC[i][j]=='NaN') or (patientsC[i][j]=='NaN\n') :
                patientsC[i][j]=meanGeneVals[j]
            else:
                patientsC[i][j] = float(patientsC[i][j])


#    print 'patients [17] = ', patients[17]
#    print 'patientsC [17] = ', patientsC[17]
    patientsArr = np.array(patientsC)


#    print patientsArr

    return patientsArr, patients, geneTags, patientTags, meanGeneVals


    full = 0
    partial = 0
    for eachRow in genes:
#        print eachRow
        if ('NaN'  in eachRow) or ('NaN\n' in eachRow):
            partial+=1
        else:
            full+=1

    print 'Genes without NaNs = ', full
    print 'Genes with NaNs = ', partial


def nearestNeighbor(filename, savePickle):
    #patientsArr is the 2d list in which NaN is replaced by the mean value.
    patientsArr, patients, geneTags, patientTags, meanGeneVals = makeArray(filename)

    neigh = NN(n_neighbors=5, radius=1.0)

    neigh.fit(patientsArr)
#    ct = 0
    print '# patients', len(patientTags)
    print '# genes', len(geneTags)
    for i in range(len(patientTags)):
        for j in range(len(geneTags)):
            if (patients[i][j]=='NaN') or (patients[i][j]=='NaN\n') :
#                ct+=1
#                if ct>2:
#                    sys.exit()

#                print 'patient ', i, ' has a missing value '
                nbrs = neigh.kneighbors(patientsArr[i]) # we are fitting the model with patientsArr, since in this file,
                #the NaN have been replaced by mean values
                knbrs = nbrs[1]
#                print 'nearest neighbors are ', nbrs[0],'  ||||  ' ,nbrs[1]
#                print knbrs
#                print 'new value for patients [', i+1, '][', j+1,'] = '
                patients[i][j]= retMissingVal(knbrs, patientsArr, j)
                #calculate the mean of the genevalues of these patients
#                pass
                # """fill in missing values"""
#                patients[i][j]=meanGeneVals[j]
            else:
                patients[i][j] = float(patients[i][j])
    if savePickle:
        joblib.dump(patients, 'imputed_test_data.pkl')
#        joblib.dump(patients, 'imputed_data.pkl')
##    fh_pickle = open('imputed_data', 'w')
##    pickle.dump(patients, fh_pickle)
##    fh_pickle.close()
    return patients

def crossValidateImputation(filename):


    patients = nearestNeighbor(filename, False)
    # patients has imputed values

    patientsC = copy.deepcopy(patients) # this is a deep copy of patients. We will replace the gene values in patientsC with 'NaN'

#    print type(patients)
#    print type(patients[0][0])

    locations = []

    numPatients = len(patients)
    numGenes = len(patients[0])
#    print numPatients
#    print numGenes
    # we have 54342 NaNs in the original dataset

    for x in range (10000):
        i = rd.randint(0,numPatients-1)
        j = rd.randint(0, numGenes-1)
        patientsC[i][j]='NaN'
        locations.append([i,j])

    # now the data in patientsC has NaNs

#    print 'patients[3]', patients[3]

#    print 'patientsC[3]', patientsC[3]
#    patientsArr = np.array(patientsC)
    #patientsArr is the array having missing values at random locations , patientsArr is totally separate from patientsC


    fh = open(filename, 'rU')
    data = fh.readlines()
    genes = []
    geneTags = []
    for line in data[1:]:

        geneTags.append(line.split(',')[0])
        flds = line.split(',')[1:]
        genes.append(flds)

#    print 'genes[0] = ',genes[0]



    meanGeneVals= []
    for aGene in genes:
        meanGeneVals.append(mean(aGene))

    stDevGenes = []
    for aGene in genes:
        stDevGenes.append(stdev(aGene))

#    print meanGeneVals
#    print stDevGenes

    patientsMean = copy.deepcopy(patientsC)
    for i in range(numPatients):
        for j in range(numGenes):
            if (patientsMean[i][j]=='NaN') or (patientsMean[i][j]=='NaN\n') :
                patientsMean[i][j]=meanGeneVals[j]

    # we will use the patientsMean to fit the nearest neighbor model
#    print 'meanGeneVals[5]' , meanGeneVals[5]
#    print  'patientsMean[3]',  patientsMean[3]
    neigh = NN(n_neighbors=5, radius=1.0)

    neigh.fit(patientsMean) # fit the model to the list having mean values

    for i in range(numPatients):
        for j in range(numGenes):
            if (patientsC[i][j]=='NaN') or (patientsC[i][j]=='NaN\n') :
                nbrs = neigh.kneighbors(patientsMean[i])
                knbrs = nbrs[1]

#                print nbrs
                patientsC[i][j]= retMissingVal(knbrs, patientsMean, j)

    # now in patientsC, randomly inserted NaN have been replaced by imputed values.

    compareVals = []
    for aLoc in locations:
        # compareVals is a list of pairs, each pair being [ starting data value, imputed value replacing NaN, mean Value, Standard Deviation]
        compareVals.append([ patients[aLoc[0]][aLoc[1]] , patientsC[aLoc[0]][aLoc[1]] , meanGeneVals[aLoc[1]], stDevGenes[aLoc[1]]  ])

#    print 'compareVals[:20]', compareVals[:20]
    fhpickle = open('compareVals', 'w')
    pickle.dump(compareVals, fhpickle)


def meanCenteredData(filename):

#    originalData = nearestNeighbor(filename, False)
    originalData = joblib.load('imputed_data.pkl')


    processed = copy.deepcopy(originalData)

    processedArr = np.array(processed)

    meanGeneVals = []
    for x in range(len(originalData[0])):
        mean = np.mean(processedArr[:,x])
        meanGeneVals.append(mean)

    for i in range(len(originalData)):
        for j in range(len(originalData[1])):
            processedArr[i][j] = processedArr[i][j]/meanGeneVals[j]


    joblib.dump(processedArr, 'meanCenteredData.pkl')




def hC(filename):
    data = meanCenteredData(filename)

    st = T.time()
    ward = Ward(n_clusters=6).fit()
    label = ward.labels_
    print "Elapsed time: ", T.time() - st
    print "Number of points: ", label.size


'''
hCwR = hierarchical clustering with R
dataType = meanCentered or imputed
featureType = univariate or kmeans

'''
def hCwR(dataType, featureType, numFeatures):

#    data = meanCenteredData(filename)
    fh = open('train.csv', 'rU')
    data = fh.readlines()
    fh.close()
    patientTags = data[0].split(',')[1:]

    patientTagsN = []

    for each in patientTags:
        if re.search('CON', each):
            patientTagsN.append(each.replace('WGA', '>->->->->->->->->->'))
        else:
            patientTagsN.append(each.replace('WGA', '<                  <'))



    geneTags = []
    for line in data[1:]:
        geneTags.append(line.split(',')[0])

    if dataType == 'meanCentered':
        data  = joblib.load('GS_pickles/meanCenteredData.pkl')
    else:
        data = joblib.load('GS_pickles/imputed_data.pkl')

    if featureType == 'univariate':
        if numFeatures == '44':
            top20Features = joblib.load('data/univariate_features_44.pkl')
        elif numFeatures == '87':
            top20Features = joblib.load('data/univariate_features_87.pkl')
        elif numFeatures == '433':
            top20Features = joblib.load('data/univariate_features_433.pkl')
        elif numFeatures == '865':
            top20Features = joblib.load('data/univariate_features_865.pkl')

    elif featureType == 'kmeans':
        if numFeatures == '44':
            top20Features = joblib.load('GS_pickles/kmeans_Genes_44_100x_v1.pkl')
        elif numFeatures == '87':
            top20Features = joblib.load('GS_pickles/kmeans_Genes_87_100x_v1.pkl')
        elif numFeatures == '433':
            top20Features = joblib.load('GS_pickles/kmeans_Genes_433_50x_v1.pkl')
        elif numFeatures == '865':
            top20Features = joblib.load('GS_pickles/kmeans_Genes_865_50x_v2.pkl')
    elif featureType =='randomforest':
        top20Features = joblib.load('randomForest_features_44.pkl')

    else:
        if numFeatures =='44':
            top20Features = []
            for i in range(44):
                top20Features.append(rd.randint(0,8649))
            top20Features = sorted(top20Features)
        elif numFeatures =='87':
            top20Features = []
            for i in range(87):
                top20Features.append(rd.randint(0,8649))
            top20Features = sorted(top20Features)

        elif numFeatures =='433':
            top20Features = []
            for i in range(433):
                top20Features.append(rd.randint(0,8649))
            top20Features = Set(top20Features)
            top20Features = sorted(top20Features)
            print len(top20Features)

        elif numFeatures =='865':
            top20Features = []
            for i in range(865):
                top20Features.append(rd.randint(0,8649))
            top20Features = Set(top20Features)
            top20Features = sorted(top20Features)
            print len(top20Features)
        else:
            print 'change numGenes'
        print 'random features have been selected'



        #add custom feature pickle here


    top20Data = []
    top20geneTags = []


    for j in range(len(top20Features)):
            top20geneTags.append(geneTags[top20Features[j]])

    for i in range(len(data)):
        top20pGenes = []
        for j in range(len(top20Features)):
            top20pGenes.append(data[i][top20Features[j]])

        top20Data.append(top20pGenes)

    top20DataArr = np.array(top20Data)
    top20DataArr = top20DataArr.transpose()
    top20DataL = list(top20DataArr)


    csvfile = 'top' + str(len(top20Features))+'_'+ dataType +'_'+ featureType+'.csv'

    fhout = open(csvfile, 'w')
#    fhout2 = open('top20Data2.csv', 'w')

    cols = 'TargetID,'+ ','.join(patientTagsN)+ '\n'

    fhout.write(cols)
#    fhout2.write(cols)

    numGenes = len(top20DataL)
    numPatients  = len(top20DataL[0])


    for j in range(numGenes):
        top20DataString = [str(n) for n in top20DataL[j]]
        row1 = top20geneTags[j]+','+ ','.join(top20DataString)+'\n'
        fhout.write(row1)
#        row2 = geneTags[j]+','+ ','.join(data2[j])+'\n'
#        fhout2.write(row2)
    fhout.close()
#    fhout2.close()


def kmeansIter():

    # pick the specs you like
    kmeans(44, 100, 'v1')
#    kmeans(44, 100, 'v2')
#    kmeans(87, 100, 'v1')
#    kmeans(87, 100, 'v2')
#    kmeans(433, 50, 'v1')
#    kmeans(433, 50, 'v2')
#    kmeans(865, 50, 'v1')
#    kmeans(865, 50, 'v2')
#    kmeans(1730, 10, 'v1')
#    kmeans(2163, 10, 'v1')


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





def mean(alist):
    total= 0
    for each in alist:
        if each.strip() != 'NaN':
            total+=float(each)
    NaNs = alist.count('NaN') + alist.count('NaN\n')
    return (total/(len(alist)-NaNs))

def stdev(alist):

    total= 0
    for each in alist:
        if each.strip() != 'NaN':
            total+=float(each)
    NaNs = alist.count('NaN') + alist.count('NaN\n')
    mean = (total/(len(alist)-NaNs))


    sqTotal = 0

    for each in alist:
        if each.strip() != 'NaN':
            sqTotal+= ((float(each)-mean)**2)
    return math.sqrt(sqTotal/(len(alist)-NaNs))

def mean2(array):
    alist = list(array)
    total= 0
    for each in alist:
        if each != float('NaN'):
            total+=float(each)
    NaNs = alist.count(float('NaN')) + alist.count(float('NaN\n'))
    return (total/(len(alist)-NaNs))


'''
@list : list of patients, which are the nearest neighbors
@patientsArr: array of patient data with missing values been replaced by mean values
'''
def retMissingVal(alist, patientsArr, j):

    total = 0

    for i in alist[0]:

        total = total+ patientsArr[i][j]

    newVal = total/len(alist[0])

    return newVal



def plotCVres():

    #!/usr/bin/env python


    fhopen = open('compareVals', 'rU')
    vals = pickle.load(fhopen)

    stds = []
    for each in vals:
        std = (math.fabs(each[1]-each[0]))/each[3]
        stds.append(std)



    sortedS = sorted(stds)

    arrTill4 = sortedS[:-22]

    ArrStd = np.array(arrTill4)

    x, y = np.histogram(ArrStd, bins=50)



    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.hist(ArrStd, bins=50)
    plt.title('Accuracy of Imputation' )
    plt.xlabel("Abs(Imputed Value - Original Value) / Std Dev")
    plt.ylabel("Frequency")
    plt.show()

    ax.grid(True)

    plt.show()



    filename = 'cvResults.jpeg'

    plt.savefig(filename)




'''
@criteria: 'gini' or 'entropy'
@maxN = 1730

'''
def RFClassifier(criteria, maxN):

    fhin = open('train.csv', 'rU')
    header = fhin.readline()
    fhin.close()
    patientTags = header.split(',')[1:]
    y = []
    for each in patientTags:
        if re.search('CON', each):
            y.append(1)
        else:
            y.append(0)
    data = joblib.load('GS_pickles/meanCenteredData.pkl')

    RFModel = RFC(criterion=criteria, max_features = "auto",  compute_importances=True, n_jobs=6)

    classifier = RFModel.fit(data, y)


    testData = joblib.load('GS_pickles/imputed_test_data.pkl')

    predictions = RFModel.predict(testData)

    realLabels = []
    for each in predictions:
        if each==0:
            realLabels.append('AD')
        else:
            realLabels.append('Normal')

    print predictions
    print realLabels

#    sys.exit()
    featureImp = classifier.feature_importances_

#    print fsorted
    print 'feature importance', featureImp.shape, featureImp

    featureInd = []

    for i in range(8650):
        featureInd.append([featureImp[i], i])

    fBest = []
    fBestInd = []
#    for i in range(8650):
#        if featureInd[i][0]>0.001:
#            fBest.append(featureInd[i])
#            fBestInd.append(featureInd[i][1])
    fSorted = sorted(featureInd, key=sortFun)
#
#    print featureInd[:500]
    print fSorted[-44:]

    for each in fSorted[-44:]:
        fBest.append(each[1])

    fBestInd = sorted(fBest)
    print fBestInd

#    print 'len(fBest)',  len(fBest)
#    print fBest
#    print fBestInd
    joblib.dump(fBestInd, 'randomForest_features_44v2.pkl')
#
#    scor = classifier.oob_score_
#
#    df = classifier.oob_decision_function_
#    sys.exit()
    skf = cross_validation.StratifiedKFold(y, 10)
    cv_scores = cross_validation.cross_val_score(RFModel, data, y, cv=skf, n_jobs=1)
    print "Accuracy: %0.2f (+/- %0.2f)" % (cv_scores.mean(), cv_scores.std() / 2)
#
#
#
#
################################################################################
## Classification and ROC analysis
#
## Run classifier with crossvalidation and plot ROC curves
##cv = StratifiedKFold(y, k=6)
##classifier = svm.SVC(kernel='linear', probability=True)
#
    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 1, 100)
    all_tpr = []
    y = np.array(y).transpose()
    print y

    dataAr = np.array(data)
#
    dataTrans = RFModel.transform(dataAr)

    for i, (train, test) in enumerate(skf):
#        print dataTrans[train].shape
###        print y[train].shape
##        dataTrans[test].shape
##        print y

        probas_ = RFModel.fit(dataTrans[train], y[train]).predict_proba(dataTrans[test])
        # Compute ROC curve and area the curve
        fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
        mean_tpr += interp(mean_fpr, fpr, tpr)
        mean_tpr[0] = 0.0
        roc_auc = auc(fpr, tpr)
        pl.plot(fpr, tpr, lw=1, label='ROC fold %d (area = %0.2f)' % (i, roc_auc))
#
    pl.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
#
    mean_tpr /= len(skf)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    pl.plot(mean_fpr, mean_tpr, 'k--',
        label='Mean ROC (area = %0.2f)' % mean_auc, lw=2)
#
    pl.xlim([-0.05, 1.05])
    pl.ylim([-0.05, 1.05])
    pl.xlabel('False Positive Rate')
    pl.ylabel('True Positive Rate')
    pl.title('Receiver operating characteristic for Random Forest Classifier (entropy)')
    pl.legend(loc="lower right")
    pl.show()
#
def sortFun(ls):
    return ls[0]

def main():
#    run()
#    makeArray()
#    makeMatrix()
#    nearestNeighbor('train.csv', False)


#    crossValidateImputation('train.csv')
#    meanCenteredData('train.csv')
#    kmeans('train_2.csv')
#    kClusters = int(sys.argv[1])
#
#    iters = int(sys.argv[2])
#
#    v = sys.argv[3]
#
#    hCwR('imputed', 'randomforest', '44')
##    tsv2csv()
##    nearestNeighbor('test.csv', False)
#    plotCVres()
    RFClassifier('entropy', 'auto')
if __name__ == '__main__':
    main()