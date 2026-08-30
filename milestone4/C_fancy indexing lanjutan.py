import numpy as np

#soal 9
nilai = np.array([72, 88, 65, 95, 58, 81, 90])
urutan_nilai = np.argsort(nilai) #index terkecil ke terbesar
print(urutan_nilai)
tiga_nilai_tertinggi = urutan_nilai[-3:] #3 indeks terakhir/3 nilai terbesar
print(nilai[tiga_nilai_tertinggi])

#soal 10
matriks = np.array([[10,20,30],[40,50,60],[70,80,90]])
baris = np.array([0, 1, 2])
kolom = np.array([0, 1, 2])
print(matriks[baris, kolom])

#soal 11
siswa = np.array(["Ana", "Budi", "Citra", "Dedi", "Eka"])
nilai2 = np.array([75, 92, 60, 88, 55])
idx_urut_nilai = np.argsort(nilai2)
print(siswa[idx_urut_nilai[-3:]])