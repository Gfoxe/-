import cv2
img = cv2.imread('1.png')

scaled_image = cv2.resize(img,(500,500))
rotated_image = cv2.rotate(scaled_image, cv2.ROTATE_90_CLOCKWISE)
cropped_image = img[100:300, 100:300]

enhanced_image = cv2.convertScaleAbs(img, alpha=1, beta=0)  #增强图像
denoised_image = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

cv2.imshow('baka',denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()