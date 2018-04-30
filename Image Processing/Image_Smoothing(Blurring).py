import numpy as np
import cv2
import matplotlib.pyplot as plt
#Learn how to smooth images, bad for edge detection,
#there are four types of edge detection:
#averaging,
#Gaussian Filtering,
#Median Filtering &
#Bilateral Filtering
class Smooth():
    def __init__(self,boom):
        self.boom = boom
        self.img =cv2.imread('/Users/josed.sotorivera/Desktop/Me.jpg')
        self.img_1 = cv2.resize(self.img,(400,300),interpolation = cv2.INTER_AREA)
        #kernel -> 5*5 matrix multiplied by 1/25
        self.kernel = np.ones((5,5),np.float32)/25

    #blurs image quite a bit
    def image_filtering(self):
        #cv2.filter2D() is taking the average of all the pixels around the image

        return cv2.filter2D(self.img_1,-1,self.kernel)
    #blurs by averaging out, using a box kernel
    def averaging(self):
        return cv2.blur(self.img_1,(5,5))
    #uses a Gaussian Kernal
    def Gaussian_Filtering(self):
        #you need to specify width and height of kernel which should be positive and odd(second argument)
        #also specify standard deviation as third & fourth arguments
        #Create Gaussian Kernel by using cv2.getGaussianKernel()
        return cv2.GaussianBlur(self.img_1,(5,5),0)

    #useful to filter salt and pepper noise, kernel must be positive and odd
    #will not allow values not in image through
    def Median_Filtering(self):
        return cv2.medianBlur(self.img_1,5)
    #bilateral filtering, preserves edges while removing noise
    #slow
    def Bilateral_Filtering(self):
        #arg 1 = diameter of each pixel neighberhood
        #arg_2 = sigma_color, larger value = more mixed colors
        #arg_3 = sigmaSpace, similar colors will influence each other even if far away
        return cv2.bilateralFilter(self.img_1,9,75,75)
if __name__ == "__main__":
    test = Smooth('boom')
    while True:
        cv2.imshow('Original', test.img_1)

        #fast filtering
        cv2.imshow("transformed", test.image_filtering())
        #averaging
        cv2.imshow('averaged',test.averaging())
        #Gaussian
        cv2.imshow("gaussian",test.Gaussian_Filtering())
        #Median
        cv2.imshow('median',test.Median_Filtering())
        #bilateral, best & slowest

        cv2.imshow('bilateral',test.Bilateral_Filtering())
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
