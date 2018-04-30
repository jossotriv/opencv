import cv2
import numpy as np
from matplotlib import pyplot as plt
class Transform():
    def __init__(self,img):
        self.img = img
    #rescale an image
    def scale(self,state_of_resizing,style_of_rezising):
        # state of resizing could be cv2.INTER_AREA for shrinking, cv2.INTER_CUBIC & cv2.INTER_LINEAR for zooming
        if state_of_resizing.lower() == 'scaling':
            res = cv2.resize(self.img, None, fx = 2, fy=2,interpolation = style_of_rezising)
        if state_of_resizing.lower() == "manual":
            height, width = img.shape[:2]
            res = cv2.resize(self.img,(int(width*1/4),int(height*1/4)),interpolation = style_of_rezising)
        return res
    #create a matrix to shift an image from one place to another
    def Translation(self):
        rows,cols = self.img.shape[:2]
        #this is the translation matrix:
        #[1 0 50]
        #[0 1 100]
        M = np.float32([[1,0,100],[0,1,50]])
        #applies the matrix to the rows
        dst = cv2.warpAffine(self.img,M,(cols,rows))
        return dst
    #rotate
    def Rotation(self):
        #retrievees the values of the rows and columns of the image
        rows,cols = self.img.shape[:2]
        # find the rotation matrix about the center with a 90º counterclockwise rotation and no scaling
        M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
        dst = cv2.warpAffine(img,M,(cols,rows))
        return dst
    # parallel lines stay parallel, try to maintain shape of figure
    def affine_trans(self):
        # retrieves columns,rows and channels of colors from image
        rows,cols,ch = img.shape
        #makes points
        pts1 = np.float32([[50,50],[200,50],[50,200]])
        pts2 = np.float32([[10,100],[200,50],[100,250]])

        #find the matric that will shift the points above to this location, simplest
        M = cv2.getAffineTransform(pts1,pts2)

        dst = cv2.warpAffine(self.img,M,(cols,rows))
        plt.subplot(121),plt.imshow(img),plt.title("Input")
        plt.subplot(122),plt.imshow(dst),plt.title("output")
        plt.show()

    #straihgt lines will remain straight,basically rotate perspective
    def persp_trans(self):
        #retrives the rows, cols
        rows,cols = img.shape[:2]
        #sets the initial poins and describes their final position
        pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
        pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

        #get transformation matrix

        M = cv2.getPerspectiveTransform(pts1,pts2)

        #make the transformation
        dst = cv2.warpPerspective(self.img,M,(300,300))

        plt.subplot(121),plt.imshow(self.img),plt.title("Input")
        plt.subplot(122),plt.imshow(dst),plt.title("Output")
        plt.show()
if "__main__" == __name__:
    img = cv2.imread("/Users/josed.sotorivera/Desktop/Me.jpg")
    trans = Transform(img)


    img =trans.scale('manual', cv2.INTER_AREA)
    #cv2.imshow('res', trans.scale('manual',img))
    trans = Transform(img)
    # translate image
    # cv2.imshow('img',trans.Translation())
    # make perspective transformation
    trans.persp_trans()
    #code that destroys image

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.destroyAllWindows()
