import matplotlib.pyplot as plt    # Mengimport modul matplotlib untuk membuat plot
import cv2    # Mengimport modul cv2 (OpenCV) untuk membaca citra
#%matplotlib inline

from skimage import data    # Mengimport submodul data dari skimage untuk mengakses dataset citra
from skimage.io import imread    # Mengimport fungsi imread dari submodul io skimage untuk membaca citra
from skimage.color import rgb2gray    # Mengimport fungsi rgb2gray dari submodul color skimage untuk mengubah citra ke skala abu-abu
import numpy as np    # Mengimport modul numpy untuk manipulasi array

citra1 = cv2.imread("riram.jpg", cv2.IMREAD_GRAYSCALE)    # Membaca citra 1 dalam mode skala abu-abu menggunakan cv2
citra2 = cv2.imread("uin.png", cv2.IMREAD_GRAYSCALE)    # Membaca citra 2 dalam mode skala abu-abu menggunakan cv2

print('Shape citra 1 : ', citra1.shape)    # Menampilkan dimensi citra 1
print('Shape citra 1 : ', citra2.shape)    # Menampilkan dimensi citra 2

fig, axes = plt.subplots(1, 2, figsize=(10, 10))    # Membuat subplots dengan 1 baris dan 2 kolom
ax = axes.ravel()    # Mengubah array axes menjadi satu dimensi

ax[0].imshow(citra1, cmap='gray')    # Menampilkan citra 1 pada subplot pertama
ax[0].set_title("Citra 1")    # Menetapkan judul pada subplot pertama

ax[1].imshow(citra2, cmap='gray')    # Menampilkan citra 2 pada subplot kedua
ax[1].set_title("Citra 2")    # Menetapkan judul pada subplot kedua

# Algoritma pemrosesan dengan filter median

copyCitra1 = citra1.copy()    # Mengcopy citra 1 untuk pemrosesan
copyCitra2 = citra2.copy()    # Mengcopy citra 2 untuk pemrosesan

m1, n1 = copyCitra1.shape    # Mengambil dimensi citra 1
output1 = np.empty([m1, n1])    # Membuat array kosong dengan dimensi citra 1

m2, n2 = copyCitra2.shape    # Mengambil dimensi citra 2
output2 = np.empty([m2, n2])    # Membuat array kosong dengan dimensi citra 2

print('Shape copy citra 1 : ', copyCitra1.shape)    # Menampilkan dimensi citra 1 yang sudah dicopy
print('Shape output citra 1 : ', output1.shape)    # Menampilkan dimensi output citra 1

print('m1 : ', m1)    # Menampilkan nilai m1
print('n1 : ', n1)    # Menampilkan nilai n1

print()

print('Shape copy citra 2 : ', copyCitra2.shape)    # Menampilkan dimensi citra 2 yang sudah dicopy
print('Shape output citra 3 : ', output2.shape)    # Menampilkan dimensi output citra 2

print('m2 : ', m2)    # Menampilkan nilai m2
print('n2 : ', n2)    # Menampilkan nilai n2

print()

for baris in range(0, m1 - 1):    # Looping untuk setiap baris dalam citra 1
    for kolom in range(0, n1 - 1):    # Looping untuk setiap kolom dalam citra 1

        a1 = baris    # Menetapkan nilai a1 sebagai baris saat ini
        b1 = kolom    # Menetapkan nilai b1 sebagai kolom saat ini

        arr = np.array([copyCitra1[a1 - 1, b1 - 1], copyCitra1[a1 - 1, b1], copyCitra1[a1, b1 + 1], \
                        copyCitra1[a1, b1 - 1], copyCitra1[a1, b1 + 1], copyCitra1[a1 + 1, b1 - 1], \
                        copyCitra1[a1 + 1, b1], copyCitra1[a1 + 1, b1 + 1]])    # Membuat array yang berisi nilai piksel tetangga

        minPiksel = np.amin(arr)    # Menentukan nilai piksel minimum
        maksPiksel = np.amax(arr)    # Menentukan nilai piksel maksimum

        if copyCitra1[baris, kolom] < minPiksel:    # Jika nilai piksel saat ini kurang dari nilai piksel minimum
            output1[baris, kolom] = minPiksel    # Set nilai output citra 1 sebagai nilai piksel minimum
        else:
            if copyCitra1[baris, kolom] > maksPiksel:    # Jika nilai piksel saat ini lebih dari nilai piksel maksimum
                output1[baris, kolom] = maksPiksel    # Set nilai output citra 1 sebagai nilai piksel maksimum
            else:
                output1[baris, kolom] = copyCitra1[baris, kolom]    # Set nilai output citra 1 sebagai nilai piksel saat ini

for baris1 in range(0, m2 - 1):    # Looping untuk setiap baris dalam citra 2
    for kolom1 in range(0, n2 - 1):    # Looping untuk setiap kolom dalam citra 2

        a1 = baris1    # Menetapkan nilai a1 sebagai baris saat ini
        b1 = kolom1    # Menetapkan nilai b1 sebagai kolom saat ini

        arr = np.array([copyCitra2[a1 - 1, b1 - 1], copyCitra2[a1 - 1, b1], copyCitra2[a1, b1 + 1], \
                        copyCitra2[a1, b1 - 1], copyCitra2[a1, b1 + 1], copyCitra2[a1 + 1, b1 - 1], \
                        copyCitra2[a1 + 1, b1], copyCitra2[a1 + 1, b1 + 1]])    # Membuat array yang berisi nilai piksel tetangga

        minPiksel = np.amin(arr)    # Menentukan nilai piksel minimum
        maksPiksel = np.amax(arr)    # Menentukan nilai piksel maksimum

        if copyCitra2[baris1, kolom1] < minPiksel:    # Jika nilai piksel saat ini kurang dari nilai piksel minimum
            output2[baris1, kolom1] = minPiksel    # Set nilai output citra 2 sebagai nilai piksel minimum
        else:
            if copyCitra2[baris1, kolom1] > maksPiksel:    # Jika nilai piksel saat ini lebih dari nilai piksel maksimum
                output2[baris1, kolom1] = maksPiksel    # Set nilai output citra 2 sebagai nilai piksel maksimum
            else:
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]    # Set nilai output citra 2 sebagai nilai piksel saat ini

fig, axes = plt.subplots(2, 2, figsize=(10, 10))    # Membuat subplots dengan 2 baris dan 2 kolom
ax = axes.ravel()    # Mengubah array axes menjadi satu dimensi

ax[0].imshow(citra1, cmap='gray')    # Menampilkan citra 1 pada subplot pertama
ax[0].set_title("Input Citra 1")    # Menetapkan judul pada subplot pertama

ax[1].imshow(citra2, cmap='gray')    # Menampilkan citra 2 pada subplot kedua
ax[1].set_title("Input Citra 2")    # Menetapkan judul pada subplot kedua

ax[2].imshow(output1, cmap='gray')    # Menampilkan output citra 1 pada subplot ketiga
ax[2].set_title("Output Citra 1")    # Menetapkan judul pada subplot ketiga

ax[3].imshow(output2, cmap='gray')    # Menampilkan output citra 2 pada subplot keempat
ax[3].set_title("Output Citra 2")    # Menetapkan judul pada subplot keempat

fig.tight_layout()    # Mengatur tata letak subplot agar rapi
plt.show()    # Menampilkan plot
