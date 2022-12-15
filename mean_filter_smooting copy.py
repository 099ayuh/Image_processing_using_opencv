import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image2.jpg', 0)
img2 = img.copy()

h, w = img.shape[:2]

karnal = np.ones([3, 3], int)

zeroPaddingImg = np.zeros([h+2, w+2], int)

for i in range(1, h-1):
    for j in range(1, w-1):
        zeroPaddingImg[i][j] = img[i-1][j-1]

for i in range(1, h-1):
    for j in range(1, w-1):
        for k in range(3):
            for l in range(3):
                karnal[k][l] = zeroPaddingImg[i + k - 1][j + l - 1]

        """ karnal[0][0] = zeroPaddingImg[i-1][j-1]
        karnal[0][1] = zeroPaddingImg[i-1][j]
        karnal[0][2] = zeroPaddingImg[i-1][j+1]

        karnal[1][0] = zeroPaddingImg[i][j-1]
        karnal[1][1] = zeroPaddingImg[i][j]
        karnal[1][2] = zeroPaddingImg[i][j+1]

        karnal[2][0] = zeroPaddingImg[i+1][j-1]
        karnal[2][1] = zeroPaddingImg[i+1][j]
        karnal[2][2] = zeroPaddingImg[i+1][j+1] """

        # for min filter
        img[i-1][j-1] = karnal.mean()

# for adding to different images in a single frame
img12 = np.hstack((img2, img))
cv.imshow('img', img12)

cv.waitKey(0)
