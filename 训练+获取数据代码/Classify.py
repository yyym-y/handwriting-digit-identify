import DataPre
import numpy as np
import time
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

Begin = time.time()

trainFeature, trainLabel = DataPre.getTrainFeature()
testFeature, Label2 = DataPre.getInputFeature("../data/Img", "../data/Text")
Label2 = [int(pr) for pr in Label2]
# KNN
def k_means(K):
    model = KNeighborsClassifier(n_neighbors=K)
    model.fit(trainFeature, trainLabel)
    return model
# Bayes
def Bayes():
    model = GaussianNB()
    model.fit(trainFeature, trainLabel)
    return model.predict(testFeature)
# Tree
def Tree():
    dtc = DecisionTreeClassifier()
    dtc.fit(trainFeature, trainLabel)
    return dtc.predict(testFeature)
def precision(correct, predict):
    total, right = len(correct), 0
    for i in range(total):
        if correct[i] == predict[i]:
            right += 1
    return right / total
def SVC_():
    model = SVC(kernel="linear")
    model.fit(trainFeature, trainLabel)
    return model.predict(testFeature)

List = k_means(4)
print(List)
print(precision(Label2, List))

End = time.time()
print(End - Begin)

# k_means(4)

