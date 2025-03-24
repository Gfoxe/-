import cv2
from ultralytics import YOLO
import pyautogui
from PIL import ImageGrab

model = YOLO("yolov8x.pt")

while True:
    screenshot = ImageGrab.grab(bbox=(1,1,1919,1079))
    model.predict(screenshot,show=True)