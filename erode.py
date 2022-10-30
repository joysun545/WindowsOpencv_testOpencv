# 图片形态学 腐蚀和膨胀 开运算和闭运算

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\sunFather.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, img2 = cv2.threshold(img1, 90, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)  # 自定义卷积核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 调用API卷积核（ELLIPSE椭圆,RECT矩形,CROSS十字)

# 腐蚀
img3 = cv2.erode(img2, kernel, iterations=1)

# 膨胀
img4 = cv2.dilate(img2, kernel, iterations=1)

# 开运算、闭运算、梯度运算、顶帽运算和黑帽运算的API相同，
# 第二个参数不一样，分别是v2.MORPH_OPEN、v2.MORPH_CLOSE、cv2.MORPH_GRADIENT、cv2.MORPH_TOPHAT、cv2.MORPH_BLACKHAT

# 开运算 服饰后在膨胀
img5 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
# 闭运算 膨胀后再腐蚀
img6 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)
# 梯度运算 原图减腐蚀
img7 = cv2.morphologyEx(img2, cv2.MORPH_GRADIENT, kernel)
# 顶帽运算 原图减开运算
img8 = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, kernel)

# 黑帽运算 原图减闭运算
img9 = cv2.morphologyEx(img2, cv2.MORPH_BLACKHAT, kernel)

# cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.imshow('img5', img5)
cv2.imshow('img6', img6)
cv2.imshow('img7', img7)
cv2.imshow('img8', img8)
cv2.imshow('img9', img9)

cv2.waitKey(0)
