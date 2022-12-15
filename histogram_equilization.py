import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image2.jpg', 0)

cv2.imshow('before equilization', img)

histogram = cv2.calcHist([img], [0], None, [256], [0, 255])
plt.plot(histogram)


freq = np.zeros(256, int)

h, w = img.shape[:2]

for i in range(h):
    for j in range(w):
        freq[img[i][j]] += 1

sum = np.sum(freq)

freq = (freq / sum)

freq = np.cumsum(freq)

freq *= 255

freq = np.ceil(freq)

img2 = img.copy()

for i in range(h):
    for j in range(w):
        img2[i][j] = freq[img[i][j]]

cv2.imshow('after equilization', img2)

histogram = cv2.calcHist([img2], [0], None, [256], [0, 255])
plt.plot(histogram)

plt.show()

cv2.waitKey(0)
