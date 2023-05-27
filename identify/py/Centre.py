from base64 import b64decode
from random import SystemRandom
import cv2
import numpy as np
import pickle
import sklearn


# function to form the file's name
def name(suffix):
    sys_random = SystemRandom()
    Have = "tdyifytrqze636875v9f7hnfhjgfjmhghyrdmngh" \
           "xdlxgjhxdiDCLCKDDLGJMHTDUJFDURUJXDKUJJCFHGRUZXLSQQWERTYUIOPASDFGHJKLZXCVBNM"
    Name = ""
    for i in range(1,32):
        Name = Name + sys_random.choice(Have)
    return Name + suffix


# funtion to decode Base64 into picture and save in roadPath
def decodeBase64(roadPath, lastName):
    with open("../data/tem/" + lastName + '.txt', 'rb') as f:
        image_base64 = f.read()
    imgdata = b64decode(image_base64)
    with open(roadPath + lastName + '.jpg','wb') as f:
        f.write(imgdata)

# to make the base64 legal
def clearBase64(put):
    head, content = put.split(",")
    content = content.replace(" ", "+")
    content = content.replace("%2F", "/")
    content = content.replace("%3D", "=")
    return content

# save the Base64 temporarily
def Write(put, lastName):
    put = clearBase64(put)
    with open("../data/tem/" + lastName + '.txt', 'w') as f:
        f.write(put)

# read the image's info and return with vector and image after operate
def readImg(Road):
    image = cv2.imread(Road, cv2.IMREAD_GRAYSCALE)
    down_width = 32
    down_height = 32
    down_points = (down_width, down_height)
    image = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)
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

# load the model
with open('K-means','rb') as f:
    model = pickle.load(f)

# predict the image
def run(lastName):
    decodeBase64("../data/Img/", lastName)
    Info, img = readImg("../data/Img/" + lastName + '.jpg')
    RE = Info
    Info = [Info]
    List = model.predict(Info)
    cv2.imwrite("../data/TEXT/Img/" + lastName + ".png", img)
    return "../data/TEXT/Img/" + lastName + ".png", str(List[0]), RE

# remember the file's name
LastName = name("")
Give, Road, Text, Label, Pic = [],[],[],[],[]

# order function
def middle(put):
    global LastName, Give, Road, Text, Label, Pic
    if put != "RUN":
        Road.clear(), Text.clear(), Label.clear()
        Tem = LastName
        LastName = name("")
        Write(put, Tem)
        Give.append(Tem)
        return {'url':"none"}
    else:
        for i in Give:
            getUrl, getLabel, getText = run(i)
            Road.append(getUrl), Text.append(getText), Label.append(getLabel)
        Give.clear()
        return {"url": Road, 'result':Label, 'text': Text}
