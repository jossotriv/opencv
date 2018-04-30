import cv2
import numpy as np

img1 = cv2.imread('/Users/josed.sotorivera/Desktop/Random.png')
e1 =cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()

time = (e2-e1)/cv2.getTickFrequency()
print(time)

#set optimized code
#cv2.useOptimized returns if optimized code or not

#%timeit res = cv2.medianBlur(img,49)

#cv2.setUseOptimized()
#%timeit res =cv2.medianBlur(img1,49)