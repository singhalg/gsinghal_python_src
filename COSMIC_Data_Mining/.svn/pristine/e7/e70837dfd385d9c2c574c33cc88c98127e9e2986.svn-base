# Copyright 2012 Colin McDonough (cmcdonough@wustl.edu)

from module2_GS import *
from sklearn.decomposition import KernelPCA
from sklearn.decomposition import PCA
from sklearn.decomposition import SparsePCA
from sklearn.decomposition import RandomizedPCA
from sklearn.externals import joblib

X = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')
random_pca_data_50 = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')
random_pca_data_25 = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')
random_pca_data_10 = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')
pca_data = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')
sparse_pca_data = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')
kernel_pca_data = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')

random_pca_50 = RandomizedPCA(n_components=50)
random_pca_model_50 = random_pca_50.fit(random_pca_data_50)
random_X_new_50 = random_pca_50.fit_transform(X)
print 'random_pca_50 explained', random_pca_50.explained_variance_ratio_
print 'random_pca_50 explained sum', sum(random_pca_50.explained_variance_ratio_)
joblib.dump(random_pca_model_50, 'random_pca_model_50.pkl')
joblib.dump(random_pca_50.explained_variance_ratio_, 'random_pca_50.explained_variance_ratio_.pkl')
joblib.dump(random_X_new_50, 'random_X_new_50.pkl')

random_pca_25 = RandomizedPCA(n_components=25)
random_pca_model_25 = random_pca_25.fit(random_pca_data_25)
random_X_new_25 = random_pca_25.fit_transform(X)
print 'random_pca_25 explained', random_pca_25.explained_variance_ratio_
print 'random_pca_25 explained sum', sum(random_pca_25.explained_variance_ratio_)
joblib.dump(random_pca_model_25, 'random_pca_model_25.pkl')
joblib.dump(random_pca_25.explained_variance_ratio_, 'random_pca_25.explained_variance_ratio_.pkl')
joblib.dump(random_X_new_25, 'random_X_new_25.pkl')

random_pca_10 = RandomizedPCA(n_components=10)
random_pca_model_10 = random_pca_10.fit(random_pca_data_10)
random_X_new_10 = random_pca_10.fit_transform(X)
print 'random_pca_10 explained', random_pca_10.explained_variance_ratio_
print 'random_pca_10 explained sum', sum(random_pca_10.explained_variance_ratio_)
joblib.dump(random_pca_model_10, 'random_pca_model_10.pkl')
joblib.dump(random_pca_10.explained_variance_ratio_, 'random_pca_10.explained_variance_ratio_.pkl')
joblib.dump(random_X_new_10, 'random_X_new_10.pkl')

pca = PCA(n_components=50)
pca_model = pca.fit(pca_data)
pca_X_new = pca.fit_transform(X)
print 'pca explained', pca.explained_variance_ratio_
print 'pca explained sum', sum(pca.explained_variance_ratio_)
joblib.dump(pca_model, 'pca_model.pkl')
joblib.dump(pca_X_new, 'pca_X_new.pkl')
print pca_model

sparse_pca = SparsePCA(n_components=50)
sparse_pca_model = pca.fit(sparse_pca_data)
sparse_pca_X_new = pca.fit_transform(X)
joblib.dump(sparse_pca_model, 'sparse_pca_model.pkl')
joblib.dump(sparse_pca_X_new, 'sparse_pca_X_new.pkl')
print sparse_pca_model

kernel_pca = KernelPCA(n_components=50)
kernel_pca_model = kernel_pca.fit(kernel_pca_data)
kernel_X_new = kernel_pca.fit_transform(X)
joblib.dump(kernel_pca_model, 'kernel_pca_model.pkl')
joblib.dump(kernel_X_new, 'kernel_X_new.pkl')
