import numpy as np
import cv2

def nothing(x):
    pass


background = np.zeros((512, 512, 3), np.uint8)
drawing_layer = np.zeros((512, 512, 3), np.uint8)
img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow('image')

circles = False
rectangles = True
ix, iy = -1,-1

def draw_shape(event,x,y,flags,param):
    global ix,iy,circles,rectangles, drawing_layer
    
    if event == cv2.EVENT_LBUTTONDOWN:
        circles = True
        ix,iy = x,y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if circles:
            
            temp = drawing_layer.copy()
            if rectangles == True:
                cv2.rectangle(temp,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(temp,(x,y),5,(0,0,255),-1)
            img[:] = cv2.add(background, temp)
            
    elif event == cv2.EVENT_LBUTTONUP:
        circles = False
        if rectangles == True:
            cv2.rectangle(drawing_layer,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(drawing_layer,(x,y),5,(0,0,255),-1)
        img[:] = cv2.add(background,drawing_layer)

r = cv2.createTrackbar('R','image',0,255,nothing)
g = cv2.createTrackbar('G','image',0,255,nothing)
b = cv2.createTrackbar('B','image',0,255,nothing)
switch = "on | of"
cv2.createTrackbar(switch,'image',0,1,nothing)

cv2.setMouseCallback('image', draw_shape)

while True:
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')
    
    if s == 0:
        background[:] = 0
    else:
        background[:] = [b,g,r]
        
    img[:] = cv2.add(background,drawing_layer)
    
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    
    if k == ord('m'):
        rectangles = not rectangles
    elif k == 27:
        break
        

cv2.destroyAllWindows()