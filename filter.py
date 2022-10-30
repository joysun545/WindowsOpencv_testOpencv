# 卷积 均值滤波和高斯滤波

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\2015.jpg")

# #定义滤波盒
# kernel=np.ones((5,5),np.float32)/25
# dst=cv2.filter2D(img,-1,kernel)

# 直接调用 均值滤波API（blur） 和上面的效果一样
dst = cv2.blur(img, (5, 5))

# 直接调用 高斯滤波API（Gaussian Blur）（高斯噪音）
dst2 = cv2.GaussianBlur(img, (5, 5), sigmaX=1)

# 直接调用 中值滤波（胡椒噪音）
dst3 = cv2.medianBlur(img, 5)

# 直接调用双边滤波 (美颜)
dst4 = cv2.bilateralFilter(img, 7, 20, 50)

cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.imshow('img', img)
cv2.waitKey(0)
