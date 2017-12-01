from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import random
from seededkmeans import *
from elm import *
from clusterassignment import *
from validitychecks import *
from morechecks import *

dataset=load_files("./preprocess/data", description=None, categories="alt", load_content=True, shuffle=False, encoding=None, decode_error='strict', random_state=0)

categories= list(dataset.target_names)

print("%d documents" % len(dataset.data))
print("%d categories" % len(dataset.target_names))
print(list(dataset.target_names))

num_categories=len(dataset.target_names)
orig_labels = dataset.target
orig_labels = map(lambda x: x + 1, orig_labels)

labels=list(orig_labels)
toRemove = random.sample(range(0,len(dataset.data)), int(0.9*len(dataset.data)));
for x in toRemove:
    labels[x]=0

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(dataset.data)


vectors=vectors.todense()
print("%d features " % vectors.shape[1])

elmvectors = elmMap(vectors,15400,'sigmoid')
print "Number of Hidden Neurons: 15400"
numberOfIterations=5
clusters,centroids= kmeans_iter(elmvectors.tolist(),labels,numberOfIterations)
cluster_labels=assign_clusters(clusters, labels)
moremeasures(clusters,elmvectors,centroids)
print elmvectors[0]

