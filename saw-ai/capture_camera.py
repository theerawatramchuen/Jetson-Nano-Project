import numpy as np
import cv2

cap = cv2.VideoCapture('project.avi')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:  # New
        break  # Get out if we don't read a frame successfully

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()