import matplotlib.pyplot as plt
# Mengimport library matplotlib.pyplot untuk membuat plot gambar.

#%matplotlib inline
# Komentar: Komentar ini mungkin seharusnya digunakan di lingkungan notebook untuk menampilkan plot secara langsung.

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np

import cv2
# Mengimport beberapa modul yang akan digunakan dalam kode. Modul skimage digunakan untuk memanipulasi gambar, sedangkan numpy dan cv2 digunakan untuk operasi pengolahan citra.

citra1 = cv2.imread("riram.jpg", cv2.IMREAD_GRAYSCALE)
# Membaca gambar dengan nama file "riram.jpg" dan mengubahnya menjadi citra grayscale.

print(citra1.shape)
# Menampilkan dimensi citra dalam bentuk (tinggi, lebar).

plt.imshow(citra1, cmap='gray')
# Menampilkan citra grayscale menggunakan imshow dengan colormap 'gray'.

kernel = np.array([[-1, 0, -1],
                   [0, 4, 0],
                   [-1, 0, -1]])
# Membuat kernel dengan matriks tertentu yang akan digunakan dalam operasi konvolusi.

citraOutput = cv2.filter2D(citra1, -1, kernel)
# Melakukan operasi konvolusi pada citra citra1 menggunakan kernel yang telah dibuat sebelumnya, dan hasilnya disimpan dalam variabel citraOutput.

fig, axes = plt.subplots(1, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')
ax[0].set_title("Citra Input")
ax[1].imshow(citraOutput, cmap='gray')
ax[1].set_title("Citra Output")

fig.tight_layout()
# Mengatur tata letak plot agar lebih rapi.

plt.show()
# Menampilkan plot ke layar.
