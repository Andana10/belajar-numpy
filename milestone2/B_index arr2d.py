import numpy as np

#soal 6
matriks = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matriks[1, 2]) #ambil baris 1 kolom 2

#soal 7
print(matriks[0]) #mengamil baris pertama
print(matriks[:, 0]) #mengambil kolom pertama

#soal 8
#ambil sub-matriks 2x2 di pojok kiri atas (baris 0-1, kolom 0-1)
print(matriks[0:2, 0:2]) 

#soal 9
print(matriks[-1]) #ambil baris terakhir
print(matriks[:, -1]) #ambil kolom terakhir

#soal 10
#(Matematika, Fisika, Kimia, Biologi):
nilai_siswa = np.array([
    [80, 75, 90, 85],
    [70, 65, 80, 75],
    [95, 90, 85, 92],
    [60, 55, 70, 65],
    [88, 92, 78, 84]
])
#Ambil semua nilai Fisika (kolom index 1) untuk semua siswa, 
#lalu ambil semua nilai siswa ke-3 (index 2) untuk semua mata pelajaran.

fisika = nilai_siswa[:, 1]
semua_mapel = nilai_siswa[2]
print(fisika)
print(semua_mapel)