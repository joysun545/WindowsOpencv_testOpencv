# haar haarcascade_russian_plate_number.xml车牌识别

import cv2
import numpy as np

import pytesseract

# 第一步，创建HAAR级联器
plate = cv2.CascadeClassifier('C:\\opencv\\sources\\data\\haarcascades\\haarcascade_russian_plate_number.xml')

# 第二步，导入车牌图片并灰度化
img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\carplate02.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 第三步、进行人脸识别
plates = plate.detectMultiScale(gray, 1.1, 3)
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# 对获取的车牌进行预处理
# 1提取roi
roi = gray[y:y + h, x:x + w]
# 2二值化处理
ret, roi_bin = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print(pytesseract.image_to_string(roi, lang='chi_sim+eng', config='--psm 8 --oem 3'))

cv2.imshow('img', img)
cv2.imshow('roi_bin', roi_bin)
cv2.waitKey()
