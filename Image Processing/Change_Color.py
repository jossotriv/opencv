import cv2
import numpy as np
# how to detect the flags of color conversion
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)


# how to find hsv values to track
green = np.uint8([[[0,255,0]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)
#[h-10,100,100] = lower bound and [h+10,255,255] = higher bound

cap = cv2.VideoCapture(0)
while(True):
    #Take each frame
    _,frame = cap.read()
    #Convert BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    #define range of red color in HSV
    lower_red  = np.array([-10,100,100])
    upper_red = np.array([10,255,255])

    #threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv,lower_blue,upper_blue)
    mask_red = cv2.inRange(hsv,lower_red,upper_red)
    mask= mask_red+mask_blue
    #bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k ==27:
        break
cv2.destroyAllWindows()