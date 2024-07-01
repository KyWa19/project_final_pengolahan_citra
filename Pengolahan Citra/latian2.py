import cv2
import numpy as np;

# Membaca foto
foto_asli = cv2.imread('w.jpg')

# Menambahkan pencahayaan
brightness_factor = 50  # Ubah nilai ini sesuai kebutuhan Anda
citra_brightened = cv2.add(foto_asli, np.array([brightness_factor]))

# Menampilkan citra asli dan citra brightened
cv2.imshow('Citra Asli', foto_asli)
cv2.imshow('Citra Brightened', citra_brightened)
cv2.waitKey(0)
cv2.destroyAllWindows()