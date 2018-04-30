import cv2
import numpy as np
#___adding explanation _________________________________
x= np.uint8([250])
y = np.uint8([10])

print(cv2.add(x,y)) # Normal Addition: 250 +10 = 260

print (x+y) # Modulo addition according to bit value(here its 2**8): 250 +10 = 260 %256 = 4
#________________________________________________________

class Resize:
    def __init__(self,hey):
        self.hey =hey
    def image_blending(self,a,b,y):

    #image blending = g(x) = (1-a) * ƒ_0(x) + a* f_1(x)

    #cv2.addWeighted() = dst = a *img_1 + b*img2 + y
    #images must be same size
        img1 = cv2.resize(cv2.imread("/Users/josed.sotorivera/Desktop/Me.jpg"),(400,200),interpolation=cv2.INTER_AREA)
        img2 = cv2.resize(cv2.imread("/Users/josed.sotorivera/Desktop/Random.jpg"),(400,200),interpolation = cv2.INTER_AREA)
        dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
        cv2.imshow('dst',dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def roi_bit(self):
        img1= cv2.imread("/Users/josed.sotorivera/Desktop/Me.jpg")
        img2= cv2.imread("/Users/josed.sotorivera/Desktop/Random.jpg")
        rows, cols, channels = img1.shape
        roi = img1[0:rows,0:cols]

        img1gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        ret,mask = cv2.threshold(img1gray,10,255,cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        img2_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        img1_fg = cv2.bitwise_and(img1,img1,mask = mask)
        dst = cv2.add(img2_bg,img1_fg)
        img1[0:rows,0:cols] = dst
        cv2.imshow('res',img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



if __name__ == "__main__":
    rz = Resize('hey')
    rz.image_blending('a','b','c')
    rz.roi_bit('hey')