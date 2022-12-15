import cv2 as chutiya
import numpy as np
import math
import matplotlib.pyplot as plt

image = chutiya.imread('low_contrast.jpg', 0)

h, w = image.shape[:2]

print(h, w)

chutiya.imshow('Original Image', image)

histogram = chutiya.calcHist([image], [0], None, [256], [0, 255])
plt.plot(histogram)
plt.show()

def evaluatePixel(pixel):
    return math.log(pixel+1, 10)

for i in range(h):
    for j in range(w):
        image[i][j] = evaluatePixel(image[i][j])

histogram = chutiya.calcHist([image], [0], None, [256], [0, 255])
plt.plot(histogram)
plt.show()

chutiya.imshow('After Log Transformation', image)

chutiya.waitKey(0)
