import os
import cv2

# Change image into .txt
def readImg(Road):
    image = cv2.imread(Road, cv2.IMREAD_GRAYSCALE)
    down_width = 32
    down_height = 32
    down_points = (down_width, down_height)
    image = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)
    Info = []
    for i in range(32):
        for j in range(32):
            if image[i][j] >= 127:
                Info.append(1)
            else:
                Info.append(0)
    return Info

def writeInfo(imgRoad, fileRoad):
    ff = open(fileRoad, 'w')
    index = 0
    Info = readImg(imgRoad)
    # print(Info)
    for pr in Info:
        ff.write(str(pr))
        index += 1
        if index == 32:
            index = 0
            ff.write("\n")

Road = "./train/"
List = os.listdir(Road)
i = 9
path = Road + List[i] + "/"
L = os.listdir(path)
# print(L)
for j in L:
    fileRoad = "./trainInfo/" + List[i] + "_" + j.split('.')[0] + ".txt"
    imgRoad = path + j
    # print(imgRoad)
    writeInfo(imgRoad, fileRoad)

print(List)