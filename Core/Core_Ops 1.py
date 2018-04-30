import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/Users/josed.sotorivera/Desktop/Random.jpg')

px = img[100,100]
print (px)
blue = img[100,100,0]
print(blue)
#access red value
print(img.item(10,10,2))
#modify red value
print(img.itemset((10,10,2),100))
#look at red
print(img.item(10,10,2))

#returns rows,columns and channels of colors
print("rows,columns & channels")
print (img.shape)

#returns total number of pixels
print("number of pixels")
print(img.size)

#returns image datatype
print("image datatype")
print(img.dtype)

#selecting the ball
hand = img[520:660,935:1105]
# printing the ball somewhere else

#the channels of the image can be split
b,g,r = cv2.split(img)

# then they can be remerged
img = cv2.merge((b,g,r))
#make red pixels 0
img[:,:,2] =0


#different types of borders for images
#coloring around hand and printing image
img[300:440, 200:370] = hand
cv2.rectangle(img,(935,520),(1105,660),(0,255,0),3)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('random_gray.png', img)
    cv2.destroyAllWindows()


