def assign_clusters(clusters, labels):
    label_freq_matrix=[]
    for i in clusters:
        #determine maximum labelled data
        # label_count=[None]*len(clusters)
        label_count=[]
        for j in range(len(clusters)):
            label_count.append(0)
        for j in i:
            if labels[j]!=0:
                label_count[labels[j]-1]+=1
        label_freq_matrix.append(label_count)
    cluster_labels=[]

    # print label_freq_matrix

    for i in range(len(clusters)):
        maximum_index=0
        maximum_index_value=0
        for j in range(len(clusters)):
            if j in cluster_labels :
                continue
            else:
                if label_freq_matrix[j][i]>=maximum_index_value:
                        maximum_index_value=label_freq_matrix[j][i]
                        maximum_index=j
        cluster_labels.append(maximum_index)

    for i in cluster_labels:
        i+=1
    return cluster_labels
