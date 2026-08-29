import numpy as np

#soal 16
nilai_kelas = np.array([[80, 75, 90],
    [70, 85, 88],
    [95, 60, 77],
    [82, 91, 73]])

print(nilai_kelas.shape)
print(nilai_kelas.mean()) #mengitung rata rata nilai 

#soal 17
rata_per_siswa = nilai_kelas.mean(axis = 1) #hasil per baris
rata_per_mapel = nilai_kelas.mean(axis = 0) #hasil per kolom
print("Rata-rata per siswa:", rata_per_siswa)
print("Rata-rata per mapel:", rata_per_mapel)

#soal 18, Buat array 2D ukuran 5x5 isinya angka 1-25 berurutan
arr2d = np.arange(1, 26).reshape(5, 5)
print(arr2d)

#soal 19
print(arr2d.max())
print(arr2d.min())
print(arr2d.sum())

#soal 20
np.random.seed(42)  # biar hasilnya konsisten tiap dijalankan
suhu_mingguan = np.random.randint(20, 36, size=(3, 7))
kota = ["Jakarta", "Bandung", "Surabaya"]

rata_per_kota = suhu_mingguan.mean(axis=1)
print("Rata-rata suhu per kota:", rata_per_kota)

idx_tertinggi = rata_per_kota.argmax()
print(f"Kota dengan rata-rata suhu tertinggi: {kota[idx_tertinggi]}")
