# 三种特征检测方法 SIFT SURF ORB 准确性按顺序递减，运算速度反之
import cv2
import numpy as np

# 读取文件
img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\lightning.png")
# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建SIFT对象
# sift = cv2.SIFT_create()

# 创建SURF对象
# surf = cv2.SURF_create()

# 创建ORB对象
orb = cv2.ORB_create()
# 进行检测
# kp, des = sift.detectAndCompute(gray, None)
# kp, des = surf.detectAndCompute(gray, None)
kp, des = orb.detectAndCompute(gray, None)

# 绘制keypoints
cv2.drawKeypoints(gray, kp, img)

cv2.imshow('img', img)
cv2.waitKey(0)
