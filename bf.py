# 暴力特征匹配
import cv2
import numpy as np

# 读取图片文件
img1 = cv2.imread("C:\\Users\\joysu\\Pictures\\testImg\\opencv-logo-white.png")
img2 = cv2.imread("C:\\Users\\joysu\\Pictures\\testImg\\opencv-logo.png")

# 灰度化
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 创建sift对象
sift = cv2.SIFT_create()

# 进行特征检测，计算特征点和扫描子
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# 创建匹配器 有四种描述子计算 NORM_L1、 NORM_L2、 HAMMING1、 HAMMING2 前两种适用于SIFT SURF,后两种适用于ORB
bf = cv2.BFMatcher(cv2.NORM_L1, True)

# 进行特征匹配
match = bf.match(des1, des2)

# 绘制匹配结果
img3 = cv2.drawMatches(img1, kp1, img2, kp2, match, None)

cv2.imshow('img3', img3)
cv2.waitKey(0)
