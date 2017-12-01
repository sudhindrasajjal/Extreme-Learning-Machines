import math

def moremeasures(clusters,vectors,centroids):#list of points in each cluster, the vectors, the cluster centroids
    sse=0
    ssb=0
    tss=0
    total=0
    c=[]
    for i in range(len(centroids[0])):
        x=0
        for j in range(len(centroids)):
            x=x+centroids[j][i]*(len(clusters[j]))

        for j in range(len(centroids)):
            total=total+len(clusters[j])
        x=x/total
        c.append(x)
    #print len(c)
    # print "overall f-measure"

    for i in range(len(centroids)):
        x=0
        for j in range(len(centroids[i])):
            x=x+( centroids[i][j] - c[j] )*( centroids[i][j] - c[j] )
        #print x*len(clusters[i])
        ssb=ssb+x*len(clusters[i])
        #print ssb
    print"The SSB for the clustering"
    print ssb

    vec=vectors.tolist()

    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            for k in range(len(c)):
                tss=tss + (vec[clusters[i][j]][k] - c[k])*(vec[clusters[i][j]][k] - c[k])
    print "The TSS for the clustering"
    print tss


    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            for k in range(len(c)):
                sse=sse + (vec[clusters[i][j]][k] - centroids[i][k])*(vec[clusters[i][j]][k] - centroids[i][k])
    print "The SSE for the clustering"
    print sse
