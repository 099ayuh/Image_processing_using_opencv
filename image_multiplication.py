import cv2 as c
import numpy as np

img1 = c.imread('image1.jpg')
img2 = c.imread('image2.jpg')

img_result = (img1 * img2)

c.imshow('', img_result)
c.waitKey(0)