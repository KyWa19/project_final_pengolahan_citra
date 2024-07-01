import cv2
import numpy as np

# Baca gambar
img = cv2.imread('risky.jpg', 0)

# Gaussian Filtering
img_blur = cv2.GaussianBlur(img, (3, 3), 0)

# Laplacian
laplacian = cv2.Laplacian(img_blur, cv2.CV_64F)

# Konvolusi dengan Mask
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
laplacian_mask = cv2.filter2D(laplacian, -1, kernel)

# Operator Kompas
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
magnitude = np.sqrt(sobelx*2 + sobely*2)

# Tampilkan gambar
cv2.imshow('Original Image', img)
cv2.imshow('Laplacian', laplacian)
cv2.imshow('Laplacian with Mask', laplacian_mask)
cv2.imshow('Operator Compass', magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()