import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('maya.png', 0)
cv2.imshow('initial image', img)

h,w = img.shape[:2]

gamma = 1/0.25

c=1

def evaluatePixel(pixel):
    global gamma, c
    return ((c*pixel)**gamma)

for i in range(h):
    for j in range(w):
        img[i][j] = evaluatePixel(img[i][j])

cv2.imshow('tranform image', img)

cv2.waitKey(0)