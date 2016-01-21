import math
import numpy as np
import random

# def eudist(A,B):
#     distance=0
#     for i in range(len(A)):
#         distance +=(A[i]-B[i])*(A[i]-B[i])
#     return math.sqrt(distance)

def updatelabels(data,centroids):
    cluster_list=[];
    for i in centroids:
        cluster_list.append([])
    for i in range(len(data)):
        mini=10000000
        n=0
        for j in range(len(centroids)):
            # m=eudist(data[i],centroids[j])
            distance=0
            for k in range(len(data[i])):
                distance +=(data[i][k]-centroids[j][k])*(data[i][k]-centroids[j][k])
            m= math.sqrt(distance)

            if(m<mini):
                mini=m
                n=j
        cluster_list[n].append(i)
    return cluster_list


def calculatecentroids(data,cluster_list):
    new_centroids=[]
    for i in range(len(cluster_list)):
        point=[]
        for k in range(len(data[1])):
            summation=0
            for j in cluster_list[i]:
                summation += data[j][k]
            if(len(cluster_list[i])!=0):
                updated_centers = summation/float(len(cluster_list[i]))
                point.append(updated_centers)
            else:
                point.append(0)
        new_centroids.append(point)
    return new_centroids


def kmeans_iter(data,labels,num_iter):
    label_counts=[]
    for i in labels:
        if(i not in label_counts):
            label_counts.append(i)
    label_counts.sort()

    cluster_list=[]
    for i in label_counts:
        if i!=0:
            cluster_list.append([])

    for i in label_counts:
        for j in range(len(labels)):
            if labels[j]==i and labels[j]!=0:
                cluster_list[i-1].append(j)

    for i in range(num_iter):
        centroids= calculatecentroids(data, cluster_list)
        cluster_list=updatelabels(data, centroids)
        print "iteration complete"
    return cluster_list,centroids
