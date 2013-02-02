#!/usr/bin/env python
import re, math
import os
import csv
import shutil
from os import environ
from os.path import dirname
from os.path import join
from os.path import exists
from os.path import expanduser
from os.path import isdir
from os import listdir
from os import makedirs
import numpy as np
import pylab as pl
from sklearn import datasets, svm
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.externals import joblib
from sklearn import cross_validation
from sklearn import metrics

class Bunch(dict):
	"""Container object for datasets: dictionary-like object that
	   exposes its keys as attributes."""

	def __init__(self, **kwargs):
		dict.__init__(self, kwargs)
		self.__dict__ = self


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

# This function generates the data required for sklearn
def genData():
	result = convert_file2dictionary("train.tsv","TargetID") #row major
	result2 = convert_file2dictionary2("train.tsv", "TargetID") #col major
	print "dictionary has %s items" % len(result)
	print "dictionary2 has %s items" % len(result2)
   	cols = sorted(result.keys())  # this gives us gene names in order
	rows = sorted(result2.keys())  # this gives us patient names in order

	# reprint the data into a new file, column major
	# this now prints the data out to a .csv file that is suitable for sklearn
	with open("skdata.csv", "w") as f:
		firstline = "%s,%s,%s,%s\n"%(len(rows), len(cols), "AD", "CON")
		f.write(firstline)
		for i in xrange(len(rows)):
			line = ""
			row = result2["%s"%rows[i]]
			for j in xrange(len(cols)):
				line = "%s,%s" %(line,row["%s"%cols[j]].replace("NaN","0"))
			line = line.lstrip(",") # we need to strip the leading comma
			label = ""
			if re.search("AD", rows[i]):
				label = "0" # kind of a bad way to assign labels, but whatever
			else:
				label = "1"
			line = "%s,%s\n" %(line,label)
			f.write(line)
	f.close()

	# load the data using our modified load_data() function
	# we must pass in the feature names for the Bunch data structure
	data_matrix = load_data(fnames=cols)

	# save the data matrix along with column and row names to file
	# this uses the joblib dump function, for great justice
	joblib.dump(data_matrix, 'datamatrix.pkl')
	joblib.dump(cols, 'features.pkl')
	joblib.dump(rows, 'samples.pkl')

# This function reads the data from files and returns a 3 tuple
def readData():
	data_matrix = joblib.load('datamatrix.pkl')
	features = joblib.load('features.pkl')
	samples = joblib.load('samples.pkl')
	return (data_matrix, features, samples)

def run():
	#genData()     # generate data files; comment out if data already exist
	(data_matrix, features, samples) = readData()   # extract data from data files

	# Print the data we just read in
	x = data_matrix.data
	y = data_matrix.target
	target_names = data_matrix.target_names
	print "data: %s\n" % x
	print "targets: %s\n" % y
   	print "target names: %s\n" % target_names

	x_indices = np.arange(x.shape[-1])
##	pl.figure(1)
##	pl.clf()

	###############################################################################
	# Univariate feature selection with F-test for feature scoring
	# We use the default selection function: the 1% most significant features
	selector = SelectPercentile(f_classif, percentile=1)
	selector.fit(x, y)
	scores = -np.log10(selector._pvalues)
	scores /= scores.max()
##	pl.bar(x_indices - .45, scores, width=.1,
##			label=r'Univariate score ($-Log(p_{value})$)',
##			color='g')

	# Trimming the matrix, now should contain 1% of the 8650 features
	trimmed_x = selector.transform(x)
	(i,j) = trimmed_x.shape
	print "new data matrix: %s" % trimmed_x
	print "new matrix shape: (%s,%s)" % (i,j)
	print "selected features: %s" %(selector.get_support(indices=True))

	###############################################################################
	# Compare to the weights of an SVM
##	clf = svm.SVC(kernel='linear')
##	clf.fit(x, y)
##
##	svm_weights = (clf.coef_ ** 2).sum(axis=0)
##	svm_weights /= svm_weights.max()
##	pl.bar(x_indices - .15, svm_weights, width=.1, label='SVM weight',
##			color='r')

