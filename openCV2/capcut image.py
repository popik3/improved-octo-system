import cv2
import numpy as np

img = cv2.imread('openCV2/image/fak.png', -1)

tag = img[100:110, 120:140]
img[110:120, 130:150] = tag

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()