from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import random

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

from sklearn.metrics import silhouette_score, silhouette_samples

dataset=load_files("./preprocess/data", description=None, categories="alt,comp", load_content=True, shuffle=True, encoding=None, decode_error='strict', random_state=0)

categories= list(dataset.target_names)

num_categories=len(dataset.target_names)

orig_labels = dataset.target_names      # target_names => individual 'y' values for each of the documents : (In this case: 0(=>alt) through 6(=>soc))

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(dataset.data)

vectors=vectors.todense()
print("%d features " % vectors.shape[1])

"""
clusters= kmeans_iter(vectors.tolist(),labels,20)
cluster_labels=make_assumption(clusters, labels,num_categories)
"""
clusterer = KMeans(n_clusters=len(dataset.target_names))
cluster_labels = clusterer.fit_predict(vectors)

silhouette_avg = silhouette_score(vectors, cluster_labels)

# Compute the silhouette scores for each sample
sample_silhouette_values = silhouette_samples(vectors, cluster_labels)

print "The silhouette_avg is: ", 1-silhouette_avg

print "Silhoutte sample values: "
for i in range(len(dataset.target_names)):
    print i, " : ", sample_silhouette_values[cluster_labels==i]

