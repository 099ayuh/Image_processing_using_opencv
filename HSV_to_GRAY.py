import cv2

HSV_img = cv2.imread('HSV_Lenna.png')

RGB_img = cv2.cvtColor(HSV_img, cv2.COLOR_HSV2RGB)

cv2.imwrite('RGB_Lenna.png', RGB_img)
