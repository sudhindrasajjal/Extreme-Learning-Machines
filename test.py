from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import random
from seededkmeans import *
# from clusterassumption import *
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

# print "Number of Iterations = 5"
# for hiddenNeurons in range(15400,17001, 200):
#     print("Number of Hidden Neurons: %d" % hiddenNeurons)
#     elmvectors = elmMap(vectors,hiddenNeurons,'sigmoid')
#     print "Without ELM"
#     clusters= kmeans_iter(vectors.tolist(),labels,5)
#     cluster_labels=assign_clusters(clusters, labels)
#     # print cluster_labels
#     measures(clusters,cluster_labels, orig_labels)

#     # cluster_labels=make_assumption(clusters, labels,num_categories)
#     print "With ELM"
#     clusters= kmeans_iter(elmvectors.tolist(),labels,5)
#     cluster_labels=assign_clusters(clusters, labels)
#     # print cluster_labels
#     measures(clusters,cluster_labels, orig_labels)
#     print " "

elmvectors = elmMap(vectors,15400,'sigmoid')
# for numberOfIterations in range(5, 11):
#     print("Number of Iterations: %d" % numberOfIterations)
print "Number of Hidden Neurons: 15400"
    # print "Without ELM"
numberOfIterations=5
clusters,centroids= kmeans_iter(elmvectors.tolist(),labels,numberOfIterations)
cluster_labels=assign_clusters(clusters, labels)
#print len(centroids[0])
moremeasures(clusters,elmvectors,centroids)
print elmvectors[0]

#print len(centroids[0])
#print vectors.tolist()[1][1]  just checking the vector structure
# print cluster_labels
#measures(clusters,cluster_labels, orig_labels)

# cluster_labels=make_assumption(clusters, labels,num_categories)
# print "With ELM"
# clusters= kmeans_iter(elmvectors.tolist(),labels,numberOfIterations)
# cluster_labels=assign_clusters(clusters, labels)
# # print cluster_labels
# measures(clusters,cluster_labels, orig_labels)
# print " "
