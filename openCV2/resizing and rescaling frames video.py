import cv2 as cv

capture = cv.VideoCapture('openCV2/video/1718886349_sample_640x360.avi')

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    
while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.waitKey(0)