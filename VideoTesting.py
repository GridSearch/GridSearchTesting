import numpy as np
import cv2
#Tests isolating red leds and blue boxs colors in buff_test_video_01.mpeg video file

cap = cv2.VideoCapture("buff_test_video_01.mpeg")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here


    # Display the resulting frame
#******************************************* Resized imaged shown to be smaller
    r = 500.0 / frame.shape[1]
    dim = (500, int(frame.shape[0] * r))
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
#*******************************************

    convertedimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#*******************************************
#define range of blue color in HSV
    lower_blue = np.array([100,50,50])
    upper_blue = np.array([130,255,255])

#define range of blue color in HSV
    lower_red = np.array([0,100,100])
#define range of red color in HSV
    upper_red = np.array([100, 255, 255])
        #Adjust accordingly


# Threshold the HSV image to get only blue colors
    mask = cv2.inRange(convertedimage, lower_red, upper_red)
    mask2 = cv2.inRange(convertedimage, lower_blue, upper_blue)

# Bitwise-AND mask and original image
    #Consider making function
    res = cv2.bitwise_and(frame,frame, mask=mask)
    res2 = cv2.bitwise_and(frame,frame, mask=mask2)

    cv2.imshow('Original',frame)
    cv2.moveWindow('Original', 0, 0)

    cv2.imshow('RED_LED',res)
    cv2.moveWindow('RED_LED', 500, 0)

    cv2.imshow('Blue_Boxes',res2)
    cv2.moveWindow('Blue_Boxes', 0, 350)

    cv2.moveWindow('frame', 0, 0)      #Moves window to top left of screen

    k = cv2.waitKey(5) & 0xFF
    if k == 27: #ESC  to quit
        print "Quitting"
        break

#*******************************************

    frame[100,100] = [0,0,0]				#draws a small straight black
    frame[101,100] = [0,0,0]				#line where pixels are
    frame[102,100] = [0,0,0]

#*******************************************
#Red Contour lines

    ret,thresh = cv2.threshold(mask,127,255,1)

    im2,contours,h = cv2.findContours(thresh,1,2)

    cv2.drawContours(frame, contours, -1, (0,0,255), 2)

    cv2.imshow('Contours',frame)
    cv2.moveWindow('Contours',500,350)

#*******************************************
#captures image of frame then quits
    if cv2.waitKey(1) & 0xFF == ord('a'):
        cv2.imwrite('BlueGrid.png',frame)
        print "captured image"
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
