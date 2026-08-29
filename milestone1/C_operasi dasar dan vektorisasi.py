import numpy as np

# #soal 11
# #hitung harga setelah diskon 15% untuk semua item tanpa loop
# harga = np.array([10000, 25000, 5000, 40000], dtype= np.float64)
# harga *= 0.85
# print(harga)

# #soal 12
# #hitung nilai akhir dengan bobot uts 40% dan uas 60% tanpa loop
# uts = np.array([80, 70, 90])
# uas = np.array([85, 75, 95])
# nilai_akhir = uts*0.40 + uas*0.60
# print(nilai_akhir)

#soal 13
#Buktikan kenapa vectorization NumPy lebih cepat dari loop Python biasa.
#Buat array besar (1 juta elemen), lalu bandingkan waktu kuadratkan semua 
#elemen pakai loop for vs operasi NumPy langsung (pakai modul time).

# import time
# n = 1_000_000
# data = list(range(n))
# data_np = np.arange(n)

# # Cara 1: Loop Python biasa
# start = time.time()
# hasil_loop = [x**2 for x in data]
# print("Loop:", time.time() - start, "detik")

# # Cara 2: Vectorization NumPy
# start = time.time()
# hasil_np = data_np ** 2
# print("NumPy:", time.time() - start, "detik")

#soal 14
suhu_celcius = np.array([0, 20, 37, 100])
F = suhu_celcius * 9/5 + 32
print(F)

#soal 15
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
#Hitung: penjumlahan, pengurangan, perkalian elemen-per-elemen, 
#dan pembagian — semuanya elementwise (bukan operasi matriks).
print(a + b)  # [5 7 9]
print(a - b)  # [-3 -3 -3]
print(a * b)  # [ 4 10 18]
print(a / b)  # [0.25 0.4  0.5 ]