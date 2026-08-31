import numpy as np

#soal 16
produk = np.array(["Kaos", "Celana", "Topi", "Sepatu", "Jaket", "Kaos Kaki"])
harga = np.array([80000, 150000, 50000, 300000, 250000, 20000])
terjual = np.array([120, 45, 200, 30, 60, 500])
kategori = np.array(["Atasan", "Bawahan", "Aksesoris", "Sepatu", "Atasan", "Aksesoris"])

pendapatan = harga * terjual
print(pendapatan)
target = np.isin(kategori, ["Atasan", "Aksesoris"])
produk_terpilih = produk[target]
print("Produk terpilih:", produk_terpilih)
diatas_rata2 = pendapatan > pendapatan.mean()
print("Produk diatas rata2:", produk[diatas_rata2])

#soal 17
nilai = np.array([
    [70, 65, 80],
    [55, 90, 75],
    [88, 92, 95],
    [45, 50, 40],
    [65, 60, 70],
    [90, 40, 85]
])
lulus_semua_mapel = np.all(nilai >= 60, axis = 1)
print(lulus_semua_mapel)
print(nilai[lulus_semua_mapel])

#soal 18
nama = np.array(["Andi", "Budi", "Citra", "Dedi", "Eka", "Fani", "Gita"])
gaji = np.array([5000000, 8000000, 6500000, 12000000, 4500000, 9000000, 7000000])
departemen = np.array(["IT", "Sales", "IT", "Manajemen", "HR", "Sales", "IT"])
tahun_gabung = np.array([2020, 2018, 2021, 2015, 2022, 2019, 2017])

#karyawan IT dengan gaji diatara rata2 gaji IT
it = np.isin(departemen, ["IT"])
karyawan_it = nama[it] #nama karyawan it
it_diatas_rata2 = gaji[it] > gaji[it].mean() 
print(karyawan_it[it_diatas_rata2]) #nama karyawan dengann gaji diatas rata2

#karyawan yang sudah 5 tahun dan gajinya < 8 juta
lama_kerja = 2026 - tahun_gabung
mask_kandidat = (lama_kerja > 5) & (gaji < 8000000)
print("Kandidat kenaikan gaji:", nama[mask_kandidat])

#urutan nama dengan gaji tertinggi ke terendah
idx_urutan = np.argsort(gaji)[::-1] #balik jadi terbesar ke terkecil
print("Ranking gaji (tertinggi dulu):", nama[idx_urutan])
print("Gajinya:", gaji[idx_urutan])