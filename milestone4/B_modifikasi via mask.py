import numpy as np

# Selain buat "mengintip" data, mask juga bisa dipakai di sisi kiri (=) untuk mengubah nilai yang memenuhi kondisi tertentu — ini disebut conditional assignment.

# nilai = np.array([65, 45, 80, 90, 55])
# nilai[nilai < 60] = 0   # semua yang < 60 diganti jadi 0
# print(nilai)  # [65  0 80 90  0]

# Ini beda dengan np.where() yang kamu pelajari di Milestone 2 — np.where() menghasilkan array BARU, sementara conditional assignment langsung mengubah array aslinya (in-place).

# Kapan pakai yang mana?
# Pakai conditional assignment (arr[mask] = nilai) kalau kamu memang mau array aslinya berubah permanen.
# Pakai np.where() kalau kamu mau array baru tanpa mengubah yang asli (lebih aman untuk debugging).


#soal 6
stok = np.array([50, 0, 30, 0, 15, 0, 8], dtype = float) #angka 0 data hilang/error, harus float supaya bisa nan
stok[stok == 0] = np.nan #menandai data hilang
print(stok)

#soal 7
harga = np.array([15000, -5000, 22000, -1000, 30000])
harga[harga < 0] = 0
print(harga)

#soal 8
nilai = np.array([55, 70, 88, 45, 92, 60, 78])
nilai[nilai < 60] = 0 
nilai[nilai >= 60] += 5
print(nilai)