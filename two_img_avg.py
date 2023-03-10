import cv2 as c
import numpy as np

img1 = c.imread('image1.jpg', 0)
img2 = c.imread('maya.png', 0)

c.imshow('image1', img1)

print(img1.shape)
print(img2.shape)

c.imshow('image', img2)


h1, w1 = img1.shape[:2]
img2 = c.resize(img2, (w1, h1))
print(img2.shape)
h2, w2 = img2.shape[:2]

# if (h1 == h2 and w1 == w2):
img_avg = np.zeros([h1, w1], int)
img_avg = (img1+img2)/2
c.imshow('average image', img_avg)
c.waitKey(0)
# else:
#     print('average not possible')

