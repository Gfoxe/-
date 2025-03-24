from ultralytics import YOLO
import numpy as np
import pyautogui
import cv2

#screen_width, screen_height = 1919,1079
#capture_width, capture_height = 1920,1080
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('desktop.mp4', fourcc, 20.0, (capture_width, capture_height))


model = YOLO("yolov8n.pt")
video = 'D:\VSC_project\YOLO\catear.mp4'
#img = cv2.imread('baka.jpg')
# Track with the model
while True:
    #screenshot = pyautogui.screenshot(region=(1,1,screen_width,screen_height))
    #frame1 = np.array(screenshot)
    #frame1 = cv2.resize(frame1, (capture_width, capture_height))
    #out.write(frame1)
    #cv2.imshow('Screen Capture', frame1)

    index = model.track(source=video, show=True,show_conf=False)
    print(index)
    if cv2.waitKey(0):
        break
cv2.destroyAllWindows()