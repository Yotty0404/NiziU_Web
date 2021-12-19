import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import sys
from keras.models import load_model

def detect_face(root_path, image):
    model = load_model(os.path.join(root_path, 'static/models/','my_model'))
    image = cv2.imdecode(image, 1)
    if image is None:
        print("Not open:")
        return False

    b,g,r = cv2.split(image)
    image = cv2.merge([r,g,b])

    #opencvを使って顔抽出
    image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(os.path.join(root_path, 'static/models/','haarcascade_frontalface_alt.xml'))

    # 顔認識の実行
    face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=2,minSize=(64,64))
    #顔が１つ以上検出された時
    if len(face_list) > 0:
        for rect in face_list:
            x,y,width,height = rect
            cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (255, 0, 0), thickness=3)
            img = image[rect[1]:rect[1] + rect[3],rect[0]:rect[0] + rect[2]]
            if image.shape[0] < 64:
                print("too small")
                continue
            img = cv2.resize(image,(64,64))
            img = np.expand_dims(img,axis=0)

            predict = model.predict(img)
            members = ['Mako', 'Rio', 'Maya', 'Riku', 'Ayaka', 'Mayuka', 'Rima', 'Miihi', 'Nina']

            dic = {}
            for i in range(len(members)):
                dic[i] = predict[0][i]

            dic = sorted(dic.items(), reverse=True, key=lambda x : x[1])

            data = []
            for i in range(3):
                name = members[dic[i][0]]
                percentage = round(dic[i][1] * 100, 1)

                data.append([name, f'{percentage}%'])

    #顔が検出されなかった時
    else:
        print("no face")
        return False
    return data

if __name__ == '__main__':
    model = load_model('./my_model.h5')
    image = cv2.imread("C:/Users/tyuke/Desktop/maya.jpg")
    if image is None:
        print("Not open:")
    b,g,r = cv2.split(image)
    image = cv2.merge([r,g,b])
    whoImage = detect_face(image)

    plt.imshow(whoImage)
    plt.show()