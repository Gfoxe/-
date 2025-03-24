import cv2

img = cv2.imread('baka.png')
img1 = cv2.resize(img,(1000,1400))
canny = cv2.Canny(img1,100,50)
cv2.imwrite('output_baka.png',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()