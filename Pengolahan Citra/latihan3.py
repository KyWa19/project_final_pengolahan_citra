import cv2
import numpy as np
from matplotlib import pyplot as plt
# Baca gambar
img = cv2.imread('rico.jpg', 0)  # Baca gambar dalam mode grayscale
# Tampilkan gambar asli
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Gambar Asli')
plt.axis('off')
# Fourier Transform
f_img = np.fft.fft2(img)
f_shift = np.fft.fftshift(f_img)
magnitude_spectrum = 20 * np.log(np.abs(f_shift))
# Gaussian Blur
sigma = 5  # Nilai sigma untuk Gaussian blur
f_blur = cv2.GaussianBlur(magnitude_spectrum, (0, 0), sigma)
# Tampilkan gambar hasil Fourier dengan Gaussian Blur
plt.subplot(2, 2, 2)
plt.imshow(f_blur, cmap='gray')
plt.title('Hasil Fourier Transform dan Gaussian Blur')
plt.axis('off')
# Tampilkan histogram gambar asli
plt.subplot(2, 2, 3)
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histogram Gambar Asli')
# Tampilkan histogram gambar hasil Fourier dengan Gaussian Blur
plt.subplot(2, 2, 4)
plt.hist(f_blur.ravel(), 256, [0, 256])
plt.title('Histogram Hasil Fourier Transform dan Gaussian Blur')
plt.tight_layout()
plt.show()
cap = cv2.VideoCapture(0)