import numpy as np
import cv2

# Logan was here

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame

    frame[100,100] = [0,0,0]				#draws a small straight black
    frame[101,100] = [0,0,0]				#line where pixels are
    frame[102,100] = [0,0,0]

   # for x in range(260,460):
    #    for y in range(540,740):
     #       gray[x,y] = [0,0,0]



    cv2.imshow('frame',gray)

    cv2.namedWindow("frame", 0)
    #cv2.resizeWindow("frame", 1000,1000)   #resize image, not really useful
    cv2.moveWindow('frame', 0, 0)      #Moves window to top left of screen

    #cv2.imwrite('max.png',gray)  #saves image
    print gray.shape	#image properties [rows columns channels]
    if cv2.waitKey(1) & 0xFF == ord('q'):	#waitkey does not work
    	print "Quitting"
        break
    if cv2.waitKey(1) & 0xFF == ord('a'):
        cv2.imwrite('max.png',gray)
        print "captured image"

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
