# 图片拼接

import cv2
import numpy as np


def stitch_image(img1, img2, H):
    # 1.获得图像的四个角点
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    img1_dims = np.float32([[0, 0], [0, h1], [w1, h1], [w1, 0]]).reshape(-1, 1, 2)
    img2_dims = np.float32([[0, 0], [0, h2], [w2, h2], [w2, 0]]).reshape(-1, 1, 2)
    print(img1_dims)
    print(img2_dims)
    # 2.对图片进行变换
    img1_transform = cv2.perspectiveTransform(img1_dims, H)
    print(img1_transform)

    result_dims = np.concatenate((img2_dims, img1_transform), axis=0)
    print(result_dims)
    # 3.创建一张大图，将两张图拼接在一起
    # 输出结果
    [x_min, y_min] = np.int32(result_dims.min(axis=0).ravel() - 0.5)
    [x_max, y_max] = np.int32(result_dims.max(axis=0).ravel() + 0.5)

    # 平移距离
    transform_dist = [-x_min, -y_min]
    print(transform_dist)

    transform_array = np.array([[1, 0, transform_dist[0]], [0, 1, transform_dist[1]], [0, 0, 1]])
    print(transform_array)

    result_img = cv2.warpPerspective(img1, transform_array.dot(H), (x_max - x_min, y_max - y_min))

    # result_img[transform_dist[1]:transform_dist[1] + h2, transform_dist[0]:transform_dist[0] + w2] = img2

    return result_img


def get_homo(img1, img2):
    # 1.创建特征转换对象
    sift = cv2.SIFT_create()

    # 2.通过特征转换对象获得特征点和描述子
    k1, d1 = sift.detectAndCompute(img1, None)
    k2, d2 = sift.detectAndCompute(img2, None)

    # 3.创建特征匹配器
    bf = cv2.BFMatcher()

    # 4.进行特征匹配
    matches = bf.knnMatch(d1, d2, k=2)

    # 5.过滤特征，找出有效的特征匹配点
    verify_matches = []
    verify_ratio = 0.8
    for m1, m2 in matches:
        if m1.distance < verify_ratio * m2.distance:
            verify_matches.append(m1)

    min_matches = 8
    if len(verify_matches) > min_matches:

        img1_pts = []
        img2_pts = []
        for m in verify_matches:
            img1_pts.append(k1[m.queryIdx].pt)
            img2_pts.append(k2[m.queryIdx].pt)

        img1_pts = np.float32(img1_pts).reshape(-1, 1, 2)
        img2_pts = np.float32(img2_pts).reshape(-1, 1, 2)
        H, mask = cv2.findHomography(img1_pts, img2_pts)
        return H
    else:
        print('err:Not enough matches!')
        exit()


# # 拼接并输出最终结果

# 读取图片文件
img1 = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\test01.png")
img2 = cv2.imread("C:\\Users\\joysu\\Pictures\\inputOpencv\\test02.png")

# 重设两张图片的大小600x420
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))

inputs=np.hstack((img1,img2))

# 找特征点，描述子，计算单应性矩阵
H = get_homo(img1, img2)

# 根据单应性矩阵对图像进行交换，然后平移
result_image = stitch_image(img1, img2, H)

cv2.imshow('inputs img', inputs)
cv2.imshow('input img', result_image)
cv2.waitKey()
