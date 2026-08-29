import numpy as np

#soal 13
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
gabung = np.concatenate([a, b])#menggabungkan array
print(gabung)

#soal 14
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
gabung_vertikal = np.vstack([A, B])
gabung_horizontal = np.hstack([A, B])
print(gabung_vertikal)
print(gabung_horizontal)

#soal 15
jan = np.array([100, 150, 200])
feb = np.array([120, 140, 210])
gabung2 = np.vstack([jan, feb]) #(2, 3) 
print(gabung2)

#soal 16
arr =np.arange(1, 13)
pecah = np.split(arr, 3) #pecah menjadi 3 bagian sama besar
print(pecah)

#soal 17
matriks = np.arange(1, 17).reshape(4, 4)

matriks = np.arange(1, 17).reshape(4, 4)

atas, bawah = np.vsplit(matriks, 2) #pecah menjadi 2 bagian horizontal
print("Atas:\n", atas)
print("Bawah:\n", bawah)

kiri, kanan = np.hsplit(matriks, 2) #pecah menjadi 2 bagian vertikal
print("Kiri:\n", kiri)
print("Kanan:\n", kanan)