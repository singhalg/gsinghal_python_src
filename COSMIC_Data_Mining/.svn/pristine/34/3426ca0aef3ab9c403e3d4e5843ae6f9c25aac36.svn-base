# Copyright 2012 Colin McDonough (cmcdonough@wustl.edu)

from module2_GS import *
from sklearn.decomposition import KernelPCA
from sklearn.decomposition import PCA
from sklearn.decomposition import SparsePCA
from sklearn.decomposition import RandomizedPCA
from sklearn.externals import joblib

X = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')
random_pca_data = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')
pca_data = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')
sparse_pca_data = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')
kernel_pca_data = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')

random_pca = RandomizedPCA(n_components=50)
random_pca_model = random_pca.fit(random_pca_data)
random_X_new = random_pca.fit_transform(X)
print 'random_pca explained', random_pca.explained_variance_ratio_
print 'random_pca explained sum', sum(random_pca.explained_variance_ratio_)
joblib.dump(random_pca_model, 'random_pca_model.pkl')
joblib.dump(random_pca.explained_variance_ratio_, 'random_pca.explained_variance_ratio_.pkl')
joblib.dump(random_X_new, 'random_X_new.pkl')

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
