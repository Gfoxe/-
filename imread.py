import cv2
img = cv2.imread('example.jpg',1)  #读取一张图片
print(img.shape)

cv2.imshow('example',img)   #显示读取的图片
cv2.waitKey(0) 
cv2.destroyAllWindows() #dv2.destroyWindow(wname)


cv2.imwrite('1.png',img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])  #保存已读取的图片
cv2.imwrite('1.png',img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9]) #cv2.imwrite(file，img，num)