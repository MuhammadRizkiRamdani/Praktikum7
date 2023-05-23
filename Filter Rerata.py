import cv2                          # Mengimpor modul cv2 dari OpenCV untuk pemrosesan citra
import numpy as np
from skimage import data, io       # Mengimpor modul data dan io dari skimage untuk pemrosesan citra
import matplotlib.pyplot as plt    # Mengimpor modul pyplot dari matplotlib untuk membuat plot

img1 = cv2.imread("riram.jpg", cv2.IMREAD_GRAYSCALE)    # Membaca citra "riram.jpg" dalam mode grayscale
img2 = cv2.imread("uin.png", cv2.IMREAD_GRAYSCALE)      # Membaca citra "uin.png" dalam mode grayscale

print('Shape citra 1 : ', img1.shape)    # Menampilkan bentuk (shape) dari citra 1
print('Shape citra 2 : ', img2.shape)    # Menampilkan bentuk (shape) dari citra 2

fig, axes = plt.subplots(1, 2, figsize=(10, 10))    # Membuat subplots dengan 1 baris dan 2 kolom
ax = axes.ravel()                                   # Mengubah array axes menjadi satu dimensi

ax[0].imshow(img1, cmap='gray')     # Menampilkan citra 1 dengan colormap gray pada subplot pertama
ax[0].set_title("Citra 1")           # Menetapkan judul pada subplot pertama
ax[1].imshow(img2, cmap='gray')     # Menampilkan citra 2 dengan colormap gray pada subplot kedua
ax[1].set_title("Citra 2")           # Menetapkan judul pada subplot kedua

copy_img1 = img1.copy().astype(float)    # Membuat salinan citra 1 dengan tipe data float
copy_img2 = img2.copy().astype(float)    # Membuat salinan citra 2 dengan tipe data float

m1, n1 = copy_img1.shape    # Mendapatkan dimensi citra 1
output1 = np.empty([m1, n1])    # Membuat array kosong dengan dimensi yang sama dengan citra 1

m2, n2 = copy_img2.shape    # Mendapatkan dimensi citra 2
output2 = np.empty([m2, n2])    # Membuat array kosong dengan dimensi yang sama dengan citra 2

print('Shape copy citra 1 : ', copy_img1.shape)    # Menampilkan bentuk (shape) dari salinan citra 1
print('Shape output citra 1 : ', output1.shape)    # Menampilkan bentuk (shape) dari output citra 1

print('m1 : ', m1)    # Menampilkan nilai m1
print('n1 : ', n1)    # Menampilkan nilai n1

print()

print('Shape copy citra 2 : ', copy_img2.shape)    # Menampilkan bentuk (shape) dari salinan citra 2
print('Shape output citra 2 : ', output2.shape)    # Menampilkan bentuk (shape) dari output citra 2

print('m2 : ', m2)    # Menampilkan nilai m2
print('n2 : ', n2)    # Menampilkan nilai n2

print()

# Proses filtering dengan metode rerata
for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        jumlah = copy_img1[a1-1, b1-1] + copy_img1[a1-1, b1] + copy_img1[a1-1, b1-1] + \
                 copy_img1[a1, b1-1] + copy_img1[a1, b1] + copy_img1[a1, b1+1] + \
                 copy_img1[a1+1, b1-1] + copy_img1[a1+1, b1] + copy_img1[a1+1, b1+1]
        output1[a1, b1] = (1/9 * jumlah)

for baris1 in range(0, m2-1):
    for kolom1 in range(0, n2-1):
        a1 = baris1
        b1 = kolom1
        jumlah = copy_img2[a1-1, b1-1] + copy_img2[a1-1, b1] + copy_img2[a1-1, b1-1] + \
                 copy_img2[a1, b1-1] + copy_img2[a1, b1] + copy_img2[a1, b1+1] + \
                 copy_img2[a1+1, b1-1] + copy_img2[a1+1, b1] + copy_img2[a1+1, b1+1]
        output2[a1, b1] = (1/9 * jumlah)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))    # Membuat subplots dengan 2 baris dan 2 kolom
ax = axes.ravel()                                   # Mengubah array axes menjadi satu dimensi

ax[0].imshow(img1, cmap='gray')    # Menampilkan citra 1 pada subplot pertama
ax[0].set_title("Input Citra 1")    # Menetapkan judul pada subplot pertama

ax[1].imshow(img2, cmap='gray')    # Menampilkan citra 2 pada subplot kedua
ax[1].set_title("Input Citra 2")    # Menetapkan judul pada subplot kedua

ax[2].imshow(output1, cmap='gray')    # Menampilkan output citra 1 pada subplot ketiga
ax[2].set_title("Output Citra 1")    # Menetapkan judul pada subplot ketiga

ax[3].imshow(output2, cmap='gray')    # Menampilkan output citra 2 pada subplot keempat
ax[3].set_title("Output Citra 2")    # Menetapkan judul pada subplot keempat

fig.tight_layout()    # Menyesuaikan tata letak subplot
plt.show()    # Menampilkan plot