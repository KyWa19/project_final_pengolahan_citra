import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
import cv2

def add_uniform_noise(image, min_val=0, max_val=50):
    """
    Menambahkan noise uniform ke dalam citra.

    Args:
    - image: Citra asli (array NumPy).
    - min_val: Nilai minimum noise uniform.
    - max_val: Nilai maksimum noise uniform.

    Returns:
    - noisy_image: Citra dengan noise uniform (array NumPy).
    """
    # Membuat noise uniform
    noise = np.random.uniform(min_val, max_val, image.shape)
    
    # Menambahkan noise ke dalam citra asli
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    
    return noisy_image

def restore_image(noisy_image, filter_size=3):
    """
    Merestorasi citra yang terkena noise menggunakan filter rata-rata.

    Args:
    - noisy_image: Citra dengan noise (array NumPy).
    - filter_size: Ukuran filter rata-rata (misalnya 3 untuk filter 3x3).

    Returns:
    - restored_image: Citra yang telah direstorasi (array NumPy).
    """
    # Membuat filter rata-rata
    filter_kernel = np.ones((filter_size, filter_size)) / (filter_size ** 2)
    
    # Menerapkan filter rata-rata ke dalam citra dengan noise
    restored_image = convolve(noisy_image.astype(np.float32), filter_kernel)
    
    return restored_image.astype(np.uint8)

# Misalnya, membuat citra dummy untuk contoh
#image = np.ones((256, 256), dtype=np.uint8) * 128  # Citra abu-abu dengan intensitas 128
image = cv2.imread('risky.jpg', cv2.IMREAD_GRAYSCALE)

# Tambahkan noise uniform dengan min_val=0 dan max_val=50
noisy_image = add_uniform_noise(image, min_val=0, max_val=50)

# Restorasi citra dengan filter rata-rata 3x3
restored_image = restore_image(noisy_image, filter_size=3)

# Tampilkan citra asli, citra dengan noise, dan citra yang direstorasi
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Citra Asli')

plt.subplot(1, 3, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('Citra dengan Noise Uniform')

plt.subplot(1, 3, 3)
plt.imshow(restored_image, cmap='gray')
plt.title('Citra yang Direstorasi')

plt.show()
