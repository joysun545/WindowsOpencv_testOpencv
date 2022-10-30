# FLANN 特征匹配
import cv2
import numpy as np

# 读取图片文件
img1 = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\opencv-test-01.png")
img2 = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\opencv-test-02.png")

# 灰度化
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 创建sift对象
sift = cv2.SIFT_create()

# 进行特征检测，计算特征点和扫描子
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# 创建匹配器 有四种描述子计算 NORM_L1、 NORM_L2、 HAMMING1、 HAMMING2 前两种适用于SIFT SURF,后两种适用于ORB
index_params = dict(algorithm=1, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# 进行特征匹配
matchs = flann.knnMatch(des1, des2, k=2)

good = []
for i, (m, n) in enumerate(matchs):
    if m.distance < 0.7 * n.distance:
        good.append(m)


if len(good) >= 4:

    srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    H, _ = cv2.findHomography(srcPts, dstPts, cv2.RANSAC, 5.0)

    h, w = img1.shape[:2]
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, H)

    cv2.polylines(img2, [np.int32(dst)], True, (0, 0, 255))
else:
    print('the number of good in less than 4.')
    exit()

# 绘制匹配结果
ret = cv2.drawMatchesKnn(img1, kp1, img2, kp2, [good], None)
cv2.imshow('result', ret)
cv2.waitKey(0)
