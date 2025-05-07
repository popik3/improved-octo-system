import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outpot.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,0)

        out.write(frame)

        cv2.imshow('пизда', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else:
        print("файл не читаемый брат")
        break

cap.release()
out.release()
cv2.destroyAllWindows()