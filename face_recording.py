import numpy as np
import cv2
import pyautogui
screen_width, screen_height = pyautogui.size()
capture_width, capture_height = 1920,1080

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('screen_capture.avi', fourcc, 20.0, (capture_width, capture_height))

while True:
    # 获取屏幕截图
    screenshot = pyautogui.screenshot()
 
    # 将截图转换为OpenCV图像
    frame1 = np.array(screenshot)
 
    # 调整捕获窗口的大小
    frame1 = cv2.resize(frame1, (capture_width, capture_height))
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)   # 將圖片轉成灰階

    face_cascade = cv2.CascadeClassifier("D:\VSC_project\OpenCV\sources\data\haarcascades\haarcascade_fullbody.xml")   # 載入人臉模型
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)    # 偵測人臉

    for (x, y, w, h) in faces:
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)    # 利用 for 迴圈，抓取每個人臉屬性，繪製方框
        #mosaic = frame1[y:y+h, x:x+w]   # 馬賽克區域
        #level = 15                   # 馬賽克程度
        #mh = int(h/level)            # 根據馬賽克程度縮小的高度
        #mw = int(w/level)            # 根據馬賽克程度縮小的寬度
        #mosaic = cv2.resize(mosaic, (mw,mh), interpolation=cv2.INTER_LINEAR) # 先縮小
        #mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_NEAREST)  # 然後放大
        #frame1[y:y+h, x:x+w] = mosaic   # 將指定區域換成馬賽克區域

    # 将屏幕截图写入视频文件
    out.write(frame1)
    cv2.imshow('Screen Capture', frame1)
 
    # 按'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        
cap.release()
cv2.destroyAllWindows()
