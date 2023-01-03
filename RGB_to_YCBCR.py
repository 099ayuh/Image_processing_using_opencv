import cv2

RGB_img = cv2.imread('Lenna.png')

YCBCR = cv2.cvtColor(RGB_img, cv2.COLOR_RGB2YCrCb)

cv2.imwrite('YCbCr_Lenna.jpg', YCBCR)
