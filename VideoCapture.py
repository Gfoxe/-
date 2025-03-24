import numpy as np
import cv2
import pyautogui
#cap = cv2.VideoCapture(0)

down = 0
up = 500


Option = cv2.namedWindow('Option')

def setting(val):
    print(val)

cv2.createTrackbar('Config','Option',down,up,setting)


screen_width, screen_height = pyautogui.size()
capture_width, capture_height = 1440,900
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('screen_capture.avi', fourcc, 240.0, (capture_width, capture_height))

while True:
    # 获取屏幕截图
    screenshot = pyautogui.screenshot()
 
    # 将截图转换为OpenCV图像
    frame1 = np.array(screenshot)
 
    # 调整捕获窗口的大小
    frame1 = cv2.resize(frame1, (capture_width, capture_height))
 
    # 将屏幕截图写入视频文件
    out.write(frame1)


    Color = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

#    gauss = cv2.GaussianBlur(Color,(3,3),0)

 
    Canny_desktop = cv2.Canny(frame1,cv2.getTrackbarPos('Config','Option'),cv2.getTrackbarPos('Config','Option'))

    Output = cv2.bitwise_and(frame1,frame1,mask = Canny_desktop) 
    # 显示屏幕截图
#    uplight = np.power(Output,1.2)
    cv2.imshow('Screen Capture', Canny_desktop)
 
    # 按'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#调用摄像头
#while(cap.isOpened()):
#    ret, frame = cap.read()
#    detected_edges = cv2.GaussianBlur(frame,(3,3),0)
#
#    fix = cv2.Canny(detected_edges,0,200)
#
#    cv2.imshow('frame',fix)
#    c = cv2.waitKey(1)
#    if c==27: #ESC 键
#        break
#


    

cv2.destroyAllWindows()


