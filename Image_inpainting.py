
import cv2 as cv
import numpy as np

# Read the original image
img = cv.imread('image.jpg', 0)

if img is None:
    raise FileNotFoundError("Could not load image.jpg")

# Create a damaged image
damaged = img.copy()

# Create a mask: 255 represents missing pixels
mask = np.zeros(img.shape, dtype=np.uint8)

# Example damaged region (white rectangle)
cv.rectangle(mask, (100, 100), (200, 200), 255, -1)

damaged[mask == 255] = 0

# Initialize the reconstructed image
result = damaged.astype(np.float32)

# Iterative diffusion inpainting
for iteration in range(500):

    previous = result.copy()

    for r in range(1, img.shape[0] - 1):
        for c in range(1, img.shape[1] - 1):

            if mask[r, c] == 255:

                result[r, c] = (
                    previous[r-1, c] +
                    previous[r+1, c] +
                    previous[r, c-1] +
                    previous[r, c+1]
                ) / 4.0

# Convert the result to an image
result = np.clip(result, 0, 255).astype(np.uint8)

# Display results
cv.imshow('Original Image', img)
cv.imshow('Damaged Image', damaged)
cv.imshow('Inpainted Image', result)

# Save results
cv.imwrite('damaged.png', damaged)
cv.imwrite('inpainted.png', result)

cv.waitKey()
