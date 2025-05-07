import cv2 as cv

img = cv.imread('openCV2/image 2/Screenshot_16.png')
cv.imshow('img', img)

def Frameresize(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

resized_image = Frameresize(img)
cv.imshow('resize img', resized_image)

cv.waitKey(0)
cv.destroyAllWindows()