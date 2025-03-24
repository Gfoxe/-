import cv2
import numpy as np

def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray,(3,3),0)
    detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
    dst = cv2.bitwise_and(resize,resize,mask = detected_edges) 
    cv2.imshow('canny demo',dst)
    cv2.imwrite('wzken_output.png',dst)




lowThreshold = -100
max_lowThreshold = 200
ratio = 3
kernel_size = 3
img = cv2.imread('wzken.png')
resize = cv2.resize(img,(3840,2160))
gray = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('canny demo')
cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)

CannyThreshold(0)  # initialization

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()