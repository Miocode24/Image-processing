
import cv2 as cv
import numpy as np

sobel_x = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
]

sobel_y = [
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1],
]

img = cv.imread('Image Name.jpg', 0)
img = img.astype("float32")

height, width = np.shape(img)

sobel_x_result = np.zeros((height, width))
sobel_y_result = np.zeros((height, width))

for i in range(1, height - 1):
    for j in range(1, width - 1):

        val = (
            img[i - 1][j - 1] * sobel_x[0][0] +
            img[i - 1][j] * sobel_x[0][1] +
            img[i - 1][j + 1] * sobel_x[0][2] +
            img[i][j - 1] * sobel_x[1][0] +
            img[i][j] * sobel_x[1][1] +
            img[i][j + 1] * sobel_x[1][2] +
            img[i + 1][j - 1] * sobel_x[2][0] +
            img[i + 1][j] * sobel_x[2][1] +
            img[i + 1][j + 1] * sobel_x[2][2]
        )

        sobel_x_result[i][j] = val

        val = (
            img[i - 1][j - 1] * sobel_y[0][0] +
            img[i - 1][j] * sobel_y[0][1] +
            img[i - 1][j + 1] * sobel_y[0][2] +
            img[i][j - 1] * sobel_y[1][0] +
            img[i][j] * sobel_y[1][1] +
            img[i][j + 1] * sobel_y[1][2] +
            img[i + 1][j - 1] * sobel_y[2][0] +
            img[i + 1][j] * sobel_y[2][1] +
            img[i + 1][j + 1] * sobel_y[2][2]
        )

        sobel_y_result[i][j] = val

sobel_result = np.sqrt(
    sobel_x_result**2 + sobel_y_result**2
)

sobel_result = np.clip(
    sobel_result, 0, 255
).astype("uint8")

cv.imshow('Sobel Edge Detection', sobel_result)
cv.waitKey()
