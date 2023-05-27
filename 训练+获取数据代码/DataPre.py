import numpy as np
import os
import cv2


# query specific single .txt info and return a vector that conclude zero or one
def queryData(filepath):
    returnVec = []
    fr = open(filepath)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVec.append(int(lineStr[j]))
    return returnVec


# give a root that conclude all train datas
# return two vectors, one is two-dimensional vector, another is one-dimensional vector
# two-dimensional vector conclude all data's feature and another is all data's label
def queryInfo(Road):
    trainingFileList = os.listdir(Road)
    fileLen = len(trainingFileList)
    returnFeature = np.zeros((fileLen, 1024))
    for i in range(fileLen):
        path = Road + "/" + trainingFileList[i]
        returnFeature[i] = queryData(path)
    # query all data's label
    Label = np.zeros(fileLen, int)
    Count = np.zeros(10)
    for i in range(fileLen):
        Str = trainingFileList[i]
        Label[i] = int(Str[0])
        Count[int(Str[0])] += 1
    # print(Count)
    return returnFeature, Label


# function to get the training data and label
def getTrainFeature():
    Road = '../data/trainData'
    return queryInfo(Road)


# function to read an image and change to a vector that conclude zero and one
# the input form must indicate the image not it's root
# the function will return the feature vector
def readImg(Road):
    image = cv2.imread(Road, cv2.IMREAD_GRAYSCALE)
    down_width = 32
    down_height = 32
    down_points = (down_width, down_height)
    image = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)
    # cv2.imshow('Contours', image)
    # cv2.waitKey(0)
    _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    Use = cv2.Canny(image, 10,10)
    cv2.drawContours(image, contours,-1, (0, 255, 0), 2)
    Info = []
    img = np.zeros((32,32))
    for i in range(32):
        for j in range(32):
            if image[i][j] >= 127:
                Info.append(0)
                img[i][j] = 0
            else:
                Info.append(1)
                img[i][j] = 255
    for i in range(32):
        for j in range(32):
            if Use[i][j] == 255:
                Info[i * 32 + j] = 1
                img[i][j] = 255
    for i in range(32):
        for j in range(32):
            if i == 1 or i == 0 or i == 31 or i == 30:
                Info[i*32 + j] = 0
                img[i][j] = 0
            if j == 1 or j == 0 or j == 31 or j == 30:
                Info[i*32 + j] = 0
                img[i][j] = 0
    return Info, img



# the function to save the victor
# change lines every 32 numbers
# to use the function, you must input the specific img road and the save file road(include file name)
def writeInfo(imgRoad, fileRoad, img):
    ff = open(fileRoad, 'w')
    for i in range(32):
        for j in range(32):
            ff.write(str(int(img[i][j])))
        ff.write("\n")
    cv2.imwrite(imgRoad, img)


# this function will read all img in one folder
# It will save it as .txt form and return a two-dimensional vector conclude feature
def getInputFeature(imgRoot, digRoot):
    imgList = os.listdir(imgRoot)
    Len = len(imgList)
    Info = np.zeros((Len, 1024))
    Label2 = []
    for i in range(Len):
        Info[i], img = readImg(imgRoot + "/" + imgList[i])
        writeInfo(digRoot + "/Img/" + imgList[i].split('.')[0] + '.jpg',
                  digRoot + "/" + imgList[i].split('.')[0] + '.txt', img)
        Label2.append(imgList[i].split('.')[0].split('-')[0])
    return Info, Label2


def Strength(imgRoad):
    image = cv2.imread(imgRoad, cv2.IMREAD_GRAYSCALE)
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    cv2.imshow('Contours',image)
    cv2.waitKey(0)
