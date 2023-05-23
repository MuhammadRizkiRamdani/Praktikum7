import cv2                      # Mengimpor modul cv2 dari OpenCV untuk pemrosesan citra
import numpy as np              # Mengimpor modul numpy untuk operasi numerik
from skimage import data        # Mengimpor modul data dari skimage untuk citra contoh
import matplotlib.pyplot as plt  # Mengimpor modul pyplot dari matplotlib untuk visualisasi
#%matplotlib inline               # Komentar ini mungkin merujuk pada pengaturan output plot dalam lingkungan spesifik

img = cv2.imread("riram.jpg", cv2.IMREAD_GRAYSCALE)  # Membaca citra "riram.jpg" dalam mode grayscale

row, column = img.shape  # Mendapatkan dimensi citra

img1 = np.zeros((row, column), dtype='uint8')  # Membuat array kosong dengan dimensi yang sama dengan citra

min_range = 10  # Menetapkan nilai batas bawah
max_range = 60  # Menetapkan nilai batas atas

# Looping untuk mengubah piksel menjadi 255 atau 0 berdasarkan batas rentang
for i in range(row):
    for j in range(column):
        if img[i, j] > min_range and img[i, j] < max_range:
            img1[i, j] = 255
        else:
            img1[i, j] = 0

fig, axes = plt.subplots(2, 2, figsize=(12, 12))  # Membuat subplot dengan 2 baris dan 2 kolom
ax = axes.ravel()  # Mengubah array subplot menjadi 1 dimensi

ax[0].imshow(img, cmap=plt.cm.gray)  # Menampilkan citra asli pada subplot pertama
ax[0].set_title("Citra Input")  # Memberikan judul pada subplot pertama
ax[1].hist(img.ravel(), bins=256)  # Menampilkan histogram citra asli pada subplot kedua
ax[1].set_title('Histogram Input')  # Memberikan judul pada subplot kedua

ax[2].imshow(img1, cmap=plt.cm.gray)  # Menampilkan citra hasil pada subplot ketiga
ax[2].set_title("Citra Output")  # Memberikan judul pada subplot ketiga
ax[3].hist(img1.ravel(), bins=256)  # Menampilkan histogram citra hasil pada subplot keempat
ax[3].set_title('Histogram Output')  # Memberikan judul pada subplot keempat

fig.tight_layout()  # Menyesuaikan tata letak subplot agar rapi
plt.show()  # Menampilkan plot