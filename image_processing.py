import cv2
import numpy as np

img = cv2.imread('grayscale.jpeg', 0)

if img is None:
    print("Image not found")
    exit()

# NEGATIVE IMAGE
L = img.max()
negative = L - img
cv2.imwrite('negative.jpeg', negative)

# FLIP IMAGE (Horizontal)
flip_img = cv2.flip(img, 1)
cv2.imwrite('flip.jpeg', flip_img)

# THRESHOLDING
T = 150
m, n = img.shape
thresh = np.zeros((m, n), dtype=np.uint8)

for i in range(m):
    for j in range(n):
        thresh[i, j] = 255 if img[i, j] > T else 0

cv2.imwrite('threshold.jpeg', thresh)

# CONTRAST STRETCHING
rmin, rmax = img.min(), img.max()
contrast = ((img - rmin) / (rmax - rmin)) * 255
contrast = contrast.astype(np.uint8)

cv2.imwrite('contrast.jpeg', contrast)

print("All image processing operations completed.")
