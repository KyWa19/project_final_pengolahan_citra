from PIL import Image
import matplotlib.pyplot as plt
import cv2

def rgb_to_gray(rgb_image):
    # Konversi citra RGB ke grayscale
    gray_image = rgb_image.convert('L')
    return gray_image

def display_image_and_histogram(image_path):
    # Baca citra menggunakan Pillow
    rgb_image = Image.open(image_path)

    # Konversi RGB ke grayscale
    gray_image = rgb_to_gray(rgb_image)

    # Tampilkan citra
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.axis('off')
    plt.title('Citra Grayscale')

    # Hitung histogram citra grayscale
    histogram = gray_image.histogram()

    # Plot histogram
    plt.subplot(1, 2, 2)
    plt.hist(histogram, bins=256, range=(0, 256), color='gray', alpha=0.7)
    plt.xlabel('Intensitas Pixel')
    plt.ylabel('Frekuensi')
    plt.title('Histogram Citra Grayscale')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    # Lokasi citra yang ingin dibaca
    image_path = 'risky.jpg'

    # Tampilkan citra dan histogram
    display_image_and_histogram(image_path)

if __name__ == "__main__":
    main()