import cv2

YCBCR_img = cv2.imread('YCbCr_Lenna.jpg')

RGB_img = cv2.cvtColor(YCBCR_img, cv2.COLOR_YCrCb2RGB)

cv2.imwrite('RGB_Lenna.jpg', RGB_img)
