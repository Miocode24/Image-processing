import cv2 as cv
import numpy as np

img=cv.imread('rgbimage.jpg',1)
img=img/255
#cv.imshow('image',img)
#cv.waitKey()
height,width,channels=np.shape(img)
for row in range(height):
    for column in range(width):
       if row==column:
          img[row][column]=1
       #img[row][column]=1-img[row][column]
       if img[row][column]>=0 and img[row][column]<=0.5:
        img[row][column]=0
       else:
        img[row][column]=1
cv.imshow('after',img)
cv.waitKey()
