import cv2 
img = cv2.imread('Lenna.png')
g_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('Gray_lenna',g_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
cv2.imwrite('Gray_Lenna.png',g_img) #output file name followed by image array