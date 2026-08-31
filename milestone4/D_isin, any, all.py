import numpy as np

#np.isin() --> Cek Keanggotaan
kategori = np.array(["A", "B", "C", "D", "E"])
target = ["A", "C", "E"]
mask = np.isin(kategori, target)
print(mask)  # [ True False  True False  True]

#np.any() dan np.all() --> Cek Kondisi Keseluruhan
# np.any(kondisi) → True kalau ADA MINIMAL SATU elemen yang memenuhi kondisi
# np.all(kondisi) → True kalau SEMUA elemen memenuhi kondisi

nilai = np.array([70, 85, 45, 90])
print(np.any(nilai < 50))   # True -> ada minimal 1 yang < 50
print(np.all(nilai >= 60))  # False -> nggak semua >= 60

#soal 12
kota = np.array(["Jakarta", "Bandung", "Surabaya", "Medan", "Semarang"])
daftar = ["Jakarta", "Semarang", "Malang"]
cek = np.isin(kota, daftar)
print(cek)
print(kota[cek])

#soal 13
data = np.array([25, 30, np.nan, 40, np.nan, 55])
cek_nilai_hilang = np.any(np.isnan(data))
print(cek_nilai_hilang)

#soal 14
#hitung berapa banyak nilai yang hilang
banyak_nilai_hilang = np.isnan(data).sum()
print(banyak_nilai_hilang)
data_valid = data[~np.isnan(data)]
print("data bersih:", data_valid)

#soal 15
kelas_a = np.array([70, 80, 90, 65])
kelas_b = np.array([75, 60, 85, 95])

print(np.all(kelas_a >= 60))
print(np.any(kelas_b == 100))