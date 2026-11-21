import cv2 as cv
import numpy as np
img=cv.imread('grayscale.jpg',0)  #0 if grayscale and 1 if rgb
img=img/255 #to normalize
#cv.imshow('before',img)
#cv.waitKey()    #to wait until press on any key
height,width=np.shape(img)
for row in range(height):
    for col in range(width):
       # img[row,col]=1 #to make it white and 0 for black

        if [row]==[col]:
            img[row][col]=1  #to make the diagonal white

        img[row][col]=1-img[row][col]  #to change the 0 to 1 and the 1 to 0
     
        if img[row][col]>=0 and img[row][col]<0.5:
            img[row][col]=0

        else:
           img[row][col]=1
cv.imshow('result',img)
cv.waitKey()
