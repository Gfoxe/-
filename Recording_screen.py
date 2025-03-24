import numpy as np
import cv2
import pyautogui
screen_width, screen_height = pyautogui.size()
capture_width, capture_height = 1920,1080
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
    cv2.imshow('Screen Capture', frame1)
 
    # 按'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

        

cv2.destroyAllWindows()
