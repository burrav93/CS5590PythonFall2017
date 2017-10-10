import pandas
import matplotlib.pyplot as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

variables=pandas.read_csv('Customers.csv')
Y=variables[['Annual Income']]
X=variables[['Spending Score']]

Nc=range(1,20)
kmeans=[KMeans(n_clusters=i) for i in Nc]
score=[kmeans[i].fit(Y).score(Y)for i in range(len(kmeans))]
pl.plot(Nc,score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.show()

pca=PCA(n_components=1).fit(Y)
pca_d=pca.transform(Y)
pca_c=pca.transform(X)


kmeans=KMeans(n_clusters=5)

kmeansoutput=kmeans.fit(Y)


pl.figure('5 Cluster K-Means')

pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)

pl.xlabel('Annual Income')

pl.ylabel('Spending Score')

pl.title('5 Cluster K-Means')

pl.show()
