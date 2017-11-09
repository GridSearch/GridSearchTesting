import numpy as np
import cv2
import math
#Tests isolating red leds and blue boxs colors in buff_test_video_01.mpeg video file

cap = cv2.VideoCapture("buff_test_video_01.mpeg")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here


    # Display the resulting frame
#*******************************************
#Resized imaged shown to be smaller
    r = 500.0 / frame.shape[1]
    dim = (500, int(frame.shape[0] * r))
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    Nframe = frame
#*******************************************

    convertedimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#*******************************************
#Isolate colors Red and Blue

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

#Shows the Isolated colors in two different windows for red and blue
    cv2.imshow('RED_LED',res)
    cv2.moveWindow('RED_LED', 500, 0)
    cv2.imshow('Blue_Boxes',res2)
    cv2.moveWindow('Blue_Boxes', 0, 350)

#*******************************************
#draws a small straight black
#line where pixels are
#Essential has zero use currently
    frame[100,100] = [0,0,0]
    frame[101,100] = [0,0,0]
    frame[102,100] = [0,0,0]
#*******************************************
#Red Contour lines
    ret,thresh = cv2.threshold(mask2,127,255,1)
    im2,contours,h = cv2.findContours(thresh,1,2)
    #cv2.drawContours(frame, contours, -1, (0,0,255), 1)
    #cv2.imshow('Contours',frame)    #having difficulties displaying contour lines on this window and not the original frame
    #cv2.moveWindow('Contours',500,350)
#*******************************************
#White Boundary Boxes

    CropBox = []

    for contour in contours:
        tempRect = cv2.minAreaRect(contour) #returns the [(x,y),(width,height),(rotation)] of contour lines

        width = int(tempRect[1][0])
        height = int(tempRect[1][1])
        x = int(tempRect[0][0])
        y = int(tempRect[0][1])
        
        if (width > 25) & (width < 35) & (height > 14) & (height < 30): #roughly the size of our boxes. ***Would not work if camera got closer or further***
            cv2.rectangle(frame,(x-14,y-8),(width+x-14,height+y-8),(255,255,0),1) #x,y seem to be off by a factor??? why?
            #print "width: %f " %width  #Helpful figuring out the right approximated heights and width of boxes
            #print " height: %f"  %height  #not need for now
            CropBox.append([x,y,width,height])
    cv2.imshow('Original',frame)    #Show frame, currently need to get the countour lines off but still show it in "Contour" window
    cv2.moveWindow('Original', 0, 0)
#*******************************************
#Crops images
#NOTE: its frame[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
    x = CropBox[0][0] - 14
    y = CropBox[0][1] - 8
    w = CropBox[0][2]
    h = CropBox[0][3]

    crop_img = frame[y:y+h,x:x+w] # Crop from x, y, w, h -> 0, 0, 100, 100
    cv2.imshow("cropped", crop_img)
#*******************************************
# Esc closes the program
# 'a' captures a still image, saves it, then quits

    k = cv2.waitKey(5) & 0xFF
    if k == 27: #ESC  to quit
        print "Quitting"
        break
    if cv2.waitKey(1) & 0xFF == ord('a'):
        cv2.imwrite('BlueGrid.png',frame)
        print "captured image"
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
