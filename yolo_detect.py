from ultralytics import YOLO
import cv2
import numpy as np
import win32api
import win32con
import time
import ctypes
import pyautogui
from PIL import ImageGrab
MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA

num = 32

def keydownup():

    time.sleep(0.1)
    win32api.keybd_event(num, MapVirtualKey(num, 0), 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(num, MapVirtualKey(num, 0), win32con.KEYEVENTF_KEYUP, 0)

screen_width, screen_height = pyautogui.size()
capture_width, capture_height = 1920,1080

model = YOLO("yolov8x.pt")


#model(img,show=True)
def detect():
    # 获取屏幕截图
    #screenshot = pyautogui.screenshot()
 
    # 将截图转换为OpenCV图像
    #frame1 = np.array(screenshot)
    frame1 = ImageGrab.grab(bbox=(0,0,1919,1079))
    # 调整捕获窗口的大小
    #frame1 = cv2.resize(frame1, (capture_width, capture_height))
    # 色彩空间处理
    frame1_np = cv2.cvtColor(np.array(frame1),cv2.COLOR_RGB2BGR)
    #识别
    results = model(source=frame1_np)

    image = results[0].plot()
    #print('results:',results[0].names)

    boxes = results[0].boxes.data
    #print(boxes)
    boxes_index = []
    for box in boxes:
        box1 = [float(f"{num:.2f}") for num in box.tolist()]
        boxes_index.append(box1)
    print(boxes_index)

    return image,boxes_index

def positions(pos):
    x_min = pos[0]
    y_min = pos[1]
    x_max = pos[2]
    y_max = pos[3]
    x_centre = x_max - (x_max - x_min)/2
    y_centre = y_max - (y_max - y_min)/2
    xpos = int(x_centre - 960)
    ypos = int(y_centre - 540)
    print(xpos,ypos,x_centre,y_centre)
    return xpos,ypos,x_centre,y_centre

if __name__ == "__main__":
    while True:
        x,y = win32api.GetCursorPos()
        print("光标当前位置：",x,y)
        image, boxes_index = detect()
        if len(boxes_index) > 0 :
            # 判断对象分类是否是人类，且判断相似度大于0.5
            check = [index for index, item in enumerate(boxes_index) if (item[-1] == 0.0 and item[-2] > 0.5)]
            print("index:",check)

            if len(check) > 0 and win32api.GetKeyState(0x14) & 0x0001:
                x_centre, x_centre, xpos, ypos = positions(boxes_index[check[0]])
                win32api.SetCursorPos(int(xpos),int(ypos))

        cv2.namedWindow('result',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('result',800,430)

        cv2.imshow('result',image)
        cv2.setWindowProperty('result',cv2.WND_PROP_TOPMOST, 1)
        
cv2.destroyAllWindows()