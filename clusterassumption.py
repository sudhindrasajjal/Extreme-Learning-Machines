def make_assumption(clusters, labels,num_categories):
    cluster_labels=[]
    for i in clusters:
        #determine maximum labelled data
        label_count=[None]*num_categories
        for j in label_count:
            j=0
        for j in i:
            if labels[j]!=0:
                label_count[labels[j]-1]+=1

        max_index=0
        max_count=max(label_count)
        for j in range(len(label_count)):
            if label_count[j]==max_count:
                max_index=j

        cluster_labels.append(max_index+1)
    return cluster_labels
