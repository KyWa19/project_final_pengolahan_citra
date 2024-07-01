import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter
import cv2

def add_salt_and_pepper_noise(image, salt_prob=0.05, pepper_prob=0.05):
    """
    Menambahkan noise salt and pepper ke dalam citra.

    Args:
    - image: Citra asli (array NumPy).
    - salt_prob: Probabilitas noise salt.
    - pepper_prob: Probabilitas noise pepper.

    Returns:
    - noisy_image: Citra dengan noise salt and pepper (array NumPy).
    """
    # Membuat citra dengan noise salt and pepper
    noisy_image = np.copy(image)
    height, width = noisy_image.shape
    salt_pixels = np.random.rand(height, width) < salt_prob
    pepper_pixels = np.random.rand(height, width) < pepper_prob
    noisy_image[salt_pixels] = 255
    noisy_image[pepper_pixels] = 0
    
    return noisy_image

def restore_image(noisy_image, filter_size=3):
    """
    Merestorasi citra yang terkena noise menggunakan filter median.

    Args:
    - noisy_image: Citra dengan noise (array NumPy).
    - filter_size: Ukuran filter median (misalnya 3 untuk filter 3x3).

    Returns:
    - restored_image: Citra yang telah direstorasi (array NumPy).
    """
    # Menerapkan filter median ke dalam citra dengan noise
    restored_image = median_filter(noisy_image, size=filter_size)
    
    return restored_image

# Misalnya, membuat citra dummy untuk contoh
#image = np.ones((256, 256), dtype=np.uint8) * 128  # Citra abu-abu dengan intensitas 128
image = cv2.imread('risky.jpg', cv2.IMREAD_GRAYSCALE)

# Tambahkan noise salt and pepper dengan salt_prob=0.05 dan pepper_prob=0.05
noisy_image = add_salt_and_pepper_noise(image, salt_prob=0.05, pepper_prob=0.05)

# Restorasi citra dengan filter median 3x3
restored_image = restore_image(noisy_image, filter_size=3)

# Tampilkan citra asli, citra dengan noise, dan citra yang direstorasi
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Citra Asli')

plt.subplot(1, 3, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('Citra dengan Noise Salt & Pepper')

plt.subplot(1, 3, 3)
plt.imshow(restored_image, cmap='gray')
plt.title('Citra yang Direstorasi')

plt.show()