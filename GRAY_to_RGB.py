import cv2 as cv
img = cv.imread('Gray_Lenna.png',0)
g_img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
cv.imshow('RGB_lenna',g_img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('RGB_Lenna.png',g_img) #output file name followed by image array

