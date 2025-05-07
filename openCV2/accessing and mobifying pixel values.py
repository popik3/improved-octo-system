import cv2
import numpy as np

img = cv2.imread('openCV2/image 2/Screenshot_16.png')

px = img[100,100]
print(px)
'[126 128 130]'

#accessing only blue pixel
blue = img[100,100,0]
print(blue)
'126'
img[100,100] = [255,255,255]
print (img[100,100])
'[255 255 255]'

cv2.imshow('imsge', img)

cv2.waitKey(0)
cv2.destroyAllWindows()