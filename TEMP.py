import cv2
import time
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0)#读取摄像头
# 设置窗口大小：1280*720
cap.set(3, 1280)#窗口宽度
cap.set(4, 700)#窗口高度

keyboard = Controller()#键盘控制器
detector = HandDetector(mode=False,  # 视频流图像
                        maxHands=2 ,  # 最多检测一只手
                        detectionCon=0.8,  # 最小检测置信度
                        minTrackCon=0.5)  # 最小跟踪置信度