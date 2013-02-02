# Copyright 2012 Colin McDonough (cmcdonough@wustl.edu)

from module2_GS import *
from sklearn.decomposition import RandomizedPCA
from sklearn.decomposition import PCA
from sklearn.externals import joblib

random_pca_data = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')
pca_data = normalization('gene_IndividualsArr.pkl', 'top10Genes_Indiv.pkl')

random_pca = RandomizedPCA(n_components=50)
random_pca_model = random_pca.fit(random_pca_data)
print 'random_pca explained', random_pca.explained_variance_ratio_
print 'random_pca explained sum', sum(random_pca.explained_variance_ratio_)
joblib.dump(random_pca_model, 'random_pca_model')

pca = PCA(n_components=50)
pca_model = pca.fit(pca_data)
print 'pca explained', pca.explained_variance_ratio_
print pca_model
