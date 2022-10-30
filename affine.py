# 变换矩阵

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\1.jpg")
h, w, c = img.shape

# 500表示x轴正向平移500，300表示y轴负向(向下)平移300
M=np.float32([[1,0,50],[0,1,50]])
new = cv2.warpAffine(img, M, (w, h))

# (100,100)表示旋转中心，15表示选装的逆时针方向的角度， 1.0表示缩放倍数
M2 = cv2.getRotationMatrix2D((w/2, h/2), 20, 0.5)
new2 = cv2.warpAffine(new, M2, (w, h))

# 通过指定点集坐标的变换改变图片属性 左上 右上 左下 右下
src=np.float32([[100,100],[300,100],[100,400]])
dst=np.float32([[70,150],[200,200],[80,450]])
M3=cv2.getAffineTransform(src,dst)
new3 = cv2.warpAffine(img, M3, (w, h))

cv2.imshow('img', img)
cv2.imshow('new', new)
cv2.imshow('new2', new2)
cv2.imshow('new3', new3)

cv2.waitKey(0)
