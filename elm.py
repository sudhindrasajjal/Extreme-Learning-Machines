
import numpy as np
import random

def elmMap(X,NumberofHiddenNeurons,ActivationFunction):
    NumberofTrainingData=X.shape[0]
    NumberofInputNeurons=X.shape[1]
    X=X.T
    InputWeight=np.random.rand(NumberofHiddenNeurons,NumberofInputNeurons)*2-1
    tempH=np.dot(InputWeight,X)
    ind=np.ones([NumberofHiddenNeurons,NumberofTrainingData-1])
    BiasofHiddenNeurons=np.random.rand(NumberofHiddenNeurons,1)
    BiasMatrix=np.concatenate((BiasofHiddenNeurons,ind), axis=1)
    tempH=tempH+BiasMatrix
    if ActivationFunction=='sigmoid':
        mapresult = 1.0 / (1.0 + np.exp(-tempH))
    if ActivationFunction=='sin':
        mapresult = np.sin(tempH);
    if ActivationFunction=='radbas':
        mapresult = np.exp(-tempH**2);
    mapresult=mapresult.T

    return mapresult;
