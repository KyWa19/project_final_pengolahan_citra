import cv2
import numpy as np

# Baca gambar
img = cv2.imread('ky2.jpg', cv2.IMREAD_GRAYSCALE)

# Deteksi tepi dengan metode thresholding
thresh_value = 100
max_value = 255
_, edges = cv2.threshold(img, thresh_value, max_value, cv2.THRESH_BINARY)

# Tampilkan gambar hasil deteksi tepi
cv2.imshow('Original Image', img)
cv2.imshow('Edge Detection with Thresholding', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()