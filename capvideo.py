# 视频读取和保存

import cv2

# 创建VideoWriter为多媒体文件
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vw = cv2.VideoWriter("C:\\Users\\joysu\\Videos\\outputOpencv\\test01.mp4", fourcc, 30, (1920, 1080))

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)  # 视频窗口的指定长宽，必须配合上一行的WINDOW_NORMAL

# 从视频文件中读取视频帧
cap = cv2.VideoCapture(0)

# 判断摄像头是否打开
while cap.isOpened():
    # 从摄像头读视频
    ret, frame = cap.read()
    if ret ==True:
        # 将视频帧在窗口中显示
        cv2.imshow('video', frame)

        # 写数据到多媒体文件

        # 等待键盘事件，如果是Q，退出
        key = cv2.waitKey(1)  # 20是读取一帧的间隔时间，这个时间要和原视频帧率大致匹配，视频播放才流畅
        if key & 0xFF == ord('q'):
            break

    else:
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
