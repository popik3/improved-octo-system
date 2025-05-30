import cv2
import matplotlib.pyplot as plt

img = cv2.imread('openCV2\image 2\Screenshot_16.png')
cv2.imshow('image', img)

#plt.imshow(img)
plt.show()

#BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', gray)

#BGR to HSV
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow('HSV', HSV)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#cv2.imshow('lab', lab)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('rgb', rgb)

plt.imshow(rgb)
plt.show()

cv2.waitKey(0)