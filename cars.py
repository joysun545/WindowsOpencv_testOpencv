#车辆识别并计数

import cv2
import numpy as np

min_w = 90
min_h = 150
line_height = 200
cars = []
offset = 6
carno = 0


def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1

    return cx, cy


cap = cv2.VideoCapture("C:\\Users\\joysu\\Videos\\inputOpencv\\zl.mp4")
bgsubmog = cv2.createBackgroundSubtractorMOG2()  # 去除背景
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

while True:
    ret, frame = cap.read()
    if ret == True:
        # 灰度
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 去噪
        blur = cv2.GaussianBlur(frame, (3, 3), 5)
        # 去背影
        mask = bgsubmog.apply(frame)
        # 腐蚀
        erode = cv2.erode(mask, kernel)
        # 膨胀
        dilate = cv2.dilate(erode, kernel, iterations=2)
        # 闭操作
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
        # 查找轮廓
        cnts, h = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.line(frame, (10, line_height), (950, line_height), (255, 255, 0), 3)

        for i, c in enumerate(cnts):
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            isValid = (w >= min_w) and (h >= min_h)
            if not isValid:
                continue

            cpoint = center(x, y, w, h)
            cars.append(cpoint)

            for x, y in cars:
                if y < line_height + offset and y > line_height - offset:
                    carno = +1
                    print(carno)
                    cars.remove((x, y))

        cv2.putText(frame,"Cars Count:"+str(carno),(300,60),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
        cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
