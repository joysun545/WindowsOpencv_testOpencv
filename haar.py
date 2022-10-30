# haar人脸识别

import cv2
import numpy as np

# 第一步，创建HAAR级联器
facer = cv2.CascadeClassifier('C:\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
eyer = cv2.CascadeClassifier('C:\\opencv\\sources\\data\\haarcascades\\haarcascade_eye.xml')

# 第二步，导入人脸识别图片并灰度化
img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\test02.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 第三步、进行人脸识别
faces = facer.detectMultiScale(gray, 1.1, 3)
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    roi_img = img[y:y + h, x:x + w]

    eyes = eyer.detectMultiScale(roi_img, 1.1, 3)
    for x, y, w, h in eyes:
        cv2.rectangle(roi_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    i = i + 1
    winname = 'face' + str(i)
    cv2.imshow(winname, roi_img)
cv2.waitKey()
