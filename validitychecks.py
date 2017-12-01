def measures(clusters,cluster_labels, labels):
    f1=[]
    accuracy=[]
    for i in range(len(clusters)):
        tp=0
        total_correct=0
        for j in range(len(clusters[i])):
                if labels[clusters[i][j]]-1==cluster_labels[i]:
                    tp+=1

        for j in labels:
            if j-1==cluster_labels[i]:
                total_correct+=1
        tn=len(labels)-len(clusters[i])-(total_correct-tp)
        p=(float(tp))/len(clusters[i])
        r=(float(tp))/total_correct
        f=2*((p*r)/(p+r))
        a=(float(tp+tn))/len(labels)
        accuracy.append(a)
        f1.append(f)
    print "f-measure:"
    print f1
    print "Accuracy:"
    print accuracy
