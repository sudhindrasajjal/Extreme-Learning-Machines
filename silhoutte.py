from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import random

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

from sklearn.metrics import silhouette_score, silhouette_samples

dataset=load_files("./preprocess/data", description=None, categories="alt,comp", load_content=True, shuffle=True, encoding=None, decode_error='strict', random_state=0)
# ,comp,misc,rec,sci,soc
# print dataset.data[0]
# print dataset.target[0:25]
# print dataset.target_names

categories= list(dataset.target_names)

# print("%d documents" % len(dataset.data))
# print("%d categories" % len(dataset.target_names))
# print(list(dataset.target_names))

num_categories=len(dataset.target_names)

orig_labels = dataset.target_names      # target_names => individual 'y' values for each of the documents : (In this case: 0(=>alt) through 6(=>soc))
# print orig_labels
# orig_labels = map(lambda x: x + 1, orig_labels) # Change it to 1 through 7.

# labels=list(orig_labels)


# toRemove = random.sample(range(0,len(dataset.data)), int(0.9*len(dataset.data)));
# for x in toRemove:
    # labels[x]=0

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(dataset.data)

# del toRemove
# del dataset
# gc.collect()

vectors=vectors.todense()
print("%d features " % vectors.shape[1])
# print vectors.shape[0]    # num of docs = len(dataset.data)

# print vectors[799,107]
# vectors=np.random.rand(500,5000)
# elmvectors = elmMap(vectors,20000,'sigmoid')
# gc.collect()

"""
clusters= kmeans_iter(vectors.tolist(),labels,20)
cluster_labels=make_assumption(clusters, labels,num_categories)
"""
# print dataset.target_names

# clusters = KMeans(n_clusters=2).fit(vectors[:0.9*len(vectors)]) #, dataset.target[:0.9*len(vectors)])
clusterer = KMeans(n_clusters=len(dataset.target_names))
cluster_labels = clusterer.fit_predict(vectors)

# The silhouette_score gives the average value for all the samples.
# This gives a perspective into the density and separation of the formed
# clusters

silhouette_avg = silhouette_score(vectors, cluster_labels)

# Compute the silhouette scores for each sample
sample_silhouette_values = silhouette_samples(vectors, cluster_labels)

print "The silhouette_avg is: ", 1-silhouette_avg

print "Silhoutte sample values: "
for i in range(len(dataset.target_names)):
    print i, " : ",                                                                                                                                                                                                                                                                                                                                                                                                                                                         sample_silhouette_values[cluster_labels==i]


# print sample_silhouette_values[cluster_labels == 0]
# print sample_silhouette_values[cluster_labels == 1]
# print sample_silhouette_values[cluster_labels == 2]
# print sample_silhouette_values[cluster_labels == 3]
# print sample_silhouette_values[cluster_labels == 4]
# print "KMeans done!"
# # print "Score: ", clusters.score(vectors[0.9*len(vectors):]) #, dataset.target[0.9*len(vectors):])

# print "Silhoutte score (total): ", silhouette_score(vectors, clusters.labels_)

# print "Silhoutte sample_scores: ", silhouette_samples(vectors[:10],clusters.labels_[:10])
