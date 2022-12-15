import cv2 
import numpy as np

img = cv2.imread('image2.jpg', 0)

h, w = img.shape[:2]

for i in range(h):
    for j in range(w):
        img[i][j] = 255 - img[i][j]

cv2.imshow('negetive image', img)
cv2.waitKey(0)


