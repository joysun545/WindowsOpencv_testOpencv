# 查找轮廓

import cv2
import numpy as np


def drawShape(src, points):
    i = 0
    while i < len(points):
        if (i == len(points) - 1):
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 2)
        else:
            x, y = points[i][0]
            x1, y1 = points[i + 1][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 2)
        i = i + 1


img = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\lightning.png")

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# 轮廓查找
# 共4种查找模式 RETR_EXTERNAL=0,RETR_LIST=1,RETR_CCOMP=2,RETR_TREE=3
# 两种保存模式 CHAIN_APPROX_SIMPLE(只保存角点），CHAIN_APPROX_NONE（保存所有轮廓上的点
contours, hicrarchy = cv2.findContours(binary, 3, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv2.drawContours(img, contours, 0, (0, 255, 255), 8)

# 计算面积
# area = cv2.contourArea(contours[0])
# print("area=%d" % (area))

# 计算周长
# len = cv2.arcLength(contours[0], True)
# print("len=%d" % (len))


# 多边形逼近
e = 20
approx = cv2.approxPolyDP(contours[0], e, True)
drawShape(img, approx)

# 凸包
hull = cv2.convexHull(contours[0])
drawShape(img, hull)

# 最小外接矩形
r = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(r)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# 最大外接矩形
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
