import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/josed.sotorivera/Desktop/Me.jpg')
img_gra = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
def thresholding(state,img_):
    if state == 0:
        # makes black or white
        ret,thresh1 = cv2.threshold(img_,127,255,cv2.THRESH_BINARY)
        #makes black or white inverted
        ret,thresh2 = cv2.threshold(img_,127,255,cv2.THRESH_BINARY_INV)
        #after a certain value will just go white
        ret,thresh3 = cv2.threshold(img_,127,255,cv2.THRESH_TRUNC)
        #before a certain value will be black
        ret,thresh4 = cv2.threshold(img_,127,255,cv2.THRESH_TOZERO)
        # before a certain value will be black but inversed
        ret,thresh5 = cv2.threshold(img_,127,255,cv2.THRESH_TOZERO_INV)

        titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
        images = [img_, thresh1, thresh2, thresh3, thresh4, thresh5]

        for i in range(6):
            plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])

        plt.show()
    if state == 1:
        img = cv2.medianBlur(img_, 5)

        ret, th1 = cv2.threshold(img_, 127, 255, cv2.THRESH_BINARY)
        th2 = cv2.adaptiveThreshold(img_, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                    cv2.THRESH_BINARY, 11, 2)
        th3 = cv2.adaptiveThreshold(img_, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                    cv2.THRESH_BINARY, 11, 2)

        titles = ['Original Image', 'Global Thresholding (v = 127)',
                  'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
        images = [img_, th1, th2, th3]

        for i in range(4):
            plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
        plt.show()
    if state == 2:
        # global thresholding
        ret1, th1 = cv2.threshold(img_, 127, 255, cv2.THRESH_BINARY)

        # Otsu's thresholding
        ret2, th2 = cv2.threshold(img_, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Otsu's thresholding after Gaussian filtering
        blur = cv2.GaussianBlur(img_, (5, 5), 0)
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # plot all the images and their histograms
        images = [img_, 0, th1,
                  img_, 0, th2,
                  blur, 0, th3]
        titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
                  'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
                  'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

        for i in range(3):
            plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
            plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
            plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
            plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
            plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
            plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
        plt.show()
thresholding(2,img_gra)