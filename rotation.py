import cv2 as c
import numpy as np
import matplotlib.pyplot as plt

image = c.imread('image2.jpg')
c.imshow('original',image)

image1 = c.rotate(image, c.ROTATE_90_CLOCKWISE)
c.imshow('clockwise',image1)

image2 = c.rotate(image, c.ROTATE_90_COUNTERCLOCKWISE)
c.imshow('Anti-clockwise',image2)

c.waitKey(0)