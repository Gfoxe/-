import numpy as np
import cv2
import pyautogui
from PIL import ImageGrab
import win32api
import time
screen_width, screen_height = 1920,1080 #监视区域分辨率
capture_width, capture_height = 1920,1080 #设置屏幕分辨率

x = screen_width / capture_width #比例计算 #test
y = screen_height / capture_height
xx = capture_width // screen_width
yy = capture_height // screen_height
xy = (capture_width*capture_height)/(screen_width*screen_height)

fourcc = cv2.VideoWriter_fourcc(*'XVID') #视频编码格式
out = cv2.VideoWriter('screen_capture.avi', fourcc, 20.0, (capture_width, capture_height)) #视频写入参数

#target_color = (48,163,93)

template = cv2.imread("item_recording_find_template_1.png") #读取对象图片
template1 = cv2.imread('Next.png')
nx,nt = template.shape[:2]

nxx = nx//2
ntt = nt//2

theight, twidth = template.shape[:2] #获取对象图片长宽
h, w = template.shape[:2] #获取对象图片长宽
template_resize = cv2.resize(template,(theight*xx,twidth*yy))
th,tw = template_resize.shape[:2]

h1,w1 = h//2,w//2 #比率计算

while True:
    # 获取屏幕截图
    screenshot = pyautogui.screenshot(region=(1,1,screen_width,screen_height))

    # 将截图转换为OpenCV图像
    frame1 = np.array(screenshot)

    # 调整捕获窗口的大小
    frame1 = cv2.resize(frame1, (capture_width, capture_height))
    
    res = cv2.matchTemplate(frame1, template_resize, cv2.TM_CCOEFF_NORMED) #查找目标
    threshold = 0.5 #拟合度
    loc = np.where(res >= threshold) #过滤
    coordinates = []
    for pt in zip(*loc[::-1]): #目标绘制框选
        cv2.rectangle(frame1, pt, (pt[0] + tw, pt[1] + th),(0,255,0), 1)
        coordinates.append((pt[0], pt[1]))
    
    #mouse = win32api.GetCursorPos()

    for coord in coordinates: #提取目标坐标
        x1 = int(coord[0]+h1)
        y1 = int(coord[1]+w1)
        print((x1),(y1)) #输出坐标
        pyautogui.moveTo((x1,y1))
        pyautogui.click()
        #pixel_color = screenshot.getpixel(x1,y1)

        

    # 将屏幕截图写入视频文件
    out.write(frame1)
    cv2.imshow('Screen Capture', frame1)
    
    # 按'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
