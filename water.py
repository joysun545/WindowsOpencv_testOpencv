# 分水岭法 图片分割
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 打开图片
img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\sunFather.jpg")
# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
# 开运算
kernel = np.ones((3, 3), np.uint8)
open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 膨胀
bg = cv2.dilate(open, kernel, iterations=1)

# 获取前景物体
dist = cv2.distanceTransform(open, cv2.DIST_L2, 5)
ret, fg = cv2.threshold(dist, 0.7 * dist.max(), 255, cv2.THRESH_BINARY)

# 获取未知区域
fg = np.uint8(fg)
unknow = cv2.subtract(bg, fg)

# 创建连通域
ret, marker = cv2.connectedComponents(fg)

marker += 1
marker[unknow == 255] = 0

# 进行图像分割
result = cv2.watershed(img, marker)

img[result == -1] = [0, 0, 255]

cv2.imshow('unknow', unknow)

cv2.imshow("fg", fg)
cv2.imshow("bg", bg)
cv2.imshow('img', img)
cv2.waitKey()
