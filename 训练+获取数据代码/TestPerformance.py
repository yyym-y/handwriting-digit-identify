import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import time

# test performance

def GetInfo(Road):
    List = os.listdir(Road)
    Len = len(List)
    Label1 = np.zeros(Len)
    Sum = np.zeros(10)
    Info = np.zeros((Len, 1024))
    for i in range(Len):
        Path = Road + List[i]
        Label1[i] = int(List[i][0])
        Sum[int(Label1[i])] += 1
        fr = open(Path)
        for j in range(32):
            lineStr = fr.readline()
            for k in range(32):
                Info[i][j * 32 + k] = int(lineStr[j])
    return Info, Label1, Sum

def precision(correct, predict):
    total, right = len(correct), 0
    for i in range(total):
        if correct[i] == predict[i]:
            right += 1
    return right / total

def PaintEach(Sum1, Sum2, Sum3, num):
    global Begin
    plt.rcParams['font.sans-serif'] = ['SimHei']
    x = plt.figure(figsize=(10,5))
    x_label = [i for i in range(10)]
    a = x.add_subplot(111)
    for i in range(10):
        a.bar(x_label[i] - 0.2, Sum1[i], color="red", width=0.2, align="center")
        a.bar(x_label[i], Sum2[i], color="blue", width=0.2,align="center",alpha=0.5)
        a.bar(x_label[i] + 0.2, Sum3[i], color="green",align="center", width=0.2)
    a.bar([0],[0], color="red", label="实际个数")
    a.bar([0], [0], color="blue",alpha=0.5, label="被预测个数")
    a.bar([0], [0], color="green", label="正确个数")
    a.legend(loc='upper right')
    b = a.twinx()
    use = [Sum3[i] / Sum1[i] for i in range(10)]
    b.plot(x_label, use, label="准确率", color="black", linewidth=2
           ,marker='o',markersize='3',markeredgewidth=3)
    b.legend(loc='upper left')
    for i in range(10):
        plt.text(i - 0.2, use[i] + 0.0045, str(round(use[i],2)), fontsize=13)
    # plt.savefig(str(num) + '.png')
    plt.show()

def Paint(correct, predict, num):
    have = np.zeros(10)
    ac = np.zeros(10)
    right = np.zeros(10)
    for i in range(len(predict)):
        ac[int(correct[i])] += 1
        have[int(predict[i])] += 1
        if correct[i] == predict[i]:
            right[int(predict[i])] += 1
    PaintEach(ac, have, right, num)
def Precision(correct, predict):
    total, right = len(correct), 0
    for i in range(total):
        if correct[i] == predict[i]:
            right += 1
    return right / total



Begin = time.time()
TrainInfo, TrainLabel, TrainHave = GetInfo("./trainData/")
TestInfo, TestLabel, TestHave = GetInfo("./trainData/")
End1 = time.time()
print("read data cost %.5f second" % (End1 - Begin))
print(TrainHave)

def k_means(K):
    model = KNeighborsClassifier(n_neighbors=K)
    model.fit(TrainInfo, TrainLabel)
    return model.predict(TestInfo)

for i in range(4,5):
    Begin2 = time.time()
    List = k_means(i)
    End2 = time.time()
    print("the model which K is %d cost %.5f second" % (i, (End2 - Begin2)))
    print("A model with K of %d has an accuracy of %.5f" % (i, Precision(TestLabel, List)))
    print("")
    Paint(TestLabel, List, i)

