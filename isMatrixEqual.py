import cv2 as c
import numpy as np

img1 = c.imread('image1.jpg')
img2 = c.imread('image1.jpg')

h1,w1 = img1.shape[:2]
img2 = c.resize(img2, [w1,h1])
img_status = (img1 - img2)
h,w = img_status.shape[:2]

flag = 0
for i in range(h):
    for j in range(w):
        if(img_status[i][j].all() != 0):
            flag = 1
            break
        
if(flag == 1):
    print('img1 and img2 are not equal..')
else:
    print('img1 and img2 are equal..')

c.imshow('', img_status)
c.waitKey(0)