import cv2
import numpy as np

blockSize = 2
ksize = 3
k = 0.04

maxCorners = 1000
ql = 0.01
minDistance = 10

img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\chessboard.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# harris角点检测
dst = cv2.cornerHarris(gray, blockSize, ksize, k)

# Shi-Tomasi角点检测
dst2 = cv2.goodFeaturesToTrack(gray, maxCorners, ql, minDistance)
dst2 = np.int0(dst2)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

for i in dst2:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

cv2.imshow('harris', img)
cv2.waitKey(0)
