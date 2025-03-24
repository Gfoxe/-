import cv2
import numpy as np
from PIL import ImageGrab
import random
import win32api
import win32con
from win32api import GetSystemMetrics
import pyautogui
pyautogui.FAILSAFE=False
from ultralytics import YOLO
import time
from ctypes import CDLL
from simple_pid import PID
import pynput
import ctypes
MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA

try:
    gm = CDLL(r'../ghub_device.dll')
    gmok = gm.device_open() == 1
    if not gmok:
        print('未安装GHUB驱动!!!')
    else:
        print('初始化成功!')
except FileNotFoundError:
    print('缺少文件')

def mouse_xy(x, y, abs_move = False):
    if gmok:
        gm.moveR(int(x), int(y), abs_move)


def mouse_move(driver,target_x,target_y):
    mouse = pynput.mouse.Controller()
    while True:
        if abs(target_x - mouse.position[0])<3 and abs(target_y - mouse.position[1])<3:
            break
        pid_x = PID(0.25, 0.01, 0.01, setpoint=target_x)
        pid_y = PID(0.25, 0.01, 0.01, setpoint=target_y)
        next_x,next_y = pid_x(mouse.position[0]),pid_y(mouse.position[1])
        driver.moveR(int(round(next_x)), int(round(next_y)), False) # 鼠标移动
        # print(mouse.position) # 打印鼠标位置

def mouse_xy(a, b, abs_move = False):
    if gmok:
        gm.moveR(int(a), int(b), abs_move)


# 初始化YOLO模型
model = YOLO('yolov8n.pt')

def location(a):
    aimx = a[0][0] + ((a[0][2] - a[0][0])/2)# - 960
    aimy = a[0][1] + ((a[0][3] - a[0][1])/2)# - 540
    return aimx,aimy


#d_x1 = 800
#d_y1 = 440
#d_x2 = 1120
#d_y2 = 640
#ampx = 1920/(d_x2 - d_x1)
#ampy = 1080/(d_y2 - d_y1)
while True:
    # 屏幕截图
    screenshot = ImageGrab.grab()
    #screenshot = screenshot.crop((800,440,1120,640))
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # 图像输入模型进行检测
    results = model.track(source=img,classes=[0],persist=True)

    image = results[0].plot()
    boxes = results[0].boxes.data
    xy = []

    # 获得最左侧人的检测框中心位置
    for box in boxes:
        box1 = [float(f"{num:.2f}") for num in box.tolist()]
        if len(box1) > 0:
            xy.append(box1)
    

    # 获取当前鼠标位置
    x,y = pyautogui.position()
    print("鼠标位置",x,y)
    # 打印坐标信息

    if len(xy) > 0 and win32api.GetKeyState(0x14) & 0x0001:
        target_x = int(location(xy)[0])
        target_y = int(location(xy)[1])
        #print("目标位置：", xy)
        mouse_move(gm,target_x,target_y)
        #mouse_xy(target_x,target_y)
        #pyautogui.moveRel(target_x,target_y)
        print("瞄准位置",int(location(xy)[0]),int(location(xy)[1]))
        print(xy[0][0])
        #print('results:',results[0].names)
