import cv2

RGB_img = cv2.imread('Lenna.png')

HSV_img = cv2.cvtColor(RGB_img, cv2.COLOR_RGB2HSV)

cv2.imwrite('HSV_Lenna.png', HSV_img)