import numpy as np
import cv2
from matplotlib import pyplot as plt
class open_cv:

    """This is a tutorial for learning how to use opencv"""

    def __init__(self,boom):
        #starts something
        self.boom = boom
    #learning how to read,exit and save images
    def img_proc(self,n):
        if n ==0:
        #using cv2 library
            img = cv2.imread('/Users/josed.sotorivera/Desktop/Random.jpg',0)
            cv2.imshow('image',img)
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()
            elif k == ord('s'):
                cv2.imwrite('random_gray.png',img)
                cv2.destroyAllWindows()
        elif n == 1:
        #using Matplotlib
            img = cv2.imread('/Users/josed.sotorivera/Desktop/Random.jpg', 0)
            plt.imshow(img, cmap='gray', interpolation='bicubic')
            plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
            plt.show()

    #learn how to capture video
    def vid_proc(self,i):
        #capture video
        if i ==0:
            cap = cv2.VideoCapture(0)

            while(True):
                # Capture frame-by-frame
                ret, frame = cap.read()

                #our operations on the frame come here
                gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

                #Display frame
                cv2.imshow('frame',gray)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                #When everything done, release the capture
            cap.release()
            cv2.destroyAllWindows()
        #play video from file
        if i == 1:
            cap = cv2.VideoCapture('/Users/josed.sotorivera/Desktop/drop.avi')

            while (cap.isOpened()):
                ret, frame = cap.read()

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                cv2.imshow('frame', gray)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
        # save video
        if i == 2:
            cap = cv2.VideoCapture(0)

            #Define the codec and create VideoWriter object
            fourcc = cv2.VideoWriter_fourcc(*'MPG4')
            out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,680))

            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    frame = cv2.flip(frame,0)

                    #write the flipped frame
                    out.write(frame)

                    cv2.imshow('frame',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            #release everything
            cap.release()
            out.release()
            cv2.destroyAllWindows()
    #learn how to draw in openCV
    def draw_pic(self,line,rect,circle,ellips,polygon,text,challenge):
        #draw line
        img = np.zeros((512, 512, 3), np.uint8)

        if line:
            #create a black image

            #Draw a diagonal blue line with thickness of 5 px
            img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
        # draw a green rectagle with pixel width of 3
        if rect:
            img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
        #draw a red circle with 63px radius and filled in
        if circle == 1:
            img = cv2.circle(img,(447,63),63,(0,0,255),-1)
        # draw an ellipse
        if ellips:
            img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
        #draw a polygon
        if polygon:
            pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            img = cv2.polylines(img, [pts], True, (0, 255, 255))
        #draws Text
        if text:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

        #draw Challenge
        if challenge:
            #draw one of the large boundary circles
            img = cv2.circle(img,(320,320),60,(0,0,255),-1)
            #draw one of the small inner circles
            img = cv2.circle(img,(320,320),24,(0,0,0),-1)
            #draw one of the pentagon outide
            img =cv2.rectangle(img, (310,200),(320,320), (0, 0, 0), -3)


        #displays image and makes it wait
        cv2.imshow('image',img)
        k = cv2.waitKey(0)
        if k == 27:
            cv2.destroyAllWindows()
        elif k == ord('s'):
            cv2.imwrite('random_gray.png', img)
            cv2.destroyAllWindows()

    #draws a circle when click made
    def draw_circle(self,event,x,y,flags,param):
        global ix,iy,drawing,mode

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix,iy = x,y
        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing == True:
                if mode == True:
                    cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
                else:
                    cv2.circle(img,(x,y),5,(0,0,255),-1)
        elif event == EVENT_LBUTTONUP:
            drawing = False
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    #def a mousecallback function
    def mouse_callback(self,func_):
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',func_)

        while True:
            cv2.imshow('image',img)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('m'):
                mode = not mode
            elif k == 2
        cv2.destroyAllWindows()


# this is used to determine whether or not
if __name__ == '__main__':
    CV_Tut = open_cv('boom')
    # create img for mouse_callback & draw circle
    img = np.zeros((512, 512, 3), np.uint8)

    #img = CV_Tut.draw_pic(False,False,False,False,False,False,True)
    CV_Tut.mouse_callback(CV_Tut.draw_circle)