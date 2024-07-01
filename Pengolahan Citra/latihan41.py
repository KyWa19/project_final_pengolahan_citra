from PIL import Image
import matplotlib.pyplot as plt

def gray_to_binary(gray_image, threshold):
    # Konversi citra grayscale ke citra biner menggunakan thresholding
    binary_image = gray_image.point(lambda x: 0 if x < threshold else 255, 'L')
    return binary_image

def display_image_and_histogram(image_path, threshold):
    # Baca citra grayscale menggunakan Pillow
    gray_image = Image.open(image_path).convert('L')

    # Konversi citra grayscale ke citra biner
    binary_image = gray_to_binary(gray_image, threshold)

    # Tampilkan citra biner
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(binary_image, cmap='gray',vmin=0,vmax=255)
    plt.axis('off')
    plt.title('Citra Biner')

    # Hitung histogram citra biner
    histogram = binary_image.histogram()

    # Plot histogram
    plt.subplot(1, 2, 2)
    plt.hist(histogram, bins=256, range=(0, 256), color='gray', alpha=0.7)
    plt.xlabel('Intensitas Pixel')
    plt.ylabel('Frekuensi')
    plt.title('Histogram Citra Biner')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    # Lokasi citra grayscale yang ingin dibaca
    image_path = 'risky.jpg'
    # Threshold untuk konversi ke citra biner (sesuaikan sesuai kebutuhan)
    threshold = 128  # Contoh nilai threshold

    # Tampilkan citra biner dan histogram
    display_image_and_histogram(image_path, threshold)

if __name__ == "__main__":
    main()