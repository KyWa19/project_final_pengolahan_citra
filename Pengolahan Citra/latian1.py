import cv2
import numpy as np

# Membaca foto
foto_asli = cv2.imread('ky2.jpg')

# Membuat citra negatif
citra_negatif = 255 - foto_asli

# Menampilkan citra asli dan citra negatif
cv2.imshow('Citra Asli', foto_asli)
cv2.imshow('Citra Negatif', citra_negatif)
cv2.waitKey(0)
cv2.destroyAllWindows()