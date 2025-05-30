import cv2 
import numpy as np

img = cv2.imread('openCV2/image 2/Screenshot_16.png')
cv2.imshow('image', img)

def translate(img,x ,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2,height//2)
        
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv2.warpAffine(img,rotMat,dimensions)

rotated = rotate(img, 350)
#cv2.imshow('rotate image', rotated)

flip = cv2.flip(img,-1)
#cv2.imshow('flip image', flip)

translated = translate(img, 100,100)
#cv2.imshow('Traslated', translated)

cropped = img[300:400, 500:600]
#cv2.imshow('cropped', cropped)

cv2.waitKey(0)