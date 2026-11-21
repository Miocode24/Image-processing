
import cv2 as cv
import numpy as np

img = cv.imread('grayscale.jpg', 0)

cv.imshow('Original Image', img)

row, col = np.shape(img)

newimg = np.zeros((row, col))

for r in range(1, row - 1):
    for c in range(1, col - 1):

        vec = np.array([
            img[r][c],
            img[r][c-1],
            img[r][c+1],
            img[r-1][c],
            img[r-1][c+1],
            img[r-1][c-1],
            img[r+1][c+1],
            img[r+1][c-1],
            img[r+1][c]
        ])

        s = np.sort(vec)

        newimg[r][c] = s[-1]  # Maximum value

newimg = newimg / 255

cv.imshow('Maximum Filter', newimg)
cv.waitKey()
