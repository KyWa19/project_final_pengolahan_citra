from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def gray_to_mbit(gray_image, m):
    # Mendapatkan nilai maksimum yang mungkin dari m-bit
    max_value = 2**m - 1
    # Mendapatkan array numpy dari citra grayscale
    gray_array = np.array(gray_image)
    # Melakukan quantisasi ke m-bit
    quantized_array = (gray_array * max_value // 255) * (255 // max_value)
    # Konversi kembali ke citra PIL
    mbit_image = Image.fromarray(quantized_array.astype('uint8'), 'L')
    return mbit_image
def display_image_and_histogram(image_path, m):
    # Baca citra grayscale menggunakan Pillow
    gray_image = Image.open(image_path).convert('L')
    # Konversi citra grayscale ke m-bit
    mbit_image = gray_to_mbit(gray_image, m)
    # Tampilkan citra m-bit
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(mbit_image, cmap='gray')
    plt.axis('off')
    plt.title(f'Citra {m}-Bit')
    # Hitung histogram citra m-bit
    histogram = mbit_image.histogram()
    # Plot histogram
    plt.subplot(1, 2, 2)
    plt.hist(histogram, bins=256, range=(0, 256), color='gray', alpha=0.7)
    plt.xlabel('Intensitas Pixel')
    plt.ylabel('Frekuensi')
    plt.title(f'Histogram Citra {m}-Bit')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
def main():
    # Lokasi citra grayscale yang ingin dibaca
    image_path = 'risky.jpg'
    # Jumlah bit untuk konversi ke m-bit (misalnya, m = 2, 4, 8, dll.)
    m = 4  # Contoh jumlah bit
    # Tampilkan citra m-bit dan histogram
    display_image_and_histogram(image_path, m)
if __name__ == "__main__":
    main()