""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np
kernel = np.ones((21,21),'uint8')

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    for (x,y,w,h) in faces:
    	 cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
    	 for (x,y,w,h) in faces:
			frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
			cv2.circle(frame, (int(x + w/3), int(y + h/3)), int(w/7), (0, 0, 0), -1)
			cv2.circle(frame, (int(x + w*2/3), int(y + h/3)), int(w/7), (0, 0, 0), -1)
			cv2.ellipse(frame, (int(x + w/2), int(y + h*2/3)), (int(w/4), int(h/5)), 0, 0, 180, (0, 0, 0), 20)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()