##	pl.title("Comparing feature selection")
##	pl.xlabel('Feature number')
##	pl.yticks(())
##	pl.axis('tight')
##	pl.legend(loc='upper right')
##	pl.show()

	###############################################################################
	# Fitting the trimmed data to a linear SVM classifier
	clf = svm.SVC(kernel='linear')
	clf.fit(trimmed_x,y)
	# Save this classifier to file, for future reference
	joblib.dump(clf, 'SVM_trimmed1.pkl')

	###############################################################################
	# An example of cross-validation with SVM classifier
	clf2 = svm.SVC(kernel='linear')
	n_samples = x.shape[0] # should be 330 (shape = (330, xxx))

	# This gives us an iterator for stratified 10-fold
	skf = cross_validation.StratifiedKFold(y, 10)

	# We perform cv with this iterator, get scores
	cv_scores = cross_validation.cross_val_score(clf2, x, y, cv=skf)
	print "Scores using stratified 10-fold cv: %s" % cv_scores
	print "Accuracy: %0.2f (+/- %0.2f)" % (cv_scores.mean(), cv_scores.std() / 2)


# stuff below is pretty obsolete
##	# computes mean and std of the values of AD vs CON for each GI
##	with open("stats.txt", "w") as f:
##		f.write("TargetID\tmeanAD\tsdAD\tmeanCON\tsdCON\tdiff\n")
##		stats = []
##		for k,row in result.iteritems():
##			# each row corresponds to data from one GI
##			valuesAD = []
##			valuesCON = []
##			for (k,v) in row.iteritems():
##				if re.search("AD", k):
##					valuesAD.append(v)
##				elif re.search("CON", k):
##					valuesCON.append(v)
##			row_dict = dict()
##			row_dict["meanAD"] = getMean(valuesAD)
##			row_dict["sdAD"] = getSD(valuesAD)
##			row_dict["meanCON"] = getMean(valuesCON)
##			row_dict["sdCON"] = getSD(valuesCON)
##			row_dict["TargetID"] = row["TargetID"]
##			row_dict["diff"] = diff(valuesAD, valuesCON)
##			stats.append(row_dict)
##			f.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (row_dict["TargetID"],row_dict["meanAD"],row_dict["sdAD"],row_dict["meanCON"],row_dict["sdCON"],row_dict["diff"]))
##		print "computed stats for %s GIs" % len(stats)
##	f.close()



##	top = shrink(stats, size=20)
##	top_names = map(lambda x: x["TargetID"], top)
##	print top_names
##
##	lean_results = []
##	for k,row in result.iteritems():
##		if row["TargetID"] in top_names:
##			lean_results.append(row)
##	print "lean results contain %s results" % (len(lean_results))
##	# printing lean results into file
##	with open("output_lean.txt", "w") as f:
##		cols = sorted(lean_results[0].keys())  # this gives us column names in order
##		firstrow_string = ""
##		for col_name in cols:
##			firstrow_string = "%s\t%s" %(firstrow_string, col_name)  # concat column names to first line, tab separated
##		f.write("%s\n" % (firstrow_string.lstrip("\t")))  # stripping leading tab
##		for row in lean_results:
##			row_string = ""
##			for col_name in cols:
##				row_string = "%s\t%s" %(row_string, row[col_name].replace("NaN", "NaN"))
##			f.write("%s\n" %(row_string.lstrip("\t")))
##	f.close()

# This function loads the data into a ndarray from the .csv data file
def load_data(fnames=[]):
	data_file = csv.reader(open("skdata.csv"))
	temp = data_file.next()
	n_samples = int(temp[0])
	n_features = int(temp[1])
	target_names = np.array(temp[2:])
	data = np.empty((n_samples, n_features))
	target = np.empty((n_samples,), dtype=np.int)

	for i, ir in enumerate(data_file):
		data[i] = np.asarray(ir[:-1], dtype=np.float)
		target[i] = np.asarray(ir[-1], dtype=np.int)

	return Bunch(data=data, target=target,
				 target_names=target_names,
				 DESCR="big dataset",
				 feature_names=fnames)

def diff(v1, v2):
	mean1 = getMean(v1)
	sd1 = getSD(v1)
	mean2 = getMean(v2)
	sd2 = getSD(v2)
	return math.fabs(mean1-mean2)/((sd1+sd2)/2)

def getMean(v):
	floatv = toFloat(v)
	return (sum(floatv)/len(floatv))

def getSD(v):
	floatv = toFloat(v)
	mean = getMean(floatv)
	sd = math.sqrt(sum((x-mean)**2 for x in floatv)/len(floatv))
	return sd

def toFloat(v):
	temp = []
	for each in v:
		if not each == "NaN":
			temp.append(float(each))
	return temp

def shrink(d, size=3, key="diff"):
	s = sorted(d, key=lambda x: x[key])
	return s[-size:]


def main():
	run()

if __name__ == '__main__':
	main()
