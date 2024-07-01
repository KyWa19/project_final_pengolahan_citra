import cv2
import numpy as np

# Baca gambar
img = cv2.imread('risky.jpg', cv2.IMREAD_GRAYSCALE)

# Deteksi tepi dengan operasi Sobel
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.addWeighted(cv2.convertScaleAbs(sobelx), 0.5, cv2.convertScaleAbs(sobely), 0.5, 0)

# Deteksi tepi dengan operasi Prewitt
kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
prewittx = cv2.filter2D(img, -1, kernelx)
prewitty = cv2.filter2D(img, -1, kernely)
prewitt_combined = cv2.addWeighted(cv2.convertScaleAbs(prewittx), 0.5, cv2.convertScaleAbs(prewitty), 0.5, 0)

# Deteksi tepi dengan operasi Roberts
roberts_cross_v = np.array([[0, 1], [-1, 0]])
roberts_cross_h = np.array([[1, 0], [0, -1]])
roberts_x = cv2.filter2D(img, -1, roberts_cross_v)
roberts_y = cv2.filter2D(img, -1, roberts_cross_h)
roberts_combined = cv2.addWeighted(cv2.convertScaleAbs(roberts_x), 0.5, cv2.convertScaleAbs(roberts_y), 0.5, 0)

# Deteksi tepi dengan operasi Laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Tampilkan gambar
cv2.imshow('Original Image', img)
cv2.imshow('Sobel Edge Detection', sobel_combined)
cv2.imshow('Prewitt Edge Detection', prewitt_combined)
cv2.imshow('Roberts Edge Detection', roberts_combined)
cv2.imshow('Laplacian Edge Detection', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

# Baca gambar
img = cv2.imread('risky.jpg', cv2.IMREAD_GRAYSCALE)

# Deteksi tepi dengan metode thresholding
thresh_value = 100
max_value = 255
_, edges = cv2.threshold(img, thresh_value, max_value, cv2.THRESH_BINARY)

# Tampilkan gambar hasil deteksi tepi
cv2.imshow('Original Image', img)
cv2.imshow('Edge Detection with Thresholding', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()